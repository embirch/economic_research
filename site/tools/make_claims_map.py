#!/usr/bin/env python3
"""Editor's tool: build posts/post1/notes/claims-map.json from POST.md.

Every quantitative sentence of POST.md is listed here with the claims.md
sentence id it is written under and the results.json key(s) it is bound to.
The values are read out of results.json at generation time so that the map
records what the numbers were; verify_page.py then fails if results.json and
the map ever drift apart.
"""
import json, re, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
ROOT = "/workspace/economic_research"
sys.path.insert(0, os.path.join(ROOT, "site", "tools"))
import verify_page as V  # noqa: E402

POST = "post1"
post_dir = os.path.join(ROOT, "posts", POST)
results = json.loads(V.read(os.path.join(post_dir, "data", "processed", "results.json")))
md = V.read(os.path.join(post_dir, "POST.md"))

W = ["aug2025", "nov2025", "feb2026"]


def k(*parts):
    return list(parts)


def d(tmpl, waves=W):
    return [tmpl.format(w=w) for w in waves]


def flat(*groups):
    out = []
    for g in groups:
        out += g if isinstance(g, list) else [g]
    return out


CONV = "facts.conventions_and_constants"

# Each quantitative sentence of POST.md is matched by a unique anchor, so that
# editing the prose around a sentence cannot silently re-point its bindings.
#   anchor -> (claims.md sentence id(s), [results.json keys], [as_printed])
SPEC = [
 ("| Explanation | What it says", "2, 16, and the pre-registered margin",
  ["facts.declared_owner.value", "facts.H3_declaration.value",
   "facts.H1_signature_clause.value", CONV + ".delta_pp"], []),
 ("The shares themselves are not monotone", "11", flat(
   d("tests.desc_quartile_shares_{w}.estimates.Q1.coef"),
   d("tests.desc_quartile_shares_{w}.estimates.Q2.coef"),
   d("tests.desc_quartile_shares_{w}.estimates.Q3.coef"),
   d("tests.desc_quartile_shares_{w}.estimates.Q4.coef"),
   d("tests.desc_quartile_shares_{w}.estimates.Q1.none_share"),
   d("tests.desc_quartile_shares_{w}.estimates.Q2.none_share"),
   d("tests.desc_quartile_shares_{w}.estimates.Q3.none_share"),
   d("tests.desc_quartile_shares_{w}.estimates.Q4.none_share")), []),
 ("In each of the three Claude.ai windows the automation share", "1 and 5", flat(
   d("tests.D_{w}.estimates.D.coef"), d("tests.D_{w}.estimates.D.ci"),
   [CONV + ".percent_signs", CONV + ".z_two_sided_95"]), []),
 ("On the corrected quartile rule", "3",
  d("tests.D_{w}.estimates.D_corrected_quartile_rule.coef"), []),
 ("Tasks are sorted into usage-weighted wage quartiles",
  "Figure 1 caption: the construction", [CONV + ".hours_per_year"], []),
 ("Sample: the 1,802", "24 and 25 (Figure 1 caption)", flat(
   d("facts.sample_{w}.value"), d("facts.sample_{w}.analysis_share_named"),
   d("facts.sample_{w}.classified_conversations"), d("facts.kish_{w}.value"),
   d("facts.sample_{w}.dropped_wage_no_classified_cell"),
   d("facts.sample_{w}.dropped_classified_cell_no_wage")), []),
 ("Bars are two-sided 95% intervals from a conversation-level binomial with the task mix held fixed; no release",
  "5 (Figure 1 caption)", [CONV + ".percent_signs"], []),
 ("The shaded band is the pre-registered indifference region",
  "the pre-registered margin (Figure 1 caption)", [CONV + ".delta_pp"], []),
 ("Read as a statement about tasks rather than about these windows' conversations, a task-resampling",
  "7 (Figure 1 caption)", ["facts.generalisation_sentence.realised_mde_by_wave"], []),
 ("Under the modal-holder wage rule", "9",
  ["tests.rob_W1_modal_holder_feb2026.estimates.D.coef",
   "tests.rob_W1_modal_holder_feb2026.estimates.D.ci",
   "facts.owner_under_robustness.owners.W1_modal_holder",
   "facts.owner_under_robustness.points.W1_equal_split"], []),
 ("Dropping the 23 November tasks", "8",
  ["tests.rob_X5_drop_sc_over_10pc_nov2025.estimates.D.coef",
   "tests.rob_X4_sc_netted_weights_nov2025.estimates.D.coef",
   "facts.november_is_corroborated_not_independent.value"], []),
 ("Those 23 tasks include", "8 (the bound on attribution)", flat(
   d("facts.composition_of_the_top_quartile.largest_software_tasks.{w}.q4_mass_first"),
   ["facts.composition_of_the_top_quartile.largest_software_tasks.nov2025.q4_mass_total"]), []),
 ("Counting every Seychelles conversation", "8 (the Seychelles worst case)",
  ["facts.seychelles_worst_case_bound.D_worst_case"], []),
 ("In the other direction, dropping tasks", "10",
  d("tests.rob_X3_drop_under_100_classified_{w}.estimates.D.coef"), []),
 ("The third quartile boundary is $43.40 an hour", "4", flat(
   ["facts.quartile_boundaries_aug2025.value"],
   d('facts.quartile_boundaries_{w}.boundary_tie_mass."b3_43.40".tasks'),
   d('facts.quartile_boundaries_{w}.boundary_tie_mass."b3_43.40".mass')), []),
 ("And the top quartile is small where it counts", "25",
  flat(d("facts.kish_{w}.value"), d("facts.kish_{w}.by_quartile[3]")), []),
 ("The continuous slope of the automation share", "12", flat(
   d("tests.slope_{w}.estimates.slope.coef"),
   ["tests.slope_aug2025.estimates.slope.mde", CONV + ".percent_signs"]), []),
 ("Bars are two-sided 95% intervals from a conversation-level binomial with the task mix held fixed and are a lower bound",
  "5 (Figure 2 caption)", [CONV + ".percent_signs"], []),
 ("The excess is carried by Computer & Mathematical tasks", "13",
  flat(d("tests.leg_a_{w}.coverage.dropped_share_q4"),
       d("tests.leg_a_{w}.coverage.dropped_share_analysis")), []),
 ("With Computer & Mathematical tasks excluded", "14 and 31", flat(
   d("tests.leg_a_{w}.estimates.D_L.coef"),
   d("facts.composition_of_the_top_quartile.residual_after_soc15_exclusion.{w}.q4_mass")), []),
 ("The leave-one-group-out series is the same evidence", "17", flat(
   d("tests.desc_leave_one_group_out_{w}.estimates.leave_out_15.move"),
   d("tests.desc_leave_one_group_out_{w}.estimates.leave_out_43.move")), []),
 ("Within SOC major group \u2014", "15 and 18", flat(
   d("tests.leg_b_{w}.estimates.D_L.coef"),
   d("tests.leg_b_{w}.coverage.identified_mass_share_q1_q4"),
   d("tests.desc_ten_largest_out_{w}.estimates.D.coef")), []),
 ("Leg (a) removes the tasks assigned", "13 (Figure 3 caption)", flat(
   d("tests.leg_a_{w}.coverage.dropped_share_analysis"),
   d("tests.leg_a_{w}.coverage.dropped_share_q4"),
   [CONV + ".soc_computer_and_mathematical"]), []),
 ("Leg (e) keeps the tasks whose", "19 (Figure 3 caption)", flat(
   d("tests.leg_e_{w}.coverage.kept_tasks", W[1:]),
   d("tests.leg_e_{w}.coverage.undefined_tasks_analysis", W[1:])), []),
 ("Bars are two-sided 95% intervals on the same conversation-level binomial model as Figure 1",
  "5 (Figure 3 caption)", [CONV + ".percent_signs"], []),
 ("Restricting to work-dominant tasks", "19", flat(
   d("tests.leg_e_{w}.coverage.kept_tasks", W[1:]),
   d("tests.leg_e_{w}.estimates.D_L.coef", W[1:]),
   ["tests.leg_e_nov2025.estimates.r_L.coef"],
   d("tests.leg_e_{w}.coverage.kept_share_q4", W[1:]),
   d("tests.leg_e_{w}.coverage.kept_share_q1", W[1:])), []),
 ("The mix it is drawn from is stark", "20", flat(
   d("tests.desc_use_case_mix_{w}.estimates.Q1_work.coef", W[1:]),
   d("tests.desc_use_case_mix_{w}.estimates.Q4_work.coef", W[1:]),
   d("tests.desc_use_case_mix_{w}.estimates.Q1_personal.coef", W[1:])), []),
 ("One exploratory reading is recorded", "28 (exploratory)", flat(
   d("tests.exp_b_pattern_split.estimates.directive_{w}.coef"),
   d("tests.exp_b_pattern_split.estimates.feedback loop_{w}.coef")), []),
 ("Weighting the published automation share by the hourly wage", "22",
  d("tests.DeltaW_{w}.estimates.Delta_W.coef"), []),
 ("August's null is a tight one", "22 (the MDE beside the null)",
  ["tests.DeltaW_aug2025.estimates.Delta_W.mde"], []),
 ("In levels:", "23", flat(d("tests.DeltaW_{w}.estimates.unweighted_share.coef"),
                           d("tests.DeltaW_{w}.estimates.wage_weighted_share.coef")), []),
 ("Bars are two-sided 95% intervals on the conversation-level binomial model and are a lower bound",
  "5 (Figure 4 caption)", [CONV + ".percent_signs"], []),
 ("The top quartile's effective size, and the threshold", "25 and 4 (limitation 4)", flat(
   d("facts.kish_{w}.by_quartile[3]"),
   d("facts.quartile_boundaries_{w}.q4_mass_from_boundary_tie")), []),
 ("The generalisation bound.", "7 (limitation 9)",
  ["facts.generalisation_sentence.realised_mde_by_wave"], []),
 ("Tasks are priced through the shipped", "the construction constants",
  [CONV + ".hours_per_year", CONV + ".source_check"], []),
 ("Analysis set: the 1,802", "24 and 25", flat(
   d("facts.sample_{w}.value"), d("facts.sample_{w}.analysis_share_named"),
   d("facts.sample_{w}.classified_conversations"), d("facts.kish_{w}.value"),
   d("facts.sample_{w}.dropped_wage_no_classified_cell"),
   d("facts.sample_{w}.dropped_classified_cell_no_wage")), []),
 ("D and the composition legs are estimated", "5", [CONV + ".percent_signs"], []),
 ("Every confirmatory quantity is produced twice", "27",
  ["facts.second_implementation_agreement.value",
   "facts.second_implementation_agreement.bootstrap_vs_closed_form_max_rel",
   "facts.second_implementation_agreement.bootstrap_coverage"], ["1.8", "0.9"]),
 ("Each wave's own five-pattern automation share reproduces", "26", flat(
   d("facts.replication_{w}.value"),
   ["facts.fig211_released_library.value", "facts.fig211_released_library.partial_r2",
    "facts.fig211_released_library.n_countries", "facts.replication_aug2025.source_check"]), []),
 ("The confirmatory set was named and counted", "the confirmatory count",
  ["counts.confirmatory_estimates", "counts.leg_tests", "counts.exploratory_tests"], []),
 ("The assumed effect and its provenance", "1 (the MDE) and the registered margin",
  flat(d("facts.mde_{w}.value"), [CONV + ".delta_pp", CONV + ".percent_signs"]), []),
 ("The separate materiality line", "the brief's materiality line",
  [CONV + ".materiality_pp_of_delta_w_per_point_of_gap"], []),
 ("The quartile rule at the $43.40 wage mass point.", "4 (deviation 1)",
  ["facts.quartile_boundaries_aug2025.value"], []),
 ("The permutation placebo's size band", "deviation 3",
  [CONV + ".delta_pp",
   "facts.composition_of_the_top_quartile.largest_software_tasks.aug2025.tasks_matching_first"], []),
]


def block_sections(md_text):
    """(normalised block text, the H2 it sits under) for every block of POST.md."""
    out, sec, buf = [], None, []
    for line in md_text.split("\n"):
        if line.startswith("## "):
            if buf:
                out.append((V.normalise(" ".join(buf)), sec))
                buf = []
            sec = line[3:].strip()
            continue
        if not line.strip():
            if buf:
                out.append((V.normalise(" ".join(buf)), sec))
                buf = []
            continue
        buf.append(line)
    if buf:
        out.append((V.normalise(" ".join(buf)), sec))
    return out


BLOCKS = block_sections(md)


def section_of(sent):
    n = V.normalise(sent)
    hits = [sec for text, sec in BLOCKS if n in text]
    if len(hits) != 1:
        sys.exit(f"sentence sits in {len(hits)} blocks: {sent[:100]}")
    return hits[0]


quant = [s for s in V.sentences(md) if V.numbers_in(s)]
claims, used = [], set()
for i, sent in enumerate(quant, start=1):
    hits = [j for j, (anchor, *_ ) in enumerate(SPEC) if anchor in sent]
    if len(hits) != 1:
        sys.exit(f"sentence {i} matches {len(hits)} anchors: {sent[:120]}")
    j = hits[0]
    if j in used:
        sys.exit(f"anchor {SPEC[j][0]!r} matches more than one sentence")
    used.add(j)
    _, cid, keys, printed = SPEC[j]
    bindings = []
    for key in keys:
        val = V.resolve(results, key)
        if isinstance(val, float):
            val = round(val, 6)
        elif isinstance(val, list):
            val = [round(v, 6) if isinstance(v, float) else v for v in val]
        b = {"key": key, "value": val}
        if printed:
            b["as_printed"] = printed
            printed = []
        bindings.append(b)
    claims.append({
        "id": f"S{i:02d}",
        "claims_md": cid,
        "section": section_of(sent),
        "sentence": sent,
        "bindings": bindings,
    })
missing = [SPEC[j][0] for j in range(len(SPEC)) if j not in used]
if missing:
    sys.exit("anchors that matched no sentence: " + "; ".join(missing))

out = {
    "post": POST,
    "post_md": "posts/post1/POST.md",
    "results": "posts/post1/data/processed/results.json",
    "claims_list": "posts/post1/notes/claims.md",
    "note": ("Every quantitative sentence in POST.md, the claims.md sentence it is written "
             "under, and the results.json key(s) and value(s) it is bound to. `as_printed` "
             "records a rounding the sentence prints that is not a plain rounding of the "
             "stored value (a mantissa, or a ratio printed as a percentage). Generated by "
             "site/tools/make_claims_map.py; checked by site/tools/verify_page.py."),
    "claims": claims,
}
with open(os.path.join(post_dir, "notes", "claims-map.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
print(f"wrote claims-map.json: {len(claims)} sentences, "
       f"{sum(len(c['bindings']) for c in claims)} bindings")
