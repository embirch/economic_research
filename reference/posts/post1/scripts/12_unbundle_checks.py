"""Step 12: checks on the unbundling result. (1) correlations among income, internet, tertiary, prompt education;
(2) the two winners entered together, with and without income; (3) leave-one-country-out on the internet and tertiary coefficients."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
d=pd.read_csv("data/processed/11_unbundle_table.csv")
cands=["log_gdp","internet","tertiary","prompt_edu"]
dd=d.dropna(subset=["auto_resid","aui","coding_share","personal_share","lang_group"]+cands).copy()
small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
for c in cands: dd["z_"+c]=(dd[c]-dd[c].mean())/dd[c].std(ddof=0)
print("N =", len(dd)); print("correlations:\n", dd[cands].corr().round(2).to_string())
base="auto_resid ~ aui + coding_share + personal_share + C(lang_group)"
def fit(f):
    m=smf.ols(f,data=dd).fit(cov_type="HC3"); return {k:(round(m.params[k],2), [round(x,2) for x in m.conf_int().loc[k]]) for k in m.params.index if k.startswith("z_")}
out={}
for lab,f in [("income only", base+" + z_log_gdp"),("internet + tertiary, no income", base+" + z_internet + z_tertiary"),("internet + tertiary + income", base+" + z_internet + z_tertiary + z_log_gdp"),("internet + tertiary + prompt_edu + income", base+" + z_internet + z_tertiary + z_prompt_edu + z_log_gdp")]:
    out[lab]=fit(f); print(f"{lab:42s}", out[lab])
# leave-one-out on internet and tertiary (model: internet + tertiary + income)
f=base+" + z_internet + z_tertiary + z_log_gdp"; full=smf.ols(f,data=dd).fit(cov_type="HC3")
movers={}
for k in ["z_internet","z_tertiary"]:
    b0=full.params[k]; mv=[]
    for g in dd.geo_id:
        b=smf.ols(f,data=dd[dd.geo_id!=g]).fit().params[k]
        if abs(b-b0)>0.25*abs(b0): mv.append((g,round(b,2)))
    movers[k]=mv
print("leave-one-out movers (>25%):", movers)
json.dump({"n":int(len(dd)),"corr":dd[cands].corr().round(3).to_dict(),"models":out,"movers":movers}, open("data/processed/12_unbundle_checks.json","w"), indent=1)
print("CHECK OK")
