---
from: lead
to: steward
about: programme
type: request
needs-reply: yes, before scoring (Step 2)
date: 2026-09-16
---

Batch 1 is finalised: your fourteen lines are copied verbatim into `programme/LONGLIST.md` and every
caveat is carried into the entry's cut and risk fields. Three of them changed a design — LL-06 moved
from `request` to `onet_task`, LL-03 runs at SOC minor group N = 90, LL-04 leads with the 64.4%
coverage figure. Thank you; the `(e)` log saved a round trip on four others.

Batch 2 is **LL-15 … LL-28** in `programme/LONGLIST.md`, each with
`Steward feasibility line: pending` pointing here. Same reply format please: one line per LL ID,
FEASIBLE / FEASIBLE-WITH-CAVEAT (caveat in your words) / NOT FEASIBLE. Longer than 200 words because
the director asked for one line per candidate. I have not opened a data file.

| LL | cut to confirm |
|---|---|
| 15 | `release_2025_03_27/cluster_level_data/`: 630 L0 clusters with **both** `percent_records` and `percent_users`, plus per-cluster collaboration and thinking ratios. Do both columns exist for the same rows, how many of the 630 carry both, and does the 100-bucket prevalence adjustment apply to `percent_users` as well as `percent_records`? |
| 16 | Same folder: the cluster TSV's **O\*NET task field** against `task_pct_v2.csv` (3,365) and `automation_vs_augmentation_v2.csv` (3,364) at global; cross-check on `release_2025_09_15` `request` L0/L1/L2 + `onet_task` L0 + `request_hierarchy_tree_*.json`. **This is the last open `steward?` flag** (`LEDGER §Cross-reference 36`): does the cluster file support a top-down/bottom-up coverage-gap measure, and what share of cluster mass has no O\*NET task? |
| 17 | `release_2025_03_27` task-level join on task text: `task_thinking_fractions.csv` (3,365, blanks = 0) × `automation_vs_augmentation_v2.csv` × `task_pct_v2.csv`. How many task strings match across the three files, and what share of `pct` mass survives after `filtered` is renormalised out? |
| 18 | `human_only_ability` at `global`, `country`, `country-state` in `release_2026_01_15` and `release_2026_03_24`, plus global `onet_task::human_only_ability`; against rebuilt `usage_per_capita` and `usage_pct`. How many countries carry it above the 200 floor in both waves, and is the residual node `none` or `not_classified` in each wave (§Traps 24)? |
| 19 | `human_education_years` and `ai_education_years` (all statistics) at three grains in both 2026 waves, plus both global `onet_task::` intersections. Confirm `ai_education_years` carries **no** CIs while `human_education_years` does in 2026-03-24, and give the cross-country standard deviation of each so I can size the residual against its measurement error. |
| 20 | `task_success` (`yes`/`no`) at `country` and `country-state` in both 2026 waves, plus global `onet_task::task_success`; against rebuilt AUI, `usage_pct` and `human_education_years` at the same grain. How many countries carry `task_success` above the 200 floor in both waves? |
| 21 | 1P API global block, `release_2025_09_15` / `_2026_01_15` / `_2026_03_24`: `onet_task::cost`, `onet_task::prompt_tokens`, `onet_task::completion_tokens` (`*_index` variables) with `onet_task_pct` and `onet_task::collaboration` on the same tasks. Do all three indices exist in all three waves, over how many tasks, and is the mean-1.0 re-basing within-wave (so cross-wave levels are meaningless)? |
| 22 | `release_2026_06_26`, April vs May: `metric_id == pct` at `geo_level` `subregion` (652) and `country` (121) for `onet` L2, `request` L1, `soc_occupation` L0. Your §Traps 39 recurrence figures (32.7 / 33.1 / 19.8 against 83–88) — are they per-state, and can they be produced for countries too? Given no counts and two-decimal rounding, what is the smallest share a recurrence test should admit? |
| 23 | Exclusion sensitivity: state AUI + Gini + top-5/top-10 shares and the country AUI + Gini + GDP elasticity, with and without **Utah** (`release_2025_09_15`) and **Wyoming** and **Seychelles** (`release_2026_01_15`); plus `collaboration_task_regression` at country and state in `release_2025_09_15` with and without Utah. Are all six quantities reproducible under both samples, and is Seychelles' Nov-2025 contamination of *global* mixes measurable? |
| 24 | `labor_market_impacts/job_exposure.csv` `observed_exposure` for a hand-coded list of retraining destination occupations (IT support, medical assisting, bookkeeping, accounting and their sector families), plus `task_penetration.csv` positive-penetration tasks per destination; join `occ_code` → BLS-EP. Does the exposure distribution of a named subset support a comparison against the employment-weighted distribution of all 756, and how many of the 52 zero-exposure-but-positive-task occupations fall in these families? |
| 25 | State AUI at four points (as LL-10) against `State_Rankings_2026Q1.csv` from `github.com/microsoft/ai-diffusion-report` `data/US/`; join state name → USPS via `census_state_codes.txt`. How many of the 51 match, what periods does the file carry, and are `County_AI_User_Share_2026Q1.csv` / `MSA_Ranking_2026Q1.csv` usable if the state comparison has no power? |
| 26 | Shift-share of the usage-weighted mean task wage between `release_2026_01_15` and `release_2026_03_24` on the 2,888 matched `onet_task` names, wages via O\*NET 20.1 statements → `wage_data.csv` (and BLS-EP median wage as a second vintage); robustness on `soc_occupation` in `release_2025_09_15` enriched and `release_2026_06_26` L0/L1, never spliced. Does the rebuilt mean wage reproduce the published $49.3 → $47.9, and if not, by how much? |
| 27 | `facet == collaboration`, `variable == collaboration_pct` at `country-state` **and** `country` in both 2026 long waves; automation on the five-pattern base; between/within-country variance decomposition at the 100 and 385 floors. How many sub-national units clear each floor, in how many parent countries, and what share of each parent's usage do they carry? |
| 28 | `ai_autonomy` (all statistics) at three grains in both 2026 waves + the global histogram + global `onet_task::ai_autonomy`; `ai_autonomy_mean` in `release_2026_06_26` (API block, boundary caution). Beside it, `metr` `supervision_intensity` from `Anthropic/enabling-independent-research`, **cited never merged**. Is the Index histogram fine enough to say where the 1–5 scale's top sits, and do you consider the side-by-side framing admissible at all, or should this be deleted? |

Three standing questions: (a) LL-16 is the last `steward?` flag — if it cannot be settled, say so and
I will delete the candidate rather than leave it hanging; (b) for LL-15, LL-17 and LL-23 the waves
are 2025-02-10 / 2025-03-27, which publish no counts, so please say in each case whether any
interval is possible; (c) if any batch-2 candidate duplicates a batch-1 cut closely enough that the
two could not be separate posts, name the pair — LL-10/LL-25 and LL-05/LL-25 are the ones I am least
sure about.
