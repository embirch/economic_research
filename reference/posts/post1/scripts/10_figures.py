"""Step 10: the four figures for the post, from processed tables only (no recomputation).
  Fig 1  Anthropic's Figure 2.11 reproduced, plus the same plot on the four later waves.
  Fig 2  Task-mix-adjusted automation residual against power distance, raw (the pattern people would see)
         and after income is removed (the pattern that survives), with the off-diagonal countries labelled.
  Fig 3  The primary coefficients: power distance alone, with income, full model; with intervals and MDE.
  Fig 4  Within occupation groups (June 2026): income coefficient by group, learning-heavy vs routine.
"""
import pandas as pd, numpy as np, json, statsmodels.api as sm
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
OUT="data/processed"; FIG="outputs/figures"
G="#3e6b52"; T="#c9a86a"; K="#333"
d = pd.read_csv(f"{OUT}/03_partial_by_wave.csv"); stats=json.load(open(f"{OUT}/03_partial_stats.json"))["by_wave"]
# Fig 1
waves=["2025-08","2025-11","2026-02","2026-04","2026-05"]; fig,axes=plt.subplots(1,5,figsize=(17,3.6),sharey=True)
for ax,w in zip(axes,waves):
    x=d[d.wave==w]; ax.scatter(x.aui_resid,x.auto_resid,s=12,color=G,alpha=.8)
    b=np.polyfit(x.aui_resid,x.auto_resid,1); xs=np.linspace(x.aui_resid.min(),x.aui_resid.max(),50); ax.plot(xs,np.polyval(b,xs),color=T,lw=2)
    ax.set_title(f"{w}\nslope {stats[w]['slope']:.2f}, R² {stats[w]['r2']:.2f}, N {stats[w]['n']}",fontsize=9); ax.set_xlabel("Usage Index, residual after task mix",fontsize=8)
    for g in ["IND","DNK","SGP","USA","NGA","JPN"]:
        r=x[x.geo_id==g]
        if len(r): ax.annotate(g,(r.aui_resid.iloc[0],r.auto_resid.iloc[0]),fontsize=7)
axes[0].set_ylabel("Automation share, residual after task mix (points)")
plt.suptitle("Figure 1. Anthropic's Figure 2.11 reproduced with its released code (Aug 2025) and repeated on later waves",fontsize=10); plt.tight_layout(); plt.savefig(f"{FIG}/fig1_replication_by_wave.png",dpi=150); plt.close()
# Fig 2
t=pd.read_csv(f"{OUT}/04_country_table.csv"); a=t[(t.wave=="2025-08")].dropna(subset=["auto_resid","hof_pdi","log_gdp"]).copy()
a["resid_after_income"]=sm.OLS(a.auto_resid,sm.add_constant(a.log_gdp)).fit().resid
fig,axes=plt.subplots(1,2,figsize=(12,4.6))
for ax,col,title in [(axes[0],"auto_resid","Before removing income: power distance appears to matter"),(axes[1],"resid_after_income","After removing income: it does not")]:
    ax.scatter(a.hof_pdi,a[col],s=16,color=G); b=np.polyfit(a.hof_pdi,a[col],1); xs=np.linspace(a.hof_pdi.min(),a.hof_pdi.max(),50); ax.plot(xs,np.polyval(b,xs),color=T,lw=2)
    for g in ["SGP","JPN","KOR","ARE","SAU","IRL","NZL","DNK","IND","NGA","USA","MEX"]:
        r=a[a.geo_id==g]
        if len(r): ax.annotate(g,(r.hof_pdi.iloc[0],r[col].iloc[0]),fontsize=7)
    ax.set_xlabel("Hofstede power distance (0–100)"); ax.set_ylabel("Automation share, task-mix adjusted (points)"); ax.set_title(title,fontsize=10); ax.axhline(0,color="#bbb",lw=.8)
plt.suptitle("Figure 2. Authority norms against delegation, 61 countries, August 2025",fontsize=10); plt.tight_layout(); plt.savefig(f"{FIG}/fig2_pdi_before_after_income.png",dpi=150); plt.close()
# Fig 3
m=json.load(open(f"{OUT}/06_main_test.json"))
rows=[("Power distance alone",m["pdi_only"]),("Power distance + log income",m["pdi_plus_income"]["z_pdi"]),("Full pre-registered model",m["full"]["z_pdi"])]
fig,ax=plt.subplots(figsize=(8,3.4))
for i,(lab,r) in enumerate(rows):
    ax.errorbar(r["coef"],i,xerr=[[r["coef"]-r["ci_low"]],[r["ci_high"]-r["coef"]]],fmt="o",color=G,capsize=4)
    ax.plot([-r["mde"],r["mde"]],[i-.18,i-.18],color=T,lw=3,alpha=.7)
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in rows]); ax.axvline(0,color=K,lw=.8); ax.invert_yaxis()
ax.set_xlabel("Points of automation per standard deviation of power distance (95% interval; gold bar = minimum detectable effect)")
ax.set_title("Figure 3. The power-distance coefficient, before and after income",fontsize=10); plt.tight_layout(); plt.savefig(f"{FIG}/fig3_coefficients.png",dpi=150); plt.close()
# Fig 4 (revised 15 Sep): education coefficient on within-group automation share, all SOC groups, May 2026
r=pd.read_csv(f"{OUT}/14_all_groups.csv"); may=r[r.month=="2026-05"].sort_values("tert_coef")
fig,ax=plt.subplots(figsize=(9,6.2))
for i,row in enumerate(may.itertuples()):
    sig = row.tert_hi < 0
    ax.errorbar(row.tert_coef,i,xerr=[[row.tert_coef-row.tert_lo],[row.tert_hi-row.tert_coef]],fmt="o",color=G if sig else T,capsize=3)
ax.set_yticks(range(len(may))); ax.set_yticklabels([f"{g[:38]}  (auto {a:.0f}%)" for g,a in zip(may.group,may.global_automation)],fontsize=8); ax.invert_yaxis(); ax.axvline(0,color=K,lw=.8)
ax.set_xlabel("Points of automation share within the group per standard deviation of tertiary enrolment (95% interval); group's global automation share in brackets")
ax.set_title("Figure 4. Where education lowers delegation: all 19 occupation groups with enough countries, May 2026",fontsize=10)
plt.tight_layout(); plt.savefig(f"{FIG}/fig4_within_groups.png",dpi=150); plt.close()
print("CHECK OK: four figures written"); import os; print(sorted(os.listdir(FIG)))

# Fig 5 (added 15 Sep): how the income coefficient shrinks as its components enter (all-country sample)
u=json.load(open(f"{OUT}/11_unbundle.json"))["all_111"]
labs=[r["model"] for r in u]; vals=[r["income_coef"] for r in u]; los=[r["income_ci"][0] for r in u]; his=[r["income_ci"][1] for r in u]
fig,ax=plt.subplots(figsize=(8.5,4.2))
for i,(l,v,lo,hi) in enumerate(zip(labs,vals,los,his)):
    ax.errorbar(v,i,xerr=[[v-lo],[hi-v]],fmt="o",color=G if l in ("income (baseline)","+ all candidates") else T,capsize=3)
ax.set_yticks(range(len(labs))); ax.set_yticklabels([l.replace("_"," ") for l in labs],fontsize=9); ax.invert_yaxis(); ax.axvline(0,color=K,lw=.8)
ax.set_xlabel("Income coefficient on adjusted automation (points per standard deviation of log GDP), 95% interval")
ax.set_title("Figure 5. The income effect shrinks when internet access and tertiary enrolment enter, and not otherwise (100 countries)",fontsize=10)
plt.tight_layout(); plt.savefig(f"{FIG}/fig5_unbundling.png",dpi=150); plt.close(); print("fig5 written")

# Fig 6 (added 15 Sep): education coefficient by work activity, May 2026
a=pd.read_csv(f"{OUT}/16_activities.csv"); may=a[a.month=="2026-05"].sort_values("tert")
fig,ax=plt.subplots(figsize=(9,6.4))
for i,row in enumerate(may.itertuples()):
    sig = (row.tert_hi < 0) or (row.tert_lo > 0)
    ax.errorbar(row.tert,i,xerr=[[row.tert-row.tert_lo],[row.tert_hi-row.tert]],fmt="o",color=G if sig else T,capsize=3)
ax.set_yticks(range(len(may))); ax.set_yticklabels([f"{g[:44]}  (auto {x:.0f}%)" for g,x in zip(may.activity,may.global_auto)],fontsize=8); ax.invert_yaxis(); ax.axvline(0,color=K,lw=.8)
ax.set_xlabel("Points of automation share within the activity per standard deviation of tertiary enrolment (95% interval)")
ax.set_title("Figure 6. Selective delegation: education lowers handover of strategy, creative and information work and raises it for computer work (May 2026)",fontsize=9.5)
plt.tight_layout(); plt.savefig(f"{FIG}/fig6_activities.png",dpi=150); plt.close(); print("fig6 written")
