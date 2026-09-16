"""Step 04: build the analysis table, one row per country per wave, with every merge audited.

What this does
  1. Starts from step 03's per-wave residuals (automation, expected, residual, AUI).
  2. Adds country traits that do not change between waves:
       - income: GDP per working-age adult (2024), from the Aug 2025 file
       - coding share: the share of a country's usage mapped to Computer & Mathematical occupations (Aug 2025)
       - personal-use share: share of conversations that are personal use (first available: Nov 2025)
       - language group: majority conversation language from the Stanford partner file (>= 60%)
       - Stanford human-agency 'AI handles alone' share (second instrument)
       - Hofstede power distance, individualism, uncertainty avoidance (country-specific rows only;
         regional rows such as 'Arab countries' are kept in a separate file for robustness)
       - GLOBE power-distance practices and participative leadership (62 societies)
  3. Prints, for every merge, how many countries matched and which did not, by name.
  4. Spot-checks India, Denmark and Singapore by printing their full rows.
Why
  Every later regression reads this one table. If a merge is wrong here, everything after is wrong,
  so this is where we look hardest.
"""
import pandas as pd, numpy as np, re, json, os
RAW="data/raw"; OUT="data/processed"
base = pd.read_csv(f"{OUT}/03_partial_by_wave.csv")
pop = pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_country.csv", keep_default_na=False); pop=pop[pop.iso_alpha_3!=""]
iso2to3 = dict(zip(pop.country_code, pop.iso_alpha_3)); name2iso = {n.lower(): i for n,i in zip(pop.country_name, pop.iso_alpha_3)}
report = {}

def audit(label, series, universe):
    have = series.dropna().index; miss = sorted(set(universe) - set(have))
    report[label] = {"matched": int(len(set(universe) & set(have))), "of": int(len(universe)), "missing": miss}
    print(f"{label:34s} matched {len(set(universe)&set(have)):3d} of {len(universe)} thresholded countries; missing: {', '.join(miss) if len(miss)<=25 else str(len(miss))+' countries'}")

universe = sorted(base[base.wave=="2025-08"].geo_id.unique())   # the 111 countries of the exact replication

# ---- income and coding share (Aug 2025 enriched file) ----
aug = pd.read_csv(f"{RAW}/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv", keep_default_na=False, low_memory=False, usecols=["geo_id","geography","facet","variable","cluster_name","value"])
aug["value"]=pd.to_numeric(aug["value"],errors="coerce"); c=aug[aug.geography=="country"]
gdp = c[(c.facet=="country")&(c.variable=="gdp_per_working_age_capita")].set_index("geo_id")["value"].rename("gdp_pwa")
coding = c[(c.facet=="soc_occupation")&(c.variable=="soc_pct")&(c.cluster_name=="Computer and Mathematical")].set_index("geo_id")["value"].rename("coding_share")
audit("GDP per working-age adult", gdp, universe); audit("Coding share (SOC, Aug 2025)", coding, universe)

# ---- personal-use share (Nov 2025 raw file; ISO-2 -> ISO-3) ----
nov = pd.read_csv(f"{RAW}/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv", keep_default_na=False, low_memory=False, usecols=["geo_id","geography","facet","variable","cluster_name","value"])
nov["value"]=pd.to_numeric(nov["value"],errors="coerce"); n=nov[nov.geography=="country"].copy(); n["geo_id"]=n.geo_id.map(iso2to3).fillna(n.geo_id)
uc = n[(n.facet=="use_case")&(n.variable=="use_case_pct")].pivot_table(index="geo_id",columns="cluster_name",values="value",aggfunc="first")
cls = uc[["work","coursework","personal"]].sum(axis=1)
personal = (uc["personal"]/cls*100).rename("personal_share")     # share of classified conversations
audit("Personal-use share (Nov 2025)", personal, universe)

# ---- Stanford partner file: language group and human agency (country rows, ISO-2 lowercase) ----
st = pd.read_csv(f"{RAW}/stanford_clusters.csv", keep_default_na=False, low_memory=False)
sc = st[st.facet_id=="country"].copy(); sc["iso3"]=sc.cluster_name.str.upper().map(iso2to3)
langcols=[col for col in sc.columns if col.startswith("lang:") and col.endswith("_ratio")]
L = sc.set_index("iso3")[langcols].apply(pd.to_numeric, errors="coerce")
top = L.idxmax(axis=1).str.replace("lang:","").str.replace("_ratio",""); topv = L.max(axis=1)
lang_group = pd.Series(np.where(topv>=0.60, top, "mixed"), index=L.index, name="lang_group")
lang_group = lang_group[lang_group.index.notna()]
agency = pd.to_numeric(sc.set_index("iso3")["human_agency_level:ai_handles_alone_ratio"], errors="coerce").rename("agency_ai_alone")
agency = agency[agency.index.notna()]
audit("Language group (Stanford)", lang_group, universe); audit("Human agency: AI handles alone", agency, universe)

# ---- Hofstede (semicolon CSV; own codes; '#NULL!' = missing) ----
hf = pd.read_csv(f"{RAW}/hofstede_6d_2015-08-16.csv", sep=";", keep_default_na=False)
for col in ["pdi","idv","mas","uai","ltowvs","ivr"]: hf[col]=pd.to_numeric(hf[col].replace("#NULL!",np.nan), errors="coerce")
alias = {"u.s.a.":"USA","great britain":"GBR","korea south":"KOR","russia":"RUS","czech rep":"CZE","slovak rep":"SVK","iran":"IRN","vietnam":"VNM",
         "taiwan":"TWN","trinidad and tobago":"TTO","serbia":"SRB","syria":"SYR","venezuela":"VEN","bolivia":"BOL","tanzania":"TZA","moldova":"MDA",
         "cape verde":"CPV","dominican rep":"DOM","el salvador":"SLV","hong kong":"HKG","macedonia rep":"MKD","north macedonia":"MKD","sri lanka":"LKA",
         "south africa":"ZAF","new zealand":"NZL","saudi arabia":"SAU","united arab emirates":"ARE","costa rica":"CRI","puerto rico":"PRI","bosnia":"BIH",
         "turkey":"TUR","türkiye":"TUR","egypt":"EGY","laos":"LAO","north korea":"PRK","brunei":"BRN","ivory coast":"CIV","kyrgyz rep":"KGZ","kyrgyzstan":"KGZ",
         "montenegro":"MNE","belgium":"BEL","germany":"DEU","surinam":"SUR","suriname":"SUR","burkina faso":"BFA","sierra leone":"SLE","tunisia":"TUN","zambia":"ZMB"}
regional = {"africa east","africa west","arab countries"}
def to_iso(nm):
    k=nm.strip().lower()
    if k in regional: return None
    if k in alias: return alias[k]
    if k in name2iso: return name2iso[k]
    # try removing bracketed parts and 'the'
    k2=re.sub(r"\(.*?\)","",k).replace("the ","").strip()
    return name2iso.get(k2) or alias.get(k2)
hf["iso3"]=hf.country.map(to_iso)
# South Africa: Hofstede publishes only the 'South Africa white' sample (PDI 49); his own site reports it as South Africa's score. Used, and stated.
hf.loc[hf.ctr=="SAW","iso3"]="ZAF"; hf.loc[hf.ctr=="SAF","iso3"]=None
# Hofstede's regional scores and the member countries he assigns them to (kept OUT of the primary; used in robustness A)
REGIONAL_MEMBERS = {"Arab countries": ["EGY","IRQ","KWT","LBN","LBY","SAU","ARE"], "Africa East": ["ETH","KEN","TZA","ZMB"], "Africa West": ["GHA","NGA","SLE"]}
reg_rows=[]
for region, members in REGIONAL_MEMBERS.items():
    r=hf[hf.country.str.lower()==region.lower()].iloc[0]
    for m in members: reg_rows.append({"iso3":m,"hof_pdi_regional":r.pdi,"hof_idv_regional":r.idv,"hof_uai_regional":r.uai,"region":region})
hof_reg = pd.DataFrame(reg_rows).set_index("iso3")
unm = hf[hf.iso3.isna() & ~hf.country.str.lower().isin(regional)][["ctr","country","pdi"]]
print("Hofstede rows not mapped to a country code (must be resolved by hand or confirmed as non-countries):"); print(unm.to_string(index=False))
hof = hf.dropna(subset=["iso3"]).set_index("iso3")[["pdi","idv","uai"]].rename(columns={"pdi":"hof_pdi","idv":"hof_idv","uai":"hof_uai"})
hof_regional = hf[hf.country.str.lower().isin(regional)][["ctr","country","pdi","idv","uai"]]
hof_regional.to_csv(f"{OUT}/04_hofstede_regional_rows.csv", index=False)
audit("Hofstede power distance", hof["hof_pdi"], universe)
audit("Hofstede PDI incl. regional (robustness)", pd.concat([hof["hof_pdi"], hof_reg["hof_pdi_regional"]]).groupby(level=0).first(), universe)

# ---- GLOBE (62 societies) ----
gc = pd.read_excel(f"{RAW}/GLOBE-Phase-2-Aggregated-Societal-Culture-Data.xls", sheet_name=0)
gl = pd.read_excel(f"{RAW}/GLOBE-Phase-2-Aggregated-Leadership-Data.xls", sheet_name=0)
galias = {"england":"GBR","germany (west)":"DEU","germany (east)":None,"south africa (black sample)":None,"south africa (white sample)":"ZAF","switzerland (french speaking)":None,
          "french switzerland":None,"usa":"USA","the netherlands":"NLD","netherlands":"NLD","hong kong":"HKG","taiwan":"TWN","south korea":"KOR","iran":"IRN","russia":"RUS",
          "czech republic":"CZE","kuwait":"KWT","qatar":"QAT","zambia":"ZMB","zimbabwe":"ZWE","nigeria":"NGA","namibia":"NAM","el salvador":"SLV","costa rica":"CRI",
          "venezuela":"VEN","bolivia":"BOL","ecuador":"ECU","guatemala":"GTM","colombia":"COL","argentina":"ARG","brazil":"BRA","mexico":"MEX","new zealand":"NZL","australia":"AUS"}
def giso(nm):
    k=str(nm).strip().lower()
    if k in galias: return galias[k]
    return name2iso.get(k) or alias.get(k)
gc["iso3"]=gc["Country Name"].map(giso); gl["iso3"]=gl["Country Name"].map(giso)
print("GLOBE societies not mapped:", gc[gc.iso3.isna()]["Country Name"].tolist())
part_col=[col for col in gl.columns if "participative" in col.lower()]
print("GLOBE leadership columns containing 'participative':", part_col)
globe = gc.dropna(subset=["iso3"]).drop_duplicates("iso3").set_index("iso3")[["Power Distance Societal Practices"]].rename(columns={"Power Distance Societal Practices":"globe_pdi_practices"})
if part_col:
    globe = globe.join(gl.dropna(subset=["iso3"]).drop_duplicates("iso3").set_index("iso3")[[part_col[0]]].rename(columns={part_col[0]:"globe_participative"}))
audit("GLOBE power-distance practices", globe["globe_pdi_practices"], universe)

# ---- assemble ----
traits = pd.concat([gdp, coding, personal, lang_group, agency, hof, hof_reg.drop(columns=["region"]), globe], axis=1)
traits["hof_pdi_extended"] = traits.hof_pdi.fillna(traits.hof_pdi_regional)   # robustness A only
traits.index.name="geo_id"; traits.to_csv(f"{OUT}/04_country_traits.csv")
table = base.merge(traits, left_on="geo_id", right_index=True, how="left")
table["log_gdp"] = np.log(table.gdp_pwa)
table.to_csv(f"{OUT}/04_country_table.csv", index=False)
json.dump(report, open(f"{OUT}/04_merge_report.json","w"), indent=1)

# ---- spot check + check block ----
cols=["geo_id","wave","automation","expected","auto_resid","aui","gdp_pwa","coding_share","personal_share","lang_group","hof_pdi","hof_idv","hof_uai","globe_pdi_practices","globe_participative"]
print("\nSpot check, Aug 2025 rows:"); print(table[(table.wave=="2025-08")&(table.geo_id.isin(["IND","DNK","SGP"]))][cols].round(2).to_string(index=False))
prim = table[(table.wave=="2025-08")].dropna(subset=["auto_resid","hof_pdi","log_gdp","aui","coding_share","personal_share","lang_group"])
print(f"\nCountries available for the primary test (all variables present): {len(prim)}")
assert table.groupby(["geo_id","wave"]).size().max()==1, "duplicate country-wave rows"
assert table.hof_pdi.dropna().between(0,120).all() and table.coding_share.dropna().between(0,100).all() and table.personal_share.dropna().between(0,100).all()
assert (table.loc[(table.wave=="2025-08")&(table.geo_id=="IND"),"hof_pdi"].iloc[0]==77) and (table.loc[(table.wave=="2025-08")&(table.geo_id=="DNK"),"hof_pdi"].iloc[0]==18), "Hofstede spot values (India 77, Denmark 18) not as published"
print("CHECK OK: one row per country-wave; ranges valid; India PDI 77 and Denmark PDI 18 as published")
