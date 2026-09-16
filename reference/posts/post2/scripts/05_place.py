"""Step 05 (pre-registered H3): what is the place? Residual of log Usage Index (May 2026) after the workforce computer/math share,
on education, median age, broadband and income. Utah excluded. HC3, standardised, MDE with every coefficient."""
import pandas as pd, numpy as np, statsmodels.formula.api as smf, json
OUT="data/processed"; L=pd.read_csv(f"{OUT}/01_state_levels.csv",index_col=0); C=pd.read_csv(f"{OUT}/01_covariates.csv",index_col=0)
FIPS={"01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY"}
a=pd.read_csv("data/raw/census/acsdt1y2023-b01002.dat",sep="|",dtype=str); a=a[a.GEO_ID.str.startswith("0400000US")].copy(); a["state"]=a.GEO_ID.str[-2:].map(FIPS); age=a.dropna(subset=["state"]).set_index("state")["B01002_E001"].astype(float).rename("median_age")
C=C.join(age); C.to_csv(f"{OUT}/05_covariates_plus.csv"); print("median age: DC %.1f, ME %.1f, UT %.1f (Census: 34.8, 44.8, 31.9)" % (age["DC"],age["ME"],age["UT"]))
def z(x): return (x-x.mean())/x.std(ddof=0)
res={}
for wave in ["2026-05","2026-04"]:
    d=L[L.wave==wave].join(C).drop(index="UT",errors="ignore").rename(columns={"wf_Computer and Mathematical":"tech"}); d["log_aui"]=np.log(d.aui)
    base=smf.ols("log_aui ~ tech",data=d).fit(); d["resid"]=base.resid
    for v in ["bachelors_plus","median_age","broadband","log_gdp","tech"]: d["z_"+v]=z(d[v])
    specs={"(a) education alone":"resid ~ z_bachelors_plus","(b) education + age + broadband":"resid ~ z_bachelors_plus + z_median_age + z_broadband","(c) income alone":"resid ~ z_log_gdp","(d) education + income":"resid ~ z_bachelors_plus + z_log_gdp",
           "(e) not residualised: log AUI on tech + education":"log_aui ~ z_tech + z_bachelors_plus"}
    res[wave]={"base_r2":round(base.rsquared,3),"resid_sd":round(d.resid.std(),3)}; print(f"\n{wave}: base R2 (tech share) {base.rsquared:.2f}; residual SD {d.resid.std():.2f} log points; N {len(d)}")
    for k,f in specs.items():
        m=smf.ols(f,data=d).fit(cov_type="HC3"); row={}
        for t in m.params.index[1:]:
            lo,hi=m.conf_int().loc[t]; row[t.replace("z_","")]={"coef":round(m.params[t],3),"ci":[round(lo,3),round(hi,3)],"mde":round(2.8*m.bse[t],3)}
        res[wave][k]={"r2":round(m.rsquared,3),"terms":row}; print(f"  {k:48s} R2 {m.rsquared:.2f} | "+"  ".join(f"{t} {v['coef']:+.3f} [{v['ci'][0]:+.2f},{v['ci'][1]:+.2f}] MDE {v['mde']:.2f}" for t,v in row.items()))
    d[["aui","log_aui","tech","resid","bachelors_plus","median_age","broadband","log_gdp"]].to_csv(f"{OUT}/05_place_{wave}.csv")
e=res["2026-05"]; ea=e["(a) education alone"]["terms"]["bachelors_plus"]; eb=e["(b) education + age + broadband"]["terms"]["bachelors_plus"]
ok=lambda t: (t["ci"][0]>0 or t["ci"][1]<0) and abs(t["coef"])>=t["mde"]
print("\nPre-registered read-out (May): education explains the residual:", ok(ea) and ok(eb), "| income (c,d):", ok(e["(c) income alone"]["terms"]["log_gdp"]) and ok(e["(d) education + income"]["terms"]["log_gdp"]), "| broadband (b):", ok(eb) and ok(e["(b) education + age + broadband"]["terms"]["broadband"]))
json.dump(res,open(f"{OUT}/05_place.json","w"),indent=1); print("CHECK OK")
