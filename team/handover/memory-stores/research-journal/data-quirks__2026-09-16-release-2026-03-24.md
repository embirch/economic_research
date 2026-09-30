# release_2026_03_24 profiling (keywords: 2026-03-24, learning curves, fifth report, AUI, Gini, automation share, primitives, ai_education_years, country-state, top 10 tasks)

Profiled 2026-09-16 by the steward thread for `release_2026_03_24`. Full note:
`data/releases/release_2026_03_24.md`; fetch script `data/fetch/release_2026_03_24.py`.

## Shape
- 3 files. `data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` 477,717 rows;
  `data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv` 195,156 rows. Same 10-column long schema as
  2025-09-15/2026-01-15: `geo_id, geography, date_start, date_end, platform_and_product, facet,
  level, variable, cluster_name, value`. Key
  `(geo_id, geography, facet, level, variable, cluster_name)` is unique in both files (0 dups).
- **Counts are scaled to a 1,000,000-conversation sample**, not raw conversations. Global
  `*_count` for every facet sums to exactly 1e6. So "200 conversations per country" is 200
  per million in these files.
- Geographies: `global`, `country` (ISO-2, 178 geo_ids incl. `not_classified` and `NONE`),
  `country-state` (ISO 3166-2, **1,256 regions across 155 countries, not just the US**;
  54 `US-*` incl. GU/PR/VI). No `state_us` facet any more.
- **No `soc_occupation` facet in this wave, at any geography.** No `collaboration_automation_augmentation`.
- **Nothing was added or removed versus 2026-01-15.** The facet set (34) and the variable set are
  identical in both waves' Claude.ai files; only row counts differ (458,778 → 477,717). The
  `economic-index-data` skill's primitive list for these waves is incomplete: it omits
  `ai_education_years` (present in BOTH waves) and the API-only indexed facets
  `onet_task::cost`, `onet_task::prompt_tokens`, `onet_task::completion_tokens` (variables
  `cost_index`, `prompt_tokens_index`, `completion_tokens_index`, 1.0 = average).
- What did change 2026-01-15 → 2026-03-24: `platform_and_product` "Claude AI (Free and Pro)" →
  "Claude AI (Free, Pro, and Max)"; the documentation drops the `onet_task_pct_index` entry, the
  `data/intermediate` path level, and — importantly — **the sentence stating the 200/100
  minimum-observation thresholds**; `use_case` at global carries `not_classified` in Nov and
  `none` in Feb.
- Nothing in any column names Claude Code, a model class, tenure, or a survey. The report's
  model-selection and learning-curve results are **log-level** work with no public file.

## Traps found
- `human_only_time` and `human_with_ai_time` are in **hours** in the file; the report's Table 1.1
  prints minutes. Global mean 3.0629 h × 60 = 183.77 min = the published figure exactly.
- The US `country` usage_count (222,372) **excludes** PR/GU/VI, but the `US-*` `country-state`
  rows **include** them (sum 223,004 = 222,372 + 587 + 26 + 19). `usage_pct` for US-* therefore
  sums to 100.284, not 100.
- `country` usage_count sums to 989,313, not 1e6: ~1.07% of usage is in suppressed geographies.
- Global rows for `ai_autonomy`, `ai_education_years`, `human_only_time`, `human_with_ai_time`
  carry no `_mean_ci_*`/`_median_ci_*`; `human_education_years` does. CI rows are also missing
  for a handful of countries/regions (e.g. 171 of 177 for `human_only_time_mean_ci_lower`).

## Specifications that reproduce the published numbers
- **Top-10 O*NET task concentration**: drop cluster_names `none` AND `not_classified` from
  facet `onet_task` at global, take the 10 largest `onet_task_pct`, sum WITHOUT renormalising.
  Claude.ai 19.4410 → published 19%; 1P API 32.5729 → published 33%. Including `none` gives
  22.49 / 35.18 (wrong); renormalising gives 20.91 / 36.08 (wrong).
- **Automation / augmentation (Figure 1.3)**: denominator is ALL conversations including the
  `none` collaboration cluster, i.e. just sum `collaboration_pct`. Claude.ai automation
  44.1569 → 44%, augmentation 52.7941 → 53% (they sum to 96.95, not 100). **The
  economic-index-data skill is wrong for this wave**: dividing by the five classified patterns
  gives 45.55/54.45 and does not match the figure.
- **AUI / Lorenz / Gini**: unweighted Gini over the AUI values; countries thresholded at
  usage_count ≥ 200, US states at ≥ 100 (all 51 pass). Verified against Anthropic's own
  published `usage_per_capita_index` in the 2025-09-15 enriched file: Aug 2025 states
  Gini 0.3665 → published 0.37, top-5 AUI share 29.68% → published 30%; countries (N=115)
  Gini 0.4781 → published 0.48, top-20 share 45.33% → published 45%. Method confirmed.

## The AUI shortfall worth remembering
Rebuilt for Feb 2026 with the 2025-09-15 population files (World Bank SP.POP.1564.TO 2024 for
countries, Census sc-est2024 ages 15-64 for states):
- countries thr 200, N=116: Gini **0.5049** → published 0.50 ✓; top-20 share **47.27%** vs
  published 48% ✗.
- states N=51: Gini **0.2859** → published 0.29 ✓; top-5 **23.31%** vs 24% ✗; top-10 **37.08%**
  vs 38% ✗.
Tried and rejected: World Bank 2025 population (countries Gini 0.5078 → 0.51 ✗, top20 47.75 ✓);
Census 2025 (no change); all-ages state population (top5 24.49 ✓, top10 38.29 ✓ but Gini
0.3001 → 0.30 ✗). No single vintage reproduces both the Gini and the top-N shares. The release
ships **no population file at all**, so the denominators Anthropic used are not public.

## Other reproductions (Claude.ai global, Feb 2026)
human_education_years mean 11.9187 → 11.92 ✓ · ai_autonomy 3.4067 → 3.41 ✓ ·
human_with_ai_time 14.3033 min → 14.30 ✓ · human_only_time 183.77 min → 183.77 ✓ ·
human_only_ability 'no' 12.2401% → 12.24 ✓ · use_case work 45.23/personal 42.29/coursework
12.44 → 45/42/12 ✓. API automation 67.63% (all-conversation base) / 79.75% (five-pattern base).
The whole Nov 2025 column of Table 1.1 also reproduces from the 2026-01-15 file (12.2051,
3.3818, 185.53 min, 15.3524, 12.0903) — which is how the published "+0.02" autonomy difference
is explained: 3.4067 − 3.3818 = 0.0249, not 0.03.
API top-10 tasks: Nov 32.1445 → 32%, Feb 32.5729 → 33%. API automation Nov 74.61% → Feb 67.63%
on the all-conversation base ("decreased sharply", Appendix Figure A.3 — its labels are raster,
not extractable text).

## Not reproducible from this release
Average task value ($49.3 → $47.9: needs BLS OEWS May 2024 wages + an O*NET task→SOC crosswalk,
neither shipped); SOC occupational-category shares (35% Computer & Mathematical, Management
3→5%: no soc_occupation facet, and the report uses **2019** O*NET-SOC codes while the shipped
crosswalks are 2010 vintage); everything in Chapter 2 (Opus share, tenure, success regressions).

## Sources used, all keyless
- HF LFS `oid` in the tree API **is the sha256 of the file content** — use it to verify downloads.
- `resolve/main` 302-redirects to the CDN: `curl` needs `-L` (without it you get a 325-byte stub
  and a silent wrong file). `requests` follows redirects by default.
- World Bank `api.worldbank.org/v2/country/all/indicator/SP.POP.1564.TO?format=json&date=YYYY&per_page=400`
  (no Taiwan; Anthropic patches Taiwan in from the national projection file).
- Census `www2.census.gov/programs-surveys/popest/datasets/2020-2025/state/asrh/sc-est2025-agesex-civ.csv`
  (200 without a browser UA); ages 15-64, SEX==0, drop NAME=="United States".
