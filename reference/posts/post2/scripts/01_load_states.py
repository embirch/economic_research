"""Step 01: load every wave of US-state data from the Anthropic releases, plus Census, Microsoft and OpenAI, into tidy tables.
Waves: Aug 2025 (state_us), Nov 2025 and Feb 2026 (country-state US-XX), Apr and May 2026 (subregion US-XX).
Outputs (data/processed): 01_state_levels.csv (one row per state-wave: usage_pct, aui, working_age_pop; automation share),
01_soc_<wave>.csv (user occupation shares, Aug 2025 and Apr/May 2026 only), 01_request_L1|L2_<wave>.csv (request shares),
01_june_overall.csv (artifact/use-case/collaboration by state-month), 01_covariates.csv (Census workforce occupation shares,
education, broadband, income; Microsoft AI user share; OpenAI rank and topic shares)."""
import pandas as pd, numpy as np, json, re
RAW="data/raw"; OUT="data/processed"
pop=pd.read_csv(f"{RAW}/release_2025_09_15/working_age_pop_2024_us_state.csv").set_index("state_code")["working_age_pop"]
levels=[]; audit={}
# ---------- Aug 2025 (enriched long schema)
a=pd.read_csv(f"{RAW}/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv",keep_default_na=False,low_memory=False,usecols=["geo_id","geography","facet","level","variable","cluster_name","value"])
a["value"]=pd.to_numeric(a.value,errors="coerce"); s=a[(a.geography=="state_us")&(a.geo_id!="not_classified")]
def sv(v): return s[(s.facet=="state_us")&(s.variable==v)].set_index("geo_id")["value"]
auto=s[(s.facet=="collaboration_automation_augmentation")&(s.variable=="automation_pct")].set_index("geo_id")["value"]
lv=pd.DataFrame({"usage_count":sv("usage_count"),"usage_pct":sv("usage_pct"),"aui":sv("usage_per_capita_index"),"automation_pct":auto}); lv["wave"]="2025-08"; levels.append(lv)
soc=s[(s.facet=="soc_occupation")&(s.variable=="soc_pct")].pivot_table(index="geo_id",columns="cluster_name",values="value"); soc.to_csv(f"{OUT}/01_soc_2025-08.csv")
for L in (1,2):
    r=s[(s.facet=="request")&(s.variable=="request_pct")&(s.level==L)].pivot_table(index="geo_id",columns="cluster_name",values="value"); r.to_csv(f"{OUT}/01_request_L{L}_2025-08.csv"); audit[f"2025-08 request L{L}"]=[int(r.shape[0]),int(r.shape[1])]
audit["2025-08"]={"states":int(lv.aui.notna().sum()),"soc states":int(soc.shape[0]),"soc groups":int(soc.shape[1])}
# ---------- Nov 2025, Feb 2026 (raw long schema, country-state)
for wave,path in [("2025-11",f"{RAW}/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"),("2026-02",f"{RAW}/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv")]:
    d=pd.read_csv(path,keep_default_na=False,low_memory=False,usecols=["geo_id","geography","facet","level","variable","cluster_name","value"]); d["value"]=pd.to_numeric(d.value,errors="coerce")
    s=d[(d.geography=="country-state")&(d.geo_id.str.startswith("US-"))].copy(); s["geo_id"]=s.geo_id.str[3:]
    s=s[s.geo_id.isin(pop.index)]   # drops territories (PR, GU, VI) and unknown codes; named below
    dropped=sorted(set(d[(d.geography=="country-state")&(d.geo_id.str.startswith("US-"))].geo_id.str[3:])-set(pop.index))
    uc=s[(s.facet=="country-state")&(s.variable=="usage_count")].set_index("geo_id")["value"]
    # Usage Index rebuilt to the convention verified in post 1: usage share over the states in the population file / population share
    up=uc/uc.sum(); ps=pop/pop.sum(); aui=(up/ps.reindex(up.index))
    col=s[(s.facet=="collaboration")&(s.variable=="collaboration_pct")]; classified=col[~col.cluster_name.isin(["not_classified","none"])].groupby("geo_id").value.sum()
    auto=(col[col.cluster_name.isin(["directive","feedback loop"])].groupby("geo_id").value.sum()/classified*100)
    lv=pd.DataFrame({"usage_count":uc,"usage_pct":up*100,"aui":aui,"automation_pct":auto}); lv["wave"]=wave; levels.append(lv)
    for L in (1,2):
        r=s[(s.facet=="request")&(s.variable=="request_pct")&(s.level==L)].pivot_table(index="geo_id",columns="cluster_name",values="value"); r.to_csv(f"{OUT}/01_request_L{L}_{wave}.csv"); audit[f"{wave} request L{L}"]=[int(r.shape[0]),int(r.shape[1])]
    audit[wave]={"states":int(lv.aui.notna().sum()),"dropped_non_states":dropped,"usage_count_min":float(uc.min())}
# ---------- Apr, May 2026 (wide schema, subregion)
j=pd.read_csv(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv",keep_default_na=False,low_memory=False,usecols=["date_start","geo_id","geo_level","category_name","hierarchy_level","metric_id","value","node_name"])
j["value"]=pd.to_numeric(j.value,errors="coerce"); js=j[(j.geo_level=="subregion")&(j.geo_id.str.startswith("US-"))].copy(); js["geo_id"]=js.geo_id.str[3:]; js=js[js.geo_id.isin(pop.index)]
overall=[]
for ds,wave in [("2026-04-01","2026-04"),("2026-05-01","2026-05")]:
    m=js[js.date_start==ds]; ov=m[m.category_name=="overall"].pivot_table(index="geo_id",columns="metric_id",values="value")
    lv=pd.DataFrame({"usage_pct":ov.get("usage_pct"),"aui":ov.get("usage_per_capita_index"),"automation_pct":ov.get("collaboration_bucket_automation_pct")}); lv["wave"]=wave; levels.append(lv)
    o=ov.copy(); o["wave"]=wave; overall.append(o)
    soc=m[(m.category_name=="soc_occupation")&(m.hierarchy_level.astype(str)=="1")&(m.metric_id=="pct")].pivot_table(index="geo_id",columns="node_name",values="value"); soc.to_csv(f"{OUT}/01_soc_{wave}.csv")
    for L in (1,2):
        r=m[(m.category_name=="request")&(m.hierarchy_level.astype(str)==str(L))&(m.metric_id=="pct")].pivot_table(index="geo_id",columns="node_name",values="value"); r.to_csv(f"{OUT}/01_request_L{L}_{wave}.csv"); audit[f"{wave} request L{L}"]=[int(r.shape[0]),int(r.shape[1])]
    audit[wave]={"states":int(lv.aui.notna().sum()),"soc states":int(soc.shape[0]),"soc groups":int(soc.shape[1])}
pd.concat(overall).to_csv(f"{OUT}/01_june_overall.csv")
L=pd.concat(levels); L.index.name="state"; L.to_csv(f"{OUT}/01_state_levels.csv")
# ---------- Census C24010: workforce occupation shares (male + female), mapped to SOC major groups
FIPS={"01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY"}
c=pd.read_csv(f"{RAW}/census/acsdt1y2023-c24010.dat",sep="|",dtype=str); c=c[c.GEO_ID.str.startswith("0400000US")].copy(); c["state"]=c.GEO_ID.str[-2:].map(FIPS); c=c.dropna(subset=["state"]).set_index("state").apply(pd.to_numeric,errors="coerce")
male={"Management":[5],"Business and Financial Operations":[6],"Computer and Mathematical":[8],"Architecture and Engineering":[9],"Life, Physical, and Social Science":[10],"Community and Social Service":[12],"Legal":[13],"Educational Instruction and Library":[14],"Arts, Design, Entertainment, Sports, and Media":[15],"Healthcare Practitioners and Technical":[16],"Healthcare Support":[20],"Protective Service":[21],"Food Preparation and Serving Related":[24],"Building and Grounds Cleaning and Maintenance":[25],"Personal Care and Service":[26],"Sales and Related":[28],"Office and Administrative Support":[29],"Farming, Fishing, and Forestry":[31],"Construction and Extraction":[32],"Installation, Maintenance, and Repair":[33],"Production":[35],"Transportation and Material Moving":[36,37]}
wf=pd.DataFrame({g:sum(c[f"C24010_E{k:03d}"]+c[f"C24010_E{k+36:03d}"] for k in ks) for g,ks in male.items()},index=c.index)
tot=c["C24010_E001"]; wf=wf.div(tot,axis=0)*100; assert (wf.sum(axis=1).between(99.5,100.5)).all(), "workforce shares must sum to 100"
wf.columns=["wf_"+x for x in wf.columns]
# ---------- covariates from post 1 (Census education, broadband, income; state GDP)
cov=pd.read_csv(f"{RAW}/census_post1/../../../post1/data/processed/20_census_states.csv",index_col=0) if False else pd.read_csv("../post1/data/processed/20_census_states.csv",index_col=0)
ms=pd.read_csv(f"{RAW}/microsoft_ai_diffusion/US/State_Rankings_2026Q1.csv",encoding="utf-8-sig").set_index("State Abbr")["AI User Share"].rename("ms_ai_user_share")
oa=pd.read_csv(f"{RAW}/openai_signals/public_release_csv/usa_share_of_messages_by_state_2025_rank.csv").set_index("state_code")["rank"].rename("openai_rank_2025")
oat=pd.read_csv(f"{RAW}/openai_signals/public_release_csv/usa_share_of_messages_by_topic_state_2025.csv").pivot_table(index="state_code",columns="topic",values="share_of_messages"); oat.columns=["oa_"+x for x in oat.columns]; oat.to_csv(f"{OUT}/01_openai_topics_by_state.csv")
C=pd.concat([wf,cov,ms,oa],axis=1); C.index.name="state"; C.to_csv(f"{OUT}/01_covariates.csv")
audit["covariates"]={"states":int(len(C)),"missing_by_source":{k:int(C[k].isna().sum()) for k in ["wf_Computer and Mathematical","bachelors_plus","ms_ai_user_share","openai_rank_2025"]},"openai_topics":list(oat.columns)}
print(json.dumps(audit,indent=1))
print("Spot checks: DC computer/math workforce share %.1f%% (ACS ~7); CA %.1f; MS %.1f | Microsoft DC %.1f MD %.1f | OpenAI DC rank %d VA rank %d" % (wf.loc["DC","wf_Computer and Mathematical"],wf.loc["CA","wf_Computer and Mathematical"],wf.loc["MS","wf_Computer and Mathematical"],ms["DC"],ms["MD"],oa["DC"],oa["VA"]))
print("AUI by wave (DC, CA, WV):"); print(L.reset_index().pivot_table(index="state",columns="wave",values="aui").loc[["DC","CA","UT","WV"]].round(2).to_string())
chk=L[L.wave=="2025-08"].aui; assert abs(chk["DC"]-3.82)<0.02 and abs(chk["UT"]-3.78)<0.02, "Aug 2025 AUI must match the report (DC 3.82, UT 3.78)"
assert all(v["states"]>=50 for k,v in audit.items() if re.match(r"^\d{4}-\d{2}$",k)), "every wave should have >=50 states"
print("CHECK OK")
