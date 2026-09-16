"""Step 04, stage 2 (pre-registered H2): do the users' jobs explain what each state asks for and makes?
Expected mix(s) = sum_g user_share(g,s) x US within-group mix(g); observed = the state's overall shares. June 2026, May primary, April replication."""
import pandas as pd, numpy as np, statsmodels.api as sm, json
OUT="data/processed"; j=pd.read_csv("data/raw/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["date_start","geo_id","geo_level","category_name","hierarchy_level","metric_id","value","node_name"]); j["value"]=pd.to_numeric(j.value,errors="coerce")
ov=pd.read_csv(f"{OUT}/01_june_overall.csv",index_col=0); res={}
fam={"artifact":[c for c in ov.columns if c.startswith("artifact_")],"use_case":[c for c in ov.columns if c.startswith("use_case_")],"collaboration":["collaboration_directive_pct","collaboration_feedback_loop_pct","collaboration_task_iteration_pct","collaboration_learning_pct","collaboration_validation_pct"]}
for ds,wave in [("2026-05-01","2026-05"),("2026-04-01","2026-04")]:
    # within-group mix from the UNITED STATES rows (country level publishes all metrics for SOC major groups), not the global rows:
    # the global mix under-predicts advice and email for every US state alike, which is a US-vs-world difference, not a state one.
    g=j[(j.geo_level=="country")&(j.geo_id=="USA")&(j.date_start==ds)&(j.category_name=="soc_occupation")&(j.hierarchy_level.astype(str)=="1")]
    mix=g.pivot_table(index="node_name",columns="metric_id",values="value"); assert mix.shape[0]>=21 and "artifact_explanation_or_answer_pct" in mix.columns, mix.shape
    u=pd.read_csv(f"{OUT}/01_soc_{wave}.csv",index_col=0).drop(columns=["not_classified"],errors="ignore").fillna(0); u=u.div(u.sum(axis=1),axis=0)
    groups=[x for x in u.columns if x in mix.index]; assert len(groups)>=21, groups
    o=ov[ov.wave==wave].drop(columns=["wave"]).drop(index="UT",errors="ignore"); u=u.loc[o.index.intersection(u.index),groups]; o=o.loc[u.index]
    res[wave]={}
    print(f"\n{wave}: {len(u)} states (Utah excluded), {len(groups)} occupation groups")
    for name,cols in fam.items():
        cols=[c for c in cols if c in mix.columns and c in o.columns]; E=u.values@mix.loc[groups,cols].fillna(0).values; E=pd.DataFrame(E,index=u.index,columns=cols); O=o[cols]
        Od=O-O.mean(); Ed=E-E.mean(); x=Ed.values.ravel(); y=Od.values.ravel(); m=sm.OLS(y,sm.add_constant(x)).fit()
        dis=((O-E).abs().sum(axis=1)/2); top=dis.sort_values(ascending=False).head(5)
        # per-state driver: the category with the largest absolute residual
        drivers={s:(O.loc[s]-E.loc[s]).abs().idxmax().replace("artifact_","").replace("_pct","")+f" ({(O.loc[s]-E.loc[s])[(O.loc[s]-E.loc[s]).abs().idxmax()]:+.1f})" for s in top.index}
        var_between=float(np.mean(O.var(ddof=0)))  # mean between-state variance per category
        res[wave][name]={"pooled_r2":round(m.rsquared,3),"slope":round(m.params[1],3),"n_cells":int(len(y)),"dissimilarity_median":round(dis.median(),2),"top5":{k:round(v,2) for k,v in top.items()},"drivers":drivers,"user_mix_dissim_from_global":None}
        print(f"  {name:14s} pooled R2 {m.rsquared:.3f} (slope {m.params[1]:.2f}, {len(y)} cells) | dissimilarity observed vs expected: median {dis.median():.1f} pts, top5 {top.round(1).to_dict()} | drivers {drivers}")
        pd.concat([O.add_prefix("obs_"),E.add_prefix("exp_"),dis.rename("dissimilarity")],axis=1).to_csv(f"{OUT}/04_stage2_{name}_{wave}.csv")
        if name=="artifact":
            # how much do states differ at all? compare the expected mix's own spread to the observed spread
            print(f"     between-state SD of observed shares (mean over categories) {np.sqrt(O.var(ddof=0)).mean():.2f} pts; of expected {np.sqrt(E.var(ddof=0)).mean():.2f} pts; corr of per-category SDs {np.corrcoef(O.std(),E.std())[0,1]:.2f}")
r=res["2026-05"]["artifact"]["pooled_r2"]; verdict="EXPLAINS THE MIX" if r>=0.5 else ("DOES NOT" if r<0.25 else "PARTIAL"); print("\nPre-registered verdict (artifact mix, May):", verdict, f"(pooled R2 {r})"); res["verdict"]=verdict
top5=set(res["2026-05"]["artifact"]["top5"])&set(res["2026-04"]["artifact"]["top5"]); print("largest residual states in both months:", sorted(top5)); res["top5_both_months"]=sorted(top5)
json.dump(res,open(f"{OUT}/04_stage2.json","w"),indent=1); print("CHECK OK")
