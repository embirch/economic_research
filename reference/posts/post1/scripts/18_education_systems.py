"""Step 18 (exploratory): does the QUALITY or the CHARACTER of a country's education, rather than its quantity, carry the delegation effect?
Candidates by country: harmonised test scores (World Bank HCI, HLOS), learning-adjusted years of school (LAYS), expected years (EYRS),
secondary enrolment, education spending (% GDP); GLOBE future orientation and performance orientation practices; Hofstede long-term
orientation and indulgence. Each added to the unbundled model (tertiary + internet + income + controls) on the Aug 2025 outcome, and
each tested on the two 'selective' activities (strategy: expect negative; working with computers: expect positive) in May 2026."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
t=pd.read_csv(f"{OUT}/11_unbundle_table.csv")
eq=pd.read_csv(f"{OUT}/18_education_quality.csv",index_col=0); eq.index.name="geo_id"
eq=eq.rename(columns={"HD.HCI.HLOS":"test_scores","HD.HCI.LAYS":"learning_adj_years","HD.HCI.EYRS":"expected_years","SE.SEC.ENRR":"secondary_enrol","SE.PRM.ENRR":"primary_enrol","SE.XPD.TOTL.GD.ZS":"edu_spend"})
hf=pd.read_csv(f"{RAW}/hofstede_6d_2015-08-16.csv",sep=";",keep_default_na=False)
tr=pd.read_csv(f"{OUT}/04_country_traits.csv")   # has hof_idv/uai but not ltowvs/ivr: rebuild mapping via hof_pdi match on values? simpler: merge by name map used in step 04 is not saved, so use GLOBE only + Hofstede via pdi join
gc=pd.read_excel(f"{RAW}/GLOBE-Phase-2-Aggregated-Societal-Culture-Data.xls",sheet_name=0)
# reuse step-04 name mapping by importing it
import importlib.util, sys
spec=importlib.util.spec_from_file_location("s04","scripts/04_build_table.py")
# (avoid re-running step 04) -> replicate the small mapping helpers inline
pop=pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_country.csv",keep_default_na=False); pop=pop[pop.iso_alpha_3!=""]; name2iso={n.lower():i for n,i in zip(pop.country_name,pop.iso_alpha_3)}
galias={"england":"GBR","germany (west)":"DEU","south africa (white sample)":"ZAF","usa":"USA","the netherlands":"NLD","netherlands":"NLD","hong kong":"HKG","taiwan":"TWN","south korea":"KOR","iran":"IRN","russia":"RUS","czech republic":"CZE","kuwait":"KWT","qatar":"QAT","zambia":"ZMB","zimbabwe":"ZWE","nigeria":"NGA","namibia":"NAM","el salvador":"SLV","costa rica":"CRI","venezuela":"VEN","bolivia":"BOL","ecuador":"ECU","guatemala":"GTM","colombia":"COL","argentina":"ARG","brazil":"BRA","mexico":"MEX","new zealand":"NZL","australia":"AUS","turkey":"TUR","egypt":"EGY","israel":"ISR","japan":"JPN","china":None}
gc["iso3"]=gc["Country Name"].map(lambda n: galias.get(str(n).strip().lower(), name2iso.get(str(n).strip().lower())))
globe=gc.dropna(subset=["iso3"]).drop_duplicates("iso3").set_index("iso3")[["Future Orientation Societal Practices","Performance Orientation Societal Practices","Uncertainty Avoidance Societal Practices","Collectivism I Societal Practices (Institutional Collectivism)"]]
globe.columns=["globe_future","globe_performance","globe_uai","globe_inst_collectivism"]
halias={"u.s.a.":"USA","great britain":"GBR","korea south":"KOR","russia":"RUS","czech rep":"CZE","slovak rep":"SVK","iran":"IRN","vietnam":"VNM","taiwan":"TWN","trinidad and tobago":"TTO","serbia":"SRB","venezuela":"VEN","bolivia":"BOL","tanzania":"TZA","moldova":"MDA","dominican rep":"DOM","el salvador":"SLV","hong kong":"HKG","sri lanka":"LKA","south africa white":"ZAF","new zealand":"NZL","saudi arabia":"SAU","united arab emirates":"ARE","costa rica":"CRI","turkey":"TUR","egypt":"EGY","laos":"LAO","brunei":"BRN","kyrgyz rep":"KGZ","montenegro":"MNE","belgium":"BEL","germany":"DEU","suriname":"SUR","burkina faso":"BFA","sierra leone":"SLE","tunisia":"TUN","zambia":"ZMB"}
hf["iso3"]=hf.country.map(lambda n: halias.get(n.strip().lower(), name2iso.get(n.strip().lower())))
for c in ["ltowvs","ivr"]: hf[c]=pd.to_numeric(hf[c].replace("#NULL!",np.nan),errors="coerce")
hof=hf.dropna(subset=["iso3"]).drop_duplicates("iso3").set_index("iso3")[["ltowvs","ivr"]].rename(columns={"ltowvs":"hof_longterm","ivr":"hof_indulgence"})
d=t.merge(eq,left_on="geo_id",right_index=True,how="left").merge(globe,left_on="geo_id",right_index=True,how="left").merge(hof,left_on="geo_id",right_index=True,how="left")
d.to_csv(f"{OUT}/18_education_systems_table.csv",index=False)
cands=["test_scores","learning_adj_years","expected_years","secondary_enrol","edu_spend","globe_future","globe_performance","globe_uai","globe_inst_collectivism","hof_longterm","hof_indulgence"]
def z(s): return (s-s.mean())/s.std(ddof=0)
base_vars=["auto_resid","aui","coding_share","personal_share","lang_group","tertiary","internet","log_gdp"]
print("(A) Aug 2025 outcome: each candidate added to tertiary + internet + income (+controls). Coef per SD [95% CI]; tertiary coef after adding.\n")
rows={}
for c in cands:
    dd=d.dropna(subset=base_vars+[c]).copy(); small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
    for v in ["tertiary","internet","log_gdp",c]: dd["z_"+v]=z(dd[v])
    m=smf.ols(f"auto_resid ~ z_tertiary + z_internet + z_log_gdp + aui + coding_share + personal_share + C(lang_group) + z_{c}",data=dd).fit(cov_type="HC3")
    lo,hi=m.conf_int().loc["z_"+c]; rows[c]={"n":int(m.nobs),"coef":round(m.params["z_"+c],2),"ci":[round(lo,2),round(hi,2)],"tertiary_after":round(m.params["z_tertiary"],2),"corr_with_tertiary":round(dd[[c,"tertiary"]].corr().iloc[0,1],2)}
    print(f"  {c:24s} N={int(m.nobs):3d}  {m.params['z_'+c]:+.2f} [{lo:+.2f},{hi:+.2f}]   tertiary after: {m.params['z_tertiary']:+.2f}   corr(candidate, tertiary) {dd[[c,'tertiary']].corr().iloc[0,1]:+.2f}")
# (B) the two selective activities, May 2026
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce"); m6=v6[v6.date_start=="2026-05-01"]
gwa=m6[(m6.category_name=="onet")&(m6.hierarchy_level.astype(str)=="3")&(m6.geo_level=="country")&(m6.metric_id=="collaboration_bucket_automation_pct")]
aui=m6[(m6.geo_level=="country")&(m6.category_name=="overall")&(m6.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
print("\n(B) Selective activities, May 2026: candidate coef per SD with tertiary, internet, income in the model")
actres={}
for act in ["Developing Objectives and Strategies","Thinking Creatively","Working with Computers"]:
    y=gwa[gwa.node_name==act].set_index("geo_id")["value"].rename("auto_g")
    base=pd.concat([y,aui.rename("aui")],axis=1,join="inner").merge(d[["geo_id","tertiary","internet","log_gdp","lang_group"]+cands],left_index=True,right_on="geo_id")
    out={}
    for c in ["test_scores","learning_adj_years","globe_future","globe_performance","hof_longterm","hof_indulgence"]:
        dd=base.dropna(subset=["auto_g","aui","tertiary","internet","log_gdp","lang_group",c]).copy(); small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
        for v in ["tertiary","internet","log_gdp",c]: dd["z_"+v]=z(dd[v])
        m=smf.ols(f"auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group) + z_{c}",data=dd).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["z_"+c]
        out[c]={"n":int(m.nobs),"coef":round(m.params["z_"+c],2),"ci":[round(lo,2),round(hi,2)],"tertiary_after":round(m.params["z_tertiary"],2)}
    actres[act]=out
    print(f"  {act}:"); [print(f"     {c:20s} N={v['n']:3d} {v['coef']:+.2f} {v['ci']}  tertiary after {v['tertiary_after']:+.2f}") for c,v in out.items()]
json.dump({"overall":rows,"activities":actres},open(f"{OUT}/18_education_systems.json","w"),indent=1); print("CHECK OK")
