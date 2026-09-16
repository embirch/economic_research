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
| 2 | LL-15 … LL-28 | `room/lead-2026-09-16-longlist-feasibility-batch-2.md` | pending | awaiting feasibility |
| 3 | — | — | — | not started |

New atlas facts the steward logged for batch 1 are at `data/ATLAS.md ## Dated log 2026-09-16 (e)`
(fifteen numbered facts) and `## Supplementary sources`, "Third-party comparators fetched, joined
and licence-checked 2026-09-16 (e)" (the four external series, with their merge audits). Three of
them changed a design rather than confirming it: the `request` ladder has almost no cross-wave node
correspondence (LL-06 moves to `onet_task`), the RPS occupation index is published at SOC minor
group and not by 3-digit prefix (LL-03 runs at N = 90), and a country's published task mix covers
only about 30% of that country's conversations (LL-06's suppression control changes).

## Counts

| | |
|---|---|
| drafted | 28 |
| deleted | 0 |
| surviving | 28 (LL-01 … LL-14 confirmed by the steward; LL-15 … LL-28 provisional) |

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
itself. No work compares `observed_exposure` to a survey adoption index.

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

**Contribution.** *If it holds* (records and users rank clusters alike): conversation shares are a
usable proxy for user shares, and the Index's standing unit caveat is bounded by a measured
correlation for the first time. *If it fails*: the post names the use cases that are concentrated
in few users and the ones that are broad, which is the breadth/intensity split the corpus says it
cannot make. *If null* (bucketing destroys the comparison): the post documents how much resolution
the privacy bucketing costs, which is a measurement fact for anyone using that file.

**Economic Index cut (proposed).** `release_2025_03_27/cluster_level_data/` — the 630 level-0
clusters (→145 L1 →30 L2) with `percent_records` **and** `percent_users`, plus the per-cluster
collaboration and thinking ratios in the same TSV. Caveats to carry: prevalence is bucketed into
100 buckets so ties are artefacts and no test assuming distinct values may be used
(`ATLAS §Traps 34`); 178 of 630 rows have suppressed collaboration/thinking cells
(`ATLAS §Thresholds`); cluster names carry no ids and match no later taxonomy (`§Cuts 31`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. `percent_records` has exactly 100 distinct values across 630 rows because of
the privacy bucketing, so the ratio of the two columns may be dominated by bucket width rather than
by behaviour. If it bites, the ratio is a step function and the post reports the bucket structure
and a rank test robust to ties, not an elasticity.

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
patterns + `filtered`) at global. Cross-check on a later wave with `request` L0/L1/L2 and
`onet_task` L0 at global in `release_2025_09_15`, where a `request_hierarchy_tree_*.json` also
ships (`ATLAS §Cuts 25` — it is the last wave that has one).

**Supplementary data.** `release_2025_02_10/onet_task_statements.csv` (byte-identical to the March
copy, `82e4c418…`) for the task → O*NET-SOC side of the concordance.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. This is the one remaining `steward?` flag in the ledger
(`LEDGER §Cross-reference 36`): whether the cluster file's O*NET field and the hierarchy JSON
support a published coverage-gap measure is unresolved, and cluster names carry no ids. If it bites,
the concordance is a text match with an unmeasurable error rate, and the post must present it as a
descriptive mapping with the unmatched mass reported rather than as a gap statistic.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. Joining two marginals on the same tasks cannot distinguish "the same
conversations that were directive also used thinking" from "tasks that attract directive use happen
to attract thinking", and `filtered` swamps rare tasks (1,066 of 3,364 are 100% filtered,
`ATLAS §Traps 35`). If it bites, the correlation is a between-task fact only; the post states the
inferential limit in the sentence that carries the number and weights by `pct` with `filtered`
renormalised out.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Construct. "Could the human have done this alone" is a classifier's judgement
about a counterfactual, made from a transcript, with no validation statistic anywhere in the corpus
(`L-2026-01-R4-01` is the standing caveat). If it bites, cross-country differences in the primitive
are differences in how the classifier reads prompts in different languages, and the post must report
the task-mix-held-constant version beside the raw one and treat the level as uninterpretable.

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
with their statistics at all three grains in `release_2026_01_15` and `release_2026_03_24`;
`human_education_years` is the one numeric facet carrying confidence intervals in 2026-03-24
(`ATLAS §Cuts 20`), so the residual's uncertainty is one-sided and must be stated. Task mix held
constant at global with `onet_task::human_education_years` and `onet_task::ai_education_years`.

**Supplementary data.** None required; if an education benchmark is wanted, the report's own
comparator is BLS attainment, which ships in no release (`ATLAS §Cuts 29`) and would be an external
join.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. A difference of two classifier outputs has the variance of both and the
validation of neither, and the two are correlated at r ≈ 0.93, so the residual may be almost all
noise. If it bites, the residual's cross-country variance will be small relative to its measurement
error; the pre-registration therefore states the reliability floor the post needs and reports the
raw pair beside the residual.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. Success is classified by the same model that produced the conversation and
is confounded with task mix, language and prompt style, all of which vary by country; and the
composition control is global-only, so it cannot be applied within country. If it bites, the
gradient is a task-mix artefact; the post therefore reports the raw gradient, the global
composition-adjusted benchmark, and the share of each country's mass on tasks whose global success
rate is known.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. Every cost and token measure is an index re-based to mean 1.0 at global
grain, so levels are unrecoverable and "cost" is realised spend, which already embeds model choice.
If it bites, unit price cannot be separated from model mix at all and the honest post is a
decomposition of *spend* into tokens and residual, with the residual named as model mix and the
published elasticity re-expressed in those terms.

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
by raw share", month to month, with the specification stated — the atlas already records 32.7% /
33.1% / 19.8% against 83–88% under the two rules (`ATLAS §Traps 39`), so the post extends a measured
fact rather than guessing. Total April→May unit recurrence holds (every April unit recurs in May;
7 countries and 116 subregions are May-only, `ATLAS §Coverage`).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. The June wave publishes **no count metric of any kind** (`ATLAS §Cuts 17`)
and `value` is pre-rounded to two decimals, so cells cannot be sized and Iceland's 0.02 carries
±25% relative error. If it bites, the recurrence rate cannot be converted into a per-cell noise
estimate, and the post must present persistence as an observable proxy for reliability, stated as
such, rather than as a standard error.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. The exercise can only re-run the quantities Anthropic published, and
"Utah's activity is not driving the results" is a claim about results we can reproduce only where a
specification is documented — the elasticities and the Gini, not the internal checks. If it bites,
the post reports sensitivity for the four reproducible quantities and states plainly that the
report's own unnamed checks remain unverifiable, which is the ledger item's real content.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. The destination list is a handful of occupations named in prose, so the
post is coding a small, judgement-laden set and any claim about "retraining destinations" in general
rests on it. If it bites, the result is sensitive to the coding of four titles; the pre-registration
therefore publishes the crosswalk, reports the result for the named set and for the broader sector
families separately, and states which occupations would have to be added to flip the conclusion.

**Mentor interests.** ⟨mentor⟩ "If current data on AI usage are any guide, college-educated
workers—software developers, paralegals, accountants—are most at risk (Massenkoff and McCrory 2026).
But this is highly uncertain." (`worker-retraining-2026-08`, p.4.) ⟨mentor⟩ "Impose a high
evidentiary standard" (ibid. p.5).

**Institute agenda.** `ED-5`; Research Fund Priority 2.

---

## LL-25 — Is the American geography of Claude the American geography of AI?

**Thread.** T2.

**Ledger items.** `L-2025-09-R3-45` *open* (the AUI's working-age denominator is a proxy the
report's own conjectures contradict); `L-2026-01-R4-09` *open* (the relationship pattern at country
level contradicts the pattern at state level, flagged and left);
`L-2026-07-CONN-04` *open* (the connector implies a reliable state-by-use-case cut while the
reports' own results carry thresholds and suppression).

**Closest existing answer and why it falls short.** `economic-index-2026-01-report` Fig 1.7 p.13
explains nearly two-thirds of cross-state AUI variation with the tech-worker share, and
`economic-index-2025-09-report` p.19 gives the state income slope of 1.8. Both explain Claude's
state geography with state characteristics; neither compares it with another measurement of AI use
by state, and the fourth report's own puzzle — that country and state relationships have opposite
signs — is left open. This candidate is deliberately distinct from LL-05 (countries) and LL-10 (the
convergence rate): it asks whether the state ranking itself is a Claude artefact.

**External literature checked.** Misra et al. (2025) and the Microsoft AI Diffusion repository
[abs] — publishes `State_Rankings_2026Q1.csv`, `County_AI_User_Share_2026Q1.csv` and
`MSA_Ranking_2026Q1.csv`, i.e. a population-normalised AI user share for US states, counties and
metros, with no comparison to any provider's own index. Bick, Blandin, Deming & Schumacher (2026)
[full] — national, not sub-national. Daepp & Counts (2025), "The Emerging Generative Artificial
Intelligence Divide in the United States" [abs] — a US sub-national divide measured on different
telemetry. Nobody compares a provider's state index with an independent state measure.

**Why it matters.** The state convergence result is the Index's strongest policy-facing claim and
the one an American policymaker is most likely to act on. If Claude's state ranking and an
independent AI ranking agree, the convergence finding is about AI; if they do not, it is about where
Anthropic's users are, and the `ED-1` access question has a different answer inside the US than
across countries — which is exactly the level-dependence puzzle the fourth report flagged.

**Contribution.** *If it holds* (state rankings agree): the state-level diffusion story is about AI
and the post says so with a rank correlation and the states that disagree. *If it fails*: the
convergence claim is partly a statement about Claude's user base, and the post identifies the states
that drive the difference and whether tech-worker share explains them. *If null*: the post reports
the overlap, the interval, and the fact that 51 units cannot separate the two hypotheses — with the
county and metro files named as the route that could.

**Economic Index cut (proposed).** State AUI at two published points and two rebuilt ones:
`release_2025_09_15` enriched `state_us` (51 rows, published AUI, 100-conversation floor);
`release_2026_06_26` `geo_level == subregion`, `metric_id == usage_per_capita_index`, 51 US ids in
each of April and May 2026 (never `US-PR`, `ATLAS §Cuts 4`; the union of country and subregion rows
double-counts `US-PR`, `§Traps 16`); and `US-*` rows in `release_2026_01_15` and
`release_2026_03_24` rebuilt on the Census state population file. Ranks and ratios, not levels.

**Supplementary data.** `State_Rankings_2026Q1.csv` from `github.com/microsoft/ai-diffusion-report`
(`data/US/`), joined on state name → USPS via
`release_2025_09_15/data/input/census_state_codes.txt` (pipe-delimited FIPS/USPS, 57 rows); the
county and metro files are the extension if the state comparison has no power.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. The external state file is one quarter (Q1 2026) while the Index's nearest
windows are February and April–May 2026, so the comparison straddles different periods and different
constructs (conversations per working-age person against the share of working-age people using AI).
If it bites, a rank disagreement cannot be attributed to market share rather than timing, and the
post must report the comparison at every available Index window to show the ranking is stable before
it interprets any gap.

**Mentor interests.** ⟨mentor⟩ T2(e): lead author of the report that built the state convergence
model (`economic-index-2026-01-report`, p.1).

**Institute agenda.** `ED-1`; `Share 1`.

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

**Contribution.** *If it holds* (the fall is between-occupation composition): Anthropic's mechanical
reading is right, and the post supplies the decomposition it asserted. *If it fails* (a
within-occupation component): AI is being used for cheaper work inside the same occupations, which is
a different and more consequential statement. *If null*: the post publishes the shift-share with its
uncertainty and shows how much of the $1.40 movement is smaller than the measure's own vintage
sensitivity.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Design. The published movement is $1.40 on a $49 base, which is small relative to
the wage measure's own vintage and deflator ambiguity, and Anthropic states neither. If it bites,
the decomposition's components are each larger than the total and the post's honest finding is that
the published change is inside the measure's uncertainty — which is worth publishing, since the
report reads a mechanism into it.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Data. Roughly half the sub-national units are below the 100-conversation floor, so
the units that survive are the large metros, and a within-country variance computed on them
understates dispersion while their `not_classified` share varies. If it bites, the decomposition is
about big regions only; the post must report the surviving units' share of each country's usage and
run the decomposition at both the 100 and the 385 floors the steward proposed (`SB2 17`).

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

**Economic Index cut (proposed).** `ai_autonomy` — a numeric facet with its statistics at all three
grains in `release_2026_01_15` and `release_2026_03_24` (global mean 3.38 → 3.41), plus the global
histogram (histograms are global only, `ATLAS §Cuts 20`) and the global
`onet_task::ai_autonomy` intersection; and `ai_autonomy_mean` in `release_2026_06_26` for the API
block, with the boundary caution attached (`SB2 15`).

**Supplementary data.** `Anthropic/enabling-independent-research`, `metr` subset: 604 rows, 14
facets, 247,315 records on one April–May 2026 window, including `supervision_intensity`
(`fully_autonomous` 42.8%) and `task_success`, licensed CC BY 4.0. It carries **no** O*NET task, SOC
code, occupation or date column, so the steward's rule governs: "the two can be cited side by side,
each on its own sample, never merged" (`SB2 6`). Facet × facet two-way tables inside it *are*
recoverable (`SB2 5`).

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-2.md`.

**Biggest risk.** Construct, and it is the reason this candidate could be deleted: the two measures
have no common unit, no common sample and no common window, so any comparison is of distributions
from different populations. If it bites, the post can only bound the Index scale's reach and must not
state a difference as a finding; the assumptions sweep therefore carries the steward's
never-merge rule verbatim, and the post's claim is about the **measure**, not about surfaces.

**Mentor interests.** ⟨mentor⟩ T3(e): "API workflows are far more likely to be directive, with less
need for a human in the loop" (`economic-index-2026-03-report`, OQ 17, p.9); ⟨mentor⟩ he is second
author of the agentic-coding paper (`claude-code-expertise-2026-06`, p.1).

**Institute agenda.** `WILD-10` (where humans are in the loop); `ED-8`.

---

## Deletions

| ID | question | deletion reason |
|---|---|---|
| — | — | none yet; no steward feasibility line has been returned |
