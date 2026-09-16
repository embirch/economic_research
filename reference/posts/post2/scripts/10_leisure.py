"""Step 10 (pre-registered H2): the hobbyist signature. For each leisure cluster, log distinctiveness on log Usage Index (a) and
on log Usage Index + personal-use share (b), 50 states, HC3, April and May."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; cov=pd.read_csv(f"{OUT}/09_covariates_outliers.csv",index_col=0); LEIS=["Fiction writing","Gaming","Companionship and conversation","Media discovery"]
res={}; passes=0
for c in LEIS:
    res[c]={}; ok=True
    for m_ in ["apr","may"]:
        d=pd.read_csv(f"{OUT}/09_distinctiveness_{m_}.csv",index_col=0); y=np.log(d[c]).rename("y"); dd=pd.concat([y,cov],axis=1).dropna(subset=["y","log_aui","personal_share"])
        a=smf.ols("y ~ log_aui",data=dd).fit(cov_type="HC3"); b=smf.ols("y ~ log_aui + personal_share",data=dd).fit(cov_type="HC3")
        lo,hi=a.conf_int().loc["log_aui"]; blo,bhi=b.conf_int().loc["log_aui"]; plo,phi=b.conf_int().loc["personal_share"]
        res[c][m_]={"n":int(a.nobs),"a_index":{"coef":round(a.params.log_aui,3),"ci":[round(lo,3),round(hi,3)],"mde":round(2.8*a.bse.log_aui,3),"r2":round(a.rsquared,3)},"b_index":{"coef":round(b.params.log_aui,3),"ci":[round(blo,3),round(bhi,3)]},"b_personal":{"coef":round(b.params.personal_share,3),"ci":[round(plo,3),round(phi,3)],"mde":round(2.8*b.bse.personal_share,3)},"r2_b":round(b.rsquared,3)}
        ok&= (hi<0) and abs(a.params.log_aui)>=2.8*a.bse.log_aui
        print(f"  {c:32s} {m_}: N={int(a.nobs)} (a) index {a.params.log_aui:+.3f} [{lo:+.2f},{hi:+.2f}] MDE {2.8*a.bse.log_aui:.2f} R2 {a.rsquared:.2f} | (b) index {b.params.log_aui:+.3f} [{blo:+.2f},{bhi:+.2f}], personal {b.params.personal_share:+.3f} [{plo:+.3f},{phi:+.3f}] R2 {b.rsquared:.2f}")
    res[c]["passes"]=bool(ok); passes+=ok
res["clusters_passing"]=int(passes); res["H2"]="HOLDS" if passes>=3 else "DOES NOT HOLD"; print(f"\nH2 hobbyist signature: {passes} of 4 clusters pass in both months →", res["H2"])
# what a doubling of the index means, in the passing clusters, and the pooled leisure index
for m_ in ["apr","may"]:
    d=pd.read_csv(f"{OUT}/09_distinctiveness_{m_}.csv",index_col=0); y=np.log(d[LEIS].mean(axis=1)).rename("y"); dd=pd.concat([y,cov],axis=1).dropna(subset=["y","log_aui"]); a=smf.ols("y ~ log_aui",data=dd).fit(cov_type="HC3")
    print(f"  pooled leisure index, {m_}: {a.params.log_aui:+.3f} [{a.conf_int().loc['log_aui',0]:+.2f},{a.conf_int().loc['log_aui',1]:+.2f}] R2 {a.rsquared:.2f}  (a state at half the national index has leisure distinctiveness {np.exp(-a.params.log_aui*np.log(2)):.2f}x a state at the national index)")
    res[f"pooled_{m_}"]={"coef":round(a.params.log_aui,3),"r2":round(a.rsquared,3)}
json.dump(res,open(f"{OUT}/10_leisure.json","w"),indent=1); print("CHECK OK")
