"""Step 09 (extension, pre-registered): does power distance raise automation within occupation groups, and
as much in learning-heavy groups as in routine ones?  Uses June 2026 (May), where automation share is
published within each SOC major group by country. For each of four groups, regress the country's automation
share within that group on z(power distance) + log income + AUI (May 2026) + language group. Learning-heavy:
Educational Instruction; Life, Physical and Social Science. Routine: Office and Administrative Support; Sales."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
RAW="data/raw"; OUT="data/processed"
v6 = pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv", keep_default_na=False, low_memory=False,
                 usecols=["geo_id","geo_level","category_name","hierarchy_level","metric_id","value","date_start","node_name"])
v6["value"]=pd.to_numeric(v6["value"],errors="coerce"); m=v6[(v6.date_start=="2026-05-01")]
soc = m[(m.category_name=="soc_occupation")&(m.hierarchy_level.astype(str)=="1")&(m.geo_level=="country")&(m.metric_id=="collaboration_bucket_automation_pct")]
groups = {"Educational Instruction and Library":"learning","Life, Physical, and Social Science":"learning","Office and Administrative Support":"routine","Sales and Related":"routine"}
avail = sorted(soc.node_name.unique()); print("SOC groups with by-country automation (May 2026):", len(avail))
missing=[g for g in groups if g not in avail]; print("requested groups not found by exact name:", missing)
tr = pd.read_csv(f"{OUT}/04_country_traits.csv").set_index("geo_id")
aui = m[(m.geo_level=="country")&(m.category_name=="overall")&(m.metric_id=="usage_per_capita_index")].set_index("geo_id")["value"]
res = {}
for g, kind in groups.items():
    if g not in avail: continue
    y = soc[soc.node_name==g].set_index("geo_id")["value"].rename("auto_g")
    d = pd.concat([y, aui.rename("aui"), tr[["hof_pdi","gdp_pwa","lang_group"]].assign(log_gdp=lambda x: np.log(x.gdp_pwa))], axis=1, join="inner").dropna()
    d["z_pdi"]=(d.hof_pdi-d.hof_pdi.mean())/d.hof_pdi.std(ddof=0)
    small=d.lang_group.value_counts(); d["lang_group"]=d.lang_group.where(d.lang_group.map(small)>=5,"other")
    mod = smf.ols("auto_g ~ z_pdi + log_gdp + aui + C(lang_group)", data=d).fit(cov_type="HC3"); lo,hi=mod.conf_int().loc["z_pdi"]
    res[g] = {"kind": kind, "n": int(mod.nobs), "pdi_coef": round(mod.params["z_pdi"],3), "ci": [round(lo,3), round(hi,3)], "mde": round(2.8*mod.bse["z_pdi"],3), "income_coef": round(mod.params["log_gdp"],3), "income_p": round(mod.pvalues["log_gdp"],4)}
    print(f"{g:40s} [{kind:8s}] N={int(mod.nobs):3d}  PDI coef {mod.params['z_pdi']:+.2f} [{lo:+.2f}, {hi:+.2f}] MDE {2.8*mod.bse['z_pdi']:.2f} | income coef {mod.params['log_gdp']:+.2f} (p={mod.pvalues['log_gdp']:.3f})")
json.dump(res, open(f"{OUT}/09_extension.json","w"), indent=1)
assert len(res)>=2; print("CHECK OK: within-group models fitted")
