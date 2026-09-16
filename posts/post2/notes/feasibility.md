# post2 (LL-11) · feasibility note

Data steward, 16 September 2026. Brief of record: `posts/post2/BRIEF.md` (commit `e172045`);
lead's status note `room/lead-2026-09-16-brief-post2-status.md`. Authority for every convention
and trap cited here: `data/ATLAS.md` and the per-release profiles in `data/releases/`.

Everything below was run today against the cached files (`data/cache/`, rebuilt by
`data/fetch/<release>.py`, sha256 verified). Two runnable scripts carry the commands and print the
audits:

- `python data/replication/post2_panel_checks.py` — the §8 cuts, the panels, the floors, the
  intersections, the coding set (writes `data/replication/results/post2_panel_checks.csv`).
- `python data/replication/soc15_figA1_2026_03.py` — the replication target (writes
  `data/replication/results/soc15_figA1_2026_03.csv`).

New external input required by the replication and by H4:
`python data/fetch/supplementary_onet.py` (O\*NET-SOC 2010 → 2019 crosswalk; see §3).

---

## 1. Cuts confirmed at column level

Common to every cut below: `geography == "global"`, `facet == "onet_task"`, `level == "0"`
(string), `variable == "onet_task_pct"`; read with `keep_default_na=False, na_values=[]` for CSV
and `df["level"] = df["level"].astype(str)` after a Parquet read (§Traps 1, 2, 6, 7). The key
`(geo_id, geography, facet, level, variable, cluster_name)` is unique in all six frames.

| cut | release · file | nodes (incl. pseudo) | named nodes | `pct` sum | `*_count` sum | floor | verdict |
|---|---|---|---|---|---|---|---|
| 1 | `release_2025_09_15` `data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv` | 2,618 | **2,616** | 100.0 | 964,494 | min count **15** | **CONFIRMED** |
| 2 | `release_2026_01_15` `data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` | 3,170 | **3,168** | 100.0 | **999,875** | min count 15 | **CONFIRMED** (the brief's denominator 999,875 is right) |
| 3 | `release_2026_03_24` `data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` | 3,260 | **3,258** | 100.0 | **1,000,000** | min count 15 | **CONFIRMED** (counts are per million, §Other bases) |
| 4 | `release_2025_09_15` `…/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv` | 2,056 | **2,054** | 100.0 | 944,638 | min count 15 | **CONFIRMED WITH CAVEAT** — see (a) below |
| 5 | `release_2026_01_15` `…/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv` | 2,253 | **2,251** | 100.0 | 971,525 | min count 15 | **CONFIRMED WITH CAVEAT** |
| 6 | `release_2026_03_24` `data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv` | 2,299 | **2,297** | 100.0 | 1,000,000 | min count 15 | **CONFIRMED WITH CAVEAT** |
| 7 | `release_2025_09_15` `data/intermediate/onet_task_statements.csv` (19,530 × 9, O\*NET DB **20.1**) | 18,428 distinct task keys, 974 O\*NET-SOC codes | — | — | join on lower-cased, stripped task text | **CONFIRMED WITH CAVEAT** — wrong SOC vintage for the published number; see §2 |

The two pseudo-tasks are present in every frame and are different things (§Traps 24): `none`
5.7162 / 3.7124 / 4.2922 (Claude.ai, Aug/Nov/Feb) and 4.0509 / 3.5999 / 3.6961 (API);
`not_classified` 2.4111 / 2.7732 / 2.7364 (Claude.ai) and **8.1108 / 8.1210 / 6.0163** (API). The
brief drops both, correctly; note the API residual is three times the consumer one, so the two
surfaces' named mass is not comparable in level (the brief never compares levels — §7(2) — which
is the right call).

**Cuts 4–6, the caveat, and the lead's question (a): `onet_task_count` *does* exist on the API
side, at global, in all three waves** (2,056 / 2,253 / 2,299 rows, one per published task,
minimum 15). `data/ATLAS.md` §Cuts 18 says there is no **`usage_count`** in any API file — that is
a *geography*-total variable and the API has no geography at all (§Cuts 2). It says nothing about
facet counts. So the brief's §Levels sentence ("The API files carry no usage count … so a level
diagnostic is possible on one surface only") is **wrong as written**: the H3 level diagnostic is
available on **both** surfaces. Two conditions on using it: the count is a count of *sampled
records* on bases that differ by wave and surface (964,494 / 999,875 / 1,000,000 on Claude.ai;
944,638 / 971,525 / 1,000,000 on the API — within 5.9%), and an API record is a prompt–response
pair, not a conversation, so an API count is not a count of work (§7(2)). Used as a diagnostic,
not an outcome, as the brief already specifies, this is sound.

**Panel, exclusions and conventions (§8 prose).**

- The **1,241-task six-frame panel is CONFIRMED** exactly: named nodes 2,616 / 3,168 / 3,258
  (Claude.ai) and 2,054 / 2,251 / 2,297 (API); pairwise overlaps 1,603 / 1,823 / 1,908; the
  intersection of all six frames is **1,241**.
- **CONFIRMED WITH CAVEAT on the wording of the mass figures.** The panel carries **80.8906%** of
  Claude.ai and **83.2233%** of API February mass — but those are shares of the **geography
  total**, which includes `none` and `not_classified`, *not* of named mass as the brief's quoted
  line (mine, from the long-list) says. As a share of *named* mass the panel is **87.01%**
  (Claude.ai) and **92.18%** (API). Both bases are defensible; the brief must say which. Full
  set: panel mass 83.1365 / 82.4755 / 82.6289 / 81.5020 / 80.8906 / 83.2233 across the six frames.
- **Wider panels exist and are larger than the six-frame one.** Tasks named on both surfaces in
  *both* waves of a window pair: **1,317** (Aug→Nov) and **1,595** (Nov→Feb), carrying 82.2–84.1
  and 84.5–86.3 of each frame's total. The brief's choice of one fixed 1,241-task panel for both
  windows is the conservative one (a constant sample across windows); the wider panels are the
  natural robustness cut and should be named as such rather than left unmentioned.
- **Case-variant duplicates: none in the Index.** Every frame's `cluster_name` set is already
  lower-cased; 0 duplicates after lower-casing and stripping in all six frames. Trap 21 therefore
  bites only on the *statements* side (19,530 rows → 18,428 distinct keys, several holders per
  key), where the de-duplication rule below handles it. The brief's §8 sentence about
  de-duplicating case-variant task strings is a no-op on the Index side; keep it for the join.
- **Absent ≠ zero** confirmed: no suppression flag in any frame, no zero-`pct` rows, the floor is
  the privacy floor of 15 (minimum published count is exactly 15 in five frames and 16 in the
  February Claude.ai one). Near-floor counts on the panel: tasks with count ≤ 20 number 53 / 59 /
  23 / 48 / 14 / 65 across the six frames, so the brief's near-floor sensitivity (§10) bites on
  ~5% of the panel.
- **The series stopping at 2026-03-24 is right** (§Components, the 58.22 → 80.88 API `directive`
  jump at the Claude Code documentation boundary). Nothing here needs June.
- **"Supplementary data. None." is wrong** for the reproduction leg and for H4's coding set: the
  published SOC-15 series requires an external O\*NET-SOC 2010 → 2019 crosswalk (§2, §3). The
  correlation tests themselves need no external file.

---

## 2. Replication target

**The published number.** `economic-index-2026-03-report`, p.7: "Since August 2025, the share of
tasks in this category has increased by **14%** in the API and decreased by **18%** in
Claude.ai", "this category" being Computer and Mathematical. Its evidence is Appendix Figure A.1
(`economic-index-2026-03-appendix`, p.5, "Task usage share trends by occupation group (V1-V5,
**2019 O\*NET-SOC**)"), and the report also prints, p.5: "tasks associated with Computer and
Mathematical occupations accounting for **35%** of conversations on Claude.ai (see Appendix)".
Footnote 2, p.11: "This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010
vintage."

**Anthropic's released code does not cover it.** Reports 4, 5 and 6 ship no code (§Released code);
the 2025-09-15 library is the specification of record and has no occupational-recode path (and no
`soc_occupation` facet exists in 2026-01-15 or 2026-03-24 — §Cuts 13). The reproduction is
therefore a re-implementation, stated as such.

**Run today. It reproduces — but only on the 2019 vintage, which no released file ships.**
`python data/replication/soc15_figA1_2026_03.py`, merge audit printed (rows in / matched /
unmatched: 2,616→2,616, 2,054→2,054, 3,168→3,168, 2,251→2,251, 3,258→3,258, 2,297→2,297; zero
unmatched in every frame, on both vintages):

| specification | Claude.ai Aug → Nov → Feb | Aug→Feb | 1P API Aug → Nov → Feb | Aug→Feb |
|---|---|---|---|---|
| **2019 O\*NET-SOC** (crosswalk recode, classified base) | **41.9682 → 38.5001 → 34.6150** | **−17.5208%** | **53.8833 → 59.2074 → 61.6363** | **+14.3885%** |
| 2010 O\*NET-SOC (shipped file as-is, classified base) | 39.0706 → 36.0583 → 32.2626 | −17.4248% | 50.0841 → 51.8285 → 51.7084 | **+3.2433%** |
| 2019 vintage, all-conversation base | 38.557 → 36.003 → 32.182 | −16.53% | 47.330 → 52.268 → 55.650 | +17.58% |

**Answer to the lead's question (b): the "+14% API" does reproduce, at +14.3885%, and the
lead's suspicion was right about the cause.** It does **not** reproduce from the public files
alone: on the shipped `onet_task_statements.csv` (O\*NET DB 20.1, the 2010 O\*NET-SOC taxonomy)
the API leg is **+3.24%**, which is the number in my LL-36 line and the number the brief flagged.
The missing ingredient is the vintage the report names in its own footnote. The Claude.ai leg
(−18%) reproduces on either vintage, at −17.52% / −17.42%, which is why it looked fine.

**The specification that reproduces it**, in full, for the pre-registration:

1. global `onet_task` level-0 `onet_task_pct`, per surface, per wave (cuts 1–6);
2. drop `none` and `not_classified`;
3. join the task text (lower-cased, stripped) to the shipped O\*NET 20.1 statements → O\*NET-SOC
   **2010** codes;
4. recode each 2010 code to its **2019** code(s) with the O\*NET Center crosswalk (§3);
5. split a task's `pct` equally across its distinct 2019 codes (the `pct_occ_scaled` rule,
   §Conventions; splitting over occupation *Titles* instead changes nothing to four decimals);
6. renormalise over the matched named mass — the **classified** base. The all-conversation base
   gives +17.58% / −16.53% and does not match the figure.

**Cross-check against the whole of Figure A.1.** On this specification the other seven panels also
land on the appendix's axis readings (`wiki/reports/economic-index-2026-03-appendix.md`, ±0.2 pp,
not published values). API, Aug/Nov/Feb, reconstruction vs reading: Arts 6.01/6.36/5.30 vs
6.0/6.3/5.3; Educational 4.11/4.08/3.10 vs 4.1/4.1/3.1; Office and Administrative Support
6.66/7.21/7.17 vs 6.7/7.2/7.2; Life, Physical and Social Science 8.11/4.62/4.41 vs 8.1/4.6/4.4;
Business and Financial 4.34/3.98/3.92 vs 4.3/4.0/3.9; Management 3.65/3.62/3.63 vs 3.6/3.6/3.6.
Claude.ai matches equally closely, and the February Claude.ai level, **34.6150**, is the report's
published "35% of conversations on Claude.ai". On the 2010 vintage those same panels also match —
except Computer and Mathematical and Office and Administrative Support, which are wrong in
opposite directions and whose **sum** matches on both vintages. That is the tell.

**What the recode actually is, and why the post must carry it.** *(Corrected 2026-09-16 on
`room/referee-2026-09-16-post2-recode-correction.md`. The referee's attribution is right: my first
version named the wrong occupation — 43-9011 Computer Operators — reported the mass on an unnamed
base, and overstated the single task's share of the result. Re-derived with
`data/replication/post2_recode_attribution.py`, which also returns the headline series above, so
both numbers come from one specification.)*

337 of 20,081 (task, code) pairs change major group between the vintages: **34 pairs move into SOC
15 and 36 move out of it**. The into-15 move is the one that matters, and it comes from SOC 43. On
**one named base, the classified (matched named) mass**, it carries **4.3615 (August), 7.8350
(November), 10.3190 (February)** of the API's mass; the February figure is **9.3168 points of the
geography total**, which is the number my first version mislabelled "matched mass". Two 2010 codes
make it up, and the larger is **43-9111.01 "Bioinformatics Technicians" → 15-2099.01
"Bioinformatics Technicians"** at 3.7385 / 7.2796 / **9.7110** of classified mass; **43-9011.00
"Computer Operators" → 15-1299.00 "Computer Occupations, All Other"** carries only 0.6231 / 0.5554
/ **0.6081**. On Claude.ai the same move is 3.4653 / 2.9504 / 2.8419. The out-of-15 leg is one code
pair (15-1199.10 Search Marketing Strategists → 13-1161.01) worth 0.5623 / 0.4561 / 0.3912 on the
API — an order of magnitude smaller, but it is why the net effect of the recode is not the into-15
figure.

Inside the into-15 move, **one task** — "perform routine system administrative functions such as
troubleshooting, back-ups, and upgrades.", which the shipped O\*NET 20.1 statements file holds
under **43-9111.01 Bioinformatics Technicians and no other code** — runs **1.2396 → 3.9479 →
6.7260** on the API (counts 11,710 → 38,355 → 67,260) against **1.6426 → 1.2693 → 1.4451** on
Claude.ai; in February it is 7.4495 of classified mass, i.e. 72% of the into-15 move. But it is
**about a third of the published result, not most of it**: drop the task and the 2019-vintage API
leg is still **+10.0054%** (53.2231 → 58.5483), against +3.24% on the shipped vintage. So the
published "+14% API" is a taxonomy revision first and a fast-growing task second, and the post must
say both. That the task grew 5.4× on the enterprise surface and not on the consumer one is
**consistent with** the brief's H4 (call-splitting); it is not a demonstration of it — no file
attributes a generic system-administration statement, filed by O\*NET under Bioinformatics
Technicians, to Claude Code or to agentic call-splitting. Report it as the first result exactly as
§8 provides, in that language.

**Level comparability, stated.** The reproduction is a *task* taxonomy wearing occupation labels
(§Traps 36: occupation is inferred from the task, never from the user), and the surfaces' units
differ (conversation vs prompt–response pair). The reproduced number is a within-surface time
comparison on one taxonomy, which is exactly what the report claims; nothing here licenses a
cross-surface level comparison.

---

## 3. Supplementary joins tested

The brief says "None". **One is required**, for the replication leg and for any coding/non-coding
split that claims to be on the report's definition:

| item | detail |
|---|---|
| source | O\*NET-SOC **2010 → 2019** crosswalk, O\*NET Resource Center |
| how obtained | `curl -sL "https://www.onetcenter.org/taxonomy/2019/walk/2010_to_2019.csv?fmt=csv"` → 200, 108,052 B, sha256 `8f026a33…ecc5a`; scripted at `data/fetch/supplementary_onet.py`, cached at `data/cache/supplementary/onet_soc_2019_crosswalk/` |
| vintage | the 2019 O\*NET-SOC taxonomy (the one report 5 fn 2 names); 1,164 rows, 1,110 distinct 2010 codes, 1,012 distinct 2019 codes |
| join key | `O*NET-SOC 2010 Code`, against the shipped statements file's `O*NET-SOC Code` |
| merge audit | 19,530 (task key, 2010 code) pairs in → **20,081 (task key, 2019 code) rows out, 0 unmatched 2010 codes**; 18,428 of 18,428 distinct task keys carry at least one 2019 code. The expansion (+551 rows) is the 2010 codes that split into several 2019 codes; the equal-split rule absorbs it |
| coverage against the Index | every named task in all six frames maps: 2,616 / 2,054 / 3,168 / 2,251 / 3,258 / 2,297, zero unmatched |
| licence | O\*NET data, **CC BY 4.0**, requires attribution to the O\*NET program (U.S. Department of Labor). Not the same licence as the Index's CC-BY-no-version |

**Rejected alternative, recorded so nobody repeats it.** Joining the Index task text directly to
**O\*NET 27.3** `Task Statements.txt` (a 2019-taxonomy database, `db_27_3_text.zip`, 200,
11,504,351 B, sha256 `98450a43…92b41`, also in `data/fetch/supplementary_onet.py`) matches only
2,208 of 2,616 / 1,738 of 2,054 / … task strings, because statements were reworded between DB
20.1 and 27.3; it drops 17–28% of each frame's named mass and gives +12.58% / −16.24%. The Task-ID
bridge (20.1 Task ID → 27.3 code) is worse: 16,210 of 19,530 pairs survive, 18–25% of mass is
lost non-randomly, and it gives +24.23%. **Use the crosswalk, not a later O\*NET database.**

No other supplementary source is needed: the panel, the correlations, the within-surface
benchmark and the exploratory tests are all inside the Index.

---

## 4. Hypothesis-by-hypothesis

**H1 · Migration.** *Exists at the stated grain.* Both change vectors are computable for all 1,241
panel tasks in both windows from cuts 1–6. Effective N: **1,241** on the fixed six-frame panel
(the brief's design), or 1,317 (Aug→Nov) and 1,595 (Nov→Feb) on window-specific panels.
Minimum detectable |r| at 5% two-sided, 80% power: **0.0795** at N = 1,241 (the brief's "about
0.08" is right), 0.0771 at 1,317, 0.0701 at 1,595. Caveats: the unit differs across surfaces
(§7(2)); the two shares have different residual masses (`not_classified` 2.74 vs 6.02 in
February), so a renormalised-panel sensitivity is worth pre-specifying, as §8 does; the change is
a difference of two published shares with no published standard error, but both frames carry
counts, so a sampling-error band on each task's share *can* be constructed if the analyst wants
one (approximate, on a sample base, not a design-based SE).

**H2 · Independent growth.** Same data, same N. Feasible. The interval, not a p-value, is the
deliverable, and the MDE above is the number that makes a null measured rather than absent.

**H3 · Common denominator.** The within-surface benchmark is computable from the same vectors. The
level diagnostic is now available on **both** surfaces (see §1(a)) rather than one. **But the
February Super Bowl inflow cannot be identified in the data at all**: there is no user, account,
plan, tenure, signup-date, first-time-user or within-window date field in any release
(§Cuts 26, 27b), and no sub-weekly grain. The inflow can only be handled the way the brief already
handles it — by reporting the two windows separately, naming the inflow beside the
November→February estimate, and reading the window contrast as the test. Say plainly in the post
that the inflow is stated by Anthropic (fn 3, p.18) and is unobservable in the files.

**H4 · Call-splitting.** *Exists, but the coding set is vintage-dependent, and the brief must
pre-specify which vintage.* On the 1,241-task panel, the modal-holder rule puts **242** tasks in
SOC 15 under the 2010 vintage and **242** under the 2019 vintage — with an overlap of only **228**.
The mass difference is what matters: in February the coding set carries **46.31** (2010) vs
**55.29** (2019) of the API's 83.22 panel mass, and 29.42 vs 31.61 of Claude.ai's 80.89. Since the
post reproduces the report's number on the 2019 vintage, the coding/non-coding split should be on
the 2019 vintage too, with the 2010 split reported as the robustness cut; otherwise the post's
"coding set" and its replicated number mean different things. Note also that the single task named
in §2 — the system-administration statement, in SOC 15 only under the 2019 recode — is inside the
coding set on one vintage and outside it on the other, so the vintage choice is not cosmetic, it
sits next to the hypothesis. It is *consistent with* H4, not evidence for it. The brief cites post1
for the task → SOC join and the multi-holder rule (LL-32: allocation rules move the SOC-15 share by
≤0.17 pp, confirmed again here — splitting over codes and over Titles agree to four decimals); the
*vintage* is a separate choice and post1 does not make it.

**Exploratory (b), directive-weighted.** `onet_task::collaboration` exists at global on the API in
all three waves (2,055 / 2,252 / 2,298 base tasks; variables `onet_task_collaboration_pct` and
`_count`). A per-task `directive` share is published for **1,143 / 1,155 / 1,135** of the 1,241
panel tasks (August / November / February). The missing ~90 are suppressed, not zero (§Traps 25),
and the intersection `_pct` is a share of its base cluster, not of the surface (§Other bases).
Feasible, with the coverage stated.

**Exploratory (a), naming the migrating quadrant.** Description only, no data obstacle.

---

## 5. Traps that apply

| trap (`data/ATLAS.md`) | where it touches the brief |
|---|---|
| 1, 2 — `NA` is Namibia; `NONE` is a real pseudo-geography in 2026-03-24 | §8 read rule: `keep_default_na=False`, `na_values=[]`. Harmless at global but the frames are read whole |
| 6, 7 — `level` is a string, and its Parquet dtype differs by wave | §8 already says cast to string; without it `level == "0"` silently returns zero rows on one wave |
| 24 — `none` ≠ `not_classified` | §8 drops both, correctly; the API residual is 2–3× the consumer one |
| 25 — absent ≠ zero, no suppression flag | §8 panel rule (exclude, don't zero) and the exploratory test's 90 missing directive cells |
| 21 — case-variant task strings | a no-op inside the Index (0 duplicates), live on the statements side of the join |
| 36 — occupation is inferred from the task, never the user | §7(2) and every sentence about "coding tasks"; the reproduced figure is a task aggregate wearing an occupation label |
| §Taxonomies — O\*NET vintages differ by folder; the shipped crosswalk is the 2010 vintage while report 5 uses 2019 | §8 cut 7 and the replication target — the single largest issue in this brief (§2, §3) |
| §Components — the API population changes at the 2026-03-24 → 2026-06-26 boundary | §8's decision to stop at February is correct and must stay |
| §Other bases — 2026-03-24 counts are per **million**; `{facet}_pct` includes `not_classified` | the mass statements in §8 and any count-based diagnostic |
| 26 — four files are byte-identical across releases ("v1" *is* the December-2024 release) | Figure A.1's Jan-2025 and Mar-2025 points are the flat family, Claude.ai only; the post must not read them as part of the API series (§7(4) already says the API begins in August 2025) |
| §Taxonomies — request clusters are not comparable across waves | not used here; the design correctly runs on `onet_task`, where 2,888 names and >99% of mass survive between waves |

---

## 6. Verdict

**FEASIBLE WITH CAVEAT.**

Every cut in §8 exists at the grain and coverage the design assumes, the 1,241-task panel and its
mass reproduce exactly, and the published number the post extends reproduces to +14.3885% (API)
and −17.5208% (Claude.ai) against the report's "+14%" and "−18%" — but **only on the 2019
O\*NET-SOC vintage, which no Economic Index release ships**; on the shipped 2010-vintage file
the API leg is +3.24%. The whole difference is the SOC 43 → SOC 15 move — **10.3190 of February
API classified mass, i.e. 9.3168 points of the geography total** — of which **43-9111.01
Bioinformatics Technicians → 15-2099.01** carries 9.7110 and 43-9011.00 Computer Operators →
15-1299.00 only 0.6081 *(attribution corrected 2026-09-16 on
`room/referee-2026-09-16-post2-recode-correction.md`; my first version named the second of those)*.
One task inside the move, the system-administration statement O\*NET files under Bioinformatics
Technicians, grew 5.4× on the API and is about a third of the result: without it the 2019 leg is
still +10.0054%. Four things in §8 therefore
need amending once, before the pre-registration: (i) the API **does** publish `onet_task_count`,
so the H3 level diagnostic runs on both surfaces, not one; (ii) "Supplementary data. None." is
wrong — the O\*NET-SOC 2010→2019 crosswalk is an external input, fetched and checksummed at
`data/fetch/supplementary_onet.py`; (iii) the 80.9% / 83.2% panel-mass figures are shares of the
geography total including `none` and `not_classified` (87.0% / 92.2% of *named* mass), and the
brief must say which base; (iv) H4's coding set must name its vintage — 2019 to match the
replication, with 2010 as the robustness cut — because the two sets differ by 14 tasks and by 9 pp
of API mass, and the recode is where the published result lives. The referee and the lead should
carry this sentence: *the post's headline correlations are internal to the Index and need no
external file, but the published claim it extends is not reproducible from the public files alone,
and the coding set it tests H4 on is a taxonomy choice that moves the API's coding share from 51.7%
to 61.6%.*
