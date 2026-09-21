---
from: human (Emily Birch)
to: director, lead, steward, analyst, referee, editor
about: programme
type: decision
needs-reply: no
date: 2026-09-21
---

# The programme's central focus moves to gender and the economic consequences of AI

From today the programme's central question is: **how do gender differences in AI exposure, adoption and workplace conditions translate into differences in economic opportunity?** The Anthropic Economic Index remains a data source but is no longer the only one; the first post in the new series is built on Eurostat's 2025 generative-AI tables.

What stays exactly as it is: the three gates for any candidate (a real gap, data confirmed at column level, a standalone question with a why-it-matters); the stage structure (brief → pre-registration → analysis → verification → write-up); the templates; the referee's review procedure at every review point; the claims list as the boundary of the write-up; the page builder and verifier; the style corpus and the editor's two-reader standard; file ownership and the room protocol.

What changes:

- `posts/gender1/` is the first post of the new series. Its brief (`BRIEF.md`, v1.1) was reviewed by the human's assistant with the four lenses (`notes/brief-review.md`) and is approved at Gate 1b by the human. The data audit behind it is `notes/data-audit.md`.
- A new data profile, `data/releases/eurostat_isoc_ai_iaiu.md`, and fetch script, `data/fetch/eurostat_isoc_ai_iaiu.py`. The steward owns the profile from here and has one open task in it: the national sample sizes.
- The `economic-index-data` skill does not apply to this post; the empirical-standards, qc-rubric, room-protocol and anthropic-style skills do.
- The themed long-list draft (`programme/LONGLIST-2-themed-DRAFT.md`) and its themes note stand as drafts; the gender candidates in it (TL-01 to TL-03) are the reserve for later posts in this series, alongside the two further pieces in the data audit (the Spanish first-use survey; OpenAI Signals representation across topics).

Next step: the analyst writes `posts/gender1/prereg/prereg.md` from the brief, with the hypotheses, the class rule and the analysis sequence fixed; the referee reviews it (Gate 2a); the human approves; the analysis runs locally or in a direct analyst session.
