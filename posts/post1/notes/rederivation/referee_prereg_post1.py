"""Referee re-derivation for the post1 pre-registration review (2026-09-17).

Loads NO data. Inputs are the published per-wave SEs of D (feasibility.md §4 model (a)) and
mass fractions already in BRIEF.md §8/§9. Nothing here touches an automation share, a quartile
share, D, Δ_W or any leg.

Three things are re-derived with the referee's own code, independent of
posts/post1/scripts/01_power_rules.py:

  A. The power of each §9(1) rule, three waves conjoined — including the probability that H4 is
     DECLARED (step (4) after step (3) has failed), which the analyst says the referee's item 23
     mis-stated.  Normal CDF via math.erf, not scipy, so the code path is independent.
  B. The §9(1) partition on the 41³ grid of point-estimate triples.
  C. The H3 leg rule of §9(3) — "a leg fires if D_L loses more than half of D or its sign", on
     point estimates — under the two wave-count readings the pre-registration names (P4):
     the persistent-leg rule (primary) and the literal any-wave rule.  Neither the brief nor the
     pre-registration states this rule's false-declaration rate or its power; this section
     computes both under a stated covariance model so the referee can judge whether the
     completion is a tilt or a necessity, and what the pre-registration must state.

Covariance model for C (stated, approximate). D = A4 − A1 (quartile means of per-task shares).
Var(A1) = Var(A4) = ½ Var(D) (classified counts per quartile are within 20% of each other,
feasibility.md §4). A leg keeps a fraction f1 of Q1's usage mass and f4 of Q4's; the leg's quartile
mean has variance Var(A_q)/f_q and covariance Var(A_q) with the full mean (a sub-mean of a
weighted mean with similar per-unit variance). Hence
    Var(D_L) = ½Var(D)(1/f1 + 1/f4),   Cov(D, D_L) = Var(D).
Leg (a): SOC-15 is 77.1 / 75.7 / 69.9% of Q4 mass (BRIEF §6) and assumed absent from Q1
(f1 = 1; f4 = 0.229 / 0.243 / 0.301). Leg (e): work-dominant tasks retain 53–54% of analysis mass
(BRIEF §9(3)(e)); the quartile work shares are 33 → 62% (Q1 → Q4), so f1 = 0.35 and f4 = 0.65 are
used, with f1 = 0.25 / f4 = 0.60 as a harsher case. Leg (b): identified mass unknown; SE ratios
2.0 and 2.5 are used as illustrations. True D is constant across waves; waves independent.
H3 is evaluated only after H1, H2 or O-A has been declared, so every probability below is
conditional on all three D̂ intervals excluding zero with the positive sign.
"""

import math
import numpy as np

Z = 1.959963984540054
DELTA = 1.0
SE_SETS = {
    "steward 0.151/0.148/0.154": (0.151, 0.148, 0.154),
    "referee 0.151/0.149/0.151": (0.151, 0.149, 0.151),
    "flat 0.15": (0.15, 0.15, 0.15),
}


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# ------------------------------------------------------------------ A. rule power, own derivation
def per_wave(d, s):
    """Per-wave probabilities of the interval events, given true D = d and SE = s."""
    lo_gt_delta = 1.0 - Phi((DELTA + Z * s - d) / s)          # lower bound > +1
    hi_lt_mdelta = Phi((-DELTA - Z * s - d) / s)              # upper bound < -1
    lo_gt_0 = 1.0 - Phi((Z * s - d) / s)                      # lower bound > 0
    hi_lt_0 = Phi((-Z * s - d) / s)                           # upper bound < 0
    inside = Phi((DELTA - Z * s - d) / s) - Phi((-DELTA + Z * s - d) / s)   # both bounds in ±1
    inside_pos = Phi((DELTA - Z * s - d) / s) - Phi((Z * s - d) / s)        # 0 < lo, hi < 1
    inside_neg = Phi((-Z * s - d) / s) - Phi((-DELTA + Z * s - d) / s)      # -1 < lo, hi < 0
    return dict(lo_gt_delta=lo_gt_delta, hi_lt_mdelta=hi_lt_mdelta, lo_gt_0=lo_gt_0,
                hi_lt_0=hi_lt_0, inside=inside, inside_pos=inside_pos, inside_neg=inside_neg)


def owners_prob(d, ses):
    pw = [per_wave(d, s) for s in ses]
    prod = lambda k: math.prod(p[k] for p in pw)
    h1 = prod("lo_gt_delta")
    h2 = prod("hi_lt_mdelta")
    signed = prod("lo_gt_0") + prod("hi_lt_0")
    oa = signed - h1 - h2
    inside = prod("inside")
    h4 = inside - prod("inside_pos") - prod("inside_neg")
    ob = 1.0 - h1 - h2 - oa - h4
    return dict(H1=h1, H2=h2, OA=oa, H4=h4, OB=ob, signed=signed, inside=inside)


def bisect(f, target, lo, hi, increasing=True, it=200):
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        below = f(mid) < target
        if below == increasing:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def section_a(out):
    out.append("A. Power of the §9(1) rules, three waves conjoined (referee's own code, math.erf)")
    keep = {}
    for label, ses in SE_SETS.items():
        f_h1 = lambda d: owners_prob(d, ses)["H1"]
        f_signed = lambda d: owners_prob(d, ses)["signed"]
        f_inside = lambda d: owners_prob(d, ses)["inside"]
        f_h4 = lambda d: owners_prob(d, ses)["H4"]
        t_h1 = bisect(f_h1, 0.80, 0.0, 4.0)
        t_oa = bisect(f_signed, 0.80, 0.0, 4.0)
        t_h4c = bisect(f_inside, 0.80, 0.0, 4.0, increasing=False)
        t_h4d = bisect(f_h4, 0.80, 0.0, 4.0, increasing=False)
        out.append(f"  SE set {label}:")
        out.append(f"    H1 (H2 by symmetry)          80% from   {t_h1:.3f} pp   P(H1|D=1.0)={f_h1(1.0):.5f}  P(H1|D=1.42)={f_h1(1.42):.3f}")
        out.append(f"    O-A or stronger (all signed) 80% from   {t_oa:.3f} pp")
        out.append(f"    H4 clause alone (all inside) 80% up to  {t_h4c:.3f} pp   clause at 0.70: {f_inside(0.70):.3f}")
        out.append(f"    H4 DECLARED (after step 3)   80% up to  {t_h4d:.3f} pp   declared at 0.49: {f_h4(0.49):.3f}, at 0.32: {f_h4(0.32):.3f}")
        keep[label] = dict(t_h1=t_h1, t_oa=t_oa, t_h4c=t_h4c, t_h4d=t_h4d)
    ses = SE_SETS["steward 0.151/0.148/0.154"]
    out.append("  Owner probabilities at the steward's SEs (true D constant across waves):")
    out.append(f"  {'D':>5} {'H1':>7} {'H2':>7} {'O-A':>7} {'H4':>7} {'O-B':>7} | {'inside':>7} {'signed':>7}")
    for d in (0.0, 0.2, 0.3, 0.32, 0.4, 0.49, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.42, 1.5, 1.52, 2.0):
        p = owners_prob(d, ses)
        assert abs(p["H1"] + p["H2"] + p["OA"] + p["H4"] + p["OB"] - 1) < 1e-9
        out.append(f"  {d:5.2f} {p['H1']:7.3f} {p['H2']:7.3f} {p['OA']:7.3f} {p['H4']:7.3f} {p['OB']:7.3f} | {p['inside']:7.3f} {p['signed']:7.3f}")
    return keep["steward 0.151/0.148/0.154"]


# ------------------------------------------------------------------ B. partition, own code
def owner_of(triple, ses):
    lo = [p - Z * s for p, s in zip(triple, ses)]
    hi = [p + Z * s for p, s in zip(triple, ses)]
    if min(lo) > DELTA:
        return "H1"
    if max(hi) < -DELTA:
        return "H2"
    if min(lo) > 0 or max(hi) < 0:
        return "O-A"
    if min(lo) > -DELTA and max(hi) < DELTA:
        return "H4"
    return "O-B"


def section_b(out):
    grid = np.round(np.linspace(-2, 2, 41), 4)
    counts = {}
    for a in grid:
        for b in grid:
            for c in grid:
                k = owner_of((a, b, c), (0.15, 0.15, 0.15))
                counts[k] = counts.get(k, 0) + 1
    out.append("B. §9(1) partition on the 41^3 grid at SE 0.15: " + str(dict(sorted(counts.items()))))
    assert sum(counts.values()) == 68921 and set(counts) == {"H1", "H2", "O-A", "H4", "O-B"}
    for trip, exp in (((0.8, 0.8, -0.2), "O-B"), ((0.6, 0.6, -0.2), "H4"), ((0.6, 0.6, 0.6), "O-A"),
                      ((1.2, 1.15, 1.5), "O-A"), ((1.5, 1.5, 0.9), "O-A"), ((1.5, 1.6, 1.7), "H1")):
        got = owner_of(trip, (0.15, 0.15, 0.15))
        assert got == exp, (trip, got, exp)
    out.append("   named triples resolve as §9(1) says (6 asserted)")
    return counts


# ------------------------------------------------------------------ C. the H3 leg rule
def leg_cov(var_d, f1, f4=None, se_ratio=None):
    """Return (Var(D_L), Cov(D, D_L)) under the stated model; se_ratio overrides f1/f4."""
    if se_ratio is not None:
        return (se_ratio ** 2) * var_d, var_d
    return 0.5 * var_d * (1.0 / f1 + 1.0 / f4), var_d


def simulate_leg(d, rho_loss, ses, legs, n=200_000, seed=17):
    """rho_loss: fraction of D the leg truly loses (0 = no composition, 0.75 = three-quarters lost).
    Returns dict of per-wave fire probabilities (conditional on declaration) and the H3 rates under
    the persistent-leg and any-wave readings, over the given legs.
    legs: dict name -> list of (Var(D_L), Cov(D,D_L)) per wave (None where untestable)."""
    rng = np.random.default_rng(seed)
    W = len(ses)
    # draw D-hat per wave
    Dhat = np.column_stack([rng.normal(d, s, n) for s in ses])
    declared = (Dhat - Z * np.array(ses) > 0).all(axis=1)      # all three signed positive
    fires = {}
    for name, per_wave_cov in legs.items():
        F = np.zeros((n, W), dtype=bool)
        testable = np.zeros(W, dtype=bool)
        for w in range(W):
            if per_wave_cov[w] is None:
                continue
            testable[w] = True
            var_d = ses[w] ** 2
            var_l, cov = per_wave_cov[w]
            # conditional draw of D_L-hat given D-hat (bivariate normal)
            mean_l = d * (1 - rho_loss) + (cov / var_d) * (Dhat[:, w] - d)
            var_l_cond = var_l - cov ** 2 / var_d
            Lhat = mean_l + rng.normal(0, math.sqrt(max(var_l_cond, 0)), n)
            F[:, w] = (np.sign(Lhat) != np.sign(Dhat[:, w])) | (np.abs(Lhat) < 0.5 * np.abs(Dhat[:, w]))
        fires[name] = (F, testable)
    # H3 under the two readings, conditional on declaration
    sel = declared
    nd = sel.sum()
    res = {"P(declared)": declared.mean(), "n_declared": int(nd)}
    persist_any_leg = np.zeros(n, dtype=bool)
    anywave_any_leg = np.zeros(n, dtype=bool)
    for name, (F, testable) in fires.items():
        Ft = F[:, testable]
        per_wave = Ft[sel].mean(axis=0)
        persist = Ft.all(axis=1)
        anyw = Ft.any(axis=1)
        res[f"{name} per-wave fire"] = per_wave
        res[f"{name} persistent"] = persist[sel].mean()
        res[f"{name} any-wave"] = anyw[sel].mean()
        persist_any_leg |= persist
        anywave_any_leg |= anyw
    res["H3 persistent-leg rule"] = persist_any_leg[sel].mean()
    res["H3 any-wave rule"] = anywave_any_leg[sel].mean()
    return res


def section_c(out):
    ses = SE_SETS["steward 0.151/0.148/0.154"]
    f4_a = (0.229, 0.243, 0.301)            # 1 − SOC-15 share of Q4 mass, Aug / Nov / Feb
    legs_main = {
        "leg(a)": [leg_cov(s ** 2, 1.0, f4) for s, f4 in zip(ses, f4_a)],
        "leg(b)": [leg_cov(s ** 2, None, se_ratio=2.0) for s in ses],
        "leg(e)": [None] + [leg_cov(s ** 2, 0.35, 0.65) for s in ses[1:]],
    }
    legs_harsh = {
        "leg(a)": [leg_cov(s ** 2, 1.0, f4) for s, f4 in zip(ses, f4_a)],
        "leg(b)": [leg_cov(s ** 2, None, se_ratio=2.5) for s in ses],
        "leg(e)": [None] + [leg_cov(s ** 2, 0.25, 0.60) for s in ses[1:]],
    }
    out.append("C. The H3 leg rule on point estimates: false-declaration rate and power, conditional on a")
    out.append("   declared positive gradient (all three D-hat intervals exclude zero). Covariance model in docstring.")
    for w, s in enumerate(ses):
        va, ca = legs_main["leg(a)"][w]
        out.append(f"   wave {w}: SE(D)={s:.3f}  SE(D_a)={math.sqrt(va):.3f} (x{math.sqrt(va)/s:.2f})  corr(D,D_a)={ca/math.sqrt(va*s*s):.2f}"
                   f"  SE(D_a - D/2)={math.sqrt(va + 0.25*s*s - ca):.3f}"
                   + (f"  SE(D_e)={math.sqrt(legs_main['leg(e)'][w][0]):.3f} (x{math.sqrt(legs_main['leg(e)'][w][0])/s:.2f})" if legs_main['leg(e)'][w] else "  leg(e) untestable"))
    for tag, legs in (("main", legs_main), ("harsh", legs_harsh)):
        out.append(f"   --- scenario set: {tag} (leg(b) SE ratio {'2.0' if tag=='main' else '2.5'}; leg(e) f1/f4 {'0.35/0.65' if tag=='main' else '0.25/0.60'})")
        out.append(f"   {'true D':>7} {'loss':>5} | {'a/wave':>18} | {'a pers':>7} {'a any':>7} | {'b pers':>7} {'b any':>7} | {'e pers':>7} {'e any':>7} | {'H3 pers':>8} {'H3 any':>7}")
        for d in (0.5, 0.6, 0.8, 1.0, 1.5, 2.0):
            for loss in (0.0, 0.5, 0.75, 1.0):
                r = simulate_leg(d, loss, ses, legs)
                pa = r["leg(a) per-wave fire"]
                out.append(f"   {d:7.2f} {loss:5.2f} | {pa[0]:5.3f} {pa[1]:5.3f} {pa[2]:5.3f} | "
                           f"{r['leg(a) persistent']:7.3f} {r['leg(a) any-wave']:7.3f} | "
                           f"{r['leg(b) persistent']:7.3f} {r['leg(b) any-wave']:7.3f} | "
                           f"{r['leg(e) persistent']:7.3f} {r['leg(e) any-wave']:7.3f} | "
                           f"{r['H3 persistent-leg rule']:8.3f} {r['H3 any-wave rule']:7.3f}")
    out.append("   Reading: 'loss 0.00' rows are the false-declaration rate of H3 when no composition exists;")
    out.append("   'loss 0.75' rows are the power to declare H3 when the leg truly loses three-quarters of D.")


if __name__ == "__main__":
    out = []
    ta = section_a(out)
    section_b(out)
    section_c(out)
    # check block: the analyst's P2 figures reproduce with independent code
    assert abs(ta["t_h1"] - 1.517) < 0.002, ta
    assert abs(ta["t_oa"] - 0.517) < 0.002, ta
    assert abs(ta["t_h4c"] - 0.483) < 0.002, ta
    assert abs(ta["t_h4d"] - 0.324) < 0.002, ta
    out.append("CHECK BLOCK PASSED — referee_prereg_post1.py (P2 figures reproduce: 1.517 / 0.517 / 0.483 / 0.324)")
    text = "\n".join(out)
    print(text)
    import pathlib
    pathlib.Path(__file__).with_suffix(".out.txt").write_text(text + "\n")
