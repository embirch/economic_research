"""Step 06: the primary test (H1 culture vs H3 development), exactly as pre-registered.

What this does
  0. Tests the regression code on synthetic data: (a) fake data built with a known power-distance effect
     must give that effect back; (b) fake data with no effect must give roughly zero. Then a hand-written
     least-squares calculation (matrix algebra, no library) must agree with statsmodels.
  1. Plots every variable (histograms) and the outcome against each control (scatters), saved to outputs/figures/06_*.
  2. Fits the pre-registered model on the Aug 2025 wave with HC3 robust standard errors:
       auto_resid ~ z(hof_pdi) + log_gdp + aui + coding_share + personal_share + lang_group
  3. Reports each coefficient with its 95% interval, the MDE ((1.96+0.84) x SE), VIFs, and the
     two-variable model (power distance alone; income alone) beside the full one.
  4. Applies the pre-registered decision rule for H1 and prints it.
Why
  This is the one number the post stands on. Everything else is robustness.
Vocabulary
  z(x) = (x - mean) / standard deviation, so a coefficient reads "points of automation per standard deviation".
  HC3 = a robust standard error that does not assume every country is equally noisy.
  VIF = variance inflation factor; how much a control's overlap with others inflates uncertainty (>5 is a warning).
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf, json, os
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
OUT="data/processed"; FIG="outputs/figures"; TAB="outputs/tables"; os.makedirs(FIG,exist_ok=True); os.makedirs(TAB,exist_ok=True)
rng = np.random.default_rng(20260915)

# ---------- 0a. synthetic test: known effect must be recovered ----------
def fit_formula(df, formula):
    return smf.ols(formula, data=df).fit(cov_type="HC3")
n=61
for true_beta in [3.0, 0.0]:
    z=rng.normal(size=n); inc=rng.normal(size=n); ad=rng.normal(size=n)
    y = true_beta*z + 1.0*inc + rng.normal(scale=4, size=n)
    fake=pd.DataFrame({"y":y,"z":z,"inc":inc,"ad":ad})
    ests=[fit_formula(fake.assign(y=true_beta*fake.z+fake.inc+rng.normal(scale=4,size=n)),"y ~ z + inc + ad").params["z"] for _ in range(300)]
    print(f"synthetic test, true effect {true_beta}: mean estimate over 300 draws = {np.mean(ests):.2f} (sd {np.std(ests):.2f})")
    assert abs(np.mean(ests)-true_beta) < 0.15, "regression code does not recover a known effect"

# ---------- 0b. hand-written OLS must agree with the library ----------
t = pd.read_csv(f"{OUT}/04_country_table.csv")
d = t[t.wave=="2025-08"].dropna(subset=["auto_resid","hof_pdi","log_gdp","aui","coding_share","personal_share","lang_group"]).copy()
d["z_pdi"] = (d.hof_pdi - d.hof_pdi.mean())/d.hof_pdi.std(ddof=0)
# DEVIATION (logged 15 Sep): language groups with fewer than 5 countries are collapsed into "other".
# Reason: a group with one country gives that point leverage 1, which makes the HC3 robust error undefined.
small = d.lang_group.value_counts(); d["lang_group"] = d.lang_group.where(d.lang_group.map(small) >= 5, "other")
X = pd.get_dummies(d[["z_pdi","log_gdp","aui","coding_share","personal_share","lang_group"]], columns=["lang_group"], drop_first=True, dtype=float)
X = sm.add_constant(X); y = d["auto_resid"].values
beta_hand = np.linalg.solve(X.values.T @ X.values, X.values.T @ y)           # (X'X)^-1 X'y, the least-squares formula
lib = sm.OLS(y, X).fit(cov_type="HC3")
assert np.allclose(beta_hand, lib.params.values, atol=1e-8), "hand-written OLS disagrees with statsmodels"
print(f"hand-written least squares agrees with statsmodels on all {len(beta_hand)} coefficients")

# ---------- 1. look before modelling ----------
vars_=["auto_resid","hof_pdi","log_gdp","aui","coding_share","personal_share"]
fig,axes=plt.subplots(2,3,figsize=(11,6))
for ax,v in zip(axes.flat,vars_): ax.hist(d[v].dropna(),bins=15,color="#3e6b52"); ax.set_title(v)
plt.tight_layout(); plt.savefig(f"{FIG}/06_histograms.png",dpi=120); plt.close()
fig,axes=plt.subplots(1,5,figsize=(16,3.4))
for ax,v in zip(axes,vars_[1:]):
    ax.scatter(d[v],d.auto_resid,s=14,color="#3e6b52"); ax.set_xlabel(v); ax.set_ylabel("auto_resid")
    for g,r in d.set_index("geo_id").iterrows():
        if g in ["IND","DNK","SGP","JPN","KOR","NGA","IRL","USA"]: ax.annotate(g,(r[v],r.auto_resid),fontsize=7)
plt.tight_layout(); plt.savefig(f"{FIG}/06_scatters.png",dpi=120); plt.close()
print(f"figures saved; estimation sample N = {len(d)}; language groups: {d.lang_group.value_counts().to_dict()}")

# ---------- 2. the pre-registered model ----------
full = fit_formula(d, "auto_resid ~ z_pdi + log_gdp + aui + coding_share + personal_share + C(lang_group)")
pdi_only = fit_formula(d, "auto_resid ~ z_pdi"); inc_only = fit_formula(d, "auto_resid ~ log_gdp + aui")
two = fit_formula(d, "auto_resid ~ z_pdi + log_gdp")
def row(m, name):
    b=m.params[name]; se=m.bse[name]; lo,hi=m.conf_int().loc[name]; mde=(1.96+0.84)*se
    return {"coef":round(b,3),"se":round(se,3),"ci_low":round(lo,3),"ci_high":round(hi,3),"p":round(m.pvalues[name],4),"mde":round(mde,3)}
res = {"n": int(full.nobs), "r2": round(full.rsquared,3),
       "full": {k: row(full,k) for k in ["z_pdi","log_gdp","aui","coding_share","personal_share"]},
       "pdi_only": row(pdi_only,"z_pdi"), "pdi_plus_income": {k: row(two,k) for k in ["z_pdi","log_gdp"]},
       "income_only": {k: row(inc_only,k) for k in ["log_gdp","aui"]}}
# VIFs on the numeric design matrix
Xn = sm.add_constant(d[["z_pdi","log_gdp","aui","coding_share","personal_share"]])
res["vif"] = {c: round(variance_inflation_factor(Xn.values, i),2) for i,c in enumerate(Xn.columns) if c!="const"}
json.dump(res, open(f"{OUT}/06_main_test.json","w"), indent=1)
tab = pd.DataFrame(res["full"]).T; tab.to_csv(f"{TAB}/06_main_model.csv"); 
print("\nFull pre-registered model (Aug 2025, HC3):"); print(tab.to_string())
print("VIF:", res["vif"])
print(f"\nPower distance alone: {res['pdi_only']}"); print(f"Power distance + log income: {res['pdi_plus_income']}"); print(f"Income + adoption only: {res['income_only']}")

# ---------- 3. decision rule, as pre-registered ----------
b=res["full"]["z_pdi"]
support = (b["coef"]>0) and (b["ci_low"]>0) and (b["coef"]>=b["mde"])
verdict = "SUPPORTS H1 (culture): positive, interval excludes zero, above the MDE" if support else ("AGAINST H1: coefficient below the MDE" if b["coef"]<b["mde"] else "INCONCLUSIVE: sign/interval fail the rule but coefficient not below MDE")
print(f"\nPre-registered decision: {verdict}")
inc=res["full"]["log_gdp"]; print(f"Income (log GDP) in the full model: coef {inc['coef']} [{inc['ci_low']}, {inc['ci_high']}], MDE {inc['mde']}")
assert res["n"]>=50, "estimation sample smaller than expected"
print("CHECK OK: synthetic recovery, hand-vs-library agreement, model fitted on the pre-registered specification")
