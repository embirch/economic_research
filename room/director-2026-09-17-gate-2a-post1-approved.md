---
from: director
to: analyst, referee, steward, lead, editor
about: post1
type: status
needs-reply: no
date: 2026-09-17
---

**GATE 2a (post1 · LL-07) — APPROVED by the human.** The analysis runs exactly as pre-registered at `066b761` (`posts/post1/prereg/prereg.md`, content `c9b1b45`). No rule, threshold, sample rule or exploratory test moves; any departure is a dated deviation in `posts/post1/notes/lab-notebook.md` reporting both the pre-registered rule and the corrected one.

Sequence:
5. **Analyst** — the 17 confirmatory estimates in numbered Python scripts under `posts/post1/scripts/`, each ending in a passing check block; two independent implementations of every headline number; the synthetic recovery test; interval and MDE beside every coefficient; the noise checks the prereg lists; then the three exploratory tests the brief §9 names and nothing more. Writes `posts/post1/data/processed/results.json` on `team/templates/RESULTS.schema.json`, `posts/post1/outputs/figures.json` with captions and the figures, and the lab notebook. Commits as it goes.
6. **Referee (full)** — re-derives three headline numbers from the raw files with its own code (`posts/post1/notes/rederivation/`); judges every logged deviation; counts tests run against tests registered; writes `posts/post1/notes/red-team.md` and `posts/post1/notes/claims.md` (sentences the post may and may not state, each bound to a results.json key; the strongest title and opening claim the evidence supports).
7. **Director** — status note, journal, push; STOP at Gate 2b.

No prose, no POST.md and no editor work before the human has read results.json and the claims list.
