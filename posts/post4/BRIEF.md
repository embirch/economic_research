# post4 · Does AI's self-assessed success rate predict which work people keep bringing to it?

*Brief of record. Question, title and contribution freeze at Gate 1b. Candidate LL-09
(`programme/SHORTLIST.md` §6; `programme/LONGLIST.md` LL-09), carrying referee correction 3
(`room/referee-2026-09-16-shortlist-audit.md`, confirmed applied in `-audit-2.md` §(c)), the editor's
note `room/editor-2026-09-16-sketch-LL-09.md`, and the steward's five amendments of
`room/steward-2026-09-16-feasibility-post4.md`, each marked below.*

**Title form, settled here (editor's note, final paragraph).** The sketch's "AI's *measured* success
rate" presupposes that the label measures success, which is this post's own circularity risk; the corpus
names the instrument inside the noun — "Task success measures **Claude's assessment** of whether Claude
completes tasks successfully" (`economic-index-2026-01-report`, p.21) — so the question says
**self-assessed**. The question says AI; every finding and axis label says Claude; the measure is named
on first use as *Claude's own assessment of whether it completed the task* and thereafter as *the success
rate Claude assigns a task*.

## 1. The question

Does the success rate an AI system assigns its own work on a task predict whether that task's share of
use grows in the next observation window?

## 2. Why it matters, and to whom

The economic question is whether a machine's self-report about its own performance carries information
about where work goes next. Task success is the primitive Anthropic uses to turn raw usage into
economics: it discounts the productivity estimate, reorders which occupations count as covered, and
carries the learning-curve result. Anthropic states the validation that would settle it — "Ultimately,
the strongest validation will come from the primitives' ability to capture meaningful variation in labor
market outcomes" (`economic-index-2026-01-report`, 2026-01-15, p.24) — and no publication in the corpus
runs any predictive test of it against anything observable. The public data permits the nearest available
version: does the November success rate predict the change in a task's usage share to February.

The reader who decides something differently is the economist or policy analyst quoting the
success-adjusted productivity revision: "implied productivity growth falls from 1.8 to 1.2 percentage
points per year for the next decade based on Claude.ai usage, and to 1.0 percentage points for API
traffic" (ibid., p.48), summarised as "Adjusting productivity estimates for task reliability roughly
halves the implied gains, from 1.8 to about 1.0 percentage points" (ibid., p.38). That revision is a
reweighting of task-level speedups by this measure. If the measure has no demonstrated relation to any
observable, the citation has to change from "gains are about half as large once reliability is accounted
for" to "half as large under Claude's own assessment of its reliability, which has not been shown to
predict anything" — and the platform ambiguity travels with it, since the "about 1.0" of p.38 is the API
figure and the Claude.ai figure is 1.2. The same holds for effective coverage, "the percent of a worker's
day that can be performed successfully by Claude… calculated as the weighted sum of task success rates"
(ibid., p.43), which the labour-market literature has begun to borrow, and for the Institute's ambition
for this data — "We'll try to be an early warning signal for significant change and disruption"
(`institute-agenda-2026-05`, 2026-05-07, *Share 1*), which needs the primitives to be forward-looking.

Only the Economic Index releases can answer it: they publish, on one taxonomy and at one grain, a
per-task success rate a model assigned by reading transcripts and the same task's share of a million
conversations, in two windows three months apart. No other public source pairs an LLM-judged success
measure with the same named task's subsequent usage share at this scale; Microsoft's Copilot study is the
one analogue and it has no second window.

## 3. The thread of Anthropic's inquiry this builds on

Thread **T4** (task-level primitives and productivity), with **T8** (measurement and methods), in
`programme/THREADS.md`. The measure, verbatim:

> "**Task success** measures Claude's assessment of whether Claude completes tasks successfully. Task
> success helps assess whether tasks can be automated effectively (can a task be automated at all?)
> and efficiently (how many attempts would it take to automate a task?). That is, task success
> matters for both the feasibility and the cost of automation labor tasks."
> — `economic-index-2026-01-report`, 2026-01-15, p.21

The classifier prompt, shared across platforms, verbatim:

> "Did the Assistant complete the task provided by the User successfully? Choose from these options:
> • Yes: the Assistant completed the task provided by the User successfully • No: the Assistant did
> not complete the task provided by the User successfully"
> — ibid., Table 2.1, p.20 (full prompt, Online Appendix §2.1.4, appendix p.13)

What the thread has established, on single waves: the level (Figure 2.2, p.25, global Claude.ai task
success **67%**, N = 999,875; API **49%**, p.26); that success falls as work gets harder — "Harder
tasks—those requiring more specialized knowledge and where users could not easily complete them
alone—show lower estimated success rates" (ibid., p.26); the task-horizon result (pp.41–42); and a
cross-sectional association with user tenure, where "long-tenure users are about 5 percentage points more
likely to have a successful conversation" before controls and about 4 points with them
(`economic-index-2026-03-report`, 2026-03-24, Fig 2.4 and text pp.17–18).

Where it is open. The fourth report gives no accuracy, agreement or kappa statistic for this classifier
and says only that the nine primitives are "directionally accurate" (p.22) — ledger `L-2026-01-R4-37`
**open**: task success has no reported validation statistic and carries three headline results. The fifth
report then raises the reading that would void its own tenure finding — "This could reflect that higher
tenure users are better at prompting. But what if it reflects that they bring different tasks to
Claude—ones more likely to be successful?" (`economic-index-2026-03-report`, p.18) — ledger
`L-2026-03-R5-29` **open**: a model judging its own success could produce the tenure result with no
learning. **Those two are the gap this post addresses.** `L-2026-01-R4-25` (p.24, quoted in §2) is cited
**only as the criterion this design approximates**: it asks for labour-market outcomes, and a task's
share of conversations is not one. ⟨mentor⟩ Massenkoff is a lead author of the report that built the
success adjustment and effective coverage (`economic-index-2026-01-report`, p.1, ch.4) and of the one
that first tracked the primitives over time (`economic-index-2026-03-report`, Table 1.1, p.9); the design
follows his practice of naming a design's power and publishing nulls — "differential increases in
unemployment on the order of 1 percentage point would be detectable" (`labor-market-impacts-2026-03`,
p.12). Institute agenda: `ED-4`, "What impact will AI have on the rate of innovation and productivity
growth across the economy?", and `Share 1`, quoted in §2 (`institute-agenda-2026-05`, 2026-05-07).

## 4. Overlap, stated

- **Anthropic, levels and cross-sections.** The corpus publishes success levels by platform, request
  cluster, education band and task horizon, and one cross-sectional regression of success on user tenure.
  *New here:* the first test of whether the measure predicts a later change in anything, run on the
  released aggregates rather than on log-level data.
- **Anthropic, a stricter success measure elsewhere.** The Claude Code paper states the limitation of
  judged success and builds around it — "We do not observe users' real-world outcomes, and we cannot ask
  them directly whether they got what they wanted out of Claude", so "Verified success requires both that
  the session is judged successful and there is at least one hard verifiable signal of success"
  (`claude-code-expertise-2026-06`, PDF p.10). *New here:* the Economic Index primitive is judged-only,
  and this post asks whether the judged-only version has predictive content where the verified version is
  unavailable.
- **Microsoft Research (Tomlinson, Jaffe, Wang, Counts, Suri, arXiv 2507.07935 v6, 22 Dec 2025).**
  Closest external precedent: an LLM completion measure on 200k Bing Copilot conversations, "highly
  correlated with direct user feedback (weighted … r>0.75; Figure S5)" (arXiv HTML v6, §Results), with a
  scope measure whose correlation with the log share of user activity `programme/LONGLIST.md` records at
  r = 0.64. *New here:* the Anthropic-data version, across two windows rather than one cross-section, on
  a measure with no thumbs validation behind it. The idea is theirs; the test on this corpus is not.
- **Separation from post2 (LL-11), per the director's pairs ruling.** The two share one series — the
  November 2025 → February 2026 change in a task's Claude.ai usage share at global grain — and therefore
  the same February Super Bowl exposure. **This post headlines the success-rate relation with the
  August-2025 share as the instrument**; post2 headlines the cross-surface correlation between API and
  Claude.ai share changes. This post reports no cross-surface correlation, does not decompose coding's
  share (post3, LL-36), reports the API only as a named exploratory replication (§9), and needs no task →
  SOC join, so it neither states nor inherits post1's multi-holder rule.

## 5. Contribution

If the relation holds, the post supplies the first predictive validation of Anthropic's task-success
primitive and its elasticity — how much of a task's subsequent share growth a point of self-assessed
success buys; if it fails or is null at a stated power, the post shows that the measure carrying the
success-adjusted productivity revision and effective coverage does not predict what users bring back, and
says what the released data would have to contain for the question to be settled.

## 6. Hypotheses

**H1 — Predictive content.** Tasks with a higher November 2025 success rate gain usage share by February
2026. *Signature only it predicts:* a positive coefficient on the November success rate in the regression
of the Nov→Feb share change, which survives controlling for the November share level (instrumented by the
August 2025 share, available for 2,140 of the 2,524 labelled tasks) and for the task's November
education-years, and which is **absent in the pre-period placebo** (the same November success rate
against the Aug→Nov share change). Rivals predict a gradient that is either level-driven,
complexity-driven or equally present in the pre-period. *What counts against it:* a coefficient of zero
or negative sign; or a pre-period gradient of the same sign and comparable magnitude; or a gradient that
disappears once education-years enters. *Stated limit:* the exclusion restriction is arguable, not
testable — August publishes no success facet and no release carries a unit identifier — so the evidence
for it is the first stage (corr(Aug, Nov share) = 0.9167, R² 0.84) and the placebo, said plainly and not
as an over-identification test.

**H2 — Composition, not return behaviour.** Any positive gradient is produced by a change in who was
using Claude in the February window rather than by users returning to work that Claude completes.
*Signature:* the gradient concentrated in tasks whose November profile is consumer-like — low
education-years, high personal or coursework share — and attenuating where the November `use_case` mix is
work-dominant; the fifth report's named inflow of first-time users is the mechanism. *What counts against
it:* the gradient is the same size among work-dominant tasks and survives the `use_case` and education
controls. *Stated limit:* the inflow itself is unobservable — no release carries a tenure, user, account
or first-time-user column — so this tests only the interaction pattern the inflow would produce, on the
1,782 tasks whose November `work` share is published.

**H3 — The label is an inverse index of difficulty.** Success is largely a restatement of how simple a
task is, so any gradient records the published drift toward simpler prompts rather than users returning
to what works. *Signature:* November education-years predicts share growth with the opposite sign and
comparable strength, and the success coefficient loses its magnitude once it is included; Anthropic's own
gradient (70% success below high-school level, 66% at college level, ibid., p.39) is the mechanism. *What
counts against it:* success retains its coefficient with education-years, use-case and the instrumented
level included, and the channel is too weak to carry the result — the steward's pre-check puts the
November success–education correlation at −0.0703 unweighted and −0.1752 usage-weighted over the 2,524
tasks.

**H4 — The movement is at the margin, not among survivors.** What the success measure ranks is which
tasks enter and leave the published sample, not which surviving tasks grow. *Signature:* February-only
entrants carry a higher February success rate than survivors and November-only exits a lower November
rate, while the within-survivor gradient of H1 is flat. *What counts against it:* the three groups'
success distributions are indistinguishable at the stated power while survivors show the gradient.
*Stated limit, from the steward's note:* only 86 of the 282 exits and 140 of the 372 entrants carry a
success label, and 213 exits and 264 entrants have 20 or fewer conversations, so these are
**floor-crossers, not new or vanished work** (absent ≠ zero). The comparison is pre-registered
unweighted, with MDEs of 7.70 pp (exits) and 5.98 pp (entrants) against survivor means of 66.60% and
69.25%; the raw gaps sit near those MDEs, so H4 is reported as suggestive or null either way, and the
post never calls an entrant a new task.

## 7. Assumptions sweep

**(1) Value judgement in the framing — *needs a design change; the change is made in this brief*.**
"Success" and "keep bringing to it" both smuggle in approval: that the label measures success, and that
returning to a task is the rational response to it. The change: the question and every finding say
*self-assessed* and name the instrument on first use (title-form note above); a high success rate is
stated as a property of Claude's judgement of a transcript, not of the work; and share growth is
described as what users brought back, never as what worked. Anthropic is the authority for the qualifier:
"Success is Claude's assessment of whether the conversation was successful"
(`economic-index-2026-03-report`, p.18).

**(2) Construct mapping — *newly flagged; handled, with one construction corrected*.** The verbatim
definition and prompt are in §3: one binary judgement per conversation, by a classifier reading the
transcript, on whether the Assistant completed the User's task. No human rating, no user feedback and no
outcome enters it; Anthropic reports no accuracy statistic (p.22) and, in a later paper, treats judged
success as insufficient alone, requiring "at least one hard verifiable signal" for verified success
(`claude-code-expertise-2026-06`, p.10). **Corrected on the steward's note
(`posts/post4/notes/feasibility.md` §1 row 2):** the intersection publishes **three** categories — `yes`,
`no`, `not_classified` — the third not a verdict but the **folded sub-15 privacy residual**, with the
published cells partitioning the node's `onet_task_count` exactly (3,169 of 3,169 November nodes). The
construct is therefore **the published `yes` `_pct`**, already the share of that task's own conversations
Claude judged successful; the earlier fallback `yes/(yes+no)` is withdrawn, since it would set 961 nodes
whose `no` cell is folded rather than zero to exactly 100% success and is undefined for 558 with no
substantive label. The folded mass is the published error bound — median 22.73 pp on 971 of the 2,524
sample nodes, maximum 48.28 pp, wider for smaller nodes and so correlated with the instrumented level —
and travels with every estimate. Handled also by reproducing the published level first (§8) and by the
steward's tie of the column to the headline: the usage-weighted mean of per-task `yes_pct` is 66.9141%
against the published 66.9060%.

**(3) Composition and selection — *needs a design change; the change is specified*.** Units are
conversations, not users, and occupation is inferred from the task, so a task's share can move because
the user base moved. Three named shocks sit inside the outcome window: *(a) the February Super Bowl
inflow* — "Our sampling period overlapped with the release of our Super Bowl advertisements, which
brought many first-time users" (`economic-index-2026-03-report`, ch.2 endnote 3, p.18) — first-time users
being the low-tenure group whose success rate the same report puts below the high-tenure group's, so the
inflow moves both sides of the relation; *(b) winter school breaks*, quantified only for coursework — a
drop of "5 percentage points in countries where the school term was active and 12 percentage points"
where students were on break (ibid., ch.1 endnote 3, p.11); and *(c) Seychelles*, 24,715 November
conversations (2.47% of the base) with **zero rows at any grain** in February. **Corrected on the
steward's note (§5):** the *outcome* is netted task by task — Seychelles publishes 67 `onet_task` nodes
summing to its 24,715 conversations, 65 in the regression sample — and materially so, because the panel's
largest task ("modify existing software to correct errors…") owes 6,790 of its 59,739 November
conversations (11.37%) to Seychelles, and its raw Nov→Feb change of −1.8160 pp, the biggest movement in
the panel, becomes −1.2712 pp netted. The *regressor* cannot be netted: intersections are global only.
The changes: the November `use_case` mix and education-years enter as pre-specified controls; H2's
primary test is work-dominant against consumer-like tasks; the coursework share is the winter-break
exposure; the Seychelles-netted outcome is a required robustness run (§10) with the 11.37% named in the
post; and the residual asymmetry on the regressor is stated before the estimate.

**(4) Anthropic's own results that cut against or bound the framing — *needs a design change; the change
is specified*.** Two published findings can manufacture H1's pattern with no predictive content. First,
success is inversely related to difficulty in Anthropic's own measurement: "tasks requiring less than a
high school education… attain a 70% success rate, but this drops to 66% for college-level conversations
like developing analysis plans" (`economic-index-2026-01-report`, p.39, Fig 4.1b). Second, the aggregate
mix moved toward simpler prompts in exactly this window: human education fell from 12.21 to 11.92 years,
"statistically significant with p<0.001" (`economic-index-2026-03-report`, Table 1.1, p.9), read by the
report as "a slight decrease in the aggregate complexity of prompts in Claude.ai" (ibid., p.19). A
positive success–growth gradient is therefore partly the image of a published complexity decline. The
change, and a stated departure from the sketch: November education-years is promoted from placebo to
**pre-specified control and benchmark**, because its coefficient has a known non-zero prior, and the null
placebo is the pre-period growth window alone (§10). Cutting the other way, the fifth report's tenure
result has returning users bringing *higher*-education tasks and succeeding more often (Table 2.1, p.15),
which predicts a negative gradient among returning users — so neither sign is safe to assume, and the
post states both priors before the estimate. The steward's pre-check bounds the channel: the
success–education correlation across the 2,524 tasks is −0.0703 unweighted, −0.1752 weighted.

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`programme/LONGLIST.md`, LL-09, "Steward feasibility
line"; source `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`):

> "**LL-09. FEASIBLE.** `onet_task::task_success` at `geography=global` (`_count`, `_pct`; `yes`/`no`)
> in both waves. Matching lower-cased task text: **2,886** named tasks common to Nov 2025 and Feb
> 2026; **2,427** carry a Nov-2025 success rate and so enter the regression (91.95% of Nov named
> mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only, 372 Feb-only** — report both. Log (e) 13."

The caveat inside that line is binding: the sample is 2,427 of the 2,886 matched tasks, reported with its
mass share, and the 282 Nov-only and 372 Feb-only nodes are a margin (H4), not a silent drop. The steward
corrects one reading (the quote stands): the 91.95% is 91.9470 **of 100**, i.e. of all November
conversations, which is 98.32% of November *named* mass. Three nested samples, adopted here: **A** any
published November `yes`/`no` cell, N 2,524, instrument 2,140; **B** a published `yes` cell (the
long-list's 2,427), instrument 2,065 — **primary**; **C** exactly identified, no folded cell, N 1,553,
instrument 1,493. Headline estimates run on B with A and C beside them, the regressor's folding error
(§7.2) being absent in C by construction.

**Cuts, at column level.** Confirmed by the steward at `posts/post4/notes/feasibility.md` (verdict
**FEASIBLE WITH CAVEAT**; every cut exists, five amendments, all applied below; script
`data/replication/post4_feasibility_checks.py`). In the files the metric labels carry underscores, not
colons: `onet_task_task_success_pct`. Rows are checked against `data/ATLAS.md` (Family B; §Cuts that do
not exist 7, 10, 21, 26b; §Conventions; §Thresholds; §Traps 1, 5, 7, 11, 24, 25) and the new fact at
dated log (h).

| # | release | grain | facet / category | metric | threshold and rule |
|---|---|---|---|---|---|
| 1 | `release_2026_01_15`, `release_2026_03_24` (Claude.ai) | `geography=global`, `level=0` | `onet_task` | `onet_task_pct`, `onet_task_count` | drop `none` and `not_classified` (Traps 24); privacy floor 15 on `_count` applies in both waves; outcome = Δ percentage points on the all-conversation base, second implementation on the named-task renormalised base |
| 2 | same two releases | `geography=global` | `onet_task::task_success`, categories `yes` / `no` / **`not_classified`** (the folded sub-15 residual; no node publishes all three) | `onet_task_task_success_pct`, `_count` | per-task success = **the published `yes` `_pct`**, no renormalisation, because the published cells partition the node's `onet_task_count` exactly (3,169/3,169 Nov, 3,259/3,259 Feb); `yes/(yes+no)` **withdrawn** (§7.2). The "`_count` ≥ 15" rule is **inert** — every published `yes`/`no` cell is already ≥ 15 — and is replaced by a near-floor sensitivity on `onet_task_count` (15–20) and on the folded `not_classified` `_pct`, which is also the regressor's error bound |
| 3 | `release_2025_09_15` (Claude.ai) | `geography=global`, `level=0` | `onet_task` | `onet_task_pct` (2,618 nodes, count sum 964,494) | instrument for the November level; matched by lower-cased task text; available for **2,140 of the 2,524** (sample A) and **2,065 of the 2,427** (sample B), **not the ~2,284 this row previously implied** — the named three-wave intersection is 2,282. The 2,140 carry 98.60% of the sample's mass; first stage corr(Aug, Nov) 0.9167 in levels. August publishes no `task_success` facet, so the exclusion restriction is argued, never tested (§6 H1) |
| 4 | `release_2025_09_15` → `release_2026_01_15` | `geography=global` | `onet_task` | `onet_task_pct` | placebo outcome: the Aug→Nov change, defined on the **2,140** instrumented tasks (not 2,427); its sd is 0.0837 pp against the outcome's 0.0530 pp, and corr(outcome, placebo) = −0.4251, the mechanical sign §10 anticipates |
| 5 | `release_2026_01_15` | `geography=global` | `onet_task::human_education_years` (`cluster_name` is the task alone, no `::category`; nine variables); `onet_task::use_case` (`work`, `personal`, `coursework`, `not_classified`) | `_mean` (published 3,169/3,169, range 1.009–17.512 yr); `onet_task_use_case_pct` | pre-specified control and benchmark (§7.4) and the composition controls (§7.3). The `work` cell is folded for 742 of the 2,524, so H2's split is **pre-registered on the 1,782 tasks with a published work share** (median 59.91), with the folded-to-zero split over all 2,524 (median 41.37) as robustness |
| 6 | `release_2026_01_15`, `release_2026_03_24` (1P API) | `geography=global` | `onet_task`, `onet_task::task_success` | `onet_task_pct`; `yes` `_pct` | exploratory replication only (§9); the API has no geography and no `usage_count`. Matched named panel 1,930; **pre-registered on the 1,686 with a November success label**, with the 1,428 instrumented subset reported beside it |

Matching is on lower-cased, stripped task text, rows in, matched and unmatched printed (ATLAS
§Taxonomies: "Never diff cluster sets across waves without an explicit name match and a report of the
unmatched names"); the steward reports 0 case-variant collisions in all three waves and reconciles 2,888
against 2,886 as the two pseudo-nodes. Files are read with `keep_default_na=False, na_values=[]` and
`level` cast to string after any parquet read (Traps 1, 2, 7); the 200/100 geography thresholds do not
bite at global grain. **No supplementary data, no external join.**

**The published number reproduced first** (criterion 3), now confirmed as the replication target: global
Claude.ai task success **67%**, Figure 2.2, p.25, N = 999,875, and the pair **67% vs 49%**, p.26
(`economic-index-2026-01-report` on `release_2026_01_15`). Specification: `facet == 'task_success'`,
`geography == 'global'`, `variable == 'task_success_pct'`, `cluster_name == 'yes'`, all-conversation
base, no renormalisation. The steward's run reproduces it exactly — **66.9060% → 67%**, facet `_count`
summing to **999,875**, the published N to the digit, and the API **49.3638% → 49%** — with the count
route agreeing to four decimals, so §10's second implementation already passes for the anchor. Anthropic
ships no code for it in reports 4–6, which the post states. No published number exists for the per-task
rates or their relation to share growth; the February global level (`yes` 69.9385%) is a data fact,
reported as such.

## 9. Confirmatory tests and the exploratory allowance

Four confirmatory tests, one per hypothesis, run once after the pre-registration is committed.

1. **H1.** Regression of the Nov→Feb change in a task's global share on its November success rate, over
   sample B (2,427 tasks; instrument for 2,065), controlling for the November share level instrumented by
   the August 2025 share and for November education-years; robust errors. **The confirmatory test is
   unweighted**, on the steward's power finding: usage weights collapse the sample to a Kish N_eff of
   86.5 (November weights; 128.2 on February), because the ten largest matched tasks are 19.4410 pp of
   all February conversations — 19.4% of the all-conversation base, 20.9% of named-task mass. Unweighted
   MDE |r| ≈ **0.0569** at 80% power, 5% two-sided (2.8 × SE, SE = 1/√(N−3)); the usage-weighted estimate
   is **required robustness**, with its own MDE of |r| ≈ **0.31** on November weights and **0.25** on
   February, both carried beside the estimate, and the post states that a small weighted coefficient is
   evidence of nothing either way. Headline comparison: the share-growth difference between the top and
   bottom success quartile, unweighted, with the weighted version beside it.
2. **H2.** The same regression with the November `use_case` shares entered and the success coefficient
   estimated separately either side of the median published `work` share over the 1,782 tasks that
   publish one (robustness: folded-to-zero over all 2,524); the difference between the two coefficients
   is the test — of the pattern, not of the inflow, which no file observes.
3. **H3.** The success coefficient with and without November education-years, beside the across-task
   success–education correlation (−0.0703 unweighted, −0.1752 weighted) and pairwise collinearity; the
   test is whether it survives at a magnitude the education channel cannot account for.
4. **H4.** Success rates of the three groups — survivors, the 140 labelled February-only entrants, the 86
   labelled November-only exits — compared unweighted on their own wave's rate, with the MDE for each
   comparison (7.70 pp and 5.98 pp), against the within-survivor gradient from test 1, and with the
   floor-crossing reading stated first.

**Exploratory allowance: three tests, no more, each labelled exploratory and barred from the headline.**
(i) Shape: quartile or decile bins instead of the linear term, in case a linear coefficient hides a
threshold. (ii) Population: the H1 specification on the 1P API global frame (1,686 labelled tasks), to
see whether a consumer-surface relation appears on a work-dominant one. (iii) Direction: the reverse
regression of the change in a task's success rate on its November share, which asks whether growth
predicts success. Any further question is logged for a later post.

## 10. Noise and robustness required

- **Persistence across windows / placebo.** The pre-period test — November success against the Aug→Nov
  share change, on the 2,140 instrumented tasks — is the null placebo, and the only one: a pre-period
  gradient of the same sign and comparable magnitude means a standing task-level correlate, not
  prediction. Its expected sign under pure sampling noise is the mirror of the main test's, since the
  November share enters the two changes with opposite signs, and the steward's measured corr(outcome,
  placebo) = −0.4251 is that mechanism at work, so the magnitudes are read together with the bootstrap
  below. The education-years term is **not** a null placebo (§7.4) and is reported as a benchmark
  coefficient.
- **Flagged units excluded by rule, shown separately.** `none` and `not_classified` task nodes dropped
  throughout (6.49 pp November, 7.03 pp February combined); near-floor sensitivity on `onet_task_count`
  15–20 and on the folded `not_classified` `_pct` (the intersection-cell rule was inert and is withdrawn,
  §8 row 2); samples A and C reported beside B.
- **The Seychelles run, required.** The outcome recomputed with Seychelles' 65 sample nodes netted out of
  the November side (23,173 conversations, 2.3176 pp of the base) and both versions reported, since the
  panel's largest mover goes from −1.8160 to −1.2712 pp. The regressor cannot be netted,
  `onet_task::task_success` being global-only; that residual is named as a limitation.
- **Leave-one-out.** The ten largest tasks dropped one at a time under both estimators, movers named;
  plus a count-based bootstrap over the published `_count` columns, so that a coefficient inside the
  resampling band is reported as such.
- **Second implementation.** The panel and both estimates rebuilt by a second route — shares from
  `_count` (dividing by 999,875 in November, 1,000,000 in February) against shares from `_pct`, the
  regression re-run independently — agreeing to the reported precision before any number enters the post.
- **Synthetic recovery.** A known gradient injected into simulated task shares must be recovered and a
  zero gradient reported as zero, including under the instrumented level control.

## 11. Literature check

Searches run (2026-09-16): the corpus for every use of `task success` in `wiki/reports/` (fourth report
chs.2 and 4, fifth report ch.2, the Claude Code paper's judged/verified distinction); arXiv for an LLM
self-assessed completion measure validated against usage, returning Tomlinson et al., fetched and
verified today at `arxiv.org/abs/2507.07935` (v6, 22 Dec 2025, 40 pp, Microsoft Research, 200k Bing
Copilot conversations); and the long-list's recorded checks of Bick, Blandin, Deming & Schumacher (2026)
— exposure explains "roughly half" of adoption variation, with who the worker is mattering more, the
rival to task quality — and METR (2025), on measured outcomes diverging from believed ones. Closest prior
work is Tomlinson et al. (quoted in §4); this post sits one step to the side of it, on a measure with no
feedback validation behind it, tested across two windows rather than within one.

## 12. What the closing section will be able to say

**If H1 holds.** People bring back the work Claude says it completed: a point of self-assessed success in
November buys a stated amount of subsequent share growth by February, and the relation is absent in the
window before the measurement — the first evidence that the primitive tracks something outside its own
output. The productivity revision and effective coverage then rest on a measure with one demonstrated
predictive relation, stated with its elasticity and the composition shocks that bound it.

**If H1 fails.** What Claude judges itself to have completed and what people return with are different
things: the success rate does not predict the movement of a task's share, and in a corpus where that
measure halves the published productivity estimate and reorders which occupations count as covered, the
three results resting on it inherit the gap. The close names what would close it: a success measure with
a verifiable signal behind it, of the kind the Claude Code work already constructs, published at task
grain.

**If the result is null at the stated power.** Across the 2,427 tasks Claude brought back no more of the
work it judged successful than of the work it judged unsuccessful, to within a correlation of 0.0569 — a
bound the design delivers unweighted, with the usage-weighted version bounded only at 0.31 because a
fifth of the mass sits in ten tasks — while the sample's own edges move more than its middle: 282 nodes
leave and 372 arrive, four-fifths of them within five conversations of the publication floor, so a
measure's predictive content cannot be read off a panel that conditions on survival. The close states
what the next release would have to publish for the test to be decisive: the same task-by-success
intersection at a third window, which the June 2026 telemetry change does not carry, and counts for the
nodes that cross the floor.
