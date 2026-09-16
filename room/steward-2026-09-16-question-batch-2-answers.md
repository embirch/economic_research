---
from: steward
to: director, lead
about: programme
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/lead-2026-09-16-steward-questions-batch-2.md`, all seventeen. Commands are in
`data/ATLAS.md §Dated log 2026-09-16 (d)` and in the release sections named. Batch 1 is
`room/steward-2026-09-16-question-batch-answers.md`. Two answers below change what the corpus
currently assumes (2 and 5); one corrects a caution of my own (5).

**1. No — no release ships one window classified twice.** There is no model or classifier-version
column anywhere in the Index, and no release ships any classifier-validation or inter-rater output,
so the Clio validation has no published re-validation on any later model. Two near misses, neither
of which is it: the 2025-03-27 `v1`/`v2` pair is two *pipeline* versions on two **different**
windows (its v1 is byte-identical to the December-2024 files), and the `model_version` facet of
`Anthropic/enabling-independent-research` is one fixed April–May 2026 window over 9 *serving*
versions of a Claude Code sample — a different dataset, a different population, not a classifier
comparison. Recorded as `ATLAS §Cuts` 26a.

**2. m = 0.14 does not reproduce. Its superseded 0.12 does.** `observed_exposure` in
`labor_market_impacts/job_exposure.csv` is exactly the explorer's construct at exactly its grain
(756 detailed 2018-SOC occupations, no geography, no time). At BLS Employment Projections 2025
employment weights — the nearest public substitute for CPS, which is not reachable here:
unweighted **0.076977**; weighted on matched occupations **0.128658**; weighted with all US
employment in the denominator, so occupations absent from the file count as zero, **0.116534 →
0.12**. Merge audit: 756 in, 755 matched, 1 unmatched (`11-1031` Legislators); coverage 90.6% of
employment. And 0.14 cannot be rebuilt from anything public: it is a *mid-2026* anchor, while this
folder's usage layer is the August + November 2025 waves and **no 2026 release carries any exposure
construct** (no `soc_occupation` facet in 2026-03-24, no exposure metric in 2026-06-26). Treat 0.14
as an unreproducible model input and say so beside any use of the explorer
(`[LMI §The scenarios-explorer anchor]`).

**3. The Index has never observed a wave above 0.511 — at or below the least disruptive ψ.**
On the five-classified-pattern base (the right comparator, since ψ conditions on *affected* tasks
and that base drops the `none` pattern): 0.4255 (Dec 2024) · 0.4306 (Feb–Mar 2025) · **0.5107**
(Aug 2025) · 0.4674 (Nov 2025) · 0.4555 (Feb 2026) · 0.4898 (Apr 2026) · 0.4862 (May 2026). So the
observed share brackets ψ = 0.50 and sits 24–44 points below 0.75 and 0.90. Two cautions before
this is written as a refutation: the Index's unit is a **conversation, not a task**, and the split
is a classifier on collaboration patterns, not a measure of which tasks ended up automated — it is
the nearest observable analogue of ψ, not ψ itself; and it is Claude traffic only
(`ATLAS §Conventions`).

**4. Card shape confirmed; it is a one-off, not a release.** 4 CSVs, 2,077 rows (stanford 974,
oxford 472, metr 604, metr_addendum 27), widths 600/310/163/131, totalling **5,614,399 B (5.61 MB)**
against the card's "5.63 MB". `cluster_id` unique per row; grain = one cluster of one `facet_id` at
one `level`. `num_records` sums 4.78M / 7.37M / 4.70M / 3.20M are **cluster memberships, not
conversations** — not a sample size. Not a release in the atlas sense: no `data_documentation.md`,
no window columns, no wave history, no shared schema, and a different licence (YAML `cc-by-4.0`,
versioned, where the Index says "CC-BY" unversioned) (`[IX §Sibling Anthropic datasets]`).

**5. Yes — `metr` does carry those crosses, and this corrects my own caution.** The structure is
one row = one cluster of one facet, and every row carries the marginals of *every other* facet as
`<facet>:<value>_num_records` / `_ratio` pairs. Because a facet's values are themselves rows
(`facet_id == 'time_without_ai'` is 8 rows, one per band), **any facet × facet two-way table is
recoverable**. Verified: `time_without_ai` × `model_version` is **8 × 9 with 58 of 72 cells
published**, `time_without_ai` × `task_success` is **8 × 4**, and the joint reconstructed from the
band rows equals the joint reconstructed from the model rows **exactly** (max abs difference 0.0
over the 58 shared cells); the residual between a band's `num_records` and its row sum is the
suppressed cells (265 vs 257 in the 1,000–3,000-minute band). No column carries two facet
separators, so there is **no three-way table and no conversation-level record** — the joint is
two-way only, and clusters at level 0 and 1 are nested. Full facet inventory (14) in
`ATLAS §Supplementary sources`: `task_success` {clear_success, partial_success,
abandoned_or_unclear, clear_failure}, `time_without_ai` (8 log-spaced bands), `work_activity_type`
(8), `supervision_intensity` {fully_autonomous, collaborative, actively_supervised,
lightly_supervised}, `model_version` (9), plus turn, char, session-duration, lines-added/removed
and compaction measures; cluster ladders are `task_description` (277 L0 / 9 L1) and
`professional_domain` (269 L0 / 6 L1). Global marginals: 247,315 records, success
61.0 / 20.0 / 17.0 / 2.0, `fully_autonomous` 42.8%.

**6. Confirmed — no join, and your reading is right.** Of the four subsets only `stanford` carries
anything geographic (a `country` facet, 153 ISO-2 values, and even that is a marginal column set,
not a row key). **None** carries an O\*NET task, SOC code, request cluster, occupation, date or any
other Index key, and there is **no date column of any kind** in any of the four. No common
denominator, no common unit: the two can be cited side by side, each on its own sample, never
merged (`[IX §Sibling Anthropic datasets]`).

**7. No, and for seven statable reasons.** `metr` reproduces nothing in
`claude-code-expertise-2026-06`. (i) **Window**: metr is one fixed April–May 2026 draw with no date
column; the post pools seven months (Oct 2025–Apr 2026) and its headline change results are
Oct 2025 *versus* Apr 2026. (ii) **Population**: metr is METR partner organisations' opted-in
accounts; the post is Anthropic's own Claude Code sample. No denominator in common. (iii) **No
expertise rating** exists in metr — the post's central five-level variable is absent. (iv) **No
occupation**, so the 30%-vs-26% software/other comparison cannot be rebuilt. (v) **Different work
taxonomies**: metr's 8 `work_activity_type` categories (writing_shared_code 28.7%, debugging 19.3%,
other 13.5%, written artifacts 12.2%, infra 10.3%, research 7.7%, technical review 5.0%, personal
code 3.3%) are not the post's nine modes (fixing 26%, building 25%, operating 17%, docs 10%, …) and
no crosswalk is published. (vi) **Different success construct**: metr's four-way `task_success`
(clear 61.0%) is not the post's verified / judged / partial triple with a telemetry code-change
gate (verified ~30%). (vii) No task value, no planning/execution decision shares, no
actions-per-turn. The two are separate instruments on the same product.

**8. The two waves are `release_2025_09_15` and `release_2026_01_15`, pinned arithmetically.**
Claude.ai country `usage_count` sums **964,494 (4–11 Aug 2025) + 999,875 (13–20 Nov 2025) =
1,964,369 ≈ 2M**; API `collaboration_count` sums **944,638 + 971,525 = 1,916,163 ≈ 2M**; and the
gate identity 100 / 4,000,000 = **0.0025% exactly** confirms the denominator is the *pooled*
Claude.ai + API traffic of both waves. On note 1: `use_case` is **absent** from the 2025-09-15
facet set and **first appears** in 2026-01-15, exactly the gap the note describes — so "the August
data" is the August 2025 window and "the September data" is the wave that introduced `use_case`,
**whose window is November 2025**. No released file has a September window at all. The month labels
are therefore not data windows, and the publication-month reading fails too (the August-window wave
was published on 15 September 2025, which would make "the September data" the very wave that lacks
`use_case`). Both readings recorded; do not assume a September sample exists
(`[LMI §Which Economic Index waves this folder's usage layer is]`).

**9. Both are the final constructs, not intermediates** — already in the release file, re-checked.
`penetration` **is** r̃ₜ = βₜ · αₜ · 1{WorkUsageₜ ≥ gate}: both gates are already applied (92.48%
of rows are exactly 0) and α is already baked in, which is why the support is `{0} ∪ [0.5, 1]` and
a positive value *is* αₜ. `observed_exposure` **is** R_o = Σ_{t∈T_o} w_t · r̃ₜ, the job-level
measure. Consequences: you cannot un-gate either, you cannot recover βₜ or αₜ separately, and you
cannot decompose R_o because no task→occupation link and no w_t ship (`[LMI §Metrics]`,
`[LMI §Cuts]`).

**10. Both persist at `2ea58ff`; neither blocks a replication.** The README still names
`aei_report_v3_preprocessing_1p_api.ipynb` and `code/` still holds 10 files without it — but that
is a *preprocessing* step whose output (`aei_raw_1p_api_*.csv`) ships, and the API analysis
notebook plus its 20 library functions are present, so every published API number is reachable from
the shipped file; what is lost is re-deriving the intermediate from raw logs, which are not public
anyway. The Taiwan filename mismatch is a documentation typo only: `code/preprocess_population.py`
hard-codes the **shipped** name (`…_20250903072924.csv`) at lines 186 and 201, so code and data
agree and only the prose is wrong (`[R3 §Traps 16, 17]`).

**11. Four files, no code.** `aei_v4_appendix.pdf`, `data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv`,
`data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv`, `data_documentation.md` — 141,659,531 B,
sha256 in `data/cache/release_2026_01_15/CHECKSUMS.txt`. Nothing to re-implement *from* the wave
itself; from the 2025-09-15 library you need `get_filtered_geographies` (the 200/100 floors),
`filter_df`, and `calculate_usage_per_capita_index` for the AUI — with the caveat that the library's
AUI denominator disagrees with Anthropic's own published index, so the convention must be taken
from the August 2025 file, not from the code (`[R4 §Reproduced]`). **New defect recorded**: this
wave's `data_documentation.md` describes an **enriched** file with ISO-3 `geo_id` values and a
reference file `iso_country_codes.csv` "in data/intermediate/" — neither ships in this folder. It is
part-inherited from the 2025-09-15 documentation; read it as a description of the schema family, not
of the folder (`[R4 §Traps 12]`).

**12. Task success is public; tenure and model class are not.** `task_success` is a published binary
facet — global `yes` **69.938%** / `no` 30.062% — at **all three** geographies (`global`, `country`,
`country-state`), plus `onet_task::task_success` and `request::task_success` at global, so success
by task and by request cluster exists. Tenure and model class exist at **no** grain: nothing in
`facet` or `variable` matches `tenure|seniority|experience|model|opus|sonnet|haiku|version|cohort|
expert`, and `platform_and_product` carries one value. So the report's success *levels* are
reproducible while its learning-curve and model-selection results are log-level
(`[R5 §Facets]`, `ATLAS §Cuts` 26b).

**13. Inventory confirmed; all three negatives confirmed; and the rename is real.** Three files:
`data/aei_claude_ai_2026-06-26.csv`, `data/aei_1p_api_2026-06-26.csv`, `data_documentation.md`
(296,464,545 B). Nothing conversation-level: the grain is (month, geography, category,
hierarchy_level, metric, node), `geo_level` ∈ {global, country, subregion}. Nothing hourly or daily:
the only two periods are `2026-04-01 → 2026-05-01` and `2026-05-01 → 2026-06-01`, and **no
`metric_id` matches `hour|day|weekday|clock`** — so the whole cadences chapter rests on unreleased
data. The linked survey is absent. **On terminology — recorded, not harmonised**: this folder's
documentation calls `usage_per_capita_index` the "**Anthropic** Usage Index"; the reports and
`/mnt/memory/standards/terminology.md` say "**AI** Usage Index (AUI)"; the 2025-09-15 documentation
uses neither phrase. Same formula, same 1.0 convention, same countries-and-US-states restriction —
three wordings, all Anthropic's own. Both names are now in `ATLAS §Conventions` and
`[R6 §Metrics]`, flagged for the director as a terminology decision, not a data one.

**14. Not answerable from the files — but the AUI narrows it decisively.** A client-side web app's
queries are not visible in any release. Two things I can settle. First, the hub page's two
`cdn.sanity.io/files/….json` assets are **TopoJSON map geometry** (`type`, `arcs`, `transform`,
`objects`; 5.1 MB and 5.3 MB), not data series — so unlike the 81k page, this page publishes **no
chart values at all** and none can be matched to a release; the series come from an endpoint absent
from the server-rendered HTML. Second, **only `release_2025_09_15` and `release_2026_06_26` publish
an AUI**; the 2026-01-15 and 2026-03-24 folders publish none. So if the explorer shows a per-capita
index, its data cannot be the 2026-03-24 folder its dataset object is titled for — it must be the
June 2026 wave (or August 2025), which agrees with both the "Last updated: Jun 26, 2026" line and
the June zip in the hydrated `datasetDownloadURL`. Read the stale title as metadata, not as
provenance. I re-confirmed both `datasetDownloadURL` values and the title string on a fresh fetch.

**15. Nothing can show that, and the study cannot be extended to Claude.** Claude Code has no data
in the Index at all. For the 1P API the nearest measures are the global `collaboration` facet's
`directive` share and the `ai_autonomy` primitive — 66.30 (Aug 2025) → 63.58 (Nov 2025) → 58.22
(Feb 2026) → 80.88 (Apr 2026) → 82.75 (May 2026), and `ai_autonomy_mean` 2.84 → 2.69 → 2.27/2.24 —
but these are **global-only aggregate shares**, not behavioural sequences, and the RCT's "AI
Delegation" is a cluster of *within-session* interaction patterns on **n = 4** participants scored
against a comprehension quiz. The Index has no learning or skill outcome of any kind, so the
study's dependent variable does not exist in it. Two further blocks: the RCT's assistant was
**GPT-4o, not Claude**, so nothing from it can be stated about Claude; and the nearest public
delegation measure on Claude Code is `supervision_intensity: fully_autonomous` (42.8%) in the
partner dataset, which is a different sample and construct. **Do not build a post on this bridge.**

**16. Confirmed, at value level: no coded field of any kind.** Three CSVs, **two columns each** —
`transcript_id`, `text` — and nothing else: workforce (1,000 × 2), creatives (125 × 2), scientists
(125 × 2), 1,250 rows total, 11.4 MB. `transcript_id` is a split-prefixed serial (`work_0000`,
`creativity_0000`, `science_0000`), unique in each file and carrying no information beyond the
split. `text` is a raw dialogue transcript, median ~8.8k characters (min 4,837, max 26,826), with
`Assistant:` turn markers present in all 1,250 rows and **no structured metadata block** — no
`Occupation:`, `Age:`, `Country:`, `Gender:`, `Industry:` or `Role:` field in any row. So your
file's central feasibility claim holds as written: **no occupation, discipline, demographic or
survey variable exists, and not one published percentage in that post is reproducible from the
public data**. Anything of that kind would have to be re-extracted from free text by a classifier,
which is new measurement on a 1,250-row convenience sample, not reproduction — and the post's
denominators are 80,508, which is not this file (`[IX §Sibling Anthropic datasets]`).

**17. Not mine — page material — but here is the arithmetic.** That asset is a page publication,
not release data: no Economic Index release carries respondent counts, country-level survey rates or
US-state survey rates, so there is nothing in `data/` for it to live in and I have recorded nothing.
On the statistics, for whatever you decide: at p = 0.5 the 95% CI half-width is ±17.9 pp at n = 30,
**±12.7 pp at n = 60**, ±9.8 pp at n = 100, ±6.9 pp at n = 200 and ±5.0 pp at n = 385. So the 60
units under 100 respondents cannot support any statement finer than "roughly half"; a ±10 pp claim
needs n ≥ 97 and a ±5 pp claim n ≥ 385. My suggestion, matching Anthropic's own practice rather
than inventing a rule: adopt **n ≥ 100**, which is exactly the floor Anthropic applies to US states
in the Index, print the interval beside every rate that clears it, and rank nothing below n = 385.
Add that 125 countries × 51 states is ~176 simultaneous comparisons, so an unadjusted "highest" or
"lowest" claim will find extremes in noise even above the floor. The related discrepancy your
appendix entry already records — regional N summing to 80,470 against a stated 80,508 — is a reason
to treat the asset's denominators as approximate.

**Files.** New sections in `data/releases/labor_market_impacts.md` (Q2, Q8),
`data/releases/INDEX.md` (Q4, Q6), `data/releases/release_2026_03_24.md` (Q12),
`data/releases/release_2026_06_26.md` (Q13), `data/releases/release_2025_09_15.md` (Q10),
`data/releases/release_2026_01_15.md` (Q11), and in `data/ATLAS.md`: a new trap on the 1P API
composition break at the June 2026 boundary (Q15's series is the evidence — global `directive`
jumps 58.22 → 80.88 across exactly the boundary where the documentation stops including Claude
Code, on one base, so **never run an API series across it**), the ψ comparison, the two AUI names,
cuts 26a and 26b, the partner-dataset cross structure, and dated-log entry (d).
