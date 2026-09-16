"""Step 13 (exploratory): WHICH collaboration pattern moves with education and access?
For each of the five patterns, the country's share of classified conversations in that pattern (Aug 2025), residualised on the
task-mix-expected automation share (so task composition is held constant the same way as the main outcome), regressed on
standardised tertiary enrolment, internet users, log income, plus the usual controls. Coefficients in points of share per SD."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, statsmodels.api as sm, json
d=pd.read_csv("data/processed/11_unbundle_table.csv")
col=pd.read_csv("data/processed/01_collab_by_country_thresholded.csv"); col=col[col.wave=="2025-08"]
five=["directive","feedback loop","task iteration","learning","validation"]
col["classified"]=col[five].sum(axis=1)
for p in five: col[p+"_c"]=col[p]/col.classified*100
d=d.merge(col[["geo_id"]+[p+"_c" for p in five]], on="geo_id", how="left")
dd=d.dropna(subset=["expected","aui","coding_share","personal_share","lang_group","tertiary","internet","log_gdp"]+[p+"_c" for p in five]).copy()
small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
for c in ["tertiary","internet","log_gdp"]: dd["z_"+c]=(dd[c]-dd[c].mean())/dd[c].std(ddof=0)
res={}; print(f"N = {len(dd)}  (coefficients: points of pattern share per SD; interval)")
print(f"{'pattern':16s} {'mean share':>10s} | {'tertiary':>22s} | {'internet':>22s} | {'log income':>22s}")
for p in five:
    y=p+"_c"; dd["y_resid"]=sm.OLS(dd[y],sm.add_constant(dd.expected)).fit().resid     # hold task mix constant
    m=smf.ols("y_resid ~ z_tertiary + z_internet + z_log_gdp + aui + coding_share + personal_share + C(lang_group)",data=dd).fit(cov_type="HC3")
    row={}
    for k in ["z_tertiary","z_internet","z_log_gdp"]:
        lo,hi=m.conf_int().loc[k]; row[k]=(round(m.params[k],2),round(lo,2),round(hi,2))
    res[p]={"mean_share":round(dd[y].mean(),1),**{k:v for k,v in row.items()}}
    f=lambda k: f"{row[k][0]:+.2f} [{row[k][1]:+.2f},{row[k][2]:+.2f}]"
    print(f"{p:16s} {dd[y].mean():10.1f} | {f('z_tertiary'):>22s} | {f('z_internet'):>22s} | {f('z_log_gdp'):>22s}")
json.dump(res, open("data/processed/13_which_pattern.json","w"), indent=1); print("CHECK OK")
