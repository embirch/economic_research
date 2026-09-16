"""Step 16 (exploratory): the education/income gradient by WORK ACTIVITY (35 O*NET generalized work activities, June 2026), and what
explains which activities show it. For each activity: country automation share within the activity ~ z(tertiary) + z(internet) +
z(log income) + aui + C(lang_group). Then the activity-level education coefficient is related to the activity's global profile:
its global automation share, its global AI-autonomy, and the artifact types it produces."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce")
tr=pd.read_csv(f"{OUT}/11_unbundle_table.csv")[["geo_id","gdp_pwa","lang_group","tertiary","internet"]].dropna().copy(); tr["log_gdp"]=np.log(tr.gdp_pwa)
rows=[]
for ds in ["2026-04-01","2026-05-01"]:
    m=v6[v6.date_start==ds]; gwa=m[(m.category_name=="onet")&(m.hierarchy_level.astype(str)=="3")]
    aui=m[(m.geo_level=="country")&(m.category_name=="overall")&(m.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
    glob=gwa[gwa.geo_level=="global"].pivot_table(index="node_name",columns="metric_id",values="value",aggfunc="first")
    for g in sorted(gwa.node_name.unique()):
        y=gwa[(gwa.node_name==g)&(gwa.geo_level=="country")&(gwa.metric_id=="collaboration_bucket_automation_pct")].set_index("geo_id")["value"]
        d=pd.concat([y.rename("auto_g"),aui.rename("aui")],axis=1,join="inner").merge(tr,left_index=True,right_on="geo_id").dropna()
        if len(d)<40: continue
        for c in ["tertiary","internet","log_gdp"]: d["z_"+c]=(d[c]-d[c].mean())/d[c].std(ddof=0)
        small=d.lang_group.value_counts(); d["lang_group"]=d.lang_group.where(d.lang_group.map(small)>=5,"other")
        mod=smf.ols("auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group)",data=d).fit(cov_type="HC3"); lo,hi=mod.conf_int().loc["z_tertiary"]
        # 'income bundle' effect: joint contribution = coefficient on the first principal direction is overkill; report tertiary and the sum of the three standardised coefficients
        rows.append({"month":ds[:7],"activity":g,"n":int(mod.nobs),"tert":round(mod.params["z_tertiary"],2),"tert_lo":round(lo,2),"tert_hi":round(hi,2),
                     "bundle":round(mod.params["z_tertiary"]+mod.params["z_internet"]+mod.params["z_log_gdp"],2),
                     "global_auto":round(float(glob.loc[g,"collaboration_bucket_automation_pct"]),1),
                     "global_autonomy":round(float(glob.loc[g,"ai_autonomy_mean"]),2) if "ai_autonomy_mean" in glob.columns else np.nan,
                     "global_share":round(float(glob.loc[g,"pct"]),2) if "pct" in glob.columns else np.nan})
r=pd.DataFrame(rows); r.to_csv(f"{OUT}/16_activities.csv",index=False)
may=r[r.month=="2026-05"].sort_values("tert")
print("May 2026, by work activity: education coefficient on within-activity automation share (points per SD of tertiary enrolment)\n")
print(may[["activity","n","tert","tert_lo","tert_hi","bundle","global_auto","global_autonomy","global_share"]].to_string(index=False))
apr=r[r.month=="2026-04"].set_index("activity").tert; both=may.set_index("activity").tert.to_frame("may").join(apr.rename("apr"))
print("\nApril vs May agreement across activities (correlation):", round(both.corr().iloc[0,1],2))
print("Education coefficient vs activity's global automation share:", round(may[["tert","global_auto"]].corr().iloc[0,1],2), "| vs global autonomy:", round(may[["tert","global_autonomy"]].corr().iloc[0,1],2), "| vs global share of use:", round(may[["tert","global_share"]].corr().iloc[0,1],2))
print("Activities with intervals clear of zero (May):", may[may.tert_hi<0].activity.tolist())
print("CHECK OK")
