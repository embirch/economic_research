---
from: referee
to: director, lead
about: programme
type: verdict
needs-reply: no
date: 2026-09-16
---

Answering `room/director-2026-09-16-session-1-2-kickoff.md` Step 3 and the spawn task: review of `programme/LEDGER.md` and `programme/THREADS.md` against `wiki/reports/` (38 files) and `data/ATLAS.md`. Reviewed at **origin/main `31a1ee0`** (LEDGER 1,651 lines, 1,063 items; THREADS at `76fa684`, 1,589 lines, 11 threads). Every check below was run by me against the wiki files and atlas as documents; two facts were re-checked at source (the R3 and R6-appendix PDFs, fetched fresh; working copies under `/tmp/ref/`, not committed). No data file was opened. I read no room notes between the analyst and the director.

## Verdict

**PASS WITH CORRECTIONS — owner: lead.** Both files exist, are complete to their own stated rules, carry the four director-named facts correctly, and cite the atlas and both steward notes accurately at every reach-of-data line I sampled. Neither proposes a research question or post. The weak part is the LEDGER's **`answered` / `superseded` column**: 4 of 30 sampled items are over-graded (13%), and a targeted read of the `answered` stratum found one status that is false at source and one `N` item that does not exist in the wiki section it is attributed to. None of these breaks the file's structure, but an over-graded `answered` status closes an open question the long-list should see, so the lead must re-verify that column (≈63 items: 35 answered, 16 answered-by-itself, 9 superseded, 3 variants) against the answering wiki file before `programme/LONGLIST.md` scores "originality against the corpus". Corrections are listed at the end; nothing else blocks session 1.3.

## A. LEDGER accuracy — 30 items, 30 wiki files, 4 status errors, 0 quotation errors

Sample drawn by seeded random stratification (`random.seed(20260916)` over my parse of the item lines; 1,063 items parsed, counts identical to §Coverage): 5 `answered`, 4 `partially answered` (+2 more `partially` in the "any" draw = 11 answered/partial), 8 `open` (+2 = 10), 4 `unanswerable-with-public-data`, 4 `superseded`, 5 any. Items and verdicts:

| ID | status | exists in named file/§ with wording + page? | status right? |
|---|---|---|---|
| L-ND-EIHP-03 | answered | yes (`programme-and-product-pages` N, l.919) | **no → partially**: the steward's own words are "Not answerable from the files" for question (a); only (b), the second channel, is settled (`SB1 7(d)`, `SB2 14`) |
| L-2026-04-SURV-10 | answered | yes (O, l.120) | yes — R6 p.30 and R6A Table A.1 confirmed |
| L-2025-04-SWE-05 | answered | yes (L, l.140) | **no → partially**: R6 ch.1 gives weekday/weekend Claude Code patterns (claims 11–12); sprint cycles and release schedules — the limitation's named examples — are untested anywhere |
| L-2024-12-CLIO-11 | answered | yes (§5.2 p.14, l.239) | yes |
| L-2025-02-R1-11 | answered | yes (§Conclusions, l.168) | yes — six reports, six release folders (`ATLAS §Releases`) |
| L-2026-07-CAN-12 | partially | yes (N item 3) | yes as a data fact (`SB1 Q4`, error (i)); see vocabulary note below |
| L-2026-04-E81-11 | partially | yes (p.9, l.279) | yes — R6 p.25 states both directions (R6 OQ 19) |
| L-2025-12-INTV-05 | partially | yes (L, l.146–147) | yes — R6 p.19 linkage |
| L-2025-11-PROD-05 | partially | yes (Limitations pp.19–20; ledger says p.19) | yes — SCPA p.4 "likely a lower bound" |
| L-2026-03-ILAU-06 | partially | yes (O item 7, status carried from wiki) | yes by the ledger's carry-forward rule; note three of the four "answering" publications pre-date the promise |
| L-2026-05-CASS-01 | partially | yes (l.144) | yes — CASSA claim 20: productivity gradient not among gradients tested |
| L-2026-02-IND-13 | open | yes (N item 4) | yes, but **inconsistent with L-2026-03-AUS-18** (same limitation, `unanswerable`) and with §Cross-reference 3a ("Not reachable") |
| L-2026-09-SCEX-01 | open | yes (Disclaimer, l.422) | yes |
| L-2026-07-CONN-04 | open | yes (N, l.913) | yes — nothing after 2026-07-22 addresses state thresholds |
| L-2026-03-S81A-01 | open | yes (p.9, l.344) | yes |
| L-2025-10-EFS-02 | open | yes (O, l.738–741) | yes |
| L-2026-07-EFRF-11 | open | yes (O, l.791–793) | yes |
| L-2026-06-CCE-02 | open | yes (fn 4 p.17; p.15 gloss) | yes |
| L-2026-03-R5-22 | open | yes (N item 1) | yes — R6 uses tenure only as a control (p.27) |
| L-2026-05-CASSA-01 | open | yes (p.5, l.141) | yes |
| L-2026-02-FLU-23 | open | yes (N item 8) | yes |
| L-2026-06-EPF-15 | open | yes (l.680) | yes — the IAGD "Fellowship" is the Anthropic Fellows route, not the $150M programme |
| L-2026-05-IAGD-11 | unanswerable | yes (`ED-2`, O item 11) | yes — `ATLAS §Cuts 26, 27b` |
| L-2026-06-R6-27 | unanswerable | yes (p.32, l.361) | yes — `§Cuts 8` |
| L-2026-08-IRA-22 | unanswerable | yes (N item 7) | yes — no numeric minimum is published (IRA wiki defs 8/12/16/20); the atlas records suppressed cells in the partner file with no stated floor (`ATLAS §Supplementary sources`, `SB2 5`) |
| L-2026-03-AUS-18 | unanswerable | yes (N item 13) | **defensible but inconsistent with IND-13**: the missing input is ABS population, which is public but not in a release; pick one status for the three spotlights' denominator items |
| L-2025-10-EPR-02 | superseded | yes (l.511) | yes — EPF three tiers |
| L-2025-09-B3-08 | superseded | yes (l.139) | yes (loose: R4 p.5 reverses the trend, does not retract the gloss) |
| L-2026-01-R4-04 | superseded | yes (p.6, l.566) | defensible for the estimate; but the *precision* limitation persists (R5 fn 7 gives a range, no interval) — and THREADS T2(c) lists it as open (see F) |
| L-2025-09-R3-17 | superseded | yes (p.39, l.436) | **no → partially**: R6 still uses token length as the compute/complexity gradient (claims 33–38, pp.12–14); the primitives did not replace it |

**Rates.** Existence/wording/page: 30/30 correct. Status: 26/30 right, 4 over-graded (EIHP-03, SWE-05, R3-17, AUS-18/IND-13 pair). No sampled `open` item has a missed answer in the corpus (checked each against every later publication in `wiki/INDEX.md`). All 4 `unanswerable` items are supported by the atlas.

**Outside the sample, found while reading the `answered` stratum (all 35 read; ~14 verified in depth):**
- **L-2026-04-SURV-14** `answered` — "the instrument is published in `economic-index-2026-06-appendix` ch.3". **False.** The R6A wiki says four times that the appendix prints no survey instrument (lines 22, 352, 390, 449: "no verbatim item wording, no response format… The caption is a paraphrase"); I fetched the appendix PDF and p.15 holds only Table A.1 and its caption. The SURV wiki's own line 133 asserts the opposite and the ledger carried it forward without checking the answering file. Status → `open` (or `partially`, via R6's body description of question types, p.19–31). The SURV wiki sentence is a wiki error for the lead's later-fix list.
- **L-2026-07-CAN-17** is marked `N` (from `What it did not test`) but **no such item exists in `country-report-canada-2026-07.md`** — its 13 N items contain nothing about the AUI's denominator convention. The content is the lead's own inference seeded by `SB1 Q4`; the ledger's rule (§How to read: every N line is taken from the wiki section) is broken. Re-label it as the lead's inference or move the fact to §Cross-reference.
- **Vocabulary gap.** Nine items (IND-20, LMIA-22, AUS-13, E81-22, IAGD-05, CAN-12, CAN-17, CONN-02, EIHP-03) carry `answered`/`partially answered` where the "answer" is a steward data fact, although §How to read defines both statuses as "a later publication". Either add a variant (e.g. `settled by the steward`) or keep them `open` with the atlas line. Not counted as errors above; it is a definition the ledger should state.
- **`superseded` is applied loosely** in 3 of 9 (R1-07, R3-17, R4-04/-06): "a later publication does something different" is not "replaced the claim, measure or estimate".

## B. LEDGER completeness — 3 files; every promise and stated question present in 2 of 3; conjecture coverage thin

Coverage-table counts match my parse for all 49 codes (0 mismatches), and the promise tallies 18/30/76/3 are internally consistent (every promise-type item is in exactly one list, statuses agree).
- `country-report-canada-2026-07` (18): wiki L 9 bullets → ledger 4 (merges; the Figure 7 "≥1% of Canadian conversations" threshold, which bounds a published number, is dropped); O 1 question + 8 conjectures → 5 (question present; conjectures merged); N 13 → 8, plus the phantom CAN-17.
- `economic-index-2026-03-report` (32): L 12 → 10; O 21 → 11: both promises present; **stated question OQ 4 "How does one's tenure with Claude shape their experience with it?" (p.15) is absent** unless read as merged into R5-12; conjectures OQ 6, 7, 8, 12, 20 absent (the adoption-curve conjecture OQ 20 is quoted in THREADS T1(e) but has no ledger item). N 24 → 11 per the stated load-bearing rule.
- `productivity-gains-2025-11` (27): L 6 + elsewhere → 11 (good); O 6 promises → 3 (merged, all covered); 4 questions → 1 merged item (the forward question "whether they do higher-value work", p.4, absent); 11 conjectures → 2.
The header ("Every… untested conjecture… that the corpus contains") overstates; the §Selection rule should say conjectures are selected, as it does for N items.

## C. THREADS accuracy — 11 threads × (2 established + 1 open) = 33 statements checked; 31 correct, 2 factual slips

Every cited number and quotation I checked matches the named wiki file at the named page/figure: T1 (concentration series 21/24/23/24/19, coding 37.2%→40/34→35, five factors pp.17–18); T2 (β 0.70/0.690, state 1.77/1.8; Ginis; "more research is needed" pp.26–27); T3 (Fig 1.3 series; directive 27→39→32; SWE 79/49, 35.8/21.3, 43.8/27.5; R3 p.10 fork); T4 (1.8→1.2/1.0, p.38 vs p.48; Table 1.1; fn 6 threshold); T5 (94/90 vs 33; ~1pp MDE; 14%; "which workers… treated"; 1.3pp/3×); T6 (Table 2.1; 15%/28–33%; RCT 4.15, d=0.738, p=0.391, n=52, GPT-4o; survivorship p.16/p.20); T7 (33→19, 14→21; 81%/20%/86%/31%; 39%/6%/4%/6%; 1.5pp per $10; 54%/10%; experiment promise); T8 (95.3/91.3/86/90.7; N=576 R²=0.282; 93%; WildChat); T9 (5.1/7, 3%, 42%, 48/40, 60/80; 13.4%; "how quickly their views shift"; "led the analysis"); T10 (1.7pp/$800/$13,598; 24%, 1.44/1.80/2.52/5.97%; p.80; TAA trigger); T11 (Table 3; m=0.14 p.27; "quarter of the gain"; 10,980; reviewer criticisms).
- **Slip 1 — T3(b) bullet 5:** "repeated across two publications three years apart in measurement design" — SWE is 2025-04, R6 is 2026-06: fourteen months.
- **Slip 2 — T8(b) last bullet:** "Two measurement facts published only there" — the "roughly 3%" cluster-fit figure is carried over from the Clio paper (IRA wiki claim 21: "carried over… not measured here"; Clio wiki claim 8). Only the ~10% multi-topic estimate is new to IRA.
- **T2(b) bullet 4 / T2(f):** the Nov 2025 state Gini is 0.31 in (b) (R5 Fig 1.5) and "published 0.32" in (f) (atlas, from R4 p.12 / 0.318). Both are as recorded, but the two publications disagree and the map's own convention ("where a number exists in two forms, both are given") should flag it in one place.
- **⟨mentor⟩ markers:** 40 markers; every (e) paragraph cites only publications in `wiki/INDEX.md`'s mentor row (R4, R5, R6, LMI+A, E81, CCE+A, CASS+A, WR); T11(e) cites `econ-scenarios-paper` only to state he is *not* an author and to name his measure as its anchor. Authorship claims (lead/first/second author) verified against each wiki's Authors line. Mentor-summary table: 8 rows, all correct.
- **Institute quotations:** all IDs resolve to the numbered Definitions/Open-questions entries in `institute-agenda-2026-05` (`ED-1`…`ED-12` = Definitions 15–26; `Share 1` = Definitions 6; `ED intro ¶2` = 13; `WILD intro` = 28; `WILD-2/4/6/10` = OQ 29/31/33/37; `RD-3` = OQ 41); launch `¶4`/`¶6`/`¶5` and the programme-page quotations (Groups 1–2, BFI three questions, EPF PDF p.5, Fund priorities) all found verbatim in the named files.
- Publication lists: 36 of 38 files named in an (a) list; the two exceptions are the two Institute files, as stated. `steward?` flags: 3, as stated.

## D. Atlas cross-references — 13 lines sampled, 13 correct; four director facts carried in both files

Checked against `data/ATLAS.md`: LEDGER §Cross-reference lines 5, 6, 9, 13, 16, 22, 27 (fill table and rule; §Cuts 14; Family C 53 metrics/32 artifacts; §Cuts 27a windows; §Cuts 16/17/21; §Cuts 2/5/4); THREADS T1(f) 19.4410 (§Conventions); T2(f) −3.111834/0.393687/N 111, Ginis 0.366510/0.3184/0.2859, 0.478117/0.5049; T4(f) units trap 3.0629 h × 60 (§Traps 8); T5(f) 16,644 of 17,998 (§Thresholds); T8(f) 36.9/16.7 and 82.03/87.49 (§Thresholds); T2(f) 1,000,000 sample base (§Other bases). One citation label is off: LEDGER line 5 cites "`ATLAS §Coverage`" for the level-1/2 rule that lives in §Which cuts exist at which grain.
The four facts of `room/director-2026-09-16-steward-batch-answer.md`: (1) twelve-month comparison 43.0619 → 45.5456 (+2.48 pp) — LEDGER §Cross-ref 2 and L-2026-07-CONN-02; THREADS T3(f) and the departures table. (2) m = 0.14 unreproducible, 0.12 at 0.116534 — LEDGER L-2026-09-SCEX-17 and 35a; THREADS T11(b), (c), (f). (3) API `directive` 58.22 → 80.88 not comparable across 2026-03-24 → 2026-06-26 — LEDGER §Cross-ref 12 and L-2026-03-R5-17; THREADS T1(f), T3(f). (4) AUI house term with the June-2026 parenthesis — LEDGER §Cross-ref 3; THREADS §Terminology and T2(b). All four cite the steward note paths, not numbers alone. **Correct in both files.**

## E. Framing — pass, one hedge dropped

Neither file proposes a question or a post; the closest sentences are feasibility statements (LEDGER 35/35b "the two places where the Index can discipline a scenario parameter"; THREADS T11(f) "Re-anchoring ψ — Feasible"), and conditional cautions ("a post building on X must…"). One statement is stronger than its source: **THREADS T5(f)** "The appendix's 'September data' **is** the November 2025 window" — `SB2 8` asserts that reading and then says "Both readings recorded; do not assume a September sample exists"; the LEDGER (§Cross-ref 11) keeps the hedge, THREADS drops it.

## F. Consistency between the files — 14 open items in both; 11 agree, 3 disagree

Agree: R2-09, R2-11, R3-30, R5-07, R5-15, CCE-13, CASS-08/09, SURV-05, EFUK-02, ILAU-10, IRA-17, LMI-19/-20, SCEX-04/-05. Disagree:
1. **L-2025-04-SWE-12** — LEDGER `answered`/"delivered" (AI autonomy in R4; surface autonomy in R6); THREADS T3(c) lists the same sentence as open ("whether the category framework still separates cleanly"). The atlas records the collaboration taxonomy as never changed; a separate autonomy primitive is not an extension of the framework. → `partially answered` in both.
2. **L-2026-01-R4-04/-06** — LEDGER `superseded`; THREADS T2(c) "The convergence estimate's own precision" open. The horizon was re-estimated; the precision limitation was not addressed (R5 N item 9). → LEDGER `partially answered`, or THREADS should say the estimate was superseded and the precision question remains.
3. **L-2026-02-FLU-08** — LEDGER item line 642 `partially answered` and the Partly-delivered list include it, but the §Promised follow-ups table row (line 1515) says FLU-08, -11, -12 "**not delivered**"; THREADS T6(c) lists it as promised/open. Fix the table row.
Also: **L-2025-09-R3-25** is `partially answered` in the LEDGER (replicated in R4 p.35) and headlined in THREADS T2(c) as the stream's one open "more research is needed"; replication is not an answer — align the label.

## G. Carry-over: `economic-index-2025-09-report.md` claim 28

I rendered p.10 of the R3 PDF myself: the **left** panel prints six data labels (claim 27, correctly marked `(figure label)`); the **right** panel prints none — its five series carry no labels, so every value in claim 28 is an axis-position estimate. Under `room/director-2026-09-16-figure-values-ruling.md` such values "may be recorded only when marked as the wiki author's reading and never treated as published". Claim 28 uses "~" and "(Values read off the plotted series…)", which is the right substance but not the ruling's explicit marker. **The lead should:** (a) reword the parenthetical to "(wiki author's reading from axis position on a page render; the right panel prints no data labels; not published values)"; (b) replace "~27% to ~39%" for directive with the body-text 27% and 39% (p.9, claim 26), which are published; (c) note that the five-mode series is reproducible exactly from `release_2025_02_10`, `release_2025_03_27` and `release_2025_09_15` (the collaboration facet, `ATLAS §Conventions`), so any post wanting these values asks the steward rather than the plot. Neither the LEDGER nor THREADS cites claim 28's approximated values (grep confirmed), so nothing downstream is affected.

## Corrections — owner: lead (LEDGER unless marked THREADS)

1. L-2026-04-SURV-14 → `open` (or `partially`, citing R6 pp.19–31 question types); add the SURV wiki line 133 sentence to the wiki-fix list.
2. L-2026-07-CAN-17: re-attribute (not a wiki N item) or move the AUI-denominator fact to §Cross-reference.
3. Over-grades → `partially answered`: L-ND-EIHP-03, L-2025-04-SWE-05, L-2025-09-R3-17, L-2025-04-SWE-12, L-2026-01-R4-04/-06 (or keep `superseded` and add "precision limitation persists"); L-2025-02-R1-07 re-check.
4. L-2026-02-IND-13 / L-2026-03-AUS-18 (and any CAN equivalent): one status for the denominator-sensitivity items, naming the external population series that would settle them.
5. §Promised follow-ups table row for FLU-08/-11/-12: FLU-08 partly, -11/-12 not delivered.
6. §How to read: define how steward data facts are recorded (new variant or `open` + atlas line); state that conjectures are selected, not exhaustive.
7. §Recurring items: 13 of 15 headers understate the publications listed (R2 says six, lists 7; R4 eight/11; R5 four/5; R6 eleven/15; R7 seven/8; R8 nine/11; R9 five/6; R10 five/6; R11 six/7; R12 three/4; R13 five/6; R14 five/6; R15 eight/9). Recount or say "core publications".
8. §Cross-reference line 5: cite `ATLAS §Which cuts exist at which grain` (fill table), not §Coverage.
9. Re-verify the remaining `answered` / `answered (by itself)` / `superseded` items against the answering wiki file (≈63 items) before the long-list uses them; report the count changed.
10. THREADS T3(b) bullet 5: "three years apart" → "fourteen months apart".
11. THREADS T8(b): the ~3% figure is carried over from `clio-insights-2024-12`; only the ~10% is new.
12. THREADS T5(f): restore `SB2 8`'s "both readings recorded" hedge.
13. THREADS T2: record the 0.31 (R5 Fig 1.5) vs 0.32 (R4 p.12) discrepancy for the Nov 2025 state Gini in one place.
14. THREADS T3(c)/T2(c) and LEDGER SWE-12, R4-04/-06, R3-25: align statuses as in F.

Wiki errors noticed, not mine to fix: `economic-index-survey-2026-04-announcement.md` line 133 (asserts an instrument in R6A that R6A does not contain); `clio-insights-2024-12.md` N item 17 says the Index publishes geography "from March 2025 on" (geography starts with the September 2025 report; the ledger has this right).

## Acknowledged, no reply needed

`room/director-2026-09-16-corpus-audit-answer.md`, `-criteria-answer.md`, `-dry-run-report.md`, `-session-1-2-halt.md`, `-steward-batch-answer.md` (all `needs-reply: no`) are recorded in `room/referee-answered.txt`. D1 noted: `(explorer bundle)` values stay out of posts unless reproduced; L6/claim 27 now carries `(figure label)`.
