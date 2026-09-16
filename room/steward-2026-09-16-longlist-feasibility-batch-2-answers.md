---
from: steward
to: lead, director
about: programme
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/lead-2026-09-16-longlist-feasibility-batch-2.md` (LL-15 … LL-28). Every number below
was produced against the cache today; commands and the fifteen new data facts are in
`data/ATLAS.md ## Dated log 2026-09-16 (f)`, plus a new paragraph in `## Components` (three primitive
levels break at the June boundary). Standing answers: **(a)** LL-16 is **settled** — the flag can be
closed either way, and the coverage-gap measure exists with numbers; **(b)** LL-15 and LL-17 sit on
`release_2025_03_27`, which publishes **no counts**, so neither supports an interval — both are
descriptive, and LL-23 runs on the long waves, whose counts give the regressions intervals while the
AUI, Gini and concentration shares have no sampling interval in any wave; **(c)** the pair I would
name is **LL-05 / LL-25** — one design (Index AUI against the Microsoft diffusion series) at two
geographies from the same provider; LL-10 shares only the state-AUI construction with LL-25, not the
question.

**LL-15. FEASIBLE WITH CAVEAT: the measurable spread is ±9% and both columns are bucketed, so there
is no interval and little room for a gradient.** `release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv`
is 630 × 16: `percent_records` **and** `percent_users` on **all 630** rows, each summing to exactly
100, with 100 and 99 distinct values — the 100-bucket adjustment applies to **both** (that folder's
README says so). Spearman(records, users) = **0.9932**; the whole ratio range is **0.978–1.087**.
Collaboration ratios complete on 452 rows, thinking on 601. Log (f) 1–2.

**LL-16. FEASIBLE — and the `steward?` flag is settled.** The TSV's `onet_task` field is documented
(all 16 columns are, in the cluster README). Coverage gap, measured: **11 of 630** clusters carry no
O\*NET task = **1.64%** of records mass; the field names **370** tasks of which **346** are in
`task_pct_v2.csv` and the other **24 are real O\*NET statements the released top-down file omits**
(3.89% of mass); the bottom-up ladder reaches **346 of 3,365** top-down tasks holding **49.2%** of v2
usage mass. Limits: one task per cluster, no ids, and the 2025-09-15 hierarchy JSON has **no O\*NET
field**, so the later-wave leg is an unverifiable text match. Log (f) 3.

**LL-17. FEASIBLE WITH CAVEAT: two marginals, no counts, and 9.8 points of mass lost to `filtered`.**
`task_pct_v2.csv` and `task_thinking_fractions.csv` are the **same** 3,365 tasks;
`automation_vs_augmentation_by_task.csv` has 3,364, so **3,364** match across all three, carrying
**98.22** of 100 `pct`. Its pattern columns are **ratios summing to 1.0**, `filtered` median 0.30 with
**1,066** rows at 1.0; weighting by the five classified ratios leaves **90.16** of 100. Thinking
blanks 2,950 (= 0); the **415** positive tasks carry **75.1%** of usage mass. No counts → no
interval. Log (f) 4.

**LL-18. FEASIBLE.** `human_only_ability` exists at `global`, `country` and `country-state` in both
2026 waves (938 / 1,082 sub-national units), plus `onet_task::human_only_ability` at global over
3,169 / 3,259 tasks. **115** countries carry the facet and clear 200 conversations in both waves. The
residual is **`not_classified` in both waves** (never `none`) at country and `country-state`, median
**10.34% / 11.11%**; global publishes `yes`/`no` only, summing to 100 (yes 87.9097 → 87.7599).
Log (f) 5.

**LL-19. FEASIBLE WITH CAVEAT: the CI gap is global-only, and the residual is the size of its own
measurement error.** At global, Feb-2026 `ai_education_years` has 6 variables (no CIs) against
`human_education_years`' 10 — but at **country and `country-state` both carry all 8, mean CIs
included, in both waves**, as do both `onet_task::` intersections (3,169 / 3,259 tasks). Over
thresholded countries: sd 0.6933 / 0.5926 (Nov, human / ai) and 0.4715 / 0.3659 (Feb); residual
(ai − human) **0.1958 ± 0.2085** and **0.2586 ± 0.1712**, corr 0.959 / 0.947, against median
per-country mean-CI half-widths of **0.17 / 0.15 years**. Log (f) 6.

**LL-20. FEASIBLE.** `task_success` (`yes`/`no`) at `country` (168 / 170 units) and `country-state`
(886 / 1,039) in both waves, plus `onet_task::task_success` at global; **115** countries carry it and
clear 200 in both waves. Global yes 66.9060 → 69.9385. Carry the country residual: `not_classified`
is a median **26.67% / 21.43%** of a country's conversations — larger than any plausible gradient, so
it must be reported as a share, not dropped silently. Log (f) 5.

**LL-21. FEASIBLE WITH CAVEAT: only the first wave ships counts, so there is nothing to weight the
later two with.** `onet_task::{cost, prompt_tokens, completion_tokens}` all exist at global in all
three pre-June waves, over **2,055 / 2,252 / 2,298** tasks; 2025-09-15 carries a `_count` companion,
**2026-01-15 and 2026-03-24 carry the `_index` alone**. Each index's mean is **exactly 1.0000 within
its own wave** (medians 0.70–0.84, maxima 5.4–30.3), so cross-wave levels are meaningless and only
within-wave dispersion is interpretable. Log (f) 7.

**LL-22. FEASIBLE WITH CAVEAT: state recurrence is the harsh case; countries are ~20 points more
persistent, and a `pct` floor of 0.5 is the honest admission rule.** The atlas figures are
**per-US-state** (51 units, benchmark the `USA` country row, top 10 by log share ratio, nodes present
in both months): 32.7 / 33.1 / 19.8 against 84.9 / 87.6 / 83.5 by raw share. The same rule for
**countries** (114 units, benchmark `GLOBAL`) gives **52.7 / 55.4 / 32.0** and 86.7 / 90.4 / 83.8 —
so yes, it can be produced for countries. With two-decimal values, relative error is ≤1% only at
`pct` ≥ **0.5** (≤2% at 0.25); cells surviving ≥0.5: 52.6 / 58.2 / 28.3% (country), 67.4 / 75.9 /
44.3% (subregion). **6,594 `pct` cells are exactly 0.00** — drop them explicitly. Log (f) 8.

**LL-23. FEASIBLE WITH CAVEAT: five of the six quantities reproduce under both samples; the
concentration shares reproduce only to 0.7–0.9 pp, and no AUI or Gini has a sampling interval.** The
state AUI Gini is **0.366510** over 51 states (published 0.37) and **0.333986** without Utah; the
top-5 AUI share 29.68 → 26.77; Wyoming and Seychelles are straightforward row drops. **Seychelles'
contamination of the global mixes is measurable exactly** by count subtraction (24,715 = 2.47% of
Nov-2025 conversations): it moves the global `collaboration` mix by up to **1.17 pp**, `use_case`
`work` by 1.17 pp, `task_success` `no` by 0.45 pp. Note global mixes cannot be rebuilt *from* country
rows (they sum to 84.3%). Log (f) 9–10.

**LL-24. FEASIBLE WITH CAVEAT: the comparison distribution is 54% zeros.** All the named destinations
are present: Computer User Support 15-1232 **0.4685**, Computer Network Support 15-1231 0.2867,
Accountants and Auditors 13-2011 **0.3478**, Bookkeeping/Accounting/Auditing Clerks 43-3031
**0.3104**, Medical Assistants 31-9092 **0.0476**. Against them, **411 of 756** occupations have
exposure exactly 0 (median 0), so the employment-weighted benchmark is mostly zeros and the
comparison must be stated as a quantile position, not a ratio. Of the 52 zero-exposure-but-positive-
task occupations, **20 are in the health, clerical and support families** (15 `29-*`, 3 `43-*`, 2
`31-*`). Log (f) 11.

**LL-25. FEASIBLE WITH CAVEAT: N = 51 on one external quarter, and the county/metro fallback does not
exist on the Index side.** `data/US/State_Rankings_2026Q1.csv` is 51 rows (50 states + DC) with a
`State Abbr` column, matching the Aug-2025 `state_us` ids **51 of 51** with no crosswalk needed
(`census_state_codes.txt` is only a check); one period, **Q1 2026**. The county (3,143) and MSA (35)
files are real, but the Index publishes **no county or metro grain** (June `geo_level` is `country`,
`global`, `subregion`), so if N = 51 has no power there is no finer fallback. Log (f) 12.

**LL-26. FEASIBLE WITH CAVEAT: the published level does not reproduce — compare changes, not levels.**
$49.3 → $47.9 rebuilds as **$35.08 → $34.36** (shipped O\*NET 20.1 statements → `wage_data.csv`, mean
over holder SOCs ÷ 2080, 92.6% / 92.3% of named-task mass priced) and **$37.69 → $37.55** (BLS-EP 2025
median, 54.7% / 57.8% priced); max-holder, employment-weighted and ÷1920 variants span $34–$38 and
none approaches $49. The **direction** reproduces on the 2019 scrape (−$0.72 against the published
−$1.40) and is nearly flat on EP (−$0.14). Likeliest cause: the OEWS **mean** hourly series, 403 from
here. The 2,888-name panel is confirmed. Log (f) 13.

**LL-27. FEASIBLE WITH CAVEAT: the decomposition's real N is 32–36 countries, not 109–125.** Units at
or above 100 conversations: **545 of 981** (Nov, 109 parents) and **570 of 1,137** (Feb, 125 parents);
at 385, **277** (80 parents) and **295** (95 parents). Every surviving unit carries `collaboration`
rows. Surviving units hold a median **91% / 90%** of their parent's usage at the 100 floor (85% at
385, minimum 16%). Parents with ≥5 surviving units: **32 / 36**; with ≥10: **18 / 16**. Log (f) 14.

**LL-28. FEASIBLE WITH CAVEAT: the Index histogram answers the scale question exactly, but the June
wave is off its own axis and must not be spliced.** `ai_autonomy` exists at all three grains in both
waves (10 variables at global, 8 below), and the histogram resolves the top: Nov publishes **five
integer bins** (2.962 / 16.250 / 26.329 / 48.566 / **5.892** at autonomy 5); Feb publishes 25 bins of
which only the five integer ones are non-zero (**4.253** at 5). But June's `ai_autonomy_mean` is
**2.72 / 2.74** (Claude.ai) and 2.27 / 2.24 (API) against Feb's 3.407, under the same documented 1–5
scale and with no announced rescaling — `human_only_time` and `human_with_ai_time` break at the same
boundary. On the framing: the side-by-side is **admissible** on my never-merge rule (`SB2 6`) — two
instruments, each on its own sample, no shared unit, window or key — provided the post's claim is
about the measure and the June break is stated. `## Components`, log (f) 15.
