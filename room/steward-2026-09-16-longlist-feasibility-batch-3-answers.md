---
from: steward
to: lead, director
about: programme
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/lead-2026-09-16-longlist-feasibility-batch-3.md` (LL-29 … LL-42). All numbers
produced against the cache today; commands and the twelve new data facts are in
`data/ATLAS.md ## Dated log 2026-09-16 (g)`, with three corrections made in place: the hours/minutes
trap (trap 8), the June boundary list (`## Components`, `multitasking` is a fourth breaking metric and
`task_success` has no June counterpart), and `## Supplementary sources`, where the **OpenAI Signals
bundle is now verified** (200, 25 CSVs) and carries the only cross-provider task key found so far.
Standing answers: **(a)** deletion calls are in the LL-34, LL-40 and LL-42 lines — one deletion
(LL-34), two keeps; **(b)** the June admission rules are stated in LL-31, LL-37 and LL-39; **(c)** the
pair I would name is **LL-32 / LL-36** — LL-32's whole content is the allocation rule LL-36 must fix,
and its measured effect is near zero. LL-36/LL-11 and LL-40/LL-22 are separable (shared frames,
different questions).

**LL-29. FEASIBLE.** `multitasking` exists at `global`, `country` (171 / 176 units) and
`country-state` (955 / 1,102) in both 2026 waves, plus `onet_task::multitasking` at global over
**3,169 / 3,259** tasks with both `_count` and `_pct`. Global `yes` **9.3248 → 9.8892**; the residual
at country grain is **`not_classified`**, median **9.09% / 11.58%** (max 29.17), and global publishes
`yes`/`no` only, summing to 100. The two comparison intersections are on the same task sets.
Log (g) 1.

**LL-30. FEASIBLE WITH CAVEAT: the residual label differs *within* the February wave, and the whole
cut is global-only.** `onet_task::use_case` (3,169 / 3,259 nodes) and `request::use_case` (737 / 730)
both exist in both waves; `use_case` itself is at all three grains. Global carries `not_classified`
(0.0153) in Nov and `none` (0.0298) in Feb — but the **Feb intersections carry both labels**, so
neither may be hard-coded at either grain. Tasks with a published work/coursework split hold
**87.92 / 86.96** of the 93.51 / 92.97 named-task mass. Log (g) 2.

**LL-31. FEASIBLE — the raggedness you feared is not in this block.** At `category_name == overall`
**every** published unit-month carries all 32 `artifact_*_pct` metrics: 235 of 235 country
unit-months and 1,188 of 1,188 subregion unit-months. **114 of 121** countries and **536** subregions
(including all 52 US units) publish all 32 in **both** months, and all 114 countries also carry the
AUI; subregions **do** carry these metrics at `overall` (the `pct`-only rule bites inside the
ladders). No counts: pool as the unweighted April–May mean and admit only both-month units, with a
`pct` ≥ 0.5 floor wherever a ratio is formed. Log (g) 3.

**LL-32. FEASIBLE WITH CAVEAT: the answer is almost certainly "the rule barely matters", and the
effect size is the finding.** In the O\*NET 20.1 statements a task text has one holder occupation for
all but **72 / 91 / 84** tasks — **4.05% / 5.57% / 4.50%** of named usage mass (the flat family: 84
tasks, 2.56%). Equal-split, employment-weighted and modal-holder allocation move the SOC-15 share by
**≤0.17 pp** and the 22-group ranking by at most **one** position (Aug 2025) or **none** (Nov, Feb).
Publishable as a bound on a construction choice, not as a correction. Log (g) 4.

**LL-33. FEASIBLE WITH CAVEAT: there is one residual node, not two.** `collaboration_pct` sums to
exactly 100 in all six long-wave frames, but `not_classified` is **0.0001 / 0.0015 / 0.0001** where it
exists and **absent entirely** from Nov Claude.ai, Feb Claude.ai and Feb API. The substantive
residual is `none`: Claude.ai 3.8609 → 2.9612 → 3.0490 against 1P API **10.2116 → 11.0413 →
15.1944**. June cannot be added — no `not_classified` metric exists, its patterns sum to 99.99/100.01,
and the API population changes at that boundary. Log (g) 6.

**LL-34. NOT FEASIBLE: three changes move together, there are no counts, and the two files are not a
panel — recommend deletion.** The bound does exist and is large: 2,781 common task names (97.35% /
98.11% of each file's mass), total-variation distance **27.24 pp** on the renormalised common set,
largest single-task move 1.85 pp, Spearman 0.7475, with 733 v1-only and 584 v2-only tasks. But v1 **is**
the December-2024 release, so model, classifier and occupational-relevance filter all differ, and
neither file publishes a count, so nothing about a launch is identified. The question survives where
the taxonomy is fixed on one side: **LL-39**. Log (g) 7.

**LL-35. FEASIBLE.** **113** countries clear 200 conversations in all three waves (Aug 2025, Nov 2025,
Feb 2026) and **all 113** carry `task_success` at country grain in Feb 2026. The ISO-3 (enriched) →
ISO-2 (raw) bridge through `iso_country_codes.csv` is clean for all 115 Aug-2025 thresholded
countries, **0 unmapped**; filter on `geography`, never on `geo_id` alone (`ATLAS §Traps 41`). Carry
the `not_classified` share beside every rate as your entry already says. Log (g) 8.

**LL-36. FEASIBLE — and the reconstruction gap you feared is 0.02 pp.** Rebuilding SOC major group 15
from global `onet_task_pct` through the shipped O\*NET 20.1 statements gives, for August 2025,
**39.03%** (classified base) and **35.86%** (all-conversation base) against the published
`soc_occupation` facet's **39.0412%** and **35.8771%**. Series: Claude.ai 39.03 → 36.02 → **32.23**
(classified); 1P API 49.98 → 51.73 → 51.61, i.e. 45.67 / 46.60 on the all-conversation base —
the published "~46%" and "34–35%" both reproduce once the base is named. Log (g) 5.

**LL-37. FEASIBLE WITH CAVEAT: the panel is the right base, and the two flat windows can enter only on
names.** The three-wave matched panel is **2,282 named nodes** carrying **90.94 / 91.27 / 90.30** of
each wave's task mass — a sound trigger base. By task name, **1,988** of those nodes appear in
`task_pct_v2.csv` (92.27% of its mass) and **2,015** in `_v1.csv` (91.97%), with **1,868** in all five
windows; but the flat waves have no counts, no geography and a different relevance filter, so they
enter as shares only. June admission rule: a share-based trigger may use June as a **terminal
cross-section** only — no counts to weight it, and the `onet` taxonomy changed, so the matched panel
stops at Feb 2026. Log (g) 9.

**LL-38. FEASIBLE WITH CAVEAT: the list is nearly complete — there are two more observable dials, and
both are classifier judgements.** ψ, m (0.116534 at BLS-EP weights), a (the two time primitives, hours
÷ minutes in **both** 2026 waves per the trap-8 refinement), d (external BTOS only) and the
unmeasurable frictions are right. What you have missed, if you want them: **`human_only_ability`**
(global `yes` 87.91 → 87.76 — the Index's nearest observable to "share of tasks AI could do") and
**`task_success`** (66.91 → 69.94, the natural discount on a); `ai_autonomy` is a third, but it breaks
at the June boundary. None is a model parameter, so each enters as a bound, not an estimate.
Log (g) 10, `## Components`.

**LL-39. FEASIBLE — here is the spine.** Claude.ai global, Feb 2026 against the April–May mean.
*Comparable (moves < 1.1):* `human_only_ability_pct` −0.06, `human_education_years_mean` −0.08,
`collaboration_none_pct` −0.45, `use_case_work_pct` −0.79, `collaboration_directive_pct` −1.09.
*Comparable only with the break stated (1.8–5.7):* validation −1.78, personal −2.95, coursework
+3.78, feedback loop +4.46, task iteration +4.56, learning −5.70. *Breaking:* `ai_autonomy_mean`
−0.68, `ai_education_years_mean` +0.63, `human_only_time_mean` +1.60 h, `human_with_ai_time_mean`
+25.08 min, **`multitasking_pct` +12.72 pp**. *Absent in June:* **`task_success`** (no such metric
id), all counts, all `not_classified` nodes. *Not comparable by construction:* `onet` node counts
(3,260 vs 2,451 / 2,757) and the entire `request` ladder. June admission rule: report magnitudes with
no tests, and require April and May — the only within-wave replication — to agree in sign and size.
Log (g) 10.

**LL-40. FEASIBLE WITH CAVEAT — and plainly: the internal half *is* our atlas restated.** The
accounting itself (counts against `_pct` sums, floors of exactly 15, denominators 964,494 / 999,875 /
1,000,000, the `none`/`not_classified` mass by grain, June's 82.03 / 87.49 shortfall) is already in
`ATLAS §Thresholds` wave by wave; assembling it across waves is a table, not a finding. The
contribution has to be the external leg, and that leg is **now available**: OpenAI's Signals bundle
fetches (200, 25 CSVs, 24 months, 125 countries, 165 O\*NET IWAs) and Microsoft's diffusion and
`working-with-ai` files are already verified — and **149 of OpenAI's 165 IWA ids match the June wave's
`onet` level-2 node ids**, so a like-for-like disclosure comparison is constructible rather than
rhetorical. Keep it only with that leg as the confirmatory object. Log (g), `## Supplementary sources`.

**LL-41. FEASIBLE — and the sweep can run in the report's own unit.** `onet_task_count` is published,
so "at least 200 observations in our sample of 1M" is applicable exactly rather than as a share.
Nov 2025: 3,168 tasks / 93.51 mass / **11.93×** at the ≥15 floor → **578 / 79.65 / 11.83×** at ≥200 →
139 / 61.24 / 11.59× at ≥1,000. Feb 2026: 3,258 / 92.97 / **12.71×** → **616 / 78.41 / 12.62×** →
148 / 58.13 / 12.25×. The speedup is therefore near-invariant to the threshold (0.34× / 0.46× over
that whole range), so the published 1.8pp → ~5pp sensitivity lives in the coverage-and-weighting step.
Confirmed: the aggregate itself cannot be rebuilt — it needs conversation-level speedups and a
wage-bill weighting no release ships. Log (g) 11.

**LL-42. FEASIBLE WITH CAVEAT: neither of your two options is needed — the premise is wrong.** All
three quantities co-exist in **`release_2026_01_15`**: 118 countries clear 200 conversations, **117**
have a working-age population row (so the AUI is rebuildable on the symmetric, thresholded-only rule,
`ATLAS §Conventions`), **116** of those carry IMF 2024 GDP, and all **116** carry `use_case` and
`request` L2 at country grain (114 carry `onet_task`). The population and GDP files are static 2024
annuals, not wave quantities, so pairing them with the November wave is **not** a splice. Ruling:
decompose inside 2026-01-15 at N = 116; do **not** splice a later `use_case` mix onto the Aug-2025
income axis. Log (g) 12.
