"""Step 02: replicate Anthropic's Figure 2.11 exactly, two ways.

What this does
  A. Extracts the numerical part of Anthropic's own function `collaboration_task_regression`
     from the released code file (everything up to where it starts drawing the figure) and runs
     it verbatim on the public August 2025 file. Published result: slope 3.112 (negative
     relationship), R^2 0.394, p < 0.001.
  B. Re-computes the same thing with our own independent code, written from the description:
       expected automation for a country = sum over its tasks of (task weight x global
       automation rate for that task) / sum of weights;  then regress actual automation on
       expected (residual A), regress the Usage Index on expected (residual B), and regress
       residual A on residual B. The slope of that last regression is the "partial" slope.
  C. Compares A and B to the decimal, and both to the published numbers.
Why
  If our pipeline reproduces their number with their code AND with ours, every later step
  starts from the same place they did. If it does not, we stop.
Vocabulary
  partial regression = the relationship between two things after a third (task mix) has been
  removed from both. "Residual" = what is left after removing it.
"""
import re, types, pandas as pd, numpy as np, statsmodels.api as sm, os, json
RAW = "data/raw/release_2025_09_15"; OUT = "data/processed"; CHK = "outputs/checks"
FILE = f"{RAW}/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"
PUBLISHED = {"slope": 3.112, "r2": 0.394}

# ---------- A. Anthropic's code, verbatim (numerical part only) ----------
src = open(f"{RAW}/code/aei_analysis_functions_claude_ai.py").read()
def grab(name, stop_marker):
    start = src.index(f"def {name}(")
    end = src.index(stop_marker, start)
    return src[start:end]
filter_src = grab("filter_df", "\ndef get_filtered_geographies")
geos_src   = grab("get_filtered_geographies", "\ndef ")            # up to the next function
core_src   = grab("collaboration_task_regression", "    # Create visualization")
core_src  += "    return df_regression, partial_slope, partial_r2, partial_p, n_tasks\n"
ns = {"pd": pd, "np": np, "sm": sm, "MIN_OBSERVATIONS_COUNTRY": 200, "MIN_OBSERVATIONS_US_STATE": 100}
exec(filter_src + "\n" + geos_src + "\n" + core_src, ns)
df = pd.read_csv(FILE, keep_default_na=False, low_memory=False)
df["value"] = pd.to_numeric(df["value"], errors="coerce")
regA, slopeA, r2A, pA, ntasksA = ns["collaboration_task_regression"](df, geography="country")
print(f"A. Anthropic's function: slope = {slopeA:.3f}, R2 = {r2A:.3f}, p = {pA:.2e}, countries = {len(regA)}, tasks = {ntasksA}")

# ---------- B. Our independent implementation ----------
c = df[df.geography == "country"]
usage = c[(c.facet == "country") & (c.variable == "usage_count")].set_index("geo_id")["value"]
keep = [g for g in usage[usage >= 200].index if g != "not_classified"]
auto = c[(c.facet == "collaboration_automation_augmentation") & (c.variable == "automation_pct") & (c.geo_id.isin(keep))].set_index("geo_id")["value"]
aui  = c[(c.facet == "country") & (c.variable == "usage_per_capita_index") & (c.geo_id.isin(keep))].set_index("geo_id")["value"]
tasks = c[(c.facet == "onet_task") & (c.variable == "onet_task_pct") & (c.geo_id.isin(keep))]
tasks = tasks[~tasks.cluster_name.isin(["not_classified", "none"])]
g = df[(df.geography == "global") & (df.facet == "onet_task::collaboration") & (df.variable == "onet_task_collaboration_pct")].copy()
g["task"] = g.cluster_name.str.split("::").str[0]; g["mode"] = g.cluster_name.str.split("::").str[1]
g = g[g["mode"].isin(["directive", "feedback loop", "validation", "task iteration", "learning"])]
g["is_auto"] = g["mode"].isin(["directive", "feedback loop"])
rate = g.groupby("task").apply(lambda t: t.loc[t.is_auto, "value"].sum() / t["value"].sum() * 100)
rows = []
for geo, t in tasks.groupby("geo_id"):
    t = t[t.cluster_name.isin(rate.index)]
    if t.empty: continue
    rows.append((geo, float((t["value"] * t.cluster_name.map(rate)).sum() / t["value"].sum())))
exp = pd.DataFrame(rows, columns=["geo_id", "expected"]).set_index("geo_id")["expected"]
B = pd.concat([auto.rename("automation"), aui.rename("aui"), exp], axis=1, join="inner")
def resid(y, x):
    X = sm.add_constant(x); return sm.OLS(y, X).fit().resid
B["auto_resid"] = resid(B.automation, B.expected); B["aui_resid"] = resid(B.aui, B.expected)
fitB = sm.OLS(B.auto_resid, sm.add_constant(B.aui_resid)).fit()
slopeB, r2B, pB = fitB.params.iloc[1], fitB.rsquared, fitB.pvalues.iloc[1]
print(f"B. Independent code:      slope = {slopeB:.3f}, R2 = {r2B:.3f}, p = {pB:.2e}, countries = {len(B)}, tasks = {len(rate)}")

# ---------- write the replication table (this is the object later steps use) ----------
B.index.name = "geo_id"
B.to_csv(f"{OUT}/02_replication_aug2025.csv")
json.dump({"anthropic_fn": {"slope": slopeA, "r2": r2A, "p": pA, "n": int(len(regA))},
           "independent": {"slope": slopeB, "r2": r2B, "p": pB, "n": int(len(B))},
           "published": PUBLISHED}, open(f"{OUT}/02_replication_stats.json", "w"), indent=1)

# ---------- C. check block ----------
assert abs(abs(slopeA) - PUBLISHED["slope"]) < 0.05, f"Anthropic-code slope {slopeA:.3f} vs published {PUBLISHED['slope']}"
assert abs(r2A - PUBLISHED["r2"]) < 0.01, f"Anthropic-code R2 {r2A:.3f} vs published {PUBLISHED['r2']}"
assert abs(slopeA - slopeB) < 1e-6 and abs(r2A - r2B) < 1e-6, "our implementation disagrees with Anthropic's"
assert slopeA < 0, "relationship should be negative (more adoption, less automation)"
print(f"CHECK OK: both implementations agree to the decimal and match the published slope {PUBLISHED['slope']} and R2 {PUBLISHED['r2']}; sign negative as reported")
