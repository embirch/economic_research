"""Step 12 (pre-registered H4): real after jobs? Each persistent cluster's log distinctiveness on the state's user occupation
shares for the groups fixed in the pre-registration; composition if R2 >= 0.5 in both months."""
import pandas as pd, numpy as np, statsmodels.api as sm, json
OUT="data/processed"
G={"Fiction writing":["Arts, Design, Entertainment, Sports, and Media"],"Gaming":["Computer and Mathematical","Arts, Design, Entertainment, Sports, and Media"],"Companionship and conversation":["Arts, Design, Entertainment, Sports, and Media"],"Media discovery":["Arts, Design, Entertainment, Sports, and Media"],
   "Science":["Life, Physical, and Social Science"],"Editing and rewriting":["Management","Business and Financial Operations","Office and Administrative Support"],"Self-presentation writing":["Management","Business and Financial Operations","Office and Administrative Support"],"Research and evidence":["Management","Business and Financial Operations","Office and Administrative Support"],
   "Outdoor and garden":["Farming, Fishing, and Forestry"],"Destination research":["Sales and Related","Personal Care and Service"],"Instructional design":["Educational Instruction and Library"],"Formatted writing":["Educational Instruction and Library"]}
pers=pd.read_csv(f"{OUT}/09_persistent.csv"); res={}
for c in pers.cluster.unique():
    res[c]={}; comp=True
    for m_,wave in [("apr","2026-04"),("may","2026-05")]:
        d=pd.read_csv(f"{OUT}/09_distinctiveness_{m_}.csv",index_col=0); soc=pd.read_csv(f"{OUT}/01_soc_{wave}.csv",index_col=0).drop(columns=["not_classified"],errors="ignore").fillna(0); soc=soc.div(soc.sum(axis=1),axis=0)*100
        y=np.log(d[c]).dropna(); X=soc[G[c]].reindex(y.index).dropna(); y=y.loc[X.index]; m=sm.OLS(y,sm.add_constant(X)).fit(); res[c][m_]=round(m.rsquared,3); comp&=m.rsquared>=0.5
    res[c]["composition"]=bool(comp); print(f"  {c:32s} R2 on user occupation shares: Apr {res[c]['apr']:.2f}, May {res[c]['may']:.2f} → {'COMPOSITION' if comp else 'not composition'}")
json.dump(res,open(f"{OUT}/12_after_jobs.json","w"),indent=1); print("CHECK OK")
