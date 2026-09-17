"""Referee, post1 (LL-07), brief RE-VERDICT after the lead's design pass (BRIEF.md 9af7bad).

Re-derives from the raw files, with my own code and no reference to the steward's or lead's
scripts, the facts the re-verdict rests on:
  A. C9  `onet_task::use_case` at global (Nov 2025, Feb 2026; absent Aug 2025): rows, categories,
         residual labels, the floor/fold rule, the "87.92 / 86.96" mass and what it is the mass OF,
         coverage of the analysis set, the work share by usage-weighted wage quartile (the
         composition rival), and the work-dominant set under the two candidate denominators.
  B. C10 `release_2025_03_27/automation_vs_augmentation_by_task.csv`: columns (is any named
         `collaboration`? any count?), ratio sums, `filtered`, the `task_pct_v2` merge, and the
         intersection with each wave's analysis set.
  C. §9(1)'s ordered five-step rule: does it give every outcome exactly one owner; what does O-A
         actually contain; and the power of each three-wave rule at the conversation-level SE.

The analysis set and the wage quartiles are rebuilt exactly as in my first-verdict script
(`referee_brief_post1.py`): C5 join on lower-cased stripped task text, C6 wage on the full
10-character O*NET-SOC code with the EQUAL-SPLIT holder mean (the steward's primary rule is
employment-weighted; boundaries agree within $0.31). NO quartile automation share is computed.

Run from the repository root:
    python posts/post1/notes/rederivation/referee_brief2_post1_reverdict.py
"""
import itertools
import numpy as np
import pandas as pd
from scipy.stats import norm

ROOT = "data/cache"
WAVES = {
    "aug2025": (f"{ROOT}/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv", "csv"),
    "nov2025": (f"{ROOT}/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet", "pq"),
    "feb2026": (f"{ROOT}/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet", "pq"),
}
AUTO = ["directive", "feedback loop"]
FIVE = AUTO + ["learning", "task iteration", "validation"]
RESID = {"none", "not_classified"}

out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def load(path, kind):
    if kind == "csv":
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != "value":
                df[c] = df[c].astype(str)
    df["value"] = df["value"].astype(float)
    return df

# ---- supplementary: statements (C5) and wage (C6) --------------------------------------------
stm = pd.read_csv(f"{ROOT}/release_2025_09_15/data/intermediate/onet_task_statements.csv",
                  keep_default_na=False, na_values=[], dtype=str)
stm["key"] = stm["Task"].str.lower().str.strip()
holders = stm.groupby("key")["O*NET-SOC Code"].apply(lambda s: sorted(set(s)))
wage = pd.read_csv(f"{ROOT}/release_2025_02_10/wage_data.csv", keep_default_na=False, na_values=[])
wage["MedianSalary"] = pd.to_numeric(wage["MedianSalary"], errors="coerce")
w100 = wage[wage["MedianSalary"] > 100]
wage_by_code = w100.set_index("SOCcode")["MedianSalary"] / 2080.0

def eq_wage(h):
    v = [wage_by_code.get(c) for c in h]
    v = [x for x in v if x is not None and not np.isnan(x)]
    return float(np.mean(v)) if v else np.nan

analysis_sets = {}   # wave -> DataFrame(task, key, w, wage, q)

# ---- per wave: analysis set, quartiles, C9 -----------------------------------------------------
for wv, (path, kind) in WAVES.items():
    df = load(path, kind)
    g = df[df["geography"] == "global"]
    say(f"\n===== {wv} =====")

    # base weights and the intersection (as in the first verdict)
    bt = g[g["facet"] == "onet_task"]
    wpct = bt[bt["variable"] == "onet_task_pct"].set_index("cluster_name")["value"]
    wcnt = bt[bt["variable"] == "onet_task_count"].set_index("cluster_name")["value"]
    named_w = wpct[~wpct.index.isin(RESID)]
    ix = g[g["facet"] == "onet_task::collaboration"].copy()
    p = ix["cluster_name"].str.rsplit("::", n=1); ix["task"], ix["pattern"] = p.str[0], p.str[1]
    C = ix[ix["variable"].str.endswith("_count")].pivot_table(index="task", columns="pattern", values="value", aggfunc="sum").fillna(0.0)
    for pat in FIVE:
        if pat not in C: C[pat] = 0.0
    cls_tasks = set(C[(~C.index.isin(RESID)) & (C[FIVE].sum(axis=1) > 0)].index)

    tasks = pd.DataFrame({"task": named_w.index, "w": named_w.values})
    tasks["key"] = tasks["task"].str.lower().str.strip()
    tasks["holders"] = tasks["key"].map(holders)
    tasks = tasks.dropna(subset=["holders"])
    tasks["wage"] = tasks["holders"].apply(eq_wage)
    an = tasks.dropna(subset=["wage"])
    an = an[an["task"].isin(cls_tasks)].copy()
    an = an.sort_values("wage"); cw = an["w"].cumsum() / an["w"].sum()
    bounds = [an["wage"].values[np.searchsorted(cw.values, q)] for q in (0.25, 0.5, 0.75)]
    an["q"] = (1 + np.searchsorted(np.array(bounds), an["wage"].values, side="right")).clip(1, 4)
    analysis_sets[wv] = an
    say(f"analysis set rebuilt: {len(an)} tasks | {an['w'].sum():.4f} pp of wave | quartile boundaries (equal-split wage) "
        f"{[round(b, 2) for b in bounds]} | tasks per quartile {an.groupby('q')['task'].count().tolist()}")

    # C9
    uc_all = df[df["facet"] == "onet_task::use_case"]
    uc = uc_all[uc_all["geography"] == "global"].copy()
    say(f"C9 onet_task::use_case: rows at global {len(uc)} | rows at other geographies {len(uc_all) - len(uc)} | "
        f"any facet name containing 'use_case': {sorted(f for f in df['facet'].unique() if 'use_case' in f)}")
    if len(uc) == 0:
        say("  -> facet ABSENT in this wave (not an empty cut): legs (d)-(e) untestable, no substitute at task grain")
        continue
    pp = uc["cluster_name"].str.rsplit("::", n=1); uc["task"], uc["cat"] = pp.str[0], pp.str[1]
    say("  variables:", sorted(uc["variable"].unique()), "| level:", sorted(uc["level"].unique()),
        "| categories:", sorted(uc["cat"].unique()), "| base nodes:", uc["task"].nunique(),
        "| named:", uc.loc[~uc["task"].isin(RESID), "task"].nunique())
    U = uc[uc["variable"].str.endswith("_count")].pivot_table(index="task", columns="cat", values="value", aggfunc="sum").fillna(0.0)
    Up = uc[uc["variable"].str.endswith("_pct")].groupby("task")["value"].sum()
    UN = U[~U.index.isin(RESID)]
    subst = [c for c in UN.columns if c not in RESID]
    if "none" in UN.columns:
        nz = UN[UN["none"] > 0]
        say(f"  `none` category: {len(nz)} task cell(s), {UN['none'].sum():.0f} conversations, "
            f"{100 * UN['none'].sum() / UN.sum().sum():.4f}% of the intersection's counts")
    say(f"  min published substantive cell: {UN[subst].replace(0, np.nan).min().min():.0f} | not_classified range: "
        f"{UN['not_classified'].replace(0, np.nan).min():.0f}-{UN['not_classified'].max():.0f} | "
        f"per-task _pct sum min/max: {Up.min():.4f}/{Up.max():.4f} | "
        f"max |sum of cells - onet_task_count|: {(UN.sum(axis=1) - wcnt.reindex(UN.index)).abs().max():.0f}")
    nm = named_w.sum()
    m_work = named_w.reindex(UN.index[UN["work"] > 0]).sum()
    m_both = named_w.reindex(UN.index[(UN["work"] > 0) & (UN["coursework"] > 0)]).sum()
    m_wc = named_w.reindex(UN.index[(UN["work"] > 0) | (UN["coursework"] > 0)]).sum()
    m_any = named_w.reindex(UN.index[UN[subst].sum(axis=1) > 0]).sum()
    say(f"  named mass {nm:.4f} | mass of tasks with a published WORK cell {m_work:.4f} | with BOTH work and coursework "
        f"{m_both:.4f} | work OR coursework {m_wc:.4f} | any substantive cell {m_any:.4f}")
    cov = an["task"].isin(UN.index)
    say(f"  coverage of the analysis set: {cov.sum()} of {len(an)} tasks, {an.loc[cov, 'w'].sum():.4f} of {an['w'].sum():.4f} pp | "
        f"per quartile all covered: {an.groupby('q').apply(lambda d: d['task'].isin(UN.index).all()).tolist()}")
    # composition rival: work share by usage-weighted wage quartile (share of the node's counts)
    A = an.merge(UN, left_on="task", right_index=True, how="left").fillna(0.0)
    for cat in ("work", "personal", "coursework", "not_classified"):
        A[cat + "_sh"] = A[cat] / A[subst + ["not_classified"] + (["none"] if "none" in A.columns else [])].sum(axis=1)
    qs = A.groupby("q").apply(lambda d: pd.Series({c: 100 * np.average(d[c + "_sh"], weights=d["w"]) for c in ("work", "personal", "coursework", "not_classified")}))
    say("  usage-weighted use-case mix by wage quartile Q1..Q4 (% of node counts):")
    for c in ("work", "personal", "coursework", "not_classified"):
        say(f"    {c:15s}", [round(x, 2) for x in qs[c].tolist()])
    # work-dominant set under the two denominators, on the analysis set
    den_all = A[[c for c in UN.columns]].sum(axis=1)
    den_sub = A[subst].sum(axis=1)
    ws_all = A["work"] / den_all
    ws_sub = (A["work"] / den_sub.replace(0, np.nan))
    only_nc = (den_sub == 0)
    dom_all = ws_all >= 0.5
    dom_sub = ws_sub >= 0.5
    say(f"  work-dominant (>= 50%): denominator ALL published cells -> {int(dom_all.sum())} tasks, {A.loc[dom_all, 'w'].sum():.4f} pp "
        f"= {100 * A.loc[dom_all, 'w'].sum() / A['w'].sum():.2f}% of analysis mass | denominator SUBSTANTIVE cells -> "
        f"{int(dom_sub.fillna(False).sum())} tasks | tasks that flip between the two: {int((dom_all != dom_sub.fillna(False)).sum())} | "
        f"analysis-set tasks publishing only not_classified: {int(only_nc.sum())} ({A.loc[only_nc, 'w'].sum():.4f} pp)")
    say(f"  folded residual share of the intersection's counts: {100 * UN['not_classified'].sum() / UN.sum().sum():.2f}% | "
        f"median per-task not_classified pct over the analysis set: {100 * np.median(A['not_classified_sh']):.2f} pp")

# ---- C10 ---------------------------------------------------------------------------------------
say("\n===== C10 release_2025_03_27 =====")
d = f"{ROOT}/release_2025_03_27"
bt = pd.read_csv(f"{d}/automation_vs_augmentation_by_task.csv", keep_default_na=False, na_values=[])
say("columns:", list(bt.columns), "| shape:", bt.shape)
say("  column named 'collaboration':", "collaboration" in bt.columns,
    "| any column containing 'collab':", [c for c in bt.columns if "collab" in c.lower()],
    "| any _count / _pct column:", [c for c in bt.columns if c.endswith(("_count", "_pct"))],
    "| dtypes:", sorted(set(str(t) for t in bt.dtypes)))
ratio = [c for c in bt.columns if c != "task_name"]
rs = bt[ratio].sum(axis=1)
say(f"  row sums: min {rs.min():.12f} median {rs.median():.12f} max {rs.max():.12f} | max |sum-1| {(rs - 1).abs().max():.1e}")
say(f"  filtered: median {bt['filtered'].median():.4f} | rows at 1.0: {int((bt['filtered'] == 1.0).sum())} | rows at 0: {int((bt['filtered'] == 0).sum())}")
tp = pd.read_csv(f"{d}/task_pct_v2.csv", keep_default_na=False, na_values=[])
say("  task_pct_v2:", tp.shape, list(tp.columns), f"| pct sum {tp['pct'].sum():.6f} | none row {tp.loc[tp['task_name'] == 'none', 'pct'].sum():.6f}")
m = tp.merge(bt, on="task_name", how="left", indicator=True)
un = m[m["_merge"] == "left_only"]
mm = m[m["_merge"] == "both"]
say(f"  task_pct_v2 -> by_task: {len(tp)} in, {len(mm)} matched, {len(un)} unmatched ({un['task_name'].tolist()}) | "
    f"matched pct {mm['pct'].sum():.4f} | after weighting by (1 - filtered) {(mm['pct'] * (1 - mm['filtered'])).sum():.4f} | "
    f"usage-weighted filtered {np.average(mm['filtered'], weights=mm['pct']):.6f} | filtered pp of the 100-pct base "
    f"{(mm['pct'] * mm['filtered']).sum():.4f}")
try:
    gl = pd.read_csv(f"{d}/automation_vs_augmentation_v2.csv", keep_default_na=False, na_values=[])
    say("  global automation_vs_augmentation_v2.csv:", list(gl.columns), gl.to_dict("records"))
except Exception as e:  # noqa: BLE001
    say("  global file not read:", e)
bt["key"] = bt["task_name"].str.lower().str.strip()
say(f"  distinct lower-cased keys {bt['key'].nunique()} of {len(bt)} rows")
for wv, an in analysis_sets.items():
    j = an.merge(bt[["key", "filtered"]], on="key", how="left", indicator=True)
    hit = j["_merge"] == "both"
    say(f"  {wv}: analysis-set tasks {len(an)} | in the Mar-2025 file {int(hit.sum())} | unmatched {int((~hit).sum())} | "
        f"matched mass {j.loc[hit, 'w'].sum():.4f} of {an['w'].sum():.4f} pp = {100 * j.loc[hit, 'w'].sum() / an['w'].sum():.2f}% | "
        f"filtered == 1.0 among matched {int((j.loc[hit, 'filtered'] == 1.0).sum())} | usable split {int((j.loc[hit, 'filtered'] < 1.0).sum())}")

# ---- §9(1): partition, O-A content, and the power of the three-wave rules ---------------------
say("\n===== §9(1) ordered rule =====")
def owner(ivs, delta=1.0):
    if all(l > delta for l, u in ivs): return "H1"
    if all(u < -delta for l, u in ivs): return "H2"
    if all(l > 0 for l, u in ivs) or all(u < 0 for l, u in ivs): return "O-A"
    if all(l > -delta and u < delta for l, u in ivs): return "H4"
    return "O-B"
SE = 0.15; half = 1.96 * SE
grid = np.round(np.arange(-2.0, 2.001, 0.1), 2)
counts, oa_all_past, oa_pts_past_any = {}, 0, 0
for pts in itertools.product(grid, repeat=3):
    o = owner([(x - half, x + half) for x in pts])
    counts[o] = counts.get(o, 0) + 1
    if o == "O-A":
        if all(abs(x) > 1 for x in pts): oa_all_past += 1
        if any(abs(x) > 1 for x in pts): oa_pts_past_any += 1
say(f"41^3 grid of point-estimate triples, half-width {half:.3f} pp (SE {SE} pp): owners {counts} | "
    f"total {sum(counts.values())} = 68,921, each triple exactly one owner (ordered 'otherwise' chain)")
say(f"  O-A triples {counts['O-A']}: with ALL three point estimates beyond ±1 pp {oa_all_past}; with AT LEAST one beyond ±1 pp {oa_pts_past_any}")
for pts in ([1.2, 1.15, 1.5], [0.8, 0.8, -0.2], [0.6, 0.6, -0.2], [0.6, 0.6, 0.6], [1.5, 1.5, 0.9], [0.2, -0.2, 0.1]):
    say(f"  points {pts} ->", owner([(x - half, x + half) for x in pts]))
# power: P(rule fires) = prod over three independent waves of the per-wave probability, normal approx
def p_h1(D): return norm.sf((1 + half - D) / SE) ** 3            # lower bound > 1 in all three
def p_oa_or_stronger(D): return norm.sf((half - D) / SE) ** 3      # lower bound > 0 in all three (same sign)
def p_h4(D): return (norm.cdf((1 - half - D) / SE) - norm.cdf((-1 + half - D) / SE)) ** 3   # interval inside ±1 in all three
say("  power of the three-wave rules at the conversation-level SE (independent waves, true D constant across waves):")
for D in (1.0, 1.3, 1.42, 1.52, 1.6, 2.0):
    say(f"    true D = {D:.2f} pp: P(H1 declared) = {p_h1(D):.3f}")
for D in (0.30, 0.42, 0.52, 0.60, 0.80):
    say(f"    true D = {D:.2f} pp: P(all three intervals exclude zero, same sign; i.e. O-A or H1) = {p_oa_or_stronger(D):.3f}")
for D in (0.0, 0.42, 0.50, 0.60, 0.70, 0.80):
    say(f"    true D = {D:.2f} pp: P(all three intervals inside ±1) = {p_h4(D):.3f}")
def solve(f, target=0.8, lo=0.0, hi=5.0):
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < target: lo = mid
        else: hi = mid
    return (lo + hi) / 2
say(f"  smallest true D declared H1 with 80% joint power: {solve(p_h1):.2f} pp | smallest true D with 80% joint power of three same-sign "
    f"zero-excluding intervals: {solve(p_oa_or_stronger):.2f} pp | largest true D at which H4 still fires with 80% joint power: "
    f"{solve(lambda D: 1 - p_h4(D), target=0.2):.2f} pp")
say("  (per-wave MDE(80%) for D != 0 at this SE: 2.80 x SE =", round(2.8 * SE, 2), "pp — the number the brief carries)")

open("posts/post1/notes/rederivation/referee_brief2_post1_reverdict.out.txt", "w").write("\n".join(out) + "\n")
print("Done.")
