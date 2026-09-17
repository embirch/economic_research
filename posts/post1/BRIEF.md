# post1 · Is AI delegated more on low-wage work or on high-wage work?

*Brief of record (LL-07, Σ 28, rank 1), rewritten once from the record (960080c) on the referee's verdict
`posts/post1/notes/referee-brief.md` (e2affe4), items 1–12; earlier amended on `posts/post1/notes/feasibility.md`. The title is the human's
decision on item 3 (option A). Question, title and contribution freeze at Gate 1b. Numbers marked ⟨ref⟩ are the referee's re-derivation
(`posts/post1/notes/rederivation/referee_brief_post1.out.txt`); the cuts marked ⟨new⟩ in §8 are his and need the steward's confirmation before
signing.*

## 1. The question

Does the share of AI use that is delegated outright rather than worked through collaboratively rise or fall with the wage of the work being done?

Body rule throughout the post: "the wage of the work", never "cheap" or "expensive"; low-wage and high-wage work mean the bottom and top
usage-weighted wage quartile of the tasks brought to Claude, defined in the post's first paragraph (§7(1)).

## 2. Why it matters, and to whom

The sign of that gradient does not fix whether delegation lowers the labour share: automation of any task lowers it, whatever that task pays. It
fixes the sign of the error made when an unweighted automation share is read as though it were weighted by the wage bill at stake. Anthropic's
scenario paper weights by that bill, "the importance of each task by its initial share of total labor payments: m_i ≡ s_i,t0/s_L,t0"
(`econ-scenarios-paper-2026-09`, 2026-09, p. 9), while the automation share the Economic Index publishes counts conversations and weights every
task the same. A conversation count is not the quantity a wage-bill model weights by, and if delegation sits at one end of the wage distribution
that discrepancy is signed. Its size is small and stated: a 1 pp quartile gap moves the wage-weighted automation share **0.11–0.12 pp** from the
unweighted one ⟨ref⟩, and that difference is published with its own interval beside the gap (§9(1)).

Who decides differently. Anyone calibrating an exposure or automation parameter: the scenarios paper holds ψ at 0.50 / 0.75 / 0.90 by assumption,
and its affected-mass anchor is "observed exposure, averaged over occupations" without saying whether that average is employment- or
wage-bill-weighted (ibid., Table 1 p. 23; open ledger item `L-2026-09-SCPA-27`). Anyone reading a published automation share as a statement about
the economy: it is a conversation count, and this post says how much of the wage bill sits behind it. And anyone weighting delegation against
augmentation in a labour-market measure — observed exposure sets α = 1/2 + 1/2 × automation share, so "A task with only automative uses would have
α_t = 1" (`labor-market-impacts-2026-03-appendix`, 2026-03, p. 3), a wage-blind weighting of a wage-relevant quantity.

What this data can say that nothing else can. The Economic Index publishes the collaboration facet crossed with the O\*NET task at global grain in
three waves, with per-task usage weights in the same wave. No survey and no job-posting series observes how a given task was actually worked on,
at task resolution and on a million-conversation sample; that cross with a wage exists in no publication.

## 3. The thread of Anthropic's inquiry this builds on

Thread T3 (automation versus augmentation, delegation and autonomy) with T4 (task-level primitives). The taxonomy is fixed and repeated across six
waves:

> "At a high level, we distinguish between automation and augmentation modes of using Claude: Automation
> encompasses interaction patterns focused on task completion: Directive: Users give Claude a task and it
> completes it with minimal back-and-forth; Feedback Loops: Users automate tasks and provide feedback to Claude
> as needed. Augmentation focuses on collaborative interaction patterns: Learning… Task Iteration… Validation…"
> (`economic-index-2025-09-report`, 2025-09, PDF p. 9)

> "'Directive' conversations, where users delegate complete tasks to Claude" (ibid., PDF p. 3)

The corpus prices the work, prices the compute, and never prices the delegation. `economic-index-2026-03-report` (2026-03) prices the task mix —
"Another way to measure the change in the mix of tasks done on Claude is to look at the change in the average value of tasks, which we define as
the average hourly wage of US workers who perform that task" (p. 8), its Claude.ai series reading $49.3 (Jan 2025), $48.5 (Mar 2025), $48.9 (Aug
2025), $48.3 (Nov 2025), $47.9 (Feb 2026) (Fig. 1.4 p. 8; the windows matter for §8(iv)) — and sorts *model choice* by the same wage: "for every
additional $10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points for Claude.ai users" (p. 14,
Fig. 2.2). `economic-index-2026-06-report` (2026-06) sorts *compute* by it: "more compute is associated with more valuable artifacts; the tokens a
given output consumes rise with the estimated value of the work" (pp. 2–3; Fig. 2.3, caption p. 13). ⟨mentor⟩ Both wage cuts are the mentor's
chapters.

Established: the five-pattern split, its five-wave Claude.ai series, the API's automation dominance, delegation's rise with the agentic surface,
and two results bearing on the sign. At the high-wage end the corpus reports *more* human involvement, not less — "In conversations mapped to
higher-wage occupations, Claude produces more (1.34 times as much output per turn), while users engage more (1.53 times as many turns)", read
conditionally as "If the human remains involved in the highest-value tasks, the pattern looks more labor-augmenting than labor-displacing"
(2026-06, pp. 13–14, Table 2.4). And the one published cross of the collaboration facet with occupational category is not monotone in wage:
Protective Service 55.40% and Production 54.88% automation above Computer and Mathematical at 49.53%, with Community and Social Service tasks that
"approach 75% augmentation" and translators "among the highest amounts of *directive* behavior" (`economic-index-2025-03-report`, 2025-03, § "How
does augmentation vs. automation vary by task and occupation?"; steward's bar-by-bar reproduction in `data/releases/release_2025_03_27.md`). Open:
the collaboration facet is crossed with occupation and with category and never with wage (`programme/LEDGER.md` `L-2025-02-R1-16`, *partially
answered* — "the wage cross is published nowhere"); automation share by wage or Job Zone "was one join away (the facets were intersected) and is
never shown" (`L-2025-02-P1-22`); the affected-mass weighting is unstated (`L-2026-09-SCPA-27`, *open*). The closest published result is a null on
a neighbouring ordering — "the automation share is essentially unrelated to the human levels of education required to write the prompt" (2026-01,
p. 40) — a property of the prompt, not of the occupation (§4).

## 4. Overlap, stated

- **Anthropic, the wage as a sorting variable.** The task mix is priced by occupational wage across five windows and two platforms (2026-03, Fig.
  1.4 p. 8); Opus share rises with task wage (Fig. 2.2 p. 14); tokens rise with mapped-occupation wage (2026-06, Fig. 2.3 p. 13). New: the same
  gradient on the collaboration facet, which those chapters leave untouched — the wage crossed with how the work was done, not with how much there
  was.
- **Anthropic, turns, output and the one category cross.** Higher-wage conversations already show more human involvement — 1.53× the turns, 1.34×
  the output per turn — with the augmenting reading offered conditionally (2026-06, pp. 13–14); and automation by occupational category, published
  once for Feb–Mar 2025, is not monotone in wage (2025-03). New: that reading tested on the measure that defines delegation, where "Directive" is
  "minimal back-and-forth" (2025-09, p. 9), and the wage ordering itself at task grain, usage-weighted, in three later waves.
- **Anthropic, the education null.** The automation share is flat in the education level of the prompt — `human_education_years`, a
  per-conversation reading-level primitive (2026-01, p. 40, Appendix Figure A.1, no statistic). New: wage is not that; it is the price of the
  labour a task resembles and the quantity the scenario framework weights by, so a null here sits beside Anthropic's null rather than extending
  it.
- **Chatterji et al. (2025), "How People Use ChatGPT".** Work usage concentrates in highly paid occupations and "Doing" exceeds "Asking" in work
  messages, never regressed on a wage. New: that gradient, estimated.
- **Tomlinson et al. (2025), "Working with AI".** Wage and education against an AI *applicability* score, plus a delegate-versus-assist
  prediction. New: the gradient inside the delegation measure itself, on observed usage.
- **Acemoglu (2025), "The Simple Macroeconomics of AI".** The wage bill of automated tasks as what moves the labour share, with no usage
  measurement. New: the measurement.

**Separation from its pair partners** (`programme/SHORTLIST.md` §5, pair 3). post3 (LL-36) is composition *inside* one occupational category;
post8 (LL-30) headlines the work/coursework use-case mix, a control here (§9(3)). All three build the same task → SOC join and fix the same
multi-holder rule; this post is written first and states that construction in §8, and the other two cite it. No other post estimates a wage
gradient in the collaboration facet.

## 5. Contribution

If the gradient exceeds the pre-registered margin in one direction, the post supplies the sign and size of the weighting error in a published
automation share — the wage-weighted number an unweighted one misses — and names the wage bill behind it; if it is real but below that margin, it
supplies the direction with the arithmetic that makes the correction a tenth of a point, not a repair; if it lies inside the margin at the stated
power, it publishes the first wage-by-collaboration table in the corpus, a second null beside Anthropic's null for the education level of the
prompt.

## 6. Hypotheses

One size criterion serves all four: the pre-registered **smallest effect of interest δ = 1 pp** on the usage-weighted top-minus-bottom
wage-quartile difference D in the automation share, on two-sided 95% intervals under §9(4)'s conversation-level model (MDE(80%) 0.42–0.43 pp). The
ordered rule in §9(1) partitions D's outcome space between H1, H2, H4 and two further named outcomes — **O-A, a persistent gradient below the
margin**, and **O-B, no persistent gradient** — so no result is unowned and none has two owners. H3 is a rival *explanation* of a gradient, not a
rival value of D, evaluated only when one is declared.

**H1 · Price gradient (delegation rises with the wage of the work).** The usage-weighted automation share is higher for high-wage than for
low-wage tasks. *Signature only it predicts:* D's lower bound above **+1 pp in all three waves** (§9(1) step 1) **and** D keeping more than half
its size, with the same sign, on all three composition legs — SOC-15 excluded, within major group, work-dominant tasks (§9(3)). *Against it:* any
wave whose lower bound does not clear +1 pp (the outcome goes to H2, O-A, H4 or O-B by the same rule); losing more than half the size, or the
sign, on any composition leg (H3); a sign that disagrees between the two wage sources.

**H2 · Inverse gradient (the high-wage work is the collaborative work).** The automation share falls with the wage of the work — the reading
Anthropic has offered for its own turn counts, "the pattern looks more labor-augmenting than labor-displacing" (2026-06, pp. 13–14). *Signature
only it predicts:* D's upper bound below **−1 pp in all three waves** (step 2), with augmentation components rising in wage — at least two of
learning, task iteration and validation weakly increasing across quartiles — and the `none` and `not_classified` shares by quartile beside them,
so a shift in the classified base is visible. *Against it:* any wave whose upper bound does not fall below −1 pp; the movement sitting in the
`none`/`not_classified` composition rather than in the augmentation patterns (a negative D without the augmentation signature, reported as such);
losing more than half the size, or the sign, on a composition leg (H3).

**H3 · Composition, not price.** A declared gradient is carried by a mix that travels with wage rather than by the price of the work: the coding
family — Anthropic's own definition makes the mechanism explicit, "automative uses, like asking the model to directly complete a task or debug
errors" (2025-03), and SOC-15 is **77.1 / 75.7 / 69.9% of top-quartile mass** ⟨ref⟩ — or the use-case mix, the bottom quartile being two-thirds
personal and coursework against three-fifths work in the top (§7(3)). *Signature only it predicts:* a D declared under H1, H2 or O-A that **loses
more than half its size, or its sign,** on at least one of the three legs, with a leave-one-group-out series in which one group's removal moves
the estimate by more than all others combined. *Against it:* D keeping more than half its size and its sign on all three legs and across all 22
leave-one-group-out re-estimates, in all three waves.

**H4 · No relation at the stated margin (the null the design can deliver).** The automation share does not track the price of the work by as much
as a point. *Signature only it predicts:* D's interval **inside ±1 pp in all three waves** *and* the three intervals not all excluding zero with
one sign (steps 3–4) — the second clause is what separates H4 from O-A. *Against it:* three same-signed intervals excluding zero (O-A, or H1/H2 if
they clear the margin); any wave whose interval leaves ±1 pp (O-B, or H1/H2).

## 7. Assumptions sweep

**(1) Value judgement in the framing. Marked: needs a design change — change made (the title).** The frame prices work by the wage of the people
who do it, Anthropic's own construct: "the average hourly wage of US workers who perform that task" and, where several occupations do it, "we
average their wages weighting by employment and the fraction of time spent on that task" (2026-03, p. 8, footnote 5 p. 11). The editor's premise
that "cheap" and "expensive" are corpus terms is false — the corpus writes "task value" (2026-03, p. 8), "less remunerated tasks" and "high-value,
complex work" (p. 19), "tasks that command lower wages" (2026-06, p. 32) — and "cheap" in plain English also means shoddy, which this design does
not measure. **Change, taken by the human on the referee's option A:** the title is "Is AI delegated more on low-wage work or on high-wage work?",
every word of which the design tests; the body says "the wage of the work". The post's first paragraph defines low-wage and high-wage as the
bottom and top usage-weighted wage quartile of the tasks brought to Claude, and says that low-wage is relative to that mix, not to the economy:
the bottom quartile's ceiling is $24–26/hr against a median US occupation wage on the same file of about $22.9/hr (occupations weighted by their
major group's BLS May-2023 employment), 54–58% of that wage mass falling below the ceiling ⟨ref⟩. Anthropic bounds it the same way: "Overall,
Claude is used for high-value, complex work that is not broadly representative of the US economy" (2026-03, p. 19). Neither direction is called
good or bad; the labour-share reading is a consequence for a model input, not a verdict.

**(2) Construct mapping. Marked: needs a design change — change made.** The measure is a classifier on conversations: "**automation_pct**:
Percentage of classifiable collaboration that is automation-focused (directive, feedback loop patterns)"
(`release_2025_09_15/data_documentation.md`), from the prompt's own definition, "Directive – Human delegates complete task execution to AI with
minimal interaction" (`economic-index-2025-02-paper`, Appendix F.3, p. 25). It is not a count of tasks automated, and not autonomy — "high
automation (directive, minimal back-and-forth) but low AI autonomy" (2026-01, p. 19) — and Anthropic's caveats bound what one dialogue's shape can
mean: "users might edit and adjust the response they receive from Claude outside the chat window"; "even automation of simple tasks can serve to
enhance human capabilities when embedded within broader human-directed workflows" (2025-02 paper, p. 9). The post carries all of that, which is
why §2's wage-bill reading is a statement about a model input, not a measurement of displaced labour. Two mappings needed changes. *The wage is a
rate, not a bill:* the scenarios paper's m_i is a share of "total labor payments" (2026-09, p. 9), wage × hours, while task value is an hourly
wage (2026-03, p. 8). This post measures a rate and says so; the wage × human-time version is one join away in two of three waves
(`onet_task::human_only_time` at global, 28,533 rows Nov, 29,291 Feb, none in Aug ⟨ref⟩) and is **stated as not run** — that facet is a bucketed
estimate of human-only time rather than hours worked, it is missing from August, and it would import a second construct mapping the steward has
not confirmed. *The wage level does not reproduce* (§8(iv) gives the matched windows and four causes). **Design change:** the post is rank-based,
sorting tasks into usage-weighted wage quartiles — Anthropic's own convention, "Wage quartiles are calculated using BLS data, weighted by number
of transcripts" (2026-06, Fig. 1.3 caption p. 7) — the headline is a quartile difference with the wage-weighted-minus-unweighted share beside it,
the dollar slope is secondary and carries the non-reproduction in its caption, and no wage level is reported as Anthropic's.

**(3) Composition and selection. Marked: needs a design change — change made.** The unit is a conversation on Claude.ai and "occupation is
inferred from the task, not the user" (`/mnt/memory/standards/terminology.md`; 2026-06, p. 7: "While we can't conclusively identify the jobs of
the people making these requests…"), so a task's wage is the wage of work that *resembles* it. Four mixes could produce a gradient with no price
mechanism.

*Use case — the most direct rival.* The usage-weighted work share by wage quartile is **32.8 / 48.4 / 41.8 / 62.0%** (Nov) and **28.4 / 51.5 /
41.6 / 61.3%** (Feb) ⟨ref⟩: the bottom quartile is two-thirds personal and coursework, the top three-fifths work. A one-shot personal request is
the classifier's "directive" by definition, and §2's wage-bill reading is undefined for a recipe or a homework question — no one's labour is
priced. Anthropic restricts its own wage-quartile figure to work for that reason, "the share of work-related tasks coming from the specified wage
quartile" (2026-06, Fig. 1.3 caption p. 7), and attributes its task-value fall to the same mix, "mostly due to an increase in simple factual
questions (e.g., sports outcomes, weather)" (2026-03, p. 8). **Design change:** a use-case leg in H3, confirmatory in Nov and Feb and untestable
in Aug, at §9(3)(d)–(e).

*The coding family.* High-wage, and automative by Anthropic's definition ("debug errors", 2025-03); SOC-15 is 77.1 / 75.7 / 69.9% of top-quartile
mass ⟨ref⟩. Handled by H3's SOC-15 and within-group legs, confirmatory rather than robustness.

*The country mix inside a task.* A task at global grain is a usage-weighted blend over countries, and the blend moves the outcome: with task mix
removed, "low-AUI countries are more likely to delegate complete tasks (automation)" (2025-09, p. 4, Fig. 2.11, reproduced by the steward at
−3.111834, partial R² 0.393687, N 111), and "Higher per capita usage countries … show lower automation" (2026-01, p. 35). India is 7.2% of usage
with coding over half of it (2025-09) and sits in the top quartile. Intersections are global only, so the per-task rate cannot be cleaned and no
reverse construction is identified — only about 71% of a wave's mass in a single category is recoverable from country rows (the steward's November
SOC-15 figure). Stated first in the post's limitations; not testable here.

*Cohorts and windows.* February carries the Super Bowl inflow, whose signature in the published data is the use-case mix — coursework 19% → 12%,
personal 35% → 42% (2026-03, p. 6, Fig. 1.2; reproduced at 19.3 → 12.4, 34.7 → 42.3 ⟨ref⟩) — and the cohort shift moves the wage distribution:
"Early adopters were highly technical. Our most recent users apply Claude to tasks that command lower wages in the labor market" (2026-06, p. 32).
Each wave is reported separately and never pooled, and persistence across the three tests conversation-sampling noise and cohort change, not task
sampling (§9(4), §12). Seychelles (`SC`), 2.47% of the November wave and in the file though not in the report (`data/ATLAS.md` §Traps 14), is
handled at C8 and §10.

**(4) Anthropic's own results that cut against or bound the framing. Marked: newly flagged, carried into the post.** Four. The turn counts of §3
are a mechanical prior for H2 through the classifier's own "minimal back-and-forth", and the reading §12 H2 states is Anthropic's, which this post
tests. The published category cross is not monotone in wage (2025-03, figures in §3): a prior against a clean gradient in either direction. The
published null on a correlate (2026-01, p. 40) is about the prompt, so the post reports the wage gradient beside it and calls a null here a second
null, not an extension. And Fig. 2.2's Opus gradient (2026-03, p. 14) means the high-wage work already draws the more capable model, so a positive
gradient may be a demand-for-intelligence result rather than a delegation one, the pattern-level split being the exploratory probe — while
automation and autonomy are distinct constructs (2026-01, p. 19), so June's finding that compute and autonomy rise with the value of the work does
**not** predict this gradient's sign; it is motivation, not a prior.

## 8. Data, confirmed at column level

**Steward's feasibility line, verbatim** (`programme/LONGLIST.md` LL-07; originally
`room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`):

> "**LL-07. FEASIBLE.** `onet_task::collaboration` exists at `geography=global` in all three long
> waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259 tasks, with global `onet_task_pct`
> weights in the same wave. Wage coverage is near-total, not marginal: through the shipped O\*NET
> 20.1 statements to `wage_data.csv` after `MedianSalary > 100` (1,084 of 1,090 rows), **99.4% /
> 99.0% / 99.3%** of *named*-task usage mass carries a wage. State the multi-holder rule (a task's
> wage is an aggregate over the occupations holding it). Log (e) 7."

The caveat is the last sentence, discharged below. The steward's confirming note is **`posts/post1/notes/feasibility.md`** (**FEASIBLE WITH
CAVEAT**; corrections in `room/steward-2026-09-16-feasibility-post1.md`): C1–C3 and C5 confirmed at column level; C4, C6, C7 and C8 amended below
on his numbers; §9(4)'s variance model and margin reset on his power table. C9 and C10 ⟨new⟩ are the referee's and need his confirmation before
signing.

**Cuts, at column level.**

| # | release (window) | grain | facet / category | metric | threshold / base |
|---|---|---|---|---|---|
| C1 | `release_2025_09_15` (4–11 Aug 2025), `platform_and_product = "Claude AI (Free and Pro)"` | `geography = global` | `onet_task::collaboration` (14,454 rows, `level` `'0'`) | `_pct` and `_count` per (task, pattern) | the six substantive patterns (`none` included) each have a per-cell floor of 15; the `_count` values of 1–59 are the folded `not_classified` residual (`data/ATLAS.md` §Thresholds), which is why a per-cell floor rule would be inert (§10). Per-task `_pct` sums to 100; the intersection publishes 100.00% of base named counts, so there is no cell suppression inside it |
| C2 | `release_2026_01_15` (13–20 Nov 2025), same platform label (sample is Free, Pro and Max) | `geography = global` | `onet_task::collaboration` (16,778 rows) | `_pct`, `_count` | same; classified 92.34% / `none` 2.02% / `not_classified` 5.64% of named counts; Seychelles sensitivity at C8 |
| C3 | `release_2026_03_24` (5–12 Feb 2026), `"Claude AI (Free, Pro, and Max)"` | `geography = global` | `onet_task::collaboration` (17,530 rows) | `_pct`, `_count` | same; counts are on a 1,000,000 sample base (named tasks carry 929,714) |
| C4 | each of C1–C3, same wave | `geography = global` | `onet_task` base facet | `onet_task_pct` (sums to exactly 100), `onet_task_count` (floor 15) | the usage weight. **The two frames have different residuals:** the base facet is named + `none` + `not_classified` (2,618 / 3,170 / 3,260 nodes), the intersection is named + `none` only (2,617 / 3,169 / 3,259). The analysis universe is the **2,616 / 3,168 / 3,258 named** nodes; dropping the two residual base nodes removes 8.13 / 6.49 / 7.03 pp of usage mass, not one node's worth |
| C5 | `release_2025_09_15/data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 × 9, 974 codes, 18,428 lower-cased keys) | — | task → O\*NET-SOC | `Task ID`, `O*NET-SOC Code`, `soc_major_group` | join key is the **lower-cased, stripped** task text, de-duplicated on that key before the merge (up to 34 rows on one key; §Traps 21). Confirmed: 2,616 / 3,168 / 3,258 named nodes in, **all matched**, 0 unmatched, 0 collisions |
| C6 | `release_2025_02_10/wage_data.csv` (O\*NET website wage scrape, Kilbourne-Quirk 2019 — **not** a BLS series) | — | occupation wage, primary | `MedianSalary` (annual), filtered `> 100` (1,084 of 1,090 rows) | join on the **full 10-character `O*NET-SOC Code` → `SOCcode`**, which is what Anthropic's released `plots.ipynb` (cell 26) does: **970 of 974** occupations; the `[:7]` prefix key of the first version matches **0 of 775** and is withdrawn. Anthropic applies the `> 100` filter *after* the join and after an `agg('first')` to occupation title, so the pre-filter here is this post's choice and is labelled as such, as is the ÷ 2080 hourly conversion. `MedianSalary` is top-coded at $208,000 (6 occupations, 0.05–0.06% of analysis mass); `-1` is a missing sentinel in `JobZone`/`ChanceAuto` (§Traps 10). Coverage: 2,607 / 3,154 / 3,244 tasks = **99.35 / 98.98 / 99.30% of named mass** |
| C7 | BLS Employment Projections (`data.bls.gov/projections/occupationProj`, 200, 831 detailed-SOC rows) | — | occupation wage, second source | `Median Annual Wage 2025` on `occ_code`; `Employment 2025` for the multi-holder wage rule | join `soc7` → `occ_code`, 775 in, **670 matched**. Prices **55.66 / 58.52 / 62.22% of named mass** (51.14 / 54.73 / 57.85 pp of the wave) against C6's 99%; used for rank and sign agreement (Spearman 0.9869 / 0.9859 / 0.9870 against C6), never for a level. OEWS, Anthropic's own source, 403s from this sandbox |
| C8 | `release_2026_01_15`, country rows | `geography = country` | `onet_task` | `onet_task_count` for **`SC`** (ISO-2 in this wave; `SYC` returns 0 rows) | Seychelles is 24,715 conversations, 2.47% of the wave. **The netting reaches the weights only**: `SC` has 0 rows of `onet_task::collaboration`, intersections being global only, so the per-task automation *rates* cannot be cleaned of it. Two cuts: (a) net `SC` out of the November task weights (mean \|shift\| 0.0012 pp, up to 0.58 pp on one task); (b) a pre-registered drop of the tasks where `SC` exceeds 10% of the global count (23 tasks, 11.59 pp of wave mass, of which **9.04 pp sits in the top wage quartile**), with the >20% variant (14 tasks, 1.97 pp) beside it |
| C9 ⟨new⟩ | `release_2026_01_15`, `release_2026_03_24` | `geography = global` | `onet_task::use_case` (13,908 rows Nov; 14,430 Feb; **0 rows in Aug 2025**) | `_pct`, `_count` per (task, category) | categories `coursework` / `personal` / `work` / `not_classified`, plus `none` in Feb — neither residual label may be hard-coded (§Facets). A per-task work share is a share of published cells: up to three cells can fold into `not_classified` (maximum 39 conversations, §Thresholds), and tasks with a published work/coursework split hold 87.92 / 86.96 of the 93.51 / 92.97 named mass. Coverage of this post's analysis set: 100% of tasks in both waves ⟨ref⟩ |
| C10 ⟨new⟩ | `release_2025_03_27/automation_vs_augmentation_by_task.csv` (Feb–Mar 2025) | flat file, global | per-task collaboration split, five patterns plus a `filtered` residual | row ratios summing to exactly 1.0; `task_pct_v2.csv` weights | a fourth task-level window on the unchanged taxonomy: 3,364 tasks matched across the release's three task files, carrying 98.2183 of 100 `pct`. **No counts**, `filtered` median 0.30 with **1,066 rows at filtered = 1.0**, and weighting `pct` by the five classified ratios leaves 90.1561 of 100 (`data/ATLAS.md` log (j) 4) — which is why it sits outside the confirmatory persistence set and is design-based only (§10) |

Grain rule observed: intersections are **global only** in all three long waves (`data/ATLAS.md` §Cuts 10), so there is no country or state version
of this post; `soc_occupation` is absent as a facet in the two 2026 waves (§Cuts 13), which is why H3's occupational split runs through C5.

**The task → SOC join, the vintage, the wage rule and the allocation rule, stated here for the construction triple.** A task text is joined to
O\*NET-SOC through C5 on the lower-cased stripped task text, de-duplicated on that key, and priced through C6 on the full 10-character O\*NET-SOC
code.

*Vintage, as a stated choice.* The shipped 20.1 file carries **2010** O\*NET-SOC codes and `wage_data.csv` joins to exactly those (970 of 974);
the 2019 taxonomy — "This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage" (2026-03, footnote 2 p. 11) — is
reachable only through the external O\*NET Center crosswalk at `data/fetch/supplementary_onet.py` (1,164 rows, 1,110 2010 codes, **44
one-to-many**), and Anthropic's published occupational series reproduces only on that recode (`posts/post2/notes/feasibility.md` §2). Rule: **the
wage is attached on the shipped 2010 codes**, the only taxonomy the wage file joins to; **any occupational grouping** is reported on the **2019
recode** as primary with the 2010 grouping beside it. It matters: 55 / 71 / 70 tasks change their major-group set between vintages ⟨ref⟩.

*The wage of a task with several holders.* Anthropic's rule is employment-and-time weighted (footnote 5, p. 11); the public files carry no
time-on-task weight, so the pre-registered primary rule is the **employment-weighted mean over holder occupations** (BLS-EP employment on
`occ_code`), with the equal-split mean and the modal holder beside it in every table. BLS-EP employment is 7-character only, so the rule is
identified across distinct 7-char SOCs and degenerates to the equal-split mean for the two tasks whose holders sit inside one. Exposure is small:
one 10-character code for all but **74 / 93 / 86** tasks (Aug / Nov / Feb), 72 / 91 / 84 at 7-char SOC, **4.44 / 5.98 / 4.87% of named** mass, the
two wages correlating at **0.9998** with a maximum single-task gap of $6.38/hr.

*Allocating usage mass to an occupation or a group* — a different construction from the wage, and the one post3 and post8 cite. (i) The allocation
unit is the **(task key, 2019 code) pair, de-duplicated**: 18 of the 20,081 (key, 2010 code, 2019 code) rows are a second 2010 source for a pair
already present, and double-counting them raises the February API SOC-15 share from 61.6363 to 61.7795 (steward, `a452d01`,
`data/replication/post2_recode_attribution.py`); on this post's named Claude.ai tasks there are **6 duplicate (task key, 2019 code) rows per
wave** ⟨ref⟩. (ii) Where a 2010 code recodes to several 2019 codes, mass is **split equally over the distinct 2019 codes held by the key** (w =
1/n), as `data/replication/soc15_figA1_2026_03.py` does. (iii) The **6 / 10 / 9** tasks whose holders span more than one major group (0.28–0.31%
of named mass) go to the holder with the largest BLS-EP employment; where employment is missing or tied, to the lexicographically smallest
10-character O\*NET-SOC code; they are also reported as a 23rd bucket in the leave-one-group-out series. (iv) The **primary allocation rule is the
equal split over distinct holder codes**, the released convention, with modal-holder and employment-weighted allocations beside it. The bound is
on a *share*: across allocation rules the SOC-15 share moves by **≤ 0.17–0.18 pp** (LL-32 at ≤0.17 pp; ≤0.18 pp on the four-rule set in
`posts/post3/notes/feasibility.md` §4; the referee's equal-split and modal shares are 40.04 / 37.29 / 33.26 against 40.12 / 37.36 / 33.32) and the
22-group ranking by at most one position (Aug) or none (Nov, Feb). It is **not** a bound on a within-category statistic, which moves up to 0.39
pp, nor on this post's gradient, re-estimated under all three rules (§10).

**The published numbers this reproduces first.** (i) Each wave's global collaboration split on the base its report used: 49.0980 (Aug 2025, all
seven patterns, published "49%"), 45.3554 (Nov 2025, "45%"), 44.1569 (Feb 2026, "44%") — and the same three on the five-classified-pattern
analysis base (51.0698 / 46.7394 / 45.5456), the base named every time; all six reproduced by the steward to four decimals and independently by
the referee. (ii) The estimator is Anthropic's: the released `collaboration_task_regression` returns Figure 2.11 exactly (−3.111834, partial R²
0.393687, N 111); its spec keeps the `none` task node and drops the `none`/`not_classified` patterns from each task's base, and this post's
universe is the named nodes with the `none`-node variant as robustness. (iii) The internal check that licenses the estimator: the usage-weighted
mean of per-task automation shares must return the wave's five-pattern value **within 0.36 pp and positive in all three waves** — it returns
+0.1303 / +0.2931 / +0.3510, the gap being not suppression (the intersection publishes 100.00% of base named counts) but the named-task
restriction plus the intersection's own `not_classified` *pattern*, absent from the marginal facet (4.64 / 5.64 / 5.90% of named counts). (iv) A
**known non-reproduction**, stated not attempted, on matched windows: task value rebuilds at $35.34 (Aug) / $35.08 (Nov) / $34.36 (Feb) on C6 and
$37.64 / $37.69 / $37.55 on C7, against Fig. 1.4's $48.9 / $48.3 / $47.9 for the same windows, while the *changes* are close — Nov→Feb published
−$0.40 against a rebuilt −$0.72, Aug→Feb published −$1.00 against −$0.98 (the "−$1.40" of the first version set a published Jan-2025→Feb-2026
change against a Nov→Feb rebuild). Four causes of the level gap, so that "non-reproduction" is not read as a failure of the released data: a 2019
O\*NET website scrape against OEWS May 2024; those dollars expressed in February-2026 dollars by an unstated deflator; no time-on-task weights;
and equal-split or employment weights in place of employment-and-time weights. Hence the rank-based design.

**The analysis set.** Tasks with a C6 wage and at least one classified-pattern cell: **1,802 / 2,075 / 2,188** tasks, **97.15 / 96.23 / 96.52% of
named mass**, on 818,673 / 854,432 / 848,716 classified conversations. Both losses are audited: 5 / 12 / 12 tasks with a classified cell and no
wage, 805 / 1,079 / 1,056 with a wage and no classified cell, dropped explicitly and never zeroed. Usage-weighted quartile boundaries on the
primary wage rule are $25.78 / $35.79 / $43.40 (Aug), $25.78 / $34.56 / $43.40 (Nov) and $24.00 / $34.40 / $43.40 (Feb); quartile mean wages about
$19 / $31 / $39 / $49–50 ⟨ref⟩.

## 9. Confirmatory tests and the exploratory allowance

1. **The key number, and the ordered rule that assigns the outcome.** Per wave, D = the usage-weighted automation share of the top wage quartile
   minus that of the bottom, on the five-classified-pattern base, with the `none` share beside it in every table so the base is never implicit,
   and quartile boundaries drawn on usage-weighted wage; interval two-sided 95% under the model in (4). **δ = 1 pp** is the pre-registered
   smallest effect of interest: more than twice the MDE(80%) of 0.42–0.43 pp, and the point at which §2's quantity begins to move (0.11–0.12 pp of
   wage-weighted-minus-unweighted share per point of gap ⟨ref⟩). Δ_W is published with its own interval beside D, and the **materiality line is
   separate and higher** — a full point of Δ_W needs a gap of roughly 8–9 pp, so below that the post calls the weighting of a published automation
   share signed and small, never wrong. The rule, in order, first match winning, so every result has exactly one owner: **(1)** lower bound > +1
   pp in all three waves → **H1**; **(2)** upper bound < −1 pp in all three → **H2**; **(3)** otherwise, every interval excluding zero with the
   same sign in all three → **O-A**; **(4)** otherwise, every interval inside ±1 pp → **H4**; **(5)** otherwise → **O-B** (signs disagreeing
   across waves, or one wave past the margin while another does not resolve — the +0.8 / +0.8 / −0.2 pp case). H3 then qualifies whichever of H1,
   H2 or O-A was declared; under H4 or O-B it is not evaluated and the post says so.
2. **The continuous companion.** The usage-weighted slope of the automation share in the task's hourly wage, per +$10/hr in Anthropic's own
   Opus-gradient form, sign and significance only.
3. **H3 — composition, five legs, confirmatory, all keyed to the fraction of D retained.** (a) D with SOC-15 excluded — 39.86 / 37.12 / 33.11% of
   analysis mass, 77.1 / 75.7 / 69.9% of top-quartile mass, so it dominates the leave-one-out series by construction, which the post states; (b) D
   within SOC major group, averaged by usage weight **over the groups that span the global bottom and top quartile (7 / 8 / 6 of 22 span all
   four)**, the rest reported as not identified rather than as zeros; (c) 22 leave-one-group-out re-estimates; (d) each wage quartile's work /
   personal / coursework mix reported beside its automation share, Nov and Feb (C9); (e) D re-estimated on the pre-registered set of
   **work-dominant tasks** (work share ≥ 50% of a task's published use-case cells, fixed here and not left open) and with the task's work share as
   a covariate in the continuous companion. August publishes no `use_case` intersection and is untestable on (d)–(e). H3 is declared if D loses
   more than half its size, or its sign, on at least one of (a), (b) and (e).
4. **The variance model, named in advance.** Primary: **conversation-level binomial on the classified counts, task mix held fixed** — the right
   model for a statement about the conversations in these three windows. Its MDE(80%, two-sided 5%) is **0.42 / 0.42 / 0.43 pp**
   (`posts/post1/notes/feasibility.md` §4; the referee reproduces SE 0.151 / 0.149 / 0.151 pp), so δ = 1 pp is deliverable where the first
   version's ±3 pp was not under its own task-resampling bootstrap (MDE 3.26 / 3.44 / 3.68 pp). The design-based model — resampling tasks
   equal-probability, which is what generalises to other task mixes — is reported beside it as the bound it is: MDE **12.5 / 17.4 / 16.1 pp**,
   resolving nothing below about 12 pp as a statement about tasks, so every close in §12 is written about these windows' conversations. The **Kish
   effective N** on the `onet_task_pct` weights is printed beside the nominal count throughout: **99.7 / 89.5 / 134.3** against a nominal 2,616 /
   3,168 / 3,258, and **11.5 to 19 tasks** in the top quartile depending on the wage rule — which is why the task-level models cannot carry a
   null. Nothing is reported as "underpowered" for the within-window statement; the generalisation to other task mixes is, and that sentence
   appears in every close.

**Exploratory allowance: three tests, after the confirmatory set, none in the headline and each labelled exploratory.** (a) The same gradient on
the 1P API global intersection (`onet_task::collaboration`, 11,660 rows at global in the February file ⟨ref⟩), to say whether the sign is a
property of the surface rather than of the work — the API is automation-dominant and its February sample includes Claude Code ("This includes data
from Claude Code", 2026-03, footnote 1 p. 11), which moves its automation share by construction, so this is context, not a replication. (b) The
pattern-level split: which of directive and feedback loop carries a positive gradient, and whether learning, task iteration and validation move
the other way — the probe for §7(4)'s demand-for-intelligence rival. (c) The gradient against `JobZone` from C6 (99.22 / 98.83 / 99.06% of named
mass with the 119 `-1` sentinel occupations dropped; the 99.8% of the first version counted the sentinels), a non-wage ordering separating price
from required preparation. No further tests; any additional cut is a logged deviation.

## 10. Noise and robustness required

- **Persistence across windows** — in the confirmatory rule: three waves, estimated and reported separately, never pooled or spliced. C10's
  Feb–Mar 2025 file is a **fourth** task-level window on the unchanged taxonomy, reported design-based only and outside the confirmatory set: it
  publishes no counts (so no conversation-level interval), its residual is a `filtered` ratio with 1,066 tasks entirely filtered, and its weights
  are `task_pct_v2`.
- **Leave-one-out** — 22 leave-one-group-out re-estimates plus the group-spanning bucket (confirmatory under H3) and a leave-out of the ten
  largest tasks by usage mass, 19.4410 pp of the Feb-2026 wave and **20.91% of named** mass (Aug 24.97%, Nov 25.93%); the denominator is stated
  each time.
- **Flagged units excluded** — November's netting reaches the task **weights** only (C8), so its per-task automation **rates** keep a geography
  that reaches 64% of one task's global count and sits behind 9.04 pp of the top quartile. Three pre-registered consequences: the weight-netted
  re-estimate; the drop of tasks where `SC` exceeds 10% of the global count (23 tasks, 11.59 pp of wave mass), with the >20% variant beside it;
  and November treated as corroborated by August and February rather than as independent confirmation. Utah's August anomaly is a `state_us` row
  and cannot move a global intersection. The low-count sensitivity cut drops tasks with fewer than 100 classified conversations, fixed here so the
  pre-registration carries no free parameter; a per-cell floor rule would be inert (C1).
- **Placebo** — a permutation null with one role and one place: the wage vector is permuted across tasks within SOC major group and the estimator
  re-run, and the distribution is reported **here, as the task-level bound it is** — its band is of the order of the design-based MDE, 12.5–17.4
  pp, since the top quartile holds 11.5–19 effective tasks. It is in no decision rule (item 1(iv)).
- **Country mix, named and not testable** — §7(3)'s fourth channel: uncleanable at this grain, no reverse construction identified, and raised
  first in the post's limitations rather than claimed as closed.
- **Second implementation** — the gradient rebuilt independently by the analyst on the second wage source (C7) and under both alternative wage
  rules and both alternative allocation rules, sign agreement required for any claim, with the wage join re-run from the task side and the SOC
  side as two builds.

## 11. Literature check

Searches run for the long-list entry and re-checked here: Anthropic's corpus (`wiki/reports/`, every Economic Index report and appendix, the
labour-market and scenarios papers) for "wage", "value", "collaboration", "automation share"; and the comparators in `data/ATLAS.md`
§Supplementary sources. Closest prior work: **Chatterji et al. (2025)**, the nearest rival measurement — an Asking/Doing split on a consumer
surface with work usage concentrated in highly paid occupations, never regressed on a wage; **Tomlinson et al. (2025)**, where the wage enters an
applicability index rather than the delegation measure; **Acemoglu (2025)**, which supplies the reason the sign matters and no measurement; and
**Anthropic**, whose wage cuts and nulls are listed in §3 and §4 and which crosses the collaboration facet with wage nowhere. This post sits in
the empty cell: a usage-weighted estimate of the delegation share as a function of the price of the work, on Anthropic's own published
intersection, in three waves.

## 12. What the closing section will be able to say

**If H1 holds (a gradient above the margin, upward).** In each of the three windows, Claude.ai conversations on top-quartile tasks were delegated
at a rate more than a point above those on bottom-quartile tasks — and X points above with Computer & Mathematical tasks excluded, the number that
matters, that family being 70–77% of the top quartile's usage. Weighting the published automation share by the wage of the work raises it by Δ_W
points, the number a model of labour payments should take; a claim about work in general is not licensed, since a design that resamples tasks
resolves nothing below about twelve points.

**If H2 holds (a gradient above the margin, downward).** In each of the three windows, Claude.ai conversations on high-wage tasks were delegated
at a rate more than a point *below* those on low-wage tasks, with the learning, task-iteration and validation shares rising across quartiles.
Anthropic had offered this reading for its own turn counts — "If the human remains involved in the highest-value tasks, the pattern looks more
labor-augmenting than labor-displacing" (2026-06, pp. 13–14) — and it holds on the measure that defines delegation, on these windows'
conversations.

**If O-A holds (a persistent gradient below the margin).** Delegation on Claude.ai does track the price of the work, in the direction stated and
in all three windows, and the gradient is smaller than a point: weighting a published automation share by the wage bill moves it by roughly a
tenth of a point per point of gap, so the direction is the finding and the correction is not a repair. For anyone calibrating an exposure
parameter the sign is then known and the magnitude bounds how much it matters.

**If H3 holds (composition, not price).** The relation between delegation on Claude.ai and the price of the work is a mix that travels with wage:
coding tasks, both the best paid and, by Anthropic's own definition of automative use, the most fully handed over — or use case, since the
low-wage work in this data is largely personal and coursework conversations rather than low-wage labour, and a one-shot personal request is
directive by construction. What looks like a statement about the wage distribution is one about software, or about who is asking; anyone weighting
an automation share by wage must know which.

**If H4 holds (the null, at the stated margin).** In each of the three windows the delegated share of Claude.ai conversations on top-quartile and
bottom-quartile tasks differed by less than one percentage point — and by less again with Computer & Mathematical tasks excluded — a margin the
design resolves with an MDE of 0.42 to 0.43 percentage points on these windows' conversations, though not as a statement about tasks in general,
where nothing below about twelve points is resolved. That sets a second null beside Anthropic's null for the education level of the prompt: for
weighting purposes an unweighted automation share is, in these windows, the right number after all.

**If O-B holds (no persistent gradient).** The gradient is not a stable feature of these three Claude.ai windows: it reaches past the margin in
one and is unresolved or reversed in another, over a period in which Anthropic reports its own user base moving toward lower-wage tasks. The wage
of the work then does not order delegation in a way that survives a change of window, and the post says what a longer released series would
settle.
