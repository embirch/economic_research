"""Step 03, stage 1 of the decomposition: who in each state uses Claude. Compares the occupation mix Anthropic infers from
conversations (user composition, soc_occupation shares by state; Aug 2025 and May 2026) with the state's workforce (ACS C24010).
Questions: which occupations are over-represented among users everywhere; how much of the state-to-state variation in the
users' tech share is the workforce's tech share; and how selected each state's user base is (a dissimilarity index)."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; C=pd.read_csv(f"{OUT}/01_covariates.csv",index_col=0); wf=C[[c for c in C.columns if c.startswith("wf_")]]; wf.columns=[c[3:] for c in wf.columns]
res={}
# August 2025 state occupation shares are unusable for a mix: not_classified averages 74% and 679 of 1,034 cells are suppressed. Stage 1 uses April and May 2026.
for wave in ["2026-04","2026-05"]:
    soc=pd.read_csv(f"{OUT}/01_soc_{wave}.csv",index_col=0); soc=soc.drop(columns=[c for c in soc.columns if c=="not_classified"],errors="ignore")
    print(f"\n{wave}: suppressed cells {int(soc.isna().sum().sum())} of {soc.size} (small groups in small states); treated as zero, row sums before fill: median {soc.sum(axis=1).median():.1f}")
    soc=soc.fillna(0); soc=soc.div(soc.sum(axis=1),axis=0)*100   # renormalise over classified groups
    common=[g for g in wf.columns if g in soc.columns]; miss=[g for g in soc.columns if g not in wf.columns]
    print(f"\n{wave}: user groups {soc.shape[1]}, matched to workforce {len(common)}; unmatched user groups: {miss}")
    u=soc[common]; w=wf.loc[u.index,common]
    # (i) over-representation ratio, all-state usage-weighted mean of user share / workforce share
    ratio=(u.mean()/w.mean()).sort_values(ascending=False); print("  over-representation among users (mean user share / mean workforce share):"); print("   "+", ".join(f"{g} {r:.1f}x" for g,r in ratio.head(6).items())+" ... "+", ".join(f"{g} {r:.2f}x" for g,r in ratio.tail(3).items()))
    # (ii) does the workforce tech share predict the users' tech share across states?
    d=pd.DataFrame({"user_tech":u["Computer and Mathematical"],"wf_tech":w["Computer and Mathematical"]}).dropna(); d=d.drop("UT",errors="ignore")
    m=smf.ols("user_tech ~ wf_tech",data=d).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["wf_tech"]
    print(f"  users' computer/math share on workforce computer/math share (no Utah): {m.params.wf_tech:+.2f} [{lo:+.2f},{hi:+.2f}] per point, R2 {m.rsquared:.2f}, N {int(m.nobs)}; user share mean {d.user_tech.mean():.1f}%, workforce mean {d.wf_tech.mean():.1f}%")
    # (iii) dissimilarity index per state: half the sum of absolute differences between user and workforce shares
    dis=(u-w).abs().sum(axis=1)/2; print(f"  dissimilarity user vs workforce mix: median {dis.median():.1f} pts, min {dis.min():.1f} ({dis.idxmin()}), max {dis.max():.1f} ({dis.idxmax()})")
    top=dis.sort_values(ascending=False).head(5).round(1).to_dict(); print("  most selected user bases:", top)
    res[wave]={"ratio":ratio.round(2).to_dict(),"user_on_wf_tech":{"coef":round(m.params.wf_tech,3),"ci":[round(lo,3),round(hi,3)],"r2":round(m.rsquared,3),"n":int(m.nobs)},"dissimilarity":dis.round(2).to_dict()}
    pd.concat([u.add_prefix("user_"),w.add_prefix("wf_"),dis.rename("dissimilarity")],axis=1).to_csv(f"{OUT}/03_stage1_{wave}.csv")
json.dump(res,open(f"{OUT}/03_stage1.json","w"),indent=1)
assert res["2026-05"]["ratio"]["Computer and Mathematical"]>3 and abs(pd.read_csv(f"{OUT}/03_stage1_2026-05.csv",index_col=0)["user_Computer and Mathematical"].median()-21)<3, "computer/math should be heavily over-represented among users"
print("CHECK OK")
