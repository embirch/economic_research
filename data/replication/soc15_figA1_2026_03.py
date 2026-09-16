#!/usr/bin/env python3
"""Reproduce the March-2026 report's occupational usage shares (Figure A.1 and the
"+14% API / -18% Claude.ai" sentence, p.7), from the public files plus the O*NET-SOC
2010 -> 2019 crosswalk.

Specification of record (data/ATLAS.md `## Conventions` -> "SOC major groups from onet_task,
and the 2019 recode"):

  1. global `onet_task` level-0 `onet_task_pct`, both surfaces, the three long waves
     (2025-09-15, 2026-01-15, 2026-03-24). Read with keep_default_na=False, na_values=[];
     cast `level` to str after a parquet read.
  2. drop the pseudo-tasks `none` and `not_classified` (different things; both go).
  3. join the task text, lower-cased and stripped, to the shipped O*NET DB 20.1
     `onet_task_statements.csv` (release_2025_09_15/data/intermediate/) -> O*NET-SOC **2010**
     codes.
  4. recode each 2010 code to its O*NET-SOC **2019** code(s) with the O*NET Center crosswalk
     (data/fetch/supplementary_onet.py). Report 5 fn 2 (p.11) says the occupation numbers use
     the 2019 vintage; no release ships a 2019 crosswalk.
  5. allocate a task's pct equally across its distinct 2019 O*NET-SOC codes (the
     `pct_occ_scaled` rule; splitting over Titles instead changes nothing to 4 dp).
  6. renormalise over the matched named mass -- the **classified** base. The
     all-conversation base does not reproduce the figure.

Run from the repository root:  python data/replication/soc15_figA1_2026_03.py
Writes data/replication/results/soc15_figA1_2026_03.csv and prints the audit.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

FRAMES = {
    "aug_ai": "data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
    "aug_api": "data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
    "nov_ai": "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet",
    "nov_api": "data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet",
    "feb_ai": "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet",
    "feb_api": "data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet",
}
STATEMENTS = "data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv"
CROSSWALK = "data/cache/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv"
OUT = Path("data/replication/results/soc15_figA1_2026_03.csv")


def load(path: str) -> pd.DataFrame:
    if path.endswith(".parquet"):
        df = pd.read_parquet(path)
    else:
        df = pd.read_csv(path, keep_default_na=False, na_values=[])
    df["level"] = df["level"].astype(str)
    return df


def major_group_weights(vintage: str) -> pd.DataFrame:
    """key (task text) x SOC major group -> weight, summing to 1 per key."""
    st = pd.read_csv(STATEMENTS, keep_default_na=False)
    st["key"] = st["Task"].str.lower().str.strip()
    pairs = st[["key", "O*NET-SOC Code"]].drop_duplicates().rename(columns={"O*NET-SOC Code": "c2010"})
    if vintage == "2010":
        pairs["code"] = pairs["c2010"]
    else:
        walk = pd.read_csv(CROSSWALK)
        walk.columns = ["c2010", "t2010", "c2019", "t2019"]
        pairs = pairs.merge(walk[["c2010", "c2019"]], on="c2010", how="left")
        missing = int(pairs["c2019"].isna().sum())
        if missing:
            print(f"  crosswalk: {missing} (key, 2010 code) pairs have no 2019 code -- dropped")
        pairs = pairs.dropna(subset=["c2019"])
        pairs["code"] = pairs["c2019"]
    pairs["maj"] = pairs["code"].str[:2]
    h = pairs[["key", "code", "maj"]].drop_duplicates()
    n = h.groupby("key")["code"].nunique().rename("n")
    h = h.join(n, on="key")
    h["w"] = 1.0 / h["n"]
    return h.groupby(["key", "maj"])["w"].sum().reset_index()


def mix(frame_path: str, weights: pd.DataFrame) -> tuple[pd.Series, dict]:
    df = load(frame_path)
    g = df[
        (df.facet == "onet_task")
        & (df.geography == "global")
        & (df.level == "0")
        & (df.variable == "onet_task_pct")
    ]
    s = g[["cluster_name", "value"]].copy()
    s["value"] = s["value"].astype(float)
    named = s[~s.cluster_name.isin(["none", "not_classified", ""])].copy()
    named["key"] = named.cluster_name.str.lower().str.strip()
    m = named.merge(weights, on="key", how="inner")
    m["alloc"] = m.value * m.w
    by = m.groupby("maj")["alloc"].sum()
    audit = dict(
        rows_in=len(named),
        keys_in=named.key.nunique(),
        keys_matched=m.key.nunique(),
        unmatched=named.key.nunique() - m.key.nunique(),
        named_mass=round(float(named.value.sum()), 4),
        matched_mass=round(float(by.sum()), 4),
    )
    return by, audit


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")
    if not Path(CROSSWALK).exists():
        raise SystemExit("missing the crosswalk: run python data/fetch/supplementary_onet.py")

    rows = []
    for vintage in ("2010", "2019"):
        print(f"\n=== O*NET-SOC {vintage} vintage "
              f"({'shipped onet_task_statements.csv' if vintage == '2010' else 'recoded through the crosswalk'})")
        W = major_group_weights(vintage)
        shares = {}
        for name, path in FRAMES.items():
            by, audit = mix(path, W)
            tot = by.sum()
            shares[name] = 100 * by / tot
            print(f"  {name:8} keys in {audit['keys_in']:5} matched {audit['keys_matched']:5} "
                  f"unmatched {audit['unmatched']:3} | named mass {audit['named_mass']:7.4f} "
                  f"| matched mass {audit['matched_mass']:7.4f}")
        S = pd.DataFrame(shares).fillna(0.0)
        for surf, label in (("ai", "Claude.ai"), ("api", "1P API")):
            a, n, f = (S.loc["15", f"{w}_{surf}"] for w in ("aug", "nov", "feb"))
            print(f"  SOC 15 {label:9} {a:7.4f} -> {n:7.4f} -> {f:7.4f}   "
                  f"Aug->Feb {100 * (f / a - 1):+.4f}%")
            rows.append(dict(vintage=vintage, surface=label, aug_2025=a, nov_2025=n, feb_2026=f,
                             rel_aug_to_feb_pct=100 * (f / a - 1)))
        for maj in ("11", "13", "15", "17", "19", "25", "27", "43"):
            for name in FRAMES:
                rows.append(dict(vintage=vintage, surface=name, soc_major=maj,
                                 share_of_classified=float(S.loc[maj, name])))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"\npublished targets (economic-index-2026-03-report p.7): +14% API, -18% Claude.ai;"
          f" 35% Claude.ai Feb-2026 (p.5)")
    print(f"written: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
