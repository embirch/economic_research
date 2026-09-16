---
name: economic-index-data
description: How the Anthropic Economic Index public releases are laid out, the conventions that reproduce Anthropic's published numbers, and the traps found so far. Read before loading any release or quoting any published number.
---

# Economic Index data: layout, conventions, traps

Source: Hugging Face dataset `Anthropic/EconomicIndex` (CC-BY 4.0), one folder per release with `data_documentation.md`, data files, and for some releases the analysis code and notebooks. Verify every statement below against the file in front of you before relying on it; releases change schema.

## Releases and schemas (as of September 2026)
- **2025-02-10, 2025-03-27**: early releases; O*NET task mappings, request clusters, automation/augmentation at global level; `onet_task_statements.csv` (task → O*NET-SOC code) lives in 2025-02-10.
- **2025-09-15** (long schema; enriched and raw files): columns `geo_id, geography (country | state_us | global), date_start, date_end, platform_and_product, facet, level, variable, cluster_name, value`. Facets: `country`, `state_us`, `onet_task`, `collaboration`, `collaboration_automation_augmentation`, `request` (levels 0–2), `soc_occupation`, `onet_task::collaboration` and `request::collaboration` (GLOBAL ONLY). Country codes ISO-3 in the enriched file. Also `gdp_2024_country.csv`, `working_age_pop_2024_country.csv`, and the US-state equivalents. Code: `aei_analysis_functions_claude_ai.py` with `filter_df`, `get_filtered_geographies`, `collaboration_task_regression(df, geography="country"|"state_us")`.
- **2026-01-15 and 2026-03-24** (raw long schema): `geography` values `country`, `country-state` (ISO 3166-2 such as `US-CA`), `global`; country codes ISO-2. Facets add primitives (`ai_autonomy`, `human_education_years`, `human_only_time`, `human_with_ai_time`, `task_success`, `use_case`, `multitasking`, `human_only_ability`). No AUI in file; no `soc_occupation` at state level.
- **2026-06-26** (wide schema, monthly April and May): `date_start, date_end, geo_id, geo_level (global | country | subregion), category_name (overall | onet | request | soc_occupation), hierarchy_level, metric_id, value, node_name, node_external_id`. `overall` carries usage, AUI (countries and US states only), use-case shares, collaboration patterns and buckets, artifact shares, primitives. Country rows publish all metrics for top-level nodes (GWA, request Major, SOC Major Group) and only `pct` below; subregion rows publish `pct` only for onet/request/soc. Separate `aei_1p_api_*.csv` is global only.
- `labor_market_impacts/`: `job_exposure.csv` (756 SOC occupations) and `task_penetration.csv`.

## Conventions that reproduce published numbers
- **Thresholds are not applied in the public files.** Apply 200 conversations per country and 100 per US state yourself (constants in Anthropic's code). June 2026 files carry no per-country usage counts; treat them as pre-filtered.
- **AI Usage Index** = country's share of usage ÷ share of working-age population. Verified to five decimals: the usage denominator is usage over thresholded countries PLUS `not_classified`; the population denominator is over thresholded countries only. Rebuild it this way for the waves that do not carry it.
- **Automation share** = (directive + feedback loop) ÷ (sum of the five classified patterns) × 100, not ÷ all conversations. June's `collaboration_bucket_automation_pct` uses the same base.
- **Task-mix adjustment**: expected automation from a geography's task weights × global per-task automation rates, residualised; Anthropic's function reproduces Figure 2.11 (slope −3.112, R² 0.394, N 111) exactly on the August 2025 enriched file.
- **"Each 1% increase in the share of tech workers"** (January 2026) means one percentage point of share: log AUI on share in points reproduces 0.36 (0.369, R² 0.62 on August 2025). The log-log elasticity does not.
- **State Gini of the AUI** is the unweighted Gini over 51 state values (0.367, 0.318, 0.286); the population-weighted Lorenz version does not match.

## Traps
- `NA` is Namibia: read every long file with `keep_default_na=False`.
- Seychelles, November 2025: AUI 1,055 (routed traffic); exclude by a stated anomaly rule (index > 25).
- Utah, August 2025: flagged by Anthropic for possible coordinated abuse; its adjusted automation is 25 points off every other state and its AUI fell from 3.8 to 1.1 by November. Exclude by rule and show separately.
- August 2025 state-level `soc_occupation`: 74% `not_classified` and two-thirds of cells suppressed; unusable as a mix. Use June 2026.
- June 2026 publishes no request-by-occupation cross at any grain; artifact, use-case and collaboration metrics by occupation group exist at global and country level.
- Cluster suppression is heavy at fine levels (per-country level-0 request clusters present: median 42 of 588). Compare mixes at levels 1–2 and within a wave; taxonomies change between releases.
- Single-window distinctiveness is half noise at state level (April-to-May recurrence 45%); require persistence across independent windows.
- Occupation in the data is inferred from the task, not from the user.
- Files offloaded to iCloud stall loads; use `usecols` and numeric conversion on load.

## Supplementary sources that work without keys
Census ACS table-based summary files at `www2.census.gov/programs-surveys/acs/summary_file/<year>/table-based-SF/data/1YRData/acsdt1y<year>-<table>.dat` (the API now needs a key); Census `PctUrbanRural_State.txt`; World Bank API; Microsoft AI Diffusion state and county CSVs (`github.com/microsoft/ai-diffusion-report`); OpenAI Signals CSV bundle (`cdn.openai.com/signals/data-download-csv.zip`, state rank and topic shares). BLS OEWS and the Census gazetteer block non-browser downloads.
