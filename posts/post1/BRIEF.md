# post1 · Is AI delegated more on cheap work or on expensive work?

*Brief of record (LL-07, Σ 28, rank 1), amended once on `posts/post1/notes/feasibility.md` and
`room/steward-2026-09-16-feasibility-post1.md`. Question, title and contribution freeze at Gate 1b.*

## 1. The question

Does the share of AI use that is delegated outright rather than worked through collaboratively rise
or fall with the wage of the work being done?

## 2. Why it matters, and to whom

The sign of that gradient is the sign of the first-order labour-share effect: delegating expensive
work moves a large wage bill, delegating cheap work a small one. Anthropic's own scenario paper makes
the point by construction, measuring "the importance of each task by its initial share of total labor
payments: m_i ≡ s_i,t0/s_L,t0" (`econ-scenarios-paper-2026-09`, 2026-09, p. 9), while the automation
share the Economic Index publishes counts conversations and weights every task the same. If
delegation is concentrated at one end of the wage distribution, an unweighted automation share is the
wrong input to a wage-bill model, and wrong in a knowable direction.

Who decides differently. Anyone calibrating an exposure or automation parameter: the scenarios paper
holds its automation share ψ constant at 0.50 / 0.75 / 0.90 by assumption, and its affected-mass
anchor is "observed exposure, averaged over occupations" without saying whether that average is
employment- or wage-bill-weighted (ibid., Table 1 p. 23; open ledger item `L-2026-09-SCPA-27`).
Anyone reading a published automation share as a statement about the economy: it is a conversation
count, and this post says how much of the wage bill sits behind it. And anyone weighting delegation
against augmentation in a labour-market measure — observed exposure sets α = 1/2 + 1/2 × automation
share, so "A task with only automative uses would have α_t = 1"
(`labor-market-impacts-2026-03-appendix`, 2026-03, p. 3), a wage-blind weighting of a wage-relevant
quantity.

What this data can say that nothing else can. The Economic Index publishes the collaboration facet
crossed with the O\*NET task at global grain in three waves, with per-task usage weights in the same
wave. No survey and no job-posting series observes how a given task was actually worked on, at task
resolution, on a million-conversation sample, and that cross with a wage exists in no publication.

## 3. The thread of Anthropic's inquiry this builds on

Thread T3 (automation versus augmentation, delegation and autonomy) with T4 (task-level primitives).
The taxonomy is fixed and repeated across six waves:

> "At a high level, we distinguish between automation and augmentation modes of using Claude:
> Automation encompasses interaction patterns focused on task completion: Directive: Users give
> Claude a task and it completes it with minimal back-and-forth; Feedback Loops: Users automate tasks
> and provide feedback to Claude as needed. Augmentation focuses on collaborative interaction
> patterns: Learning… Task Iteration… Validation…"
> (`economic-index-2025-09-report`, 2025-09, PDF p. 9)

> "'Directive' conversations, where users delegate complete tasks to Claude"
> (`economic-index-2025-09-report`, 2025-09, PDF p. 3)

The corpus prices the work, and prices the compute, and never prices the delegation.
`economic-index-2026-03-report` (2026-03) prices the task mix — "Another way to measure the change in
the mix of tasks done on Claude is to look at the change in the average value of tasks, which we
define as the average hourly wage of US workers who perform that task" (p. 8) — and reports "$49.3 to
$47.9" (p. 8, Fig. 1.4); it sorts *model choice* by that same wage, "for every additional $10 of
hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points for
Claude.ai users" (p. 14, Fig. 2.2). `economic-index-2026-06-report` (2026-06) sorts *compute* by it:
"more compute is associated with more valuable artifacts; the tokens a given output consumes rise
with the estimated value of the work" (pp. 2–3; Fig. 2.3, body p. 12, caption p. 13). ⟨mentor⟩ Both
wage cuts are the mentor's chapters.

What the thread has established: the five-pattern split, its five-wave Claude.ai series, the API's
automation dominance, and delegation's rise with the agentic surface. Where it is open: the
collaboration facet is crossed with occupation and with category and never with wage
(`programme/LEDGER.md` `L-2025-02-R1-16`, *partially answered* — "the wage cross is published
nowhere"); automation share by wage or Job Zone "was one join away (the facets were intersected) and
is never shown" (`L-2025-02-P1-22`); and the affected-mass weighting is unstated
(`L-2026-09-SCPA-27`, *open*). The published result closest to the question is a null on a
neighbouring ordering: "the automation share is essentially unrelated to the human levels of
education required to write the prompt" (`economic-index-2026-01-report`, 2026-01, p. 40).

## 4. Overlap, stated

- **Anthropic, task value.** The task mix is priced by occupational wage across five windows and two
  platforms (`economic-index-2026-03-report`, Fig. 1.4 p. 8). New here: the wage is crossed with how
  the work was done, not with how much of it there was.
- **Anthropic, wage gradients in other measures.** Opus share rises with task wage (ibid., Fig. 2.2
  p. 14); tokens rise with mapped-occupation wage (`economic-index-2026-06-report`, Fig. 2.3 p. 13).
  New here: the same gradient on the collaboration facet, which those two chapters leave untouched.
- **Anthropic, the education null.** Automation share is flat in required human education
  (`economic-index-2026-01-report`, p. 40). New here: wage is not education — it is the price of the
  labour a task displaces, and the quantity the scenario framework weights by.
- **Chatterji et al. (2025), "How People Use ChatGPT".** Work usage concentrates in highly paid
  occupations and "Doing" exceeds "Asking" in work messages; the split is never regressed on a wage.
  New here: that gradient, estimated.
- **Tomlinson et al. (2025), "Working with AI".** Wage and education against an AI *applicability*
  score, plus a delegate-versus-assist prediction. New here: the gradient sits in the delegation
  measure itself, on observed usage and on a different surface.
- **Acemoglu (2025), "The Simple Macroeconomics of AI".** The theory that the wage bill of automated
  tasks is what moves the labour share, with no usage measurement. New here: the measurement.

**Separation from its pair partners** (`programme/SHORTLIST.md` §5, pair 3). post3 (LL-36) is
composition *inside* one occupational category; post8 (LL-30) is the work/coursework use-case mix.
All three build the same task → SOC join and must fix the same multi-holder rule; under the
director's sequencing ruling this post is written first and states that construction in §8, and the
other two cite it rather than re-deriving it. No other post estimates a wage gradient in the
collaboration facet.

## 5. Contribution

If the gradient is positive, the post supplies the wage-weighted automation share that an unweighted
one understates and names the wage bill behind a published number; if it is negative, it shows that
the expensive work is the work people stay inside, which is the observable form of the
labour-augmenting reading; if it is flat at a stated power, it publishes the first
wage-by-collaboration table in the corpus and extends Anthropic's education null to the price of the
work.

## 6. Hypotheses

**H1 · Price gradient (delegation rises with the wage of the work).** The usage-weighted automation
share is higher for high-wage tasks than for low-wage tasks.
*Signature only it predicts:* a top-minus-bottom wage-quartile difference that is positive and
outside the MDE in **all three** waves, is monotone across the four quartiles in at least two of
them, and survives both the exclusion of Computer & Mathematical (SOC-15) tasks and the
within-major-group estimator.
*What counts against it:* a negative or inside-MDE difference in any wave; a positive difference that
loses more than half its size or its sign when SOC-15 tasks are dropped (that is H3); a sign flipping
between the two wage sources; a difference inside the permutation null's central 95%.

**H2 · Inverse gradient (the expensive work is the collaborative work).** The usage-weighted
automation share falls with the wage of the work.
*Signature only it predicts:* a negative, outside-MDE top-minus-bottom difference in all three waves
**with** the augmentation components rising in wage — learning, task-iteration and validation shares
each weakly increasing across quartiles — rather than the `none` residual moving.
*What counts against it:* a positive or inside-MDE difference in any wave; a negative difference
carried by the residual rather than by the five classified patterns; a negative difference that
disappears within major group.

**H3 · Composition, not price.** Any gradient is carried by one occupational family — coding tasks
are both high-wage and the most delegated — so wage is standing in for a task family.
*Signature only it predicts:* a gradient outside the MDE overall that falls inside it when SOC-15
tasks are excluded or when estimated within major group, and a leave-one-group-out series in which
one group's removal moves the estimate by more than all others combined.
*What counts against it:* the gradient's size and sign surviving all 22 leave-one-group-out
re-estimates and the within-group estimator, in all three waves.

**H4 · No relation (the null the design can deliver).** The automation share does not track the price
of the work, extending the published education null.
*Signature only it predicts:* |top-minus-bottom| whose two-sided 95% interval lies inside **±1 pp**
in all three waves — the pre-registered equivalence margin, set at more than twice the MDE(80%) of
0.42–0.43 pp that the primary variance model delivers (§9(4); `posts/post1/notes/feasibility.md` §4)
— with no monotone ordering across quartiles and a continuous slope indistinguishable from zero.
*What counts against it:* any wave whose interval excludes zero with a consistent sign across waves;
an ordering that is monotone in all three waves even if each difference is small.

## 7. Assumptions sweep

**(1) Value judgement in the framing — "cheap", "expensive", "delegated". Marked: handled, with a
wording rule.** The frame prices work by the wage of the people who do it, which is Anthropic's own
construct — "the average hourly wage of US workers who perform that task" and, where several
occupations do it, "we average their wages weighting by employment and the fraction of time spent on
that task" (`economic-index-2026-03-report`, 2026-03, p. 8 and footnote 5 p. 11). A wage is the price
of the labour a task displaces, not a measure of the work's worth, and the title's "cheap" and
"expensive" are shorthand for that price. Rule adopted, since question and title freeze at Gate 1b:
the title keeps the editor's ruling ("'Delegated', 'cheap' and 'expensive' are the corpus's own
terms", `room/editor-2026-09-16-sketch-LL-07.md`) and the body says "the wage of the work"
throughout; neither direction of the gradient is called good or bad, and the labour-share reading is
stated as a consequence for a model input, not as a verdict.

**(2) Construct mapping. Marked: needs a design change — change made.** The measure is a classifier
on conversations: "**automation_pct**: Percentage of classifiable collaboration that is
automation-focused (directive, feedback loop patterns)"
(`release_2025_09_15/data_documentation.md`, quoted in `economic-index-2025-09-report`, 2025-09,
Definitions). It is not a count of tasks automated, and it is not autonomy: "'Translate this
paragraph into French' is high automation (directive, minimal back-and-forth) but low AI autonomy"
(`economic-index-2026-01-report`, 2026-01, p. 19). Both are said in the post. The mapping that
needed the change is the wage: Anthropic's task value uses BLS OEWS May 2024 with employment *and*
time-on-task weights (footnote 5, p. 11); the public files carry neither OEWS (which 403s from this
sandbox) nor any time-on-task weight, and a public rebuild returns $35.34 → $35.08 → $34.36 against
the published $49.3 → $47.9. **Design change:** the post is rank-based. Tasks are sorted into
usage-weighted wage quartiles — Anthropic's own convention, "Wage quartiles are calculated using BLS
data, weighted by number of transcripts" (`economic-index-2026-06-report`, 2026-06, Fig. 1.3 caption
p. 7) — the headline is a quartile difference, the dollar slope is secondary and carries the
non-reproduction in its caption, and no wage level is reported as Anthropic's.

**(3) Composition and selection. Marked: needs a design change — change made.** The unit is a
conversation on Claude.ai, and "occupation is inferred from the task, not the user"
(`/mnt/memory/standards/terminology.md`; `economic-index-2026-06-report`, 2026-06, p. 7: "While we
can't conclusively identify the jobs of the people making these requests…"). A task's wage is
therefore the wage of work that *resembles* it. Three mixes could produce a gradient without any
price mechanism: coding tasks, high-wage and the most delegated, carrying the whole relation; the
February wave's Super Bowl inflow of new consumer users changing the task mix under the same global
label; and Seychelles (`SC`), 2.47% of the November wave, excluded by the report but not by the file
(`data/ATLAS.md` §Traps 14). **Design change:** H3's within-major-group estimator and the 22
leave-one-group-out re-estimates are confirmatory, not robustness; each wave is reported separately
and never pooled; November is re-estimated with `SC` netted out of the task weights and, because the
global-only intersection leaves its automation rates uncleanable, with the pre-registered drop of
the tasks it dominates (§8 C8, §10); and the finding is stated about Claude.ai conversations, with
one sentence on what generalises.

**(4) Anthropic's own results that cut against or bound the framing. Marked: newly flagged, carried
into the post.** Three. First, the published education null — "the automation share is essentially
unrelated to the human levels of education required to write the prompt"
(`economic-index-2026-01-report`, 2026-01, p. 40) — is a real prior for H4 on a correlate of wage,
and the post reports the wage gradient beside it rather than in ignorance of it. Second, Fig. 2.2's
Opus gradient (2026-03, p. 14) means the expensive work already draws the more capable model, so a
positive gradient may be a demand-for-intelligence result rather than a delegation one; the post says
so, and the pattern-level split is the exploratory probe. Third, the corpus insists automation and
autonomy are distinct constructs (2026-01, p. 19), so the June finding that compute and autonomy rise
with the value of the work does **not** predict this gradient's sign; it is motivation, not a prior.

## 8. Data, confirmed at column level

**Steward's feasibility line, verbatim** (`programme/LONGLIST.md` LL-07; originally
`room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`):

> "**LL-07. FEASIBLE.** `onet_task::collaboration` exists at `geography=global` in all three long
> waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259 tasks, with global `onet_task_pct`
> weights in the same wave. Wage coverage is near-total, not marginal: through the shipped O\*NET
> 20.1 statements to `wage_data.csv` after `MedianSalary > 100` (1,084 of 1,090 rows), **99.4% /
> 99.0% / 99.3%** of *named*-task usage mass carries a wage. State the multi-holder rule (a task's
> wage is an aggregate over the occupations holding it). Log (e) 7."

The caveat is the last sentence and it is discharged below. The steward's confirming note is
**`posts/post1/notes/feasibility.md`** (verdict **FEASIBLE WITH CAVEAT**; corrections in
`room/steward-2026-09-16-feasibility-post1.md`): C1–C3 and C5 confirmed at column level, C4, C6, C7
and C8 amended below on his numbers, and §9(4)'s variance model and equivalence margin reset on his
power table.

**Cuts, at column level.**

| # | release (window) | grain | facet / category | metric | threshold / base |
|---|---|---|---|---|---|
| C1 | `release_2025_09_15` (4–11 Aug 2025), `platform_and_product = "Claude AI (Free and Pro)"` | `geography = global` | `onet_task::collaboration` (14,454 rows, `level` `'0'`) | `_pct` and `_count` per (task, pattern) | privacy floor is **1**, not 15; all seven patterns present; per-task `_pct` sums to 100; the intersection publishes 100.00% of base named counts, so there is no cell suppression inside it |
| C2 | `release_2026_01_15` (13–20 Nov 2025), same platform label (sample is Free, Pro and Max) | `geography = global` | `onet_task::collaboration` (16,778 rows) | `_pct`, `_count` | same; classified 92.34% / `none` 2.02% / `not_classified` 5.64% of named counts; Seychelles sensitivity at C8 |
| C3 | `release_2026_03_24` (5–12 Feb 2026), `"Claude AI (Free, Pro, and Max)"` | `geography = global` | `onet_task::collaboration` (17,530 rows) | `_pct`, `_count` | same; counts are on a 1,000,000 sample base (named tasks carry 929,714) |
| C4 | each of C1–C3, same wave | `geography = global` | `onet_task` base facet | `onet_task_pct` (sums to exactly 100), `onet_task_count` (floor 15) | the usage weight. **The two frames have different residuals:** the base facet is named + `none` + `not_classified` (2,618 / 3,170 / 3,260 nodes), the intersection is named + `none` only (2,617 / 3,169 / 3,259). The analysis universe is the **2,616 / 3,168 / 3,258 named** nodes; dropping the two residual base nodes removes 8.13 / 6.49 / 7.03 pp of usage mass, not one node's worth |
| C5 | `release_2025_09_15/data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 × 9, 974 codes, 18,428 lower-cased keys) | — | task → O\*NET-SOC | `Task ID`, `O*NET-SOC Code`, `soc_major_group` | join key is the **lower-cased, stripped** task text, de-duplicated on that key before the merge (up to 34 rows on one key; `data/ATLAS.md` §Traps 21). Confirmed: 2,616 / 3,168 / 3,258 named nodes in, **all matched**, 0 unmatched, 0 collisions |
| C6 | `release_2025_02_10/wage_data.csv` (O\*NET website wage scrape, Kilbourne-Quirk 2019 — **not** a BLS series) | — | occupation wage, primary | `MedianSalary` (annual), filtered `> 100` (1,084 of 1,090 rows) | join on the **full 10-character `O*NET-SOC Code` → `SOCcode`**, which is what Anthropic's released `plots.ipynb` (cell 26) does: **970 of 974** occupations. The `[:7]` prefix key stated in the first version of this brief matches **0 of 775** and is withdrawn. ÷ 2080 for an hourly rate is this post's conversion, not Anthropic's, and is labelled as such; `MedianSalary` is top-coded at $208,000 (6 occupations, 0.05–0.06% of analysis mass); `-1` is a missing sentinel in `JobZone`/`ChanceAuto` (`§Traps 10`). Coverage: 2,607 / 3,154 / 3,244 tasks = **99.35 / 98.98 / 99.30% of named mass** |
| C7 | BLS Employment Projections (`data.bls.gov/projections/occupationProj`, 200, 831 detailed-SOC rows) | — | occupation wage, second source | `Median Annual Wage 2025` on `occ_code`; `Employment 2025` for the multi-holder rule | join `soc7` → `occ_code`, 775 in, **670 matched**. Prices **55.66 / 58.52 / 62.22% of named mass** (51.14 / 54.73 / 57.85 pp of the wave) against C6's 99%; used for rank and sign agreement (Spearman 0.9869 / 0.9859 / 0.9870 against C6), never for a level. OEWS, Anthropic's own source, 403s from this sandbox |
| C8 | `release_2026_01_15`, country rows | `geography = country` | `onet_task` | `onet_task_count` for **`SC`** (ISO-2 in this wave; `SYC` returns 0 rows) | Seychelles is 24,715 conversations, 2.47% of the wave. **The netting reaches the weights only**: `SC` has 0 rows of `onet_task::collaboration`, because intersections are global only, so the per-task automation *rates* cannot be cleaned of it. Restated as two cuts: (a) net `SC` out of the November task weights (mean |shift| 0.0012 pp, up to 0.58 pp on one task); (b) a pre-registered drop of the tasks where `SC` exceeds 10% of the global count (23 tasks, 11.59 pp of wave mass, of which **9.04 pp sits in the top wage quartile**), with the >20% variant (14 tasks, 1.97 pp) beside it |

Grain rule observed: intersections are **global only** in all three long waves (`data/ATLAS.md`
§Cuts 10), so there is no country or state version of this post; `soc_occupation` is absent as a
facet in the two 2026 waves (§Cuts 13), which is why H3's occupational split runs through C5.

**The task → SOC join, the O\*NET-SOC vintage and the multi-holder rule, stated here for the
construction triple.** A task text is joined to O\*NET-SOC through C5 on the lower-cased stripped
task text, de-duplicated on that key, and priced through C6 on the **full 10-character O\*NET-SOC
code**.

*Vintage, as a stated choice and not an inherited default.* The shipped 20.1 statements file carries
**2010** O\*NET-SOC codes and `wage_data.csv` joins to exactly those codes (970 of 974); the 2019
taxonomy — "This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage"
(`economic-index-2026-03-report`, 2026-03, footnote 2 p. 11) — is reachable only through the external
O\*NET Center crosswalk scripted at `data/fetch/supplementary_onet.py`, and Anthropic's published
occupational series reproduces only on that recode (`posts/post2/notes/feasibility.md` §2). The rule
adopted: **the wage is attached on the shipped 2010 codes**, the only taxonomy the wage file joins
to; **any occupational grouping** — H3's major groups, the SOC-15 exclusion, anything set beside a
published occupational number — is reported on the **2019 recode** as primary with the 2010 grouping
beside it as robustness. post3 (LL-36) and post8 (LL-30) cite this paragraph, vintage rule included,
and state which vintage their coding set uses.

*Multi-holder.* Where a task is held by more than one occupation it has no single wage. Anthropic's
rule is employment-and-time weighted (footnote 5, p. 11); the public files carry no time-on-task
weight, so the pre-registered primary rule is the **employment-weighted mean over holder
occupations** (BLS-EP employment on `occ_code`), the nearest analogue of Anthropic's definition, with
the equal-split mean and the modal holder beside it in every table. BLS-EP employment is published at
7-character SOC only, so that rule is identified across distinct 7-char SOCs and degenerates to the
equal-split mean for the two tasks whose holders sit inside one. The exposure is small and bounded: a
task text maps to one 10-character code for all but **74 / 93 / 86** tasks (Aug / Nov / Feb) —
72 / 91 / 84 at 7-char SOC, **4.44 / 5.98 / 4.87% of named** usage mass — the equal-split and
employment-weighted wages correlate at **0.9998** with a maximum single-task gap of $6.38/hr, and the
three rules move the SOC-15 share by **≤ 0.17 pp** and the 22-group ranking by at most one position
(Aug) or none (Nov, Feb) (`posts/post1/notes/feasibility.md` §1 C5). That bound is on an occupational
share, not on this post's gradient, so it is context and the gradient is re-estimated under all
three rules.

**The published numbers this reproduces first.** (i) The wave's own global collaboration split, on
the base each report used: 49.0980 (Aug 2025, all seven patterns, published "49%"), 45.3554 (Nov
2025, all conversations, "45%"), 44.1569 (Feb 2026, all conversations, "44%") — and the same three on
the five-classified-pattern analysis base (0.5107 / 0.4674 / 0.4555), the base named every time; all
six reproduced by the steward to four decimals. (ii) The estimator itself is Anthropic's: the released
`collaboration_task_regression` returns Figure 2.11 exactly (−3.111834, partial R² 0.393687, N 111)
on the machinery this post extends. Its released spec drops the `not_classified` task node, keeps the
`none` task node, drops the `none`/`not_classified` patterns from each task's base and renormalises;
this post's universe is the named nodes, and the released variant keeping the `none` node is a
robustness cut. (iii) The internal check that licenses the estimator: the usage-weighted mean of the
per-task automation shares must return the wave's five-pattern value **within 0.36 pp and positive in all three waves** — it
returns +0.1303 / +0.2931 / +0.3510, and the gap is not suppression (the intersection publishes
100.00% of base named counts) but the named-task restriction plus the intersection's own
`not_classified` *pattern*, which the marginal facet does not carry (4.64 / 5.64 / 5.90% of named
counts). A tolerance of "rounding", as first written, would have failed a check that passes.
(iv) Stated as a **known non-reproduction**, not attempted: Anthropic's $49.3 → $47.9 task value
rebuilds as $35.34 → $35.08 → $34.36 (C6) and $37.64 → $37.69 → $37.55 (C7), direction preserved
(−$0.72 against the published −$1.40) — which is why the design is rank-based.

**The analysis set.** Tasks with a C6 wage and at least one classified-pattern cell: **1,802 / 2,075
/ 2,188** tasks, **97.15 / 96.23 / 96.52% of named mass**, on 818,673 / 854,432 / 848,716 classified
conversations. Both losses are audited and reported: 5 / 12 / 12 tasks with a classified cell and no
wage, and 805 / 1,079 / 1,056 with a wage and no classified cell, dropped explicitly, never zeroed.

## 9. Confirmatory tests and the exploratory allowance

1. **H1 / H2 — the key number.** Per wave, the usage-weighted automation share of the top wage
   quartile of tasks minus that of the bottom, on the five-classified-pattern base, with the `none`
   share beside it in every table so the base is never implicit, and quartile boundaries drawn on
   usage-weighted wage. Decision rule: H1 if positive and outside the MDE in all three waves; H2 if
   negative and outside it in all three; anything else goes to H3 or H4.
2. **The continuous companion.** The usage-weighted slope of the automation share in the task's
   hourly wage, per +$10/hr in the form Anthropic uses for its Opus gradient, sign and significance
   only.
3. **H3 — composition.** The same difference (a) with SOC-15 tasks excluded — 39.86 / 37.12 / 33.11%
   of analysis mass, so that exclusion is a third of the sample and dominates the leave-one-out
   series by construction, which the post states; (b) estimated within SOC major group and averaged
   by usage weight **over the groups that span the global bottom and top quartile (7 / 8 / 6 of 22
   span all four)**, the rest reported as not identified rather than as zeros; (c) as 22
   leave-one-group-out re-estimates.
4. **H4 — the null, under one named variance model.** Primary variance model: **conversation-level
   binomial on the classified counts, with the task mix held fixed** — the right model for a
   statement about the conversations in these three windows. Its MDE(80%, two-sided 5%) is
   **0.42 / 0.42 / 0.43 pp** (`posts/post1/notes/feasibility.md` §4), so the pre-registered
   equivalence margin is **±1 pp**: the null is declared only if the two-sided 95% interval for the
   quartile difference lies inside ±1 pp in all three waves. That margin is more than twice the MDE,
   and it is reset from the ±3 pp of this brief's first version, which the steward showed was not
   deliverable under the task-resampling bootstrap that version specified (MDE 3.26 / 3.44 / 3.68 pp).
   The design-based model — resampling tasks equal-probability, which generalises to other task
   mixes — is reported beside it as the bound it is: MDE 12.5 / 17.4 / 16.1 pp, resolving nothing
   below about 12 pp, so the null is a statement about these windows' conversations and the post says
   so in that sentence. The **Kish effective N** on the `onet_task_pct` weights is printed beside the
   nominal count throughout (referee correction 2): **99.7 / 89.5 / 134.3** against a nominal
   2,616 / 3,168 / 3,258, and **11.5 to 16.5 tasks** in the top wage quartile — which is why the
   task-level models cannot carry a null and the conversation-level one is named in advance.

**Exploratory allowance: three tests, after the confirmatory set, none in the headline and each
labelled exploratory in the post.** (a) The same gradient on the 1P API global intersection, to say
whether the sign is a property of the surface rather than of the work — the API is
automation-dominant by construction, so this is context, not a replication. (b) The pattern-level
split: which of directive and feedback loop carries a positive gradient, and whether learning, task
iteration and validation move the other way — the probe for the demand-for-intelligence rival in
§7(4). (c) The gradient against `JobZone` from C6 (99.8% of named mass, `-1` sentinels dropped) as a
non-wage ordering, to separate price from required preparation. No further tests; any additional cut
is a deviation and is logged as one.

## 10. Noise and robustness required

- **Persistence across windows** — in the confirmatory rule: three waves, each estimated and reported
  separately, never pooled and never spliced.
- **Leave-one-out** — 22 leave-one-group-out re-estimates (confirmatory under H3) and a leave-out of
  the ten largest tasks by usage mass, 19.4410 pp of the Feb-2026 wave total and **20.91% of named**
  mass (Aug 24.97%, Nov 25.93%); the denominator is stated each time.
- **Flagged units excluded** — Seychelles is `SC` in this wave and is 2.47% of it, and the netting
  reaches the task **weights** only: `SC` publishes no intersection rows, so November's per-task
  automation **rates** cannot be cleaned of a geography that reaches 64% of an individual task's
  global count and sits behind 9.04 pp of the top wage quartile. Three things follow, all
  pre-registered: the weight-netted re-estimate; the drop of tasks where `SC` exceeds 10% of the
  global count (23 tasks, 11.59 pp of wave mass), with the >20% variant beside it; and November
  treated as the wave corroborated by August and February rather than as independent confirmation.
  Utah's August anomaly is a `state_us` row and cannot move a global intersection; the post says that
  rather than silently ignoring it. Tasks whose intersection `_count` falls below a pre-registered
  floor are excluded in a sensitivity cut, since the published floor is 1.
- **Placebo** — a permutation null: the wage vector is permuted across tasks within SOC major group
  and the estimator re-run, giving the distribution of the quartile difference under no
  wage–delegation relation; the observed statistic is reported against that distribution.
- **Second implementation** — the gradient rebuilt independently by the analyst on the second wage
  source (C7) and under the two alternative multi-holder rules, sign agreement required for any
  claim, with the wage join re-run from the task side and the SOC side as two separate builds.

## 11. Literature check

Searches run for the long-list entry and re-checked for this brief: Anthropic's own corpus
(`wiki/reports/`, every Economic Index report and appendix, the labour-market and scenarios papers)
for "wage", "value", "collaboration", "automation share"; and the external comparators in
`data/ATLAS.md` §Supplementary sources. Closest prior work: **Chatterji et al. (2025)**, the nearest
rival measurement — an Asking/Doing split on a consumer surface with work usage concentrated in
highly paid occupations, never regressed on a wage; **Tomlinson et al. (2025)**, where the wage
enters an applicability index rather than the delegation measure, on Copilot conversations;
**Acemoglu (2025)**, which supplies the reason the sign matters and no measurement; and **Anthropic**,
which prices tasks (2026-03 Fig. 1.4), model choice (Fig. 2.2) and tokens (2026-06 Fig. 2.3) by wage
and publishes a null for automation share against required education (2026-01 p. 40), while crossing
the collaboration facet with wage nowhere. This post sits in the empty cell: a usage-weighted
estimate of the delegation share as a function of the price of the work, on Anthropic's own published
intersection, in three waves.

## 12. What the closing section will be able to say

**If H1 holds.** The work people hand over to Claude outright is the expensive work, so an automation
share that counts conversations understates the wage bill behind it, and the wage-weighted version is
the one a model of labour payments should take. The work being delegated is not a random draw from
the wage distribution, and the first-order effect of that is measurable now rather than in prospect.

**If H2 holds.** The expensive work is the work people stay inside: on Claude.ai, high-wage tasks
draw collaboration and low-wage tasks draw delegation, the opposite of what an unweighted automation
share implies about the wage bill at stake. Read against the corpus's own finding that compute rises
with the value of the work, more capability is being spent on work that people are not handing over.

**If H3 holds (composition, not price).** The apparent relation between delegation and the price of
the work is one occupational family: coding tasks are both the best paid and the most fully handed
over, and outside them the gradient is flat. What looks like a statement about the wage distribution
is a statement about software, which anyone weighting an automation share by wage needs to know.

**If H4 holds (the null, at the stated power).** Delegation does not track the price of the work: in
each of the three windows the delegated share of high-wage and of low-wage tasks differs by less than
one percentage point, a margin the design resolves with an MDE of 0.42 to 0.43 percentage points on
the conversations these windows contain. That extends Anthropic's published null for required
education to the wage of the work itself, and it means an unweighted automation share is, for this
purpose, the right number after all.
