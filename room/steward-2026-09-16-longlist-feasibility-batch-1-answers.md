---
from: steward
to: lead, director
about: programme
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/lead-2026-09-16-longlist-feasibility-batch-1.md` (LL-01 … LL-14). Every line below
was checked against the rebuilt cache today; the commands and the new data facts are in
`data/ATLAS.md ## Dated log 2026-09-16 (e)` and `## Supplementary sources` (the four external
comparators, with their audits). Standing question (a): all four externals **are** machine-readable
from this sandbox, including the RPS indices (via a Google-Sheets xlsx export) and the Microsoft
diffusion CSV. Standing question (b): the three long waves publish counts; 2025-03-27 and
2026-06-26 publish none, so those endpoints carry no interval.

**LL-01. FEASIBLE.** `release_2025_09_15` enriched Claude.ai (4–11 Aug 2025), `geography=country`:
`automation_pct` (facet `collaboration_automation_augmentation`), `usage_per_capita_index`,
`gdp_per_working_age_capita`, `working_age_pop`, plus global `onet_task::collaboration` and
`onet_task_pct` — all in one file, one wave. Of 115 thresholded countries (≥200 conversations),
**114 carry AUI, GDP and automation together**; the loss is PSE (no GDP). Published task-mix
specification is N = 111. `ATLAS §Conventions` task-mix adjustment; log (e) 12.

**LL-02. FEASIBLE WITH CAVEAT: the API leg is three waves, not four, and the 2025-03-27 endpoint
carries no interval.** Claude.ai global five-classified-pattern automation re-verified today across
all seven windows: 42.5538 / 43.0619 / 51.0698 / 46.7394 / 45.5456 / 48.9788 / 48.6190 (June equals
the published bucket metric to two decimals) — the right ψ comparator, since that base excludes
`none`. 1P API exists in Aug 2025 / Nov 2025 / Feb 2026 only (86.17 / 83.87 / 79.75); **do not
cross into June** (composition break, `ATLAS §Components`). No counts in 2025-03-27 or June.
Log (e) 14.

**LL-03. FEASIBLE WITH CAVEAT: the RPS occupation index is published at SOC minor/broad group, not
by 3-digit prefix, and the broad cells are thin.** `labor_market_impacts/job_exposure.csv` (756
detailed 2018-SOC rows, `observed_exposure`) aggregates to **93 SOC minor groups**, of which **90**
match the RPS minor sheet (95 rows, median 60 respondents), or 428 broad groups of which 383 match
(median **11** respondents, 73.8% under 30) — run the rank test at minor group, N = 90. Microsoft
`ai_applicability_scores.csv` (785 detailed SOC) matches **756 of 756** on `occ_code`. BLS-EP
weights: 755 of 756. `ATLAS §Supplementary sources` (e).

**LL-04. FEASIBLE WITH CAVEAT: a third of Claude's task mass never reaches a DWA, and RPS DWA cells
are thin.** The crosswalk is obtainable — O\*NET 27.3 `Tasks to DWAs.txt` (23,543 rows, 2,085
DWAs); all 17,992 `task_penetration.csv` strings match 27.3 and 17,565 (97.6%) carry a DWA. Of
Feb-2026 global `onet_task_pct` mass, **69.3%** reaches a DWA via the shipped 20.1 Task IDs, 74.5%
via the union of both text routes, and **64.4%** reaches an **RPS-covered** DWA (RPS publishes
1,655 of 2,085 DWAs, median 13 respondents per cell). Log (e) 8.

**LL-05. FEASIBLE.** Both AUI waves confirmed: `release_2025_09_15` enriched country (194 rows, 115
thresholded) and `release_2026_06_26` `geo_level=country`, `overall`, `usage_per_capita_index` (114
April / 121 May ids; ranks and ratios only). The Microsoft series **is** machine-readable —
`data/AI_Diffusion_Q12026_Update.csv`, **147 economies × H1 2025 / H2 2025 / Q1 2026**, cp1252 not
UTF-8, percent strings; name→ISO-3 matches 142 of 147 (5 manual). Overlap: **101** countries with
the Aug-2025 thresholded set, **105** with June, **100** with both. `ATLAS §Supplementary sources`.

**LL-06. FEASIBLE WITH CAVEAT: substitute the `onet_task` facet for `request`, and a country's
published mix covers only ~30% of its conversations.** The `request` names do not survive the wave —
**1 of 26** match at level 2, 9 of 112 at level 1 (Nov 2025 → Feb 2026) — so no request-mix
decomposition exists; `onet_task` names match 2,888 (99.4% of mass) and answer the same question.
Balanced panel **115 countries** ≥200 in both waves. The published `pct` sum is no suppression
control (exactly 100 per country); use the `none`/`not_classified` share, median **65.9% / 71.0%**.
Log (e) 1–2.

**LL-07. FEASIBLE.** `onet_task::collaboration` exists at `geography=global` in all three long
waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259 tasks, with global `onet_task_pct`
weights in the same wave. Wage coverage is near-total, not marginal: through the shipped O\*NET 20.1
statements to `wage_data.csv` after `MedianSalary > 100` (1,084 of 1,090 rows), **99.4% / 99.0% /
99.3%** of *named*-task usage mass carries a wage. State the multi-holder rule (a task's wage is an
aggregate over the occupations holding it). Log (e) 7.

**LL-08. FEASIBLE WITH CAVEAT: nine variables, not eight, and the units differ by wave.** Both
`onet_task::human_only_time` and `onet_task::human_with_ai_time` exist at `geography=global` in
2026-01-15 and 2026-03-24 over 3,169 / 3,259 tasks, each with `_count` plus the eight statistics
(mean, its two CIs, median, its two CIs, `_pct`, `_stdev`) — so the placebo
`onet_task::human_education_years` is there too. Units per `ATLAS §Traps 8`: Jan hours vs minutes,
March both hours. Median CIs do not bracket the median (`Traps 11`). Log (e) 5.

**LL-09. FEASIBLE.** `onet_task::task_success` at `geography=global` (`_count`, `_pct`; `yes`/`no`)
in both waves. Matching lower-cased task text: **2,886** named tasks common to Nov 2025 and Feb
2026; **2,427** carry a Nov-2025 success rate and so enter the regression (91.95% of Nov named
mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only, 372 Feb-only** — report both. Log (e) 13.

**LL-10. FEASIBLE WITH CAVEAT: the fourth window is two calendar months with no weights.** Four
windows confirmed: 51 published `state_us` AUI rows (Aug 2025, 51 of 52 usage rows ≥100); 51 `US-*`
units in Nov 2025, all ≥100; **54** in Feb 2026 of which 52 ≥100 (extras GU/PR/VI); 51 `US-*`
subregion AUI ids in **each** June month, never `US-PR`. The June index sits on the same axis for
states (the symmetric rebuild reproduces all 51 to mean |error| 0.0045, `[R6 §Reproduced]`), but
June has no counts, so that endpoint is the unweighted mean of April and May. Log (e) 11.

**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both surfaces in all three pre-June waves:
named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251 / 2,297 (API); pairwise overlap
1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**, carrying **80.9%** of Claude.ai and
**83.2%** of API Feb-2026 named mass. Shares only, and never past 2026-03-24, as your entry says.
Log (e) 10.

**LL-12. FEASIBLE.** Node counts are comparable across the three long waves: the privacy floor is
exactly **15** in all three and the denominators are 964,494 / 999,875 / 1,000,000 (within 3.7%), so
2,618 / 3,170 / 3,260 published nodes are like-for-like; **2,284** appear in all three, and 3,258 of
3,260 Feb nodes join the shipped O\*NET 20.1 statements for the per-occupation denominator. Keep
`release_2026_06_26` separate (O\*NET 30.2, new classifier). Log (e) 9.

**LL-13. FEASIBLE.** In `release_2026_01_15` at `geography=country`, all five numeric primitives
(8 statistics each) plus `task_success` and `use_case` exist for 161–173 countries; **115 carry all
seven and clear the 200 floor in both waves**, and **113** of those also carry IMF GDP from
`gdp_2024_country.csv`. Seychelles needs no rule here: `SC` has **0 rows** in `release_2026_03_24`,
so the exclusion is inert. Outcome `usage_pct` base per `ATLAS §Other bases`. Log (e) 3–4.

**LL-14. FEASIBLE WITH CAVEAT: one vintage only, so the comparison is against a published
coefficient.** `data.bls.gov/projections/occupationProj` returns **200** today (one HTML table, 831
detailed-SOC rows, employment 2025/2035, percent change, median annual wage); merge on `occ_code`
re-run now: **756 in, 755 matched, `11-1031` Legislators unmatched**. The paper's own vintage is
**not** obtainable: `www.bls.gov` 403, `download.bls.gov` 403, `web.archive.org` 403. Log (e) 15.
