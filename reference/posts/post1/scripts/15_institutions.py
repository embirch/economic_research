"""Step 15 (exploratory): is the education effect in professional work about ACCOUNTABILITY rather than authority norms?
World Bank Worldwide Governance Indicators (public API): rule of law (RL.EST), regulatory quality (RQ.EST), government effectiveness (GE.EST).
Tests: (1) overall Aug 2025 outcome: add each WGI to the unbundled model (tertiary + internet + income); (2) within the five
professional groups where education mattered most in May 2026 (science, management, healthcare practitioners, business, arts):
automation share ~ z(tertiary) + z(internet) + z(log income) + z(rule of law) + aui + lang."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json, subprocess
RAW="data/raw"; OUT="data/processed"
def wgi_sheet(sheet):
    """Read one WGI sheet from the 2023-update workbook (years in row 13, headers in row 14, data from row 15); latest year's Estimate."""
    v=pd.read_excel(f"{RAW}/wgidataset.xlsx", sheet_name=sheet, engine="openpyxl", header=None)
    years=v.iloc[13]; heads=v.iloc[14]; data=v.iloc[15:]
    est_cols=[i for i in range(len(heads)) if str(heads[i]).strip()=="Estimate"]
    last=max(est_cols, key=lambda i: int(years[i]))
    out=pd.Series(pd.to_numeric(data[last],errors="coerce").values, index=data[1].astype(str).values)
    return out.dropna()
wgi=pd.DataFrame({"rule_of_law":wgi_sheet("RuleofLaw"),"reg_quality":wgi_sheet("RegulatoryQuality"),"gov_eff":wgi_sheet("GovernmentEffectiveness")}); wgi.index.name="geo_id"; wgi.to_csv(f"{OUT}/15_wgi.csv")
t=pd.read_csv(f"{OUT}/11_unbundle_table.csv").merge(wgi,left_on="geo_id",right_index=True,how="left")
def z(s): return (s-s.mean())/s.std(ddof=0)
# (1) overall
d=t.dropna(subset=["auto_resid","aui","coding_share","personal_share","lang_group","tertiary","internet","log_gdp","rule_of_law","reg_quality","gov_eff"]).copy()
small=d.lang_group.value_counts(); d["lang_group"]=d.lang_group.where(d.lang_group.map(small)>=5,"other")
for c in ["tertiary","internet","log_gdp","rule_of_law","reg_quality","gov_eff"]: d["z_"+c]=z(d[c])
print(f"(1) Overall outcome, N={len(d)}; correlations: rule_of_law~log_gdp {d[['rule_of_law','log_gdp']].corr().iloc[0,1]:.2f}, rule_of_law~tertiary {d[['rule_of_law','tertiary']].corr().iloc[0,1]:.2f}")
base="auto_resid ~ z_tertiary + z_internet + z_log_gdp + aui + coding_share + personal_share + C(lang_group)"
for extra in ["", " + z_rule_of_law", " + z_reg_quality", " + z_gov_eff"]:
    m=smf.ols(base+extra,data=d).fit(cov_type="HC3")
    keys=[k for k in m.params.index if k.startswith("z_")]
    print("   "+(extra or " baseline").strip(), {k.replace("z_",""):(round(m.params[k],2),[round(x,2) for x in m.conf_int().loc[k]]) for k in keys})
# (2) within professional groups, May 2026
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce"); m6=v6[v6.date_start=="2026-05-01"]
soc=m6[(m6.category_name=="soc_occupation")&(m6.hierarchy_level.astype(str)=="1")&(m6.geo_level=="country")&(m6.metric_id=="collaboration_bucket_automation_pct")]
aui=m6[(m6.geo_level=="country")&(m6.category_name=="overall")&(m6.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
groups=["Life, Physical, and Social Science","Management","Healthcare Practitioners and Technical","Business and Financial Operations","Arts, Design, Entertainment, Sports, and Media","Office and Administrative Support","Computer and Mathematical"]
print("\n(2) Within occupation groups, May 2026: coefficients per SD (tertiary | rule of law | log income)")
res={}
for g in groups:
    y=soc[soc.node_name==g].set_index("geo_id")["value"].rename("auto_g")
    dd=pd.concat([y,aui.rename("aui")],axis=1,join="inner").merge(t[["geo_id","tertiary","internet","log_gdp","lang_group","rule_of_law"]],left_index=True,right_on="geo_id").dropna()
    for c in ["tertiary","internet","log_gdp","rule_of_law"]: dd["z_"+c]=z(dd[c])
    small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
    m=smf.ols("auto_g ~ z_tertiary + z_internet + z_log_gdp + z_rule_of_law + aui + C(lang_group)",data=dd).fit(cov_type="HC3")
    f=lambda k: f"{m.params[k]:+.2f} [{m.conf_int().loc[k][0]:+.2f},{m.conf_int().loc[k][1]:+.2f}]"
    res[g]={k:[round(m.params[k],2)]+[round(x,2) for x in m.conf_int().loc[k]] for k in ["z_tertiary","z_rule_of_law","z_log_gdp","z_internet"]}
    print(f"   {g[:44]:44s} N={int(m.nobs):3d}  tertiary {f('z_tertiary')} | rule of law {f('z_rule_of_law')} | income {f('z_log_gdp')}")
json.dump(res,open(f"{OUT}/15_institutions.json","w"),indent=1); print("CHECK OK")
