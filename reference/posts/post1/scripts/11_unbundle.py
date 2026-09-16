"""Step 11 (exploratory, spec in prereg addendum): which components of 'income' carry the income effect?"""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json, subprocess, io
RAW="data/raw"; OUT="data/processed"
t = pd.read_csv(f"{OUT}/04_country_table.csv"); aug = t[t.wave=="2025-08"].copy()
pop = pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_country.csv", keep_default_na=False); pop=pop[pop.iso_alpha_3!=""]
iso2to3=dict(zip(pop.country_code,pop.iso_alpha_3))
# (a)(b)(c)(g) from Nov 2025 primitives
nov = pd.read_csv(f"{RAW}/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv", keep_default_na=False, low_memory=False, usecols=["geo_id","geography","facet","variable","cluster_name","value"])
nov["value"]=pd.to_numeric(nov["value"],errors="coerce"); n=nov[nov.geography=="country"].copy(); n["geo_id"]=n.geo_id.map(iso2to3).fillna(n.geo_id)
def prim(facet,var): return n[(n.facet==facet)&(n.variable==var)].set_index("geo_id")["value"]
extra = pd.DataFrame({"prompt_edu": prim("human_education_years","human_education_years_mean"),
                      "task_hours": prim("human_only_time","human_only_time_mean"),
                      "autonomy": prim("ai_autonomy","ai_autonomy_mean")})
uc = n[(n.facet=="use_case")&(n.variable=="use_case_pct")].pivot_table(index="geo_id",columns="cluster_name",values="value",aggfunc="first")
cls=uc[["work","coursework","personal"]].sum(axis=1); extra["work_share"]=uc["work"]/cls*100; extra["coursework_share"]=uc["coursework"]/cls*100
# (d) English share from Stanford
st = pd.read_csv(f"{RAW}/stanford_clusters.csv", keep_default_na=False, low_memory=False); sc=st[st.facet_id=="country"].copy(); sc["iso3"]=sc.cluster_name.str.upper().map(iso2to3); sc=sc.dropna(subset=["iso3"]).drop_duplicates("iso3")
extra["english_share"]=pd.to_numeric(sc.set_index("iso3")["lang:english_ratio"],errors="coerce")*100
# (e)(f) World Bank, latest non-missing value 2018-2024
def wb(ind):
    url=f"https://api.worldbank.org/v2/country/all/indicator/{ind}?format=json&date=2018:2024&per_page=20000"
    js=json.loads(subprocess.run(["curl","-sL",url],capture_output=True,text=True).stdout)[1]
    d=pd.DataFrame([{"iso3":r["countryiso3code"],"year":int(r["date"]),"v":r["value"]} for r in js if r["value"] is not None])
    return d.sort_values("year").groupby("iso3").v.last()
extra["internet"]=wb("IT.NET.USER.ZS"); extra["tertiary"]=wb("SE.TER.ENRR")
extra.index.name="geo_id"; extra.to_csv(f"{OUT}/11_income_components.csv")
d = aug.merge(extra, left_on="geo_id", right_index=True, how="left")
d.to_csv(f"{OUT}/11_unbundle_table.csv", index=False)
cands=["prompt_edu","task_hours","work_share","coursework_share","english_share","internet","tertiary"]
print("coverage among the 111:", {c:int(d[c].notna().sum()) for c in cands})
def z(s): return (s-s.mean())/s.std(ddof=0)
def run(sample, base_terms, label):
    dd=sample.dropna(subset=["auto_resid","log_gdp","aui","coding_share","personal_share","lang_group"]+cands).copy()
    small=dd.lang_group.value_counts(); dd["lang_group"]=dd.lang_group.where(dd.lang_group.map(small)>=5,"other")
    for c in cands+["log_gdp"]: dd["z_"+c]=z(dd[c])
    if "z_pdi" in base_terms: dd["z_pdi"]=z(dd.hof_pdi)
    base=f"auto_resid ~ z_log_gdp + aui + coding_share + personal_share + C(lang_group)" + (" + z_pdi" if "z_pdi" in base_terms else "")
    m0=smf.ols(base,data=dd).fit(cov_type="HC3"); b0=m0.params["z_log_gdp"]
    rows=[{"model":"income (baseline)","n":int(m0.nobs),"income_coef":round(b0,2),"income_ci":[round(x,2) for x in m0.conf_int().loc["z_log_gdp"]],"candidate":None,"cand_coef":None,"cand_ci":None,"share_of_income_remaining":1.0}]
    for c in cands:
        m=smf.ols(base+f" + z_{c}",data=dd).fit(cov_type="HC3"); b=m.params["z_log_gdp"]; cc=m.params["z_"+c]; lo,hi=m.conf_int().loc["z_"+c]
        rows.append({"model":f"+ {c}","n":int(m.nobs),"income_coef":round(b,2),"income_ci":[round(x,2) for x in m.conf_int().loc["z_log_gdp"]],"candidate":c,"cand_coef":round(cc,2),"cand_ci":[round(lo,2),round(hi,2)],"share_of_income_remaining":round(b/b0,2)})
    m=smf.ols(base+" + "+" + ".join("z_"+c for c in cands),data=dd).fit(cov_type="HC3"); b=m.params["z_log_gdp"]
    rows.append({"model":"+ all candidates","n":int(m.nobs),"income_coef":round(b,2),"income_ci":[round(x,2) for x in m.conf_int().loc["z_log_gdp"]],"candidate":"all","cand_coef":{c:round(m.params["z_"+c],2) for c in cands},"cand_ci":{c:[round(x,2) for x in m.conf_int().loc["z_"+c]] for c in cands},"share_of_income_remaining":round(b/b0,2)})
    print(f"\n{label} (N={int(m0.nobs)}): income coef per SD, baseline {b0:.2f}")
    for r in rows[1:]:
        if r["candidate"]=="all": print(f"  all candidates together: income {r['income_coef']} {r['income_ci']}  remaining {r['share_of_income_remaining']}; candidates: {r['cand_coef']}")
        else: print(f"  + {r['candidate']:16s} income {r['income_coef']:6.2f} {str(r['income_ci']):16s} remaining {r['share_of_income_remaining']:5.2f} | candidate {r['cand_coef']:6.2f} {r['cand_ci']}")
    return rows
res={"hofstede_61": run(d.dropna(subset=["hof_pdi"]), ["z_pdi"], "Hofstede sample with power distance"), "all_111": run(d, [], "All countries, no power distance")}
json.dump(res, open(f"{OUT}/11_unbundle.json","w"), indent=1); print("\nCHECK OK: unbundling models fitted on both samples")
