# Long-list of candidate posts

Session 1.3, Step 1. Owner: programme lead. Corpus snapshot 2026-09-16; `programme/LEDGER.md` at
commit `0f5c1c6` (post-Step-0 statuses); `programme/THREADS.md` (11 threads); `data/ATLAS.md` at
Hugging Face revision `2ea58ff`.

**Purpose.** To hold every candidate research question that survives three hard gates, in enough
detail that the short-list can be scored on evidence rather than on appeal. No scores are in this
file; scoring is Step 2 (`programme/SHORTLIST.md`). The human gave no thread steer, so the spread
across threads is the team's judgement and is reported in
`room/lead-2026-09-16-longlist-status.md`.

## The three hard gates (verbatim, as set by the director)

**(1) GAP.** The question has not been answered by any Anthropic publication or by the external
literature checked. Every candidate cites the ledger item(s) it addresses, with the item ID and its
current status, which must be `open` or `partially answered` (not `answered`, `superseded`,
`settled by data (steward)`, or `unanswerable-with-public-data`). For each candidate the corpus is
re-checked and the entry states: the closest existing answer (publication, page or figure, one
sentence of what it shows) and why it falls short of the question. The external works checked are
named by author-year and title, with what each does or does not show on this question.

**(2) DATA.** The data steward confirms, in a feasibility line written into the entry (copied
verbatim from the steward's room note, with the note path), that the Economic Index releases (any
component: Claude.ai, 1P API, Claude Code, survey, labour-market and productivity files,
primitives, country/state files) contain the cut at the grain and coverage the question needs —
naming release, grain, facet or category, metric, and any supplementary source with its join key.
A candidate the steward marks NOT FEASIBLE is deleted; one marked feasible-with-caveat keeps the
caveat verbatim.

**(3) STANDALONE.** One question, answerable in one post. A why-it-matters paragraph written so
that an economist at the Anthropic Institute would care (what decision, model or measurement it
informs; whose prior it moves). A one-sentence contribution stated for EACH outcome (if the
hypothesis holds; if it fails; if the result is null/underpowered) so that either outcome is a
finished post.

## Conventions in this file

- **Naming.** The question says AI; every finding, sample and measurement will say Claude
  (`/mnt/memory/standards/terminology.md`). Questions here are written in the AI register.
- **Ledger citations** are `L-…` IDs with the status they carry in `programme/LEDGER.md` at
  `0f5c1c6`. Where Step 0 re-graded an item, the entry uses the new status.
- **Atlas citations** use the atlas's own reference forms (`§Cuts 10`, `[R5 §Reproduced]`), and
  `SB1`/`SB2` are `room/steward-2026-09-16-question-batch-answers.md` and
  `…-batch-2-answers.md`.
- **External literature provenance.** `[full]` = the document was fetched and read in this session;
  `[abs]` = the publisher's abstract, summary or results page was read. Quotations are taken only
  from text actually read. The full digest is in the batch note; nothing is quoted second-hand.
- The lead never opens data files. Every cut below is a *proposal* to the steward, stated precisely
  enough to be confirmed or refuted rather than guessed at.

## Batch log

| batch | LL IDs drafted | request note to steward | steward answer note | status |
|---|---|---|---|---|
| 1 | LL-01 … LL-14 | `room/lead-2026-09-16-longlist-feasibility-batch-1.md` | `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md` | **finalised**: 7 FEASIBLE, 7 FEASIBLE-WITH-CAVEAT, 0 NOT FEASIBLE; every caveat carried into the entry's cut and risk fields |
| 2 | LL-15 … LL-28 | `room/lead-2026-09-16-longlist-feasibility-batch-2.md` | `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md` | **finalised**: 3 FEASIBLE (LL-16, LL-18, LL-20), 11 FEASIBLE-WITH-CAVEAT, 0 NOT FEASIBLE; every caveat carried into the entry's cut, contribution and risk fields; **LL-25 deleted by the lead** as subsumed by LL-05 on the steward's pairing |
| 3 | LL-29 … LL-42 | `room/lead-2026-09-16-longlist-feasibility-batch-3.md` | pending | awaiting feasibility |

New atlas facts the steward logged for batch 1 are at `data/ATLAS.md ## Dated log 2026-09-16 (e)`
(fifteen numbered facts) and `## Supplementary sources`, "Third-party comparators fetched, joined
and licence-checked 2026-09-16 (e)" (the four external series, with their merge audits); batch 2's
are at `## Dated log 2026-09-16 (f)` (fifteen more) plus a new `## Components` paragraph recording
that three primitive levels break at the June 2026 boundary. Three batch-1 caveats changed a design
rather than confirming it: the `request` ladder has almost no cross-wave node correspondence (LL-06
moves to `onet_task`), the RPS occupation index is published at SOC minor group and not by 3-digit
prefix (LL-03 runs at N = 90), and a country's published task mix covers only about 30% of that
country's conversations (LL-06's suppression control changes). Four batch-2 caveats did the same:
LL-16's `steward?` flag is **settled** with numbers, LL-19's residual turns out to be the size of its
own measurement error, LL-26's published task-value **level does not reproduce** under any of five
wage constructions, and LL-28's June wave is off its own autonomy axis.

## Counts

| | |
|---|---|
| drafted | 41 (LL-01 … LL-42, no LL-25 in the surviving set) |
| deleted | 1 (LL-25, by the lead, as subsumed — reason in the deletions table) |
| surviving | 41: LL-01 … LL-24 and LL-26 … LL-28 confirmed by the steward (27), LL-29 … LL-42 provisional (14) |

The gate requires thirty or more surviving candidates. Twenty-seven are already through both the
steward and the gap check; batch 3 is drafted so that the total clears thirty with margin even if the
steward refuses several. LL-34 and LL-42 are the two I expect to be most at risk, and each entry says
so in its own risk field.

---

## LL-01 — Do places that use AI more use it more autonomously, or is that gradient just income?

**Thread.** T2 (geography), with T3 (the collaboration facet).

**Ledger items.** `L-2025-09-R3-25` *open* (the stream's only explicit "more research is needed");
`L-2025-09-R3-37` *open* (whether the automation–AUI relationship survives income is untested);
`L-2025-09-R3-38` *open* (nor the `not_classified` share); `L-2025-09-B3-06` *open* ("We're not yet
sure why this is").

**Closest existing answer and why it falls short.** `economic-index-2025-09-report` Fig 2.11 p.27
regresses automation-share residuals on AUI residuals after adjusting for task mix and finds
β = −3.112, R² = 0.394, N = 111 — higher-adoption countries collaborate more. It falls short three
ways: the residualisation is on task mix only, though GDP per working-age capita ships in the same
file; the report offers two untested speculations (culture; early adopters) and asks for research;
and `economic-index-2026-01-report` p.35 only replicates the pattern, which Step 0 re-graded as not
an answer.

**External literature checked.** Chatterji et al. (2025) "How People Use ChatGPT" [abs] — finds
higher growth in lower-income countries and a work/non-work gradient by education, but publishes no
automation-versus-augmentation construct. Bick, Blandin, Deming, Fuchs-Schündeln & Jessen (2026)
"Mind the Gap" [abs] — measures adoption *rates* across the US and six European countries, not how
delegated the use is. arXiv 2605.30685 "How Early Adopters Used Generative AI Worldwide" [abs] —
income gradients in *purpose* (schooling down, leisure up), not in delegation. Misra et al. (2025)
"Measuring AI Diffusion" [abs] — a population-normalised adoption level, no interaction measure.
None conditions a delegation measure on income.

**Why it matters.** The automation share is the input Anthropic's own scenario model turns into the
labour share (ψ in `econ-scenarios-paper-2026-09` Eq. 11), and the policy stream reads rising
delegation as the reason to prepare. If the delegation gradient across places is an income gradient,
then projecting today's rich-country automation share onto a diffusing world overstates it, and the
Institute's `ED-1` question about value capture has a first answer. It moves the prior of anyone who
reads Figure 2.11 as a cultural fact.

**Contribution.** *If it holds* (the AUI coefficient survives income): the corpus's one open "more
research is needed" gets its first test, and adoption — not culture or income — is the thing
associated with collaborative use. *If it fails* (income absorbs it): Anthropic's flagship
geographic interaction is an income relationship, and every cross-country delegation comparison
needs an income control. *If null/underpowered*: we publish the minimum detectable slope at N = 111
and show that the published −3.112 cannot be distinguished from an income effect with one wave.

**Economic Index cut (proposed).** `release_2025_09_15`, enriched Claude.ai file
(`data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv`), `geography == country`:
`collaboration_automation_augmentation` → `automation_pct`; `usage_per_capita` and
`usage_per_capita_index` (AUI); `gdp_per_working_age_capita`; `working_age_pop`; plus
`onet_task_pct` weights and the global `onet_task::collaboration` intersection for the task-mix
adjustment; window 4–11 Aug 2025; thresholded set (200 conversations per country), N = 111.
`ATLAS §Conventions`, "Task-mix adjustment"; §Cuts, Family B geography row; §Cuts 22 for why later
waves cannot be used. Estimation sample after the steward's audit: **114** of the 115 thresholded
countries carry AUI, GDP and automation together (PSE has no GDP); the published task-mix
specification is N = 111, so both are reported.

**Supplementary data.** None needed: this is the one wave shipping AUI, population and GDP in one
file (`SB2 14`).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-01. FEASIBLE.** `release_2025_09_15` enriched Claude.ai (4–11 Aug 2025), `geography=country`:
`automation_pct` (facet `collaboration_automation_augmentation`), `usage_per_capita_index`,
`gdp_per_working_age_capita`, `working_age_pop`, plus global `onet_task::collaboration` and
`onet_task_pct` — all in one file, one wave. Of 115 thresholded countries (≥200 conversations),
**114 carry AUI, GDP and automation together**; the loss is PSE (no GDP). Published task-mix
specification is N = 111. `ATLAS §Conventions` task-mix adjustment; log (e) 12."

**Biggest risk.** Design. AUI and log GDP per capita are collinear (r = 0.869 at country level,
`economic-index-2026-01-report` Fig 3.3), so with one wave and 111 countries the two coefficients
may not be separately identified. If it bites, we will see the AUI standard error roughly double
when income enters and neither coefficient significant — which is a reportable null with an MDE, not
a failure.

**Mentor interests.** ⟨mentor⟩ T2(e): "lower income, less educated countries paradoxically showing
more complex use in some cases. The earliest adopters often have high-value, technical use cases."
(`economic-index-2026-03-report`, OQ 13, p.17.)

**Institute agenda.** `ED-1` (who adopts AI; value capture).

---

## LL-02 — Does observed AI use support the automation share Anthropic's own scenario model assumes?

**Thread.** T11 (scenarios and macro aggregation), with T3.

**Ledger items.** `L-2026-09-SCPA-24` *open* (ψ anchored to the one wave where automation exceeded
augmentation, then frozen); `L-2026-09-SCPA-21` *open* (the ψ mapping asserted);
`L-2026-09-SCPA-25` *open* (the two constructs are different objects, mapping asserted);
`L-2026-09-SCEX-25` *open* (whether the explorer and the Index agree is never asked).

**Closest existing answer and why it falls short.** `econ-scenarios-paper-2026-09` pp.27–28 sets
ψ — the share of affected tasks automated rather than augmented — at 0.50 / 0.75 / 0.90 by
assumption and glosses it: "So 0.5 describes chat use today, and 0.9 a world in which agentic use is
the norm." The Index publishes the corresponding series in every wave. No publication puts the two
numbers side by side, and ψ moves the labour share one-for-one in Eq. (11).

**External literature checked.** Acemoglu (2025) "The Simple Macroeconomics of AI" [abs] — a
task-share calibration with no usage measure. Humlum & Vestergaard (2025) [abs] — "precise null
effects … ruling out effects larger than 2%", which constrains realised effects, not the automation
share. Bick et al. (2026) "Mind the Gap" [abs] — adoption rates and time savings, no
automation/augmentation split. Chatterji et al. (2025) [abs] — "Asking" ~49% against "Doing" ~40%,
a different taxonomy on a different product, never mapped to ψ. Nobody has disciplined ψ with usage
data.

**Why it matters.** The explorer is the Institute's public instrument for what AI could do to GDP,
wages and the labour share by 2030, and it says its parameters are "something we can potentially
measure" (`econ-scenarios-paper-2026-09` p.38). One of the five is measured, monthly, by the same
company — and the measurement has never been carried to the model. This informs which scenario the
Institute treats as the central case, and it moves the prior of anyone reading the middle scenario
as neutral.

**Contribution.** *If it holds* (the observed share brackets the least disruptive preset): the
model's two more disruptive presets are 24–44 points above anything the Index has ever seen, and the
post says what would have to change for them to be reached. *If it fails* (the observed share rises
past 0.5 on a defensible base): the Index is moving toward the middle scenario and the post dates
it. *If null* (bases disagree and no comparison is defensible): the post publishes the base-choice
sensitivity table the corpus lacks and says the parameter is not currently checkable.

**Economic Index cut (proposed).** The `collaboration` facet on the **five-classified-pattern**
base, Claude.ai global, all seven published windows: `release_2025_02_10`
`automation_vs_augmentation.csv`; `release_2025_03_27` `_v1`/`_v2`; the three long waves
(`facet == collaboration`, `variable == collaboration_pct`, `geography == global`); and
`release_2026_06_26` (`geo_id == GLOBAL`, `category_name == overall`, `collaboration_*_pct` and
`collaboration_bucket_automation_pct`). Base and caveats per `ATLAS §Conventions`, "A like-for-like
automation comparison twelve months apart does exist" and the ψ sub-section. The API leg is three
waves only — Aug 2025 / Nov 2025 / Feb 2026, at 86.17 / 83.87 / 79.75 on the same base — and stops
before the June composition break.

**Supplementary data.** None. The presets come from the published explorer and paper.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-02. FEASIBLE WITH CAVEAT: the API leg is three waves, not four, and the 2025-03-27 endpoint
carries no interval.** Claude.ai global five-classified-pattern automation re-verified today across
all seven windows: 42.5538 / 43.0619 / 51.0698 / 46.7394 / 45.5456 / 48.9788 / 48.6190 (June equals
the published bucket metric to two decimals) — the right ψ comparator, since that base excludes
`none`. 1P API exists in Aug 2025 / Nov 2025 / Feb 2026 only (86.17 / 83.87 / 79.75); **do not
cross into June** (composition break, `ATLAS §Components`). No counts in 2025-03-27 or June.
Log (e) 14."

**Biggest risk.** Construct, not data. The Index's unit is a conversation and its split is a
classifier on collaboration patterns, while ψ is a share of *task instances* whose wage bill moves
to capital. If the mismatch bites, the post can bound ψ only as an analogue, and a referee will say
the comparison is not like-for-like — so the assumptions sweep must carry the steward's two cautions
verbatim and the post must offer the conversation-to-task mapping it cannot validate.

**Mentor interests.** none on the scenario papers (Massenkoff is not an author,
`econ-scenarios-paper-2026-09` p.1); the series being used is the facet he reports in three waves.

**Institute agenda.** `ED-4` (productivity growth); `ED intro ¶2`.

---

## LL-03 — Does a usage-based measure of AI exposure rank occupations the way workers' own reports do?

**Thread.** T5 (labour-market exposure), with T8 (measurement).

**Ledger items.** `L-2026-03-LMI-26` *open* (non-Claude usage absent, so the measure's level is not
interpretable); `L-2026-03-LMIA-21` *open* (every comparison is rank-based, and two measures can
rank alike yet move occupations across the quartile cut the employment analysis uses);
`L-2026-03-LMI-06` *partially answered* (judgment calls at every step; rank stability shown, levels
not).

**Closest existing answer and why it falls short.** `labor-market-impacts-2026-03-appendix` Fig 4
p.10 compares ten construction variants by Spearman correlation against the baseline (Claude.ai
usage 0.81, Eloundou β 0.70, DWA 0.71, IWA 0.66). Every variant is built from the same Claude usage
layer and the same capability input, so the exercise shows internal robustness and says nothing
about whether the measure agrees with any independent measurement of who actually uses AI.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) "What Work Does
Generative AI Do?" [full] — publishes the first nationally representative occupation-level adoption
index and reports that "some exposure predictions explain roughly half of the variation in AI
adoption across occupations and tasks", with named counter-cases (medical secretaries 16.8% actual
against 61% predicted); it compares *capability-based* exposure scores, not Anthropic's
usage-weighted measure, and criticises chat-log measures for classifying "tasks without knowing the
user's occupation". Tomlinson et al. (2025) "Working with AI" [abs] — an AI applicability score per
detailed 2018 SOC from Bing Copilot conversations, published at SOC level, and explicitly "not …
measuring the ability of AI to replace jobs". Eloundou et al. (2024) [abs] — the capability input
itself. No work compares `observed_exposure` to a survey adoption index. **Addendum** (searched
again while drafting batch 3): the file now has external users — Audoly, Guerin & Topa (2026), NY
Fed [abs], joins Anthropic's measure to Lightcast job postings, and Brynjolfsson, Chandar & Chen's
June 2026 Stanford DEL indicator note [abs] joins the Index's automation ratio to ADP employment.
Both join it to *outcomes*, neither to another measure of adoption, so the comparison proposed here
is still unmade — but the post must position itself against those users rather than treat the file
as unused.

**Why it matters.** `observed_exposure` is the measure the Institute's scenario model is calibrated
on, the measure the retraining review uses to say who is at risk, and the measure the survey work
regresses fear on. Whether it agrees with workers' own reports of what they use AI for decides how
much weight any of those three uses can bear, and it is the one check a frontier lab cannot run on
its own logs. It moves the prior of anyone treating a Claude-derived ranking as an AI-wide ranking.

**Contribution.** *If it holds* (high rank agreement): the corpus's central exposure measure is
validated against an independent instrument for the first time, and the Claude-only caveat is
bounded rather than asserted. *If it fails*: the post names the occupations where the two disagree
and shows whether the automation weighting α or the usage gate drives the disagreement. *If null*
(agreement indistinguishable from chance given the crosswalk loss): the post reports the merge audit
and the attenuation, and states what coverage a usable external check would need.

**Economic Index cut (proposed).** `labor_market_impacts/job_exposure.csv` — 756 rows,
`occ_code` (7-character 2018 SOC detailed), `title`, `observed_exposure`; no aggregates, no
geography, no date (`SB1 8`; `SB2 9`). Aggregated to SOC **minor group** (93 groups) for the survey comparison, on BLS-EP employment
weights, and kept at detailed SOC for the Microsoft comparison.

**Supplementary data.** (a) RPS occupation-level genAI adoption index, Bick–Blandin–Deming–
Schumacher (2026), ~14,000 workers over four waves Aug 2025–May 2026, published at SOC **minor and
broad group** (the minor sheet is 95 rows, median 60 respondents), downloadable from the RPS data
page as an xlsx export — join on the minor group of `occ_code`. (b)
`github.com/microsoft/working-with-ai` `ai_applicability_scores.csv`, 785 detailed 2018 SOC rows,
matching all 756 on `occ_code` — join on `occ_code`. (c) BLS Employment Projections
(`data.bls.gov/projections/occupationProj`, 831 rows) for employment weights; merge audit already
run: 756 in, 755 matched, one unmatched (`11-1031`).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-03. FEASIBLE WITH CAVEAT: the RPS occupation index is published at SOC minor/broad group, not
by 3-digit prefix, and the broad cells are thin.** `labor_market_impacts/job_exposure.csv` (756
detailed 2018-SOC rows, `observed_exposure`) aggregates to **93 SOC minor groups**, of which **90**
match the RPS minor sheet (95 rows, median 60 respondents), or 428 broad groups of which 383 match
(median **11** respondents, 73.8% under 30) — run the rank test at minor group, N = 90. Microsoft
`ai_applicability_scores.csv` (785 detailed SOC) matches **756 of 756** on `occ_code`. BLS-EP
weights: 755 of 756. `ATLAS §Supplementary sources` (e)."

**Biggest risk.** Data, and the steward's caveat re-sizes it: the rank test runs at SOC **minor
group**, N = 90 matched cells with a median of 60 RPS respondents each, not at the 756 detailed
codes. If it bites, aggregation attenuates both measures and Spearman's ρ has a confidence band
wide enough to be uninformative; the broad-group version (383 cells, median 11 respondents, 73.8%
under 30) is therefore excluded by rule rather than reported as a robustness check, and the
detailed-code comparison runs against Microsoft's score (756 of 756 matched), which is the leg that
carries the resolution.

**Mentor interests.** ⟨mentor⟩ "the Spearman (rank-rank) correlation of job exposure across many
resolutions to these questions is exceedingly high" (`labor-market-impacts-2026-03`, fn 6 p.16);
⟨mentor⟩ "An established approach may help future observers separate signal from noise" (ibid.
p.14).

**Institute agenda.** `ED-7` (AI and jobs); `Share 1` (early warning).

---

## LL-04 — Are the tasks people bring to AI the tasks workers say AI helps them do?

**Thread.** T5, with T1 and T8.

**Ledger items.** `L-2026-03-LMIA-11` *open* ("Researchers could aggregate the 18,000 task
statements to the DWA or IWA level" — handed to researchers and never done);
`L-2025-02-P1-06` *open* (the occupational classification of a conversation does not mean the user
was a professional in that field); `L-2026-06-R6-35` *open* (task-inferred occupation is never
checked against a self-report).

**Closest existing answer and why it falls short.** `labor-market-impacts-2026-03` Fig 1 p.4 shows
that tasks rated β = 1 account for 68% of observed Claude usage against 3% for β = 0 — usage is
concentrated on *theoretically feasible* tasks. That compares usage to a capability rating, not to
any measurement of what workers use AI for; and the appendix's own suggestion, to aggregate the
task statements to the DWA level where an external comparison becomes possible, is left to others.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the task-level
index is defined on O*NET **detailed work activities**, "the share of workers who perform the task
and report using AI for it", with the most-assisted tasks being "reading documents to gather
technical information (61.3%), preparing research reports (60.7%) and analyzing data to identify
trends (57.5%)"; they do not join it to any platform's task shares, and argue chat-log measures
"tend to over-classify chats into generic activities" [abs]. Tomlinson et al. (2025) [abs] —
publishes metrics at the IWA level from Copilot conversations, an alternative platform measure, not
a worker report. Nobody has put a platform task distribution and a survey task distribution on one
axis.

**Why it matters.** Every occupational number in the Index — the concentration series, effective
coverage, the wage-based task value, observed exposure — rests on mapping a conversation to an O*NET
task and then to the occupations that perform it. Anthropic states the limitation in every report
and has never bounded it. A task-level comparison with workers' own reports is the cheapest external
validation of the inference the whole programme stands on, and its result changes how much of the
Index a policymaker should read as a labour-market statement.

**Contribution.** *If it holds* (platform task shares and survey adoption line up at DWA level):
the Index's task mapping earns an external validation and the Claude-only caveat is quantified.
*If it fails*: the post names the activity families where the platform over- or under-states, which
is exactly the "over-classification into generic activities" the external literature alleges and
nobody has measured. *If null*: the post reports how much of the Index's task mass cannot be matched
to a DWA at all, which is itself a measurement fact the corpus lacks.

**Economic Index cut (proposed).** `labor_market_impacts/task_penetration.csv` — 17,998 rows over
17,992 distinct O*NET task strings, `penetration` with both gates applied (de-duplicate on `task`
first; never lower-case before the join: `ATLAS §Traps 20, 21`). Cross-checked against
`onet_task` L0 `onet_task_pct` at `global` in `release_2026_03_24` so that the usage weighting is on
a dated window as well as on the undated exposure file.

**Supplementary data.** O*NET database **27.3** text zip
(`onetcenter.org/dl_files/database/`) for the **Tasks-to-DWAs** reference table (`Tasks to
DWAs.txt`, 23,543 rows, 2,085 DWAs) — `labor_market_impacts/` matches O*NET 27.0–27.3
set-identically on all 17,992 task strings (`ATLAS §Taxonomies`), and 17,565 of them (97.6%) carry a
DWA; plus the RPS task-level adoption index (O*NET DWAs, 1,655 of 2,085 published, median 13
respondents per cell) from Bick et al. (2026), joined on DWA id.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-04. FEASIBLE WITH CAVEAT: a third of Claude's task mass never reaches a DWA, and RPS DWA cells
are thin.** The crosswalk is obtainable — O\*NET 27.3 `Tasks to DWAs.txt` (23,543 rows, 2,085
DWAs); all 17,992 `task_penetration.csv` strings match 27.3 and 17,565 (97.6%) carry a DWA. Of
Feb-2026 global `onet_task_pct` mass, **69.3%** reaches a DWA via the shipped 20.1 Task IDs, 74.5%
via the union of both text routes, and **64.4%** reaches an **RPS-covered** DWA (RPS publishes
1,655 of 2,085 DWAs, median 13 respondents per cell). Log (e) 8."

**Biggest risk.** Data, and the steward has sized it: only **64.4%** of February 2026 global task
mass reaches a DWA that the RPS publishes, and the median RPS DWA cell holds 13 respondents. If it
bites, the comparison is over a covered two-thirds of usage against survey cells too thin to rank,
and the honest post is a coverage-and-power statement plus an activity-family comparison rather than
a task-level correlation. The covered share of Claude's task mass is therefore the first number in
the post, before any agreement statistic.

**Mentor interests.** ⟨mentor⟩ "There are judgment calls involved at every step"
(`labor-market-impacts-2026-03`, fn 6 pp.15–16); the DWA/IWA aggregation is his appendix's own
proposal (`labor-market-impacts-2026-03-appendix`, p.8).

**Institute agenda.** `ED-7`; `WILD-6` (enabling research).

---

## LL-05 — Is the geography of Claude usage the geography of AI usage?

**Thread.** T2, with T8.

**Ledger items.** `L-2025-09-R3-45` *open* (the AUI's working-age denominator is a proxy the
report's own conjectures contradict); `L-2026-07-CONN-01` *open* ("the Index reflects patterns in
Claude usage rather than the labor market as a whole"); `L-2026-09-SCPA-07` *open* ("Claude is one
of several AI assistants in use at work, so the measure is a proxy for AI use generally rather than
a census of it").

**Closest existing answer and why it falls short.** `economic-index-2025-09-report` Fig 2.2 p.14
publishes the AUI for 194 countries and benchmarks it against GDP per working-age capita (Fig 2.4
p.17, β = 0.690). The only external series it is ever placed beside is income. No publication in the
corpus compares the AUI with an independent measure of AI adoption, and the caveat that Claude is
not AI is stated in three places and quantified in none.

**External literature checked.** Misra, Wang, McCullers, White & Ferres (2025) "Measuring AI
Diffusion: A Population-Normalized Metric" and the Microsoft AI Diffusion Report H2 2025 [abs] — an
"AI User Share" over the **working-age population**, the same denominator convention as the AUI,
for 147 economies (UAE 64.0%, Singapore 60.9%, US 28.3% and 24th); it reports alignment with
"existing AI indices" in the top ranks but publishes no comparison with Anthropic's index and no
decomposition of disagreement. Bick et al. (2026) "Mind the Gap" [abs] — worker-survey adoption for
the US and six European countries (43% against 32% in 2026). Chatterji et al. (2025) [abs] — growth
by country income, no per-capita index. The comparison is available and unmade.

**Why it matters.** Three spotlights, a convergence model, a policy framework and an Institute
agenda item all read the AUI as the geography of AI adoption. If Claude's geography and AI's
geography rank countries differently, every ranking claim in that chain needs the word Claude in it,
and the Institute's `ED-1` question about who can access AI has a measurable answer. If they rank
the same, the Index becomes usable as a high-frequency proxy for a quantity otherwise measured
annually by survey — which is precisely the early-warning role `Share 1` promises.

**Contribution.** *If it holds* (ranks agree): the Index is validated as a diffusion proxy and the
post states the rank correlation and the countries it does not cover. *If it fails*: the post names
the systematic gaps — coding-heavy against consumer-heavy economies — and shows whether task mix
explains them, which turns the standing caveat into a correction factor. *If null* (too few
countries with published external values): the post reports the overlap set and the power, and says
what an external check of the AUI would require.

**Economic Index cut (proposed).** (a) `release_2025_09_15` enriched, `geography == country`,
`usage_per_capita_index` (AUI), 194 rows, 115 above the 200-conversation floor; (b)
`release_2026_06_26`, `geo_level == country`, `category_name == overall`,
`metric_id == usage_per_capita_index`, April and May 2026 (121 country ids), used for **ranks,
ratios and month-to-month changes only** — absolute country levels carry a ~1% uniform error
(`ATLAS §Conventions`, AUI, June 2026). Only these two waves publish an AUI (`SB2 14`).

**Supplementary data.** Microsoft AI Diffusion country shares —
`data/AI_Diffusion_Q12026_Update.csv`, 147 economies × H1 2025 / H2 2025 / Q1 2026, cp1252 encoding
and percent strings — joined name → ISO-3 via
`release_2025_09_15/data/intermediate/iso_country_codes.csv` (252 rows), 142 of 147 matched
automatically and five by hand; overlap with the Index is 101 countries at August 2025, 105 at June
2026 and 100 in both. Bick et al. (2026) published adoption rates for the US and six European
countries as a second, survey-based comparator.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-05. FEASIBLE.** Both AUI waves confirmed: `release_2025_09_15` enriched country (194 rows, 115
thresholded) and `release_2026_06_26` `geo_level=country`, `overall`, `usage_per_capita_index` (114
April / 121 May ids; ranks and ratios only). The Microsoft series **is** machine-readable —
`data/AI_Diffusion_Q12026_Update.csv`, **147 economies × H1 2025 / H2 2025 / Q1 2026**, cp1252 not
UTF-8, percent strings; name→ISO-3 matches 142 of 147 (5 manual). Overlap: **101** countries with
the Aug-2025 thresholded set, **105** with June, **100** with both. `ATLAS §Supplementary sources`."

**Biggest risk.** Construct, now that the data risk is settled. The two measures count different
things — Claude conversations per working-age person against the share of working-age people who
used any AI product at least once — so a rank disagreement can mean market share rather than
diffusion. If it bites, high-Claude-share countries sit above the line and the post cannot tell
Anthropic's commercial footprint from a country's AI use; the pre-registration therefore states in
advance which disagreements would count as market share (English-language, coding-heavy economies)
and reports the task mix of the outliers.

**Mentor interests.** ⟨mentor⟩ T2(e): he is lead author of the report that built the state
convergence model and of the report that reported the country-Gini reversal
(`economic-index-2026-01-report` p.1; `economic-index-2026-03-report` claims 15–16).

**Institute agenda.** `ED-1`; `ED-3` (is AI a general purpose technology).

---

## LL-06 — Did AI use spread to new tasks, or to new countries?

**Thread.** T1 (adoption and diffusion).

**Ledger items.** `L-2026-03-R5-02` *open* (new signups and the Super Bowl advertisements, never
reweighted outside the coursework figure); `L-2025-09-R3-06` *open* ("This could also be due to
changes in the underlying user base"); `L-2026-01-B4-14` *open* (the coverage comparison is not
like-for-like).

**Closest existing answer and why it falls short.** `economic-index-2026-03-report` Fig 1.1 p.5
reports the top-ten-task share falling from 24% to 19% between November 2025 and February 2026 and
attributes it partly to coding migrating to the API (p.6) and partly to new users (fn 3, p.11). No
wave decomposes a share change into who arrived and what existing users did; the corpus's one worked
decomposition is of an autonomy gap between surfaces, not of the concentration series.

**External literature checked.** Chatterji et al. (2025) [abs] — decomposes ChatGPT's work-share
fall *within cohorts* and reports that it is mostly within-cohort behaviour rather than entry, the
closest external analogue and on a different product with a user panel Anthropic does not release.
Bick et al. (2026) "Mind the Gap" [abs] — attributes cross-country adoption gaps partly to "worker
demographics and firm composition", a composition argument at the adoption margin, not at the task
margin. Nobody decomposes a platform task-concentration series.

**Why it matters.** "Usage is diversifying" is the Index's headline diffusion claim and the evidence
behind the mentor's adoption-curve reading. If the fall in concentration is mostly countries
entering with different task mixes, then diversification is a statement about Anthropic's marketing
reach; if it is mostly existing places changing what they bring, it is a statement about the
technology. The distinction decides whether the Index can be read as an early-warning instrument at
all, which is what `Share 1` promises.

**Contribution.** *If it holds* (within-country change dominates): the diversification claim is
about behaviour, and the post gives the first composition-adjusted concentration series in the
corpus. *If it fails* (between-country weights dominate): the headline is partly a composition
artefact and every "usage diversified" sentence needs a reweighted counterpart. *If null*: the post
publishes the decomposition with its suppression bounds and shows how much of the change is simply
not decomposable from public files.

**Economic Index cut (proposed, amended on the steward's caveat).** `release_2026_01_15` and
`release_2026_03_24`, long schema: `facet == onet_task`, `variable == onet_task_pct` at
`geography == country` and at `global`, plus `usage_pct` at `country` for the weights. The
`request` ladder was the original proposal and is **refuted**: its cluster names do not survive the
wave (1 of 26 match at level 2, 9 of 112 at level 1), while `onet_task` names match 2,888 nodes
carrying 99.4% of the mass. Shift-share of the change in the global concentration measure into a
within-country mix component and a between-country weight component, on the balanced panel of 115
countries at or above 200 conversations in both waves.

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-06. FEASIBLE WITH CAVEAT: substitute the `onet_task` facet for `request`, and a country's
published mix covers only ~30% of its conversations.** The `request` names do not survive the wave —
**1 of 26** match at level 2, 9 of 112 at level 1 (Nov 2025 → Feb 2026) — so no request-mix
decomposition exists; `onet_task` names match 2,888 (99.4% of mass) and answer the same question.
Balanced panel **115 countries** ≥200 in both waves. The published `pct` sum is no suppression
control (exactly 100 per country); use the `none`/`not_classified` share, median **65.9% / 71.0%**.
Log (e) 1–2."

**Biggest risk.** Design, and the steward's caveat sharpens it: a country's *named*-task mix covers
only about 30% of its conversations, with the `none`/`not_classified` share at a median of 65.9%
(Nov 2025) and 71.0% (Feb 2026), and that residual itself moves between waves. If it bites, the
within-country component is a statement about what got classified rather than about what people
did; the pre-registration therefore uses the residual share as the suppression control in place of
the `pct` sum, and reports the decomposition on both the named base and the all-conversation base.

**Mentor interests.** ⟨mentor⟩ "The pattern is consistent with a standard 'adoption curve' story,
in which early adopters favor specific high-value uses like coding, and later adopters take on a
much wider range of tasks." (`economic-index-2026-03-report`, OQ 20, p.3.)

**Institute agenda.** `ED-1`; `Share 1`.

---

## LL-07 — Is AI delegated more on cheap work or on expensive work?

**Thread.** T3 (automation versus augmentation), with T4.

**Ledger items.** `L-2025-02-R1-16` *partially answered* (occupation and category delivered; "the
wage cross is published nowhere"); `L-2025-02-P1-22` *partially answered* (automation share by wage
or Job Zone was one join away and is never shown); `L-2026-09-SCPA-27` *open* (whether the exposure
anchor is employment- or wage-bill-weighted is not stated).

**Closest existing answer and why it falls short.** `economic-index-2026-03-report` Fig 1.4 p.8
prices the task mix by the US wage of the occupation that performs each task ($49.3 → $47.9) and
Fig 2.2 p.14 sorts *model choice* by that wage; `economic-index-2026-06-report` Fig 2.3 sorts
*tokens* by it. The collaboration facet is never crossed with wage in any wave, so the corpus prices
the work and prices the compute but never prices the delegation.

**External literature checked.** Chatterji et al. (2025) [abs] — "Doing" is higher among work
messages and work usage is concentrated in "highly-paid professional occupations", but the
Asking/Doing split is never regressed on a wage. Tomlinson et al. (2025) [abs] — reports how wage
and education correlate with an AI *applicability* score, and separately predicts which occupations
"delegate" versus "assist", but on Copilot conversations and without a wage gradient in the
delegation measure itself. Acemoglu (2025) [abs] — the theory that the wage bill of automated tasks
is what moves the labour share, with no usage measurement. The gradient is unmeasured everywhere.

**Why it matters.** Whether delegation rises or falls with the price of the work is the sign of the
first-order labour-share effect in Anthropic's own scenario framework: automation of expensive tasks
moves a large wage bill, automation of cheap tasks moves a small one. The corpus asserts the value
of the work is rising in compute and falling in task mix, and never says whether the expensive work
is the delegated work. It moves the prior of anyone who reads "automation share" as if all tasks
were the same size.

**Contribution.** *If it holds* (delegation rises with wage): the automation share understates the
wage bill at stake, and the post supplies the wage-weighted automation share the scenario model
needs. *If it fails* (delegation falls with wage): high-wage work is the collaborative work, which
is the observable version of the mentor's labour-augmenting reading and cuts against the simple
displacement story. *If null*: the post publishes the first wage-by-collaboration table in the
corpus with its MDE, and states what the 2025-09-15 intersection can and cannot resolve.

**Economic Index cut (proposed).** `onet_task::collaboration` at `geography == global` — the
task × collaboration intersection — in `release_2025_09_15`, `release_2026_01_15` and
`release_2026_03_24` (intersections are global only: `ATLAS §Cuts 10`), with per-task weights from
`onet_task_pct` at global in the same wave; automation share per task on the five-classified-pattern
base; three waves so the gradient can be shown to persist rather than asserted from one.

**Supplementary data.** Task → O*NET-SOC via
`release_2025_09_15/data/intermediate/onet_task_statements.csv` (O*NET DB 20.1, 19,530 rows; join on
the lower-cased, stripped task text — clean 3,168/3,168 for the Nov 2025 wave per
`ATLAS §Taxonomies`); occupation wage from `release_2025_02_10/wage_data.csv` (`SOCcode`, 1,090
occupations, with the `MedianSalary > 100` filter the released notebook applies, `ATLAS §Traps 10`)
and cross-checked against the BLS Employment Projections median annual wage column.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-07. FEASIBLE.** `onet_task::collaboration` exists at `geography=global` in all three long
waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259 tasks, with global `onet_task_pct`
weights in the same wave. Wage coverage is near-total, not marginal: through the shipped O\*NET 20.1
statements to `wage_data.csv` after `MedianSalary > 100` (1,084 of 1,090 rows), **99.4% / 99.0% /
99.3%** of *named*-task usage mass carries a wage. State the multi-holder rule (a task's wage is an
aggregate over the occupations holding it). Log (e) 7."

**Biggest risk.** Design, not data: the steward's audit moves the risk. Wage coverage is 99.0–99.4%
of named-task mass, so the binding problem is the **multi-holder rule** — a task performed by
several occupations has no single wage, and the aggregation choice (unweighted mean over holders,
employment-weighted mean, or the modal holder) is a judgement that can move the gradient's sign for
tasks held across the wage distribution. If it bites, the three aggregation rules disagree; the
pre-registration fixes one, reports all three, and reports the share of usage mass on tasks with
more than one holder.

**Mentor interests.** ⟨mentor⟩ task value as "the average hourly wage of US workers who perform
that task" (`economic-index-2026-03-report`, p.8, fn 5 p.11); ⟨mentor⟩ "more compute is associated
with more valuable artifacts" (`economic-index-2026-06-report`, pp.2–3).

**Institute agenda.** `ED-7`; the EPF's measurement ask (`economic-policy-framework-2026-06`, PDF
p.5).

---

## LL-08 — Is AI used most for the work it speeds up most?

**Thread.** T4 (primitives and productivity).

**Ledger items.** `L-2026-01-R4-49` *open* (speedup is never split by use case);
`L-2025-11-PROD-26` *open* (tasks unobserved in the sample are assigned zero gain and the
consequence is never bounded); `L-2025-11-PROD-27` *open* (no comparison with the Index's own
facets).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` pp.38–39
Fig 4.1 shows estimated speedups rising with the education required to write the prompt (9× at 12
years, 12× at 16), and pp.44–45 Fig 4.4 ranks occupations by effective coverage. Neither relates the
estimated time saving on a task to how much that task is actually used — the elasticity that decides
whether the aggregate 1.8pp is a weighted average of large gains or of small ones.

**External literature checked.** METR (2025) "Measuring the Impact of Early-2025 AI on Experienced
Open-Source Developer Productivity" [abs] — a randomised 19% *slowdown* against a forecast 24%
speedup, i.e. direct evidence that estimated and realised speedups diverge in exactly the direction
that matters here, on one task family. Humlum & Vestergaard (2025) [abs] — average time savings
~3%, an order of magnitude below Claude's estimates. Bick et al. (2026) "Mind the Gap" [abs] —
aggregate time savings 2.3% of hours in the US. Nobody has asked whether usage is concentrated where
the estimated saving is largest.

**Why it matters.** The productivity chain runs from a per-task time saving to a Hulten aggregate,
and the 0.02% usage threshold that selects which tasks enter moves the headline from 1.8pp to
"roughly 5 percentage points" (fn 6, pp.52–53). If usage is uncorrelated with the estimated saving,
the aggregate is dominated by the weighting rule rather than by the technology, and the Institute's
`ED-4` question needs a different instrument. It moves the prior of anyone quoting 1.8pp without
quoting the threshold.

**Contribution.** *If it holds* (usage concentrates where savings are largest): the aggregate is
robust to the threshold in the direction that matters, and the post says by how much. *If it fails*:
the corpus's productivity number is a weighting artefact and the post shows the threshold's
elasticity. *If null*: the post reports the MDE on the elasticity and shows that the estimator
cannot separate a real gradient from Claude's own compression bias.

**Economic Index cut (proposed).** `release_2026_01_15` and `release_2026_03_24`,
`geography == global`: the numeric intersections `onet_task::human_only_time` and
`onet_task::human_with_ai_time` (eight statistics each) against `onet_task_pct` at global in the
same wave; the implied speedup per task computed with the wave's own units — Jan 2026 mixes hours
(`human_only_time`) and minutes (`human_with_ai_time`), March 2026 has both in hours
(`ATLAS §Traps 8`). Placebo: the same regression with `onet_task::human_education_years`.

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-08. FEASIBLE WITH CAVEAT: nine variables, not eight, and the units differ by wave.** Both
`onet_task::human_only_time` and `onet_task::human_with_ai_time` exist at `geography=global` in
2026-01-15 and 2026-03-24 over 3,169 / 3,259 tasks, each with `_count` plus the eight statistics
(mean, its two CIs, median, its two CIs, `_pct`, `_stdev`) — so the placebo
`onet_task::human_education_years` is there too. Units per `ATLAS §Traps 8`: Jan hours vs minutes,
March both hours. Median CIs do not bracket the median (`Traps 11`). Log (e) 5."

**Biggest risk.** Design. Both variables are produced by the same estimator reading the same
transcripts, and users bring tasks they expect to work, so a positive elasticity is consistent with
selection and with estimator artefacts as much as with economics. If it bites, the placebo
(`onet_task::human_education_years`, confirmed present) moves with the outcome too; the post
pre-registers that reading and states it as a property of the measure rather than of the economy.
The nine-variable set gives `_count` per task, so every cell can be sized and the median CIs are
excluded from any error bar by rule (`ATLAS §Traps 11`).

**Mentor interests.** ⟨mentor⟩ T4(e): he is lead author of the report that built the success
adjustment and effective coverage (`economic-index-2026-01-report`, p.1, ch.4).

**Institute agenda.** `ED-4`.

---

## LL-09 — Does AI's measured success rate predict which work people keep bringing to it?

**Thread.** T4, with T8.

**Ledger items.** `L-2026-01-R4-25` *open* ("the strongest validation will come from the primitives'
ability to capture meaningful variation in labor market outcomes"); `L-2026-01-R4-37` *open* (task
success has no reported validation statistic and carries three headline results);
`L-2026-03-R5-29` *open* (a model judging its own success could produce the tenure result with no
learning).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` p.24 states the
validation criterion and no publication in the corpus runs it: task success is reported as a level
(global `yes` 69.9% in February 2026), used inside the productivity revision and effective coverage,
and never tested against anything observable. The nearest thing to a predictive check is the
tenure–success association of `economic-index-2026-03-report` Fig 2.4, which is a cross-section.

**External literature checked.** Tomlinson et al. (2025) [abs] — validates an LLM completion
measure against real user thumbs feedback and reports that "Scope in particular is highly correlated
with (log) share of user activity (r = 0.64)", i.e. the same test on a different platform's data,
and the closest external precedent for what this candidate proposes. Bick, Blandin, Deming &
Schumacher (2026) [full] — finds exposure explains "roughly half" of adoption variation and that
who the worker is matters more, which is the rival explanation to task quality. METR (2025) [abs] —
measured outcomes diverging from believed ones. No Anthropic-data version of the test exists.

**Why it matters.** Task success is the most load-bearing and least validated primitive in the
corpus: it halves the published productivity number, reorders effective coverage, and carries the
learning-curve result. Anthropic itself named prediction as the validation that counts. A test of
whether success at *t* predicts task growth to *t+1* is the only version of that validation the
public data supports, and its result decides how much of chapter 4 of the fourth report survives.

**Contribution.** *If it holds* (success predicts growth): the primitive earns its first predictive
validation and the post supplies the elasticity. *If it fails*: a measure Claude computes about its
own work does not predict what users do next, and three published results inherit that. *If null*:
the post reports the MDE over the matched task set and identifies how many waves would be needed —
a direct input to the Institute's cadence promise.

**Economic Index cut (proposed).** `onet_task::task_success` at `geography == global` in
`release_2026_01_15` (13–20 Nov 2025) and `release_2026_03_24` (5–12 Feb 2026) — task success is a
published binary facet at all three geographies and both global intersections exist (`SB2 12`) —
against the change in `onet_task_pct` at global between the same two waves; tasks matched by
lower-cased task text with the unmatched count reported (`ATLAS §Traps`, "Never diff cluster sets
across waves without an explicit name match"). Placebo: `onet_task::human_education_years`.

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-09. FEASIBLE.** `onet_task::task_success` at `geography=global` (`_count`, `_pct`; `yes`/`no`)
in both waves. Matching lower-cased task text: **2,886** named tasks common to Nov 2025 and Feb
2026; **2,427** carry a Nov-2025 success rate and so enter the regression (91.95% of Nov named
mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only, 372 Feb-only** — report both. Log (e) 13."

**Biggest risk.** Design. Task shares mean-revert and both waves' shares are measured with error, so
a regression of share growth on the initial level inherits a negative bias; and 282 Nov-only and 372
Feb-only tasks mean entry and exit are themselves outcomes the regression conditions away. If it
bites, the coefficient is negative for mechanical reasons; the pre-registration specifies a
split-sample instrument for the initial level, reports the estimate on the 2,427-task regression
sample and its 91.95% mass share, and reports the entry/exit margin separately rather than dropping
it.

**Mentor interests.** ⟨mentor⟩ interest 3, stating the design's power and publishing nulls:
"differential increases in unemployment on the order of 1 percentage point would be detectable"
(`labor-market-impacts-2026-03`, p.12).

**Institute agenda.** `ED-4`; `Share 1`.

---

## LL-10 — How fast is AI use actually converging across US states, and how wide is the band?

**Thread.** T2.

**Ledger items.** `L-2026-01-R4-04` and `L-2026-01-R4-06` *partially answered* (the estimate was
superseded; the precision limitation was not); `L-2026-01-R4-43` *open* (whether the result survives
dropping DC is not reported); `L-2026-01-R4-41` *open* (no first-stage F, no standard errors for any
convergence estimate).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` pp.15–17
estimates β̂ ≈ 0.77 and concludes usage "would be equalized across the country in 2-5 years";
`economic-index-2026-03-report` claim 15 p.10 revises the horizon to 5–9 years, and fn 7 p.11 says
the range "is given to reflect the different estimates from running the model in our previous report
with (5 years) or without (9 years) weights" — the spread between two specifications, not an
interval. No standard error, bootstrap or confidence band has ever been published for either
horizon, and the state AUI now exists for four windows rather than three.

**External literature checked.** Misra et al. (2025) [abs] and the Microsoft AI Diffusion Report
[abs] — publish country and regional adoption levels over time but estimate no convergence model.
Bick et al. (2026) "Mind the Gap" [abs] — documents cross-country gaps and notes "early adoption
leaders tending to pull further ahead of early laggards", the opposite sign to Anthropic's state
result, with no within-country estimate. OECD (2025) "Emerging divides in the transition to
artificial intelligence" [abs] — "Gaps in AI adoption rates have widened across places, sectors and
firms". No external work estimates a within-US-state AI convergence rate.

**Why it matters.** "Ten times faster than previous economically consequential technologies" is the
most quotable diffusion claim the Index has produced, it has already been revised once, and it has
never carried an interval. Whether the data can distinguish two years from twenty decides whether
the Institute can use the Index for `Share 1`'s early-warning function and whether the policy
framework's regional reasoning has a basis. It moves the prior of anyone quoting a convergence
horizon as a measurement.

**Contribution.** *If it holds* (the band excludes no-convergence): convergence is real and the post
publishes the first interval and the first leave-one-out for it. *If it fails* (the band includes
no-convergence): a headline finding is not distinguishable from noise on four windows, stated with
the specification that produced each end of the published range. *If null*: the same, plus the
number of waves the design would need — a concrete answer to the cadence promise.

**Economic Index cut (proposed).** State-level AUI at four windows: `release_2025_09_15` enriched
`state_us` (published AUI, thresholded at 100 conversations); `release_2026_01_15` and
`release_2026_03_24` `country-state` filtered on the `US-` prefix (54 units, of which 51 match
population), AUI rebuilt because those waves ship none (`ATLAS §Cuts 22`); and `release_2026_06_26`
`subregion` `usage_per_capita_index` (51 states + DC, never `US-PR`, `ATLAS §Cuts 4`). Conventions:
state AUI excludes `not_classified` from both numerator and denominator
(`[R4 §Reproduced, V25]`); Gini unweighted over the 51 values; Wyoming and Utah handled by a stated
rule and shown separately (`ATLAS §Traps 13, 15`).

**Supplementary data.** `release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv`
(Census SC-EST2024, ages 15–64, `SEX == 0`, 51 rows) as the denominator for the three waves that
ship no AUI.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-10. FEASIBLE WITH CAVEAT: the fourth window is two calendar months with no weights.** Four
windows confirmed: 51 published `state_us` AUI rows (Aug 2025, 51 of 52 usage rows ≥100); 51 `US-*`
units in Nov 2025, all ≥100; **54** in Feb 2026 of which 52 ≥100 (extras GU/PR/VI); 51 `US-*`
subregion AUI ids in **each** June month, never `US-PR`. The June index sits on the same axis for
states (the symmetric rebuild reproduces all 51 to mean |error| 0.0045, `[R6 §Reproduced]`), but
June has no counts, so that endpoint is the unweighted mean of April and May. Log (e) 11."

**Biggest risk.** Design. Four windows over ten months, 51 units, Wyoming and Utah flagged by
Anthropic in one wave and not another, and a fourth endpoint that is an unweighted mean of two
calendar months because the June wave publishes no counts to weight them with. If it bites, the
bootstrap band spans "no convergence" to "two years" — which the post reports as the finding rather
than hiding, since either end is informative about a published claim that has never carried an
interval. The June endpoint is reported both included and excluded.

**Mentor interests.** ⟨mentor⟩ T2(e): lead author of the report that built the state convergence
model and of the one that revised its horizon (`economic-index-2026-01-report` p.1;
`economic-index-2026-03-report` claim 15).

**Institute agenda.** `ED-1`; `Share 1`.

---

## LL-11 — Do the tasks that grow on the enterprise API shrink on the consumer surface?

**Thread.** T3, with T1.

**Ledger items.** `L-2026-03-R5-17` *open* (the migration is asserted, never measured as a
migration); `L-2026-03-R5-18` *open* ("we expect that this migration … may signal more imminent
transformation of work"); `L-2026-01-R4-23` *open* (the promised API analysis of which tasks enter
production workflows).

**Closest existing answer and why it falls short.** `economic-index-2026-03-report` p.7 states that
"Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in
our first-party API traffic" and p.6 gives the mechanism (Claude Code splitting work into smaller
API calls). Both are statements about two independently moving share series; no publication reports a
task-level correspondence between the two surfaces, and the ledger records the migration as never
measured.

**External literature checked.** Chatterji et al. (2025) [abs] — consumer ChatGPT only, and
explicitly excludes business, enterprise and education plans, so it cannot see the consumer-to-API
margin. Tomlinson et al. (2025) [abs] — one surface. Dillon, Jaffe, Immorlica & Stanton (2026)
"Shifting Work Patterns with Generative AI" [abs] — within-firm work-pattern shifts, not a
cross-surface task flow. Kharazian et al. (2026) [abs] — firm adoption from vendor spending, no task
detail. The cross-surface task flow is measurable only from a provider's own data, and no provider
has published it.

**Why it matters.** This is the mentor's stated leading indicator for labour-market change: tasks
moving to the surface where a human is not in the loop. The policy stream rests on it, and it has
never been tested. Whether the two surfaces' task series are negatively related at task level
decides whether "migration" is a real flow or two independent growth stories — and therefore whether
the Index has a leading indicator at all.

**Contribution.** *If it holds* (task-level shares move in opposite directions across surfaces): the
corpus's central leading-indicator conjecture has its first evidence, and the post publishes the
migration measure. *If it fails*: the two surfaces are growing independently, the mechanism claim
needs restating, and the policy framing built on it loses its empirical anchor. *If null*: the post
reports the correlation with its interval and shows that three waves of two global cross-sections
cannot separate migration from independent growth.

**Economic Index cut (proposed).** `onet_task` L0 `onet_task_pct` at `geography == global` for
**both** the Claude.ai and the 1P API file in `release_2025_09_15` (4–11 Aug 2025),
`release_2026_01_15` (13–20 Nov 2025) and `release_2026_03_24` (5–12 Feb 2026) — three windows, all
before the composition break. **The series must not cross the 2026-03-24 → 2026-06-26 boundary**: the
API `directive` share jumps 58.22 → 80.88 at exactly the boundary where the documentation stops
including Claude Code (`SB2 15`; `ATLAS §Components`). Shares only: 2026-03-24 counts are on a
1,000,000 sample base (`ATLAS §Other bases`).

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both surfaces in all three pre-June waves:
named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251 / 2,297 (API); pairwise overlap
1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**, carrying **80.9%** of Claude.ai and
**83.2%** of API Feb-2026 named mass. Shares only, and never past 2026-03-24, as your entry says.
Log (e) 10."

**Biggest risk.** Design. Both surfaces publish shares, not levels, so a task's share can fall on
one and rise on the other with no conversation moving; and the report's own mechanism — one coding
job becoming many API tasks — mechanically dilutes API shares. If it bites, the negative correlation
appears for accounting reasons; the pre-registration therefore states the identity, restricts to the
**1,241** tasks present in all six frames (80.9% of Claude.ai and 83.2% of API named mass in
February 2026), and reports the same test on non-coding tasks as a control.

**Mentor interests.** ⟨mentor⟩ "As tasks migrate to the API, they may become more exposed to
automation. API workflows are far more likely to be directive, with less need for a human in the
loop." (`economic-index-2026-03-report`, OQ 17, p.9.)

**Institute agenda.** `ED-7`; `Share 1`.

---

## LL-12 — Is AI use getting broader, or is the same work simply recurring?

**Thread.** T1.

**Ledger items.** `L-2025-02-P1-17` *partially answered* (the branching hypothesis: occupations
evolve if the pattern persists, transition if breadth grows without saturation);
`L-2026-03-R5A-06` *open* (the cumulative construction cannot fall, so flattening is consistent with
saturation or with a smaller pull); `L-2025-02-P1-10` *partially answered* (fewer than 20% of the
~20k O*NET tasks are recovered).

**Closest existing answer and why it falls short.** `economic-index-2026-03-appendix` Fig A.2 p.5
plots cumulative coverage across five pulls and reads 49% / 24% / 7% at the three thresholds. Because
it is cumulative and pooled across waves, it can only rise, and the wiki records that its flattening
is equally consistent with saturation and with a smaller February sample. No within-wave version of
the curve is published anywhere, so the fork the first paper posed is scoreable and unscored.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the direct
external answer on a different instrument: "AI adoption is widespread. In more than 80% of
occupations, at least 1 in 5 workers uses AI on the job, and more than 40% of tasks have adoption
rates above 20%", and "AI adoption runs shallow almost everywhere … Fewer than 3% of tasks have
adoption rates above 50%, and none exceed 70%". Their measure is workers per task; the Index's is
conversations per task, and the two have never been placed on one axis. Eloundou et al. (2024)
[abs] — a capability ceiling, not observed breadth.

**Why it matters.** Breadth-versus-depth is the fork on which the first paper hung its two futures —
jobs evolving or jobs transitioning — and the Institute's `ED-7` restates it. The published curve
cannot answer it by construction. A within-wave curve, repeated across three comparable waves, is
the cheapest correction available and changes which of two published futures the Index's own data
supports.

**Contribution.** *If it holds* (within-wave breadth rising): breadth is growing and the post dates
the growth per wave, with the concentration series as a cross-check. *If it fails* (within-wave
breadth flat while the cumulative curve rises): the published coverage claim is an artefact of
pooling, and the post supplies the non-cumulative series. *If null*: the post reports how much of the
apparent flattening is taxonomy change rather than behaviour — a measurement result the corpus needs
before any later wave is compared.

**Economic Index cut (proposed).** `onet_task` L0 at `geography == global` in `release_2025_09_15`,
`release_2026_01_15` and `release_2026_03_24`: the count of distinct published task nodes, the task
`pct` Lorenz curve and its Gini, and the per-occupation share of tasks observed within each single
wave after an external O*NET task → SOC join. `release_2026_06_26` `onet` L0 is reported separately
and never spliced, because that wave rebuilt the classifier on O*NET 30.2
(`ATLAS §Taxonomies`; §Cuts 15a).

**Supplementary data.** `release_2025_09_15/data/intermediate/onet_task_statements.csv` (O*NET
DB 20.1, 19,530 rows, 974 O*NET-SOC codes) for the task → occupation denominator; the join is on the
lower-cased, stripped task text.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-12. FEASIBLE.** Node counts are comparable across the three long waves: the privacy floor is
exactly **15** in all three and the denominators are 964,494 / 999,875 / 1,000,000 (within 3.7%), so
2,618 / 3,170 / 3,260 published nodes are like-for-like; **2,284** appear in all three, and 3,258 of
3,260 Feb nodes join the shipped O\*NET 20.1 statements for the per-occupation denominator. Keep
`release_2026_06_26` separate (O\*NET 30.2, new classifier). Log (e) 9."

**Biggest risk.** Design rather than data, on the steward's audit: the three long waves are
like-for-like (same floor of 15, denominators within 3.7%), so a rising published node count is
interpretable — but the count is bounded by how many tasks a fixed sample of ~1M conversations can
reach, so breadth and sample size are not separable in levels. If it bites, the node count rises
with nothing but the denominator; the pre-registration therefore reads breadth off the 2,284 tasks
common to all three waves and off the Lorenz curve, which is scale-free, and reports the raw counts
beside the denominators.

**Mentor interests.** ⟨mentor⟩ T1(e), the adoption-curve reading, and ⟨mentor⟩ the task-value series
that the breadth change mechanically drives (`economic-index-2026-03-report`, claim 11, Fig 1.4
p.8).

**Institute agenda.** `ED-7` (new tasks and jobs); `ED-3`.

---

## LL-13 — Do the economic primitives predict where AI use grows next?

**Thread.** T4, with T2.

**Ledger items.** `L-2026-01-R4-25` *open* (no publication relates a primitive to an outcome);
`L-2026-01-R4-07` *open* ("the primitives themselves are not necessarily causal factors");
`L-2026-01-R4-08` *open* (state-level nulls with no MDE).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` ch.3 correlates
the five primitives and GDP with the AUI in a single cross-section and states plainly that the
primitives "are not necessarily causal factors — we don't know if income or education are truly
driving adoption, or if they're proxies". Every relationship in that chapter is contemporaneous.
Nothing in the corpus asks whether a primitive measured in one wave predicts the change in usage by
the next, which is the weakest version of the validation the same report demands.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the external
answer to the analogous question at worker level: "an important determinant of AI adoption is
learning from experience", and demographics "explain little" of the variation. Bick et al. (2026)
"Mind the Gap" [abs] — cross-country adoption gaps partly explained by "worker demographics and
firm composition" and by firm encouragement, contemporaneously. Misra et al. (2025) [abs] — levels
and changes with no predictors. No work uses platform-measured task characteristics to forecast
adoption growth.

**Why it matters.** The Index's claim to be an early-warning instrument rests on its measures
carrying information about what happens next, and the fourth report says so in terms. If country-
level primitives at November 2025 predict which countries' usage share grew by February 2026, the
Index has a forward-looking use beyond description; if they do not, `Share 1` needs a different
instrument and chapter 3 is a description of correlates. It moves the prior of anyone treating
primitive levels as adoption drivers.

**Contribution.** *If it holds*: the primitives have predictive content at a one-quarter horizon,
stated as an elasticity, and the Index gains a forward-looking use. *If it fails*: the corpus's
adoption correlates do not forecast, and the post says which of the five comes closest. *If null*:
the post publishes the MDE at 118 countries and a three-month horizon and states how many waves the
test would need — which is the cadence question in an answerable form.

**Economic Index cut (proposed).** `release_2026_01_15`, `geography == country`: the five numeric
facets (`ai_autonomy`, `human_education_years`, `ai_education_years`, `human_only_time`,
`human_with_ai_time`) plus the categorical `task_success` and `use_case`, all with their eight
statistics at country grain (`ATLAS §Cuts`, Family B primitives row); outcome = the change in
`usage_pct` at `country` between `release_2026_01_15` and `release_2026_03_24`. Thresholds: 200
conversations per country applied by us, not by the file (`ATLAS §Thresholds`); Seychelles excluded
by the report's own rule and shown separately (`ATLAS §Traps 14`).

**Supplementary data.** None required; if an income control is wanted it must come from
`release_2025_09_15/data/intermediate/gdp_2024_country.csv` (IMF WEO 2024, 174 countries) because
the 2026 waves ship no GDP file (`ATLAS §Cuts 22, 29`).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-13. FEASIBLE.** In `release_2026_01_15` at `geography=country`, all five numeric primitives
(8 statistics each) plus `task_success` and `use_case` exist for 161–173 countries; **115 carry all
seven and clear the 200 floor in both waves**, and **113** of those also carry IMF GDP from
`gdp_2024_country.csv`. Seychelles needs no rule here: `SC` has **0 rows** in `release_2026_03_24`,
so the exclusion is inert. Outcome `usage_pct` base per `ATLAS §Other bases`. Log (e) 3–4."

**Biggest risk.** Design. One three-month step, 115 countries with all seven predictors, and an
outcome (`usage_pct`) that is a share of a global total, so one large country's growth mechanically
lowers everyone else's. If it bites, every coefficient is a mirror of US and Indian growth; the
pre-registration therefore uses log usage relative to the global mean and reports the raw-share
version beside it. The Seychelles exclusion is inert here (`SC` has no rows in the second wave), so
no discretionary exclusion enters.

**Mentor interests.** ⟨mentor⟩ T4(e): he is lead author of the report that introduced the
primitives' first time comparison (`economic-index-2026-03-report`, Table 1.1 p.9).

**Institute agenda.** `ED-1`; `ED-4`.

---

## LL-14 — Have official employment forecasts started to price AI exposure?

**Thread.** T5.

**Ledger items.** `L-2026-03-LMI-05` *open* ("although the relationship is slight");
`L-2026-03-LMI-16` *open* ("Interestingly, there is no such correlation using the Eloundou et al.
measure alone" — flagged and left); `L-2026-03-LMI-12` *open* (the capability half of the measure is
three years old at publication).

**Closest existing answer and why it falls short.** `labor-market-impacts-2026-03` pp.8–9 Fig 4
reports that "For every 10 percentage point increase in coverage, the BLS's growth projection drops
by 0.6 percentage points", and that the same correlation is absent using the capability measure
alone. The check is run once, on one projections vintage the paper does not name, with no interval
and no decomposition; and the paper's own opening argues that official forecasts have "added little
predictive value beyond linear extrapolation of past trends".

**External literature checked.** Brynjolfsson, Chandar & Chen (2026) "Canaries in the Coal Mine?"
[abs] — ADP payroll through June 2026 finds no economy-wide displacement but a 19% relative
employment gap for 22–25-year-olds in exposed occupations, "operat[ing] primarily through reduced
hiring"; it measures realised employment, not forecasters' beliefs. Humlum & Vestergaard (2025)
[abs] — "precise null effects … ruling out effects larger than 2%". Bick et al. (2026) "Mind the
Gap" [abs] — "no clear evidence that recent AI adoption is associated with systematic changes in
employment". Nobody has asked whether the official forecast has begun to price exposure.

**External literature, addendum** (searched again while drafting batch 3, 2026-09-16). Two works use
`observed_exposure` itself and belong on the record here. Audoly, Guerin & Topa (2026), "Do Job
Postings Show Early Labor-Market Effects of AI?", NY Fed Liberty Street Economics [abs] — combines
"a task-level AI exposure metric developed by Anthropic that combines detailed task descriptions
from O\*NET with observed AI usage" with Lightcast postings, reports that "40 percent of workers are
in jobs with zero measured AI exposure", and finds "little indication of a distinct AI-driven
decline in labor demand". Brynjolfsson, Chandar & Chen, "AI Economic Indicators: June 2026 Update",
Stanford DEL research note [abs] — uses the Index's automation and augmentation ratios against ADP
employment and reports that "occupations with a higher automation ratio see decreases or smaller
increases in the employment index" while augmentation "does not appear correlated". Neither examines
the BLS projection gradient, so the gap holds; both mean the post must position itself against
external users of the same file rather than treating it as unused.

**Why it matters.** The exposure measure's only external validation is its correlation with the
BLS projection, and the mentor's own prior is that those projections carry little information. If a
newer vintage prices exposure more steeply, the forecasters have updated and the measure gains an
independent corroboration; if it prices it less, the one validation in the paper is fragile. Either
way, this is the cheapest live test of a published Anthropic result, and it speaks directly to
`Share 1`'s early-warning claim.

**Contribution.** *If it holds* (a steeper gradient on the newer vintage): official forecasts have
begun to price AI exposure, and the post dates it and states the slope with an interval. *If it
fails* (flatter or absent): the exposure measure's single external validation does not replicate on
a later vintage, which the post reports with the merge audit. *If null*: the post publishes the first
interval on the −0.6pp coefficient and shows that 755 occupations cannot distinguish the two
vintages.

**Economic Index cut (proposed).** `labor_market_impacts/job_exposure.csv` — 756 rows, `occ_code`
(2018 SOC detail, unique, no aggregates, no SOC 55 Military), `observed_exposure`, which **is** the
job-level R_o and not an intermediate (`SB2 9`); the only join key is `occ_code` (`SB1 8`). No
un-gating and no decomposition is attempted (`ATLAS §Cuts 15`, §Thresholds).

**Supplementary data.** BLS Employment Projections occupation table
(`data.bls.gov/projections/occupationProj`), 831 detailed-SOC rows with employment 2025 and 2035,
percent change and median annual wage; US Government work, public domain; already fetched by the
steward with the merge audit 756 in / 755 matched / 1 unmatched (`11-1031` Legislators).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`).
"**LL-14. FEASIBLE WITH CAVEAT: one vintage only, so the comparison is against a published
coefficient.** `data.bls.gov/projections/occupationProj` returns **200** today (one HTML table, 831
detailed-SOC rows, employment 2025/2035, percent change, median annual wage); merge on `occ_code`
re-run now: **756 in, 755 matched, `11-1031` Legislators unmatched**. The paper's own vintage is
**not** obtainable: `www.bls.gov` 403, `download.bls.gov` 403, `web.archive.org` 403. Log (e) 15."

**Biggest risk.** Data, and the steward has confirmed it bites: the vintage the paper used is
unobtainable from this sandbox (three separate 403s), so the post compares a **published
coefficient** against one it computes on the current vintage rather than two vintages it computed
itself. The consequence is that a difference cannot be attributed to forecaster updating rather than
to a specification difference we cannot see. The post must say that in the sentence that carries the
comparison, and its limitations section must name it as the item that withdraws the strong reading.

**Mentor interests.** ⟨mentor⟩ "The government's own occupational growth forecasts, while
directionally correct, have added little predictive value beyond linear extrapolation of past
trends" (`labor-market-impacts-2026-03`, p.3, fn 1); ⟨mentor⟩ interest 1, a displacement measure
checkable against official series.

**Institute agenda.** `ED-7`; `Share 1`.

---

## LL-15 — Is AI use broad across people or deep among a few?

**Thread.** T1, with T8.

**Ledger items.** `L-2025-03-R2-20` *open* (cluster prevalence, and the breadth-versus-depth
question that `percent_records` against `percent_users` would answer, are untouched — both columns
are released); `L-2025-09-R3-01` *open* (the unit of observation is a conversation, not a user);
`L-2025-03-R2-08` *open* (the bucketing adjustment that replaced values with bucket averages).

**Closest existing answer and why it falls short.** `economic-index-2025-02-paper` p.7 Fig 4 gives
the depth-of-use curve across occupations, and `economic-index-2026-01-report` p.43 revises it to
effective coverage — both are depth in *tasks*, not in people. The corpus states in seven
publications that its unit is a conversation and never the user (`LEDGER §Recurring` R2), and the
one released file that carries a per-user denominator alongside a per-conversation one has never
been analysed in any publication.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the direct
external statement of this distinction: adoption is "widespread but shallow", and "in those
occupations, nearly everyone uses AI, but workers use it for different parts of their jobs"; their
denominator is workers, which is exactly what the Index lacks. Chatterji et al. (2025) [abs] —
reports per-user message volumes and cohort decompositions on a user panel Anthropic does not
release. Humlum & Vestergaard (2025) [abs] — adoption rates by worker, not by conversation. Nobody
has used the one Anthropic file that publishes both denominators.

**Why it matters.** Every share in the Index is a share of conversations, so a cluster that is 2% of
traffic could be 2% of users doing a little or 0.2% of users doing a lot — and the difference is
the difference between diffusion and intensity, which is what `ED-2` asks about concentration and
what the policy framework needs to know about churn. It moves the prior of anyone who reads a
conversation share as a population share.

**Contribution** (rewritten after the steward's audit, which supplies the headline number). *If it
holds* (records and users rank clusters alike, as ρ = 0.9932 says): the corpus's most repeated
caveat — the unit is a conversation, never the user — is **bounded** for the first time, at a
user-to-record ratio inside ±9% across 630 use cases, so every conversation share in every wave can
be read as a user share to within that band. *If it fails* (the collaboration-complete subset
diverges): delegated use is the habit of a few users rather than a property of the work, which is
the intensity story the corpus says it cannot tell. *If null* (the bucketing destroys resolution):
the post documents how much resolution the privacy bucketing costs and retires an open item with a
measured bound instead of a caveat.

**Economic Index cut (proposed).** `release_2025_03_27/cluster_level_data/` — the 630 level-0
clusters (→145 L1 →30 L2) with `percent_records` **and** `percent_users`, plus the per-cluster
collaboration and thinking ratios in the same TSV. Caveats to carry: prevalence is bucketed into
100 buckets so ties are artefacts and no test assuming distinct values may be used
(`ATLAS §Traps 34`); 178 of 630 rows have suppressed collaboration/thinking cells
(`ATLAS §Thresholds`); cluster names carry no ids and match no later taxonomy (`§Cuts 31`).

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-15. FEASIBLE WITH CAVEAT: the measurable spread is ±9% and both columns are bucketed, so there
is no interval and little room for a gradient.** `release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv`
is 630 × 16: `percent_records` **and** `percent_users` on **all 630** rows, each summing to exactly
100, with 100 and 99 distinct values — the 100-bucket adjustment applies to **both** (that folder's
README says so). Spearman(records, users) = **0.9932**; the whole ratio range is **0.978–1.087**.
Collaboration ratios complete on 452 rows, thinking on 601. Log (f) 1–2."

**Biggest risk.** Data, and the steward's audit has already realised it: both columns are bucketed
into 100 buckets, the rank correlation is 0.9932 and the entire user-to-record ratio range is
0.978–1.087, so there is no gradient to estimate and no interval to put on it. The consequence is
that this candidate is now a **bounding** post rather than a decomposition, and it is the weakest
survivor in the file: the contribution triplet below is rewritten to say so, and the referee should
scrutinise it at scoring before it reaches the short-list.

**Mentor interests.** none directly; the construct bears on ⟨mentor⟩ T6(e), the claim that advanced
users behave differently, which is a statement about people measured on conversations.

**Institute agenda.** `ED-2` (how concentrated is AI usage); `ED-1`.

---

## LL-16 — Does AI's own description of what people ask for match the occupational taxonomy used to measure it?

**Thread.** T1, with T8.

**Ledger items.** `L-2025-03-R2-11` *open* ("This dataset … enables comparisons between top-down
and bottom-up approaches" — a comparison enabled and never performed); `L-2025-03-R2-12` *open*
("we leave detailed analysis of this dataset to future work"); `L-2026-03-R5A-15` *open* (request
clusters are defined in Key terms and used in none of the figures, so no mapping between the two
taxonomies is given).

**Closest existing answer and why it falls short.** `economic-index-2025-03-report` released the
630-cluster bottom-up taxonomy expressly to enable the comparison and states that it is not
performed in the report. Eighteen months and four waves later no publication in the corpus
quantifies the gap between the two ladders, and the fifth report's appendix defines request clusters
without using them. The comparison is the corpus's oldest unexecuted handoff, and the release that
enables it ships an O*NET task field inside the cluster file.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — argues chat-log
measures "tend to over-classify chats into generic activities spanning many occupations" [abs],
which is precisely the top-down taxonomy's failure mode and is asserted about, not measured with,
Anthropic's data. Tomlinson et al. (2025) [abs] — classifies to O*NET intermediate work activities
and separates a "user goal" from an "AI action", a second top-down scheme rather than a bottom-up
one. Chatterji et al. (2025) [abs] — builds its own conversation taxonomy and maps only some of it
to O*NET work activities, without publishing the correspondence. No external work measures
top-down against bottom-up on one sample.

**Why it matters.** Everything the Index says about occupations and the labour market runs through
the O*NET ladder, and the first paper's own limitation is that O*NET "cannot capture emerging
tasks". The bottom-up ladder is the only instrument in the corpus that can name work O*NET does
not, and the size of the mismatch is the size of the measurement risk in every occupational claim —
including `ED-7`, which the atlas records as structurally blocked precisely because the top-down
ladder is a closed universe.

**Contribution.** *If it holds* (the two ladders agree): the O*NET mapping is not losing much, and
the post supplies the concordance the release promised. *If it fails*: the post names the bottom-up
clusters with no good O*NET home and measures the share of usage they carry — the first
quantification of what the Index cannot see. *If null*: the post reports why the two cannot be
compared even with both files in hand, which retires an open item that has sat on the ledger since
March 2025.

**Economic Index cut (proposed).** `release_2025_03_27`: `cluster_level_data/` (630 L0 clusters,
145 L1, 30 L2, with the O*NET task field and `percent_records`) against the same folder's
`task_pct_v2.csv` (3,365 tasks) and `automation_vs_augmentation_v2.csv` (3,364 tasks × five
patterns + `filtered`) at global. `onet_task` L0 at global in `release_2025_09_15` is **dropped** on the steward's finding that the
2025-09-15 hierarchy JSON carries no O*NET field, so that leg would be an unverifiable text match.
The measured coverage gap the post starts from: 11 of 630 clusters carry no O*NET task (1.64% of
records mass), the field names 370 tasks of which 24 are real O*NET statements the released
top-down file omits, and the bottom-up ladder reaches 346 of 3,365 top-down tasks holding 49.2% of
v2 usage mass.

**Supplementary data.** `release_2025_02_10/onet_task_statements.csv` (byte-identical to the March
copy, `82e4c418…`) for the task → O*NET-SOC side of the concordance.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-16. FEASIBLE — and the `steward?` flag is settled.** The TSV's `onet_task` field is documented
(all 16 columns are, in the cluster README). Coverage gap, measured: **11 of 630** clusters carry no
O\*NET task = **1.64%** of records mass; the field names **370** tasks of which **346** are in
`task_pct_v2.csv` and the other **24 are real O\*NET statements the released top-down file omits**
(3.89% of mass); the bottom-up ladder reaches **346 of 3,365** top-down tasks holding **49.2%** of v2
usage mass. Limits: one task per cluster, no ids, and the 2025-09-15 hierarchy JSON has **no O\*NET
field**, so the later-wave leg is an unverifiable text match. Log (f) 3."

**Biggest risk.** Design, now that the flag is settled. The cluster file carries **one** O*NET task
per cluster, so the concordance is one-to-one by construction and cannot express a cluster that
spans several tasks — which is exactly the over-classification the external literature alleges. If
it bites, the 49.2% mass figure understates overlap because a cluster's second and third tasks are
invisible; the post therefore reports the gap in both directions (clusters with no task; top-down
tasks no cluster reaches) and drops the 2025-09-15 leg, which the steward has shown is an
unverifiable text match.

**Mentor interests.** none on this release; the measure bears on ⟨mentor⟩ interest 2, judgement
calls at every step of a task-based measure.

**Institute agenda.** `ED-7` (new tasks and jobs); `WILD-6`.

---

## LL-17 — Does AI spend longer thinking on the work it is handed outright?

**Thread.** T3, with T4 and T8.

**Ledger items.** `L-2025-03-R2-19` *open* (extended thinking is never crossed with collaboration
mode, though both sit in the same released cluster row); `L-2025-03-R2-10` *open* (the thinking
dataset was released as an explicit handoff and no publication analyses it);
`L-2025-03-R2-21` *open* (thinking is used as a proxy for difficulty without validation).

**Closest existing answer and why it falls short.** `economic-index-2025-03-report`'s extended-
thinking section reports occupational thinking rates of roughly 6–10% and releases a per-task
thinking-fraction file "to enable further research". `economic-index-2026-06-report` ch.2 shows
extended thinking once more, as a share by wage tercile. Neither relates thinking to how the work
was delegated, although the same release publishes per-task collaboration shares on the same task
universe.

**External literature checked.** METR (2025) [abs] — finds that with AI allowed, developers "spend
less time actively coding … and instead spend time prompting AI, waiting on/reviewing AI outputs,
and idle", i.e. machine time substituting for human time in a measured setting, which is the
mechanism this candidate tests at task level. Chatterji et al. (2025) [abs] — "Asking" against
"Doing" with user satisfaction, no compute measure. Tomlinson et al. (2025) [abs] — a scope measure
of how much of an activity AI can do, not how much computation it spends. No work relates a
reasoning-effort measure to a delegation measure.

**Why it matters.** Anthropic's own reading of compute is that it prices the work
(`economic-index-2026-06-report` pp.12–13) and that more compute means more valuable output. If
thinking rises with delegation, then automation and compute cost are the same story and the
scenario model's per-instance gain and its automation share are not independent parameters. If it
falls, delegation is what people do for easy work, which changes how the automation share should be
read in every wave.

**Contribution.** *If it holds* (thinking rises with automation): delegation and reasoning effort
move together, and the post gives the first task-level estimate of that relationship. *If it fails*:
delegated work is the cheap work, and the automation share is partly a measure of task difficulty
rather than of trust. *If null*: the post publishes the correlation with its interval and shows what
the 2025-03-27 file can and cannot support, retiring a handoff that has sat unanswered since March
2025.

**Economic Index cut (proposed).** `release_2025_03_27` at task level, joined on task text:
`task_thinking_fractions.csv` (3,365 tasks; **blanks are zero** — the published figure reproduces
to 0.02pp only with blank = 0, full task set in the denominator, usage-weighted, restricted to
occupations with `pct_occ_scaled ≥ 0.5`, `ATLAS §Conventions`) against
`automation_vs_augmentation_v2.csv` (3,364 tasks × five patterns + `filtered`, sum 99.9965) and
`task_pct_v2.csv` for weights. This is a join of two per-task marginals, **not** a conversation-level
cross, and the post must say so: `ATLAS §Cuts 9` records that no thinking × collaboration cross
exists at task level.

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-17. FEASIBLE WITH CAVEAT: two marginals, no counts, and 9.8 points of mass lost to `filtered`.**
`task_pct_v2.csv` and `task_thinking_fractions.csv` are the **same** 3,365 tasks;
`automation_vs_augmentation_by_task.csv` has 3,364, so **3,364** match across all three, carrying
**98.22** of 100 `pct`. Its pattern columns are **ratios summing to 1.0**, `filtered` median 0.30 with
**1,066** rows at 1.0; weighting by the five classified ratios leaves **90.16** of 100. Thinking
blanks 2,950 (= 0); the **415** positive tasks carry **75.1%** of usage mass. No counts → no
interval. Log (f) 4."

**Biggest risk.** Design. Joining two marginals on the same tasks cannot distinguish "the same
conversations that were directive also used thinking" from "tasks that attract directive use happen
to attract thinking", and the steward's audit adds two hard numbers: only **415** tasks have a
positive thinking fraction (75.1% of usage mass), and renormalising out `filtered` costs 9.8 points
of mass. With no counts in this release there is no interval either. If it bites, the correlation is
a between-task fact on a minority of task nodes; the post states the inferential limit in the
sentence that carries the number, weights by `pct` with `filtered` renormalised out, and reports the
415-task support before anything else.

**Mentor interests.** ⟨mentor⟩ interest 5, pricing the work: "more compute is associated with more
valuable artifacts" (`economic-index-2026-06-report`, pp.2–3).

**Institute agenda.** `ED-4`; `ED-8` (diffusion dials).

---

## LL-18 — Where is AI doing work people say they could not do alone?

**Thread.** T4.

**Ledger items.** `L-2026-01-R4-39` *open* ("human could do alone", 88% globally, is measured and
never used in an analysis — the primitive most directly about substitution);
`L-2026-02-IND-16` *open* (two readings of the same 84.6% figure sit unreconciled);
`L-2026-02-IND-06` *open* (the conjecture that Indian users are "at the frontier" never holds
composition constant).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` Fig 2.2 p.25
publishes the global level (88%) and uses the primitive once, as a control in the Figure 3.5 set;
`country-brief-india-2026-02` quotes India's 84.6% twice, in two directions, without a comparison
group. So the corpus has a substitution primitive at three geographic grains, uses it nowhere, and
has one country reading it both ways.

**External literature checked.** Humlum & Vestergaard (2025) [abs] — workers report time savings of
about 3% with quality and satisfaction varying by occupation, a self-reported complementarity
measure with no counterfactual-capability item. Bick et al. (2026) "Mind the Gap" [abs] — aggregate
time savings, not a could-not-do-alone measure. Tomlinson et al. (2025) [abs] — "scope" measures how
much of an activity AI can do, the nearest external construct, and it is a capability rating rather
than a statement about the user. Nobody publishes a geography of work the user could not have done
unaided.

**Why it matters.** Substitution and complementarity is the question the third report calls "perhaps
the most important question that we hope our data will help answer", and the corpus has a primitive
built exactly for it and never uses it. Whether the share of work people could not do alone is
higher in low-adoption or high-adoption places decides whether AI is closing a capability gap or
amplifying an existing one — the distributional question `ED-5` asks and the scenario model's
cognitive-wage result turns on.

**Contribution.** *If it holds* (the share is higher where adoption is lower): AI is doing work that
would otherwise not get done in the places that use it least intensively, which is the
capability-bypass story the survey work reports qualitatively and nobody has measured. *If it fails*:
the frontier of unaided-impossible work sits in rich, high-adoption economies, which sharpens the
convergence worry. *If null*: the post publishes the first cross-country distribution of the
primitive with its intervals and the MDE, and states that the 88% global figure hides no detectable
geography.

**Economic Index cut (proposed).** `human_only_ability` — a categorical facet at **all three**
grains (`global`, `country`, `country-state`) in `release_2026_01_15` and `release_2026_03_24`
(`ATLAS §Cuts`, Family B primitives row) — against `usage_per_capita` rebuilt for those waves and
`usage_pct`; plus the global `onet_task::human_only_ability` intersection to hold task mix constant
at global. Thresholds 200/country applied by us; `none` versus `not_classified` handled explicitly
(`ATLAS §Traps 24`).

**Supplementary data.** `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` and
`gdp_2024_country.csv` for the per-capita and income axes, since the 2026 waves ship neither
(`ATLAS §Cuts 22, 29`).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-18. FEASIBLE.** `human_only_ability` exists at `global`, `country` and `country-state` in both
2026 waves (938 / 1,082 sub-national units), plus `onet_task::human_only_ability` at global over
3,169 / 3,259 tasks. **115** countries carry the facet and clear 200 conversations in both waves. The
residual is **`not_classified` in both waves** (never `none`) at country and `country-state`, median
**10.34% / 11.11%**; global publishes `yes`/`no` only, summing to 100 (yes 87.9097 → 87.7599).
Log (f) 5."

**Biggest risk.** Construct. "Could the human have done this alone" is a classifier's judgement
about a counterfactual, made from a transcript, with no validation statistic anywhere in the corpus
(`L-2026-01-R4-01` is the standing caveat). If it bites, cross-country differences in the primitive
are differences in how the classifier reads prompts in different languages; the post reports the
task-mix-held-constant version beside the raw one, treats the level as uninterpretable, and prints
the country `not_classified` residual (median 10.34% in November, 11.11% in February) as a share
beside every rate rather than renormalising it away.

**Mentor interests.** ⟨mentor⟩ T4(e): he is lead author of the report that built the primitives
(`economic-index-2026-01-report`, p.1, ch.4) and of the first tracking of them over time
(`economic-index-2026-03-report`, Table 1.1 p.9).

**Institute agenda.** `ED-5` (sharing the gains); `ED-1`.

---

## LL-19 — Does AI bring more schooling to the work than the person asking does?

**Thread.** T4, with T6.

**Ledger items.** `L-2026-01-R4-50` *open* (the AI-education primitive is measured, correlated with
human education at r ≈ 0.93, then dropped; "the residual … is a construct the data supports and the
report does not build"); `L-2026-01-R4-35` *open* (the conjecture that educated populations are
better positioned, and that the skills to use AI well are unevenly distributed);
`L-2026-03-R5-19` *open* (the skill-biased channel, named and never tested).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` p.34 reports the
two education primitives' correlation and then uses only the human one; p.24 Fig 2.1 validates human
education against BLS attainment (N = 576, R² = 0.282). The report names a skill-biased channel and
a distributional worry, and the one construct that would separate "AI supplies expertise the user
lacks" from "expert users bring expert prompts" is measured in both 2026 waves and never built.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — finds
demographics including education "explain little" of adoption differences and that learning from
experience matters more, which is the rival explanation to a schooling-gap story. Brynjolfsson,
Chandar & Chen (2026) [abs] — the entry-level employment gap, i.e. the labour-market outcome a
schooling residual would predict. Humlum & Vestergaard (2025) [abs] — firm-led investment narrows
demographic gaps in take-up. No work measures the difference between the expertise a task needs and
the expertise its user brings.

**Why it matters.** `ED-10` asks how people become experts if AI absorbs the tasks that built
expertise, and `ED-11` asks what to study. A residual that says where AI is supplying schooling the
user does not have is the closest observable proxy for that question in the released data, and it is
one subtraction away. It moves the prior of anyone who reads the human-education primitive as a
measure of user sophistication rather than of task difficulty.

**Contribution.** *If it holds* (the residual is systematically positive and larger in
lower-education geographies): AI is supplying schooling where it is scarcest, which is the
levelling story stated and untested in the corpus. *If it fails* (the residual is flat or negative
where education is low): expert users extract expert work, which is the inequality-deepening channel
the fifth report names. *If null*: the post shows that the two primitives are too collinear
(r ≈ 0.93) to support a residual, which retires an open item and warns off a tempting construct.

**Economic Index cut (proposed).** `human_education_years` and `ai_education_years` — numeric facets
with their statistics at all three grains in `release_2026_01_15` and `release_2026_03_24`. The CI
gap is **global-only**: at country and `country-state` both facets carry all eight variables
including the mean CIs in both waves, which is what the residual needs; the missing CIs of
`ATLAS §Cuts 20` bite at global. Task mix held constant at global with
`onet_task::human_education_years` and `onet_task::ai_education_years` (3,169 / 3,259 tasks).

**Supplementary data.** None required; if an education benchmark is wanted, the report's own
comparator is BLS attainment, which ships in no release (`ATLAS §Cuts 29`) and would be an external
join.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-19. FEASIBLE WITH CAVEAT: the CI gap is global-only, and the residual is the size of its own
measurement error.** At global, Feb-2026 `ai_education_years` has 6 variables (no CIs) against
`human_education_years`' 10 — but at **country and `country-state` both carry all 8, mean CIs
included, in both waves**, as do both `onet_task::` intersections (3,169 / 3,259 tasks). Over
thresholded countries: sd 0.6933 / 0.5926 (Nov, human / ai) and 0.4715 / 0.3659 (Feb); residual
(ai − human) **0.1958 ± 0.2085** and **0.2586 ± 0.1712**, corr 0.959 / 0.947, against median
per-country mean-CI half-widths of **0.17 / 0.15 years**. Log (f) 6."

**Biggest risk.** Design, and the steward has measured it landing: the residual is 0.1958 ± 0.2085
years in November and 0.2586 ± 0.1712 in February, against median per-country mean-CI half-widths of
0.17 and 0.15 years — a construct whose cross-country dispersion is about the size of its own
measurement error, with the two inputs correlated at 0.95. If it bites, the null branch below is the
branch we report, and it is a real result: the corpus's most tempting unbuilt construct cannot be
built at country grain. The post pre-registers the reliability floor and reports the raw pair beside
the residual.

**Mentor interests.** ⟨mentor⟩ "These observed differences in success rates could deepen
inequalities in the labor market… early adopters with high-skill tasks have more successful
interactions with Claude than later, less technical adopters" (`economic-index-2026-03-report`,
OQ 21, p.20).

**Institute agenda.** `ED-10` (the professional pipeline); `ED-11`.

---

## LL-20 — Does AI work less well where it is used most?

**Thread.** T4, with T2.

**Ledger items.** `L-2026-01-R4-32` *open* (the conjecture that educated populations attempt harder
tasks and therefore see lower success, offered as the explanation of a level-dependence);
`L-2026-01-R4-08` *open* (state-level relationships not significant, with no MDE);
`L-2026-03-R5-19` *open* (success differences could deepen labour-market inequalities).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` ch.3 reports
that primitives correlate with the AUI at country level and not at state level, and pp.32–33 offer
the harder-tasks conjecture for why. Task success itself is published as a global level (69.9% in
February 2026) and as a tenure gradient (`economic-index-2026-03-report` Fig 2.4), never as a
geography. The one primitive that is an outcome rather than an input has no published map.

**External literature checked.** Tomlinson et al. (2025) [abs] — publishes completion rates by
activity validated against user thumbs feedback, but for one country ("conversations … from Bing
Copilot in the United States"). Bick, Blandin, Deming & Schumacher (2026) [full] — adoption by
occupation and task with no success measure. Humlum & Vestergaard (2025) [abs] — reports that
quality improvements vary sharply by occupation (69.8% of marketing professionals against 32.1% of
teachers), the nearest external heterogeneity result, and it is by occupation, not by place. No work
publishes a geography of AI task success.

**Why it matters.** If success falls where adoption rises, the Index's own diffusion story carries a
warning: later adopters get less from the technology, which is the mechanism behind the
self-reinforcing-advantage conjecture the fifth report names and the distributional question `ED-5`
asks. And because success carries the productivity revision, a geography of success is the first
step toward a geography of the productivity gain — which nothing in the corpus has.

**Contribution.** *If it holds* (success falls as adoption rises, holding task mix): later adopters
face a lower return, and the post supplies the gradient with its interval. *If it fails* (success
rises with adoption): the advantage of early adoption compounds in outcomes as well as in usage,
which is the sharper version of the same worry. *If null*: the post publishes the first success map
with the MDE at country grain and shows that the conjecture in chapter 3 cannot be tested on one
step.

**Economic Index cut (proposed).** `task_success` — a published binary facet (`yes`/`no`) at **all
three** geographies in `release_2026_01_15` and `release_2026_03_24` (`SB2 12`,
`ATLAS §Cuts 26b`) — against the AUI rebuilt for those waves, `usage_pct`, and
`human_education_years` at the same grain; task mix held constant at global via
`onet_task::task_success`. Balanced panel of countries above 200 conversations in both waves.

**Supplementary data.** `working_age_pop_2024_country.csv` and `gdp_2024_country.csv` from
`release_2025_09_15/data/intermediate/` for the per-capita and income axes.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-20. FEASIBLE.** `task_success` (`yes`/`no`) at `country` (168 / 170 units) and `country-state`
(886 / 1,039) in both waves, plus `onet_task::task_success` at global; **115** countries carry it and
clear 200 in both waves. Global yes 66.9060 → 69.9385. Carry the country residual: `not_classified`
is a median **26.67% / 21.43%** of a country's conversations — larger than any plausible gradient, so
it must be reported as a share, not dropped silently. Log (f) 5."

**Biggest risk.** Design, and the steward has named the binding form of it: `not_classified` is a
median 26.67% of a country's conversations in November and 21.43% in February — larger than any
gradient the post could find — so a country whose classification rate moves between waves will look
as though its success rate moved. If it bites, the gradient tracks classifiability rather than
success; the pre-registration therefore reports the residual share beside every rate, tests the
gradient on the residual itself as a placebo, and reports the raw, the composition-adjusted and the
residual-controlled versions together.

**Mentor interests.** ⟨mentor⟩ "This pushes back against a hypothesis we made last year…"
(`economic-index-2026-03-report`, OQ 14, p.19) — the same measure, at user level rather than
geography.

**Institute agenda.** `ED-1`; `ED-5`.

---

## LL-21 — Does enterprise AI use respond to price, or to what the model costs to run?

**Thread.** T4, with T3.

**Ledger items.** `L-2025-09-R3-18` *open* (the −0.29 cost elasticity is called a preliminary
exploration and never revisited); `L-2025-09-R3-42` *open* (cost is realised spend per transcript,
so the model-choice channel and the token channel are never separated — "the three indices are
released separately and could be separated"); `L-2025-09-R3-22` *open* ("What role, if any, does
cost-per-task play in shaping enterprise deployment patterns?").

**Closest existing answer and why it falls short.** `economic-index-2025-09-report` p.42 reports
"each 1% cost increase is associated with a 0.29% reduction in usage frequency" and p.41
simultaneously concludes that "cost plays an immaterial role"; the companion blog says capability
matters more than cost. The wiki records all three as published (`THREADS §Cross-thread tensions`
8). The elasticity is never re-estimated on a later wave, and the released files carry cost, prompt
tokens and completion tokens as three separate indices, which is exactly what would separate the
channels.

**External literature checked.** Cui, Demirer, Jaffe, Musolff, Peng & Salz (2026), Management
Science [abs] — three field experiments on developers, an experimental complement with no price
variation. Bick et al. (2026) "Mind the Gap" [abs] — notes that subscription prices are similar
across the countries it compares, treating price as a constant. Kharazian et al. (2026) [abs] —
firm AI adoption from vendor spending, i.e. expenditure rather than unit price. Yotzov et al.
(2026) [abs] — executives' AI spending and its perceived returns. No work decomposes usage against
unit cost and token volume separately.

**Why it matters.** `ED-8` asks whether there are dials a lab could turn to modulate diffusion
sector by sector, and price is the only dial a lab actually controls. The corpus contains a
published elasticity, a published contradiction of it, and three released series that could settle
which channel the elasticity measures. Whether enterprise usage responds to price or to
compute-intensity decides whether that dial exists.

**Contribution.** *If it holds* (usage responds to unit cost with tokens held fixed): there is a
price channel, the −0.29 is partly a demand elasticity, and the post states it for the first time
with the channels separated. *If it fails* (the relationship is all token volume): the published
−0.29 is a composition fact about which tasks are expensive, and the "immaterial role" sentence is
the right reading. *If null*: the post publishes the decomposition with its interval and shows that
global-only indices re-based to mean 1.0 cannot identify a price response.

**Economic Index cut (proposed).** The 1P API global block in `release_2025_09_15`,
`release_2026_01_15` and `release_2026_03_24`: `onet_task::cost`, `onet_task::prompt_tokens` and
`onet_task::completion_tokens` (variables `cost_index`, `prompt_tokens_index`,
`completion_tokens_index`) with `onet_task_pct` and `onet_task::collaboration` on the same tasks —
all **global only**, all **indices re-based to mean 1.0**, never levels (`ATLAS §Components`, First-
party API; §Cuts 27). Three waves, none crossing the June boundary.

**Supplementary data.** None; published list prices are not in any release and would be an external,
undated layer the post should avoid.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-21. FEASIBLE WITH CAVEAT: only the first wave ships counts, so there is nothing to weight the
later two with.** `onet_task::{cost, prompt_tokens, completion_tokens}` all exist at global in all
three pre-June waves, over **2,055 / 2,252 / 2,298** tasks; 2025-09-15 carries a `_count` companion,
**2026-01-15 and 2026-03-24 carry the `_index` alone**. Each index's mean is **exactly 1.0000 within
its own wave** (medians 0.70–0.84, maxima 5.4–30.3), so cross-wave levels are meaningless and only
within-wave dispersion is interpretable. Log (f) 7."

**Biggest risk.** Data, and the steward has sharpened it: the indices are re-based to mean exactly
1.0000 *within each wave*, and only the August 2025 wave ships a `_count` companion, so the later two
waves cannot be usage-weighted at all and no level travels across waves. If it bites, the design
collapses to three separate within-wave cross-sections and the "has the elasticity changed" question
is unanswerable; the post therefore pre-registers the within-wave decomposition of spend into token
volume and residual model mix, reports it three times, and states plainly that a trend in the
elasticity is not identified.

**Mentor interests.** ⟨mentor⟩ interest 5, pricing the work and its compute
(`economic-index-2026-06-report`, pp.12–13).

**Institute agenda.** `ED-8` (can AI diffusion be modulated); `ED-2`.

---

## LL-22 — How much of a month's local AI-use pattern is real, and how much is noise?

**Thread.** T2, with T8.

**Ledger items.** `L-2026-06-R6-29` *open* (April versus May is never compared, though the release
publishes two calendar months side by side — "the largest unexploited cut in the wave");
`L-2025-09-B3-17` *open* (multiple comparisons in the overrepresentation stories, with no cell sizes
and no null distribution); `L-2025-09-R3-41` *open* (no sampling uncertainty on any geographic
number, though Ns down to 283 are printed).

**Closest existing answer and why it falls short.** Every geographic "overrepresented use" claim in
the corpus — Brazil translation 6.4×, India UI/layout 2.4×, DC job-application help 1.84×
(`economic-index-2025-09-report` Figs 2.8–2.10), and the three country spotlights — is the largest
ratio on a large place × use grid, reported without a cell count, an interval or a null. No
publication reports how many of these survive into the next window, and the one release that ships
two consecutive months never compares them.

**External literature checked.** Misra et al. (2025) [abs] — aggregates telemetry "going back to
late 2024 in all analyses unless otherwise indicated" to "mitigate short-term fluctuations" and
restricts to countries with sufficient volume, i.e. an external team's stated noise discipline
without a published persistence rate. Brynjolfsson, Chandar & Chen (2026) [abs] — uses
high-frequency payroll data and reports event-study controls, the analogous discipline on a
different series. No work publishes a persistence floor for platform usage rankings.

**Why it matters.** This is the post that makes every other geographic post in the programme
defensible, and it is the measurement Anthropic's own early-warning promise needs: a signal is only
early if it is not noise. The team's own lessons file records that half of one month's state
outliers vanished the next month. Publishing the persistence rate of distinctiveness claims gives
the Institute a rule for how much of a single window to believe.

**Contribution.** *If it holds* (high persistence): single-window distinctiveness is informative and
the post states the recurrence rate and the floor at which it holds. *If it fails* (low
persistence): a large part of the corpus's local-colour findings are noise, and the post supplies the
threshold that separates signal from it. *If null*: the post publishes the recurrence rate under
several specifications and shows that with two months and no counts the floor cannot be pinned —
which is itself the argument for the cadence the Institute promised.

**Economic Index cut (proposed).** `release_2026_06_26`, the two calendar months (April, May 2026):
`geo_level == subregion` (652 ids, 51 US states + DC carrying the AUI) and `geo_level == country`
(121 ids), `metric_id == pct` at the top of each ladder and below it, for `onet` L2, `request` L1 and
`soc_occupation` L0. Recurrence of "top 10 nodes by log(local share ÷ parent share)" and of "top 10
by raw share", month to month, with the specification stated. The steward has now produced both
legs: per US state (51 units, benchmarked on the `USA` row) recurrence is 32.7 / 33.1 / 19.8 against
84.9 / 87.6 / 83.5 by raw share, and per country (114 units, benchmarked on `GLOBAL`) it is
**52.7 / 55.4 / 32.0** against 86.7 / 90.4 / 83.8 — so the post reports both geographies, and the
20-point gap between them is part of the finding. Admission rule: `pct` ≥ 0.5 (relative error ≤1% at
two-decimal rounding), with the 6,594 exactly-0.00 cells dropped explicitly. Total April→May unit
recurrence holds (every April unit recurs in May; 7 countries and 116 subregions are May-only,
`ATLAS §Coverage`).

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-22. FEASIBLE WITH CAVEAT: state recurrence is the harsh case; countries are ~20 points more
persistent, and a `pct` floor of 0.5 is the honest admission rule.** The atlas figures are
**per-US-state** (51 units, benchmark the `USA` country row, top 10 by log share ratio, nodes present
in both months): 32.7 / 33.1 / 19.8 against 84.9 / 87.6 / 83.5 by raw share. The same rule for
**countries** (114 units, benchmark `GLOBAL`) gives **52.7 / 55.4 / 32.0** and 86.7 / 90.4 / 83.8 —
so yes, it can be produced for countries. With two-decimal values, relative error is ≤1% only at
`pct` ≥ **0.5** (≤2% at 0.25); cells surviving ≥0.5: 52.6 / 58.2 / 28.3% (country), 67.4 / 75.9 /
44.3% (subregion). **6,594 `pct` cells are exactly 0.00** — drop them explicitly. Log (f) 8."

**Biggest risk.** Data. The June wave publishes **no count metric of any kind** (`ATLAS §Cuts 17`)
and `value` is pre-rounded to two decimals, so cells cannot be sized; the steward's audit turns that
into a rule — relative error is ≤1% only at `pct` ≥ 0.5, which admits 28–76% of cells depending on
the ladder, and 6,594 cells are exactly 0.00. If it bites, the recurrence rate cannot be converted
into a per-cell noise estimate; the post presents persistence as an observable proxy for reliability,
stated as such, reports it at both the 0.5 and 0.25 floors, and drops the exact-zero cells
explicitly rather than silently.

**Mentor interests.** ⟨mentor⟩ interest 2, robustness by rank
(`labor-market-impacts-2026-03-appendix`, Fig 4 p.10) — the same discipline applied to geography.

**Institute agenda.** `Share 1` (early warning, granularity and cadence); `ED-1`.

---

## LL-23 — Do Anthropic's own exclusion rules change what its data says about geography?

**Thread.** T2, with T8.

**Ledger items.** `L-2025-09-R3-14` *open* (Utah: "we ran robustness checks and believe that this
activity is not driving the results" — the checks are asserted, never shown);
`L-2025-09-R3-40` *open* (no excluded-Utah AUI, elasticity or directive share);
`L-2026-01-R4-18` *open* (Seychelles and Wyoming excluded from all geographic analyses, in contrast
with the Utah decision one wave earlier).

**Closest existing answer and why it falls short.** The third report flags Utah for possible
coordinated abuse and keeps it; the fourth report excludes Seychelles and Wyoming outright; neither
publishes a number with and without. The atlas shows the stakes: Utah's automation share is 73.40
against a state median of 48.16 and its task-mix residual is +25.14 where the next largest is +4.19;
Seychelles is 2.5% of the entire November global sample at an AUI of 1,054.6; and the published state
Gini of 0.32 **includes** Wyoming while the published education correlation excludes it.

**External literature checked.** Misra et al. (2025) [abs] — restricts to countries with sufficient
traffic volume and a minimum population of two million, an explicit exclusion rule published as
such, with no sensitivity analysis. Brynjolfsson, Chandar & Chen (2026) [abs] — publishes controls
and alternative samples for its main estimate. Humlum & Vestergaard (2025) [abs] — reports that
nulls "hold for intensive users, early adopters, workplaces with substantial investments", i.e. the
discipline of showing the result under every sample choice. Nobody has audited Anthropic's
geographic exclusions, because only the released files allow it.

**Why it matters.** Three spotlights, a convergence model and a policy framework rest on geographic
numbers whose sample is set by undocumented, wave-specific exclusions applied in the prose and not
in the files. An economist deciding whether to use the released geography needs to know how much the
headline moves under each rule — and the team's own standing lesson is that flagged units must be
excluded by rule, not by hand.

**Contribution.** *If it holds* (the numbers are robust): the exclusions are cosmetic, Anthropic's
assertion is vindicated with the number it never published, and future work can pool the waves.
*If it fails*: one or more published geographic findings depend on a discretionary exclusion, and the
post says which and by how much. *If null*: the post supplies the exclusion-sensitivity table the
corpus lacks and the rule the programme will use in every later geographic post.

**Economic Index cut (proposed).** Recompute the published geographic quantities with and without
each flagged unit, on the waves where each rule applies: state AUI and its Gini and the top-5/top-10
concentration shares in `release_2025_09_15` (Utah) and `release_2026_01_15` (Wyoming, Seychelles);
the country AUI, its Gini and the GDP elasticity in the same two waves; and the task-mix automation
regression (`collaboration_task_regression`) at country and state level in `release_2025_09_15`,
where Utah's residual is the outlier. Conventions and published targets per `ATLAS §Conventions`
(AUI, Gini) and `§Traps 13–15`.

**Supplementary data.** `working_age_pop_2024_*.csv` and `gdp_2024_*.csv` from
`release_2025_09_15/data/intermediate/` for the rebuilt waves.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-23. FEASIBLE WITH CAVEAT: five of the six quantities reproduce under both samples; the
concentration shares reproduce only to 0.7–0.9 pp, and no AUI or Gini has a sampling interval.** The
state AUI Gini is **0.366510** over 51 states (published 0.37) and **0.333986** without Utah; the
top-5 AUI share 29.68 → 26.77; Wyoming and Seychelles are straightforward row drops. **Seychelles'
contamination of the global mixes is measurable exactly** by count subtraction (24,715 = 2.47% of
Nov-2025 conversations): it moves the global `collaboration` mix by up to **1.17 pp**, `use_case`
`work` by 1.17 pp, `task_success` `no` by 0.45 pp. Note global mixes cannot be rebuilt *from* country
rows (they sum to 84.3%). Log (f) 9–10."

**Biggest risk.** Design. Five of the six quantities reproduce under both samples, so the exercise
runs — but no AUI, Gini or concentration share carries a sampling interval in any wave, and the
concentration shares themselves reproduce only to 0.7–0.9pp because the population denominator is
unpublished. If it bites, a movement of that size cannot be told from a rebuild artefact; the post
therefore reports exclusion effects only where they exceed the reproduction error (the Utah Gini
moves 0.366510 → 0.333986, which does), states the reproduction error beside every number, and
treats the report's own unnamed internal checks as unverifiable rather than refuted.

**Mentor interests.** ⟨mentor⟩ interest 2, judgement calls at every step and robustness shown rather
than asserted (`labor-market-impacts-2026-03`, fn 6 pp.15–16).

**Institute agenda.** `Share 1`; `WILD-6`.

---

## LL-24 — Do retraining programmes train people for the work AI is already doing?

**Thread.** T10, with T5.

**Ledger items.** `L-2026-08-WR-25` *open* (whether the trained occupations are the exposed
occupations is never asked; the sector destinations include occupations Anthropic's own exposure
work ranks as most exposed, and no exposure measure is joined);
`L-2026-08-WR-17` *open* (retraining for the highest-skilled may need a compressed mid-career
degree, handed to future research); `L-2026-07-EFRF-08` *partially answered* (Priority 2's
evaluations and pipeline experiments — reviewed, nothing run).

**Closest existing answer and why it falls short.** `worker-retraining-2026-08` is the corpus's one
systematic evidence review: sector programmes lift earnings "10 times as much", with a benefit–cost
ratio of 7.18, and the review names their destinations — IT support, medical assisting, bookkeeping,
accounting. Four pages earlier the same authors use their own exposure measure to say that
"college-educated workers—software developers, paralegals, accountants—are most at risk". The two
lists are never put side by side, and the review states plainly that there is no evidence on
retraining under AI displacement.

**External literature checked.** Brynjolfsson, Chandar & Chen (2026) [abs] — the employment gap is
concentrated in young workers in exposed occupations and "operates primarily through reduced hiring",
so where a programme places matters more than whether it trains. Humlum & Vestergaard (2025) [abs] —
"Adoption is linked to occupational switching and task restructuring", i.e. the destinations are
themselves moving. Bick et al. (2026) "Mind the Gap" [abs] — no clear employment effects to date.
Among the works read, none joins a programme-destination occupation list to an AI exposure or usage
measure.

**Why it matters.** The Economic Policy Framework lists workforce training grants as a Tier 1
instrument, the Research Fund is paying for retraining evaluations, and Anthropic's own review
doubts current programmes are adequate. If the destinations are themselves exposed, the fiscal case
in the review is being made for training into occupations the same authors rank as at risk. That is
a decision-relevant fact for the Fund's Priority 2 and for any government reading the framework.

**Contribution.** *If it holds* (destinations are more exposed than the average occupation): the
targeting problem is real and quantified, and the post gives the Fund a screening measure. *If it
fails*: retraining destinations are in the safer part of the exposure distribution and the review's
recommendation survives the check it never ran. *If null*: the post publishes the exposure
distribution of the named destinations with the merge audit and shows that four named occupations
cannot support a general claim.

**Economic Index cut (proposed).** `labor_market_impacts/job_exposure.csv` (756 detailed 2018-SOC
rows, `observed_exposure`, join key `occ_code` only) for the exposure of each destination
occupation, and `task_penetration.csv` (de-duplicated on `task`, never lower-cased first) to show
which of a destination's tasks carry positive penetration. A zero in `job_exposure.csv` means "no
measured exposure", never "no tasks used" — 52 occupations have exposure 0 while owning 1–10
positive-penetration tasks (`ATLAS §Traps 37`), and that distinction is the post's main caveat.

**Supplementary data.** The destination occupations named in `worker-retraining-2026-08` (pp.2, 9,
77) coded to 2018 SOC by hand, with the coding published; BLS Employment Projections
(`occupationProj`, 831 rows, employment 2025/2035 and median annual wage) on `occ_code` for the
growth and pay of each destination; merge audit 756 in / 755 matched.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-24. FEASIBLE WITH CAVEAT: the comparison distribution is 54% zeros.** All the named destinations
are present: Computer User Support 15-1232 **0.4685**, Computer Network Support 15-1231 0.2867,
Accountants and Auditors 13-2011 **0.3478**, Bookkeeping/Accounting/Auditing Clerks 43-3031
**0.3104**, Medical Assistants 31-9092 **0.0476**. Against them, **411 of 756** occupations have
exposure exactly 0 (median 0), so the employment-weighted benchmark is mostly zeros and the
comparison must be stated as a quantile position, not a ratio. Of the 52 zero-exposure-but-positive-
task occupations, **20 are in the health, clerical and support families** (15 `29-*`, 3 `43-*`, 2
`31-*`). Log (f) 11."

**Biggest risk.** Design, and the steward's audit changes its shape: 411 of 756 occupations have
exposure exactly 0, so the comparison distribution has a median of zero and a ratio against "the
average occupation" is meaningless. If it bites, any headline of the form "destinations are N times
more exposed" is an artefact of the zero mass; the post therefore states the result as a quantile
position of each destination in the employment-weighted distribution, and reports separately that 20
of the 52 zero-exposure-but-positive-task occupations sit in exactly the health, clerical and support
families the sector programmes place into — which is the measurement caveat that decides how the
quantile should be read.

**Mentor interests.** ⟨mentor⟩ "If current data on AI usage are any guide, college-educated
workers—software developers, paralegals, accountants—are most at risk (Massenkoff and McCrory 2026).
But this is highly uncertain." (`worker-retraining-2026-08`, p.4.) ⟨mentor⟩ "Impose a high
evidentiary standard" (ibid. p.5).

**Institute agenda.** `ED-5`; Research Fund Priority 2.

---

## LL-26 — Has AI use moved up or down the occupational wage ladder?

**Thread.** T1, with T4.

**Ledger items.** `L-2026-03-R5-27` *open* (the task-value fall is asserted to be "mostly due to"
composition with no shift-share decomposition, though task shares and task wages are both in hand);
`L-2025-02-R1-16` *partially answered* (occupation and category delivered; the wage cross published
nowhere); `L-2025-02-P1-26` *partially answered* (use-case by occupation still
published nowhere).

**Closest existing answer and why it falls short.** `economic-index-2026-03-report` claim 11 and
Fig 1.4 p.8 report that the average wage of the work done on Claude "dropped slightly from $49.3 to
$47.9" and attribute the fall mechanically to a rise in personal queries. The attribution is
asserted: no decomposition separates "the same occupations' tasks became cheaper" from "cheaper
occupations' tasks gained share", although both ingredients are released. And the same report prices
tasks with a wage vintage and deflator it does not state (`L-2026-03-R5-31` *open*).

**External literature checked.** Brynjolfsson, Chandar & Chen (2026) [abs] — employment effects
concentrated by age within exposed occupations, a distributional result on employment rather than on
the wage level of AI-performed work. Chatterji et al. (2025) [abs] — work usage "more common for
educated users in highly-paid professional occupations", a user-side wage gradient rather than a
task-side one. Tomlinson et al. (2025) [abs] — reports how wage and education correlate with
applicability, in levels and for one window. No work decomposes the change in the wage level of
AI-performed work.

**Why it matters.** The wage level of the work AI does is the corpus's only direct indicator of
whose work is being done, and it is the quantity that maps onto the scenario model's cognitive wage
bill. If the fall is composition — more cheap personal queries — it says the user base broadened; if
it is within-occupation, it says AI moved down the ladder inside the same jobs. Those have opposite
implications for `ED-7`, and Anthropic asserted the first without testing it.

**Contribution** (amended after the steward's audit, which shows the published level does not
reproduce). *If it holds* (the change is between-occupation composition): Anthropic's mechanical
reading is right, and the post supplies the decomposition it asserted, on a rebuilt series whose
level is stated as not matching the published one. *If it fails* (a within-occupation component):
AI is being used for cheaper work inside the same occupations, which is a different and more
consequential statement. *If null*: the post publishes the non-reproduction of the published task
value under five wage constructions — the first public statement that the Index's wage series cannot
be rebuilt from the files Anthropic ships — together with the shift-share on the sources that can.

**Economic Index cut (proposed).** `onet_task` L0 `onet_task_pct` at `geography == global` in
`release_2026_01_15` and `release_2026_03_24` (the two waves either side of the published fall), with
per-task wages attached through the shipped O*NET 20.1 statements to `wage_data.csv`; shift-share of
the change in the usage-weighted mean wage into a within-occupation component and a between-
occupation component, using the 2,888 task names that match across the two waves (99.4% / 99.2% of
mass, `ATLAS §Dated log (e) 1`). Reported beside the same decomposition on the `soc_occupation`
ladder where it exists — `release_2025_09_15` enriched and `release_2026_06_26` L0/L1 — as a
robustness check, never spliced (`ATLAS §Cuts 13`).

**Supplementary data.** `release_2025_09_15/data/intermediate/onet_task_statements.csv` (task → SOC)
and `release_2025_02_10/wage_data.csv` (`SOCcode`, 1,084 usable rows after the `MedianSalary > 100`
filter); BLS Employment Projections median annual wage as the second wage source, so the result can
be shown under two wage vintages.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-26. FEASIBLE WITH CAVEAT: the published level does not reproduce — compare changes, not levels.**
$49.3 → $47.9 rebuilds as **$35.08 → $34.36** (shipped O\*NET 20.1 statements → `wage_data.csv`, mean
over holder SOCs ÷ 2080, 92.6% / 92.3% of named-task mass priced) and **$37.69 → $37.55** (BLS-EP 2025
median, 54.7% / 57.8% priced); max-holder, employment-weighted and ÷1920 variants span $34–$38 and
none approaches $49. The **direction** reproduces on the 2019 scrape (−$0.72 against the published
−$1.40) and is nearly flat on EP (−$0.14). Likeliest cause: the OEWS **mean** hourly series, 403 from
here. The 2,888-name panel is confirmed. Log (f) 13."

**Biggest risk.** Data, and it is now measured: the published **level** does not reproduce under any
of five wage constructions (rebuilds span $34–$38 against a published $49.3), because Anthropic
almost certainly priced tasks on the OEWS mean hourly series, which returns 403 from this sandbox.
The house criterion is that a published number is reproduced before anything new is built on it, and
here it cannot be. If it bites — and it has — the post is explicitly a **change** decomposition with
the non-reproduction reported as its first result, the published level quoted as published and never
rebuilt, and the direction shown under both wage sources (−$0.72 on the 2019 scrape, −$0.14 on
BLS-EP, against a published −$1.40).

**Mentor interests.** ⟨mentor⟩ interest 5: task value as "the average hourly wage of US workers who
perform that task" (`economic-index-2026-03-report`, p.8, fn 5 p.11), and the published claim that
the fall is compositional (claim 11).

**Institute agenda.** `ED-7`; `ED-5`.

---

## LL-27 — Is AI delegated the same way everywhere inside one country?

**Thread.** T2, with T3.

**Ledger items.** `L-2026-03-AUS-16` *open* (no collaboration/automation split for Australia,
though the facet exists for Australian states); `L-2026-07-CAN-16` *open* (no Index facet beyond the
use-case mix for Canada or its provinces); `L-2026-01-R4-09` *open* (the country-level pattern
contradicts the state-level pattern and the level-dependence is unexplained).

**Closest existing answer and why it falls short.** The collaboration facet is published at
`country-state` grain in all three long waves, and no publication in the corpus reports it below the
country: the Australian spotlight glosses autonomy in collaboration language without computing the
split, the Canadian spotlight reports only a use-case mix, and the third report's state-level
task-mix regression flips sign against the country one (+2.73 against −3.11) with no explanation.
Sub-national delegation is the most available unused cut in the geography thread.

**External literature checked.** Misra et al. (2025) [abs] — sub-national AI user shares for US
states, counties and metros, with no interaction or delegation measure. Daepp & Counts (2025) [abs]
— a US generative-AI divide in access and adoption, not in how AI is used. Bick et al. (2026)
"Mind the Gap" [abs] — cross-country and within-Europe adoption, no sub-national delegation split.
Nobody has published a sub-national map of how delegated AI use is.

**Why it matters.** If delegation varies as much inside countries as between them, then the
cross-country delegation gradient the corpus keeps reporting is a composition fact about which
regions dominate a country's sample — and the country is the wrong unit for the whole T2 thread.
That bears directly on the fourth report's unexplained level-dependence and on whether the policy
framework's regional reasoning should be national or local.

**Contribution.** *If it holds* (within-country variance is large relative to between-country
variance): the country is the wrong unit, and the post supplies the variance decomposition that says
so. *If it fails* (within-country variance is small): country-level delegation comparisons are
sound and the post licenses them for the first time. *If null*: the post reports the decomposition
with its small-cell floor and states which countries have enough sub-national mass to support any
comparison at all.

**Economic Index cut (proposed).** `facet == collaboration`, `variable == collaboration_pct` at
`geography == country-state` and `country` in `release_2026_01_15` (1,091 units / 135 parents) and
`release_2026_03_24` (1,256 units / 155 parents); automation on the five-classified-pattern base,
with the base stated; variance decomposition of the automation share into between-country and
within-country components on units at or above the 100-conversation floor (540 of 1,091 and 680 of
1,256 are below it, `ATLAS §Thresholds`). US states are a prefix filter on `country-state`, not a
facet (`§Cuts 5`).

**Supplementary data.** None.

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-27. FEASIBLE WITH CAVEAT: the decomposition's real N is 32–36 countries, not 109–125.** Units at
or above 100 conversations: **545 of 981** (Nov, 109 parents) and **570 of 1,137** (Feb, 125 parents);
at 385, **277** (80 parents) and **295** (95 parents). Every surviving unit carries `collaboration`
rows. Surviving units hold a median **91% / 90%** of their parent's usage at the 100 floor (85% at
385, minimum 16%). Parents with ≥5 surviving units: **32 / 36**; with ≥10: **18 / 16**. Log (f) 14."

**Biggest risk.** Data, re-sized by the steward: a variance decomposition needs several units per
country, and only **32** countries in November and **36** in February have five or more sub-national
units above the 100-conversation floor (18 and 16 have ten or more). If it bites, the within-country
component is estimated on three dozen mostly rich countries and cannot be generalised; the post
therefore reports the decomposition on the ≥5-unit and ≥10-unit panels separately, states the
surviving units' share of each parent's usage (median 91% / 90%), and runs it at both the 100 and
385 floors.

**Mentor interests.** ⟨mentor⟩ T3(e): the migration of work toward the automated surface as the
mechanism for imminent change (`economic-index-2026-03-report`, OQ 17, p.9) — tested here across
places rather than surfaces.

**Institute agenda.** `ED-1`; `ED-8`.

---

## LL-28 — Does the Index's autonomy measure capture what happens when AI can act on its own?

**Thread.** T3, with T7 and T8.

**Ledger items.** `L-2026-08-IRA-21` *open* (no partner finding is connected to an Anthropic measure
of the same thing, and "nobody reconciles them in either direction");
`L-2025-04-SWE-12` *partially answered* (the promised extension of the automation/augmentation
framework for agentic tools: new primitives arrived beside the framework, the five-pattern taxonomy
is unchanged); `L-2025-04-SWE-02` *partially answered* (the boundary between automation and
augmentation blurs with agentic tools).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` p.19 defines AI
autonomy as a 1–5 primitive and insists it is a separate construct from automation, and
`economic-index-2026-06-report` pp.14–16 reports a 0.37-point autonomy gap between Claude Code and
chat, two thirds of it within-task. All of that is log-level: the Index releases no Claude Code data
at all, and the one public Anthropic file with agentic sessions carries a different construct
(`supervision_intensity`, `fully_autonomous` 42.8% of 247,315 records) that no publication relates
to the autonomy primitive.

**External literature checked.** METR (2025) [abs] — the randomised developer study whose sessions
sit behind the partner file, and whose finding (19% slowdown, with time shifted to prompting and
reviewing) is about outcomes rather than autonomy. Cui et al. (2026) [abs] — developer field
experiments with no autonomy measure. Tomlinson et al. (2025) [abs] — predicts which occupations
"delegate" against "assist" from conversations, a third construct again. The three public measures of
delegation — Anthropic's autonomy primitive, Anthropic's collaboration facet and the partner file's
supervision intensity — have never been placed on one page.

**Why it matters.** The whole policy framing of the corpus rests on delegation rising, and the
measure that framing uses was built for chat while the delegation it worries about happens on agentic
surfaces. If the Index's autonomy scale saturates exactly where agentic work begins, then the
early-warning instrument is blind to the thing it is watching for — which is what `WILD-10` asks
about human-in-the-loop oversight and what the fourth report's own construct note implies.

**Contribution.** *If it holds* (the Index's autonomy distribution reaches the agentic range): the
primitive is a usable measure of full delegation and the post shows where the scale's top sits
relative to an agentic sample. *If it fails* (it saturates below it): the corpus's delegation series
cannot see the agentic margin, which is a measurement finding with immediate consequences for the
automation/augmentation framework the April 2025 report promised to extend. *If null*: the post
publishes the two distributions side by side with the seven reasons they cannot be merged, which is
the reconciliation the access post invited and nobody has written.

**Economic Index cut (proposed, amended on the steward's caveat).** `ai_autonomy` — a numeric facet
at all three grains in `release_2026_01_15` and `release_2026_03_24` (10 variables at global, 8
below), with the **global histogram**, which is what resolves the scale's top: November publishes
five integer bins (2.962 / 16.250 / 26.329 / 48.566 / 5.892 at autonomy 5) and February 25 bins of
which only the five integer ones are non-zero (4.253 at 5). Plus the global
`onet_task::ai_autonomy` intersection. **`release_2026_06_26` is excluded from the scale axis**: its
`ai_autonomy_mean` is 2.72 / 2.74 against February's 3.407 on the same documented scale with no
announced rescaling, and the two time primitives break at the same boundary — the break is reported,
not spliced.

**Supplementary data.** `Anthropic/enabling-independent-research`, `metr` subset: 604 rows, 14
facets, 247,315 records on one April–May 2026 window, including `supervision_intensity`
(`fully_autonomous` 42.8%) and `task_success`, licensed CC BY 4.0. It carries **no** O*NET task, SOC
code, occupation or date column, so the steward's rule governs: "the two can be cited side by side,
each on its own sample, never merged" (`SB2 6`). Facet × facet two-way tables inside it *are*
recoverable (`SB2 5`).

**Steward feasibility line** (verbatim; `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`).
"**LL-28. FEASIBLE WITH CAVEAT: the Index histogram answers the scale question exactly, but the June
wave is off its own axis and must not be spliced.** `ai_autonomy` exists at all three grains in both
waves (10 variables at global, 8 below), and the histogram resolves the top: Nov publishes **five
integer bins** (2.962 / 16.250 / 26.329 / 48.566 / **5.892** at autonomy 5); Feb publishes 25 bins of
which only the five integer ones are non-zero (**4.253** at 5). But June's `ai_autonomy_mean` is
**2.72 / 2.74** (Claude.ai) and 2.27 / 2.24 (API) against Feb's 3.407, under the same documented 1–5
scale and with no announced rescaling — `human_only_time` and `human_with_ai_time` break at the same
boundary. On the framing: the side-by-side is **admissible** on my never-merge rule (`SB2 6`) — two
instruments, each on its own sample, no shared unit, window or key — provided the post's claim is
about the measure and the June break is stated. `## Components`, log (f) 15."

**Biggest risk.** Construct, and a second one the steward has just surfaced. First: the two
instruments have no common unit, sample or window, so the comparison is of distributions from
different populations and the post's claim must be about the **measure**, never about surfaces.
Second: June's `ai_autonomy_mean` is 2.72/2.74 against February's 3.407 on the same documented 1–5
scale with no announced rescaling, and two time primitives break at the same boundary — so the June
wave is off its own axis and is excluded from the scale comparison, and that break is reported as a
finding in its own right rather than smoothed over.

**Mentor interests.** ⟨mentor⟩ T3(e): "API workflows are far more likely to be directive, with less
need for a human in the loop" (`economic-index-2026-03-report`, OQ 17, p.9); ⟨mentor⟩ he is second
author of the agentic-coding paper (`claude-code-expertise-2026-06`, p.1).

**Institute agenda.** `WILD-10` (where humans are in the loop); `ED-8`.

---

## LL-29 — Do people do one thing at a time with AI, and does it change what they get?

**Thread.** T4.

**Ledger items.** `L-2026-01-R4-40` *open* (multitasking, 9%, is measured and set aside; its bearing
on the human-with-AI time estimate is not examined); `L-2026-03-R5A-14` *open* (multitasking and the
collaboration modes are both conversation-level and which task a single label refers to in a
multi-task conversation is unspecified); `L-2026-01-R4-01` *open* (the standing directional-accuracy
caveat on all five primitives).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` Fig 2.2 p.25
publishes multitasking at 9% globally and uses it in no analysis; the appendix concedes that in a
multi-task conversation it is unspecified which task the other labels describe. So the corpus has a
measure that tells it when its own unit of observation is ambiguous, and never checks what that
ambiguity does to the estimates built on the unit.

**External literature checked.** METR (2025) [abs] — the time-use decomposition of AI-assisted work
(prompting, waiting, reviewing, idle), the nearest external treatment of what a single task actually
contains. Chatterji et al. (2025) [abs] — classifies messages, not conversations, and so sidesteps
the problem by construction. Tomlinson et al. (2025) [abs] — separates "user goal" from "AI action"
within one conversation, an explicit acknowledgement that one exchange can carry more than one unit
of work. Nobody has measured how much of a usage corpus is multi-task, or what it does to the
estimates.

**Why it matters.** Every published speedup, success rate and collaboration share is a
conversation-level average, and 9% of conversations are known to contain more than one task. If the
multi-task share is concentrated in particular tasks or places, then those cells' primitives are
measuring something different from the rest, and the productivity chain inherits it. It moves the
prior of anyone treating a conversation as a task.

**Contribution.** *If it holds* (multi-task conversations differ systematically in time and
success): the corpus's unit ambiguity has a measurable footprint, and the post gives the correction
factor. *If it fails*: the 9% is spread evenly and the unit ambiguity is harmless, which licenses
every conversation-level average for the first time. *If null*: the post publishes the multi-task
share by task and geography with its MDE, which is a measurement fact the corpus has never printed.

**Economic Index cut (proposed).** `multitasking` — a categorical facet at `global`, `country` and
`country-state` in `release_2026_01_15` and `release_2026_03_24` — with the global
`onet_task::multitasking` intersection, against `onet_task::human_with_ai_time` and
`onet_task::task_success` on the same tasks at global. Residual node named explicitly
(`ATLAS §Traps 24`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Construct. Multitasking is a classifier judgement with no validation statistic,
and it may simply track conversation length, which is published nowhere (`ATLAS §Cuts 27`). If it
bites, the multi-task share is a length proxy and every correlation with it is mechanical; the post
must say so and report the relationship with the time primitives, which are the only length-adjacent
measures available.

**Mentor interests.** ⟨mentor⟩ T4(e): he is lead author of the report that built the primitives and
of the first tracking of them (`economic-index-2026-01-report` p.1; `economic-index-2026-03-report`
Table 1.1 p.9).

**Institute agenda.** `ED-4`.

---

## LL-30 — Is the work AI does for work the same work it does for study?

**Thread.** T1, with T4.

**Ledger items.** `L-2025-02-P1-26` *partially answered* (the facet was run and only two aggregate
numbers reported; a use-case × occupation distribution is still published nowhere);
`L-2026-01-R4-49` *open* (speedup is never split by use case, though 54% of Claude.ai conversations
are not work); `L-2026-03-R5-06` *open* (educational tasks may be easier, or students mindful of
usage limits — offered and untested).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` p.26 publishes
the three-way split (46% work / 19% coursework / 35% personal) and
`economic-index-2026-03-report` Fig 1.2 p.6 reports its movement (coursework 19% → 12%, personal
35% → 42%). `economic-index-2026-06-report` Fig 1.3 p.7 shows work-related conversations by
occupation **wage quartile**. A use-case × occupation or use-case × task distribution appears
nowhere, and the atlas confirms no release carries the cross below global (`ATLAS §Cuts 10, 11`) —
but the global intersection does exist, which is the one place the question can be asked.

**External literature checked.** Chatterji et al. (2025) [abs] — the direct external comparator:
non-work messages grew "from 53% to more than 70%", work usage concentrated among educated
professionals, and a published work/non-work split by topic. Bick, Blandin, Deming & Schumacher
(2026) [full] — measures work adoption only, by design, and notes 55% of US adults use AI for
non-work against 45% for work. arXiv 2605.30685 [abs] — schooling use falls and leisure use rises
with national income. Nobody publishes the occupational composition of *non-work* AI use.

**Why it matters.** Every occupational claim in the Index is built on conversations of which more
than half are not work, and the occupational mapping does not know which is which. If the
occupational mix of coursework and personal use differs sharply from that of work use, then the
headline occupational shares — and the exposure measure that gates on work usage — are averaging two
different populations. That is the construct risk under `ED-7` and under the exposure measure's own
work gate.

**Contribution.** *If it holds* (the mixes differ): the post supplies the work-only occupational mix
the corpus has never published, and quantifies how much the headline shares move. *If it fails* (the
mixes are similar): the work gate is doing little, which simplifies the interpretation of every
occupational series. *If null*: the post publishes the global use-case × task intersection with its
suppression accounting — the first time that cut appears anywhere.

**Economic Index cut (proposed).** `onet_task::use_case` and `request::use_case` at
`geography == global` in `release_2026_01_15` and `release_2026_03_24` (two of the twenty
intersections, global only, `ATLAS §Cuts 10`), with `use_case` at all three grains for the
aggregate; task → SOC via the shipped O*NET 20.1 statements to build the occupational mix under each
use case. Residual differs by wave — `not_classified` in November, `none` in February — and must not
be hard-coded (`ATLAS §Traps 24`).

**Supplementary data.** `release_2025_09_15/data/intermediate/onet_task_statements.csv` for
task → O*NET-SOC.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Data. The intersection is global only, so the whole post is one cross-section per
wave with no geography, and the use-case residual changes label between waves. If it bites, the
comparison is two global tables and the post cannot say whether the pattern travels; it should then
report the two waves as a replication rather than a trend.

**Mentor interests.** ⟨mentor⟩ interest 5, pricing the work by the wage of the occupation that
performs it (`economic-index-2026-03-report`, p.8) — which the work/non-work split directly
qualifies.

**Institute agenda.** `ED-7`; `ED-11`.

---

## LL-31 — Does what people take away from AI depend on where they are?

**Thread.** T2, with T1.

**Ledger items.** `L-2026-06-R6-30` *open* (no per-capita geography result at all in the sixth
report, though the index is released); `L-2026-06-R6-31` *open* (no subregion result, though the
grain exists); `L-2026-06-R6A-19` *open* ("Cowork" is used as a surface name without definition and
no exhibit separates chat from Cowork).

**Closest existing answer and why it falls short.** `economic-index-2026-06-report` ch.2 publishes
the artifact taxonomy and the global shares — 93% of conversations produce an artifact, with the
four largest categories at 7 / 17 / 15 / 11 percent — and the release ships 32 `artifact_*_pct`
metrics at country and subregion grain. The report publishes no geography of any kind, which the
threads map records as an absence: "Geography's measure gets finer and geography's reporting stops."
So the newest and most concrete output measure in the corpus has never been cut by place.

**External literature checked.** Chatterji et al. (2025) [abs] — topic mix by country income, not
output type. arXiv 2605.30685 [abs] — purposes by country income and language. Misra et al. (2025)
[abs] — adoption levels by economy with no content dimension. Tomlinson et al. (2025) [abs] — one
country. Nobody has published what AI *produces* by geography, because no other provider releases an
artifact taxonomy.

**Why it matters.** Artifacts are the closest thing in the corpus to output: a spreadsheet, a
document, a piece of code. A geography of artifacts is therefore the first observable answer to
`ED-1`'s value-capture half — whether richer places get different things out of the same technology,
not merely more of it. It also tests the sixth report's own silence: the release made the cut
available and the report declined it.

**Contribution.** *If it holds* (artifact mix varies systematically with income or adoption): the
post supplies the first geography of AI output and names what poorer places produce more of. *If it
fails* (mixes are flat): what people take away is invariant to place, which strengthens the case
that usage differences are about volume rather than kind. *If null*: the post reports the
suppression-limited coverage of the artifact metrics below global and shows which grains support any
comparison.

**Economic Index cut (proposed).** `release_2026_06_26`, the 32 `artifact_*_pct` metrics at
`geo_level == country` (121 ids) and `geo_level == subregion` (652 ids), `category_name == overall`,
April and May 2026 pooled as the **unweighted mean** of the two months (the specification that
reproduces the published shares, `ATLAS §Conventions`, "Pooling the two months of June 2026");
ranked against `usage_per_capita_index` where it exists (countries and US states only,
`§Cuts 4`). `GLOBAL` identity rows excluded (`§Traps 18`); `US-PR` double-count avoided
(`§Traps 16`).

**Supplementary data.** `gdp_2024_country.csv` from `release_2025_09_15/data/intermediate/` for the
income axis.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Data. The publication rule inside the country block is ragged — 2,568 of 12,319
country top-of-ladder cells publish `pct` alone — and below the top of each ladder subregions carry
`pct` only, with no counts anywhere in the wave. If it bites, artifact metrics exist for a selected
set of countries and the geography is of publication rather than of behaviour; the post must report
how many of the 121 countries carry all 32 metrics before comparing any of them.

**Mentor interests.** ⟨mentor⟩ he is first named author of the wave that introduced artifacts
(`economic-index-2026-06-report`, p.1) and of the interpretive claim that compute and human
involvement move together (pp.13–14).

**Institute agenda.** `ED-1`; `ED-3`.

---

## LL-32 — Does it matter how a conversation is credited to the occupations that share its task?

**Thread.** T8, with T1 and T5.

**Ledger items.** `L-2025-02-P1-28` *open* (equal splitting of a task's conversations across its
occupations drives every occupation-level number and is never validated);
`L-2026-03-LMIA-03` *open* (the appendix instead allocates by employment shares, mechanically giving
large occupations more of the count, with no alternative compared);
`L-2026-06-R6-39` *open* (mapped-occupation wage is used as the value of the work, with the report's
own counter-example).

**Closest existing answer and why it falls short.** The first paper splits a task's conversations
equally across the occupations that hold it; the exposure appendix splits by employment share. Both
choices are stated once and never compared, and every occupational share, every wage-based task
value and the exposure measure itself inherit whichever rule was used. The corpus contains two
incompatible allocation rules from the same team and no sensitivity analysis.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the external
critique that makes this urgent: chat-log measures "tend to over-classify chats into generic
activities spanning many occupations" [abs], which is precisely the many-holder case the allocation
rule resolves by assumption. PIIE (2026), "Research on AI and the labor market is still in the first
inning" [abs] — "Results can be sensitive to which AI measure is chosen". Tomlinson et al. (2025)
[abs] — weights activities to occupations by O*NET importance and relevance, a third rule again.
Nobody has published the sensitivity.

**Why it matters.** This is the single assumption that stands between "conversations about tasks"
and every occupational statement Anthropic has made, including the one external researchers now
build on. If the occupational ranking is robust to the rule, the whole occupational edifice is safe
and can be said so; if it is not, then which occupations look exposed is partly a modelling choice,
and `ED-7` answers depend on it.

**Contribution.** *If it holds* (rankings are stable across rules): the corpus's most load-bearing
unvalidated choice is shown not to matter, in ranks and in the top of the distribution. *If it
fails*: the post names the occupations whose position depends on the rule and shows how far they
move — including in the exposure file external teams are using. *If null*: the post publishes the
three rules' outputs side by side with the share of usage on multi-holder tasks, which is the
sensitivity the corpus has never printed.

**Economic Index cut (proposed).** `onet_task` L0 `onet_task_pct` at `geography == global` in
`release_2025_09_15`, `release_2026_01_15` and `release_2026_03_24`, allocated to SOC occupations
under three rules — equal split across holders, employment-weighted split, and single modal holder
— using the shipped O*NET 20.1 statements; compared against the wave's published occupational
shares where they exist (`soc_occupation` in the 2025-09-15 enriched file) and against
`pct_occ_scaled`, the rule that reproduces the published category shares in the flat family
(`ATLAS §Conventions`, task mix).

**Supplementary data.** BLS Employment Projections (`occupationProj`, 831 rows) for the
employment-weighted rule; `release_2025_02_10/bls_employment_may_2023.csv` (22 major groups) as the
cross-check the first release itself shipped.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design. The three rules are all defensible and none is ground truth, so the post
can show dispersion but cannot say which is right. If it bites, the finding is "the ranking moves by
X positions" with no preferred rule, which is still decision-relevant but must be written as a
sensitivity result rather than a correction — and the post must resist the temptation to declare a
winner.

**Mentor interests.** ⟨mentor⟩ "There are judgment calls involved at every step"
(`labor-market-impacts-2026-03`, fn 6 pp.15–16); ⟨mentor⟩ the employment-share allocation is his
appendix's own choice (`labor-market-impacts-2026-03-appendix`, p.2).

**Institute agenda.** `ED-7`; `WILD-6`.

---

## LL-33 — What is the tenth of enterprise AI use that is neither delegated nor collaborative?

**Thread.** T3, with T8.

**Ledger items.** `L-2025-09-R3-39` *open* (the 11% of API transcripts that are neither automation
nor augmentation is never named or explained); `L-2026-03-R5A-08` *open* (the residual recurs at
89 / 89 / 85 and the apparent 9-point automation fall is never tested against a rise in the
residual); `L-2026-01-B4-18` *open* (the shares are reported without noting that the modes are not
exhaustive).

**Closest existing answer and why it falls short.** `economic-index-2025-09-report` p.36 reports 77%
automation and 12% augmentation on the API, and `economic-index-2026-03-appendix` Fig A.3 p.6 gives
68% / 17% — pairs that sum to 89%, 89% and 85%. No publication names the residual, and the fifth
report's 9-point fall in automation is never tested against the possibility that the residual grew
instead. The atlas confirms the residual is decomposable in the long family and not in June 2026.

**External literature checked.** Chatterji et al. (2025) [abs] — carries an explicit third category,
"Expressing" at about 11%, so a residual of this size is a known feature of conversation taxonomies
rather than an anomaly. Tomlinson et al. (2025) [abs] — reports conversations where AI's action and
the user's goal differ, a related unclassifiable case. Nobody has decomposed a provider's
unclassified residual, because only Anthropic publishes the components.

**Why it matters.** The automation share is the number the policy stream, the scenario model and
external teams all use, and it is reported on a base that changes by wave and by chapter. If the
residual is doing the moving, then published automation "falls" are classification events. Anyone
using the Index's automation ratio — and the Stanford indicator note now does — needs to know which.

**Contribution.** *If it holds* (the residual is stable and small): the published automation
movements are real, and the post supplies the residual series that shows it. *If it fails* (the
residual moves with the automation share): part of a headline series is classification, and the post
dates it. *If null*: the post publishes the first decomposition of the residual into `none` and
`not_classified` across waves and surfaces, and states what June 2026 makes undecomposable.

**Economic Index cut (proposed).** `facet == collaboration`, `variable == collaboration_pct`,
**including** the `none` and `not_classified` nodes, at `geography == global` for both Claude.ai and
the 1P API in `release_2025_09_15`, `release_2026_01_15` and `release_2026_03_24` — the long family
sums to 100 including both residual nodes, so the residual is decomposable there
(`ATLAS §Other bases`). `release_2026_06_26` is reported as a boundary: it has no `not_classified`
node at all and its gap to 100 "mixes unclassified and suppressed and is not decomposable"
(`§Cuts 24`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design. `none` and `not_classified` mean different things — the attribute is
absent, against privacy-filtered or unclassifiable — and only their sum is comparable across waves if
either label is missing in a wave. If it bites, the decomposition is partly a labelling artefact;
the post reports both nodes separately, states which waves publish which, and refuses the June wave
rather than interpolating it.

**Mentor interests.** ⟨mentor⟩ the base-dependence of the automation construct underlies his α
weighting: "A task that sees only augmentative uses … would have α_t equal to 0.5"
(`labor-market-impacts-2026-03-appendix`, Definitions 10–11, p.3).

**Institute agenda.** `ED-7`; `Share 1`.

---

## LL-34 — Can a model launch be seen in what people ask AI to do?

**Thread.** T1, with T8.

**Ledger items.** `L-2025-03-R2-17` *open* (the window is the 11 days after a model launch; launch
effect and diffusion are never separated — "the corpus's only natural experiment on a lab-controlled
lever"); `L-2025-03-R2-16` *open* (the v1→v2 comparison is never re-run through one pipeline);
`L-2025-03-R2-09` *open* (the three-way fork: diffusion, novel applications of coding, or capability
improvement).

**Closest existing answer and why it falls short.** `economic-index-2025-03-report` measures usage 11
days after the Claude 3.7 Sonnet launch and reports category shifts, offering three explanations and
testing none; its own methodology section concedes the classifier changed and the relevance filter
was dropped between the two waves. The corpus therefore contains a pre/post pair around a
lab-controlled event and no attempt to read it as one.

**External literature checked.** Chatterji et al. (2025) [abs] — documents usage composition
shifting around model releases on a much longer series, and reports that multimedia usage rose after
an April 2025 model update, the nearest external evidence that launches move the mix. Bick et al.
(2026) [abs] — quarterly adoption levels, no event structure. Misra et al. (2025) [abs] — notes a
South Korean adoption jump around a model's language capability improvement. Nobody has used a
provider's own pre/post release pair as an experiment.

**Why it matters.** `ED-8` asks whether there are "dials that AI companies … might turn to control
the rate of AI diffusion on a sector-by-sector basis", and the answer depends on whether a
capability release changes *what* people bring rather than only how much. This is the only pair in
the released data that sits either side of such an event, and its confounds are documented well
enough to bound.

**Contribution.** *If it holds* (the task mix shifts beyond what the pipeline change can explain):
a capability release is visible in the task mix, and the post gives the first estimate of a dial's
effect. *If it fails*: the shift is within the range the classifier swap and the dropped filter can
produce, so the corpus's one natural experiment cannot be read — which retires the item honestly.
*If null*: the post publishes the decomposition of the v1→v2 difference into base change, filter
change and mix change, which is the audit the second report's methodology section invites.

**Economic Index cut (proposed).** `release_2025_03_27`: `task_pct_v1.csv` against `task_pct_v2.csv`
(3,514 / 3,365 tasks) and `automation_vs_augmentation_v1/_v2.csv`, on the five-classified-pattern
base with the v1 universe difference stated — v1 sums to 84.209 and v2 to 99.9965, and **"v1" in a
later folder *is* the February 2025 release**, i.e. December 2024 and Claude 3.5 Sonnet, not an
independent window (`ATLAS §Traps 26`, §Conventions "The v1/v2 base difference"). The two task lists
are not a panel: 733 v1-only and 584 v2-only (`ATLAS §Family A`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design, and it may be fatal: three things changed at once between the two files —
the model, the classifier and the occupational-relevance filter — and the release publishes no
counts, so nothing can be tested. If it bites, the post can only bound the mix change against the
base change and must report that the experiment is not identified; the steward should be asked
whether that bound is worth a post at all, and if not this candidate should be deleted.

**Mentor interests.** none; the item predates his authorship.

**Institute agenda.** `ED-8` (can AI diffusion be modulated).

---

## LL-35 — Do places that started using AI earlier get more out of it?

**Thread.** T6, with T2.

**Ledger items.** `L-2026-03-R5-23` *open* (tenure × geography is never reported, though country
fixed effects enter the specification — "the direct test of the self-reinforcing-advantage
conjecture"); `L-2026-03-R5-15` *open* (the promise to isolate cohort and survivorship bias from
learning-by-doing); `L-2026-03-R5-11` *open* (whether the benefits of early adoption are
self-reinforcing).

**Closest existing answer and why it falls short.** `economic-index-2026-03-report` ch.2 establishes
the tenure gradient at user level — long-tenure users are 3–5pp more likely to have a successful
conversation — and states that cohort and survivorship bias cannot be cleanly separated from
learning in one cross-section. The report names geography as the dimension where the
self-reinforcing conjecture would show, runs country fixed effects, and never reports the
interaction. No release carries tenure at any grain, so geography is the only cohort proxy the
public data supports.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the external
mechanism: "workers who have used generative AI for at least six months adopt it for more of their
work tasks", and experience rather than demographics drives adoption; measured on workers, not
places. Humlum & Vestergaard (2025) [abs] — firm-led investment raises the benefits reported by
users, an organisational analogue of the same story. Misra et al. (2025) [abs] — adoption levels and
changes by economy with no outcome measure. Nobody has tested whether earlier-adopting *places* show
better AI outcomes.

**Why it matters.** The self-reinforcing-advantage conjecture is the distributional claim the fifth
report makes and does not test, and it is the mechanism behind the Institute's worry that benefits
concentrate in already-rich regions. A geography-level cohort test is the only version available on
public data, and its result bears on whether convergence in *usage* implies convergence in *benefit*.

**Contribution.** *If it holds* (earlier-adopting countries show higher success today, holding task
mix and income): early adoption compounds into outcomes, and the post supplies the first
geography-level evidence for the conjecture. *If it fails*: later adopters do as well, which is
evidence against self-reinforcing advantage and for the adoption-curve reading. *If null*: the post
publishes the cohort proxy with its MDE and states what a real cohort test would require — which is
the promise the fifth report has not kept.

**Economic Index cut (proposed).** Early-adoption proxy: a country's `usage_pct` and rebuilt
per-capita usage in `release_2025_09_15` (4–11 Aug 2025). Outcome: `task_success` `yes` share at
`geography == country` in `release_2026_03_24` (5–12 Feb 2026), with `release_2026_01_15` as the
intermediate point. Controls: `human_education_years` at country, GDP per working-age capita, and the
global `onet_task::task_success` benchmark to hold task mix constant. Balanced panel of countries
above 200 conversations in all three waves; country `not_classified` share reported beside every
rate, since the steward measured it at a median 26.67% / 21.43% for this facet.

**Supplementary data.** `working_age_pop_2024_country.csv` and `gdp_2024_country.csv` from
`release_2025_09_15/data/intermediate/`.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design. Early adoption at country level is collinear with income and with the
tech-worker share, and the outcome is a classifier judgement whose classification rate varies by
country — so a positive result has at least three readings. If it bites, the coefficient is an income
coefficient; the pre-registration states the income and composition controls in advance and reports
the result with and without them, and the post's claim is about places, never about users.

**Mentor interests.** ⟨mentor⟩ "These observed differences in success rates could deepen inequalities
in the labor market… early adopters with high-skill tasks have more successful interactions with
Claude than later, less technical adopters" (`economic-index-2026-03-report`, OQ 21, p.20).

**Institute agenda.** `ED-1`; `ED-5`; `ED-10`.

---

## LL-36 — Is coding still the leading edge of AI use, or just its largest share?

**Thread.** T7, with T1.

**Ledger items.** `L-2025-04-SWE-11` *open* (which software development roles change the most, and
which might disappear); `L-2025-04-SWE-14` *open* (the conjecture that jobs centred on simple
applications and user interfaces face earlier disruption);
`L-2025-03-R2-09` *open* (whether growth in other categories is diffusion, novel applications of
coding, or capability).

**Closest existing answer and why it falls short.** The Computer & Mathematical share is the
corpus's most-cited series — 37.2% in the first paper, a peak of 40% in March 2025, 34% in November
2025, 35% in February 2026, with the API "edged higher … to 46%" — and it is always reported as one
number. No publication decomposes it: whether coding's share is falling because non-coding grew or
because coding itself narrowed, and whether the coding tasks being used are the same ones. The
fifth report attributes movement to Claude Code splitting calls and never tests it inside the
category.

**External literature checked.** Chatterji et al. (2025) [abs] — "Computer programming and
self-expression both represent relatively small shares of use", and technical help fell from about
12% to 5% of messages, a sharply different picture on a consumer product. Tomlinson et al. (2025)
[abs] — notes that "Conversational studies of Anthropic's Claude model show more emphasis on
computer and math tasks". Brynjolfsson, Chandar & Chen (2026) [abs] — young software developers' 
employment down about 20% from late 2022. Nobody decomposes the coding share inside a provider's
own series.

**Why it matters.** The Institute's headline evidence that "jobs like software engineering are
changing radically" is this thread, and the policy reading of the Index assumes coding is the
leading indicator for knowledge work. If coding's share is falling while its internal composition
shifts toward narrower, more agentic work, the leading-indicator reading changes; if the share is
falling because everything else grew, coding is simply being diluted.

**Contribution.** *If it holds* (coding's internal composition narrows as its share falls): the
leading-edge reading survives and the post shows which coding tasks are now carrying it. *If it
fails* (the share falls with composition flat): coding is being diluted by diffusion elsewhere, and
"software engineering is changing radically" is not what this series says. *If null*: the post
publishes the first within-category decomposition of the corpus's most-quoted share, with the
taxonomy breaks marked.

**Economic Index cut (proposed).** `onet_task` L0 `onet_task_pct` at `geography == global` for
Claude.ai and the 1P API in `release_2025_09_15`, `release_2026_01_15` and `release_2026_03_24`,
aggregated to SOC major group 15 (Computer & Mathematical) through the shipped O*NET 20.1
statements, with within-category concentration (share of the category's mass in its top ten tasks)
computed per wave; `release_2025_02_10` and `release_2025_03_27` reported separately on their own
base (`pct_occ_scaled`, `ATLAS §Conventions`), and `release_2026_06_26` reported separately again
because it rebuilt on O*NET 30.2.

**Supplementary data.** None beyond the shipped O*NET statements.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Data. The category is reconstructed through an external task → SOC join in the
waves that ship no `soc_occupation` facet, and the published category share depends on the
allocation rule (which is LL-32's subject), so a within-category concentration series inherits two
construction choices. If it bites, the level of the category share will not match the published
34–35% and the post must report the reconstruction gap before the decomposition.

**Mentor interests.** ⟨mentor⟩ T3(e): the migration of coding work to the API as his stated leading
indicator (`economic-index-2026-03-report`, OQ 17–19).

**Institute agenda.** `ED-7`; the agenda's own evidence claim (`institute-agenda-2026-05`, *Lead ¶4*).

---

## LL-37 — What would an early-warning signal built on AI usage data actually fire on?

**Thread.** T5, with T10 and T8.

**Ledger items.** `L-2026-05-IAGD-06` *open* ("We'll try to be an early warning signal" — no
publication defines a trigger, threshold or lead time); `L-2026-03-LMI-22` *open* (the framework
"could help identify the most vulnerable jobs before displacement is visible");
`L-2026-06-EPF-20` *open* (the tier triggers are never operationalised, with no rule for
distinguishing a 5% from a 10% world in real time).

**Closest existing answer and why it falls short.** `institute-agenda-2026-05` promises the
early-warning function, `economic-policy-framework-2026-06` indexes its three tiers to the
unemployment rate, and `labor-market-impacts-2026-03` offers the framework as the instrument. The
ledger records that no publication anywhere in the corpus defines a trigger, a threshold or a lead
time, and the recurring-items list files this as R12, promised across four publications and
undemonstrated in all of them.

**External literature checked.** Brynjolfsson, Chandar & Chen, "AI Economic Indicators: June 2026
Update" [abs] — the closest thing that exists: a monthly indicator dashboard with a "Takeoff
Tracker", which states that occupations with a higher automation ratio see smaller employment
increases and that TFP growth shows "no evidence of a break from recent levels". Audoly, Guerin &
Topa (2026) [abs] — tests exposure against postings and finds the divergence predates ChatGPT.
Frank et al. (2026) [abs] — finds exposed-occupation unemployment rising from early 2022, before the
launch. All three are outcome-side indicators; none defines a trigger on the *usage* side, which is
the only side Anthropic controls and the side it promised.

**Why it matters.** This is the Institute's most repeated public promise and its least specified
one. A post that constructs candidate triggers from released usage data, states their false-positive
rate across the six windows, and reports what lead time is even arithmetically available, converts a
slogan into a specification — or shows that the released cadence cannot support one, which is an
argument for the cadence Anthropic said it would provide.

**Contribution.** *If it holds* (a usage-side trigger persists across windows and is not fired by
noise): the post supplies the first defined early-warning rule with its false-positive rate. *If it
fails*: the released series cannot support a trigger, and the post says precisely why — window
spacing, taxonomy breaks, or noise. *If null*: the post publishes the arithmetic of lead time
against six windows in eighteen months with gaps of two to five months, which bounds every
early-warning claim the corpus makes.

**Economic Index cut (proposed).** The six released windows as a series of cross-sections (Dec 2024,
Feb–Mar 2025, 4–11 Aug 2025, 13–20 Nov 2025, 5–12 Feb 2026, April and May 2026,
`ATLAS §Cuts 27a`): candidate triggers built from (i) the five-pattern automation share by task at
global (`onet_task::collaboration`), (ii) `observed_exposure` from
`labor_market_impacts/job_exposure.csv` as the occupational weight, and (iii) task-share growth on
the matched `onet_task` panel (2,284 nodes common to the three long waves). Each trigger scored on
persistence across adjacent windows and on how often it fires in a window whose next window does not
confirm it.

**Supplementary data.** BLS Employment Projections on `occ_code` (755 of 756 matched) to express any
trigger in employment terms; no outcome series is claimed, because none ships in any release
(`ATLAS §Cuts 29`).

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design, and it is the scope risk: a trigger is only an early warning if something
later confirms it, and no outcome series is in the data, so the post can measure persistence and
false-positive rates but not predictive validity. If it bites, the honest framing is "what a trigger
could look like and how often it would fire spuriously", not "here is a working early-warning
signal" — and the post must refuse the stronger claim in its title as well as its text.

**Mentor interests.** ⟨mentor⟩ "This framework is most useful when the effects are ambiguous—and
could help identify the most vulnerable jobs before displacement is visible"
(`labor-market-impacts-2026-03`, p.3); ⟨mentor⟩ "An established approach may help future observers
separate signal from noise" (ibid. p.14).

**Institute agenda.** `Share 1` (early warning); `ED-7`.

---

## LL-38 — Which of the scenario model's parameters can AI usage data actually discipline?

**Thread.** T11, with T4 and T8.

**Ledger items.** `L-2026-09-SCPA-18` *open* ("Each parameter underpinning our scenario explorer is
something we can potentially measure … those data will tell us which scenario we are in. Today, none
of the three can be ruled out" — the corpus's clearest published measurement agenda, executed
nowhere); `L-2026-09-SCEX-09` *open* ("How can we tell?" — no indicator or diagnostic is offered);
`L-2026-09-SCPA-29` *open* (only two parameters get a sensitivity table).

**Closest existing answer and why it falls short.** `econ-scenarios-paper-2026-09` p.38 names five
measurable parameters and says the data will tell us which scenario we are in; the explorer says the
model "will inform the research Anthropic funds". Neither measures any parameter. The steward has
established what the released data can do for two of them — ψ has an observable analogue, m does not
reproduce at all — and nothing in the corpus assembles the parameter-by-parameter position.

**External literature checked.** Acemoglu (2025) [abs] — an independent task-share calibration, a
rival parameterisation rather than a measurement. Bick et al. (2026) "Mind the Gap" [abs] —
aggregate time savings of 2.3% of US hours, which speaks to the per-instance gain parameter.
Humlum & Vestergaard (2025) [abs] — ~3% time savings and null earnings effects, the same parameter
from a survey. Census "Microstructure of AI Diffusion" (2026) [abs] — 18% of firms using AI in a
business function, 32% employment-weighted, which is the diffusion parameter. The parameters have
external evidence; nobody has mapped that evidence onto the model's own dials.

**Why it matters.** The explorer is the Institute's public instrument and its central defence is
that its parameters are measurable. A post that says, dial by dial, which can be measured from
released usage data, which needs an external series, and which cannot be measured at all — with the
bound where one exists — is the audit the paper invites and the fastest way to make the model
falsifiable. It moves the prior of anyone treating the three scenarios as equally supported.

**Contribution.** *If it holds* (most dials can be bounded): the post supplies the first measured
bracket around the scenarios and names which is closest to today. *If it fails* (most cannot): the
model's measurability defence does not survive contact with its own company's released data, stated
parameter by parameter. *If null*: the post publishes the audit table with the reproduction status of
each parameter — including that the published m = 0.14 reproduces from nothing public while its
superseded 0.12 reproduces at 0.116534 — which is a service to every later user of the explorer.

**Economic Index cut (proposed).** Per parameter: **ψ** from the five-classified-pattern automation
series across seven windows (the steward's 42.5538 → 48.6190); **m** from
`labor_market_impacts/job_exposure.csv` at BLS-EP employment weights (0.116534 on the
all-employment denominator, against a published 0.14 that reproduces from nothing);
**a** from `onet_task::human_only_time` and `onet_task::human_with_ai_time` at global in the two 2026
waves, with the unit trap stated (`ATLAS §Traps 8`); **d** flagged as external only (Census BTOS,
the only BTOS file in the repository being the national workbook in
`release_2025_09_15/data/input/`); the two search frictions flagged as unmeasurable from any release.

**Supplementary data.** BLS Employment Projections for the m weights; the published BTOS national
workbook for d, cited as the paper's own anchor rather than re-estimated.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design — scope. Four parameters in one post risks four thin analyses instead of one
finding, which is exactly the failure the team's lesson 5 records. If it bites, the post sprawls; the
pre-registration therefore fixes one confirmatory quantity per parameter, caps the exploratory
allowance, and states in advance that the deliverable is an audit table with two bounded dials, not
four estimates.

**Mentor interests.** none as an author; ⟨mentor⟩ the affected-mass anchor is his measure
(`econ-scenarios-paper-2026-09`, p.25, citing Massenkoff and McCrory 2026), and the corpus's clearest
instance of one mentor publication being discounted against another runs through it.

**Institute agenda.** `ED-4`; `ED intro ¶2`; `ED-5`.

---

## LL-39 — When the ruler changed, did AI use change with it?

**Thread.** T8, with T1 and T4.

**Ledger items.** `L-2026-06-R6A-10` *open* (no old-versus-new agreement rate, so no reader can tell
how much of any change between the fifth and sixth reports is the new classifier plus O*NET 30.2 —
"the load-bearing omission for any cross-wave comparison");
`L-2026-03-R5A-05` *open* (the O*NET vintage change is asserted and never bounded);
`L-2026-06-R6-20` *open* ("A chat transcript no longer fully captures how people are using AI, and
our methods … have had to rapidly adapt").

**Closest existing answer and why it falls short.** `economic-index-2026-06-appendix` validates the
rebuilt two-step classifier with seven WildChat examples, two of them adjudicated by the authors, and
publishes no agreement rate, no position-bias test and no tie-break reliability figure. The fifth
report's 2019 O*NET-SOC recode is scoped to one figure and never quantified. So the corpus's largest
measurement break is documented as a list of changes with no estimate of what they did.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — the external
argument that chat-log classification is conceptually fragile, which this candidate turns into a
measurement. Chatterji et al. (2025) [abs] — reports usage series across taxonomy revisions on one
product without publishing a bridge either. Tomlinson et al. (2025) [abs] — validates its classifier
against user feedback, the standard this wave does not meet. No external work can measure Anthropic's
break, because it needs the released files either side of it.

**Why it matters.** Every cross-wave statement the programme might make — and every one Anthropic
makes — runs across this boundary, and the steward has just shown that three primitive levels break
at it: `ai_autonomy` falls from 3.407 to 2.72/2.74 with no announced rescaling, and the two time
primitives move with it. If quantities that should be continuous jump at the boundary while the
collaboration facet (whose taxonomy did not change) does not, the break is in the ruler. That is a
prerequisite for anyone comparing June 2026 with anything.

**Contribution.** *If it holds* (quantities whose taxonomy changed jump while the unchanged facet
does not): the June wave's discontinuity is a measurement artefact, and the post supplies the first
estimate of its size, metric by metric. *If it fails* (everything moves together): the change is
behavioural and the sixth report's numbers can be compared with the fifth's. *If null*: the post
publishes the boundary audit — which metrics are comparable across it and which are not — which is
the bridge the appendix omitted and every later user needs.

**Economic Index cut (proposed).** Quantities available either side of the 2026-03-24 → 2026-06-26
boundary, each in its own base: the five-pattern automation share (taxonomy unchanged from 2025-02-10
to 2026-06-26, `ATLAS §Conventions`); `ai_autonomy_mean`, `human_only_time_mean` and
`human_with_ai_time_mean` (the three the steward found breaking, with the units trap,
`§Traps 8`); `task_success` (a facet in the long waves, a metric in June); and the `onet` ladder's
node counts and top-ten concentration, reported as **not** comparable and used as the control. The
1P API leg is excluded throughout, because its population changes at exactly this boundary
(`§Components`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design. A jump at a boundary where several things changed at once cannot be
attributed to any one of them, and the June wave publishes no counts, so nothing can be tested. If
it bites, the post reports magnitudes and a ranking of which quantities are safe to compare, without
attributing the break to the classifier, the O*NET vintage or the window — and that is still the most
useful thing anyone can say about the boundary.

**Mentor interests.** ⟨mentor⟩ he is first named author of the wave that made the break
(`economic-index-2026-06-report`, p.1) and lead author of the wave before it, so the two endpoints
are both his.

**Institute agenda.** `Share 1` (granularity and cadence); `WILD-6`.

---

## LL-40 — How much of the world's AI use can the Index actually show?

**Thread.** T8, with T2.

**Ledger items.** `L-2025-09-R3-15` *open* (the privacy filters, with no suppression flag anywhere,
so absent ≠ zero); `L-2026-06-R6-01` *open* (cells with insufficient observations are filtered and
no count metric exists in that wave); `L-2026-06-R6A-14` *open* (no sample sizes anywhere and no
uncertainty on any published number).

**Closest existing answer and why it falls short.** Every release documents that cells below a
privacy floor are dropped, and no release publishes a suppression flag or a count of suppressed
cells. The atlas has measured the consequence in three places — country `usage_pct` sums to 82.03 and
87.49 in the two June months, a median country accounts for 55% of itself at June `request` L0, and
the steward has now added that a country's named-task mix covers only about 30% of its own
conversations. No publication states any of this, and external users of the released files have no
way to know it.

**External literature checked.** Bick, Blandin, Deming & Schumacher (2026) [full] — publishes
`number_observations` for every cell of both its indexes, which is the disclosure standard this
candidate measures the Index against. Tomlinson et al. (2025) [abs] — publishes activity shares with
a stated 0.05% coverage screen. Misra et al. (2025) [abs] — states its own volume and population
floors explicitly. Anthropic is the only one of the four whose published cells cannot be sized, and
nobody has quantified the gap.

**Why it matters.** The Institute's data-sharing promise and the independent-research programme both
rest on outsiders being able to use the released files, and the Economic Policy Framework asks
governments for exactly the granularity Anthropic itself suppresses silently. A published accounting
of what share of usage is visible at each grain is what an external researcher needs before using
the Index at all — and it is the measurement the corpus has never made about itself.

**Contribution.** *If it holds* (coverage is high at the grains people use): the released files are
more usable than the atlas's fill tables suggest, stated grain by grain. *If it fails*: a large part
of usage is invisible at the grains the reports headline, and the post gives the numbers an external
user needs to decide what to trust. *If null*: the post publishes the coverage accounting with the
one wave where it cannot be computed at all (June 2026, no counts) named as the limit case.

**Economic Index cut (proposed).** Coverage accounting at every grain that publishes counts:
`usage_count`, `onet_task_count`, `request_count` and `collaboration_count` against the
corresponding `_pct` sums, at `global`, `country` and `country-state` in `release_2025_09_15`,
`release_2026_01_15` and `release_2026_03_24` (privacy floor exactly 15 in all three, denominators
964,494 / 999,875 / 1,000,000); the `none`/`not_classified` mass by grain; and `release_2026_06_26`
reported as the case where the accounting is impossible because no count metric of any kind exists
(`ATLAS §Cuts 17`), using the `pct`-sum shortfall (82.03 / 87.49) as the only available proxy.

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Design. Much of this is already in the atlas, so the post risks being a summary of
the team's own internal document rather than a contribution. If it bites, the post has no finding of
its own; the pre-registration therefore fixes the contribution as the *cross-wave, cross-grain*
accounting the atlas records only wave by wave, plus the comparison against the three external
publishers' disclosure standards, which the atlas does not make.

**Mentor interests.** none directly; the measurement bears on ⟨mentor⟩ interest 3, stating a design's
power (`labor-market-impacts-2026-03`, p.12).

**Institute agenda.** `Share 1`; `WILD-6`; the EPF measurement ask (PDF p.5).

---

## LL-41 — Does the threshold behind AI's published productivity number survive being moved?

**Thread.** T4, with T11.

**Ledger items.** `L-2026-01-R4-16` *open* ("We choose a threshold of 0.02% because it replicates our
previous results … If we do not impose a restriction … the implied aggregate labor productivity
growth … would be roughly 5% percentage points per year" — the single most consequential
undocumented free parameter in the productivity chain);
`L-2026-01-R4-17` *open* (tasks without observed speedup are assumed to have none);
`L-2025-11-PROD-21` *open* (no uncertainty is propagated to the 1.8%).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` fn 6 pp.52–53
states the threshold, states that dropping it takes the headline from 1.8pp to roughly 5pp, and
justifies the choice by its ability to replicate the earlier result. That is the whole of the
sensitivity analysis: one alternative, reported in a footnote, with no curve between the two points
and no interval on either. The productivity number is the corpus's most quoted aggregate.

**External literature checked.** Humlum & Vestergaard (2025) [abs] — ~3% average time savings and
null earnings effects, an order of magnitude below the estimator-based figure. Bick et al. (2026)
"Mind the Gap" [abs] — aggregate time savings of 2.3% of US hours. METR (2025) [abs] — a measured
19% slowdown against a forecast speedup. Acemoglu (2025) [abs] — a much smaller macro number from a
task-share calibration. The external literature brackets Anthropic's estimate from below; nobody has
examined the threshold that sets it.

**Why it matters.** Anthropic's own scenario paper discounts this estimate by a factor of four, the
Institute cites it, and policy readers quote the 1.8pp. If the number moves monotonically and
steeply with an undocumented inclusion threshold, then the published figure is a choice about which
tasks count, and the honest headline is a range. This is the cheapest available audit of the
corpus's most-quoted number.

**Contribution.** *If it holds* (the estimate is flat over a defensible threshold range): the
published number is robust where it matters and the post says over what range. *If it fails*: the
headline is a function of the threshold, and the post publishes the curve between 1.8pp and 5pp that
the footnote only anchors at two points. *If null*: the post publishes the task-set and mean-speedup
consequences of the threshold without the aggregate — which is still the first sensitivity curve
anyone has drawn on it.

**Economic Index cut (proposed).** The threshold acts on the task set, so the reproducible object is
the task set and its speedup distribution: `onet_task_pct` at `geography == global` with
`onet_task::human_only_time` and `onet_task::human_with_ai_time` in `release_2026_01_15` and
`release_2026_03_24`, sweeping the inclusion threshold from 0 to 0.1% and reporting, at each point,
the number of tasks retained, their share of usage mass, and the usage-weighted mean speedup with
the wave's unit convention (`ATLAS §Traps 8`). The aggregate itself needs employment weights that
ship in no 2026 release (`§Cuts 29`), so it is rebuilt only as an external-join extension and
labelled as such.

**Supplementary data.** BLS Employment Projections and the shipped O*NET 20.1 statements for the
Hulten-style weights, with the merge audit printed; the 1.8pp and ~5pp figures quoted as published,
never rebuilt.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Data. The published aggregate needs conversation-level speedups and a wage-bill
weighting that no release ships, so the post cannot reproduce 1.8pp and therefore cannot show the
aggregate's threshold curve directly. If it bites — and the atlas says it will (`§Cuts 29`, "Blocked
as published") — the post's object is the task set and its mean speedup, with the aggregate discussed
only through the published endpoints, and the title must not promise more.

**Mentor interests.** ⟨mentor⟩ T4(e): he is lead author of the report carrying the threshold and the
success adjustment (`economic-index-2026-01-report`, p.1, ch.4).

**Institute agenda.** `ED-4`; the Research Fund's productivity-measurement priority.

---

## LL-42 — Is the income gradient in AI use about how much people ask, or about what they ask for?

**Thread.** T2, with T1 and T4.

**Ledger items.** `L-2025-09-R3-21` *open* ("What determines AI adoption across countries and within
the US?"); `L-2026-01-R4-31` *open* (three candidate explanations for the use-case gradient by
income, none tested); `L-2025-09-B3-01` *open* (as GDP per capita rises, use shifts away from
Computer and Mathematical tasks).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` Fig 3.2 p.30
reports the use-case gradient by income (coursework r = −0.542, personal r = 0.681, work not
significant at p = 0.131) and Fig 3.3 the AUI–GDP elasticity of 0.70; the September report gives the
task-mix version. The two are always reported separately, so nothing says how much of the income
gradient in *usage per person* is the same phenomenon as the income gradient in *what is used for*.
The report itself lists three explanations and tests none.

**External literature checked.** arXiv 2605.30685, "How Early Adopters Used Generative AI
Worldwide" [abs] — the closest external work: schooling use is most prevalent in lower-income
countries and leisure use rises with income, on a different platform's data, and it does not
decompose an adoption gradient into intensity and mix. Chatterji et al. (2025) [abs] — growth faster
in lower-income countries, with topic mix by income. Bick et al. (2026) "Mind the Gap" [abs] —
attributes cross-country adoption gaps to demographics and firm composition, i.e. to who is using
rather than to what for. The decomposition is unmade.

**Why it matters.** `ED-1` asks what determines whether a place can access AI and how it captures
value. Those are two questions, and the Index has two gradients that are always reported as one
story. If richer countries differ mainly in intensity, access is the binding constraint; if they
differ mainly in mix, then value capture is, and the policy implication changes from connectivity to
capability. It moves the prior of anyone reading the 0.70 elasticity as a statement about access.

**Contribution.** *If it holds* (the gradient is mostly intensity): access and volume are the story,
and the post says how much of the income relationship survives holding the use-case mix fixed.
*If it fails* (mostly mix): richer places use AI for different things and the same elasticity means
something else, which the post states with the mix-adjusted elasticity. *If null*: the post publishes
the first joint decomposition of the two published gradients with its MDE at 111–115 countries.

**Economic Index cut (proposed).** `release_2025_09_15` enriched, `geography == country`: the AUI,
`gdp_per_working_age_capita`, `working_age_pop` and the `onet_task` and `request` mixes in one file
(the only wave where all of these co-exist, `SB2 14`); and `release_2026_01_15` /
`release_2026_03_24` for the `use_case` facet at country grain, whose income axis must come from the
2025-09-15 GDP file because the 2026 waves ship none (`§Cuts 22, 29`). Decomposition of the
AUI–income elasticity into a within-mix component and a mix-composition component, at `request` L1/L2
where cell fill permits and never at `onet_task` L0 below global (`§Cuts`, Family B fill table).

**Supplementary data.** `gdp_2024_country.csv` and `working_age_pop_2024_country.csv` from
`release_2025_09_15/data/intermediate/`.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-3.md`.

**Biggest risk.** Data. The decomposition wants the AUI, income and the use-case mix in one wave, and
no wave has all three: the AUI and GDP are in August 2025, `use_case` arrives in November 2025. If it
bites, the post either decomposes on the task mix in 2025-09-15 (available, but not the use-case
gradient the fourth report published) or splices two waves, which the programme's own rules
discourage. The steward's ruling on which of the two is admissible determines whether this candidate
survives.

**Mentor interests.** ⟨mentor⟩ "lower income, less educated countries paradoxically showing more
complex use in some cases" (`economic-index-2026-03-report`, OQ 13, p.17).

**Institute agenda.** `ED-1`; `ED-3`.

---

## Deletions

| ID | question | deletion reason |
|---|---|---|
| LL-25 | Is the American geography of Claude the American geography of AI? | **Subsumed by LL-05**, on the steward's own pairing: "the pair I would name is **LL-05 / LL-25** — one design (Index AUI against the Microsoft diffusion series) at two geographies from the same provider" (`room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`, standing answer (c)). LL-25 was FEASIBLE WITH CAVEAT, not refused, so this is the lead's deletion, not the steward's: it has strictly less power than LL-05 (N = 51 on a single external quarter, Q1 2026, against 100 countries overlapping both AUI waves) and there is no finer fallback, because the Index publishes no county or metro grain. The US-state leg survives as a pre-registered robustness cut inside LL-05's brief, with the steward's audit carried over: `data/US/State_Rankings_2026Q1.csv` is 51 rows with a `State Abbr` column matching the August 2025 `state_us` ids 51 of 51, no crosswalk needed. The two ledger items LL-25 carried that LL-05 does not — `L-2026-01-R4-09` (the country/state level-dependence) and `L-2026-07-CONN-04` (state-by-use-case reliability) — are picked up by LL-27 and LL-22 respectively, so nothing on the ledger is dropped by this deletion. |
