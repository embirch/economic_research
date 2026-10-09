#!/usr/bin/env python3
"""Bounded E08 occupation/sector influence diagnostic, authorised 9 October 2026.

Only unpaid job work (WTQ_45 in {1, 2}) is analysed. Original analysis, results
and source pins are read but never written. No network or historical helpers.

Example, from any directory:
  python /path/to/E08/influence_check.py --cache /path/to/E08-cache \
      --private-out /path/to/private/E08-influence-20261009

Required adjacent files: source-manifest.json and results.json. Dependencies:
numpy and pandas. Fine-cell estimates, support and all labelled deletion results
are written ONLY to --private-out. That directory must be outside the served
programme tree and this script's directory. The public summary contains no
stratum labels or individual deletion estimates. Never publish private outputs.

Fixed accounting: a = (1,-1,-1,1) for Men+ nonusers/users, Women+ nonusers/users.
For stratum s and group g, q_s is the pooled employee target share, p_sg the
within-group job share and m_sg the outcome mean. Its contribution to the
common-minus-raw interaction is c_s = sum_g a_g (q_s - p_sg) m_sg.

All 16 strata are diagnosed and all 16 are deleted once, from all four groups.
Each deletion recalculates group and target weights on its remaining population.
It is NOT an alternative estimate for the original employee population.
"""

import os

for thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(thread_key, "1")

import argparse
import hashlib
import json
import platform
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parent
LABELS = ["Men+ nonusers", "Men+ users", "Women+ nonusers", "Women+ users"]
SIGNS = np.array([1.0, -1.0, -1.0, 1.0])
N_REPLICATES = 1000
TOLERANCE = 1e-12
THRESHOLDS = (5, 75, 150)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, obj, private=False):
    text = json.dumps(obj, indent=2, allow_nan=False) + "\n"
    # Set restrictive permissions when creating private files, not after writing.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600 if private else 0o644)
    with os.fdopen(fd, "w") as stream:
        stream.write(text)
    if private:
        path.chmod(0o600)


def grade(n):
    return "A" if n >= 150 else "E" if n >= 75 else "F"


def round_one(value):
    result = float(Decimal(str(float(value))).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
    return 0.0 if result == 0 else result


def summarize(values):
    values = np.asarray(values, dtype=float)
    require(values.shape == (1001,), "Unexpected replicate vector shape")
    require(np.isfinite(values).all(), "Undefined replicate; uncertainty cannot be computed")
    point = float(values[0])
    se = float(np.sqrt(np.mean((values[1:] - point) ** 2)))
    return {"estimate": point, "se": se,
            "interval_95": [point - 1.96 * se, point + 1.96 * se],
            "finite_replicates": 1000}


def public_stat(values):
    obj = summarize(values)
    return {"estimate_pp": round_one(100 * obj["estimate"]),
            "interval_95_pp": [round_one(100 * x) for x in obj["interval_95"]]}


def reconcile(values, reference, target, records):
    actual = summarize(values)
    errors = {name: abs(actual[name] - reference[name]) for name in ("estimate", "se")}
    errors["interval_95"] = float(np.max(np.abs(np.array(actual["interval_95"]) - reference["interval_95"])))
    require(max(errors.values()) < TOLERANCE, "Original-result reconciliation failed: " + target)
    records.append({"target": target, "maximum_absolute_error": max(errors.values())})


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cache", required=True, type=Path, help="Directory containing the five pinned source files")
    parser.add_argument("--private-out", required=True, type=Path, help="Ignored/external private diagnostic directory")
    parser.add_argument("--summary", type=Path, default=HERE / "influence-summary.json", help="Safe public summary output")
    args = parser.parse_args()
    cache = args.cache.resolve()
    private = args.private_out.resolve()
    summary_path = args.summary.resolve()
    require(not private.is_relative_to(HERE), "Private outputs must be outside the article directory")
    for ancestor in HERE.parents:
        if (ancestor / "programme").is_dir():
            require(not private.is_relative_to(ancestor / "programme"), "Private outputs must be outside the served programme tree")
            break
    require(private != cache and not cache.is_relative_to(private), "Use a separate diagnostic directory, not the source cache or its ancestor")
    require(summary_path.name not in {"analysis.py", "results.json", "source-manifest.json", "public-tables.csv"}, "Protected output filename")
    private.mkdir(parents=True, exist_ok=True, mode=0o700)
    private.chmod(0o700)
    require(summary_path.parent.is_dir(), "Summary output directory must already exist")

    protected = {name: sha256(HERE / name) for name in
                 ("analysis.py", "results.json", "source-manifest.json", "public-tables.csv", "PROTOCOL.md") if (HERE / name).exists()}
    manifest = json.loads((HERE / "source-manifest.json").read_text())
    original = json.loads((HERE / "results.json").read_text())
    pins = []
    for source in manifest["source_files"]:
        path = cache / source["filename"]
        digest = sha256(path)
        require(digest == source["sha256"], "Source hash mismatch: " + source["filename"])
        require(path.stat().st_size == source["bytes"], "Source size mismatch: " + source["filename"])
        pins.append({"filename": source["filename"], "sha256": digest, "matches_pin": True})
    print("Five source hashes verified. Reconstructing the original unpaid-work targets.", flush=True)

    d = pd.read_sas(cache / "cswc2024_2025_pumf.sas7bdat", encoding="utf8")
    b = pd.read_sas(cache / "cswc2024_2025_pumf_bsw.sas7bdat", encoding="utf8")
    require(len(d) == len(b) == 23314, "Unexpected source row count")
    require(d.PUMFID.notna().all() and b.PUMFID.notna().all() and d.PUMFID.is_unique and b.PUMFID.is_unique,
            "Incomplete or nonunique source keys")
    require(set(d.PUMFID) == set(b.PUMFID), "Source key sets differ")
    b = b.set_index("PUMFID").loc[d.PUMFID]
    require(np.array_equal(b.index.to_numpy(), d.PUMFID.to_numpy()), "Weight alignment failed")
    replicate_names = [f"BSW{i}" for i in range(1, 1001)]
    require(set(replicate_names) == {x for x in b.columns if x.startswith("BSW")}, "Unexpected bootstrap columns")
    W = np.column_stack([d.CSWCWT.to_numpy(float), b[replicate_names].to_numpy(float)])
    require(np.isfinite(W).all() and (W >= 0).all() and (W[:, 0] > 0).all(), "Invalid survey weights")
    domains = {"COWMAIN3": {"1", "2", "3"}, "GENDER": {1.0, 2.0}, "G_AI_05A": {1.0, 2.0},
               "WTQ_45": {1.0, 2.0, 3.0, 4.0, 5.0}, "NOC7": {f"{i:02}" for i in range(8)}}
    for name, expected in domains.items():
        require(d[name].notna().all() and set(d[name].unique()) == expected, "Unexpected variable domain: " + name)
    keep = d.COWMAIN3.isin(["1", "2"]).to_numpy()
    d = d.loc[keep].reset_index(drop=True)
    W = W[keep]
    del b
    require(len(d) == 20538, "Unexpected employee count")
    groups = (d.GENDER.to_numpy(int) - 1) * 2 + (d.G_AI_05A.to_numpy() == 1).astype(int)
    require(np.bincount(groups).tolist() == [7993, 2224, 8080, 2241], "Unexpected group sizes")
    y = d.WTQ_45.isin([1, 2]).to_numpy(float)
    keys = d.NOC7.astype(str) + "|" + d.COWMAIN3.astype(str)
    strata = sorted(keys.unique())
    require(strata == [f"{i:02}|{j}" for i in range(8) for j in (1, 2)], "Expected all 16 fixed occupation/sector strata")

    # Axes: stratum, gender/use group, full weight followed by 1,000 replicates.
    den = np.zeros((16, 4, 1001))
    num = np.zeros_like(den)
    counts = np.zeros((16, 4), dtype=int)
    events = np.zeros_like(counts)
    for s, key in enumerate(strata):
        cell = keys.to_numpy() == key
        for g in range(4):
            mask = cell & (groups == g)
            counts[s, g] = int(mask.sum())
            events[s, g] = int(y[mask].sum())
            den[s, g] = W[mask].sum(axis=0)
            # Binary outcome: direct event-weight summation avoids BLAS-specific
            # floating-point status warnings without suppressing numerical checks.
            num[s, g] = W[mask & (y == 1)].sum(axis=0)
    del d, W, groups, y, keys
    require((counts > 0).all() and (den > 0).all(), "Unsupported stratum or zero bootstrap denominator")
    means = num / den
    target = den.sum(axis=1) / den.sum(axis=(0, 1))
    group_mix = den / den.sum(axis=0)[None, :, :]
    require(np.max(np.abs(target.sum(axis=0) - 1)) < TOLERANCE, "Pooled shares do not sum to one")
    require(np.max(np.abs(group_mix.sum(axis=0) - 1)) < TOLERANCE, "Group shares do not sum to one")
    raw_rates = num.sum(axis=0) / den.sum(axis=0)
    standardized_rates = (target[:, None, :] * means).sum(axis=0)
    raw_contributions = (SIGNS[None, :, None] * group_mix * means).sum(axis=1)
    std_contributions = (SIGNS[None, :, None] * target[:, None, :] * means).sum(axis=1)
    change_contributions = (SIGNS[None, :, None] * (target[:, None, :] - group_mix) * means).sum(axis=1)
    raw = (SIGNS[:, None] * raw_rates).sum(axis=0)
    standardized = (SIGNS[:, None] * standardized_rates).sum(axis=0)
    change = standardized - raw
    sum_errors = {
        "raw_contribution_sum": float(np.max(np.abs(raw_contributions.sum(axis=0) - raw))),
        "standardized_contribution_sum": float(np.max(np.abs(std_contributions.sum(axis=0) - standardized))),
        "change_contribution_sum": float(np.max(np.abs(change_contributions.sum(axis=0) - change))),
    }
    require(max(sum_errors.values()) < TOLERANCE, "Contribution accounting identity failed")
    reconciliation = []
    saved = original["common_composition"]["occupation_sector"]["outcomes"]["frequent"]
    for g in range(4):
        reconcile(raw_rates[g], original["raw"]["frequent"]["rates"][g], "raw_rate_" + str(g), reconciliation)
        reconcile(standardized_rates[g], saved["standardized_rates"][g], "common_rate_" + str(g), reconciliation)
    reconcile(raw, original["raw"]["frequent"]["interaction"], "raw_interaction", reconciliation)
    reconcile(standardized, saved["standardized_interaction"], "common_interaction", reconciliation)
    reconcile(change, saved["composition_change"], "composition_change", reconciliation)
    require(original["common_composition"]["occupation_sector"]["support"]["minimum_internal_group_cell_n"] == int(counts.min()),
            "Original support minimum differs")
    print("Original point estimates and bootstrap intervals reconciled. Checking all 16 deletions.", flush=True)

    deletion = {name: np.zeros((16, 1001)) for name in ("raw", "standardized", "composition_change", "standardized_minus_original", "composition_change_minus_original")}
    restricted_counts = counts.sum(axis=0)[None, :] - counts
    restricted_events = events.sum(axis=0)[None, :] - events
    deletion_quality = [grade(int(min(restricted_counts[s].min(), restricted_events[s].min()))) for s in range(16)]
    deletion_records = []
    for s, key in enumerate(strata):
        retain = np.arange(16) != s
        rd = den[retain]
        rn = num[retain]
        require((rd > 0).all(), "Zero retained component denominator")
        raw_s = (SIGNS[:, None] * (rn.sum(axis=0) / rd.sum(axis=0))).sum(axis=0)
        q_s = rd.sum(axis=1) / rd.sum(axis=(0, 1))
        std_rates_s = (q_s[:, None, :] * means[retain]).sum(axis=0)
        std_s = (SIGNS[:, None] * std_rates_s).sum(axis=0)
        diff_s = std_s - raw_s
        deletion["raw"][s] = raw_s
        deletion["standardized"][s] = std_s
        deletion["composition_change"][s] = diff_s
        deletion["standardized_minus_original"][s] = std_s - standardized
        deletion["composition_change_minus_original"][s] = diff_s - change
        # An independent algebraic route checks the renormalisation each replicate.
        shortcut_std = (SIGNS[:, None] * ((standardized_rates - target[s][None, :] * means[s]) / (1 - target[s])[None, :])).sum(axis=0)
        require(np.max(np.abs(shortcut_std - std_s)) < TOLERANCE, "Deletion reweighting identity failed")
        deletion_records.append({
            "omitted_stratum": key,
            "retained_n": int(restricted_counts[s].sum()),
            "retained_groups_n": restricted_counts[s].tolist(),
            "retained_events_n": restricted_events[s].tolist(),
            "retained_full_weight_share": float(1 - target[s, 0]),
            "aggregate_release_quality": deletion_quality[s],
            "statistics": {name: summarize(values[s]) for name, values in deletion.items()},
            "scope": "Same 15 retained strata for all four groups; pooled target and group shares recomputed in every replicate",
        })

    contribution_points = change_contributions[:, 0]
    abs_mass = float(np.abs(contribution_points).sum())
    require(abs_mass > 0, "Undefined absolute-contribution shares")
    abs_order = np.argsort(-np.abs(contribution_points), kind="stable")
    private_strata = []
    for s, key in enumerate(strata):
        private_strata.append({
            "stratum": key, "NOC7": key.split("|")[0], "COWMAIN3": key.split("|")[1],
            "pooled_target_share": float(target[s, 0]),
            "target_share_statistic": summarize(target[s]),
            "groups": [{"label": LABELS[g], "n": int(counts[s, g]), "events": int(events[s, g]),
                        "domain_quality": grade(counts[s, g]), "event_quality": grade(events[s, g]),
                        "conservative_release_quality": grade(min(counts[s, g], events[s, g])),
                        "weighted_group_share": float(group_mix[s, g, 0]),
                        "full_weight_denominator": float(den[s, g, 0]),
                        "minimum_replicate_denominator": float(den[s, g, 1:].min()),
                        "outcome_rate": summarize(means[s, g])} for g in range(4)],
            "raw_interaction_contribution": summarize(raw_contributions[s]),
            "standardized_interaction_contribution": summarize(std_contributions[s]),
            "change_contribution": summarize(change_contributions[s]),
            "share_of_absolute_change_contribution_mass": float(abs(contribution_points[s]) / abs_mass),
        })

    # Fixed source thresholds, not a search for an exclusion rule. Buckets overlap.
    support_buckets = []
    private_support_buckets = []
    for kind, support in (("domain", counts), ("outcome_event", events)):
        for threshold in THRESHOLDS:
            flagged = (support < threshold).any(axis=1)
            n_strata = int(flagged.sum())
            pooled_quality = grade(int(min(counts[flagged].sum(axis=0).min(), events[flagged].sum(axis=0).min()))) if n_strata else None
            target_quality = grade(int(min(counts.sum(), counts[flagged].sum()))) if n_strata else None
            # Singleton buckets could expose one stratum's contribution. Even if
            # large enough by aggregate count, release only existence/count.
            disclose = n_strata >= 2 and pooled_quality != "F"
            disclose_target = n_strata >= 2 and target_quality != "F"
            private_support_buckets.append({"criterion": kind + "_count_below_" + str(threshold),
                                            "strata": [strata[s] for s in np.flatnonzero(flagged)],
                                            "target_share": float(target[flagged, 0].sum()),
                                            "share_of_absolute_contribution_mass": float(np.abs(contribution_points[flagged]).sum() / abs_mass),
                                            "net_change_contribution": float(contribution_points[flagged].sum()),
                                            "pooled_groups_n": counts[flagged].sum(axis=0).tolist(),
                                            "pooled_groups_events_n": events[flagged].sum(axis=0).tolist()})
            bucket = {"criterion": kind + "_count_below_" + str(threshold), "strata_n": n_strata,
                      "pooled_outcome_quality": pooled_quality, "pooled_target_share_quality": target_quality,
                      "target_weight_percent": round_one(100 * target[flagged, 0].sum()) if disclose_target else (0.0 if not n_strata else None),
                      "share_of_absolute_contribution_mass_percent": round_one(100 * np.abs(contribution_points[flagged]).sum() / abs_mass) if disclose else (0.0 if not n_strata else None),
                      "net_change_contribution_pp": round_one(100 * contribution_points[flagged].sum()) if disclose else (0.0 if not n_strata else None),
                      "disclosure_note": "Pooled across multiple strata" if disclose else ("Empty bucket" if not n_strata else "Outcome contributions withheld: singleton or F-quality pooled outcome support; target mass separately graded as a pooled covariate proportion")}
            support_buckets.append(bucket)

    # No stratum name, label, per-stratum count, weight, rate or deletion estimate
    # leaves the private directory. Ranges below pool all 16 deletions.
    all_releasable = "F" not in deletion_quality
    deletion_summary = {}
    for name in ("raw", "standardized", "composition_change", "standardized_minus_original", "composition_change_minus_original"):
        points = deletion[name][:, 0]
        intervals = np.array([summarize(v)["interval_95"] for v in deletion[name]])
        deletion_summary[name] = {
            "point_range_pp": [round_one(100 * points.min()), round_one(100 * points.max())] if all_releasable else None,
            "positive_points_n": int((points > 0).sum()) if all_releasable else None,
            "negative_points_n": int((points < 0).sum()) if all_releasable else None,
            "interval_includes_zero_n": int(((intervals[:, 0] <= 0) & (intervals[:, 1] >= 0)).sum()) if all_releasable else None,
            "interval_excludes_zero_negative_n": int((intervals[:, 1] < 0).sum()) if all_releasable else None,
            "interval_excludes_zero_positive_n": int((intervals[:, 0] > 0).sum()) if all_releasable else None,
        }

    public = {
        "study": "E08", "diagnostic_date": "2026-10-09", "outcome": "Unpaid job work daily or several times a week",
        "status": "Bounded influence diagnostic; original national-target estimates unchanged",
        "population": "20,538 public/private reference-job employees, ages 15–69, CSWC 2024–2025, ten provinces",
        "gender_categories": LABELS,
        "fixed_strata": {"variables": ["NOC7", "COWMAIN3"], "strata_n": 16, "all_employee_records_retained_in_original": True},
        "source_checks": pins,
        "original_reconciliation": {"checks_n": len(reconciliation), "tolerance": TOLERANCE,
                                    "maximum_absolute_error": max(x["maximum_absolute_error"] for x in reconciliation),
                                    "all_passed": True},
        "accounting_check": {"all_1001_weight_sets_checked": True, "maximum_absolute_error": max(sum_errors.values()),
                             "formula": "C_s = sum_g a_g * (q_s - p_sg) * m_sg; sum_s C_s = common-mix minus raw contrast",
                             "interpretation": "Descriptive accounting under observed support, not an occupational causal decomposition"},
        "original_results": {"raw_gender_contrast": public_stat(raw), "common_mix_gender_contrast": public_stat(standardized),
                             "common_minus_raw_contrast": public_stat(change)},
        "support": {"original_minimum_component_n": int(counts.min()), "zero_component_bootstrap_denominators": int((den[:, :, 1:] <= 0).sum()),
                    "thin_support_buckets": support_buckets,
                    "interpretation": "Target mass counts each flagged stratum once. Buckets overlap and must not be added. Event-count criteria are a conservative study safeguard, not an additional source theorem."},
        "concentration": {"definition": "Absolute contribution divided by sum of absolute contributions across all 16 strata; not percent of net change explained",
                          "largest_absolute_contribution_share_percent": round_one(100 * np.abs(contribution_points[abs_order[0]]) / abs_mass),
                          "three_largest_absolute_contributions_share_percent": round_one(100 * np.abs(contribution_points[abs_order[:3]]).sum() / abs_mass),
                          "largest_contributor_all_four_domain_counts_at_least_150": bool((counts[abs_order[0]] >= 150).all()),
                          "largest_contributor_has_outcome_event_count_below_75": bool((events[abs_order[0]] < 75).any()),
                          "negative_contributions_n": int((contribution_points < 0).sum()),
                          "positive_contributions_n": int((contribution_points > 0).sum())},
        "leave_one_stratum_out": {"diagnostics_n": 16, "omission_rule": "Each stratum omitted once from all four groups; no selective exclusions",
                                  "target": "Each result describes its own remaining 15-stratum employee population, with newly pooled weights",
                                  "aggregate_quality_counts": {q: deletion_quality.count(q) for q in "AEF"},
                                  "all_pooled_results_pass_aggregate_release_threshold": all_releasable,
                                  "summary": deletion_summary,
                                  "warning": "Ranges are point-estimate diagnostics, not uncertainty intervals. Intervals are dependent, pointwise and not simultaneous. No deletion estimates replace the full-population estimate."},
        "uncertainty": {"public_bootstrap_replicates": 1000, "variance": "mean((T_b - T_full_target)^2)", "normal_multiplier": 1.96,
                        "centering": "Each original or restricted target's full-weight estimate; never its replicate mean",
                        "reestimated_per_replicate": ["group rates", "pooled target shares", "group-specific job shares", "all contrasts"],
                        "scope": "Sampling uncertainty conditional on observed support; not measurement error, confounding or general model uncertainty"},
        "disclosure": {"fine_cell_rates_released": False, "stratum_identities_released": False, "individual_deletion_estimates_released": False,
                       "respondent_rows_or_weights_written": False, "percentages_and_differences_decimals": 1,
                       "quality_rule": "A >=150; E 75–149; F <75; <5 expressly unacceptable. Worse domain/event grade is the conservative study release rule.",
                       "additional_safeguard": "Fine components remain private regardless of grade; singleton bucket quantities withheld. Target mass is graded on pooled covariate counts, separately from outcome-contribution support. Public deletions summarised only across all 16."},
        "reproducibility": {"script": "influence_check.py", "script_sha256": sha256(Path(__file__)), "python": platform.python_version(),
                            "numpy": np.__version__, "pandas": pd.__version__, "original_files_unchanged": True},
        "limitations": ["Sparse components remain in both original and restricted pooled estimates.",
                        "A one-stratum deletion cannot assess all simultaneous component influences or all alternative specifications.",
                        "Thin support and large influence are distinct; a large contribution need not come from the thinnest cell.",
                        "No causal effect of AI or occupation, no equivalence conclusion and no new national estimator is identified."],
    }
    private_output = {"classification": "PRIVATE: disclosive fine-cell aggregates; never serve or publish",
                      "source_checks": pins, "reconciliation": reconciliation, "accounting_errors": sum_errors,
                      "original": {"raw": summarize(raw), "standardized": summarize(standardized), "change": summarize(change)},
                      "strata": private_strata, "support_buckets": private_support_buckets,
                      "all_stratum_deletions": deletion_records}
    write_json(private / "diagnostics-private.json", private_output, private=True)
    arrays_path = private / "replicate-diagnostics-private.npz"
    fd = os.open(arrays_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "wb") as stream:
        np.savez_compressed(stream, strata=np.array(strata), target_shares=target, group_shares=group_mix,
                            cell_rates=means, raw_contributions=raw_contributions, standardized_contributions=std_contributions,
                            change_contributions=change_contributions, **{"deletion_" + k: v for k, v in deletion.items()})
    arrays_path.chmod(0o600)
    for name, digest in protected.items():
        require(sha256(HERE / name) == digest, "Protected file changed during execution: " + name)
    write_json(summary_path, public)
    print("Completed: safe influence summary and private aggregate diagnostics. No raw rows or weights written.", flush=True)


if __name__ == "__main__":
    main()
