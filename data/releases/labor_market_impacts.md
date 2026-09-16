# `labor_market_impacts/` — release profile

Folder of the Hugging Face dataset `Anthropic/EconomicIndex`, revision
`2ea58ff75e4247d26810c37f10c179edc2466cac` (pinned in `data/releases/INDEX.md`). Two CSVs, no
`README.md`, no `data_documentation.md`, no code, no date in any file name.

Accompanying publication (not in the folder): **"Labor market impacts of AI: A new measure and
early evidence"**, Maxim Massenkoff and Peter McCrory, 5 March 2026,
<https://www.anthropic.com/research/labor-market-impacts> (Figure 7 corrected 8 March 2026),
report PDF `https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf`,
**appendix PDF** `https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf`.
The appendix is the only published specification of the two metrics; there is no released code
for this folder, so every specification below is stated explicitly and marked as *mine* where I
had to choose it.

**Vintage (establishable, two of three layers).**
Usage layer: the August 2025 and November 2025 Economic Index waves — appendix footnote 5, "We
use the previous two Anthropic Economic Index datasets, covering usage from August and November
2025", i.e. `release_2025_09_15` (window 2025-08-04→11) and `release_2026_01_15` (2025-11-13→20);
the work-related restriction uses the `use_case` primitive introduced in the September file and
is imputed from embeddings for August (footnote 1).
Task layer: **O\*NET database 27.0–27.3** — the 17,992 distinct task strings in
`task_penetration.csv` are *set-identical* to the Task Statements of db 27.0, 27.1, 27.2 and 27.3
(zero on either side), and all 756 occupation titles in `job_exposure.csv` match O\*NET 27.2
`Occupation Data.txt` exactly (V14, V15). Cannot be narrowed inside 27.x — the four sub-versions
share one task set; Eloundou et al. (2023), whose β enters the metric, used 27.2.
Capability layer: Eloundou et al. (2023) β, not shipped and not retrieved (see Traps).
The files themselves carry **no date, version or provenance column** — the vintage above comes
from the appendix and from the O\*NET set match, not from the data.

## Files

| file | bytes (INDEX.md) | bytes on disk | sha256 |
|---|---:|---:|---|
| `labor_market_impacts/job_exposure.csv` | 37,176 | 37,176 | `4f0a3adf5feeb2ec5f5d02ab18cc5e851a2a4b8470bde84c0c9335017be12d68` |
| `labor_market_impacts/task_penetration.csv` | 1,889,822 | 1,889,822 | `85bee872db1d55d3e9a7f4e89da5ae4a5d59aa8ec875d728fbf4b7d820984616` |

Fetched and checksummed by `data/fetch/labor_market_impacts.py` into
`data/cache/labor_market_impacts/` (gitignored); re-running is a no-op (V1, V2). Both files are
plain ASCII, LF line endings, no BOM, RFC-4180 quoting of fields containing commas; neither
exceeds the 20 MB Parquet threshold of `data/fetch/README.md`, so no Parquet sibling is written
(V3). There is **no licence file in the folder**; the dataset card governs (data CC-BY, code MIT —
see `data/releases/INDEX.md` Discrepancy 2).

## Schema

`job_exposure.csv` — 756 data rows × 3 columns, header `occ_code,title,observed_exposure` (V4).

| column | dtype (pandas default) | example values | notes |
|---|---|---|---|
| `occ_code` | object (str) | `11-1011`, `15-1251`, `53-7121` | detailed **2018 SOC / O\*NET-SOC 27.x** code, 7 chars, always `\d{2}-\d{4}`; never an aggregate code (none ends in `0`) (V5) |
| `title` | object (str) | `Chief Executives`, `Computer Programmers`, `Medical Records Specialists` | O\*NET 27.2 occupation title, verbatim (756/756 exact match, V15); unique |
| `observed_exposure` | float64 | `0.0333`, `0.1378`, `0.0`, `0.7451` | 4 decimal places exactly, no scientific notation, no blanks (V6) |

`task_penetration.csv` — 17,998 data rows × 2 columns, header `task,penetration` (V4).

| column | dtype | example values | notes |
|---|---|---|---|
| `task` | object (str) | `Accept and check containers of mail from large volume mailers, couriers, and contractors.` | O\*NET task statement verbatim, trailing period always present, quoted when it contains a comma; **not unique** (V8) |
| `penetration` | float64 | `0.0`, `0.5`, `0.7239`, `0.9776`, `1.0` | 4 decimal places exactly; support is `{0} ∪ [0.5, 1.0]` (V9) |

Rows are sorted: `job_exposure` by `occ_code` ascending, `task_penetration` by `task` ascending
(byte order, so upper-case variants sort before lower-case ones) (V7).

Read both with `keep_default_na=False` as house rule; here it changes nothing — **no field is
empty, no field is the string `NA`, `NaN` or `nan`** in either file (V6). This is the one release
where the "`NA` is Namibia" trap does not apply.

## Grains

- `job_exposure.csv`: **one row per detailed SOC occupation.** `occ_code` is a key — 756 rows,
  756 distinct codes, 756 distinct titles, zero duplicates (V5).
- `task_penetration.csv`: **one row per O\*NET task statement — but the file is not keyed on it.**
  17,998 rows, 17,992 distinct task strings; two strings appear four times each (V8):
  `Write interesting and effective press releases, … internet or intranet Web pages.` and the
  same string with lower-case `web pages`. In O\*NET 27.2 each of these appears exactly once
  (for 11-2033 Fundraising Managers and 11-2032 Public Relations Managers respectively) (V16), so
  the fourfold repetition is a defect of this file, not of O\*NET. All four copies of each carry
  the same value (0.7263), so `drop_duplicates('task')` is lossless.
- **There is no row linking the two files.** `task_penetration.csv` carries no `occ_code`, no
  `Task ID` and no `O*NET-SOC Code`; `job_exposure.csv` carries no task list. The task→occupation
  map must be supplied from an external O\*NET 27.x download (V14).

## Facets or categories

There are **no facet columns**. The only categorisation available in-file is derived:

- **SOC major group** = `occ_code.str[:2]`. 22 groups present (11, 13, 15, 17, 19, 21, 23, 25, 27,
  29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53) — i.e. every major group except 55 Military
  (V10). Counts, zero counts and unweighted means per group:

| major group | n | zeros | mean exposure | max |
|---|---:|---:|---:|---:|
| 11 Management | 35 | 9 | 0.0974 | 0.3907 |
| 13 Business & Financial | 29 | 4 | 0.1766 | 0.6483 |
| 15 Computer & Mathematical | 21 | 0 | 0.3787 | 0.7451 |
| 17 Architecture & Engineering | 34 | 15 | 0.0381 | 0.1453 |
| 19 Life, Physical & Social Science | 46 | 10 | 0.1219 | 0.4520 |
| 21 Community & Social Service | 12 | 6 | 0.0516 | 0.1530 |
| 23 Legal | 7 | 0 | 0.2158 | 0.3109 |
| 25 Education | 57 | 18 | 0.1293 | 0.4305 |
| 27 Arts, Design, Entertainment, Sports & Media | 34 | 10 | 0.1424 | 0.4747 |
| 29 Healthcare Practitioners | 65 | 40 | 0.0411 | 0.6674 |
| 31 Healthcare Support | 16 | 11 | 0.0494 | 0.6365 |
| 33 Protective Service | 21 | 17 | 0.0119 | 0.1234 |
| 35 Food Preparation & Serving | 15 | 12 | 0.0094 | 0.0734 |
| 37 Building & Grounds | 8 | 5 | 0.0247 | 0.1083 |
| 39 Personal Care & Service | 27 | 19 | 0.0191 | 0.1875 |
| 41 Sales | 20 | 3 | 0.2361 | 0.6279 |
| 43 Office & Administrative Support | 50 | 10 | 0.1906 | 0.7011 |
| 45 Farming, Fishing & Forestry | 11 | 10 | 0.0018 | 0.0203 |
| 47 Construction & Extraction | 56 | 49 | 0.0040 | 0.0491 |
| 49 Installation, Maintenance & Repair | 50 | 43 | 0.0071 | 0.1067 |
| 51 Production | 98 | 80 | 0.0078 | 0.1207 |
| 53 Transportation & Material Moving | 44 | 40 | 0.0065 | 0.1169 |

(V10; totals 756 rows, 411 zeros.) The report's "occupational categories" in Figures 2 and 5 are
these major groups, but note the report's category means are **employment-weighted** (see
Reproduced published numbers).

## Metrics

Both metrics come from the appendix; neither is documented in the folder.

- **`penetration` = task-level observed exposure r̃ₜ** = βₜ · αₜ · 1{WorkUsageₜ ≥ gate}, where
  βₜ is Eloundou et al. (2023) capability **upgraded to 1 whenever β > 0** (so β ∈ {0, 0.5, 1}
  becomes {0, 1}), and αₜ ∈ [0.5, 1] up-weights automative use: "A task that sees only
  augmentative uses and does not appear in the API transcripts would have αₜ equal to 0.5 …
  A task with only automative uses would have αₜ = 1." The data match this algebra exactly: the
  observed support is `{0} ∪ [0.5, 1.0]`, with **no value strictly between 0 and 0.5** (V9). So a
  positive `penetration` *is* αₜ, and 204 tasks sit at exactly 1.0, 4 at exactly 0.5.
- **`observed_exposure` = job-level measure** = Σ_{t∈T_o} w_t · r̃ₜ, with w_t the fraction of time
  the occupation spends on task t (Tamkin and McCrory 2025). **w_t is not published anywhere in
  the dataset**, so `observed_exposure` cannot be rebuilt from `task_penetration.csv`. What can be
  checked holds: no occupation's exposure exceeds the maximum penetration of its O\*NET 27.2 tasks,
  and no occupation with exposure > 0 lacks a positive-penetration task (0 violations of each,
  V17). Spearman correlation between `observed_exposure` and the unweighted mean penetration of
  an occupation's tasks is 0.873 (Pearson 0.826) — i.e. the time weights matter a lot (V17).
- Units: both are shares in [0, 1], not percentages. The report quotes them as percentages
  ("75% coverage" = 0.7451). Neither is a probability of job loss; the appendix warns the
  automation weighting means it "is not a pure percentage of task coverage".

## Thresholds

Unlike every other Economic Index release, **the thresholds here are already applied in the
public file.** Do not apply another one.

- **Usage gate (applied):** "WorkUsageₜ must be 100 or 0.0025% of traffic … Tasks that do not meet
  the gate of WorkUsageₜ ≥ 100 are assigned an exposure of 0" (appendix, and footnote 3: 100 of
  4M conversations = 0.0025%, which checks arithmetically, V18). Effect in the file: **16,644 of
  17,998 task rows (92.48%) are exactly 0**; only 1,354 (7.52%) are positive (V11).
- **Capability gate (applied):** β = 0 ⇒ r̃ = 0. Indistinguishable in the file from the usage gate —
  there is no β column and no flag.
- **Floor created by the α definition (applied):** any task passing both gates has r̃ ≥ 0.5.
- **No privacy/suppression threshold is documented and no suppression flag exists.** The appendix
  mentions a "privacy threshold for inclusion in the data" only when describing a Ridge-imputation
  robustness check, which is not the released measure.
- **Occupation-level:** no threshold is visible; but 52 occupations have `observed_exposure` = 0
  while having 1–10 positive-penetration tasks (V19), which the two gates above cannot explain —
  most plausibly missing time-fraction weights w_t. Treat a zero in `job_exposure.csv` as
  "no measured exposure", never as "no tasks used".

## Coverage counts

`job_exposure.csv` (V6, V10, V11):
- 756 occupations, 0 missing values in any column, 22 SOC major groups, 0 aggregate codes.
- `observed_exposure`: min 0.0, max 0.7451, mean 0.076977, median 0.0, sd 0.1332; p75 0.0957,
  p95 0.3850, p99 0.5748; 329 distinct values.
- 411 occupations (54.37%) at exactly 0; 345 positive; 86 above 0.25; 11 above 0.5; **none above
  0.75** (the maximum, Computer Programmers, is 0.7451).

`task_penetration.csv` (V6, V11):
- 17,998 rows / 17,992 distinct tasks / 0 missing values / 0 empty strings.
- `penetration`: 16,644 zeros (92.48%), 1,354 positive (7.52%), min positive 0.5 (4 tasks),
  max 1.0 (204 tasks), mean 0.066744, median 0.0; 870 distinct values (869 of them positive).
- 150 positive values are shared by more than one task, covering 635 tasks; the most common is
  **0.7239, carried by 100 semantically unrelated tasks** (V12).

Cross-file coverage against O\*NET 27.2 (V14, V17, V19):
- All 19,265 O\*NET 27.2 task rows join to `task_penetration.csv` on the task string; 0 unmatched.
- All 756 `occ_code`s exist in O\*NET 27.2 (798 detailed codes); **42 O\*NET occupations are absent
  from `job_exposure.csv`** — including Fundraising Managers, Project Management Specialists,
  Home Health Aides, Personal Care Aides, Mental Health Counselors, Team Assemblers. 17 of the 42
  do appear in the BLS projections table, so "no BLS employment" is not the exclusion rule; the
  rule is not establishable from public files.

Supplementary source used for the weighted reproductions: **BLS Employment Projections**,
`https://data.bls.gov/projections/occupationProj` (HTML table, 831 detailed-SOC rows, employment
2025 and 2035 in thousands, percent change, median annual wage 2025, education/training; US
Government work, public domain). Joins on `occ_code`: 756 in, **755 matched, 1 unmatched
(11-1031 Legislators)**, 154,223.4 thousand workers covered (V20). `www.bls.gov` and
`download.bls.gov` return **403** to this sandbox (OEWS zip, ind-occ-matrix xlsx), and
`web.archive.org` is blocked by egress policy, so the **2024–2034 projections vintage used in the
report could not be retrieved** (V21). O\*NET database text zips download without a key from
`https://www.onetcenter.org/dl_files/database/db_<v>_text.zip` (CC BY 4.0) (V13).

## Reproduced published numbers

My specification, stated once and used throughout: occupation-level values are taken verbatim from
`job_exposure.csv`; where the report weights by employment I use **BLS EP employment 2025**
(the report used "current employment" from the 2024–34 vintage and, for worker shares, CPS
2022 — neither is available to this sandbox); occupational categories are SOC major groups.

| # | published (source) | my value | match |
|---|---|---|---|
| 1 | Computer Programmers "at the top, with 75% coverage" (Fig. 3) | 0.7451 = 74.51% → 75% | **exact** (V22) |
| 2 | Data Entry Keyers "are 67% covered" (Fig. 3) | 0.6707 = 67.07% → 67% | **exact** (V22) |
| 3 | Order: Programmers, then Customer Service Representatives, then Data Entry Keyers (Fig. 3) | 0.7451, 0.7011, 0.6707 | **exact**; full top ten also: Medical Records Specialists 0.6674, Market Research Analysts 0.6483, Medical Transcriptionists 0.6365, Sales Reps Wholesale/Manufacturing 0.6279, Database Architects 0.5787, Financial and Investment Analysts 0.5716, Software QA Analysts 0.5195 (V22) |
| 4 | "The four highly exposed categories are: Computer & Mathematical, Office & Administrative Support, Business & Financial, and Sales" (appendix p.6) | employment-weighted major-group means rank 15 (0.3542), 43 (0.3381), 13 (0.2875), 41 (0.2750), then 23 Legal (0.2024) | **exact ranking** (V23). The **unweighted** ranking does *not* reproduce it: Legal would be third (0.2158 > 0.1906 = Office & Admin) |
| 5 | "the top quartile has … 31%" average observed coverage (appendix p.6) | employment-weighted mean over groups {15, 43, 13, 41} = **0.3117** | **matches to the published digit** (31.2% vs "31%") (V23) |
| 6 | "the bottom quartile has 1% coverage, on average" (appendix p.6) | bottom groups by weighted mean that fill a quarter of employment: {53, 51, 37} = 0.0045 (16.7% of employment), {53, 51, 37, 35} = 0.0060 (25.6%) | **near-miss, 0.5–0.6% vs 1%** (V23). Cause: the appendix's quartiles are over *CPS respondents* in DOL ETA-203 major-group categories, not BLS employment; the ordering of the groups is identical |
| 7 | "Claude currently covers just 33% of all tasks in the Computer & Math category" (Fig. 2 text) | 0.3542 employment-weighted (BLS 2025); 0.3787 unweighted | **does not reproduce, +2.4 pp** (V24). Cause: employment vintage/source — with 2024-vintage weights Software Developers (0.2880, the group's largest employer by far) carries more weight; no public weight set I can reach closes the gap |
| 8 | "30% of workers have zero coverage" (Fig. 3 text) | employment-weighted share of zero-exposure occupations = **0.3977**; unweighted share of occupations = 0.5437 | **does not reproduce, +10 pp** (V24). Cause: the report weights CPS respondents (Aug–Oct 2022) mapped through the Eckhardt–Goldschlag occ1990 crosswalk, which is not in the folder; CPS occupation shares differ materially from BLS projections employment |
| 9 | "For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points" (Fig. 4) | employment-weighted OLS of percent employment change on exposure: slope −7.687 per unit = **−0.77 pp per 10 pp**, intercept 4.05, N = 755; unweighted −0.057 pp per 10 pp | **directionally reproduces, magnitude 0.17 pp off** (V25). Cause: I regress the **2025–2035** projections (the live table) because the **2024–2034** vintage used in the report is unreachable (V21); the weighting variable also differs in vintage. Note the unweighted slope is an order of magnitude smaller — the published statement only holds employment-weighted, as the caption says |
| 10 | Appendix worked example: for "Identify, compile, abstract, and code patient data, using standard classification systems", "the automation factor is 0.96" | file value **0.9776** | **does not reproduce, +0.018** (V22). Both round to "high"; 0.9776 rounds to 0.98. Cause unknown — most likely a draft-vintage number or an α quoted before the final aggregation; there is no released code to arbitrate |
| 11 | Appendix footnote 3: "Usage of 100 represents 0.0025% of traffic … (2M from Claude.ai and 2M from 1P API)" | 100 / 4,000,000 = 0.0025% | **exact** (V18) |
| 12 | Appendix: "aggregate the 18,000 task statements"; page: O\*NET "enumerates tasks associated with around 800 unique occupations" | 17,998 rows / 17,992 distinct tasks; O\*NET 27.2 has 798 detailed occupations, of which the file covers 756 | **exact** for tasks; the "800" refers to O\*NET, not to this file (V11, V14) |

**Published numbers that cannot be reproduced from this folder at all** (inputs are not released):
Figure 1 shares of usage by β (68% β=1, 3% β=0, "97% … theoretically feasible") — needs per-task
usage counts *and* Eloundou β, neither of which is in the dataset; Figure 2's blue area (β = 94%
Computer & Math, 90% Office & Admin) — needs Eloundou β; Figures 5, 6, 7 and every unemployment,
hiring, wage, education and demographic number — needs CPS microdata plus the occ1990 crosswalk;
Appendix Figure 4's alternative measures (Ridge impute, DWA/IWA-level, coreweight, success-gated,
"Baseline × success") — none is released, only the baseline is. The nearest in-sandbox substitute
for the Figure 5 wage gap ("they earn 47% more") is BLS median annual wage 2025, employment
weighted: top-exposure quartile $70,630 vs zero-exposure $50,506 = **+39.8%**, a different
construct (occupational medians, not individual earnings) and a different year (V25).

### Which Economic Index waves this folder's usage layer is (added 2026-09-16)

Asked by `room/lead-2026-09-16-steward-questions-batch-2.md` Q8: which release folders and windows
are the appendix's "previous two Anthropic Economic Index reports (2M from Claude.ai and 2M from
1P API)" (note 3) and its "August"/"September" data (note 1). The appendix names neither. Both are
settled arithmetically from the files:

| appendix phrase | the folders it can only be | evidence |
|---|---|---|
| "2M from Claude.ai" | `release_2025_09_15` (4–11 Aug 2025) **+** `release_2026_01_15` (13–20 Nov 2025) | country `usage_count` sums **964,494 + 999,875 = 1,964,369** ≈ 2M. No other pair of released waves gets there: those are the only two Claude.ai waves with counts, and one wave alone is ~1M |
| "2M from 1P API" | the same two folders | `collaboration_count` sums **944,638 + 971,525 = 1,916,163** ≈ 2M. The 2025-09-15 wave is the first with a 1P API file, so these are the only two API waves that existed when the report was written |
| the 100-observation gate = "0.0025% of traffic" | the pooled 4M above | 100 / 4,000,000 = 0.0025% **exactly** — already item 11 of Reproduced (V18). The gate's denominator is the *pooled* Claude.ai + API traffic of both waves, not one wave and not one surface |
| "the August data", where the work share is **imputed** | `release_2025_09_15` | `use_case` is **absent** from that folder's facet set (7 facets: `collaboration`, `country`, `onet_task`, `onet_task::collaboration`, `request`, `request::collaboration`, `state_us`) — exactly the gap note 1 describes |
| "the September data", where the use-case primitive "was introduced" | `release_2026_01_15` | `use_case` **first appears** there, and in no earlier folder. **But that wave's window is 13–20 November 2025, not September** — no released file has a September window at all |

So the month labels are not data windows. "August" is the August 2025 window; "September" is the
wave that introduced `use_case`, whose window is November 2025 and whose *report* is January 2026.
The likeliest reading is that the authors named waves by an internal sample month; the alternative
— that they name them by publication month — fails too, because the August-2025-window wave was
published on 15 September 2025, which would make "the September data" the very wave that lacks
`use_case`. **Record both readings and do not assume a September sample exists.**

```bash
python3 - <<'PY'
import pandas as pd
d=pd.read_csv('data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv',
              keep_default_na=False,na_values=[],usecols=['geography','facet','variable','value'])
print('Aug Claude.ai %.0f'%d[(d.geography=='country')&(d.variable=='usage_count')].value.sum(),
      '| use_case present', 'use_case' in set(d.facet))
a=pd.read_csv('data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv',
              keep_default_na=False,na_values=[],usecols=['variable','value'])
print('Aug API %.0f'%a[a.variable=='collaboration_count'].value.sum())
e=pd.read_parquet('data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet',
                  columns=['geography','facet','variable','value'])
print('Nov Claude.ai %.0f'%e[(e.geography=='country')&(e.variable=='usage_count')].value.sum(),
      '| use_case present', 'use_case' in set(e.facet))
b=pd.read_parquet('data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet',
                  columns=['variable','value'])
print('Nov API %.0f'%b[b.variable=='collaboration_count'].value.sum())
PY
# -> Aug Claude.ai 964494 | use_case present False ; Aug API 944638
# -> Nov Claude.ai 999875 | use_case present True  ; Nov API 971525
```

### The scenarios-explorer anchor m: 0.12 reproduces, 0.14 does not (added 2026-09-16)

Asked by `room/lead-2026-09-16-steward-questions-batch-2.md` Q2. The explorer bundle defines its one
empirical anchor as "observed exposure, averaged over occupations … at CPS employment weights",
m = **0.14** at mid-2026, and records that it was **0.12** before mid-August 2026
(`wiki/reports/econ-scenarios-explorer-2026-09.md`). `observed_exposure` in this folder is exactly
that construct at exactly that grain — 756 detailed 2018-SOC occupations, no geography, no time.
Rebuilt with BLS Employment Projections 2025 base-year employment, the nearest public substitute
for CPS employment weights (BLS OEWS returns 403 to this sandbox and CPS microdata is not public
here):

| specification | value | verdict |
|---|---|---|
| unweighted mean over the 756 occupations — the phrase read literally | **0.076977** | not the anchor under any rounding |
| employment-weighted, denominator = the 755 occupations that match | **0.128658** | rounds to 0.13 |
| employment-weighted, denominator = **all** US employment, so occupations absent from the file count as zero exposure | **0.116534** | **rounds to 0.12 — the superseded anchor** |

Merge audit: 756 rows in, **755 matched**, 1 unmatched (`11-1031` Legislators, absent from the
projections table). Coverage 154,223 of 170,267 thousand jobs (90.6%).

Three conclusions. (i) The anchor is **occupation-grained and US-only**; there is no geography or
date at which it could be cut, so any scenario claim about a region or a year is outside this file.
(ii) The **0.12 vintage reproduces to rounding** on the all-employment denominator, so the
construct and this folder are almost certainly its source. (iii) **0.14 does not reproduce from any
released file, and cannot**: it is a *mid-2026* anchor, while this folder's usage layer is the
August + November 2025 waves, and **no 2026 release carries any exposure construct at all** — the
2026-03-24 folder has no `soc_occupation` facet and the 2026-06-26 folder has no exposure metric.
A mid-2026 exposure measure is unpublished. Treat 0.14 as an unreproducible model input, and say so
beside any use of the explorer.

For the related ψ question (Q3) the comparison is in `data/ATLAS.md §Conventions`: the Index's
observed automation share on the five-classified-pattern base — the base that matches ψ's
definition, since it excludes unaffected conversations — runs 42.55 / 43.06 / 51.07 / 46.74 /
45.55 / 48.98 / 48.62 across the six waves, i.e. **0.43–0.51, at or below the least disruptive
preset (ψ = 0.50) in every wave and never within 24 points of ψ = 0.75**.

```bash
python3 - <<'PY'
import pandas as pd
t=pd.read_html('/tmp/proj.html')[0]            # https://data.bls.gov/projections/occupationProj
t.columns=['title','occ_code','emp2025','emp2035','chg','pctchg','openings','wage','edu','exp','train','a','b','c'][:len(t.columns)]
t['emp2025']=pd.to_numeric(t.emp2025.astype(str).str.replace(',',''),errors='coerce')
t['occ_code']=t.occ_code.astype(str).str.strip()
j=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv', keep_default_na=False)
m=j.merge(t[['occ_code','emp2025']],on='occ_code',how='left')
print('merge: %d in, %d matched, unmatched %s'%(len(m),m.emp2025.notna().sum(),m[m.emp2025.isna()].occ_code.tolist()))
m=m.dropna(subset=['emp2025']); num=(m.observed_exposure*m.emp2025).sum()
print('unweighted %.6f | weighted/matched %.6f | weighted/all-employment %.6f'%(
      j.observed_exposure.mean(), num/m.emp2025.sum(), num/t.emp2025.sum()))
PY
# -> merge: 756 in, 755 matched, unmatched ['11-1031']
# -> unweighted 0.076977 | weighted/matched 0.128658 | weighted/all-employment 0.116534
```

## Cuts that do not exist

Plainly, and each verified by the column list (V4):

- **No geography.** No country, state, region or city column. The whole folder is implicitly US
  (O\*NET/SOC), and there is no US-vs-rest split, no state file, no sub-national anything.
- **No time dimension.** No date, window, wave, month or version column; no panel; no before/after.
  One cross-section of unstated width (August + November 2025 usage pooled).
- **No wage, employment, education or demographic column.** The report's Figure 5 characteristics
  come from the CPS, not from here. Bring your own BLS/CPS/ACS.
- **No usage counts.** No conversation counts, no task counts, no shares of traffic — the gate is
  applied and the evidence for it discarded.
- **No automation/augmentation split.** αₜ is baked into `penetration`; the underlying
  `AutoShareₜ` and the API-vs-Claude.ai split are not published.
- **No β column**, no capability rating, no `Task ID`, no `O*NET-SOC Code` in the task file.
- **No task→occupation link** in either file, and **no time-fraction weights w_t** — so the job
  measure is not decomposable and Figure 2's occupation-level averaging cannot be redone.
- **No uncertainty.** No standard errors, confidence intervals, sample sizes or suppression flags.
- **No alternative measures.** Only the baseline; the eight robustness variants of Appendix
  Figure 4 are described, not released.
- **No crosswalks.** No SOC-2010, occ1990, ISCO, NAICS or CPS mapping; no major-group labels (you
  derive them from the first two digits).
- **No 55 Military major group**, no aggregate/major-group rows, no "all occupations" total row.
- **No first-party-API vs Claude.ai, no Claude Code, no survey component** anywhere in the folder.

## Traps

1. **`task_penetration.csv` is not unique on `task`** (17,998 rows, 17,992 tasks). A naive merge
   of an O\*NET task table onto this file inflates two occupations' task lists fourfold. Always
   `drop_duplicates('task')` first; values are identical across copies, so nothing is lost (V8).
2. **Zeros conflate three causes** — β = 0, usage below the gate, and (for occupations) apparently
   missing time weights. 52 occupations have exposure exactly 0 while owning 1–10 tasks with
   positive penetration; 16 of them are in Education and 15 in Healthcare Practitioners, including
   twelve postsecondary teaching occupations, Kindergarten Teachers, Family Medicine Physicians,
   Psychiatrists and Legal Secretaries (V19). The published sentence "30% of workers have zero
   coverage, as their tasks appeared too infrequently" is therefore *not* the whole story; do not
   interpret a zero as "no observed AI use in this occupation's tasks".
3. **`penetration` is not a continuous 0–1 share.** Its support is `{0} ∪ [0.5, 1]` and a positive
   value is the automation weight α, not a usage share. Means, medians and correlations computed
   as if it were a share are meaningless; the mass at 0 is 92.5% (V9, V11).
4. **The O\*NET file shipped inside the Economic Index releases is the wrong vintage for this
   folder.** Joining `task_penetration.csv` to `release_2025_02_10/onet_task_statements.csv` (or
   the identical `release_2025_09_15/data/intermediate/onet_task_statements.csv`) matches only
   15,682 of 17,992 tasks and 670 of 756 occupation codes — that file predates the SOC-2018 codes
   this folder uses (it has no `15-1251`). Download O\*NET **27.x** instead: full match on both
   keys (V14).
5. **100 tasks share exactly the value 0.7239**, and 635 tasks sit on values shared by more than
   one task (V12). The 0.7239 group is semantically unrelated ("Assess employee performance",
   "Analyze equipment performance records…", "Answer customers' questions about services…"),
   which is consistent with a default or imputed automation factor rather than a measured one.
   This is a conjecture — nothing in the appendix documents it — but treat repeated values as
   non-independent observations in any task-level regression.
6. **Case-variant duplicate task strings exist** ("…intranet Web pages." vs "…intranet web
   pages."), in O\*NET as well as here — two different O\*NET tasks (IDs 21261 and 21245,
   belonging to two different occupations) that differ only in the case of one word (V16). Lower-
   casing task strings before a join silently collapses them into a many-to-many match.
7. **`occ_code` is 2018 SOC detail.** Matching to the CPS requires the Eckhardt–Goldschlag
   occ1990 crosswalk (report footnote 7, hosted at eig.org), which is not in the dataset; matching
   to OEWS/EP works directly but loses 11-1031 Legislators (V20).
8. **The folder is unversioned and undated.** Nothing in it would change if Anthropic rebuilt it
   on a later usage wave. Pin the sha256s in `data/cache/labor_market_impacts/CHECKSUMS.txt`
   (V1) and re-verify before reusing a number.
9. **Exposure has a low ceiling.** No occupation exceeds 0.7451 and only 11 exceed 0.5, so
   quartile-based "treated" groups are defined by a cut around 0.23 (worker-weighted), not by
   anything like "most of the job is automated" (V6, V25).
10. The "NA is Namibia" trap of the long releases does **not** apply here; no field is `NA`
    (V6). `keep_default_na=False` is still the house default and is harmless.

**Where the `economic-index-data` skill is wrong or incomplete about this folder.** The skill says
only: "`labor_market_impacts/`: `job_exposure.csv` (756 SOC occupations) and
`task_penetration.csv`." The 756 is correct (V5). Missing or misleading:
(a) the skill's headline convention "**Thresholds are not applied in the public files**" is
**false for this folder** — the ≥100 work-usage gate *is* applied, and 92.5% of task rows are
zeroed by it;
(b) the folder has no documentation and no code, so the appendix PDF (URL above) is the only
specification;
(c) the files support the 5 March 2026 labour-market report, not any of the six numbered Economic
Index reports, and their usage layer is the August + November 2025 waves;
(d) the task universe is O\*NET **27.x**, not the O\*NET file shipped in `release_2025_02_10`
(trap 4);
(e) `task_penetration.csv` is not unique on its only key column (trap 1);
(f) the `NA`-is-Namibia trap does not apply here.

## Verification

All commands run 2026-09-16 from the repository root, Python 3.11 / pandas 2.x. `je` and `tp`
below abbreviate the two loads in V4.

```bash
# V1 fetch, checksums, idempotence
python data/fetch/labor_market_impacts.py     # -> 2 fetched, 0 skipped, 1926998 bytes
python data/fetch/labor_market_impacts.py     # -> 0 fetched, 2 skipped (hash match)
(cd data/cache/labor_market_impacts && sha256sum -c CHECKSUMS.txt)   # -> both OK

# V2 byte sizes against data/releases/INDEX.md
stat -c '%s %n' data/cache/labor_market_impacts/*.csv   # -> 37176 …/job_exposure.csv; 1889822 …/task_penetration.csv

# V3 encoding, line endings, BOM, size threshold
file data/cache/labor_market_impacts/*.csv              # -> CSV ASCII text (both)
python -c "
raw=open('data/cache/labor_market_impacts/task_penetration.csv','rb').read()
print(raw.count(b'\r\n'), raw[:3]==b'\xef\xbb\xbf', sum(1 for b in raw if b>127))"   # -> 0 False 0

# V4 schema
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv', keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv', keep_default_na=False)
print(je.shape, list(je.columns), je.dtypes.to_dict())
print(tp.shape, list(tp.columns), tp.dtypes.to_dict())"
#   -> (756, 3) ['occ_code','title','observed_exposure'] {object,object,float64}
#   -> (17998, 2) ['task','penetration'] {object,float64}

# V5 key uniqueness and code shape (job_exposure)
python -c "
import pandas as pd; je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
print(len(je), je.occ_code.nunique(), je.title.nunique(),
      je.occ_code.str.fullmatch(r'\d{2}-\d{4}').all(), je.occ_code.str.endswith('0').sum())"
#   -> 756 756 756 True 0

# V6 missingness, ranges, rounding
python -c "
import pandas as pd, numpy as np
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False,dtype=str)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False,dtype=str)
for n,d in (('je',je),('tp',tp)):
    for c in d.columns: print(n,c,(d[c]=='').sum(),(d[c]=='NA').sum(),(d[c].str.lower()=='nan').sum())
je=je.astype({'observed_exposure':float}); tp=tp.astype({'penetration':float})
print(je.observed_exposure.describe(percentiles=[.75,.95,.99]).to_dict())
print(np.allclose(je.observed_exposure, je.observed_exposure.round(4)),
      np.allclose(tp.penetration, tp.penetration.round(4)))"
#   -> all zeros (no blanks, no 'NA', no 'nan'); mean 0.076977 max 0.7451 p95 0.38495 p99 0.574795; True True

# V7 sort order
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
print(je.occ_code.is_monotonic_increasing, tp.task.is_monotonic_increasing, tp.task.str.lower().is_monotonic_increasing)"
#   -> True True False

# V8 task_penetration is not unique on task
python -c "
import pandas as pd; tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
print(len(tp), tp.task.nunique()); print(tp[tp.task.duplicated(keep=False)].groupby(['task','penetration']).size())"
#   -> 17998 17992; two strings x 4 rows each, both at 0.7263

# V9 support of penetration = {0} u [0.5, 1]
python -c "
import pandas as pd; tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
p=tp.penetration; print((p==0).sum(), ((p>0)&(p<0.5)).sum(), p[p>0].min(), p.max(), (p==1).sum(), (p==0.5).sum())"
#   -> 16644 0 0.5 1.0 204 4

# V10 major groups
python -c "
import pandas as pd; je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
g=je.assign(mg=je.occ_code.str[:2]).groupby('mg').observed_exposure.agg(n='size',zeros=lambda s:(s==0).sum(),mean='mean',max='max')
print(g.round(4).to_string(), g.n.sum(), g.zeros.sum())"
#   -> the 22-row table above; 756 411

# V11 coverage counts
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
print((je.observed_exposure==0).sum(), (je.observed_exposure>0.25).sum(), (je.observed_exposure>0.5).sum(), (je.observed_exposure>0.75).sum(), je.observed_exposure.nunique())
print((tp.penetration>0).sum(), (tp.penetration>0).mean(), tp.penetration.nunique())"
#   -> 411 86 11 0 329 | 1354 0.0752 870

# V12 repeated positive values
python -c "
import pandas as pd; tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
vc=tp[tp.penetration>0].penetration.value_counts(); print((vc>1).sum(), vc[vc>1].sum()); print(vc.head(4).to_dict())"
#   -> 150 635 {1.0: 204, 0.7239: 100, 0.7263: 8, 0.972: 4}

# V13 O*NET database downloads (no key needed; CC BY 4.0)
mkdir -p /tmp/onet
for v in 27_0 27_1 27_2 27_3 28_0 28_3 29_1 30_0; do
  curl -sSL -A 'Mozilla/5.0' -o /tmp/onet/db_$v.zip "https://www.onetcenter.org/dl_files/database/db_${v}_text.zip" -w "$v %{http_code}\n"
  mkdir -p /tmp/onet/x$v && (cd /tmp/onet/x$v && unzip -oq ../db_$v.zip)
done   # -> all 200

# V14 vintage: task set identical to O*NET 27.x; EconomicIndex-shipped O*NET does not match
python -c "
import pandas as pd
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False); tt=set(tp.task)
for v in ['27_0','27_2','27_3','28_0','28_3','29_1','30_0']:
    d=pd.read_csv(f'/tmp/onet/x{v}/db_{v}_text/Task Statements.txt',sep='\t',keep_default_na=False,dtype=str)
    print(v, len(set(d.Task)), len(tt-set(d.Task)), len(set(d.Task)-tt))"
#   -> 27_0/27_2/27_3: 17992 0 0 | 28_0: 18008 21 37 | 28_3: 18008 57 73 | 29_1: 17536 543 87 | 30_0: 17538 558 104
curl -sSL -o /tmp/onet_2025_09_15.csv 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2025_09_15/data/intermediate/onet_task_statements.csv'
python -c "
import pandas as pd
on=pd.read_csv('/tmp/onet_2025_09_15.csv',keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
print(len(set(tp.task)&set(on.Task)), len(set(tp.task)-set(on.Task)),
      len(set(je.occ_code)&set(on['O*NET-SOC Code'].str[:7])))"
#   -> 15682 2310 670   (the shipped O*NET file is the wrong vintage)

# V15 titles match O*NET 27.2 exactly
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
od=pd.read_csv('/tmp/onet/x27_2/db_27_2_text/Occupation Data.txt',sep='\t',keep_default_na=False,dtype=str)
od['occ']=od['O*NET-SOC Code'].str[:7]; t=od.drop_duplicates('occ').set_index('occ')['Title']
print((je.set_index('occ_code').title==t[je.occ_code].values).mean(), len(je))"
#   -> 1.0 756

# V16 the duplicated strings appear once each in O*NET 27.2
python -c "
import pandas as pd
d=pd.read_csv('/tmp/onet/x27_2/db_27_2_text/Task Statements.txt',sep='\t',keep_default_na=False,dtype=str)
s='Write interesting and effective press releases, prepare information for media kits, and develop and maintain company internet or intranet Web pages.'
for x in (s, s.replace('Web pages','web pages')): print(d[d.Task==x][['O*NET-SOC Code','Task ID']].values.tolist())"
#   -> [['11-2033.00','21261']] and [['11-2032.00','21245']]

# V17 internal consistency of exposure against task penetration (merge audit printed)
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False).drop_duplicates('task')
on=pd.read_csv('/tmp/onet/x27_2/db_27_2_text/Task Statements.txt',sep='\t',keep_default_na=False,dtype=str)
on['occ']=on['O*NET-SOC Code'].str[:7]
m=on.merge(tp,left_on='Task',right_on='task',how='left')
print('rows in',len(on),'matched',m.penetration.notna().sum(),'unmatched',m.penetration.isna().sum())
g=m.groupby('occ').agg(n_pos=('penetration',lambda s:(s>0).sum()),maxpen=('penetration','max'),meanpen=('penetration','mean'))
j=je.set_index('occ_code').join(g)
print('exposure>0 & no positive task:',((j.observed_exposure>0)&(j.n_pos==0)).sum())
print('exposure>maxpen:',(j.observed_exposure>j.maxpen+1e-9).sum())
print('spearman', j[['observed_exposure','meanpen']].corr(method='spearman').iloc[0,1])"
#   -> rows in 19265 matched 19265 unmatched 0 | 0 | 0 | 0.8726

# V18 footnote-3 arithmetic
python -c "print(100/4_000_000*100)"   # -> 0.0025

# V19 the 52 zero-exposure occupations that own positive-penetration tasks
#   (same load as V17, then:)
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False).drop_duplicates('task')
on=pd.read_csv('/tmp/onet/x27_2/db_27_2_text/Task Statements.txt',sep='\t',keep_default_na=False,dtype=str)
on['occ']=on['O*NET-SOC Code'].str[:7]
g=on.merge(tp,left_on='Task',right_on='task',how='left').groupby('occ').penetration.apply(lambda s:(s>0).sum())
j=je.set_index('occ_code').join(g.rename('n_pos'))
z=j[(j.observed_exposure==0)&(j.n_pos>0)]; print(len(z)); print(z.index.str[:2].value_counts().to_dict())"
#   -> 52 {'25':16,'29':15,'51':4,'11':3,'43':3,'33':2,'19':2,'31':2,'39':2,'17':1,'21':1,'35':1}
#   Also: 42 O*NET 27.2 occupations absent from job_exposure, 17 of them present in the BLS table.

# V20 BLS Employment Projections: download and merge audit  (needs `pip install html5lib`)
curl -sSL -o /tmp/blsproj.html 'https://data.bls.gov/projections/occupationProj'   # -> 200, ~1.4 MB HTML
python -c "
import pandas as pd
t=pd.read_html('/tmp/blsproj.html')[0]            # 4-level header; row 0 of it is the 'Total, all occupations' filter row
t.columns=[c[1] for c in t.columns]; t.to_csv('/tmp/blsproj.csv',index=False); print(t.shape)"
#   -> (831, 14); detail SOC rows only; columns Employment 2025 / 2035, Employment Percent Change, 2025-2035, Median Annual Wage 2025
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
b=pd.read_csv('/tmp/blsproj.csv').rename(columns={'Occupation Code':'occ_code'})
m=je.merge(b,on='occ_code',how='left',indicator=True)
print('rows in',len(je),'matched',(m._merge=='both').sum(),'unmatched',(m._merge=='left_only').sum())
print(m.loc[m._merge=='left_only','title'].tolist())"
#   -> rows in 756 matched 755 unmatched 1 ['Legislators']

# V21 BLS static files and the Wayback copy are unreachable from this sandbox
curl -sSL -A 'Mozilla/5.0' -o /dev/null -w '%{http_code}\n' https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx        # -> 403
curl -sSL -A 'Mozilla/5.0' -o /dev/null -w '%{http_code}\n' https://download.bls.gov/pub/time.series/ep/ep.data.0.Current # -> 403
curl -sSL -o /dev/null -w '%{http_code}\n' 'http://web.archive.org/web/20251121191709/https://data.bls.gov/projections/occupationProj'  # -> 403 "Blocked by egress policy"

# V22 published occupation numbers and the appendix worked example
python -c "
import pandas as pd
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
print(je.nlargest(10,'observed_exposure').to_string(index=False))
tp=pd.read_csv('data/cache/labor_market_impacts/task_penetration.csv',keep_default_na=False)
print(tp[tp.task.str.startswith('Identify, compile, abstract, and code patient data')].to_string(index=False))"
#   -> 15-1251 0.7451; 43-4051 0.7011; 43-9021 0.6707; … | penetration 0.9776 (appendix says 0.96)

# V23 employment-weighted category means (published: top four groups; 31% / 1%)
python -c "
import pandas as pd, numpy as np
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
b=pd.read_csv('/tmp/blsproj.csv').rename(columns={'Occupation Code':'occ_code','Employment 2025':'emp'})
m=je.merge(b[['occ_code','emp']],on='occ_code'); m['mg']=m.occ_code.str[:2]
g=m.groupby('mg').apply(lambda d: np.average(d.observed_exposure,weights=d.emp),include_groups=False).sort_values(ascending=False)
print(g.head(5).round(4).to_dict())
f=m[m.mg.isin(['15','43','13','41'])]; print('top set', round(np.average(f.observed_exposure,weights=f.emp),4))
for sel in (['53','51','37'],['53','51','37','35']):
    s=m[m.mg.isin(sel)]; print(sel, round(np.average(s.observed_exposure,weights=s.emp),4), round(s.emp.sum()/m.emp.sum(),3))"
#   -> {'15':0.3542,'43':0.3381,'13':0.2875,'41':0.275,'23':0.2024} | top set 0.3117 | 0.0045 0.167 | 0.006 0.256

# V24 "33% of Computer & Math" and "30% of workers have zero coverage"
python -c "
import pandas as pd, numpy as np
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
b=pd.read_csv('/tmp/blsproj.csv').rename(columns={'Occupation Code':'occ_code','Employment 2025':'emp'})
m=je.merge(b[['occ_code','emp']],on='occ_code'); m['mg']=m.occ_code.str[:2]; g=m[m.mg=='15']
print('C&M weighted',round(np.average(g.observed_exposure,weights=g.emp),4),'unweighted',round(g.observed_exposure.mean(),4))
print('zero-exposure employment share',round(m.loc[m.observed_exposure==0,'emp'].sum()/m.emp.sum(),4),
      'unweighted share of occupations',round((je.observed_exposure==0).mean(),4))"
#   -> C&M weighted 0.3542 unweighted 0.3787 | zero-exposure employment share 0.3977 unweighted 0.5437

# V25 Figure 4 regression and the wage comparison (2025-2035 vintage, nearest substitute)
python -c "
import pandas as pd, numpy as np
je=pd.read_csv('data/cache/labor_market_impacts/job_exposure.csv',keep_default_na=False)
b=pd.read_csv('/tmp/blsproj.csv').rename(columns={'Occupation Code':'occ_code','Employment 2025':'emp',
        'Employment Percent Change, 2025-2035':'pctchg','Median Annual Wage 2025':'wage'})
b['wage']=pd.to_numeric(b.wage.astype(str).str.replace(r'[\$,]','',regex=True),errors='coerce')
d=je.merge(b[['occ_code','emp','pctchg','wage']],on='occ_code').dropna(subset=['emp','pctchg'])
X=np.column_stack([np.ones(len(d)),d.observed_exposure]); w=d.emp.values
bw=np.linalg.lstsq(X*np.sqrt(w)[:,None], d.pctchg.values*np.sqrt(w),rcond=None)[0]
bu=np.linalg.lstsq(X,d.pctchg.values,rcond=None)[0]
print('weighted',round(bw[1],4),round(bw[1]/10,4),'unweighted',round(bu[1],4),'N',len(d))
s=d.sort_values('observed_exposure',ascending=False); c=s.emp.cumsum()/s.emp.sum(); cut=s.observed_exposure[c<=0.25].min()
tq=s[s.observed_exposure>=cut].dropna(subset=['wage']); z=s[s.observed_exposure==0].dropna(subset=['wage'])
wt=np.average(tq.wage,weights=tq.emp); wz=np.average(z.wage,weights=z.emp)
print('cut',round(cut,4),'n top',len(tq),'wage top',round(wt),'wage zero',round(wz),'pct',round(100*(wt/wz-1),1))"
#   -> weighted -7.6868 -0.7687 unweighted -0.5747 N 755 | cut 0.2315 n top 102 wage top 70630 wage zero 50506 pct 39.8
```

## Dated log

- **2026-09-16** — First profile, at revision `2ea58ff`. Fetch script written and run twice
  (idempotent); both byte sizes match `data/releases/INDEX.md`; sha256s recorded. Vintage of the
  task universe pinned to O\*NET 27.x by an exact set match, usage vintage to the August and
  November 2025 waves from appendix footnote 5. Reproduced: the Figure 3 occupation values and
  order, the appendix's four "highly exposed categories" and its 31% top-quartile coverage, the
  18,000-task and gate-arithmetic statements. Not reproduced: the 33% Computer & Math figure
  (35.4% with BLS 2025 weights), the 30% zero-coverage share (39.8%), the −0.6 pp per 10 pp BLS
  regression (−0.77 with the 2025–35 vintage), the appendix's 0.96 worked example (file says
  0.9776). Open: the 2024–34 BLS vintage and the CPS weights are unreachable from this sandbox;
  Eloundou et al. task-level β not obtained (the `openai/GPTs-are-GPTs` README points at
  `occ_level.csv`, which 404s on `main`); the cause of the 52 zero-exposure occupations with
  positive tasks, and of the 100 tasks sharing the value 0.7239, remains conjecture.

- **2026-09-16 (b) — steward question batch** (`room/director-2026-09-16-steward-question-batch.md`
  Q8, Q10). Cache rebuilt in a fresh sandbox (2 files, 1,926,998 bytes, both sha256 matching) and
  the two column questions re-confirmed against the files rather than the report:
  `job_exposure.csv` = `occ_code, title, observed_exposure` (756 rows, `occ_code` is 7-character
  **2018 SOC detailed** code, e.g. `11-1011`, unique, no aggregates and no SOC 55 Military);
  `task_penetration.csv` = `task, penetration` (17,998 rows, 17,992 distinct O\*NET 27.x task
  strings, not unique on its only key).
  `python3 -c "import pandas as pd; [print(f, pd.read_csv('data/cache/labor_market_impacts/'+f, keep_default_na=False).columns.tolist()) for f in ('job_exposure.csv','task_penetration.csv')]"`.
  **This is the only file in any Anthropic public release that carries job-level observed
  exposure**, and it carries no survey variable, no occupation title crosswalk beyond `title`, and
  no geography — so the 81k-survey papers' job-level exposure joins to it on `occ_code` only, and
  every respondent-level variable in those papers is unreleased (see `data/ATLAS.md`
  §Supplementary sources for the two sibling Anthropic datasets that are public).
