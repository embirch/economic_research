"""Builds the interactive post page from the research folder.
Output: site/posts/post1/index.html (+ figures copied alongside).  Run from research/post1:  ../.venv/bin/python build_page.py
The page is the write-up (POST.md) with evidence drawers generated from scripts/, outputs/, prereg/ and notes/.
Nothing on the page is typed by hand; if the research changes, rerun this and the page changes with it."""
import os, re, json, html, shutil, markdown, pandas as pd
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(ROOT, "..", "..", "site", "posts", "post1"))
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
figs = {"Figure 1": "fig1_replication_by_wave.png", "Figure 2": "fig2_pdi_before_after_income.png", "Figure 3": "fig3_coefficients.png", "Figure 4": "fig4_within_groups.png", "Figure 5": "fig5_unbundling.png", "Figure 6": "fig6_activities.png", "Figure 7": "fig7_us_states.png"}
for k, f in figs.items():
    post = re.sub(rf"\*{k}\.([^*]*)\*", rf'<figure><img src="figures/{f}" alt="{k}"><figcaption>{k}.\1</figcaption></figure>', post)
body = markdown.markdown(post, extensions=["tables"])
detail = read("notes/exploratory-detail.md")
for k, f in figs.items():
    detail = re.sub(rf"\*{k}\.([^*]*)\*", rf'<figure><img src="figures/{f}" alt="{k}"><figcaption>{k}.\1</figcaption></figure>', detail)
detail_html = markdown.markdown(detail, extensions=["tables"]).replace("<h1>", "<h3>").replace("</h1>", "</h3>").replace("<h2>", "<h4>").replace("</h2>", "</h4>")

# ---------- evidence drawers keyed to the new section headings ----------
ev = {
 "The gap is real": drawer("Evidence: the replication and its repetition on later waves",
     code("scripts/02_replicate.py") + check("02") + code("scripts/03_repeat_waves.py") + check("03") +
     '<p class="note">Anthropic\'s function is extracted verbatim from the released code (numerical part) and run on the public file; the independent implementation follows the report\'s description and must agree to the decimal.</p>'),
 "Authority norms seem to matter": drawer("Evidence: the primary model and the robustness battery",
     table_csv("outputs/tables/06_main_model.csv", "Full model, August 2025, HC3 robust errors", "term") +
     table_csv("outputs/tables/07_robustness.csv", "Power-distance coefficient across specifications", "specification") +
     code("scripts/06_main_test.py") + check("06") + code("scripts/07_robustness.py") + check("07")),
 "Is it the newness": drawer("Evidence: the newness ceiling, the within-country panel and the Super Bowl comparison",
     code("scripts/05_ceiling.py") + check("05") + code("scripts/08_panel.py") + check("08")),
 "The same gradient inside": drawer("Evidence: the pre-registered state test, the 2026 waves and the subregions",
     table_csv("data/processed/20_us_states.csv", "State table, August 2025: adjusted automation, Usage Index, income, Census education and broadband", "state") +
     code("scripts/20_us_states.py") + check("20") + code("scripts/21_june_subregions.py") + check("21") + code("scripts/22_fig7.py") +
     '<p class="note">The state addendum to the pre-registration (data, models, decision rule, robustness) is in the Methodology drawer "Hypotheses and specification as set in advance"; the notebook records that the rule\'s full-model MDE turned out to be uninformative and how the verdict was reached.</p>'),
 "What income stands for": drawer("The full exploratory write-up, as it was written, with every table", detail_html) +
     drawer("Evidence: unbundling, which pattern moves, occupation groups, activities, institutions, composition, education systems, World Values Survey",
     code("scripts/11_unbundle.py") + check("11") + code("scripts/12_unbundle_checks.py") + check("12") + code("scripts/13_which_pattern.py") + check("13") +
     code("scripts/09_extension.py") + check("09") + code("scripts/14_all_groups.py") + check("14") + code("scripts/16_activities.py") + check("16") +
     code("scripts/15_institutions.py") + check("15") + code("scripts/17_composition_within_groups.py") + check("17") + code("scripts/18_education_systems.py") + check("18") + code("scripts/19_wvs.py") + check("19")),
 "Methodology": drawer("Data loading, thresholds and the country table",
     code("scripts/01_load_threshold.py") + check("01") + code("scripts/04_build_table.py") + check("04")) +
     drawer("Figures", code("scripts/10_figures.py") + check("10")) +
     drawer("Lab notebook: every step and every deviation, dated", md("notes/lab-notebook.md")) +
     drawer("Anticipated objections, and what the post concedes", md("notes/red-team.md")) +
     drawer("Hypotheses and specification as set in advance", md("prereg/prereg.md")) +
     drawer("Reproduce everything", '<p>Create a Python environment with pandas, numpy, statsmodels, scipy, matplotlib and xlrd; download the four Economic Index releases, the Stanford partner file, the Hofstede file, the two GLOBE files, the WGI workbook, the World Values Survey wave 7 CSV and the three ACS 2023 summary tables into <code>data/raw/</code>; then run:</p>' + code("scripts/run_all.sh", "bash") + '<p>Every script ends with a check block that stops on a wrong number. Steps 15, 18 and 20 need the WGI workbook, the World Bank API and the Census summary files respectively; the last full run passed every check.</p>'),
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
  <div class="top"><a href="../../index.html">← Emily Birch</a> &nbsp;·&nbsp; Self-directed research, post 1 of 5</div>
  {body}
  </div>
</div>
<script>hljs.highlightAll();</script>
</body>
</html>'''
open(os.path.join(SITE, "index.html"), "w").write(page)
print("wrote", os.path.join(SITE, "index.html"), len(page), "bytes")
