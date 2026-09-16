"""post5 (LL-18) feasibility: every cut in BRIEF.md section 8 (C1-C6), at column level.

Run from the repository root:
  python data/replication/post5_cuts_c1_c6.py | tee data/replication/results/post5_cuts_c1_c6.txt

Also writes data/replication/results/post5_cuts_c1_c6.json. Reads the cache only; never
modifies a raw file.
"""
import json
import numpy as np
import pandas as pd
from scipy import stats

NOV = "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet"
FEB = "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet"
JUN = "data/cache/release_2026_06_26/data/aei_claude_ai_2026-06-26.parquet"
POP = "data/cache/release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv"
GDP = "data/cache/release_2025_09_15/data/intermediate/gdp_2024_country.csv"
ISO = "data/cache/release_2025_09_15/data/intermediate/iso_country_codes.csv"

OUT = {}


def load(path):
    df = pd.read_parquet(path)
    df["level"] = df["level"].astype(str)   # dtype differs between parquet siblings
    return df


def wide(df, geography, facet, variables, level="0"):
    d = df[(df.geography == geography) & (df.facet == facet) & (df.level == level) & (df.variable.isin(variables))]
    return d.pivot_table(index=["geo_id", "cluster_name"], columns="variable", values="value", aggfunc="first").reset_index()


nov, feb = load(NOV), load(FEB)
waves = {"nov2025": nov, "feb2026": feb}

print("=" * 78)
print("C1  global human_only_ability")
print("=" * 78)
OUT["C1"] = {}
for w, df in waves.items():
    d = df[(df.geography == "global") & (df.facet == "human_only_ability")]
    piv = d.pivot_table(index="cluster_name", columns="variable", values="value", aggfunc="first")
    print(w, "| variables:", sorted(d.variable.unique()), "| levels:", sorted(d.level.unique()))
    print(piv.to_string())
    pct = piv["human_only_ability_pct"]
    OUT["C1"][w] = {"clusters": list(piv.index), "variables": sorted(d.variable.unique()),
                    "yes": float(pct.get("yes", np.nan)), "no": float(pct.get("no", np.nan)),
                    "sum": float(pct.sum()), "complement_of_yes": float(100 - pct.get("yes", np.nan)),
                    "rows": int(len(d))}
    print(f"  sum of pct = {pct.sum():.6f} ; 100 - yes = {100 - pct['yes']:.4f}")

print()
print("=" * 78)
print("C2  country (and country-state) human_only_ability")
print("=" * 78)
OUT["C2"] = {}
for w, df in waves.items():
    rec = {}
    for geo in ("country", "country-state"):
        d = df[(df.geography == geo) & (df.facet == "human_only_ability")]
        piv = wide(df, geo, "human_only_ability", ["human_only_ability_pct", "human_only_ability_count"])
        units = piv.geo_id.nunique()
        clusters = sorted(piv.cluster_name.unique())
        # pct sums per unit
        s = piv.groupby("geo_id")["human_only_ability_pct"].sum()
        # not_classified share
        nc = piv[piv.cluster_name == "not_classified"].set_index("geo_id")["human_only_ability_pct"]
        rec[geo] = {"units": int(units), "clusters": clusters,
                    "variables": sorted(d.variable.unique()),
                    "pct_sum_min": float(s.min()), "pct_sum_max": float(s.max()),
                    "nc_units": int(nc.notna().sum()), "nc_median": float(nc.median()),
                    "rows": int(len(d))}
        print(f"{w} {geo}: {units} units, clusters={clusters}, vars={sorted(d.variable.unique())}, "
              f"pct sums [{s.min():.4f},{s.max():.4f}], not_classified median {nc.median():.4f} over {nc.notna().sum()} units")
    OUT["C2"][w] = rec

print()
print("=" * 78)
print("C3  country usage_count / usage_pct and the 200 threshold")
print("=" * 78)
OUT["C3"] = {}
usage = {}
for w, df in waves.items():
    d = df[(df.geography == "country") & (df.facet == "country")]
    piv = d.pivot_table(index="geo_id", columns="variable", values="value", aggfunc="first")
    print(w, "| variables:", sorted(d.variable.unique()), "| cluster_name distinct:", d.cluster_name.unique().tolist()[:3],
          "| country ids:", len(piv))
    pseudo = [g for g in piv.index if g in ("not_classified", "NONE", "GLOBAL")]
    real = piv.drop(index=pseudo)
    thr = real[real["usage_count"] >= 200]
    usage[w] = real
    print(f"  pseudo-geographies present: {pseudo}")
    print(f"  real country ids {len(real)}; >=200 conversations: {len(thr)}; min count {real.usage_count.min():.0f}; "
          f"usage_pct sum (incl pseudo) {piv['usage_pct'].sum():.4f}")
    OUT["C3"][w] = {"variables": sorted(d.variable.unique()), "ids": int(len(piv)), "pseudo": pseudo,
                    "real": int(len(real)), "ge200": int(len(thr)), "min_count": float(real.usage_count.min()),
                    "usage_pct_sum_incl_pseudo": float(piv["usage_pct"].sum()),
                    "total_count_all_ids": float(piv["usage_count"].sum())}

# balanced panel: >=200 in both waves AND carrying human_only_ability
setn = set(usage["nov2025"][usage["nov2025"].usage_count >= 200].index)
setf = set(usage["feb2026"][usage["feb2026"].usage_count >= 200].index)
facet_n = set(nov[(nov.geography == "country") & (nov.facet == "human_only_ability")].geo_id)
facet_f = set(feb[(feb.geography == "country") & (feb.facet == "human_only_ability")].geo_id)
panel = (setn & setf & facet_n & facet_f) - {"not_classified", "NONE"}
panel_ex_syc = panel - {"SC"}
print(f"\n  balanced panel (>=200 in BOTH waves, facet present in both): {len(panel)}; "
      f"excluding Seychelles: {len(panel_ex_syc)}")
print(f"  SC rows: nov {int((nov.geo_id == 'SC').sum())}, feb {int((feb.geo_id == 'SC').sum())}")
OUT["panel"] = {"n": len(panel), "n_ex_syc": len(panel_ex_syc),
                "nov_ge200": len(setn), "feb_ge200": len(setf),
                "sc_rows_nov": int((nov.geo_id == "SC").sum()), "sc_rows_feb": int((feb.geo_id == "SC").sum())}

print()
print("=" * 78)
print("C2b  residual semantics, count base, and facet coverage at the threshold")
print("=" * 78)
OUT["C2b"] = {}
for w, df in waves.items():
    piv = wide(df, "country", "human_only_ability", ["human_only_ability_pct", "human_only_ability_count"])
    p = piv.pivot_table(index="geo_id", columns="cluster_name", values="human_only_ability_pct")
    c = piv.pivot_table(index="geo_id", columns="cluster_name", values="human_only_ability_count")
    u = usage[w]["usage_count"]
    joined = c.join(u, how="left")
    tot = c.sum(axis=1)
    diff = (tot - joined["usage_count"]).abs()
    has_nc = p["not_classified"].notna()
    yn = p[["yes", "no"]].sum(axis=1)
    print(f"{w}: countries carrying facet {len(p)}; carrying an explicit not_classified row {int(has_nc.sum())}")
    print(f"  where not_classified is ABSENT: yes+no pct median {yn[~has_nc].median():.4f}, min {yn[~has_nc].min():.4f}")
    print(f"  where present: yes+no pct median {yn[has_nc].median():.4f}, min {yn[has_nc].min():.4f}")
    print(f"  facet counts vs usage_count: max abs diff {diff.max():.0f}; countries where they differ {int((diff > 0).sum())}")
    ge200 = set(usage[w][usage[w].usage_count >= 200].index) - {"not_classified", "NONE"}
    missing = ge200 - set(p.index)
    print(f"  countries >=200 without the facet: {len(missing)} {sorted(missing)[:10]}")
    # minimum cell counts at the threshold
    sub = c.loc[sorted(ge200 & set(c.index))]
    print(f"  over >=200 countries: min facet total {sub.sum(axis=1).min():.0f}, median {sub.sum(axis=1).median():.0f}; "
          f"min 'no' count {sub['no'].min():.0f}; countries with no 'no' row {int(sub['no'].isna().sum())}")
    OUT["C2b"][w] = {"facet_units": int(len(p)), "explicit_nc": int(has_nc.sum()),
                     "yn_sum_median_when_nc_absent": float(yn[~has_nc].median()),
                     "count_vs_usage_maxdiff": float(diff.max()),
                     "ge200_without_facet": sorted(missing),
                     "min_facet_total_ge200": float(sub.sum(axis=1).min()),
                     "min_no_count_ge200": float(sub["no"].min()),
                     "missing_no_row_ge200": int(sub["no"].isna().sum())}

print()
print("=" * 78)
print("C4  global onet_task::human_only_ability")
print("=" * 78)
OUT["C4"] = {}
for w, df in waves.items():
    d = df[(df.geography == "global") & (df.facet == "onet_task::human_only_ability")]
    other = df[(df.geography != "global") & (df.facet == "onet_task::human_only_ability")]
    cl = d.cluster_name
    tasks = cl.str.rsplit("::", n=1).str[0]
    suff = cl.str.rsplit("::", n=1).str[1]
    print(w, "| rows", len(d), "| variables", sorted(d.variable.unique()), "| distinct tasks", tasks.nunique(),
          "| suffixes", sorted(suff.unique()), "| rows at non-global grain:", len(other))
    dd = d.assign(task=tasks, arm=suff)
    piv = dd[dd.variable == "onet_task_human_only_ability_pct"] \
        .pivot_table(index="task", columns="arm", values="value", aggfunc="first")
    cnt = dd[dd.variable == "onet_task_human_only_ability_count"] \
        .pivot_table(index="task", columns="arm", values="value", aggfunc="first")
    both = piv[["yes", "no"]].dropna()
    armsum = piv.sum(axis=1)
    print(f"  tasks with a 'no' arm: {int(piv['no'].notna().sum())}; with 'yes': {int(piv['yes'].notna().sum())}; "
          f"with both: {len(both)}; with a not_classified arm: {int(piv['not_classified'].notna().sum())}")
    print(f"  per-task pct over all published arms: median {armsum.median():.4f}, min {armsum.min():.4f}, max {armsum.max():.4f}")
    print(f"  per-task counts: min total {cnt.sum(axis=1).min():.0f}, median {cnt.sum(axis=1).median():.0f}")
    OUT["C4"][w] = {"rows": int(len(d)), "variables": sorted(d.variable.unique()), "tasks": int(tasks.nunique()),
                    "suffixes": sorted(suff.unique()), "nonglobal_rows": int(len(other)),
                    "tasks_with_no": int(piv["no"].notna().sum()), "tasks_with_yes": int(piv["yes"].notna().sum()),
                    "tasks_both_arms": int(len(both)), "armsum_median": float(armsum.median()),
                    "armsum_min": float(armsum.min()), "count_min": float(cnt.sum(axis=1).min())}

print()
print("=" * 78)
print("C5  country onet_task mix")
print("=" * 78)
OUT["C5"] = {}
for w, df in waves.items():
    d = df[(df.geography == "country") & (df.facet == "onet_task") & (df.variable == "onet_task_pct")]
    units = d.geo_id.nunique()
    nodes = d[~d.cluster_name.isin(["none", "not_classified"])].groupby("geo_id").size()
    mass = d[~d.cluster_name.isin(["none", "not_classified"])].groupby("geo_id").value.sum()
    residual_labels = sorted(set(d.cluster_name) & {"none", "not_classified"})
    tot = d.groupby("geo_id").value.sum()
    print(f"{w}: {units} country ids carry onet_task; residual labels {residual_labels}; "
          f"named nodes per country median {nodes.median():.0f}; named mass median {mass.median():.2f}%; "
          f"total pct per country [{tot.min():.4f},{tot.max():.4f}]")
    panel_mass = mass.reindex(sorted(panel)).dropna()
    print(f"  over the {len(panel)}-country panel: {len(panel_mass)} carry onet_task, named-mass median {panel_mass.median():.2f}%, "
          f"min {panel_mass.min():.2f}%, 10th pct {panel_mass.quantile(.1):.2f}%")
    OUT["C5"][w] = {"units": int(units), "residual_labels": residual_labels,
                    "named_nodes_median": float(nodes.median()), "named_mass_median": float(mass.median()),
                    "panel_units_with_onet": int(len(panel_mass)), "panel_named_mass_median": float(panel_mass.median()),
                    "panel_named_mass_min": float(panel_mass.min())}

print()
print("=" * 78)
print("C4b  request::human_only_ability (NOT named in BRIEF section 8; the wider-coverage sibling)")
print("=" * 78)
OUT["C4b"] = {}
for w, df in waves.items():
    d = df[df.facet == "request::human_only_ability"]
    rec = {"geographies": sorted(d.geography.unique()), "levels": sorted(d.level.unique()),
           "variables": sorted(d.variable.unique()), "levels_detail": {}}
    for lv in sorted(d.level.unique()):
        g = d[(d.geography == "global") & (d.level == lv) & (d.variable == "request_human_only_ability_count")]
        node = g.cluster_name.str.rsplit("::", n=1).str[0]
        arm = g.cluster_name.str.rsplit("::", n=1).str[1]
        piv = g.assign(n=node, a=arm).pivot_table(index="n", columns="a", values="value")
        rate = (100 * piv["no"] / (piv["yes"] + piv["no"])).dropna()
        rec["levels_detail"][lv] = {"nodes": int(piv.shape[0]), "with_rate": int(len(rate)),
                                    "rate_min": float(rate.min()), "rate_max": float(rate.max())}
        print(f"{w} level {lv}: {piv.shape[0]} global nodes, {len(rate)} with a computable no-rate, "
              f"spread {rate.min():.1f}-{rate.max():.1f} pp")
    OUT["C4b"][w] = rec

print()
print("=" * 78)
print("C5b  country request mix by level (the shift-share denominator alternatives)")
print("=" * 78)
OUT["C5b"] = {}
for w, df in waves.items():
    rec = {}
    for lv in ("0", "1", "2"):
        c = df[(df.geography == "country") & (df.facet == "request") & (df.variable == "request_pct") & (df.level == lv)]
        named = c[~c.cluster_name.isin(["none", "not_classified"])]
        mass = named.groupby("geo_id").value.sum()
        pm = mass.reindex(sorted(panel)).dropna()
        rec[lv] = {"ids": int(c.geo_id.nunique()), "panel_ids": int(len(pm)),
                   "panel_named_mass_median": float(pm.median()), "panel_named_mass_min": float(pm.min())}
        print(f"{w} request L{lv}: {c.geo_id.nunique()} country ids; over the panel {len(pm)} countries, "
              f"named mass median {pm.median():.1f}%, min {pm.min():.1f}%")
    OUT["C5b"][w] = rec

print()
print("=" * 78)
print("C6  June 2026 country / overall")
print("=" * 78)
jun = pd.read_parquet(JUN)
jun["hierarchy_level"] = jun["hierarchy_level"].astype(str)
d = jun[(jun.geo_level == "country") & (jun.category_name == "overall")]
mids = sorted(d.metric_id.unique())
has_hoa = [m for m in mids if "human_only_ability" in m]
has_upc = [m for m in mids if "usage_per_capita" in m]
counts = [m for m in mids if "count" in m.lower()]
ids_by_month = d.groupby("date_start").geo_id.nunique()
hoa = d[d.metric_id == "human_only_ability_pct"]
upc = d[d.metric_id == "usage_per_capita_index"]
print("metric ids at country/overall:", len(mids))
print("human_only_ability metrics:", has_hoa, "| usage_per_capita metrics:", has_upc, "| count-like:", counts)
print("country ids per month:", ids_by_month.to_dict())
print("human_only_ability_pct ids per month:", hoa.groupby("date_start").geo_id.nunique().to_dict())
print("usage_per_capita_index ids per month:", upc.groupby("date_start").geo_id.nunique().to_dict())
both_months_hoa = set.intersection(*[set(g.geo_id) for _, g in hoa.groupby("date_start")])
both_months_upc = set.intersection(*[set(g.geo_id) for _, g in upc.groupby("date_start")])
print(f"countries with human_only_ability_pct in BOTH months: {len(both_months_hoa)}; with AUI in both: {len(both_months_upc)}; "
      f"with both metrics in both months: {len(both_months_hoa & both_months_upc)}")
gl = jun[(jun.geo_id == "GLOBAL") & (jun.category_name == "overall") & (jun.metric_id == "human_only_ability_pct")]
print("global human_only_ability_pct by month:", gl.set_index("date_start").value.to_dict())
OUT["C6"] = {"metric_ids": len(mids), "hoa_metrics": has_hoa, "aui_metrics": has_upc, "count_metrics": counts,
             "ids_per_month": {k: int(v) for k, v in ids_by_month.items()},
             "hoa_both_months": len(both_months_hoa), "aui_both_months": len(both_months_upc),
             "both_metrics_both_months": len(both_months_hoa & both_months_upc),
             "global_hoa": gl.set_index("date_start").value.to_dict()}

with open("data/replication/results/post5_cuts_c1_c6.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\nwrote data/replication/results/post5_cuts_c1_c6.json")
