"""Step 06 (pre-registered H4): who caught up? Change in log Usage Index, Aug 2025 -> May 2026, Utah excluded."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; L=pd.read_csv(f"{OUT}/01_state_levels.csv",index_col=0); C=pd.read_csv(f"{OUT}/05_covariates_plus.csv",index_col=0)
w=L.reset_index().pivot_table(index="state",columns="wave",values="aui"); lw=np.log(w)
d=pd.DataFrame({"d_log":lw["2026-05"]-lw["2025-08"],"log_aug":lw["2025-08"],"log_nov":lw["2025-11"],"log_feb":lw["2026-02"],"log_apr":lw["2026-04"],"d_nov_feb":lw["2026-02"]-lw["2025-11"],"d_aug_nov":lw["2025-11"]-lw["2025-08"],"d_feb_may":lw["2026-05"]-lw["2026-02"],"d_apr_may":lw["2026-05"]-lw["2026-04"],"log_count_aug":np.log(L[L.wave=="2025-08"].usage_count)}).join(C).drop(index="UT").rename(columns={"wf_Computer and Mathematical":"tech"})
def z(x): return (x-x.mean())/x.std(ddof=0)
for v in ["bachelors_plus","tech","log_gdp"]: d["z_"+v]=z(d[v])
d["abs_d_aug_nov"]=d.d_aug_nov.abs(); res={}
print("Change in log Usage Index by sub-period (mean over 50 states, Utah excluded): Aug->Nov %.3f, Nov->Feb %.3f (advertising influx wave), Feb->May %.3f; Aug->May %.3f" % (d.d_aug_nov.mean(),d.d_nov_feb.mean(),d.d_feb_may.mean(),d.d_log.mean()))
print("Bottom-10 states in Aug (mean gain) %.3f vs top-10 %.3f" % (d.sort_values("log_aug").head(10).d_log.mean(), d.sort_values("log_aug").tail(10).d_log.mean()))
for k,f in {"(a) beta-convergence":"d_log ~ log_aug","(b) + education + tech share":"d_log ~ log_aug + z_bachelors_plus + z_tech","(c) + education + income":"d_log ~ log_aug + z_bachelors_plus + z_log_gdp","(a1) Aug->Nov on Aug level":"d_aug_nov ~ log_aug","(a2) Nov->Feb on Nov level":"d_nov_feb ~ log_nov","(a3) Feb->May on Feb level":"d_feb_may ~ log_feb","(a4) Apr->May on Apr level":"d_apr_may ~ log_apr","(n) |Aug->Nov change| on Aug sample size":"abs_d_aug_nov ~ log_count_aug"}.items():
    m=smf.ols(f,data=d).fit(cov_type="HC3"); row={}
    for t in m.params.index[1:]:
        lo,hi=m.conf_int().loc[t]; row[t.replace("z_","")]={"coef":round(m.params[t],3),"ci":[round(lo,3),round(hi,3)],"mde":round(2.8*m.bse[t],3)}
    res[k]={"r2":round(m.rsquared,3),"n":int(m.nobs),"terms":row}; print(f"  {k:32s} R2 {m.rsquared:.2f} | "+"  ".join(f"{t} {v['coef']:+.3f} [{v['ci'][0]:+.2f},{v['ci'][1]:+.2f}] MDE {v['mde']:.2f}" for t,v in row.items()))
# robustness: Wyoming moves 1.7 log points up then 1.6 down; the smallest states are the noisiest
for k,f in {"(a) without Wyoming":"d_log ~ log_aug","(a1) Aug->Nov without Wyoming":"d_aug_nov ~ log_aug"}.items():
    m=smf.ols(f,data=d.drop(index="WY")).fit(cov_type="HC3"); t=m.params.index[1]; lo,hi=m.conf_int().loc[t]; res[k]={"coef":round(m.params[t],3),"ci":[round(lo,3),round(hi,3)]}; print(f"  {k:32s} {m.params[t]:+.3f} [{lo:+.2f},{hi:+.2f}]")
print("  rank persistence of the index (Spearman): Aug25-May26 %.2f, Feb26-May26 %.2f" % tuple(__import__('scipy.stats',fromlist=['spearmanr']).spearmanr(w.drop(index='UT')[a],w.drop(index='UT')["2026-05"]).correlation for a in ["2025-08","2026-02"]))
b=res["(b) + education + tech share"]["terms"]; conv=res["(a) beta-convergence"]["terms"]["log_aug"]
print("\nPre-registered read-out: convergence real:", conv["ci"][1]<0, "| catch-up follows education:", abs(b["bachelors_plus"]["coef"])>=b["bachelors_plus"]["mde"] and (b["bachelors_plus"]["ci"][0]>0 or b["bachelors_plus"]["ci"][1]<0), "| follows composition:", abs(b["tech"]["coef"])>=b["tech"]["mde"] and (b["tech"]["ci"][0]>0 or b["tech"]["ci"][1]<0))
d.to_csv(f"{OUT}/06_catchup.csv"); json.dump(res,open(f"{OUT}/06_catchup.json","w"),indent=1); print("CHECK OK")
