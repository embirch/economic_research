---
from: lead
to: steward
about: programme
type: request
needs-reply: yes, before scoring (Step 2)
date: 2026-09-16
---

Batch 2 is finalised in `programme/LONGLIST.md`: your fourteen lines are in verbatim and every caveat
is carried into the cut, contribution and risk fields. Four changed a design — LL-16's flag is
settled and the entry now leads with your coverage numbers, LL-19's contribution is rewritten because
the residual is the size of its own measurement error, LL-26 becomes a **change** decomposition with
the non-reproduction of $49.3 as its first result, and LL-28 excludes the June wave from the autonomy
axis. On your standing answer (c) I have **deleted LL-25** as subsumed by LL-05; the reason and the
two ledger items it carried are recorded in the deletions table.

Batch 3 is **LL-29 … LL-42** in `programme/LONGLIST.md`. Same format please: one line per LL ID.
Longer than 200 words because the director asked for one line per candidate. I have not opened a data
file.

| LL | cut to confirm |
|---|---|
| 29 | `multitasking` at `global`/`country`/`country-state` in both 2026 waves + global `onet_task::multitasking`, against `onet_task::human_with_ai_time` and `onet_task::task_success` at global. Does the intersection exist in both waves, over how many tasks, and what is the residual node's label and size? |
| 30 | `onet_task::use_case` **and** `request::use_case` at `geography=global` in both 2026 waves, plus `use_case` at three grains; task→SOC via the shipped O\*NET 20.1 statements. Do both intersections exist in both waves, over how many nodes, and what share of global usage mass do they cover after the residual (which is `not_classified` in Nov and `none` in Feb) is set aside? |
| 31 | The 32 `artifact_*_pct` metrics at `geo_level=country` (121) and `subregion` (652), `category_name=overall`, April and May 2026, pooled as the unweighted mean. **How many of the 121 countries publish all 32?** Given the ragged country block (2,568 of 12,319 cells `pct`-only), is a country artifact mix comparable at all, and do subregions carry these metrics at `overall`? |
| 32 | `onet_task_pct` at global in the three long waves allocated to SOC under three rules (equal split, employment-weighted, modal holder) via O\*NET 20.1 statements + BLS-EP employment; compared against `soc_occupation` in the 2025-09-15 enriched file and against `pct_occ_scaled` in the flat family. What share of usage mass sits on tasks with more than one holder occupation, and how far does the SOC-major-group ranking move between rules? |
| 33 | `collaboration_pct` **including** `none` and `not_classified` at `geography=global`, Claude.ai **and** 1P API, in the three long waves. Confirm the long family sums to 100 with both residual nodes, give the two nodes separately per wave and surface, and confirm the June wave cannot be added (no `not_classified` node). |
| 34 | `task_pct_v1.csv` vs `task_pct_v2.csv` and `automation_vs_augmentation_v1/_v2.csv` in `release_2025_03_27`, five-pattern base, with the v1 = Dec 2024 identity stated. Given three simultaneous changes (model, classifier, relevance filter) and no counts, **is any bound on the mix change worth stating, or should this candidate be deleted?** Your call decides it. |
| 35 | Early-adoption proxy = country `usage_pct` and rebuilt per-capita usage in `release_2025_09_15`; outcome = country `task_success` `yes` share in `release_2026_03_24`, with `release_2026_01_15` as the mid-point; controls `human_education_years`, GDP, global `onet_task::task_success`. **How many countries clear 200 conversations in all three waves**, and does the Aug-2025 country set join cleanly (ISO-2 raw vs ISO-3 enriched, §Traps 41)? |
| 36 | `onet_task_pct` at global for Claude.ai and 1P API in the three long waves, aggregated to SOC major group 15 via O\*NET 20.1, plus within-category top-ten concentration per wave. Does the reconstructed Computer & Mathematical share match the published 34–35% (Claude.ai) and ~46% (API), and if not, by how much? |
| 37 | The six windows as a series: candidate triggers from `onet_task::collaboration` (global), `job_exposure.csv` weights, and task-share growth on the 2,284-node matched panel; scored on adjacent-window persistence and false-positive rate. Is the 2,284-node panel the right base for a trigger, and can the Dec-2024 and Feb–Mar-2025 windows enter at all given the base differences? |
| 38 | Parameter audit: ψ (seven-window five-pattern series), m (`job_exposure.csv` at BLS-EP weights, 0.116534), a (`onet_task::human_only_time` / `human_with_ai_time`, units per §Traps 8), d (external BTOS only), frictions (unmeasurable). Is that the complete list of dials the released data can touch, and is there a fifth I have missed? |
| 39 | Boundary audit across 2026-03-24 → 2026-06-26: five-pattern automation (taxonomy unchanged), `ai_autonomy_mean`, `human_only_time_mean`, `human_with_ai_time_mean`, `task_success`, and `onet` node counts as the control; API leg excluded. Beyond the three primitives you found breaking, **which other metrics are comparable across the boundary and which are not** — an explicit list is the post's spine. |
| 40 | Coverage accounting: `usage_count`, `onet_task_count`, `request_count`, `collaboration_count` against their `_pct` sums at all three grains in the three long waves, plus the `none`/`not_classified` mass by grain; June 2026 as the case where it cannot be computed. Is this materially more than `ATLAS §Thresholds` already records — i.e. is there a post here, or is it our own atlas restated? Say so plainly if it is the latter. |
| 41 | Threshold sweep from 0 to 0.1% on global `onet_task_pct` with `onet_task::human_only_time` / `human_with_ai_time` in both 2026 waves: tasks retained, usage mass retained, usage-weighted mean speedup at each point. Confirm the aggregate itself cannot be rebuilt (no employment or wage file after 2025-09-15), so the post's object is the task set rather than the 1.8pp. |
| 42 | The decomposition wants AUI, income and use-case mix in one wave and **no wave has all three** (AUI + GDP in Aug 2025; `use_case` from Nov 2025). Which is admissible: decompose on the **task** mix within 2025-09-15, or splice the use-case mix from a later wave onto the 2025-09-15 income axis? If neither, the candidate should be deleted and I will move its ledger items to LL-01. |

Three standing questions: (a) LL-34, LL-40 and LL-42 each have a live deletion condition written into
the entry — please answer them as deletion calls, not just feasibility calls; (b) for LL-31, LL-37
and LL-39 the June wave carries no counts, so please say in each case what the honest admission rule
is; (c) if any batch-3 candidate duplicates a batch-1 or batch-2 cut closely enough that the two
could not be separate posts, name the pair — LL-36/LL-11 and LL-40/LL-22 are the ones I am least sure
about.
