# post4 · Does AI's self-assessed success rate predict which work people keep bringing to it?

*Brief of record. Question, title and contribution freeze at Gate 1b. Candidate LL-09
(`programme/SHORTLIST.md` §6; `programme/LONGLIST.md` LL-09). Carries referee correction 3
(`room/referee-2026-09-16-shortlist-audit.md`), confirmed applied in
`room/referee-2026-09-16-shortlist-audit-2.md` §(c), and the editor's sketch note
`room/editor-2026-09-16-sketch-LL-09.md`.*

**Title form, settled here (editor's note, final paragraph).** The sketch's "AI's *measured* success
rate" presupposes that the label measures success, which is this post's own circularity risk. The
corpus names the instrument inside the noun — "Task success measures **Claude's assessment** of
whether Claude completes tasks successfully" (`economic-index-2026-01-report`, p.21) and "Success is
**Claude's assessment** of whether the conversation was successful"
(`economic-index-2026-03-report`, p.18) — so the question says **self-assessed**. The question says
AI; every finding and every axis label says Claude, and the measure is named on first use as
*Claude's own assessment of whether it completed the task*, thereafter *the success rate Claude
assigns a task*. It is never called a success rate without the qualifier, and a high-success task is
never called better work.

## 1. The question

Does the success rate an AI system assigns its own work on a task predict whether that task's share
of use grows in the next observation window?

## 2. Why it matters, and to whom

The economic question is whether a machine's self-report about its own performance carries
information about where work goes next. Task success is the primitive Anthropic uses to turn raw
usage into economics: it discounts the productivity estimate, it reorders which occupations count as
covered, and it carries the learning-curve result. Anthropic states the validation that would settle
it — "Ultimately, the strongest validation will come from the primitives' ability to capture
meaningful variation in labor market outcomes" (`economic-index-2026-01-report`, 2026-01-15, p.24) —
and no publication in the corpus runs any predictive test of the primitive against anything
observable. What the public data does permit is the nearest available version: does the success rate
in November predict the change in a task's usage share to February.

The reader who decides something differently is the economist or policy analyst who quotes the
success-adjusted productivity revision. The fourth report states it as "implied productivity growth
falls from 1.8 to 1.2 percentage points per year for the next decade based on Claude.ai usage, and to
1.0 percentage points for API traffic" (ibid., p.48), and summarises it as "Adjusting productivity
estimates for task reliability roughly halves the implied gains, from 1.8 to about 1.0 percentage
points" (ibid., p.38). That revision is a reweighting of task-level speedups by this measure. If the
measure has no demonstrated relation to any observable, the revision is a reweighting by an
unvalidated index, and the honest form of the citation changes: from "productivity gains are about
half as large once reliability is accounted for" to "about half as large under Claude's own
assessment of its reliability, which has not been shown to predict anything". The same applies to
effective coverage — "the percent of a worker's day that can be performed successfully by Claude…
calculated as the weighted sum of task success rates" (ibid., p.43) — which is the quantity the
labour-market literature has begun to borrow. The Institute's stated ambition for this data — "We'll
try to be an early warning signal for significant change and disruption" (`institute-agenda-2026-05`,
2026-05-07, *Share 1*) — needs the primitives to be forward-looking, which is exactly what is
untested, and the platform ambiguity the wiki flags (the "about 1.0" of p.38 is the API figure, the
Claude.ai figure is 1.2) is stated wherever the revision is quoted.

Only the Economic Index releases can answer it. They publish, on one taxonomy and at the same grain,
both a per-task success rate that a model assigned by reading transcripts and the same task's share
of a million conversations, in two windows three months apart. No other public source pairs an
LLM-judged success measure with the subsequent usage share of the same named task at this scale;
Microsoft's Copilot study is the one external analogue and it has no second window.

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
success **67%**, N = 999,875; API **49%**, p.26); that success falls as work gets harder — "Claude
assesses personal tasks as successfully completed 78% of the time, versus 61% for software
development. Harder tasks—those requiring more specialized knowledge and where users could not easily
complete them alone—show lower estimated success rates" (ibid., p.26); the task-horizon result (pp.41–42);
and a cross-sectional association with user tenure, where "long-tenure users are about 5 percentage
points more likely to have a successful conversation" before controls and about 4 points with them
(`economic-index-2026-03-report`, 2026-03-24, Fig 2.4 and text pp.17–18).

Where it is open. The fourth report reports no accuracy, agreement or kappa statistic for this
classifier and says only that the nine primitives are "directionally accurate" (p.22), while
recording that "a simple classifier performed better than a nuanced, complex classifier when
compared to human ratings" (p.22) — ledger `L-2026-01-R4-37` **open**: task success has no reported
validation statistic and carries three headline results. The fifth report then raises the reading
that would void its own tenure finding — "This could reflect that higher tenure users are better at
prompting. But what if it reflects that they bring different tasks to Claude—ones more likely to be
successful?" (`economic-index-2026-03-report`, p.18) — ledger `L-2026-03-R5-29` **open**: a model
judging its own success could produce the tenure result with no learning. **Those two are the gap
this post addresses.** `L-2026-01-R4-25` (p.24, quoted in §2) is cited **only as the criterion this
design approximates**: it asks for labour-market outcomes, and a task's share of conversations is not
a labour-market outcome. ⟨mentor⟩ Massenkoff is a lead author of the report that built the success
adjustment and effective coverage (`economic-index-2026-01-report`, p.1, ch.4) and of the report that
first tracked the primitives over time (`economic-index-2026-03-report`, Table 1.1, p.9); the design
follows his stated practice of naming a design's power and publishing nulls — "differential increases
in unemployment on the order of 1 percentage point would be detectable (this will change as new data
comes in, so it is merely a ballpark estimate)" (`labor-market-impacts-2026-03`, p.12). Institute
agenda: `ED-4`, "Productivity growth:" — "What impact will AI have on the rate of innovation and
productivity growth across the economy?" — and `Share 1`, quoted in §2
(`institute-agenda-2026-05`, 2026-05-07).

## 4. Overlap, stated

- **Anthropic, levels and cross-sections.** The corpus publishes success levels by platform, by
  request cluster, by education band and by task horizon, and one cross-sectional regression of
  success on user tenure. *New here:* the first test of whether the measure predicts a later change
  in anything, run on the released aggregates rather than on log-level data.
- **Anthropic, a stricter success measure elsewhere.** The Claude Code paper states the limitation of
  judged success and builds around it — "We do not observe users' real-world outcomes, and we cannot
  ask them directly whether they got what they wanted out of Claude" (`claude-code-expertise-2026-06`,
  PDF p.10) — with "Verified success requires both that the session is judged successful and there is
  at least one hard verifiable signal of success" (ibid., p.10). *New here:* the Economic Index
  primitive is judged-only, and this post asks whether the judged-only version has predictive content
  where the verified version is unavailable.
- **Microsoft Research (Tomlinson, Jaffe, Wang, Counts, Suri, arXiv 2507.07935 v6, 22 Dec 2025).**
  Closest external precedent: an LLM completion measure on 200k Bing Copilot conversations, validated
  against user thumbs feedback — "Completion is highly correlated with direct user feedback
  (weighted … r>0.75; Figure S5), and has the advantage of being available for all conversations, so
  it is not subject to the selection bias of thumbs feedback" (arXiv HTML v6, §Results) — and a scope
  measure whose correlation with the log share of user activity `programme/LONGLIST.md` records at
  r = 0.64. *New here:* the Anthropic-data version, on a second window rather than one
  cross-section, and on a measure with no thumbs validation behind it. The idea is theirs; the test
  on this corpus is not.
- **Separation from post2 (LL-11), per the director's pairs ruling.** The two posts share one series:
  the November 2025 → February 2026 change in a task's Claude.ai usage share at global grain, and
  therefore the same exposure to the February Super Bowl inflow. **This post headlines the
  success-rate relation with the August-2025 share as the instrument**; post2 headlines the
  cross-surface correlation between the API and Claude.ai share changes. This post reports no
  cross-surface correlation and does not decompose coding's share (post3, LL-36); it reports the
  API only as a named exploratory replication (§9). It needs no task → SOC occupation join, so it
  neither states nor inherits post1's multi-holder rule.

## 5. Contribution

If the relation holds, the post supplies the first predictive validation of Anthropic's task-success
primitive and its elasticity — how much of a task's subsequent share growth a point of self-assessed
success buys; if it fails or is null at a stated power, the post shows that the measure carrying the
success-adjusted productivity revision and effective coverage does not predict what users bring back,
and says what the released data would have to contain for the question to be settled.

## 6. Hypotheses

**H1 — Predictive content.** Tasks with a higher November 2025 success rate gain usage share by
February 2026.
*Signature only it predicts:* a positive coefficient on the November success rate in the
usage-weighted regression of the Nov→Feb share change, which survives controlling for the November
share level (instrumented by the August 2025 share) and for the task's November education-years, and
which is **absent in the pre-period placebo** (the same November success rate against the Aug→Nov
share change). Rivals predict a gradient that is either level-driven, complexity-driven or equally
present in the pre-period.
*What counts against it:* a coefficient of zero or negative sign; or a pre-period gradient of the
same sign and comparable magnitude; or a gradient that disappears once education-years enters.

**H2 — Composition, not return behaviour.** Any positive gradient is produced by a change in who was
using Claude in the February window rather than by users returning to work that Claude completes.
*Signature:* the gradient concentrated in tasks whose November profile is consumer-like — low
education-years, high personal or coursework share — and attenuating among tasks whose November
`use_case` mix is work-dominant; the fifth report's named inflow of first-time users is the
mechanism.
*What counts against it:* the gradient is the same size among work-dominant tasks and survives the
`use_case` and education controls.

**H3 — The label is an inverse index of difficulty.** Success is largely a restatement of how simple
a task is, so any gradient records the published drift toward simpler prompts rather than users
returning to what works.
*Signature:* the task's November education-years predicts share growth with the opposite sign and
comparable strength, and the success coefficient loses its magnitude once education-years is
included; Anthropic's own gradient (70% success at below-high-school level, 66% at college level,
`economic-index-2026-01-report`, p.39) is the mechanism.
*What counts against it:* success retains its coefficient with education-years, use-case and the
instrumented level included, and the success–education correlation across tasks is too weak to carry
the result (reported, with the collinearity diagnostics).

**H4 — The movement is at the margin, not among survivors.** What the success measure ranks is which
tasks enter and leave the published sample, not which surviving tasks grow.
*Signature:* February-only entrants carry a higher February success rate than survivors and
November-only exits a lower November rate, while the within-survivor gradient of H1 is flat.
*What counts against it:* the three groups' success distributions are indistinguishable at the stated
power while survivors show the gradient.

## 7. Assumptions sweep

**(1) Value judgement in the framing — *needs a design change; the change is made in this brief*.**
"Success" and "keep bringing to it" both smuggle in approval: that the label measures success, and
that returning to a task is the rational response to it. The change: the question and every finding
use *self-assessed* and name the instrument on first use (see the title-form note above); the post
states that a high success rate is a property of Claude's judgement of a transcript, not of the work;
and growth in a task's share is described as what users brought back, never as what worked. Anthropic
is the authority for the qualifier, not this post: "Success is Claude's assessment of whether the
conversation was successful" (`economic-index-2026-03-report`, p.18).

**(2) Construct mapping — *newly flagged; handled*.** (Marked newly flagged because the sketch asserted the primitive's dependents without mapping the column to the prompt.) The verbatim definition and prompt are in §3:
one binary judgement per conversation, made by a classifier reading the transcript, on whether the
Assistant completed the User's task. At the node the post uses, `onet_task::task_success` `yes`
`_pct`, that becomes the share of a named task's conversations Claude judged successful; no human
rating, no user feedback and no outcome enters it. Anthropic reports no accuracy statistic for it
(p.22) and, in a later paper, treats judged success as insufficient on its own, requiring "at least
one hard verifiable signal" for verified success (`claude-code-expertise-2026-06`, p.10). Handled by:
reproducing the published level first (67% Claude.ai / 49% API, §8) so the column is demonstrably the
published measure; stating the intersection's base (a share of the task's own conversations, not of
the sample); and confining every claim to the self-assessed measure.

**(3) Composition and selection — *needs a design change; the change is specified*.** Units are
conversations, not users, and occupation is inferred from the task rather than the user, so a task's
share can move because the user base moved. Three named shocks sit inside the outcome window:
*(a) the February Super Bowl inflow* — "Our sampling period overlapped with the release of our Super
Bowl advertisements, which brought many first-time users" (`economic-index-2026-03-report`, ch.2
endnote 3, p.18) — first-time users are the low-tenure group whose success rate the same report puts
below the high-tenure group's, so the inflow moves both sides of the relation;
*(b) winter school breaks* — "The drop in coursework conversations was 5 percentage points in
countries where the school term was active and 12 percentage points in the countries where most
students were on break" (ibid., ch.1 endnote 3, p.11); and *(c) Seychelles*, which contributed 24,715
conversations (2.5% of the November global sample) and has **zero rows at any grain** in the February
release (`data/ATLAS.md` §Dated log 2026-09-16 (e) 3), a compositional change that cannot be removed
at global grain because every intersection is global-only. The changes: the November `use_case` mix
and education-years of each task enter as pre-specified controls; H2's primary test is the gradient
among work-dominant tasks against consumer-like tasks; the coursework share enters as the winter-break
exposure; and the Seychelles asymmetry is stated as an unremovable composition term on the outcome,
before the estimate rather than after, with its size (2.5% of the November base) named.

**(4) Anthropic's own results that cut against or bound the framing — *needs a design change; the
change is specified*.** Two published findings can manufacture H1's pattern with no predictive
content at all. First, success is inversely related to difficulty in Anthropic's own measurement:
"tasks requiring less than a high school education (e.g., answering basic questions about products)
attain a 70% success rate, but this drops to 66% for college-level conversations like developing
analysis plans" (`economic-index-2026-01-report`, p.39, Fig 4.1b). Second, the aggregate mix moved
toward simpler prompts in exactly this window: human education fell from 12.21 to 11.92 years,
"statistically significant with p<0.001" (`economic-index-2026-03-report`, Table 1.1, p.9), which the
report reads as "a slight decrease in the aggregate complexity of prompts in Claude.ai" (ibid., p.19).
A positive success–growth gradient is therefore partly the image of a published complexity decline.
The change, and a stated departure from the sketch: the task's November education-years is promoted
from placebo to **pre-specified control and benchmark**, because its coefficient has a known non-zero
prior; the null placebo is the pre-period growth window alone (§10). Cutting the other way, the fifth
report's tenure result has returning users bringing *higher*-education tasks and succeeding more
often (Table 2.1, p.15), which predicts a negative gradient among returning users — so neither sign
is safe to assume, and the post states both priors before the estimate.

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`programme/LONGLIST.md`, LL-09, "Steward
feasibility line"; source `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`):

> "**LL-09. FEASIBLE.** `onet_task::task_success` at `geography=global` (`_count`, `_pct`; `yes`/`no`)
> in both waves. Matching lower-cased task text: **2,886** named tasks common to Nov 2025 and Feb
> 2026; **2,427** carry a Nov-2025 success rate and so enter the regression (91.95% of Nov named
> mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only, 372 Feb-only** — report both. Log (e) 13."

The caveat inside that line is binding and is carried into the design: the regression sample is 2,427
of the 2,886 matched tasks, the estimate is reported with its 91.95% mass share, and the 282 Nov-only
and 372 Feb-only nodes are reported as a margin (H4) rather than dropped silently.

**Cuts, at column level.** The steward's confirming note is `posts/post4/notes/feasibility.md`, which
the steward writes after this brief and which confirms or contradicts each row. Every row is checked
against `data/ATLAS.md` (§Which cuts exist at which grain — Family B; §Cuts that do not exist 7, 10,
21, 26b; §Conventions; §Thresholds; §Traps 1, 5, 7, 11, 24, 25).

| # | release | grain | facet / category | metric | threshold and rule |
|---|---|---|---|---|---|
| 1 | `release_2026_01_15`, `release_2026_03_24` (Claude.ai) | `geography=global`, `level=0` | `onet_task` | `onet_task_pct`, `onet_task_count` | drop `none` and `not_classified` (Traps 24); privacy floor 15 on `_count` applies in both waves; outcome = Δ percentage points on the all-conversation base, second implementation on the named-task renormalised base |
| 2 | same two releases | `geography=global` | `onet_task::task_success`, categories `yes` / `no` | `_pct`, `_count` (two variables only) | per-task success = `yes` `_pct`; steward to confirm `yes` + `no` = 100 per node, else success = yes/(yes+no); rule applied by this post: Nov `_count` ≥ 15, with a 15–20 near-floor sensitivity, because intersections go down to 1 in this wave |
| 3 | `release_2025_09_15` (Claude.ai) | `geography=global`, `level=0` | `onet_task` | `onet_task_pct` | instrument for the November level; matched by lower-cased task text; steward to confirm how many of the 2,427 carry an August share (2,284 nodes appear in all three long waves, ATLAS (e) 9) |
| 4 | `release_2025_09_15` → `release_2026_01_15` | `geography=global` | `onet_task` | `onet_task_pct` | placebo outcome: the Aug→Nov change on the same matched set |
| 5 | `release_2026_01_15` | `geography=global` | `onet_task::human_education_years`; `onet_task::use_case` (`work`, `personal`, `coursework`) | `_mean` (+ `_count`); `_pct` | pre-specified control and benchmark (§7.4) and the composition controls (§7.3) |
| 6 | `release_2026_01_15`, `release_2026_03_24` (1P API) | `geography=global` | `onet_task`, `onet_task::task_success` | `onet_task_pct`; `yes` `_pct` | exploratory replication only (§9); the API has no geography and no `usage_count` |

Matching is on lower-cased, stripped task text, with rows in, matched and unmatched printed
(ATLAS §Taxonomies: "Never diff cluster sets across waves without an explicit name match and a report
of the unmatched names"). Two counts must be reconciled in the steward's note: the atlas records
2,888 `onet_task` names matching across the two waves and the feasibility line 2,886 *named* tasks —
the difference is expected to be the two pseudo-nodes `none` and `not_classified`. Files are read with
`keep_default_na=False, na_values=[]` and `level` cast to string after any parquet read (Traps 1, 2, 7).
The 200/100 geography thresholds do not bite: every cut is at global grain. **No supplementary data
and no external join**; there is nothing outside the Index this question needs.

**The published number reproduced first** (criterion 3). Global Claude.ai task success **67%**,
Figure 2.2, p.25, N = 999,875, and the platform pair **67% vs 49%**, p.26, both from
`economic-index-2026-01-report` on `release_2026_01_15`; reproduced from `task_success` `yes` `_pct`
at `geography=global` on each platform file, with the base stated (every `{facet}_pct` is a share of
the geography's total *including* `not_classified`, ATLAS §Other bases). No published number exists
for the per-task success rates or for their relation to share growth; the February global level
(`yes` 69.938%, ATLAS §Cuts 26b) is a data fact, not a published figure, and is reported as such.

## 9. Confirmatory tests and the exploratory allowance

Four confirmatory tests, one per hypothesis, run once after the pre-registration is committed.

1. **H1.** Usage-weighted regression of the Nov→Feb change in a task's global share on its November
   success rate, over the 2,427-task sample, controlling for the November share level instrumented by
   the August 2025 share and for November education-years; heteroskedasticity-robust errors. Reported
   with the headline comparison: the usage-weighted difference in subsequent share growth between the
   top and bottom November-success quartile. Decision rule and power: with 2,427 tasks a correlation
   of about **0.057** is detectable at 80% power and 5% two-sided (MDE = 2.8 × SE); because the
   estimator is usage-weighted and task mass is concentrated (the top ten tasks are 19.4% of the
   February named mass, ATLAS §Conventions), the **Kish effective N** and the MDE implied by it are
   reported beside the nominal figure, and the null is declared against the weighted MDE, not the
   nominal one.
2. **H2.** The same regression with the November `use_case` shares entered, and the success
   coefficient estimated separately for work-dominant and consumer-like tasks (split at the
   pre-registered median of the November `work` share); the difference between the two coefficients
   is the test.
3. **H3.** The success coefficient with and without November education-years, reported beside the
   across-task success–education correlation and pairwise collinearity; the test is whether the
   success coefficient survives at a magnitude the education channel cannot account for.
4. **H4.** Success rates of the three groups — survivors, 372 February-only entrants, 282
   November-only exits — compared on their own wave's success rate, with the MDE for each comparison,
   against the within-survivor gradient from test 1.

**Exploratory allowance: three tests, no more, each labelled exploratory in the post and barred from
the headline.** (i) Shape: quartile or decile bins of the November success rate instead of the linear
term, to show whether a linear coefficient hides a threshold. (ii) Population: the same H1
specification on the 1P API global frame in both waves, to see whether a relation found on the
consumer surface appears on a work-dominant one. (iii) Direction: the reverse regression of the
change in a task's success rate on its November share, which asks whether growth predicts success
rather than the converse. Any further question is logged for a later post.

## 10. Noise and robustness required

- **Persistence across windows / placebo.** The pre-period test — November success against the
  Aug→Nov share change — is the null placebo, and the only one. It is read as follows: a gradient of
  the same sign and comparable magnitude in the pre-period means the relation is a standing
  task-level correlate, not prediction. Its expected sign under pure sampling noise is the mirror of
  the main test's, since the November share enters the two changes with opposite signs, so the
  magnitude comparison is stated together with the noise check below. The education-years term is
  **not** a null placebo (§7.4): its prior is non-zero because the published aggregate moved, and it
  is reported as a benchmark coefficient.
- **Flagged units excluded by rule, shown separately.** Tasks whose November `onet_task::task_success`
  `_count` is 15–20 (near-floor) excluded in a sensitivity run and shown separately; `none` and
  `not_classified` dropped throughout; the Seychelles asymmetry stated and its unremovability at
  global grain named.
- **Leave-one-out.** The ten largest tasks dropped one at a time under the usage-weighted estimator,
  with any mover named; plus a count-based bootstrap over the published `_count` columns, so that a
  coefficient inside the resampling band is reported as such.
- **Second implementation.** The panel and both estimates rebuilt by a second route — shares from
  `_count` columns against shares from `_pct` columns, and the regression re-run in a second
  implementation — agreeing to the reported precision before any number enters the post.
- **Synthetic recovery.** A known gradient injected into simulated task shares must be recovered and
  a zero gradient must be reported as zero, including under the instrumented level control.

## 11. Literature check

Searches run (2026-09-16): the corpus itself for every use of `task success` in `wiki/reports/`
(fourth report chs.2 and 4, fifth report ch.2, the Claude Code paper's judged/verified distinction);
arXiv for an LLM self-assessed completion measure validated against usage — which returns Tomlinson
et al., fetched and verified today at `arxiv.org/abs/2507.07935` (v6, 22 Dec 2025, 40 pp, Microsoft
Research, 200k Bing Copilot conversations); and `programme/LONGLIST.md`'s recorded checks of Bick,
Blandin, Deming & Schumacher (2026) — exposure explains "roughly half" of adoption variation, with who
the worker is mattering more, the rival explanation to task quality — and METR (2025), on measured
outcomes diverging from believed ones. Closest prior work is Tomlinson et al.: an LLM completion
measure validated against user thumbs feedback, with a companion scope measure correlated with the
log share of user activity (r = 0.64 as recorded in the long-list). This post sits one step to the
side of it: a measure with no feedback validation behind it, tested across two windows rather than
within one, on the only corpus where the same classifier's judgement and the same taxonomy's usage
shares are published together.

## 12. What the closing section will be able to say

**If H1 holds.** People bring back the work Claude says it completed: a point of self-assessed
success in November is associated with a stated amount of subsequent share growth by February, and
the relation is absent in the window before the measurement, which is the first evidence that the
primitive is tracking something outside its own output. The productivity revision and effective
coverage then rest on a measure with one demonstrated predictive relation, stated with its
elasticity and with the composition shocks that bound it.

**If H1 fails.** What Claude judges itself to have completed and what people return with are
different things: the success rate does not predict the movement of a task's share, and in a corpus
where that measure halves the published productivity estimate and reorders which occupations count as
covered, the three results that rest on it inherit the gap. The close names what would close it — a
success measure with a verifiable signal behind it, of the kind the Claude Code work already
constructs, published at task grain.

**If the result is null at the stated power.** The tasks entering and leaving the published sample
move more than the tasks that stay: with the margin at 282 November-only and 372 February-only nodes
against 2,427 survivors, the measure's predictive content cannot be read off a panel that conditions
on survival, and the reported bound — nothing larger than the weighted minimum detectable effect —
is the size of what a two-window panel of this shape can exclude. The close states what the next
release would have to publish for the test to be decisive: the same intersection at a third window,
and counts for the nodes that appear and disappear.
