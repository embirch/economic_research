# Programme calendar

Owner: director. Sequencing only; no dates promised. Status is updated at the close of each session.

## Stage 1 · Research briefs

| Session | Scope | Status |
|---|---|---|
| 1.1 Corpus and atlas | `wiki/INDEX.md`, `wiki/reports/*.md` (lead); `wiki/style/*.md` (editor); `data/releases/*.md`, `data/fetch/*.py`, `data/ATLAS.md` (steward). Human reads two wiki entries and one release file for accuracy before 1.2. | closed 2026-09-16; 35/38 wiki, 13/23 style, atlas complete; remainder listed in room/director-2026-09-16-session-1-1-status.md |
| 1.2 Ledger, threads map, criteria | `programme/LEDGER.md`, `programme/THREADS.md` (lead); README criteria and `anthropic-style` skill rewritten from the style corpus (editor); referee samples ten wiki claims and the ledger. Human weights or excludes threads. | closed 2026-09-16; LEDGER.md (1,063 items), THREADS.md (11 threads), STYLE-GUIDE.md, anthropic-style skill, README criteria; referee PASS WITH CORRECTIONS (lead applies at the open of 1.3); human reads THREADS.md before 1.3; see room/director-2026-09-16-session-1-2-status.md |
| 1.3 Long-list and short-list | `programme/LONGLIST.md` with a steward feasibility line per item; `programme/SHORTLIST.md`; referee audits scoring; editor answers each why-it-matters. **Gate 1a**: human chooses. | closed 2026-09-16; LONGLIST 39 survivors with steward lines; SHORTLIST nine (b7a44ca); referee audits 0c77fbf, c168b19; editor notes ×9. **Gate 1a decision: all nine proceed in rank order; scenarios thread excluded; programme is nine posts.** See room/director-2026-09-16-gate-1a.md |
| 1.4 Briefs, batch 1 | `posts/post{1..5}/BRIEF.md` (lead); `posts/post{1..5}/notes/feasibility.md` (steward); editor framing note per brief; referee sweep per brief. **Gate 1b**: per post, post1 first (room/director-2026-09-16-gate-1b-post1.md); posts 2–5 at their turn. | **post1 Gate 1b approved 2026-09-17**; post2 PASS WITH CHANGES; post3/post4 BLOCK awaiting lead passes; post5 sweep not run. Earlier: HALTED 2026-09-16 on API usage limit (returns 2026-10-01). Five briefs, five steward notes (all FEASIBLE WITH CAVEAT), five editor notes committed; referee post2 BLOCK committed; referee post1/3/4/5 and the post2/post5 lead passes died uncommitted. Resume checklist: room/director-2026-09-16-session-1-4-halt.md |
| 1.4 Briefs, batch 2 | `posts/post{6..9}/BRIEF.md` and the same loop. **Gate 1b (batch 2)**: human approves posts 6–9. | not started; do not begin until the human says so |

## Stage 2 · Doing the research (one session per post)

Order set at Gate 1a. Per post: replicate → pre-registration (Gate 2a) → analysis → verification (Gate 2b) → close.

| Post | Candidate | Title (frozen at Gate 1b) | Status |
|---|---|---|---|
| post1 | LL-07 | Is AI delegated more on low-wage work or on high-wage work? (frozen at Gate 1b) | Gate 1b approved 2026-09-17 (brief 9af7bad + b4ad871; items 14–20, 23 applied 8fbffbd). Replication e9a2291 (all match). Prereg: analyst 47faca0 → referee PASS WITH CHANGES 37868c3 (0 blocking) → revision c9b1b45 → second-read SIGN OFF 0a6513f → **committed 066b761. AT GATE 2a** — room/director-2026-09-17-gate-2a-post1.md. Carried to Stage 3: sharpen §2 why-it-matters (human's note); footnote BRIEF §9(4) H4 power ≈0.32 pp as declared (referee-prereg item 3); prereg "could" items 10, 15(c) at results review |
| post2 | LL-11 | When a task takes a larger share of AI use on the enterprise API, does it take a smaller share on the consumer app? | brief 746cb8d (design pass done); steward FWC (recode corrected a452d01); editor LANDS/IWC; referee BLOCK aa1c9f7 → PASS WITH CHANGES 90ee9b9 (C1–C4 owed by lead). Awaits its turn at Gate 1b |
| post3 | LL-36 | When AI's coding share falls on one surface, does the coding that remains narrow? | brief 3a649a1; steward FWC; editor LANDS/IWC; referee BLOCK a30c348 (4 items) — lead design pass owed at its turn |
| post4 | LL-09 | Does AI's self-assessed success rate predict which work people keep bringing to it? | brief 0e058a1; steward FWC; editor LANDS/IWC; referee BLOCK 240fd89 (7 items incl. title and §5 wording for the human) — lead design pass owed at its turn |
| post5 | LL-18 | Where is AI doing work users could not have completed without it? | brief 9333c67 (steward amendment pass owed); steward FWC 766b789; editor LANDS/IWC; referee sweep not run — at its turn |
| post6 | LL-31 | — | awaiting batch 2 |
| post7 | LL-12 | — | awaiting batch 2 |
| post8 | LL-30 | — | awaiting batch 2 |
| post9 | LL-24 | — | awaiting batch 2 |

## Stage 3 · Write-ups

Per post: POST.md → page → referee review → pull request (Gate 3). Set review once all nine exist.

| Post | Carried forward from earlier gates |
|---|---|
| post1 | Human's Gate 1b note: the why-it-matters (§2) is to be sharpened at the write-up stage by the editor with the lead. Footnote against BRIEF §9(4): declared-H4 has 80% power only up to ≈0.32 pp; the ≈0.5 pp is step (4)'s clause (posts/post1/notes/referee-prereg.md item 3). |

## Cumulative cost log

| Session | Threads spawned | Notes |
|---|---|---|
| Dry run (2026-09-16) | 5 | one hello turn per specialist |
| 1.1 | 25 (before pause) + 20 (batch 1) + 18 (batch 2) = 63 | cap raised $250 → $280 at close; platform limit 25 live threads, idle count; batch-2 threads in flight at close |
| 1.2 | 14 (Step 0, first pass) + 6 (Step 0 re-issue after billing stop) + 4 (Steps 1–3) = 24 | billing error killed 6 threads mid Step 0; cap raised $250 → $280 → $300 at close; idle threads archived once at the platform level |
| 1.3 | 2 persistent (lead, steward) for the long-list loop + lead scoring + referee audit ×2 + editor notes ×2 + lead revisions ×2 ≈ 9 | two persistent threads with director relays; zero tree conflicts |
| 2.1 post1 Stage 2 to Gate 2a | 5 threads: lead ×1, steward ×1, analyst ×1 (two turns), referee ×1, second-read referee ×1 | zero billing stops, zero send-backs, zero tree conflicts; at Gate 2a |
| 1.4 batch 1 | ~40 threads: 5 lead briefs, 5 lead amendment/design passes, 7 steward, 1 editor, ~12 referee attempts (7 verdicts landed) | four billing stops; cap $190 → $240 → $290 → $315; scope narrowed by the human to post1 at the third stop; Gate 1b (post1) reached |
