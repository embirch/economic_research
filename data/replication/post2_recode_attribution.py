#!/usr/bin/env python3
"""Attribute the SOC 43 -> SOC 15 mass in the 2010 -> 2019 O*NET-SOC recode to source codes.

Context. `data/replication/soc15_figA1_2026_03.py` reproduces the March-2026 report's
"+14% API / -18% Claude.ai" (p.7) only on the **2019** O*NET-SOC vintage; on the shipped
2010 file the API leg is +3.24%. Most of the difference is mass leaving major group 43
(Office and Administrative Support) for major group 15 (Computer and Mathematical). This
script says *which* (2010 code -> 2019 code) pair carries it, on both bases, and what the
2019 API leg becomes without the single task that dominates it.

Specification is identical to soc15_figA1_2026_03.py (drop `none`/`not_classified`, lower-case
text join to the shipped O*NET 20.1 statements, crosswalk recode, equal split over a task's
distinct 2019 codes, renormalise over matched named mass). Two bases are printed for every
mass figure, because they differ by ~10%:

  * "geography total"  -- value * w summed as published, i.e. a share of all sampled records
    on the surface, including `none` and `not_classified`;
  * "classified mass"  -- the same quantity renormalised over the matched named mass, the
    base Figure A.1 itself is on.

Run from the repository root:  python data/replication/post2_recode_attribution.py
Writes data/replication/results/post2_recode_attribution.csv and prints the audit.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

FRAMES = {
    "aug_api": "data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
    "nov_api": "data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet",
    "feb_api": "data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet",
    "aug_ai": "data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
    "nov_ai": "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet",
    "feb_ai": "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet",
}
STATEMENTS = "data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv"
CROSSWALK = "data/cache/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv"
SYSADMIN = ("perform routine system administrative functions such as troubleshooting, "
            "back-ups, and upgrades.")
OUT = Path("data/replication/results/post2_recode_attribution.csv")


def load(path: str) -> pd.DataFrame:
    if path.endswith(".parquet"):
        df = pd.read_parquet(path)
    else:
        df = pd.read_csv(path, keep_default_na=False, na_values=[])
    df["level"] = df["level"].astype(str)
    return df


def task_shares(path: str) -> pd.DataFrame:
    df = load(path)
    g = df[
        (df.facet == "onet_task")
        & (df.geography == "global")
        & (df.level == "0")
        & (df.variable == "onet_task_pct")
    ]
    s = g[["cluster_name", "value"]].copy()
    s["value"] = s["value"].astype(float)
    s = s[~s.cluster_name.isin(["none", "not_classified", ""])]
    s["key"] = s.cluster_name.str.lower().str.strip()
    return s[["key", "value"]]


def pairs_with_weights() -> pd.DataFrame:
    """(key, c2010, c2019, w) where w = 1 / #distinct 2019 codes held by the key.

    The unit of allocation is the (key, **2019** code) pair, as in
    soc15_figA1_2026_03.py: 18 of 20,081 (key, 2010 code, 2019 code) rows are a second 2010
    source for a (key, 2019 code) already present, and counting them twice would inflate the
    matched mass. The 2010 source kept for those 18 is the first; none of them is a 43 -> 15
    mover, so the attribution below is unaffected.
    """
    st = pd.read_csv(STATEMENTS, keep_default_na=False)
    st["key"] = st["Task"].str.lower().str.strip()
    p = (st[["key", "O*NET-SOC Code"]].drop_duplicates()
         .rename(columns={"O*NET-SOC Code": "c2010"}))
    walk = pd.read_csv(CROSSWALK)
    walk.columns = ["c2010", "t2010", "c2019", "t2019"]
    p = p.merge(walk, on="c2010", how="left")
    print(f"  crosswalk merge: {len(p)} (key, 2010 code) rows in, "
          f"{int(p.c2019.isna().sum())} with no 2019 code")
    p = p.dropna(subset=["c2019"])
    dup = len(p) - len(p.drop_duplicates(["key", "c2019"]))
    p = p.drop_duplicates(["key", "c2019"])
    n = p.groupby("key")["c2019"].nunique().rename("n")
    p = p.join(n, on="key")
    p["w"] = 1.0 / p["n"]
    print(f"  allocation units: {len(p)} (key, 2019 code) pairs "
          f"({dup} duplicate-source rows dropped)")
    return p


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")
    for f in [STATEMENTS, CROSSWALK, *FRAMES.values()]:
        if not Path(f).exists():
            raise SystemExit(f"missing {f}: run the data/fetch/ scripts")

    print("=== who holds the sysadmin task in the shipped O*NET 20.1 statements")
    st = pd.read_csv(STATEMENTS, keep_default_na=False)
    st["key"] = st["Task"].str.lower().str.strip()
    holders = (st[st.key == SYSADMIN][["O*NET-SOC Code", "Title", "Task ID"]]
               .drop_duplicates().sort_values("O*NET-SOC Code"))
    for _, r in holders.iterrows():
        print(f"  {r['O*NET-SOC Code']}  {r['Title']}  (Task ID {r['Task ID']})")
    walk = pd.read_csv(CROSSWALK)
    walk.columns = ["c2010", "t2010", "c2019", "t2019"]
    w2019 = walk[walk.c2010.isin(holders["O*NET-SOC Code"])]
    for _, r in w2019.iterrows():
        print(f"  crosswalk: {r.c2010} {r.t2010}  ->  {r.c2019} {r.t2019}")

    P = pairs_with_weights()
    rows = []
    print("\n=== SOC 43 (2010) -> SOC 15 (2019): mass by source code, per frame")
    for name, path in FRAMES.items():
        s = task_shares(path)
        m = s.merge(P, on="key", how="inner")
        m["alloc"] = m.value * m.w
        matched = float(m.alloc.sum())          # classified base for this frame
        move = m[(m.c2010.str[:2] == "43") & (m.c2019.str[:2] == "15")]
        tot_geo = float(move.alloc.sum())
        print(f"  {name:8} matched mass {matched:8.4f} | 43->15 total "
              f"{tot_geo:7.4f} of geography total = {100 * tot_geo / matched:7.4f} of classified")
        by = (move.groupby(["c2010", "t2010", "c2019", "t2019"])["alloc"].sum()
              .sort_values(ascending=False))
        for (c10, t10, c19, t19), v in by.items():
            print(f"      {c10} {t10[:38]:38} -> {c19} {t19[:30]:30} "
                  f"{v:7.4f} geo / {100 * v / matched:7.4f} classified")
            rows.append(dict(frame=name, c2010=c10, t2010=t10, c2019=c19, t2019=t19,
                             mass_geography_total=v, mass_classified=100 * v / matched,
                             frame_matched_mass=matched))
        out = m[(m.c2010.str[:2] == "15") & (m.c2019.str[:2] != "15")]
        ov = float(out.alloc.sum())
        print(f"      (out of 15: {ov:7.4f} geo / {100 * ov / matched:7.4f} classified, "
              f"all of it 15-1199.10 Search Marketing Strategists -> 13-1161.01)")
        rows.append(dict(frame=name, c2010="15-* (out)", c2019="non-15",
                         mass_geography_total=ov, mass_classified=100 * ov / matched,
                         frame_matched_mass=matched))

    print("\n=== SOC 15 share, 2019 vintage, with and without the sysadmin task")
    for surf in ("api", "ai"):
        lv = {}
        for w in ("aug", "nov", "feb"):
            s = task_shares(FRAMES[f"{w}_{surf}"])
            for label, sub in (("with", s), ("without", s[s.key != SYSADMIN])):
                m = sub.merge(P, on="key", how="inner")
                m["alloc"] = m.value * m.w
                share15 = 100 * m.loc[m.c2019.str[:2] == "15", "alloc"].sum() / m.alloc.sum()
                lv[(label, w)] = share15
        for label in ("with", "without"):
            a, n, f = (lv[(label, w)] for w in ("aug", "nov", "feb"))
            print(f"  {surf:3} {label:7} sysadmin task: {a:7.4f} -> {n:7.4f} -> {f:7.4f}"
                  f"   Aug->Feb {100 * (f / a - 1):+.4f}%")
            rows.append(dict(frame=f"{surf}_soc15_2019_{label}_sysadmin", aug_2025=a,
                             nov_2025=n, feb_2026=f, rel_aug_to_feb_pct=100 * (f / a - 1)))

    print("\n=== the sysadmin task's own share (onet_task_pct, geography total)")
    for name, path in FRAMES.items():
        s = task_shares(path)
        v = s.loc[s.key == SYSADMIN, "value"]
        print(f"  {name:8} {float(v.iloc[0]) if len(v) else float('nan'):7.4f}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"\nwritten: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
