# Referee verdict · post1 (LL-07) · results · 2026-09-17

Reviewed against `posts/post1/prereg/prereg.md` (content `c9b1b45`, committed `066b761`), `BRIEF.md` §6, §9, §12
(`8fbffbd`), `data/processed/results.json` (generated 2026-09-17T12:14:35Z, 60 test entries, 29 facts, 4 figures),
`notes/lab-notebook.md`, `scripts/02_…09_…py` and `outputs/checks/*.out.txt`, `outputs/figures.json` and the four
PNGs, `notes/feasibility.md` §1 and §7, `notes/replication.md` §1, and my own `notes/referee-prereg.md` (carried items
10 and 15(c)). Room notes to me: four, all `needs-reply: no`, recorded in `room/referee-answered.txt`. No room notes
between analyst and director on interpretation were read. `reference/` not opened.

## Verdict

**PASS WITH CHANGES.** Zero blocking items. Every headline number re-derives from the raw cache files with my own
code to 3e-14 pp or better; the declared owner (**O-A**) and the H3 declaration (**declared**, legs (a) and (b) firing
in every wave) follow mechanically from the registered rules and reproduce on my own intervals; the four deviations
are legitimate mis-specifications with the registered rule run beside the corrected one; 17 confirmatory + 3
exploratory tests were run and nothing unregistered was run as a test. The changes below (items 6–18) are exact and
clerical — two caption numbers that do not match the data, one garbled caption sentence, one notebook
mis-transcription, one registered side-estimate that was not computed, one incomplete characterisation of the second
wage source that the post's P6 sentence depends on, and two mechanical verdict strings — and the analyst applies them
without a further round. The draft review will check that each landed.

What the results say, in one paragraph, so the items below have a frame: on the registered rule D = +1.38 / +7.39 /
+0.67 pp (Aug / Nov / Feb), every interval positive and excluding zero, Feb not clearing +1 pp → **O-A**. Q4 is
65–73% Computer & Mathematical by usage mass, three software tasks carry 39–54% of it, and its Kish effective N is
8.9–16.4 tasks. With SOC-15 excluded the sign reverses in every wave (−13.0 / −10.5 / −11.9 pp); within major group it
is negative in every wave (−4.2 / −1.9 / −6.2 pp); within SOC-15 alone there is no gradient (−0.1 / +6.5 / +0.8 pp).
The `directive` pattern alone runs the other way in every wave (exploratory). Δ_W = −0.02 (contains zero) / +0.84 /
−0.15 pp. The between-window SD of D (3.7 pp) is 26× its within-window SE (0.14 pp), so the O-A label's "persistent"
is about the sign only.

## Items

**1. Re-derivation of the headline numbers — match.** `notes/rederivation/referee_results_post1.py` rebuilds, from the
three raw wave CSVs, `onet_task_statements.csv`, `wage_data.csv`, the BLS-EP HTML and the O\*NET crosswalk, with no
import from the analyst's scripts: the analysis set (1,802 / 2,075 / 2,188 tasks, 89.2530 / 89.9892 / 89.7348 pp,
818,673 / 854,432 / 848,716 classified conversations), the employment-weighted wage, the usage-weighted quartiles
(bounds $25.78 / $35.56 / $43.40; $25.78 / $34.87 / $43.40; $24.00 / $34.45 / $43.40), p_i, n_i, D with its P1
interval, Δ_W, leg (a), leg (e) and — in the supplement — leg (b). Every number matches `results.json` to ≤ 2.5e-14 pp
and every SE to ≤ 3e-17. Table in the section below. **No change.**

**2. The §9(1) chain and the H3 rule, applied by me.** On the analyst's three intervals [1.10, 1.67], [7.11, 7.66],
[0.39, 0.94]: step (1) fails (Feb lower bound 0.39 < 1), step (2) fails, step (3) holds (all three exclude zero,
positive) → **O-A**. Same on my own intervals. Leg (a) fires on sign in 3 of 3 waves; leg (b) fires on sign in 3 of 3;
leg (e) does not fire in 2 of 2 → persistent-leg rule declares **H3** on legs (a) and (b); the literal any-wave rule
agrees. H1's own signature clause fails in every wave. All as `facts.declared_owner`, `facts.H3_declaration`,
`facts.H1_signature_clause` state. **No change.**

**3. DEVIATION 1 (quartile rule at the $43.40 mass point) — legitimate.** The registered sentence does not define Q4
when a single wage value straddles the 0.75 cut, and the value that does is "Computer Occupations, All Other"
(`15-1199.xx`, MedianSalary $90,270 → $43.40/hr: 99 / 106 / 111 tasks, 10.60 / 8.36 / 7.95 pp of the wave, 7.3 / 4.9
/ 6.1 pp of Q4's 22.5 pp). The registered rule was run (tie order fixed on (wage, task text)) and declares the owner;
the fractional rule was run beside it (D = +0.54 / +7.18 / +0.34; owner O-A under both). Necessary, not a choice:
the steward's earlier unstable sort gave a different Q4 (431 / 480 / 496 tasks against 360 / 403 / 482). Two
consequences the post must carry, bound in `claims.md`: (i) August's "clears +1 pp" is a property of the tie order
— under the fractional rule August is +0.54 [+0.27, +0.82] and does not clear; (ii) the tie sits *inside* the coding
family, so which computer tasks land in Q4 is what the two readings differ on. **Should (exact):** add
`facts.quartile_boundaries_<wave>.boundary_occupation = "15-1199 Computer Occupations, All Other ($90,270 ÷ 2,080 =
$43.40/hr)"` so the post can name it.

**4. DEVIATION 2 (P6's 2% SE tolerance on r_L → 25%; the linear contrast D_L − ½D asserted at 2%) — legitimate.** A
ratio with a denominator of 0.67 pp has a heavy-tailed sampling distribution; the delta method understates the
bootstrap SE by 5–21%. The declaration is on point estimates, so nothing moves. This is exactly my carried item 10;
**resolved**: the half judgement is read from D_L − ½D, r_L is descriptive and its unit string names the
instability. **No change.**

**5. DEVIATION 3 (permutation size band ±1 pp → ±2 pp at 1,500 trials) — legitimate, but the cheaper fix was more
trials.** Monte Carlo SE at 1,500 trials is 0.6 pp; a ±1 pp band fails by chance about 10% of the time. Realised size
4.93%. The placebo is in no decision rule. **Could:** 10,000 trials would have kept the registered band.

**6. CORRECTION entries — all three sound; a fourth mis-transcription remains uncorrected.** The A2 fallback fix
matches the brief's stated rule and my independent A2 implementation (leg (a) drop mass 42.84 / 39.65 / 35.55%
reproduces). JobZone's frame is exploratory only. The SOC-15 mass figures were corrected. **But** the `05_legs.py`
notebook entry says "9 / 9 / 9 identified groups carrying 71–76% of Q1+Q4 mass" and the close's open question (ii)
repeats "9 / 9 / 9"; `results.json` and `05_legs.out.txt` have **10 / 10 / 9** groups carrying **80.0 / 80.3 / 75.5%**
(my re-derivation agrees: 10 / 10 / 9). **Should:** a dated CORRECTION entry in `notes/lab-notebook.md`.

**7. Figure 3 caption does not match the plotted data.** "over the nine major groups … the other thirteen groups" is
Feb only; Aug and Nov have ten identified and twelve not. **Should (exact):** "over the ten (August, November) or
nine (February) major groups that hold analysis-set tasks in both the global bottom and the global top quartile,
each group weighted by its usage mass in those two quartiles; the other twelve or thirteen groups are reported as not
identified, never as zeros." The word-number slipped past the script-09 verifier, which checks numerals only.

**8. Figure 4 caption misstates February.** "moves it by less than a tenth of a point in two windows and by eight
tenths in the third": Δ_W is −0.022 (Aug), +0.835 (Nov), **−0.147 (Feb)** — February is not "less than a tenth".
**Should (exact):** "**Weighting the published automation share by the wage of the work moves it by less than a
fifth of a point in two windows and by eight tenths of a point in the third, and not in the same direction as the
quartile gap in two of the three.**"

**9. Figure 1 caption's bold sentence is garbled.** "and in none of them does the difference clear a percentage
point in every window" — August and November each clear +1 pp on the registered rule; February does not.
**Should (exact):** "**In all three Claude.ai windows the delegated share is higher on top-quartile than on
bottom-quartile tasks; the difference clears a percentage point in two windows on the pre-registered quartile rule
and in none once the boundary wage is shared, and it does not clear a point in every window under either rule.**"

**10. The second wage source is the SOC-15 exclusion in disguise, and `results.json` does not say so.** BLS-EP is
keyed on SOC-2018 and does not price the renumbered computer family. My re-derivation: C7 prices **10.9 / 10.5 /
11.6%** of SOC-15 analysis mass and **26.4 / 27.7 / 31.8%** of Q4 mass; SOC-15 is **7.6 / 6.4 / 5.9%** of the
C7-priced Q4 (8.5 / 7.0 / 6.3% after the C7 quartiles are re-drawn) against 73.1 / 71.3 / 65.5% of the C6 Q4.
`robustness.json` confirms it from the other side: leg (a) under C7 retains r = 0.97 / 0.93 / 0.98 of C7's D —
removing SOC-15 from the C7 frame changes almost nothing because it is already gone. So `rob_C7_*`'s D of −15.6 /
−11.9 / −16.7 is not an independent failure of sign agreement on a second source; it is leg (a) again on 55–62% of
the mass. The current verdict string ("C7's coverage … is the reason it is not decisive") is true but hides the
mechanism, and the prereg's P6 first-sentence rule would put a misleading sentence in the post. **Should (exact):**
add to `facts.C7_sign_agreement`: `c7_share_of_soc15_analysis_mass: [10.9, 10.5, 11.6]`,
`c7_share_of_q4_mass: [26.4, 27.7, 31.8]`, `soc15_share_of_c7_priced_q4: [7.6, 6.4, 5.9]`,
`c7_leg_a_retained_fraction: [0.9685, 0.9267, 0.9811]` (from `robustness.json`), and amend the `rob_C7_*` verdict
to: "the sign does NOT agree with C6 in this window; BLS-EP (SOC-2018) does not price the renumbered computer
occupations, so C7's top quartile is 92–94% non-coding and this rebuild is the Computer & Mathematical exclusion of
leg (a) on 55–62% of the mass, not an independent second source; the owner is unchanged." The analyst verifies the
four triples from the build table.

**11. A registered side-estimate was not computed.** P3(b): "the primary identified set is the 10 / 10 / 8 groups,
with the 7 / 8 / 6 all-four subset reported beside it in every table; both go into `results.json`." `legs.json`
lists the all-four groups (8 / 9 / 8) but carries no D_(b) on that subset. My supplement computes it: **−4.0541
[−4.5703, −3.5379] / −1.7940 [−2.3520, −1.2361] / −6.0851 [−6.5615, −5.6087]** pp — the leg fires on sign under both
readings, so nothing moves. **Should:** add `D_L_all_four_subset` to the three `leg_b_*` entries (coef, ci, se) and
one line in the notebook; or log the omission as a deviation.

**12. Numbers the post might cite that are not in `results.json`.** X7 (inert for D; wave share 51.2001 → 51.7424),
the A1 allocation variants of leg (a) (−13.71 / −14.07; −11.08 / −11.40; −12.37 / −12.62) and leg (b), the C7 legs,
leg (e) on the substantive-cell denominator (+3.85 / +2.74), the 2010-grouping leg table, and the leg-(e) work-share
gradient 32.80 → 60.82 / 29.05 → 60.54 (the last is in `desc_use_case_mix`). They live in `robustness.json` /
`legs.json` only. **Could:** add as `rob_A1_*`, `rob_C7_legs_*`, `rob_leg_e_substantive_*` entries; until then
`claims.md` forbids citing them. The same applies to four referee-derived figures the claims list leans on and the
post may want: the two "modify existing software to correct errors…" tasks' share of Q4 (6.53 / 8.54 / 5.98 pp;
11.40 / 12.21 / 8.83 pp with "write new programs or modify existing programs…" as the third), the within-SOC-15 top-minus-bottom
contrast (−0.14 / +6.47 / +0.80 pp), the residual Q4 after SOC-15 exclusion (286 / 327 / 355 tasks, 6.10 / 6.47 /
7.77 pp, Kish 98 / 86 / 83, p 38.7 / 34.8 / 36.0 against Q1-residual p 51.7 / 45.2 / 47.9) and the November
Seychelles worst-case bound (+4.50 pp). All are in `referee_results_post1_supplement.out.txt`; the analyst
reproduces from the build table and adds them as facts if the post cites them.

**13. Δ_W verdict string, August.** "contains zero; … so the weighting of a published automation share is **signed**
and small, never wrong" — an interval containing zero is not signed. **Should (exact):** for any Δ_W whose interval
contains zero, "contains zero; |Δ_W| = … pp, below the separate 1 pp materiality line, so the weighting of a
published automation share is small and, in this window, of undetermined sign."

**14. Leg (e) verdict string, November.** "nothing bigger than the MDE of 0.6058 pp is shown on this leg" is the
wrong null sentence: D_L is +3.72 ± 0.22 pp; what is undetermined is whether it retains more or less than half of D
(r = 0.503; D_L − ½D = +0.02 [−0.33, +0.37] pp). **Should (exact):** "did not fire on the point estimate; D_L
retains 0.50 of D and the contrast D_L − ½D is +0.02 [−0.33, +0.37] pp, so whether the work-dominant set retains
more or less than half of D is undetermined at this precision; not composition excluded."

**15. Two check-block assertions are on results rather than facts.** `03_headline.py` L357 asserts |Δ_W| <
max(1, ½|D|); `05_legs.py` L476 asserts SOC-15 is the largest leave-one-out mover. Both encode pre-registered
expectations and both passed, but a failure would have been a finding, not a bug, and would have stopped the
pipeline. **Could:** print, don't assert.

**16. SE and MDE absent on some citable estimates.** `exp_a_api_surface` slopes and every `rob_*` Δ_W carry a `ci`
but no `se`/`mde`; `exp_c_jobzone` D's likewise. **Could:** add before the draft if any is cited; empirical
standard 6.

**17. Carried item 15(c) — resolved by the data, and the post must say it.** P2's power figures assume a constant
true D across waves. The realised D's are 1.38 / 7.39 / 0.67 pp: SD 3.69 pp against a mean SE of 0.142 pp (26×).
The constant-D assumption is falsified, so none of the P2 probabilities (O-A ≈ 1.00 near 1 pp; O-B 0.043 at 0.5 pp)
is the probability of this outcome, and no probability under a non-constant D has been computed. **Should:** one
line in `facts.rule_power.notes` to that effect; the wording is bound in `claims.md`.

**18. The generalisation sentence must carry the realised bound.** Prereg: "resolves nothing below about twelve
points" (MDE 12.5 / 17.4 / 16.1). Realised model (b) MDE **14.1 / 20.2 / 16.1 pp** (`rob_model_b_*`,
`facts.generalisation_sentence` = 20.16). Figure 1's caption already says "about 14 to 20". **Should:** the post's
sentence reads "about fourteen to twenty points", never "twelve".

**19. Tests run against tests registered — as registered.** 17 confirmatory (3 D, 3 Δ_W, 3 slope, 3 leg (a), 3 leg
(b), 2 leg (e)); 3 exploratory (with 6 + 15 + 6 sub-estimates); 24 robustness entries = X3 ×3, X4, X5 (>10%, >20%),
W1 equal-split ×3, W1 modal ×3, C7 ×3, model (b) ×3, placebo ×3, fourth window ×3 — the prereg's "Robustness, fixed
now" list exactly (X7 and the A1 variants are in `robustness.json`, item 12); 16 descriptive entries (quartile shares
×3, pattern shares ×3, leave-one-group-out ×3, ten-largest-out ×3, use-case mix ×2, slope with work share ×2). The
only additional reported reading is `D_corrected_quartile_rule`, the logged deviation. **No unregistered test.**
Multiple-testing exposure: the owner is one ordered rule on three intervals; H3 is one rule on eight leg tests, each
firing on a sign reversal of 2–13 pp at SEs of 0.2–0.3; the exploratory sub-estimates are 27, none in a headline.

**20. Two implementations, synthetic recovery, MDEs, checks.** Script 04 rebuilds p_i from `_pct`, w_i from
`onet_task_count`, the wage from the SOC side and the quartiles by lexsort; agreement 1.8e-14 pp; bootstrap SEs
within 0.9% of closed form, coverage 95.2–95.3%. It shares the loader, the `::` split, the crosswalk and the A2
function with 02, so leg (a)'s exclusion set is not independently implemented there — my own A2 covers it (item 1).
The eight recoveries pass (D coverage 94.4–95.4% at gaps 0 / 0.5 / 1 / 3; Δ_W and slope to 1e-14; leg (b) returns
the within-group +0.17 against a total gap of +16.2; leg (e) drops the only-`not_classified` tasks; permutation size
4.93%; Kish exact). MDE = 2.8 × SE beside every confirmatory coefficient; the two nulls in the confirmatory set (Aug
slope, Aug Δ_W) carry theirs. All nine check blocks pass on a clean re-run (notebook close). **No change.**

## Independent re-derivations

Code: `posts/post1/notes/rederivation/referee_results_post1.py` (headline) and
`referee_results_post1_supplement.py` (leg (b), composition, the Seychelles bound); outputs `*.out.txt` beside them.

| quantity | wave | analyst (`results.json`) | mine | match |
|---|---|---|---|---|
| D, registered rule | Aug | +1.3836 [+1.1006, +1.6667], SE 0.1444 | +1.3836 [+1.1006, +1.6667], SE 0.1444 | 6.7e-16 pp |
| D, registered rule | Nov | +7.3854 [+7.1103, +7.6605], SE 0.1404 | same | 0 |
| D, registered rule | Feb | +0.6689 [+0.3947, +0.9431], SE 0.1399 | same | 2.5e-14 pp |
| D, fractional rule | Aug / Nov / Feb | +0.5434 / +7.1793 / +0.3387 | same | ≤ 2.2e-14 |
| Δ_W | Aug | −0.0222 [−0.0572, +0.0129], SE 0.0179 | same | 3.8e-16 |
| Δ_W | Nov | +0.8352 [+0.8001, +0.8703] | same | 5.6e-16 |
| Δ_W | Feb | −0.1466 [−0.1836, −0.1097] | same | 6.7e-16 |
| leg (a) D_L | Aug / Nov / Feb | −13.0319 / −10.4701 / −11.8952 | same, same SEs | ≤ 5.3e-15 |
| leg (b) D_L | Aug / Nov / Feb | −4.1989 / −1.8716 / −6.2169 | same | ≤ 1.6e-15 |
| leg (e) D_L | Nov / Feb | +3.7160 / +2.7916 | same | ≤ 1.8e-15 |
| owner, §9(1) on the analyst's intervals | — | O-A | O-A (steps: F, F, T, —) | ✓ |
| H3, persistent-leg rule | — | declared on (a), (b) | (a) 3/3, (b) 3/3, (e) 0/2 → declared | ✓ |
| rob_C7 D | Aug / Nov / Feb | −15.5899 / −11.8901 / −16.7141 | same | ✓ |
| rob_W1_modal D | Aug / Nov / Feb | +0.3172 / +7.7044 / −0.1701 | same | ✓ |
| rob_X5 (>10%) D | Nov | −4.5815 | −4.5815 (23 tasks, 8.913 pp of Q4) | ✓ |

Cause of the exact match: the estimand is linear in published counts and the join is deterministic; there is no
estimation step in which two correct implementations could differ.

## Assumptions sweep

Not a brief- or draft-stage item; the four items are carried into `red-team.md` (§1–§4) with what the results now
say about each.

## What I could not verify

- The parametric bootstrap, the 2,000-replication coverage runs and the eight synthetic recoveries: read from
  `04_second_implementation.out.txt`, not re-run. The closed-form SEs they are compared against I did verify.
- The three exploratory tests (1P API, pattern split, JobZone) and the fourth window (C10): not re-derived. They may
  not appear in a headline, and `claims.md` binds them to the exploratory register.
- Figure 2.11 from the released library: read from `02_build.out.txt`; verified by the steward and by me at the
  brief stage.
- Within-task dependence of conversations: no identifier exists; model (a)'s SE is a lower bound and no one can
  say by how much. The between-window dispersion of D (item 17) is the only empirical hint, and it says the
  within-window interval is not the uncertainty that matters for any statement beyond one window.
- Whether the Seychelles rate contamination in November is automation-heavy: unobservable. My bound (supplement):
  even with every SC conversation on a Q4 task counted as automation and every one on a Q1 task as augmentation,
  and the weights netted, November's D is +4.50 pp — still far above August and February. Seychelles does not
  account for November's excess; the X5 flip to −4.58 removes the two largest software-modification tasks
  (8.5 pp of Q4, p ≈ 70–74 in every wave), which is leg (a) again.
