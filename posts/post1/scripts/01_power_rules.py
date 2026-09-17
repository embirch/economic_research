"""post1 · 01 · Power of the pre-registered decision rules, per rule and not per wave.

WHAT. `posts/post1/BRIEF.md` §9(1) assigns each result exactly one owner through an ordered
five-step rule on three waves' two-sided 95% intervals for D (the usage-weighted top-minus-bottom
wage-quartile difference in the automation share), with the smallest effect of interest
delta = 1 pp:

    (1) lower bound > +1 pp in all three waves            -> H1
    (2) upper bound < -1 pp in all three waves            -> H2
    (3) otherwise, all three intervals exclude zero, same sign -> O-A
    (4) otherwise, all three intervals inside +-1 pp      -> H4
    (5) otherwise                                         -> O-B

Each step conjoins three waves and is keyed to an interval bound, not to a point estimate, so its
power is not the per-wave MDE. This script computes the power of each *rule*, by an exact normal
calculation and independently by Monte Carlo, and solves for the smallest true |D| each rule
declares with 80% probability. It is the pre-registration's arithmetic for P2 of
`posts/post1/notes/referee-brief-2.md`, and it also re-checks the partition claim of §9(1)
(every outcome triple has exactly one owner).

WHY IT IS SAFE TO RUN BEFORE THE PRE-REGISTRATION IS COMMITTED. It loads no data. The only inputs
are the standard errors the data steward has already published in
`posts/post1/notes/feasibility.md` §4 (model (a), conversation-level binomial with the task mix
held fixed: 0.151 / 0.148 / 0.154 pp for Aug 2025 / Nov 2025 / Feb 2026) and the referee's
0.151 / 0.149 / 0.151 pp. No automation share, no quartile share, no value of D and no leg is
computed or touched.

ASSUMPTIONS, STATED. Independent waves; a constant true D across the three waves; the normal
approximation to the sampling distribution of D-hat at the stated SE; two-sided 95% intervals
(z = 1.959964). Because the per-wave SE varies 0.148-0.154 pp and the true D need not be constant,
every threshold below is reported to +-0.05 pp.

OUTPUT. Console table, and `posts/post1/data/processed/power_rules.json` for results.json to
absorb at the results stage.
"""

import json
import pathlib

import numpy as np
from scipy.stats import norm

Z = norm.ppf(0.975)          # 1.959964, two-sided 95%
DELTA = 1.0                  # pp, the pre-registered smallest effect of interest
SE_STEWARD = (0.151, 0.148, 0.154)   # feasibility.md §4 model (a), Aug / Nov / Feb
SE_REFEREE = (0.151, 0.149, 0.151)   # BRIEF.md §9(4) parenthetical
SE_FLAT = (0.15, 0.15, 0.15)         # the round figure the referee's item 23 quotes


# ---------------------------------------------------------------- rule probabilities (exact)
def _prod(xs):
    out = 1.0
    for x in xs:
        out *= x
    return out


def p_step1(d, ses):
    """P(lower bound > +delta in every wave) = P(H1 declared)."""
    return _prod(norm.cdf((d - DELTA - Z * s) / s) for s in ses)


def p_step2(d, ses):
    """P(upper bound < -delta in every wave) = P(H2 declared)."""
    return _prod(norm.cdf((-DELTA - Z * s - d) / s) for s in ses)


def p_zero_excluded_one_sign(d, ses):
    """P(all three intervals exclude zero with one sign) = P(O-A or stronger)."""
    pos = _prod(norm.cdf((d - Z * s) / s) for s in ses)
    neg = _prod(norm.cdf((-Z * s - d) / s) for s in ses)
    return pos + neg


def p_inside_margin(d, ses):
    """P(all three intervals inside +-delta): step (4)'s clause taken on its own."""
    return _prod(norm.cdf((DELTA - Z * s - d) / s) - norm.cdf((-DELTA + Z * s - d) / s)
                 for s in ses)


def p_inside_and_signed(d, ses):
    """P(all three inside +-delta AND all excluding zero with one sign)."""
    pos = _prod(norm.cdf((DELTA - Z * s - d) / s) - norm.cdf((Z * s - d) / s) for s in ses)
    neg = _prod(norm.cdf((-Z * s - d) / s) - norm.cdf((-DELTA + Z * s - d) / s) for s in ses)
    return pos + neg


def p_step3(d, ses):
    """P(O-A declared): step (3) after steps (1) and (2) have failed."""
    return p_zero_excluded_one_sign(d, ses) - p_step1(d, ses) - p_step2(d, ses)


def p_step4(d, ses):
    """P(H4 declared): step (4) after step (3) has failed."""
    return p_inside_margin(d, ses) - p_inside_and_signed(d, ses)


def p_step5(d, ses):
    """P(O-B declared): the residual of the ordered rule."""
    return 1.0 - p_step1(d, ses) - p_step2(d, ses) - p_step3(d, ses) - p_step4(d, ses)


# ---------------------------------------------------------------- the ordered rule, mechanically
def owner(points, ses):
    """Return the owner of one triple of point estimates under §9(1), first match winning."""
    lo = [p - Z * s for p, s in zip(points, ses)]
    hi = [p + Z * s for p, s in zip(points, ses)]
    if all(x > DELTA for x in lo):
        return "H1"
    if all(x < -DELTA for x in hi):
        return "H2"
    if all(x > 0 for x in lo) or all(x < 0 for x in hi):
        return "O-A"
    if all(l > -DELTA and h < DELTA for l, h in zip(lo, hi)):
        return "H4"
    return "O-B"


def mc_power(d, ses, n=400_000, seed=20260917):
    """Monte Carlo power of each rule, vectorised, independent of the formulas above."""
    rng = np.random.default_rng(seed)
    draws = np.column_stack([rng.normal(d, s, n) for s in ses])
    lo, hi = draws - Z * np.array(ses), draws + Z * np.array(ses)
    h1 = (lo > DELTA).all(1)
    h2 = (hi < -DELTA).all(1)
    signed = (lo > 0).all(1) | (hi < 0).all(1)
    oa = signed & ~h1 & ~h2
    inside = ((lo > -DELTA) & (hi < DELTA)).all(1)
    h4 = inside & ~signed
    ob = ~(h1 | h2 | oa | h4)
    return {"H1": h1.mean(), "H2": h2.mean(), "O-A": oa.mean(), "H4": h4.mean(),
            "O-B": ob.mean(), "inside_margin_clause": inside.mean(),
            "zero_excluded_one_sign": signed.mean()}


def solve_threshold(fn, ses, target=0.80, lo=0.0, hi=4.0, increasing=True):
    """Smallest (increasing) or largest (decreasing) true |D| at which fn reaches `target`."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (fn(mid, ses) < target) == increasing:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------- report
def main():
    rows = []
    print("Power of the §9(1) rules, three waves conjoined, exact normal calculation")
    print("SE set: steward model (a) 0.151 / 0.148 / 0.154 pp   (z = %.6f, delta = %.1f pp)\n" % (Z, DELTA))
    header = f"{'true D (pp)':>12} {'H1':>8} {'H2':>8} {'O-A':>8} {'H4':>8} {'O-B':>8} {'inside±1':>9} {'signed':>8}"
    print(header)
    for d in (0.0, 0.2, 0.3, 0.32, 0.4, 0.49, 0.5, 0.51, 0.7, 1.0, 1.42, 1.5, 1.51, 2.0):
        r = dict(d=d,
                 H1=p_step1(d, SE_STEWARD), H2=p_step2(d, SE_STEWARD),
                 OA=p_step3(d, SE_STEWARD), H4=p_step4(d, SE_STEWARD),
                 OB=p_step5(d, SE_STEWARD),
                 inside=p_inside_margin(d, SE_STEWARD),
                 signed=p_zero_excluded_one_sign(d, SE_STEWARD))
        rows.append(r)
        print(f"{d:12.2f} {r['H1']:8.3f} {r['H2']:8.3f} {r['OA']:8.3f} {r['H4']:8.3f} "
              f"{r['OB']:8.3f} {r['inside']:9.3f} {r['signed']:8.3f}")

    thresholds = {}
    for label, ses in (("steward_0.151_0.148_0.154", SE_STEWARD),
                       ("referee_0.151_0.149_0.151", SE_REFEREE),
                       ("flat_0.15", SE_FLAT)):
        thresholds[label] = {
            "H1_or_H2_80pc": solve_threshold(p_step1, ses),
            "OA_or_stronger_80pc": solve_threshold(p_zero_excluded_one_sign, ses),
            "H4_step4_clause_80pc": solve_threshold(p_inside_margin, ses, increasing=False),
            "H4_declared_80pc": solve_threshold(p_step4, ses, increasing=False),
            "P_H1_at_true_D_1.0": p_step1(1.0, ses),
            "P_H1_at_true_D_1.42": p_step1(1.42, ses),
            "P_H4_declared_at_0.49": p_step4(0.49, ses),
        }
    print("\nSmallest / largest true |D| declared with 80% probability (pp)")
    for label, t in thresholds.items():
        print(f"  {label}:")
        print(f"    H1 (or H2, by symmetry)              80% from  {t['H1_or_H2_80pc']:.3f}")
        print(f"    O-A or stronger (all three signed)   80% from  {t['OA_or_stronger_80pc']:.3f}")
        print(f"    H4, step (4)'s clause alone          80% up to {t['H4_step4_clause_80pc']:.3f}")
        print(f"    H4, DECLARED under the ordered rule  80% up to {t['H4_declared_80pc']:.3f}")
        print(f"    P(H1 | true D = 1.0 pp)              {t['P_H1_at_true_D_1.0']:.4f}")

    mc = {f"{d:.2f}": mc_power(d, SE_STEWARD) for d in (0.0, 0.32, 0.51, 1.0, 1.51)}
    print("\nMonte Carlo (400,000 triples per point, seed 20260917) against the formulas")
    for d, r in mc.items():
        ex = {"H1": p_step1(float(d), SE_STEWARD), "H2": p_step2(float(d), SE_STEWARD),
              "O-A": p_step3(float(d), SE_STEWARD), "H4": p_step4(float(d), SE_STEWARD),
              "O-B": p_step5(float(d), SE_STEWARD)}
        worst = max(abs(r[k] - ex[k]) for k in ex)
        print(f"  true D = {d} pp: max |MC - exact| over the five owners = {worst:.4f}")

    # the partition of §9(1), re-checked mechanically on a grid of point-estimate triples
    grid = np.round(np.linspace(-2.0, 2.0, 41), 4)
    seen, total = {}, 0
    for a in grid:
        for b in grid:
            for c in grid:
                seen[owner((a, b, c), SE_FLAT)] = seen.get(owner((a, b, c), SE_FLAT), 0) + 1
                total += 1
    print(f"\nPartition check: {total} triples on a 41^3 grid, owners {sorted(seen)}")
    print("  counts:", {k: seen[k] for k in sorted(seen)})

    # the MDE arithmetic of the brief, and the rounding in the steward's note
    mde = {"aug2025": 2.8 * SE_STEWARD[0], "nov2025": 2.8 * SE_STEWARD[1],
           "feb2026": 2.8 * SE_STEWARD[2]}
    print("\nMDE(80%, two-sided 5%) = 2.8 x SE on the printed (3 dp) SEs:",
          {k: round(v, 4) for k, v in mde.items()})
    print("  the steward prints 0.42 / 0.42 / 0.43 pp; 2.8 x 0.148 = 0.4144 rounds to 0.41,")
    print("  so the November figure is computed on the unrounded SE (any SE in [0.1482, 0.1518]")
    print("  prints 0.42). Script 03 recomputes SE to four decimals and asserts MDE = 2.8 x SE.")

    out = {
        "z_two_sided_95": Z, "delta_pp": DELTA,
        "se_sets": {"steward_model_a": SE_STEWARD, "referee": SE_REFEREE, "flat": SE_FLAT},
        "rule_power_curve_steward_se": rows,
        "thresholds_80pc": thresholds,
        "monte_carlo": {k: {kk: float(vv) for kk, vv in v.items()} for k, v in mc.items()},
        "partition_grid_counts": {k: seen[k] for k in sorted(seen)},
        "mde_on_printed_se_pp": mde,
        "assumptions": ("independent waves; constant true D; normal approximation at the stated "
                        "SE; two-sided 95%; thresholds reported to +-0.05 pp because the per-wave "
                        "SE varies 0.148-0.154 pp and the true D need not be constant"),
        "script": "posts/post1/scripts/01_power_rules.py",
    }
    dest = pathlib.Path("posts/post1/data/processed/power_rules.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2, default=float) + "\n")
    print(f"\nwrote {dest}")
    return thresholds, mc, seen, total


# ---------------------------------------------------------------- check block
if __name__ == "__main__":
    thresholds, mc, seen, total = main()

    TOL = 0.05   # pp, the tolerance the referee's item 23 states
    for label, t in thresholds.items():
        assert abs(t["H1_or_H2_80pc"] - 1.51) <= TOL, (label, t["H1_or_H2_80pc"])
        assert abs(t["OA_or_stronger_80pc"] - 0.51) <= TOL, (label, t["OA_or_stronger_80pc"])
        assert abs(t["H4_step4_clause_80pc"] - 0.49) <= TOL, (label, t["H4_step4_clause_80pc"])
        # the ordered rule is stricter than step (4)'s clause: O-A takes precedence
        assert t["H4_declared_80pc"] < t["H4_step4_clause_80pc"] - 0.10, label
        assert abs(t["H4_declared_80pc"] - 0.32) <= TOL, (label, t["H4_declared_80pc"])
        # delta = 1 pp is NOT detected by H1 at 80%; the referee's 0.000 and 0.51 reproduce
        assert t["P_H1_at_true_D_1.0"] < 0.001, (label, t["P_H1_at_true_D_1.0"])
        assert abs(t["P_H1_at_true_D_1.42"] - 0.51) <= 0.05, (label, t["P_H1_at_true_D_1.42"])
        assert abs(t["P_H4_declared_at_0.49"] - 0.22) <= 0.05, (label, t["P_H4_declared_at_0.49"])

    # the exact formulas and the Monte Carlo agree to 0.005 on every owner
    for d, r in mc.items():
        ex = {"H1": p_step1(float(d), SE_STEWARD), "H2": p_step2(float(d), SE_STEWARD),
              "O-A": p_step3(float(d), SE_STEWARD), "H4": p_step4(float(d), SE_STEWARD),
              "O-B": p_step5(float(d), SE_STEWARD)}
        for k in ex:
            assert abs(r[k] - ex[k]) <= 0.005, (d, k, r[k], ex[k])

    # the five owners partition the outcome space: exhaustive, unique, all reachable
    assert total == 41 ** 3 == 68921
    assert sum(seen.values()) == total
    assert sorted(seen) == ["H1", "H2", "H4", "O-A", "O-B"]
    assert all(v > 0 for v in seen.values())
    # the problem triples of the first referee verdict resolve as §9(1) says
    assert owner((0.8, 0.8, -0.2), SE_FLAT) == "O-B"
    assert owner((0.6, 0.6, -0.2), SE_FLAT) == "H4"
    assert owner((0.6, 0.6, 0.6), SE_FLAT) == "O-A"
    assert owner((1.2, 1.15, 1.5), SE_FLAT) == "O-A"      # referee item 14
    assert owner((1.5, 1.5, 0.9), SE_FLAT) == "O-A"       # referee item 14
    assert owner((1.5, 1.6, 1.7), SE_FLAT) == "H1"
    assert owner((-1.5, -1.6, -1.7), SE_FLAT) == "H2"

    # probabilities are probabilities, and the ordered rule sums to one
    for d in (0.0, 0.3, 0.5, 1.0, 1.5, 3.0):
        parts = [p_step1(d, SE_STEWARD), p_step2(d, SE_STEWARD), p_step3(d, SE_STEWARD),
                 p_step4(d, SE_STEWARD), p_step5(d, SE_STEWARD)]
        assert all(-1e-12 <= p <= 1 + 1e-12 for p in parts), (d, parts)
        assert abs(sum(parts) - 1.0) < 1e-9, (d, sum(parts))

    # MDE arithmetic: 2.8 x SE, and the November printed-precision gap is at most 0.01 pp
    assert round(2.8 * 0.151, 2) == 0.42 and round(2.8 * 0.154, 2) == 0.43
    assert abs(2.8 * 0.148 - 0.42) <= 0.01

    print("\nCHECK BLOCK PASSED — 01_power_rules.py")
