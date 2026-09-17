"""post1 · 07 · The fourth window (C10), design-based only and outside the confirmatory set.

WHAT. `release_2025_03_27/automation_vs_augmentation_by_task.csv` (Feb–Mar 2025) is a fourth
task-level window on the unchanged five-pattern taxonomy. This script rebuilds the per-task
automation share in that window, matches it onto each long wave's analysis set and wage quartiles
(kept, never re-drawn), and reports D in that window with a **design-based (task-resampling)**
interval only.

WHY IT CARRIES NO CONVERSATION-LEVEL INTERVAL (prereg P7, BRIEF §10). The file publishes **no
counts** — six float ratio columns summing to exactly 1.0 — so there is no n_i and no binomial
variance; the only interval available is the design-based one, which resamples tasks. The window is
in **no decision rule** and can neither declare nor refute an owner: it is a design-based bound on
whether the gradient's sign predates the three long waves.

WHAT ELSE THE WINDOW FORCES, all printed and asserted.
  · The per-task share is (`directive` + `feedback_loop`) renormalised over the five classified
    ratios, i.e. over 1 − `filtered`; the pattern column names are **underscored** and no column is
    named `collaboration`.
  · The **1,066 rows at `filtered` = 1.0** — 179 / 251 / 286 of the matched analysis-set tasks — are
    **dropped, never zeroed**, and the dropped count and mass are printed.
  · There is **no task-level `none` share**: `filtered` is 8.0623 pp of the task base against a
    global `none` of 3.2389, so it is `none` plus about 4.8 pp of unpublished exclusions and cannot
    be decomposed. §9(1)'s `none`-beside-every-share rule therefore holds at the **global level
    only** in this window, and that is stated wherever the window appears.
  · On this base the usage-weighted global automation share is **43.2902%** against the release's
    published **43.0619%** — a 0.23 pp gap, the analogue of §8(iii)'s +0.13 / +0.29 / +0.35 pp, and
    it is reported wherever a C10 number is.
  · The window reaches **1,635 / 1,843 / 1,904** of the 1,802 / 2,075 / 2,188 analysis-set tasks
    (98.78 / 98.49 / 98.08% of their mass) and the task list is **not a panel**, so entry and exit
    are not random.

WEIGHTS. The window's own usage weight is `task_pct_v2`'s `pct`, which is the analogue of
`onet_task_pct` and is the primary weighting here. The alternative — `pct` weighted by the five
classified ratios, i.e. by 1 − `filtered`, which is the weighting that reproduces the release's own
global share — is reported beside it in the same entry, because the release forces the choice and
neither reading is privileged by the pre-registration.

OUTPUT. `posts/post1/data/processed/fourth_window.json` and a console log.
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
C10 = ROOT / "data/cache/release_2025_03_27"

Z = 1.959964
MDE_K = 2.8
C10_CLASSIFIED = ["directive", "feedback_loop", "learning", "task_iteration", "validation"]
C10_AUTO = ["directive", "feedback_loop"]


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B = _load("02_build")
WAVES = B.WAVE_ORDER


def load_c10() -> tuple[pd.DataFrame, dict]:
    bt = pd.read_csv(C10 / "automation_vs_augmentation_by_task.csv", keep_default_na=False, na_values=[])
    v2 = pd.read_csv(C10 / "task_pct_v2.csv", keep_default_na=False, na_values=[])
    g5 = pd.read_csv(C10 / "automation_vs_augmentation_v2.csv", keep_default_na=False, na_values=[])
    audit = dict(
        by_task_shape=list(bt.shape), columns=list(bt.columns),
        has_collaboration_column=bool("collaboration" in bt.columns),
        count_or_pct_columns=[c for c in bt.columns if c.endswith(("_count", "_pct"))],
        max_abs_row_sum_minus_one=float((bt.drop(columns=["task_name"]).sum(1) - 1).abs().max()),
        filtered_median=float(bt.filtered.median()),
        rows_filtered_one=int((bt.filtered == 1.0).sum()),
        v2_rows=int(len(v2)), v2_pct_sum=float(v2.pct.sum()))
    m = v2.merge(bt, on="task_name", how="inner")
    audit["merge_rows_in"] = int(len(v2))
    audit["merge_matched"] = int(len(m))
    audit["merge_unmatched_names"] = sorted(set(v2.task_name) - set(bt.task_name))
    audit["matched_pct_carried"] = float(m.pct.sum())
    audit["classified_weighted_pct"] = float((m.pct * m[C10_CLASSIFIED].sum(1)).sum())
    auto = float((m.pct * m[C10_AUTO].sum(1)).sum())
    audit["global_automation_share"] = float(100 * auto / audit["classified_weighted_pct"])
    gp = dict(zip(g5.interaction_type, g5.pct))
    audit["published_global_automation_share"] = float(
        100 * (gp["directive"] + gp["feedback_loop"]) / (sum(gp.values()) - gp["none"])
        if "feedback_loop" in gp else float("nan"))
    audit["published_global_row"] = {k: float(v) for k, v in gp.items()}
    audit["global_none_pct"] = float(gp["none"])
    audit["filtered_pp_of_task_base"] = float(100 - audit["classified_weighted_pct"]
                                              - (100 - audit["matched_pct_carried"]))
    m["key"] = m.task_name.str.lower().str.strip()
    m["p_c10"] = np.where(m[C10_CLASSIFIED].sum(1) > 0,
                          m[C10_AUTO].sum(1) / m[C10_CLASSIFIED].sum(1) * 100, np.nan)
    return m, audit


def design_interval(p: np.ndarray, w: np.ndarray, m4: np.ndarray, m1: np.ndarray,
                    draws: int = 4000, seed: int = 20260917) -> dict:
    """The only interval this window can carry: resample **tasks** equal-probability inside each
    extreme quartile and recompute the usage-weighted mean difference."""
    rng = np.random.default_rng(seed)
    i4, i1 = np.flatnonzero(m4), np.flatnonzero(m1)
    d = np.empty(draws)
    for b in range(draws):
        s4 = rng.integers(0, len(i4), len(i4))
        s1 = rng.integers(0, len(i1), len(i1))
        d[b] = (np.average(p[i4][s4], weights=w[i4][s4])
                - np.average(p[i1][s1], weights=w[i1][s1]))
    point = float(np.average(p[m4], weights=w[m4]) - np.average(p[m1], weights=w[m1]))
    se = float(d.std(ddof=1))
    return dict(coef=point, se=se, ci=[point - Z * se, point + Z * se], mde=MDE_K * se,
                draws=draws, n_tasks_q4=int(m4.sum()), n_tasks_q1=int(m1.sum()),
                interval_type="design-based task resampling (no counts exist in this window)")


def main():
    m, audit = load_c10()
    out: dict = dict(script="posts/post1/scripts/07_fourth_window.py",
                     prereg="posts/post1/prereg/prereg.md content c9b1b45",
                     in_no_decision_rule=True,
                     audit=audit,
                     none_share_note=("there is no task-level `none` share in this release: "
                                      "`filtered` is `none` plus about 4.8 pp of unpublished "
                                      "exclusions and cannot be decomposed, so §9(1)'s "
                                      "`none`-beside-every-share rule holds at the global level "
                                      "only in this window"),
                     not_a_panel=("the release's own v1 ∩ v2 is 2,781 of 3,513 / 3,364, so entry "
                                  "and exit are not random and the window is a design-based check"),
                     waves={})
    print("=" * 96)
    print(f"C10 (Feb–Mar 2025): {audit['by_task_shape']} columns {audit['columns']}")
    print(f"  no `collaboration` column: {not audit['has_collaboration_column']}; no count/pct columns: "
          f"{audit['count_or_pct_columns'] == []}; row sums to 1 within "
          f"{audit['max_abs_row_sum_minus_one']:.1e}")
    print(f"  MERGE AUDIT task_pct_v2 -> by_task: {audit['merge_rows_in']} in, {audit['merge_matched']} "
          f"matched, unmatched {audit['merge_unmatched_names']}; matched carry "
          f"{audit['matched_pct_carried']:.4f} of 100 pct; classified-weighted "
          f"{audit['classified_weighted_pct']:.4f}")
    print(f"  filtered median {audit['filtered_median']:.4f}; rows at filtered == 1.0 "
          f"{audit['rows_filtered_one']}")
    print(f"  usage-weighted global automation share {audit['global_automation_share']:.4f}% against "
          f"the release's published 43.0619% — a "
          f"{audit['global_automation_share'] - 43.0619:.2f} pp gap, reported wherever a C10 number is")

    key_to_p = dict(zip(m.key, m.p_c10))
    key_to_w = dict(zip(m.key, m.pct))
    key_to_f = dict(zip(m.key, m.filtered))
    for wave in WAVES:
        an = B.analysis_set(wave)
        qw = B.quartile_weights(an, "wage", "registered")
        an = an.assign(p_c10=an.key.map(key_to_p), w_c10=an.key.map(key_to_w),
                       filtered=an.key.map(key_to_f))
        matched = an.filtered.notna().to_numpy()
        usable = matched & (an.filtered < 1.0).to_numpy() & an.p_c10.notna().to_numpy()
        row = dict(
            matched_tasks=int(matched.sum()),
            unmatched_tasks=int((~matched).sum()),
            matched_mass=float(an.w.to_numpy()[matched].sum()),
            matched_mass_share=float(an.w.to_numpy()[matched].sum() / an.w.sum() * 100),
            dropped_filtered_one_tasks=int((matched & (an.filtered == 1.0).to_numpy()).sum()),
            dropped_filtered_one_mass=float(an.w.to_numpy()[matched & (an.filtered == 1.0).to_numpy()].sum()),
            usable_tasks=int(usable.sum()),
            usable_mass=float(an.w.to_numpy()[usable].sum()),
            dropped_never_zeroed=True)
        p = np.nan_to_num(an.p_c10.to_numpy(), nan=0.0)
        m4 = usable & (qw[:, 3] > 0)
        m1 = usable & (qw[:, 0] > 0)
        # primary weighting: the window's own usage weight, `pct`
        w_pct = np.nan_to_num(an.w_c10.to_numpy(), nan=0.0)
        row["D_pct_weights"] = design_interval(p, w_pct, m4, m1)
        # beside it: `pct` weighted by the five classified ratios (the weighting that reproduces the
        # release's own global share)
        w_cls = w_pct * (1.0 - np.nan_to_num(an.filtered.to_numpy(), nan=1.0))
        row["D_classified_weights"] = design_interval(p, w_cls, m4, m1)
        row["quartile_masks"] = "kept from the long wave's analysis set, never re-drawn"
        out["waves"][wave] = row
        e = row["D_pct_weights"]
        print("-" * 96)
        print(f"  [{wave}] matched {row['matched_tasks']} of {len(an)} analysis-set tasks "
              f"({row['matched_mass_share']:.2f}% of their mass); filtered == 1.0 dropped on "
              f"{row['dropped_filtered_one_tasks']} tasks ({row['dropped_filtered_one_mass']:.4f} pp), "
              f"never zeroed; usable {row['usable_tasks']}")
        print(f"          D in the fourth window (task_pct_v2 weights, this wave's quartiles): "
              f"{e['coef']:+.4f} [{e['ci'][0]:+.4f}, {e['ci'][1]:+.4f}] design-based SE {e['se']:.4f}, "
              f"MDE {e['mde']:.4f}  — in no decision rule")
        e2 = row["D_classified_weights"]
        print(f"          same, weighted by pct × (1 − filtered): {e2['coef']:+.4f} "
              f"[{e2['ci'][0]:+.4f}, {e2['ci'][1]:+.4f}]  MDE {e2['mde']:.4f}")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / "fourth_window.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    print(f"\nwrote {(PROCESSED / 'fourth_window.json').relative_to(ROOT)}")
    return out


if __name__ == "__main__":
    O = main()

    # ------------------------------------------------------------ check block
    a = O["audit"]
    assert a["by_task_shape"] == [3364, 7], a["by_task_shape"]
    assert not a["has_collaboration_column"] and a["count_or_pct_columns"] == [], a
    assert a["max_abs_row_sum_minus_one"] < 1e-12, a["max_abs_row_sum_minus_one"]
    assert abs(a["filtered_median"] - 0.30) < 1e-9, a["filtered_median"]
    assert a["rows_filtered_one"] == 1066, a["rows_filtered_one"]
    assert a["v2_rows"] == 3365 and abs(a["v2_pct_sum"] - 100.0) < 1e-9, a
    assert a["merge_rows_in"] == 3365 and a["merge_matched"] == 3364, a
    assert a["merge_unmatched_names"] == ["none"], a["merge_unmatched_names"]
    assert abs(a["matched_pct_carried"] - 98.2183) < 5e-4, a["matched_pct_carried"]
    assert abs(a["classified_weighted_pct"] - 90.1561) < 5e-4, a["classified_weighted_pct"]
    assert abs(a["global_automation_share"] - 43.2902) < 5e-4, a["global_automation_share"]
    assert abs(a["global_automation_share"] - 43.0619 - 0.2283) < 5e-3, a["global_automation_share"]
    assert abs(a["global_none_pct"] - 3.238949) < 1e-6, a["global_none_pct"]

    rec_matched = {"aug2025": 1635, "nov2025": 1843, "feb2026": 1904}
    rec_filtered = {"aug2025": 179, "nov2025": 251, "feb2026": 286}
    rec_mass_share = {"aug2025": 98.78, "nov2025": 98.49, "feb2026": 98.08}
    for wave in WAVES:
        r = O["waves"][wave]
        assert r["matched_tasks"] == rec_matched[wave], (wave, r["matched_tasks"])
        assert r["dropped_filtered_one_tasks"] == rec_filtered[wave], (wave, r["dropped_filtered_one_tasks"])
        assert abs(r["matched_mass_share"] - rec_mass_share[wave]) < 0.01, (wave, r["matched_mass_share"])
        assert r["usable_tasks"] == r["matched_tasks"] - r["dropped_filtered_one_tasks"], (wave, r)
        for key in ("D_pct_weights", "D_classified_weights"):
            e = r[key]
            # the only interval this window can carry is the design-based one, and it is wide
            assert e["interval_type"].startswith("design-based"), (wave, key)
            assert abs(e["mde"] - MDE_K * e["se"]) < 1e-12, (wave, key)
            assert e["se"] > 0.5, (wave, key, e["se"])     # no conversation-level precision here
            assert e["n_tasks_q4"] > 0 and e["n_tasks_q1"] > 0, (wave, key)
    # the window is in no decision rule, and the script says so in its output
    assert O["in_no_decision_rule"] is True

    print("\nCHECK BLOCK PASSED — 07_fourth_window.py")
