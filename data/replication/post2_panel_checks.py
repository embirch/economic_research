#!/usr/bin/env python3
"""Column-level confirmation of the cuts in posts/post2/BRIEF.md section 8 (LL-11).

Confirms, against the cached files: the six global `onet_task` frames and their named-node
counts, the pairwise and six-frame panels and their mass, the privacy floor, the presence of
`onet_task_count` on BOTH surfaces, the `onet_task::collaboration` intersection on the API,
and the coding / non-coding split under the two O*NET-SOC vintages. Prints the audit and
writes data/replication/results/post2_panel_checks.csv.

Run from the repository root:  python data/replication/post2_panel_checks.py
"""

from __future__ import annotations

import json
import sys
from math import sqrt, tanh
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
OUT = Path("data/replication/results/post2_panel_checks.csv")
DROP = ["none", "not_classified", ""]


def load(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path) if path.endswith(".parquet") else pd.read_csv(
        path, keep_default_na=False, na_values=[])
    df["level"] = df["level"].astype(str)
    return df


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")

    pct, cnt, rows = {}, {}, []
    for name, path in FRAMES.items():
        df = load(path)
        g = df[(df.facet == "onet_task") & (df.geography == "global") & (df.level == "0")]
        p = g[g.variable == "onet_task_pct"].set_index("cluster_name")["value"].astype(float)
        c = g[g.variable == "onet_task_count"].set_index("cluster_name")["value"].astype(float)
        inter = sorted({f for f in df.facet.unique() if f.startswith("onet_task::")})
        rows.append(dict(frame=name, nodes=len(p), pct_sum=round(p.sum(), 4), count_sum=float(c.sum()),
                         min_count=float(c.min()), none_pct=float(p.get("none", float("nan"))),
                         not_classified_pct=float(p.get("not_classified", float("nan"))),
                         named_nodes=len(p.drop(index=[d for d in DROP if d in p.index])),
                         n_onet_task_intersections=len(inter)))
        pct[name] = p.drop(index=[d for d in DROP if d in p.index])
        cnt[name] = c.drop(index=[d for d in DROP if d in c.index])
    frames = pd.DataFrame(rows).set_index("frame")
    print(frames.to_string())

    sets = {k: set(v.index) for k, v in pct.items()}
    panels = {
        "aug_pair": sets["aug_ai"] & sets["aug_api"],
        "nov_pair": sets["nov_ai"] & sets["nov_api"],
        "feb_pair": sets["feb_ai"] & sets["feb_api"],
        "window_aug_nov": sets["aug_ai"] & sets["aug_api"] & sets["nov_ai"] & sets["nov_api"],
        "window_nov_feb": sets["nov_ai"] & sets["nov_api"] & sets["feb_ai"] & sets["feb_api"],
        "six_frame": set.intersection(*sets.values()),
    }
    out = []
    print("\npanel                N     MDE|r|   mass carried in each frame it spans")
    for label, P in panels.items():
        n = len(P)
        mde = tanh((1.959964 + 0.8416212) / sqrt(n - 3))
        mass = {k: round(float(v[sorted(P)].sum()), 4) for k, v in pct.items() if P <= sets[k]}
        print(f"  {label:15} {n:5}  {mde:6.4f}   {mass}")
        out.append(dict(item=label, n=n, mde_abs_r=round(mde, 4), **{f"mass_{k}": v for k, v in mass.items()}))

    panel = sorted(panels["six_frame"])
    print("\nnear-floor counts on the six-frame panel (privacy floor is 15):")
    for k, c in cnt.items():
        cc = c[panel]
        print(f"  {k:8} min {cc.min():5.0f}  n<=15 {int((cc <= 15).sum()):3}  n<=20 {int((cc <= 20).sum()):3}")

    # coding / non-coding split under the two vintages, modal major group
    st = pd.read_csv(STATEMENTS, keep_default_na=False)
    st["key"] = st["Task"].str.lower().str.strip()
    walk = pd.read_csv(CROSSWALK)
    walk.columns = ["c2010", "t2010", "c2019", "t2019"]
    m = (st[["key", "O*NET-SOC Code"]].drop_duplicates().rename(columns={"O*NET-SOC Code": "c2010"})
         .merge(walk[["c2010", "c2019"]], on="c2010", how="left"))
    m["maj10"], m["maj19"] = m.c2010.str[:2], m.c2019.str[:2]
    n = m.groupby("key")["c2019"].nunique().rename("n")
    m = m.join(n, on="key")
    m["w"] = 1.0 / m["n"]

    def modal(col: str) -> pd.Series:
        g = m.groupby(["key", col])["w"].sum().reset_index()
        return g.sort_values("w", ascending=False).drop_duplicates("key").set_index("key")[col]

    mm10, mm19 = modal("maj10"), modal("maj19")
    c10 = [t for t in panel if mm10.get(t) == "15"]
    c19 = [t for t in panel if mm19.get(t) == "15"]
    print(f"\ncoding set on the panel (modal SOC major group 15): 2010 vintage {len(c10)}, "
          f"2019 vintage {len(c19)}, overlap {len(set(c10) & set(c19))}")
    for k in ("feb_ai", "feb_api"):
        print(f"  {k}: panel mass {pct[k][panel].sum():.3f}, of which coding "
              f"{pct[k][c10].sum():.3f} (2010) / {pct[k][c19].sum():.3f} (2019)")
    out.append(dict(item="coding_set_2010", n=len(c10)))
    out.append(dict(item="coding_set_2019", n=len(c19)))
    out.append(dict(item="coding_set_overlap", n=len(set(c10) & set(c19))))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.concat([frames.reset_index().rename(columns={"frame": "item"}), pd.DataFrame(out)],
              ignore_index=True).to_csv(OUT, index=False)
    Path("data/replication/results/post2_panel_tasks.json").write_text(json.dumps(panel, indent=0))
    print(f"\nwritten: {OUT} and data/replication/results/post2_panel_tasks.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
