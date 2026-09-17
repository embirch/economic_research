"""post1 · 02 · Frames, joins, merge audits, the analysis set, the wage quartiles, the plots,
and the replication assertions that license the estimator.

WHAT. This script builds, once per wave, the one table every later script reads: a row per named
global `onet_task` node with its usage weight, its seven collaboration-pattern counts and per-cent
rows, its per-task automation share p_i and classified base n_i, its holder occupations, its hourly
wage under the three multi-holder rules on both wage sources, its SOC major group under both O*NET
vintages, its `use_case` cells where the facet exists, its Seychelles share in November and its
Feb–Mar-2025 ratios where the fourth window reaches it. It then draws the usage-weighted wage
quartiles, prints every merge audit (rows in, matched, unmatched by name, dropped mass) and asserts
the published numbers post1 extends before any estimate is formed.

WHY. `posts/post1/prereg/prereg.md` (content c9b1b45, committed 066b761) fixes the construction:
§Definitions 1–4 (the outcome, D, Δ_W, the predictors, the quartiles), P9 (every sample and
exclusion rule), §5 (the frames and the replication-first rule) and the "plot before modelling"
clause. Nothing here is estimated: no quartile automation share, no D, no Δ_W, no leg. The
pre-registration's §5 requires that this script re-assert the three published wave splits, the
Figure 2.11 triple from Anthropic's own released library, the §8(iii) internal check and the
analysis-set counts, masses, quartile boundaries and Kish N **before** script 03 forms an estimate.

SPECIFICATION OF RECORD, and the thresholds this post applies itself.
  · Frames: C1 `release_2025_09_15` (4–11 Aug 2025), C2 `release_2026_01_15` (13–20 Nov 2025),
    C3 `release_2026_03_24` (5–12 Feb 2026); `onet_task::collaboration` and `onet_task` at
    `geography == 'global'`, `level == '0'`, same-wave `onet_task_pct` weights (prereg §5).
  · Outcome p_i = (`directive` + `feedback loop`) ÷ the five classified patterns from
    `onet_task_collaboration_count`; `none` and `not_classified` patterns are out of the
    denominator, as Anthropic's released `collaboration_task_regression` does, and the `none` share
    of the node is carried beside every share so the base is never implicit (prereg §1).
  · Task → O*NET-SOC through C5 (`onet_task_statements.csv`, O*NET DB 20.1) on the **lower-cased,
    stripped** task text, de-duplicated on that key before the merge.
  · Wage: C6 `wage_data.csv` `MedianSalary`, joined on the **full 10-character `O*NET-SOC Code` →
    `SOCcode`** (Anthropic's `plots.ipynb` cell 26 key). **Thresholds applied by us, and labelled
    as ours:** `MedianSalary > 100` applied **before** the join (Anthropic applies it after), the
    ÷ 2080 hourly conversion, and the file's own $208,000 top code ($100.00/hr).
  · Multi-holder wage rule W1: **employment-weighted mean over holder occupations** (BLS-EP
    `Employment 2025` on the 7-character `occ_code`) is **primary**; the equal-split mean and the
    modal holder are carried beside it. Where no holder carries an employment figure the rule
    degenerates to the equal-split mean, and that count is printed.
  · Allocation rules: A1 (share statistics) equal split over the distinct 2019 holder codes, the
    released `soc15_figA1_2026_03.py` convention; A2 (each task in exactly one group) the holder
    with the largest BLS-EP employment, ties to the lexicographically smallest 10-character code.
    V1: the wage is attached on the shipped **2010** codes; **groupings are reported on the 2019
    recode as primary** with the 2010 grouping beside it.
  · Analysis set S1: a named global task node with a C6 wage **and** at least one classified-pattern
    cell. X1 (wage, no classified cell) and X2 (classified cell, no wage) are **dropped explicitly,
    never zeroed**, and their counts and masses are printed and asserted.
  · Quartiles: boundaries on **usage-weighted** wage over that wave's analysis set on the primary
    wage rule, cut at the 25th / 50th / 75th percentile of cumulative usage mass. Ties in the wage
    are split at the boundary, which is what makes each quartile exactly a quarter of the mass; the
    mass sitting at a boundary wage is printed, because Q1 and Q4 are then not defined by the wage
    alone.
  · Every load: `keep_default_na=False, na_values=[]`, every non-`value` column cast to `str`,
    `cluster_name` split on the **last** `::`, `geography` filtered before any `geo_id` use
    (`NA` is Namibia, `NONE` a real pseudo-geography — prereg E1).

OUTPUT. `/tmp/post1/build_<wave>.parquet` (scratch, rebuilt by re-running this script in ~1 min),
diagnostic plots in `posts/post1/outputs/diagnostics/`, a console log, and
`posts/post1/data/processed/build_facts.json` with every count, mass, boundary and Kish N the later
scripts and `results.json` quote. Downstream scripts import `get_build` and `quartiles` from here
rather than re-implementing the joins.
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[3]
SCRATCH = pathlib.Path("/tmp/post1")
SCRATCH.mkdir(parents=True, exist_ok=True)
PROCESSED = ROOT / "posts/post1/data/processed"
DIAG = ROOT / "posts/post1/outputs/diagnostics"

AUTO = ["directive", "feedback loop"]
AUGM = ["learning", "task iteration", "validation"]
CLASSIFIED = AUTO + AUGM
RESID = ["none", "not_classified"]
PATTERNS = CLASSIFIED + RESID
UC_CATS = ["work", "personal", "coursework", "not_classified", "none"]
C10_PATTERNS = ["directive", "feedback_loop", "learning", "task_iteration", "validation"]

WAVES = {
    "aug2025": dict(
        release="release_2025_09_15",
        frame=ROOT / "data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
        api=ROOT / "data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
        window="4–11 Aug 2025", platform="Claude AI (Free and Pro)"),
    "nov2025": dict(
        release="release_2026_01_15",
        frame=ROOT / "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet",
        api=ROOT / "data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet",
        window="13–20 Nov 2025", platform="Claude AI (Free and Pro)"),
    "feb2026": dict(
        release="release_2026_03_24",
        frame=ROOT / "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet",
        api=ROOT / "data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet",
        window="5–12 Feb 2026", platform="Claude AI (Free, Pro, and Max)"),
}
WAVE_ORDER = ["aug2025", "nov2025", "feb2026"]

# ---------------------------------------------------------------- recorded facts (the check block)
# posts/post1/notes/feasibility.md §1, §4, §7 and posts/post1/notes/replication.md §2, §3.
REC = {
    "named_nodes": {"aug2025": 2616, "nov2025": 3168, "feb2026": 3258},
    "base_nodes": {"aug2025": 2618, "nov2025": 3170, "feb2026": 3260},
    "ix_rows": {"aug2025": 14454, "nov2025": 16778, "feb2026": 17530},
    "named_mass": {"aug2025": 91.8727, "nov2025": 93.5144, "feb2026": 92.9714},
    "named_conversations": {"aug2025": 886107, "nov2025": 935027, "feb2026": 929714},
    "priced_tasks": {"aug2025": 2607, "nov2025": 3154, "feb2026": 3244},
    "analysis_tasks": {"aug2025": 1802, "nov2025": 2075, "feb2026": 2188},
    "analysis_mass_wave": {"aug2025": 89.2530, "nov2025": 89.9892, "feb2026": 89.7348},
    "analysis_share_named": {"aug2025": 97.15, "nov2025": 96.23, "feb2026": 96.52},
    "analysis_conversations": {"aug2025": 818673, "nov2025": 854432, "feb2026": 848716},
    "x1_wage_no_cell": {"aug2025": 805, "nov2025": 1079, "feb2026": 1056},
    "x2_cell_no_wage": {"aug2025": 5, "nov2025": 12, "feb2026": 12},
    "multi_holder10": {"aug2025": 74, "nov2025": 93, "feb2026": 86},
    "multi_holder7": {"aug2025": 72, "nov2025": 91, "feb2026": 84},
    "span_major_group": {"aug2025": 6, "nov2025": 10, "feb2026": 9},
    "quartile_bounds": {"aug2025": (25.78, 35.79, 43.40), "nov2025": (25.78, 34.56, 43.40),
                        "feb2026": (24.00, 34.40, 43.40)},
    "kish_named": {"aug2025": 99.7, "nov2025": 89.5, "feb2026": 134.3},
    "kish_analysis": {"aug2025": 94.4, "nov2025": 83.4, "feb2026": 125.7},
    "kish_q": {"aug2025": (62.3, 43.3, 22.2, 13.7), "nov2025": (55.6, 37.7, 22.0, 11.5),
               "feb2026": (51.0, 50.6, 36.8, 16.5)},
    "split_all_patterns": {"aug2025": 49.0980, "nov2025": 45.3554, "feb2026": 44.1569},
    "split_five_patterns": {"aug2025": 51.0698, "nov2025": 46.7394, "feb2026": 45.5456},
    "internal_check_gap": {"aug2025": 0.1303, "nov2025": 0.2931, "feb2026": 0.3510},
    "none_node_variant_aug": 51.7424,
    "fig211": (-3.111834, 0.393687, 111),
    "uc_rows": {"aug2025": 0, "nov2025": 13908, "feb2026": 14430},
    "work_dominant_tasks": {"nov2025": 943, "feb2026": 1071},
    "work_dominant_mass_wave": {"nov2025": 48.9382, "feb2026": 47.4364},
    "work_dominant_share_analysis": {"nov2025": 54.38, "feb2026": 52.86},
    "uc_only_nc": {"nov2025": 29, "feb2026": 21},
    "work_dominant_subst_tasks": {"nov2025": 978, "feb2026": 1106},
    "uc_flips": {"nov2025": 35, "feb2026": 35},
    "work_share_by_q": {"nov2025": (32.60, 48.69, 42.05, 61.91), "feb2026": (28.97, 51.21, 42.85, 61.65)},
    "c10_matched": {"aug2025": 1635, "nov2025": 1843, "feb2026": 1904},
    "c10_filtered_one": {"aug2025": 179, "nov2025": 251, "feb2026": 286},
    "sc_usage_count": 24715,
    "sc_over10_tasks": 23,
    "sc_over10_mass": 11.594,
    "sc_over20_tasks": 14,
    "sc_over20_mass": 1.966,
    "top10_named_share": {"aug2025": 24.9703, "nov2025": 25.9288, "feb2026": 20.9107},
}


def say(*a):
    print(*a)


# ---------------------------------------------------------------- loading (prereg E1)
def load_frame(path: pathlib.Path) -> pd.DataFrame:
    """Read a long-wave frame with NA disabled and every non-`value` column as a string."""
    if str(path).endswith(".parquet"):
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != "value":
                df[c] = df[c].astype(str)
    else:
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    df["value"] = pd.to_numeric(df["value"])
    return df


def split_cluster(s: pd.Series) -> tuple[pd.Series, pd.Series]:
    """`cluster_name` is `task::pattern`; split on the LAST `::` (ATLAS §Traps 21)."""
    parts = s.str.rsplit("::", n=1)
    return parts.str[0], parts.str[1]


def kish(w) -> float:
    """Kish effective N, n/(1+cv²), on positive weights."""
    w = np.asarray(w, float)
    w = w[w > 0]
    return float(w.sum() ** 2 / (w ** 2).sum()) if len(w) else float("nan")


# ---------------------------------------------------------------- C5, C6, C7, the crosswalk
def holder_tables():
    """C5: lower-cased stripped task text → sorted list of distinct 10-char O*NET-SOC holders."""
    on = pd.read_csv(ROOT / "data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv",
                     keep_default_na=False, na_values=[], dtype=str)
    on["key"] = on["Task"].str.lower().str.strip()
    holders = on.groupby("key")["O*NET-SOC Code"].apply(lambda s: sorted(set(s)))
    audit = dict(rows=len(on), codes=on["O*NET-SOC Code"].nunique(),
                 task_ids=on["Task ID"].nunique(), task_texts=on["Task"].nunique(),
                 keys=int(holders.shape[0]), max_rows_per_key=int(on.groupby("key").size().max()),
                 soc7=on["O*NET-SOC Code"].str[:7].nunique(),
                 major_groups=on["soc_major_group"].nunique())
    return holders, audit


def wage_tables():
    """C6 hourly wage and JobZone by 10-char code; C7 hourly wage and employment by 7-char code."""
    wg = pd.read_csv(ROOT / "data/cache/release_2025_02_10/wage_data.csv",
                     keep_default_na=False, na_values=[])
    kept = wg[wg.MedianSalary > 100]                      # our threshold, applied BEFORE the join
    c6 = (kept.set_index("SOCcode").MedianSalary / 2080.0).astype(float)
    jz = wg.set_index("SOCcode").JobZone
    jz = jz[jz > 0].astype(float)                         # -1 is a missing sentinel
    audit = dict(rows=len(wg), kept=int(len(kept)), dropped=int(len(wg) - len(kept)),
                 dropped_values=sorted(wg.loc[wg.MedianSalary <= 100, "MedianSalary"].tolist()),
                 jobzone_sentinels=int((wg.JobZone == -1).sum()),
                 chanceauto_sentinels=int((wg.ChanceAuto == -1).sum()),
                 top_code_annual=float(wg.MedianSalary.max()),
                 top_code_hourly=float(wg.MedianSalary.max() / 2080.0),
                 at_top_code=int((wg.MedianSalary == wg.MedianSalary.max()).sum()))

    ep_html = ROOT / "data/cache/supplementary/bls_employment_projections/occupationProj.html"
    ep = max(pd.read_html(ep_html), key=len)
    ep.columns = [c[0] if isinstance(c, tuple) else c for c in ep.columns]
    ep = ep.loc[:, ~ep.columns.duplicated()]
    ep["occ_code"] = ep["Occupation Code"].astype(str).str.strip()
    ep["wage"] = pd.to_numeric(ep["Median Annual Wage 2025"].astype(str).str.replace(r"[^0-9.]", "", regex=True),
                               errors="coerce")
    ep["emp"] = pd.to_numeric(ep["Employment 2025"].astype(str).str.replace(r"[^0-9.]", "", regex=True),
                              errors="coerce")
    ep = ep[ep.occ_code.str.match(r"^\d\d-\d{4}$")]
    c7 = (ep.set_index("occ_code").wage.dropna() / 2080.0).astype(float)
    emp = ep.set_index("occ_code").emp.dropna().astype(float)
    ep_audit = dict(rows=int(len(ep)), codes=int(ep.occ_code.nunique()),
                    wage_rows=int(len(c7)), emp_rows=int(len(emp)))
    return c6, jz, c7, emp, audit, ep_audit


def crosswalk_map():
    """2010 O*NET-SOC code → sorted list of 2019 codes (the O*NET Center crosswalk; 44 one-to-many)."""
    xw = pd.read_csv(ROOT / "data/cache/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv",
                     keep_default_na=False, na_values=[], dtype=str)
    xw.columns = ["c2010", "t2010", "c2019", "t2019"]
    m = xw.groupby("c2010")["c2019"].apply(lambda s: sorted(set(s)))
    audit = dict(rows=len(xw), codes_2010=int(m.shape[0]),
                 one_to_many=int((m.str.len() > 1).sum()))
    return m, audit


# ---------------------------------------------------------------- the three wage rules (W1)
def wage_under_rules(holders10, price: pd.Series, emp: pd.Series, seven_char_key: bool):
    """Return (employment-weighted, equal-split, modal) wage over a task's priced holders.

    `price` is indexed by 10-char code (C6) or 7-char code (C7); `emp` by 7-char code.
    Employment-weighted is the pre-registered primary rule (W1): a priced holder with no BLS-EP
    employment figure carries zero weight, and where **no** holder carries one the rule degenerates
    to the equal-split mean (counted and printed, because BLS-EP reaches 670 of 775 7-char codes).
    The modal holder is the priced holder with the largest employment, ties and missing employment
    to the lexicographically smallest code (the holder lists are sorted).
    """
    vals, wts = [], []
    for h in holders10:
        k = h[:7] if seven_char_key else h
        if k in price.index:
            vals.append(float(price[k]))
            wts.append(float(emp[h[:7]]) if h[:7] in emp.index else np.nan)
    if not vals:
        return np.nan, np.nan, np.nan, 0, False
    v = np.asarray(vals, float)
    w = np.asarray(wts, float)
    ok = np.isfinite(w) & (w > 0)
    equal = float(v.mean())
    if ok.any():
        empw = float(np.average(v[ok], weights=w[ok]))
        modal = float(v[np.nanargmax(np.where(ok, w, -np.inf))])
        degenerate = False
    else:
        empw = equal
        modal = float(v[0])           # holders are sorted, so this is the smallest 10-char code
        degenerate = True
    return empw, equal, modal, len(v), degenerate


def a2_group(holders10, emp: pd.Series, xw: pd.Series | None):
    """A2: the task's single group — the holder with the largest BLS-EP employment, ties (and
    missing employment) to the lexicographically smallest 10-character code. `xw` given → the
    2019 recode of that holder (its lexicographically smallest 2019 code); `xw` None → 2010.

    BLS-EP is keyed on SOC-2018 codes and reaches 670 of the 775 7-character O*NET-SOC 2010 codes,
    so employment is missing for whole families (the 2018 SOC renumbered the computer occupations).
    Where no holder carries an employment figure the rule falls back to the lexicographically
    smallest code, which is the brief's own stated fallback.
    """
    best, best_emp = None, -np.inf
    for h in sorted(holders10):                     # sorted ⇒ ties go to the smallest code
        e = float(emp[h[:7]]) if h[:7] in emp.index else -1.0
        if best is None or e > best_emp:
            best, best_emp = h, e
    if best is None:
        return None, None
    if xw is None:
        return best[:2], best
    codes = xw.get(best)
    if not codes:
        return None, best
    return sorted(codes)[0][:2], best


def a1_group_weights(holders10, xw: pd.Series | None):
    """A1: a task's usage mass split equally over its distinct holder codes (2019 primary), then
    summed by major group — the released `soc15_figA1_2026_03.py` convention."""
    codes = []
    for h in holders10:
        if xw is None:
            codes.append(h)
        else:
            codes.extend(xw.get(h, []))
    codes = sorted(set(codes))
    if not codes:
        return {}
    w = 1.0 / len(codes)
    out: dict[str, float] = {}
    for c in codes:
        out[c[:2]] = out.get(c[:2], 0.0) + w
    return out


def modal_group(weights: dict[str, float]) -> str | None:
    """The group carrying the largest A1 weight, ties to the lexicographically smallest group."""
    if not weights:
        return None
    return sorted(weights.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


# ---------------------------------------------------------------- the per-wave build
def build_wave(wave: str, verbose: bool = True) -> tuple[pd.DataFrame, dict]:
    """Build the per-task table and the wave's coverage facts. No estimate is formed here."""
    cfg = WAVES[wave]
    holders, c5_audit = holder_tables()
    c6, jz, c7, emp, c6_audit, c7_audit = wage_tables()
    xw, xw_audit = crosswalk_map()

    df = load_frame(cfg["frame"])
    g = df[df.geography == "global"]
    facts: dict = dict(wave=wave, release=cfg["release"], window=cfg["window"],
                       frame_rows=int(len(df)), global_rows=int(len(g)),
                       platform=sorted(df.platform_and_product.unique()),
                       date_start=sorted(df.date_start.unique()),
                       date_end=sorted(df.date_end.unique()),
                       c5_audit=c5_audit, c6_audit=c6_audit, c7_audit=c7_audit,
                       crosswalk_audit=xw_audit)

    # ---- C1–C3 the intersection
    ix = g[g.facet == "onet_task::collaboration"].copy()
    ix["task"], ix["pattern"] = split_cluster(ix.cluster_name)
    facts["ix_rows"] = int(len(ix))
    facts["ix_rows_outside_global"] = int(((df.facet == "onet_task::collaboration") & (df.geography != "global")).sum())
    facts["ix_levels"] = sorted(ix.level.unique())
    facts["ix_patterns"] = sorted(ix.pattern.unique())
    facts["ix_base_tasks"] = int(ix.task.nunique())
    facts["ix_named_tasks"] = int(ix.loc[~ix.task.isin(RESID), "task"].nunique())
    facts["ix_min_count"] = float(ix.loc[ix.variable.str.endswith("_count"), "value"].min())

    ixn = ix[~ix.task.isin(RESID)]
    cnt = ixn[ixn.variable.str.endswith("_count")].pivot_table(
        index="task", columns="pattern", values="value", aggfunc="sum").reindex(columns=PATTERNS).fillna(0.0)
    pct = ixn[ixn.variable.str.endswith("_pct")].pivot_table(
        index="task", columns="pattern", values="value", aggfunc="sum").reindex(columns=PATTERNS).fillna(0.0)
    facts["pct_row_sum_min"] = float(pct.sum(1).min())
    facts["pct_row_sum_max"] = float(pct.sum(1).max())

    # ---- C4 the base facet and the weights
    base = g[g.facet == "onet_task"]
    bp = base[base.variable == "onet_task_pct"].set_index("cluster_name").value
    bc = base[base.variable == "onet_task_count"].set_index("cluster_name").value
    facts["base_nodes"] = int(bp.shape[0])
    facts["base_pct_sum"] = float(bp.sum())
    facts["base_min_count"] = float(bc.min())
    facts["residual_nodes_in_base"] = sorted(set(bp.index) & set(RESID))
    facts["residual_nodes_in_ix"] = sorted(set(ix.task) & set(RESID))
    w_named = bp[~bp.index.isin(RESID)]
    facts["named_nodes"] = int(len(w_named))
    facts["named_mass"] = float(w_named.sum())
    facts["residual_node_mass"] = float(bp[bp.index.isin(RESID)].sum())
    facts["named_conversations"] = float(bc[~bc.index.isin(RESID)].sum())

    # ---- the wave's published splits (§8(i)) and the five-pattern base
    col = g[(g.facet == "collaboration") & (g.variable == "collaboration_pct")].set_index("cluster_name").value
    facts["split_all_patterns"] = float(col[AUTO].sum() / col.sum() * 100)
    facts["split_five_patterns"] = float(col[AUTO].sum() / col[CLASSIFIED].sum() * 100)
    facts["wave_none_pattern_pct"] = float(col.get("none", 0.0) / col.sum() * 100)

    # ---- the table, one row per named node
    t = pd.DataFrame({"task": w_named.index, "w": w_named.values})
    t["cnt"] = bc.reindex(t.task).values
    t["key"] = t.task.str.lower().str.strip()
    matched = t.key.isin(holders.index)
    facts["c5_in"] = int(len(t))
    facts["c5_matched"] = int(matched.sum())
    facts["c5_unmatched"] = int((~matched).sum())
    facts["c5_unmatched_names"] = sorted(t.loc[~matched, "task"].tolist())[:10]
    facts["c5_unmatched_mass"] = float(t.loc[~matched, "w"].sum())
    facts["c5_key_collisions"] = int(len(t) - t.key.nunique())
    t = t[matched].copy()
    t["holders"] = [holders[k] for k in t.key]
    t["n10"] = t.holders.str.len()
    t["n7"] = [len({h[:7] for h in hs}) for hs in t.holders]
    t["nmg2010"] = [len({h[:2] for h in hs}) for hs in t.holders]

    # pattern counts and per-cents
    for p in PATTERNS:
        t["c_" + p] = cnt[p].reindex(t.task).fillna(0.0).values
        t["pct_" + p] = pct[p].reindex(t.task).fillna(0.0).values
    t["n5"] = t[["c_" + p for p in CLASSIFIED]].sum(1)
    t["c_all"] = t[["c_" + p for p in PATTERNS]].sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        t["p"] = np.where(t.n5 > 0, t[["c_" + p for p in AUTO]].sum(1) / t.n5 * 100, np.nan)
        t["p_pct_route"] = np.where(t[["pct_" + p for p in CLASSIFIED]].sum(1) > 0,
                                    t[["pct_" + p for p in AUTO]].sum(1)
                                    / t[["pct_" + p for p in CLASSIFIED]].sum(1) * 100, np.nan)
        t["none_share"] = np.where(t.c_all > 0, t.c_none / t.c_all * 100, np.nan)
        t["nc_share"] = np.where(t.c_all > 0, t.c_not_classified / t.c_all * 100, np.nan)
    facts["ix_not_classified_pattern_pct"] = float(t.c_not_classified.sum() / t.c_all.sum() * 100)
    facts["ix_none_pattern_pct"] = float(t.c_none.sum() / t.c_all.sum() * 100)

    # ---- wages under the three rules, both sources
    rows6 = [wage_under_rules(hs, c6, emp, False) for hs in t.holders]
    rows7 = [wage_under_rules(hs, c7, emp, True) for hs in t.holders]
    t["wage"] = [r[0] for r in rows6]            # W1 primary: employment-weighted, C6
    t["wage_equal"] = [r[1] for r in rows6]
    t["wage_modal"] = [r[2] for r in rows6]
    t["n_priced10"] = [r[3] for r in rows6]
    t["wage_degenerate"] = [r[4] for r in rows6]
    t["wage_c7"] = [r[0] for r in rows7]
    t["wage_c7_equal"] = [r[1] for r in rows7]
    t["wage_c7_modal"] = [r[2] for r in rows7]
    t["jobzone"] = [np.mean([float(jz[h]) for h in hs if h in jz.index]) if any(h in jz.index for h in hs)
                    else np.nan for hs in t.holders]

    facts["priced_tasks"] = int(t.wage.notna().sum())
    facts["priced_mass"] = float(t.loc[t.wage.notna(), "w"].sum())
    facts["priced_share_named"] = float(t.loc[t.wage.notna(), "w"].sum() / facts["named_mass"] * 100)
    facts["c7_priced_tasks"] = int(t.wage_c7.notna().sum())
    facts["c7_priced_share_named"] = float(t.loc[t.wage_c7.notna(), "w"].sum() / facts["named_mass"] * 100)
    facts["jobzone_share_named"] = float(t.loc[t.jobzone.notna(), "w"].sum() / facts["named_mass"] * 100)
    facts["multi_holder10"] = int((t.n10 > 1).sum())
    facts["multi_holder7"] = int((t.n7 > 1).sum())
    facts["span_major_group"] = int((t.nmg2010 > 1).sum())
    facts["multi_priced_holders"] = int((t.n_priced10 > 1).sum())
    facts["wage_rule_degenerate"] = int(t.wage_degenerate.sum())
    mh = t[t.n_priced10 > 1]
    facts["w1_multi_priced_no_employment"] = int(mh.wage_degenerate.sum())
    facts["w1_multi_priced_with_employment"] = int((~mh.wage_degenerate).sum())
    facts["wage_rule_max_gap"] = float((mh.wage_equal - mh.wage).abs().max()) if len(mh) else 0.0
    facts["wage_rule_corr"] = float(t[["wage", "wage_equal"]].corr().iloc[0, 1])
    both = t.wage.notna() & t.wage_c7.notna()
    facts["c6_c7_spearman"] = float(t.loc[both, ["wage", "wage_c7"]].corr(method="spearman").iloc[0, 1])
    facts["c6_c7_n"] = int(both.sum())
    facts["at_wage_cap"] = int((t.wage >= c6_audit["top_code_hourly"] - 1e-9).sum())

    # ---- groups: A2 (one group per task) and A1 (share statistics), both vintages
    g19 = [a2_group(hs, emp, xw) for hs in t.holders]
    g10 = [a2_group(hs, emp, None) for hs in t.holders]
    t["group2019"] = [x[0] for x in g19]
    t["group2010"] = [x[0] for x in g10]
    t["a2_holder"] = [x[1] for x in g19]
    t["soc15_a1_2019"] = [a1_group_weights(hs, xw).get("15", 0.0) for hs in t.holders]
    t["soc15_a1_2010"] = [a1_group_weights(hs, None).get("15", 0.0) for hs in t.holders]
    t["soc15_a1_modal"] = [1.0 if modal_group(a1_group_weights(hs, xw)) == "15" else 0.0
                           for hs in t.holders]
    t["soc15_a1_empw"] = [1.0 if x[0] == "15" else 0.0 for x in g19]
    facts["group_set_changes_vintage"] = int(sum(
        1 for hs in t.holders
        if {h[:2] for h in hs} != {c[:2] for h in hs for c in (xw.get(h) or [h])}))
    facts["a2_group_missing"] = int(t.group2019.isna().sum())

    # ---- the analysis set (S1) and the two audited losses (X1, X2)
    has_cell = t.n5 > 0
    has_wage = t.wage.notna()
    t["in_analysis"] = has_cell & has_wage
    facts["analysis_tasks"] = int(t.in_analysis.sum())
    facts["analysis_mass_wave"] = float(t.loc[t.in_analysis, "w"].sum())
    facts["analysis_share_named"] = float(t.loc[t.in_analysis, "w"].sum() / facts["named_mass"] * 100)
    facts["analysis_conversations"] = float(t.loc[t.in_analysis, "n5"].sum())
    facts["x1_wage_no_cell"] = int((has_wage & ~has_cell).sum())
    facts["x1_mass"] = float(t.loc[has_wage & ~has_cell, "w"].sum())
    facts["x2_cell_no_wage"] = int((has_cell & ~has_wage).sum())
    facts["x2_mass"] = float(t.loc[has_cell & ~has_wage, "w"].sum())
    facts["kish_named"] = kish(t.w.values if len(t) == facts["named_nodes"] else w_named.values)
    facts["kish_analysis"] = kish(t.loc[t.in_analysis, "w"].values)

    # ---- the §8(iii) internal check: usage-weighted mean of per-task automation vs the wave value
    a = t[has_cell]
    facts["internal_check_value"] = float(np.average(a.p, weights=a.w))
    facts["internal_check_gap"] = facts["internal_check_value"] - facts["split_five_patterns"]
    # the released spec keeps the `none` TASK node (X7): its own rate, weighted in beside the named
    none_rows = ix[(ix.task == "none") & (ix.variable.str.endswith("_count"))]
    if len(none_rows):
        nn = none_rows.groupby("pattern").value.sum().reindex(PATTERNS).fillna(0.0)
        p_none_node = float(nn[AUTO].sum() / nn[CLASSIFIED].sum() * 100)
        w_none_node = float(bp.get("none", 0.0))
        facts["none_node_p"] = p_none_node
        facts["none_node_weight"] = w_none_node
        facts["internal_check_with_none_node"] = float(
            (np.average(a.p, weights=a.w) * a.w.sum() + p_none_node * w_none_node) / (a.w.sum() + w_none_node))

    # ---- C9 `use_case`, where the facet exists
    uc = g[g.facet == "onet_task::use_case"].copy()
    facts["uc_rows"] = int(len(uc))
    facts["uc_facets_containing_use_case"] = sorted({f for f in g.facet.unique() if "use_case" in f})
    for c in UC_CATS:
        t["uc_" + c] = np.nan
    t["work_share"] = np.nan
    t["work_share_subst"] = np.nan
    t["uc_only_nc"] = False
    if len(uc):
        uc["task"], uc["cat"] = split_cluster(uc.cluster_name)
        ucn = uc[(~uc.task.isin(RESID)) & (uc.variable.str.endswith("_count"))]
        utab = ucn.pivot_table(index="task", columns="cat", values="value", aggfunc="sum").fillna(0.0)
        facts["uc_categories"] = sorted(utab.columns.tolist())
        for c in UC_CATS:
            t["uc_" + c] = (utab[c].reindex(t.task).values if c in utab.columns else 0.0)
        cells = t[["uc_" + c for c in UC_CATS]].sum(1)
        subst = t[["uc_" + c for c in UC_CATS if c != "not_classified"]].sum(1)
        t["uc_only_nc"] = (cells > 0) & (subst == 0)
        with np.errstate(invalid="ignore", divide="ignore"):
            # a task whose only published cell is `not_classified` has an UNDEFINED work share and
            # is dropped by the leg-(e) rule, never scored 0 (prereg P3(e)); its count and mass are
            # printed and asserted.
            t["work_share"] = np.where((cells > 0) & ~t.uc_only_nc, t.uc_work / cells, np.nan)
            t["work_share_subst"] = np.where(subst > 0, t.uc_work / subst, np.nan)
        an = t[t.in_analysis]
        facts["uc_analysis_covered"] = int((cells[t.in_analysis.values] > 0).sum())
        facts["uc_only_nc_analysis"] = int(an.uc_only_nc.sum())
        facts["uc_only_nc_mass"] = float(an.loc[an.uc_only_nc, "w"].sum())
        wd = an[(an.work_share >= 0.5)]
        facts["work_dominant_tasks"] = int(len(wd))
        facts["work_dominant_mass_wave"] = float(wd.w.sum())
        facts["work_dominant_share_analysis"] = float(wd.w.sum() / an.w.sum() * 100)
        wds = an[(an.work_share_subst >= 0.5)]
        facts["work_dominant_subst_tasks"] = int(len(wds))
        facts["uc_flips"] = int(((an.work_share >= 0.5) != (an.work_share_subst.fillna(-1) >= 0.5)).sum())

    # ---- C8 Seychelles (November only): the task weights it can reach
    t["sc_count"] = 0.0
    if wave == "nov2025":
        sc = df[(df.geography == "country") & (df.geo_id == "SC")]
        facts["sc_usage_count"] = float(sc.loc[(sc.facet == "country") & (sc.variable == "usage_count"), "value"].iloc[0])
        facts["sc_usage_pct"] = float(sc.loc[(sc.facet == "country") & (sc.variable == "usage_pct"), "value"].iloc[0])
        sct = sc[(sc.facet == "onet_task") & (sc.variable == "onet_task_count")].set_index("cluster_name").value
        facts["sc_task_nodes"] = int(len(sct))
        facts["sc_ix_rows"] = int(((df.geo_id == "SC") & (df.facet == "onet_task::collaboration")).sum())
        t["sc_count"] = sct.reindex(t.task).fillna(0.0).values
        with np.errstate(invalid="ignore", divide="ignore"):
            t["sc_share"] = np.where(t.cnt > 0, t.sc_count / t.cnt, 0.0)
        an = t[t.in_analysis]
        facts["sc_over10_tasks"] = int((an.sc_share > 0.10).sum())
        facts["sc_over10_mass"] = float(an.loc[an.sc_share > 0.10, "w"].sum())
        facts["sc_over20_tasks"] = int((an.sc_share > 0.20).sum())
        facts["sc_over20_mass"] = float(an.loc[an.sc_share > 0.20, "w"].sum())
        facts["sc_max_share"] = float(an.sc_share.max() * 100)
    else:
        t["sc_share"] = 0.0

    # ---- C10, the fourth window (P7): the per-task ratios, matched on the task key
    bt = pd.read_csv(ROOT / "data/cache/release_2025_03_27/automation_vs_augmentation_by_task.csv",
                     keep_default_na=False, na_values=[])
    bt["key"] = bt.task_name.str.lower().str.strip()
    btx = bt.set_index("key")
    for c in C10_PATTERNS + ["filtered"]:
        t["c10_" + c] = btx[c].reindex(t.key).values
    t["c10_matched"] = t.c10_filtered.notna()
    an = t[t.in_analysis]
    facts["c10_matched"] = int(an.c10_matched.sum())
    facts["c10_unmatched"] = int((~an.c10_matched).sum())
    facts["c10_matched_mass"] = float(an.loc[an.c10_matched, "w"].sum())
    facts["c10_filtered_one"] = int((an.c10_filtered == 1.0).sum())
    facts["c10_filtered_one_mass"] = float(an.loc[an.c10_filtered == 1.0, "w"].sum())

    # ---- top-10 concentration (§10's denominators, both stated)
    top10 = t.nlargest(10, "w")
    facts["top10_wave_mass"] = float(top10.w.sum())
    facts["top10_named_share"] = float(top10.w.sum() / facts["named_mass"] * 100)

    # ---- the quartiles, on the primary wage rule
    an = t[t.in_analysis].copy()
    q, bounds = quartiles(an, "wage")
    t["q"] = np.nan
    t.loc[an.index, "q"] = q.values
    facts["quartile_bounds"] = [float(b) for b in bounds]
    facts["quartile_bounds_equal_rule"] = [float(b) for b in quartiles(an, "wage_equal")[1]]
    an["q"] = q.values
    facts["quartiles"] = {}
    for qq in (1, 2, 3, 4):
        s = an[an.q == qq]
        facts["quartiles"][f"Q{qq}"] = dict(
            tasks=int(len(s)), mass_wave=float(s.w.sum()),
            mass_share=float(s.w.sum() / an.w.sum() * 100),
            kish=kish(s.w.values), conversations=float(s.n5.sum()),
            wage_min=float(s.wage.min()), wage_max=float(s.wage.max()),
            mean_wage=float(np.average(s.wage, weights=s.w)))
    # ties split at a boundary: Q1 and Q4 are then not defined by the wage alone
    facts["boundary_tie_mass"] = {}
    for i, b in enumerate(bounds, start=1):
        at = an[np.isclose(an.wage, b)]
        facts["boundary_tie_mass"][f"b{i}_{b:.2f}"] = dict(
            tasks=int(len(at)), mass=float(at.w.sum()),
            quartiles_spanned=sorted(int(x) for x in at.q.unique()))
    # the same quarters with the boundary mass point shared in proportion (the corrected reading)
    qw_frac = quartile_weights(an, "wage", "fractional")
    facts["quartiles_fractional"] = {}
    for qq in (1, 2, 3, 4):
        col = qw_frac[:, qq - 1]
        facts["quartiles_fractional"][f"Q{qq}"] = dict(
            tasks_with_weight=int((col > 0).sum()), mass_wave=float(col.sum()),
            mass_share=float(col.sum() / an.w.sum() * 100), kish=kish(col))
    facts["q4_mass_from_boundary_tie"] = float(
        an.loc[(an.q == 4) & np.isclose(an.wage, bounds[2]), "w"].sum())
    facts["q1_q4_soc15_a1_2019"] = float(
        (an[an.q == 4].w * an[an.q == 4].soc15_a1_2019).sum() / an[an.q == 4].w.sum() * 100)
    facts["soc15_share_analysis_a1_2019"] = float((an.w * an.soc15_a1_2019).sum() / an.w.sum() * 100)
    facts["soc15_share_analysis_a1_2010"] = float((an.w * an.soc15_a1_2010).sum() / an.w.sum() * 100)
    facts["soc15_share_analysis_a2_2019"] = float(an.loc[an.group2019 == "15", "w"].sum() / an.w.sum() * 100)
    facts["soc15_share_analysis_a2_2010"] = float(an.loc[an.group2010 == "15", "w"].sum() / an.w.sum() * 100)
    facts["soc15_share_q4_a2_2019"] = float(
        an.loc[(an.q == 4) & (an.group2019 == "15"), "w"].sum() / an[an.q == 4].w.sum() * 100)
    facts["groups_present_2019"] = int(an.group2019.nunique())
    both_q = an.groupby("group2019").q.agg(lambda s: set(s))
    facts["groups_with_q1_and_q4"] = int(sum(1 for s in both_q if {1, 4} <= s))
    facts["groups_all_four"] = int(sum(1 for s in both_q if {1, 2, 3, 4} <= s))
    both_q10 = an.groupby("group2010").q.agg(lambda s: set(s))
    facts["groups_with_q1_and_q4_2010"] = int(sum(1 for s in both_q10 if {1, 4} <= s))
    facts["groups_all_four_2010"] = int(sum(1 for s in both_q10 if {1, 2, 3, 4} <= s))
    if len(uc):
        # the usage-weighted mean of the per-task work share, over the tasks where it is defined
        # (the only-`not_classified` tasks have no work share and are dropped, never scored 0)
        facts["work_share_by_q"] = []
        for qq in (1, 2, 3, 4):
            s = an[(an.q == qq) & an.work_share.notna()]
            facts["work_share_by_q"].append(float(100 * np.average(s.work_share, weights=s.w)))
        facts["uc_mix_by_q"] = {}
        for qq in (1, 2, 3, 4):
            s = an[an.q == qq]
            tot = s[["uc_" + c for c in UC_CATS]].sum().sum()
            facts["uc_mix_by_q"][f"Q{qq}"] = {c: float(100 * s["uc_" + c].sum() / tot) for c in UC_CATS}

    if verbose:
        report_wave(wave, facts)
    return t, facts


def quartiles(an: pd.DataFrame, wage_col: str) -> tuple[pd.Series, tuple[float, float, float]]:
    """Usage-weighted wage quartiles over an analysis set — the **pre-registered** rule: sort by
    wage, cut the cumulative usage mass at 0.25 / 0.50 / 0.75. Returns the quartile label aligned
    to `an`'s index and the three boundary wages (the maximum wage in Q1, Q2, Q3).

    Ties are split at a boundary, which is what makes each quartile exactly a quarter of the usage
    mass; the order inside a tie is fixed here on (wage, task text) so the cut is reproducible.
    The mass sitting at a boundary wage is large — a single wage value can carry 8–11 pp of a wave —
    so the tie rule matters and the fractional reading below is reported beside it (see the
    lab notebook's DEVIATION entry for the Q3/Q4 boundary).
    """
    s = an.sort_values([wage_col, "task"], kind="mergesort")
    cw = s.w.cumsum() / s.w.sum()
    qq = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw.values, side="left") + 1, 4)
    out = pd.Series(qq, index=s.index).reindex(an.index)
    bounds = tuple(float(s[wage_col][qq == k].max()) for k in (1, 2, 3))
    return out, bounds


def quartile_weights(an: pd.DataFrame, wage_col: str = "wage", mode: str = "registered",
                     weight_col: str = "w") -> np.ndarray:
    """The usage weight each task contributes to each quartile, as an (n, 4) array.

    mode='registered' — the pre-registered rule above: a task belongs entirely to one quartile and
    tied tasks at a boundary are split between quartiles by the (wage, task) order.
    mode='fractional' — the same quarters of usage mass, but a wage value that straddles a boundary
    contributes to both quartiles **in proportion**, so no arbitrary choice is made among tasks
    that share a wage. This is the corrected reading of "the top quarter of usage-weighted wage"
    when the wage has a mass point at the boundary, and it is run beside the registered rule.
    """
    w = an[weight_col].to_numpy(float)
    if mode == "registered":
        q = quartiles(an, wage_col)[0].to_numpy(int)
        out = np.zeros((len(an), 4))
        out[np.arange(len(an)), q - 1] = w
        return out
    if mode != "fractional":
        raise ValueError(mode)
    wage = an[wage_col].to_numpy(float)
    total = w.sum()
    out = np.zeros((len(an), 4))
    order = np.argsort(wage, kind="mergesort")
    cum = 0.0
    i = 0
    while i < len(order):
        j = i
        while j < len(order) and wage[order[j]] == wage[order[i]]:
            j += 1
        idx = order[i:j]
        mass = w[idx].sum()
        lo, hi = cum / total, (cum + mass) / total
        for k in (1, 2, 3, 4):
            a, b = (k - 1) / 4.0, k / 4.0
            overlap = max(0.0, min(hi, b) - max(lo, a))
            if overlap > 0:
                out[idx, k - 1] = w[idx] * (overlap / (hi - lo))
        cum += mass
        i = j
    return out


def report_wave(wave: str, f: dict) -> None:
    say("=" * 78)
    say(f"[{wave}] {f['release']} ({f['window']})  frame rows {f['frame_rows']:,}  "
        f"global rows {f['global_rows']:,}  platform {f['platform']}")
    say(f"  C1-C3 intersection rows {f['ix_rows']:,} (outside global: {f['ix_rows_outside_global']}) "
        f"levels {f['ix_levels']} patterns {len(f['ix_patterns'])} min count {f['ix_min_count']:.0f}")
    say(f"  C4 base nodes {f['base_nodes']} (named {f['named_nodes']}); onet_task_pct sums to "
        f"{f['base_pct_sum']:.6f}; named mass {f['named_mass']:.4f} pp; residual node mass "
        f"{f['residual_node_mass']:.4f} pp; residual in base {f['residual_nodes_in_base']} vs "
        f"intersection {f['residual_nodes_in_ix']}")
    say(f"  MERGE AUDIT C5 (task text -> O*NET 20.1 key): in {f['c5_in']}, matched {f['c5_matched']}, "
        f"unmatched {f['c5_unmatched']} ({f['c5_unmatched_mass']:.4f} pp), key collisions {f['c5_key_collisions']}")
    say(f"  MERGE AUDIT C6 (10-char O*NET-SOC -> SOCcode, MedianSalary>100 applied first): priced "
        f"{f['priced_tasks']} tasks, {f['priced_mass']:.4f} pp = {f['priced_share_named']:.2f}% of named mass; "
        f"at the $100.00/hr top code {f['at_wage_cap']} tasks")
    say(f"  MERGE AUDIT C7 (soc7 -> BLS-EP occ_code): priced {f['c7_priced_tasks']} tasks = "
        f"{f['c7_priced_share_named']:.2f}% of named mass; Spearman with C6 {f['c6_c7_spearman']:.4f} on N={f['c6_c7_n']}")
    say(f"  multi-holder: 10-char {f['multi_holder10']}, 7-char {f['multi_holder7']}, spanning a major "
        f"group {f['span_major_group']}; multi-priced {f['multi_priced_holders']}; W1 degenerate on "
        f"{f['wage_rule_degenerate']}; max |equal - empw| ${f['wage_rule_max_gap']:.2f}/hr; corr {f['wage_rule_corr']:.4f}")
    say(f"  ANALYSIS SET (S1): {f['analysis_tasks']} tasks, {f['analysis_mass_wave']:.4f} pp of the wave = "
        f"{f['analysis_share_named']:.2f}% of named mass, on {f['analysis_conversations']:,.0f} classified conversations")
    say(f"  DROPPED, NEVER ZEROED: X1 wage & no classified cell {f['x1_wage_no_cell']} tasks "
        f"({f['x1_mass']:.4f} pp); X2 classified cell & no wage {f['x2_cell_no_wage']} tasks ({f['x2_mass']:.4f} pp)")
    say(f"  Kish effective N: named {f['kish_named']:.1f} (nominal {f['named_nodes']}); analysis set "
        f"{f['kish_analysis']:.1f} (nominal {f['analysis_tasks']})")
    say(f"  REPLICATION (i) published split: all-pattern {f['split_all_patterns']:.4f} | five-pattern "
        f"{f['split_five_patterns']:.4f}")
    say(f"  REPLICATION (iii) internal check: usage-weighted mean of per-task automation "
        f"{f['internal_check_value']:.4f} vs wave five-pattern {f['split_five_patterns']:.4f} "
        f"-> gap {f['internal_check_gap']:+.4f} pp"
        + (f"; with the `none` task node kept {f['internal_check_with_none_node']:.4f}"
           if "internal_check_with_none_node" in f else ""))
    say(f"  intersection `not_classified` pattern {f['ix_not_classified_pattern_pct']:.4f}% of named counts; "
        f"`none` pattern {f['ix_none_pattern_pct']:.4f}%")
    say(f"  QUARTILE BOUNDARIES (primary W1 wage) ${f['quartile_bounds'][0]:.2f} / "
        f"${f['quartile_bounds'][1]:.2f} / ${f['quartile_bounds'][2]:.2f}  "
        f"(equal-split rule: {[round(b, 2) for b in f['quartile_bounds_equal_rule']]})")
    for qq in ("Q1", "Q2", "Q3", "Q4"):
        d = f["quartiles"][qq]
        say(f"     {qq}  tasks {d['tasks']:4d}  mass {d['mass_wave']:6.3f} pp ({d['mass_share']:5.2f}%)  "
            f"Kish {d['kish']:6.1f}  conversations {d['conversations']:>9,.0f}  "
            f"${d['wage_min']:.2f}-${d['wage_max']:.2f}  mean ${d['mean_wage']:.2f}")
    say(f"  mass at a boundary wage (ties split): "
        + "; ".join(f"{k} -> {v['tasks']} tasks, {v['mass']:.4f} pp, quartiles {v['quartiles_spanned']}"
                    for k, v in f["boundary_tie_mass"].items()))
    say(f"  Q4 mass coming from the tie at the third boundary: {f['q4_mass_from_boundary_tie']:.4f} pp of "
        f"{f['quartiles']['Q4']['mass_wave']:.4f} pp; fractional-rule quartile Kish "
        f"{[round(f['quartiles_fractional'][f'Q{q}']['kish'], 1) for q in (1, 2, 3, 4)]}")
    say(f"  SOC-15: A1 equal-split share of analysis mass 2019 {f['soc15_share_analysis_a1_2019']:.2f}% "
        f"(2010 {f['soc15_share_analysis_a1_2010']:.2f}%); A2 drop mass 2019 "
        f"{f['soc15_share_analysis_a2_2019']:.2f}% (2010 {f['soc15_share_analysis_a2_2010']:.2f}%); "
        f"A1 share of Q4 mass {f['q1_q4_soc15_a1_2019']:.1f}%, A2 share of Q4 {f['soc15_share_q4_a2_2019']:.1f}%")
    say(f"  groups (2019 recode, A2): present {f['groups_present_2019']}; containing Q1 and Q4 "
        f"{f['groups_with_q1_and_q4']}; spanning all four {f['groups_all_four']} "
        f"(2010: {f['groups_with_q1_and_q4_2010']} / {f['groups_all_four_2010']})")
    say(f"  C9 use_case rows {f['uc_rows']:,} (facets with 'use_case': {f['uc_facets_containing_use_case']})")
    if f["uc_rows"]:
        say(f"     coverage of the analysis set {f['uc_analysis_covered']} of {f['analysis_tasks']}; "
            f"only-`not_classified` {f['uc_only_nc_analysis']} tasks ({f['uc_only_nc_mass']:.4f} pp); "
            f"work-dominant {f['work_dominant_tasks']} tasks, {f['work_dominant_mass_wave']:.4f} pp = "
            f"{f['work_dominant_share_analysis']:.2f}% of analysis mass; substantive-cell rule "
            f"{f['work_dominant_subst_tasks']} tasks, flips {f['uc_flips']}")
        say(f"     work share by wage quartile Q1->Q4 {[round(x, 2) for x in f['work_share_by_q']]}")
    if wave == "nov2025":
        say(f"  C8 Seychelles: usage {f['sc_usage_count']:,.0f} ({f['sc_usage_pct']:.5f}%), task nodes "
            f"{f['sc_task_nodes']}, onet_task::collaboration rows {f['sc_ix_rows']}; analysis-set tasks with "
            f"SC > 10% of the global count {f['sc_over10_tasks']} ({f['sc_over10_mass']:.3f} pp), > 20% "
            f"{f['sc_over20_tasks']} ({f['sc_over20_mass']:.3f} pp); max share {f['sc_max_share']:.1f}%")
    say(f"  C10 reach: {f['c10_matched']} of {f['analysis_tasks']} analysis-set tasks "
        f"({f['c10_matched_mass']:.4f} of {f['analysis_mass_wave']:.4f} pp = "
        f"{100 * f['c10_matched_mass'] / f['analysis_mass_wave']:.2f}%); filtered == 1.0 on "
        f"{f['c10_filtered_one']} ({f['c10_filtered_one_mass']:.4f} pp)")
    say(f"  top-10 concentration {f['top10_wave_mass']:.4f} pp of the wave = {f['top10_named_share']:.4f}% of named mass")


# ---------------------------------------------------------------- the cached build, for later scripts
def get_build(wave: str, rebuild: bool = False) -> pd.DataFrame:
    """The per-task table for a wave, from /tmp/post1 if it is there and rebuilt if not."""
    dest = SCRATCH / f"build_{wave}.parquet"
    if dest.exists() and not rebuild:
        t = pd.read_parquet(dest)
        t["holders"] = t.holders.apply(list)
        return t
    t, _ = build_wave(wave, verbose=False)
    t.assign(holders=t.holders.apply(list)).to_parquet(dest)
    return t


def analysis_set(wave: str) -> pd.DataFrame:
    """The analysis set of a wave with its quartile labels on the primary wage rule."""
    t = get_build(wave)
    an = t[t.in_analysis].copy()
    an["q"] = quartiles(an, "wage")[0].values
    return an


# ---------------------------------------------------------------- plot before modelling
def plots(builds: dict[str, pd.DataFrame]) -> list[str]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    DIAG.mkdir(parents=True, exist_ok=True)
    written = []
    fig, axes = plt.subplots(3, 4, figsize=(18, 11))
    for r, wave in enumerate(WAVE_ORDER):
        an = builds[wave]
        an = an[an.in_analysis]
        axes[r, 0].hist(an.p, bins=40, color="#4a6fa5")
        axes[r, 0].set_title(f"{wave}: per-task automation share p_i (pp)")
        axes[r, 1].hist(np.log10(an.n5.clip(lower=1)), bins=40, color="#4a6fa5")
        axes[r, 1].set_title(f"{wave}: log10 classified conversations n_i")
        axes[r, 2].hist(np.log10(an.w.clip(lower=1e-6)), bins=40, color="#4a6fa5")
        axes[r, 2].set_title(f"{wave}: log10 usage weight w_i")
        axes[r, 3].scatter(an.wage, an.p, s=an.w * 120, alpha=0.35, color="#8a3324")
        for b in quartiles(an, "wage")[1]:
            axes[r, 3].axvline(b, color="grey", lw=0.8, ls="--")
        axes[r, 3].set_title(f"{wave}: p_i against hourly wage (size = usage weight)")
        axes[r, 3].set_xlabel("$/hr")
    fig.tight_layout()
    f1 = DIAG / "diag_distributions.png"
    fig.savefig(f1, dpi=110)
    plt.close(fig)
    written.append(str(f1.relative_to(ROOT)))

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for i, wave in enumerate(WAVE_ORDER):
        an = builds[wave]
        an = an[an.in_analysis]
        order = an.sort_values("wage")
        axes[i].plot(order.wage.values, (order.w.cumsum() / order.w.sum()).values, color="#4a6fa5")
        for b in quartiles(an, "wage")[1]:
            axes[i].axvline(b, color="grey", lw=0.8, ls="--")
        for y in (0.25, 0.5, 0.75):
            axes[i].axhline(y, color="grey", lw=0.5, ls=":")
        axes[i].set_title(f"{wave}: cumulative usage mass by wage")
        axes[i].set_xlabel("$/hr")
    fig.tight_layout()
    f2 = DIAG / "diag_wage_distribution.png"
    fig.savefig(f2, dpi=110)
    plt.close(fig)
    written.append(str(f2.relative_to(ROOT)))
    return written


# ---------------------------------------------------------------- Anthropic's released library
def fig211() -> tuple[float, float, int]:
    """Run `data/replication/post1_replicate_fig211.py` (Anthropic's own released code, in place)
    and parse the Figure 2.11 triple out of its output."""
    r = subprocess.run([sys.executable, str(ROOT / "data/replication/post1_replicate_fig211.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        raise RuntimeError(f"released-library replication failed: {r.stderr[-2000:]}")
    line = [x for x in r.stdout.splitlines() if "collaboration_task_regression" in x][0]
    slope = float(line.split("slope")[1].split()[0])
    r2 = float(line.split("partial_r2")[1].split()[0])
    n = int(line.split("n_countries")[1].split()[0])
    say(f"  released library: slope {slope:.6f}  partial R² {r2:.6f}  N countries {n}  "
        f"(published −3.112 / 0.394 / 111)")
    return slope, r2, n


# ---------------------------------------------------------------- main
def main():
    builds, allfacts = {}, {}
    for wave in WAVE_ORDER:
        t, f = build_wave(wave)
        t.assign(holders=t.holders.apply(list)).to_parquet(SCRATCH / f"build_{wave}.parquet")
        builds[wave], allfacts[wave] = t, f
    say("=" * 78)
    say("REPLICATION (ii): Anthropic's released library, Figure 2.11")
    slope, r2, ncty = fig211()
    say("=" * 78)
    figs = plots(builds)
    say("plot before modelling ->", figs)
    out = dict(script="posts/post1/scripts/02_build.py",
               prereg="posts/post1/prereg/prereg.md content c9b1b45",
               fig211=dict(slope=slope, partial_r2=r2, n_countries=ncty,
                           published=[-3.112, 0.394, 111]),
               diagnostics=figs, waves=allfacts)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / "build_facts.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    say(f"wrote {(PROCESSED / 'build_facts.json').relative_to(ROOT)}")
    return builds, allfacts, (slope, r2, ncty)


if __name__ == "__main__":
    builds, F, fig = main()

    # ------------------------------------------------------------ check block
    # Every assertion below is a fact recorded in feasibility.md §1/§4/§7 or replication.md §2/§3,
    # or an internal consistency the construction must satisfy. The script exits non-zero on any
    # failure and nothing downstream runs.
    for w in WAVE_ORDER:
        f = F[w]
        # frames, nodes, weights
        assert f["ix_rows"] == REC["ix_rows"][w], (w, f["ix_rows"])
        assert f["ix_rows_outside_global"] == 0, w
        assert f["ix_levels"] == ["0"], (w, f["ix_levels"])
        assert sorted(f["ix_patterns"]) == sorted(PATTERNS), (w, f["ix_patterns"])
        assert f["ix_min_count"] == 1.0, (w, f["ix_min_count"])
        assert f["base_nodes"] == REC["base_nodes"][w], (w, f["base_nodes"])
        assert f["named_nodes"] == REC["named_nodes"][w], (w, f["named_nodes"])
        assert abs(f["base_pct_sum"] - 100.0) < 1e-6, (w, f["base_pct_sum"])
        assert f["base_min_count"] == 15.0, (w, f["base_min_count"])
        assert f["residual_nodes_in_base"] == ["none", "not_classified"], w
        assert f["residual_nodes_in_ix"] == ["none"], w
        assert abs(f["named_mass"] - REC["named_mass"][w]) < 5e-4, (w, f["named_mass"])
        assert round(f["named_conversations"]) == REC["named_conversations"][w], (w, f["named_conversations"])
        assert abs(f["pct_row_sum_min"] - 100.0) < 1e-3 and abs(f["pct_row_sum_max"] - 100.0) < 1e-3, w
        # merge audits
        assert f["c5_in"] == REC["named_nodes"][w] and f["c5_matched"] == REC["named_nodes"][w], w
        assert f["c5_unmatched"] == 0 and f["c5_key_collisions"] == 0, w
        assert f["priced_tasks"] == REC["priced_tasks"][w], (w, f["priced_tasks"])
        assert abs(f["priced_share_named"] - {"aug2025": 99.35, "nov2025": 98.98, "feb2026": 99.30}[w]) < 0.02, w
        assert abs(f["c7_priced_share_named"] - {"aug2025": 55.66, "nov2025": 58.52, "feb2026": 62.22}[w]) < 0.05, \
            (w, f["c7_priced_share_named"])
        assert abs(f["c6_c7_spearman"] - {"aug2025": 0.9869, "nov2025": 0.9859, "feb2026": 0.9870}[w]) < 0.01, \
            (w, f["c6_c7_spearman"])
        assert f["multi_holder10"] == REC["multi_holder10"][w], (w, f["multi_holder10"])
        assert f["multi_holder7"] == REC["multi_holder7"][w], (w, f["multi_holder7"])
        assert f["span_major_group"] == REC["span_major_group"][w], (w, f["span_major_group"])
        assert f["wage_rule_max_gap"] <= 6.38 + 1e-6, (w, f["wage_rule_max_gap"])
        assert f["wage_rule_corr"] > 0.999, (w, f["wage_rule_corr"])
        # the analysis set and the two audited losses (P9 S1, X1, X2)
        assert f["analysis_tasks"] == REC["analysis_tasks"][w], (w, f["analysis_tasks"])
        assert abs(f["analysis_mass_wave"] - REC["analysis_mass_wave"][w]) < 5e-4, (w, f["analysis_mass_wave"])
        assert abs(f["analysis_share_named"] - REC["analysis_share_named"][w]) < 0.01, w
        assert round(f["analysis_conversations"]) == REC["analysis_conversations"][w], (w, f["analysis_conversations"])
        assert f["x1_wage_no_cell"] == REC["x1_wage_no_cell"][w], (w, f["x1_wage_no_cell"])
        assert f["x2_cell_no_wage"] == REC["x2_cell_no_wage"][w], (w, f["x2_cell_no_wage"])
        assert f["analysis_tasks"] + f["x1_wage_no_cell"] == f["priced_tasks"], w
        assert abs(f["kish_named"] - REC["kish_named"][w]) < 0.1, (w, f["kish_named"])
        assert abs(f["kish_analysis"] - REC["kish_analysis"][w]) < 0.1, (w, f["kish_analysis"])
        # the published splits and the internal check (§8(i), §8(iii))
        assert abs(f["split_all_patterns"] - REC["split_all_patterns"][w]) < 5e-4, (w, f["split_all_patterns"])
        assert abs(f["split_five_patterns"] - REC["split_five_patterns"][w]) < 5e-4, (w, f["split_five_patterns"])
        assert abs(f["internal_check_gap"] - REC["internal_check_gap"][w]) < 5e-4, (w, f["internal_check_gap"])
        assert 0 < f["internal_check_gap"] < 0.36, (w, f["internal_check_gap"])
        # quartiles: four quarters of the usage mass, boundaries as recorded
        tot = sum(f["quartiles"][f"Q{q}"]["mass_wave"] for q in (1, 2, 3, 4))
        assert abs(tot - f["analysis_mass_wave"]) < 1e-9, w
        for q in (1, 2, 3, 4):
            assert abs(f["quartiles"][f"Q{q}"]["mass_share"] - 25.0) < 0.6, (w, q)
        for got, rec in zip(f["quartile_bounds"], REC["quartile_bounds"][w]):
            assert abs(got - rec) <= 0.35, (w, f["quartile_bounds"], REC["quartile_bounds"][w])
        assert abs(f["quartiles"]["Q4"]["wage_max"] - 100.0) < 1e-9, w
        # Q1 and Q2 reproduce the steward's Kish N; Q3 and Q4 do not, and cannot, because the
        # third boundary is a wage MASS POINT ($43.40) carrying 8-11 pp of the wave which the
        # pre-registered rule splits by sort order — recorded in the notebook as a DEVIATION and
        # run both ways in script 03. The assertion is therefore a range, with the recorded value
        # inside it for Q1/Q2 and the tie-driven spread allowed for Q3/Q4.
        for qq, rec in zip((1, 2), REC["kish_q"][w][:2]):
            assert abs(f["quartiles"][f"Q{qq}"]["kish"] - rec) <= 3.0, (w, qq, f["quartiles"][f"Q{qq}"]["kish"], rec)
        assert 8.0 <= f["quartiles"]["Q4"]["kish"] <= 20.0, (w, f["quartiles"]["Q4"]["kish"])
        assert f["q4_mass_from_boundary_tie"] > 0, w          # the tie is real in every wave
        for qq in (1, 2, 3, 4):
            assert abs(f["quartiles_fractional"][f"Q{qq}"]["mass_share"] - 25.0) < 1e-6, (w, qq)
        # groups. The steward's 10 / 10 / 8 (groups holding both a Q1 and a Q4 task) and 7 / 8 / 6
        # (all four) are on the 2010 vintage with the group-spanning tasks in a MULTI bucket and on
        # the equal-split wage; A2 assigns every task to one group and the primary wage rule is the
        # employment-weighted one, so the counts may shift by a group. Both readings are printed
        # and both go into results.json; the assertion allows ±2 groups.
        assert abs(f["groups_with_q1_and_q4_2010"] - {"aug2025": 10, "nov2025": 10, "feb2026": 8}[w]) <= 2, \
            (w, f["groups_with_q1_and_q4_2010"])
        assert abs(f["groups_all_four_2010"] - {"aug2025": 7, "nov2025": 8, "feb2026": 6}[w]) <= 2, \
            (w, f["groups_all_four_2010"])
        assert f["groups_present_2019"] == 22, (w, f["groups_present_2019"])
        assert f["a2_group_missing"] == 0, w
        assert abs(f["soc15_share_analysis_a1_2010"] -
                   {"aug2025": 39.86, "nov2025": 37.12, "feb2026": 33.11}[w]) < 1.0, \
            (w, f["soc15_share_analysis_a1_2010"])
        assert abs(f["q1_q4_soc15_a1_2019"] - {"aug2025": 77.1, "nov2025": 75.7, "feb2026": 69.9}[w]) < 6.0, \
            (w, f["q1_q4_soc15_a1_2019"])
        # A2's SOC-15 drop mass is a drop, not a share: it must be within a few points of the A1
        # share on the same vintage, or the assignment rule has broken.
        assert abs(f["soc15_share_analysis_a2_2019"] - f["soc15_share_analysis_a1_2019"]) < 6.0, \
            (w, f["soc15_share_analysis_a2_2019"], f["soc15_share_analysis_a1_2019"])
        # C9 / C10 coverage
        assert f["uc_rows"] == REC["uc_rows"][w], (w, f["uc_rows"])
        if w == "aug2025":
            assert f["uc_facets_containing_use_case"] == [], w      # an absent facet, not an empty cut
        else:
            assert f["uc_analysis_covered"] == f["analysis_tasks"], w   # 100% coverage
            assert f["work_dominant_tasks"] == REC["work_dominant_tasks"][w], (w, f["work_dominant_tasks"])
            assert abs(f["work_dominant_mass_wave"] - REC["work_dominant_mass_wave"][w]) < 5e-4, w
            assert abs(f["work_dominant_share_analysis"] - REC["work_dominant_share_analysis"][w]) < 0.02, w
            assert f["uc_only_nc_analysis"] == REC["uc_only_nc"][w], (w, f["uc_only_nc_analysis"])
            assert f["work_dominant_subst_tasks"] == REC["work_dominant_subst_tasks"][w], w
            assert f["uc_flips"] == REC["uc_flips"][w], (w, f["uc_flips"])
            # the recorded Q1->Q4 work shares are the aggregate `work` cell share of each
            # quartile's use_case counts. Q1 and Q2 reproduce to a few hundredths; Q3 and Q4 move
            # with the $43.40 boundary tie and the wage rule, so the tolerance there is 4.5 pp and
            # what is asserted is the gradient the leg is run for.
            mix = [f["uc_mix_by_q"][f"Q{q}"]["work"] for q in (1, 2, 3, 4)]
            rec = REC["work_share_by_q"][w]
            for i in (0, 1):
                assert abs(mix[i] - rec[i]) < 0.6, (w, mix, rec)
            for i in (2, 3):
                assert abs(mix[i] - rec[i]) < 4.5, (w, mix, rec)
            assert mix[3] - mix[0] > 25.0, (w, mix)
        assert f["c10_matched"] == REC["c10_matched"][w], (w, f["c10_matched"])
        assert f["c10_filtered_one"] == REC["c10_filtered_one"][w], (w, f["c10_filtered_one"])
        assert abs(f["top10_named_share"] - REC["top10_named_share"][w]) < 5e-4, (w, f["top10_named_share"])
        # per-task internal consistency, on the build table itself
        t = builds[w]
        an = t[t.in_analysis]
        assert an.p.between(0, 100).all() and an.n5.gt(0).all(), w
        assert (an.p_pct_route - an.p).abs().max() < 0.05, (w, float((an.p_pct_route - an.p).abs().max()))
        assert an.wage.notna().all() and an.wage.between(0.01, 100.0).all(), w
        assert not an.q.isna().any() and set(an.q.unique()) == {1, 2, 3, 4}, w
        assert (t[["c_" + p for p in PATTERNS]].sum(1) - t.c_all).abs().max() < 1e-9, w

    # November's Seychelles figures (C8) and the pre-registered SC cuts
    fn = F["nov2025"]
    assert fn["sc_usage_count"] == REC["sc_usage_count"], fn["sc_usage_count"]
    assert fn["sc_ix_rows"] == 0, fn["sc_ix_rows"]           # the rates cannot be cleaned
    assert fn["sc_over10_tasks"] == REC["sc_over10_tasks"], fn["sc_over10_tasks"]
    assert abs(fn["sc_over10_mass"] - REC["sc_over10_mass"]) < 5e-3, fn["sc_over10_mass"]
    assert fn["sc_over20_tasks"] == REC["sc_over20_tasks"], fn["sc_over20_tasks"]
    assert abs(fn["sc_over20_mass"] - REC["sc_over20_mass"]) < 5e-3, fn["sc_over20_mass"]

    # Anthropic's released library reproduces Figure 2.11 exactly
    assert abs(fig[0] - REC["fig211"][0]) < 5e-6, fig
    assert abs(fig[1] - REC["fig211"][1]) < 5e-6, fig
    assert fig[2] == REC["fig211"][2], fig

    # the `none`-node variant of the released spec (X7) raises August's global figure to 51.7424
    assert abs(F["aug2025"]["internal_check_with_none_node"] - REC["none_node_variant_aug"]) < 0.01, \
        F["aug2025"]["internal_check_with_none_node"]

    # the C6 thresholds we apply ourselves
    c6a = F["aug2025"]["c6_audit"]
    assert c6a["rows"] == 1090 and c6a["kept"] == 1084 and c6a["dropped"] == 6, c6a
    assert abs(c6a["top_code_hourly"] - 100.0) < 1e-9 and c6a["at_top_code"] == 6, c6a
    assert F["aug2025"]["c5_audit"]["rows"] == 19530 and F["aug2025"]["c5_audit"]["keys"] == 18428, \
        F["aug2025"]["c5_audit"]
    assert F["aug2025"]["c7_audit"]["rows"] == 831, F["aug2025"]["c7_audit"]

    print("\nCHECK BLOCK PASSED — 02_build.py")
