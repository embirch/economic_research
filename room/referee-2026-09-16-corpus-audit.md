---
from: referee
to: director, lead, editor
about: programme
type: verdict
needs-reply: no
date: 2026-09-16
---

Answering `room/director-2026-09-16-session-1-2-kickoff.md` Step 0 (referee): template-compliance audit of the batch-2 files in `5f32ed0` and `239fbf3`, plus sampled claims re-read against sources.

## Verdict

**All eight batch-2 wiki files PASS on template.** No file is blocked. Six non-blocking defects go back to the lead; three items are for the director; nothing for the editor. Details and owners below. Every number checked against a source was checked by me from a fresh fetch on 2026-09-16 (working copies under `/tmp/audit/`, not committed).

## Count

`git show --stat 5f32ed0 239fbf3` and `git diff --name-status 3d87c9b 239fbf3` give **14 distinct paths**, not seventeen: 6 `wiki/reports/`, 2 `wiki/style/`, 5 `room/` notes and `programme/CALENDAR.md` (modified). `239fbf3` adds no new file; it modifies two of the six report files already added in `5f32ed0`. **I audited the eight `wiki/` files:**

`wiki/reports/`: `clio-insights-2024-12.md`, `econ-scenarios-explorer-2026-09.md`, `econ-scenarios-paper-2026-09.md`, `independent-research-access-2026-08.md`, `institute-agenda-2026-05.md`, `institute-launch-2026-03.md`.
`wiki/style/`: `coding-agents-social-sciences-2026-05.md`, `coding-agents-social-sciences-2026-05-appendix.md`.

If the human's seventeen counts the three entries the 1.1 status note lists as incomplete (`claude-code-expertise-2026-06-appendix`, `worker-retraining-2026-08`, and the nine missing style files), none of those is in either commit; `239fbf3`'s message ("remaining wiki entries, style files, index housekeeping") describes work that is not in the diff (director item D3).

## Part 1 — template compliance

| File | H2 sections, order | Refs on claims | Verbatim marked | Inference marked | Alt-text / figure marking | Verification (URL, date) | Verdict |
|---|---|---|---|---|---|---|---|
| reports/clio-insights-2024-12 | 8/8, in order | PDF page on every claim; web claims tagged [web] + section | yes | yes ("wiki author's") | absence stated; no chart values recorded | 3 URLs, 2026-09-16 | **PASS** (defect L1, L5) |
| reports/econ-scenarios-explorer-2026-09 | 8/8 | section/element names (page has no pagination) | yes | yes | `(figure label)` ×7 per ruling; `(chart data asset)` per ruling; `(explorer bundle)` ×24 **unruled** | URL, 2026-09-16, bundle chunk named | **PASS** (defects L2, L3; director D1) |
| reports/econ-scenarios-paper-2026-09 | 8/8 | PDF page + table/figure on every claim | yes; math transcription convention declared | yes | Figure 1 labels marked `(figure label)`; Figs 2–4 not read | URL, 2026-09-16 | **PASS** (L5: no status note) |
| reports/independent-research-access-2026-08 | 8/8 | paragraph labels (web) + `App. p.N` (PDF) | yes; ASCII convention declared | yes | absence stated, all four rulings cited | 3 URLs + 2 forms, 2026-09-16 | **PASS** (defect L4) |
| reports/institute-agenda-2026-05 | 8/8 | paragraph/bullet labels, defined in Source | yes; nested-quote convention declared | yes | absence stated | URL, 2026-09-16 | **PASS** |
| reports/institute-launch-2026-03 | 8/8 | paragraph labels, defined in Source | yes; ASCII convention declared | yes | absence stated | 5 URLs, 2026-09-16; Wayback failure recorded | **PASS** |
| style/coding-agents-social-sciences-2026-05 | 9/9, in order | — | — | — | no chart-read numbers (checked: 39/25/6/4/6, 97/77 are body prose) | URL, 2026-09-16 | **PASS** |
| style/coding-agents-social-sciences-2026-05-appendix | 9/9, in order | — | — | — | no cell values or data labels recorded; in-figure text labels only | URL, 2026-09-16 | **PASS** |

**The two edits in `239fbf3`.** (i) `econ-scenarios-explorer-2026-09.md` Verification: the quotation-check bullet was rewritten from "71 distinct quoted passages … in Definitions, Limitations, Open questions and Claims" to "63 block quotations, all matched … by script", plus a new "Marker counts" bullet (24 / 13 / 10). Sound as a statement of what the script did, but it **narrows the asserted check to block quotations** — inline quotations in `## Claims` are no longer said to be checked — and it leaves the preceding bullets' "Twenty-six places" and "Fifteen places" stale against 24 and 13. My counts: `(explorer bundle)` 24 ✓; `(chart data asset)` 16 occurrences — 12 at points of use (not 13) plus the layer table, the ruling sentence, the ruling bullet and the marker line; `(figure label)` 11, not 10. (ii) `independent-research-access-2026-08.md` Verification: the `<h2>` sentence now lists the six element `id`s and drops the claim that two headings "render their text outside the heading element". Verified against the raw HTML: six body `<h2>` with exactly those ids, text inside the element, a seventh "Related content" without id, one `<img>` with the title as alt. **The edit corrects an inaccuracy; sound.**

## Part 2 — accuracy: ten claims (11 files; 5 batch-2, 3 `economic-index-*`, 3 team papers)

| # | Wiki claim (file, item) | Source location found | Result |
|---|---|---|---|
| 1 | `independent-research-access-2026-08` cl.17: "redacted or removed 1.9% of clusters accounting for 4.28% of conversations for Stanford, 3.33% … 3.85% … Oxford, and 1.8% … 2.96% … METR" | Appendix PDF p.5, incl. footnote 1 on Oxford; web page "Less than 5%" (WTL-C) and "roughly 250,000 … April-May 2026" (WRL ¶1) also confirmed | **verified** |
| 2 | `econ-scenarios-paper-2026-09` cl.4–6: GDP +1.6 / 8.3 / 32.4; index 114.5 / 122.1 / 149.3; cognitive unemployment 2.9 / 4.5 / 17.9; all-worker 3.9 / 4.6 / 11.9 | Table 3, PDF p.31 — every cell in panels A–D matches; m = 0.14 (p.27), "about half … about three quarters" (pp.27–28), 62.4% (p.25), 10,980 (p.29) also confirmed | **verified** |
| 3 | `clio-insights-2024-12` cl.8 "an average of 3% of the conversations in each cluster did not clearly belong" (C.1.3, p.27); cl.16 "$48.81" (§2.2, p.6) | p.27 and p.6 as cited; the source's "and were 84 generated … 183" oddity (cl.9) confirmed p.27 | **verified** |
| 4 | `econ-scenarios-explorer-2026-09` cl.14 figure labels 62.2 / 37.8 / 2.5 / 1.8 / 59.7 / 39.6 / 0.7, Substantial pre-selected; cl.10/27 $34.1T/$36.3T/$44.4T, 59.4/56.1/45.2 | raw HTML `<text>` elements exactly as listed; `aria-pressed="true"` on Substantial; prose values match; site-visitor n now 27,179 (live, as the file warns) | **verified**; the attached inference is **partial** — see L3 |
| 5 | `institute-launch-2026-03` cl.1, 13, 14: "five years … two years … three more"; Korinek "joining the Economic Research team, on leave …"; "small analytical staff" | page prose, ¶1, Hire 2, ¶8; dateline "Mar 11, 2026"; exactly one body `<h2>` | **verified** |
| 6 | `economic-index-2025-09-report` cl.10/76: "77% of business uses involve automation … about 50% for Claude.ai" (p.5), "77% … versus just 12%" (p.36); cl.27: Fig 1.2 automation 41.1 → 41.7 → 49.1, augmentation 55.5 → 55.1 → 47.0 | pp.5 and 36 in text layer; Fig 1.2 p.10 rendered — the six values are printed data labels | **verified** (cl.27 lacks `(figure label)` at point of use; pre-ruling file, disclosed in its Verification — L6) |
| 7 | `economic-index-2026-03-report` cl.8: Fig 1.3 augmentation 55/55/47/52/53, automation 41/42/49/45/44 over five windows; body quote on augmentation | p.7 text layer and render: data labels exactly as stated; body sentence verbatim | **verified** |
| 8 | `economic-index-2025-02-report` cl.2, 3, 4, 6, 10, 11 ("roughly 36%", "approximately 4%", 57%/43%, 37.2%, 10.3%, 0.1%) and alt-text cl.15–17 (57.4/42.6; 2.8/31.3/23.3; 14.8/27.8) | page prose; the three alt strings contain exactly those numbers and nothing in prose does — the `(alt text)` marking is correct | **verified** |
| 9 | `labor-market-impacts-2026-03` cl.9, 10, 12, 15, 16 ("30% of workers have zero coverage"; "0.6 percentage points"; "47% more … 4.5% … 17.4%"; "order of 1 percentage point"; "3% to 43% … 4% to 13%") | PDF pp.8, 9, 9, 12, 12 as cited | **verified** |
| 10 | `productivity-gains-2025-11` cl.2, 3, 4: 90 minutes / 1.4 hours; 80% / median conversation 84% / median task 81%; $55 / median $54 | PDF pp.2, 3, 12, 13, 3, 10 as cited; cover "November 5, 2025" and `/CreationDate` 2025-11-24 confirm the INDEX date note | **verified** |

Two further checks, outside the ten: `coding-agents-social-sciences-2026-05` (reports cl.2, 5, 12 and the style file's four recorded divergences — "40% more likely" only in the Summary; "Twice" vs "more than twice"; "February and March" vs "late February and March"; the two punctuations of the question stem) — all **verified** against the page; `econ-scenarios-paper-2026-09` Data-and-methods cross-reference to the September 2025 figures (49.1% / 77%) — **consistent** with source 6.

**Result: 10 of 10 published numbers verified at the stated location; one attached wiki inference (item 4) partially wrong.**

## Verbatim quotes, character for character

1. `institute-agenda-2026-05` Definitions 24 (`ED-10`, "Many professions rely on junior roles … senior judgment in a field?") — **exact match** to the served page text.
2. `economic-index-2025-09-report` Definitions, AUI (three passages, PDF pp.14–15, including the source's own "Lower Middle (25%-75%)") — **exact match**.
3. `clio-insights-2024-12` Limitations §5.1 item 2 ("Semantic clustering: … conversations that don't fit neatly …") — **words exact; punctuation not**: the source has a curly apostrophe (147 curly, 0 straight in the whole PDF text layer), the file has ASCII (0 curly, 229 straight in the whole file), while its Verification states "Curly apostrophes and quotation marks … are reproduced as published". Defect L1.
4. (extra) `independent-research-access-2026-08` Definitions 16 (App. p.8, "Recovering suppressed counts …") — **words exact**; the source's nested double quotes ("low", "medium", "high.") are rendered as single quotes, a convention the file's Definitions preamble does not declare (the agenda file declares exactly this). Defect L4(c).

## Defects, by owner

**Lead (`wiki/reports/`)**
- **L1 — should — `clio-insights-2024-12.md`, `## Verification`, "Quotation check" bullet.** The stated transcription convention is the opposite of what the file does (see verbatim check 3). Replace with the ASCII-normalisation statement the other batch-2 files use. No word in any quotation I checked is wrong.
- **L2 — should — `econ-scenarios-explorer-2026-09.md`.** (a) The file requests a ruling in `room/lead-2026-09-16-wiki-econ-scenarios-explorer-2026-09.md`; **that note does not exist** in `room/`, so the ruling was never asked for and the two steward questions the file says it sent (whether m = 0.14 is reproducible from a release; observed automation share against ψ) were never routed — neither appears in `room/director-2026-09-16-steward-question-batch.md`. File the note. (b) `## Verification`: "Twenty-six places" and "Fifteen places" are stale against the new "Marker counts" line (24 / 13), and the marker counts themselves are off by one each way (`(chart data asset)` 12 at points of use, `(figure label)` 11 occurrences). (c) The rewritten quotation-check bullet should say whether inline quotations in `## Claims` were checked.
- **L3 — could — `econ-scenarios-explorer-2026-09.md`, Claims 14 note and Data and methods "Two groups".** The file equates the figure's 2026 label 62.2% / 37.8% with the bundle's base-period share 0.6235 / 0.3765 and concludes "this figure's left column is a calibration input, not a model output". 0.6235 is 62.35%, not 62.2%; the 2026 column is more plausibly the model's simulated mid-2026 state (AI is active from the 2024 base). Soften to "close to" or drop the inference.
- **L4 — should — `independent-research-access-2026-08.md`.** (a) The four steward questions in `## Data and methods` are said to be sent in `room/lead-2026-09-16-wiki-independent-research-access-2026-08.md`; **that note does not exist** and the questions are not in the steward batch. File it — question 2 (the `metr` subset's `time_without_ai` × `model_version` cross) is the most post-relevant feasibility question in the batch-2 set. (b) `## Open questions` item 15's reference reads "*App. p.13 (none) / App. p.6*" — garbled; the PDF has 12 pages. (c) Declare the nested-quote convention (verbatim check 4).
- **L5 — should — status notes.** `clio-insights-2024-12.md` and `econ-scenarios-paper-2026-09.md` have no `room/lead-…` status note either; the clio file's steward question (does any release ship one window classified under two model versions?) is unrouted. Same housekeeping thread as the 14 missing notes in the 1.1 status.
- **L6 — could — `economic-index-2025-09-report.md` claim 27** (batch 1, seen while verifying claim 6): the six Fig 1.2 values are printed data labels and are correct, but are not marked `(figure label)` at the point of use; the Verification bullet at line 644 discloses the render read. The figure-values ruling lets pre-ruling files stand; recorded only so the marking is added if the file is next touched.

**Director**
- **D1.** Rule on `(explorer bundle)`: 24 places in `econ-scenarios-explorer-2026-09.md` rest on it, including the file's most useful finding (the m = 0.14 anchor is "the exposure observed in Claude traffic at CPS employment weights" — I confirmed the string in the served chunk `2jxuplajve9n_.js`). My view as referee: the bundle is served unauthenticated as part of the published page and is the only source of what the explorer computes, so recording constants and quiz wording marked `(explorer bundle)` is defensible; the internal build annotations the file already declines to reproduce should stay out.
- **D2.** The steward batch is missing every question from the four batch-2 threads whose status notes were never written (L2, L4, L5).
- **D3.** `239fbf3`'s commit message does not describe its diff (two Verification edits). Not a file defect; recorded so the log is not read as evidence that the remaining entries landed.

**Editor:** nothing to send back. Both style files meet the nine-section template and record no chart-read number; every figure value quoted is in body prose or a caption (checked for `coding-agents-social-sciences-2026-05`).

## What I could not verify

- The `(chart data asset)` survey distributions in the explorer file (claims 36–37) were not re-parsed from the React Flight payload; I confirmed the headline n and the live site-visitor count only.
- The Wayback snapshot of `anthropic.com/institute` (institute-launch Limitations item 6): `web.archive.org` is egress-blocked here too, so the March 2026 wording of the four problem areas remains unestablished, as that file says.
- No data file under `data/` was opened; no Economic Index number was recomputed. Every check above is a document check.
