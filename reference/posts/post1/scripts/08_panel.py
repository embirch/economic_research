"""Step 08: the within-country test (H2 cohort vs H3 development) and the Super Bowl natural experiment.

What this does
  1. Panel: the same countries across five waves. Country fixed effects remove everything constant about a
     country (its culture, language, income level); wave fixed effects remove anything that changed for every
     country at once (a new classifier, the June population change). What is left is within-country movement:
     does a country's task-mix-adjusted automation move with its own adoption?
       cohort predicts +, development predicts -, culture predicts ~0.
     Standard errors clustered by country. Run with and without the two June 2026 waves.
  2. Super Bowl: change in US auto_resid from Nov 2025 to Feb 2026 minus the mean change over the
     pre-registered comparators (CAN, GBR, AUS, IRL, NZL). Cohort predicts the US rises more than
     one comparator standard deviation above the comparator mean.
Caveat printed with the result: adoption moves little within a country over nine months, so this test is
suggestive; the write-up says so.
"""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"
d = pd.read_csv(f"{OUT}/03_partial_by_wave.csv")
res = {}
def panel(df, label):
    df = df.copy()
    keep = df.groupby("geo_id").wave.transform("nunique") >= 3          # countries observed in at least three waves
    df = df[keep]
    m = smf.ols("auto_resid ~ aui + C(geo_id) + C(wave)", data=df).fit(cov_type="cluster", cov_kwds={"groups": df["geo_id"]})
    lo, hi = m.conf_int().loc["aui"]
    within_sd = df.groupby("geo_id").aui.std().mean()
    r = {"n_obs": int(m.nobs), "n_countries": int(df.geo_id.nunique()), "coef_aui": round(m.params["aui"],3), "ci": [round(lo,3), round(hi,3)],
         "p": round(m.pvalues["aui"],4), "mde": round(2.8*m.bse["aui"],3), "mean_within_country_sd_of_aui": round(within_sd,3)}
    print(f"{label}: N={r['n_obs']} obs, {r['n_countries']} countries; within-country coef on AUI = {r['coef_aui']} [{lo:.3f}, {hi:.3f}], p={r['p']}, MDE {r['mde']}; typical within-country movement of AUI = {within_sd:.2f} index points")
    return r
res["panel_all_waves"] = panel(d, "Panel, all five waves")
res["panel_excl_june"] = panel(d[~d.wave.isin(["2026-04","2026-05"])], "Panel, excluding June 2026")
# Super Bowl
w = d.pivot_table(index="geo_id", columns="wave", values="auto_resid")
chg = (w["2026-02"] - w["2025-11"]).dropna()
comp = ["CAN","GBR","AUS","IRL","NZL"]; us = chg.get("USA"); cm = chg.reindex(comp)
res["superbowl"] = {"us_change": round(float(us),3), "comparators": {k: round(float(v),3) for k,v in cm.items()}, "comparator_mean": round(float(cm.mean()),3), "comparator_sd": round(float(cm.std()),3),
                    "us_minus_mean": round(float(us-cm.mean()),3), "cohort_supported": bool(us - cm.mean() > cm.std())}
print(f"Super Bowl test: US change Nov->Feb = {us:+.2f} points; comparators mean {cm.mean():+.2f} (sd {cm.std():.2f}); US minus mean = {us-cm.mean():+.2f} -> cohort {'SUPPORTED' if res['superbowl']['cohort_supported'] else 'NOT supported'} by the pre-registered rule")
print("  comparators:", res["superbowl"]["comparators"])
json.dump(res, open(f"{OUT}/08_panel.json","w"), indent=1)
assert res["panel_all_waves"]["n_countries"] > 80 and all(k in chg.index for k in comp+["USA"])
print("CHECK OK: panel fitted on countries seen in >=3 waves; all comparators present")
