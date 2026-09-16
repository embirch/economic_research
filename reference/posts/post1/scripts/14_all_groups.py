"""Step 14 (exploratory): the within-occupation-group test on ALL 22 SOC major groups, both June 2026 months.
For each group and month: country automation share within the group ~ z(tertiary) + z(internet) + z(log income) + aui + C(lang_group).
Then relate each group's education coefficient to the group's own global profile: its learning share, its coursework share (from
the global pattern mix within the group), its global automation share, and its mean task value if available."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce")
tr=pd.read_csv(f"{OUT}/11_unbundle_table.csv"); tr=tr[["geo_id","gdp_pwa","lang_group","tertiary","internet","coursework_share"]].dropna().copy(); tr["log_gdp"]=np.log(tr.gdp_pwa)
rows=[]
for ds in ["2026-04-01","2026-05-01"]:
    m=v6[v6.date_start==ds]
    soc=m[(m.category_name=="soc_occupation")&(m.hierarchy_level.astype(str)=="1")]
    aui=m[(m.geo_level=="country")&(m.category_name=="overall")&(m.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
    glob=soc[soc.geo_level=="global"].pivot_table(index="node_name",columns="metric_id",values="value",aggfunc="first")
    for g in sorted(soc.node_name.unique()):
        y=soc[(soc.node_name==g)&(soc.geo_level=="country")&(soc.metric_id=="collaboration_bucket_automation_pct")].set_index("geo_id")["value"]
        d=pd.concat([y.rename("auto_g"),aui.rename("aui")],axis=1,join="inner").merge(tr,left_index=True,right_on="geo_id").dropna()
        if len(d)<40: continue
        for c in ["tertiary","internet","log_gdp"]: d["z_"+c]=(d[c]-d[c].mean())/d[c].std(ddof=0)
        small=d.lang_group.value_counts(); d["lang_group"]=d.lang_group.where(d.lang_group.map(small)>=5,"other")
        mod=smf.ols("auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group)",data=d).fit(cov_type="HC3")
        lo,hi=mod.conf_int().loc["z_tertiary"]
        rows.append({"month":ds[:7],"group":g,"n":int(mod.nobs),"tert_coef":round(mod.params["z_tertiary"],2),"tert_lo":round(lo,2),"tert_hi":round(hi,2),
                     "inc_coef":round(mod.params["z_log_gdp"],2),"int_coef":round(mod.params["z_internet"],2),
                     "global_learning":round(float(glob.loc[g,"collaboration_learning_pct"]),1) if "collaboration_learning_pct" in glob.columns else np.nan,
                     "global_automation":round(float(glob.loc[g,"collaboration_bucket_automation_pct"]),1),
                     "global_coursework":round(float(glob.loc[g,"use_case_coursework_pct"]),1) if "use_case_coursework_pct" in glob.columns else np.nan})
r=pd.DataFrame(rows); r.to_csv(f"{OUT}/14_all_groups.csv",index=False)
may=r[r.month=="2026-05"].sort_values("tert_coef")
print("May 2026: education coefficient on within-group automation share (points per SD of tertiary enrolment), all groups\n")
print(may[["group","n","tert_coef","tert_lo","tert_hi","inc_coef","global_learning","global_coursework","global_automation"]].to_string(index=False))
print("\nCorrelation across groups of the education coefficient with the group's global learning share:", round(may[["tert_coef","global_learning"]].corr().iloc[0,1],2),
      "| with global coursework share:", round(may[["tert_coef","global_coursework"]].corr().iloc[0,1],2), "| with global automation share:", round(may[["tert_coef","global_automation"]].corr().iloc[0,1],2))
apr=r[r.month=="2026-04"].set_index("group").tert_coef; both=may.set_index("group").tert_coef.to_frame("may").join(apr.rename("apr"))
print("April vs May education coefficients, correlation across groups:", round(both.corr().iloc[0,1],2))
print("CHECK OK")
