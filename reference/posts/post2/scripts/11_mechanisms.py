"""Step 11 (pre-registered H3): the place in the request. Each persistent non-leisure cluster on its pre-stated covariate,
alone and with log Usage Index, 50 states, HC3, both months. Rural share is reported beside agriculture for outdoor and garden."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; cov=pd.read_csv(f"{OUT}/09_covariates_outliers.csv",index_col=0)
MAP={"Outdoor and garden":"agri_share","Destination research":"arts_accom_share","Editing and rewriting":"pubadmin_share","Self-presentation writing":"pubadmin_share","Research and evidence":"pubadmin_share","Instructional design":"college_share","Science":"college_share","Formatted writing":"college_share"}
EXTRA={"Outdoor and garden":"rural_share"}
def z(x): return (x-x.mean())/x.std(ddof=0)
res={}
for c,v in MAP.items():
    res[c]={"covariate":v}; ok=True
    for m_ in ["apr","may"]:
        d=pd.read_csv(f"{OUT}/09_distinctiveness_{m_}.csv",index_col=0)
        if c not in d.columns: print(f"  {c}: not published/below share in {m_}"); ok=False; continue
        dd=pd.concat([np.log(d[c]).rename("y"),cov],axis=1).dropna(subset=["y",v,"log_aui"]); dd["zx"]=z(dd[v])
        a=smf.ols("y ~ zx",data=dd).fit(cov_type="HC3"); b=smf.ols("y ~ zx + log_aui",data=dd).fit(cov_type="HC3"); lo,hi=a.conf_int().loc["zx"]; blo,bhi=b.conf_int().loc["zx"]
        res[c][m_]={"n":int(a.nobs),"alone":{"coef":round(a.params.zx,3),"ci":[round(lo,3),round(hi,3)],"mde":round(2.8*a.bse.zx,3),"r2":round(a.rsquared,3)},"with_index":{"coef":round(b.params.zx,3),"ci":[round(blo,3),round(bhi,3)],"index":round(b.params.log_aui,3)}}
        ok&=(lo>0) and a.params.zx>=2.8*a.bse.zx
        line=f"  {c:28s} ← {v:18s} {m_}: alone {a.params.zx:+.3f} [{lo:+.2f},{hi:+.2f}] MDE {2.8*a.bse.zx:.2f} R2 {a.rsquared:.2f} | with index {b.params.zx:+.3f} [{blo:+.2f},{bhi:+.2f}] (index {b.params.log_aui:+.2f})"
        if c in EXTRA:
            dd["zr"]=z(dd[EXTRA[c]]); r=smf.ols("y ~ zr",data=dd).fit(cov_type="HC3"); rlo,rhi=r.conf_int().loc["zr"]; line+=f" | {EXTRA[c]} alone {r.params.zr:+.3f} [{rlo:+.2f},{rhi:+.2f}]"; res[c][m_]["rural_alone"]={"coef":round(r.params.zr,3),"ci":[round(rlo,3),round(rhi,3)]}
        print(line)
    res[c]["explained"]=bool(ok); print(f"     → {'EXPLAINED by the stated mechanism' if ok else 'NOT explained by the stated mechanism'}")
json.dump(res,open(f"{OUT}/11_mechanisms.json","w"),indent=1); print("CHECK OK")
