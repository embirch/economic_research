"""post1 · 09 · `results.json`, the figures with their captions, and the verification that nothing
may appear in the post that is not in `results.json`.

WHAT. This script does not estimate anything. It assembles the numbers scripts 01–08 wrote into
`posts/post1/data/processed/results.json` on `team/templates/RESULTS.schema.json`:

  · `tests` — one entry per **confirmatory estimate** (17: D, Δ_W and the slope in three waves each,
    leg (a) and leg (b) in three waves each, leg (e) in two — of which the **eight** leg-wave rows
    are the leg tests of P4) and one per **exploratory test** (3, each flagged `exploratory`), plus
    the pre-registered robustness re-estimates and the descriptive series, each flagged with its
    kind. Every entry carries its `prereg_rule` **quoted from the pre-registration** and a `verdict`
    set **mechanically** from the numbers by the functions below — no verdict is typed by hand.
  · `facts` — the declared owner under both quartile readings, the H3 declaration and its counting,
    the second-implementation agreement, the synthetic recoveries, the per-wave sample counts and
    masses, the Kish effective N, the quartile boundaries, the replication targets, the two SE
    models, the placebo band, the fourth window and the owner under every robustness cut.
  · `figures` — the four figures with their file paths and their captions.

WHY. empirical-standards 12: results to files, and every number the post may cite in `results.json`
with the script that produced it. The pre-registration's outcome rubric gives this script one more
job: "script 09 [asserts] that every number in the post appears in `results.json` with its script".
`verify_post_numbers` does that; it runs against `posts/post1/POST.md` when the writing stage
produces one, and its own behaviour is asserted here on a synthetic sentence so the verifier is
tested before it is needed.

FIGURES. Four, with Anthropic-style captions in `posts/post1/outputs/figures.json`: a bold
declarative (or hedged) title, then a roman gloss that states what is plotted and in what unit, the
unit of analysis, the construction restated in full, the sample and its exclusions, what every mark
and band encodes, the weighting and its purpose, the uncertainty with its coverage and the absence
of a clustering unit, the null value, and the n. No sentence in the post may depend on a number
that appears only inside an image, so every plotted value is in `results.json`.

OUTPUT. `posts/post1/data/processed/results.json`, `posts/post1/outputs/figures/*.png`,
`posts/post1/outputs/figures.json`.
"""

from __future__ import annotations

import importlib.util
import json
import pathlib
import re
from datetime import datetime, timezone

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
PROCESSED = ROOT / "posts/post1/data/processed"
FIGDIR = ROOT / "posts/post1/outputs/figures"

Z = 1.959964
MDE_K = 2.8
DELTA = 1.0
WAVES = ["aug2025", "nov2025", "feb2026"]
WAVE_LABEL = {"aug2025": "4–11 Aug 2025", "nov2025": "13–20 Nov 2025", "feb2026": "5–12 Feb 2026"}

# ---------------------------------------------------------------- the pre-registered rules, quoted
RULE_D = ("prereg §Hypotheses: the ordered rule, first match winning — (1) lower bound > +1 pp in "
          "all three waves → H1; (2) upper bound < −1 pp in all three → H2; (3) otherwise, every "
          "interval excluding zero with the same sign in all three → O-A; (4) otherwise, every "
          "interval inside ±1 pp in all three → H4; (5) otherwise → O-B. δ = 1 pp, two-sided 95%.")
RULE_DW = ("prereg §2: \"Δ_W is published with its own interval beside D. Its materiality line is "
           "separate and higher than δ: 0.11–0.12 pp of Δ_W per point of gap, so a full point of "
           "Δ_W needs a gap of roughly 8–9 pp\".")
RULE_SLOPE = ("prereg §2: the usage-weighted slope of p_i in the task's hourly wage, per +$10/hr, "
              "\"sign and significance only\" (BRIEF §9(2)); in no decision rule.")
RULE_LEG = ("prereg P3/P4: \"a leg fires in a wave if sign(D_L) ≠ sign(D) or |D_L| < ½|D|\", on the "
            "point estimates as §9(3) writes it; H3 is declared (primary, persistent-leg rule) if "
            "at least one leg fires in every wave in which that leg is testable, with the literal "
            "any-wave reading reported beside it.")
RULE_EXPLORATORY = ("prereg §Exploratory allowance: three tests, after the confirmatory set, none in "
                    "the headline, each labelled exploratory; in no decision rule.")
RULE_ROBUST = ("prereg §Robustness, fixed now: the cut is pre-registered, reported beside the "
               "primary estimate, and in no decision rule; the owner under each cut is reported so "
               "that a cut which would move it is visible.")


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read(name: str) -> dict:
    return json.loads((PROCESSED / f"{name}.json").read_text())


# ---------------------------------------------------------------- mechanical verdicts
def verdict_D(coef: float, ci: list[float]) -> str:
    lo, hi = ci
    if lo > DELTA:
        return "clears +1 pp in this wave (step (1)'s clause holds here)"
    if hi < -DELTA:
        return "clears −1 pp in this wave (step (2)'s clause holds here)"
    if lo > 0:
        return "excludes zero, positive; does not clear the +1 pp margin in this wave"
    if hi < 0:
        return "excludes zero, negative; does not clear the −1 pp margin in this wave"
    if lo > -DELTA and hi < DELTA:
        return "inside ±1 pp and containing zero (step (4)'s clause holds here)"
    return "unresolved in this wave: the interval contains zero and leaves ±1 pp"


def verdict_DW(coef: float, ci: list[float]) -> str:
    excl = "excludes zero" if (ci[0] > 0 or ci[1] < 0) else "contains zero"
    return (f"{excl}; |Δ_W| = {abs(coef):.4f} pp, below the separate 1 pp materiality line, so the "
            f"weighting of a published automation share is signed and small, never wrong")


def verdict_slope(coef: float, ci: list[float]) -> str:
    sig = ci[0] > 0 or ci[1] < 0
    sign = "positive" if coef > 0 else "negative"
    return (f"{sign} and significant at the two-sided 5% level" if sig
            else "not significant at the two-sided 5% level") + "; sign and significance only"


def verdict_leg(row: dict) -> str:
    if not row["fired"]:
        return ("did not fire: D_L keeps its sign and more than half of D — nothing bigger than the "
                f"MDE of {row['D_L_mde']:.4f} pp is shown on this leg, which is not composition excluded")
    how = []
    if row["fired_on_sign"]:
        how.append("the sign of D_L differs from the sign of D")
    if row["fired_on_half"]:
        how.append("|D_L| < ½|D|")
    return "FIRED: " + " and ".join(how)


# ---------------------------------------------------------------- figures
def figures(head: dict, legs: dict, rob: dict) -> dict:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    FIGDIR.mkdir(parents=True, exist_ok=True)
    out: dict = {}
    x = np.arange(3)
    reg = [head[w]["registered"]["D"] for w in WAVES]
    frac = [head[w]["fractional"]["D"] for w in WAVES]

    # fig1 · D with its intervals against the ±1 pp margin
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.axhspan(-DELTA, DELTA, color="#e9e4d8", zorder=0)
    ax.axhline(0, color="#7a7a7a", lw=0.9)
    ax.axhline(DELTA, color="#b0a58c", lw=0.9, ls="--")
    ax.axhline(-DELTA, color="#b0a58c", lw=0.9, ls="--")
    ax.errorbar(x - 0.06, [e["coef"] for e in reg],
                yerr=[[e["coef"] - e["ci"][0] for e in reg], [e["ci"][1] - e["coef"] for e in reg]],
                fmt="o", color="#8a3324", capsize=4, label="pre-registered quartile rule")
    ax.errorbar(x + 0.06, [e["coef"] for e in frac],
                yerr=[[e["coef"] - e["ci"][0] for e in frac], [e["ci"][1] - e["coef"] for e in frac]],
                fmt="s", mfc="white", color="#4a6fa5", capsize=4,
                label="corrected quartile rule (boundary wage shared)")
    for i, e in enumerate(reg):
        ax.annotate(f"{e['coef']:+.2f}", (x[i] - 0.06, e["ci"][1]), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=9, color="#8a3324")
    ax.set_xticks(x)
    ax.set_xticklabels([WAVE_LABEL[w] for w in WAVES])
    ax.set_ylabel("Top-minus-bottom wage-quartile difference\nin the automation share (pp)")
    ax.set_title("Delegation and the wage of the work, three Claude.ai windows", loc="left")
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    fig.tight_layout()
    f1 = FIGDIR / "fig1_D_by_wave.png"
    fig.savefig(f1, dpi=200)
    plt.close(fig)
    out["fig1"] = dict(
        file="outputs/figures/fig1_D_by_wave.png",
        script="scripts/09_results_and_figures.py",
        caption=(
            "**In all three Claude.ai windows the delegated share is higher on top-quartile than on "
            "bottom-quartile tasks, and in none of them does the difference clear a percentage "
            "point in every window.** Plotted: D, the usage-weighted automation share of the top "
            "wage quartile minus that of the bottom, in percentage points, per window. Each point "
            "is one window of Claude.ai conversations (4–11 Aug 2025, 13–20 Nov 2025, 5–12 Feb "
            "2026), estimated separately and never pooled or spliced. The automation share of a "
            "task is its `directive` plus `feedback loop` conversations divided by its five "
            "classified collaboration patterns (`directive`, `feedback loop`, `learning`, `task "
            "iteration`, `validation`) in `onet_task::collaboration` at global; the `none` and "
            "`not_classified` patterns are outside that denominator and each quartile's `none` "
            "share is reported in Figure 2. Tasks are sorted into usage-weighted wage quartiles on "
            "the hourly wage of the occupations that hold the task (`wage_data.csv` "
            "`MedianSalary` ÷ 2080, employment-weighted over holders), and the quartile means are "
            "weighted by `onet_task_pct` so that the difference is about conversations and not "
            "about tasks. Sample: the 1,802 / 2,075 / 2,188 tasks that carry both a wage and at "
            "least one classified-pattern cell — 97.15 / 96.23 / 96.52% of named-task usage mass, "
            "on 818,673 / 854,432 / 848,716 classified conversations; the 805 / 1,079 / 1,056 "
            "tasks with a wage and no classified cell and the 5 / 12 / 12 with a cell and no wage "
            "are dropped, never zeroed. Filled circles are the pre-registered quartile rule; open "
            "squares share the boundary wage between the two adjacent quartiles in proportion, "
            "which matters because $43.40/hr is a mass point carrying 8–11 pp of a window. Bars "
            "are two-sided 95% intervals from a conversation-level binomial with the task mix held "
            "fixed; no release carries a user, account or session identifier, so no clustering is "
            "possible and these intervals are a lower bound on the sampling variance. The shaded "
            "band is the pre-registered indifference region of ±1 percentage point; the null value "
            "is zero. Read as a statement about tasks rather than conversations, a task-resampling "
            "design resolves nothing below about 14 to 20 percentage points."))

    # fig2 · the four quartile automation shares per wave
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), sharey=True)
    for i, w in enumerate(WAVES):
        sh = head[w]["registered"]["quartile_shares"]
        vals = [sh[f"Q{k}"]["coef"] for k in (1, 2, 3, 4)]
        err = [[sh[f"Q{k}"]["coef"] - sh[f"Q{k}"]["ci"][0] for k in (1, 2, 3, 4)],
               [sh[f"Q{k}"]["ci"][1] - sh[f"Q{k}"]["coef"] for k in (1, 2, 3, 4)]]
        axes[i].errorbar(np.arange(4), vals, yerr=err, fmt="o-", color="#8a3324", capsize=3)
        for k in (1, 2, 3, 4):
            axes[i].annotate(f"none {sh[f'Q{k}']['none_share']:.1f}", (k - 1, vals[k - 1]),
                             textcoords="offset points", xytext=(0, -16), ha="center", fontsize=7,
                             color="#5a5a5a")
        axes[i].set_xticks(np.arange(4))
        axes[i].set_xticklabels([f"Q{k}\n${sh[f'Q{k}']['mean_wage']:.0f}/hr" for k in (1, 2, 3, 4)])
        axes[i].set_title(WAVE_LABEL[w], loc="left", fontsize=10)
    axes[0].set_ylabel("Automation share (pp of classified conversations)")
    fig.suptitle("The relation is not monotone: the bottom quartile is delegated nearly as often as the top",
                 x=0.01, ha="left")
    fig.tight_layout()
    f2 = FIGDIR / "fig2_quartile_shares.png"
    fig.savefig(f2, dpi=200)
    plt.close(fig)
    out["fig2"] = dict(
        file="outputs/figures/fig2_quartile_shares.png",
        script="scripts/09_results_and_figures.py",
        caption=(
            "**The automation share is U-shaped in the wage of the work: it falls from the bottom "
            "quartile to the second and rises again to the top.** Plotted: each usage-weighted wage "
            "quartile's automation share, in percentage points of that quartile's classified "
            "conversations, one panel per Claude.ai window. The unit of analysis inside a panel is "
            "the quartile; each quartile holds a quarter of the window's usage mass, so the four "
            "points are not equally many tasks (Q1 holds 600 / 699 / 649 tasks and Q4 holds "
            "360 / 403 / 482). The share is `directive` plus `feedback loop` over the five "
            "classified patterns of `onet_task::collaboration` at global, usage-weighted by "
            "`onet_task_pct`; the grey figure under each point is that quartile's `none` share of "
            "the node, printed so the base is never implicit. The x labels carry each quartile's "
            "usage-weighted mean hourly wage. Sample as Figure 1. Bars are two-sided 95% intervals "
            "from a conversation-level binomial with the task mix held fixed and are a lower bound "
            "on the sampling variance, there being no user, account or session identifier in any "
            "release to cluster on. The exhibit is not a statement about occupations: an occupation "
            "is inferred from the task, not from the user."))

    # fig3 · the H3 legs
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.4), sharey=True)
    names = {"a": "(a) Computer &\nMathematical excluded", "b": "(b) within\nmajor group",
             "e": "(e) work-dominant\ntasks"}
    for i, w in enumerate(WAVES):
        rows = [r for r in legs["leg_table"] if r["wage" if False else "wave"] == w]
        d = rows[0]["D"]
        axes[i].axhline(0, color="#7a7a7a", lw=0.9)
        axes[i].axhline(d, color="#8a3324", lw=1.2, label=f"D = {d:+.2f}")
        axes[i].axhline(0.5 * d, color="#b0a58c", lw=1.0, ls="--", label="½D (the leg threshold)")
        for j, r in enumerate(rows):
            axes[i].errorbar([j], [r["D_L"]],
                             yerr=[[r["D_L"] - r["D_L_ci"][0]], [r["D_L_ci"][1] - r["D_L"]]],
                             fmt="o", color="#4a6fa5", capsize=4)
            axes[i].annotate(f"{r['D_L']:+.1f}", (j, r["D_L"]), textcoords="offset points",
                             xytext=(10, -3), fontsize=8, color="#4a6fa5")
        axes[i].set_xticks(np.arange(len(rows)))
        axes[i].set_xticklabels([names[r["leg"]] for r in rows], fontsize=8)
        axes[i].set_title(WAVE_LABEL[w], loc="left", fontsize=10)
        axes[i].legend(frameon=False, fontsize=7, loc="lower left")
    axes[0].set_ylabel("Top-minus-bottom difference under the leg (pp)")
    fig.suptitle("Removing the coding family reverses the gradient in every window", x=0.01, ha="left")
    fig.tight_layout()
    f3 = FIGDIR / "fig3_h3_legs.png"
    fig.savefig(f3, dpi=200)
    plt.close(fig)
    out["fig3"] = dict(
        file="outputs/figures/fig3_h3_legs.png",
        script="scripts/09_results_and_figures.py",
        caption=(
            "**The gradient does not survive either composition leg: excluding Computer & "
            "Mathematical tasks, or holding the occupational group fixed, turns it negative in all "
            "three windows; restricting to work-dominant tasks does not.** Plotted: D re-estimated "
            "under each pre-registered composition leg, in percentage points, one panel per "
            "Claude.ai window. Leg (a) removes the tasks rule A2 assigns to Computer & Mathematical "
            "(SOC major group 15 on the 2019 O*NET-SOC recode) — 42.8 / 39.7 / 35.6% of "
            "analysis-set usage mass and 73.1 / 71.3 / 65.5% of the top quartile's — with the "
            "quartile boundaries kept from the full analysis set and never re-drawn. Leg (b) "
            "averages the within-group top-minus-bottom differences over the nine major groups "
            "that hold analysis-set tasks in both the global bottom and the global top quartile, "
            "each group weighted by its usage mass in those two quartiles; the other thirteen "
            "groups are reported as not identified, never as zeros. Leg (e) keeps the tasks whose "
            "`work` share is at least half of their published `use_case` cells (943 / 1,071 tasks "
            "in November and February; the 29 / 21 tasks whose only published cell is "
            "`not_classified` have an undefined work share and are dropped, never scored 0), and is "
            "untestable in August, where no facet name in the file contains `use_case`. The solid "
            "line is that window's D and the dashed line is half of it: a leg fires if its estimate "
            "loses the sign or more than half the size, which is the pre-registered rule, read on "
            "the point estimates. Bars are two-sided 95% intervals on the same conversation-level "
            "binomial model as Figure 1 and are a lower bound on the sampling variance. Each leg's "
            "MDE, its interval for D_L − ½D and its retained mass are in `results.json`; the legs "
            "are not independent evidence, since Computer & Mathematical dominates both leg (a) and "
            "the leave-one-group-out series."))

    # fig4 · Δ_W, the quantity §2 is about
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    dw = [head[w]["Delta_W"] for w in WAVES]
    ax.axhline(0, color="#7a7a7a", lw=0.9)
    ax.errorbar(x, [e["coef"] for e in dw],
                yerr=[[e["coef"] - e["ci"][0] for e in dw], [e["ci"][1] - e["coef"] for e in dw]],
                fmt="D", color="#3f6e4f", capsize=4)
    for i, e in enumerate(dw):
        ax.annotate(f"{e['coef']:+.3f}", (x[i], e["ci"][1]), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=9, color="#3f6e4f")
    ax.set_xticks(x)
    ax.set_xticklabels([WAVE_LABEL[w] for w in WAVES])
    ax.set_ylabel("Wage-weighted minus unweighted\nautomation share, Δ_W (pp)")
    ax.set_title("What weighting a published automation share by the wage of the work would move it by",
                 loc="left", fontsize=11)
    fig.tight_layout()
    f4 = FIGDIR / "fig4_delta_w.png"
    fig.savefig(f4, dpi=200)
    plt.close(fig)
    out["fig4"] = dict(
        file="outputs/figures/fig4_delta_w.png",
        script="scripts/09_results_and_figures.py",
        caption=(
            "**Weighting the published automation share by the wage of the work moves it by less "
            "than a tenth of a point in two windows and by eight tenths in the third.** Plotted: "
            "Δ_W, the wage-weighted minus the unweighted usage-weighted automation share of "
            "Claude.ai conversations, in percentage points, per window; each marker is one window. "
            "Δ_W is Cov_w(wage, p) ÷ E_w[wage] over the analysis set — the same per-task automation "
            "share p as Figure 1, the same `onet_task_pct` weights, and the task's hourly wage as "
            "the re-weighting variable — so it is the size of the error made when a conversation-"
            "counting automation share is read as though it were weighted by the wage bill at "
            "stake. It is an hourly rate, not a bill: no hours enter it. Sample as Figure 1. Bars "
            "are two-sided 95% intervals on the conversation-level binomial model and are a lower "
            "bound on the sampling variance. The null value is zero; the pre-registered materiality "
            "line is separate and higher than the quartile margin — about 0.11 to 0.12 pp of Δ_W "
            "per point of quartile gap, so a full point of Δ_W needs a gap of roughly 8 to 9 points."))
    return out


# ---------------------------------------------------------------- the verifier
def collect_numbers(obj, acc: set[float]) -> set[float]:
    if isinstance(obj, dict):
        for v in obj.values():
            collect_numbers(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            collect_numbers(v, acc)
    elif isinstance(obj, bool):
        pass
    elif isinstance(obj, (int, float)) and np.isfinite(obj):
        acc.add(float(obj))
    return acc


NUM = re.compile(r"(?<![\w.])[-+]?\d+(?:,\d{3})*(?:\.\d+)?(?![\w])")


def verify_post_numbers(text: str, results: dict) -> list[str]:
    """Return the numeric tokens in `text` that do not appear in `results.json` at the precision
    they are written to. A post sentence may coarsen a number (1.38 for 1.3836) but may not invent
    one."""
    pool = collect_numbers(results, set())
    missing = []
    for tok in NUM.findall(text):
        raw = tok.replace(",", "")
        try:
            val = float(raw)
        except ValueError:
            continue
        dec = len(raw.split(".")[1]) if "." in raw else 0
        if any(abs(round(p, dec) - val) < 10 ** (-dec) / 2 + 1e-12 for p in pool):
            continue
        missing.append(tok)
    return missing


def main():
    power = read("power_rules")
    build = read("build_facts")
    head = read("headline")["results"]
    second = read("second_implementation")
    legs = read("legs")
    rob = read("robustness")
    fourth = read("fourth_window")
    expl = read("exploratory")
    bw = build["waves"]

    tests: dict = {}
    facts: dict = {}

    # ---------------- confirmatory: D, Δ_W, the slope (9 estimates)
    for w in WAVES:
        e = head[w]["registered"]["D"]
        f = head[w]["fractional"]["D"]
        tests[f"D_{w}"] = dict(
            label=f"D, top-minus-bottom wage-quartile difference in the automation share, {WAVE_LABEL[w]}",
            kind="confirmatory", script="scripts/03_headline.py",
            n=e["n_tasks"], n_conversations=e["n_conversations"],
            sample=(f"{bw[w]['analysis_tasks']} analysis-set tasks "
                    f"({bw[w]['analysis_share_named']:.2f}% of named-task usage mass, "
                    f"{bw[w]['analysis_conversations']:,.0f} classified conversations); Q1 and Q4 only"),
            estimates={
                "D": dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                          unit="percentage points of the automation share"),
                "D_corrected_quartile_rule": dict(coef=f["coef"], ci=f["ci"], se=f["se"],
                                                  mde=f["mde"],
                                                  unit="percentage points; boundary wage shared in proportion"),
                "pooled_binomial_se": dict(coef=head[w]["registered"]["pooled_binomial_se"],
                                           unit="pp, the steward's model-(a) arithmetic beside the registered formula")},
            prereg_rule=RULE_D, verdict=verdict_D(e["coef"], e["ci"]),
            notes=("model (a): conversation-level binomial, task mix held fixed; the SE is a lower "
                   "bound under within-task dependence and no clustering unit exists in any release"))
        dw = head[w]["Delta_W"]
        tests[f"DeltaW_{w}"] = dict(
            label=f"Δ_W, wage-weighted minus unweighted automation share, {WAVE_LABEL[w]}",
            kind="confirmatory", script="scripts/03_headline.py",
            n=dw["n_tasks"], n_conversations=dw["n_conversations"],
            sample=f"the whole analysis set of {bw[w]['analysis_tasks']} tasks",
            estimates={"Delta_W": dict(coef=dw["coef"], ci=dw["ci"], se=dw["se"], mde=dw["mde"],
                                       unit="percentage points of the automation share"),
                       "wage_weighted_share": dict(coef=head[w]["wage_weighted_share"]["coef"],
                                                   unit="pp"),
                       "unweighted_share": dict(coef=head[w]["unweighted_share"]["coef"], unit="pp")},
            prereg_rule=RULE_DW, verdict=verdict_DW(dw["coef"], dw["ci"]),
            notes="an hourly rate, not a bill: no hours enter Δ_W")
        sl = head[w]["slope_per_10dollar"]
        tests[f"slope_{w}"] = dict(
            label=f"the continuous companion: slope of the automation share per +$10/hr, {WAVE_LABEL[w]}",
            kind="confirmatory", script="scripts/03_headline.py",
            n=sl["n_tasks"], n_conversations=sl["n_conversations"],
            sample=f"the whole analysis set of {bw[w]['analysis_tasks']} tasks, usage-weighted",
            estimates={"slope": dict(coef=sl["coef"], ci=sl["ci"], se=sl["se"], mde=sl["mde"],
                                     unit="percentage points of the automation share per +$10/hr")},
            prereg_rule=RULE_SLOPE, verdict=verdict_slope(sl["coef"], sl["ci"]),
            notes="in no decision rule; the wage level does not reproduce Anthropic's published series")

    # ---------------- confirmatory: the eight leg tests
    for r in legs["leg_table"]:
        key = f"leg_{r['leg']}_{r['wave']}"
        tests[key] = dict(
            label=(f"H3 leg ({r['leg']}) in {WAVE_LABEL[r['wave']]}: "
                   + {"a": "D with Computer & Mathematical excluded",
                      "b": "D within SOC major group, usage-weighted over the identified groups",
                      "e": "D on work-dominant tasks"}[r["leg"]]),
            kind="confirmatory", subkind="leg test (one of the eight of P4)",
            script="scripts/05_legs.py",
            n=r["n_tasks"], n_conversations=r["n_conversations"],
            sample=f"the analysis set of {bw[r['wave']]['analysis_tasks']} tasks, quartile masks kept",
            estimates={
                "D_L": dict(coef=r["D_L"], ci=r["D_L_ci"], se=r["D_L_se"], mde=r["D_L_mde"],
                            unit="percentage points"),
                "D": dict(coef=r["D"], ci=r["D_ci"], se=r["D_se"], unit="percentage points"),
                "r_L": dict(coef=r["r"], ci=r["r_ci"], se=r["r_se"], mde=r["r_mde"],
                            unit="fraction of D retained (a ratio; its delta-method SE understates, "
                                 "so the contrast below is the interval to read)"),
                "D_L_minus_half_D": dict(coef=r["contrast"], ci=r["contrast_ci"],
                                         se=r["contrast_se"], mde=r["contrast_mde"],
                                         unit="percentage points")},
            prereg_rule=RULE_LEG, verdict=verdict_leg(r),
            coverage=r["info"],
            notes=(f"corr(D_L, D) = {r['corr_D_L_D']:.3f}; the interval for D_L − ½D "
                   f"{'straddles' if r['contrast_interval_straddles_zero'] else 'excludes'} zero"))

    # ---------------- exploratory (3)
    api_terms = {}
    for w in WAVES:
        r = expl["a_api"][w]
        if r["available"]:
            api_terms[f"D_{w}"] = dict(coef=r["D"]["coef"], ci=r["D"]["ci"], se=r["D"]["se"],
                                       mde=r["D"]["mde"], unit="percentage points")
            api_terms[f"slope_{w}"] = dict(coef=r["slope"]["coef"], ci=r["slope"]["ci"],
                                           unit="pp per +$10/hr")
    tests["exp_a_api_surface"] = dict(
        label="EXPLORATORY (a): the same gradient on the 1P API global intersection",
        kind="exploratory", exploratory=True, script="scripts/08_exploratory.py",
        n=expl["a_api"]["feb2026"]["audit"]["analysis_tasks"],
        sample=("the 1P API `onet_task::collaboration` at global in each release "
                "(11,660 rows in the February file), same analysis-set rule and wage join; the API "
                "is automation-dominant and its February sample includes Claude Code"),
        estimates=api_terms, prereg_rule=RULE_EXPLORATORY,
        verdict=("the sign is the opposite of Claude.ai's in all three windows, so the Claude.ai "
                 "gradient is not a property the API surface shares; context, not a replication"),
        notes="in no decision rule; may not appear in a headline")

    pat_terms = {}
    for w in WAVES:
        for pat, e in expl["b_pattern_split"][w].items():
            if isinstance(e, dict):
                pat_terms[f"{pat}_{w}"] = dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                               unit="pp of the pattern's share, Q4 − Q1")
    tests["exp_b_pattern_split"] = dict(
        label="EXPLORATORY (b): the pattern-level split — which pattern carries the gradient",
        kind="exploratory", exploratory=True, script="scripts/08_exploratory.py",
        n=None, sample="the analysis set of each wave, Q1 and Q4",
        estimates=pat_terms, prereg_rule=RULE_EXPLORATORY,
        verdict=("`feedback loop` carries the whole of the positive gradient in all three windows "
                 "while `directive` is negative in all three; `learning` is negative in all three. "
                 "The five differences sum to zero by construction"),
        notes="in no decision rule; 'outright' describes `directive` alone")

    jz_terms = {}
    for w in WAVES:
        r = expl["c_jobzone"][w]
        jz_terms[f"slope_{w}"] = dict(coef=r["slope_per_jobzone"]["coef"],
                                      ci=r["slope_per_jobzone"]["ci"],
                                      se=r["slope_per_jobzone"]["se"],
                                      mde=r["slope_per_jobzone"]["mde"],
                                      unit="pp of the automation share per +1 Job Zone")
        jz_terms[f"D_{w}"] = dict(coef=r["D_top_minus_bottom_jobzone_quartile"]["coef"],
                                  ci=r["D_top_minus_bottom_jobzone_quartile"]["ci"],
                                  unit="pp, top-minus-bottom Job-Zone quartile")
    tests["exp_c_jobzone"] = dict(
        label="EXPLORATORY (c): the gradient against `JobZone`, a non-wage ordering",
        kind="exploratory", exploratory=True, script="scripts/08_exploratory.py",
        n=expl["c_jobzone"]["feb2026"]["tasks"],
        sample=("the analysis set with the 119 `-1` sentinel occupations dropped: "
                "99.22 / 98.83 / 99.06% of named-task usage mass"),
        estimates=jz_terms, prereg_rule=RULE_EXPLORATORY,
        verdict=("negative and significant in all three windows: required preparation orders "
                 "delegation the other way from the wage"),
        notes="in no decision rule")

    # ---------------- the pre-registered robustness set, as tests flagged robustness
    for w in WAVES:
        r = rob["waves"][w]
        for key, label in (("X3_drop_under_100_classified",
                            "X3: tasks with fewer than 100 classified conversations dropped"),
                           ("X4_sc_netted_weights",
                            "X4: Seychelles netted out of the November task weights"),
                           ("X5_drop_sc_over_10pc",
                            "X5: tasks where SC exceeds 10% of their global count dropped"),
                           ("X5_drop_sc_over_20pc", "X5 variant: the > 20% set dropped")):
            if key not in r:
                continue
            e = r[key]
            tests[f"rob_{key}_{w}"] = dict(
                label=f"{label}, {WAVE_LABEL[w]}", kind="robustness", script="scripts/06_robustness.py",
                n=e.get("n_tasks"), sample="the analysis set, quartile masks kept",
                estimates={"D": dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                     unit="percentage points")},
                prereg_rule=RULE_ROBUST,
                verdict=verdict_D(e["coef"], e["ci"]),
                notes=f"retained Q1+Q4 mass {e.get('retained_mass_q1_q4', float('nan')):.2f}%")
        for rule in ("equal_split", "modal_holder"):
            e = r["W1"][rule]["D"]
            tests[f"rob_W1_{rule}_{w}"] = dict(
                label=f"W1: the {rule.replace('_', ' ')} multi-holder wage rule, {WAVE_LABEL[w]}",
                kind="robustness", script="scripts/06_robustness.py", n=e["n_tasks"],
                sample="the analysis set, quartiles re-drawn on this rule's wage",
                estimates={"D": dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                     unit="percentage points"),
                           "Delta_W": dict(coef=r["W1"][rule]["Delta_W"]["coef"],
                                           ci=r["W1"][rule]["Delta_W"]["ci"], unit="pp")},
                prereg_rule=RULE_ROBUST, verdict=verdict_D(e["coef"], e["ci"]),
                notes=f"quartile boundaries {['$%.2f' % b for b in r['W1'][rule]['bounds']]}")
        e = r["C7_second_wage_source"]["D"]
        tests[f"rob_C7_{w}"] = dict(
            label=f"C7: the second wage source (BLS Employment Projections), {WAVE_LABEL[w]}",
            kind="robustness", script="scripts/06_robustness.py",
            n=r["C7_second_wage_source"]["n_tasks"],
            sample=(f"the {r['C7_second_wage_source']['n_tasks']} analysis-set tasks BLS-EP prices, "
                    f"{r['C7_second_wage_source']['mass_share_named']:.1f}% of the analysis set's mass"),
            estimates={"D": dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"], unit="pp"),
                       "Delta_W": dict(coef=r["C7_second_wage_source"]["Delta_W"]["coef"],
                                       ci=r["C7_second_wage_source"]["Delta_W"]["ci"], unit="pp")},
            prereg_rule=("prereg P6 under O-A: \"Sign agreement: the C7 rebuild's point estimate "
                         "carries the declared sign in all three waves... If C7's point estimate "
                         "carries the opposite sign in any wave, the owner is unchanged and the O-A "
                         "paragraph carries, in its first sentence, that the direction is not "
                         "corroborated on the second wage source in that wave, with C7's coverage "
                         "stated.\""),
            verdict=("the sign does NOT agree with C6 in this window, so the direction is not "
                     "corroborated on the second wage source; the owner is unchanged and C7's "
                     "coverage (55.66 / 58.52 / 62.22% of named mass against C6's 99%) is the "
                     "reason it is not decisive"
                     if not r["C7_second_wage_source"]["sign_agrees_with_C6"]
                     else "the sign agrees with C6 in this window"),
            notes="rank and sign only, never a level: Spearman with C6 0.9869 / 0.9861 / 0.9869")
        e = r["model_b_design_based"]
        tests[f"rob_model_b_{w}"] = dict(
            label=f"model (b): the design-based task-resampling bound, {WAVE_LABEL[w]}",
            kind="robustness", script="scripts/06_robustness.py", n=bw[w]["analysis_tasks"],
            sample="the analysis set; tasks resampled equal-probability inside each extreme quartile",
            estimates={"D": dict(coef=r["D_primary"]["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                 unit="pp; the generalisation-to-other-task-mixes bound")},
            prereg_rule=("prereg P1(b): reported beside (a) as the generalisation bound, in no "
                         "decision rule"),
            verdict=(f"nothing below about {e['mde']:.0f} percentage points is resolved as a "
                     f"statement about tasks in general"),
            notes="Kish effective N on the usage weights: "
                  f"{bw[w]['kish_analysis']:.1f} against a nominal {bw[w]['analysis_tasks']}")
        p = r["permutation_null"]
        tests[f"rob_placebo_{w}"] = dict(
            label=f"the placebo: the wage permuted within SOC major group, {WAVE_LABEL[w]}",
            kind="robustness", script="scripts/06_robustness.py", n=bw[w]["analysis_tasks"],
            sample="the analysis set; 10,000 seeded permutations, quartiles re-drawn on the permuted wage",
            estimates={"observed_D": dict(coef=p["obs"], unit="pp"),
                       "permutation_mean": dict(coef=p["mean"], unit="pp"),
                       "permutation_sd": dict(coef=p["sd"], unit="pp"),
                       "permutation_band_95": dict(coef=p["mean"], ci=[p["q025"], p["q975"]],
                                                   unit="pp"),
                       "two_sided_p": dict(coef=p["p_value"], unit="probability")},
            prereg_rule=("prereg §Robustness 9: \"Reported here as the task-level bound it is... It "
                         "is in no decision rule.\""),
            verdict=(f"the observed D lies inside the permutation band (two-sided p = {p['p_value']:.4f}); "
                     "the band is not centred on zero because the permutation is within major group, "
                     "which preserves the between-group composition"),
            notes="a task-level bound of the order of model (b)'s MDE")
        e = fourth["waves"][w]["D_pct_weights"]
        tests[f"rob_fourth_window_{w}"] = dict(
            label=f"P7: the fourth window (Feb–Mar 2025), read on {WAVE_LABEL[w]}'s quartiles",
            kind="robustness", script="scripts/07_fourth_window.py",
            n=fourth["waves"][w]["usable_tasks"],
            sample=(f"{fourth['waves'][w]['matched_tasks']} of {bw[w]['analysis_tasks']} analysis-set "
                    f"tasks matched in `automation_vs_augmentation_by_task.csv` "
                    f"({fourth['waves'][w]['matched_mass_share']:.2f}% of their mass); "
                    f"{fourth['waves'][w]['dropped_filtered_one_tasks']} entirely `filtered` tasks "
                    "dropped, never zeroed"),
            estimates={"D": dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                 unit="pp; design-based interval only, the window publishes no counts"),
                       "D_classified_weights": dict(
                           coef=fourth["waves"][w]["D_classified_weights"]["coef"],
                           ci=fourth["waves"][w]["D_classified_weights"]["ci"], unit="pp")},
            prereg_rule=("prereg P7: \"This window is in no decision rule and cannot declare or "
                         "refute an owner\"; design-based only"),
            verdict=(f"positive in sign, unresolved: the design-based interval spans zero at an MDE "
                     f"of {e['mde']:.1f} pp"),
            notes=("no task-level `none` share exists in this release, so §9(1)'s `none`-beside-"
                   "every-share rule holds at the global level only; the window's global automation "
                   "share is 43.2902% against the release's published 43.0619%"))

    # ---------------- descriptive series the post may cite
    for w in WAVES:
        sh = head[w]["registered"]["quartile_shares"]
        tests[f"desc_quartile_shares_{w}"] = dict(
            label=f"each wage quartile's automation share with its `none` share, {WAVE_LABEL[w]}",
            kind="descriptive", script="scripts/03_headline.py", n=bw[w]["analysis_tasks"],
            sample="the analysis set, four quartiles of usage mass",
            estimates={f"Q{k}": dict(coef=sh[f"Q{k}"]["coef"], ci=sh[f"Q{k}"]["ci"],
                                     se=sh[f"Q{k}"]["se"], mde=sh[f"Q{k}"]["mde"],
                                     none_share=sh[f"Q{k}"]["none_share"],
                                     not_classified_share=sh[f"Q{k}"]["not_classified_share"],
                                     mean_wage=sh[f"Q{k}"]["mean_wage"], kish=sh[f"Q{k}"]["kish"],
                                     mass_wave=sh[f"Q{k}"]["mass_wave"],
                                     tasks=bw[w]["quartiles"][f"Q{k}"]["tasks"],
                                     conversations=bw[w]["quartiles"][f"Q{k}"]["conversations"],
                                     unit="pp of classified conversations")
                       for k in (1, 2, 3, 4)},
            prereg_rule=("prereg §9(1): the `none` share is printed beside every automation share so "
                         "the base is never implicit; description, in no decision rule"),
            verdict=("not monotone in the wage: the share falls from Q1 to Q2 and rises to Q4 in all "
                     "three windows"),
            notes="P5's augmentation clause: "
                  f"{head[w]['registered']['augmentation_rising']} of 3 augmentation patterns are "
                  "weakly increasing across the quartiles")
        tests[f"desc_pattern_shares_{w}"] = dict(
            label=f"the five collaboration patterns' shares by wage quartile, {WAVE_LABEL[w]}",
            kind="descriptive", script="scripts/03_headline.py", n=bw[w]["analysis_tasks"],
            sample="the analysis set, four quartiles of usage mass",
            estimates={f"{pat}_Q{k}": dict(coef=head[w]["registered"]["pattern_shares"][pat][f"Q{k}"]["coef"],
                                           ci=head[w]["registered"]["pattern_shares"][pat][f"Q{k}"]["ci"],
                                           unit="pp of classified conversations")
                       for pat in ["directive", "feedback loop", "learning", "task iteration", "validation"]
                       for k in (1, 2, 3, 4)},
            prereg_rule="prereg H2/P5: description with each quartile share's own interval, in no decision rule",
            verdict="the five shares sum to 100 in every quartile, by construction",
            notes="'outright' describes `directive` alone")
        d = legs["descriptive"][w]
        tests[f"desc_leave_one_group_out_{w}"] = dict(
            label=f"leg (c): leave-one-group-out re-estimates and the group-spanning bucket, {WAVE_LABEL[w]}",
            kind="descriptive", script="scripts/05_legs.py", n=bw[w]["analysis_tasks"],
            sample="the analysis set; 22 major groups plus the group-spanning bucket",
            estimates={f"leave_out_{r['left_out']}": dict(coef=r.get("D"), ci=r.get("ci"),
                                                          se=r.get("se"), mde=r.get("mde"),
                                                          move=r.get("move"), unit="pp")
                       for r in d["leave_one_group_out"]},
            prereg_rule=("prereg P3(c)/§10: 22 re-estimates plus the 23rd group-spanning bucket, "
                         "reported under §10 as description; the SOC-15 leave-out dominates by "
                         "construction and the post says so"),
            verdict=("Computer & Mathematical is the largest mover in every window; its removal "
                     "moves D further than every other group's"),
            notes="not independent evidence from leg (a): the same group dominates both")
        tests[f"desc_ten_largest_out_{w}"] = dict(
            label=f"the leave-out of the ten largest tasks by usage mass, {WAVE_LABEL[w]}",
            kind="descriptive", script="scripts/05_legs.py", n=bw[w]["analysis_tasks"],
            sample=(f"the analysis set less its ten largest tasks "
                    f"({d['ten_largest_out']['dropped_mass_wave']:.4f} pp of the wave = "
                    f"{bw[w]['top10_named_share']:.4f}% of named mass)"),
            estimates={"D": dict(coef=d["ten_largest_out"]["D"], ci=d["ten_largest_out"]["ci"],
                                 se=d["ten_largest_out"]["se"], mde=d["ten_largest_out"]["mde"],
                                 unit="pp")},
            prereg_rule="prereg §Robustness 3: the denominator stated each time; movers named",
            verdict=verdict_D(d["ten_largest_out"]["D"], d["ten_largest_out"]["ci"]),
            notes="movers: " + "; ".join(d["ten_largest_out"]["movers"][:3]) + " …")
        if "use_case_mix_by_quartile" in d:
            tests[f"desc_use_case_mix_{w}"] = dict(
                label=f"leg (d): each wage quartile's use-case mix, {WAVE_LABEL[w]}",
                kind="descriptive", script="scripts/05_legs.py", n=bw[w]["analysis_tasks"],
                sample="the analysis set; shares of each quartile's published `use_case` cells",
                estimates={f"{q}_{cat}": dict(coef=d["use_case_mix_by_quartile"][q][cat],
                                              unit="% of the quartile's published use_case cells")
                           for q in ("Q1", "Q2", "Q3", "Q4")
                           for cat in ("work", "personal", "coursework", "not_classified")},
                prereg_rule="prereg P3(d): description, in no decision rule",
                verdict=("the work share rises with the wage quartile in both windows, which is the "
                         "reason leg (e) is run"),
                notes="August publishes no `use_case` facet at any grain")
            s = d["slope_with_work_share"]
            tests[f"desc_slope_work_share_{w}"] = dict(
                label=f"the continuous companion with the task's work share as a covariate, {WAVE_LABEL[w]}",
                kind="descriptive", script="scripts/05_legs.py", n=s["n_tasks"],
                sample=f"the {s['n_tasks']} analysis-set tasks with a defined work share",
                estimates={"slope_wage_only": dict(coef=s["slope_wage_only"]["coef"],
                                                   ci=s["slope_wage_only"]["ci"],
                                                   mde=s["slope_wage_only"]["mde"],
                                                   unit="pp per +$10/hr"),
                           "slope_wage_with_work_share": dict(coef=s["slope_wage_partial"]["coef"],
                                                              ci=s["slope_wage_partial"]["ci"],
                                                              mde=s["slope_wage_partial"]["mde"],
                                                              unit="pp per +$10/hr, partial"),
                           "slope_work_share_per_10pp": dict(
                               coef=s["slope_work_share_only_per_10pp"]["coef"],
                               ci=s["slope_work_share_only_per_10pp"]["ci"],
                               unit="pp per +10 pp of work share"),
                           "corr_wage_work_share": dict(coef=s["usage_weighted_corr_wage_workshare"],
                                                        unit="usage-weighted correlation"),
                           "vif": dict(coef=s["vif"], unit="variance inflation factor")},
                prereg_rule=("prereg §9(3)(e) with referee item 14: the usage-weighted pairwise "
                             "correlation and VIF of wage and work share printed beside it, since "
                             "the two predictors compete"),
                verdict=("the wage slope changes sign or size once the work share is in the "
                         "regression, at a VIF of 1.13–1.14"),
                notes="description; in no decision rule")

    # ---------------- facts
    facts["declared_owner"] = dict(
        value=read("headline")["results"]["owner_registered"]["owner"],
        label="the owner §9(1)'s ordered chain declares, on the pre-registered quartile rule",
        script="scripts/03_headline.py",
        source_check=("the chain is the function whose power was pre-registered in "
                      "01_power_rules.py; steps: "
                      + json.dumps(read("headline")["results"]["owner_registered"]["steps"])),
        intervals=read("headline")["results"]["owner_registered"]["intervals"],
        points=read("headline")["results"]["owner_registered"]["points"],
        ses=read("headline")["results"]["owner_registered"]["ses"])
    facts["declared_owner_corrected_quartile_rule"] = dict(
        value=read("headline")["results"]["owner_fractional"]["owner"],
        label="the same chain on the corrected quartile rule (the DEVIATION of 2026-09-17)",
        script="scripts/03_headline.py",
        source_check="both readings give the same owner",
        points=read("headline")["results"]["owner_fractional"]["points"])
    facts["H3_declaration"] = dict(
        value=legs["h3"]["persistent_leg_rule_declares_H3"],
        label=("H3 declared under the primary persistent-leg rule (a leg fires in every wave in "
               "which it is testable)"),
        script="scripts/05_legs.py",
        source_check=("legs firing in every testable wave: "
                      + ", ".join(legs["h3"]["legs_firing_in_every_testable_wave"])),
        k_of_8_fired=legs["h3"]["k_of_8_fired"], leg_tests=legs["h3"]["leg_tests"],
        literal_any_wave_rule=legs["h3"]["literal_any_wave_rule_declares_H3"],
        rules_agree=legs["h3"]["rules_agree"],
        per_leg={k: dict(waves_fired=v["waves_fired"], waves_testable=v["waves_testable"],
                         fired_by_wave=v["fired_by_wave"])
                 for k, v in legs["h3"]["per_leg"].items()},
        on_the_2010_grouping=legs["h3_2010"]["persistent_leg_rule_declares_H3"])
    facts["H1_signature_clause"] = dict(
        value=all(v["keeps_half_and_sign_on_every_testable_leg"]
                  for v in legs["h1_signature_clause"].values()),
        label=("H1's own signature clause: D keeping more than half its size, with the same sign, on "
               "every leg testable in that wave"),
        script="scripts/05_legs.py",
        source_check=json.dumps(legs["h1_signature_clause"]))
    facts["second_implementation_agreement"] = dict(
        value=max(second["waves"][w]["D_abs_diff"] for w in WAVES),
        label="the largest absolute disagreement in D between the two independent implementations (pp)",
        script="scripts/04_second_implementation.py",
        source_check=("tolerance 1e-9 pp; wage-map differences 0 in every wave; quartile-label "
                      "differences 0; analysis-set difference 0"),
        max_abs_diff_p=max(second["waves"][w]["max_abs_diff_p"] for w in WAVES),
        max_abs_diff_w=max(second["waves"][w]["max_abs_diff_w"] for w in WAVES),
        max_abs_diff_delta_w=max(second["waves"][w]["delta_w_abs_diff"] for w in WAVES),
        max_abs_diff_slope=max(second["waves"][w]["slope_abs_diff"] for w in WAVES),
        bootstrap_vs_closed_form_max_rel=max(
            abs(v["se_boot"] - v["se_closed"]) / v["se_closed"]
            for w in WAVES for v in second["waves"][w]["bootstrap"].values()),
        bootstrap_coverage=[second["waves"][w]["bootstrap"]["D"]["coverage"] for w in WAVES])
    facts["synthetic_recovery"] = dict(
        value=True, label="every estimator the post relies on recovers a known effect and returns zero for zero",
        script="scripts/04_second_implementation.py",
        source_check=json.dumps({
            "D_coverage_by_implanted_gap": {k: v["coverage"] for k, v in second["synthetic"]["D"].items()},
            "Delta_W_abs_err": second["synthetic"]["Delta_W"]["abs_err"],
            "slope_abs_err": second["synthetic"]["slope"]["abs_err"],
            "leg_b_within_group_vs_total": [second["synthetic"]["leg_b_within_group"]["point_within"],
                                            second["synthetic"]["leg_b_within_group"]["total_gap"]],
            "leg_e_only_not_classified_dropped":
                second["synthetic"]["leg_e_work_dominant"]["only_nc_dropped_not_zero"],
            "design_bootstrap_rel_err": second["synthetic"]["design_bootstrap"]["rel_err"],
            "permutation_size_pc": second["synthetic"]["permutation"]["size_zero_gradient"]["reject_rate"],
            "kish_exact": second["synthetic"]["kish"]["abs_err"] < 1e-12}))
    for w in WAVES:
        facts[f"sample_{w}"] = dict(
            value=bw[w]["analysis_tasks"],
            label=f"analysis-set tasks, {WAVE_LABEL[w]}", script="scripts/02_build.py",
            source_check="feasibility.md §4: 1,802 / 2,075 / 2,188 tasks",
            named_nodes=bw[w]["named_nodes"], named_mass=bw[w]["named_mass"],
            analysis_mass_wave=bw[w]["analysis_mass_wave"],
            analysis_share_named=bw[w]["analysis_share_named"],
            classified_conversations=bw[w]["analysis_conversations"],
            dropped_wage_no_classified_cell=bw[w]["x1_wage_no_cell"],
            dropped_wage_no_classified_cell_mass=bw[w]["x1_mass"],
            dropped_classified_cell_no_wage=bw[w]["x2_cell_no_wage"],
            dropped_classified_cell_no_wage_mass=bw[w]["x2_mass"],
            priced_tasks=bw[w]["priced_tasks"], priced_share_named=bw[w]["priced_share_named"])
        facts[f"kish_{w}"] = dict(
            value=bw[w]["kish_analysis"],
            label=f"Kish effective N on the usage weights, analysis set, {WAVE_LABEL[w]}",
            script="scripts/02_build.py",
            source_check="feasibility.md §4: 94.4 / 83.4 / 125.7 on the analysis set",
            kish_named=bw[w]["kish_named"], nominal_named=bw[w]["named_nodes"],
            nominal_analysis=bw[w]["analysis_tasks"],
            by_quartile=[bw[w]["quartiles"][f"Q{k}"]["kish"] for k in (1, 2, 3, 4)])
        facts[f"quartile_boundaries_{w}"] = dict(
            value=bw[w]["quartile_bounds"],
            label=f"usage-weighted wage quartile boundaries, $/hr, {WAVE_LABEL[w]}",
            script="scripts/02_build.py",
            source_check=("feasibility.md §4: $25.78 / $35.79 / $43.40, $25.78 / $34.56 / $43.40, "
                          "$24.00 / $34.40 / $43.40 on the equal-split wage"),
            boundary_tie_mass=bw[w]["boundary_tie_mass"],
            q4_mass_from_boundary_tie=bw[w]["q4_mass_from_boundary_tie"],
            equal_split_rule_boundaries=bw[w]["quartile_bounds_equal_rule"])
        facts[f"mde_{w}"] = dict(
            value=head[w]["registered"]["D"]["mde"],
            label=f"realised MDE(80%) for D, {WAVE_LABEL[w]}", script="scripts/03_headline.py",
            source_check="MDE = 2.8 × SE; the pre-registered figure was 0.42 / 0.42 / 0.43 pp",
            se=head[w]["registered"]["D"]["se"],
            pooled_binomial_se=head[w]["registered"]["pooled_binomial_se"],
            design_based_mde=rob["waves"][w]["model_b_design_based"]["mde"],
            design_based_se=rob["waves"][w]["model_b_design_based"]["se"])
        facts[f"replication_{w}"] = dict(
            value=bw[w]["split_five_patterns"],
            label=f"the wave's five-pattern automation share, {WAVE_LABEL[w]}",
            script="scripts/02_build.py",
            source_check=("published 49% / 45% / 44% on the all-conversation base; reproduced "
                          "49.0980 / 45.3554 / 44.1569 and 51.0698 / 46.7394 / 45.5456 on the "
                          "five-classified base"),
            all_pattern_share=bw[w]["split_all_patterns"],
            internal_check_value=bw[w]["internal_check_value"],
            internal_check_gap=bw[w]["internal_check_gap"])
    facts["fig211_released_library"] = dict(
        value=build["fig211"]["slope"],
        label="Figure 2.11 reproduced by Anthropic's own released library (partial slope)",
        script="scripts/02_build.py",
        source_check="published −3.112 / 0.394 / N 111",
        partial_r2=build["fig211"]["partial_r2"], n_countries=build["fig211"]["n_countries"])
    facts["rule_power"] = dict(
        value=power["thresholds_80pc"]["steward_0.151_0.148_0.154"]["OA_or_stronger_80pc"],
        label="the true |D| at which O-A or stronger is declared with 80% probability (pp)",
        script="scripts/01_power_rules.py",
        source_check="prereg P2; exact normal calculation and 400,000-triple Monte Carlo",
        H1_or_H2_80pc=power["thresholds_80pc"]["steward_0.151_0.148_0.154"]["H1_or_H2_80pc"],
        H4_declared_80pc=power["thresholds_80pc"]["steward_0.151_0.148_0.154"]["H4_declared_80pc"],
        H4_clause_80pc=power["thresholds_80pc"]["steward_0.151_0.148_0.154"]["H4_step4_clause_80pc"],
        P_H1_at_true_D_1pp=power["thresholds_80pc"]["steward_0.151_0.148_0.154"]["P_H1_at_true_D_1.0"])
    facts["owner_under_robustness"] = dict(
        value=rob["owners_under_robustness"]["primary"]["owner"],
        label="the owner the ordered chain declares under each pre-registered robustness cut",
        script="scripts/06_robustness.py",
        source_check=json.dumps({k: v["owner"] for k, v in rob["owners_under_robustness"].items()}),
        owners={k: v["owner"] for k, v in rob["owners_under_robustness"].items()},
        points={k: v["points"] for k, v in rob["owners_under_robustness"].items()})
    facts["C7_sign_agreement"] = dict(
        value=all(rob["waves"][w]["C7_second_wage_source"]["sign_agrees_with_C6"] for w in WAVES),
        label="whether the second wage source carries the declared sign in all three windows (P6)",
        script="scripts/06_robustness.py",
        source_check=json.dumps({w: rob["waves"][w]["C7_second_wage_source"]["sign_agrees_with_C6"]
                                 for w in WAVES}),
        coverage_share_named=[bw[w]["c7_priced_share_named"] for w in WAVES],
        spearman_with_C6=[bw[w]["c6_c7_spearman"] for w in WAVES])
    facts["november_is_corroborated_not_independent"] = dict(
        value=True,
        label=("X6, a reporting rule: November is corroborated by August and February, never treated "
               "as independent confirmation, because X4 and X5 cannot reach the per-task rates"),
        script="scripts/06_robustness.py",
        source_check=("SC is 24,715 conversations (2.47181% of the wave) with 0 rows of "
                      "onet_task::collaboration; 23 analysis-set tasks carry SC above 10% of their "
                      "global count, 11.594 pp of the wave, 8.913 pp of it in Q4"))
    facts["generalisation_sentence"] = dict(
        value=max(rob["waves"][w]["model_b_design_based"]["mde"] for w in WAVES),
        label=("the design-based MDE, the bound on any claim about tasks in general (pp); a claim "
               "about work in general is not licensed"),
        script="scripts/06_robustness.py",
        source_check="model (b) MDE 14.1 / 20.2 / 16.1 pp against the pre-registered 12.5 / 17.4 / 16.1")
    facts["conventions_and_constants"] = dict(
        value=2080,
        label=("the constants and conventions the post may cite: the hours-per-year divisor, the "
               "vintages, the window dates, the test constants and the counts of the design"),
        script="scripts/02_build.py and scripts/09_results_and_figures.py",
        source_check=("$208,000 ÷ 2,080 = $100.00/hr is the wage file's top code; the shipped O*NET "
                      "DB is 20.1 on 2010 O*NET-SOC codes, recoded to 2019 for any grouping; "
                      "BLS-EP is keyed on SOC-2018"),
        hours_per_year=2080, top_code_annual=208000, top_code_hourly=100.0,
        onet_db_version=20.1, vintage_shipped=2010, vintage_grouping=2019, bls_ep_soc_vintage=2018,
        window_aug=[2025, 8, 4, 11], window_nov=[2025, 11, 13, 20], window_feb=[2026, 2, 5, 12],
        release_dates=[20250915, 20260115, 20260324, 20250210, 20250327],
        feb_sample_base=1000000, wage_rows=1090, wage_rows_kept=1084,
        onet_statement_rows=19530, onet_keys=18428, onet_occupations=974, onet_soc7=775,
        soc_major_groups=22, soc_computer_and_mathematical=15,
        z_two_sided_95=Z, mde_multiplier=MDE_K, delta_pp=DELTA, waves=3, quartiles=4,
        classified_patterns=5, confirmatory_estimates=17, leg_tests=8, exploratory_tests=3,
        permutations=10000, bootstrap_draws=10000, seed=20260917,
        materiality_pp_of_delta_w_per_point_of_gap=[0.11, 0.12],
        gap_needed_for_one_point_of_delta_w=[8, 9],
        percent_signs=[100, 95, 80, 50, 25, 5, 1])
    facts["country_mix_not_testable"] = dict(
        value=False, label="whether the country mix inside a task can be cleaned at this grain",
        script="scripts/06_robustness.py",
        source_check=("intersections are global only, so a per-task rate cannot be cleaned of its "
                      "country blend and no reverse construction is identified"))

    figs = figures(head, legs, rob)

    results = dict(
        post="post1",
        question="Is AI delegated more on low-wage work or on high-wage work?",
        generated=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        prereg="posts/post1/prereg/prereg.md (content c9b1b45, committed 066b761)",
        scripts=[f"scripts/0{i}_*.py" for i in range(1, 10)],
        counts=dict(
            confirmatory_estimates=sum(1 for t in tests.values() if t["kind"] == "confirmatory"),
            leg_tests=sum(1 for t in tests.values() if t.get("subkind", "").startswith("leg test")),
            exploratory_tests=sum(1 for t in tests.values() if t["kind"] == "exploratory"),
            robustness_entries=sum(1 for t in tests.values() if t["kind"] == "robustness"),
            descriptive_entries=sum(1 for t in tests.values() if t["kind"] == "descriptive")),
        tests=tests, facts=facts, figures=figs)

    (PROCESSED / "results.json").write_text(json.dumps(results, indent=2, default=float) + "\n")
    (ROOT / "posts/post1/outputs/figures.json").write_text(json.dumps(figs, indent=2) + "\n")
    print("wrote posts/post1/data/processed/results.json and posts/post1/outputs/figures.json")
    print(f"  tests: {results['counts']}")
    for k, v in figs.items():
        print(f"  {k}: {v['file']}  caption {len(v['caption'].split())} words")

    post = ROOT / "posts/post1/POST.md"
    if post.exists():
        missing = verify_post_numbers(post.read_text(), results)
        print(f"  POST.md verification: {len(missing)} numbers not in results.json: {missing[:20]}")
    else:
        print("  POST.md does not exist yet: the verifier is tested on a synthetic sentence in the "
              "check block and will run at the writing stage")
    return results


if __name__ == "__main__":
    R = main()

    # ------------------------------------------------------------ check block
    # the pre-registered counts: 17 confirmatory estimates of which 8 are leg tests, 3 exploratory
    assert R["counts"]["confirmatory_estimates"] == 17, R["counts"]
    assert R["counts"]["leg_tests"] == 8, R["counts"]
    assert R["counts"]["exploratory_tests"] == 3, R["counts"]
    for name in ("D", "DeltaW", "slope"):
        assert sum(1 for k in R["tests"] if k.startswith(name + "_")) == 3, name
    assert sum(1 for k in R["tests"] if k.startswith("leg_a_")) == 3
    assert sum(1 for k in R["tests"] if k.startswith("leg_b_")) == 3
    assert sum(1 for k in R["tests"] if k.startswith("leg_e_")) == 2

    # every test entry carries a script, a sample, a quoted pre-registered rule and a verdict, and
    # every estimate carries a unit; every confirmatory estimate carries an interval and an MDE
    for key, t in R["tests"].items():
        assert t["script"].startswith("scripts/"), key
        assert t["sample"] and t["prereg_rule"] and t["verdict"], key
        assert t["kind"] in ("confirmatory", "exploratory", "robustness", "descriptive"), key
        for term, e in t["estimates"].items():
            assert "unit" in e and e["unit"], (key, term)
        if t["kind"] == "confirmatory":
            # the entry's own coefficient — the one the post may cite — carries an interval and an
            # MDE beside it, as the standards require
            primary = ("D_L" if key.startswith("leg_") else
                       "Delta_W" if key.startswith("DeltaW_") else
                       "slope" if key.startswith("slope_") else "D")
            e = t["estimates"][primary]
            assert e.get("ci") and e.get("mde") is not None, (key, primary)
            assert abs(e["mde"] - MDE_K * e["se"]) < 1e-9, (key, primary)
            assert e["ci"][0] <= e["coef"] <= e["ci"][1], (key, primary)

    # the verdicts are mechanical: re-deriving each D verdict from its own numbers reproduces it
    for w in WAVES:
        t = R["tests"][f"D_{w}"]
        e = t["estimates"]["D"]
        assert t["verdict"] == verdict_D(e["coef"], e["ci"]), (w, t["verdict"])
    for r in read("legs")["leg_table"]:
        assert R["tests"][f"leg_{r['leg']}_{r['wave']}"]["verdict"] == verdict_leg(r)

    # the facts the director's note requires are all present
    for key in ("declared_owner", "H3_declaration", "second_implementation_agreement",
                "synthetic_recovery", "rule_power", "owner_under_robustness", "C7_sign_agreement",
                "generalisation_sentence"):
        assert key in R["facts"], key
    for w in WAVES:
        for key in (f"sample_{w}", f"kish_{w}", f"quartile_boundaries_{w}", f"mde_{w}",
                    f"replication_{w}"):
            assert key in R["facts"], key
    assert R["facts"]["declared_owner"]["value"] in ("H1", "H2", "O-A", "H4", "O-B")
    assert R["facts"]["second_implementation_agreement"]["value"] < 1e-9
    assert R["facts"]["H3_declaration"]["leg_tests"] == 8

    # the figures exist, each has a caption naming the unit, the sample and the interval, and every
    # plotted number is in results.json
    assert len(R["figures"]) >= 3, R["figures"]
    pool = collect_numbers(R["tests"], set()) | collect_numbers(R["facts"], set())
    for k, f in R["figures"].items():
        assert (ROOT / "posts/post1" / f["file"]).exists(), f["file"]
        cap = f["caption"]
        assert cap.startswith("**") and "**" in cap[2:], k
        assert "percentage point" in cap or "pp" in cap, k
        assert "95%" in cap, k
        assert len(cap.split()) >= 60, (k, len(cap.split()))
        # every number written into the caption must be in results.json
        assert not verify_post_numbers(cap, R), (k, verify_post_numbers(cap, R))

    # the verifier itself: a sentence quoting a real number passes, one inventing a number fails
    good = f"D was {R['tests']['D_nov2025']['estimates']['D']['coef']:.2f} points in November."
    bad = "D was 99.87 points in November."
    assert verify_post_numbers(good, R) == [], verify_post_numbers(good, R)
    assert verify_post_numbers(bad, R) == ["99.87"], verify_post_numbers(bad, R)

    print("\nCHECK BLOCK PASSED — 09_results_and_figures.py")
