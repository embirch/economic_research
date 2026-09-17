"""Referee re-derivation (brief stage, post3): who carries the SOC 43 -> 15 mass in the
2010 -> 2019 O*NET-SOC recode on the 1P API, per wave, classified base.

Written independently of data/checks/post3_feasibility.py and
data/replication/post2_recode_attribution.py. Computes S-side attribution only; it does NOT
compute or print the within-category concentration C or any Delta-C (the referee stays blind
to those series until the pre-registration is committed).

Rule: equal split of a task node's mass over its distinct (task-key, 2019 code) pairs after
de-duplication on that pair; the 2010 -> 2019 walk applied to each 2010 code held in the
shipped O*NET 20.1 statements. The 'into-15 move' is mass on pairs whose 2010 major group is
not 15 and whose 2019 major group is 15.
"""
import pandas as pd, numpy as np

ROOT = "/workspace/economic_research/data/cache"
files = {
    "Aug25": f"{ROOT}/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
    "Nov25": f"{ROOT}/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet",
    "Feb26": f"{ROOT}/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet",
}
st = pd.read_csv(f"{ROOT}/release_2025_09_15/data/intermediate/onet_task_statements.csv",
                 keep_default_na=False, dtype=str)
st["key"] = st["Task"].str.lower().str.strip()
st["code2010"] = st["O*NET-SOC Code"]
xw = pd.read_csv(f"{ROOT}/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv",
                 keep_default_na=False, dtype=str)
xw = xw.rename(columns={"O*NET-SOC 2010 Code": "code2010", "O*NET-SOC 2019 Code": "code2019",
                        "O*NET-SOC 2019 Title": "title2019"})
pairs = st[["key", "code2010", "Title"]].drop_duplicates().merge(xw[["code2010", "code2019", "title2019"]],
                                                                on="code2010", how="left")
assert pairs.code2019.notna().all(), "unmatched 2010 codes"
pairs["mg2010"] = pairs.code2010.str[:2]
pairs["mg2019"] = pairs.code2019.str[:2]
# allocation unit: (key, 2019 code), de-duplicated
unit = pairs.drop_duplicates(["key", "code2019"])
n_per_key = unit.groupby("key").size().rename("n2019")

def load(p):
    if p.endswith(".csv"):
        d = pd.read_csv(p, keep_default_na=False, na_values=[], dtype=str)
    else:
        d = pd.read_parquet(p)
        d["level"] = d["level"].astype(str)
    g = d[(d.geography == "global") & (d.facet == "onet_task") & (d.level == "0")
          & (d.variable == "onet_task_pct") & (d.platform_and_product == "1P API")].copy()
    g["value"] = g["value"].astype(float)
    return g

rows = []
for w, p in files.items():
    g = load(p)
    named = g[~g.cluster_name.isin(["none", "not_classified"])].copy()
    named["key"] = named.cluster_name.str.lower().str.strip()
    tot_geo = g.value.sum(); named_mass = named.value.sum()
    m = named.merge(unit, on="key", how="left")
    assert m.code2019.notna().all(), f"{w}: unmatched task keys"
    m = m.merge(n_per_key, left_on="key", right_index=True)
    m["alloc"] = m.value / m.n2019          # equal split over de-duplicated (key, 2019 code)
    # de-dup check: keep duplicate-source rows would inflate
    m_dup = named.merge(pairs, on="key", how="left")
    m_dup = m_dup.merge(m_dup.groupby("key").size().rename("n"), left_on="key", right_index=True)
    m_dup["alloc"] = m_dup.value / m_dup.n
    S15_2019 = m.loc[m.mg2019 == "15", "alloc"].sum() / named_mass * 100
    S15_2019_dup = m_dup.loc[m_dup.mg2019 == "15", "alloc"].sum() / named_mass * 100
    S15_2010 = m.loc[m.mg2010 == "15", "alloc"].sum() / named_mass * 100
    into = m[(m.mg2010 != "15") & (m.mg2019 == "15")]
    out = m[(m.mg2010 == "15") & (m.mg2019 != "15")]
    into43 = into[into.mg2010 == "43"]
    by_pair = (into43.groupby(["code2010", "Title", "code2019", "title2019"]).alloc.sum()
               .sort_values(ascending=False) / named_mass * 100)
    rows.append(dict(wave=w, geo_total=round(tot_geo, 4), named_mass=round(named_mass, 4),
                     S15_classified_2010=round(S15_2010, 4), S15_classified_2019=round(S15_2019, 4),
                     S15_2019_if_not_deduped=round(S15_2019_dup, 4),
                     into15_classified=round(into.alloc.sum() / named_mass * 100, 4),
                     into15_geo_total_points=round(into.alloc.sum() / tot_geo * 100, 4),
                     out_of_15_classified=round(out.alloc.sum() / named_mass * 100, 4),
                     n_pairs_into15=into.drop_duplicates(["code2010", "code2019"]).shape[0],
                     n_pairs_outof15=out.drop_duplicates(["code2010", "code2019"]).shape[0]))
    print(f"\n== {w} 1P API, classified base ==")
    print(by_pair.round(4).head(5).to_string())
res = pd.DataFrame(rows)
pd.set_option("display.width", 250)
print("\n", res.to_string(index=False))
a, f = res.iloc[0], res.iloc[2]
print(f"\nAug->Feb relative change in S15, classified: 2019 recode {100*(f.S15_classified_2019/a.S15_classified_2019-1):+.4f}%  |  2010 shipped {100*(f.S15_classified_2010/a.S15_classified_2010-1):+.4f}%")
res.to_csv("/workspace/economic_research/posts/post3/notes/rederivation/recode_43_to_15_attribution.csv", index=False)
