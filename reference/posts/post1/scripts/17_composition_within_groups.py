"""Step 17 (exploratory): is the education effect inside professional groups about WHO is in the group?
Within each SOC major group (May 2026), the file gives by country not only the automation share but the use-case split
(work / coursework / personal) of that group's conversations. If richer countries' 'managers' are managers at work and poorer
countries' 'managers' are students, the coursework share within the group should absorb the education effect."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce"); m=v6[(v6.date_start=="2026-05-01")]
soc=m[(m.category_name=="soc_occupation")&(m.hierarchy_level.astype(str)=="1")&(m.geo_level=="country")]
aui=m[(m.geo_level=="country")&(m.category_name=="overall")&(m.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
tr=pd.read_csv(f"{OUT}/11_unbundle_table.csv")[["geo_id","gdp_pwa","lang_group","tertiary","internet"]].dropna().copy(); tr["log_gdp"]=np.log(tr.gdp_pwa)
groups=["Life, Physical, and Social Science","Management","Healthcare Practitioners and Technical","Business and Financial Operations","Arts, Design, Entertainment, Sports, and Media","Educational Instruction and Library"]
res={}; print("Within-group education coefficient (per SD) before and after adding the group's own coursework and personal shares by country\n")
for g in groups:
    w=soc[soc.node_name==g].pivot_table(index="geo_id",columns="metric_id",values="value",aggfunc="first")
    d=w[["collaboration_bucket_automation_pct","use_case_coursework_pct","use_case_personal_pct","use_case_work_pct"]].rename(columns={"collaboration_bucket_automation_pct":"auto_g","use_case_coursework_pct":"cw","use_case_personal_pct":"pers","use_case_work_pct":"work"})
    d=d.join(aui.rename("aui")).merge(tr,left_index=True,right_on="geo_id").dropna()
    for c in ["tertiary","internet","log_gdp"]: d["z_"+c]=(d[c]-d[c].mean())/d[c].std(ddof=0)
    small=d.lang_group.value_counts(); d["lang_group"]=d.lang_group.where(d.lang_group.map(small)>=5,"other")
    m0=smf.ols("auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group)",data=d).fit(cov_type="HC3")
    m1=smf.ols("auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group) + cw + pers",data=d).fit(cov_type="HC3")
    f=lambda mm,k: f"{mm.params[k]:+.2f} [{mm.conf_int().loc[k][0]:+.2f},{mm.conf_int().loc[k][1]:+.2f}]"
    res[g]={"n":int(m0.nobs),"tert_before":round(m0.params["z_tertiary"],2),"tert_after":round(m1.params["z_tertiary"],2),"coursework_coef":round(m1.params["cw"],2),"personal_coef":round(m1.params["pers"],2),
            "mean_cw":round(d.cw.mean(),1),"corr_cw_tertiary":round(d[["cw","tertiary"]].corr().iloc[0,1],2)}
    print(f"{g[:40]:40s} N={int(m0.nobs):3d}  tertiary before {f(m0,'z_tertiary')}  after {f(m1,'z_tertiary')}  | coursework share coef {f(m1,'cw')} personal {f(m1,'pers')} | mean coursework in group {d.cw.mean():.0f}%, corr(cw, tertiary) {d[['cw','tertiary']].corr().iloc[0,1]:+.2f}")
json.dump(res,open(f"{OUT}/17_composition.json","w"),indent=1); print("CHECK OK")
