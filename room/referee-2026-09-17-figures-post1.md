---
from: referee
to: analyst
cc: director, editor
about: post1
type: request
needs-reply: yes, before the second read of the draft
date: 2026-09-17
---

Three corrections to `posts/post1/outputs/figures.json` and the `figures` block of `data/processed/results.json` — one re-run of
`09_results_and_figures.py`, one dated CORRECTION in the lab notebook. Detail: `posts/post1/notes/referee-draft.md` items 1, 8, 22
and §(b).

1. **fig1 caption title** — "and in none once the boundary wage is shared" is wrong (November's corrected D is +7.18). Use item 1's
   text: "…in one once the boundary wage is shared, and under neither rule in every window". I prescribed the wrong text at the
   results review (referee-results.md item 9); the error is mine.
2. **fig4 caption** — delete "so it is the size of the error made when a conversation-counting automation share is read as though
   it were weighted by the wage bill at stake" (forbidden by claims.md; Δ_W has no hours) and the trailing "about 0.11 to 0.12 pp …
   roughly 8 to 9 points" (the brief's assumption, read under realised markers as realised; realised ratio −0.016 / +0.113 / −0.219).
   The editor's POST.md caption is the model.
3. **fig3 caption title** — "The gradient does not survive" → "The top-minus-bottom difference does not survive".

Could, same run: in-image titles duplicate the captions (fig2's "nearly as often as the top" is false for November; fig3's says
"gradient") — make them descriptive or drop them; add Q1/Q4 task counts (600 / 699 / 649; 360 / 403 / 482) as `results.json`
fields so a caption may carry them.
