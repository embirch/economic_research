#!/usr/bin/env python3
"""Build a post's page from its research folder.

    python3 site/tools/build_page.py <post>            # e.g. post1

Reads `posts/<post>/POST.md` and turns it into `site/posts/<post>/index.html`:

  * figures are inserted where their captions appear — a paragraph beginning
    `**Figure N.` is wrapped in <figure>, and the image file is resolved from
    `posts/<post>/outputs/figures.json`, never hard-coded here;
  * each section's evidence is wrapped in a collapsible drawer keyed to the
    section heading: every numbered script that produced a number cited in that
    section, in full with syntax highlighting, the check output it printed when
    it ran, and a table of the `results.json` entries the section cites. Which
    entries a section cites comes from `posts/<post>/notes/claims-map.json`, so
    the builder is keyed to results.json and the claims map, not to per-post
    wiring;
  * Methodology additionally carries the pre-registration, the lab notebook and
    the red-team memo;
  * a contents rail is generated from the H2 headings.

Nothing on the page is typed by hand. The scripts are shown as the analyst wrote
them and are never edited. Run `verify_page.py` after this; the page is not
publishable until it passes.
"""
import os, re, sys, json, html, shutil
import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def repo(*p):
    return os.path.join(ROOT, *p)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def esc(s):
    return html.escape(s)


def md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", html.unescape(re.sub(r"<[^>]+>", "", text)).lower()).strip("-")


# ---------------------------------------------------------------- results.json

PART = re.compile(r'''"([^"]+)"((?:\[\d+\])*)|([^.\[\]]+)((?:\[\d+\])*)''')


def resolve(obj, path):
    """Dotted path into results.json.

    `tests.D_aug2025.estimates.D.coef`, `facts.kish_aug2025.by_quartile[3]`, and
    `facts.q.boundary_tie_mass."b3_43.40".tasks` for a key containing a dot.
    """
    cur = obj
    for m in PART.finditer(path):
        key = m.group(1) if m.group(1) is not None else m.group(3)
        idxs = m.group(2) if m.group(1) is not None else m.group(4)
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(path)
        cur = cur[key]
        for i in re.findall(r"\[(\d+)\]", idxs or ""):
            cur = cur[int(i)]
    return cur


def fmt(v):
    if isinstance(v, float):
        return f"{v:.4f}" if abs(v) < 1e4 else f"{v:.4g}"
    if isinstance(v, list):
        return ", ".join(fmt(x) for x in v)
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def entry_rows(results, key):
    """One or more table rows describing a results.json entry."""
    rows = []
    node = resolve(results, key)
    if isinstance(node, dict) and "estimates" in node:
        for name, est in node["estimates"].items():
            if not isinstance(est, dict) or "coef" not in est:
                continue
            ci = est.get("ci")
            rows.append([
                key, name, fmt(est["coef"]),
                f"[{fmt(ci[0])}, {fmt(ci[1])}]" if ci else "—",
                fmt(est["se"]) if est.get("se") is not None else "—",
                fmt(est["mde"]) if est.get("mde") is not None else "—",
                est.get("unit", ""),
            ])
        if not rows:
            rows.append([key, "—", "—", "—", "—", "—", node.get("label", "")])
    elif isinstance(node, dict) and "value" in node:
        rows.append([key, "value", fmt(node["value"]), "—", "—", "—", node.get("label", "")])
    else:
        rows.append([key, "—", fmt(node), "—", "—", "—", ""])
    return rows


def table(rows, caption):
    head = ["results.json entry", "quantity", "estimate", "95% interval", "SE", "MDE", "unit / label"]
    body = "".join(
        "<tr>" + "".join(f"<td>{esc(str(c))}</td>" for c in r) + "</tr>" for r in rows
    )
    return (
        f'<details class="tab"><summary>Table · {esc(caption)}</summary>'
        f'<table><thead><tr>' + "".join(f"<th>{esc(h)}</th>" for h in head) + "</tr></thead>"
        f"<tbody>{body}</tbody></table></details>"
    )


# ---------------------------------------------------------------- drawer parts

def script_block(post_dir, rel):
    path = os.path.join(post_dir, rel)
    if not os.path.exists(path):
        return ""
    return (
        f'<details class="code"><summary>Script · <code>{esc(rel)}</code> '
        f"(as the analyst wrote it)</summary>"
        f'<pre><code class="language-python">{esc(read(path))}</code></pre></details>'
    )


def check_block(post_dir, rel):
    stem = os.path.basename(rel)[:2]
    outs = sorted(
        f for f in os.listdir(os.path.join(post_dir, "outputs", "checks"))
        if f.startswith(stem + "_")
    ) if os.path.isdir(os.path.join(post_dir, "outputs", "checks")) else []
    parts = []
    for f in outs:
        parts.append(
            f'<details class="out"><summary>Check block · what <code>{esc(os.path.basename(rel))}</code> '
            f"printed when it ran</summary>"
            f'<pre>{esc(read(os.path.join(post_dir, "outputs", "checks", f)))}</pre></details>'
        )
    return "".join(parts)


def drawer(title, inner, cls="evidence"):
    return (
        f'<details class="{cls}"><summary>{esc(title)}</summary>'
        f'<div class="inner">{inner}</div></details>'
    )


def demote(html_text, by=3):
    """Headings inside an embedded document must not compete with the post's."""
    for n in (4, 3, 2, 1):
        html_text = re.sub(rf"<(/?)h{n}>", lambda m, n=n: f"<{m.group(1)}h{min(6, n + by)}>", html_text)
    return html_text


def main(post):
    post_dir = repo("posts", post)
    site_dir = repo("site", "posts", post)
    os.makedirs(os.path.join(site_dir, "figures"), exist_ok=True)

    results = json.loads(read(os.path.join(post_dir, "data", "processed", "results.json")))
    figures = json.loads(read(os.path.join(post_dir, "outputs", "figures.json")))
    claims_map = json.loads(read(os.path.join(post_dir, "notes", "claims-map.json")))

    for fig in figures.values():
        src = os.path.join(post_dir, fig["file"])
        shutil.copy(src, os.path.join(site_dir, "figures", os.path.basename(src)))

    # figure number -> basename, from figures.json
    fig_file = {}
    for name, fig in figures.items():
        n = re.sub(r"\D", "", name)
        fig_file[n] = os.path.basename(fig["file"])

    post_md = read(os.path.join(post_dir, "POST.md"))
    title = post_md.splitlines()[0].lstrip("# ").strip()

    # --- figures inserted where their captions appear -----------------------
    def figurise(m):
        n, caption = m.group(1), m.group(0)
        f = fig_file.get(n)
        if not f:
            return caption
        return (
            f'<figure><img src="figures/{f}" alt="Figure {n}">'
            f"<figcaption>{md(caption).strip()}</figcaption></figure>"
        )

    post_md = re.sub(r"^\*\*Figure (\d+)\..*$", figurise, post_md, flags=re.M)
    body = md(post_md)

    # --- evidence, by section, from the claims map --------------------------
    sections = {}
    for c in claims_map["claims"]:
        sections.setdefault(c["section"], {"keys": [], "scripts": []})
        for b in c["bindings"]:
            key = b["key"]
            top = ".".join(key.split(".")[:2]).split("[")[0]
            if top not in sections[c["section"]]["keys"]:
                sections[c["section"]]["keys"].append(top)
    for sec, d in sections.items():
        for key in d["keys"]:
            try:
                node = resolve(results, key)
            except (KeyError, IndexError, TypeError):
                continue
            s = node.get("script") if isinstance(node, dict) else None
            for one in re.split(r"\s+and\s+|,\s*", s or ""):
                one = one.strip()
                if one.endswith(".py") and one not in d["scripts"]:
                    d["scripts"].append(one)
        d["scripts"].sort()

    evidence = {}
    for sec, d in sections.items():
        rows = []
        for key in d["keys"]:
            try:
                rows += entry_rows(results, key)
            except (KeyError, IndexError, TypeError):
                pass
        inner = table(rows, f"every results.json entry this section cites ({len(d['keys'])} entries)")
        for sc in d["scripts"]:
            inner += script_block(post_dir, sc) + check_block(post_dir, sc)
        evidence[sec] = drawer(
            "Evidence: the scripts that produced these numbers, what they printed, and the table", inner
        )

    method_extra = ""
    for label, rel in [
        ("Pre-registration, committed before any primary test", os.path.join("prereg", "prereg.md")),
        ("Lab notebook: every step, deviation and correction, dated", os.path.join("notes", "lab-notebook.md")),
        ("Red-team memo: the strongest case against each finding", os.path.join("notes", "red-team.md")),
    ]:
        path = os.path.join(post_dir, rel)
        if os.path.exists(path):
            method_extra += drawer(label, demote(md(read(path))), cls="evidence doc")

    # --- splice drawers in after each H2, build the contents rail -----------
    out, toc = [], []
    for line in body.split("\n"):
        m = re.match(r"<h2>(.*?)</h2>", line)
        if m:
            text = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
            slug = slugify(text)
            toc.append((slug, text))
            out.append(f'<h2 id="{slug}">{m.group(1)}</h2>')
            if text in evidence:
                out.append(evidence[text])
            if text.startswith("Methodology"):
                out.append(method_extra)
            continue
        out.append(line)
    body = "\n".join(out)

    rail = (
        '<nav class="toc"><div class="tl">Contents</div>'
        + "".join(f'<a href="#{s}">{esc(t)}</a>' for s, t in toc)
        + "</nav>"
    )

    page = PAGE.format(title=esc(title.split(":")[0]), rail=rail, body=body)
    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {os.path.join('site', 'posts', post, 'index.html')}  {len(page)} bytes  "
          f"{len(toc)} sections  {len(evidence)} evidence drawers")


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Emily Birch</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@500;600&family=IBM+Plex+Serif:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<style>
body{{margin:0;background:#edf1f4;color:#2a2a2a;font:16px/1.7 "IBM Plex Serif",Georgia,serif;-webkit-font-smoothing:antialiased}}
a{{color:#2a2a2a;text-underline-offset:3px;text-decoration-color:#999}}
.wrap{{max-width:1180px;margin:0 auto;padding:36px 24px 80px;display:grid;grid-template-columns:230px minmax(0,780px);gap:56px;align-items:start}}
@media(max-width:960px){{.wrap{{grid-template-columns:1fr}}.toc{{position:static}}}}
.toc{{position:sticky;top:28px;font:13.5px/1.5 "IBM Plex Sans",sans-serif;max-height:90vh;overflow:auto}}
.toc .tl{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#888;margin-bottom:10px}}
.toc a{{display:block;color:#444;text-decoration:none;padding:4px 0;border-left:2px solid #d7dde3;padding-left:10px}}
.toc a:hover{{color:#2f6f4f;border-color:#2f6f4f}}
.main{{min-width:0}}
.top{{font:13px "IBM Plex Sans",sans-serif;color:#666;margin-bottom:18px}} .top a{{text-decoration:none;color:#2a2a2a}}
h1,h2,h3,h4,summary{{font-family:"IBM Plex Sans","Helvetica Neue",sans-serif;font-weight:500;letter-spacing:0}}
h1{{font-size:30px;line-height:1.25;margin:0 0 10px}} h2{{font-size:22px;line-height:1.3;margin:38px 0 12px}} h3{{font-size:18px;margin:28px 0 8px}}
em{{color:#555}} p{{margin:0 0 14px}} li{{margin:0 0 8px}}
figure{{margin:18px 0;background:#fff;border:1px solid #d7dde3;padding:10px}} figure img{{width:100%;display:block}}
figcaption{{font:13px/1.55 "IBM Plex Sans",sans-serif;color:#666;margin-top:8px}} figcaption p{{margin:0}}
table{{border-collapse:collapse;font:13.5px/1.45 "IBM Plex Sans",sans-serif;background:#fff;margin:10px 0 16px;display:block;overflow-x:auto;max-width:100%}}
th,td{{border:1px solid #d7dde3;padding:6px 9px;text-align:left;vertical-align:top}} th{{background:#f3f5f7}}
details.evidence{{border:1px solid #c9d2da;background:#fff;border-radius:6px;margin:14px 0 24px}}
details.evidence>summary{{cursor:pointer;padding:10px 14px;font-size:14.5px;color:#2f6f4f;list-style:none}}
details.evidence>summary::before{{content:"\\25b8  "}} details.evidence[open]>summary::before{{content:"\\25be  "}}
details.evidence>.inner{{padding:4px 14px 12px;border-top:1px solid #e3e8ec;font-size:14.5px}}
details.code,details.out,details.tab,details.evidence details{{margin:8px 0}}
details.code>summary,details.out>summary,details.tab>summary,details.evidence details>summary{{cursor:pointer;font:13.5px "IBM Plex Sans",sans-serif;color:#2f6f4f}}
pre{{background:#f6f8fa;border:1px solid #e3e8ec;border-radius:6px;padding:12px;font-size:12px;line-height:1.5;overflow-x:auto;white-space:pre}}
code{{font-size:0.92em}}
blockquote{{margin:0 0 14px;padding-left:14px;border-left:3px solid #d7dde3;color:#555}}
</style>
</head>
<body>
<div class="wrap">
  {rail}
  <div class="main">
  <div class="top"><a href="../../index.html">&larr; Emily Birch</a> &nbsp;&middot;&nbsp; Self-directed research</div>
  {body}
  </div>
</div>
<script>hljs.highlightAll();</script>
</body>
</html>"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: build_page.py <post>   e.g. build_page.py post1")
    main(sys.argv[1])
