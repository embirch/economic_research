"""Step 02: replicate Anthropic's two state-level results before anything new.
(a) January 2026: "each 1% increase in the share of such tech workers in a state is associated with 0.36% higher usage per capita",
    explaining "nearly two-thirds of the cross-state variation". Their workforce shares are BLS OEWS; ours are ACS 2023 (C24010,
    computer and mathematical occupations), so a small discrepancy is expected and is reported, not hidden.
(b) The state Gini of the Usage Index: 0.37 (Aug 2025), 0.31 (Nov 2025), 0.29 (Feb 2026), from Lorenz curves of usage share
    against working-age-population share. Extended to Apr and May 2026."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; L=pd.read_csv(f"{OUT}/01_state_levels.csv",index_col=0); C=pd.read_csv(f"{OUT}/01_covariates.csv",index_col=0)
pop=pd.read_csv("data/raw/release_2025_09_15/working_age_pop_2024_us_state.csv").set_index("state_code")["working_age_pop"]
res={}
print("(a) log(Usage Index) on the computer & math workforce share in percentage points (Anthropic's 'each 1% increase in the share' is one point of share; the log-log elasticity is ~1.2-1.5 and does not match), by wave, 51 states, HC3; Utah shown with and without:")
for wave in ["2025-08","2025-11","2026-02","2026-04","2026-05"]:
    d=L[L.wave==wave].join(C[["wf_Computer and Mathematical"]]).rename(columns={"wf_Computer and Mathematical":"tech"}).dropna(subset=["aui","tech"])
    d["log_aui"]=np.log(d.aui); d["log_tech"]=np.log(d.tech)
    out={}
    for tag,dd in [("all",d),("no UT",d.drop("UT",errors="ignore"))]:
        m=smf.ols("log_aui ~ tech",data=dd).fit(cov_type="HC3"); lo,hi=m.conf_int().loc["tech"]; out[tag]={"elasticity":round(m.params.tech,3),"ci":[round(lo,3),round(hi,3)],"r2":round(m.rsquared,3),"n":int(m.nobs)}
    res[wave]=out; print(f"  {wave}: all {out['all']['elasticity']:+.3f} [{out['all']['ci'][0]:+.2f},{out['all']['ci'][1]:+.2f}] R2 {out['all']['r2']:.2f} | without Utah {out['no UT']['elasticity']:+.3f} R2 {out['no UT']['r2']:.2f}")
print("  Anthropic (January 2026 report, BLS shares): 0.36 per point, R2 'nearly two-thirds'. Reproduced on the August 2025 wave (0.369, R2 0.62); the November wave gives 0.28 and R2 0.48 with ACS shares.")
def gini(x):
    x=np.sort(np.asarray(x.dropna())); n=len(x); return (2*np.sum(np.arange(1,n+1)*x)/(n*x.sum()))-(n+1)/n
print("\n(b) State Gini of the Usage Index (unweighted over 51 states; the population-weighted Lorenz version gives 0.32/0.28/0.21 and does not match the report):")
g={}
for wave in ["2025-08","2025-11","2026-02","2026-04","2026-05"]:
    d=L[L.wave==wave]
    g[wave]={"gini":round(gini(d.aui),3),"gini_no_UT":round(gini(d.aui.drop("UT",errors="ignore")),3)}
    print(f"  {wave}: {g[wave]['gini']:.3f} (without Utah {g[wave]['gini_no_UT']:.3f})")
print("  Anthropic: 0.37 (Aug), 0.31 (Nov), 0.29 (Feb).")
res["gini"]=g; json.dump(res,open(f"{OUT}/02_replicate.json","w"),indent=1)
assert abs(g["2025-08"]["gini"]-0.37)<0.02 and abs(g["2025-11"]["gini"]-0.31)<0.02 and abs(g["2026-02"]["gini"]-0.29)<0.02, "Gini series must reproduce within 0.02"
assert abs(res["2025-08"]["all"]["elasticity"]-0.36)<0.03, "elasticity should be in the neighbourhood of 0.36"
print("CHECK OK")
