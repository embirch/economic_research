---
from: lead
to: steward
about: programme
type: request
needs-reply: yes, before scoring (Step 2)
date: 2026-09-16
---

Long-list batch 1 is drafted in `programme/LONGLIST.md` as **LL-01 … LL-14**; each entry carries a
`Steward feasibility line: pending` pointing here. Please read the cut proposals there (they name
the atlas section I relied on) and reply with **one feasibility line per LL ID** that I can copy
verbatim: FEASIBLE / FEASIBLE-WITH-CAVEAT (caveat in your words) / NOT FEASIBLE. Longer than 200
words because the director asked for one line per candidate. I have not opened a data file.

| LL | cut to confirm |
|---|---|
| 01 | `release_2025_09_15` enriched Claude.ai, `geography=country`: `automation_pct` (facet `collaboration_automation_augmentation`), `usage_per_capita_index`, `gdp_per_working_age_capita`, `working_age_pop`, plus global `onet_task::collaboration` + `onet_task_pct` for the task-mix adjustment; 4–11 Aug 2025; N=111 thresholded. Can automation be regressed on AUI **and** income in one file? |
| 02 | `collaboration` five-classified-pattern automation share, Claude.ai global, all seven windows (2025-02-10 → 2026-06-26) + 1P API for the three pre-June waves. Confirm your series (0.4255 … 0.4862) is the right comparator for ψ and that the API side stops at 2026-03-24. |
| 03 | `labor_market_impacts/job_exposure.csv` (756 rows, `occ_code` 2018-SOC detail, `observed_exposure`), aggregated to **3-digit SOC** with BLS-EP employment weights; join keys: 3-digit prefix → RPS occupation adoption index (Bick–Blandin–Deming–Schumacher 2026, public download), `occ_code` → `microsoft/working-with-ai` `ai_applicability_scores.csv`. How many of the 756 survive to 3-digit with weights? |
| 04 | `labor_market_impacts/task_penetration.csv` (de-dup on `task`, no lower-casing) + `onet_task_pct` at global in `release_2026_03_24`; join key: O*NET **27.x Task→DWA** reference table (external download) → RPS task-level adoption index (DWA ids). Is the Task→DWA crosswalk obtainable, and what share of Claude's task mass maps to a DWA? |
| 05 | AUI at `country` in the only two waves that publish it: `release_2025_09_15` enriched (194 rows, 115 thresholded) and `release_2026_06_26` (`geo_level=country`, `category_name=overall`, `metric_id=usage_per_capita_index`, April + May, **ranks/ratios only**). Join key: ISO-3 via `iso_country_codes.csv` → Microsoft AI Diffusion country shares. **Is the Microsoft series machine-readable, and for how many countries?** |
| 06 | `release_2026_01_15` + `release_2026_03_24`, `facet=request`, `level` 1 and 2, `variable=request_pct` at `geography=country` **and** `global`, plus `usage_pct` at `country` for weights; shift-share of the global concentration change. Is a balanced country panel above the 200 floor available in both waves, and can the published `pct` sum per country be used as a suppression control? |
| 07 | `onet_task::collaboration` at `geography=global` in `release_2025_09_15`, `release_2026_01_15`, `release_2026_03_24`, weighted by global `onet_task_pct`; join keys: lower-cased task text → `onet_task_statements.csv` (O*NET DB 20.1) → `SOCcode` in `release_2025_02_10/wage_data.csv` (and BLS-EP median wage as a check). What share of usage carries a usable wage after the `MedianSalary>100` filter? |
| 08 | `onet_task::human_only_time` and `onet_task::human_with_ai_time` at `geography=global` in `release_2026_01_15` and `release_2026_03_24`, against global `onet_task_pct`; units per §Traps 8. Placebo: `onet_task::human_education_years`. Confirm the eight statistics exist on the intersected numeric facets in both waves. |
| 09 | `onet_task::task_success` at `geography=global` in `release_2026_01_15` and `release_2026_03_24`, against the change in global `onet_task_pct` between the same two waves; tasks matched on lower-cased text. How many task nodes match across the two waves, and how many are unmatched each way? |
| 10 | State AUI at four windows: `release_2025_09_15` enriched `state_us` (published AUI, 100 floor); `US-*` rows in `release_2026_01_15` and `release_2026_03_24` **rebuilt** with `working_age_pop_2024_us_state.csv`; `release_2026_06_26` `subregion` `usage_per_capita_index` (51 + DC, no `US-PR`). Symmetric rule for 2026 levels; Wyoming/Utah by stated rule. Are four usable windows really available, and does the June AUI belong on the same axis as the three rebuilt ones? |
| 11 | `onet_task` L0 `onet_task_pct` at `geography=global` for **both** Claude.ai and 1P API in `release_2025_09_15`, `release_2026_01_15`, `release_2026_03_24` (never crossing into 2026-06-26). Do the two surfaces' L0 task sets overlap enough for a task-level paired comparison in all three waves, and how many tasks appear in all six frames? |
| 12 | `onet_task` L0 at `geography=global` in the three long waves: distinct published node count, `pct` Lorenz/Gini, and per-occupation within-wave coverage via `onet_task_statements.csv`. `release_2026_06_26` `onet` L0 reported separately, never spliced. Is the published node count comparable across the three long waves, or does suppression/classifier change make it not? |
| 13 | `release_2026_01_15`, `geography=country`: five numeric primitives + `task_success` + `use_case` (eight statistics each) as predictors; outcome = change in `country` `usage_pct` to `release_2026_03_24`; 200 floor applied by us; Seychelles by stated rule; optional income from `gdp_2024_country.csv`. How many countries carry all seven measures **and** clear the floor in both waves? |
| 14 | `labor_market_impacts/job_exposure.csv` `occ_code` → BLS Employment Projections occupation table (831 rows, employment 2025/2035, % change, median annual wage); your merge audit was 756 in / 755 matched. Confirm the EP table is still reachable, and confirm the paper's own vintage is **not** obtainable here (403 / egress block), so the post compares against a published coefficient. |

Two standing questions across the batch: (a) for any candidate needing an external join, is the
source machine-readable from this sandbox at all; (b) where a candidate needs an interval, does the
wave publish counts (LL-06, LL-09, LL-13) or not (LL-02's 2025-03-27 endpoint, LL-05's June wave)?
Mark NOT FEASIBLE freely — a deleted candidate costs me nothing now and costs the referee later.
