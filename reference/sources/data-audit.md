# Anthropic Economic Index (Hugging Face `Anthropic/EconomicIndex`) — Data Audit

Audit date: 2026-09-07. Purpose: verify which columns, facets, metrics and geographies actually exist in each public release so research designs can be checked against real data, not against the reports' prose.
Local copies: `/Users/emilybirch/Desktop/Anthropic/bible/data/ei/<release>/` (docs in `data/ei/docs/`).
HF API used: `https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main/<dir>?recursive=true`; raw files at `https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/<path>`.

Findings are written incrementally; sections are numbered to match the audit brief.

---

## 1. Repository tree (every file, bytes)

Root: `.gitattributes` (3,299), `.gitignore` (10), `README.md` (5,035). Root README lists 7 releases and 6 reports (1st Feb 2025 ... 6th "Cadences" Jun 2026) plus a "Labor market impacts" folder. Root README's HF `configs` block points the `raw_1p_api` split at a wrong path (`release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv` — that file lives under `release_2026_01_15`), so the HF dataset viewer for that split is broken; irrelevant for direct downloads.

### labor_market_impacts/
| file | bytes |
|---|---|
| job_exposure.csv | 37,176 |
| task_penetration.csv | 1,889,822 |

### release_2025_02_10/ (1st report, Claude 3.5 Sonnet era, Clio)
| file | bytes |
|---|---|
| README.md | 2,981 |
| SOC_Structure.csv | 77,176 |
| automation_vs_augmentation.csv | 197 |
| bls_employment_may_2023.csv | 1,132 |
| onet_task_mappings.csv | 461,306 |
| onet_task_statements.csv | 3,592,256 |
| plots.ipynb | 25,886 |
| wage_data.csv | 128,047 |
| plots/*.png (6 files) | 38 KB–230 KB each |

### release_2025_03_27/ (2nd report, Claude 3.7 Sonnet)
| file | bytes |
|---|---|
| README.md | 3,205 |
| SOC_Structure.csv | 77,176 |
| automation_vs_augmentation_by_task.csv | 561,368 |
| automation_vs_augmentation_v1.csv | 197 |
| automation_vs_augmentation_v2.csv | 198 |
| cluster_level_data/README.md | 2,917 |
| cluster_level_data/cluster_level_dataset.tsv | 947,989 |
| cluster_level_data/cluster_level_example_analysis.ipynb | 280,733 |
| onet_task_statements.csv | 3,592,256 |
| task_pct_v1.csv | 461,306 |
| task_pct_v2.csv | 435,372 |
| task_thinking_fractions.csv | 372,332 |
| v2_report_replication.ipynb | 1,897,331 |
| 3 x .png | 150 KB–854 KB |

### release_2025_09_15/ (3rd report, geography + 1P API, Sonnet 4)
| file | bytes |
|---|---|
| README.md | 2,640 |
| data_documentation.md | 20,133 |
| code/aei_analysis_functions_1p_api.py | 76,365 |
| code/aei_analysis_functions_claude_ai.py | 92,526 |
| code/aei_report_v3_analysis_1p_api.ipynb | 8,079 |
| code/aei_report_v3_analysis_claude_ai.ipynb | 22,150 |
| code/aei_report_v3_change_over_time_claude_ai.py | 18,565 |
| code/aei_report_v3_preprocessing_claude_ai.ipynb | 85,914 |
| code/preprocess_gdp.py / preprocess_iso_codes.py / preprocess_onet.py / preprocess_population.py | 11,748 / 3,226 / 5,279 / 13,542 |
| data/input/BTOS_National.xlsx | 63,052 |
| data/input/Population by single age _20250903072924.csv | 2,176 |
| data/input/automation_vs_augmentation_v1.csv / _v2.csv | 197 / 198 |
| data/input/bea_us_state_gdp_2024.csv | 1,663 |
| data/input/census_state_codes.txt | 1,485 |
| data/input/geonames_countryInfo.txt | 31,667 |
| data/input/imf_gdp_raw_2024.json | 265,358 |
| data/input/onet_task_statements_raw.xlsx | 1,204,658 |
| data/input/sc-est2024-agesex-civ.csv | 818,707 |
| data/input/soc_structure_raw.csv | 77,176 |
| data/input/task_pct_v1.csv / task_pct_v2.csv | 461,306 / 435,372 |
| data/input/working_age_pop_2024_country_raw.csv | 22,974 |
| data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv | 7,027,019 |
| data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv | 18,894,517 |
| data/intermediate/gdp_2024_country.csv | 4,115 |
| data/intermediate/gdp_2024_us_state.csv | 2,179 |
| data/intermediate/iso_country_codes.csv | 4,564 |
| data/intermediate/onet_task_statements.csv | 3,650,862 |
| data/intermediate/soc_structure.csv | 78,834 |
| data/intermediate/working_age_pop_2024_country.csv | 6,321 |
| data/intermediate/working_age_pop_2024_us_state.csv | 1,079 |
| **data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv** | **26,840,881** |
| data/output/request_hierarchy_tree_1p_api.json | 302,699 |
| data/output/request_hierarchy_tree_claude_ai.json | 438,531 |

### release_2026_01_15/ (4th report, "economic primitives", Sonnet 4.5)
| file | bytes |
|---|---|
| aei_v4_appendix.pdf | 6,036,245 |
| data_documentation.md | 18,721 |
| data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv | 41,518,256 |
| **data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv** | **94,086,309** |

No enriched file, no code, no request-hierarchy JSON shipped in this release.

### release_2026_03_24/ (5th report, "learning curves", Opus 4.5/4.6)
| file | bytes |
|---|---|
| data_documentation.md | 17,739 |
| data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv | 43,957,174 |
| **data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv** | **103,287,181** |

No enriched file, no code, no JSON.

### release_2026_06_26/ (6th report, "Cadences": monthly aggregates, Artifacts)
| file | bytes |
|---|---|
| data_documentation.md | 7,397 |
| data/aei_1p_api_2026-06-26.csv | 77,282,477 |
| **data/aei_claude_ai_2026-06-26.csv** | **219,174,671** |

No file in the repository exceeds 400 MB; everything relevant was downloaded. Largest file: 219 MB (2026_06_26 Claude.ai).

---

## 2. Documented thresholds, schema notes and minimum-observation rules (from READMEs / data_documentation.md, quoted or closely paraphrased)

### 2025_02_10 README
- `automation_vs_augmentation.csv`: `interaction_type` (directive, feedback loop, task iteration, learning, validation), `pct`. "Data obtained using Clio."
- `onet_task_mappings.csv`: `task_name`, `pct` = "Percentage of conversations involving this task". Global only. No geography, no thresholds stated.

### 2025_03_27 README + cluster_level_data/README
- `automation_vs_augmentation_by_task.csv`: `task_name`, `directive`, `feedback_loop`, `validation`, `task_iteration`, `learning`, `filtered` (ratios 0-1). Global only.
- `automation_vs_augmentation_v1/v2.csv`: `interaction_type` includes `none`.
- `task_thinking_fractions.csv`: `task_name`, `thinking_fraction`.
- `cluster_level_dataset.tsv`: 3-level Clio hierarchy (`cluster_name_0/1/2`, `cluster_description_0/1/2`), `percent_records`, `percent_users`, `onet_task`, `collaboration:<pattern>_ratio` for directive / feedback loop / learning / none / task iteration / validation, `has_thinking_ratio`.
- **Bucketing adjustment**: `percent_records` and `percent_users` were sorted, split into 100 buckets, and each value replaced with its bucket average ("to reduce precision while maintaining the distribution"). So cluster prevalence is coarsened; not a threshold but a precision loss.

### 2025_09_15 data_documentation.md
- Long format: `geo_id`, `geography` ("country", "state_us", "global"), `date_start`, `date_end`, `platform_and_product` = "Claude AI (Free and Pro)", `facet`, `level` (0-2), `variable`, `cluster_name`, `value`.
- Facets documented: country, state_us, onet_task, collaboration, request, onet_task::collaboration, request::collaboration.
- Enrichment-only variables: `*_per_capita`, `*_per_capita_index`, `*_pct_index`, `*_tier`, `automation_pct`, `augmentation_pct`, `soc_pct`, `working_age_pop`, `gdp_per_working_age_capita`.
- `usage_per_capita_index`: "Concentration index showing if a geography has more/less usage than expected based on population share (1.0 = proportional)". `usage_tier`: 0 = no/little adoption, 1-4 = quartiles among geographies with sufficient usage.
- `automation_pct` = share of classifiable collaboration that is directive + feedback loop; `augmentation_pct` = validation + task iteration + learning.
- **Minimum observations: "200 conversations per country, 100 per US state (applied in enrichment step, not raw preprocessing)".**
- `not_classified` = filtered for privacy or unclassifiable; `none` = absence of attribute. Index calculations exclude `not_classified` and `none`.
- Country codes: ISO-2 in raw file, ISO-3 in enriched file.
- 1P API file: global only; extra facets onet_task::prompt_tokens / completion_tokens / cost (index, 1.0 = average).

### 2026_01_15 data_documentation.md
- Same long schema. `geography` values now "country", "country-state" (ISO 3166-2 subnational regions globally, e.g. "AGO-LUA", "US-CA"), "global". `platform_and_product` = "Claude AI (Free and Pro)".
- New content facets: multitasking, human_only_ability, use_case (work, coursework, personal), task_success. New numeric facets: human_only_time, human_with_ai_time, ai_autonomy, human_education_years, ai_education_years, each with `_mean`, `_median`, `_stdev`, `_mean_ci_lower/upper`, `_median_ci_lower/upper`, `_count`, `_histogram_count`, `_histogram_pct` (bin range in `cluster_name`). Intersections of onet_task and request with each of those.
- Doc mentions `onet_task_pct_index` but there is no enriched file in this release (checked empirically below).
- **Minimum observations: "200 conversations per country, 100 per country-state region (applied in enrichment step, not raw preprocessing)"** — but no enriched file was published, so the raw file is what exists; whether the threshold was applied is checked empirically below.
- "Some countries were excluded from region-level analysis due to mapping issues between source data codes and ISO 3166-2 standards. Country-level data remains available for all countries."
- Units for time facets are NOT stated in this documentation (only "Estimated time for a human to complete the task").

### 2026_03_24 data_documentation.md
- Identical schema and facets to 2026_01_15. `platform_and_product` = **"Claude AI (Free, Pro, and Max)"** (Max tier added).
- The "Minimum Observations" bullet was **removed** from the Data Processing Notes; no threshold is documented. `onet_task_pct_index` line was removed from the doc.
- Units for time facets still not stated.

### 2026_06_26 data_documentation.md (new wide schema)
- "aggregated by geography and analysis dimensions (categories) **on a calendar-month basis**. This release includes data for April and May 2026."
- Source files: `aei_claude_ai_<date>.csv` (`source_id` = claude_ai; "Claude chat and Cowork (Free, Pro, and Max plans)"; global, country, subregion) and `aei_1p_api_<date>.csv` ("Anthropic 1P API calls, excluding Claude Code"; global only).
- Columns: `date_start`, `date_end` (exclusive), `geo_id` (GLOBAL / ISO 3166-1 alpha-3 / ISO 3166-2), `geo_level` (global, country, subregion), `category_name`, `hierarchy_level`, `metric_id`, `value` (rounded to 2 dp), `node_name`, `node_external_id` (O*NET element ID, SOC code, or request-topic UUID).
- Categories: `overall`; `onet` (L0 Task, L1 DWA, L2 IWA, L3 GWA); `request` (L0 Detailed, L1 Minor, L2 Major); `soc_occupation` (L0 Detailed Occupation, L1 Major Group).
- **Metric availability matrix**: Global: all metrics for all categories. Country: `overall` gets all metrics; onet/request/soc get only `pct`, EXCEPT top level (GWA / Major / Major Group) which gets all metrics. Subregion: `overall` all metrics; onet/request/soc `pct` only. 1P API: global only.
- "A cell is only published if it meets both the aggregation thresholds and the geography sample floor... `usage_per_capita_index` at the subregion grain is published only for US states. A missing row means the cell was not published, not necessarily that the value is zero." Numeric threshold values are NOT stated.
- Metrics: `usage_pct`, `usage_per_capita_index` ("Anthropic Usage Index - Usage share divided by working-age (15-64) population share... Countries and US states only"), `pct`, `multitasking_pct`, `human_only_ability_pct`, `ai_autonomy_mean` (1-5 scale), `ai_education_years_mean`, `human_education_years_mean`, **`human_only_time_mean` (unit: hours)**, **`human_with_ai_time_mean` (unit: minutes)**, `use_case_work_pct`, `use_case_personal_pct`, `use_case_coursework_pct`, `collaboration_bucket_automation_pct`, `collaboration_bucket_augmentation_pct`, `collaboration_directive_pct`, `collaboration_feedback_loop_pct`, `collaboration_task_iteration_pct`, `collaboration_learning_pct`, `collaboration_validation_pct`, `collaboration_none_pct`, `artifact_{label}_pct` (32 labels incl. `none`, `other`).
- Collaboration patterns are collapsed into the two buckets exactly as in 2025_09_15 (automation = directive + feedback_loop; augmentation = task_iteration + learning + validation).

---

## 3. Empirical file profiles (pandas, `keep_default_na=False`)

**Trap for every long-format file (2025_09_15 raw, 2026_01_15, 2026_03_24):** country codes are ISO-2, so Namibia's code `NA` is silently parsed as NaN by pandas unless you pass `keep_default_na=False`. The 2025_09_15 *enriched* file and the 2026_06_26 file use ISO-3 and are safe.

### 3.1 release_2025_09_15 — `data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv`
- Shape **(136,845, 11)**. Columns: `geo_id` object, `geography` object, `date_start` object, `date_end` object, `platform_and_product` object, `facet` object, `level` int64, `variable` object, `cluster_name` object, `value` float64, `geo_name` object (the extra column vs raw). One week: 2025-08-04 to 2025-08-11. `platform_and_product` = "Claude AI (Free and Pro)". `level` in {0,1,2}.
- `geography`: `country` 80,541 rows / **201 distinct geo_id** (200 ISO-3 + `not_classified`; includes zero-usage countries added from the population file), `global` 29,681 rows / 1, `state_us` 26,623 rows / **52** (50 states + DC + `not_classified`).
- `facet` (rows): `request` 74,323; `onet_task` 33,195; `onet_task::collaboration` 14,454; `request::collaboration` 8,508; `collaboration` 3,026; `country` 1,352; `soc_occupation` 1,208; `collaboration_automation_augmentation` 420; `state_us` 359. (Note two facets not in the doc: `soc_occupation` and `collaboration_automation_augmentation`.)
- `variable` (rows): `request_pct` 25,173; `request_count` 25,173; `request_pct_index` 23,977; `onet_task_pct` 12,040; `onet_task_count` 12,040; `onet_task_pct_index` 9,115; `onet_task_collaboration_count` 7,227; `onet_task_collaboration_pct` 7,227; `request_collaboration_pct` 4,254; `request_collaboration_count` 4,254; `soc_pct` 1,208; `collaboration_pct` 1,112; `collaboration_count` 1,112; `collaboration_pct_index` 802; `usage_count` 253; `usage_pct` 253; `usage_tier` 245; `working_age_pop` 245; `usage_per_capita_index` 245; `usage_per_capita` 245; `gdp_per_working_age_capita` 225; `augmentation_pct` 210; `automation_pct` 210.
- Collaboration `cluster_name` values (note **spaces, not underscores**): `directive`, `feedback loop`, `learning`, `none`, `not_classified`, `task iteration`, `validation`. `collaboration_automation_augmentation` cluster_name: `automation`, `augmentation`. `onet_task::collaboration` cluster_name = `<task text>::<pattern>` with the same seven suffixes.
- Coverage (distinct geo_ids) by facet/variable:

| facet / variable | countries | US states | global |
|---|---|---|---|
| `collaboration` / `collaboration_pct` | **158** (directive 157, feedback loop 125, learning 130, task iteration 137, validation 95, none 81, not_classified 81) | **51** (directive 51, feedback loop 50, learning 51, task iteration 51, validation 44, none 36) | 1 |
| `collaboration` / `collaboration_pct_index` | 115 | 51 | — |
| `collaboration_automation_augmentation` / `automation_pct`, `augmentation_pct` | 158 | 51 | 1 |
| `onet_task::collaboration` (both variables) | **0 — GLOBAL ONLY** | 0 | 1 |
| `request::collaboration` (both variables) | **0 — GLOBAL ONLY** | 0 | 1 |
| `request` / `request_pct` L0 | 70 | 28 | 1 (588 clusters) |
| `request` / `request_pct` L1 | 111 | 45 | 1 (108 clusters) |
| `request` / `request_pct` L2 | 133 | 51 | 1 (26 clusters incl. not_classified) |
| `request` / `request_pct_index` (all levels) | 115 | 51 | — |
| `onet_task` / `onet_task_pct` | 114 | 47 | 1 (2,618 tasks) |
| `onet_task` / `onet_task_pct_index` | 111 | 44 | — |
| `soc_occupation` / `soc_pct` (22 SOC major groups + not_classified) | 112 | 47 | 1 |
| `country` / `usage_count`, `usage_pct` | 201 | — | — |
| `country` / `usage_per_capita`, `usage_per_capita_index`, `usage_tier`, `working_age_pop` | 194 | — | — |
| `country` / `gdp_per_working_age_capita` | 174 | — | — |
| `state_us` / `usage_count`, `usage_pct` | — | 52 | — |
| `state_us` / `usage_per_capita_index`, `usage_tier`, `working_age_pop`, `gdp_per_working_age_capita` | — | 51 | — |

- Cluster suppression is heavy at fine levels: per country, the number of L0 request clusters present has median 42 (min 2, max 585 of 588); O*NET tasks per country median 18 (max 1,256 of 2,618); per US state median 18 tasks.
- **Threshold reality check.** `usage_count` exists for 201 countries (min 0, max 208,200). Countries with usage_count >= 200: **116**; >= 100: 129. The 200/100 threshold is implemented in `code/aei_analysis_functions_claude_ai.py` (`MIN_OBSERVATIONS_COUNTRY = 200`, `MIN_OBSERVATIONS_US_STATE = 100`, function `get_filtered_geographies`, whose docstring says "The full dataframe is preserved") and only gates derived metrics. Empirically: `collaboration_pct` and `automation_pct` are published for 158 countries of which **43 have usage_count < 200** (min 29); `request_pct` for 133 countries incl. 18 below 200; `onet_task_pct` 114 incl. 2 below; `usage_per_capita_index` for 194 countries incl. **79 below 200** (e.g. ABW, AND, ASM, ATG, BDI ...). Only `*_pct_index` (115), `soc_pct` (112) and `usage_tier` quartiles respect the threshold. **Any country-level analysis on `*_pct` or `usage_per_capita_index` must re-apply `usage_count >= 200` by hand.** US states: 51 of 52 have usage_count >= 100 (the 52nd is `not_classified`, usage 2).
- `usage_tier` (country): 0 -> 28, 1 -> 53, 2 -> 40, 3 -> 36, 4 -> 37. Tier 0 = usage_count 0.
- `usage_per_capita_index` (country): n=194, mean 0.93, median 0.46, max 7.00. Top 10: ISR 7.00, MCO 4.93, SGP 4.57, AUS 4.10, NZL 4.05, KOR 3.73, USA 3.62, EST 3.11, LIE 3.08, IMN 3.05. US states top 5: DC 3.82, UT 3.78, CA 2.13, NY 1.58, VA 1.57.
- Relationship-advice cluster (matched by name): L1 **`Provide personal relationship advice and life guidance support`** — `request_pct` for **62 countries, 33 US states, global**; `request_pct_index` for the same 62/33. Its L2 parent `Provide personalized lifestyle advice and recommendations across relationships, spirituality, entertainment, beauty, and parenting` — 82 countries / 43 states. Its L0 children: `Provide personal advice for romantic relationship problems and conflicts` (30 countries / 10 states), `Help compose personal heartfelt messages for relationships and life events` (19/8), `Help draft and analyze personal text messages for relationships` (17/9), `Provide sexual health information and intimate relationship advice` (16/4). Top L1 request_pct: IRQ 2.01, GHA 1.64, GBR 1.59, SGP 1.54, CHE 1.53, ISR 1.47, JPN 1.46, GRC 1.46.
- Coding: L2 `Provide comprehensive software development assistance across multiple programming domains and technologies` = 18.53% global; present for **133 countries / 51 states**. `soc_pct` `Computer and Mathematical` = 35.88% global; 111 countries / 43 states.
- No gender/age/sex/demographic columns or cluster names (only O*NET task text such as "...age and gender" and one request cluster on sexual health).

### 3.2 release_2025_09_15 — `data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv`
- Shape **(100,062, 10)**; same columns minus `geo_name`. ISO-2 codes (`NA` trap). `country` 173 distinct (172 ISO-2 + not_classified), `state_us` 52, `global` 1.
- Facets only: `request` 50,346; `onet_task` 24,080; `onet_task::collaboration` 14,454; `request::collaboration` 8,508; `collaboration` 2,224; `country` 346; `state_us` 104. Variables only `*_count` / `*_pct` (12 variables). No index, tier, per-capita, GDP, population or SOC variables.
- Geography coverage identical to the enriched file for the raw pct variables (collaboration 158 countries / 51 states; request L2 133 / 51; onet_task 114 / 47; intersections global-only). usage_count: 173 countries, **116 >= 200**.

### 3.3 release_2025_09_15 — `data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv`
- Shape (33,794, 10). `geography` = `global` only. Facets: `onet_task::collaboration` 10,330; `request::collaboration` 5,990; `onet_task` 4,112; `onet_task::completion_tokens` / `::cost` / `::prompt_tokens` 4,110 each; `request` 1,018; `collaboration` 14. Variables: `collaboration_count/pct`, `completion_tokens_count/index`, `cost_count/index`, `onet_task_collaboration_count/pct`, `onet_task_count/pct`, `prompt_tokens_count/index`, `request_collaboration_count/pct`, `request_count/pct`. No geography.

### 3.4 release_2025_09_15 — `data/output/request_hierarchy_tree_claude_ai.json`
- A dict with one key `request_hierarchy` -> list of level-2 nodes; each node = `{level, cluster_name, cluster_description, children:[...]}` down to level 0. **No numeric node ids** — names are the only key; matching to the CSV is by exact `cluster_name` string. The relationship L1 node sits under the L2 "Provide personalized lifestyle advice..." node. `request_hierarchy_tree_1p_api.json` has the same structure for the API taxonomy.

### 3.5 release_2025_09_15 — enrichment inputs (`data/intermediate/`)
- `gdp_2024_country.csv` (174, 3): `iso_alpha_3`, `gdp_total`, `year`. `working_age_pop_2024_country.csv` (194, 5): `iso_alpha_3`, `year`, `working_age_pop`, `country_code` (ISO-2), `country_name`. `gdp_2024_us_state.csv` (51, 5): `state_code`, `state_name`, `gdp_total`, `gdp_millions`, `year`. `working_age_pop_2024_us_state.csv` (51, 3): `state`, `working_age_pop`, `state_code`. These are the only population/GDP tables in the whole repo and are what later releases lack; they can be re-used to rebuild AUI for 2026_01_15 / 2026_03_24.

### 3.6 release_2026_01_15 — `data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv`
- Shape **(458,778, 10)**; same 10 columns as the 2025_09_15 raw file (no `geo_name`); ISO-2 (`NA` trap). `platform_and_product` = "Claude AI (Free and Pro)". One week 2025-11-13 to 2025-11-20. `level` {0,1,2}.
- `geography`: `country` 64,510 rows / **174 distinct** (173 + not_classified); `country-state` 129,460 rows / **1,091 distinct** (ISO 3166-2 incl. `XX-not_classified` rows); `global` 264,808 rows. US states appear as `US-AK` ... `US-WY` incl. `US-DC`: **51**. There is no `state_us` geography any more.
- 33 facets: `request` 89,726; `onet_task` 35,510; `onet_task::human_only_time` 28,533; `onet_task::human_with_ai_time` 28,527; `onet_task::human_education_years` / `::ai_autonomy` / `::ai_education_years` 28,521 each; `onet_task::collaboration` 16,778; `onet_task::use_case` 13,908; `onet_task::multitasking` 11,830; `onet_task::task_success` 11,540; `onet_task::human_only_ability` 11,074; `human_only_time` 9,290; `human_with_ai_time` 9,290; `human_education_years` 9,282; `ai_education_years` 9,282; `ai_autonomy` 9,250; `collaboration` 8,850; `request::collaboration` 8,832; `use_case` 5,986; `request::human_only_time` 5,293; `request::human_with_ai_time` 5,263; `request::ai_autonomy` / `::ai_education_years` / `::human_education_years` 5,257 each; `request::use_case` 4,782; `multitasking` 4,450; `human_only_ability` 4,420; `task_success` 4,218; `request::task_success` 3,004; `request::human_only_ability` 3,002; `request::multitasking` 2,994; `country-state` 2,182; `country` 348.
- Variables: 100+ names. Core: `usage_count`, `usage_pct`, `request_count/pct`, `onet_task_count/pct`, `collaboration_count/pct`, `use_case_count/pct`, `multitasking_count/pct`, `human_only_ability_count/pct`, `task_success_count/pct`; numeric: `{human_only_time,human_with_ai_time,ai_autonomy,human_education_years,ai_education_years}_{mean,median,stdev,count,mean_ci_lower,mean_ci_upper,median_ci_lower,median_ci_upper,histogram_count,histogram_pct}`; intersections `onet_task_<x>_count/pct/mean/median/...` and `request_<x>_...`. **No `*_pct_index`, `usage_per_capita*`, `usage_tier`, `working_age_pop`, `gdp_*`, `soc_pct`, `automation_pct`, `augmentation_pct`** (grep for gdp/pop/index/tier/capita/soc returned nothing). The doc's mention of `onet_task_pct_index` is not backed by the file.
- **No threshold applied**: `usage_count` for 174 countries, min 15; **119 >= 200**, 130 >= 100. US states: 51, all >= 100 (min 199).
- Collaboration cluster_names unchanged (`directive`, `feedback loop`, `learning`, `none`, `not_classified`, `task iteration`, `validation`). `collaboration_pct` by country: directive 155, feedback loop 125, learning 132, task iteration 147, validation 103, none 90, not_classified 66. US states: 51 for directive/feedback loop/learning/task iteration, validation 49, none 44.
- `use_case` cluster_names: `coursework`, `not_classified`, `personal`, `work`. `use_case_pct` by country: **personal 150**, work 158, coursework 141, not_classified 68. US states: 51 each.
- `ai_autonomy_mean`: **173 countries**, 981 country-states, 51 US states, global = 3.38 (1-5 scale; global histogram: 1 -> 2.96%, 2 -> 16.25%, 3 -> 26.33%, 4 -> 48.57%, 5 -> 5.89%).
- `human_only_time_mean` global 3.09 (median 1.5), `human_with_ai_time_mean` global 15.35 (median 11.0), both for **173 countries**. Histogram bins run 0-~8,270 (width 330.8) for human_only_time and 0-~2,000 (width 80) for human_with_ai_time. Units are not stated in this release's doc; the values and ranges are consistent with the 2026_06_26 doc: **human_only_time in hours, human_with_ai_time in minutes** (global "3.1 hours without AI vs 15 minutes with AI").
- `human_education_years_mean` 12.21, `ai_education_years_mean` 12.20 (173 countries each).
- `multitasking` (`yes`/`no`/`not_classified`): yes 9.32% global, 171 countries. `human_only_ability`: yes 87.91%, 171 countries. `task_success`: yes 66.91%, 168 countries.
- **All intersections (`onet_task::*`, `request::*`) are GLOBAL ONLY** (checked: onet_task::collaboration, request::collaboration, onet_task::use_case, onet_task::ai_autonomy, onet_task::human_only_time).
- `request_pct` coverage: L0 74 countries / 166 country-states / 30 US states; L1 121 / 395 / 48; L2 129 / 564 / 51. Global clusters: L0 618, L1 112, L2 24. Per-country L0 clusters median 41.
- Relationship-type clusters (taxonomy re-generated; names differ from 2025_09_15): L1 **`Provide relationship, dating, parenting, and family advice`** 54 countries / 30 US states / 91 subnational; L1 `Draft and refine personal messages for relationships and life events` 50 / 33 / 99; L0 `Provide relationship advice and emotional support for romantic and family conflicts` 22 / 13; L0 `Analyze and provide advice on complex romantic relationship situations` 23 / 10.
- Coding: L2 `Help debug, develop, and optimize software across multiple programming domains` 14.80% global; **126 countries / 51 US states**.
- `onet_task_pct`: 3,170 tasks global; 117 countries (median 21 tasks per country).
- No demographic columns/values.

### 3.7 release_2026_01_15 — `data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv`
- Shape (187,772, 10); `geography` = `global` only; `platform_and_product` = "1P API"; 38 facets = the 33 Claude.ai facets minus the two geographic ones plus `onet_task::completion_tokens`, `onet_task::cost`, `onet_task::prompt_tokens`, `request::completion_tokens`, `request::cost`, `request::prompt_tokens`.

### 3.8 release_2026_03_24 — `data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv`
- Shape **(477,717, 10)**; same columns; ISO-2 (`NA` trap). **`platform_and_product` = "Claude AI (Free, Pro, and Max)"** (Max added). One week 2026-02-05 to 2026-02-12.
- `country` 62,486 rows / **178 distinct**; `country-state` 143,918 rows / **1,256 distinct**; `global` 271,313. US subregions **54**: 50 states + DC + `US-GU`, `US-PR`, `US-VI`.
- Same 33 facets and an **identical variable set** to 2026_01_15 (diffed: no additions, no removals). Values are rounded to 4 dp in this file (e.g. 90.1108) whereas 2026_01_15 carries full floats.
- **No threshold applied**: usage_count 178 countries, min 15; **119 >= 200**, 133 >= 100. US subregions: 54, 52 >= 100 (min 19: GU/VI).
- `collaboration_pct` by country: directive 154, feedback loop 127, learning 140, task iteration 150, validation 101, none 94. US: 52 for directive/feedback/learning/task iteration, validation 49, none 45.
- `use_case` cluster_names now include **`none`** (2 countries) in addition to coursework / not_classified / personal / work. `use_case_pct` by country: **personal 153**, work 162, coursework 132. US: 52 each.
- `ai_autonomy_mean`: **177 countries**, 1,137 country-states, 54 US; global 3.41. Histogram now 25 fixed-width bins (0.16) but mass is still on integers (1: 2.09%, 2: 14.68%, 3: 27.94%, 4: 51.03%, 5: 4.25%).
- `human_only_time_mean` global 3.06 (median 1.5); `human_with_ai_time_mean` 14.30 (median 10.0); 177 countries each. `human_education_years_mean` 11.92; `ai_education_years_mean` 12.03.
- `multitasking` yes 9.89% (176 countries); `human_only_ability` yes 87.76% (175); `task_success` yes 69.94% (170).
- Intersections: **GLOBAL ONLY** again.
- `request_pct` coverage: L0 71 countries / 178 country-states / 39 US; L1 119 / 418 / 51; L2 134 / 642 / 52. Global clusters L0 621, L1 104, L2 26. Per-country L0 median 39.
- Relationship-type clusters (taxonomy re-generated again): L1 **`Get relationship, dating, parenting, and personal advice across life situations`** 55 countries / 32 US states / 122 subnational; L0 `Analyze and provide advice on complex romantic relationship situations` 25 / 13; L0 `Get information and support for personal relationship challenges` 13 / 10.
- Coding: L2 `Assist with software development, debugging, and programming across multiple platforms` 16.84% global; **131 countries / 52 US**.
- `onet_task_pct`: 3,260 tasks global; 118 countries.
- No demographics.

### 3.9 release_2026_03_24 — `data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv`
- Shape (195,156, 10); global only; same 38 facets as 2026_01_15 API file.

### 3.10 release_2026_06_26 — `data/aei_claude_ai_2026-06-26.csv` (new wide schema)
- Shape **(1,636,573, 10)**. Columns: `date_start` object, `date_end` object, `geo_id` object, `geo_level` object, `category_name` object, `hierarchy_level` int64, `metric_id` object, `value` float64, `node_name` object, `node_external_id` object. ISO-3 codes (no `NA` trap). Values rounded to 2 dp (max 199.11).
- **Two calendar-month periods**: (`2026-04-01`, `2026-05-01`) 743,769 rows and (`2026-05-01`, `2026-06-01`) 892,804 rows. `date_end` is exclusive.
- `geo_level`: `country` 673,272 rows / **121 distinct** (114 in April, 121 in May, 114 in both); `global` 554,941; `subregion` 408,360 rows / **652 distinct**, of which **52 US** (50 states + DC + PR). Country list (May) is a curated set of 121 (e.g. AGO, ALB, ARE ... USA, UZB, VNM, ZAF, ZMB, ZWE) — no `not_classified`, no micro-states; this is the first release where a sample floor is applied *inside the file*.
- `category_name` / `hierarchy_level`: `overall` (L0 only, `node_name` = "Overall") 73,010 rows; `onet` L0-L3 744,544; `request` L0-L2 465,202; `soc_occupation` L0-L1 353,817. Global node counts: onet L0 **2,820** tasks, L1 750 DWAs, L2 211 IWAs, L3 **35** GWAs (with O*NET element ids e.g. `4.A.4.b.6`); request L0 **1,008**, L1 195, L2 **20** (UUID `node_external_id`); soc L0 **718** detailed occupations, L1 22 major groups (2-digit SOC in `node_external_id`).
- **53 `metric_id` values**: `usage_pct`, `usage_per_capita_index`, `pct`, `multitasking_pct`, `human_only_ability_pct`, `ai_autonomy_mean`, `ai_education_years_mean`, `human_education_years_mean`, `human_only_time_mean`, `human_with_ai_time_mean`, `use_case_work_pct`, `use_case_personal_pct`, `use_case_coursework_pct`, `collaboration_bucket_automation_pct`, `collaboration_bucket_augmentation_pct`, `collaboration_directive_pct`, `collaboration_feedback_loop_pct`, `collaboration_task_iteration_pct`, `collaboration_learning_pct`, `collaboration_validation_pct`, `collaboration_none_pct`, and 32 `artifact_<label>_pct`. Only means are published for numeric facets — no medians, CIs, stdev or histograms any more.
- Empirical availability (matches the doc's matrix):

| category / level | metric | countries (Apr / May) | US states | all subregions |
|---|---|---|---|---|
| `overall` | every metric incl. `collaboration_*_pct`, `use_case_personal_pct`, `ai_autonomy_mean`, `human_only_time_mean` | 114 / **121** | **52** | 652 |
| `overall` | `usage_per_capita_index` | 114 / 121 | **51** (no PR) | 51 (US states only) |
| `onet` L0-L2, `request` L0-L1, `soc_occupation` L0 | `pct` only | 121 | 52 (request L0: 51) | yes |
| `onet` L3 (GWA), `request` L2 (Major), `soc_occupation` L1 (Major Group) | all 53 metrics | **76 / 91** (sample floor) | 52 | `pct` only |
- Sparsity by country at fine levels (May): L0 request nodes per country median 84 (min 3, max 945 of 1,008); O*NET L0 tasks per country median 63 (max 1,607 of 2,820); per US state median 78 tasks and median 117 detailed occupations (max 460 of 718).
- **No parent-pointer column.** The file is flat; the hierarchy (which L0 belongs to which L1/L2) cannot be reconstructed from the file alone and no hierarchy JSON is shipped for this release. Only naming conventions ("Software development — other") hint at parents.
- Global levels (Apr / May): `ai_autonomy_mean` **2.72 / 2.74** (vs 3.38-3.41 in 2026_01/03); `human_only_time_mean` **4.59 / 4.73 hours** (vs 3.06-3.09); `human_with_ai_time_mean` **38.65 / 40.12 minutes** (vs 14.3-15.4); `use_case_personal_pct` 38.48 / 40.20; `use_case_work_pct` 45.53 / 43.36; `use_case_coursework_pct` 15.99 / 16.45; `collaboration_directive_pct` 31.72 / 31.38; `feedback_loop` 16.00 / 15.97; `task_iteration` 29.88 / 30.41; `learning` 16.75 / 16.55; `validation` 3.08 / 3.08; `none` 2.58 / 2.61; `collaboration_bucket_automation_pct` 48.98 / 48.62; `multitasking_pct` **22.29 / 22.92** (vs 9.3-9.9); `human_only_ability_pct` 87.79 / 87.62; `artifact_none_pct` 7.06 / 6.52.
- `usage_per_capita_index` top 8 countries (May): AUS 6.40, SGP 5.81, CHE 5.02, LUX 4.85, NZL 4.84, CAN 4.13, NOR 4.04, ISL 4.02.
- Relationship-advice: the request taxonomy is entirely new; **no node named "Provide personal relationship advice..." exists**. Closest matches: L2 **`Existential, Relational, and Emotional Support`** (`e509219a-676b-5523-a84f-1479ccedb49c`) 3.44% global, `pct` for **121 countries / 52 US states / 497 subregions** and all 53 metrics for 91 countries (it is a Major-level node); L1 **`Emotional Wellbeing and Support`** (`03e9b7f8-de59-51dc-81c5-9a5cbd61a966`) 2.23%, **119 countries / 50 US states / 422 subregions** (the same UUID also appears as an L0 node with 67 countries, i.e. a singleton branch); L1 `Companionship and conversation` (`439550ed-6ff5-55a7-924a-dc739b5521d1`) 1.37%, 111 countries / 49 US states; L1 `Personal messages` 0.39%; L1 `Self-reflection` 0.54%. L2 `Companionship & General Conversation` 1.37%, 111 / 49.
- Coding: request L2 **`Software Development`** (`f1286a7a-ec7b-55b6-b252-9606092d40cd`) 12.13 / 11.51% global; `soc_occupation` L1 **`Computer and Mathematical`** (id `15`) 23.95 / 23.80%; onet L3 **`Working with Computers`** (`4.A.3.b.1`) 9.48 / 9.40% — each with `pct` for 114 / 121 countries and 52 US states. Other coding-adjacent L2s: `DevOps & Infrastructure Operations` 2.82%, `Cybersecurity & Threat Detection` 0.38%.
- Global human_only_time_mean by O*NET task (May): 2,707 tasks with values, mean 5.15 h, median 4.43, max 29.56; by SOC detailed occupation: 717 occupations.
- No demographic metric_ids (a substring grep hit only `artifact_email_or_message_pct`, `artifact_image_or_graphic_pct`, `usage_pct`, `usage_per_capita_index` — false positives on "age").

### 3.11 release_2026_06_26 — `data/aei_1p_api_2026-06-26.csv`
- Shape (491,705, 10); `geo_level` = `global` only; same two monthly periods; same 53 metric_ids (set-identical to the Claude.ai file); categories onet 314,096, request 106,831, soc_occupation 70,674, overall 104. Doc: "excluding Claude Code".

### 3.12 Early releases and labor_market_impacts (global, no geography)
- `release_2025_02_10/automation_vs_augmentation.csv` (6, 2): `interaction_type`, `pct` — directive 22.56, feedback loop 12.04, learning 18.92, none 2.90, task iteration 25.48, validation 2.31. Identical to `release_2025_03_27/automation_vs_augmentation_v1.csv`.
- `release_2025_03_27/automation_vs_augmentation_v2.csv` (6, 2): directive 29.42, feedback loop 12.25, learning 27.08, none 3.24, task iteration 24.04, validation 3.97.
- `release_2025_02_10/onet_task_mappings.csv` = `release_2025_03_27/task_pct_v1.csv` (3,514, 2): `task_name` (lower-cased O*NET task text), `pct`. `task_pct_v2.csv` (3,365, 2).
- `release_2025_03_27/automation_vs_augmentation_by_task.csv` (3,364, 7): `task_name`, `feedback_loop`, `directive`, `task_iteration`, `validation`, `learning`, `filtered` (underscored names here; rows sum to 1.0).
- `release_2025_03_27/task_thinking_fractions.csv` (3,365, 2): `task_name`, `thinking_fraction` (object dtype: many blanks).
- `release_2025_03_27/cluster_level_dataset.tsv` (630, 16): `cluster_name_0/1/2`, `cluster_description_0/1/2`, `percent_records`, `percent_users`, `onet_task`, `collaboration:directive_ratio`, `collaboration:feedback loop_ratio`, `collaboration:learning_ratio`, `collaboration:none_ratio`, `collaboration:task iteration_ratio`, `collaboration:validation_ratio`, `has_thinking_ratio`. 630 L0 / 145 L1 / 30 L2 clusters; `percent_records` has exactly 100 distinct values (the documented bucketing). Several collaboration ratio columns are object dtype (blanks). Relationship clusters present, e.g. `Provide advice on managing personal and professional relationships`, `Help me navigate dating and romantic relationships`, `Guide me through relationship challenges and personal development`.
- `release_2025_02_10/wage_data.csv` (1,090, 10): `SOCcode`, `JobName`, `JobFamily`, `isBright`, `isGreen`, `JobZone`, `MedianSalary`, `JobForecast`, `ChanceAuto`, `WageGroup`. `bls_employment_may_2023.csv` (22, 2): `SOC or O*NET-SOC 2019 Title`, `bls_distribution`.
- `labor_market_impacts/job_exposure.csv` (756, 3): `occ_code` (6-digit SOC), `title`, `observed_exposure`. `task_penetration.csv` (17,998, 2): `task`, `penetration`. Both global, US-occupation-keyed.

---

## 4. Specific checks requested

| Question | Answer |
|---|---|
| `onet_task::collaboration` rows BY COUNTRY in 2025_09_15 and later? | **No.** In 2025_09_15 (raw and enriched), 2026_01_15 and 2026_03_24 the facet exists for `geography == global` only (1 geo_id). In 2026_06_26 the equivalent (`collaboration_*_pct` on `onet` nodes) exists by country **only at hierarchy_level 3 (35 GWAs)** for 76 (Apr) / 91 (May) countries and 52 US states; onet L0-L2 by country carry `pct` only. |
| `use_case_personal_pct` (or equivalent) by country in 2026_01_15 and 2026_06_26? | **Yes.** 2026_01_15: facet `use_case`, variable `use_case_pct`, `cluster_name == 'personal'` for **150 countries** (unthresholded; apply usage_count >= 200 -> ~119) and 51 US states. 2026_03_24: 153 countries / 52 US. 2026_06_26: `metric_id == 'use_case_personal_pct'`, `category_name == 'overall'` for **114 (Apr) / 121 (May) countries**, 52 US states, 652 subregions. Not available in 2025_09_15 (no use_case facet). |
| Per-pattern collaboration shares (directive etc.) by country in every release? | **Yes for all four geographic releases.** 2025_09_15: `collaboration` / `collaboration_pct` with cluster_name `directive` 157 countries (others 95-137), 51 states, plus `collaboration_pct_index` for 115. 2026_01_15: directive 155 countries / 51 US. 2026_03_24: directive 154 / 52. 2026_06_26: `collaboration_directive_pct` etc. at `overall` for 114/121 countries, 52 US states, 652 subregions. Naming differs: `feedback loop` / `task iteration` (space) in 2025-2026_03 vs `collaboration_feedback_loop_pct` / `collaboration_task_iteration_pct` in 2026_06. Not in 2025_02/2025_03 (global only). |
| Request cluster "Provide personal relationship advice and life guidance support" by country and at what level? | 2025_09_15: exact name exists at **level 1**; `request_pct` and `request_pct_index` for **62 countries and 33 US states** (of 115/51 thresholded). 2026_01_15: closest is L1 `Provide relationship, dating, parenting, and family advice` (54 countries / 30 US). 2026_03_24: L1 `Get relationship, dating, parenting, and personal advice across life situations` (55 / 32). 2026_06_26: no equivalent name; closest L1 `Emotional Wellbeing and Support` (119 / 50) or L2 `Existential, Relational, and Emotional Support` (121 / 52). Node ids: none before 2026_06_26 (JSON tree keyed by name); UUIDs only in 2026_06_26. |
| `gdp_per_working_age_capita` and `usage_per_capita_index` by country in each release? | 2025_09_15 enriched: **yes** — `gdp_per_working_age_capita` 174 countries / 51 states; `usage_per_capita_index` 194 countries / 51 states (unthresholded; 115 countries >= 200). 2026_01_15 and 2026_03_24: **neither exists** (no enrichment shipped; only `usage_count`/`usage_pct`). 2026_06_26: `usage_per_capita_index` **yes** (114/121 countries, 51 US states, global); `gdp_per_working_age_capita` **no** (no GDP anywhere in the file). GDP/population inputs exist only in `release_2025_09_15/data/intermediate/`. |
| Unit of `human_only_time_mean` / `human_with_ai_time_mean`? | Per the 2026_06_26 doc: **`human_only_time_mean` = hours; `human_with_ai_time_mean` = minutes** (asymmetric units). The 2026_01_15 and 2026_03_24 docs do not state units; their values (global 3.09 h vs 15.35 min; histogram ranges 0-8,270 vs 0-2,000) are consistent with the same hours/minutes convention. Any "time saved" ratio must convert one side. |
| Which release has monthly/hourly aggregates ("cadences")? | Only **2026_06_26**: calendar-month aggregates for **April 2026 and May 2026** (`date_start`/`date_end` = month bounds, `date_end` exclusive). No public file has hour-of-day, day-of-week or daily granularity; every earlier release is a single one-week window (2025-08-04..11, 2025-11-13..20, 2026-02-05..12). |
| Gender, age or other respondent demographics? | **None, confirmed in every file.** No column, facet, variable, metric_id or cluster_name encodes user gender, age or any respondent attribute. Word hits are only O*NET task text ("...age and gender"), request cluster topics ("gender studies...", "sexual health...") and substring false positives (`usage`, `message`, `image`). Only "demographic" variables are geography-level `working_age_pop` (2025_09_15) and the working-age-population denominator inside `usage_per_capita_index`. |

---

## 5. Cross-release comparability (documented + observed)

| Release | Window | Platform population | Model / classifier | Schema | Geography | Notable changes vs previous |
|---|---|---|---|---|---|---|
| 2025_02_10 | not stated in repo docs (report says Dec 2024-Jan 2025 — unverified here) | Claude.ai Free & Pro | Clio; model not stated in repo docs | flat per-task CSVs | global only | Baseline: 3,514 O*NET tasks, 5 collaboration patterns + none. |
| 2025_03_27 | not stated in repo docs (report says Feb-Mar 2025 — unverified here) | Claude.ai Free & Pro | Claude 3.7 Sonnet; adds extended-thinking flag | flat CSV + 630-cluster TSV | global only | v2 automation/augmentation (directive 22.6 -> 29.4); task list 3,365; prevalence bucketed into 100 buckets. |
| 2025_09_15 | 2025-08-04 to 08-11 (1 week) | "Claude AI (Free and Pro)"; + 1P API (global) | Sonnet 4 (per root README) | long format, 10 cols (+`geo_name` enriched) | global / country (ISO-2 raw, ISO-3 enriched) / `state_us` | First geography. Bottom-up request taxonomy (588/108/26). Enrichment: `*_pct_index`, `usage_per_capita_index`, `usage_tier`, GDP, working-age pop, `soc_pct`, `automation_pct`. Thresholds 200/100 documented but applied only to derived metrics. |
| 2026_01_15 | 2025-11-13 to 11-20 | "Claude AI (Free and Pro)" | Sonnet 4.5 (per root README) | long format, 10 cols | global / country / `country-state` (ISO 3166-2 worldwide, `US-XX`) | **Dropped**: all enrichment (`*_pct_index`, `usage_per_capita_index`, `usage_tier`, GDP, pop, `soc_pct`, `automation_pct`/`augmentation_pct`, `geo_name`), request-hierarchy JSON, `state_us` geography, code. **Added**: use_case, multitasking, human_only_ability, task_success, five numeric facets with mean/median/CI/histograms, all onet_task::/request:: intersections (global only). Taxonomy regenerated (618/112/24) — cluster names not stable. No threshold applied in file. |
| 2026_03_24 | 2026-02-05 to 02-12 | **"Claude AI (Free, Pro, and Max)"** (Max added) | Opus 4.5 / 4.6 (per root README) | identical to 2026_01_15 | same; US adds GU/PR/VI | Variable set identical to v4. "Minimum observations" bullet removed from doc. Values rounded to 4 dp. `use_case` gains a `none` value. Histogram binning changed (25 fixed-width bins). Taxonomy regenerated (621/104/26). |
| 2026_06_26 | Apr 2026 and May 2026 (calendar months) | **"Claude chat and Cowork (Free, Pro, and Max plans)"** (Cowork added); API "excluding Claude Code" | not stated in doc (report: "Cadences"; Artifacts classifier added) | **new wide schema**: `geo_level`, `category_name`, `hierarchy_level`, `metric_id`, `node_name`, `node_external_id`; ISO-3; 2-dp rounding | global / country (121 curated) / `subregion` (652) | **Dropped**: counts (`*_count`), medians/CIs/stdev/histograms, `onet_task::`/`request::` intersection facets, `not_classified` rows, `task_success`, `human_only_ability` by node (kept as pct at overall), education-years medians. **Added**: `usage_per_capita_index` back (no GDP), 4-level O*NET (Task/DWA/IWA/GWA) with element ids, SOC detailed occupations (718) + major groups, request taxonomy with UUIDs (1,008/195/20) — names entirely new and not mappable to earlier clusters, 32 `artifact_*_pct` metrics, monthly cadence, in-file sample floor (only 121 countries; only 76/91 countries get full metrics at top-level nodes). **Level shifts** at global: ai_autonomy_mean 3.41 -> 2.72; human_only_time_mean 3.06 -> 4.59 h; human_with_ai_time_mean 14.3 -> 38.7 min; multitasking 9.9% -> 22.3%; directive 31-34% range stable; use_case work 45.5%. These shifts coincide with the Cowork/Max population change and are large enough to indicate classifier/prompt changes too — do not treat v5 -> v6 as a time series without a bridge. |

Stable across 2025_09_15 -> 2026_03_24: the five collaboration pattern labels (with spaces), `none`, `not_classified`; O*NET task text as `cluster_name`; long-format column names. Stable across all four: usage share by country (`usage_pct`) and US states; per-pattern collaboration shares by country; request L2 available for >=129 countries.

Never stable: request cluster names (regenerated every release, no ids until 2026_06_26); thresholding rules (documented-only in v3, absent in v4/v5, in-file in v6); country coverage (173/174/178/121).

---

## 6. Design feasibility table

| Candidate analysis | Release(s) | File | Columns / filters | Geographies available | Blockers / caveats |
|---|---|---|---|---|---|
| Country delegation patterns vs culture (share directive / feedback loop / task iteration / learning / validation by country, regressed on cultural indices) | 2025_09_15; 2026_01_15; 2026_03_24; 2026_06_26 | v3 `aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv`; v4 `aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv`; v5 `aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv`; v6 `aei_claude_ai_2026-06-26.csv` | v3-v5: `facet=='collaboration'`, `variable=='collaboration_pct'`, `cluster_name in {'directive','feedback loop','task iteration','learning','validation','none'}`, `geography=='country'`; plus v3 `automation_pct`/`augmentation_pct` and `collaboration_pct_index`. v6: `category_name=='overall'`, `metric_id in {'collaboration_directive_pct',...,'collaboration_bucket_automation_pct'}`, `geo_level=='country'` | v3: 158 countries (115 with usage_count>=200); v4: 155 (119 >=200); v5: 154 (119 >=200); v6: 114 / 121 countries, 2 months | Must re-apply `usage_count >= 200` in v3-v5 (not done in file). Task-composition confound cannot be removed at country level in v3-v5 because `onet_task::collaboration` and `request::collaboration` are global-only; v6 allows within-node comparison only at the 35 GWAs / 20 request majors / 22 SOC major groups for 76-91 countries. Rare patterns (`validation`, `none`) missing for ~40-60 countries. Cultural covariates must be merged externally by ISO code (ISO-2 in v4/v5, ISO-3 in v3 enriched and v6). |
| State request mix vs occupation mix (US states) | 2025_09_15; 2026_01_15; 2026_03_24; 2026_06_26 | same files | v3: `facet=='request'`, `variable=='request_pct'`, `geography=='state_us'`, `level` 2 (or 1); `facet=='soc_occupation'`, `variable=='soc_pct'`. v4/v5: `geography=='country-state'` & `geo_id.str.startswith('US-')`. v6: `category_name in {'request','soc_occupation','onet'}`, `metric_id=='pct'`, `geo_level=='subregion'`, `geo_id` like `US-XX` | v3: request L2 51 states, L1 45, L0 28; `soc_pct` 47 states. v4: L2 51, L1 48, L0 30. v5: L2 52, L1 51, L0 39. v6: request all levels 52 states (L0 51), SOC L0 (median 117 of 718 occupations per state) and L1 (22 groups) 52 states, O*NET L0 median 78 tasks per state | Occupation mix of the *state workforce* is not in the repo (need BLS OES state files); the in-file SOC shares are the AI-usage occupation mix, not employment. Fine-level request/task rows are heavily suppressed per state (v3 median 18 tasks). Request taxonomy changes every release, so "mix" is comparable only within a release; SOC major groups are the only stable cross-release occupational key (v3 `soc_pct`, v6 `soc_occupation` L1). |
| Personal-use share by country | 2026_01_15; 2026_03_24; 2026_06_26 (not v3) | v4, v5, v6 files | v4/v5: `facet=='use_case'`, `variable=='use_case_pct'`, `cluster_name=='personal'` (also `'work'`, `'coursework'`), `geography=='country'`. v6: `category_name=='overall'`, `metric_id=='use_case_personal_pct'` | v4: 150 countries (apply >=200 -> ~119), 51 US states; v5: 153 (119), 52 US; v6: 114 / 121 countries, 52 US states, 652 subregions | Global personal share 38-40% in v6 vs unreported in v4/v5 global rows (must compute); v6 population includes Cowork (work-oriented) and Max, shifting work/personal mix — not a clean time series. `not_classified` share varies by country (68-85 countries carry it), so renormalise to classified total. No use_case by request/task at country level (intersections global-only in v4/v5; not published in v6). |
| Relationship-advice index by country and state | 2025_09_15 (cleanest); 2026_01_15; 2026_03_24; 2026_06_26 (different construct) | v3 enriched; v4; v5; v6 | v3: `facet=='request'`, `level==1`, `cluster_name=='Provide personal relationship advice and life guidance support'`, `variable in {'request_pct','request_pct_index'}`. v4: L1 `'Provide relationship, dating, parenting, and family advice'`. v5: L1 `'Get relationship, dating, parenting, and personal advice across life situations'`. v6: `category_name=='request'`, `hierarchy_level==1`, `node_external_id=='03e9b7f8-de59-51dc-81c5-9a5cbd61a966'` (Emotional Wellbeing and Support) or L2 `'e509219a-676b-5523-a84f-1479ccedb49c'`; index = country `pct` / global `pct` | v3: 62 countries + 33 US states (with ready-made index); v4: 54 countries + 30 US states; v5: 55 + 32; v6: 119 / 121 countries + 50 / 52 US states | Country coverage capped at 54-62 in v3-v5 by cluster-level suppression (only ~half of thresholded countries). Cluster names differ every release; the v6 node is "emotional wellbeing" not "relationship advice" (different construct). No node ids before v6. Index in v4/v5/v6 must be computed by hand (country pct / global pct). L0 children (romantic-relationship advice) cover only 22-30 countries. |
| AI autonomy by country over time | 2026_01_15; 2026_03_24; 2026_06_26 | v4; v5; v6 | v4/v5: `facet=='ai_autonomy'`, `variable=='ai_autonomy_mean'` (also `_median`, `_mean_ci_lower/upper`, `_histogram_pct` with `cluster_name` bin), `geography=='country'`. v6: `category_name=='overall'`, `metric_id=='ai_autonomy_mean'` | v4: 173 countries (Nov 2025); v5: 177 (Feb 2026); v6: 114 (Apr 2026), 121 (May 2026); US states 51 / 54 / 52 | Only four time points, and a global level break between v5 (3.41) and v6 (2.72) that exceeds any plausible real change — classifier/population discontinuity; treat v4-v5 and v6-Apr/May as two separate panels or normalise to global. v4/v5 need the >=200 filter; v6 has CI/median dropped. Per-task autonomy by country not available (global only in v4/v5; only 35 GWAs / 20 majors / 22 SOC groups for 76-91 countries in v6). |
| AUI by country and state across releases (convergence / Gini) | 2025_09_15; 2026_06_26 directly; 2026_01_15 and 2026_03_24 by reconstruction | v3 enriched (`usage_per_capita_index`); v6 (`usage_per_capita_index`); v4/v5 `usage_pct` + `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` / `working_age_pop_2024_us_state.csv` | v3: `facet=='country'`/`'state_us'`, `variable=='usage_per_capita_index'` (+ `usage_count` for the >=200 filter; + `gdp_per_working_age_capita` for 174 countries). v6: `category_name=='overall'`, `metric_id=='usage_per_capita_index'`. v4/v5 reconstruction: AUI = `usage_pct` / (working_age_pop / sum working_age_pop over covered countries); for US states use `usage_pct` of `US-XX` (relative to parent country) / state pop share | v3: 194 countries (115 >=200) + 51 states (Aug 2025); v4: 174 countries (119) + 51 states (Nov 2025); v5: 178 (119) + 54 US (Feb 2026); v6: 114 / 121 countries + 51 US states (Apr, May 2026) | v3 AUI is unthresholded (79 sub-200 countries incl. zeros) — filter. Denominator population is 2024 in v3 and unstated in v6. Platform population changes (Max in v5, Cowork in v6) and the v6 curated country list (121, no micro-states) mean the Gini/convergence sample must be restricted to the ~110 countries present in all releases (114 in both v6 months). Micro-states dominate v3 tails (MCO, LIE, IMN). GDP covariate only in v3. `usage_pct` for states in v4/v5 is relative to the US, not global — reconstruct accordingly. |
| Human time saved by task / occupation | 2026_01_15; 2026_03_24 (per task, global); 2026_06_26 (per task, per DWA/IWA/GWA, per SOC occupation, global; by country only at GWA / SOC major group) | v4; v5; v6 (+ `release_2025_09_15/data/intermediate/onet_task_statements.csv` for task -> SOC mapping) | v4/v5: `facet=='onet_task::human_only_time'` and `'onet_task::human_with_ai_time'`, `variable in {'onet_task_human_only_time_mean','_median','_count','_mean_ci_lower/upper'}` (~3,169 tasks); same for `request::`. v6: `category_name in {'onet','soc_occupation'}`, `metric_id in {'human_only_time_mean','human_with_ai_time_mean'}`, `geo_level=='global'` (2,707 tasks; 717 occupations); by country at `hierarchy_level==3` (onet) / `==1` (soc) for 76-91 countries | global only for task/occupation detail in every release; country-level only for 35 GWAs / 22 SOC major groups in v6 | **Units asymmetric**: hours (human_only) vs minutes (with AI); convert before computing savings (global ratio 3.09 h vs 15 min in v4, 4.6 h vs 39 min in v6). Level shift v5 -> v6 (both numbers up ~50-150%) is a classifier/population break. v4/v5 have no occupation rows — aggregate tasks to SOC via `onet_task_statements.csv` (task text is lower-cased in `cluster_name`; match on lower-cased `Task`). Means are of LLM-estimated times (self-reported by the classifier), not measured. |
| Coding share by country | 2025_09_15; 2026_01_15; 2026_03_24; 2026_06_26 | v3 enriched; v4; v5; v6 | v3: `facet=='request'`, `level==2`, `cluster_name=='Provide comprehensive software development assistance across multiple programming domains and technologies'` (18.53% global) and/or `facet=='soc_occupation'`, `cluster_name=='Computer and Mathematical'` (`soc_pct`, 35.88%). v4: L2 `'Help debug, develop, and optimize software across multiple programming domains'` (14.80%). v5: L2 `'Assist with software development, debugging, and programming across multiple platforms'` (16.84%). v6: request L2 `node_external_id=='f1286a7a-ec7b-55b6-b252-9606092d40cd'` (Software Development, 11.5%), `soc_occupation` L1 `node_external_id=='15'` (Computer and Mathematical, 23.8%), onet L3 `'4.A.3.b.1'` (Working with Computers, 9.4%) | v3: 133 countries / 51 states (request), 111 / 43 (soc); v4: 126 / 51; v5: 131 / 52; v6: 114 / 121 countries, 52 US states | Coding cluster is defined differently in each taxonomy (v3 one broad cluster; v4/v5 split web/game/AI/trading into separate L2s; v6 splits DevOps, cybersecurity, AI app building) — the SOC "Computer and Mathematical" share is the only definitionally stable cross-release measure (v3 `soc_pct`, v6 `soc_occupation` L1; absent in v4/v5 unless rebuilt from tasks). Claude Code is excluded from API files and Claude.ai data never included it, so this measures chat-based coding only. Apply >=200 filter in v3-v5. |

### Practical notes for any design
1. Use `release_2025_09_15` enriched file for anything needing GDP, working-age population, `*_pct_index` or `usage_tier`; nothing later ships them.
2. Use `release_2026_06_26` for anything needing SOC detailed occupations, O*NET DWA/IWA/GWA rollups, artifact types, monthly cadence or stable node ids.
3. Use `release_2026_01_15` / `2026_03_24` for medians, CIs, histograms, `task_success`, and the richest set of global task-level intersections — but only global for intersections, and apply the >=200 filter yourself.
4. Read every ISO-2 file with `keep_default_na=False` (Namibia).
5. Treat the v5 -> v6 boundary as a regime change, not a time step.
