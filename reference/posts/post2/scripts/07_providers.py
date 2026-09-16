"""Step 07 (pre-registered H5): three providers, one map? Levels: Anthropic May 2026 Usage Index, Microsoft Q1 2026 AI user share,
OpenAI 2025 messages-per-capita rank; Spearman raw and after the workforce computer/math share. Mix: OpenAI topic shares by state
against Anthropic request level-2 shares mapped to the same five topics (mapping fixed here, before running)."""
import pandas as pd, numpy as np, statsmodels.api as sm, json
from scipy.stats import spearmanr
OUT="data/processed"; L=pd.read_csv(f"{OUT}/01_state_levels.csv",index_col=0); C=pd.read_csv(f"{OUT}/01_covariates.csv",index_col=0).rename(columns={"wf_Computer and Mathematical":"tech"})
d=pd.DataFrame({"anthropic":np.log(L[L.wave=="2026-05"].aui),"microsoft":C.ms_ai_user_share,"openai":-C.openai_rank_2025,"tech":C.tech}).drop(index="UT")
def resid(y,x): return sm.OLS(y,sm.add_constant(x)).fit().resid
res={"levels":{}}
print("Levels, 50 states (Utah excluded). Spearman rank correlations:")
pairs=[("anthropic","microsoft"),("anthropic","openai"),("microsoft","openai")]
for a,b in pairs:
    raw=spearmanr(d[a],d[b]).correlation; r=spearmanr(resid(d[a],d.tech),resid(d[b],d.tech)).correlation; res["levels"][f"{a}-{b}"]={"raw":round(raw,3),"residual_after_tech":round(r,3)}
    print(f"  {a:9s} vs {b:9s}: raw {raw:+.2f} | after workforce tech share {r:+.2f}")
print("  tech share alone explains: Anthropic R2 %.2f, Microsoft R2 %.2f, OpenAI(rank) R2 %.2f" % tuple(sm.OLS(d[v],sm.add_constant(d.tech)).fit().rsquared for v in ["anthropic","microsoft","openai"]))
lv=[v["residual_after_tech"] for v in res["levels"].values()]; res["levels_verdict"]="AGREE ON THE PLACE" if min(lv)>=0.5 else "DO NOT AGREE"; print("  Pre-registered read-out (all pairs >= 0.5 after composition):", res["levels_verdict"])
# ---- mix. Mapping fixed before running (Anthropic L2 cluster -> OpenAI topic)
MAP={"2025-08":{"Technical help":["Provide comprehensive software development assistance across multiple programming domains and technologies","Help develop and debug complete web applications and user interfaces","Provide technical IT support and troubleshooting assistance","Help with automation scripts, robotics programming, and workflow optimization tasks","Assist with game development programming and mobile gaming projects","Help with Docker containerization and cloud infrastructure deployment","Help develop and debug cross-platform mobile applications with Flutter","Help implement cybersecurity measures and secure authentication systems","Analyze and process data from documents, visual media, and business sources"],
  "Writing":["Help edit, improve, and create professional written documents and communications","Assist with creative writing across multiple genres including humor and romantic roleplay","Create comprehensive digital marketing strategies and promotional content","Help with job applications, resumes, and career advancement"],
  "Seeking information":["Provide educational tutoring and academic assistance across multiple subjects and disciplines","Provide technical and academic assistance across scientific research and educational domains","Create comprehensive K-12 educational materials and teaching resources"],
  "Practical Guidance":["Provide comprehensive financial guidance and investment assistance across multiple domains","Provide medical and sports training guidance","Provide comprehensive domestic life and household management guidance","Help plan and organize events, schedules, and travel arrangements","Provide comprehensive legal assistance including immigration and document services","Provide business operations support and strategic consulting services"],
  "Self-expression":["Provide personalized lifestyle advice and recommendations across relationships, spirituality, entertainment, beauty, and parenting"]},
 "2026-05":{"Technical help":["Software Development","DevOps & Infrastructure Operations","Cybersecurity & Threat Detection","Data Analysis & Business Intelligence","Document Processing & Extraction"],
  "Writing":["Content Creation & Copywriting"],"Seeking information":["Research & Intelligence","Knowledge Retrieval & Enterprise Search","Education & Learning"],
  "Practical Guidance":["Hobbies & Lifestyle","Personal AI Assistant","Business Process & Operations","Sales & Revenue Operations","Compliance & Regulatory"],"Self-expression":["Existential, Relational, and Emotional Support","Companionship & General Conversation"]}}
oa=pd.read_csv(f"{OUT}/01_openai_topics_by_state.csv",index_col=0); res["mix"]={}
for wave,mp in MAP.items():
    r=pd.read_csv(f"{OUT}/01_request_L2_{wave}.csv",index_col=0).drop(index="UT",errors="ignore").drop(columns=["not_classified","Other / Unclear"],errors="ignore").fillna(0); r=r.div(r.sum(axis=1),axis=0)*100
    missing=[c for lst in mp.values() for c in lst if c not in r.columns]; assert not missing, missing
    out={}
    for topic,lst in mp.items():
        A=r[lst].sum(axis=1); O=oa["oa_"+topic].reindex(A.index)*100; rho=spearmanr(A,O,nan_policy="omit").correlation
        out[topic]={"spearman":round(rho,3),"anthropic_mean":round(A.mean(),1),"openai_mean":round(O.mean(),1),"anthropic_sd":round(A.std(),2),"openai_sd":round(O.std(),2)}
    res["mix"][wave]=out; med=np.median([v["spearman"] for v in out.values()])
    print(f"\nMix, Anthropic {wave} L2 mapped vs OpenAI 2025 topics, Spearman across states: "+", ".join(f"{t} {v['spearman']:+.2f} (means A {v['anthropic_mean']} / O {v['openai_mean']})" for t,v in out.items())+f" | median {med:+.2f}")
    res["mix"][wave]["median"]=round(med,3)
res["mix_verdict"]="PROPERTY OF THE PLACE" if res["mix"]["2026-05"]["median"]>=0.5 else "PROVIDER USER BASES"; print("Pre-registered read-out (May median >= 0.5):", res["mix_verdict"])
json.dump(res,open(f"{OUT}/07_providers.json","w"),indent=1); print("CHECK OK")
