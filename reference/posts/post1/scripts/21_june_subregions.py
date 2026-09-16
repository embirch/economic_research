"""Step 21: (A) the US-state test repeated on the April and May 2026 waves (pre-registered robustness of step 20, same models);
(B) exploratory, not pre-registered: within-country tests across all published subregions (ISO 3166-2 units, 128 countries):
does a subregion's own adoption, or its personal-use share, predict adjusted delegation once its country is held fixed?
Adjustment: O*NET task nodes (level 0) x global per-node automation rates, exactly as step 03 does for June countries."""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"; ANOMALY_CAP=25.0
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,
               usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_external_id","node_name"])
v6["value"]=pd.to_numeric(v6.value,errors="coerce")
def z(x): return (x-x.mean())/x.std(ddof=0)
census=pd.read_csv(f"{OUT}/20_census_states.csv",index_col=0)[["bachelors_plus","broadband","log_gdp"]]   # all 51 states, built in step 20
res={"A_us_states":{},"B_within_country":{}}
frames=[]
for ds,wave in [("2026-04-01","2026-04"),("2026-05-01","2026-05")]:
    m=v6[v6.date_start==ds]; ov=m[(m.geo_level=="subregion")&(m.category_name=="overall")]
    piv=ov.pivot_table(index="geo_id",columns="metric_id",values="value")
    on=m[(m.category_name=="onet")&(m.hierarchy_level.astype(str)=="0")]
    tasks=on[(on.geo_level=="subregion")&(on.metric_id=="pct")].rename(columns={"node_external_id":"task","value":"w"})[["geo_id","task","w"]]
    rates=on[(on.geo_level=="global")&(on.metric_id=="collaboration_bucket_automation_pct")].set_index("node_external_id")["value"]
    t=tasks[tasks.task.isin(rates.index)].copy(); t["r"]=t.task.map(rates)
    exp=t.groupby("geo_id").apply(lambda x:(x.w*x.r).sum()/x.w.sum(),include_groups=False).rename("expected")
    soc=m[(m.geo_level=="subregion")&(m.category_name=="soc_occupation")&(m.metric_id=="pct")&(m.node_name=="Computer and Mathematical")].set_index("geo_id")["value"].rename("coding_share")
    p=piv.rename(columns={"collaboration_bucket_automation_pct":"automation","usage_per_capita_index":"aui","use_case_personal_pct":"personal_share","human_education_years_mean":"prompt_education"})
    d=pd.concat([p[["automation"]],exp],axis=1,join="inner").join(p[["aui","personal_share","prompt_education"]]).join(soc)
    bad=d[d.aui>ANOMALY_CAP]
    if len(bad): print(f"  {wave}: EXCLUDED subregions with index > {ANOMALY_CAP}:", bad.aui.round(0).to_dict())
    d=d[~(d.aui>ANOMALY_CAP)]; d["auto_resid"]=sm.OLS(d.automation,sm.add_constant(d.expected)).fit().resid
    print(f"  {wave}: {len(d)} subregions with automation and task mix; usage index published for {d.aui.notna().sum()} (US states only)")
    d["country"]=d.index.str[:2]; d["wave"]=wave; frames.append(d)
    # ---- (A) US states
    us=d[d.country=="US"].copy(); us.index=us.index.str[3:]; us=us.join(census,how="inner")
    us["auto_resid"]=sm.OLS(us.automation,sm.add_constant(us.expected)).fit().resid   # residualised within the states, as Anthropic's function does for states (step 20); part B uses the pooled residual
    for v in ["bachelors_plus","log_gdp","broadband","coding_share","personal_share"]: us["z_"+v]=z(us[v])
    out={}
    for k,f in {"(1) education alone":"auto_resid ~ z_bachelors_plus","(2) education + log income":"auto_resid ~ z_bachelors_plus + z_log_gdp",
                "(3) full":"auto_resid ~ z_bachelors_plus + z_log_gdp + z_broadband + aui + z_coding_share + z_personal_share","income alone":"auto_resid ~ z_log_gdp","personal alone":"auto_resid ~ z_personal_share"}.items():
        mo=smf.ols(f,data=us).fit(cov_type="HC3"); terms={}
        for term in mo.params.index[1:]:
            lo,hi=mo.conf_int().loc[term]; terms[term.replace("z_","")]={"coef":round(mo.params[term],2),"ci":[round(lo,2),round(hi,2)],"mde":round(2.8*mo.bse[term],2)}
        out[k]={"n":int(mo.nobs),"r2":round(mo.rsquared,2),"terms":terms}
    res["A_us_states"][wave]=out
    print(f"\n(A) US states, {wave}: N={len(us)}  [all 51 published; no threshold information in the June file]")
    # the same on the 43 states that passed the August 2025 threshold, so the waves compare like for like
    us43=us[us.index.isin(pd.read_csv(f"{OUT}/20_us_states.csv",index_col=0).index)].copy(); us43["z_bachelors_plus"]=z(us43.bachelors_plus)
    mo=smf.ols("auto_resid ~ z_bachelors_plus",data=us43).fit(cov_type="HC3"); lo,hi=mo.conf_int().loc["z_bachelors_plus"]
    res["A_us_states"][wave]["(1) on the 43 August states"]={"n":int(mo.nobs),"r2":round(mo.rsquared,2),"terms":{"bachelors_plus":{"coef":round(mo.params["z_bachelors_plus"],2),"ci":[round(lo,2),round(hi,2)]}}}
    for k,v in out.items(): print(f"  {k:26s} R2={v['r2']:.2f}  "+"  ".join(f"{tn} {tv['coef']:+.2f} [{tv['ci'][0]:+.2f},{tv['ci'][1]:+.2f}]" for tn,tv in v['terms'].items()))
allsub=pd.concat(frames); allsub.to_csv(f"{OUT}/21_subregions.csv")
# ---- (B) within-country, all subregions (exploratory)
print("\n(B) Within-country across subregions (country fixed effects, SEs clustered by country), exploratory:")
for wave in ["2026-04","2026-05"]:
    d=allsub[allsub.wave==wave].copy(); cnt=d.groupby("country").size(); d=d[d.country.map(cnt)>=3]
    out={}
    for k,f in {"personal share":"auto_resid ~ personal_share + C(country)","coding share":"auto_resid ~ coding_share + C(country)","prompt education (years)":"auto_resid ~ prompt_education + C(country)","all three":"auto_resid ~ personal_share + coding_share + prompt_education + C(country)"}.items():
        dd=d.dropna(subset=[c for c in ["personal_share","coding_share","prompt_education"] if c in f]+["auto_resid"]); mo=smf.ols(f,data=dd).fit(cov_type="cluster",cov_kwds={"groups":pd.factorize(dd.country)[0]}); terms={}
        for term in [x for x in mo.params.index if not x.startswith("C(") and x!="Intercept"]:
            lo,hi=mo.conf_int().loc[term]; terms[term]={"coef":round(mo.params[term],3),"ci":[round(lo,3),round(hi,3)]}
        out[k]={"n":int(mo.nobs),"countries":int(d.country.nunique()),"terms":terms}
    res["B_within_country"][wave]=out
    print(f"  {wave}: {len(d)} subregions in {d.country.nunique()} countries (>=3 subregions each); mean within-country SD: personal share {d.groupby('country').personal_share.std().mean():.1f} pts, prompt education {d.groupby('country').prompt_education.std().mean():.2f} yrs")
    for k,v in out.items(): print(f"    {k:22s} "+"  ".join(f"{tn} {tv['coef']:+.3f} [{tv['ci'][0]:+.3f},{tv['ci'][1]:+.3f}]" for tn,tv in v['terms'].items()))
    # the same across countries in the same month, for scale
    c=d.groupby("country").agg(auto_resid=("auto_resid","mean"),personal_share=("personal_share","mean"),prompt_education=("prompt_education","mean"))
    for v in ["personal_share","prompt_education"]:
        mo=smf.ols(f"auto_resid ~ {v}",data=c).fit(cov_type="HC3"); print(f"    for scale, between countries (subregion means, N={len(c)}): {v} {mo.params[v]:+.3f} [{mo.conf_int().loc[v,0]:+.3f},{mo.conf_int().loc[v,1]:+.3f}]")
        res["B_within_country"][wave]["between_"+v]=round(mo.params[v],3)
json.dump(res,open(f"{OUT}/21_june_subregions.json","w"),indent=1)
assert all(res["A_us_states"][w]["(1) education alone"]["n"]>=40 for w in res["A_us_states"]); print("CHECK OK")
