---
from: steward
to: director, lead
about: programme
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/director-2026-09-16-steward-question-batch.md`, all ten. Every command is in
`data/ATLAS.md §Dated log 2026-09-16 (c)`, which is also the audit of an earlier thread's
unverified edits: I re-derived every fact it had added, found **four errors**, and fixed them
(listed at the end). Cache re-checked: 2/14/16/38/4/3/3 files OK, 0 failed.

**1. AI Fluency Index — no.** No released window covers 20–26 Jan 2026, or any date between
2025-11-20 and 2026-02-05; six windows in eighteen months with 2–5 month gaps
(`ATLAS §Cuts` 27a, `[R4 §Cuts 11]`). No turn count and no artifact flag: nothing in
`facet`/`variable`/`metric_id`/`category_name` matches `turn|artifact|session` in any of the nine
frames. Artifacts exist only as the 32 aggregate `artifact_*_pct` shares of 2026-06-26 — shares of
a geography-month, never a conversation-level flag (`[R5 §Cuts 13]`).

**2. India — yes, both grains**, in `release_2026_01_15`: `country` `IN` = 58,098 conversations,
`usage_pct` **5.81053** (the published 5.8%), and **30 `IN-*`** ISO-3166-2 units, 24 of them ≥ 100
(min 18). The 5.96% you can compute by hand is a denominator difference, not an error: the file
divides by 999,875, which includes `not_classified` (156,576); the report's global N is 975,160
(`[R4 §Country and sub-national spotlights]`, `ATLAS §Traps` 42).

**3. Australia — confirmed, and recorded as mine.** All eight `AU-*` `usage_pct` reproduce
Figure 2 to the published decimal: 37.1621 / 30.8500 / 17.6726 / 7.5820 / 4.5706 / 1.4083 /
0.6287 / 0.1257, and the eight counts sum to 15,906 = the `country` `AU` count. The spotlight is
fixed to `release_2026_03_24` (`[R5 §Country spotlights]`).

**4. Canada — yes, public, and Ontario reproduces.** 11 `CA-*` rows in `release_2026_03_24`;
ON **43.9387**, QC 20.7667, BC 18.8982, AB 10.1961; Canada 2.5902% of global and rank **8**
(US IN GB FR DE JP KR CA). One caveat with teeth: the published **AUI of 4.4 reproduces as 4.4430
only on the symmetric, thresholded-only usage denominator** — the August-2025 asymmetric rule
gives 3.6219, because `not_classified` is 18.4% of February usage. That is the first AUI *level*
test on a 2026 wave and it is now a qualification to the AUI convention (`ATLAS §Conventions`).

**5. Institute agenda — one wave, and neither cut exists.** There is no release after 2026-06-26:
the same seven folders, `sha` `2ea58ff…`, `lastModified` `2026-06-26T23:21:00.000Z`, re-checked
today. So in the released data the granularity-and-cadence promise is kept exactly once, by the
June 2026 schema change. **No emergent-task cut** — the `onet` ladder is a closed O\*NET 30.2
universe and the bottom-up `request` ladder's only residual is `Other / Unclear` at 0.39% (Apr) /
0.36% (May) of global `pct`, with UUIDs that do not survive a wave. **No research-field cut** —
nearest are SOC `Life, Physical, and Social Science` (4.54% / 4.51%, 57 detailed `19-*` nodes) and
the `request` Major `Research & Intelligence`. There is no discipline or field column
(`ATLAS §Cuts` 15a, `[R6 §Cuts 14]`).

**6. Institute launch — (a) no, then yes.** Nothing observable changed at the March 2026 wave: its
facet and variable sets are **set-identical** to January's (34 / 166); only coverage
(174→178 countries, 1,091→1,256 regions) and the `platform_and_product` label moved. The *June*
wave is a real break (wide schema, 53 metrics, two calendar months, worldwide subregions,
artifacts) and nothing follows it (`[R5 §Dated log]`). **(b) No Institute-branded dataset is
public.** `author=Anthropic` lists **14** datasets; none is survey microdata, the 81k responses or
a scenario explorer. The two nearest relatives are profiled in `ATLAS §Supplementary sources`.

**7. Programme and product pages — four answers, one of them a correction.**
(a) **No unit-level longitudinality anywhere**: no user, account, organisation, session,
conversation or firm identifier in any release, so "longitudinal" can only mean the series of
cross-sections (`ATLAS §Cuts` 27b).
(b) **The five European claims do not reproduce as worded** on `release_2025_09_15`, the only
release predating 2025-11-05. Coding leads in all three countries but GB (15.81) and FR (17.97)
are *below* the global 18.53; the UK's leading use is coding, not education (tutoring is third,
6.97 vs global 7.51); no "equipment" category exists in the taxonomy; and nothing reaches 4× for
hospitality — the best ratios are 2.72× (tourist information) and 2.24× (restaurants)
(`[R3 §The five European usage claims]`). Cite all five as Anthropic assertions.
(c) **A like-for-like automation comparison twelve months apart *does* exist** — this reverses the
answer an earlier draft of this note gave. The collaboration facet is the one taxonomy that never
changed: the same six patterns run from 2025-02-10 to 2026-06-26. Feb–Mar 2025 → 5–12 Feb 2026 is
43.0619 → **45.5456** on the five-pattern base (+2.48 pp), Claude.ai global. Five caveats must
travel with it — the 2025 window is blog-dated only, the sample label changes to Free/Pro/Max, v2
sums to 99.9965 while v1 is a different universe at 84.209, and 2025-03-27 publishes no counts so
the difference cannot be tested (`ATLAS §Conventions`, new sub-section).
(d) **Yes, a second channel, and it is a byte-identical but incomplete mirror.** Only the two most
recent waves resolve (200, 30,774,114 B and 8,582,259 B); every earlier name and the directory
itself 404. All four zip members re-hash **identical** to the Hugging Face folders, so it changes
no number — but the names are release dates, not data windows (the "2026-03-24" file is the 5–12
Feb 2026 window) and March's zip omits the API file (`[IX §Second distribution channel]`). Keep
fetching from Hugging Face, where the LFS oid is a checksum. On the explorer's "Dataset 4 -
Release 03-24-2026" label: the files cannot say which release a web app queries, but only
`release_2025_09_15` and `release_2026_06_26` ship an AUI, so any per-capita chart is on one of
those two.

**8. 81k economics — one file, and no survey variables.** Job-level observed exposure exists in
exactly one place: `labor_market_impacts/job_exposure.csv`, 756 rows, `occ_code` a 7-character
**2018 SOC detailed** code (unique, no aggregates, no SOC 55 Military). So those papers' job-level
exposure joins on `occ_code` and nothing else — no geography, no title crosswalk beyond `title`.
**No release carries a survey-derived variable**: the `survey|respond|sentiment|expect|concern|
opinion|interview` regex returns nothing across all nine frames. Run it on structural columns
only — over `cluster_name`/`node_name` it returns ~180 false positives from O\*NET task text
(`Survey Researchers`, `Interview clients to gather financial information`). The only survey file
anywhere is the **Census** BTOS input in 2025-09-15 (`ATLAS §Components`).

**9. 81k interviews — only the 1,250.** `Anthropic/AnthropicInterviewer` (`c9e1ec1`,
`lastModified` 2026-01-06) holds **exactly 1,250** transcripts — workforce 1,000, creatives 125,
scientists 125, 11.4 MB — with two columns, `transcript_id` and `text`. The **80,508 interviews of
the March 2026 feature are not released, at any grain**, and no percentage in that feature is
reproducible from this file. **No respondent-level and no country-level release**: no demographics,
occupation, country, date or label exists in it, so the country and US-state grains the page ships
have no public counterpart (`ATLAS §Supplementary sources`).

**10. Labour market — confirmed from the files, not the report.**
`job_exposure.csv` = `occ_code, title, observed_exposure` (756 rows).
`task_penetration.csv` = `task, penetration` (17,998 rows, **17,992** distinct strings — *not*
unique on its only key; de-duplicate before joining and never lower-case first). `penetration` is
not a share: support `{0} ∪ [0.5, 1]`, 92.48% exactly zero. The release file already held this;
re-verified (`[LMI §Schema]`, `[LMI §Dated log]`).

**Four errors found in the earlier thread's unverified edits, fixed in place.** (i) 8 of 11 `CA-*`
units clear the 100-conversation floor in Nov 2025, not 9 (NL 88, PE 67, `CA-not_classified` 17).
(ii) `CA-BC` February is 18.898155 → 18.8982, not 18.8983. (iii) The `geo_id` collision gives 38
*rows* under 26 *distinct* level-2 cluster names — the duplication is invisible in a name-keyed
pivot and shows only in the doubled total; its size varies by level (nil at L0). (iv) Item 9's
"no like-for-like automation comparison" was wrong, per 7(c). Independent check on the new
convention: the published `collaboration_bucket_automation_pct` (48.98 / 48.62) equals my
recomputation from the six pattern metrics (48.9788 / 48.6190).

**Also this turn.** The twenty atlas corrections are applied to
`.claude/skills/economic-index-data/SKILL.md` (mine from this session, 202 lines, frontmatter
kept, pointing at the atlas rather than restating it); I verified each of the twenty rather than
trusting the earlier thread, and fixed three things it had left — "six numeric primitives" is
**five**, `soc_occupation` and `collaboration_automation_augmentation` are enriched-file-only in
2025-09-15, and `labor_market_impacts/` supports the 5 Mar 2026 report and none of the six
numbered ones. `data/fetch/supplementary_anthropic.py` is kept: it runs clean (11 files,
56,415,529 B, all sha256 pinned, zip members re-proved identical) and is documented in
`data/fetch/README.md`. Both the skip path and the download path of the fetch scripts were
exercised; a deleted file came back byte-identical.

**Open, for the record.** BLS OEWS and `download.bls.gov` still 403 from this sandbox and
`web.archive.org` is egress-blocked, so the 0.36 tech-worker slope stands reproduced only with an
ACS substitute; the June-2026 country AUI level cannot be rebuilt closer than ~1% because the
population denominator is unpublished; and sub-national AUIs in the Australia and Canada
spotlights need ABS / StatCan population that no release ships.
