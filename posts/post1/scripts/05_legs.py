"""post1 · 05 · The H3 legs: (a) SOC-15 excluded, (b) within SOC major group, (e) work-dominant
tasks, with the retained fractions, the eight-row leg table, and the P4 persistence rule applied.

WHAT. prereg P3 fixes each leg's estimand and P4 fixes how the leg tests are counted and how H3 is
declared. This script produces, for every leg-wave (legs (a) and (b) in all three waves, leg (e) in
November and February — 3 + 3 + 2 = **eight leg tests**, the eight of the seventeen confirmatory
estimates):

    leg · wave · D · D_L · r_L = D_L/D · 95% interval for D_L · interval for r_L · interval for
    D_L − ½D · MDE for D_L · N (tasks and classified conversations) · retained mass · fired flag

and then the two verdicts P4 requires: the **persistent-leg rule** (primary — a leg must fire in
every wave in which it is testable) and the **literal any-wave reading** (reported beside it). It
also produces the descriptive material the pre-registration lists beside the legs and puts in no
decision rule: leg (c)'s leave-one-group-out series over the 22 major groups plus the group-spanning
bucket, leg (d)'s use-case mix by wage quartile (November and February), and the continuous slope
with the task's work share as a covariate, with the usage-weighted correlation and the VIF of the
two competing predictors printed beside it.

WHY, and what each leg is for (prereg P3, BRIEF §9(3)).
  (a) SOC-15 excluded — the coding family is 70–77% of top-quartile mass and is automative by
      Anthropic's own definition, so if the gradient is the coding family this leg removes it. The
      quartile boundaries are **kept from the full analysis set and are not re-drawn**; a
      group-spanning task is excluded if and only if rule A2 assigns it to SOC-15; the grouping is
      on the **2019 recode** as primary (V1) with the 2010 grouping beside it.
  (b) Within SOC major group — holds the group mix fixed and averages the within-group Q4−Q1
      contrasts over the groups that hold analysis-set tasks in **both** the global Q1 and the
      global Q4, each group weighted by W_{g,1} + W_{g,4}. Groups that do not hold both are
      reported as **not identified, never as zeros**. The primary identified set is the groups
      holding both (the marked completion of P3(b)); the subset spanning all four quartiles is
      reported beside it.
  (e) Work-dominant tasks — work share ≥ 0.50 of a task's **published** use-case cells, including
      `not_classified`, fixed in the pre-registration. Tasks whose only published cell is
      `not_classified` have an undefined work share and are **dropped, never scored 0**; the
      substantive-cell denominator is the pre-registered sensitivity. August publishes no `use_case`
      facet at any grain, so the leg is a two-wave statement there and is untestable in August.

HOW THE HALF JUDGEMENT IS READ. §9(3) declares a leg on the **point estimates** — a leg fires in a
wave if sign(D_L) ≠ sign(D) or |D_L| < ½|D| — and that is what is done here. Beside every leg this
script reports the interval for **D_L − ½D** (linear in the same per-task shares, so its SE is
exact) and the interval for r_L (a ratio with a small denominator; its delta-method SE understates,
which is why the contrast is the interval to read — the DEVIATION entry of 2026-09-17 in the
notebook).

VARIANCE. The same model as script 03 (prereg P1(a)): every leg is linear in the per-task shares, so
Var(D_L), Cov(D_L, D) and hence the intervals for r_L and for D_L − ½D are closed-form. The SE is a
lower bound under within-task dependence. Every coefficient carries its interval and its
MDE = 2.8 × SE.

OUTPUT. `posts/post1/data/processed/legs.json` and a console log. The check block compares every leg
point estimate against the independent implementation stored by script 04.
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

Z = 1.959964
MDE_K = 2.8


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B = _load("02_build")
H = _load("03_headline")
WAVES = B.WAVE_ORDER
UC_CATS = B.UC_CATS


# ---------------------------------------------------------------- leg estimands (prereg P3)
def leg_coefficients(an: pd.DataFrame, qw: np.ndarray, leg: str, group_col: str = "group2019",
                     work_col: str = "work_share", subset: str = "identified"
                     ) -> tuple[np.ndarray | None, dict]:
    """The coefficient vector of a leg, with the leg's coverage audit. Quartile masks are kept from
    the full analysis set and are never re-drawn (prereg P3).

    `subset` applies to leg (b) only: "identified" is the primary set of P3(b) (the groups holding
    analysis-set tasks in both the global Q1 and the global Q4) and "all_four" is the subset
    spanning all four quartiles, which P3(b) registers as reported beside it in every table.
    """
    w4, w1 = qw[:, 3].copy(), qw[:, 0].copy()
    info: dict = {}
    if leg == "a":
        drop = (an[group_col] == "15").to_numpy()
        keep = ~drop
        info["dropped_tasks"] = int(drop.sum())
        info["dropped_mass"] = float(an.w.to_numpy()[drop].sum())
        info["dropped_share_analysis"] = float(an.w.to_numpy()[drop].sum() / an.w.sum() * 100)
        info["dropped_share_q4"] = float(w4[drop].sum() / w4.sum() * 100)
        info["dropped_share_q1"] = float(w1[drop].sum() / w1.sum() * 100)
        w4, w1 = np.where(keep, w4, 0.0), np.where(keep, w1, 0.0)
    elif leg == "e":
        undefined = an[work_col].isna().to_numpy()
        keep = (an[work_col] >= 0.5).to_numpy() & ~undefined
        info["dropped_undefined_tasks"] = int((undefined & ((qw[:, 3] > 0) | (qw[:, 0] > 0))).sum())
        info["undefined_tasks_analysis"] = int(undefined.sum())
        info["undefined_mass_analysis"] = float(an.w.to_numpy()[undefined].sum())
        info["kept_tasks"] = int(keep.sum())
        info["kept_mass"] = float(an.w.to_numpy()[keep].sum())
        info["kept_share_analysis"] = float(an.w.to_numpy()[keep].sum() / an.w.sum() * 100)
        info["kept_share_q4"] = float(w4[keep].sum() / w4.sum() * 100)
        info["kept_share_q1"] = float(w1[keep].sum() / w1.sum() * 100)
        w4, w1 = np.where(keep, w4, 0.0), np.where(keep, w1, 0.0)
    elif leg == "b":
        groups = an[group_col].to_numpy()
        c = np.zeros(len(an))
        tot, identified, notid, all_four = 0.0, [], [], []
        qlab = qw.argmax(1) + 1
        for gname in sorted({g for g in groups if g is not None and not pd.isna(g)}):
            m = groups == gname
            g4, g1 = np.where(m, w4, 0.0), np.where(m, w1, 0.0)
            if g4.sum() <= 0 or g1.sum() <= 0:
                notid.append(gname)
                continue
            identified.append(gname)
            spans_all_four = {1, 2, 3, 4} <= set(qlab[m])
            if spans_all_four:
                all_four.append(gname)
            if subset == "all_four" and not spans_all_four:
                continue
            mass = g4.sum() + g1.sum()
            c += mass * (g4 / g4.sum() - g1 / g1.sum())
            tot += mass
        info["identified_groups"] = identified
        info["n_identified"] = len(identified)
        info["not_identified_groups"] = notid            # reported, never zeroed
        info["n_not_identified"] = len(notid)
        info["groups_all_four"] = all_four
        info["n_groups_all_four"] = len(all_four)
        info["subset"] = subset
        info["mass_share_q1_q4_used"] = float(tot / (w4.sum() + w1.sum()) * 100)
        info["identified_mass_share_q1_q4"] = float(tot / (w4.sum() + w1.sum()) * 100) \
            if subset == "identified" else None
        info["tasks_in_identified_groups"] = int(np.sum(np.isin(groups, identified)))
        return (c / tot if tot > 0 else None), info
    else:
        raise ValueError(leg)
    if w4.sum() <= 0 or w1.sum() <= 0:
        return None, info
    info["retained_mass_q1_q4"] = float((w4.sum() + w1.sum()) / (qw[:, 3].sum() + qw[:, 0].sum()) * 100)
    return w4 / w4.sum() - w1 / w1.sum(), info


def leg_row(an: pd.DataFrame, qw: np.ndarray, leg: str, wave: str, **kw) -> dict | None:
    """One row of the eight-row leg table (prereg P4)."""
    c_l, info = leg_coefficients(an, qw, leg, **kw)
    if c_l is None:
        return None
    c_d = H.quartile_coefficients(qw, 3) - H.quartile_coefficients(qw, 0)
    p, n = an.p.to_numpy(), an.n5.to_numpy()
    d = H.linear_stat(c_d, p, n)
    dl = H.linear_stat(c_l, p, n)
    contrast = H.linear_stat(c_l - 0.5 * c_d, p, n)
    var_l, var_d = dl["se"] ** 2, d["se"] ** 2
    cov = H.cov_linear(c_l, c_d, p, n)
    r = dl["coef"] / d["coef"]
    se_r = float(np.sqrt(max(var_l / d["coef"] ** 2
                             - 2 * dl["coef"] * cov / d["coef"] ** 3
                             + dl["coef"] ** 2 * var_d / d["coef"] ** 4, 0.0)))
    fired = bool(np.sign(dl["coef"]) != np.sign(d["coef"]) or abs(dl["coef"]) < 0.5 * abs(d["coef"]))
    used = c_l != 0
    # prereg P3(b): "the primary identified set is the 10 / 10 / 8 groups, with the 7 / 8 / 6
    # all-four subset reported beside it in every table; both go into results.json". The side-
    # estimate on the all-four subset, its interval and whether it fires, computed here.
    all_four = None
    if leg == "b" and kw.get("subset", "identified") == "identified":
        c_af, info_af = leg_coefficients(an, qw, "b", subset="all_four",
                                         **{k: v for k, v in kw.items() if k != "subset"})
        if c_af is not None:
            e = H.linear_stat(c_af, p, n)
            fired_af = bool(np.sign(e["coef"]) != np.sign(d["coef"])
                            or abs(e["coef"]) < 0.5 * abs(d["coef"]))
            all_four = dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                            r=e["coef"] / d["coef"], fired=fired_af,
                            groups=info_af["groups_all_four"],
                            n_groups=info_af["n_groups_all_four"],
                            mass_share_q1_q4=info_af["mass_share_q1_q4_used"])
    return dict(leg=leg, wave=wave, D=d["coef"], D_ci=d["ci"], D_se=d["se"],
                D_L=dl["coef"], D_L_ci=dl["ci"], D_L_se=dl["se"], D_L_mde=dl["mde"],
                r=r, r_se=se_r, r_ci=[r - Z * se_r, r + Z * se_r], r_mde=MDE_K * se_r,
                contrast=contrast["coef"], contrast_ci=contrast["ci"], contrast_se=contrast["se"],
                contrast_mde=contrast["mde"],
                corr_D_L_D=float(cov / np.sqrt(var_l * var_d)),
                n_tasks=int(used.sum()), n_conversations=float(n[used].sum()),
                fired=fired,
                fired_on_sign=bool(np.sign(dl["coef"]) != np.sign(d["coef"])),
                fired_on_half=bool(abs(dl["coef"]) < 0.5 * abs(d["coef"])),
                contrast_interval_straddles_zero=bool(contrast["ci"][0] <= 0 <= contrast["ci"][1]),
                D_L_all_four_subset=all_four,
                info=info)


# ---------------------------------------------------------------- descriptive material
def leave_one_group_out(an: pd.DataFrame, qw: np.ndarray, group_col: str = "group2019") -> list[dict]:
    """Leg (c): 22 leave-one-group-out re-estimates plus the group-spanning bucket. Description
    under §10; the SOC-15 leave-out dominates by construction and the post says so."""
    c_d = H.quartile_coefficients(qw, 3) - H.quartile_coefficients(qw, 0)
    p, n = an.p.to_numpy(), an.n5.to_numpy()
    base = H.linear_stat(c_d, p, n)["coef"]
    rows = []
    groups = an[group_col].to_numpy()
    for gname in sorted({g for g in groups if g is not None and not pd.isna(g)}):
        keep = groups != gname
        w4, w1 = np.where(keep, qw[:, 3], 0.0), np.where(keep, qw[:, 1 - 1], 0.0)
        if w4.sum() <= 0 or w1.sum() <= 0:
            rows.append(dict(left_out=gname, D=None, note="not identified after the leave-out"))
            continue
        c = w4 / w4.sum() - w1 / w1.sum()
        e = H.linear_stat(c, p, n)
        rows.append(dict(left_out=gname, D=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                         move=e["coef"] - base,
                         dropped_mass=float(an.w.to_numpy()[~keep].sum())))
    # the 23rd bucket: the tasks whose holders span more than one major group
    span = (an.nmg2010 > 1).to_numpy()
    w4, w1 = np.where(~span, qw[:, 3], 0.0), np.where(~span, qw[:, 0], 0.0)
    c = w4 / w4.sum() - w1 / w1.sum()
    e = H.linear_stat(c, p, n)
    rows.append(dict(left_out="group-spanning bucket", D=e["coef"], ci=e["ci"], se=e["se"],
                     mde=e["mde"], move=e["coef"] - base,
                     dropped_tasks=int(span.sum()),
                     dropped_mass=float(an.w.to_numpy()[span].sum())))
    return rows


def ten_largest_out(an: pd.DataFrame, qw: np.ndarray) -> dict:
    """The leave-out of the ten largest tasks by usage mass, with the denominator stated."""
    c_d = H.quartile_coefficients(qw, 3) - H.quartile_coefficients(qw, 0)
    p, n = an.p.to_numpy(), an.n5.to_numpy()
    base = H.linear_stat(c_d, p, n)["coef"]
    big = an.w.rank(ascending=False, method="first") <= 10
    keep = ~big.to_numpy()
    w4, w1 = np.where(keep, qw[:, 3], 0.0), np.where(keep, qw[:, 0], 0.0)
    c = w4 / w4.sum() - w1 / w1.sum()
    e = H.linear_stat(c, p, n)
    return dict(D=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"], move=e["coef"] - base,
                dropped_mass_wave=float(an.w.to_numpy()[big.to_numpy()].sum()),
                movers=list(an.task[big.to_numpy()].values))


def use_case_mix_by_quartile(an: pd.DataFrame, qw: np.ndarray) -> dict:
    """Leg (d): each wage quartile's work / personal / coursework mix beside its automation share.
    Description, in no decision rule."""
    out = {}
    for col, name in enumerate(["Q1", "Q2", "Q3", "Q4"]):
        m = qw[:, col] > 0
        cells = an.loc[m, ["uc_" + c for c in UC_CATS]].sum()
        tot = float(cells.sum())
        out[name] = {c: float(100 * cells["uc_" + c] / tot) for c in UC_CATS}
        out[name]["automation_share"] = float(np.average(an.p[m], weights=qw[m, col]))
    return out


def composition_figures(an: pd.DataFrame, qw: np.ndarray, group_col: str = "group2019") -> dict:
    """The composition figures `posts/post1/notes/referee-results.md` item 12 asks the analyst to
    reproduce from the build table, so that the post may cite them: the named software tasks' share
    of Q4, the top-minus-bottom contrast **inside** SOC-15, and what is left of Q4 once SOC-15 is
    excluded. Description of the sample's composition, in no decision rule and no new test — each is
    a re-weighting of the per-task shares already estimated for leg (a)."""
    w4, w1 = qw[:, 3], qw[:, 0]
    p, n = an.p.to_numpy(), an.n5.to_numpy()
    is15 = (an[group_col] == "15").to_numpy()
    out: dict = {}
    # (i) the largest software tasks' share of Q4's usage mass
    keys = ["modify existing software to correct errors",
            "write new programs or modify existing programs"]
    m_two = an.task.str.startswith(keys[0]).to_numpy()
    m_three = m_two | an.task.str.startswith(keys[1]).to_numpy()
    out["largest_software_tasks"] = dict(
        task_prefixes=keys,
        tasks_matching_first=int(m_two.sum()), tasks_matching_either=int(m_three.sum()),
        q4_mass_first=float(w4[m_two].sum()), q4_mass_either=float(w4[m_three].sum()),
        q4_mass_total=float(w4.sum()),
        q4_share_first=float(w4[m_two].sum() / w4.sum() * 100),
        q4_share_either=float(w4[m_three].sum() / w4.sum() * 100))
    # (ii) the top-minus-bottom contrast inside SOC-15 alone
    a4, a1 = np.where(is15, w4, 0.0), np.where(is15, w1, 0.0)
    if a4.sum() > 0 and a1.sum() > 0:
        c = a4 / a4.sum() - a1 / a1.sum()
        e = H.linear_stat(c, p, n)
        out["within_soc15_contrast"] = dict(coef=e["coef"], ci=e["ci"], se=e["se"], mde=e["mde"],
                                            q4_mass=float(a4.sum()), q1_mass=float(a1.sum()),
                                            q4_tasks=int((a4 > 0).sum()), q1_tasks=int((a1 > 0).sum()))
    # (iii) what is left of Q4 and Q1 once SOC-15 is excluded (leg (a)'s residual sample)
    r4, r1 = np.where(~is15, w4, 0.0), np.where(~is15, w1, 0.0)
    out["residual_after_soc15_exclusion"] = dict(
        q4_tasks=int((r4 > 0).sum()), q4_mass=float(r4.sum()), q4_kish=B.kish(r4),
        q4_share=float(np.average(p, weights=r4)),
        q1_tasks=int((r1 > 0).sum()), q1_mass=float(r1.sum()), q1_kish=B.kish(r1),
        q1_share=float(np.average(p, weights=r1)))
    return out


def slope_with_work_share(an: pd.DataFrame) -> dict:
    """The continuous companion with the task's work share as a covariate (§9(3)(e)), with the
    usage-weighted pairwise correlation and the VIF of the two competing predictors beside it."""
    sub = an[an.work_share.notna()].copy()
    plain, _ = H.slope(sub)
    partial, _ = H.slope(sub, extra_x="work_share")
    w = sub.w.to_numpy(float)
    x = sub.wage.to_numpy(float) / 10.0
    z = sub.work_share.to_numpy(float)
    ex, ez = np.average(x, weights=w), np.average(z, weights=w)
    cor = float(np.average((x - ex) * (z - ez), weights=w)
                / np.sqrt(np.average((x - ex) ** 2, weights=w) * np.average((z - ez) ** 2, weights=w)))
    vif = float(1.0 / (1.0 - cor ** 2))
    work_slope, _ = H.slope(sub.assign(work_pct=sub.work_share * 100), x_col="work_pct", per=10.0,
                            extra_x=None)
    return dict(n_tasks=int(len(sub)), slope_wage_only=plain, slope_wage_partial=partial,
                slope_work_share_only_per_10pp=work_slope,
                usage_weighted_corr_wage_workshare=cor, vif=vif)


# ---------------------------------------------------------------- P4: the two verdicts
def h3_verdicts(rows: list[dict]) -> dict:
    """The persistent-leg rule (primary) and the literal any-wave reading (reported beside it)."""
    by_leg: dict[str, list[dict]] = {}
    for r in rows:
        by_leg.setdefault(r["leg"], []).append(r)
    per_leg = {}
    for leg, rs in by_leg.items():
        per_leg[leg] = dict(waves_testable=len(rs), waves_fired=sum(1 for r in rs if r["fired"]),
                            fired_in_every_testable_wave=all(r["fired"] for r in rs),
                            waves=[r["wave"] for r in rs],
                            fired_by_wave={r["wave"]: r["fired"] for r in rs})
    persistent = any(v["fired_in_every_testable_wave"] for v in per_leg.values())
    any_wave = any(r["fired"] for r in rows)
    return dict(per_leg=per_leg,
                k_of_8_fired=sum(1 for r in rows if r["fired"]),
                leg_tests=len(rows),
                persistent_leg_rule_declares_H3=persistent,
                literal_any_wave_rule_declares_H3=any_wave,
                rules_agree=(persistent == any_wave),
                legs_firing_in_every_testable_wave=[k for k, v in per_leg.items()
                                                    if v["fired_in_every_testable_wave"]])


def main():
    out: dict = dict(script="posts/post1/scripts/05_legs.py",
                     prereg="posts/post1/prereg/prereg.md content c9b1b45",
                     leg_table=[], leg_table_2010=[], descriptive={}, waves={})
    rows, rows2010 = [], []
    print("=" * 104)
    print("THE EIGHT LEG TESTS (prereg P3, P4). Legs (a) and (b) in three waves, leg (e) in two.")
    print("  a leg fires in a wave if sign(D_L) ≠ sign(D) or |D_L| < ½|D| — the point-estimate rule of §9(3)")
    for wave in WAVES:
        an = B.analysis_set(wave)
        qw = B.quartile_weights(an, "wage", "registered")
        has_uc = an.work_share.notna().any()
        legs = ["a", "b"] + (["e"] if has_uc else [])
        print("-" * 104)
        print(f"  [{wave}]  legs testable: {legs}" + ("" if has_uc else
              "   (August publishes no `use_case` facet at any grain: leg (e) untestable, asserted not tested)"))
        for leg in legs:
            r = leg_row(an, qw, leg, wave)
            rows.append(r)
            print(f"    leg ({leg})  D {r['D']:+.4f}  D_L {r['D_L']:+.4f} "
                  f"[{r['D_L_ci'][0]:+.4f}, {r['D_L_ci'][1]:+.4f}]  SE {r['D_L_se']:.4f}  "
                  f"MDE {r['D_L_mde']:.4f}")
            print(f"              r_L {r['r']:+.4f} [{r['r_ci'][0]:+.4f}, {r['r_ci'][1]:+.4f}]  "
                  f"D_L−½D {r['contrast']:+.4f} [{r['contrast_ci'][0]:+.4f}, {r['contrast_ci'][1]:+.4f}] "
                  f"(MDE {r['contrast_mde']:.4f})  corr(D_L, D) {r['corr_D_L_D']:.3f}")
            print(f"              tasks {r['n_tasks']}  conversations {r['n_conversations']:,.0f}  "
                  f"FIRED: {r['fired']} (on sign {r['fired_on_sign']}, on half {r['fired_on_half']})")
            print(f"              coverage: {r['info']}")
            if r.get("D_L_all_four_subset"):
                af = r["D_L_all_four_subset"]
                print(f"              [all-four subset, the P3(b) side-estimate] D_(b) {af['coef']:+.4f} "
                      f"[{af['ci'][0]:+.4f}, {af['ci'][1]:+.4f}]  SE {af['se']:.4f}  r {af['r']:+.4f}  "
                      f"FIRED {af['fired']}  over {af['n_groups']} groups carrying "
                      f"{af['mass_share_q1_q4']:.2f}% of Q1+Q4 mass")
            r2 = leg_row(an, qw, leg, wave, group_col="group2010") if leg in ("a", "b") else None
            if r2:
                rows2010.append(r2)
                print(f"              [2010 grouping beside it] D_L {r2['D_L']:+.4f} "
                      f"[{r2['D_L_ci'][0]:+.4f}, {r2['D_L_ci'][1]:+.4f}]  r_L {r2['r']:+.4f}  "
                      f"FIRED {r2['fired']}")
            if leg == "e":
                rs = leg_row(an, qw, leg, wave, work_col="work_share_subst")
                out["waves"].setdefault(wave, {})["leg_e_substantive_denominator"] = rs
                print(f"              [substantive-cell denominator, the pre-registered sensitivity] "
                      f"D_L {rs['D_L']:+.4f} [{rs['D_L_ci'][0]:+.4f}, {rs['D_L_ci'][1]:+.4f}]  "
                      f"r_L {rs['r']:+.4f}  FIRED {rs['fired']}")
        # descriptive material
        d = out["descriptive"].setdefault(wave, {})
        d["composition_figures"] = composition_figures(an, qw)
        d["leave_one_group_out"] = leave_one_group_out(an, qw)
        d["ten_largest_out"] = ten_largest_out(an, qw)
        if has_uc:
            d["use_case_mix_by_quartile"] = use_case_mix_by_quartile(an, qw)
            d["slope_with_work_share"] = slope_with_work_share(an)

    out["leg_table"] = rows
    out["leg_table_2010"] = rows2010
    out["h3"] = h3_verdicts(rows)
    out["h3_2010"] = h3_verdicts(rows2010)

    print("=" * 104)
    v = out["h3"]
    print(f"P4 · {v['k_of_8_fired']} of {v['leg_tests']} leg tests fired "
          f"(legs (a) and (b) out of 3 waves each, leg (e) out of 2)")
    for leg, s in v["per_leg"].items():
        print(f"   leg ({leg}) fired in {s['waves_fired']} of {s['waves_testable']} testable waves "
              f"{s['fired_by_wave']}")
    print(f"   PRIMARY (persistent-leg rule): H3 declared = {v['persistent_leg_rule_declares_H3']}"
          f"  (legs firing in every testable wave: {v['legs_firing_in_every_testable_wave']})")
    print(f"   REPORTED BESIDE IT (literal any-wave reading): H3 declared = "
          f"{v['literal_any_wave_rule_declares_H3']}   the two rules agree: {v['rules_agree']}")
    print(f"   on the 2010 grouping: persistent {out['h3_2010']['persistent_leg_rule_declares_H3']}, "
          f"any-wave {out['h3_2010']['literal_any_wave_rule_declares_H3']}, "
          f"{out['h3_2010']['k_of_8_fired']} of {out['h3_2010']['leg_tests']} fired")

    # H1's own signature clause (prereg H1 "rule for support"): D keeping more than half its size,
    # same sign, on every leg testable in that wave. Reported whatever the owner is.
    sig = {}
    for wave in WAVES:
        rs = [r for r in rows if r["wave"] == wave]
        sig[wave] = dict(legs_testable=[r["leg"] for r in rs],
                         keeps_half_and_sign_on_every_testable_leg=all(not r["fired"] for r in rs))
    out["h1_signature_clause"] = sig
    print("\nH1's signature clause (D keeping more than half its size, same sign, on every leg "
          "testable in that wave):")
    for wave, s in sig.items():
        print(f"   {wave}: {s['keeps_half_and_sign_on_every_testable_leg']}  (legs {s['legs_testable']})")

    print("\n" + "=" * 104)
    print("Description, in no decision rule")
    for wave in WAVES:
        d = out["descriptive"][wave]
        logo = [r for r in d["leave_one_group_out"] if r.get("D") is not None]
        worst = max(logo, key=lambda r: abs(r["move"]))
        second = sorted(logo, key=lambda r: -abs(r["move"]))[1]
        print(f"  [{wave}] leave-one-group-out: {len(logo)} re-estimates; largest mover "
              f"{worst['left_out']} ({worst['move']:+.4f} pp), second {second['left_out']} "
              f"({second['move']:+.4f} pp); |largest| > sum of the others: "
              f"{abs(worst['move']) > sum(abs(r['move']) for r in logo if r is not worst)}")
        cf = d["composition_figures"]
        print(f"          composition (referee-results item 12): the two \"modify existing "
              f"software…\" tasks hold {cf['largest_software_tasks']['q4_mass_first']:.2f} pp of "
              f"Q4's {cf['largest_software_tasks']['q4_mass_total']:.2f} pp "
              f"({cf['largest_software_tasks']['q4_share_first']:.1f}%), "
              f"{cf['largest_software_tasks']['q4_mass_either']:.2f} pp with the third; within "
              f"SOC-15 alone D = {cf['within_soc15_contrast']['coef']:+.4f} "
              f"[{cf['within_soc15_contrast']['ci'][0]:+.4f}, "
              f"{cf['within_soc15_contrast']['ci'][1]:+.4f}]; the residual Q4 after the SOC-15 "
              f"exclusion is {cf['residual_after_soc15_exclusion']['q4_tasks']} tasks, "
              f"{cf['residual_after_soc15_exclusion']['q4_mass']:.2f} pp, Kish "
              f"{cf['residual_after_soc15_exclusion']['q4_kish']:.1f}, share "
              f"{cf['residual_after_soc15_exclusion']['q4_share']:.2f} against a residual Q1 of "
              f"{cf['residual_after_soc15_exclusion']['q1_share']:.2f}")
        t10 = d["ten_largest_out"]
        print(f"          ten largest tasks out: D {t10['D']:+.4f} [{t10['ci'][0]:+.4f}, "
              f"{t10['ci'][1]:+.4f}] (move {t10['move']:+.4f} pp; {t10['dropped_mass_wave']:.4f} pp "
              f"of the wave)")
        if "use_case_mix_by_quartile" in d:
            mix = d["use_case_mix_by_quartile"]
            print("          use-case mix by quartile (work / personal / coursework, % of published cells):")
            for q in ("Q1", "Q2", "Q3", "Q4"):
                print(f"             {q}  work {mix[q]['work']:5.2f}  personal {mix[q]['personal']:5.2f}  "
                      f"coursework {mix[q]['coursework']:5.2f}  not_classified {mix[q]['not_classified']:5.2f}"
                      f"  automation share {mix[q]['automation_share']:.4f}")
            s = d["slope_with_work_share"]
            print(f"          slope per +$10/hr alone {s['slope_wage_only']['coef']:+.4f} "
                  f"[{s['slope_wage_only']['ci'][0]:+.4f}, {s['slope_wage_only']['ci'][1]:+.4f}]; "
                  f"with the work share as a covariate {s['slope_wage_partial']['coef']:+.4f} "
                  f"[{s['slope_wage_partial']['ci'][0]:+.4f}, {s['slope_wage_partial']['ci'][1]:+.4f}]; "
                  f"usage-weighted corr(wage, work share) {s['usage_weighted_corr_wage_workshare']:+.4f}, "
                  f"VIF {s['vif']:.3f}")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / "legs.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    print(f"\nwrote {(PROCESSED / 'legs.json').relative_to(ROOT)}")
    return out


if __name__ == "__main__":
    O = main()

    # ------------------------------------------------------------ check block
    second = json.loads((PROCESSED / "second_implementation.json").read_text())

    # exactly eight leg tests: (a) and (b) in three waves, (e) in two
    assert len(O["leg_table"]) == 8, len(O["leg_table"])
    counts = {leg: sum(1 for r in O["leg_table"] if r["leg"] == leg) for leg in "abe"}
    assert counts == {"a": 3, "b": 3, "e": 2}, counts
    assert all(r["wave"] != "aug2025" for r in O["leg_table"] if r["leg"] == "e"), "leg (e) in August"

    for r in O["leg_table"]:
        # every leg carries an interval and an MDE, and the arithmetic of the row is consistent
        assert abs(r["D_L_mde"] - MDE_K * r["D_L_se"]) < 1e-12, r
        assert abs(r["r"] - r["D_L"] / r["D"]) < 1e-12, r
        assert abs(r["contrast"] - (r["D_L"] - 0.5 * r["D"])) < 1e-9, r
        assert r["D_L_ci"][0] < r["D_L"] < r["D_L_ci"][1], r
        assert -1.0 <= r["corr_D_L_D"] <= 1.0, r
        # the fired flag is exactly the §9(3) rule on the point estimates
        assert r["fired"] == bool(np.sign(r["D_L"]) != np.sign(r["D"]) or abs(r["D_L"]) < 0.5 * abs(r["D"])), r
        assert r["n_tasks"] > 0 and r["n_conversations"] > 0, r
        # the second, independent implementation agrees on the point estimate to 1e-6 pp
        s = second["waves"][r["wave"]]["legs_second"][r["leg"]]
        assert s is not None, r
        assert abs(s["coef"] - r["D_L"]) < 1e-6, (r["leg"], r["wave"], s["coef"], r["D_L"])
        assert abs(s["se"] - r["D_L_se"]) < 1e-6, (r["leg"], r["wave"])
        assert np.sign(s["r"]) == np.sign(r["r"]), (r["leg"], r["wave"])

    # leg coverage counts, as the pre-registration records them
    for r in O["leg_table"]:
        info = r["info"]
        if r["leg"] == "a":
            rec = {"aug2025": 39.86, "nov2025": 37.12, "feb2026": 33.11}[r["wave"]]
            # A2's drop mass on the 2019 recode against the recorded 2010 A1 share (±6 pp: a
            # different vintage and a different allocation rule, both printed by script 02)
            assert abs(info["dropped_share_analysis"] - rec) < 6.0, (r["wave"], info)
            # the leg removes most of Q4 by construction, which is why its SE rises
            assert info["dropped_share_q4"] > 60.0, (r["wave"], info)
            assert r["D_L_se"] > r["D_se"], (r["wave"], r["D_L_se"], r["D_se"])
        if r["leg"] == "b":
            assert abs(info["n_identified"] - {"aug2025": 10, "nov2025": 10, "feb2026": 8}[r["wave"]]) <= 2, \
                (r["wave"], info["n_identified"])
            assert abs(info["n_groups_all_four"] - {"aug2025": 7, "nov2025": 8, "feb2026": 6}[r["wave"]]) <= 2, \
                (r["wave"], info["n_groups_all_four"])
            assert info["n_identified"] + info["n_not_identified"] == 22, (r["wave"], info)
            assert info["identified_mass_share_q1_q4"] > 50.0, (r["wave"], info)
        if r["leg"] == "e":
            assert info["kept_tasks"] == {"nov2025": 943, "feb2026": 1071}[r["wave"]], (r["wave"], info)
            assert abs(info["kept_share_analysis"] - {"nov2025": 54.38, "feb2026": 52.86}[r["wave"]]) < 0.05, \
                (r["wave"], info)
            assert info["undefined_tasks_analysis"] == {"nov2025": 29, "feb2026": 21}[r["wave"]], \
                (r["wave"], info)
            assert abs(info["undefined_mass_analysis"] - {"nov2025": 0.0779, "feb2026": 0.0527}[r["wave"]]) < 5e-4, \
                (r["wave"], info)

    # P4's counting and the two verdicts
    h3 = O["h3"]
    assert h3["leg_tests"] == 8 and 0 <= h3["k_of_8_fired"] <= 8, h3
    assert h3["per_leg"]["a"]["waves_testable"] == 3 and h3["per_leg"]["e"]["waves_testable"] == 2, h3
    assert h3["persistent_leg_rule_declares_H3"] == any(
        v["fired_in_every_testable_wave"] for v in h3["per_leg"].values()), h3
    assert h3["literal_any_wave_rule_declares_H3"] == any(r["fired"] for r in O["leg_table"]), h3
    # the persistent rule is at least as strict as the literal one
    assert not (h3["persistent_leg_rule_declares_H3"] and not h3["literal_any_wave_rule_declares_H3"]), h3
    # H1's signature clause is the complement of "some testable leg fired in that wave"
    for wave, s in O["h1_signature_clause"].items():
        fired_here = any(r["fired"] for r in O["leg_table"] if r["wave"] == wave)
        assert s["keeps_half_and_sign_on_every_testable_leg"] == (not fired_here), (wave, s)

    # description: the leave-one-group-out series has 22 groups plus the spanning bucket, and the
    # SOC-15 leave-out dominates it by construction (the post states this)
    for wave in WAVES:
        logo = O["descriptive"][wave]["leave_one_group_out"]
        assert len([r for r in logo if r["left_out"] != "group-spanning bucket"]) == 22, (wave, len(logo))
        assert any(r["left_out"] == "group-spanning bucket" for r in logo), wave
        # referee-results item 15: this is a RESULT, not a fact about the code — the SOC-15
        # leave-out dominating the series is what H3 predicts and a failure would have been a
        # finding. Printed, not asserted.
        moves = {r["left_out"]: abs(r["move"]) for r in logo if r.get("D") is not None}
        top = sorted(moves.items(), key=lambda kv: -kv[1])[:3]
        print(f"  [{wave}] largest leave-one-group-out movers (printed, not asserted): {top}")
        t10 = O["descriptive"][wave]["ten_largest_out"]
        assert len(t10["movers"]) == 10 and t10["dropped_mass_wave"] > 0, (wave, t10)

    # leg (d) and the competing predictors, where the facet exists
    for wave in ("nov2025", "feb2026"):
        mix = O["descriptive"][wave]["use_case_mix_by_quartile"]
        for q in ("Q1", "Q2", "Q3", "Q4"):
            tot = sum(mix[q][c] for c in UC_CATS)
            assert abs(tot - 100.0) < 1e-6, (wave, q, tot)
        assert mix["Q4"]["work"] > mix["Q1"]["work"] + 25.0, (wave, mix["Q1"]["work"], mix["Q4"]["work"])
        s = O["descriptive"][wave]["slope_with_work_share"]
        assert 0.9 <= s["vif"] <= 5.0, (wave, s["vif"])          # collinearity reported, not assumed
        assert abs(s["vif"] - 1.0 / (1.0 - s["usage_weighted_corr_wage_workshare"] ** 2)) < 1e-9, wave

    print("\nCHECK BLOCK PASSED — 05_legs.py")
