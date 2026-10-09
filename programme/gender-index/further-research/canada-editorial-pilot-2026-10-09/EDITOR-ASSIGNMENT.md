# Managed Claude Editor: complete Canada developmental redraft

This is Emily's authorised Canadian editorial pilot, approved 9 October 2026. You are the deployed managed Claude Editor v5. Your service budget is $13.50 within a $15 editorial task allocation and a $30 complete pilot. No cap increase or other paid session is authorised. Work only on `work/canada-editorial-pilot-2026-10-09-safe`. This replaces the initial branch after an input packaging correction. Never push or use the superseded initial branch; the safe branch has a clean parent and excludes internal results.json.

## Current policy and actual task

Read current AGENTS.md, PROJECT.md, programme/DECISIONS.md and team/SETUP.md, then this assignment and the current handover. Old preambles saying the European article is active are superseded. The European manuscript is historical and protected. Do not read or rewrite posts/gender1 or restart its comparison. This task is ONLY E08 Canada, unpaid job work. Time-off is outside the article, although preserved analytical files still contain it.

Emily has rejected the latest editorial quality. Statistical checks do not establish editorial acceptance. The replacement paragraph proposed in a previous chat is not approved wording. Your task is to produce a complete, carefully reasoned proposed research article, not another broad editorial assessment or cosmetic edit.

The audience is a rigorous economics reader such as Maxim Massenkoff, arriving with no knowledge of this project. Do not impersonate him or imply his approval. The basic acceptance question is: **could a new reader follow the argument without having to reconstruct it?**

You own the entire proposed article: title, Introduction, results explanations and transitions, figure titles/captions, Discussion and reader-facing Methodology. Use Emily's voice, clear complete sentences and short paragraphs. No em dashes or first person. Keep exact research questions once in Introduction; Discussion precedes Methodology. The goal is coherent synthesis supported by the data and literature, not a chain of numerical results and generic caveats.

## Verify your input before work

The coordinator has prepared latest local material, including uncommitted changes, on this branch. Check every path/hash in `programme/gender-index/further-research/canada-editorial-pilot-2026-10-09/input-manifest.json`. If required inputs do not match, report the discrepancy before substantive work. Record the actual source commit and input-manifest hash in your editorial notes. Do not assume the old remote HEAD is current.

## Required reading, with scope

Current study directory: `programme/gender-index/further-research/studies-2026-10-07/E08/`.

Read manuscript.md, presentation-copy.json, figure-specs.json, METHODS.md, CLAIMS.csv, public-tables.csv, scale-comparison.csv, influence-summary.json and literature-review.md. Use released aggregates and analysis.py to resolve defined interpretive points. Internal results.json is intentionally excluded because it contains a suppressed time-off aggregate. Do not recreate, copy, quote or publish that file or any suppressed value. Do not run an estimator or fetch respondent data.

Also read:

- `programme/gender-index/further-research/editorial-method-2026-10-09/PROPOSED-METHOD.md`.
- `programme/gender-index/further-research/approved-revision-2026-10-09/CANADA-INFLUENCE.md`, `independent-canada-verification.json`, and relevant completion/check records. The all-16-stratum influence check is DONE.
- `programme/gender-index/further-research/studies-2026-10-07/reviews/E08-NUMERICAL-REVIEW.md`.
- `.claude/skills/anthropic-style/SKILL.md`. Historical style-guide rules do not override current directions.

Read three relevant primary reference pieces for explanatory technique, with relevant local annotations in wiki/style/ as navigation:

1. https://www.anthropic.com/research/labor-market-impacts : especially Introduction, Counterfactuals and Prioritizing outcomes.
2. https://www.anthropic.com/research/estimating-productivity-gains : especially Introduction, measure definitions and Validation.
3. https://www.anthropic.com/research/81k-economics : especially Who benefits from AI?, Scope and speed, and Discussion.

The existing Cadences reference is https://www.anthropic.com/research/economic-index-june-2026-report . Consult relevant passages if useful, without mechanically copying its structure. Learn how the authors motivate a comparison, explain a construct concretely and integrate evidence. Do not repeat their wording or borrow stronger identification claims.

Use the current E08 literature note for scientific source versions and reading depths. Any new substantive supporting sentence must be checked against an actual primary passage. Goldin currently has an abstract-level reading, not a verified full-paper reading. Dillon's randomised access experiment measures out-of-hours application activity, not total or necessarily unpaid work. The current Jiang full-text access limit remains. Relevant Cranney/Delecourt/Koning interpretation is recorded in E08's literature note: participation does not by itself measure workers' benefits. Carry that distinction into the internal synthesis; no compulsory HBS section in the article. Targeted source checks are allowed, new corpus construction is not.

## First develop the argument

Before polished prose, create a short argument brief covering:

- The concrete economic question and why the gender comparison matters.
- The actual survey measure, eligible population, period and comparison.
- What the observed results jointly establish, and why that is useful beyond listing rates.
- The connection to closest prior work and the actual incremental contribution.
- Alternative interpretations that genuinely change the conclusion.
- The purpose of each main figure and how it advances the argument.

Then write the COMPLETE proposed article. Do not stop after the brief. It is acceptable to narrow the ambition or shorten material. Do not invent methodological novelty, promise a causal answer, manufacture a striking reversal or frame inconclusiveness as equality. A conclusion only saying “collect better data” is inadequate; explain the present supported insight.

Emily identified these specific failures in the current Canadian opening:

1. It does not name AI.
2. “Working less” is ambiguous between hours, effort and output.
3. A shorter working day, more output and different responsibilities mix concepts that are not equivalent or mutually exclusive.
4. “Depends on demand for output” does not explain how time saved on a task translates into workers' experience.

Apply this level of scrutiny across the entire manuscript. Explain who does what, under what condition, with what implication. Distinguish hypothetical mechanisms from observed results. The data measure unpaid-job-work FREQUENCY, not hours, productivity, pay, personal-time gains or causal adoption effects. Establish the bridge between the economic motivation and this narrower observation, without turning the opening into a list of disclaimers.

## Scientific boundaries to preserve

The analysis compares 20,538 public/private reference-job employees aged 15–69 in ten Canadian provinces in pooled 2024–2025 cross-sections. Some reference jobs are former jobs. GenAI use is any reported use over the relevant 12 months, not intensity. Men+/Women+ are the source gender categories. Unpaid job work during personal time is not domestic/caring work.

Users' frequent unpaid-work rates are higher in both groups. The raw Women+-minus-Men+ difference between user/nonuser gaps is +3.4 points [0.5,6.3]; additive adjustment +2.7 [−0.2,5.6]; common occupation/sector mix −1.7 [−5.2,1.7]. The observed and common-mix targets are both legitimate descriptions. The latter is not the uniquely correct answer and does not identify what occupation causes. Absolute and proportional associations differ. Covariates AND modelling assumptions differ between additive and common-mix results.

The completed influence check gives common-mix point estimates of −2.6 to +0.1 points across all 16 single-stratum deletions, all intervals including zero. Restricted-population deletions are not alternative national estimates. Contributions are concentrated. Do not claim a stable reversal. Do not rerun these checks or expose private fine-cell results.

## Writable outputs and stopping point

Write ONLY inside `programme/gender-index/further-research/canada-editorial-pilot-2026-10-09/editor/`:

- `argument-brief.md`: concise developmental argument and paragraph/figure plan.
- `manuscript.md`: complete proposed article, retaining working relative source/result links and the three current figure markers. You may change their narrative placement if justified; do not reintroduce time-off.
- `presentation-copy.json`: complete compatible copy file based on the current one, with any proposed wording changes. Preserve identifiers, units, data, row membership, source links and scientific scope; retain unused historical time-off entry unchanged.
- `editorial-notes.md`: substantive changes, exact source passages/version/read-depth, claim-to-evidence support for changed interpretations, unresolved weaknesses, source commit/hash, and final spend if available. Clearly distinguish a fetched original from inherited notes.

Do not edit live study inputs, builders, analysis, results, empirical figures, project instructions, ledger, other studies or previous versions. No reviewer agents or paid sessions. Codex will build the proposed view locally, show it to Emily, commission the independent readers and integrate corrections. You may use existing renderer logic for a local scratch check but do not commit generated pages or unrelated files.

Before returning, read the full proposed manuscript as continuous prose, then check every edited quantitative claim against the saved aggregate records. Check that title, findings, chart language and Discussion agree. Commit only the four owned outputs and push the assigned branch, never main, no force-push or merge. Return commit, paths, principal editorial changes, unresolved issues and actual spend. Stop after delivery; do not begin the referee stage.
