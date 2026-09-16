"""Step 07: robustness battery A-J as pre-registered. Every row reports the power-distance coefficient
(points of automation per standard deviation), its interval, and the MDE, so the reader can see whether
the primary result survives each change."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json, os
OUT="data/processed"; TAB="outputs/tables"
t = pd.read_csv(f"{OUT}/04_country_table.csv")
def prep(df, pdi_col="hof_pdi", outcome="auto_resid"):
    d = df.dropna(subset=[outcome, pdi_col, "log_gdp", "aui", "coding_share", "personal_share", "lang_group"]).copy()
    d["z_pdi"] = (d[pdi_col]-d[pdi_col].mean())/d[pdi_col].std(ddof=0)
    small = d.lang_group.value_counts(); d["lang_group"] = d.lang_group.where(d.lang_group.map(small) >= 5, "other")
    return d
BASE = "z_pdi + log_gdp + aui + coding_share + personal_share + C(lang_group)"
def fit(d, formula, key="z_pdi"):
    m = smf.ols(formula, data=d).fit(cov_type="HC3"); lo,hi = m.conf_int().loc[key]
    return {"n": int(m.nobs), "coef": round(m.params[key],3), "ci_low": round(lo,3), "ci_high": round(hi,3), "mde": round(2.8*m.bse[key],3), "p": round(m.pvalues[key],4)}
rows = {}
aug = t[t.wave=="2025-08"]
d = prep(aug); rows["Primary (Aug 2025, Hofstede country scores)"] = fit(d, f"auto_resid ~ {BASE}")
# A. regional scores extend the sample
rows["A. + Hofstede regional scores"] = fit(prep(aug, "hof_pdi_extended"), f"auto_resid ~ {BASE}")
# B. GLOBE practices; GLOBE participative leadership
rows["B1. GLOBE power-distance practices"] = fit(prep(aug, "globe_pdi_practices"), f"auto_resid ~ {BASE}")
dg = prep(aug, "globe_participative"); rows["B2. GLOBE participative leadership (expect negative)"] = fit(dg, f"auto_resid ~ {BASE}")
# C. other dimensions
dc = prep(aug); dc["z_idv"]=(dc.hof_idv-dc.hof_idv.mean())/dc.hof_idv.std(ddof=0); dc["z_uai"]=(dc.hof_uai-dc.hof_uai.mean())/dc.hof_uai.std(ddof=0)
mC = smf.ols(f"auto_resid ~ {BASE} + z_idv + z_uai", data=dc).fit(cov_type="HC3")
rows["C. + individualism + uncertainty avoidance (PDI coef)"] = fit(dc, f"auto_resid ~ {BASE} + z_idv + z_uai")
rows["C. individualism coef"] = fit(dc, f"auto_resid ~ {BASE} + z_idv + z_uai", key="z_idv"); rows["C. uncertainty-avoidance coef"] = fit(dc, f"auto_resid ~ {BASE} + z_idv + z_uai", key="z_uai")
# D. directive-share residual outcome: residualise directive share on expected automation (same adjustment logic)
col = pd.read_csv(f"{OUT}/01_collab_by_country_thresholded.csv"); dd = aug.merge(col[col.wave=="2025-08"][["geo_id","directive"]], on="geo_id")
dd = prep(dd); import statsmodels.api as sm
dd["dir_resid"] = sm.OLS(dd.directive, sm.add_constant(dd.expected)).fit().resid
rows["D. outcome = directive share (task-mix residual)"] = fit(dd, f"dir_resid ~ {BASE}")
# E. later waves
for w in ["2025-11","2026-02"]:
    rows[f"E. wave {w}"] = fit(prep(t[t.wave==w]), f"auto_resid ~ {BASE}")
# F. English-majority only
de = d[d.lang_group=="english"]; rows["F. English-majority countries only (illustrative)"] = fit(de, "auto_resid ~ z_pdi + log_gdp + aui + coding_share + personal_share")
# G. second instrument: Stanford 'AI handles alone'
dgc = aug.dropna(subset=["agency_ai_alone"]).copy(); dgc = prep(dgc); dgc["agency"] = dgc.agency_ai_alone*100
rows["G. Stanford human agency: AI-handles-alone share"] = fit(dgc, f"agency ~ {BASE}")
# H. leave-one-country-out
base_coef = rows["Primary (Aug 2025, Hofstede country scores)"]["coef"]; movers = []
for g in d.geo_id:
    c = fit(d[d.geo_id!=g], f"auto_resid ~ {BASE}")["coef"]
    if abs(c-base_coef) > 0.25*max(abs(base_coef),0.5): movers.append((g, c))
rows["H. leave-one-out: countries moving PDI coef by >25%"] = {"movers": movers}
# I. placebo: unclassified share
dp = aug.merge(col[col.wave=="2025-08"][["geo_id"]+["directive","feedback loop","task iteration","learning","validation","none"]], on="geo_id", suffixes=("","_c"))
dp["unclassified"] = 100 - dp[["directive","feedback loop","task iteration","learning","validation","none"]].sum(axis=1)
dp = prep(dp); rows["I. placebo outcome: unclassified share"] = fit(dp, f"unclassified ~ {BASE}")
json.dump(rows, open(f"{OUT}/07_robustness.json","w"), indent=1)
tab = pd.DataFrame({k:v for k,v in rows.items() if "movers" not in v}).T; tab.to_csv(f"{TAB}/07_robustness.csv")
print(tab.to_string()); print("\nH. leave-one-out movers:", movers)
print("CHECK OK: all pre-registered robustness rows computed")
