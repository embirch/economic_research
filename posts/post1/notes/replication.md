# post1 (LL-07) — replication and cache manifest

*Data steward, 2026-09-17 (session 2.1, Stage 2 step 1), written against `posts/post1/BRIEF.md`
§8–§9 at `0e41a50` and `posts/post1/notes/feasibility.md` §2/§4/§7. Scope: rebuild the cache in a
fresh sandbox, reproduce the published numbers post1 extends with Anthropic's released code where
it exists, and re-run every committed post1 check. **Nothing in the headline was computed** — see
§5, "what has been seen". Authority for conventions and traps: `data/ATLAS.md`; every fact below
carries the command that produced it in §6.*

---

## 1. Cache manifest (rebuilt from empty)

`data/cache/` was empty at the start of this session. Every folder was re-downloaded from
Hugging Face by its own fetch script, which pins the byte size from `data/releases/INDEX.md` and
the sha256 of every file, and `sha256sum -c CHECKSUMS.txt` was then re-run **from inside** each
cache folder (the paths in `CHECKSUMS.txt` are relative to it).

| release (window) | why post1 needs it | files | bytes | `sha256sum -c` | key file, rows |
|---|---|---|---|---|---|
| `release_2025_09_15` (4–11 Aug 2025) | C1 wave; C5 O\*NET 20.1 statements; the released `code/` library | 38 | 60,997,757 | **38 OK, 0 failed** | `aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv` 100,062 rows; enriched 136,845 |
| `release_2026_01_15` (13–20 Nov 2025) | C2 wave; C8 Seychelles; C9 `use_case` | 4 | 141,659,531 | **4 OK, 0 failed** | `aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` 458,778 rows |
| `release_2026_03_24` (5–12 Feb 2026) | C3 wave; C9 `use_case`; exploratory (a) API | 3 | 147,262,094 | **3 OK, 0 failed** | `aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` 477,717 rows |
| `release_2025_02_10` (Dec 2024) | C6 `wage_data.csv`; `plots.ipynb` as the join's specification | 14 | 5,239,526 | **14 OK, 0 failed** | `wage_data.csv` 1,090 × 10 |
| `release_2025_03_27` (Feb–Mar 2025) | C10 per-task collaboration, fourth window | 16 | 10,308,805 | **16 OK, 0 failed** | `automation_vs_augmentation_by_task.csv` 3,364 × 7; `task_pct_v2.csv` 3,365 |
| **five releases** | | **75** | **365,467,713** | **75 OK, 0 failed** | |
| `supplementary/onet_soc_2019_crosswalk` | the 2019 recode of §8's vintage rule | 1 | 108,052 | sha256 = the 2026-09-16 pin | 1,164 rows |
| `supplementary/onet_db_27_3` | not used by post1 (fetched by the same script) | 1 | 11,504,351 | sha256 = the pin | zip, left packed |
| `supplementary/bls_employment_projections` | C7 second wage source + employment weights | 1 | 1,397,448 | **new pin, see below** | 831 detailed-SOC rows |

Parquet siblings (gitignored, derived) were written for the four files above 20 MB, read with
`keep_default_na=False` as `data/fetch/README.md` requires. Total on disk 371 MiB including
Parquet. Rebuild time: under three minutes; no network retry was needed.

**New fetch script: `data/fetch/supplementary_bls_ep.py`.** C7 had no fetch script — the BLS
Employment Projections table was being pulled ad hoc to `/tmp` inside
`data/replication/post1_joins_c5_c7.py`, so the cut was not rebuildable from `data/fetch/` alone.
The new script downloads `https://data.bls.gov/projections/occupationProj` (HTTP **200**,
**1,397,448 B**, sha256 `bbde16e0457b9b93662b17d5ccb3e9bec66929a175c1770c21f381d57765e795`,
observed 2026-09-17) into `data/cache/supplementary/bls_employment_projections/`, writes
`CHECKSUMS.txt`, and asserts the structure the C7 audit depends on: **831** detailed-SOC rows and
the columns `Occupation Code`, `Median Annual Wage 2025`, `Employment 2025`. Because this is a
**live page, not a pinned artefact**, a hash change is *reported*, not fatal; a structure change
**fails**. OEWS — Anthropic's own wage source — remains unobtainable: `www.bls.gov` and
`download.bls.gov` still return **403**.

---

## 2. Replication targets: published value, specification, reproduced value

### (a) Figure 2.11, `economic-index-2025-09-report` p. 4 — Anthropic's own released code

The only released library in the dataset (`release_2025_09_15/code/`) is run in place, unmodified.
It is the estimator post1 extends: per-task automation rates from `onet_task::collaboration` at
global on the five-classified-pattern base, weighted by `onet_task_pct`.

| quantity | published | reproduced | match |
|---|---|---|---|
| partial slope (automation on log AUI, task mix partialled out) | −3.112 | **−3.111834** | exact to the published precision |
| partial R² | 0.394 | **0.393687** | exact |
| N countries | 111 | **111** | exact |
| N tasks | (not published) | 1,808 | — |
| p | (not published) | 1.721e-13 | — |

Command: `python data/replication/post1_replicate_fig211.py` (unchanged from the feasibility
session; re-run on the fresh cache and **byte-identical** to the committed output). Two sandbox
conditions, both recorded in `data/ATLAS.md` §Traps 31: a stub `geopandas` module is injected
(imported at module scope, not installed, not used by these functions) and the process must
`chdir` into `code/` because the library hard-codes `../data/...` paths. The released spec, taken
from the function itself: drop the `not_classified` **task** node, **keep** the `none` task node,
drop `none`/`not_classified` **patterns** from each task's base, renormalise the weights over
tasks that have a rate.

### (b) The wave collaboration splits (§8(i)) — the base changes by wave and chapter

| wave | report's word | all-conversation base | five-classified base | published-base match |
|---|---|---|---|---|
| Aug 2025 | "49%" | **49.0980** | **51.0698** | exact (and the enriched file's own `automation_pct` at global is 51.0698) |
| Nov 2025 | "45%" | **45.3554** | **46.7394** | exact |
| Feb 2026 | "44%" | **44.1569** | **45.5456** | exact |

Command: `python data/replication/post1_cuts_c1_c8.py`. Re-run on the fresh cache: identical to
the committed output to four decimals.

### (c) The internal check that licenses the estimator (§8(iii))

Usage-weighted mean of per-task automation (named tasks, `onet_task_pct` weights) against the
wave's five-pattern value: **+0.1303 / +0.2931 / +0.3510 pp** (Aug / Nov / Feb), positive in all
three and inside the brief's stated 0.36 pp tolerance. Keeping the `none` task node as the
released code does gives 51.7424 in August (+0.67). This is **not** suppression — the intersection
publishes **100.00%** of the base named `onet_task_count` (886,107 / 935,027 / 929,714); the two
causes are the named-task restriction (8.13 / 6.49 / 7.03 pp of dropped `none` + `not_classified`
task mass) and the intersection's own `not_classified` **pattern** (41,134 / 52,693 / 54,893
conversations = 4.64 / 5.64 / 5.90% of named counts), which the marginal facet does not have
(1 / 0 / 0 conversations).

### (d) The task-value series on matched windows — the non-reproduction, stated in full

Target: `economic-index-2026-03-report` **Fig. 1.4, p. 8**, Claude.ai "average value of tasks" =
"the average hourly wage of US workers who perform that task" (p. 8), employment-and-time weighted
where several occupations hold a task (footnote 5, p. 11). Anthropic ships **no code** for reports
4–6, so the specification is re-implemented from the released library's conventions plus each
wave's `data_documentation.md`, and is stated in the script's docstring.

| window | published (Fig. 1.4) | rebuilt on C6 (`wage_data.csv`, 2019 scrape) | rebuilt on C7 (BLS-EP 2025 medians) |
|---|---|---|---|
| 4–11 Aug 2025 | $48.9 | **$35.3420** | **$37.6440** |
| 13–20 Nov 2025 | $48.3 | **$35.0758** | **$37.6911** |
| 5–12 Feb 2026 | $47.9 | **$34.3590** | **$37.5460** |
| **Nov → Feb change** | **−$0.40** | **−$0.7168** | −$0.1450 |
| **Aug → Feb change** | **−$1.00** | **−$0.9830** | −$0.0980 |

Both pairs the brief quotes reproduce: −$0.40 vs −$0.72 and −$1.00 vs −$0.98. The "−$1.40" of the
brief's first version compared a published **Jan-2025 → Feb-2026** change with a Nov → Feb rebuild;
on matched windows that pairing does not arise. Coverage, audited: C6 prices 2,607 / 3,154 / 3,244
tasks = **99.35 / 98.98 / 99.30%** of named mass, C7 2,042 / 2,534 / 2,593 = **55.66 / 58.52 /
62.22%**; the C5 merge is 2,616 / 3,168 / 3,258 in, **all matched**, 0 unmatched.

**The level does not reproduce, and this session quantifies the largest identified cause.** On the
2,042 / 2,534 / 2,593 tasks priced by **both** sources — a like-for-like set — BLS-EP 2025 medians
sit **+24.06 / +24.88 / +25.15%** above the 2019 O\*NET website scrape ($30.34 vs $37.64, $30.18 vs
$37.69, $30.00 vs $37.55). Carrying that uplift onto the full C6 set gives **$43.85 / $43.80 /
$43.00** against the published $48.9 / $48.3 / $47.9 — so **vintage plus deflator account for about
three quarters of the $13.5 level gap, leaving ≈$4.50–$5.05/hr (about 10%)**. That residual is
attributable to the two causes the public files cannot supply: no time-on-task weights, and
equal-split or employment weights in place of employment-and-time weights; a third, smaller
channel is the universe (Anthropic's occupational coverage is not the 99% of named mass this join
reaches). The four causes in the brief's §8(iv) therefore stand, now with a size on the first two.
No further specification was found that closes the gap: alternative aggregations (equal-split,
employment-weighted, modal holder, intersection-count weights, unweighted task mean,
cap-excluded) span **$33.11–$35.37** and none approaches $48.

Command: `python data/replication/post1_taskvalue_matched.py` (new; check block asserts all six
levels, both matched-window changes, both coverage series, the common-set N, and that the level
gap exceeds $10 — the recorded non-reproduction is itself asserted, so a silent change in the
wage file would fail the script).

---

## 3. Every committed post1 check, re-run on the fresh cache

| script | what it covers | result |
|---|---|---|
| `post1_cuts_c1_c8.py` | C1–C4 row counts, patterns, floors, node-set relations, the published splits, the internal check, C8 Seychelles | **byte-identical** to the committed output |
| `post1_joins_c5_c7.py` | C5/C6/C7 merge audits, wage coverage, multi-holder rules, Kish N, quartile boundaries | **byte-identical** |
| `post1_variance_mde.py` | the three variance models, SOC major groups, the API exploratory cut, wage top-coding | **byte-identical** |
| `post1_cuts_c9_c10.py` | C9 `use_case`, C10 March-2025 per-task file | **byte-identical** to `results/post1_cuts_c9_c10.txt` |
| `post1_replicate_fig211.py` | the released library | **byte-identical** |

The four feasibility-session scripts pool to the first 238 lines of
`data/replication/results/post1_feasibility_checks.txt`; `diff` against the committed file is
**empty**. The seeded bootstraps are therefore reproducible as well as the closed-form numbers.
Spot-confirmations against the numbers `feasibility.md` records:

- **C1–C3 rows** 14,454 / 16,778 / 17,530 at `geography == 'global'`, `level '0'`, seven patterns,
  `min(_count) = 1`, per-task `_pct` summing to exactly 100; **0 intersection rows outside global**.
- **C4** base nodes 2,618 / 3,170 / 3,260; named mass 91.8727 / 93.5144 / 92.9714; `onet_task_pct`
  summing to exactly 100.000000; `min(onet_task_count) = 15`.
- **C5** 19,530 rows → 18,428 keys, 974 codes, 775 7-char SOCs; all named nodes matched, 0
  collisions. **C6** 970 of 974 on the 10-char key, 0 of 775 on `[:7]`. **C7** 831 rows, 670 of 775
  matched, Spearman with C6 0.9869 / 0.9859 / 0.9870.
- **Analysis set** 1,802 / 2,075 / 2,188 tasks, 89.2530 / 89.9892 / 89.7348 pp of the wave =
  97.15 / 96.23 / 96.52% of named mass, on 818,673 / 854,432 / 848,716 classified conversations;
  losses 5 / 12 / 12 and 805 / 1,079 / 1,056 as recorded.
- **Kish effective N** 99.7 / 89.5 / 134.3 (named) and 94.4 / 83.4 / 125.7 (analysis set); by wage
  quartile Q1→Q4 62.3 / 43.3 / 22.2 / 13.7, 55.6 / 37.7 / 22.0 / 11.5, 51.0 / 50.6 / 36.8 / 16.5.
- **MDE(80%, two-sided 5%)** (a) conversation-level binomial **0.42 / 0.42 / 0.43 pp**
  (SE 0.151 / 0.148 / 0.154 pp); (b) design-based task bootstrap **12.49 / 17.43 / 16.10 pp**;
  (c) the first brief's literal spec 3.26 / 3.44 / 3.68 pp. §9(4)'s 0.42–0.43 pp confirmed.
- **Quartile boundaries** on the primary wage rule $25.78 / $35.79 / $43.40 (Aug), $25.78 / $34.56 /
  $43.40 (Nov), $24.00 / $34.40 / $43.40 (Feb), Q4 running to the $100.00/hr top code.
- **C9** 13,908 / 14,430 rows, 0 at any other geography, **0 rows in August**; published-`work`-cell
  mass **87.9153 / 86.9555** of 93.5144 / 92.9714 named; both cells 76.9463 / 69.6432; work-dominant
  set 943 / 1,071 tasks; 29 Nov / 21 Feb analysis-set tasks publish only `not_classified`.
- **C10** `task_pct_v2` → `by_task` **3,365 in, 3,364 matched, 1 unmatched and it is `none`**;
  matched mass 98.2183 of 100; classified-weighted 90.1561; `filtered == 1.0` on 1,066 rows;
  analysis-set reach 1,635 / 1,843 / 1,904 tasks at 98.78 / 98.49 / 98.08% of mass.

**Two figures were not re-runnable from a committed script and now are.** Lines 239–274 of
`results/post1_feasibility_checks.txt` (the Seychelles shares, the pre-registered SC>10% / >20%
task sets with their quartile mass, the top-10 concentration on both denominators, the
intersection count split, and the task-value means) came from a scratch script that was never
committed — a gap, since C8 and §10 pre-register cuts that depend on them. They are now reproduced
with check blocks by `post1_c8_concentration.py` and `post1_taskvalue_matched.py`, and every value
matches: SC `usage_count` 24,715 (2.47181% of the wave), 67 nodes / 65 named carrying 93.7609% of
SC's mass, **0** `onet_task::collaboration` rows for `SC`, max named-weight shift **0.5823 pp**
(mean 0.00119), SC up to **64.3%** of one task's global count (median 4.77%), **23 tasks >10%**
holding **11.594 pp** of the wave of which **9.039 pp in Q4**, 14 tasks >20% holding 1.966 pp,
top-10 concentration 22.9409 / 24.2471 / 19.4410 of the wave = 24.9703 / 25.9288 / 20.9107% of
named mass.

---

## 4. Deviations from `feasibility.md`

**No numerical deviation.** Every figure in `feasibility.md` §1, §2, §4 and §7 reproduced on the
fresh cache, most of them byte-identically. Three wording-level items, none of which changes a
decision rule:

1. **`feasibility.md` §2(iii) compares mismatched windows.** It reads "Direction preserved (−$0.72
   against the published −$1.40)". The −$1.40 is the published **Jan-2025 → Feb-2026** change; on
   matched windows the pairs are **−$0.40 vs −$0.72** (Nov→Feb) and **−$1.00 vs −$0.98** (Aug→Feb),
   which is what `BRIEF.md` §8(iv) now says and what §2(d) above reproduces. The same stale
   comparison sat in `data/ATLAS.md` log (f) 13 and has been corrected in place there; this note is
   the record for §2(iii), which is a closed file.
2. **The brief's §9(4) parenthetical** attributes SE 0.151 / **0.149** / **0.151** pp to the
   referee's reproduction; the steward's model (a) gives 0.151 / **0.148** / **0.154** pp. The
   MDEs agree to two decimals (0.42 / 0.42 / 0.43 pp), so nothing in the design moves; the
   difference is presumably the analysis-set construction, and it is flagged to the lead in
   `room/steward-2026-09-17-replication-post1.md` rather than edited into a file I do not own.
3. **Two SC weight-shift numbers are both correct and are different statistics.** 0.5823 pp is the
   maximum shift when SC's **named** nodes are netted out of the named-task weights (the cut C8
   pre-registers); 0.54487 pp is the maximum when all 67 SC nodes are netted from all base nodes.
   `feasibility.md` quotes the first and `post1_cuts_c1_c8.py` prints the second.

---

## 5. What has been seen (for the analyst's disclosure section)

Every quantity this session computed that bears on post1, exhaustively:

- **Frame and coverage counts:** all C1–C10 row counts, node sets, thresholds, floors, residual
  masses and merge audits listed in §3; the analysis set (1,802 / 2,075 / 2,188 tasks) and its two
  audited losses.
- **Wage distribution:** the usage-weighted mean hourly wage per wave on both sources, the
  matched-window changes, the common-set uplift, the four alternative aggregations, the wage
  quartile **boundaries** and each quartile's task count, usage mass, Kish N and classified
  conversation count, and the wage cap exposure.
- **Automation shares at the wave level only:** the three published splits on both bases
  (49.0980 / 51.0698, 45.3554 / 46.7394, 44.1569 / 45.5456), the SC-netted November value
  (46.7394 → 45.4868), the usage-weighted mean of per-task automation for the §8(iii) internal
  check (51.2001 / 47.0325 / 45.8966, and 51.7424 with the `none` node), the March-2025 window's
  43.2902 against its published 43.0619, and Figure 2.11's country-level regression (−3.111834).
  All of these are **global or wave aggregates**, already published or already in `feasibility.md`.
- **Variance only, not level:** the SEs and MDEs of the top-minus-bottom difference under three
  models, plus the task-level sd of the automation share by quartile (27–31 pp) and Q1/Q4 Kish N.
- **Use-case mix by wage quartile** (C9), already recorded in `feasibility.md` §7 and
  `data/ATLAS.md` log (n) 4: work share Q1→Q4 32.60 / 48.69 / 42.05 / 61.91% (Nov) and 28.97 /
  51.21 / 42.85 / 61.65% (Feb).

**Not computed, and deliberately not seen.** The headline **D** (top-minus-bottom quartile
difference in the automation share) in any wave, on any wage rule, under any leg; **Δ_W** (the
wage-weighted minus unweighted automation share); **any quartile's automation share**; the
continuous wage slope; and every H1/H2/H3/H4 leg, including the SOC-15 and work-dominant
re-estimates and the permutation null. `post1_joins_c5_c7.py` and `post1_variance_mde.py` form
quartile automation means *inside* their bootstrap loops, but neither prints, writes or returns
them — only standard deviations of resampled differences leave the functions, and no output file in
`data/replication/results/` contains a quartile automation share or a value of D. The
`/tmp/p1/tk_*.csv` working tables do carry a per-task `autom` column; they are scratch, outside the
repository, and were not aggregated by quartile in this session.

---

## 6. Commands run, 2026-09-17, from `/workspace/economic_research`

```bash
# 1. cache, from empty
for r in release_2025_09_15 release_2026_01_15 release_2026_03_24 \
         release_2025_02_10 release_2025_03_27; do python data/fetch/$r.py; done
#   -> 75 files, 365,467,713 B, every size and sha256 = data/releases/INDEX.md
for r in release_2025_02_10 release_2025_03_27 release_2025_09_15 \
         release_2026_01_15 release_2026_03_24; do
  (cd data/cache/$r && sha256sum -c CHECKSUMS.txt); done     # 14/16/38/4/3 OK, 0 failed
python data/fetch/supplementary_onet.py        # 2 files, 11,612,403 B, sha256 = the pins
python data/fetch/supplementary_bls_ep.py      # NEW: 200, 1,397,448 B, 831 detailed-SOC rows

# 2. replication
python data/replication/post1_replicate_fig211.py    # released library: -3.111834 / 0.393687 / 111
python data/replication/post1_taskvalue_matched.py   # NEW: matched-window task value + check block
python data/replication/post1_c8_concentration.py    # NEW: C8 + §10 concentration + check block

# 3. the committed checks, re-run
python data/replication/post1_cuts_c1_c8.py
python data/replication/post1_joins_c5_c7.py
python data/replication/post1_variance_mde.py
python data/replication/post1_cuts_c9_c10.py
cat /tmp/p1/{a,b,c,d}_out.txt > /tmp/p1/pooled_new.txt
head -238 data/replication/results/post1_feasibility_checks.txt > /tmp/p1/pooled_old.txt
diff /tmp/p1/pooled_old.txt /tmp/p1/pooled_new.txt          # empty
diff data/replication/results/post1_cuts_c9_c10.txt <(python data/replication/post1_cuts_c9_c10.py)  # empty
```

Outputs: `data/replication/results/post1_taskvalue_matched.txt`,
`data/replication/results/post1_c8_concentration.txt`,
`data/replication/results/post1_feasibility_checks.txt` (unchanged),
`data/replication/results/post1_cuts_c9_c10.txt` (unchanged). Atlas entry: `data/ATLAS.md` log
**(o) 2026-09-17**.
