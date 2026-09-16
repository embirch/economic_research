# post1 · Is AI delegated more on cheap work or on expensive work?

*Brief of record. Candidate LL-07 (Σ 28, rank 1). Question, title and contribution freeze at Gate 1b.
Written on `team/templates/BRIEF.md`; the sketch is `programme/SHORTLIST.md` §6, lines 219–297.*

## 1. The question

Does the share of AI use that is delegated outright rather than worked through collaboratively rise
or fall with the wage of the work being done?

## 2. Why it matters, and to whom

The sign of that gradient is the sign of the first-order labour-share effect. Delegating expensive
work moves a large wage bill; delegating cheap work moves a small one. Anthropic's own scenario
paper makes the point unavoidable by construction: it measures "the importance of each task by its
initial share of total labor payments: m_i ≡ s_i,t0/s_L,t0" (`econ-scenarios-paper-2026-09`,
2026-09, p. 9), while the automation share the Economic Index publishes counts conversations and
weights every task the same. If delegation is concentrated at one end of the wage distribution, an
unweighted automation share is the wrong input to a wage-bill model, and it is wrong in a knowable
direction.

Who decides differently. Anyone calibrating an exposure or automation parameter: the scenarios
paper holds its automation share ψ constant at 0.50 / 0.75 / 0.90 by assumption, and its
affected-mass anchor is reported as "observed exposure, averaged over occupations" without saying
whether that average is employment- or wage-bill-weighted (`econ-scenarios-paper-2026-09`, 2026-09,
Table 1 p. 23; open ledger item `L-2026-09-SCPA-27`). Anyone reading a published automation share as
a statement about the economy: the number is a conversation count, and this post says how much of
the wage bill sits behind it. And anyone weighting delegation against augmentation in a labour-market
measure — the observed-exposure measure sets α = 1/2 + 1/2 × automation share, so "A task with only
automative uses would have α_t = 1" (`labor-market-impacts-2026-03-appendix`, 2026-03, p. 3), which
is a wage-blind weighting of a wage-relevant quantity.

What this data can say that nothing else can. The Economic Index publishes the collaboration facet
crossed with the O\*NET task at global grain in three waves, with per-task usage weights in the same
wave. No survey and no job-posting series observes how a given task was actually worked on, at
task resolution, on a million-conversation sample. The cross of that facet with a wage exists in no
publication, Anthropic's or anyone's.

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
define as the average hourly wage of US workers who perform that task" (p. 8) — and reports
"$49.3 to $47.9" (p. 8, Fig. 1.4); it sorts *model choice* by that same wage, "for every additional
$10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage
points for Claude.ai users" (p. 14, Fig. 2.2). `economic-index-2026-06-report` (2026-06) sorts
*compute* by it: "We also see that more compute is associated with more valuable artifacts; the
tokens a given output consumes rise with the estimated value of the work" (pp. 2–3), delivered at
Fig. 2.3 (body p. 12, caption p. 13). ⟨mentor⟩ Both of those wage cuts are the mentor's chapters.

What the thread has established: the five-pattern split, its five-wave Claude.ai series, the API's
automation dominance, and delegation's rise with the agentic surface. Where it is open: the
collaboration facet is crossed with occupation and with category and never with wage
(`programme/LEDGER.md` `L-2025-02-R1-16`, *partially answered* — "the wage cross is published
nowhere"); automation share by wage or Job Zone "was one join away (the facets were intersected) and
is never shown" (`L-2025-02-P1-22`, *partially answered*); and the affected-mass weighting is
unstated (`L-2026-09-SCPA-27`, *open*). The one published result closest to the question is a null on
a neighbouring ordering: "the automation share is essentially unrelated to the human levels of
education required to write the prompt (Appendix Figure A.1)" (`economic-index-2026-01-report`,
2026-01, p. 40).

## 4. Overlap, stated

- **Anthropic, task value.** The task mix is priced by occupational wage across five windows and two
  platforms (`economic-index-2026-03-report`, Fig. 1.4 p. 8). New here: the wage is crossed with how
  the work was done, not with how much of it there was.
- **Anthropic, wage gradients in other measures.** Opus share rises with task wage (ibid., Fig. 2.2
  p. 14); tokens rise with mapped-occupation wage (`economic-index-2026-06-report`, Fig. 2.3 p. 13).
  New here: the same gradient estimated on the collaboration facet, which those two chapters leave
  untouched.
- **Anthropic, the education null.** Automation share is flat in required human education
  (`economic-index-2026-01-report`, p. 40). New here: wage is not education, it is the price of the
  labour a task displaces, and it is the quantity the scenario framework weights by.
- **Chatterji et al. (2025), "How People Use ChatGPT".** Work usage concentrates in highly paid
  professional occupations and "Doing" exceeds "Asking" in work messages. New here: the
  Asking/Doing split is never regressed on a wage there; this post estimates that gradient.
- **Tomlinson et al. (2025), "Working with AI".** Correlates wage and education with an AI
  *applicability* score and predicts which occupations delegate versus assist. New here: the
  gradient is in the delegation measure itself, on observed usage rather than on an applicability
  index, and on a different surface.
- **Acemoglu (2025), "The Simple Macroeconomics of AI".** The theory that the wage bill of automated
  tasks is what moves the labour share, with no usage measurement. New here: the measurement.

**Separation from its pair partners** (`programme/SHORTLIST.md` §5, pairs 3). post3 (LL-36) is
composition *inside* one occupational category; post8 (LL-30) is the work/coursework use-case mix.
All three build the same task → SOC join and must fix the same multi-holder rule. Under the
director's sequencing ruling this post is written first, states that construction in §8, and the
other two cite the statement rather than re-deriving it. No other post in the programme estimates a
wage gradient in the collaboration facet.

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
loses more than half its size or its sign when SOC-15 tasks are dropped (that is H3); a sign that
flips between the two wage sources; a difference that sits inside the permutation null's central 95%.

**H2 · Inverse gradient (the expensive work is the collaborative work).** The usage-weighted
automation share falls with the wage of the work.
*Signature only it predicts:* a negative, outside-MDE top-minus-bottom difference in all three waves,
**with** the augmentation components rising in wage — the learning, task-iteration and validation
shares each weakly increasing across quartiles — rather than the difference being produced by the
`none` residual moving.
*What counts against it:* a positive or inside-MDE difference in any wave; a negative difference
carried by the residual rather than by the five classified patterns; a negative difference that
disappears within major group.

**H3 · Composition, not price.** Any gradient is carried by one occupational family — coding tasks
are both high-wage and the most delegated — so wage is standing in for a task family.
*Signature only it predicts:* a gradient outside the MDE in the pooled estimate that falls inside it
when SOC-15 tasks are excluded or when it is estimated within major group and averaged, and a
leave-one-group-out series in which one group's removal moves the estimate by more than all others
combined.
*What counts against it:* the gradient's size and sign surviving all 22 leave-one-group-out
re-estimates and the within-group estimator, in all three waves.

**H4 · No relation (the null the design can deliver).** The automation share does not track the price
of the work, extending the published education null.
*Signature only it predicts:* |top-minus-bottom| whose two-sided 95% interval excludes ±3 pp in all
three waves — the pre-registered indifference band, set at the size of the corpus's own twelve-month
move in the global automation share (+2.48 pp, `data/ATLAS.md` §Conventions) — with no monotone
ordering across quartiles and a continuous slope indistinguishable from zero.
*What counts against it:* any wave whose interval excludes zero with a consistent sign across waves;
an ordering that is monotone in all three waves even if each difference is small.

## 7. Assumptions sweep

**(1) Value judgement in the framing — "cheap", "expensive", "delegated". Marked: handled, with a
wording rule.** The frame prices work by the wage of the people who do it, which is Anthropic's own
construct — "the average hourly wage of US workers who perform that task" and, where several
occupations do it, "we average their wages weighting by employment and the fraction of time spent on
that task" (`economic-index-2026-03-report`, 2026-03, p. 8 and footnote 5 p. 11). A wage is the price
of the labour a task displaces, not a measure of the work's worth to anyone, and the title's "cheap"
and "expensive" are shorthand for that price. Rule adopted, since question and title freeze at
Gate 1b: the title keeps the editor's ruling ("'Delegated', 'cheap' and 'expensive' are the corpus's
own terms", `room/editor-2026-09-16-sketch-LL-07.md`) and the body says "the wage of the work"
throughout; no finding is written as a gain or a deficit, and neither direction of the gradient is
called good or bad. The labour-share reading is stated as a consequence for a model input, not as a
verdict.

**(2) Construct mapping. Marked: needs a design change — change made.** The measure is a classifier
on conversations: "**automation_pct**: Percentage of classifiable collaboration that is
automation-focused (directive, feedback loop patterns)"
(`release_2025_09_15/data_documentation.md`, quoted in `economic-index-2025-09-report`, 2025-09,
Definitions). It is not a count of tasks automated, and it is not autonomy: "'Translate this
paragraph into French' is high automation (directive, minimal back-and-forth) but low AI autonomy"
(`economic-index-2026-01-report`, 2026-01, p. 19). Both are said in the post. The mapping that
needed the change is the wage: Anthropic's task value uses BLS OEWS May 2024 with employment *and*
time-on-task weights (footnote 5, p. 11); the public files carry neither OEWS nor any time-on-task
weight, and a public rebuild returns $35.08 → $34.36 against the published $49.3 → $47.9
(`data/ATLAS.md` log (f) 13). **Design change:** the post is rank-based. Tasks are sorted into
usage-weighted wage quartiles — Anthropic's own convention, "Wage quartiles are calculated using BLS
data, weighted by number of transcripts" (`economic-index-2026-06-report`, 2026-06, Fig. 1.3 caption
p. 7) — the headline is a quartile difference, the dollar slope is secondary and carries the
non-reproduction in its caption, and no wage level is reported as Anthropic's.

**(3) Composition and selection. Marked: needs a design change — change made.** The unit is a
conversation on Claude.ai, and "occupation is inferred from the task, not the user"
(`/mnt/memory/standards/terminology.md`; `economic-index-2026-06-report`, 2026-06, p. 7: "While we
can't conclusively identify the jobs of the people making these requests…"). A task's wage is
therefore the wage of work that *resembles* it. Three mixes could produce a gradient without any
price mechanism: coding tasks, which are high-wage and the most delegated, carrying the whole
relation; the February wave's Super Bowl inflow of new consumer users changing the task mix under
the same global label; and Seychelles, 2.5% of the whole November global sample and excluded by the
report but not by the file (`data/ATLAS.md` §Traps 14). **Design change:** H3's within-major-group
estimator and the 22 leave-one-group-out re-estimates are confirmatory, not robustness; each wave is
reported separately and never pooled; the November wave is re-estimated with Seychelles netted out
of the global mix (max shift 1.17 pp, `data/ATLAS.md` log (f)); and the finding is stated about
Claude.ai conversations, with one sentence on what generalises.

**(4) Anthropic's own results that cut against or bound the framing. Marked: newly flagged, carried
into the post.** Three. First, the published education null — "the automation share is essentially
unrelated to the human levels of education required to write the prompt"
(`economic-index-2026-01-report`, 2026-01, p. 40) — is a real prior for H4 on a correlate of wage,
and the post reports the wage gradient beside it rather than in ignorance of it. Second, Fig. 2.2's
Opus gradient (2026-03, p. 14) means the expensive work already draws the more capable model, so a
positive gradient may be a demand-for-intelligence result rather than a delegation result; the post
says so and the pattern-level split is the exploratory probe. Third, the corpus insists automation
and autonomy are distinct constructs (2026-01, p. 19), so the June finding that compute and autonomy
rise with the value of the work does **not** predict this gradient's sign — it is quoted as
motivation and never as a prior.

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
**`posts/post1/notes/feasibility.md`**, written after this brief; every cut below is to be confirmed
or contradicted there, at column level, with a command.

**Cuts, at column level.**

| # | release (window) | grain | facet / category | metric | threshold / base |
|---|---|---|---|---|---|
| C1 | `release_2025_09_15` (4–11 Aug 2025), `platform_and_product = "Claude AI (Free and Pro)"` | `geography = global` | `onet_task::collaboration`, `level` per file | `_pct` and `_count` per (task, pattern) | published privacy floor only; residual patterns `none`, `not_classified` dropped from the numerator base |
| C2 | `release_2026_01_15` (13–20 Nov 2025), same platform label (sample is Free, Pro and Max) | `geography = global` | `onet_task::collaboration` | `_pct`, `_count` | same; Seychelles netting re-run at C8 |
| C3 | `release_2026_03_24` (5–12 Feb 2026), `"Claude AI (Free, Pro, and Max)"` | `geography = global` | `onet_task::collaboration` | `_pct`, `_count` | same; counts are on a 1,000,000 sample base |
| C4 | each of C1–C3, same wave | `geography = global` | `onet_task` base facet | `onet_task_pct` | the usage weight; `none` and `not_classified` task nodes dropped (the one-node difference between 2,617 / 3,169 / 3,259 intersection nodes and 2,616 / 3,168 / 3,258 named nodes, for the steward to confirm) |
| C5 | `release_2025_09_15/data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 rows, 974 occupations) | — | task → O\*NET-SOC | `Task ID`, `O*NET-SOC Code` | join key is the **lower-cased, stripped** task text, de-duplicated on that key before the merge (`data/ATLAS.md` §Traps 21: case-variant duplicates create a silent many-to-many) |
| C6 | `release_2025_02_10/wage_data.csv` (O\*NET website wage scrape, Kilbourne-Quirk 2019 — **not** a BLS series) | — | occupation wage, primary | `MedianSalary`, filtered `> 100` (1,084 of 1,090 rows) | join `O*NET-SOC Code[:7]` → `SOCcode`; annual ÷ 2080 for an hourly rate; `-1` is a missing sentinel in `JobZone`/`ChanceAuto` (`§Traps 10`) |
| C7 | BLS Employment Projections (`data.bls.gov/projections/occupationProj`, 831 detailed-SOC rows) | — | occupation wage, second source | median annual wage on `occ_code` | prices only 54.7% / 57.8% of named-task mass against C6's 99.0–99.4% (`ATLAS` log (f) 13); used for sign agreement, never for a level |
| C8 | `release_2026_01_15`, country rows | `geography = country` | `onet_task` | `onet_task_count` for `SYC` | netted out of the global mix and renormalised for the November re-estimate (max shift 1.17 pp) |

Grain rule observed: intersections are **global only** in all three long waves (`data/ATLAS.md`
§Cuts 10), so there is no country or state version of this post and none is implied. `soc_occupation`
is absent as a facet in the two 2026 waves (§Cuts 13), which is why the occupational split in H3 runs
through the C5 join rather than through a published facet.

**The task → SOC join and the multi-holder rule, stated here for the construction triple.** A task
text is joined to O\*NET-SOC through C5 on the lower-cased stripped task text and priced through C6
on the 7-character SOC prefix. Where a task is held by more than one occupation it has no single
wage. Anthropic's rule is employment-and-time weighted (footnote 5, p. 11); the public files carry no
time-on-task weight, so the pre-registered primary rule is the **employment-weighted mean over holder
occupations** (BLS-EP employment on `occ_code`), as the nearest available analogue of Anthropic's
definition, with the equal-split mean and the modal holder reported beside it in every table. The
exposure is small and bounded: a task text maps to one SOC code for all but **72 / 91 / 84** tasks
(Aug / Nov / Feb), **4.05% / 5.57% / 4.50%** of named usage mass, and the three rules move the SOC-15
share by **≤ 0.17 pp** and the 22-group ranking by at most one position (Aug) or none (Nov, Feb)
(`room/steward-2026-09-16-longlist-feasibility-batch-3-answers.md`, LL-32; `data/ATLAS.md` log (g) 4).
That bound is on an occupational share, not on this post's gradient, so it is reported as context and
the gradient itself is re-estimated under all three rules. post3 (LL-36) and post8 (LL-30) cite this
paragraph.

**The published numbers this reproduces first.** (i) The wave's own global collaboration split, on
the base each report used: 49.0980 (Aug 2025, all seven patterns, published "49%"), 45.3554 (Nov
2025, all conversations, published "45%"), 44.1569 (Feb 2026, all conversations, published "44%")
— and the same three on the five-classified-pattern analysis base (0.5107 / 0.4674 / 0.4555), with
the base named every time. (ii) The internal check that licenses the estimator: the usage-weighted
mean of the per-task automation shares from the intersection must return that wave's global value
within rounding. (iii) Stated as a **known non-reproduction**, not attempted as a target:
Anthropic's task value of $49.3 → $47.9 rebuilds from public files as $35.08 → $34.36, with the
direction preserved (−$0.72 against the published −$1.40) — which is why the design is rank-based.

## 9. Confirmatory tests and the exploratory allowance

1. **H1 / H2 — the key number.** Per wave, the usage-weighted automation share of the top wage
   quartile of tasks minus that of the bottom quartile, on the five-classified-pattern base, with the
   `none` share reported beside it in every table so the base is never implicit, and with quartile
   boundaries drawn on usage-weighted wage. Decision rule: H1 if positive and outside the MDE in all
   three waves; H2 if negative and outside the MDE in all three; anything else goes to H3 or H4.
2. **The continuous companion.** The usage-weighted slope of the automation share in the task's
   hourly wage, reported per +$10/hr in the form Anthropic uses for its Opus gradient, sign and
   significance only.
3. **H3 — composition.** The same quartile difference (a) with SOC-15 tasks excluded, (b) estimated
   within SOC major group and averaged by usage weight, (c) as 22 leave-one-group-out re-estimates.
4. **H4 — the null.** The two-sided 95% interval for the quartile difference against the
   pre-registered ±3 pp indifference band. Variance comes from a task-level bootstrap that resamples
   tasks with probability proportional to usage weight; the MDE is computed on the **Kish effective
   N**, n/(1+cv²) on the `onet_task_pct` weights, which usage concentration will put well below the
   nominal 2,617 / 3,169 / 3,259, and the effective N is printed beside the nominal count in the post
   (referee correction 2). A null is reported only if the MDE is below 3 pp; otherwise the result is
   reported as underpowered, which is a different sentence.

**Exploratory allowance: three tests, after the confirmatory set, none of them in the headline and
each labelled as exploratory in the post.** (a) The same gradient on the 1P API global intersection,
to say whether the sign is a property of the surface rather than of the work — the API is
automation-dominant by construction, so this is context, not a replication. (b) The pattern-level
split: which of directive and feedback loop carries a positive gradient, and whether learning,
task iteration and validation move in the opposite direction — the probe for the
demand-for-intelligence rival named in §7(4). (c) The gradient against `JobZone` from C6 as a
non-wage ordering of the same tasks, to separate price from required preparation. No further tests;
any additional cut is a deviation and is logged as one.

## 10. Noise and robustness required

- **Persistence across windows** — built into the confirmatory rule: three waves, each estimated and
  reported separately, never pooled and never spliced.
- **Leave-one-out** — 22 leave-one-group-out re-estimates (confirmatory under H3) and a
  leave-out of the ten largest tasks by usage mass, since the top-10 tasks hold 19.4% of Feb-2026
  named usage.
- **Flagged units excluded** — Seychelles netted out of the November global mix and the gradient
  re-estimated (C8). Utah's August anomaly is a state-level artefact and cannot move a global
  intersection materially; the post says that rather than silently ignoring it. Tasks whose
  intersection `_count` falls below a pre-registered floor are excluded in a sensitivity cut, since
  the published intersection floor goes down to 1.
- **Placebo** — a permutation null: the wage vector is permuted across tasks within SOC major group
  and the estimator re-run, giving the distribution of the quartile difference under no
  wage–delegation relation; the observed statistic is reported against that distribution.
- **Second implementation** — the gradient rebuilt independently by the analyst on the second wage
  source (C7) and with the two alternative multi-holder rules, with sign agreement required for any
  claim; and the wage join re-run from the task side and the SOC side as two separate builds.

## 11. Literature check

Searches run for the long-list entry and re-checked for this brief: Anthropic's own corpus
(`wiki/reports/`, every Economic Index report and appendix, the labour-market and scenarios papers)
for "wage", "value", "collaboration", "automation share"; and the external comparators recorded in
`data/ATLAS.md` §Supplementary sources. Closest prior work, and where this sits:

- **Chatterji et al. (2025), "How People Use ChatGPT"** — the nearest thing to a rival measurement:
  an Asking/Doing split on a consumer surface, with work usage concentrated in highly paid
  occupations. It never regresses that split on a wage, so the gradient is unmeasured there.
- **Tomlinson et al. (2025), "Working with AI"** — wage and education against an AI *applicability*
  score, and a separate delegate-versus-assist prediction, on Copilot conversations. The wage enters
  the applicability index, not the delegation measure.
- **Acemoglu (2025), "The Simple Macroeconomics of AI"** — supplies the reason the sign matters (the
  wage bill of automated tasks is what moves the labour share) and no usage measurement at all.
- **Anthropic** — prices tasks (2026-03 Fig. 1.4), model choice (2026-03 Fig. 2.2) and tokens
  (2026-06 Fig. 2.3) by wage, and publishes a null for automation share against required education
  (2026-01 p. 40). The collaboration facet is crossed with wage nowhere.

This post sits in the empty cell: a usage-weighted estimate of the delegation share as a function of
the price of the work, on Anthropic's own published intersection, in three waves.

## 12. What the closing section will be able to say

**If H1 holds.** The work people hand over to Claude outright is the expensive work, so an automation
share that counts conversations understates the wage bill behind it, and the wage-weighted version is
the one a model of labour payments should take. The people whose work is being delegated are not a
random draw from the wage distribution, and the first-order effect of that is measurable now rather
than in prospect.

**If H2 holds.** The expensive work is the work people stay inside: on Claude.ai, high-wage tasks
draw collaboration and low-wage tasks draw delegation, which is the opposite of what an unweighted
automation share implies about the wage bill at stake. Read against the corpus's own finding that
compute and model capability rise with the value of the work, the pattern says that more capability
is being spent on work that people are not handing over.

**If H3 holds (composition, not price).** The apparent relation between delegation and the price of
the work is one occupational family: coding tasks are both the best paid and the most fully handed
over, and outside them the gradient is flat. What looks like a statement about the wage distribution
is a statement about software, which is the reading anyone weighting an automation share by wage
would need to know before doing so.

**If H4 holds (the null, at the stated power).** Delegation does not track the price of the work:
across three waves the delegated share of high-wage tasks and of low-wage tasks differs by less than
three percentage points, an interval the design can resolve at the effective sample size reported
beside it. That extends Anthropic's published null for required education to the wage of the work
itself, and it means an unweighted automation share is, for this purpose, the right number after all.
