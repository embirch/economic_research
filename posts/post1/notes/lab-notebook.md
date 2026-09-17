# Lab notebook · post1 (LL-07)

Dated entries, newest last. One entry per step. Each entry: what was run (script), what it showed
(two lines, numbers), what was decided. Every deviation from the pre-registration is its own entry
beginning DEVIATION, with the reason. Every mistake found is its own entry beginning CORRECTION,
with what changed downstream.

---

## 2026-09-17 · Stage 2 step 2 — pre-registration drafted (P1–P9)

**Read, in full, from the record:** `posts/post1/BRIEF.md` (`8fbffbd`, all twelve sections),
`posts/post1/notes/referee-brief-2.md`, `posts/post1/notes/feasibility.md` (§4 and §7 in full),
`posts/post1/notes/replication.md` (§4 and §5 in full),
`room/steward-2026-09-17-replication-post1.md`, `team/templates/PREREG.md`, and the
`empirical-standards`, `economic-index-data` and `room-protocol` skills. Room notes addressed to the
analyst: nine, all `needs-reply: no`, recorded in `room/analyst-answered.txt`. `reference/` was not
opened. No file owned by another agent was edited.

**Run:** `posts/post1/scripts/01_power_rules.py` — the only script run before the pre-registration
commit, and it loads no data: its inputs are the three standard errors the steward has already
published (`feasibility.md` §4 model (a): 0.151 / 0.148 / 0.154 pp) and the referee's
0.151 / 0.149 / 0.151 pp. Output `posts/post1/data/processed/power_rules.json`.

**What it showed.** The power of each §9(1) rule, three waves conjoined, by exact normal calculation
and by Monte Carlo (400,000 triples, seed 20260917; the two agree to 0.0007 on every owner): H1 (and
H2 by symmetry) reaches 80% at a true |D| of **1.517 pp** and 0.000 at 1.0 pp (0.501 at 1.42 pp);
O-A-or-stronger reaches 80% from **0.517 pp**; step (4)'s clause holds with 80% probability up to
**0.483 pp**. The 41³ grid partition gives every one of 68,921 triples exactly one owner (H1 512,
H2 512, O-A 10,640, H4 3,125, O-B 54,132 — the O-A count matching the referee's 10,640), and the
named problem triples resolve as §9(1) says. Check block passed.

**Decided.** The pre-registration is written on the template's six headings with every referee item
P1–P9 under its own labelled heading or bullet; the §9 rules are reproduced, not redesigned; the
question, title, contribution and hypotheses are untouched. Three places where the brief is silent
are completed and marked in place, with the literal reading reported beside the completed one in each
(P4 leg persistence, P3(b) identified set, P2 declared power). Seventeen confirmatory estimates are
named and counted (3 D + 3 Δ_W + 3 slope + 3 leg (a) + 3 leg (b) + 2 leg (e)), of which eight are the
leg tests. `posts/post1/prereg/prereg.md` goes to the referee; the director commits it.

## 2026-09-17 · CORRECTION — §9(4)'s H4 power figure is step (4)'s clause, not the declaration probability

Item 23 of `referee-brief-2.md` and BRIEF §9(4) state that H4 "fires with 80% joint power at a true
|D| up to ≈ 0.49 pp" (and 0.14 at 0.70 pp). Those are the probabilities that **all three intervals
lie inside ±1 pp** — step (4)'s clause taken on its own, reproduced here exactly (0.483 pp at 80%;
0.133 at 0.70 pp). They are not the probability that **H4 is declared**, because step (3) takes
precedence whenever all three intervals exclude zero with one sign, which is likely at |D| near
0.5 pp. The declared-H4 probability is 0.810 at a true D of 0.32 pp and **0.228 at 0.49 pp**.
Downstream: the pre-registration reports both figures (P2), the brief is left as it stands (it is
frozen and not the analyst's file), and the point is raised for the lead and the referee in
`room/analyst-2026-09-17-prereg-post1.md`. No decision rule changes — the rule is the rule; only its
stated power does.

## 2026-09-17 · CORRECTION (printed precision, not a discrepancy) — 2.8 × 0.148 = 0.4144

`replication.md` §3 and `feasibility.md` §4 print SE 0.151 / **0.148** / 0.154 pp with
MDE(80%) 0.42 / **0.42** / 0.43 pp; on the SE rounded to three decimals the November MDE is 0.4144,
which rounds to 0.41. Any unrounded SE in [0.1482, 0.1518] prints 0.42, so this is the rounding of the
printed SE and not an arithmetic error — asserted as such in `01_power_rules.py`'s check block
(|2.8 × 0.148 − 0.42| ≤ 0.01). Downstream: script 03 recomputes the SE to four decimals and asserts
MDE = 2.8 × SE, so the published figure will carry its own precision.

## 2026-09-17 · Noted for the referee, not changed — two wordings the pre-registration had to resolve

(i) BRIEF §9(3)(b) names "the groups that span the global bottom and top quartile" in words and
"7 / 8 / 6 of 22 span all four" in its parenthesis; `feasibility.md` §4 gives **10 / 10 / 8** groups
containing tasks in both the bottom and the top quartile. The estimand needs only Q1 and Q4, so the
pre-registration takes the 10 / 10 / 8 set as primary and reports the 7 / 8 / 6 subset beside it.
(ii) BRIEF §9(3) does not say in how many waves a leg must fire for H3; the pre-registration mirrors
§9(1)'s persistence for D (a leg must fire in every wave in which it is testable) and reports the
literal any-wave reading beside it. Both are flagged in the room note; neither changes a rule.

## 2026-09-17 · What the data cannot show, recorded as it was met

The per-task automation rate is a usage-weighted blend over countries and cannot be cleaned at this
grain (intersections are global only), so no country statement is available and November's rates keep
a Seychelles share sitting behind 9.039 pp of the top quartile. August publishes no `use_case` facet
at any grain and has no substitute, so leg (e) is a two-wave statement and the work-mix rival is
asserted, not tested, for August. The March-2025 window publishes no counts, so it can carry no
conversation-level interval and no `none` share at task level. The wage is an occupational aggregate
for work that *resembles* the task, and its level does not reproduce Anthropic's published series —
which is why the design is rank-based and no wage level is reported as Anthropic's.

## 2026-09-17 · Stage 2 step 3b — referee's pre-registration items applied

**Read:** `posts/post1/notes/referee-prereg.md` (`f859206`, PASS WITH CHANGES, zero blocking) and
`room/referee-2026-09-17-prereg-post1-verdict.md`. **Applied to `posts/post1/prereg/prereg.md`,
exactly as the referee words them:** item **4** (P4's justification replaced: the persistent-leg rule
is primary for a reason of specification, not of text — the any-wave reading declares H3 with no
composition present in ≈60 / 50 / 27 / 12% of declared gradients at a true D of 0.5 / 0.6 / 0.8 /
1.0 pp against ≤1–2% for the persistent rule); item **5** (H3's "rule against" rewritten as the
complement of the support rule, so H3's space is a partition; "rule for support" now reads "when H1,
H2 or O-A has been declared (a declaration spans the three waves)"); item **6** (new bullet giving
the H3 *rule's* power and false-declaration rate under the referee's covariance model, and the
Interpretation table's last row now says a non-declaration under O-A is "nothing shown" and may not
say composition has been ruled out); item **7** (H1's and H2's "rule against" re-worded to the
every-wave leg language); item **9** (model (a)'s SE stated as a **lower bound** under unmeasurable
within-task dependence); item **11** (new P6 bullet under H1/H2, and the O-A bullet's consequence, for
a C7 sign disagreement: the owner is unchanged, the §12 first sentence carries the non-corroboration
with C7's coverage); item **14** (the work-share covariate listed, with the usage-weighted pairwise
correlation and VIF of wage and work share printed beside it).

**Also applied, as pure wording substitutions with exact text and no rule effect:** item **15(a)**
(O-A's expected-MDE line: O-A-or-stronger 80% from ≈0.5 pp; O-A as declared ≈1.00 near 1.0 pp and
yielding to H1 above ≈1.4 pp — both read off the committed `power_rules.json` curve: O-A 1.000 at
D = 1.0; H1 0.501 against O-A 0.499 at 1.42) and item **15(b)** ("(the figure BRIEF §9(4) quotes)"
on the P2 table's H4-clause row).

**Not applied, and why.** Item **10** (make the D_L − ½D interval the one read for the half judgement,
r_L descriptive with its instability named) and item **15(c)** (state that O-B's probability under a
non-constant true D is not computed) are "could" items with no exact replacement text; both require
new sentences rather than a substitution — item 10 would also shift which interval a reader is
directed to for the half judgement — so both are left for the director's call at the commit or for
Stage 3. No rule, hypothesis, threshold or exploratory test moved. `01_power_rules.py` was not changed
and was re-run: check block passes. "Committed as" left unfilled for the director.

## 2026-09-17 · Stage 2 step 5a — `02_build.py`: frames, joins, the analysis set, the quartiles

**Run:** `posts/post1/scripts/02_build.py` (output `posts/post1/outputs/checks/02_build.out.txt`,
facts `posts/post1/data/processed/build_facts.json`, diagnostic plots
`posts/post1/outputs/diagnostics/`). Room notes addressed to the analyst and not yet recorded:
three, all `needs-reply: no` (`director-…-gate-2a-post1.md`, `director-…-gate-2a-post1-approved.md`,
`referee2-…-prereg-post1-reverdict.md`); recorded in `room/analyst-answered.txt` and answered in one
note. `reference/` not opened; no file owned by another agent edited.

**What it showed.** Every recorded construction fact reproduces: intersection rows 14,454 / 16,778 /
17,530 at global only, seven patterns, min count 1; named nodes 2,616 / 3,168 / 3,258 at
91.8727 / 93.5144 / 92.9714 pp; C5 all matched, 0 unmatched, 0 collisions; C6 priced
2,607 / 3,154 / 3,244 (99.35 / 98.98 / 99.30% of named mass); **analysis set 1,802 / 2,075 / 2,188
tasks, 89.2530 / 89.9892 / 89.7348 pp = 97.15 / 96.23 / 96.52% of named mass, on 818,673 / 854,432 /
848,716 classified conversations**, with X1 = 805 / 1,079 / 1,056 and X2 = 5 / 12 / 12 dropped and
never zeroed; Kish 99.7 / 89.5 / 134.3 named and 94.4 / 83.4 / 125.7 on the analysis set. Published
splits 49.0980 / 51.0698, 45.3554 / 46.7394, 44.1569 / 45.5456; the §8(iii) internal check
+0.1303 / +0.2931 / +0.3510 pp; the `none`-node variant 51.7424 in August; Anthropic's released
library returns Figure 2.11 at −3.111834 / 0.393687 / N 111. C9 covers 100% of the analysis set in
Nov and Feb (943 / 1,071 work-dominant tasks, 29 / 21 only-`not_classified`, 35 flips each wave);
C8 SC 24,715 conversations with 0 intersection rows, 23 tasks > 10% (11.594 pp) and 14 > 20%
(1.966 pp); C10 reaches 1,635 / 1,843 / 1,904 analysis-set tasks.

**Decided.** The build table is the single source for scripts 03–09 (`/tmp/post1/build_<wave>.parquet`,
rebuilt by re-running this script); quartiles, quartile weights and the analysis set are imported
from it rather than re-implemented. Check block passed (110 assertions).

## 2026-09-17 · DEVIATION — the quartile rule is under-specified at a wage mass point; both readings run

**Pre-registered rule** (prereg §Definitions 3, from BRIEF §9(1)): "quartile boundaries are drawn on
usage-weighted wage over the analysis set of that wave, on the primary wage rule". **What the data
does:** the third boundary is $43.40/hr in all three waves and it is a *mass point* — 99 / 106 / 111
analysis-set tasks share exactly that wage, carrying **10.6012 / 8.3586 / 7.9528 pp** of the wave,
against a Q4 of about 22.5 pp. Cutting the cumulative usage mass at 0.75 therefore splits a tie, and
**which** of the tied tasks lands in Q4 is decided by the sort order, not by the rule: 4.9 / 5.2 /
6.1 pp of Q4's mass comes from inside the tie. The steward's feasibility run (an unstable sort on
the equal-split wage) put 431 / 480 / 496 tasks in Q4 with Kish 13.7 / 11.5 / 16.5; this script's
order gives 360 / 403 / 482 tasks and Kish 10.6 / 8.9 / 16.4. Neither is more faithful to the
pre-registered sentence.

**Reason it is a mis-specification and not a coding choice:** two tasks with the same wage are
assigned to different quartiles, so "the top quarter of usage-weighted wage" is not a function of
the wage alone, and D inherits the arbitrary part.

**Both rules are run** (script 03, both reported in `results.json`):
1. **the pre-registered rule**, made reproducible by fixing the order inside a tie on (wage, task
   text) — each quartile exactly a quarter of the usage mass, ties split;
2. **the corrected rule**, fractional allocation: a wage value straddling a boundary contributes to
   the two adjacent quartiles **in proportion**, so each quartile is still exactly a quarter of the
   usage mass and no choice is made among tasks that share a wage.
The primary owner declaration is read off the pre-registered rule, as registered; the corrected
rule's three intervals and its owner are reported beside it.

## 2026-09-17 · CORRECTION — BLS-EP employment does not reach the 2010 computer codes, and the A2 rule had to fall back

`feasibility.md` §1 C7 records that BLS-EP employment is 7-character only and says the
employment-weighted rule "degenerates to the equal-split mean for the two tasks whose holders sit
inside one 7-char SOC". The larger gap is the **vintage**: BLS-EP is keyed on SOC-2018 codes and
matches 670 of the 775 7-character O\*NET-SOC **2010** codes, and the codes it misses include the
renumbered computer family (`15-1132` → `15-1252`). Consequences, both handled by rules the brief
already states: (i) W1's employment-weighted wage has **no** employment figure for any holder on
620 / 651 / 620-odd tasks — almost all of them single-holder, where all three wage rules coincide;
of the 74 / 93 / 86 genuinely multi-priced-holder tasks the rule is identified on 42 / 55 / 51 and
falls back to the equal-split mean on the rest (printed by the script). (ii) A2 ("each task in
exactly one group") must use the brief's stated fallback — where employment is missing or tied, the
**lexicographically smallest 10-character code** — which my first implementation skipped, leaving
the group unassigned and the SOC-15 drop mass at a nonsense 4.66%. Fixed before any estimate:
A2's SOC-15 drop mass is now 43.00 / 39.75 / 35.55% of analysis mass on the 2019 recode and
40.04 / 37.29 / 33.11% on 2010, against the A1 equal-split shares of 43.02 / 39.82 / 35.70% (2019)
and 40.04 / 37.29 / 33.26% (2010) and the recorded 39.86 / 37.12 / 33.11% (2010, MULTI bucket).
Downstream: leg (a) is run on the 2019 recode as primary (V1) with the 2010 grouping beside it.

## 2026-09-17 · Stage 2 step 5b — `03_headline.py`: D, Δ_W, the slope, and the ordered chain

**Run:** `posts/post1/scripts/03_headline.py` (output
`posts/post1/outputs/checks/03_headline.out.txt`, numbers
`posts/post1/data/processed/headline.json`). The §9(1) chain is imported from `01_power_rules.py`,
so the code that declares the owner is the code whose power was pre-registered.

**What it showed.** On the pre-registered quartile rule, D = **+1.3836** [+1.1006, +1.6667],
**+7.3854** [+7.1103, +7.6605] and **+0.6689** [+0.3947, +0.9431] pp (Aug / Nov / Feb), SE
0.1444 / 0.1404 / 0.1399 pp and MDE 0.404 / 0.393 / 0.392 pp; the ordered chain gives step (1)
false, step (2) false, **step (3) true → OWNER = O-A**. On the corrected quartile rule D =
+0.5434 / +7.1793 / +0.3387 pp and the owner is **O-A** as well. Δ_W = −0.0222 / +0.8352 / −0.1466
pp (its own intervals, MDE 0.05); the slope per +$10/hr is −0.0507 (not significant) / +1.7657 /
−0.2843 pp, so the continuous companion's sign disagrees across waves. The quartile shares are
**not monotone**: 53.05 / 47.01 / 49.84 / 54.43 (Aug), 46.58 / 41.32 / 45.98 / 53.97 (Nov),
48.85 / 41.55 / 43.51 / 49.52 (Feb) — a U shape, which is why Δ_W is near zero while D is positive,
and 0 of 3 augmentation patterns are weakly increasing across quartiles in any wave (P5's clause
fails; the `none` share falls 3.6 → 1.2, 3.1 → 1.2, 3.4 → 1.1 from Q1 to Q4).

**Decided.** The owner is read off the pre-registered rule and is **O-A** under both quartile
readings, so the tie deviation does not change the owner; both sets of three intervals go into
`results.json`. Check block passed (D equals the difference of the two quartile shares it is built
from; the five pattern shares sum to 100 in every quartile; directive + feedback loop equals the
automation share; each quartile holds a quarter of the usage mass; mean wage rises across
quartiles; MDE = 2.8 × SE exactly; the imported chain still resolves the referee's problem triples).

## 2026-09-17 · Note on the variance model — the registered formula and the steward's arithmetic agree to 0.01–0.02 pp

The pre-registered formula (P1(a)) is Var(D) = Σ_{i∈Q4}(w_i/W_4)² p_i(1−p_i)/n_i + the same over Q1,
i.e. the variance of the **usage-weighted** difference. `data/replication/post1_variance_mde.py`
computes model (a) as a pooled binomial on each quartile's total classified conversations at that
quartile's aggregate share, which ignores the usage weights: a different statistic on the same
model. Both are computed here: registered 0.1444 / 0.1404 / 0.1399 pp, pooled 0.1557 / 0.1534 /
0.1539 pp, against the recorded 0.151 / 0.148 / 0.154 pp. The realised MDE is therefore
0.40 / 0.39 / 0.39 pp against the pre-registered 0.42 / 0.42 / 0.43 pp — no rule moves (δ = 1 pp is
still more than twice the MDE), and the realised SE and MDE are printed beside every coefficient as
the pre-registration requires. The SE remains a **lower bound** under within-task dependence
(P1(a)), which no public file lets us correct.

## 2026-09-17 · Stage 2 step 5c — `04_second_implementation.py`: the second code path, the bootstrap, the recoveries

**Run:** `posts/post1/scripts/04_second_implementation.py` (output
`posts/post1/outputs/checks/04_second_implementation.out.txt`, numbers
`posts/post1/data/processed/second_implementation.json`).

**What it showed.** The second path — p_i from the `_pct` rows renormalised, w_i from
`onet_task_count` renormalised, the wage built from the **SOC side** (C6 → C5 → task text), the
quartiles cut by an independent lexsort-and-cumsum route, D in pooled form, Δ_W as
Cov_w(wage, p)/E_w[wage], the slope as a weighted covariance ÷ a weighted variance and again through
`statsmodels` WLS — selects the **same analysis set** (set difference 0), the same quartile labels
(0 differences), an identical task→wage map (0 differences), and reproduces D, Δ_W and the slope to
**1.8e-14 pp or better** in all three waves. The published `_pct` rows turn out to be exact, not
rounded (max |Δp| 2.1e-14), so P6's fallback 0.01 pp clause was not needed. The seeded parametric
bootstrap (10,000 draws) reproduces the closed-form SEs to 0.04–0.93% and covers at
95.0–95.3%. Synthetic recovery: D recovered exactly at implanted gaps of 0 / 0.5 / 1 / 3 pp with
coverage 94.4–95.4% over 2,000 replications and the zero case's interval covering zero; Δ_W and the
slope recovered to 3e-15; leg (b) returns the implanted **within-group** average +0.1655 while the
total gap is +16.2423 (the property the leg is run for) and the bottom-only group is reported as not
identified, never zeroed; leg (e)'s threshold selects the implanted set and drops the
only-`not_classified` tasks rather than scoring them 0; the design-based bootstrap SE is within
3.6% of its analytic value; the permutation test's size is **4.93%** on 1,500 independent trials;
Kish N exact.

**Decided.** The headline numbers are confirmed by an independent implementation, so scripts 05 and
06 estimate every leg and every robustness cut through the primary path and compare against this
script's stored leg values. Check block passed.

## 2026-09-17 · DEVIATION — P6's 2% SE-agreement tolerance is unattainable for the ratio r_L; the half judgement is read from D_L − ½D

**Pre-registered:** P6's last two rows require the retained fraction r_L = D_L/D to agree between the
delta method and the parametric bootstrap "to 2%". **What the data does:** D is +1.38 pp (Aug) and
+0.67 pp (Feb), so r_L is a ratio with a small denominator; its sampling distribution is
heavy-tailed and the delta method understates the bootstrap SE by 5% (Aug leg (b): 0.450 vs 0.473)
and by up to **21%** (Feb leg (a): 3.93 vs 4.75). No implementation can make them agree to 2%: the
tolerance was mis-specified, not the code.

**Both are run and both are reported.** The tolerance actually asserted for r_L is 25%, and the
statistic whose agreement **is** asserted at 2% is the **linear** contrast **D_L − ½D**, which the
pre-registration already requires beside every leg and whose closed-form SE the bootstrap reproduces
to 0.1–2.0%. This is the reading the referee's carried item 10 asked for (the half judgement read
from D_L − ½D, r_L descriptive with its instability named); r_L and both of its SEs go into
`results.json` with the gap between them. **The declaration itself is unaffected:** §9(3) declares a
leg on the point estimates, and the point estimates are identical across implementations.

## 2026-09-17 · DEVIATION — recovery test 7's size band widened from ±1 pp to ±2 pp, with the reason

Prereg's synthetic test 7 asks the permutation null to reject at "5.0% ± 1 pp" under a zero
gradient. The size estimate itself is a Monte Carlo quantity: at 1,500 independent trials its
binomial error is 0.6 pp, and the seed-to-seed spread is about ±1.2 pp (three 1,000-trial runs gave
5.7 / 3.5 / 5.8%) because the permutation structure and the 29 / 31 quartile sizes are discrete.
The check therefore asserts ±2 pp and prints the Monte Carlo error beside the estimate; the realised
size is **4.93%** on 1,500 trials. Two implementation notes recorded with it: the test is the exact
two-sided permutation p-value (1 + #{|perm| ≥ |obs|})/(B + 1), not a quantile-band comparison (the
band is noisy at small B and is reported as a band, not as the test); and the wage vector and the
outcome are re-drawn in every trial, so the trials are independent. The placebo is in no decision
rule.

## 2026-09-17 · Stage 2 step 5d — `05_legs.py`: the eight leg tests and the P4 verdicts

**Run:** `posts/post1/scripts/05_legs.py` (output `posts/post1/outputs/checks/05_legs.out.txt`,
numbers `posts/post1/data/processed/legs.json`).

**What it showed.** Eight leg tests, legs (a) and (b) in three waves and leg (e) in two.
Leg (a) (SOC-15 excluded, 2019 recode, 43.0 / 39.8 / 35.6% of analysis mass and 73.7 / 71.5 / 65.5%
of Q4 mass removed): D_L = **−13.0319 / −10.4701 / −11.8952** pp against D = +1.3836 / +7.3854 /
+0.6689, so r_L = −9.42 / −1.42 / −17.78 and the leg **fires on sign in all three waves**.
Leg (b) (within major group, 9 / 9 / 9 identified groups carrying 71–76% of Q1+Q4 mass, the rest
reported as not identified): D_L = **−4.1989 / −1.8716 / −6.2169** pp, fires on sign in all three.
Leg (e) (work-dominant, 943 / 1,071 tasks = 54.38 / 52.86% of analysis mass, 29 / 21
only-`not_classified` tasks dropped): D_L = **+3.7160 / +2.7916** pp, r_L = +0.50 / +4.17, and it
does **not** fire in either wave (the substantive-cell denominator gives +3.85 / +2.74, also not
firing). **6 of 8 leg tests fired.** The persistent-leg rule and the literal any-wave reading
**agree**: H3 is declared, on legs (a) and (b), each firing in every wave in which it is testable.
The 2010 grouping gives the same verdict (6 of 6 fired). H1's signature clause fails in all three
waves. Description: the leave-one-group-out series is dominated by SOC-15 in every wave
(−14.42 / −17.86 / −12.56 pp against a second-largest of +3.24 / +2.32 / +2.91), and its removal
exceeds the sum of all other moves in Aug and Nov but not in Feb; the ten largest tasks out moves D
to −11.62 / −13.08 / −11.43 pp; the work share rises Q1→Q4 32.80 → 60.82 (Nov) and 29.05 → 60.54
(Feb) while corr(wage, work share) is only +0.34 (VIF 1.13–1.14), and the wage slope falls from
+1.78 to −0.06 (Nov) and from −0.28 to −1.63 (Feb) once the work share is in the regression.

**Decided.** H3 is declared under the pre-registered rule and under the literal reading, so no
disagreement to report; every leg point estimate matches the independent implementation of script 04
to better than 1e-6 pp. Check block passed.

## 2026-09-17 · Stage 2 step 5e — `06_robustness.py`: every pre-registered cut, and nothing else

**Run:** `posts/post1/scripts/06_robustness.py` (output
`posts/post1/outputs/checks/06_robustness.out.txt`, numbers
`posts/post1/data/processed/robustness.json`).

**What it showed.** D primary +1.3836 / +7.3854 / +0.6689. X3 (drop tasks with < 100 classified
conversations; 1,140 / 1,222 / 1,278 tasks, 7.0–7.6 pp) gives **+2.6049 / +9.0725 / +1.5934**, and
the ordered chain on those three would declare **H1**. X4 (SC netted from the November weights, max
shift 0.5391 pp) gives +6.5463; X5 (drop the 23 tasks where SC exceeds 10% of their global count,
11.594 pp of the wave, 8.913 pp of it in Q4) turns November **negative, −4.5815**, and with that
wave the chain declares **O-B**; the > 20% variant (14 tasks, 1.966 pp) leaves it at +7.5042 (O-A).
X7 is inert for D by construction (the `none` node carries no wage, so it cannot enter a quartile);
what it moves is the wave-level mean, 51.2001 → 51.7424 in August. W1: the equal-split wage gives
+1.3770 / +7.3853 / +0.6581 (O-A) and the **modal holder** gives +0.3172 / +7.7044 / **−0.1701**
(O-B). A1 moves only the group statistics, as it must — leg (a) D_L −13.71 / −14.07 / −13.03 across
the three allocation rules — and cannot move D or Δ_W (asserted, not assumed). Model (b), the
design-based bound: SE 5.03 / 7.20 / 5.76 pp, **MDE 14.1 / 20.2 / 16.1 pp**. C7, the second wage
source (55.4 / 58.4 / 62.1% of the analysis set's mass): D **−15.5899 / −11.8901 / −16.7141** —
the sign **disagrees with C6 in all three waves**, so under P6's O-A rule the owner is unchanged and
the non-corroboration is carried in the first sentence with C7's coverage as the reason it is not
decisive. The placebo (10,000 permutations of the wage within SOC major group) has mean
+3.3797 / +8.8871 / +4.7632 pp, sd 3.31 / 4.47 / 3.68 pp, and two-sided p of 0.83 / 0.68 / 0.95 —
the observed D sits inside the band in every wave.

**Decided.** Nothing was added to the pre-registered list, and model (c) was not run (P1(c) records
it as neither primary nor reported). The owner under every cut is reported in `results.json` so that
the cuts which would move it — X3 → H1, X5 → O-B, the modal-holder wage rule → O-B — are visible
beside the declared O-A. Check block passed.

## 2026-09-17 · Note on the placebo — the permutation null is not centred on zero, and cannot be

The pre-registered placebo permutes the wage **within** SOC major group. That destroys the
within-group wage–automation relation and **preserves the between-group composition**, so the
permutation distribution of D is centred on the composition effect, not on zero: +3.38 / +8.89 /
+4.76 pp. Its band must therefore not be read as a null distribution for "no gradient"; it is what
the pre-registration calls it, a task-level bound, and it is in no decision rule. The observed D
lies inside that band in all three waves (p = 0.83 / 0.68 / 0.95). One sentence of reading, as the
notebook allows: the gradient is no larger than the wage-group composition alone produces.
