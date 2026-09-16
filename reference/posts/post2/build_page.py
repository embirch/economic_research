"""Builds the interactive post page from the research folder.
Output: site/posts/post1/index.html (+ figures copied alongside).  Run from research/post1:  ../.venv/bin/python build_page.py
The page is the write-up (POST.md) with evidence drawers generated from scripts/, outputs/, prereg/ and notes/.
Nothing on the page is typed by hand; if the research changes, rerun this and the page changes with it."""
import os, re, json, html, shutil, markdown, pandas as pd
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(ROOT, "..", "..", "site", "posts", "post2"))
os.makedirs(os.path.join(SITE, "figures"), exist_ok=True)
for f in os.listdir(os.path.join(ROOT, "outputs", "figures")):
    if f.startswith("fig"): shutil.copy(os.path.join(ROOT, "outputs", "figures", f), os.path.join(SITE, "figures", f))

def read(p): return open(os.path.join(ROOT, p)).read()
def md(p): return markdown.markdown(read(p), extensions=["tables", "fenced_code"])
def esc(s): return html.escape(s)
def code(path, lang="python"):
    return f'<details class="code"><summary>Script · <code>{esc(path)}</code></summary><pre><code class="language-{lang}">{esc(read(path))}</code></pre></details>'
def check(step):
    p = f"outputs/checks/{step}.txt"
    return f'<details class="out"><summary>Check block · what the script printed when it ran</summary><pre>{esc(read(p))}</pre></details>' if os.path.exists(os.path.join(ROOT, p)) else ""
def table_csv(path, caption, index_name=""):
    df = pd.read_csv(os.path.join(ROOT, path))
    if index_name: df = df.rename(columns={"Unnamed: 0": index_name, "geo_id": index_name})
    return f'<details class="tab"><summary>Table · {esc(caption)}</summary>{df.to_html(index=False, float_format=lambda x: f"{x:.3f}")}</details>'
def drawer(title, inner, open_=False):
    return f'<details class="evidence"{" open" if open_ else ""}><summary>{title}</summary><div class="inner">{inner}</div></details>'

# ---------- write-up with figures ----------
post = read("POST.md")
TITLE = post.splitlines()[0].lstrip("# ").split(":")[0].strip()
figs = {"Figure 1": "fig1_jobs_and_gini.png", "Figure 2": "fig2_who_and_what.png", "Figure 3": "fig3_catchup.png", "Figure 4": "fig4_providers.png", "Figure 5": "fig5_persistence.png", "Figure 6": "fig6_hobbyist.png", "Figure 7": "fig7_mechanisms.png"}
for k, f in figs.items():
    post = re.sub(rf"\*{k}\.([^*]*)\*", rf'<figure><img src="figures/{f}" alt="{k}"><figcaption>{k}.\1</figcaption></figure>', post)
body = markdown.markdown(post, extensions=["tables"])


# ---------- evidence drawers keyed to the new section headings ----------
ev = {
 "Are they real": drawer("Evidence: the persistence test", table_csv("data/processed/09_persistent.csv", "The 22 persistent outliers with their April and May distinctiveness") + code("scripts/09_outliers.py") + check("09")),
 "What jobs explain": drawer("Evidence: the replication, the decomposition and the three providers", code("scripts/02_replicate.py") + check("02") + code("scripts/03_stage1_selection.py") + check("03") + code("scripts/04_stage2_mix.py") + check("04") + code("scripts/05_place.py") + check("05") + code("scripts/07_providers.py") + check("07") + code("scripts/12_after_jobs.py") + check("12")),
 "The hobbyist signature": drawer("Evidence: the four leisure clusters against adoption", code("scripts/10_leisure.py") + check("10")),
 "The place in the request": drawer("Evidence: one mechanism per outlier, across all states", table_csv("data/processed/09_covariates_outliers.csv", "State covariates: industry shares, college enrolment, rural share, usage", "state") + code("scripts/11_mechanisms.py") + check("11")),
 "Methodology": drawer("Data loading and the merge audit", code("scripts/01_load_states.py") + check("01")) +
     drawer("Catch-up across waves (from the decomposition stage)", code("scripts/06_catchup.py") + check("06")) +
     drawer("Figures", code("scripts/08_figures.py") + check("08") + code("scripts/13_figures_outliers.py") + check("13")) +
     drawer("Lab notebook: every step and every deviation, dated", md("notes/lab-notebook.md")) +
     drawer("Anticipated objections, and what the post concedes", md("notes/red-team.md")) +
     drawer("Research brief: why this matters", md("BRIEF.md")) +
     drawer("Pre-registration: the outliers (committed before steps 09-12)", md("prereg/prereg-outliers.md")) +
     drawer("Pre-registration: the decomposition (committed before steps 04-07)", md("prereg/prereg.md")) +
     drawer("Plan and assumptions sweep", md("PLAN.md")) +
     drawer("Reproduce everything", '<p>Create a Python environment with pandas, numpy, statsmodels, scipy and matplotlib; link the four Economic Index releases into <code>data/raw/</code>; download the ACS 2023 summary tables, the Census rural-share file, Microsoft\'s state file and OpenAI\'s Signals CSV bundle as listed in the Methodology; then run:</p>' + code("scripts/run_all.sh", "bash") + '<p>Every script ends with a check block that stops on a wrong number.</p>'),
}
lines = body.split("\n"); out = []; pending = None; toc = []
for ln in lines:
    m = re.match(r'<h2>(.*?)</h2>', ln)
    if m:
        if pending: out.append(pending); pending = None
        title = re.sub(r'<[^>]+>', '', m.group(1)); slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        toc.append((slug, title)); ln = f'<h2 id="{slug}">{m.group(1)}</h2>'
        pending = next((v for k, v in ev.items() if title.startswith(k)), None)
        if title.startswith("Methodology"): out.append(ln); out.append(pending); pending = None; continue
    out.append(ln)
if pending: out.append(pending)
body = "\n".join(out)
tocnav = '<nav class="toc"><div class="tl">Contents</div>' + "".join(f'<a href="#{s_}">{t}</a>' for s_, t in toc) + '</nav>'

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} · Emily Birch</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@500;600&family=IBM+Plex+Serif:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<style>
body{{margin:0;background:#edf1f4;color:#2a2a2a;font:16px/1.7 "IBM Plex Serif",Georgia,serif;-webkit-font-smoothing:antialiased}}
a{{color:#2a2a2a;text-underline-offset:3px;text-decoration-color:#999}}
.wrap{{max-width:1180px;margin:0 auto;padding:36px 24px 80px;display:grid;grid-template-columns:230px minmax(0,780px);gap:56px;align-items:start}}
@media(max-width:960px){{.wrap{{grid-template-columns:1fr}}.toc{{position:static}}}}
.toc{{position:sticky;top:28px;font:13.5px/1.5 "IBM Plex Sans",sans-serif}} .toc .tl{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#888;margin-bottom:10px}} .toc a{{display:block;color:#444;text-decoration:none;padding:4px 0;border-left:2px solid #d7dde3;padding-left:10px}} .toc a:hover{{color:#2f6f4f;border-color:#2f6f4f}}
.main{{min-width:0}}
.top{{font:13px "IBM Plex Sans",sans-serif;color:#666;margin-bottom:18px}} .top a{{text-decoration:none;color:#2a2a2a}}
h1,h2,h3,h4,summary{{font-family:"IBM Plex Sans","Helvetica Neue",sans-serif;font-weight:500;letter-spacing:0}}
h1{{font-size:30px;line-height:1.2;margin:0 0 10px}} h2{{font-size:22px;margin:38px 0 12px}} h3{{font-size:18px;margin:28px 0 8px}}
em{{color:#555}} p{{margin:0 0 14px}} li{{margin:0 0 6px}}
figure{{margin:18px 0;background:#fff;border:1px solid #d7dde3;padding:10px}} figure img{{width:100%;display:block}} figcaption{{font:13px/1.5 "IBM Plex Sans",sans-serif;color:#666;margin-top:8px}}
table{{border-collapse:collapse;font:13.5px/1.45 "IBM Plex Sans",sans-serif;background:#fff;margin:10px 0 16px;display:block;overflow-x:auto;max-width:100%}} th,td{{border:1px solid #d7dde3;padding:6px 9px;text-align:left;vertical-align:top}} th{{background:#f3f5f7}}
details.evidence{{border:1px solid #c9d2da;background:#fff;border-radius:6px;margin:14px 0 24px}}
details.evidence>summary{{cursor:pointer;padding:10px 14px;font-size:14.5px;color:#2f6f4f;list-style:none}} details.evidence>summary::before{{content:"▸ ";}} details.evidence[open]>summary::before{{content:"▾ ";}}
details.evidence>.inner{{padding:4px 14px 12px;border-top:1px solid #e3e8ec;font-size:14.5px}}
details.code,details.out,details.tab,details.evidence details{{margin:8px 0}} details.code>summary,details.out>summary,details.tab>summary,details.evidence details>summary{{cursor:pointer;font:13.5px "IBM Plex Sans",sans-serif;color:#2f6f4f}}
pre{{background:#f6f8fa;border:1px solid #e3e8ec;border-radius:6px;padding:12px;font-size:12px;line-height:1.5;overflow-x:auto;white-space:pre}} .note{{font-size:13.5px;color:#555;margin-top:8px}}
.byline{{font:13.5px "IBM Plex Sans",sans-serif;color:#666;margin:0 0 22px}}
</style>
</head>
<body>
<div class="wrap">
  {tocnav}
  <div class="main">
  <div class="top"><a href="../../index.html">← Emily Birch</a> &nbsp;·&nbsp; Self-directed research, post 2 of 5</div>
  {body}
  </div>
</div>
<script>hljs.highlightAll();</script>
</body>
</html>'''
open(os.path.join(SITE, "index.html"), "w").write(page)
print("wrote", os.path.join(SITE, "index.html"), len(page), "bytes")
