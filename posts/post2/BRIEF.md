# post2 · When a task takes a larger share of AI use on the enterprise API, does it take a smaller share on the consumer app?

*Candidate LL-11. Brief of record, written on `team/templates/BRIEF.md`. The question and the title
above are the frozen forms and settle the two title-form defects the short list carried: the
question now says AI (criterion 6; referee audit-2 correction 20), and "grow"/"shrink" are gone,
because the design measures shares and not levels (editor's note, `room/editor-2026-09-16-sketch-LL-11.md`,
"Title form"). Findings will say Claude.*

## 1. The question

When an O\*NET task takes a larger share of AI use on the enterprise-facing first-party API, does
it take a smaller share of AI use on the consumer-facing app?

## 2. Why it matters, and to whom

A published, dated claim says work is moving between the two surfaces on which Anthropic measures
AI use: "Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated
workflows in our first-party API traffic" (`economic-index-2026-03-report`, p.7, 24 March 2026).
The economic content of that sentence is a flow. If tasks move from a surface where a person is in
the loop to one where a service calls the model without one, the same work is being done under a
different division of labour, and the report says so: "As tasks migrate to the API, they may become
more exposed to automation. API workflows are far more likely to be directive, with less need for a
human in the loop" (ibid., p.9), and "we expect that this migration from Claude.ai to the API may
signal more imminent transformation of work for the associated jobs" (ibid., p.7).

The claim is load-bearing outside its own chapter. Anthropic's displacement measure raises an
occupation's exposure when "It has a relatively higher share of automated use patterns or API
implementation" (`labor-market-impacts-2026-03`, PDF p.5), and the second-ranked occupation on that
measure is ranked there because of the surface its tasks appear on: "Customer Service
Representatives, whose main tasks we increasingly see in first-party API traffic" (ibid., pp.7–8,
Figure 3). Anyone quoting the migration — a policy analyst reading the exposure ranking, the
Institute's own agenda item on how AI changes jobs, an economist deciding whether the Index carries
a leading indicator — is relying on a correspondence between two surfaces that has never been
measured as a correspondence.

The public Economic Index releases can say something no other source can: they publish the same
task taxonomy on both surfaces in the same week, three times. No provider publishes a consumer and
an enterprise task series on one taxonomy, and Anthropic's own reports report the two series side by
side without ever relating them task by task. The answer also tells Anthropic what to publish: the
Institute's only concrete data commitment is "More granular information from The Anthropic Economic
Index, at a higher cadence" (`institute-agenda-2026-05`, *Share 1*), and a negative result here
names the missing field.

## 3. The thread of Anthropic's inquiry this builds on

Thread **T3** (automation, augmentation, delegation), with **T1** (adoption and diffusion).
`programme/THREADS.md` records the migration as the mentor's stated mechanism for imminent
labour-market change, quoting the two conjectures above (T3 (e)), and records as open that "The 1P
API's falling automation is not decomposed into behaviour and Claude Code's call-splitting"
(T3 (c)). Three ledger items are the gap:

- `L-2026-03-R5-17` **open** — conjecture, "As tasks migrate to the API, they may become more
  exposed to automation. API workflows are far more likely to be directive, with less need for a
  human in the loop" (p.9). The ledger's own note: the migration is asserted, never measured as a
  migration, and it cannot be measured as a *series*, because the API `directive` share jumps
  58.22 → 80.88 across the 2026-03-24 → 2026-06-26 boundary at which the documentation stops
  including Claude Code.
- `L-2026-03-R5-18` **open** — conjecture, "we expect that this migration from Claude.ai to the API
  may signal more imminent transformation of work for the associated jobs" (p.7).
- `L-2026-01-R4-23` **open** — promised follow-up, "In future work, we could leverage our 1P API
  data to understand which of these tasks are being integrated into production workflows" (p.45).
  The migration story is restated in `economic-index-2026-03-report` p.7 without that analysis.

What the thread has established: both surfaces' task and collaboration series, wave by wave, and the
direction of each. Coding's share on Claude.ai fell "from a peak of 40% in March 2025 to 34% in
November 2025" while on the API it "edged higher from 44% in August to 46% in November 2025"
(`economic-index-2026-01-report`, p.7). Anthropic also states its own mechanism for part of the API
movement: "Claude Code's agentic architecture splits coding work into smaller API calls, which are
labeled as distinct tasks. So while coding's overall share of API traffic has grown, it is spread
across many task categories rather than concentrated in a few" (`economic-index-2026-03-report`,
p.6). Where it is open: nothing in the corpus relates a task's movement on one surface to the same
task's movement on the other.

## 4. Overlap, stated

**What Anthropic has shown.** Two independently moving share series, one per surface, with a
category-level relative change stated for coding: "Since August 2025, the share of tasks in this
category has increased by 14% in the API and decreased by 18% in Claude.ai"
(`economic-index-2026-03-report`, p.7), plus the mechanism at p.6 and the labour-market reading at
p.9. What is new here: the task-level correspondence between the two surfaces' *changes* — whether
the tasks that gain share on one lose it on the other — which is the statistic the word "migration"
asserts and no publication reports.

**What others have shown.** Chatterji et al., *How People Use ChatGPT* (NBER Working Paper 34255,
September 2025), documents a consumer chatbot at scale and by construction excludes the other side
of this margin: "We exclude users on non-consumer plans (Business f.k.a. Teams, Enterprise,
Education)". Dillon, Jaffe, Immorlica and Stanton, *Shifting Work Patterns with Generative AI*
(NBER Working Paper 33795 / arXiv 2504.11436, May 2025, revised November 2025), is a firm-level
field experiment that reports it does "not detect shifts in the quantity or composition of workers'
tasks resulting from individual-level AI provision" — within-firm work patterns, not a cross-surface
task flow. What is new here: a measured flow between a consumer and an enterprise surface of the
same model, on one task taxonomy.

**Separation from the two short-list partners** (`programme/SHORTLIST.md` §5, pairs 1 and 2; the
director's pairs ruling of this session). Against **post3 (LL-36)**: this post headlines the
cross-surface correspondence of task-share changes and **does not** headline coding's share of use
as its key number; post3 headlines composition inside coding and cites this post for the migration
frame. Against **post4 (LL-09)**: the two share one input series, the November→February change in a
task's Claude.ai share, and therefore the same February exposure; post4 headlines the relation
between Claude's measured success rate and subsequent use with the August-2025 share as its
instrument, this post headlines the cross-surface correlation. Both posts name the shared
November→February Claude.ai series and the Super Bowl exposure — here in §7, item 3.

## 5. Contribution

If task shares move in opposite directions across the two surfaces, the post publishes the first
measure of the corpus's central leading-indicator claim and names the tasks making the move; if they
do not, the post shows that the two surfaces have been growing independently, so the migration
sentence describes two series rather than a flow and the exposure framing built on it loses its
anchor.

## 6. Hypotheses

**H1 · Migration.** A task's change in Claude.ai share and its change in API share are negatively
related across the 1,241 tasks published on both surfaces in all three windows.
*Signature only it predicts:* the negative relation appears in **both** adjacent windows
(August→November 2025 and November 2025→February 2026), holds in the non-coding tasks as well as
the coding tasks, and is larger in magnitude than the same statistic computed *within* each surface
(the mechanical share-accounting benchmark).
*What would count against it:* either window's correlation not distinguishable from zero at the
stated power; the two windows' correlations disagreeing in sign; or the relation present only in
coding tasks.

**H2 · Independent growth.** The two surfaces' task mixes move for their own reasons and the
cross-surface relation is zero.
*Signature:* correlations near zero in both windows and on the long August→February change, with
intervals that exclude the migration magnitudes, while each surface's own task mix still moves.
*What would count against it:* a negative correlation outside the interval around zero in both
windows, or a negative long-change correlation with both adjacent windows negative.

**H3 · Common denominator, not a flow.** The negative relation is produced by composition shocks
moving one surface's denominator for every task at once — first-time Claude.ai users in February
above all.
*Signature:* the relation concentrates in the November→February window and vanishes in
August→November; and the within-surface benchmark statistic is of similar magnitude to the
cross-surface one.
*What would count against it:* equal-sized negative correlations in both windows, with the
within-surface benchmark materially smaller.

**H4 · Call-splitting, not a flow.** The API's coding-task shares rise because agentic coding is
labelled as many tasks, which dilutes non-coding API shares arithmetically; Claude.ai's coding share
falls for user-mix reasons. Anthropic states the first half itself (p.6, quoted in §3).
*Signature:* the negative relation is carried by tasks in SOC major group 15 and is absent in the
pre-specified non-coding control set.
*What would count against it:* a negative correlation of similar magnitude in the non-coding
control.

## 7. Assumptions sweep

**(1) Value judgement in the framing — handled, with a change made here.** "Migration" and
"exposure" carry a direction of travel and a loss; "grow" and "shrink" claim levels the design
cannot see. The change: the question and title are now in share language and name no winner
(§1); the words "exposed", "at risk" and "transformation" appear in the post only inside quotation
marks from Anthropic; and the post states that a share moving is not a volume moving. Anthropic's
own construct is a share of sampled records, not a count of work: "Figure 1.1: Usage shares among
top 10 tasks over time by platform, Claude.ai and 1P API / Share of conversations assigned to the
10 most prevalent O\*NET tasks, by platform and report version" (`economic-index-2026-03-report`,
p.5).

**(2) Construct mapping — needs a design change, and the change is specified.** The two surfaces'
shares do not share a unit. Anthropic's verbatim definition: "we analyze a random sample of 1M
conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as 'consumer
data' since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API
traffic (we also refer to this as 'enterprise data' since it mostly represents enterprise use)… For
1P API data, each record is a prompt-response pair from our sample period which in some instances is
mid-session for multi-turn interactions" (`economic-index-2026-01-report`, fn 1, p.17); and
"We sample 1 million conversations from both Claude.ai, our consumer-facing web product, and our
first-party API, the developer-facing interface for integrating Claude into products and workflows"
(`economic-index-2026-03-report`, p.5). The classifiers are also not identical across surfaces: the
API collaboration prompt carries "IMPORTANT: These interactions are happening via an LLM API, not an
actual human-AI assistant conversation… For the purposes of this task, when we say 'human', we mean
'end user'" (`economic-index-2026-01-report` online appendix, p.19, §2.3.4). **The change:** no
statistic in this post compares a level or a share *across* surfaces; every estimate is a
correlation of *within-surface changes*, each computed on its own denominator, and the post states
in the measurement paragraph that a share of prompt–response pairs is not a share of conversations.
For the reproduction leg the occupational label is a task label: "Occupation is inferred from the
task, not the user" (`/mnt/memory/standards/terminology.md`; `data/ATLAS.md` §Traps 36), and the
post says so beside the reproduced number.

**(3) Composition and selection — newly flagged; the design change is the window split.** The
February 2026 Claude.ai window carries an inflow of new users: "Our sampling period overlapped with
the release of our Super Bowl advertisements, which brought many first-time users"
(`economic-index-2026-03-report`, fn 3, p.18) and "At the same time, increasing signups beginning
around February brought more casual AI users" (ibid., p.6). Those users move the Claude.ai
denominator for every task at once, so a task's share can fall with nothing leaving it. The API
population moves too: its sample "includes data from Claude Code" (ibid., fn 1, p.11), and the
documentation stops including Claude Code after this wave, which is why the series stops at
2026-03-24. **The change:** the two adjacent windows are estimated and reported separately and are
never pooled into the headline; the November→February estimate is reported with the inflow named in
the same sentence; the within-surface benchmark statistic is reported beside every cross-surface
estimate; and the coding / non-coding split is pre-specified rather than chosen after the fact.

**(4) Anthropic's own results that cut against or bound the framing — handled.** Three bound it.
First, Anthropic's own mechanism makes part of the predicted pattern arithmetic rather than
behavioural: "Claude Code's agentic architecture splits coding work into smaller API calls, which
are labeled as distinct tasks" (p.6) — so the post carries it as rival **H4** with its own
signature, not as a closing caveat. Second, the Claude.ai coding decline predates the API series:
"down from a peak of 40% in March 2025 to 34% in November 2025"
(`economic-index-2026-01-report`, p.7), and the API series begins only in August 2025
(`economic-index-2026-03-report`, Fig. 1.1, p.5), so no part of the fall before August 2025 can be
read as migration. Third, the task universe is nearly closed between these waves — "Our data from
this report showed many fewer novel O\*NET tasks than in our previous report" (ibid., p.7) — which
supports a matched panel but also means entry and exit are small and cannot carry the result; the
panel's mass coverage (80.9% and 83.2%) is reported beside every estimate.

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`programme/LONGLIST.md`, LL-11, quoting
`room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`), caveat included:

> "**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both surfaces in all three pre-June waves:
> named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251 / 2,297 (API); pairwise overlap
> 1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**, carrying **80.9%** of Claude.ai and
> **83.2%** of API Feb-2026 named mass. Shares only, and never past 2026-03-24, as your entry says.
> Log (e) 10."

The steward's confirming note is **`posts/post2/notes/feasibility.md`**; it confirms or contradicts
each cut below at column level, with a command per cut. Cuts are named against `data/ATLAS.md`
(§Which cuts exist at which grain, §Cuts that do not exist, §Conventions, §Thresholds, §Traps).

| # | release (window) | file | geography | facet · level | variable | threshold / base |
|---|---|---|---|---|---|---|
| 1 | `release_2025_09_15` (4–11 Aug 2025) | Claude.ai long file | `geography == global` | `onet_task` · L0 | `onet_task_pct` | privacy floor `onet_task_count ≥ 15`, applied upstream |
| 2 | `release_2026_01_15` (13–20 Nov 2025) | Claude.ai long file | `global` | `onet_task` · L0 | `onet_task_pct` | same floor; denominator 999,875 |
| 3 | `release_2026_03_24` (5–12 Feb 2026) | Claude.ai long file | `global` | `onet_task` · L0 | `onet_task_pct` | same floor; counts on a 1,000,000 sample base (§Other bases) |
| 4–6 | the same three releases | 1P API file (global only, §Components) | `global` | `onet_task` · L0 | `onet_task_pct` | same floor; no `usage_count` in any API file (§Cuts 18) |
| 7 | `release_2025_09_15` reference | `data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 × 9, with `soc_major_group`) | — | — | task text → SOC major group | join key is the lower-cased, stripped task text (§Taxonomies) |

**Panel, exclusions and conventions.** `none` and `not_classified` are dropped — they are different
things and both must go (§Traps 24). The analysis panel is the **1,241** tasks published on both
surfaces in all three waves; absent is not zero, so a task missing from any frame is excluded rather
than set to zero (§Traps 25). `{facet}_pct` is a share of the geography total *including*
`not_classified` (§Other bases), so the primary estimates use the published `onet_task_pct`
unrenormalised, with a renormalisation over the 1,241-task panel as a stated sensitivity. Reads use
`keep_default_na=False` everywhere and `na_values=[]` on 2026-03-24, and `level` is cast to string
after any parquet read (§Traps 1, 2, 7). Case-variant duplicate task strings are de-duplicated
before the text join, by a stated rule, with collisions counted (§Traps 21). **The series stops at
2026-03-24**: across the next boundary the API `directive` share jumps 58.22 → 80.88 where the
documentation stops including Claude Code (§Components), so the June release is not used at all.

**Supplementary data.** None. The join is task text inside the Index.

**Levels.** Shares only, per the steward's caveat. The API files carry no usage count (§Cuts 18);
Claude.ai carries `onet_task_count` on sample bases within 3.7% of each other across the three
waves, so a level diagnostic is possible on one surface only. It is used only as a diagnostic for
H3, never as an outcome, and the steward is asked to confirm whether any `_count` exists for
`onet_task` on the API side.

**The published number this reproduces first** (criterion 3; referee correction 4). Before any new
number: "Since August 2025, the share of tasks in this category has increased by 14% in the API and
decreased by 18% in Claude.ai" (`economic-index-2026-03-report`, p.7), "this category" being
Computer and Mathematical. The reproduction rebuilds SOC major group 15 from global `onet_task_pct`
through cut 7, states the base (classified or all-conversation) and states the vintage caveat
Anthropic attaches to its own occupational number: "This number uses 2019 O\*NET-SOC codes, while
previous reports use the 2010 vintage" (ibid., fn 2, p.11). The task → SOC join and the multi-holder
rule are **stated in post1 (LL-07)**, which is written first in the construction triple
(`programme/SHORTLIST.md` §5, pair 3; director's pairs ruling); this post cites post1's statement
rather than re-deriving it, and adds nothing to it. One flag for the steward: the steward's LL-36
line (`room/steward-2026-09-16-longlist-feasibility-batch-3-answers.md`) gives a SOC-15
reconstruction of "Claude.ai 39.03 → 36.02 → **32.23** (classified); 1P API 49.98 → 51.73 → 51.61",
which implies about −17.4% on Claude.ai and about +3% on the API, not +14%. The Claude.ai leg
therefore looks reproducible and the API leg may not be on this base and vintage. The
pre-registration fixes the rule in advance: the reproduction is reported as run, with base and
vintage named; if the API leg does not reproduce, the discrepancy is reported as the first result
and the confirmatory design proceeds unchanged, since no test in §9 depends on the published
relative change.

## 9. Confirmatory tests and the exploratory allowance

Four confirmatory tests, one per hypothesis, all on the 1,241-task panel and all pre-registered
before any estimate is read:

1. **H1.** The correlation across tasks between the change in a task's Claude.ai share and the change
   in its API share, computed separately in each adjacent window (August→November, November→February),
   with confidence intervals; the confirmatory claim requires both to be negative with intervals
   excluding zero. The long August→February change is reported as a third estimate. Key number: the
   window correlations with their intervals. At 1,241 tasks a correlation of about 0.08 is detectable
   at conventional power, so a weak but real relation would be visible and a strong one unmistakable;
   the minimum detectable effect is printed beside every estimate, and beside a null it is the
   finding.
2. **H2.** The same two correlations tested against zero, reported as an interval rather than a
   verdict, so that a null is a measured null and not an absence of evidence.
3. **H3.** The same statistic computed *within* each surface (a task's change against the
   mass-weighted change of the other tasks on the same surface) as the share-accounting benchmark,
   and the window-by-window comparison: a relation carried by November→February alone is the
   composition reading.
4. **H4.** The same estimate on the pre-specified coding set (SOC major group 15 through cut 7) and
   on the non-coding control set, with the difference between them reported.

**Exploratory allowance: two tests, after the confirmatory set, labelled exploratory in the post and
excluded from the headline.** (a) Naming the tasks in the migrating quadrant — the largest negative
products of the two changes — so the post can say which work is making the move; this is
description, not inference, and carries no interval. (b) Whether the relation is stronger among tasks
whose API use is more directive, using `onet_task::collaboration` at global on the API side, which is
the nearest public test of the mentor's conjecture that migrating tasks are the less supervised ones
(`economic-index-2026-03-report`, p.9). Any further test is a deviation and is logged as one.

## 10. Noise and robustness required

- **Persistence across windows** — the two adjacent windows must agree in sign; the long change is
  the third window and is reported whatever it shows.
- **Leave-one-out** — the estimate recomputed dropping the highest-mass task, then jackknifed across
  all 1,241 tasks, with the largest single-task influence reported.
- **Flagged and fragile units excluded** — `none` and `not_classified` dropped; a near-floor
  sensitivity that drops tasks whose Claude.ai count is 15–20 in any wave, since those shares are the
  noisiest and the floor is exactly 15 in all three waves (§Thresholds).
- **Placebo** — a permutation null that pairs each task's Claude.ai change with another task's API
  change, 10,000 draws, giving the distribution of the statistic under no correspondence; and the
  within-surface benchmark of test 3 as the accounting placebo.
- **Second implementation** — the correlation recomputed as a rank correlation and as a mass-weighted
  regression, and the whole panel rebuilt independently from the parquet siblings by the analyst, with
  the two panels reconciled task by task.

## 11. Literature check

Searches run for this brief (16 September 2026): the Chatterji et al. consumer-ChatGPT paper and its
sample exclusions; Dillon, Jaffe, Immorlica and Stanton's field experiment; and a search for any study
relating enterprise-API and consumer task composition, which returned vendor and market material and
no research literature. Closest prior work: Chatterji et al., *How People Use ChatGPT* (NBER 34255,
September 2025), the largest consumer-side task description, which excludes "users on non-consumer
plans (Business f.k.a. Teams, Enterprise, Education)" and so cannot see this margin; Dillon et al.,
*Shifting Work Patterns with Generative AI* (NBER 33795 / arXiv 2504.11436, May 2025, revised
November 2025 — the short list's "(2026)" is a citation error corrected here), which finds no shift in
the composition of workers' tasks from individual AI provision, inside firms rather than across
surfaces; and Tomlinson et al. (2025), *Working with AI*, which measures occupational implications on
a single surface. Kharazian et al. (2026) on firm adoption from vendor spending is recorded in
`programme/LONGLIST.md` and was not re-verified today; it carries no task detail. Where this sits: the
cross-surface task flow is observable only from a provider's own data on one taxonomy, and no provider
has published it.

## 12. What the closing section will be able to say

**If H1 holds.** Across the tasks Claude performs on both surfaces, the work that gained share on the
enterprise API lost share on the consumer app, in both windows and outside coding as well as inside
it, and the post names the tasks that moved. The migration Anthropic has described three times in
prose is a measurable correspondence, and the size of it — with its interval, and with the
share-accounting benchmark beside it — is the first number the claim has had.

**If H1 fails (H2).** The two surfaces' task mixes moved independently: a task gaining share on the
API says nothing about its share on the consumer app, within an interval that excludes any relation
large enough to be called a flow. The migration sentence describes two series measured in the same
week rather than work passing between them, and the exposure ranking that treats API presence as a
signal of displacement risk rests on the surface a task appears on, not on its having arrived there
from somewhere else.

**If the result is null (H3, at the stated power).** The cross-surface relation is distinguishable
from neither zero nor the share-accounting benchmark at a precision where a correlation of about 0.08
would have been visible, and it is carried by the one window in which the consumer denominator moved
for every task at once. The operating rule the post leaves behind is explicit: a share falling on one
surface and rising on another is not evidence of movement between them, so a migration claim needs
levels, a common denominator, or a within-task cross-surface cut before it can be made — and until one
of those is published, the claim is a description of two series.
