"""Step 09 (pre-registered H1): distinctiveness of level-1 request clusters by state, April and May 2026; which outliers persist;
recurrence against state size. Also builds the covariates for H3 (Census industry, enrolment, rural share)."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"; MINSHARE=0.5; THR=1.6
j=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["date_start","geo_id","geo_level","category_name","hierarchy_level","metric_id","value","node_name"]); j["value"]=pd.to_numeric(j.value,errors="coerce")
req=j[(j.category_name=="request")&(j.hierarchy_level.astype(str)=="1")&(j.metric_id=="pct")]
D={}
for ds,m_ in [("2026-04-01","apr"),("2026-05-01","may")]:
    m=req[req.date_start==ds]; us=m[(m.geo_level=="country")&(m.geo_id=="USA")].set_index("node_name").value
    p=m[(m.geo_level=="subregion")&(m.geo_id.str.startswith("US-"))].pivot_table(index="geo_id",columns="node_name",values="value"); p.index=p.index.str[3:]
    p=p.loc[[i for i in p.index if len(i)==2 and i!="UT"]]; us=us.reindex(p.columns); keep=us[us>=MINSHARE].index; d=p[keep].div(us[keep],axis=1); D[m_]=d; d.to_csv(f"{OUT}/09_distinctiveness_{m_}.csv")
a,b=D["apr"],D["may"]; cols=a.columns.intersection(b.columns); a=a[cols]; b=b[cols]
print(f"clusters with >= {MINSHARE}% of US use in both months: {len(cols)}; states {len(a)} (Utah excluded)")
oa=(a>=THR); ob=(b>=THR); both=oa&ob
print(f"outlier cells (>= {THR}x): April {int(oa.sum().sum())}, May {int(ob.sum().sum())}, both {int(both.sum().sum())}; recurrence of April outliers {both.sum().sum()/oa.sum().sum():.0%}, of May outliers {both.sum().sum()/ob.sum().sum():.0%}")
s=pd.concat([np.log(a.stack()).rename("a"),np.log(b.stack()).rename("b")],axis=1).dropna(); print(f"month-to-month correlation of log distinctiveness: {s.a.corr(s.b):.2f}")
# usage share by state (May) for the size test
ov=pd.read_csv(f"{OUT}/01_june_overall.csv",index_col=0); usage=ov[ov.wave=="2026-05"].usage_pct
cells=[]
for st in a.index:
    for c in cols:
        if oa.loc[st,c]: cells.append({"state":st,"cluster":c,"apr":a.loc[st,c],"may":b.loc[st,c],"recurs":int(both.loc[st,c]),"log_usage":np.log(usage[st])})
cells=pd.DataFrame(cells); m=smf.ols("recurs ~ log_usage",data=cells).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["log_usage"]
print(f"recurrence on log state usage share (linear probability, {len(cells)} April outlier cells): {m.params.log_usage:+.3f} [{lo:+.3f},{hi:+.3f}] MDE {2.8*m.bse.log_usage:.3f}")
terc=pd.qcut(usage.reindex(a.index),3,labels=["small","mid","large"]); byt=cells.assign(t=cells.state.map(terc)).groupby("t").recurs.mean(); print("recurrence by state-size tercile:", byt.round(2).to_dict()); cnt=oa.sum(axis=1); print("April outliers per state by tercile (mean):", cnt.groupby(terc).mean().round(1).to_dict())
pers=cells[cells.recurs==1].sort_values("may",ascending=False); pers["min"]=pers[["apr","may"]].min(axis=1); pers=pers.sort_values("min",ascending=False); pers.to_csv(f"{OUT}/09_persistent.csv",index=False)
print("persistent outliers:"); [print(f"  {r.state} {r['min']:.1f}x  {r.cluster}") for _,r in pers.iterrows()]
# thresholds robustness
for t in (1.5,2.0): print(f"  threshold {t}: April {int((a>=t).sum().sum())}, May {int((b>=t).sum().sum())}, both {int(((a>=t)&(b>=t)).sum().sum())}")
# ---- covariates for H3
FIPS={"01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY"}
def acs(t):
    c=pd.read_csv(f"{RAW}/census/acsdt1y2023-{t}.dat",sep="|",dtype=str); c=c[c.GEO_ID.str.startswith("0400000US")].copy(); c["state"]=c.GEO_ID.str[-2:].map(FIPS); return c.dropna(subset=["state"]).set_index("state").apply(pd.to_numeric,errors="coerce")
i=acs("c24030"); tot=i.C24030_E001; F=27  # female offset in C24030: 55 estimates, male block 002-028, female 029-055
cov=pd.DataFrame({"agri_share":(i.C24030_E004+i[f"C24030_E{4+F:03d}"])/tot*100,"arts_accom_share":(i.C24030_E024+i[f"C24030_E{24+F:03d}"])/tot*100,"pubadmin_share":(i.C24030_E028+i[f"C24030_E{28+F:03d}"])/tot*100})
e=acs("b14001"); cov["college_share"]=(e.B14001_E008+e.B14001_E009)/e.B14001_E001*100
ru=pd.read_csv(f"{RAW}/census/PctUrbanRural_State.txt",sep=",",encoding="latin-1"); ru.columns=[c.strip() for c in ru.columns]
name2=pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_us_state.csv").set_index("state")["state_code"]; ru["state"]=ru["STATENAME"].map(name2); cov=cov.join(ru.dropna(subset=["state"]).set_index("state")[["POPPCT_RURAL"]].rename(columns={"POPPCT_RURAL":"rural_share"}).astype(float))
cov=cov.join(np.log(usage).rename("log_usage")).join(np.log(ov[ov.wave=="2026-05"].usage_per_capita_index).rename("log_aui")).join(ov[ov.wave=="2026-05"].use_case_personal_pct.rename("personal_share"))
cov.to_csv(f"{OUT}/09_covariates_outliers.csv")
print("covariate spot checks: DC public admin %.1f%% (Census ~17), VT rural %.1f%% (Census 64.9), HI arts/accommodation %.1f%%, NE agriculture %.1f%%, UT college %.1f%%" % (cov.loc["DC","pubadmin_share"],cov.loc["VT","rural_share"],cov.loc["HI","arts_accom_share"],cov.loc["NE","agri_share"],cov.loc["UT","college_share"]))
res={"clusters":int(len(cols)),"outliers":{"apr":int(oa.sum().sum()),"may":int(ob.sum().sum()),"both":int(both.sum().sum())},"recurrence_apr":round(both.sum().sum()/oa.sum().sum(),3),"corr_months":round(s.a.corr(s.b),3),"recurrence_on_log_usage":{"coef":round(m.params.log_usage,3),"ci":[round(lo,3),round(hi,3)],"mde":round(2.8*m.bse.log_usage,3)},"recurrence_by_tercile":byt.round(3).to_dict(),"persistent":pers[["state","cluster","apr","may"]].round(2).to_dict("records")}
res["H1"]="HOLDS" if res["recurrence_apr"]<0.6 and lo>0 else "DOES NOT HOLD"; print("H1 (recurrence < 60% and rises with usage):", res["H1"])
json.dump(res,open(f"{OUT}/09_outliers.json","w"),indent=1); assert 15<=len(pers)<=40 and cov.rural_share.notna().sum()>=50; print("CHECK OK")
