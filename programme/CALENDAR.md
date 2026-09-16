# Programme calendar

Owner: director. Sequencing only; no dates promised. Status is updated at the close of each session.

## Stage 1 · Research briefs

| Session | Scope | Status |
|---|---|---|
| 1.1 Corpus and atlas | `wiki/INDEX.md`, `wiki/reports/*.md` (lead); `wiki/style/*.md` (editor); `data/releases/*.md`, `data/fetch/*.py`, `data/ATLAS.md` (steward). Human reads two wiki entries and one release file for accuracy before 1.2. | closed 2026-09-16; 35/38 wiki, 13/23 style, atlas complete; remainder listed in room/director-2026-09-16-session-1-1-status.md |
| 1.2 Ledger, threads map, criteria | `programme/LEDGER.md`, `programme/THREADS.md` (lead); README criteria and `anthropic-style` skill rewritten from the style corpus (editor); referee samples ten wiki claims and the ledger. Human weights or excludes threads. | closed 2026-09-16; LEDGER.md (1,063 items), THREADS.md (11 threads), STYLE-GUIDE.md, anthropic-style skill, README criteria; referee PASS WITH CORRECTIONS (lead applies at the open of 1.3); human reads THREADS.md before 1.3; see room/director-2026-09-16-session-1-2-status.md |
| 1.3 Long-list and short-list | `programme/LONGLIST.md` with a steward feasibility line per item; `programme/SHORTLIST.md`; referee audits scoring; editor answers each why-it-matters. **Gate 1a**: human chooses. | closed 2026-09-16; LONGLIST 39 survivors with steward lines; SHORTLIST nine (b7a44ca); referee audits 0c77fbf, c168b19; editor notes ×9. **Gate 1a decision: all nine proceed in rank order; scenarios thread excluded; programme is nine posts.** See room/director-2026-09-16-gate-1a.md |
| 1.4 Briefs, batch 1 | `posts/post{1..5}/BRIEF.md` (lead); `posts/post{1..5}/notes/feasibility.md` (steward); editor framing note per brief; referee sweep per brief. **Gate 1b (batch 1)**: human approves posts 1–5. | HALTED 2026-09-16 on API usage limit (returns 2026-10-01). Five briefs, five steward notes (all FEASIBLE WITH CAVEAT), five editor notes committed; referee post2 BLOCK committed; referee post1/3/4/5 and the post2/post5 lead passes died uncommitted. Resume checklist: room/director-2026-09-16-session-1-4-halt.md |
| 1.4 Briefs, batch 2 | `posts/post{6..9}/BRIEF.md` and the same loop. **Gate 1b (batch 2)**: human approves posts 6–9. | not started; do not begin until the human says so |

## Stage 2 · Doing the research (one session per post)

Order set at Gate 1a. Per post: replicate → pre-registration (Gate 2a) → analysis → verification (Gate 2b) → close.

| Post | Candidate | Title (frozen at Gate 1b) | Status |
|---|---|---|---|
| post1 | LL-07 | Is AI delegated more on cheap work or on expensive work? (frozen at 1b) | brief 960080c; steward FWC; editor LANDS/IWC; referee sweep pending |
| post2 | LL-11 | When a task takes a larger share of AI use on the enterprise API, does it take a smaller share on the consumer app? | brief 31e5297; steward FWC; editor LANDS/IWC; referee BLOCK aa1c9f7 — one design pass owed |
| post3 | LL-36 | When AI's coding share falls on one surface, does the coding that remains narrow? | brief 3a649a1; steward FWC; editor LANDS/IWC; referee sweep pending |
| post4 | LL-09 | Does AI's self-assessed success rate predict which work people keep bringing to it? | brief 0e058a1; steward FWC; editor LANDS/IWC; referee sweep pending |
| post5 | LL-18 | Where is AI doing work users could not have completed without it? | brief 9333c67 (steward amendment pass owed); steward FWC; editor LANDS/IWC; referee sweep pending |
| post6 | LL-31 | — | awaiting batch 2 |
| post7 | LL-12 | — | awaiting batch 2 |
| post8 | LL-30 | — | awaiting batch 2 |
| post9 | LL-24 | — | awaiting batch 2 |

## Stage 3 · Write-ups

Per post: POST.md → page → referee review → pull request (Gate 3). Set review once all nine exist.

## Cumulative cost log

| Session | Threads spawned | Notes |
|---|---|---|
| Dry run (2026-09-16) | 5 | one hello turn per specialist |
| 1.1 | 25 (before pause) + 20 (batch 1) + 18 (batch 2) = 63 | cap raised $250 → $280 at close; platform limit 25 live threads, idle count; batch-2 threads in flight at close |
| 1.2 | 14 (Step 0, first pass) + 6 (Step 0 re-issue after billing stop) + 4 (Steps 1–3) = 24 | billing error killed 6 threads mid Step 0; cap raised $250 → $280 → $300 at close; idle threads archived once at the platform level |
| 1.3 | 2 persistent (lead, steward) for the long-list loop + lead scoring + referee audit ×2 + editor notes ×2 + lead revisions ×2 ≈ 9 | two persistent threads with director relays; zero tree conflicts |
| 1.4 batch 1 | 5 lead + 5 steward + 1 editor + 4 referee = 15 (lead amendment passes reused the lead threads) | cap $190 for batch 1; halted on API usage limit with 6 threads mid-turn (3 referee, 2 lead, 1 steward); referee post5 not yet spawned |
