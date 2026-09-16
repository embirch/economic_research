"""Step 03: repeat the task-mix-adjusted partial regression on every wave, and harmonise codes.

What this does
  1. Validates our reconstruction of the AI Usage Index (AUI): in Aug 2025 the file carries both
     usage_pct and the published AUI, so we rebuild AUI from usage_pct and the population file and
     check it matches. Only then do we use the same formula for Nov 2025 and Feb 2026, which carry
     usage_pct but no AUI.  AUI = (country's share of usage) / (country's share of working-age
     population among the countries in the population file).
  2. For each wave: expected automation from the country's task mix x global per-task automation
     rates (the Aug 2025 method), residuals, partial slope.  June 2026 has no task-level automation
     by country, so its adjustment uses the O*NET task nodes (level 0) with global automation rates
     per node, which is the same construction on the same objects under a new schema.
  3. Harmonises country codes to ISO-3 (Nov 2025 and Feb 2026 use ISO-2) and writes one table with
     one row per country-wave: automation, expected, residual, AUI.
Why
  Nobody has asked whether the Aug 2025 gap persisted. And later steps need every wave on one
  code system.
"""
import pandas as pd, numpy as np, statsmodels.api as sm, json, os
RAW="data/raw"; OUT="data/processed"
pop = pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_country.csv", keep_default_na=False)
pop = pop[pop.iso_alpha_3 != ""]
iso2to3 = dict(zip(pop.country_code, pop.iso_alpha_3))
pop_share = (pop.set_index("iso_alpha_3").working_age_pop / pop.working_age_pop.sum())

def partial(auto, aui, expected):
    d = pd.concat([auto.rename("automation"), aui.rename("aui"), expected.rename("expected")], axis=1, join="inner").dropna()
    r = lambda y, x: sm.OLS(y, sm.add_constant(x)).fit().resid
    d["auto_resid"] = r(d.automation, d.expected); d["aui_resid"] = r(d.aui, d.expected)
    f = sm.OLS(d.auto_resid, sm.add_constant(d.aui_resid)).fit()
    return d, f.params.iloc[1], f.rsquared, f.pvalues.iloc[1]

def expected_from_tasks(task_shares, global_rates):
    """task_shares: DataFrame[geo_id, task, w]; global_rates: Series task -> automation % ."""
    t = task_shares[task_shares.task.isin(global_rates.index)].copy()
    t["r"] = t.task.map(global_rates)
    g = t.groupby("geo_id")
    return (g.apply(lambda x: (x.w * x.r).sum() / x.w.sum(), include_groups=False)).rename("expected")

ANOMALY_CAP = 25.0   # pre-stated rule (plan §5, added 15 Sep): an index above 25 (Israel, the highest ever published, is 7.0)
                     # means machine or routed traffic, not a population using Claude. Excluded and named, never silently.
exclusions = []
def drop_anomalies(aui, wave):
    bad = aui[aui > ANOMALY_CAP]
    for g, v in bad.items():
        exclusions.append({"wave": wave, "geo_id": g, "aui": float(v)}); print(f"  EXCLUDED {wave} {g}: index {v:.0f} (> {ANOMALY_CAP})")
    return aui.drop(bad.index)
results = {}; frames = []

# ---------- long-schema waves (Aug 2025, Nov 2025, Feb 2026) ----------
long_waves = [("2025-08", f"{RAW}/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv", "ISO3"),
              ("2025-11", f"{RAW}/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv", "ISO2"),
              ("2026-02", f"{RAW}/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv", "ISO2")]
for wave, path, codesys in long_waves:
    df = pd.read_csv(path, keep_default_na=False, low_memory=False, usecols=["geo_id","geography","facet","variable","cluster_name","value"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    c = df[df.geography == "country"].copy()
    if codesys == "ISO2":
        c["geo_id"] = c.geo_id.map(iso2to3).fillna(c.geo_id)      # harmonise to ISO-3 (NA=Namibia survives: keep_default_na=False)
    usage = c[(c.facet=="country")&(c.variable=="usage_count")].set_index("geo_id")["value"]
    keep = [g for g in usage[usage>=200].index if g!="not_classified"]
    col = c[(c.facet=="collaboration")&(c.variable=="collaboration_pct")&(c.geo_id.isin(keep))]
    # Anthropic's automation share is a percentage of the FIVE classified patterns (verified on Aug 2025: automation_pct
    # equals (directive + feedback loop) / (sum of the five) x 100, not the share of all conversations). Same base here.
    five = col[col.cluster_name.isin(["directive","feedback loop","task iteration","learning","validation"])].groupby("geo_id")["value"].sum()
    auto = col[col.cluster_name.isin(["directive","feedback loop"])].groupby("geo_id")["value"].sum() / five * 100
    # Anthropic's convention (release notebook, calculate_usage_per_capita_index): both the usage total and
    # the population total are taken over the thresholded countries only, then index = usage share / pop share.
    # Verified empirically on Aug 2025 (max difference 0.00000 against the published index):
    #   usage share = country count / (sum of counts over thresholded countries + the 'not_classified' count)
    #   pop share   = country working-age pop / (sum over thresholded countries)
    wap = pop.set_index("iso_alpha_3").working_age_pop
    kept_pop = wap.reindex(keep).dropna()
    total_usage = usage.reindex(kept_pop.index).sum() + float(usage.get("not_classified", 0.0))
    total_pop = kept_pop.sum()
    aui_rebuilt = (usage.reindex(kept_pop.index) / total_usage) / (kept_pop / total_pop)
    if wave == "2025-08":
        aui_pub = c[(c.facet=="country")&(c.variable=="usage_per_capita_index")].set_index("geo_id")["value"]
        both = pd.concat([aui_pub.rename("pub"), aui_rebuilt.rename("rebuilt")], axis=1, join="inner").dropna()
        both = both[both.index.isin(keep)]
        maxdiff = (both.pub - both.rebuilt).abs().max()
        print(f"AUI reconstruction check on Aug 2025: {len(both)} countries, max |published - rebuilt| = {maxdiff:.4f}")
        assert maxdiff < 0.005, "AUI reconstruction does not match the published index"
        aui = aui_pub
        auto = c[(c.facet=="collaboration_automation_augmentation")&(c.variable=="automation_pct")&(c.geo_id.isin(keep))].set_index("geo_id")["value"]
    else:
        aui = aui_rebuilt
    aui = drop_anomalies(aui, wave)
    tasks = c[(c.facet=="onet_task")&(c.variable=="onet_task_pct")&(c.geo_id.isin(keep))]
    tasks = tasks[~tasks.cluster_name.isin(["not_classified","none"])].rename(columns={"cluster_name":"task","value":"w"})[["geo_id","task","w"]]
    g = df[(df.geography=="global")&(df.facet=="onet_task::collaboration")&(df.variable=="onet_task_collaboration_pct")].copy()
    g["task"]=g.cluster_name.str.split("::").str[0]; g["mode"]=g.cluster_name.str.split("::").str[1]
    g = g[g["mode"].isin(["directive","feedback loop","validation","task iteration","learning"])]
    rates = g.groupby("task").apply(lambda t: t.loc[t["mode"].isin(["directive","feedback loop"]),"value"].sum()/t["value"].sum()*100, include_groups=False)
    exp = expected_from_tasks(tasks, rates)
    d, slope, r2, p = partial(auto, aui.reindex(auto.index), exp)
    d["wave"]=wave; d.index.name="geo_id"; frames.append(d.reset_index())
    results[wave] = {"slope": float(slope), "r2": float(r2), "p": float(p), "n": int(len(d)), "tasks": int(len(rates))}
    print(f"{wave}: slope = {slope:.3f}, R2 = {r2:.3f}, p = {p:.1e}, N = {len(d)}, tasks with rates = {len(rates)}")

# ---------- June 2026 (wide schema; O*NET nodes level 0 = tasks) ----------
v6 = pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv", keep_default_na=False, low_memory=False,
                 usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_external_id"])
v6["value"] = pd.to_numeric(v6["value"], errors="coerce")
for ds, wave in [("2026-04-01","2026-04"),("2026-05-01","2026-05")]:
    m = v6[v6.date_start==ds]
    ov = m[(m.geo_level=="country")&(m.category_name=="overall")]
    auto = ov[ov.metric_id=="collaboration_bucket_automation_pct"].set_index("geo_id")["value"]
    aui  = drop_anomalies(ov[ov.metric_id=="usage_per_capita_index"].set_index("geo_id")["value"], wave)
    on = m[(m.category_name=="onet")&(m.hierarchy_level.astype(str)=="0")]
    tasks = on[(on.geo_level=="country")&(on.metric_id=="pct")].rename(columns={"node_external_id":"task","value":"w"})[["geo_id","task","w"]]
    rates = on[(on.geo_level=="global")&(on.metric_id=="collaboration_bucket_automation_pct")].set_index("node_external_id")["value"]
    exp = expected_from_tasks(tasks, rates)
    d, slope, r2, p = partial(auto, aui.reindex(auto.index), exp)
    d["wave"]=wave; d.index.name="geo_id"; frames.append(d.reset_index())
    results[wave] = {"slope": float(slope), "r2": float(r2), "p": float(p), "n": int(len(d)), "tasks": int(len(rates))}
    print(f"{wave}: slope = {slope:.3f}, R2 = {r2:.3f}, p = {p:.1e}, N = {len(d)}, task nodes with rates = {len(rates)}  [June: node-level adjustment]")

allw = pd.concat(frames, ignore_index=True)
allw.to_csv(f"{OUT}/03_partial_by_wave.csv", index=False)
json.dump({"by_wave": results, "exclusions": exclusions}, open(f"{OUT}/03_partial_stats.json","w"), indent=1)

# ---------- check block ----------
assert abs(results["2025-08"]["slope"] + 3.112) < 0.01 and results["2025-08"]["n"] == 111, "Aug 2025 must reproduce step 02 exactly"
assert all(v["slope"] < 0 for v in results.values()), "every wave should show the negative relationship"
assert allw.geo_id.str.len().eq(3).all(), "all codes should be ISO-3 after harmonisation"
print("CHECK OK: Aug 2025 reproduces step 02; all waves negative; codes harmonised to ISO-3")
