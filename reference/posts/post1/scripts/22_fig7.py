"""Figure 7: the gradient inside one country. US states, bachelor's-or-higher share against task-mix-adjusted automation,
in the three waves that publish state data (Aug 2025 thresholded at 100 conversations; Apr and May 2026 all states)."""
import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, statsmodels.api as sm, json
OUT="data/processed"; cen=pd.read_csv(f"{OUT}/20_census_states.csv",index_col=0)
aug=pd.read_csv(f"{OUT}/20_us_states.csv",index_col=0); sub=pd.read_csv(f"{OUT}/21_subregions.csv",index_col=0)
panels=[("August 2025 (week; 43 states)",aug[["auto_resid","bachelors_plus"]])]
for w,lab in [("2026-04","April 2026 (month; 51 states)"),("2026-05","May 2026 (month; 50 states)")]:
    d=sub[(sub.wave==w)&(sub.country=="US")].copy(); d.index=d.index.str[3:]; d["auto_resid"]=sm.OLS(d.automation,sm.add_constant(d.expected)).fit().resid; panels.append((lab,d[["auto_resid"]].join(cen[["bachelors_plus"]],how="inner")))
fig,axes=plt.subplots(1,3,figsize=(13,4.2),sharey=True)
for ax,(lab,d) in zip(axes,panels):
    d=d.dropna(); x=d.bachelors_plus; y=d.auto_resid; f=sm.OLS(y,sm.add_constant(x)).fit(cov_type="HC3")
    zb=f.params.iloc[1]*x.std(ddof=0); ax.scatter(x,y,s=18,color="#2f6f4f",alpha=.8)
    for s_ in d.index: ax.annotate(s_,(x[s_],y[s_]),fontsize=6.5,alpha=.7,xytext=(3,2),textcoords="offset points")
    xs=np.linspace(x.min(),x.max(),10); ax.plot(xs,f.params.iloc[0]+f.params.iloc[1]*xs,color="#333",lw=1)
    ax.set_title(f"{lab}\n{zb:+.2f} pts per SD, R² {f.rsquared:.2f}",fontsize=10); ax.set_xlabel("Adults 25+ with a bachelor's degree or higher, %"); ax.axhline(0,color="#bbb",lw=.6)
axes[0].set_ylabel("Automation share after task mix, points")
plt.tight_layout(); plt.savefig("outputs/figures/fig7_us_states.png",dpi=160); print("wrote fig7")
