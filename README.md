# economic_research

A research team of Claude managed agents producing standalone empirical research posts built on Anthropic's Economic Index public data, each an original contribution to a thread of inquiry the economics stream at the Anthropic Institute is pursuing. Author and principal: Emily Birch.

Read in this order: `team/SETUP.md` (the operating model), `team/LESSONS.md` (what the team guards against), `.claude/skills/room-protocol/SKILL.md` (how to communicate and the file-ownership rule), then the skill for your role.

## Working criteria for "Anthropic-grade" (rewritten from the style corpus, session 1.2; grounding in `wiki/style/STYLE-GUIDE.md`)
1. Inspired by a named thread of Anthropic's inquiry, with the contribution stated as a difference rather than a characterisation: how many of the thread's units the post shares, and how its measure differs from the Anthropic measure nearest it, said before that measure is used.
2. Founded on the Economic Index releases in any of their components, with other data layered only where the question needs it and the layering justified by naming what the Index cannot see.
3. Every construct verified against Anthropic's definitions and the actual columns; where the post builds on a published number, that number reproduced before anything new; every departure from a source's parameter or threshold disclosed with its reason in the sentence that makes it.
4. An assumptions sweep before pre-registration and again before the draft, written as the questions a sceptic would ask; pre-registered hypotheses stated as a disjunction whose rules can fail, with the assumed effect, its provenance, any discount applied, and the realised effect all reported.
5. Every quantitative sentence traceable to one entry in `results.json` and quoted identically everywhere it appears (prose, caption, heading, table and close, unit and construct name included); a minimum detectable effect beside every null, stated as a scenario a reader can judge; a noise check beside every geographic or small-cell claim, with its cell count in the sentence that states its magnitude.
6. Structured and voiced as Anthropic writes: one opening move chosen from the corpus and committed to, with the stakes before the first own-number; no first person, no summary block; the question, the title and the recommendations say AI while every sample, index, number and caption says Claude; findings in pre-registration order, each stated once with its figure, the fence inside the clause that carries the number and the comparison carrying the finding.
7. The exits earn the post: caveats in their layer and signed; a ranked limitations section of which one item withdraws a claim and one names the threshold at which a conclusion flips; captions that could be lifted; a close with no numbers whose ending uses the title's key word doing work; recommendations to Anthropic naming an actor and the circumstance in which they would not work; and reproduction and assistance disclosure that say what Claude was asked to do and what was done to catch it being wrong.

Proposed by the editor in `room/editor-2026-09-16-criteria-proposal.md`; applied by the director. The operational form is `.claude/skills/anthropic-style/SKILL.md`.

## File ownership
| Owner | Writes only under |
|---|---|
| Director | `README.md`, `room/director-*.md`, `programme/CALENDAR.md`, the research-journal memory store |
| Programme lead | `wiki/reports/`, `wiki/INDEX.md`, `programme/` (LEDGER, THREADS, LONGLIST, SHORTLIST, briefs/), `posts/postN/BRIEF.md`, `room/lead-*.md` |
| Data steward | `data/`, `.claude/skills/economic-index-data/`, `posts/postN/notes/feasibility.md`, `posts/postN/notes/replication.md`, `room/steward-*.md` |
| Analyst | `posts/postN/prereg/`, `scripts/`, `data/processed/`, `outputs/`, `notes/lab-notebook.md`, `notes/ideas.md`, `room/analyst-*.md` |
| Referee and second-read referee | `posts/postN/notes/referee-*.md`, `notes/red-team.md`, `notes/claims.md`, `notes/rederivation/`, `room/referee-*.md` |
| Editor | `wiki/style/`, `.claude/skills/anthropic-style/`, `.claude/skills/page-build/`, `team/templates/POST.md`, `posts/postN/POST.md`, `notes/claims-map.json`, `site/` (incl. `site/tools/`), `room/editor-*.md` |

`reference/` is read-only material from earlier single-session work (two posts and source digests). It may be cited; nothing in it is inherited.

## Layout
`room/` conversation · `wiki/` publications and style corpora · `data/` atlas, fetch scripts, cache · `programme/` ledger, threads, long-list, short-list, briefs, calendar · `posts/` one folder per post · `site/` the public site · `team/` agents, templates, environment, driver · `.claude/skills/` procedures.
