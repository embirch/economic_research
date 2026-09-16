---
name: economic-index-data
description: How the Anthropic Economic Index public releases are laid out, the conventions that reproduce Anthropic's published numbers, and the traps found so far. Read before loading any release or quoting any published number.
---

# Economic Index data: layout, conventions, traps

`data/ATLAS.md` is the authority; the per-release profiles in `data/releases/*.md` hold every
fact with the command that verified it. **This skill is the map, not the territory** — it tells
you what to look up and what will bite you. Never quote a number from here without opening the
release file it belongs to; every statement below was checked against the files on 2026-09-16 at
Hugging Face revision `2ea58ff`.

Source: Hugging Face dataset `Anthropic/EconomicIndex` — **seven data folders, 83 files, no
release after 2026-06-26**. Data licence **"CC-BY" with no version** in the card body; the YAML
and API say `mit` only. Never write "CC-BY 4.0"; attribute Anthropic. A second channel,
`economic-research.anthropic.com/releases/econ-index/release-<date>.zip`, mirrors the two most
recent waves **byte for byte** but is incomplete and its file names are release dates, not data
windows (`INDEX.md §Second distribution channel`). Fetch from Hugging Face by explicit path: the
card's one viewer config 404s, so `datasets` and the viewer are unusable.

Rebuild the cache (≈2 minutes, 633 MiB, idempotent, checksummed):

```bash
for r in labor_market_impacts release_2025_02_10 release_2025_03_27 release_2025_09_15 \
         release_2026_01_15 release_2026_03_24 release_2026_06_26; do python data/fetch/$r.py; done
python data/fetch/supplementary_anthropic.py   # the two sibling datasets and the mirror zips
```

## The seven folders, and what schema family each is in

| folder | report | window | family | notes |
|---|---|---|---|---|
| `release_2025_02_10` | 1st, Feb 2025 | Dec 2024, one week (stated only in the paper) | **A: flat global** | 3,514 O\*NET tasks, 6 collaboration patterns, occupations derived through `onet_task_statements.csv`; ships `plots.ipynb`, which runs clean |
| `release_2025_03_27` | 2nd, Mar 2025 | Feb–Mar 2025 | **A** | v1 **and** v2 task files, per-task automation, per-task extended-thinking fractions, a 630-cluster bottom-up taxonomy, and the dataset's **only replication notebook** |
| `release_2025_09_15` | 3rd, Sep 2025 | 4–11 Aug 2025 | **B: long** | raw **and** enriched Claude.ai, 1P API, reference files, Census BTOS; the **only released library** (`code/`, 28+20 functions) |
| `release_2026_01_15` | 4th, Jan 2026 | 13–20 Nov 2025 | **B** | adds the primitives; no code, no reference files |
| `release_2026_03_24` | 5th, Mar 2026 | 5–12 Feb 2026 | **B** | facet and variable sets **set-identical** to the January wave |
| `release_2026_06_26` | 6th, Jun 2026 | April and May 2026 (two calendar months) | **C: wide** | 53 metrics incl. artifacts and AUI; **no counts of any kind** |
| `labor_market_impacts/` | Massenkoff & McCrory, Mar 2026 | undated; usage layer = the Aug + Nov 2025 waves | **A** | `job_exposure.csv` (`occ_code, title, observed_exposure`, 756 SOC-2018 detailed) and `task_penetration.csv` (`task, penetration`, 17,998 rows); O\*NET **27.x** task universe; supports the 5 Mar 2026 report and **none of the six numbered reports**; no documentation, no code, no date, no geography — the appendix PDF is the only specification |

**Family B** columns: `geo_id, geography, date_start, date_end, platform_and_product, facet,
level, variable, cluster_name, value`. **Family C**: `date_start, date_end, geo_id, geo_level,
category_name, hierarchy_level, metric_id, value, node_name, node_external_id`. Keys are unique
in every file. Grain-by-grain availability: `ATLAS.md §Which cuts exist at which grain`.

The 2026 long waves carry **five numeric primitives** (`ai_autonomy`, `ai_education_years`,
`human_education_years`, `human_only_time`, `human_with_ai_time` — 8 statistics each, and each
also appearing as an `onet_task::` and a `request::` intersection), four **categorical** facets
often miscalled primitives (`use_case`, `task_success`, `multitasking`, `human_only_ability`) and
**twenty `onet_task::*` / `request::*` intersections**, global only; the API adds
`cost_index`, `prompt_tokens_index` and `completion_tokens_index`, which are **indices re-based to
mean 1.0, never levels**. In 2025-09-15, `soc_occupation` and
`collaboration_automation_augmentation` exist in the **enriched file only**, not the raw one.
`onet_task_statements.csv` is **8 columns,
not a two-column mapping**, and ships byte-identically in 2025-02-10 and 2025-03-27 with a
re-derived 9-column version in 2025-09-15. In June 2026 publication inside the country
"all metrics" block is **ragged** (2,568 of 12,319 top-of-ladder cells publish `pct` alone),
subregions are **`pct`-only even at the top of a ladder**, and `GLOBAL` carries a trivial AUI of
1.00.

## Before you assume a cut exists

The list that saves the most time is `ATLAS.md §Cuts that do not exist` (32 numbered items). The
ones briefs assume most often:

- **No geography at all** before 2025-09-15, in any 1P API file, or in `labor_market_impacts/`.
  1P API is **global only**, every wave.
- **No `soc_occupation` facet at any grain** in 2026-01-15 or 2026-03-24 (rebuild through an
  external O\*NET→SOC join); the August-2025 state-level one exists but is unusable (74%
  `not_classified`).
- **Intersections are global only** in the long family; 2026-06-26 has **no cross of any two
  categories or two metrics at any grain** — so no request-by-occupation, ever.
- **No time dimension inside a release.** Six windows in eighteen months with 2–5 month gaps;
  nothing covers 20–26 Jan 2026, and no unit-level identifier exists in any release, so
  "longitudinal" can only mean the series of cross-sections. **Comparison across waves is still
  possible** where a taxonomy survived — the collaboration facet is the one that did (see
  Conventions).
- **No counts in 2026-06-26**, no suppression flag anywhere, and **absent ≠ zero** everywhere.
- **No model, product, plan, user, account, firm, industry, language, tenure, turn, session or
  artifact field** — artifacts exist only as the 32 aggregate `artifact_*_pct` shares of
  2026-06-26.
- **No Claude Code and no Anthropic survey data in this dataset.** The only survey file anywhere
  is the **Census** BTOS input in 2025-09-15.
- **No emergent-task or research-field cut**; the nearest are the `Other / Unclear` request Major
  (0.4%) and the 57 detailed `19-*` science occupations in June 2026.

## Conventions that reproduce published numbers

Full table with the reproducing command per wave: `ATLAS.md §Conventions`. The rules:

- **Say which base you are on, every time; re-check it every wave.** Automation share is
  (directive + feedback loop) ÷ **the five classified patterns** for 2025-02-10, 2025-03-27, the
  2025-09-15 *file variable* and the 2026-06-26 bucket metric; ÷ **all seven patterns** for the
  2025-09-15 report headline (49% / 77% / 12%); ÷ **all conversations including `none`** for the
  published 45% (Jan 2026) and 44% (Mar 2026). The wrong base moves the answer by 1–8 points.
- **The collaboration facet is the one taxonomy that never changed**, so automation *is*
  comparable across waves once the base is fixed: the same six patterns run from 2025-02-10 to
  2026-06-26. The longest Claude.ai-global pair is **twelve months** — Feb–Mar 2025 → 5–12 Feb
  2026, 43.0619 → 45.5456 on the five-pattern base. State the five caveats in
  `ATLAS.md §Conventions` (the 2025 window is blog-dated only; Free+Pro → Free, Pro and Max; v2
  sums to 99.9965 and v1 is a different universe at 84.209; no counts, so no standard error;
  the June endpoint needs the pooling rule).
- **The AUI has three conventions.** August-2025 countries: usage over thresholded countries
  **plus `not_classified`**, population over thresholded countries only (reproduces to
  0.00000000). US states: `not_classified` excluded from both. **The 2026 long waves and June
  2026 are symmetric** — thresholded set only; Canada's published 4.4 reproduces as 4.4430 that
  way and 3.62 the other. Anthropic's own released function disagrees with its own published
  index. Ranks, Ginis and top-*N* shares are unaffected; levels are not.
- **Thresholds: there is no single rule.** 2025-02-10, `labor_market_impacts/` and 2026-06-26
  apply theirs **before release** (June's cannot even be checked — no counts). The three long
  waves do not: apply **200 conversations per country, 100 per US state** yourself, remembering
  that 2026-03-24 counts are per **million** and that its documentation deleted the threshold
  sentence. Add the reports' own exclusions (Seychelles and Wyoming in Nov 2025), which the files
  do not apply.
- **Ginis are unweighted** over the 51 state or the ≥200-conversation country values, Wyoming
  included. Concentration shares are more fragile than the Gini: no population vintage
  reproduces both.
- **"Each 1% increase in the share of tech workers" means one percentage point**, not a log-log
  elasticity.
- **June 2026 has two months and no weights**: the specification that reproduces the published
  artifact shares is the **unweighted mean of April and May**, stated as such.
- **Blank means zero** in the 2025-03-27 thinking fractions (2,950 of 3,365 cells). That folder
  also bucketes cluster prevalence into 100 privacy buckets (ties are artefacts), publishes
  `filtered` as the task-level residual (1,066 of 3,364 tasks are 100% filtered — weight by `pct`
  and renormalise it out), and every published occupation figure sits behind a **≥0.5% prevalence
  screen**.
- **`pct_occ_scaled`** divides a task's `pct` by the number of distinct occupation *Titles*
  holding it, then renormalises.
- Where the report's prose and Anthropic's code disagree, **record both** — the prose is
  routinely the looser one (Chapter 1 renormalisation, the Figure 3.4 Lorenz Gini).

## Traps

Full list, attributed: `ATLAS.md §Traps` (42 items). The ones that silently corrupt results:

**Reading.** `NA` is Namibia in the three long waves — read everything with
`keep_default_na=False`; 2026-03-24 also needs `na_values=[]` because `NONE` is a real
pseudo-geography. `cluster_name` is an empty string, not null. `level` and `hierarchy_level` are
strings though documented as int. Read the big files from the Parquet siblings the fetch scripts
write. `resolve/main` needs `curl -L` or you cache a 325-byte stub with HTTP 200.

**Identifiers.** In the August-2025 raw file **22 `geo_id` values are both an ISO-2 country and a
USPS state** (`DE` = Germany and Delaware, `CA` = Canada and California, `IN` = India and
Indiana) — always filter on `geography`. Code systems differ by file: ISO-2 raw, ISO-3 enriched,
ISO-3166-2 worldwide for `country-state` (**not** a US cut: 1,256 units / 155 parents in Feb
2026, of which 54 are US), ISO-3 countries with ISO-2 subregion prefixes in June 2026. `US-PR` is
both a subregion and a country; `GLOBAL` identity rows pollute level-agnostic aggregations;
`node_name` is not a key.

**Bases and units.** `usage_pct` at country level is a share of the global sample **including
`not_classified`** (this, not an error, is why India is 5.8% and not 5.96%); at `country-state`
and `subregion` it is a share of the **parent country**. `human_only_time` is hours and
`human_with_ai_time` minutes in 2026-01-15 and 2026-06-26, both hours in 2026-03-24 while the
report prints minutes. Intersection `_pct` is a share of its base cluster. `penetration` is not a
share (support `{0} ∪ [0.5, 1]`), and `task_penetration.csv` is **not unique on `task`**
(17,998 rows, 17,992 strings) — de-duplicate before joining, and never lower-case first, which
silently creates a many-to-many match. June 2026 values are pre-rounded to two decimals, the
binding constraint on any reconstruction. Median CIs can be negative and do not bracket the
median.

**Anomalies and suppression.** Utah Aug 2025 (flagged in the report, nowhere in the data),
Seychelles Nov 2025 (AUI 1,055; both rules inert in June 2026). Cluster suppression is heavy at
fine levels — **quote the `pct` sum, not the node count**, and compare mixes at level 1 or 2,
never at level 0 below global. Single-window distinctiveness at state level is largely noise
(April→May recurrence 32.7% by over-representation, 83–88% by raw share): require persistence
across independent windows and **state the specification**.

**Taxonomies.** Request clusters are bottom-up and **not comparable across waves** (names only,
no ids, until June 2026's release-specific UUIDs); `request` `level` is 0 = finest in the long
family, while in June 2026 `hierarchy_level` 0 = leaf. O\*NET vintages differ by folder (20.1,
27.x, 30.2) and `labor_market_impacts/` needs O\*NET 27.x, not the shipped file. Four files are
**byte-identical across releases**, so "v1" in a later folder *is* the February 2025 release.
Running a released notebook in place **overwrites the shipped PNGs**.

**Interpretation.** Occupation is inferred from the task, never from the user — a question about
a Rust NLP library maps to a *sales* occupation. Treat `soc_occupation` as a task taxonomy wearing
occupation labels.

## Replication and released code

Only three folders ship code: `plots.ipynb` (2025-02-10), `v2_report_replication.ipynb`
(2025-03-27) and the 2025-09-15 `code/` library. **That library is the specification of record for
every later wave** — reports 4, 5 and 6 ship nothing, so their numbers are re-implemented from it
plus each wave's `data_documentation.md`, and you say which. Its `state_us` paths do not exist
after August 2025 and it assumes the long schema. Anthropic's own documentation has errors (a
notebook that does not exist, a facet list missing two facets, a documented `onet_task_pct_index`
that is absent from the file). Reproduce the published number **before** extending it, state the
match to the decimal or the discrepancy and its cause, and print merge audits: rows in, rows
matched, unmatched names.

## Supplementary sources

Prefer the reference files **shipped inside 2025-09-15** (World Bank working-age population, IMF
and BEA GDP, GeoNames ISO codes, O\*NET 20.1, SOC structure, Census state codes) — the 2026
folders ship none, so every population, GDP or SOC join for a 2026 wave is external. Verified
keyless externals and the blocked ones (BLS 403, `web.archive.org` egress-blocked) are listed in
`ATLAS.md §Supplementary sources`, with two sibling Anthropic datasets:
`Anthropic/AnthropicInterviewer` (exactly **1,250** transcripts, `transcript_id` and `text` — the
80,508 interviews of the March 2026 feature are **not** released) and
`Anthropic/enabling-independent-research` (April–May 2026 partner cluster tables, CC-BY-4.0, the
only public Anthropic data with Claude Code fields and a `turn_count`).
