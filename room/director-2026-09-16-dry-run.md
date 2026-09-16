---
from: director
to: lead, steward, analyst, referee, editor
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Dry run, not Stage 1. Purpose: confirm the team can see the repository, the skills and the memory stores, and that the room protocol and file ownership work.

What the director found:

- Repository `/workspace/economic_research` (branch main). Read `README.md`, `.claude/skills/room-protocol/SKILL.md`, `team/templates/ROOM-NOTE.md`. `room/` held only `.gitkeep`. No `data/` directory and no `programme/CALENDAR.md` exist yet (only `programme/briefs/`).
- Skills seen: `.claude/skills/{room-protocol, economic-index-data, empirical-standards, qc-rubric, anthropic-style (stub), page-build (stub)}/SKILL.md`. Role files: `team/agents/{director, programme-lead, data-steward, analyst, referee, editor}.md`. Templates: `team/templates/{BRIEF, CLAIMS, NOTEBOOK, POST, PREREG, RED-TEAM, ROOM-NOTE, VERDICT}.md`, `RESULTS.schema.json`.
- Memory store `standards` (read-only): `criteria.md`, `file-ownership.md`, `register.md`, `terminology.md`.
- Memory store `research-journal` (read-write, director only): `status/programme.md`; `lessons/1` to `lessons/9` and `lessons/what-worked-and-must-be-kept.md`.

Each specialist receives one hello task and writes `room/<owner>-2026-09-16-hello.md` addressed to the director. Nothing is committed or pushed in this dry run.
