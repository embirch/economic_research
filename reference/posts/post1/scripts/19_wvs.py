"""Step 19 (exploratory; the direct test of 'learning culture'): World Values Survey wave 7 (2017-2022), country-level shares.
Items: 'important qualities children can be encouraged to learn at home' (1 = mentioned): Q8 independence, Q11 imagination,
Q17 obedience, Q9 hard work, Q14 determination/perseverance; and Q45 'greater respect for authority' (1 good, 2 don't mind, 3 bad).
Weighted by W_WEIGHT within country. Each measure added to the unbundled model (tertiary + internet + income + controls), then to
the strategy, creative and computer activity models. Negative codes are missing."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
use=["B_COUNTRY_ALPHA","W_WEIGHT","Q8","Q11","Q17","Q9","Q14","Q45"]
w=pd.read_csv(f"{RAW}/WVS_Cross-National_Wave_7_csv_v6_0.csv", usecols=use, low_memory=False)
for c in use[2:]: w[c]=pd.to_numeric(w[c],errors="coerce"); w.loc[w[c]<0,c]=np.nan
w["W_WEIGHT"]=pd.to_numeric(w.W_WEIGHT,errors="coerce").fillna(1.0)
def wshare(df, col, val): 
    m=df[col].notna(); return (df.loc[m,"W_WEIGHT"]*(df.loc[m,col]==val)).sum()/df.loc[m,"W_WEIGHT"].sum()*100
rows=[]
for iso,g in w.groupby("B_COUNTRY_ALPHA"):
    rows.append({"geo_id":iso,"n_resp":int(len(g)),"wvs_independence":wshare(g,"Q8",1),"wvs_imagination":wshare(g,"Q11",1),"wvs_obedience":wshare(g,"Q17",1),
                 "wvs_hardwork":wshare(g,"Q9",1),"wvs_perseverance":wshare(g,"Q14",1),"wvs_respect_authority_good":wshare(g,"Q45",1)})
wv=pd.DataFrame(rows).set_index("geo_id"); wv["wvs_autonomy_index"]=(wv.wvs_independence+wv.wvs_imagination)-wv.wvs_obedience   # inquiry minus obedience
wv.to_csv(f"{OUT}/19_wvs_country.csv"); print("WVS countries:", len(wv), "| respondents:", wv.n_resp.sum())
t=pd.read_csv(f"{OUT}/11_unbundle_table.csv"); d=t.merge(wv,left_on="geo_id",right_index=True,how="left")
cands=["wvs_independence","wvs_imagination","wvs_obedience","wvs_hardwork","wvs_perseverance","wvs_respect_authority_good","wvs_autonomy_index"]
def z(s): return (s-s.mean())/s.std(ddof=0)
base_vars=["auto_resid","aui","coding_share","personal_share","lang_group","tertiary","internet","log_gdp"]
res={"overall":{}}
print("\n(A) Aug 2025 outcome: WVS item added to tertiary + internet + income (+controls). Coef per SD [95% CI]; tertiary after; corr with tertiary")
for c in cands:
    dd=d.dropna(subset=base_vars+[c]).copy(); small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
    for v in ["tertiary","internet","log_gdp",c]: dd["z_"+v]=z(dd[v])
    m=smf.ols(f"auto_resid ~ z_tertiary + z_internet + z_log_gdp + aui + coding_share + personal_share + C(lang_group) + z_{c}",data=dd).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["z_"+c]
    res["overall"][c]={"n":int(m.nobs),"coef":round(m.params["z_"+c],2),"ci":[round(lo,2),round(hi,2)],"mde":round(2.8*m.bse["z_"+c],2),"tertiary_after":round(m.params["z_tertiary"],2),"corr_tertiary":round(dd[[c,"tertiary"]].corr().iloc[0,1],2)}
    print(f"  {c:28s} N={int(m.nobs):3d}  {m.params['z_'+c]:+.2f} [{lo:+.2f},{hi:+.2f}]  MDE {2.8*m.bse['z_'+c]:.2f}  tertiary after {m.params['z_tertiary']:+.2f}  corr {dd[[c,'tertiary']].corr().iloc[0,1]:+.2f}")
# also: does the WVS item survive with the culture-of-learning measures from step 18?
# (B) activities
v6=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce"); m6=v6[v6.date_start=="2026-05-01"]
gwa=m6[(m6.category_name=="onet")&(m6.hierarchy_level.astype(str)=="3")&(m6.geo_level=="country")&(m6.metric_id=="collaboration_bucket_automation_pct")]
aui=m6[(m6.geo_level=="country")&(m6.category_name=="overall")&(m6.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
res["activities"]={}
print("\n(B) Selective activities, May 2026")
for act in ["Developing Objectives and Strategies","Thinking Creatively","Working with Computers"]:
    y=gwa[gwa.node_name==act].set_index("geo_id")["value"].rename("auto_g")
    base=pd.concat([y,aui.rename("aui")],axis=1,join="inner").merge(d[["geo_id","tertiary","internet","log_gdp","lang_group"]+cands],left_index=True,right_on="geo_id")
    out={}
    for c in ["wvs_independence","wvs_imagination","wvs_obedience","wvs_autonomy_index","wvs_respect_authority_good"]:
        dd=base.dropna(subset=["auto_g","aui","tertiary","internet","log_gdp","lang_group",c]).copy(); small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
        for v in ["tertiary","internet","log_gdp",c]: dd["z_"+v]=z(dd[v])
        m=smf.ols(f"auto_g ~ z_tertiary + z_internet + z_log_gdp + aui + C(lang_group) + z_{c}",data=dd).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["z_"+c]
        out[c]={"n":int(m.nobs),"coef":round(m.params["z_"+c],2),"ci":[round(lo,2),round(hi,2)]}
    res["activities"][act]=out; print(f"  {act}:"); [print(f"     {c:28s} N={v['n']:3d} {v['coef']:+.2f} {v['ci']}") for c,v in out.items()]
json.dump(res,open(f"{OUT}/19_wvs.json","w"),indent=1); print("CHECK OK")
