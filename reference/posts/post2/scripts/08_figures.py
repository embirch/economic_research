"""Figures for post 2."""
import pandas as pd, numpy as np, json, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, statsmodels.api as sm
OUT="data/processed"; FIG="outputs/figures"; G="#2f6f4f"
L=pd.read_csv(f"{OUT}/01_state_levels.csv",index_col=0); C=pd.read_csv(f"{OUT}/05_covariates_plus.csv",index_col=0).rename(columns={"wf_Computer and Mathematical":"tech"})
rep=json.load(open(f"{OUT}/02_replicate.json"))
# Fig 1: elasticity scatter (May) + Gini series
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
d=L[L.wave=="2026-05"].join(C).drop(index="UT"); x=d.tech; y=np.log(d.aui); f=sm.OLS(y,sm.add_constant(x)).fit()
ax[0].scatter(x,y,s=18,color=G); [ax[0].annotate(s,(x[s],y[s]),fontsize=6.5,alpha=.7,xytext=(3,2),textcoords="offset points") for s in d.index]
xs=np.linspace(x.min(),x.max(),10); ax[0].plot(xs,f.params.iloc[0]+f.params.iloc[1]*xs,color="#333",lw=1); ax[0].set_xlabel("Computer and mathematical share of the state's workforce, % (ACS 2023)"); ax[0].set_ylabel("log Usage Index, May 2026"); ax[0].set_title(f"Jobs explain how many: {f.params.iloc[1]:.2f} log points per point of share, R² {f.rsquared:.2f}",fontsize=10)
waves=["2025-08","2025-11","2026-02","2026-04","2026-05"]; gs=[rep["gini"][w]["gini"] for w in waves]; gn=[rep["gini"][w]["gini_no_UT"] for w in waves]
ax[1].plot(waves,gs,marker="o",color=G,label="all 51 states"); ax[1].plot(waves,gn,marker="o",color="#999",ls="--",label="without Utah"); ax[1].set_ylim(0.2,0.4); ax[1].set_ylabel("Gini of the state Usage Index"); ax[1].set_title("Convergence: fast to February 2026, then flat",fontsize=10); ax[1].legend(fontsize=8)
plt.tight_layout(); plt.savefig(f"{FIG}/fig1_jobs_and_gini.png",dpi=160)
# Fig 2: who uses it: users' tech share vs workforce tech share (May); and expected vs observed artifact spread
s1=pd.read_csv(f"{OUT}/03_stage1_2026-05.csv",index_col=0).drop(index="UT",errors="ignore")
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
x=s1["wf_Computer and Mathematical"]; y=s1["user_Computer and Mathematical"]; f=sm.OLS(y,sm.add_constant(x)).fit()
ax[0].scatter(x,y,s=18,color=G); [ax[0].annotate(s,(x[s],y[s]),fontsize=6.5,alpha=.7,xytext=(3,2),textcoords="offset points") for s in s1.index]; xs=np.linspace(x.min(),x.max(),10); ax[0].plot(xs,f.params.iloc[0]+f.params.iloc[1]*xs,color="#333",lw=1)
ax[0].set_xlabel("Computer and mathematical share of the workforce, %"); ax[0].set_ylabel("Computer and mathematical share of Claude's users, %"); ax[0].set_title(f"Who uses it barely follows the workforce: {f.params.iloc[1]:+.2f} per point, R² {f.rsquared:.2f}",fontsize=10)
st=pd.read_csv(f"{OUT}/04_stage2_artifact_2026-05.csv",index_col=0); obs=st[[c for c in st.columns if c.startswith("obs_")]]; exp=st[[c for c in st.columns if c.startswith("exp_")]]
so=obs.std().sort_values(ascending=False).head(12); se=exp.std().reindex([c.replace("obs_","exp_") for c in so.index])
labels=[c[13:-4].replace("_"," ") for c in so.index]; yv=np.arange(len(labels)); ax[1].barh(yv+0.2,so.values,height=0.4,color=G,label="observed across states"); ax[1].barh(yv-0.2,se.values,height=0.4,color="#bbb",label="expected from users' jobs"); ax[1].set_yticks(yv); ax[1].set_yticklabels(labels,fontsize=8); ax[1].invert_yaxis(); ax[1].set_xlabel("Between-state standard deviation of the share, points"); ax[1].set_title("What they make varies far more than their jobs predict",fontsize=10); ax[1].legend(fontsize=8)
plt.tight_layout(); plt.savefig(f"{FIG}/fig2_who_and_what.png",dpi=160)
# Fig 3: catch-up by sub-period
cu=pd.read_csv(f"{OUT}/06_catchup.csv",index_col=0)
fig,ax=plt.subplots(1,3,figsize=(13,4),sharey=True)
for a,(dy,dx,lab) in zip(ax,[("d_aug_nov","log_aug","Aug → Nov 2025"),("d_nov_feb","log_nov","Nov 2025 → Feb 2026 (advertising influx)"),("d_feb_may","log_feb","Feb → May 2026")]):
    x=cu[dx]; y=cu[dy]; f=sm.OLS(y,sm.add_constant(x)).fit(cov_type="HC3"); a.scatter(x,y,s=18,color=G); [a.annotate(s,(x[s],y[s]),fontsize=6,alpha=.6,xytext=(3,2),textcoords="offset points") for s in cu.index]
    xs=np.linspace(x.min(),x.max(),10); a.plot(xs,f.params.iloc[0]+f.params.iloc[1]*xs,color="#333",lw=1); a.axhline(0,color="#bbb",lw=.6); a.set_title(f"{lab}\nslope {f.params.iloc[1]:+.2f} [{f.conf_int().iloc[1,0]:+.2f}, {f.conf_int().iloc[1,1]:+.2f}]",fontsize=10); a.set_xlabel("log Usage Index at start of period")
ax[0].set_ylabel("Change in log Usage Index"); plt.tight_layout(); plt.savefig(f"{FIG}/fig3_catchup.png",dpi=160)
# Fig 4: three providers after composition
d=pd.DataFrame({"Anthropic (log index, May 2026)":np.log(L[L.wave=="2026-05"].aui),"Microsoft (AI user share, Q1 2026)":C.ms_ai_user_share,"OpenAI (−rank, 2025)":-C.openai_rank_2025,"tech":C.tech}).drop(index="UT")
r={k:sm.OLS(d[k],sm.add_constant(d.tech)).fit().resid for k in d.columns[:3]}
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
for a,(p,q) in zip(ax,[("Anthropic (log index, May 2026)","OpenAI (−rank, 2025)"),("Anthropic (log index, May 2026)","Microsoft (AI user share, Q1 2026)")]):
    a.scatter(r[p],r[q],s=18,color=G); [a.annotate(s,(r[p][s],r[q][s]),fontsize=6.5,alpha=.7,xytext=(3,2),textcoords="offset points") for s in d.index]; a.axhline(0,color="#bbb",lw=.6); a.axvline(0,color="#bbb",lw=.6)
    from scipy.stats import spearmanr; a.set_title(f"Residuals after the workforce tech share: Spearman {spearmanr(r[p],r[q]).correlation:+.2f}",fontsize=10); a.set_xlabel(p+", residual"); a.set_ylabel(q+", residual")
plt.tight_layout(); plt.savefig(f"{FIG}/fig4_providers.png",dpi=160); print("wrote 4 figures")
