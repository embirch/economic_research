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
| 1 | LL-01 … LL-14 | `room/lead-2026-09-16-longlist-feasibility-batch-1.md` | pending | awaiting feasibility |
| 2 | — | — | — | not started |
| 3 | — | — | — | not started |

## Counts

| | |
|---|---|
| drafted | 14 |
| deleted | 0 |
| surviving | 14 (all provisional until the steward's lines land) |

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
waves cannot be used.

**Supplementary data.** None needed: this is the one wave shipping AUI, population and GDP in one
file (`SB2 14`).

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

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
automation comparison twelve months apart does exist" and the ψ sub-section.

**Supplementary data.** None. The presets come from the published explorer and paper.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

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
geography, no date (`SB1 8`; `SB2 9`). Aggregated to 3-digit SOC with external employment weights
for the rank test, and kept at detailed SOC for the Microsoft comparison.

**Supplementary data.** (a) RPS occupation-level genAI adoption index, Bick–Blandin–Deming–
Schumacher (2026), ~14,000 workers over four waves Aug 2025–May 2026, 3-digit SOC, downloadable
from the RPS data page — join on the 3-digit SOC prefix of `occ_code`. (b)
`github.com/microsoft/working-with-ai` `ai_applicability_scores.csv`, detailed 2018 SOC — join on
`occ_code`. (c) BLS Employment Projections (`data.bls.gov/projections/occupationProj`, 831 rows) for
employment weights; merge audit already run: 756 in, 755 matched, one unmatched (`11-1031`).

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The RPS index is published at 3-digit SOC while `job_exposure.csv` is
7-character detail, so the comparison needs an employment-weighted aggregation and will lose
occupations on both sides. If it bites, the rank test runs on far fewer than 756 units and the
confidence band on Spearman's ρ is wide enough to be uninformative — which is why the merge audit is
a pre-registered output, not a footnote.

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

**Supplementary data.** O*NET database 27.x text zip (`onetcenter.org/dl_files/database/`) for the
**Task-to-DWA** reference table — `labor_market_impacts/` matches O*NET 27.0–27.3 set-identically on
all 17,992 task strings (`ATLAS §Taxonomies`), so the crosswalk vintage is determined; plus the RPS
task-level adoption index (O*NET DWAs) from Bick et al. (2026), joined on DWA id.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The RPS task index covers only the ten most important activities per
occupation that respondents were shown, so its DWA coverage is a selected subset of O*NET's ~2,000;
if that bites, the comparison is over a few hundred DWAs weighted toward important activities, and
the post must report the covered share of Claude's task mass before any comparison.

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

**Supplementary data.** Microsoft AI Diffusion country shares (H2 2025 report and/or the
`arXiv:2511.02781` tables), join on country name → ISO-3 via
`release_2025_09_15/data/intermediate/iso_country_codes.csv` (252 rows); Bick et al. (2026)
published country adoption rates for the US and six European countries.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The external series may be published only as report figures for a few dozen
countries rather than as a machine-readable table; if that bites, the overlap set is small enough
that a rank test has no power, and the post falls back to a named-country comparison with the
interval printed. The steward's judgement on machine-readability decides the design.

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

**Economic Index cut (proposed).** `release_2026_01_15` and `release_2026_03_24`, long schema:
`facet == request`, `level` 1 and 2, `variable == request_pct` at `geography == country` and at
`global`; plus `usage_pct` at `country` for the weights; plus `onet_task` L0 at `global` for the
published headline. Shift-share of the change in the global concentration measure into a
within-country mix component and a between-country weight component, computed at `request` L1/L2
because `ATLAS §Cuts`, Family B fill table, says "Compare mixes at level 1 or 2, never at level 0
below global" (median 18 of 3,260 `onet_task` L0 cells per country in Feb 2026).

**Supplementary data.** None.

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. Suppression is silent and varies by country and wave, so a country's
published mix can change because publication changed rather than because behaviour changed. If it
bites, the within component will track each country's published `pct` sum; the pre-registration
therefore fixes a balanced panel of countries above the floor in both waves and reports the
published-mass share as a control.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The wage file is a 2019 third-party O*NET scrape that mixes hourly and
annual values for six occupations and covers 1,090 of 974+ code variants, and the 2026 waves ship no
reference file at all. If it bites, the gradient is estimated on the subset of tasks whose
occupation carries a usable wage, and the post must report that subset's share of total usage before
the coefficient.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. Both variables are produced by the same estimator reading the same
transcripts, and users bring tasks they expect to work, so a positive elasticity is consistent with
selection and with estimator artefacts as much as with economics. If it bites, the placebo moves
with the outcome too; the post must pre-register that reading and state it as a property of the
measure rather than of the economy.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. Task shares mean-revert and both waves' shares are measured with error, so
a regression of the change on the initial level inherits a negative bias, and the classifier changed
nothing between these two waves but the taxonomy vintage did shift for one figure. If it bites, the
coefficient is negative for mechanical reasons; the pre-registration therefore specifies a
split-sample instrument for the initial level and reports both.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. Four windows over ten months, 51 units, two of them excluded by
Anthropic's own rules in one wave and not in another, and a population vintage that reproduces the
Gini but lands 0.7–0.9pp below published concentration shares. If it bites, the bootstrap band spans
"no convergence" to "two years" — which the post reports as the finding rather than hiding, since
either end is informative about the published claim.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. Both surfaces publish shares, not levels, so a task's share can fall on
one and rise on the other with no conversation moving; and the report's own mechanism — one coding
job becoming many API tasks — mechanically dilutes API shares. If it bites, the negative correlation
appears for accounting reasons; the pre-registration therefore states the identity, restricts to
tasks present in all six frames, and reports the same test on non-coding tasks as a control.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The task universe is not constant: the fifth report recoded to 2019
O*NET-SOC for one figure and the sixth rebuilt on O*NET 30.2 with a two-step classifier, and
suppression removes rare tasks first. If it bites, a rising within-wave count is a classifier
artefact; the post therefore restricts to the three waves whose facet and variable sets are
set-identical and reports the count of tasks published in all three.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Design. One three-month step, ~118 countries above the floor, and an outcome
(`usage_pct`) that is a share of a global total, so one large country's growth mechanically lowers
everyone else's. If it bites, every coefficient is a mirror of US and Indian growth; the
pre-registration therefore uses log usage relative to the global mean and reports the raw-share
version beside it.

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

**Steward feasibility line.** pending — see
`room/lead-2026-09-16-longlist-feasibility-batch-1.md`.

**Biggest risk.** Data. The vintage the paper used is unobtainable from this sandbox —
`download.bls.gov` returns 403 and `web.archive.org` is egress-blocked (`ATLAS §Supplementary
sources`) — so the post can compare a *published coefficient* against a coefficient it computes on
the current vintage, not two vintages it computed itself. If that bites, the post is a level check on
one vintage with the published number quoted as published, and it must say so in the sentence that
carries the comparison.

**Mentor interests.** ⟨mentor⟩ "The government's own occupational growth forecasts, while
directionally correct, have added little predictive value beyond linear extrapolation of past
trends" (`labor-market-impacts-2026-03`, p.3, fn 1); ⟨mentor⟩ interest 1, a displacement measure
checkable against official series.

**Institute agenda.** `ED-7`; `Share 1`.

---

## Deletions

| ID | question | deletion reason |
|---|---|---|
| — | — | none yet; no steward feasibility line has been returned |
