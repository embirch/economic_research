"""Referee re-derivation · post1 (LL-07) · results stage · 2026-09-17

Independent of the analyst's scripts: nothing is imported from posts/post1/scripts/. The analysis
set, the wage, the usage-weighted quartiles, the per-task shares, D, its P1 interval, Δ_W and the
H3 legs (a) and (e) are rebuilt from the raw cache files exactly as prereg.md (content c9b1b45)
defines them, and compared with posts/post1/data/processed/results.json.

Three headline numbers, at minimum (procedure item 1):
  (1) D and its P1 interval, all three waves (the owner rests on the three intervals);
  (2) Δ_W, all three waves;
  (3) leg (a) — D with Computer & Mathematical excluded — in all three waves (the H3 declaration
      rests on legs (a) and (b) firing in every wave); leg (e) in Nov and Feb beside it.
Then the §9(1) chain is applied to the analyst's three intervals, independently.

Extra checks the referee wanted for the red-team memo (not part of the confirmatory set):
  · the fractional ("corrected") quartile rule, to see whether the deviation's number reproduces;
  · what the C7 (BLS-EP) wage coverage does to SOC-15's share of the top quartile — the test of
    whether the second wage source is a second source or a disguised leg (a);
  · the Nov X5 (> 10 % Seychelles) drop, which flips the November sign in the analyst's table;
  · Q4 effective N under the registered rule.

Raw inputs (paths from feasibility.md §1, §7):
  release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv
  release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv
  release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv
  release_2025_09_15/data/intermediate/onet_task_statements.csv       (C5, O*NET 20.1)
  release_2025_02_10/wage_data.csv                                      (C6)
  supplementary/bls_employment_projections/occupationProj.html          (C7 / W1 employment)
  supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv (V1)
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[4]
CACHE = ROOT / "data/cache"
RES = json.load(open(ROOT / "posts/post1/data/processed/results.json"))
Z = 1.959964

AUTO = ["directive", "feedback loop"]
CLASSIFIED = AUTO + ["learning", "task iteration", "validation"]
RESID = ["none", "not_classified"]

WAVES = {
    "aug2025": CACHE / "release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
    "nov2025": CACHE / "release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv",
    "feb2026": CACHE / "release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv",
}

out_lines: list[str] = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out_lines.append(s)


# ------------------------------------------------------------------ reference tables
def load_c5():
    on = pd.read_csv(CACHE / "release_2025_09_15/data/intermediate/onet_task_statements.csv",
                     keep_default_na=False, na_values=[], dtype=str)
    on["key"] = on["Task"].str.lower().str.strip()
    # holders: distinct 10-char O*NET-SOC codes per key
    return on.groupby("key")["O*NET-SOC Code"].agg(lambda s: tuple(sorted(set(s))))


def load_c6():
    wg = pd.read_csv(CACHE / "release_2025_02_10/wage_data.csv", keep_default_na=False, na_values=[])
    wg = wg[wg.MedianSalary > 100]                # this post's pre-join filter
    return (wg.set_index("SOCcode").MedianSalary.astype(float) / 2080.0)


def load_bls_ep():
    """BLS-EP table: occ_code (7-char SOC-2018) → (median annual wage 2025, employment 2025)."""
    html = (CACHE / "supplementary/bls_employment_projections/occupationProj.html").read_text(errors="ignore")
    tables = pd.read_html(html)
    t = max(tables, key=len)
    t.columns = [c[0] if isinstance(c, tuple) else c for c in t.columns]
    t = t.loc[:, ~t.columns.duplicated()]
    code_col = [c for c in t.columns if "Code" in str(c)][0]
    wage_col = [c for c in t.columns if "Wage" in str(c)][0]
    emp_col = [c for c in t.columns if str(c).startswith("Employment 2025") or str(c) == "Employment 2025"][0]
    t["occ"] = t[code_col].astype(str).str.strip()
    t = t[t.occ.str.match(r"^\d\d-\d{4}$")]
    t["wage"] = pd.to_numeric(t[wage_col].astype(str).str.replace(r"[^0-9.]", "", regex=True), errors="coerce")
    t["emp"] = pd.to_numeric(t[emp_col].astype(str).str.replace(r"[^0-9.]", "", regex=True), errors="coerce")
    t = t.set_index("occ")
    return (t.wage / 2080.0).dropna(), t.emp.dropna()


def load_xw():
    xw = pd.read_csv(CACHE / "supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv",
                     keep_default_na=False, na_values=[], dtype=str)
    xw.columns = ["c2010", "t2010", "c2019", "t2019"]
    return xw.groupby("c2010")["c2019"].agg(lambda s: tuple(sorted(set(s))))


HOLDERS = load_c5()
C6 = load_c6()
C7, EMP = load_bls_ep()
XW = load_xw()
say(f"C5 keys {len(HOLDERS):,}; C6 priced codes {len(C6):,}; BLS-EP wage rows {len(C7)}, emp rows {len(EMP)}; "
    f"crosswalk 2010 codes {len(XW)}")


# ------------------------------------------------------------------ per-wave build (my own)
def wage_rules(holders, price, emp, seven):
    """(employment-weighted, equal-split, modal) over the holders that carry a price."""
    vals, wts = [], []
    for h in holders:
        k = h[:7] if seven else h
        if k in price.index:
            vals.append(float(price[k]))
            wts.append(float(emp[h[:7]]) if h[:7] in emp.index else np.nan)
    if not vals:
        return np.nan, np.nan, np.nan
    v, w = np.array(vals), np.array(wts)
    ok = np.isfinite(w) & (w > 0)
    eq = v.mean()
    if ok.any():
        return float(np.average(v[ok], weights=w[ok])), float(eq), float(v[np.argmax(np.where(ok, w, -np.inf))])
    return float(eq), float(eq), float(v[0])


def a2_group_2019(holders, emp, xw):
    best, be = None, -np.inf
    for h in sorted(holders):
        e = float(emp[h[:7]]) if h[:7] in emp.index else -1.0
        if best is None or e > be:
            best, be = h, e
    codes = xw.get(best)
    if not codes:
        return None
    return sorted(codes)[0][:2]


def build(wave):
    path = WAVES[wave]
    df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    df["value"] = pd.to_numeric(df["value"])
    g = df[df.geography == "global"]
    ix = g[g.facet == "onet_task::collaboration"].copy()
    parts = ix.cluster_name.str.rsplit("::", n=1)
    ix["task"], ix["pattern"] = parts.str[0], parts.str[1]
    ixn = ix[~ix.task.isin(RESID) & ix.variable.str.endswith("_count")]
    cnt = ixn.pivot_table(index="task", columns="pattern", values="value", aggfunc="sum").fillna(0.0)
    for p in CLASSIFIED + RESID:
        if p not in cnt.columns:
            cnt[p] = 0.0
    base = g[g.facet == "onet_task"]
    wpct = base[base.variable == "onet_task_pct"].set_index("cluster_name").value
    wcnt = base[base.variable == "onet_task_count"].set_index("cluster_name").value
    named = wpct[~wpct.index.isin(RESID)]
    t = pd.DataFrame({"task": named.index, "w": named.values})
    t["cnt"] = wcnt.reindex(t.task).values
    t["key"] = t.task.str.lower().str.strip()
    t = t[t.key.isin(HOLDERS.index)].copy()
    t["holders"] = [HOLDERS[k] for k in t.key]
    for p in CLASSIFIED + RESID:
        t["c_" + p] = cnt[p].reindex(t.task).fillna(0.0).values
    t["n5"] = t[["c_" + p for p in CLASSIFIED]].sum(1)
    t["p"] = np.where(t.n5 > 0, (t.c_directive + t["c_feedback loop"]) / t.n5.where(t.n5 > 0, np.nan) * 100, np.nan)
    r6 = [wage_rules(h, C6, EMP, False) for h in t.holders]
    r7 = [wage_rules(h, C7, EMP, True) for h in t.holders]
    t["wage"] = [r[0] for r in r6]
    t["wage_eq"] = [r[1] for r in r6]
    t["wage_modal"] = [r[2] for r in r6]
    t["wage_c7"] = [r[0] for r in r7]
    t["g19"] = [a2_group_2019(h, EMP, XW) for h in t.holders]
    t["in"] = (t.n5 > 0) & t.wage.notna()
    # use_case (Nov, Feb)
    uc = g[g.facet == "onet_task::use_case"]
    t["work_share"] = np.nan
    if len(uc):
        uc = uc[uc.variable.str.endswith("_count")].copy()
        parts = uc.cluster_name.str.rsplit("::", n=1)
        uc["task"], uc["cat"] = parts.str[0], parts.str[1]
        ut = uc[~uc.task.isin(RESID)].pivot_table(index="task", columns="cat", values="value", aggfunc="sum").fillna(0.0)
        cells = ut.sum(1)
        subst = ut.drop(columns=[c for c in ["not_classified"] if c in ut.columns]).sum(1)
        ws = pd.Series(np.where((cells > 0) & (subst > 0), ut.get("work", 0.0) / cells.where(cells > 0, np.nan), np.nan),
                       index=ut.index)
        t["work_share"] = ws.reindex(t.task).values
    # Seychelles share of the global count (Nov)
    t["sc_share"] = 0.0
    if wave == "nov2025":
        sc = df[(df.geography == "country") & (df.geo_id == "SC") & (df.facet == "onet_task")
                & (df.variable == "onet_task_count")].set_index("cluster_name").value
        t["sc_share"] = (sc.reindex(t.task).fillna(0.0).values / t.cnt.values)
    an = t[t["in"]].copy().reset_index(drop=True)
    return an, dict(named=len(named), named_mass=float(named.sum()), n_an=len(an), an_mass=float(an.w.sum()),
                    an_conv=float(an.n5.sum()))


def quartile_labels(an, wage_col="wage"):
    """Registered rule, ties ordered on (wage, task) as the analyst's DEVIATION fixes it."""
    s = an.sort_values([wage_col, "task"], kind="mergesort")
    cw = s.w.cumsum() / s.w.sum()
    q = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw.values, side="left") + 1, 4)
    return pd.Series(q, index=s.index).reindex(an.index).astype(int)


def fractional_weights(an, wage_col="wage"):
    """Corrected rule: a wage value straddling a boundary is shared in proportion."""
    w = an.w.to_numpy(float)
    wage = an[wage_col].to_numpy(float)
    total = w.sum()
    out = np.zeros((len(an), 4))
    order = np.argsort(wage, kind="mergesort")
    cum, i = 0.0, 0
    while i < len(order):
        j = i
        while j < len(order) and wage[order[j]] == wage[order[i]]:
            j += 1
        idx = order[i:j]
        mass = w[idx].sum()
        lo, hi = cum / total, (cum + mass) / total
        for k in range(4):
            ov = max(0.0, min(hi, (k + 1) / 4) - max(lo, k / 4))
            if ov > 0:
                out[idx, k] = w[idx] * ov / (hi - lo)
        cum += mass
        i = j
    return out


def lin(c, p_pp, n):
    """L = Σ c_i p_i with P1's binomial variance; returns coef, se, ci (pp)."""
    p = np.asarray(p_pp, float) / 100
    c = np.asarray(c, float)
    n = np.asarray(n, float)
    coef = float(c @ p * 100)
    var = float(np.sum(c ** 2 * p * (1 - p) / n) * 1e4)
    se = np.sqrt(var)
    return coef, se, (coef - Z * se, coef + Z * se)


def d_from_masks(an, m4, m1):
    w = an.w.to_numpy(float)
    c = np.where(m4, w / w[m4].sum(), 0.0) - np.where(m1, w / w[m1].sum(), 0.0)
    return lin(c, an.p.to_numpy(), an.n5.to_numpy())


def kish(w):
    w = np.asarray(w, float)
    w = w[w > 0]
    return float(w.sum() ** 2 / (w ** 2).sum())


def fmt(v):
    return f"{v[0]:+.4f} [{v[2][0]:+.4f}, {v[2][1]:+.4f}] se {v[1]:.4f}"


results = {}
for wave in ["aug2025", "nov2025", "feb2026"]:
    an, f = build(wave)
    q = quartile_labels(an)
    an["q"] = q
    m4, m1 = (q == 4).to_numpy(), (q == 1).to_numpy()
    bounds = tuple(float(an.wage[an.q == k].max()) for k in (1, 2, 3))
    D = d_from_masks(an, m4, m1)
    # Δ_W
    w, wage, p, n = an.w.to_numpy(float), an.wage.to_numpy(float), an.p.to_numpy(), an.n5.to_numpy()
    a = w * wage / (w * wage).sum()
    b = w / w.sum()
    DW = lin(a - b, p, n)
    # fractional rule D
    qf = fractional_weights(an)
    cf = qf[:, 3] / qf[:, 3].sum() - qf[:, 0] / qf[:, 0].sum()
    Df = lin(cf, p, n)
    # leg (a): SOC-15 (2019 recode, A2) excluded, masks kept
    not15 = (an.g19 != "15").to_numpy()
    La = d_from_masks(an, m4 & not15, m1 & not15)
    soc15_q4 = float(w[m4 & ~not15].sum() / w[m4].sum() * 100)
    # leg (e), Nov & Feb: work share ≥ 0.5, undefined dropped
    Le = None
    if an.work_share.notna().any():
        wd = (an.work_share >= 0.5).to_numpy()
        Le = d_from_masks(an, m4 & wd, m1 & wd)
    # C7 coverage of Q4 and SOC-15 within the C7-covered Q4
    has7 = an.wage_c7.notna().to_numpy()
    c7_q4_cov = float(w[m4 & has7].sum() / w[m4].sum() * 100)
    c7_q4_soc15 = float(w[m4 & has7 & ~not15].sum() / max(w[m4 & has7].sum(), 1e-12) * 100)
    c7_soc15_cov = float(w[~not15 & has7].sum() / w[~not15].sum() * 100)
    # C7 gradient, with quartiles re-drawn on the C7-priced subset (the analyst's rob_C7)
    an7 = an[has7].copy()
    q7 = quartile_labels(an7, "wage_c7")
    D7 = d_from_masks(an7, (q7 == 4).to_numpy(), (q7 == 1).to_numpy())
    soc15_q4_c7 = float(an7.w[(q7 == 4) & (an7.g19 == "15")].sum() / an7.w[q7 == 4].sum() * 100)
    # X5 (Nov): drop tasks with SC > 10 % of the global count, masks kept
    X5 = None
    if wave == "nov2025":
        keep = (an.sc_share <= 0.10).to_numpy()
        X5 = d_from_masks(an, m4 & keep, m1 & keep)
        sc_q4_mass = float(w[m4 & ~keep].sum())
        sc_tasks = int((~keep).sum())
    # modal-holder wage rule, quartiles re-drawn
    qm = quartile_labels(an, "wage_modal")
    Dm = d_from_masks(an, (qm == 4).to_numpy(), (qm == 1).to_numpy())

    R = RES["tests"]
    rD = R[f"D_{wave}"]["estimates"]["D"]
    rDc = R[f"D_{wave}"]["estimates"]["D_corrected_quartile_rule"]
    rDW = R[f"DeltaW_{wave}"]["estimates"]["Delta_W"]
    rLa = R[f"leg_a_{wave}"]["estimates"]["D_L"]
    say("=" * 100)
    say(f"[{wave}] named {f['named']} ({f['named_mass']:.4f} pp); analysis set {f['n_an']} tasks, "
        f"{f['an_mass']:.4f} pp, {f['an_conv']:,.0f} classified conversations   "
        f"(analyst: {RES['facts'][f'sample_{wave}']['value']} tasks, "
        f"{RES['facts'][f'sample_{wave}']['analysis_mass_wave']:.4f} pp, "
        f"{RES['facts'][f'sample_{wave}']['classified_conversations']:,.0f})")
    say(f"  quartile bounds ${bounds[0]:.2f} / ${bounds[1]:.2f} / ${bounds[2]:.2f}   "
        f"(analyst {['$%.2f' % b for b in RES['facts'][f'quartile_boundaries_{wave}']['value']]})")
    say(f"  Q1 {int(m1.sum())} tasks Kish {kish(w[m1]):.1f}; Q4 {int(m4.sum())} tasks Kish {kish(w[m4]):.1f}; "
        f"SOC-15 share of Q4 mass {soc15_q4:.2f}%")
    say(f"  D  (registered rule)  mine {fmt(D)}")
    say(f"                        analyst {rD['coef']:+.4f} [{rD['ci'][0]:+.4f}, {rD['ci'][1]:+.4f}] se {rD['se']:.4f}"
        f"   |Δ| = {abs(D[0] - rD['coef']):.2e} pp, |Δse| = {abs(D[1] - rD['se']):.2e}")
    say(f"  D  (fractional rule)  mine {fmt(Df)}   analyst {rDc['coef']:+.4f}   |Δ| = {abs(Df[0] - rDc['coef']):.2e}")
    say(f"  Δ_W                   mine {fmt(DW)}")
    say(f"                        analyst {rDW['coef']:+.4f} [{rDW['ci'][0]:+.4f}, {rDW['ci'][1]:+.4f}] se {rDW['se']:.4f}"
        f"   |Δ| = {abs(DW[0] - rDW['coef']):.2e} pp")
    say(f"  leg (a) SOC-15 out    mine {fmt(La)}")
    say(f"                        analyst {rLa['coef']:+.4f} [{rLa['ci'][0]:+.4f}, {rLa['ci'][1]:+.4f}] se {rLa['se']:.4f}"
        f"   |Δ| = {abs(La[0] - rLa['coef']):.2e} pp")
    if Le is not None:
        rLe = R[f"leg_e_{wave}"]["estimates"]["D_L"]
        say(f"  leg (e) work-dominant mine {fmt(Le)}   analyst {rLe['coef']:+.4f} se {rLe['se']:.4f}   |Δ| = {abs(Le[0] - rLe['coef']):.2e} pp")
    say(f"  -- red-team checks --")
    say(f"  C7 prices {c7_q4_cov:.1f}% of Q4 mass; SOC-15 is {c7_q4_soc15:.1f}% of the C7-priced Q4 mass; "
        f"C7 prices {c7_soc15_cov:.1f}% of SOC-15 analysis mass")
    say(f"  C7 rebuild D (quartiles on C7 wage) mine {fmt(D7)}   analyst {R[f'rob_C7_{wave}']['estimates']['D']['coef']:+.4f}; "
        f"SOC-15 share of the C7 Q4 = {soc15_q4_c7:.1f}%")
    say(f"  modal-holder wage rule D mine {fmt(Dm)}   analyst {R[f'rob_W1_modal_holder_{wave}']['estimates']['D']['coef']:+.4f}")
    if X5 is not None:
        say(f"  X5 drop SC>10%: {sc_tasks} tasks, {sc_q4_mass:.3f} pp of Q4 mass; D mine {fmt(X5)}   "
            f"analyst {R['rob_X5_drop_sc_over_10pc_nov2025']['estimates']['D']['coef']:+.4f}")
    results[wave] = dict(D=D, Df=Df, DW=DW, La=La, Le=Le, bounds=bounds, D7=D7, Dm=Dm)

# ------------------------------------------------------------------ the §9(1) chain, my own
say("=" * 100)
say("§9(1) ordered chain applied to the ANALYST's three intervals (results.json facts.declared_owner.intervals):")
ivs = RES["facts"]["declared_owner"]["intervals"]
lo = [x[0] for x in ivs]
hi = [x[1] for x in ivs]
delta = 1.0
if all(l > delta for l in lo):
    owner = "H1"
elif all(h < -delta for h in hi):
    owner = "H2"
elif all(l > 0 for l in lo) or all(h < 0 for h in hi):
    owner = "O-A"
elif all(l > -delta and h < delta for l, h in zip(lo, hi)):
    owner = "H4"
else:
    owner = "O-B"
say(f"  step1 all lower > +1: {all(l > delta for l in lo)}; step2 all upper < -1: {all(h < -delta for h in hi)}; "
    f"step3 all same-signed excl. 0: {all(l > 0 for l in lo) or all(h < 0 for h in hi)}; "
    f"step4 all inside ±1: {all(l > -delta and h < delta for l, h in zip(lo, hi))}")
say(f"  OWNER (mine) = {owner}; analyst declared {RES['facts']['declared_owner']['value']}")
# and on my own intervals
lo2 = [results[w]["D"][2][0] for w in ["aug2025", "nov2025", "feb2026"]]
hi2 = [results[w]["D"][2][1] for w in ["aug2025", "nov2025", "feb2026"]]
own2 = "H1" if all(l > 1 for l in lo2) else "H2" if all(h < -1 for h in hi2) else \
    "O-A" if (all(l > 0 for l in lo2) or all(h < 0 for h in hi2)) else \
    "H4" if all(l > -1 and h < 1 for l, h in zip(lo2, hi2)) else "O-B"
say(f"  OWNER on my own re-derived intervals = {own2}")

# H3 declaration from my leg (a) numbers
fires_a = [np.sign(results[w]["La"][0]) != np.sign(results[w]["D"][0]) or abs(results[w]["La"][0]) < 0.5 * abs(results[w]["D"][0])
           for w in ["aug2025", "nov2025", "feb2026"]]
fires_e = [np.sign(results[w]["Le"][0]) != np.sign(results[w]["D"][0]) or abs(results[w]["Le"][0]) < 0.5 * abs(results[w]["D"][0])
           for w in ["nov2025", "feb2026"]]
say(f"  leg (a) fires by wave (mine): {fires_a}  → persistent-leg rule on leg (a) alone: {all(fires_a)}")
say(f"  leg (e) fires by wave (mine): {fires_e}")

pathlib.Path(__file__).with_suffix(".out.txt").write_text("\n".join(out_lines) + "\n")
