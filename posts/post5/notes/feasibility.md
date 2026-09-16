# post5 (LL-18) · feasibility — data steward, 2026-09-16

Against `posts/post5/BRIEF.md` (commit `9333c67`, question frozen: *Where is AI doing work users
could not have completed without it?*) and the lead's request in
`room/lead-2026-09-16-brief-post5-status.md`.

Everything below was re-derived today from the cache, in this sandbox, at Hugging Face revision
`2ea58ff`. Nothing is asserted from `data/ATLAS.md` alone. The cache folder the brief needs for
cut C6 (`release_2026_06_26`) was absent from this sandbox and was rebuilt with
`python data/fetch/release_2026_06_26.py` before anything in §1 was confirmed. Three scripts
produce every number here; their full output sits beside them:

```bash
python data/fetch/release_2026_01_15.py && python data/fetch/release_2026_03_24.py \
  && python data/fetch/release_2026_06_26.py && python data/fetch/release_2025_09_15.py   # ~2 min, checksummed
python data/replication/post5_cuts_c1_c6.py              # C1-C6, ~25 s
python data/replication/post5_replication_and_mde.py     # the four published numbers, joins, MDE
python data/replication/post5_residual_language_june.py  # the residual, country-state, language, June
```

→ `data/replication/results/post5_cuts_c1_c6.{txt,json}`,
`…/post5_replication_and_mde.{txt,json}`, `…/post5_residual_language_june.{txt,json}`.

Cache state when this note was written: `sha256sum -c CHECKSUMS.txt` inside the four release
folders — 4 / 3 / 3 / 38 files, **0 failed**. Every long file is read with
`keep_default_na=False, na_values=[]` (traps 1, 2) and `level` cast to `str` after each Parquet
read (trap 7). Raw files were not modified. **No gradient of the outcome on adoption or income was
estimated** — the confirmatory tests stay sealed until pre-registration; what is reported here is
availability, coverage, precision and the published numbers.

**Headline. FEASIBLE WITH CAVEAT.** The primitive exists exactly where §8 says it does, the
published number reproduces to four decimals, and the 115-country balanced panel is real. Three
things in §8/§9/§10 are wrong as written and need one amendment:

1. **The country `not_classified` residual does not exist in the analysis panel at all.** Zero of
   the 118 (Nov) and 117 (Feb) countries at or above 200 conversations carries a `not_classified`
   row; the 39 / 42 that do are microstates of 18–187 conversations, and their residual is the
   **folded sub-15 privacy cell**, not a classifier abstention (max `not_classified` count is 14 /
   13; none of them publishes a `no` cell; the smallest published `no` cell anywhere is 16 / 15).
   So `no / (yes + no)` and the raw `no_pct` are **the same number** on the panel, §8's raw-base
   robustness is a no-op, and **H4's first confirmatory signature cannot fire** (there is no
   residual to regress on adoption).
2. **T3 has a sibling with three times the coverage that §8 does not name.**
   `request::human_only_ability` exists at global at levels 0, 1 **and 2**; at level 2 all 23 / 25
   nodes carry both arms, and a country's published `request` L2 mix covers a median **98.4% /
   95.5%** of that country's conversations for all 115 panel countries, against **34.5% / 29.2%**
   for the `onet_task` route of C4/C5.
3. **Count-weighting, as §8 and §10 pre-register it, destroys the test.** The Kish effective N is
   **11.02 / 10.39** of 115 (the top three countries hold 38–40% of the weight), which puts the
   tercile MDE at **7.0 pp** — wider than the entire interquartile range of the outcome. The
   variance decomposition says the weights are not needed: of the observed between-country variance
   11.56 (sd 3.40 pp), only 1.31 (sd 1.15 pp) is within-country sampling noise.

---

## 1. Cuts confirmed at column level

Grain vocabulary: "global" = `geography == 'global'` (`geo_id == 'GLOBAL'`); the long-family key is
`(geo_id, geography, date_start, date_end, platform_and_product, facet, level, variable,
cluster_name)`. Both 2026 waves are Claude.ai files;
`platform_and_product` is `Claude AI (Free and Pro)` in November (the label is wrong — the sample
is Free, Pro and Max, `[R4 §Traps 10]`) and `Claude AI (Free, Pro, and Max)` in February. The
brief's metric labels correspond to file `variable` values with underscores, never colons:
`onet_task_human_only_ability_pct`, not `onet_task::human_only_ability_pct`.

Files behind every row below:
`release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` (Nov 2025)
and `release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` (Feb 2026), read from
their Parquet siblings; `release_2026_06_26/data/aei_claude_ai_2026-06-26.csv` for C6.

### C1 — global `human_only_ability` · **CONFIRMED**

| | |
|---|---|
| grain | `geography == 'global'`, `facet == 'human_only_ability'`, `level == '0'` (one level only) |
| categories | `cluster_name ∈ {yes, no}` — **two**, as §8 says; no `not_classified` at global |
| metric columns | `human_only_ability_pct`, `human_only_ability_count` (§8 lists only `_pct`; the count is there and is what fixes the base) |
| threshold | none applies; `_pct` sums to exactly 100.000000 in both waves |

```python
d = df[(df.geography=='global') & (df.facet=='human_only_ability')]
d.pivot_table(index='cluster_name', columns='variable', values='value')
```

- November: `yes` 87.909689 (878,987), `no` 12.090311 (120,888); total **999,875**.
- February: `yes` 87.759900 (877,599), `no` 12.240100 (122,401); total **1,000,000** — the
  per-million sample base, not conversations (`[R5 §Metrics]`).

### C2 — country `human_only_ability` · **CONFIRMED WITH CAVEAT** (the residual is mis-described)

| | |
|---|---|
| grain | `geography == 'country'`, `facet == 'human_only_ability'`, `level == '0'` |
| units carrying the facet | **171** (Nov) / **175** (Feb) country ids |
| categories | `cluster_name ∈ {yes, no, not_classified}` — three in the file, **two in the panel** (see below) |
| metric columns | `human_only_ability_pct`, `human_only_ability_count`; per-country `_pct` sums to exactly 100.0000 and `_count` sums to that country's `usage_count` (max abs diff **0** over every country, both waves) |
| threshold | the file applies a **15**-count privacy floor per cell and nothing else; the 200-conversation rule is the post's to apply |

Coverage at the threshold: **118** (Nov) and **117** (Feb) real country ids reach 200
conversations, and **every one of them carries the facet** (0 missing in either wave). The
balanced panel — facet present and ≥ 200 conversations in **both** waves — is **115** countries,
confirming §8 and long-list log (e) 4. Seychelles drops out by construction (410 rows in November,
**0 rows in February**), so the report's exclusion rule removes nothing from the panel; it bites
only the global row and the November cross-section.

**The caveat, and it is the one design-relevant correction.** §8 and the steward's own long-list
line say the residual is `not_classified` at country grain with a median of 10.34% / 11.11%. That
is true of the **file** and false of the **panel**:

```python
p = df[(df.geography=='country')&(df.facet=='human_only_ability')
       &(df.variable=='human_only_ability_pct')].pivot_table(index='geo_id',columns='cluster_name',values='value')
u = df[(df.geography=='country')&(df.facet=='country')&(df.variable=='usage_count')].set_index('geo_id').value
p.loc[u[u>=200].index, 'not_classified'].notna().sum()   # -> 0 in both waves
```

- 39 (Nov) / 42 (Feb) countries carry an explicit `not_classified` row; their `usage_count` runs
  19–187 (median 47) and 18–124 (median 42). **None reaches 200.**
- Over the 118 / 117 thresholded countries, `yes + no` = 100.0000 for **118 of 118** and **117 of
  117**.
- The mechanism: `not_classified` counts never exceed **14** (Nov) / **13** (Feb), none of those
  countries publishes a `no` cell, and the smallest published `no` cell anywhere is **16** / **15**.
  The residual is the **sub-15 `no` cell folded**, exactly as the steward found for `task_success`
  in post4 — not the classifier declining to judge.

Consequences for the brief: (a) the "renormalised base `no/(yes+no)`" and the raw `no_pct` are the
same number on the panel, so the §8 sentence about reporting both and the §6 H1 falsifier "reverses
on the all-conversation base" are inert; (b) **H4's first signature is untestable at country
grain** (see §4); (c) nothing is lost — the outcome is well defined and unaffected.

### C2b — `country-state` `human_only_ability` (not a cut in §8; recorded because the coordinator asked)

Exists in both waves: **938** / **1,082** real units carry the facet (excluding the
`<ISO2>-not_classified` pseudo-units, which are units in this file). At the 100-conversation floor,
**545** (109 parents, 51 US) and **570** (125 parents, 52 US) survive; the **balanced sub-national
panel is 496 units across 105 parents, 51 of them US**. Unlike the country grain, 33 / 25 of the
surviving units **do** carry an explicit `not_classified` row. The totals facet at this grain is
named `country-state`, not `country`. If the lead wants H4's residual leg back, this is where it
lives — at the cost of a different estimand (`usage_pct` at this grain is a share of the **parent
country**, not of the world).

### C3 — country `usage_count` / `usage_pct` · **CONFIRMED WITH CAVEAT**

| | |
|---|---|
| grain | `geography == 'country'`, `facet == 'country'`, `level == '0'`, `cluster_name == ''` (empty string, not null — trap 5) |
| metric columns | `usage_count`, `usage_pct` — both present in both waves |
| ids | 174 (Nov: 173 countries + `not_classified`) and 178 (Feb: 176 + `not_classified` + `NONE`) |
| threshold | none applied in the file; min `usage_count` is **15** in both waves |

`usage_pct` at country grain is a share of the **global** sample including `not_classified`
(trap, `[R4 §Metrics, V17]`) — and the two waves differ in how complete that is: November country
rows sum to **100.0000** (`usage_count` sums to 999,875, the whole sample), February country rows
sum to **98.9313** (`usage_count` sums to 989,313 of the 1,000,000 base). The missing 10,687 per
million sit in geographies below the privacy floor and are **absent, not zero**. Any February
denominator built by summing country rows is 1.07% short; use the published base.

### C4 — global `onet_task::human_only_ability` · **CONFIRMED WITH CAVEAT** (the "3,169 / 3,259 tasks" overstates)

| | |
|---|---|
| grain | `geography == 'global'` **only** — 0 rows at country or country-state in either wave (cut 10) |
| categories | `cluster_name == '<task>::<arm>'`, arm ∈ {`yes`, `no`, `not_classified`}; the task is the lower-cased O\*NET statement |
| metric columns | `onet_task_human_only_ability_pct`, `onet_task_human_only_ability_count` |
| threshold | published cells go down to **count 1**; the per-task published arms sum to exactly 100.0000 of that task's base cluster |

Rows 11,074 / 11,592 over **3,169** / **3,259** distinct tasks — as §8 says. But the arm the design
needs is thin:

- tasks publishing a **`no`** cell: **540 of 3,169** (Nov) and **646 of 3,259** (Feb);
- those tasks carry **78.4% / 77.7%** of global *named*-task mass (73.30 / 72.21 of 100 including
  the `none`/`not_classified` nodes) and **92.0% / 90.6%** of all `no` conversations
  (111,170 of 120,888; 110,901 of 122,401);
- a `not_classified` arm exists for 1,954 / 2,045 tasks and is again a fold of sub-floor cells.

So §9's "the global `no` shares over 3,169 / 3,259 tasks" should read "over the 540 / 646 tasks
that publish a `no` cell, carrying 78% of named-task mass"; the rest must be 0-imputed or bounded,
and the post must say which. In practice this costs almost nothing, because the tasks a country
publishes are the large ones: the shift-share below covers a median **100%** of each country's own
named-task mass.

### C4b — `request::human_only_ability` (not in §8; the wider-coverage sibling) · **EXISTS**

Same two waves, **global only**, `variable ∈ {request_human_only_ability_pct,
request_human_only_ability_count}`, at `level` **0, 1 and 2**:

| wave | L0 nodes / with a computable `no`-rate | L1 | L2 | L2 `no`-rate spread |
|---|---|---|---|---|
| Nov 2025 | 617 / 591 | 111 / 111 | **23 / 23** | 2.8 – 34.5 pp |
| Feb 2026 | 620 / 574 | 103 / 101 | **25 / 25** | 1.2 – 29.7 pp |

Paired with the country `request` mix (C5b), this is the task-mix adjustment the brief wants, with
the coverage the brief says it cannot have. One constraint: **0 of 23 / 25 L2 node names are shared
between the waves** (log (e) 1), so each wave's adjustment is internal to that wave — the sign test
per wave is valid, the predicted *levels* are not comparable across waves.

### C5 — country `onet_task` mix · **CONFIRMED** (one number restated)

`geography == 'country'`, `facet == 'onet_task'`, `variable == 'onet_task_pct'`, `level == '0'`;
**117** / **118** country ids, of which **113** / **114** are in the 115-panel. Residual labels are
`none` **and** `not_classified` (both, unlike the primitive facets). Per-country `onet_task_pct`
sums to exactly 100.

- named nodes per country: median **19** (Nov) / **16** (Feb) — §8's "median 21 / 18" counts the
  two residual pseudo-nodes;
- named mass per country: median **34.27% / 29.05%** (all countries), **34.46% / 29.44%** over the
  panel, minimum **3.74% / 3.24%**, 10th percentile 12.98% / 8.79% — §7(3)'s "about 30%" is right,
  and the tail is worse than the median suggests;
- shift-share coverage actually achieved (country mix × tasks with a global `no` cell): median
  **34.46% / 29.16%** of a country's conversations, min 3.74% / 3.24%, max 78.09% / 76.50%.

### C5b — country `request` mix by level (not in §8) · **EXISTS**

| level | country ids (Nov / Feb) | panel countries | named mass per panel country, median | min |
|---|---|---|---|---|
| L0 | 74 / 71 | 72 / 70 | 22.2% / 19.9% | 1.1% / 1.2% |
| L1 | 121 / 119 | 114 / 114 | 69.8% / 76.5% | 6.7% / 6.5% |
| **L2** | **129 / 134** | **115 / 115** | **98.4% / 95.5%** | 44.5% / 41.8% |

At L2 every country row matches a global node name (100.0% of rows), so the shift-share is complete
for all 115 panel countries in both waves.

### C6 — June 2026 `country` / `overall` (robustness only) · **CONFIRMED WITH CAVEAT**

| | |
|---|---|
| file | `release_2026_06_26/data/aei_claude_ai_2026-06-26.csv` (wide Family C) |
| grain | `geo_level == 'country'`, `category_name == 'overall'`, two months (`date_start` 2026-04-01, 2026-05-01) |
| metrics present | `human_only_ability_pct` ✓ and `usage_per_capita_index` ✓ (52 metric ids at this block) |
| counts | **none** — 0 count-like metric ids, so the 200 rule cannot be applied or checked |
| residual | **no `not_classified` metric of any kind** (cut 24) |
| ids | **114** countries in April, **121** in May, **114 in both months**, all 114 carrying both metrics; **112** of them are in the 115-country panel (`MZ`, `RE`, `TG` absent); Seychelles absent entirely |

Two corrections to §8: (i) "121 country ids" is the **May** count; the usable both-month set is
**114**. (ii) The June metric is the **`yes` share**, not the `no` share — global 87.79 (Apr) and
87.62 (May), continuous with the long waves' 87.91 → 87.76 — so the outcome is `100 − value`.
Values are pre-rounded to two decimals (trap 12), which is the binding constraint on any June rank.
The June AUI here is Anthropic's own published index (`usage_per_capita_index`), not a rebuild, and
the June and long-wave AUI levels are not on one axis (`[R6 §Reproduced]`); ranks are.

---

## 2. Replication target

The brief names four (§8, "The published numbers this reproduces first"). All four were run today;
three reproduce exactly, and the fourth reproduces only under a specification the report does not
state. **Anthropic's released code covers none of them**: the only released library is the
2025-09-15 `code/` folder, whose `state_us` paths and enrichment steps predate the primitives; the
2026-01-15 and 2026-03-24 folders ship no code, so every number here is re-implemented from that
library plus each wave's `data_documentation.md` (skill, *Replication and released code*).

| # | published | source | rebuilt | match |
|---|---|---|---|---|
| 1 | "Human can't do alone (%) **12.09 → 12.24**" | R5 Table 1.1, p.9 | `100 − human_only_ability_pct[yes]` at global: **12.0903** → **12.2401** | **exact to 4 dp** |
| 2 | "Human could do alone **88%**", N = 999,875 | R4 Fig 2.2, p.25 | `human_only_ability_pct[yes]` = **87.9097**, count total **999,875** | **exact** |
| 3 | Canada's AUI "**4.4**" | Canada spotlight, Jul 2026, Fig 1 | **4.4430** on the symmetric (thresholded-only) usage denominator; **3.6219** on the August-2025 `+ not_classified` rule | **confirmed**, symmetric rule |
| 4 | ln AUI on human education: **r = 0.359, R² = 0.129, β = 0.75** | R4 Fig 3.3, p.31 | **r = 0.3586, R² = 0.1286, β = 0.7544, N = 116** | **exact**, *only* with Seychelles dropped |

Specification notes, for the pre-registration:

- **Target 1** reproduces with Seychelles **included**, as published; November's total is the
  999,875-conversation sample and February's is the 1,000,000 per-million base. The polarity is
  settled: the published series is `100 − yes`, and the file's `no` cell equals it to the last
  decimal (12.090311, 12.240100).
- **Target 3**: AUI rebuilt from `usage_count` over countries at ≥ 200 conversations and World Bank
  working-age population (§3), both denominators over the same thresholded set. USA comes out at
  4.3842 (Nov) and 4.6550 (Feb); Canada 3.7376 (Nov), 4.4430 (Feb) — the spotlight's wave is
  February, as the atlas records.
- **Target 4 is the one that needed the specification found rather than read.** Over all 117
  thresholded November countries with an AUI and an education mean, the regression gives r =
  0.5903, R² = 0.3484, β = 1.0633 — nothing like the published figures. Dropping **Seychelles**
  (AUI 1,054.6, the report's own exclusion, applied nowhere in the file) gives r = 0.3586,
  R² = 0.1286, p = 7.7e-05, **β = 0.7544, N = 116** against the published 0.359 / 0.129 / 0.75.
  Whether Seychelles is also removed from the AUI *denominator* changes nothing to four decimals
  (a constant shift in ln AUI), so the rule to pre-register is: **Seychelles out of the regression
  sample; denominator rule immaterial for slopes and correlations, material for levels.** The same
  regression on the February wave (SYC already absent) gives r = 0.4400, R² = 0.1936, β = 1.0419 —
  not a published number, and a caution that the control is wave-specific.
- β is the slope of **ln AUI on education years**, not the reverse (the reverse is 0.1704).

---

## 3. Supplementary joins tested

§8 names two, both shipped inside `release_2025_09_15` and used as static 2024 annuals. Merge
audits printed in full; both were re-run today.

**(a) World Bank working-age population** —
`release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv`, 194 × 5
(`iso_alpha_3, year, working_age_pop, country_code, country_name`), SP.POP.1564.TO 2024 plus Taiwan
(NDC). Join key: the file's ISO-2 `country_code` against the waves' `geo_id`. Licence: World Bank
CC-BY; obtained by `python data/fetch/release_2025_09_15.py` (Hugging Face, checksummed).

| wave | rows in | matched | unmatched |
|---|---|---|---|
| Nov 2025 | 174 | **167** | 7: `GF, GP, JE, MQ, RE, YT, not_classified` |
| Feb 2026 | 178 | **170** | 8: `GF, GG, GP, JE, MQ, NONE, RE, not_classified` |

The February audit is identical to the one recorded in `data/ATLAS.md` §Conventions. Over the
thresholded sets: **117 of 118** (Nov) and **116 of 117** (Feb) countries carry a population row.
Over the 115-country panel: **114** (only `RE`, Réunion, is missing).

**(b) IMF WEO GDP** — `release_2025_09_15/data/intermediate/gdp_2024_country.csv`, 174 × 3
(`iso_alpha_3, gdp_total, year`), NGDPD 2024 in USD. Join key: `iso_alpha_3`, reached from the
wave's ISO-2 `geo_id` through the population file's own bridge (`iso_country_codes.csv`, 252 rows,
is the check). Licence: IMF terms; same fetch script.

| wave | rows in | matched | unmatched with an ISO-3 |
|---|---|---|---|
| Nov 2025 | 174 | **156** | `BM, CW, GU, IM, KY, LI, MC, NC, PF, PS, VI` |
| Feb 2026 | 178 | **157** | `BM, CW, GI, GU, IM, KY, LI, MC, MF, NC, PF, PS, VI` |

Over the thresholded sets: 116 of 118 (Nov), 115 of 117 (Feb). Over the panel: **113 of 115**
(missing `PS` and `RE`) — §8's "113 of the 115" **CONFIRMED**. Effective N for any test carrying
income is therefore **113**, not 115.

**(c) For the exploratory E1 only — no shipped source exists; two externals were tested.**

- **GeoNames `countryInfo.txt`** — `https://download.geonames.org/export/dump/countryInfo.txt`
  (HTTP 200, 31,678 B, sha256 `93bafc52…` on 2026-09-16), CC BY 4.0, no key. 252 rows; the
  `Languages` column is a comma-separated ISO-639 list. Merge on ISO-2 against the panel: **115
  rows in, 115 matched, 0 unmatched.** English listed **first** in 17 countries (`AU CA CM GB GH IE
  IN JM KE MU NG NZ PR UG US ZM ZW`), listed **anywhere** in 48. Two cautions: the file is **live
  and unversioned** (no vintage, the checksum will drift), and the field is spoken/administrative
  languages, not a legal "official language" list — so it is a coding choice the post must state,
  which is why E1 stays exploratory. Trap found today: a default
  `pd.read_csv(..., comment='#')` **truncates every row**, because the postal-code-format column
  contains `#`; strip comment lines before parsing.
- **`Anthropic/enabling-independent-research`, `stanford_clusters.csv`** (already cached by
  `python data/fetch/supplementary_anthropic.py`; CC-BY-4.0) carries **74 `lang:*` facets × 153
  `country:*` facets** at cluster grain over an April–May 2026 opt-in sample. It is the only
  Anthropic file with a language field, and it is a different instrument, a different population
  and has no denominator in common with the Index — usable as a *cited comparator*, never as a join.

No other supplementary source is needed: adoption, income and population are the only external
quantities the design uses, and both are shipped inside a release.

---

## 4. Hypothesis by hypothesis

Common panel: **115** countries (≥ 200 conversations and the facet in both waves); **113** with
both population and GDP; Seychelles excluded automatically. Every pre-registered covariate exists
at country grain for all 115 in both waves: `human_only_time_mean`, `human_education_years_mean`,
`ai_autonomy_mean`, `multitasking_pct`, `task_success_pct`, `use_case_pct` — checked, 115 / 115
each.

Precision, once, since every hypothesis leans on it:

| | Nov 2025 | Feb 2026 |
|---|---|---|
| country `no` share (renormalised = raw), mean / sd | 13.783 / **3.400** | 14.317 / **3.328** |
| range | 7.74 – 22.92 | 8.67 – 23.58 |
| classified conversations per country, median / min | 1,673 / 248 | 1,643 / 225 |
| mean within-country sampling sd | 1.15 pp | 1.15 pp |
| implied true between-country sd | **3.20 pp** | **3.12 pp** |
| Kish effective N under count weights | **11.02** | **10.39** |
| n_eff with weights capped at the 90th percentile | 48.4 | 47.6 |
| tercile-difference MDE, 80% power, α = 0.05 — unweighted | **2.18 pp** | **2.14 pp** |
| same, on the Kish effective N | **7.02 pp** | **7.08 pp** |
| detectable correlation at N = 115 | **0.265** | 0.265 |

§10's "a correlation of about 0.26 is detectable" is **CONFIRMED** (0.265). The percentage-point
MDE the lead asked for is **2.2 pp unweighted** — but **7.0 pp under the count weights §8
pre-registers**, because the US, India and Japan/GB hold 38–40% of the weight. Since only 11% of
the observed between-country variance is sampling noise, count-weighting buys nothing and costs the
whole design. Recommendation for §9/§10: **unweighted country-level OLS as the primary, count
weights (with n_eff printed) as a robustness**, or weights capped at the 90th percentile.

**H1 (share falls with adoption) — feasible.** Outcome, adoption and both controls exist at the
grain assumed: N = 115 for the AUI-only specification, **N = 113** once log GDP per working-age
capita enters, in both waves. The AUI must be rebuilt (no 2026 wave publishes it, cut 22); the
rebuild is validated end to end by replication target 4. Caveat: `human_only_time` enters as a
pre-registered control and it is on the **hours** scale in both 2026 waves (trap 8) — do not mix it
with `human_with_ai_time`, which is minutes.

**H2 (share rises with adoption and income) — feasible, same N**, with the note that the income and
adoption axes are collinear enough that §9's T2 is the only test that separates them; both variables
are static 2024 annuals joined to two 2025–26 waves, which is a levels comparison, not a splice.

**H3 (composition, not capability) — feasible, and better than the brief assumes.** Two independent
shift-shares exist:

| route | taxonomy | per-country coverage (median, Nov / Feb) | countries |
|---|---|---|---|
| §8's C4 × C5 | `onet_task` | **34.5% / 29.2%** of conversations | 113 / 114 of 115 |
| C4b × C5b (new) | `request` L2 | **98.4% / 95.5%** of conversations | 115 / 115 |

Run both; they use different taxonomies (top-down O\*NET vs bottom-up request), so agreement is
evidence and disagreement is informative. The `request` route's constraint is that its node names
do not survive a wave (0 of 23 / 25 shared), so the adjustment is computed within each wave and the
predicted *series* are not comparable across waves. The `onet_task` route's constraint is the one
§7(3) already states, plus C4's: the per-task `no` rate is only published for 540 / 646 tasks.

**H4 (the classifier is reading places differently) — NOT feasible as specified; one leg survives.**
Signature 1 — "the `not_classified` share has its own gradient in adoption, so that renormalising is
not neutral and the raw and renormalised gradients disagree in sign" — **cannot be tested**: the
residual is identically absent for all 115 panel countries, raw and renormalised are the same
number, and where the residual does appear it is a folded sub-15 `no` cell in a microstate, i.e. a
suppression artefact of the privacy floor rather than classifier abstention. Nearest substitutes,
with costs: (i) run the residual leg at **`country-state`** grain, where 33 / 25 surviving units
carry an explicit residual — different estimand, parent-country base, and the same fold
interpretation; (ii) use the **`task_success`** residual (median 26.67% / 21.43% at country grain)
as a general classifier-abstention proxy — a different facet, so it bounds the instrument, not this
measure; (iii) drop signature 1 and rest H4 on signature 2. Signature 2 — rank stability against
count-based resampling — **is** feasible: counts exist in both waves (per-million in February), and
the raw November-to-February Spearman over the 115 panel countries is **0.7762** (Pearson 0.7985)
against a within-country sampling sd of 1.15 pp. Disclosed here because it is the precision input
the lead asked for; the referee may prefer it sealed until the pre-registration is filed.

**Composition, as a data fact (§7(3)).** The files cannot identify who Claude's users are — no
user, account, plan, industry, language or tenure column exists in any release (cut 26, re-verified
today over all six 2026 frames). What they *can* show is the mix of work: `use_case` (work /
personal / coursework), `task_success`, `multitasking` and the `request` L2 mix are published for
all 115 panel countries in both waves, and the `request` L2 shift-share covers ~96% of each
country's conversations. So the post can hold the **mix of work** nearly constant and can say
nothing directly about the **users** — which is exactly the wording discipline §7(3)(a) imposes.

---

## 5. Traps that apply

| trap (`data/ATLAS.md` §Traps unless noted) | where it bites this brief |
|---|---|
| 1, 2 — `NA` is Namibia; `NONE` is a real February `geo_id` | §8's read rule is right; both waves need `keep_default_na=False`, February also `na_values=[]`. `NONE` must be dropped as a pseudo-geography before any count |
| 7 — `level` dtype differs between the Parquet siblings | `level == '0'` silently returns nothing on one wave unless `level` is cast to `str` |
| §Other bases — `usage_pct` at country is a share of the global sample | §8 states it; add that February's country rows sum to **98.93**, not 100 |
| §Other bases — February counts are per **million** | §8 states it; the 200 rule is 200 per million, and the binomial se at that floor is 2.3 pp (§4) |
| §Other bases — intersection `_pct` is a share of its **base cluster** | C4 and C4b: per-task and per-node arms sum to 100 of that node, never of the sample |
| 21 (cut) — no suppression flag; absent ≠ zero | C2's missing `not_classified`, C4's missing `no` arms, C5's unpublished tasks, February's missing 1.07% of the sample |
| 14 — Seychelles | in the November global row and the AUI denominator; **not** in the panel; fatal to replication target 4 if left in |
| 40 / log (e) 1 — `request` names are not comparable across waves | C4b/C5b: each wave's shift-share is internal; 0 of 23 / 25 L2 names shared |
| 10 (cut) — intersections are global only | §9's T3 must apply a **global** rate to a **country** mix; no country-level intersection exists |
| 8 — hours vs minutes | `human_only_time` is hours in both 2026 waves; it is a control in §9 T1 |
| 12 / 17 (cut) — June is pre-rounded to 2 dp and has no counts | C6: ranks only, no threshold, no interval |
| 24 (cut) — no `not_classified` in June | C6: the June base is not the panel's base; use `100 − yes` and say so |
| 16 — `US-PR` is both a subregion and a country | `PR` is a panel country and a June subregion; never union the two |
| §The AI Usage Index — symmetric vs asymmetric denominator | §8 item 3 is right: symmetric for 2026 levels. Immaterial for slopes and ranks (verified today) |
| 5 — `cluster_name` is an empty string on the totals facet | C3: a `dropna()` loses every `usage_count` row |
| §Thresholds — the February documentation deleted the threshold sentence | the 200 / 100 rule is the post's to apply and to state |
| skill, *Interpretation* — the primitive is a classifier judgement, unvalidated for this facet | §7(2) already carries it; no validation statistic exists anywhere in the corpus to cite |

---

## 6. Verdict

**FEASIBLE WITH CAVEAT.**

The measure, the grain, the panel, the covariates and the published anchor are all real: the
`human_only_ability` facet exists at global and country in both 2026 long waves, 115 countries clear
200 conversations in both, 113 of them carry income, every pre-registered covariate is present for
all 115, and the number the post extends — "Human can't do alone 12.09 → 12.24" — reproduces to four
decimals as `100 − human_only_ability_pct[yes]`, with the AUI rebuild validated against a published
regression (r 0.3586, β 0.7544 against 0.359 / 0.75) once Seychelles is dropped. **Three things in
§8–§10 are wrong as written and must be amended once.** First, the country `not_classified`
residual does not exist anywhere in the analysis panel — it appears only in 39 / 42 sub-threshold
microstates, where it is a folded sub-15 `no` cell rather than a classifier abstention — so the raw
and renormalised bases are identical, §8's raw-base robustness is a no-op, and **H4's first
confirmatory signature cannot fire**; H4 must be re-specified on its rank-stability leg, or moved to
`country-state` grain (496 balanced units, 105 parents), or dropped. Second, §8 omits
`request::human_only_ability`, which exists at global levels 0–2 and, crossed with the country
`request` L2 mix, gives the task-mix adjustment **96% coverage instead of 30%** for all 115
countries in both waves — the `onet_task` route should become the robustness rather than the
primary, and §9's "over 3,169 / 3,259 tasks" should read "over the 540 / 646 tasks that publish a
`no` cell". Third, the count weighting §8 and §10 pre-register drives the Kish effective N to
**11 of 115** and the tercile MDE to **7.0 pp**, against **2.2 pp** unweighted and a between-country
sd of 3.4 pp of which only a ninth is sampling noise: the weights should be a robustness, not the
primary, or the null branch of §12 will report a minimum detectable difference wider than the
measure's own cross-country range. With those three amendments the design is sound, and the caveat
the post must carry to the end is the one §7(2) already names — this is one classifier's judgement
of a counterfactual, unvalidated for this facet anywhere in the corpus, so only differences between
places on one instrument are claimable, never a level.

---

*Dated log entry added to `data/ATLAS.md` (2026-09-16 (h)) for the six new facts: the folded country
residual, the `request::human_only_ability` levels and coverage, the Figure 3.3 positive control's
Seychelles specification, the February country-row shortfall, the June polarity and both-month set,
and the GeoNames language file with its parsing trap.*
