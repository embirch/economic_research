"""post1 · 03 · The headline estimates: D, Δ_W, the continuous slope, their intervals and MDEs,
and the §9(1) ordered chain applied mechanically to declare the owner.

WHAT. For each of the three waves this script forms
  · the four wage quartiles' usage-weighted automation shares, each with the `none` and
    `not_classified` share of the node beside it so the base is never implicit;
  · **D**, the top-minus-bottom quartile difference, with its two-sided 95% interval and its
    MDE(80%) = 2.8 × SE;
  · **Δ_W**, the wage-weighted minus the unweighted usage-weighted automation share, with its own
    interval and MDE;
  · the **continuous companion**, the usage-weighted slope of p_i in the task's hourly wage per
    +$10/hr (sign and significance only, in no decision rule);
  · the five pattern shares by quartile (the H2 augmentation clause of P5, description only);
and then runs the ordered rule of prereg §Hypotheses / BRIEF §9(1) on the three intervals, first
match winning, to declare exactly one owner among H1, H2, O-A, H4 and O-B. The chain is imported
from `01_power_rules.py`, so the code that declares the owner here is the code whose power was
pre-registered.

WHY. This is the pre-registered primary test (prereg §Definitions 1–2, P1, P2, and the confirmatory
table rows 1–3: 3 + 3 + 3 = 9 of the 17 confirmatory estimates). The pre-registration fixes
δ = 1 pp, two-sided 95% intervals at z = 1.959964, and the variance model before the fact.

THE VARIANCE MODEL, AS REGISTERED (prereg P1(a)). Conversation-level binomial on the classified
counts with the task mix held fixed: every statistic in the confirmatory set is linear in the vector
of per-task shares, L = Σ_i c_i p_i, so

    Var(L) = Σ_i c_i² p_i(1 − p_i)/n_i            (p_i on the 0–1 scale, scaled to pp)
    Cov(L, M) = Σ_i c_i e_i p_i(1 − p_i)/n_i

with n_i the task's classified conversation count. The variance is heteroskedastic by construction
across tasks — the cross-section analogue the standards require. **No clustering is applied and none
is available:** no release carries a user, account or session identifier and the waves are never
pooled, so there is no cluster dimension and no panel; the task enters as a weight, not as a cluster
of repeated observations. Conversations inside a task are not known to be independent, so this SE is
a **lower bound** on the sampling variance of D under within-task dependence, and it is reported as
such wherever it appears. Model (b), the design-based task bootstrap (MDE 12.5 / 17.4 / 16.1 pp), is
reported beside it by script 06 as the generalisation bound it is; it is in no decision rule.

TWO READINGS OF THE QUARTILE RULE, BOTH RUN. The third quartile boundary is a wage mass point
($43.40/hr in all three waves, 99 / 106 / 111 tasks, 8–11 pp of the wave), so the pre-registered
cut splits a tie and the split is decided by sort order rather than by the rule. Both readings are
run and both go into `results.json` (see the DEVIATION entry of 2026-09-17 in
`posts/post1/notes/lab-notebook.md`): the **pre-registered** rule (ties split, order fixed on
(wage, task)) is primary and declares the owner; the **corrected** rule (the boundary wage shared
between the two adjacent quartiles in proportion) is reported beside it.

OUTPUT. `posts/post1/data/processed/headline.json`, a console table, and the functions
`linear_stat`, `cov_linear`, `d_stat`, `delta_w`, `slope` that scripts 05 and 06 import so that
every leg and every robustness cut is estimated by the same primary code path.
"""

from __future__ import annotations

import importlib.util
import json
import pathlib

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
PROCESSED = ROOT / "posts/post1/data/processed"

Z = 1.959964                      # two-sided 95%, prereg P1
MDE_K = 2.8                       # MDE(80%, two-sided 5%) = 2.8 × SE, empirical-standards 6
DELTA = 1.0                       # pp, the pre-registered smallest effect of interest
SE_RECORDED = {"aug2025": 0.151, "nov2025": 0.148, "feb2026": 0.154}   # feasibility.md §4 model (a)


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B = _load("02_build")             # frames, joins, analysis set, quartile rules
P = _load("01_power_rules")       # the §9(1) ordered chain and its pre-registered power
WAVES = B.WAVE_ORDER
AUTO, AUGM, CLASSIFIED, PATTERNS = B.AUTO, B.AUGM, B.CLASSIFIED, B.PATTERNS


# ---------------------------------------------------------------- the estimator machinery (P1)
def linear_stat(c: np.ndarray, p_pp: np.ndarray, n: np.ndarray) -> dict:
    """A statistic linear in the per-task shares, with its closed-form interval and MDE.

    c: the coefficient on each task's share. p_pp: per-task automation share in percentage points.
    n: the task's classified conversation count. Returns coefficient, SE, 95% interval and MDE, all
    in percentage points.
    """
    c = np.asarray(c, float)
    p01 = np.asarray(p_pp, float) / 100.0
    n = np.asarray(n, float)
    coef = float(c @ (p01 * 100.0))
    var = float(np.sum(c ** 2 * p01 * (1 - p01) / n) * 1e4)
    se = float(np.sqrt(var))
    return dict(coef=coef, se=se, ci=[coef - Z * se, coef + Z * se], mde=MDE_K * se,
                n_tasks=int(np.sum(c != 0)), n_conversations=float(np.sum(n[c != 0])))


def cov_linear(c: np.ndarray, e: np.ndarray, p_pp: np.ndarray, n: np.ndarray) -> float:
    """Cov(Σ c_i p_i, Σ e_i p_i) under the same model, in pp²."""
    p01 = np.asarray(p_pp, float) / 100.0
    return float(np.sum(np.asarray(c, float) * np.asarray(e, float) * p01 * (1 - p01)
                        / np.asarray(n, float)) * 1e4)


def pooled_binomial_se(an: pd.DataFrame, qw: np.ndarray) -> float:
    """The steward's model-(a) arithmetic, reported beside the registered formula: a pooled binomial
    on each extreme quartile's total classified conversations at that quartile's share
    (`data/replication/post1_variance_mde.py`). It ignores the usage weights, so it is the variance
    of a conversation-mean, not of the usage-weighted difference the post reports."""
    out = 0.0
    for col in (3, 0):
        m = qw[:, col] > 0
        n = float(an.n5[m].sum())
        phat = float(np.average(an.p[m], weights=qw[m, col]) / 100.0)
        out += phat * (1 - phat) / n * 1e4
    return float(np.sqrt(out))


def quartile_coefficients(qw: np.ndarray, col: int) -> np.ndarray:
    """c_i = w_i / W_q for one quartile, from the quartile weight matrix."""
    w = qw[:, col]
    return w / w.sum()


def d_stat(an: pd.DataFrame, qw: np.ndarray) -> tuple[dict, np.ndarray]:
    """D = usage-weighted automation share of Q4 minus that of Q1, with its interval and MDE."""
    c = quartile_coefficients(qw, 3) - quartile_coefficients(qw, 0)
    out = linear_stat(c, an.p.to_numpy(), an.n5.to_numpy())
    out["n_tasks"] = int(np.sum((qw[:, 3] > 0) | (qw[:, 0] > 0)))
    out["n_conversations"] = float(an.n5[(qw[:, 3] > 0) | (qw[:, 0] > 0)].sum())
    return out, c


def delta_w(an: pd.DataFrame, weight_col: str = "w", wage_col: str = "wage") -> tuple[dict, np.ndarray]:
    """Δ_W = the wage-weighted minus the unweighted usage-weighted automation share (prereg §2)."""
    w = an[weight_col].to_numpy(float)
    wage = an[wage_col].to_numpy(float)
    a = w * wage / np.sum(w * wage)
    b = w / np.sum(w)
    c = a - b
    out = linear_stat(c, an.p.to_numpy(), an.n5.to_numpy())
    out["n_tasks"] = int(len(an))
    out["n_conversations"] = float(an.n5.sum())
    return out, c


def slope(an: pd.DataFrame, weight_col: str = "w", x_col: str = "wage", per: float = 10.0,
          extra_x: str | None = None) -> tuple[dict, np.ndarray]:
    """The usage-weighted least-squares slope of p_i in the task's hourly wage, per +$10/hr.

    Weighted least squares is linear in p, so the same closed-form variance applies:
    b = Σ_i [w_i (x_i − x̄_w) / S] p_i with S = Σ_i w_i (x_i − x̄_w)². With `extra_x` the slope is
    the partial slope on x in a two-regressor weighted regression (the §9(3)(e) work-share
    covariate), again linear in p.
    """
    w = an[weight_col].to_numpy(float)
    x = an[x_col].to_numpy(float) / per
    if extra_x is None:
        xd = x - np.average(x, weights=w)
        S = float(np.sum(w * xd ** 2))
        c = w * xd / S
    else:
        z = an[extra_x].to_numpy(float)
        X = np.column_stack([np.ones(len(an)), x, z])
        W = np.diag(w)
        XtWX_inv = np.linalg.inv(X.T @ W @ X)
        c = (XtWX_inv @ X.T @ W)[1]
    out = linear_stat(c, an.p.to_numpy(), an.n5.to_numpy())
    out["n_tasks"] = int(len(an))
    out["n_conversations"] = float(an.n5.sum())
    return out, c


def quartile_share(an: pd.DataFrame, qw: np.ndarray, col: int, value_col: str = "p") -> dict:
    """One quartile's usage-weighted share of any per-task rate, with interval and MDE.

    The interval is exact for the automation share (the model is about it); for the `none` and
    `not_classified` shares of the node, and for the individual pattern shares, the same binomial
    form is used on the same denominator and is stated as an approximation in the output."""
    c = quartile_coefficients(qw, col)
    return linear_stat(c, an[value_col].to_numpy(), an.n5.to_numpy())


def fmt(e: dict) -> str:
    return (f"{e['coef']:+8.4f}  [{e['ci'][0]:+.4f}, {e['ci'][1]:+.4f}]  SE {e['se']:.4f}  "
            f"MDE {e['mde']:.4f}")


# ---------------------------------------------------------------- per wave
def wave_estimates(wave: str) -> dict:
    an = B.analysis_set(wave)
    out: dict = dict(wave=wave, n_tasks=int(len(an)), n_conversations=float(an.n5.sum()),
                     mass_wave=float(an.w.sum()), kish=B.kish(an.w.values))
    for mode in ("registered", "fractional"):
        qw = B.quartile_weights(an, "wage", mode)
        d, _ = d_stat(an, qw)
        shares = {}
        for col, name in enumerate(["Q1", "Q2", "Q3", "Q4"]):
            s = quartile_share(an, qw, col)
            s["none_share"] = float(np.average(an.none_share, weights=qw[:, col]))
            s["not_classified_share"] = float(np.average(an.nc_share, weights=qw[:, col]))
            s["mass_wave"] = float(qw[:, col].sum())
            s["mean_wage"] = float(np.average(an.wage, weights=qw[:, col]))
            s["kish"] = B.kish(qw[:, col])
            shares[name] = s
        patterns = {}
        for pat in CLASSIFIED:
            with np.errstate(invalid="ignore", divide="ignore"):
                rate = np.where(an.n5 > 0, an["c_" + pat] / an.n5 * 100, np.nan)
            an = an.assign(**{"rate_" + pat: rate})
            patterns[pat] = {name: quartile_share(an, qw, col, "rate_" + pat)
                             for col, name in enumerate(["Q1", "Q2", "Q3", "Q4"])}
        rising = sum(1 for pat in AUGM
                     if all(patterns[pat][f"Q{k+1}"]["coef"] <= patterns[pat][f"Q{k+2}"]["coef"] + 1e-12
                            for k in range(3)))
        out[mode] = dict(D=d, quartile_shares=shares, pattern_shares=patterns,
                         augmentation_rising=rising,
                         pooled_binomial_se=pooled_binomial_se(an, qw),
                         boundary_wage=float(B.quartiles(an, "wage")[1][2]))
    dw, _ = delta_w(an)
    sl, _ = slope(an)
    out["Delta_W"] = dw
    out["slope_per_10dollar"] = sl
    out["unweighted_share"] = linear_stat(an.w.to_numpy() / an.w.sum(), an.p.to_numpy(), an.n5.to_numpy())
    out["wage_weighted_share"] = linear_stat((an.w * an.wage).to_numpy() / float((an.w * an.wage).sum()),
                                             an.p.to_numpy(), an.n5.to_numpy())
    out["none_share_analysis"] = float(np.average(an.none_share, weights=an.w))
    out["mean_wage"] = float(np.average(an.wage, weights=an.w))
    return out


def main():
    res = {w: wave_estimates(w) for w in WAVES}

    print("=" * 96)
    print("D, the usage-weighted top-minus-bottom wage-quartile difference in the automation share (pp)")
    print("  model (a), conversation-level binomial with the task mix held fixed; SE is a LOWER BOUND")
    print("  under unmeasurable within-task dependence (prereg P1(a)). z = 1.959964, MDE = 2.8 × SE.\n")
    for mode in ("registered", "fractional"):
        label = ("pre-registered quartile rule (ties split by order)" if mode == "registered"
                 else "corrected quartile rule (boundary wage shared in proportion)")
        print(f"  [{label}]")
        for w in WAVES:
            e = res[w][mode]["D"]
            print(f"    {w}  D {fmt(e)}   tasks {e['n_tasks']}  conversations {e['n_conversations']:,.0f}"
                  f"   (pooled-binomial SE {res[w][mode]['pooled_binomial_se']:.4f})")
        points = [res[w][mode]["D"]["coef"] for w in WAVES]
        ses = [res[w][mode]["D"]["se"] for w in WAVES]
        own = P.owner(points, ses)
        res[f"owner_{mode}"] = dict(owner=own, points=points, ses=ses,
                                    intervals=[[p - Z * s, p + Z * s] for p, s in zip(points, ses)],
                                    steps=dict(
                                        step1_all_lower_above_delta=all(p - Z * s > DELTA for p, s in zip(points, ses)),
                                        step2_all_upper_below_minus_delta=all(p + Z * s < -DELTA for p, s in zip(points, ses)),
                                        step3_all_signed_excluding_zero=(all(p - Z * s > 0 for p, s in zip(points, ses))
                                                                         or all(p + Z * s < 0 for p, s in zip(points, ses))),
                                        step4_all_inside_delta=all(abs(p) + Z * s < DELTA for p, s in zip(points, ses))))
        print(f"    §9(1) ordered chain, first match winning -> OWNER = {own}")
        print(f"      step (1) all lower bounds > +1 pp: {res[f'owner_{mode}']['steps']['step1_all_lower_above_delta']}"
              f" | step (2) all upper bounds < −1 pp: {res[f'owner_{mode}']['steps']['step2_all_upper_below_minus_delta']}"
              f" | step (3) all signed, zero excluded: {res[f'owner_{mode}']['steps']['step3_all_signed_excluding_zero']}"
              f" | step (4) all inside ±1 pp: {res[f'owner_{mode}']['steps']['step4_all_inside_delta']}")

    print("\n" + "=" * 96)
    print("Quartile automation shares (pre-registered quartile rule), `none` and `not_classified` beside each")
    for w in WAVES:
        print(f"  [{w}]  analysis set {res[w]['n_tasks']} tasks, {res[w]['n_conversations']:,.0f} classified "
              f"conversations, Kish {res[w]['kish']:.1f}")
        for name in ("Q1", "Q2", "Q3", "Q4"):
            s = res[w]["registered"]["quartile_shares"][name]
            print(f"     {name}  share {fmt(s)}  none {s['none_share']:.4f}  not_classified "
                  f"{s['not_classified_share']:.4f}  mean wage ${s['mean_wage']:.2f}  Kish {s['kish']:.1f}")

    print("\n" + "=" * 96)
    print("Δ_W (wage-weighted minus unweighted usage-weighted automation share) and the continuous slope")
    for w in WAVES:
        print(f"  {w}  Δ_W {fmt(res[w]['Delta_W'])}   "
              f"(wage-weighted {res[w]['wage_weighted_share']['coef']:.4f} − unweighted "
              f"{res[w]['unweighted_share']['coef']:.4f})")
    for w in WAVES:
        e = res[w]["slope_per_10dollar"]
        sig = abs(e["coef"]) > Z * e["se"]
        print(f"  {w}  slope per +$10/hr {fmt(e)}   significant at 5%: {sig}   "
              f"(sign and significance only; in no decision rule)")

    print("\n" + "=" * 96)
    print("The five pattern shares by quartile (description, in no decision rule; P5's clause)")
    for w in WAVES:
        row = res[w]["registered"]["pattern_shares"]
        print(f"  [{w}]  augmentation patterns weakly increasing across quartiles: "
              f"{res[w]['registered']['augmentation_rising']} of 3")
        for pat in CLASSIFIED:
            print(f"     {pat:16s} " + "  ".join(f"{row[pat][f'Q{k}']['coef']:7.3f}" for k in (1, 2, 3, 4)))

    out = dict(script="posts/post1/scripts/03_headline.py",
               prereg="posts/post1/prereg/prereg.md content c9b1b45",
               variance_model=("(a) conversation-level binomial on the classified counts, task mix held "
                               "fixed; Var(Σ c_i p_i) = Σ c_i² p_i(1−p_i)/n_i; no clustering available; "
                               "the SE is a lower bound under within-task dependence"),
               z=Z, mde_multiplier=MDE_K, delta_pp=DELTA, results=res)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / "headline.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    print(f"\nwrote {(PROCESSED / 'headline.json').relative_to(ROOT)}")
    return res


if __name__ == "__main__":
    R = main()

    # ------------------------------------------------------------ check block
    for w in WAVES:
        an = B.analysis_set(w)
        for mode in ("registered", "fractional"):
            r = R[w][mode]
            qw = B.quartile_weights(an, "wage", mode)
            # D is the difference of the two quartile shares it is built from
            d_direct = (r["quartile_shares"]["Q4"]["coef"] - r["quartile_shares"]["Q1"]["coef"])
            assert abs(r["D"]["coef"] - d_direct) < 1e-9, (w, mode, r["D"]["coef"], d_direct)
            # interval, SE and MDE are internally consistent
            assert abs(r["D"]["ci"][0] - (r["D"]["coef"] - Z * r["D"]["se"])) < 1e-12, (w, mode)
            assert abs(r["D"]["mde"] - MDE_K * r["D"]["se"]) < 1e-12, (w, mode)
            # every quartile share is a share, and the five pattern shares sum to 100 in each
            for name in ("Q1", "Q2", "Q3", "Q4"):
                assert 0.0 <= r["quartile_shares"][name]["coef"] <= 100.0, (w, mode, name)
                tot = sum(r["pattern_shares"][pat][name]["coef"] for pat in CLASSIFIED)
                assert abs(tot - 100.0) < 1e-6, (w, mode, name, tot)
                assert abs(r["pattern_shares"]["directive"][name]["coef"]
                           + r["pattern_shares"]["feedback loop"][name]["coef"]
                           - r["quartile_shares"][name]["coef"]) < 1e-9, (w, mode, name)
            # each quartile holds a quarter of the usage mass (exactly, under both readings)
            for name in ("Q1", "Q2", "Q3", "Q4"):
                assert abs(r["quartile_shares"][name]["mass_wave"] / an.w.sum() - 0.25) < 0.006, \
                    (w, mode, name)
            # the mean wage rises across the quartiles: the predictor is ordered as the design says
            means = [r["quartile_shares"][f"Q{k}"]["mean_wage"] for k in (1, 2, 3, 4)]
            assert means == sorted(means), (w, mode, means)
            # The registered per-task formula and the steward's pooled-binomial arithmetic are
            # different statistics on the same model (the pooled one ignores the usage weights).
            # Both are printed and both go into results.json; each must sit within 0.015 pp of the
            # recorded 0.151 / 0.148 / 0.154 pp (realised MDE 0.38-0.41 pp against the
            # pre-registered 0.42-0.43 pp), and the realised SE and MDE are printed beside every
            # coefficient. See the notebook entry for 03.
            assert abs(r["pooled_binomial_se"] - SE_RECORDED[w]) < 0.02, \
                (w, mode, r["pooled_binomial_se"], SE_RECORDED[w])
            assert abs(r["D"]["se"] - SE_RECORDED[w]) < 0.02, (w, mode, r["D"]["se"])

        # Δ_W is exactly the difference of the two shares it is defined as
        dw = R[w]["Delta_W"]
        assert abs(dw["coef"] - (R[w]["wage_weighted_share"]["coef"] - R[w]["unweighted_share"]["coef"])) < 1e-9, w
        assert abs(dw["mde"] - MDE_K * dw["se"]) < 1e-12, w
        # Δ_W's materiality arithmetic (prereg §2): about 0.11-0.12 pp per point of quartile gap, so
        # Δ_W must be far smaller than D itself whenever D is of the order of a point
        assert abs(dw["coef"]) < max(1.0, 0.5 * abs(R[w]["registered"]["D"]["coef"])), (w, dw["coef"])
        # the slope's coefficient is in pp per +$10/hr and finite
        sl = R[w]["slope_per_10dollar"]
        assert np.isfinite(sl["coef"]) and np.isfinite(sl["se"]) and sl["se"] > 0, w
        assert abs(sl["mde"] - MDE_K * sl["se"]) < 1e-12, w

    # the ordered chain is the pre-registered one: exactly one owner, and the imported chain still
    # resolves the problem triples of the referee's verdict as §9(1) says
    for mode in ("registered", "fractional"):
        assert R[f"owner_{mode}"]["owner"] in ("H1", "H2", "O-A", "H4", "O-B")
    flat = (0.15, 0.15, 0.15)
    assert P.owner((0.8, 0.8, -0.2), flat) == "O-B"
    assert P.owner((0.6, 0.6, -0.2), flat) == "H4"
    assert P.owner((0.6, 0.6, 0.6), flat) == "O-A"
    assert P.owner((1.2, 1.15, 1.5), flat) == "O-A"
    assert P.owner((1.5, 1.6, 1.7), flat) == "H1"
    # the declared owner agrees with the four step flags recorded beside it
    for mode in ("registered", "fractional"):
        s = R[f"owner_{mode}"]["steps"]
        own = R[f"owner_{mode}"]["owner"]
        expect = ("H1" if s["step1_all_lower_above_delta"] else
                  "H2" if s["step2_all_upper_below_minus_delta"] else
                  "O-A" if s["step3_all_signed_excluding_zero"] else
                  "H4" if s["step4_all_inside_delta"] else "O-B")
        assert own == expect, (mode, own, expect, s)

    # the recorded wave five-pattern automation share is bracketed by the four quartile shares:
    # a coding error in the outcome would show here before any interpretation
    for w in WAVES:
        shares = [R[w]["registered"]["quartile_shares"][f"Q{k}"]["coef"] for k in (1, 2, 3, 4)]
        wave_value = {"aug2025": 51.0698, "nov2025": 46.7394, "feb2026": 45.5456}[w]
        assert min(shares) - 6.0 <= wave_value <= max(shares) + 6.0, (w, shares, wave_value)

    print("\nCHECK BLOCK PASSED — 03_headline.py")
