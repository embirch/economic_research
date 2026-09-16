# Data atlas — Anthropic Economic Index

The single document to read before proposing, briefing or running anything on the Economic Index
public data. It consolidates the seven per-release profiles in `data/releases/`; those files hold
the detail and the command for every fact. Nothing here is asserted from Anthropic's prose alone.

## How to use this atlas

**What it is.** A map of what exists, at what grain, under which conventions, with the traps and
the cuts that do **not** exist. It answers "can this question be asked of this data?" before a
brief is written, and "which specification reproduces the published number?" before an analysis
is run. It is not a substitute for the per-release file: every section below points at one.

**Layout of the data documentation.**

| file | what it holds |
|---|---|
| `data/releases/INDEX.md` | enumeration of every folder and file of the Hugging Face dataset, verbatim from the tree API, with byte sizes and seven repository-level discrepancies |
| `data/releases/<release>.md` | one profile per folder: `Files`, `Schema`, `Grains`, `Facets or categories`, `Metrics`, `Thresholds`, `Coverage counts`, `Reproduced published numbers`, `Cuts that do not exist`, `Traps`, `Verification`, `Dated log` |
| `data/fetch/<release>.py` | the download-and-checksum script for that folder |
| `data/ATLAS.md` (this file) | the cross-release view and the corrections to the `economic-index-data` skill |

**How facts are verified.** Every fact in a release file carries the command that produced it, in
that file's `Verification` section. This atlas cites them in square brackets:

- `[LMI]` = `labor_market_impacts.md` · `[R1]` = `release_2025_02_10.md` ·
  `[R2]` = `release_2025_03_27.md` · `[R3]` = `release_2025_09_15.md` ·
  `[R4]` = `release_2026_01_15.md` · `[R5]` = `release_2026_03_24.md` ·
  `[R6]` = `release_2026_06_26.md` · `[IX]` = `INDEX.md`.
- `[R3 §Metrics, V4]` = the section, then the numbered command in that file's `Verification`.
  `[R2 §Traps]` where the file's commands are inline rather than numbered.
- Facts re-verified in this session are marked **(re-run 2026-09-16)** and the command is in
  `## Dated log`.

Where Anthropic's report text and Anthropic's own code or file disagree, **both** are recorded —
the report's words are routinely looser than its code (see `## Conventions`).

**Rebuilding the cache.** From the repository root:

```bash
for r in labor_market_impacts release_2025_02_10 release_2025_03_27 release_2025_09_15 \
         release_2026_01_15 release_2026_03_24 release_2026_06_26; do python data/fetch/$r.py; done
```

Each script downloads every file of its folder to `data/cache/<release>/` keeping the folder's
internal path, skips files whose sha256 already matches (a rebuild is a no-op), writes
`CHECKSUMS.txt`, checks byte sizes against `data/releases/INDEX.md`, and converts CSV/TSV over
20 MB to a Parquet sibling read with `keep_default_na=False`. Raw files are never modified;
`data/cache/` and `*.parquet` are gitignored. Verify with
`(cd data/cache/<release> && sha256sum -c CHECKSUMS.txt)` — **from inside the cache directory**,
because the paths are relative to it `[R3 §Traps 21]`. Total: 80 files, ~633 MiB; the cache is
currently complete for all seven folders (CHECKSUMS.txt line counts 2/14/16/38/4/3/3).
Conventions for the scripts are in `data/fetch/README.md`.

**Revision.** Everything in this atlas is pinned to Hugging Face revision
**`2ea58ff75e4247d26810c37f10c179edc2466cac`** (`2ea58ff`), dataset `lastModified`
`2026-06-26T23:21:00.000Z` `[IX §Verification 5, 7]`. The `x-repo-commit` header was re-fetched
today and still returns `2ea58ff` (re-run 2026-09-16). If it ever differs, re-run the fetch
scripts: a hash mismatch fails loudly.

**Licence.** Data CC-BY (**no version given**), code MIT — the dataset card body and the
2025-02-10 folder README both say exactly this; the card's YAML front matter and the HF API
`cardData.license` say `mit` only `[IX §Discrepancies 2]`, `[R1 §Files, V2]`. Attribute Anthropic;
do not rely on the HF licence tag; do not write "CC-BY 4.0".

## Releases at a glance

| release | report it accompanies | data window | schema family | components | files (bytes) | code shipped | documentation shipped |
|---|---|---|---|---|---|---|---|
| `labor_market_impacts/` | *Labor market impacts of AI* (Massenkoff & McCrory), 5 Mar 2026 | undated in-file; usage layer = Aug + Nov 2025 waves `[LMI §Vintage]` | flat (2 CSVs, no long/wide) | derived occupation/task measures only | 2 (1,926,998) | none | **none** — no README, no data documentation |
| `release_2025_02_10` | 1st report, 10 Feb 2025; paper arXiv:2503.04761 | 2024-12-16 → 12-23 (~1M Claude.ai Free+Pro), stated only in the paper `[R1 §Files, V19]` | flat (global percentages) | Claude.ai; O\*NET/SOC/BLS/wage reference | 14 (5,239,526) | `plots.ipynb` (21 code cells, runs clean) | folder `README.md` |
| `release_2025_03_27` | 2nd report, 27 Mar 2025 | Feb–Mar 2025, 11 days after Sonnet 3.7 launch; window named only in the blog `[R2 §Facets]` | flat (global percentages + cluster TSV) | Claude.ai; O\*NET/SOC reference | 16 (10,308,805) | `v2_report_replication.ipynb` (16 cells, all outputs reproduce), `cluster_level_example_analysis.ipynb` | `README.md`, `cluster_level_data/README.md` |
| `release_2025_09_15` | 3rd report, 15 Sep 2025 | **2025-08-04 → 08-11** | **long** (`facet/level/variable/cluster_name`) | Claude.ai (raw + enriched), 1P API, reference files, Census BTOS input | 38 (60,997,757) | `code/`: 6 `.py` + 4 `.ipynb` — the only released library | `README.md`, `data_documentation.md` |
| `release_2026_01_15` | 4th report, 15 Jan 2026 | **2025-11-13 → 11-20** | long | Claude.ai raw, 1P API raw | 4 (141,659,531) | **none** | `data_documentation.md`, `aei_v4_appendix.pdf` (prompts) |
| `release_2026_03_24` | 5th report ("Learning curves"), 24 Mar 2026 | **2026-02-05 → 02-12** | long | Claude.ai raw, 1P API raw | 3 (147,262,094) | **none** | `data_documentation.md` |
| `release_2026_06_26` | 6th report ("Cadences"), 26 Jun 2026 | **April and May 2026** (two calendar months) | **wide** (`category_name/hierarchy_level/metric_id/node_*`) | Claude.ai (chat + Cowork), 1P API (excl. Claude Code) | 3 (296,464,545) | **none** | `data_documentation.md` |

Ordinals and report URLs are the dataset card's `[IX §Folders]`. Byte totals match the tree API
exactly; all seven fetch scripts re-verify them.

**Repository root (3 files, 8,344 bytes)** — profiled from `[IX §(root)]` plus a fresh fetch
today (re-run 2026-09-16):

- **`README.md` (the dataset card, 5,035 bytes)** lists the seven data folders, the six report
  URLs plus the labour-market report, the licence sentence, `econ-research@anthropic.com`, and
  BibTeX for releases 2–6 (none for the first release). Two defects: (i) its YAML declares one
  `config_name` only, `release_2026_01_15`, whose `raw_1p_api` split points at
  `release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv`, which
  **404s** — re-confirmed today; the file is under `release_2026_01_15/` `[IX §Discrepancies 1]`.
  (ii) the card has **nine** code fences: the sixth-release citation block is never closed, so the
  "### Fifth release" heading renders inside it. Consequence: five of the seven folders have no
  viewer config at all; always fetch by explicit path, never through `datasets`.
- **`.gitattributes` (3,299 bytes, 70 lines)** — LFS rules. Generic binary patterns plus
  `*.png`, and **per-release** CSV/XLSX/JSON/PDF rules for `release_2025_09_15`,
  `release_2026_01_15` and named files in `release_2026_03_24` and `release_2026_06_26`. The
  2025-02-10 and 2025-03-27 CSVs are **not** LFS, which is why only 40 of 83 files are pointers;
  the tree API's `size` is the content size for those 40 `[IX §Verification 4]`.
- **`.gitignore` (10 bytes)** — `.DS_Store`, and nothing else.

## Components

**Claude.ai.** Present in every release except `labor_market_impacts/`. Labelled
`platform_and_product = "Claude AI (Free and Pro)"` in 2025-09-15 and 2026-01-15,
`"Claude AI (Free, Pro, and Max)"` from 2026-03-24, and split into a separate file
(`aei_claude_ai_2026-06-26.csv`, "chat and Cowork") in 2026-06-26 `[R3 §Schema]`, `[R5 §Schema]`,
`[R6 §Files]`. **The 2026-01-15 label is wrong**: the sample is Free, Pro *and* Max, per the
appendix and Chapter 1 footnote 1 `[R4 §Traps 10]`. The unit is a conversation; occupation is
inferred from the task, never from the user `[R4 §Grains]`, `[R6 §Traps 15]`.

**First-party API.** Starts at 2025-09-15 and exists in every wave since, always in its own file
and **always global only** — no country, no state, no region, no per-capita anything
`[R3 §Cuts]`, `[R4 §Cuts 5]`, `[R5 §Cuts 6]`, `[R6 §Metrics]`. Unit is a prompt–response record
(2025-09-15 → 2026-03-24) `[R4 §Grains]`. It is the only place token and cost metrics exist, and
they are **indices re-based to mean 1.0**, never levels `[R3 §Facets]`, `[R4 §Facets, V14]`. The
March 2026 report says the API sample "includes data from Claude Code"; the June 2026 file says
its API data **excludes** Claude Code. Neither is separable in any file `[R5 §Facets]`,
`[R6 §Cuts 8]`.

**Labour-market files.** `labor_market_impacts/` is a separate, undated, unversioned folder of two
CSVs — `job_exposure.csv` (756 detailed SOC occupations × `observed_exposure`) and
`task_penetration.csv` (17,998 rows / 17,992 O\*NET task strings × `penetration`). No
documentation, no code, no date column, no geography, no time. It supports the 5 March 2026
labour-market report, **not** any of the six numbered Economic Index reports `[LMI §Vintage]`.

**Reference files.** Only three folders ship any: 2025-02-10 (`SOC_Structure.csv`,
`onet_task_statements.csv`, `bls_employment_may_2023.csv`, `wage_data.csv`), 2025-03-27
(byte-identical copies of the first two), and 2025-09-15 (`data/input/` + `data/intermediate/`:
O\*NET, SOC, ISO codes, IMF/BEA GDP, World Bank/Census working-age population, Census BTOS)
`[R1 §Files]`, `[R2 §Files]`, `[R3 §Files]`. **The 2026 releases ship none** — every population,
GDP, O\*NET or SOC join for the 2026 waves is an external join, usually from 2025-09-15
`[R4 §Files]`, `[R5 §Files]`, `[R6 §Cuts 12]`.

**Claude Code — stated plainly: there is no Claude Code data anywhere in the dataset.** No folder,
file, facet, variable, `metric_id`, `category_name` or column name mentions it, at revision
`2ea58ff` `[IX §Components]`, `[R4 §Facets, V15]`, `[R5 §Facets]`, `[R6 §Cuts 8, V15]`. The June
2026 file explicitly excludes it from the API aggregate. Any Claude Code claim in the reports
(the 0.37-point autonomy gap, the 54%-Opus figure, the April 2025 software-development report) is
log-level work with no public file behind it.

**Survey — stated plainly: there is no Anthropic survey data anywhere in the dataset.** The only
survey file in the whole repository is `release_2025_09_15/data/input/BTOS_National.xlsx`, the
**Census** Business Trends and Outlook Survey, used as the input to Figure 3.1 and never joined to
any Claude data `[R3 §Files]`, `[R3 §Cuts]`, `[R6 §Cuts 9]`. The June 2026 report's Chapter 3
(9,700 linked respondents) and the 2026 survey write-ups are unreleased.

## Which cuts exist at which grain

Three schema families. Detail per release in the linked file; below is what exists, not how it is
named.

### Family A — flat global (2025-02-10, 2025-03-27, and `labor_market_impacts/`)

No geography, no date column, no counts. One row per task / pattern / cluster / occupation.

| release | unit | metric | cross-tabs that exist | geography | time |
|---|---|---|---|---|---|
| 2025-02-10 | O\*NET task (3,514 rows incl. pseudo-task `none`); 6 collaboration patterns; 974 occupations and 22 SOC major groups **derived** through `onet_task_statements.csv` | `pct` (sums to exactly 100 incl. `none`) | **none** — no task × pattern, no occupation × pattern `[R1 §Cuts]` | none | none |
| 2025-03-27 | v1 and v2 task files (3,514 / 3,365); 6 patterns × 2 versions; 3,364 tasks × 5 patterns + `filtered`; 3,365 task thinking fractions; 630 level-0 clusters (→145 L1 →30 L2) | `pct`, ratios in [0,1], `percent_records`/`percent_users` | **task × collaboration (v2 only)**; cluster × collaboration; cluster × thinking. **No** thinking × collaboration at task level `[R2 §Cuts]` | none | v1 vs v2 only, and the two task lists are not a panel (733 v1-only, 584 v2-only) `[R2 §Coverage]` |
| `labor_market_impacts/` | 756 SOC occupations; 17,992 O\*NET tasks | `observed_exposure`, `penetration` | **none**; the two files share no key `[LMI §Grains]` | none (implicitly US) | none |

### Family B — long schema (2025-09-15, 2026-01-15, 2026-03-24)

Columns `geo_id, geography, date_start, date_end, platform_and_product, facet, level, variable,
cluster_name, value`. One row = one (geography, facet, level, variable, cluster) cell; the
nine-column key is unique with zero duplicates in every file `[R3 §Grains]`, `[R4 §Grains, V10]`,
`[R5 §Grains]`. **(re-run 2026-09-16: 0 duplicates on 136,845 enriched rows.)**

| facet family | 2025-09-15 (enriched Claude.ai) | 2026-01-15 | 2026-03-24 | 1P API (all three waves) |
|---|---|---|---|---|
| geography totals | `country`, `state_us` (`usage_count`, `usage_pct`, and enrichment: `usage_per_capita`, **AUI**, `usage_tier`, `working_age_pop`, `gdp_per_working_age_capita`) | `country`, `country-state` — counts and shares **only** | `country`, `country-state` — counts and shares only | none |
| task / request | `onet_task` (L0), `request` (L0/1/2) at global + country + state | same at global + country + country-state | same | global only |
| occupation | `soc_occupation` (enriched only) at global + country + state | **absent at every grain** | **absent at every grain** | none |
| collaboration | `collaboration` (7 patterns) everywhere; `collaboration_automation_augmentation` (enriched only) | `collaboration` everywhere; no bucket facet | same | global |
| primitives | none | `use_case`, `task_success`, `multitasking`, `human_only_ability` (categorical) and `human_only_time`, `human_with_ai_time`, `ai_autonomy`, `human_education_years`, `ai_education_years` (numeric, 8 statistics each) at all three grains; histograms **global only** | identical facet and variable sets to 2026-01-15 — nothing added or removed `[R5 §Facets]` | same, global only |
| intersections | `onet_task::collaboration`, `request::collaboration` — **GLOBAL ONLY** | ten `onet_task::*` and ten `request::*` — **GLOBAL ONLY** | same 20 — **GLOBAL ONLY** | the same plus `onet_task::{cost, prompt_tokens, completion_tokens}` and `request::` equivalents — global only |
| specialisation index | `*_pct_index` (enriched only) | none (documented but absent) | none | none |

Geographic coverage: 2025-09-15 = 200 countries + 51 US states (+`not_classified`);
2026-01-15 = 173 countries + 1,091 ISO-3166-2 units across 135 parents; 2026-03-24 = 176 countries
+ 1,256 units across 155 parents (`US-*` = 54, including GU/PR/VI) `[R3 §Coverage]`,
`[R4 §Grains, V11]`, `[R5 §Grains]`. **`country-state` is worldwide, not a US-state cut.**

Cell fill is thin and gets thinner as the taxonomy gets finer — the single most important
planning number in the long family:

| cut | 2025-09-15 (per thresholded country) | 2026-01-15 (per country) | 2026-03-24 (per country) |
|---|---|---|---|
| `onet_task` L0 | median 20 of 2,618; 112 of 115 countries | median 21 of 3,170; 117 units | median 18 of 3,260; 118 units (1.95% of cells) |
| `request` L0 | median 42 of 588; **only 70 of 115** | median 41 of 618; 74 units | median 39 of 621; **only 71 of 176** |
| `request` L1 | median 43 of 108; 109 countries | median 35 of 112; 121 units | median 39 of 104; 119 units |
| `request` L2 | median 25 of 26; 115 of 115 | median 20 of 24; 129 units | median 18 of 26; 134 units |
| `soc_occupation` | median 5 of 23 (country); state level unusable | facet absent | facet absent |

`[R3 §Coverage]`, `[R4 §Coverage, V23]`, `[R5 §Coverage]`. **Compare mixes at level 1 or 2, never
at level 0 below global.**

### Family C — wide schema (2026-06-26)

Columns `date_start, date_end, geo_id, geo_level, category_name, hierarchy_level, metric_id,
value, node_name, node_external_id`. Key
`(date_start, geo_id, category_name, hierarchy_level, metric_id, node_external_id)`, 0 duplicates
`[R6 §Grains]`. 53 metrics, the same 53 in both files. The availability rule, from the 40-block
matrix in `[R6 §Metrics]`:

| geo_level | `overall` | top of each ladder (`onet` L3 GWA, `request` L2 Major, `soc_occupation` L1) | below the top |
|---|---|---|---|
| `global` (1 id) | 52 metrics (all but `pct`) | **all 51** metrics (all but the two usage metrics) | **all 51** — the only grain where primitives/collaboration/artifacts exist below the top of a taxonomy |
| `country` (121 ids) | 52 metrics | 51 metrics, but **ragged**: 9,557 of 12,319 cells publish all 51, 2,568 publish `pct` alone, 194 publish 41–50 | `pct` only |
| `subregion` (652 ids) | 52 metrics (51 US states + DC also carry the AUI; `US-PR` never) | **`pct` only** | **`pct` only** |
| `1p_api` | global only, mirrors the global block exactly | | |

Two calendar months, total April→May unit recurrence (every April unit recurs in May; 7 countries
and 116 subregions are May-only) `[R6 §Coverage]`. **There is no crossed category at any grain** —
`category_name` has four values and none is a cross, so every two-way table in the report
(artifact × use case, artifact × autonomy, occupation × artifact) is absent `[R6 §Facets]`.

## Cuts that do not exist

Consolidated; each with the release it belongs to. "Does not exist" means: not a column, not a
value, not derivable from the released files.

**Geography**
1. No geography of any kind before 2025-09-15 — no country, state, region, city or language
   column in 2025-02-10, 2025-03-27 or `labor_market_impacts/` `[R1 §Cuts]`, `[R2 §Cuts]`,
   `[LMI §Cuts]`.
2. No geography at all in any 1P API file, any wave `[R3 §Cuts]`, `[R4 §Cuts 5]`, `[R5 §Cuts 6]`.
3. No sub-national geography outside the US in 2025-09-15, and none below the state `[R3 §Cuts]`.
4. No AUI for non-US subregions in 2026-06-26 (601 of 652), none for `US-PR`, none for the API
   `[R6 §Cuts 10]`.
5. No `state_us` facet after 2025-09-15; US states are a prefix filter on `country-state` /
   `subregion` `[R5 §Cuts 8]`.

**Time**
6. No date, week or month column in 2025-02-10, 2025-03-27 or `labor_market_impacts/`; the
   windows exist only in the paper/blog `[R1 §Cuts]`, `[R2 §Cuts]`, `[LMI §Cuts]`.
7. No time dimension *inside* any long-schema release: one seven-day window each. Every "change
   since" number needs a second folder `[R3 §Cuts]`, `[R4 §Cuts 6]`, `[R5 §Cuts 10]`.
8. No day, week or hour grain in 2026-06-26 — the entire cadences chapter (weekday/weekend,
   hourly profiles, the 14–16 April tax spike) rests on unreleased data `[R6 §Cuts 6]`.

**Crosses**
9. No cross-tabs at all in 2025-02-10 `[R1 §Cuts]`; no thinking × collaboration at task level in
   2025-03-27 `[R2 §Cuts]`; no `request` × `onet_task` cross in any release `[R3 §Cuts]`,
   `[R5 §Cuts 5]`.
10. All intersections are **global only** in 2025-09-15, 2026-01-15 and 2026-03-24 — no
    automation-by-task, use-case-by-task or primitive-by-task for any country or region
    `[R3 §Cuts]`, `[R4 §Cuts 2]`, `[R5 §Cuts 1]`.
11. 2026-06-26 has **no cross of any two categories and no cross of any two metrics**; there is no
    request-by-occupation cross at any grain `[R6 §Cuts 1, 2]`.
12. No `soc_occupation` × collaboration, × request or × token/cost cross, ever `[R3 §Cuts]`.

**Occupation**
13. No `soc_occupation` facet at any grain in 2026-01-15 and 2026-03-24 — occupational shares must
    be rebuilt through an external O\*NET→SOC join `[R4 §Cuts 1]`, `[R5 §Cuts 2]`.
14. 2025-09-15 state-level `soc_occupation` exists but is unusable as a mix (74.28% mean
    `not_classified`, 69.7% of cells absent) `[R3 §Coverage]`.
15. No task → occupation link and no time-on-task weights in `labor_market_impacts/`, so
    `observed_exposure` is not decomposable `[LMI §Cuts]`.

**Counts, denominators, uncertainty**
16. No counts of any kind in 2025-02-10, 2025-03-27 or `labor_market_impacts/`; percentages only,
    so no standard error, confidence interval or significance test `[R1 §Cuts]`, `[R2 §Cuts]`,
    `[LMI §Cuts]`.
17. **No count metric of any kind in 2026-06-26** — no conversation count, no denominator, no
    sample size, nothing to weight the two months with `[R6 §Thresholds]`.
18. No `usage_count` variable in any 1P API file `[R4 §Cuts 5, V24]`.
19. No `usage_count` or `usage_pct` at global level in 2025-09-15 — totals must be summed
    `[R3 §Cuts]`.
20. No confidence intervals on four of the five global numeric facets in 2026-03-24 (only
    `human_education_years` has them) `[R5 §Cuts 4]`; no histograms below global in any long wave
    `[R4 §Cuts 3]`, `[R5 §Cuts 3]`.
21. No suppression flag anywhere, in any release. Absent cells are absent rows; absent ≠ zero
    `[R3 §Traps 11]`, `[R4 §Thresholds]`, `[R5 §Traps]`, `[R6 §Thresholds]`.

**Derived quantities Anthropic publishes but does not ship**
22. No AUI, no population, no GDP, no usage tier, no `*_pct_index` in 2026-01-15 or 2026-03-24
    `[R4 §Cuts 4, V18]`, `[R5 §Cuts 7]`. `onet_task_pct_index` is documented in the 2026-01-15
    documentation and **absent from the file**.
23. No automation/augmentation bucket variable in 2026-01-15 or 2026-03-24 (it exists as a facet
    only in the 2025-09-15 enriched file and as a metric in 2026-06-26) `[R4 §Metrics]`.
24. No `not_classified` residual node at all in 2026-06-26 — the gap between a `pct` sum and 100
    mixes unclassified and suppressed and is not decomposable `[R6 §Cuts 5]`.
25. No request-hierarchy file after 2025-09-15, so the parent of a level-0 cluster is not
    recoverable from the later folders `[R4 §Cuts 8]`.

**Product, model, user, firm**
26. No model, product, plan, tier, user, account, firm, industry (NAICS), language or tenure
    column in any release `[R1 §Cuts]`, `[R2 §Cuts]`, `[R3 §Cuts]`, `[R4 §Cuts 6]`,
    `[R5 §Cuts 9]`, `[R6 §Cuts 7, 8]`.
27. No token, turn, extended-thinking, session-length or active-time field outside the API token
    indices; extended thinking exists only as the 2025-03-27 per-task fraction `[R6 §Cuts 7]`,
    `[R2 §Facets]`.
28. No demographics anywhere `[R1 §Cuts]`, `[LMI §Cuts]`.

**Reference and external quantities**
29. No wages, employment, population, GDP or O\*NET/SOC reference file in 2026-01-15, 2026-03-24
    or 2026-06-26 `[R4 §Files]`, `[R5 §Files]`, `[R6 §Cuts 12]`.
30. No crosswalks in `labor_market_impacts/` (no SOC-2010, occ1990, ISCO, NAICS or CPS map), no
    β column, no alternative measures `[LMI §Cuts]`.
31. No cluster-level v1 in 2025-03-27, so no cluster change over time; and the cluster names carry
    no ids, so they cannot be matched to later request taxonomies `[R2 §Cuts]`.
32. No SOC 55 Military anywhere: absent from the 2025-02-10 task universe and explicitly excluded
    from the 2026-06-26 SOC major groups `[R1 §Facets]`, `[R6 §Facets]`.

## Conventions that reproduce published numbers

Each convention is the specification that reproduces the published figure, with the release file
section carrying the verifying command. **Where the report's prose and Anthropic's code disagree,
both readings are recorded.**

### The AI Usage Index

- **Countries (August 2025, the only wave where Anthropic publishes the index):**
  `AUI[g] = (usage[g] / U) / (pop[g] / P)` where `U` = usage over countries with
  `usage_count ≥ 200` **plus `not_classified`**, and `P` = working-age population over the
  thresholded countries only (`not_classified` has usage but no population row). Reproduced to
  **maxabsdiff 0.00000000** over 194 countries, USA 3.624352. The three rival denominators are off
  by 1.31, 0.20 and 1.54 index points `[R3 §Metrics, V4]`. **(re-run 2026-09-16: 0.00000000
  confirmed; thresholded-only 1.30622157.)**
- **US states:** thresholded states only, `not_classified` **excluded** from both numerator and
  denominator (maxabsdiff 0.000000; adding `not_classified` gives 0.000037) `[R4 §Reproduced,
  V25]`.
- **The released code disagrees with the released index.** `calculate_usage_per_capita_index` in
  `aei_report_v3_preprocessing_claude_ai.ipynb` takes the usage denominator over thresholded
  countries only; the published values match the `+not_classified` version. The mechanism is that
  the *notebook's* `get_filtered_geographies` keeps `not_classified` while the *library's* drops it
  `[R3 §Metrics]`, `[R3 §Traps 6]`.
- **June 2026 is different.** There is no `not_classified` row and `usage_pct` is already a share
  of the global total (it sums to 82.03 / 87.49). The specification that reproduces renormalises
  **both** numerator and denominator over the published set of that month: US states reproduce to
  mean |error| 0.0045/0.0048, all 51 within 0.05; countries reproduce in form but not in level
  (mean |error| 0.033, and ~1% uniform level error because the population denominator is a later,
  wider vintage). Applying the August asymmetric rule here introduces a uniform ~8% level error
  `[R6 §Reproduced]`. **Country AUI ranks, ratios and month-to-month changes reproduce exactly;
  absolute country levels do not.**
- Rebuilding for a wave that ships no AUI: population is
  `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` (World Bank
  SP.POP.1564.TO 2024 + Taiwan) and `…_us_state.csv` (Census SC-EST2024, ages 15–64, `SEX==0`)
  `[R5 §Reproduced]`. Print the merge audit: for Feb 2026, 178 country rows in, 170 matched,
  8 unmatched (`not_classified`, `NONE`, GF, GG, GP, JE, MQ, RE); 54 `US-*` in, 51 matched.

### Automation and augmentation — the base changes by wave *and* by chapter

| wave | published figure | base that reproduces it | file variable, if any |
|---|---|---|---|
| 2025-02-10 | 43% automation / 57% augmentation | ÷ the **five classified patterns** (81.30793074392103), i.e. drop `none`; the file sums to 84.209, not 100 | none — derive `[R1 §Metrics, V7, V13]` |
| 2025-03-27 | 57% augmentation (v2), v1 restated as 57/43 | same five-pattern rule on each version file; v1 sums to 84.209, v2 to 99.9965 | none `[R2 §Metrics]` |
| 2025-09-15, enriched variable | `automation_pct` = 51.0698 global | five classified patterns (`none` and `not_classified` excluded) | `collaboration_automation_augmentation` facet `[R3 §Metrics]` |
| 2025-09-15, **report headline** | 49% Claude.ai; 77% / 12% API | **all seven patterns**, including `none` **and** `not_classified` → 49.0980, 77.3723, 12.4146 | — `[R3 §Traps 2]` |
| 2026-01-15 | automation 45%, augmentation 52%, "neither" 3.0% | **all conversations**; `collaboration_pct` sums to 100 and the two shares to 97.04. The classified base gives 46.74 and matches nothing | — `[R4 §Reproduced]`, `[R4 §Traps 3]` |
| 2026-03-24 | automation 44%, augmentation 53% (Fig 1.3) | **all conversations** → 44.1569 / 52.7941 (sum 96.95). Five-pattern base gives 45.55 / 54.45 ✗ | — `[R5 §Reproduced]` |
| 2026-06-26 | the `collaboration_bucket_automation_pct` column | **five classified patterns**, `none` excluded — confirmed to rounding over 21,809 cells (mean abs error 0.0035); the six-pattern base is off by 2.02 on average | `collaboration_bucket_automation_pct` `[R6 §Metrics]` |

**(re-run 2026-09-16: 2025-02-10 42.553753 on the five-pattern base; 2025-03-27 v1 42.5538 /
v2 43.0619; 2026-01-15 all-conversation automation 45.3554 vs classified 46.7394; 2026-03-24
44.1569 / 52.7941; 2026-06-26 five-pattern identity mean |err| 0.00345, six-pattern 2.018.)**
**Say which base you are on, every time, and re-check it every wave.**

### Task mix and occupation allocation

- **`pct_occ_scaled` (2025-02-10, 2025-03-27):** a task's `pct` divided by the number of distinct
  occupation *Titles* holding it, then renormalised to 100 over matched rows. Any other choice
  (duplicating the full `pct`, or de-duplicating) fails to reproduce the published category
  shares `[R1 §Metrics, V7]`, `[R2 §Traps 4]`.
- **Task-mix adjustment (Figure 2.11, Aug 2025):** expected automation = the geography's
  `onet_task_pct` weights (dropping `none` and `not_classified`) × the global per-task automation
  rate from `onet_task::collaboration`; residualise both `automation_pct` and the AUI on expected
  automation and regress residual on residual. Anthropic's
  `collaboration_task_regression(df, geography="country")` returns slope **−3.111834**, R²
  **0.393687**, p 1.72e-13, **N = 111** — the published −3.112 / 0.394 / 111 exactly. At state
  level the sign flips (+2.728597, R² 0.184, N 44) `[R3 §Reproduced]`, `[R3 §Verification 5]`.
- **Chapter 1 renormalisation (Aug 2025):** the released change-over-time script drops
  `not_classified` and renormalises by ×1.0247; the report's **prose** quotes the
  un-renormalised numbers and the figure panels use the renormalised ones. Both are listed in
  `[R3 §Reproduced]`; quoting the script's output as the prose number turns 12.4% into 12.68%
  `[R3 §Traps 4]`.
- **Top-10 task concentration (Feb 2026):** drop `none` **and** `not_classified`, take the ten
  largest `onet_task_pct`, **do not renormalise** → 19.4410 ("19%"). Dropping only
  `not_classified` gives 22.49; renormalising gives 20.91 `[R5 §Reproduced]`. **(re-run
  2026-09-16: 19.4410.)**

### "Each 1% increase in the share of tech workers"

Means **one percentage point of share**, not a log-log elasticity. On the August 2025 file,
ln(AUI) on the Computer & Mathematical share in points gives 0.369 with R² 0.62, reproducing the
published 0.36; on the November 2025 file with an ACS C24010 workforce substitute it gives 0.3124
with R² 0.616 ("nearly two-thirds" reproduces, the slope does not — Anthropic used BLS OEWS, which
returns 403 to this sandbox). The log-log version is 1.05, R² 0.454, and matches nothing
`[R4 §Reproduced, V27]`.

### Gini conventions

- **State AUI Gini:** the **unweighted** Gini over the 51 state values (50 states + DC),
  including Wyoming. 0.366510 (Aug 2025), 0.3184 (Nov 2025), 0.2859 (Feb 2026) — published 0.37 /
  0.32 / 0.29. Dropping Wyoming gives 0.3095 and the population-weighted Lorenz version 0.2758;
  neither is the published figure `[R3 §Reproduced]`, `[R4 §Reproduced]`, `[R5 §Reproduced]`.
- **Country AUI Gini:** unweighted over countries at or above 200 conversations — 0.478117 (Aug,
  N 115), 0.5049 (Feb 2026, N 116); published 0.48 and 0.50 `[R5 §Reproduced]`.
- **Concentration shares are more fragile than the Gini:** the same rebuild that reproduces all
  three Feb-2026 Ginis lands 0.7–0.9 pp below the published top-20 country (47.27 vs 48%) and
  top-5/top-10 state shares. The cause is the unpublished population denominator, and no single
  vintage reproduces both `[R5 §Reproduced]`.
- **The Figure 3.4 Lorenz Gini (Aug 2025) is a different construct:** the released
  `create_platform_lorenz_curves` drops `none` and `not_classified` and returns 0.8225 / 0.8421;
  the published 0.84 / 0.86 come from keeping **all** `onet_task_pct` rows. The bottom-80% figures
  in the same chart use the released spec. Two numbers in one caption, two task universes
  `[R3 §Reproduced]`, `[R3 §Verification 8]`.

### Pooling the two months of June 2026

The report's Chapter 2 window is 10 April – 10 June 2026 and matches neither published month; the
files carry no counts, so there is **no way to weight them**. The specification that reproduces
the published artifact shares is the **unweighted mean of April and May**, stated as such: 6.79
(published "7%" as 93% produce an artifact), 16.66 ("17%"), 14.67 ("15%"), 10.39 ("11%") on
Claude.ai, and three of four on the API. The one 1.0 pp miss
(`artifact_data_or_spreadsheet_pct`, 12.99 vs 14) is a window mismatch on a fast-rising metric,
not a specification error `[R6 §Reproduced]`. **(re-run 2026-09-16: 6.790 / 16.660 / 14.665 /
10.390.)**

### The v1/v2 base difference

`automation_vs_augmentation_v1.csv` sums to **84.209233**, `_v2.csv` to **99.996500**. The v1
shortfall is the occupational-relevance filter the second report dropped. Always drop `none` and
renormalise over the five classified patterns before comparing versions; dividing v1 by 100 gives
34.60% automation against the comparable 42.55% `[R2 §Traps 2]`, `[R1 §Traps 2]`. The same trap
bites the Aug-2025 change-over-time script, which renormalises v1 internally `[R3 §Traps 14]`.
**(re-run 2026-09-16: 84.209233 / 99.996500.)**

### Blank thinking fractions are zero

In `task_thinking_fractions.csv` (2025-03-27), 2,950 of 3,365 cells are blank. Anthropic's
published extended-thinking figure reproduces to 0.02 pp mean error **only** with blank = 0 and
the full task set in the denominator, usage-weighted, restricted to occupations with
`pct_occ_scaled ≥ 0.5`. Dropping blanks gives up to 1.14 pp error and changes the ranking
`[R2 §Traps 3]`, `[R2 §Reproduced]`. **(re-run 2026-09-16: 2,950 of 3,365 blank.)**

### Other bases worth stating before use

- `usage_pct` at country level is a share of the **global** sample; at `country-state` /
  `subregion` it is a share of the **parent country** `[R4 §Metrics, V17]`, `[R6 §Coverage]`.
- Every `{facet}_pct` is a share of the geography's total **including `not_classified`**; every
  intersection `_pct` is a share of its **base cluster**, so summing it over a file gives
  ~325,900, not 100 `[R4 §Metrics]`, `[R5 §Traps 9]`.
- `*_pct_index` (Aug 2025) is the geography's raw `*_pct` over the parent's raw `*_pct`,
  **without renormalising the base**; renormalising first moves India's task indices by up to 0.17
  `[R3 §Traps 10]`.
- 2025-09-15 occupation shares: Chapter 1 quotes an all-conversation base and Chapter 2 a
  classified base; both reproduce, and the apparent contradiction between chapters (34% vs 36%
  Computer & Mathematical in Jan 2026) is two bases, not an error `[R4 §Traps 11]`.
- 2026-03-24 counts are on a **1,000,000 sample base**, not conversations: every global
  `{facet}_count` sums to exactly 1e6, so "200 per country" means 200 per million `[R5 §Metrics]`.

## Thresholds and suppression

Whether the public file applies the threshold, or you must, changes by release. **There is no
single rule.**

| release | applied before release | you must apply | evidence |
|---|---|---|---|
| 2025-02-10 | **Yes.** 5 unique accounts / 15 conversations per task, applied upstream; 3,513 of 18,428 tasks survive, no zero-`pct` rows, and the threshold **cannot be relaxed** because no counts are published | nothing (no geography exists) | `[R1 §Thresholds, V6, V19]` |
| 2025-03-27 | Cluster prevalence is **bucketed** (100 buckets, so `percent_records` has exactly 100 distinct values across 630 rows); collaboration/thinking cells are suppressed by blanks (178 of 630 rows); `filtered` is the task-level residual, published as a number | the report's figure screens: `min_prevalence = 0.5` for occupations and categories | `[R2 §Thresholds]` |
| 2025-09-15 | Privacy floor only: `onet_task_count`, `request_count` ≥ 15 (`collaboration_count` goes to 1); request *clusters* formed at ≥500 conversations / ≥250 accounts; `EXCLUDED_COUNTRIES` (23 ISO-3) absent | **200 conversations per country, 100 per US state.** 85 of 201 country rows and 79 of 194 AUI rows are below 200; `get_filtered_geographies` → 115 countries, 51 states | `[R3 §Thresholds, V3]`; **(re-run 2026-09-16: 115 thresholded, 85 below 200)** |
| 2026-01-15 | Privacy floor: base cells ≥15, request clusters ≥523 observed; intersections go down to 1 | **200 / 100** — the documentation states them and says they are "applied in enrichment step, not raw preprocessing". 55 of 174 country ids below 200 (min 15); 540 of 1,091 sub-national below 100 (min 1). Plus the report's **Seychelles** and **Wyoming** exclusions, which the file does not apply | `[R4 §Thresholds, V19–V22]`; **(re-run 2026-09-16: 174/55/15 and 1,091/540/1)** |
| 2026-03-24 | same privacy behaviour; the 23 excluded countries are already absent (re-applying the list is a no-op) | **200 / 100**, from the 2025-09-15 code — **this wave's documentation deletes the threshold sentence**; do not read its absence as "pre-filtered". 59 of 176 countries below 200; 680 of 1,256 regions below 100 | `[R5 §Thresholds]` |
| 2026-06-26 | **Yes, everything.** "A cell is only published if it meets both the aggregation thresholds and the geography sample floor… A missing row means the cell was not published, not necessarily that the value is zero." Neither value is stated | **nothing — and you cannot.** There is no count metric of any kind, so the 200/100 rule cannot be applied or checked. Any inclusion rule must be an observable proxy, stated as such | `[R6 §Thresholds]`; **(re-run 2026-09-16: zero count-like metric ids)** |
| `labor_market_impacts/` | **Yes.** The ≥100 work-usage gate is applied: 16,644 of 17,998 task rows (92.48%) are exactly 0. Capability gate (β = 0) also applied and indistinguishable | nothing; **do not apply another** | `[LMI §Thresholds, V11, V18]`; **(re-run 2026-09-16: 16,644 zeros, support {0} ∪ [0.5, 1])** |

**Suppression is always silent.** No release has a suppression flag or a count of suppressed
cells. An absent cell and a true zero are indistinguishable, except for the 28 population-padded
countries in the Aug-2025 enriched file `[R3 §Traps 11]`. In June 2026 the suppression is large
and systematic: median `pct` sums per unit-month are 36.9 (country `onet` L0) and 16.7 (subregion
`onet` L0), and country `usage_pct` sums to only 82.03 / 87.49 `[R6 §Thresholds]`.
**(re-run 2026-09-16: 82.03 / 87.49.)**

## Traps

Consolidated; each attributed. Read this list before writing a loader.

**Reading files**
1. **`NA` is Namibia** — but only where it bites. It bites the long files of 2025-09-15
   (22 rows nulled on a default read), 2026-01-15 and 2026-03-24 `[R3 §Traps 1]`,
   `[R4 §Traps 1, V11]`, `[R5 §Traps 1]`. **(re-run 2026-09-16: `NA` present and `NAM` absent in
   the Nov-2025 file.)** It does **not** bite `labor_market_impacts/` (no field is `NA`)
   `[LMI §Traps 10]`, 2025-02-10 or 2025-03-27 (no default-NA token but the empty string)
   `[R1 §Traps 10]`, `[R2 §Traps 15]`, or 2026-06-26, where Namibia is `NAM`/`NA-KH`
   `[R6 §Traps 14]`. Use `keep_default_na=False` everywhere regardless; it costs nothing.
2. **2026-03-24 also needs `na_values=[]`**: `geo_id` `NONE` is a real pseudo-geography and a
   default read nulls 3,672 `geo_id` values `[R5 §Traps 1]`.
3. **Anthropic's own `load_preprocessed_data` (1P API library) is a plain `pd.read_csv`** — the
   Claude.ai frame loaded through it is missing Namibia. Harmless for the API chapter, not
   harmless if reused for geography `[R3 §Traps 1]`.
4. **`resolve/main` 302-redirects to the CDN**; `curl` without `-L` returns a 325-byte stub with
   HTTP 200 and caches the wrong bytes silently `[R5 §Files]`.
5. **`cluster_name` is an empty string, not null**, on aggregate rows (48,730 in Nov 2025); a
   `dropna()` or default read breaks joins `[R4 §Traps 7]`.
6. **`level` is a string** in 2026-01-15 and `hierarchy_level` is a string in 2026-06-26 though
   documented as int `[R4 §Traps 8]`, `[R6 §Traps 2]`.
7. **Read the big files from Parquet.** The 219 MB June CSV costs ~8× its Parquet sibling
   `[R6 §Traps 16]`. (The skill's "files offloaded to iCloud stall loads" has no analogue here.)

**Units and scales**
8. **Hours versus minutes.** 2026-01-15: `human_only_time` is in **hours**, `human_with_ai_time`
   in **minutes** — a speedup is `hours × 60 ÷ minutes` `[R4 §Traps 2]`. 2026-03-24: **both** are
   in hours and the report prints minutes (3.0629 h × 60 = 183.77 min, the published figure)
   `[R5 §Traps 3]`. **(re-run 2026-09-16.)** 2026-06-26: `human_only_time_mean` hours,
   `human_with_ai_time_mean` minutes and the only metric exceeding 100 `[R6 §Metrics]`.
9. **`penetration` is not a share.** Its support is `{0} ∪ [0.5, 1]`; a positive value is the
   automation weight α, and 92.5% of the mass is at 0 `[LMI §Traps 3]`.
10. **`wage_data.MedianSalary` mixes hourly and annual** for six occupations; the released
    notebook's `MedianSalary > 100` filter removes them and 0.839 points of usage. `-1` is a
    missing-value sentinel in `JobZone` and `ChanceAuto` `[R1 §Traps 4, 5]`.
11. **`*_median_ci_lower` can be negative** and median CIs do not bracket the discrete median —
    never plot them as error bars `[R4 §Traps 6, V9]`, `[R5 §Traps 12]`.
12. **June 2026 `value` is pre-rounded to two decimals**, which is the binding constraint on every
    reconstruction: Iceland's `usage_pct` of 0.02 carries ±25% relative error `[R6 §Traps 8]`.

**Geographies and anomalies**
13. **Utah, August 2025.** Flagged by the report for possible coordinated abuse but **flagged
    nowhere in the data or the code**. Its `directive` share is 64.75% against a state median of
    37.08; `automation_pct` 73.40 against 48.16; its task-mix automation residual is +25.14 when
    the next largest is +4.19. Exclude by a stated rule and show it separately `[R3 §Traps 7]`.
    Utah is **not** anomalous in June 2026 (AUI 1.26 → 1.21, automation 51.5 → 51.9)
    `[R6 §Coverage]`.
14. **Seychelles, November 2025.** 24,715 conversations = 2.5% of the whole global sample, AUI
    1,054.638; excluded by the report from all geographic analyses, and **not** excluded in the
    file — so `usage_pct` and every global mix are contaminated unless you drop it
    `[R4 §Thresholds, V21, V22]`. SYC is not published at all in June 2026, so the "index > 25"
    rule is inert there `[R6 §Skill corrections]`.
15. **Wyoming, November 2025.** Excluded by the report from all US-state analyses for the same
    reason (AUI 2.073, third highest). Confirmed by replication: the published state education
    correlation reproduces at r = 0.9279, N = 50, i.e. 51 states less Wyoming — but the published
    state **Gini** of 0.32 is over all 51 **including** Wyoming `[R4 §Thresholds]`,
    `[R4 §Reproduced]`. Two different samples in one chapter.
16. **`US-PR` is both a subregion of `US` and a country (`PRI`)** in June 2026, so a union of
    country and subregion rows double-counts it; the 51 states + DC sum to 100.00 without it
    `[R6 §Traps 5]`. In Feb 2026 the US `country` row *excludes* PR/GU/VI while the `US-*` rows
    include them, so `usage_pct` over `US-*` sums to 100.284 `[R5 §Traps 5]`.
17. **`geo_id` code systems change within and between releases** — see `## Taxonomies`.
18. **`GLOBAL` identity rows** in June 2026 (`usage_pct` = 100.00, `usage_per_capita_index` =
    1.00) pollute any `geo_level`-agnostic aggregation `[R6 §Traps 6]`.

**Cells, keys and joins**
19. **`node_name` is not a key** in June 2026: 309 duplicate rows; always key on
    `node_external_id` `[R6 §Traps 3]`.
20. **`task_penetration.csv` is not unique on `task`** (17,998 rows, 17,992 strings; two strings
    appear four times). `drop_duplicates('task')` first `[LMI §Traps 1]`.
21. **Case-variant duplicate task strings exist** in O\*NET and in the labour-market file;
    lower-casing before a join silently creates a many-to-many match `[LMI §Traps 6]`.
22. **A metric's presence for one node says nothing about a sibling** (June 2026: 2,568 of 12,319
    country top-of-ladder cells publish `pct` alone). Pivot wide, check `notna()`, never
    `fillna(0)` `[R6 §Traps 7]`.
23. **`onet_task_mappings.csv` contains a pseudo-task `none`** that matches no O\*NET task and is
    inside the 100% denominator `[R1 §Traps 1]`, `[R2 §Traps 1]`.
24. **`none` and `not_classified` are different things.** `none` = the attribute is absent,
    `not_classified` = privacy-filtered or unclassifiable; the Feb-2026 top-10 figure needs both
    dropped `[R5 §Traps 7]`. Global `use_case` carries `not_classified` in Nov 2025 and `none` in
    Feb 2026 — do not hard-code either `[R5 §Traps 8]`.
25. **Absent ≠ zero** everywhere (see `## Thresholds and suppression`).

**Files that are the same file**
26. **Four files are byte-identical across releases.** `release_2025_02_10/onet_task_mappings.csv`
    = `release_2025_03_27/task_pct_v1.csv` = `release_2025_09_15/data/input/task_pct_v1.csv`
    (sha256 `8de89c99f762…`); `automation_vs_augmentation.csv` = both `…_v1.csv` copies
    (`d1e264882b17…`); `SOC_Structure.csv` = the March copy = `soc_structure_raw.csv`
    (`05eb5e689fb4…`); `onet_task_statements.csv` = the March copy (`82e4c418dc08…`)
    `[R1 §Files, V15]`, `[R2 §Files]`. **"v1" in a later folder *is* the February 2025 release** —
    December 2024, Claude 3.5 Sonnet — not an independent window.
27. **Running a released notebook in place overwrites the released PNGs.** Cells 17–19 of
    `v2_report_replication.ipynb` call `savefig` on exactly the three PNG names shipped in the
    folder. Run in a scratch directory with symlinks to the CSVs `[R2 §Traps 6]`. The Aug-2025
    change-over-time script likewise writes PNGs into `../data/output/figures/` in the cache
    `[R3 §Traps 13]`.
28. **The dataset card's `raw_1p_api` config path 404s** (it names the September folder for a
    November file). Anything loading through `datasets` or the viewer config fails
    `[IX §Discrepancies 1]`. **(re-run 2026-09-16: still 404.)**
29. **Licence wording.** The card body says "Data released under CC-BY, code released under MIT
    License"; the YAML and API say `mit`; the repo tags carry `license:mit` only. Cite the body,
    write "CC-BY" without a version `[IX §Discrepancies 2]`, `[R1 §Files, V2]`,
    `[R6 §Skill corrections]`.

**Code and documentation defects**
30. **Two different `get_filtered_geographies`** in the 2025-09-15 release — the library's drops
    `not_classified` (115 countries), the preprocessing notebook's does not (116). The AUI depends
    on the notebook's `[R3 §Traps 6]`.
31. **The 2025-09-15 library imports `geopandas` and `plotly` at module scope** and
    `load_world_shapefile()` downloads from `naciscdn.org` at call time; `load_onet_mappings()` and
    the change-over-time script hard-code `../data/…`, so you must `chdir` into `code/`
    `[R3 §Traps 12, 13]`.
32. **`plots.ipynb` cell 29 references `mcolors` without importing it** (survives only because it
    is called with RGB tuples) and its wage aggregation uses `agg('first')` for every non-grouped
    column `[R1 §Traps 11, 13]`. **`cluster_level_example_analysis.ipynb` cell 2 calls
    `display()`** and fails outside a kernel; both March notebooks declare a `Coconut` kernelspec
    and are ordinary Python `[R2 §Traps 7, 8]`.
33. **Anthropic's own documentation has errors**: the 2025-09-15 `README.md` names a
    `aei_report_v3_preprocessing_1p_api.ipynb` that does not exist; `data_documentation.md` names
    a population file with the wrong timestamp and omits two facets and the `geo_name` column
    `[R3 §Traps 16–18]`. The 2026-01-15 documentation describes `onet_task_pct_index`, which is
    absent from the file `[R4 §Metrics, V18]`. The 2025-03-27 README misnames the cluster folder
    and documents 3 of 8 columns `[R2 §Skill corrections]`.
34. **Cluster prevalence values are bucket averages** (2025-03-27): up to 7 clusters share a
    value, so ties are artefacts — no HHI, Gini or rank test that assumes distinct values
    `[R2 §Traps 11]`.
35. **`filtered` swamps rare tasks** (1,066 of 3,364 tasks are 100% filtered); weight by `pct`
    and renormalise out `filtered` `[R2 §Traps 12]`.

**Interpretation**
36. **Occupation is inferred from the task, not the user** — in every release. The June 2026
    appendix makes it explicit: "which Rust library is best for NLP?" maps to a *sales* occupation
    because the assistant is recommending products. Treat `soc_occupation` as a task taxonomy
    wearing occupation labels `[R6 §Traps 15]`, `[R2 §Traps 16]`.
37. **A zero in `job_exposure.csv` means "no measured exposure", never "no tasks used"**: 52
    occupations have exposure 0 while owning 1–10 positive-penetration tasks `[LMI §Traps 2]`.
38. **Cluster suppression is heavy at fine levels and the node count understates it.** Quote the
    `pct` sum, not the node count: a median country accounts for 55% of itself at June-2026
    `request` L0 `[R6 §Thresholds]`.
39. **Single-window distinctiveness at state level is largely noise.** Under "top 10 nodes by
    log(state share ÷ US share)", April→May recurrence across the 51 states averages 32.7%
    (`request` L1), 33.1% (`onet` L2), 19.8% (`soc` L0); under "top 10 by raw share" it is
    83–88%. Require persistence across independent windows and **state the specification**
    `[R6 §Skill corrections]`.
40. **Taxonomies change between waves** — see `## Taxonomies and identifiers`.

## Taxonomies and identifiers

**O\*NET and SOC**

| release | task universe | occupation codes | notes |
|---|---|---|---|
| 2025-02-10, 2025-03-27 | `onet_task_statements.csv`: 19,530 rows, 18,429 distinct task texts, 974 O\*NET-SOC codes; join key is the **lower-cased, stripped** task text | 10-char O\*NET-SOC 2019 (`11-1011.00`); `SOC_Structure.csv` is a **ragged** 2018 SOC hierarchy with 7-char codes | the two code systems do not join below the major group (687 of 775 base codes match) `[R1 §Traps 6]` |
| 2025-09-15 | `data/intermediate/onet_task_statements.csv` — **O\*NET DB 20.1**, 19,530 × 9 (adds `soc_major_group`) | same, plus `soc_structure.csv` | `soc_occupation` clusters are the 22 SOC major groups + `not_classified` `[R3 §Files]` |
| 2026-01-15, 2026-03-24 | task cluster names are lower-cased O\*NET task statements; **no reference file ships**. The 2026-01-15 join to the 2025-09-15 O\*NET file is clean (3,168/3,168; API 2,251/2,251) | none in-file | March 2026 report footnote 3 says it used **2019** O\*NET-SOC codes while every shipped crosswalk is the 2010 vintage — any SOC rebuild is an approximation `[R4 §Reproduced]`, `[R5 §Reproduced]` |
| 2026-06-26 | **O\*NET 30.2** (Feb 2026), with a rebuilt DWA-first classifier. `node_external_id` = O\*NET **Task ID** at L0 and O\*NET **element IDs** at L1/L2/L3 (DWA/IWA/GWA) | `soc_occupation` L0 = `##-####.##`, L1 = 2-digit major group (22 groups, **no 55 Military**) | only 2,258 of 2,861 Task IDs and 543 of 718 SOC codes join to the 2025-09-15 O\*NET file; **the DWA/IWA/GWA element ids join to nothing in the repository** `[R6 §Traps 13]` |
| `labor_market_impacts/` | **O\*NET 27.0–27.3** — a set-identical match on all 17,992 task strings, and all 756 titles match 27.2 exactly | 2018 SOC detail, 7 chars, no aggregates | the O\*NET file shipped inside the Economic Index releases is the **wrong vintage**: 15,682 of 17,992 tasks and 670 of 756 codes match. Download O\*NET 27.x `[LMI §Traps 4, V14]` |

**Request-cluster taxonomies are bottom-up and are NOT comparable across waves.**

| wave | levels and sizes (Claude.ai, global) | identifiers |
|---|---|---|
| 2025-03-27 | 630 level-0 → 145 level-1 → 30 level-2 (a strict tree) | **names only, no ids** — cannot be matched to any later taxonomy `[R2 §Cuts]` |
| 2025-09-15 | L0 **588** · L1 108 · L2 26 (API: 384/93/32); `level` 0 = finest | names; a `request_hierarchy_tree_*.json` ships |
| 2026-01-15 | 618 / 112 / 24 | names; **no hierarchy file** |
| 2026-03-24 | 621 / 104 / 26 | names; no hierarchy file |
| 2026-06-26 | 1,012 Detailed / 196 Minor / **20 Major**; `hierarchy_level` **0 = leaf, 2 = Major** | **UUID v5, release-specific**; the top level was replaced this wave, so nothing carries over `[R6 §Facets, §Cuts 14]` |

Never diff cluster sets across waves without an explicit name match and a report of the unmatched
names `[R5 §Traps 11]`. Within 2026-06-26, the two months also differ (global `onet` L0: 2,410 in
April, 2,713 in May) — restrict month-over-month comparisons to the intersection `[R6 §Traps 11]`.

**Level semantics.** In 2025-09-15 → 2026-03-24, `request` `level` **0 = finest, 2 = coarsest**.
In 2026-06-26, `hierarchy_level` **0 = leaf** and the top of each ladder is `onet` **3**,
`request` **2**, `soc_occupation` **1** `[R5 §Traps 16]`, `[R6 §Traps 1]`. `level` is 0 for every
non-request facet in the long family — do not join on it across facets `[R5 §Traps 13]`.

**Geographic identifiers.**

| release | country codes | sub-national codes |
|---|---|---|
| 2025-09-15 raw | ISO **3166-1 alpha-2** | USPS state codes (`CA`), facet `state_us` |
| 2025-09-15 enriched | ISO **3166-1 alpha-3** (+ `geo_name`) | USPS state codes |
| 2026-01-15 | ISO alpha-2, plus `not_classified` | ISO **3166-2** worldwide (`US-CA`, `AO-LUA`), plus `<ISO2>-not_classified` |
| 2026-03-24 | ISO alpha-2, plus `not_classified` and `NONE` | ISO 3166-2 worldwide, 1,256 regions / 155 parents; `US-*` = 54 incl. GU/PR/VI |
| 2026-06-26 | ISO **alpha-3** | ISO 3166-2 whose **prefix is alpha-2** — so `US-CA` does not join to `USA` without a crosswalk |

`[R3 §Traps 19]`, `[R4 §Schema]`, `[R5 §Grains]`, `[R6 §Traps 4, §Cuts 13]`. The cheapest bridge is
`release_2025_09_15/data/intermediate/iso_country_codes.csv` (252 rows, GeoNames) or
`working_age_pop_2024_country.csv`, which carries both `iso_alpha_3` and an ISO-2 `country_code`
for 194 countries. `census_state_codes.txt` (pipe-delimited FIPS/USPS) covers the US states.

## Released code

Only three folders ship code. **Reports 4, 5 and 6 ship none** `[IX §Discrepancies 4]`.

| folder | file | what it reproduces |
|---|---|---|
| 2025-02-10 | `plots.ipynb` — 30 cells, 21 code | the whole first report: the 22-category distribution (Computer & Mathematical 37.2249%), the BLS comparison, the 57.4/42.6 split and all five pattern shares. **Runs end to end with zero failures** on pandas 2.3.3 `[R1 §Reproduced, V14]` |
| 2025-03-27 | `v2_report_replication.ipynb` — 16 code cells, outputs stored; `cluster_level_data/cluster_level_example_analysis.ipynb` (illustrative, produces no published number) | **the only published replication notebook in the dataset**; every stored output reproduced exactly, nothing needed changing `[R2 §Reproduced]` |
| 2025-09-15 | `code/` — `aei_analysis_functions_claude_ai.py` (28 functions), `aei_analysis_functions_1p_api.py` (20), `aei_report_v3_change_over_time_claude_ai.py`, three analysis/preprocessing notebooks, four `preprocess_*.py` | the whole third report. Key entry points: `filter_df` (the workhorse), `get_filtered_geographies` (200/100), `filter_requests_by_threshold` (the "1% locally and 1% globally" rule), `collaboration_task_regression` (**Figure 2.11**), `plot_gdp_scatter` (the GDP elasticities), `create_platform_lorenz_curves`, `create_partial_regression_plot`, `calculate_usage_per_capita_index` (in the preprocessing notebook — **the AUI**). Constants: `MIN_OBSERVATIONS_COUNTRY = 200`, `MIN_OBSERVATIONS_US_STATE = 100`, `EXCLUDED_COUNTRIES` (23 ISO-3) `[R3 §Released code]` |

**This library is the specification of record for everything after it.** Replication of the 2026
waves re-implements from it plus each wave's `data_documentation.md`, and says which. Note that it
is written for the **long** schema: pointing it at the June 2026 wide files requires a
rename-and-reshape layer, and its `state_us` paths do not exist after August 2025
`[R6 §Files]`, `[R5 §Verification 6]`. Third-party requirements beyond pandas/numpy/statsmodels:
`geopandas`, `plotly`, `seaborn`, `openpyxl`.

## Corrections to the economic-index-data skill

The skill is the starting point; the files correct it in twenty places. Format: **skill statement
→ what the files show → reference.** *(The skill file belongs to another owner; this list is for
the director to route — nothing here edits it.)*

1. **"Thresholds are not applied in the public files."** → **False for three of the seven
   folders.** 2025-02-10 applies a 5-account / 15-conversation task threshold upstream and it
   cannot be undone; `labor_market_impacts/` applies a ≥100 work-usage gate that zeroes 92.48% of
   task rows; 2026-06-26 applies *all* thresholds and publishes no counts, so none can be applied
   or checked. It is true for 2025-09-15, 2026-01-15 and 2026-03-24. → `[R1 §Thresholds]`,
   `[LMI §Thresholds]`, `[R6 §Thresholds]`.
2. **"Automation share = (directive + feedback loop) ÷ (sum of the five classified patterns)."**
   → **Needs a wave-and-chapter qualifier.** Correct for 2025-02-10, 2025-03-27, the 2025-09-15
   *file variable* (51.07) and the 2026-06-26 bucket metric. Wrong for the 2025-09-15 *report
   headline* (49% / 77% / 12%, which use all seven patterns) and for the published 45% (Jan 2026)
   and 44% (Mar 2026), which use all conversations including `none`. → `[R3 §Traps 2]`,
   `[R4 §Traps 3]`, `[R5 §Skill corrections]`, `[R6 §Metrics]`.
3. **AUI: "usage over thresholded countries PLUS `not_classified`; population over thresholded
   countries only."** → Correct for August-2025 **countries**, now verified to 0.00000000 rather
   than five decimals — but (a) the **state** convention excludes `not_classified` from both,
   (b) Anthropic's own released function uses a different (wrong) usage denominator, and (c) the
   rule is **wrong for June 2026**, where both sides renormalise over the published set and the
   asymmetric version leaves a uniform ~8% level error. → `[R3 §Metrics]`, `[R4 §Traps 4]`,
   `[R6 §Skill corrections]`.
4. **"2025-02-10, 2025-03-27: … request clusters."** → **There are no request clusters in the
   2025-02-10 folder**; the 630-cluster bottom-up taxonomy lives in
   `release_2025_03_27/cluster_level_data/`. → `[R1 §Skill corrections]`.
5. **"`onet_task_statements.csv` (task → O\*NET-SOC code) lives in 2025-02-10."** → It lives in
   **both** 2025-02-10 and 2025-03-27, byte-identical (`82e4c418…`), with a re-derived 9-column
   version in 2025-09-15; and it is not a two-column mapping but 8 columns including `Task ID`,
   `Task Type`, `Incumbents Responding`, `Date`, `Domain Source`. → `[R2 §Skill corrections]`,
   `[R1 §Files, V15]`.
6. **2025-03-27 described as "automation/augmentation at global level".** → Understates it: the
   folder also ships **per-task** automation/augmentation, **per-task extended-thinking
   fractions**, a **630-cluster taxonomy** with per-cluster collaboration and thinking ratios, and
   **the only published replication notebook** in the dataset. → `[R2 §Skill corrections]`.
7. **The skill lists three functions for 2025-09-15.** → There are **28 + 20** library functions
   plus the change-over-time driver, two analysis notebooks, a preprocessing notebook and four
   preprocessing scripts. The skill's facet list is the **enriched** file's: `soc_occupation` and
   `collaboration_automation_augmentation` do not exist in the raw file, and the three API
   token/cost intersections are missing from the skill entirely. The raw Claude.ai file is
   **ISO-2**, the enriched one ISO-3. → `[R3 §Skill corrections]`.
8. **The 2026 primitive list.** → Omits **`ai_education_years`** (a sixth numeric primitive,
   present in both 2026 waves), the **twenty `onet_task::*` / `request::*` intersections**, and the
   API-only `onet_task::{cost, prompt_tokens, completion_tokens}` and `request::` equivalents. It
   also calls `task_success`, `use_case`, `multitasking` and `human_only_ability` "primitives" when
   they are categorical facets. → `[R4 §Skill corrections]`, `[R5 §Skill corrections]`.
9. **"No `soc_occupation` at state level" (2026-01-15, 2026-03-24).** → Understates it: there is
   **no `soc_occupation` facet at any level** in either wave. → `[R4 §Cuts 1]`, `[R5 §Cuts 2]`.
10. **"`geography` values `country`, `country-state` (ISO 3166-2 such as `US-CA`)."** → True but
    misleading: `country-state` is **ISO 3166-2 worldwide** — 1,091 units / 135 parents in Nov
    2025 and 1,256 / 155 in Feb 2026, of which the US is 54. There is no US-only file.
    → `[R5 §Skill corrections]`.
11. **Missing: counts are on a 1,000,000 sample base** in 2026-03-24 (every global `*_count` sums
    to exactly 1e6), so "200 conversations per country" means 200 per million; and **that wave's
    documentation deletes the threshold sentence** entirely. → `[R5 §Metrics, §Thresholds]`.
12. **Missing: hours versus minutes.** 2026-01-15 mixes hours (`human_only_time`) and minutes
    (`human_with_ai_time`) inside one facet family; 2026-03-24 has both in hours while the report
    prints minutes; 2026-06-26 mixes them again. → `[R4 §Traps 2]`, `[R5 §Traps 3]`,
    `[R6 §Metrics]`.
13. **"`NA` is Namibia: read every long file with `keep_default_na=False`."** → Correct for the
    three long waves, and **inapplicable** to `labor_market_impacts/`, 2025-02-10, 2025-03-27 and
    2026-06-26 (where Namibia is `NAM`/`NA-KH`). 2026-03-24 additionally needs `na_values=[]`
    because `NONE` is a real geography. → `[LMI §Traps 10]`, `[R5 §Traps 1]`, `[R6 §Traps 14]`.
14. **Seychelles / Utah exclusion rules.** → Wave-specific, and the skill omits **Wyoming**, which
    the January 2026 report excludes from all US-state analyses (while its published state Gini
    still includes it). Both the Seychelles and Utah rules are **inert in June 2026**. →
    `[R4 §Thresholds]`, `[R6 §Skill corrections]`.
15. **"Cluster suppression … per-country level-0 request clusters present: median 42 of 588."** →
    Correct for August 2025; the June-2026 equivalents are median 78 of 1,012 (country) and 20 of
    1,012 (subregion), and the better statistic is the `pct` sum (a median country accounts for
    55% of itself at `request` L0). → `[R6 §Thresholds]`.
16. **"Single-window distinctiveness is half noise at state level (April-to-May recurrence 45%)."**
    → **Not reproduced under any natural specification**, and the skill records none: 32.7%
    (`request` L1), 33.1% (`onet` L2), 19.8% (`soc` L0) by over-representation; 83–88% by raw
    share. Replace the number with a stated specification. → `[R6 §Skill corrections]`.
17. **Missing for 2025-03-27:** blank `thinking_fraction` must be treated as **zero** to reproduce
    the published figure; the 100-bucket privacy bucketing of cluster prevalence; the `filtered`
    residual; the ≥0.5% prevalence screen behind every published occupation figure; and that the
    released notebook **overwrites the shipped PNGs** when run in place. → `[R2 §Traps 3, 6, 11,
    12]`, `[R2 §Thresholds]`.
18. **Missing for 2026-06-26:** `GLOBAL` also carries a (trivial) AUI of 1.00, contradicting
    "countries and US states only"; publication inside the country "all metrics" block is
    **ragged** (2,568 of 12,319 cells publish `pct` alone); and the subregion `pct`-only rule is
    **stronger** than stated — it holds at the top of each ladder too. → `[R6 §Skill
    corrections]`.
19. **Licence "CC-BY 4.0".** → The card and the folder READMEs say "CC-BY" with **no version**;
    the YAML and API say `mit` only. → `[IX §Discrepancies 2]`.
20. **Missing entirely:** the `labor_market_impacts/` vintage (O\*NET 27.x task universe, usage
    layer = the August + November 2025 waves, supports the 5 March 2026 report and none of the six
    numbered ones), that `task_penetration.csv` is **not unique on its only key**, that
    `penetration`'s support is `{0} ∪ [0.5, 1]`, and that the folder has no documentation so the
    appendix PDF is the only specification. Also missing: the **four byte-identical files** across
    releases and the meaning of "v1"; the **dataset-card 404**; and that "files offloaded to
    iCloud stall loads" has no analogue here — the operative rule is to read the big files from
    the Parquet siblings. → `[LMI §Skill corrections]`, `[R1 §Traps 12]`, `[IX §Discrepancies 1]`,
    `[R6 §Traps 16]`.

## Supplementary sources

Only what the release files or the skill already establish. **No new supplementary research was
done in this thread**; anything not verified against a file is marked *unverified*.

**Shipped inside the dataset (CC-BY via the card; the underlying sources as noted).** These are
the cleanest joins available and should be preferred over re-fetching:

| source | file | keys | coverage | licence |
|---|---|---|---|---|
| World Bank SP.POP.1564.TO 2024 (+ Taiwan NDC) | `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` | `iso_alpha_3`, `country_code` (ISO-2) | 194 countries | World Bank CC-BY |
| Census SC-EST2024-AGESEX-CIV | `…/working_age_pop_2024_us_state.csv` | `state_code` | 51 (50 + DC) | public domain |
| IMF WEO NGDPD 2024 | `…/gdp_2024_country.csv` (raw JSON in `data/input/`) | `iso_alpha_3` | 174 countries | IMF terms |
| BEA SASUMMARY state GDP 2024 | `…/gdp_2024_us_state.csv` | `state_code` | 51 | public domain |
| GeoNames country info | `…/iso_country_codes.csv` | `iso_alpha_2` ↔ `iso_alpha_3` | 252 | CC-BY |
| Census state codes | `data/input/census_state_codes.txt` | FIPS ↔ USPS | 57 | public domain |
| O\*NET DB 20.1 task statements; SOC 2019 structure | `…/onet_task_statements.csv`, `…/soc_structure.csv` | `O*NET-SOC Code`, `Task ID`, task text | 19,530 rows / 974 occupations | O\*NET CC-BY |
| BLS employment by SOC major group, May 2023 | `release_2025_02_10/bls_employment_may_2023.csv` | major-group title | 22 groups, 151,853,870 jobs | public domain |
| O\*NET website wage scrape (Kilbourne-Quirk 2019) — **not** a BLS series | `release_2025_02_10/wage_data.csv` | `SOCcode` | 1,090 occupations | see folder README |
| Census Business Trends and Outlook Survey, national | `release_2025_09_15/data/input/BTOS_National.xlsx` | period codes (`202517`) | 6 sheets | public domain |

`[R3 §Files]`, `[R1 §Files]`. Every one of these is fetched by `data/fetch/release_2025_09_15.py`
or `…_2025_02_10.py` and is already in the cache.

**Fetched and verified during replication this session-day (recorded in the release files):**

- **O\*NET database text zips** — `https://www.onetcenter.org/dl_files/database/db_<v>_text.zip`,
  no key, CC BY 4.0. Required for `labor_market_impacts/` (27.x) because the shipped O\*NET file is
  the wrong vintage `[LMI §Verification V13, V14]`.
- **BLS Employment Projections** — `https://data.bls.gov/projections/occupationProj`, an HTML
  table, 831 detailed-SOC rows with employment 2025/2035, percent change and median annual wage;
  US Government work, public domain. Merge audit on `occ_code`: 756 in, **755 matched, 1
  unmatched (11-1031 Legislators)** `[LMI §Verification V20]`.
- **Census ACS table-based summary file** —
  `https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/1YRData/acsdt1y2023-c24010.dat`
  (200; cached at `data/cache/supplementary/`). Used as the workforce-share substitute for the
  tech-worker regression `[R4 §Verification V27]`.
- **World Bank API** —
  `https://api.worldbank.org/v2/country/all/indicator/SP.POP.1564.TO?format=json&date=YYYY&per_page=400`
  (200, 265 rows incl. aggregates, **no Taiwan**); **Census population estimates** —
  `https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/state/asrh/sc-est2025-agesex-civ.csv`
  (200 without a browser user agent) `[R5 §Verification 7]`.
- **Blocked from this sandbox:** `www.bls.gov` and `download.bls.gov` return **403** (OEWS zips,
  the ind-occ matrix), and `web.archive.org` is blocked by egress policy — so the BLS OEWS
  workforce shares and the 2024–34 projections vintage Anthropic used are **unobtainable here**
  `[LMI §Verification V21]`, `[R4 §Verification V27]`.
- **`cdn.sanity.io` (the report and appendix PDFs) is refused by `web_fetch` but retrievable with
  `curl`** `[R6 §Verification 17]`.

**Named in the skill, not verified here — treat as unverified leads:** Census
`PctUrbanRural_State.txt`; Microsoft AI Diffusion state and county CSVs
(`github.com/microsoft/ai-diffusion-report`); the OpenAI Signals CSV bundle
(`cdn.openai.com/signals/data-download-csv.zip`); the Census gazetteer (reported to block
non-browser downloads). None was fetched, joined or licence-checked in this thread.

## Dated log

- **2026-09-16 — first assembly.** Built from the seven release profiles written today
  (`data/releases/*.md`) plus `data/releases/INDEX.md`, at revision `2ea58ff`. The repository root
  was re-fetched and profiled (card 5,035 B, `.gitattributes` 3,299 B / 70 lines,
  `.gitignore` 10 B); two card defects recorded — the `raw_1p_api` config path still returns
  **404**, and the sixth-release citation block is an unterminated code fence, so "### Fifth
  release" renders inside it. Twenty corrections to the `economic-index-data` skill consolidated
  for the director to route.

  **Facts re-verified in this session, one per release** (all reproduced the release files
  exactly):

  ```bash
  # labor_market_impacts [LMI V9]  -> 16644 zeros, 0 in (0,0.5), min positive 0.5, 204 at 1.0, 4 at 0.5
  # release_2025_02_10  [R1 V6/V13] -> aa sum 84.209233, classified 81.30793074392,
  #                                    automation 42.553753 (five-pattern), 41.088 (incl none),
  #                                    34.600 (/100); task pct sums to 100.0000000000
  # release_2025_03_27  [R2 §Metrics] -> v1 total 84.209233 / automation 42.5538;
  #                                      v2 total 99.996500 / automation 43.0619;
  #                                      thinking blanks 2,950 of 3,365
  # release_2025_09_15  [R3 V4]     -> AUI denominators: thresholded+not_classified maxabsdiff
  #                                    0.00000000 (USA 3.624352); thresholded only 1.30622157;
  #                                    all incl nc 0.20364849; all ex nc 1.54147124;
  #                                    115 thresholded countries, 85 of 201 rows below 200;
  #                                    0 duplicates on the nine-column key (136,845 rows)
  # release_2026_01_15  [R4 V19]    -> 174 country ids, 55 below 200 (min 15); 1,091 sub-national,
  #                                    540 below 100 (min 1); automation 45.3554 on the
  #                                    all-conversation base vs 46.7394 classified; NA present,
  #                                    NAM absent
  # release_2026_03_24  [R5 §Reproduced] -> top-10 tasks 19.4410; automation 44.1569 /
  #                                    augmentation 52.7941 (sum 96.95); human_only_time_mean
  #                                    3.0629 h = 183.771 min
  # release_2026_06_26  [R6 §Metrics] -> bucket identity on the five classified patterns:
  #                                    mean |err| 0.00345, max 0.1245, 21,802 of 21,809 within
  #                                    0.05 (six-pattern base 2.018); artifact means 6.790 /
  #                                    16.660 / 14.665 / 10.390; 53 metric ids, none count-like;
  #                                    country usage_pct sums 82.03 (Apr) / 87.49 (May)
  ```

  Open questions carried forward: BLS OEWS and the 2024–34 projections vintage are unreachable
  (403), so two published numbers (the 0.36 tech-worker slope, the −0.6 pp BLS regression) stand
  reproduced only with substitutes; the June-2026 country AUI level cannot be rebuilt to better
  than ~1% because the population denominator is unpublished; the Eloundou et al. task-level β
  behind `labor_market_impacts/` was not obtained; and the skill's "45% April-to-May recurrence"
  has no recoverable specification.
