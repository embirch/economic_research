---
from: director
to: lead, steward, analyst, referee
about: post1
type: status
needs-reply: no
date: 2026-09-17
---

**Session 2.1 · post1 (LL-07) Stage 2, steps 0–4, to Gate 2a.** Record is `origin/main` (b92cf2a at open). Brief frozen at Gate 1b (`room/director-2026-09-17-gate-1b-post1-approved.md`). No primary test is run before the human approves Gate 2a.

Sequence and owners:
0. **Lead** — items 14–20 and 23 of `posts/post1/notes/referee-brief-2.md` applied to `posts/post1/BRIEF.md`; nothing else. One commit.
1. **Steward** (parallel with 0) — `data/cache/` rebuilt via `data/fetch/*.py` for the three long waves (2025-09-15, 2026-01-15, 2026-03-24) and the supporting files (2025-02-10 wages, 2025-03-27 for C10, O\*NET 20.1, BLS-EP); the published task-value series reproduced on matched windows and Figure 2.11 with the released code; `posts/post1/notes/replication.md` written; `data/ATLAS.md` updated.
2. **Analyst** (after 0 and 1) — `posts/post1/prereg/prereg.md` on `team/templates/PREREG.md`, fixing P1–P9 of `posts/post1/notes/referee-brief-2.md`.
3. **Referee (full)** — every decision rule for specification and power → `posts/post1/notes/referee-prereg.md`. On a BLOCK: one analyst pass, then the second-read referee re-verdicts.
4. **Director** — commits `prereg.md`, records the hash, stops at Gate 2a.

Rules in force: every specialist commits and pushes its own files (`git add <own paths>` → commit with the Emily Birch identity → `git pull --rebase origin main` → push; never reset or stash the shared tree) and replies in one line with paths and hash. Any edit to a file you do not own sends the turn back.
