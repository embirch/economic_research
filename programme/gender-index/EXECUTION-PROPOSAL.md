# Gender & AI Index: proposed research and delivery plan

Prepared for Emily Birch, 30 September 2026. Discussion draft requested in Codex; no research session, spending, publication or new paper is authorised by this proposal. Current starting programme commit: `3f72fdb`. Earlier decisions and the authoritative first paper remain in force.

Update, 1 October 2026: Emily accepted the recommended first $20 data-steward pilot and requested a data-led assessment of global rather than European-only scope. The current assignment is `team/assignments/2026-10-01-steward-pilot.md`; further tranches remain uncommissioned. See [geographic scope](GEOGRAPHIC-SCOPE.md). Global ambition applies to the resource; the existing European paper remains unchanged.

Pilot outcome: delivered for $6.21. The [coordinator review](reviews/2026-10-01-pilot-review.md) reproduces the file diagnostics and identifies corrections required before integrating the scientific claims. This is not release or methods approval.

## 1. What we would build

A maintained evidence resource answering three questions: who uses generative AI, what they use it for, and what opportunities or barriers shape their experience. Economic consequences remain a research question. The working name is Gender & AI Index, but the first edition would present separately defined indicators and an evidence explorer. A single score or worldwide league table is not needed for a useful release.

The proposed primary audience is researchers and policymakers; a short narrative layer would serve interested readers and journalists. Emily confirms this audience and scope before the first research tranche. Success is a reader being able to understand a comparison, inspect its limitations, and trace it to its source and calculation.

Proposed first edition:

| Component | Minimum useful version | Conditional extension |
|---|---|---|
| Participation | European use rates and absolute/relative gaps, reusing the authoritative paper's frozen source and derived results | Other national surveys displayed separately after instrument checks |
| Purposes and patterns | European use contexts with explicit denominators | A distinct ChatGPT message-pattern panel if Signals passes its audit |
| Experience and opportunity | Evidence cards and coverage gaps; non-use reasons if eligible | Workplace support/training and source-specific case studies after joint-field checks |
| Economic implications | A clearly labelled library of bounded published studies | Occupational exposure context or new outcome analysis only after a separate feasibility decision |
| Methods and coverage | Definitions, source cards, missing coverage, reproducibility, permissible downloads, release date and correction log | Additional countries and years as eligible sources become available |

The release can be useful with one strong survey family. A blocked second source should not force a weak comparison or delay the existing paper. Binary source categories will be described as such; absent nonbinary data remain an explicit coverage gap. Higher male use is not a target, and more use does not establish greater welfare.

## 2. Responsibilities and when Claude is useful

### Two repositories, one programme

`gender-gap-generative-ai` owns paper one: its frozen European inputs, analysis, figures and live author edits. `economic_research` owns the index and wider programme: evidence register, source audits, geographic scope, new indicator methods, explorer, assignments and reviews. The current steward pilot writes only to the programme repository.

The planned connection is a read-only, version-pinned reuse of permitted paper outputs, with the article commit and source hashes recorded in the index. The adapter has not yet been built. There should be no second editable manuscript in the programme repository; `posts/gender1` remains historical reference. A broader index or newer source release does not silently change paper one's geography, results or author text. Later papers can remain separate projects with the same documented output interface.

At pilot launch, the current credential cannot access the article repository; the agent receives a coordinator-supplied provenance summary, not an assertion that it independently inspected the frozen files. Local copies and preserved commits remain available to Codex for read-only checks.

| Owner | Specific responsibility | When engaged |
|---|---|---|
| Emily | Scientific direction, interpretation, editorial voice, budgets, final inclusion and release | Three main decisions: commission feasibility; choose release scope; approve publication |
| Codex | Prepare assignments and inputs, manage branches and provenance, integrate results, run checks, build the explorer, present decisions and costs | Throughout; one integration owner |
| Claude data steward | Verify actual data, measures, access/reuse terms, coverage and source families | First research task; limited later source corrections |
| Claude programme lead | Focused literature and adjacent-resource comparison; identify the contribution and strongest follow-up questions | Alongside source verification, with separate output ownership |
| Claude analyst | Draft measurement plan, implement permitted calculations and source-specific diagnostics | After source selection; no speculative modelling to compensate for missing variables |
| Claude referee | Independently inspect source evidence, challenge estimands and reproduce material results | Short feasibility review, then substantive methods/results review |
| Claude second-read referee | Verify a finite list of resolved review issues | Only if substantive corrections warrant it; not a default second full review |
| Claude editor | Improve new explanatory prose, evidence cards and consistency using approved claims | After Emily sees the initial draft and commissions editorial work |
| Claude director | Coordinate a genuinely complex batch of interdependent specialist tasks | Not proposed for the initial edition; Codex already coordinates |

Use the existing deployed roles and their configured models. The local deployment receipt records analyst/data-steward/programme-lead/referee v3, second-read referee v2, editor v5 and director v6; verify the current deployment against the lockfile at launch. Do not silently update models or reuse an old session with obsolete context.

AI review is useful for reproducibility and criticism, but it is not independent human peer review. Before making strong methodological or gender-measurement claims, seek a suitable human methods/gender reviewer when available. Any outreach or paid human review requires a separate instruction and budget.

## 3. Step-by-step work

### Step 1 — Fix the brief and launch only a bounded first tranche

Codex turns this proposal into a one-page agreed brief: audience, organising questions, provisional modules, exclusions, deliverables and spending envelope. Reuse the concept, additional-source audit, 14 candidate indicators and 8 literature records. Do not reopen the first-paper comparison.

Prepare versioned assignment files using `team/templates/ASSIGNMENT.md`. Each specifies the source commit, role/version, writable files, branch, output, validation, cap and stopping point. Give agents only the inputs they need. Agent work requiring local raw files stays blocked until access, licence and permitted processing environment are checked; do not upload respondent data merely to make a cloud assignment convenient.

Deliverable: launch-ready briefs and an explicit authorisation entry. Decision A: Emily approves the first tranche and its caps. Routine work inside it then proceeds without repeated permission requests.

### Step 2 — Verify the evidence inventory

The data steward follows `FIRST-ASSIGNMENT.md`, starting with the three Eurostat entries. Reuse local audit manifests and the paper's frozen source version before downloading newer releases. Check all 14 candidates, grouped by source family, rather than commissioning 14 disconnected reviews.

For each, inspect actual permitted files and documentation where available: population, fieldwork and reference dates, AI definition, survey question/routing, sex/gender variable, unit, denominator, weights/design, joint variables, subgroup sizes, suppression/missingness, uncertainty, source version, access and redistribution terms. Reproduce a relevant published benchmark where feasible. A codebook or report alone earns documentation-only status.

Use a bounded triage rule: one documented access route and one reasonable alternative before recording an access blocker. Do not spend a whole session repeatedly trying a blocked download. Record unavailable, not yet checked and inaccessible as different states.

Deliverables: updated indicator register; source-family profiles in `evidence/sources/`; country/year/measure coverage matrix; `evidence/VERIFICATION-REPORT.md`. Every candidate receives a verdict: ready for bounded calculation, documentation-only, blocked, or unsuitable for the intended construct.

The historical `new_check_this_setup=false` field continues to mean that the original setup performed no verification. Date subsequent checks in linked source profiles; preserve the earlier audit trail.

### Step 3 — Establish the contribution and identify omissions

The programme lead examines the existing eight literature entries and the specific overlap questions already raised in the audits: adoption syntheses, national gender reports, platform dashboards, workplace studies and neighbouring gender/AI indices. Record search terms, dates, versions, inclusion decisions and underlying sample families. This is a focused scoping review, not a systematic review unless a separate protocol and search justify that label.

Ask what the resource adds beyond republishing existing charts: traceable source-specific measures, explicit comparability, maintained coverage and uncertainty, and original analyses where feasible. Include female advantages, null findings and measurement gaps. Review excluded populations, unpaid work and nonbinary gender coverage as scope questions rather than manufacture indicators for them.

Deliverables: a short contribution memo and overlap table, plus a shortlist of possible papers. The lead may flag missing sources, including the UK leads already in the concept but absent from the 14-row register; additions go into a proposed queue, not an automatic expansion of the first steward assignment.

Steps 2 and 3 can run concurrently once authorised: the steward owns indicators/source profiles, while the lead owns literature and a contribution memo. Both read common inputs. Codex reconciles disagreements and source-family IDs.

### Step 4 — Choose the smallest defensible release

Codex integrates the two outputs. The referee performs a bounded challenge of the proposed inclusion decisions and the weakest critical assumptions, with access to primary evidence rather than only the authors' summary.

Separate statistical indicators from literature-only evidence. Inclusion requires a meaningful question, interpretable measurement and denominator, usable coverage, permitted reuse, reproducible provenance, and an honest treatment of uncertainty. Do not force an ordinal quality score to substitute for these judgements.

Present Emily with a concrete release list, exclusions with reasons, and a small number of unresolved choices. Decision B: approve modules and methods development. If only Eurostat is ready, proceed with that core and clearly labelled evidence cards. If Signals is ready, add it as a separate platform module. If workplace data remain inaccessible, retain that question in the research queue.

### Step 5 — Write and review the measurement plan

The analyst specifies each selected indicator before substantive new analysis. The plan records the estimand, population, eligible cells, numerator/denominator, country/year coverage, exclusions, sample overlap, gap direction, uncertainty, missingness handling and sensitivity checks. Disclose all previous data inspection and distinguish confirmatory questions from exploratory comparisons. The existing paper's scope and prior-inspection statement remain unchanged.

Survey conventions follow the current article: absolute gap = male rate minus female rate in percentage points; relative gap = 100 × (male rate − female rate) / male rate. Always show both underlying rates. Mark the relative gap undefined at a zero male rate. Do not clip negative gaps. Source labels take priority over casually treating sex categories as complete gender measurement.

Signals would use a different estimand: the feminine-name share within a topic relative to a compatible overall baseline in the same period. It does not measure women's participation rate, their share of activity devoted to a topic, or changes within the same people. Confirm available category denominators and release compatibility first.

Specify survey-design-based uncertainty when supported. Do not create confidence intervals from rounded aggregate percentages or use global message totals as subgroup sample sizes. Describe noisy/suppressed data limitations; separate descriptive sensitivity checks from statistical significance. If many comparisons are made, prespecify the primary set and how exploratory results will be labelled.

The referee reviews the plan's critical assumptions before calculations. Codex integrates agreed changes; refer only material scope disagreements to Emily under Decision B.

### Step 6 — Build the reproducible data layer

The analyst produces source-specific acquisition/transform scripts, diagnostics, derived tables and figures for the approved modules. Codex defines a shared output contract and integration checks. Proposed new paths, created only when needed, are `programme/gender-index/methods/`, `analysis/`, `derived/`, and `reviews/`; existing `evidence/` remains the source register.

Every observation carries indicator ID, source/release ID, geography, field/reference period, population/subgroup, source sex/gender category, unit, denominator, value, uncertainty status, flags and provenance. Paper figures and the explorer consume the same reviewed derived values. Keep immutable source snapshots and checksums; record software dependencies and the command needed to reproduce outputs.

For the first paper, Codex makes a read-only adapter to its frozen permitted outputs. No specialist receives permission to edit `gender-gap-generative-ai`, and `paper/author-edits/blog.html` is never regenerated or overwritten. A newer data vintage would be a separate index release, not a silent revision to the manuscript.

Checks target real risks: joins preserve expected keys and counts; missing/suppressed values are not zeros; percentage scales and sign conventions are correct; every public number is traceable; reproducible benchmarks match or have explained differences. Public Git contains scripts, hashes, schemas and permitted aggregates, not individual-level files, restricted excerpts or credentials.

### Step 7 — Independently verify results and claims

The referee reproduces at least one complete indicator per source family and all headline comparisons from source inputs, checks discrepant/extreme cells, audits denominators and sign conventions, and challenges alternative interpretations. Review must not consist only of rerunning the analyst's final notebook or agreeing with its prose.

Deliverable: findings classified as release-blocking, required correction, or optional improvement, linked to exact files and evidence. The analyst fixes analytical issues; Codex fixes integration problems. If needed, the second-read referee checks the defined corrections once. If a substantive disagreement persists, present it to Emily rather than commission an endless loop of model reviews.

A human reviewer, where available and commissioned, should assess the interpretation and gender-measurement limitations. Keep the record explicit about what was AI-assisted checking and what received human review.

### Step 8 — Build a small usable explorer and explanatory draft

Codex adapts the existing prototype only after the derived-data contract is stable. Proposed reader flow: choose a question, select a valid source-specific comparison, see underlying rates and the gap, then open its evidence card and methods. Filters show only valid combinations. Missing coverage is visible; maps do not imply global representativeness.

Prepare accessible charts, keyboard operation, text/table equivalents, readable source labels, exportable permitted data and explicit field dates. Test a few substantive questions end to end and reconcile displayed values with the reviewed tables. Do not label illustrative prototype values as validated output.

Emily sees the initial narrative and evidence cards. If commissioned, the editor improves clarity and consistency against an approved claims map and Emily's voice, without modifying calculations or touching the first paper. Recheck changed empirical wording against the reviewed evidence. Human usability feedback should focus on whether readers understand who/what is counted and what comparisons mean.

### Step 9 — Publish a versioned first edition

Codex assembles a release candidate: explorer, source register, methods, permitted downloads, reproducible code, release manifest, limitations, corrections policy, and AI-assistance disclosure. Verify code/content/data licences separately; the project does not acquire redistribution rights merely by linking to or downloading a source.

Decision C: Emily approves the final public presentation and release. A public working Git repository is not equivalent to approval to publish the website or announce findings. No public announcement, source-owner message, scheduled monitoring, or paid hosting is included without its own instruction.

Publish a dated static edition first. Keep prior editions and associate each chart/paper with its exact source and derived-data version. The existing paper need not wait for the whole explorer if Emily wishes to release it separately.

### Step 10 — Maintain the resource and select later papers

Refresh when eligible source releases materially change the evidence, with separately approved maintenance work. Check questionnaire, population, classification and release changes before extending a series. Preserve breaks and corrections; do not promise quarterly updates for annual or irregular sources. Notifications/automations would be a separate explicit setup.

Keep paper one as the existing European manuscript. Select papers two and three only after feasibility and contribution review. Compare: longitudinal task representation using Signals; workplace conditions using permitted EWCS/Eurobarometer data; a Spanish motivation pilot; and returns/intensity only where variables and reuse terms support it. Select a replacement if a candidate fails; do not automatically grow the portfolio.

The Spanish pilot, if chosen later, would code 100–150 short responses in Spanish, blind coders to gender, allow ambiguity/multiple codes, and compare with independent human coding. Recalled motives are not observed first tasks; cross-sectional current/former use is not longitudinal retention. Human coding time and any restricted-data processing permission are separate dependencies.

## 4. Initial source queue

This table describes the existing local audit record, not a new verification of current online releases.

| Queue | Candidates | First action / stopping rule |
|---|---|---|
| Core reuse | EU_USE, EU_PURPOSE, EU_NONUSE | Reuse authoritative source vintage and inspect exact denominator/routing/terms; no paper rewrite |
| Candidate second module | SIGNALS_TOPIC | Check release licence, category denominator, country/month/topic completeness and noise/suppression limitations |
| Workplace and experience feasibility | EWCS_WORK, EB_SUPPORT, PEW_GENDER | Resolve actual joint-field access and coverage; reproduce a benchmark only with permitted data |
| Specific access questions | CEDEFOP_SKILLS, ECB_WORK, RPS_USE_RETURNS | Resolve named release/variable/permission issue, otherwise record blocked; no repeated speculative acquisition |
| Conditional contextual/case material | SPAIN_MOTIVATION, ISSP_ATTITUDES, ILO_EXPOSURE | Check terms, constructs and usable coverage; preserve broad-AI, modelled exposure and selected-sample labels |
| Literature context | ANTHROPIC_CONTEXT | Attribute published findings; do not infer user gender from occupational shares or unstructured transcripts |

Later acquisition priorities may differ from the minimum-release queue. The follow-up audit's emphasis on workplace sources is a reason to assess their feasibility early, not a reason to delay reuse of the completed European analysis.

## 5. Proposed spending and pacing

These are suggested control envelopes, not estimates based on measured session costs, quotations or guarantees of completion. No amount is approved. Codex work in this chat is excluded from the separate Claude session envelopes, not represented as free. Human review, data fees and hosting are excluded. Keep models as currently configured.

| Tranche | Proposed Claude allocation | Suggested ceiling |
|---|---|---:|
| A: evidence and contribution decision | Steward $60, programme lead $25, feasibility referee $15 | $100 |
| B: selected first-edition measures and verification | Analyst $60, substantive referee $30 | $90 |
| C: conditional corrections and editorial support | Second-read referee $15 if needed; editor $20 after Emily sees the draft | $35 |
| Total possible first-edition envelope | All three separately commissioned tranches | $225 |

Start with a steward pilot capped at $20 within its $60 allocation: verify the Eurostat family and report actual cost and blockers. Commission the remaining steward work only after checking this calibration; it is not an automatic budget increase. If the initial allocation is inadequate, reduce scope or return with a concrete revised proposal. There is no automatic transfer of unused money between roles and no automatic restart after a limit or idle state.

The service's documented limits are enforced between requests and can overshoot by an in-flight request. Treat numeric session caps as operational controls rather than a guaranteed invoice maximum; leave headroom when configuring a user-approved overall envelope and reconcile actual spend from the API. Do not promise exact completion or cost from the suggested ceilings.

Indicative sequence, dependent on access and Emily's review time: first working week for bounded verification/contribution; second for selection and methods; following one to two weeks for approved calculations, checking and a small preview. External access or human review can extend this. Papers two and three have no schedule or budget in this plan. Re-estimate after the first tranche using observed throughput.

## 6. How each Claude assignment would actually run

1. Codex verifies the approved scope/cap, deployment receipt and model configuration; prepares the assignment and permitted inputs from a known programme commit.
2. Create and push a named work branch. Give each concurrent agent non-overlapping files. An agent receives the mounted programme repository, not automatic access to all local folders or the separate paper repository.
3. Launch the existing specialist directly through `team/run_agent.py` with assignment path, explicit dollar cap and branch. Do not start a director by default. Verify public/private data processing permissions before providing any new source files to a cloud environment.
4. Monitor progress and actual spend; stop for a concrete access/measurement blocker rather than encourage unbounded exploration. At completion, budget stop or idle, collect the deliverable, provenance, branch/commit, checks, unresolved issues, session ID and actual spend in `team/RUNS.csv`.
5. Codex reviews changes, runs relevant empirical checks as well as setup CI, and resolves integration conflicts. Merge through a PR only within the approved task and review requirements. Repository protection does not establish statistical correctness.
6. Update current decisions and assignment status once; pass only the necessary evidence to the next role. Existing memory provides retrieval context, not authority to activate old tasks.

For concurrency, the steward and lead may run in parallel after approval. Analytical work depends on source selection; a referee begins from a fixed plan/results version; editorial work depends on reviewed claims. Never put the analyst and reviewer in charge of editing the same files.

## 7. Proposed next decision

Agree the first-edition direction and commission only Tranche A, initially releasing the $20 steward pilot. Its immediate output is verified Eurostat source profiles and a cost/blocker report. Then use the remaining proposed tranche to finish the 14-candidate inventory, contribution assessment and feasibility review. No new paper, composite index, broad literature collection or full website build is implied.

## Basis and methodological references

- Current local records: `PROJECT.md`, `programme/DECISIONS.md`, `team/SETUP.md`, `programme/SETUP-READINESS.md`, `team/deployment/agents.json`.
- Existing index materials: `concept-and-feasibility.md`, `additional-sources-audit-2026-09-30.md`, `FIRST-ASSIGNMENT.md`, `evidence/indicators.csv`, `evidence/literature.csv`.
- [Eurostat digital economy and society methodology](https://ec.europa.eu/eurostat/web/digital-economy-and-society/methodology): use the relevant survey-year instruments and quality information when verifying measures. Consulted 30 September 2026.
- [OECD/JRC Handbook on Constructing Composite Indicators](https://www.oecd.org/en/publications/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en.html): methodological reference for any separately commissioned future composite; this proposal does not perform that exercise. Consulted 30 September 2026.

The targeted methodology-page checks for this proposal are not a new data audit. Candidate source availability and novelty claims still require Steps 2–4.
