"""Figures 5-7 for the outliers post."""
import pandas as pd, numpy as np, json, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, statsmodels.api as sm
OUT="data/processed"; FIG="outputs/figures"; G="#2f6f4f"
a=pd.read_csv(f"{OUT}/09_distinctiveness_apr.csv",index_col=0); b=pd.read_csv(f"{OUT}/09_distinctiveness_may.csv",index_col=0); cols=a.columns.intersection(b.columns); a=a[cols]; b=b[cols]; cov=pd.read_csv(f"{OUT}/09_covariates_outliers.csv",index_col=0)
# Fig 5: persistence
fig,ax=plt.subplots(figsize=(6.4,5.6)); x=a.stack(); y=b.stack().reindex(x.index); ok=x.notna()&y.notna(); x=x[ok]; y=y[ok]
both=(x>=1.6)&(y>=1.6); one=((x>=1.6)|(y>=1.6))&~both
ax.scatter(x[~(both|one)],y[~(both|one)],s=8,color="#bbb",alpha=.5,label="all state × cluster cells"); ax.scatter(x[one],y[one],s=22,color="#c9a227",label="outlier in one month only"); ax.scatter(x[both],y[both],s=26,color=G,label="outlier in both months")
for (st,c),v in x[both].items(): ax.annotate(f"{st} {c[:18]}",(v,y[(st,c)]),fontsize=6,xytext=(3,2),textcoords="offset points")
ax.axhline(1.6,color="#999",lw=.6,ls="--"); ax.axvline(1.6,color="#999",lw=.6,ls="--"); ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("Distinctiveness, April 2026 (state share ÷ US share)"); ax.set_ylabel("Distinctiveness, May 2026"); ax.set_title("Half of one month's distinctive uses are gone the next",fontsize=10); ax.legend(fontsize=7,loc="lower right")
plt.tight_layout(); plt.savefig(f"{FIG}/fig5_persistence.png",dpi=160)
# Fig 6: hobbyist signature
LEIS=["Fiction writing","Gaming","Companionship and conversation","Media discovery"]; fig,ax=plt.subplots(figsize=(7,5))
lz=np.log(b[LEIS].mean(axis=1)); d=pd.concat([lz.rename("y"),cov.log_aui],axis=1).dropna(); f=sm.OLS(d.y,sm.add_constant(d.log_aui)).fit()
ax.scatter(np.exp(d.log_aui),np.exp(d.y),s=20,color=G); [ax.annotate(s,(np.exp(d.log_aui[s]),np.exp(d.y[s])),fontsize=7,alpha=.8,xytext=(3,2),textcoords="offset points") for s in d.index]
xs=np.linspace(d.log_aui.min(),d.log_aui.max(),20); ax.plot(np.exp(xs),np.exp(f.params.iloc[0]+f.params.iloc[1]*xs),color="#333",lw=1); ax.set_xscale("log"); ax.set_yscale("log"); ax.axhline(1,color="#bbb",lw=.6)
ax.set_xlabel("Usage Index, May 2026 (log scale)"); ax.set_ylabel("Leisure distinctiveness (mean of four clusters, log scale)"); ax.set_title(f"The hobbyist signature: leisure use is distinctive where adoption is low (slope {f.params.iloc[1]:+.2f}, R² {f.rsquared:.2f})",fontsize=9.5)
plt.tight_layout(); plt.savefig(f"{FIG}/fig6_hobbyist.png",dpi=160)
# Fig 7: two mechanisms
fig,ax=plt.subplots(1,2,figsize=(11,4.4))
for A,(c,v,lab) in zip(ax,[("Outdoor and garden","rural_share","Rural share of population, % (2020 Census)"),("Editing and rewriting","pubadmin_share","Public administration share of employment, % (ACS 2023)")]):
    d=pd.concat([np.log(b[c]).rename("y"),cov[v]],axis=1).dropna(); f=sm.OLS(d.y,sm.add_constant(d[v])).fit(cov_type="HC3")
    A.scatter(d[v],np.exp(d.y),s=20,color=G); [A.annotate(s,(d[v][s],np.exp(d.y[s])),fontsize=6.5,alpha=.8,xytext=(3,2),textcoords="offset points") for s in d.index]; xs=np.linspace(d[v].min(),d[v].max(),20); A.plot(xs,np.exp(f.params.iloc[0]+f.params.iloc[1]*xs),color="#333",lw=1); A.axhline(1,color="#bbb",lw=.6); A.set_yscale("log")
    A.set_xlabel(lab); A.set_ylabel(f"{c}: state share ÷ US share, May 2026"); A.set_title(f"{c}: R² {f.rsquared:.2f}",fontsize=10)
plt.tight_layout(); plt.savefig(f"{FIG}/fig7_mechanisms.png",dpi=160); print("wrote figs 5-7")
