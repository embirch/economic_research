# economic_research

A research team of Claude managed agents producing standalone empirical research posts built on Anthropic's Economic Index public data, each an original contribution to a thread of inquiry the economics stream at the Anthropic Institute is pursuing. Author and principal: Emily Birch.

Read in this order: `team/SETUP.md` (the operating model), `team/LESSONS.md` (what the team guards against), `.claude/skills/room-protocol/SKILL.md` (how to communicate and the file-ownership rule), then the skill for your role.

## Working criteria for "Anthropic-grade" (to be rewritten from the style corpus in Stage 1)
1. Inspired by a named thread of Anthropic's inquiry; states plainly what it adds and where it overlaps.
2. Founded on the Economic Index releases in any of their components; other data layered where the question needs it, and the layering justified.
3. Every construct verified against Anthropic's definitions and the actual columns; where the post builds on a published number, that number reproduced first.
4. Assumptions sweep before pre-registration and again before the draft.
5. Pre-registered hypotheses with rules that can fail and whose power is stated; deviations logged.
6. Every claim traceable to a number in results.json; MDE beside every null; noise checks for geographic or small-cell claims.
7. Written as Anthropic writes: why it matters first, findings as plain sentences with their caveats, comparison as the finding, limitations a referee would raise first, a close about what was learned.

## File ownership
| Owner | Writes only under |
|---|---|
| Director | `README.md`, `room/director-*.md`, `programme/CALENDAR.md`, the research-journal memory store |
| Programme lead | `wiki/reports/`, `wiki/INDEX.md`, `programme/` (LEDGER, THREADS, LONGLIST, SHORTLIST, briefs/), `posts/postN/BRIEF.md`, `room/lead-*.md` |
| Data steward | `data/`, `.claude/skills/economic-index-data/`, `posts/postN/notes/feasibility.md`, `posts/postN/notes/replication.md`, `room/steward-*.md` |
| Analyst | `posts/postN/prereg/`, `scripts/`, `data/processed/`, `outputs/`, `notes/lab-notebook.md`, `notes/ideas.md`, `room/analyst-*.md` |
| Referee | `posts/postN/notes/referee-*.md`, `notes/red-team.md`, `notes/claims.md`, `notes/rederivation/`, `room/referee-*.md` |
| Editor | `wiki/style/`, `.claude/skills/anthropic-style/`, `.claude/skills/page-build/`, `posts/postN/POST.md`, `notes/claims-map.json`, `site/` (incl. `site/tools/`), `room/editor-*.md` |

`reference/` is read-only material from earlier single-session work (two posts and source digests). It may be cited; nothing in it is inherited.

## Layout
`room/` conversation · `wiki/` publications and style corpora · `data/` atlas, fetch scripts, cache · `programme/` ledger, threads, long-list, short-list, briefs, calendar · `posts/` one folder per post · `site/` the public site · `team/` agents, templates, environment, driver · `.claude/skills/` procedures.
