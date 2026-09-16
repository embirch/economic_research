"""post5 (LL-18) feasibility: the four replication targets of BRIEF section 8, the two
supplementary joins with merge audits, the MDE inputs, and shift-share coverage for T3.

Run from the repository root:
  python data/replication/post5_replication_and_mde.py | tee data/replication/results/post5_replication_and_mde.txt

Also writes data/replication/results/post5_replication_and_mde.json.
"""
import json
import numpy as np
import pandas as pd
from scipy import stats

NOV = "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet"
FEB = "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet"
POP = "data/cache/release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv"
GDP = "data/cache/release_2025_09_15/data/intermediate/gdp_2024_country.csv"
ISO = "data/cache/release_2025_09_15/data/intermediate/iso_country_codes.csv"
OUT = {}


def load(p):
    d = pd.read_parquet(p)
    d["level"] = d["level"].astype(str)
    return d


def country_facet(df, facet, variable):
    d = df[(df.geography == "country") & (df.facet == facet) & (df.variable == variable) & (df.level == "0")]
    return d.pivot_table(index="geo_id", columns="cluster_name", values="value", aggfunc="first")


nov, feb = load(NOV), load(FEB)
waves = {"nov2025": nov, "feb2026": feb}

# ---------------------------------------------------------------- R1 / R2
print("=" * 78)
print("R1/R2  global 'Human can't do alone (%)' 12.09 -> 12.24 and Figure 2.2's 88%")
print("=" * 78)
rep = {}
for w, df in waves.items():
    g = df[(df.geography == "global") & (df.facet == "human_only_ability")]
    p = g[g.variable == "human_only_ability_pct"].set_index("cluster_name").value
    c = g[g.variable == "human_only_ability_count"].set_index("cluster_name").value
    rep[w] = {"yes_pct": float(p["yes"]), "no_pct": float(p["no"]), "complement": float(100 - p["yes"]),
              "yes_count": float(c["yes"]), "no_count": float(c["no"]), "N": float(c.sum())}
    print(f"{w}: yes {p['yes']:.6f}  no {p['no']:.6f}  100-yes {100 - p['yes']:.4f}  N {c.sum():.0f}")
print(f"published R5 Table 1.1: 12.09 -> 12.24 ; rebuilt {rep['nov2025']['complement']:.2f} -> {rep['feb2026']['complement']:.2f}")
print(f"published R4 Fig 2.2: 88% (N=999,875) ; rebuilt {rep['nov2025']['yes_pct']:.2f}% (N={rep['nov2025']['N']:.0f})")
OUT["R1_R2"] = rep

# ---------------------------------------------------------------- joins
print()
print("=" * 78)
print("Supplementary joins: World Bank working-age population and IMF GDP (both shipped in 2025-09-15)")
print("=" * 78)
pop = pd.read_csv(POP, keep_default_na=False)
gdp = pd.read_csv(GDP, keep_default_na=False)
iso = pd.read_csv(ISO, keep_default_na=False, encoding="latin-1")
print("pop:", pop.shape, list(pop.columns), "| gdp:", gdp.shape, list(gdp.columns), "| iso:", iso.shape, list(iso.columns))
pop2 = pop[["country_code", "iso_alpha_3", "working_age_pop"]].rename(columns={"country_code": "geo_id"})
gdp2 = gdp[["iso_alpha_3", "gdp_total"]]

OUT["joins"] = {}
usage = {}
for w, df in waves.items():
    u = df[(df.geography == "country") & (df.facet == "country")].pivot_table(index="geo_id", columns="variable", values="value")
    usage[w] = u
    rows_in = len(u)
    m = u.reset_index().merge(pop2, on="geo_id", how="left")
    matched = m.working_age_pop.notna().sum()
    unmatched = sorted(m.loc[m.working_age_pop.isna(), "geo_id"])
    print(f"\n[{w}] population join on ISO-2 country_code: rows in {rows_in}, matched {matched}, "
          f"unmatched {rows_in - matched}: {unmatched}")
    mg = m.merge(gdp2, on="iso_alpha_3", how="left")
    matched_g = mg.gdp_total.notna().sum()
    unmatched_g = sorted(mg.loc[mg.gdp_total.isna() & mg.iso_alpha_3.notna() & (mg.iso_alpha_3 != ""), "geo_id"])
    print(f"[{w}] GDP join on iso_alpha_3: rows in {rows_in}, matched {matched_g}, unmatched {rows_in - matched_g}"
          f" (of those with an ISO-3: {unmatched_g})")
    thr = mg[mg.usage_count >= 200]
    print(f"[{w}] over the >=200 set ({len(thr)} countries): population {thr.working_age_pop.notna().sum()}, "
          f"GDP {thr.gdp_total.notna().sum()}, both {(thr.working_age_pop.notna() & thr.gdp_total.notna()).sum()}")
    OUT["joins"][w] = {"rows_in": int(rows_in), "pop_matched": int(matched), "pop_unmatched": unmatched,
                       "gdp_matched": int(matched_g), "gdp_unmatched_with_iso3": unmatched_g,
                       "ge200": int(len(thr)), "ge200_pop": int(thr.working_age_pop.notna().sum()),
                       "ge200_gdp": int(thr.gdp_total.notna().sum()),
                       "ge200_both": int((thr.working_age_pop.notna() & thr.gdp_total.notna()).sum())}

# balanced panel
panel = sorted((set(usage["nov2025"].query("usage_count>=200").index) &
                set(usage["feb2026"].query("usage_count>=200").index)) - {"not_classified", "NONE"})
pj = pd.DataFrame({"geo_id": panel}).merge(pop2, on="geo_id", how="left").merge(gdp2, on="iso_alpha_3", how="left")
print(f"\nbalanced panel {len(panel)} countries: population {pj.working_age_pop.notna().sum()}, "
      f"GDP {pj.gdp_total.notna().sum()}, both {(pj.working_age_pop.notna() & pj.gdp_total.notna()).sum()}")
print("  panel countries missing population:", sorted(pj.loc[pj.working_age_pop.isna(), 'geo_id']))
print("  panel countries missing GDP:", sorted(pj.loc[pj.gdp_total.isna(), 'geo_id']))
OUT["panel_join"] = {"n": len(panel), "pop": int(pj.working_age_pop.notna().sum()), "gdp": int(pj.gdp_total.notna().sum()),
                     "both": int((pj.working_age_pop.notna() & pj.gdp_total.notna()).sum()),
                     "missing_pop": sorted(pj.loc[pj.working_age_pop.isna(), "geo_id"]),
                     "missing_gdp": sorted(pj.loc[pj.gdp_total.isna(), "geo_id"])}

# ---------------------------------------------------------------- R3 AUI rebuild, Canada
print()
print("=" * 78)
print("R3  AUI rebuild; Canada's published 4.4 (July 2026 spotlight, February sample)")
print("=" * 78)
OUT["AUI"] = {}
aui = {}
for w, df in waves.items():
    u = usage[w].reset_index()
    m = u.merge(pop2, on="geo_id", how="left")
    thr = m[(m.usage_count >= 200) & (~m.geo_id.isin(["not_classified", "NONE"])) & m.working_age_pop.notna()].copy()
    # symmetric rule: usage and population both over the thresholded set
    thr["aui"] = (thr.usage_count / thr.usage_count.sum()) / (thr.working_age_pop / thr.working_age_pop.sum())
    # asymmetric (August-2025) rule: usage denominator adds not_classified
    denom_asym = thr.usage_count.sum() + float(m.loc[m.geo_id == "not_classified", "usage_count"].sum())
    thr["aui_asym"] = (thr.usage_count / denom_asym) / (thr.working_age_pop / thr.working_age_pop.sum())
    aui[w] = thr.set_index("geo_id")
    ca = thr[thr.geo_id == "CA"]
    print(f"{w}: N in index {len(thr)}; Canada AUI symmetric {float(ca.aui.iloc[0]):.4f}, "
          f"asymmetric {float(ca.aui_asym.iloc[0]):.4f}; USA {float(thr.loc[thr.geo_id == 'US', 'aui'].iloc[0]):.4f}")
    OUT["AUI"][w] = {"N": int(len(thr)), "CA_sym": float(ca.aui.iloc[0]), "CA_asym": float(ca.aui_asym.iloc[0])}

# ---------------------------------------------------------------- R4 positive control
print()
print("=" * 78)
print("R4  positive control: R4 Fig 3.3 country regression of ln AUI on human education")
print("   published r = 0.359, R2 = 0.129, p < 0.001, beta = 0.75 (Nov 2025 wave)")
print("=" * 78)
OUT["R4_control"] = {}
for w, df in waves.items():
    he = df[(df.geography == "country") & (df.facet == "human_education_years") &
            (df.variable == "human_education_years_mean")].set_index("geo_id").value
    a = aui[w].join(he.rename("human_education"), how="inner").dropna(subset=["human_education"])
    for label, sub in [("all thresholded", a), ("ex-Seychelles", a[a.index != "SC"])]:
        x = np.log(sub.aui.values)
        y = sub.human_education.values
        r = stats.pearsonr(y, x)
        sl = stats.linregress(y, x)          # published beta: ln AUI on education
        sl2 = stats.linregress(x, y)
        print(f"{w} [{label}] N={len(sub)}  r={r[0]:.4f}  R2={r[0]**2:.4f}  p={r[1]:.2e}  "
              f"slope(lnAUI~educ)={sl.slope:.4f}  slope(educ~lnAUI)={sl2.slope:.4f}")
        OUT["R4_control"][f"{w}|{label}"] = {"N": int(len(sub)), "r": float(r[0]), "R2": float(r[0] ** 2),
                                             "p": float(r[1]), "slope_lnaui_on_educ": float(sl.slope),
                                             "slope_educ_on_lnaui": float(sl2.slope)}

# ---------------------------------------------------------------- outcome, sd, Kish, MDE
print()
print("=" * 78)
print("Outcome distribution, Kish effective N and the MDE inputs")
print("=" * 78)
OUT["mde"] = {}
out = {}
for w, df in waves.items():
    p = country_facet(df, "human_only_ability", "human_only_ability_pct")
    c = country_facet(df, "human_only_ability", "human_only_ability_count")
    d = pd.DataFrame({"yes": p.get("yes"), "no": p.get("no"), "nc": p.get("not_classified")})
    d["nc"] = d["nc"].fillna(0.0)
    d["no_renorm"] = 100 * d["no"] / (d["yes"] + d["no"])
    d["n_class"] = c[["yes", "no"]].sum(axis=1, min_count=1)
    d["n_total"] = c.sum(axis=1)
    d = d.loc[[g for g in panel if g in d.index]]
    out[w] = d
    sd = d.no_renorm.std(ddof=1)
    sd_raw = d.no.std(ddof=1)
    wts = d.n_class
    kish = wts.sum() ** 2 / (wts ** 2).sum()
    # count-weighted mean and its MDE
    mean_w = np.average(d.no_renorm, weights=wts)
    # tercile difference MDE (two-sample, equal n per tercile, unweighted)
    n_t = len(d) // 3
    mde_unw = (1.96 + 0.84) * sd * np.sqrt(2 / n_t)
    n_t_eff = kish / 3
    mde_kish = (1.96 + 0.84) * sd * np.sqrt(2 / n_t_eff)
    # binomial sampling sd of a country's own share at the threshold
    se_200 = 100 * np.sqrt(0.12 * 0.88 / 200)
    se_med = 100 * np.sqrt(0.12 * 0.88 / d.n_class.median())
    r_mde = 0.26
    print(f"\n[{w}] panel N={len(d)}")
    print(f"  no (raw, incl not_classified) : mean {d.no.mean():.3f}  sd {sd_raw:.3f}  range [{d.no.min():.2f},{d.no.max():.2f}]")
    print(f"  no (renormalised yes+no base) : mean {d.no_renorm.mean():.3f}  count-weighted {mean_w:.3f}  sd {sd:.3f}  "
          f"range [{d.no_renorm.min():.2f},{d.no_renorm.max():.2f}]")
    print(f"  not_classified share          : mean {d.nc.mean():.3f}  sd {d.nc.std(ddof=1):.3f}  max {d.nc.max():.2f}  "
          f"(non-zero in {(d.nc > 0).sum()} of {len(d)})")
    print(f"  classified counts per country : median {d.n_class.median():.0f}  min {d.n_class.min():.0f}  max {d.n_class.max():.0f}")
    print(f"  Kish effective N (count weights) = {kish:.2f} of {len(d)} nominal")
    print(f"  binomial se of a country's own share at n=200: {se_200:.2f} pp; at the median n: {se_med:.2f} pp")
    print(f"  implied within-country sampling sd vs between-country sd: {se_med:.2f} vs {sd:.2f} pp")
    print(f"  MDE (tercile difference, 80% power, a=0.05): unweighted n/3={n_t} -> {mde_unw:.2f} pp; "
          f"Kish n_eff/3={n_t_eff:.1f} -> {mde_kish:.2f} pp")
    print(f"  detectable correlation at N={len(d)}, 80% power: r ~ {2.8 / np.sqrt(len(d) - 3):.3f}")
    # how much of the between-country variance is sampling noise
    share = d.no_renorm / 100
    var_obs = d.no_renorm.var(ddof=1)
    var_samp = float(np.mean(10000 * share * (1 - share) / d.n_class))
    top3 = wts.sort_values(ascending=False).head(3)
    cap = np.minimum(wts, wts.quantile(0.90))
    kish_cap = cap.sum() ** 2 / (cap ** 2).sum()
    print(f"  variance decomposition: observed {var_obs:.3f} (sd {np.sqrt(var_obs):.3f}) = sampling {var_samp:.3f} "
          f"(sd {np.sqrt(var_samp):.3f}) + true {var_obs - var_samp:.3f} (sd {np.sqrt(max(var_obs - var_samp, 0)):.3f})")
    print(f"  count weights: top-3 hold {100 * top3.sum() / wts.sum():.1f}% ({list(top3.index)}); "
          f"n_eff capped at the 90th pct = {kish_cap:.1f}")
    OUT["mde"][w] = {"N": int(len(d)), "sd_renorm": float(sd), "sd_raw": float(sd_raw),
                     "mean_renorm": float(d.no_renorm.mean()), "mean_weighted": float(mean_w),
                     "kish": float(kish), "mde_unweighted_pp": float(mde_unw), "mde_kish_pp": float(mde_kish),
                     "se_at_200": float(se_200), "se_at_median_n": float(se_med),
                     "nc_mean": float(d.nc.mean()), "nc_nonzero": int((d.nc > 0).sum()),
                     "median_n_class": float(d.n_class.median()),
                     "var_observed": float(var_obs), "var_sampling": float(var_samp),
                     "sd_true": float(np.sqrt(max(var_obs - var_samp, 0))),
                     "top3_weight_share": float(100 * top3.sum() / wts.sum()), "kish_capped_p90": float(kish_cap),
                     "detectable_r": float(2.8 / np.sqrt(len(d) - 3))}

# between-wave rank stability and the raw-vs-renormalised question
a, b = out["nov2025"], out["feb2026"]
j = a.join(b, lsuffix="_nov", rsuffix="_feb", how="inner")
print(f"\nrank stability over {len(j)} panel countries: Spearman(no_renorm) "
      f"{stats.spearmanr(j.no_renorm_nov, j.no_renorm_feb)[0]:.4f}; Pearson {stats.pearsonr(j.no_renorm_nov, j.no_renorm_feb)[0]:.4f}")
print(f"raw vs renormalised within wave: Spearman nov {stats.spearmanr(a.no, a.no_renorm)[0]:.4f}, "
      f"feb {stats.spearmanr(b.no, b.no_renorm)[0]:.4f}")
OUT["stability"] = {"spearman_no_renorm": float(stats.spearmanr(j.no_renorm_nov, j.no_renorm_feb)[0]),
                    "pearson": float(stats.pearsonr(j.no_renorm_nov, j.no_renorm_feb)[0]),
                    "spearman_raw_vs_renorm_nov": float(stats.spearmanr(a.no, a.no_renorm)[0]),
                    "spearman_raw_vs_renorm_feb": float(stats.spearmanr(b.no, b.no_renorm)[0])}

# ---------------------------------------------------------------- T3 shift-share coverage
print()
print("=" * 78)
print("T3 feasibility: shift-share coverage from global onet_task::human_only_ability")
print("=" * 78)
OUT["T3"] = {}
for w, df in waves.items():
    d = df[(df.geography == "global") & (df.facet == "onet_task::human_only_ability")]
    task = d.cluster_name.str.rsplit("::", n=1).str[0]
    arm = d.cluster_name.str.rsplit("::", n=1).str[1]
    dd = d.assign(task=task, arm=arm)
    cnt = dd[dd.variable == "onet_task_human_only_ability_count"].pivot_table(index="task", columns="arm", values="value")
    glob_task = df[(df.geography == "global") & (df.facet == "onet_task") & (df.variable == "onet_task_pct")] \
        .set_index("cluster_name").value
    named = glob_task.drop(index=[i for i in ("none", "not_classified") if i in glob_task.index])
    with_no = cnt.index[cnt["no"].notna()]
    covered_mass = named.reindex(with_no).sum()
    total_named = named.sum()
    no_count_published = cnt["no"].sum()
    no_count_global = float(df[(df.geography == "global") & (df.facet == "human_only_ability") &
                               (df.variable == "human_only_ability_count") & (df.cluster_name == "no")].value.iloc[0])
    print(f"\n[{w}] tasks with a published 'no' cell: {len(with_no)} of {cnt.shape[0]}")
    print(f"  global named-task mass carried by those tasks: {covered_mass:.2f} of {total_named:.2f} named "
          f"({100 * covered_mass / total_named:.1f}% of named mass, {covered_mass:.2f}% of all conversations)")
    print(f"  'no' conversations visible at task level: {no_count_published:.0f} of the global {no_count_global:.0f} "
          f"({100 * no_count_published / no_count_global:.1f}%)")
    print(f"  min published intersection cell count: {np.nanmin(cnt.values):.0f}")
    # country-level coverage of the shift-share: country named mix x tasks with a no arm
    ct = df[(df.geography == "country") & (df.facet == "onet_task") & (df.variable == "onet_task_pct")]
    ct = ct[~ct.cluster_name.isin(["none", "not_classified"])]
    ct = ct[ct.geo_id.isin(panel)]
    cov = ct.assign(has=ct.cluster_name.isin(set(with_no))).groupby("geo_id").apply(
        lambda g: pd.Series({"named": g.value.sum(), "covered": g.loc[g.has, "value"].sum()}), include_groups=False)
    print(f"  per-country conversations covered by the shift-share (country mix x task with a 'no' cell): "
          f"median {cov.covered.median():.2f}% of all conversations, min {cov.covered.min():.2f}%, "
          f"max {cov.covered.max():.2f}%; as a share of that country's NAMED mass median "
          f"{(100 * cov.covered / cov.named).median():.1f}%")
    OUT["T3"][w] = {"tasks_total": int(cnt.shape[0]), "tasks_with_no": int(len(with_no)),
                    "named_mass_covered": float(covered_mass), "named_mass_total": float(total_named),
                    "no_count_visible": float(no_count_published), "no_count_global": float(no_count_global),
                    "country_covered_median_pct": float(cov.covered.median()),
                    "country_covered_min_pct": float(cov.covered.min()),
                    "country_covered_share_of_named_median": float((100 * cov.covered / cov.named).median())}

print()
print("=" * 78)
print("T3 alternative: shift-share on request::human_only_ability level 2 x country request L2 mix")
print("=" * 78)
OUT["T3_request_L2"] = {}
l2names = {}
for w, df in waves.items():
    g = df[(df.facet == "request::human_only_ability") & (df.geography == "global") & (df.level == "2") &
           (df.variable == "request_human_only_ability_count")]
    node = g.cluster_name.str.rsplit("::", n=1).str[0]
    arm = g.cluster_name.str.rsplit("::", n=1).str[1]
    piv = g.assign(n=node, a=arm).pivot_table(index="n", columns="a", values="value")
    rate = (100 * piv["no"] / (piv["yes"] + piv["no"])).dropna()
    l2names[w] = set(piv.index)
    c = df[(df.geography == "country") & (df.facet == "request") & (df.variable == "request_pct") &
           (df.level == "2") & (df.geo_id.isin(panel))].copy()
    c = c[~c.cluster_name.isin(["none", "not_classified"])]
    c["has"] = c.cluster_name.isin(set(rate.index))
    cov = c.groupby("geo_id").apply(lambda g: pd.Series({"named": g.value.sum(), "cov": g.loc[g.has, "value"].sum()}),
                                    include_groups=False)
    print(f"[{w}] {len(rate)} global L2 nodes with a no-rate (spread {rate.min():.1f}-{rate.max():.1f} pp); "
          f"country L2 rows matching a global node: {100 * c.has.mean():.1f}%")
    print(f"  per-country conversations covered: median {cov['cov'].median():.1f}%, min {cov['cov'].min():.1f}%, "
          f"over {len(cov)} of {len(panel)} panel countries")
    OUT["T3_request_L2"][w] = {"nodes_with_rate": int(len(rate)), "rate_min": float(rate.min()),
                               "rate_max": float(rate.max()), "panel_countries": int(len(cov)),
                               "covered_median_pct": float(cov["cov"].median()),
                               "covered_min_pct": float(cov["cov"].min())}
shared = l2names["nov2025"] & l2names["feb2026"]
print(f"request L2 node names shared across the two waves: {len(shared)} of {len(l2names['nov2025'])} and "
      f"{len(l2names['feb2026'])} -> each wave's adjustment is internal to that wave")
OUT["T3_request_L2"]["shared_names_across_waves"] = len(shared)

print()
print("=" * 78)
print("Covariate coverage at country grain over the panel")
print("=" * 78)
OUT["covariates"] = {}
for w, df in waves.items():
    c = df[df.geography == "country"]
    rec = {}
    for facet, var in [("human_only_time", "human_only_time_mean"),
                       ("human_education_years", "human_education_years_mean"),
                       ("ai_autonomy", "ai_autonomy_mean"), ("multitasking", "multitasking_pct"),
                       ("task_success", "task_success_pct"), ("use_case", "use_case_pct")]:
        d = c[(c.facet == facet) & (c.variable == var)]
        rec[f"{facet}.{var}"] = len(set(d.geo_id) & set(panel))
    print(w, rec, f"(panel = {len(panel)})")
    OUT["covariates"][w] = rec

with open("data/replication/results/post5_replication_and_mde.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\nwrote data/replication/results/post5_replication_and_mde.json")
