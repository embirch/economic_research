"""Step 20 (pre-registered, addendum 3): the within-country test. Does the income/education gradient in delegation reappear
across US states, where language, product, pricing, classifier and national culture are constant?
Outcome: task-mix-adjusted automation share by state from Anthropic's own function (geography="state_us"), Aug 2025.
Predictors: log GDP per working-age adult (Anthropic's state file), bachelor's-or-higher share of adults 25+ (ACS 2023 1-yr B15003),
broadband subscription share of households (ACS 2023 1-yr B28002), state Usage Index, computer/math share of conversations."""
import re, pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf, json
RAW="data/raw/release_2025_09_15"; OUT="data/processed"
src=open(f"{RAW}/code/aei_analysis_functions_claude_ai.py").read()
def grab(name, stop):
    s=src.index(f"def {name}("); return src[s:src.index(stop,s)]
core=grab("collaboration_task_regression","    # Create visualization")+"    return df_regression, partial_slope, partial_r2, partial_p, n_tasks\n"
ns={"pd":pd,"np":np,"sm":sm,"MIN_OBSERVATIONS_COUNTRY":200,"MIN_OBSERVATIONS_US_STATE":100}
exec(grab("filter_df","\ndef get_filtered_geographies")+"\n"+grab("get_filtered_geographies","\ndef ")+"\n"+core, ns)
df=pd.read_csv(f"{RAW}/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv",keep_default_na=False,low_memory=False); df["value"]=pd.to_numeric(df.value,errors="coerce")
reg,slope,r2,p,nt=ns["collaboration_task_regression"](df,geography="state_us")
print(f"(0) Anthropic's function on states: AUI partial slope {slope:+.3f}, R2 {r2:.3f}, p {p:.3f}, states {len(reg)}, tasks {nt}   [report: 'not significant across US states']")
for drop in (["UT"],["DC"],["UT","DC"]):
    r_,s_,r2_,p_,_=ns["collaboration_task_regression"](df[~df.geo_id.isin(drop)],geography="state_us")
    print(f"    same function without {'+'.join(drop)}: slope {s_:+.3f}, R2 {r2_:.3f}, p {p_:.3f}, states {len(r_)}")
reg=reg.set_index("geo_id")
# ---- state covariates from the file
st=df[df.geography=="state_us"]
def var(v): return st[(st.facet=="state_us")&(st.variable==v)].set_index("geo_id")["value"]
coding=st[(st.facet=="soc_occupation")&(st.cluster_name=="Computer and Mathematical")].set_index("geo_id")["value"].rename("coding_share")
directive=st[(st.facet=="collaboration")&(st.variable=="collaboration_pct")&(st.cluster_name=="directive")].set_index("geo_id")["value"]
classified=st[(st.facet=="collaboration")&(st.variable=="collaboration_pct")&(~st.cluster_name.isin(["not_classified","none"]))].groupby("geo_id")["value"].sum()
directive=(directive/classified*100).rename("directive")          # same base as automation_pct (share of the five classified patterns)
# ---- Census ACS 2023 1-year, table-based summary files (state rows: GEO_ID 0400000USff)
FIPS={"01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY"}
def acs(table):
    d=pd.read_csv(f"data/raw/census/acsdt1y2023-{table}.dat",sep="|",dtype=str); d=d[d.GEO_ID.str.startswith("0400000US")].copy()
    d["geo_id"]=d.GEO_ID.str[-2:].map(FIPS); d=d.dropna(subset=["geo_id"]).set_index("geo_id")
    return d.apply(pd.to_numeric,errors="coerce")
e=acs("b15003"); bach=((e.B15003_E022+e.B15003_E023+e.B15003_E024+e.B15003_E025)/e.B15003_E001*100).rename("bachelors_plus")
i=acs("b28002"); broadband=(i.B28002_E004/i.B28002_E001*100).rename("broadband")
m=acs("b19013"); medinc=m.B19013_E001.rename("median_hh_income")
pd.concat([bach,broadband,medinc,np.log(var("gdp_per_working_age_capita")).rename("log_gdp")],axis=1).to_csv(f"{OUT}/20_census_states.csv")   # all 51, for step 21
t=pd.concat([reg[["automation_pct","expected_automation_pct","automation_residuals","usage_per_capita_index"]].rename(columns={"automation_residuals":"auto_resid","usage_per_capita_index":"aui"}),
             np.log(var("gdp_per_working_age_capita")).rename("log_gdp"),coding,directive,bach,broadband,medinc],axis=1,join="inner")
t["directive_resid"]=sm.OLS(t.directive,sm.add_constant(t.expected_automation_pct)).fit().resid
print(f"merged states: {len(t)} (Anthropic threshold leaves {len(reg)} of 51); missing after merge:", sorted(set(reg.index)-set(t.index)))
print("excluded by Anthropic's 100-conversation rule:", sorted(set(var("usage_count").index)-set(reg.index)))
print("ranges: bachelors %.1f-%.1f  broadband %.1f-%.1f  log_gdp %.2f-%.2f  aui %.2f-%.2f" % (t.bachelors_plus.min(),t.bachelors_plus.max(),t.broadband.min(),t.broadband.max(),t.log_gdp.min(),t.log_gdp.max(),t.aui.min(),t.aui.max()))
print("Spot check, Census series before merge: Massachusetts bachelors %.1f (published ~47), Mississippi %.1f (~24), DC %.1f (~66)" % (bach["MA"],bach["MS"],bach["DC"]))
print("correlations:"); print(t[["auto_resid","bachelors_plus","log_gdp","broadband","aui","coding_share"]].corr().round(2).to_string())
def z(x): return (x-x.mean())/x.std(ddof=0)
for v in ["bachelors_plus","log_gdp","broadband","coding_share"]: t["z_"+v]=z(t[v])
t.to_csv(f"{OUT}/20_us_states.csv")
res={"anthropic_state_slope":{"slope":round(slope,3),"r2":round(r2,3),"p":round(p,4),"n":int(len(reg))}}
def fit(formula,d=t,tag=None):
    m=smf.ols(formula,data=d).fit(cov_type="HC3"); return m
specs={"(1) education alone":"auto_resid ~ z_bachelors_plus","(2) education + log income":"auto_resid ~ z_bachelors_plus + z_log_gdp",
       "(3) full":"auto_resid ~ z_bachelors_plus + z_log_gdp + z_broadband + aui + z_coding_share","(2b) income alone":"auto_resid ~ z_log_gdp","(2c) broadband alone":"auto_resid ~ z_broadband"}
print("\nPre-registered models (HC3), coefficient per SD [95% CI]:")
for k,f in specs.items():
    m=fit(f); row={}
    for term in m.params.index:
        if term=="Intercept": continue
        lo,hi=m.conf_int().loc[term]; row[term]={"coef":round(m.params[term],2),"ci":[round(lo,2),round(hi,2)],"mde":round(2.8*m.bse[term],2)}
    res[k]={"n":int(m.nobs),"r2":round(m.rsquared,3),"terms":row}
    print(f"  {k:28s} N={int(m.nobs)} R2={m.rsquared:.2f}  "+"  ".join(f"{term.replace('z_','')} {v['coef']:+.2f} [{v['ci'][0]:+.2f},{v['ci'][1]:+.2f}]" for term,v in row.items()))
full=fit(specs["(3) full"]); e_full=res["(3) full"]["terms"]["z_bachelors_plus"]
print(f"  MDE for education in (3): {e_full['mde']:.2f}")
# ---- decision rule
e1=res["(1) education alone"]["terms"]["z_bachelors_plus"]
reappears = e1["coef"]<0 and e1["ci"][1]<0 and e_full["coef"]<0 and e_full["ci"][1]<0
inside_mde = abs(e_full["coef"])<e_full["mde"]
verdict="REAPPEARS" if reappears else ("DOES NOT REAPPEAR (inside MDE)" if inside_mde else "INCONCLUSIVE")
if e1["coef"]>0 and e1["ci"][0]>0: verdict+=" ; NOTE sign is POSITIVE and clear of zero in (1)"
print("Decision:", verdict); res["verdict"]=verdict
# ---- robustness fixed in advance
print("\nRobustness (full model, education coefficient):")
rob={}
for k,d in {"drop DC":t.drop("DC",errors="ignore"),"drop Utah":t.drop("UT",errors="ignore"),"drop DC and Utah":t.drop(["DC","UT"],errors="ignore")}.items():
    for v in ["bachelors_plus","log_gdp","broadband","coding_share"]: d=d.assign(**{"z_"+v:z(d[v])})
    m=fit(specs["(3) full"],d); lo,hi=m.conf_int().loc["z_bachelors_plus"]; rob[k]=[round(m.params["z_bachelors_plus"],2),round(lo,2),round(hi,2)]; print(f"  {k:20s} {m.params['z_bachelors_plus']:+.2f} [{lo:+.2f},{hi:+.2f}]  income {m.params['z_log_gdp']:+.2f}  aui {m.params['aui']:+.2f}")
for k,d in {"drop Utah, education alone":t.drop("UT"),"drop Utah and DC, education alone":t.drop(["UT","DC"])}.items():
    d=d.assign(z_bachelors_plus=z(d.bachelors_plus)); m=fit("auto_resid ~ z_bachelors_plus",d); lo,hi=m.conf_int().loc["z_bachelors_plus"]; rob[k]=[round(m.params["z_bachelors_plus"],2),round(lo,2),round(hi,2)]; print(f"  {k:34s} {m.params['z_bachelors_plus']:+.2f} [{lo:+.2f},{hi:+.2f}]  R2 {m.rsquared:.2f}   (Utah's residual is +{t.loc['UT','auto_resid']:.0f} points)")
for k,f in {"directive outcome (adjusted)":"directive_resid ~ z_bachelors_plus + z_log_gdp + z_broadband + aui + z_coding_share","unadjusted automation":"automation_pct ~ z_bachelors_plus + z_log_gdp + z_broadband + aui + z_coding_share"}.items():
    m=fit(f); lo,hi=m.conf_int().loc["z_bachelors_plus"]; rob[k]=[round(m.params["z_bachelors_plus"],2),round(lo,2),round(hi,2)]; print(f"  {k:28s} {m.params['z_bachelors_plus']:+.2f} [{lo:+.2f},{hi:+.2f}]  income {m.params['z_log_gdp']:+.2f}  aui {m.params['aui']:+.2f}")
loo=[]
for g in t.index:
    d=t.drop(g); m=fit(specs["(3) full"],d); loo.append((g,m.params["z_bachelors_plus"]))
base=full.params["z_bachelors_plus"]; movers=[(g,round(v,2)) for g,v in loo if abs(v-base)>0.25*abs(base)]
print(f"  leave-one-out: education ranges {min(v for _,v in loo):+.2f} to {max(v for _,v in loo):+.2f}; states moving it >25%: {movers}")
rob["loo_range"]=[round(min(v for _,v in loo),2),round(max(v for _,v in loo),2)]; rob["loo_movers"]=movers; res["robustness"]=rob
# ---- for comparison: what the same three orderings give across countries (from step 11/12 outputs)
# ---- like-for-like across countries: same simple models on the country table (step 11), per SD
c=pd.read_csv(f"{OUT}/11_unbundle_table.csv").dropna(subset=["auto_resid","tertiary","internet","log_gdp"])
for v in ["tertiary","internet","log_gdp"]: c["z_"+v]=z(c[v])
res["countries_like_for_like"]={}
print("\nLike-for-like across countries (N=%d), per SD:" % len(c))
for k,f in {"education alone":"auto_resid ~ z_tertiary","education + log income":"auto_resid ~ z_tertiary + z_log_gdp","income alone":"auto_resid ~ z_log_gdp","internet alone":"auto_resid ~ z_internet"}.items():
    m=smf.ols(f,data=c).fit(cov_type="HC3"); term=m.params.index[1]; lo,hi=m.conf_int().loc[term]
    res["countries_like_for_like"][k]={"coef":round(m.params[term],2),"ci":[round(lo,2),round(hi,2)],"r2":round(m.rsquared,2)}
    print(f"  {k:24s} {term.replace('z_','')} {m.params[term]:+.2f} [{lo:+.2f},{hi:+.2f}]  R2 {m.rsquared:.2f}")
e1=res["(1) education alone"]["terms"]["z_bachelors_plus"]; print(f"  State model (1) MDE {e1['mde']:.2f}: the country-sized education effect ({res['countries_like_for_like']['education alone']['coef']:+.2f}) is {'outside' if res['countries_like_for_like']['education alone']['coef']<e1['ci'][0] else 'inside'} the state interval [{e1['ci'][0]:+.2f},{e1['ci'][1]:+.2f}]")
print("\nReminder, countries (step 11): tertiary −1.9 per SD alone-with-income; with internet and income −1.6.")
json.dump(res,open(f"{OUT}/20_us_states.json","w"),indent=1)
assert len(t)>=40 and t.bachelors_plus.between(20,70).all() and t.broadband.between(70,100).all(); print("CHECK OK")
