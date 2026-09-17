---
from: lead
to: director, steward, editor, referee
about: post1
type: status
needs-reply: yes; steward before the feasibility note, referee before Gate 1b
date: 2026-09-16
---

Produced `posts/post1/BRIEF.md` (LL-07), twelve sections on `team/templates/BRIEF.md`.

**Title, frozen:** "Is AI delegated more on cheap work or on expensive work?" The editor's note
raised no title-form defect; settled unchanged, with a wording rule in §7(1) — the body says "the
wage of the work" and never grades a direction.

**Steward, please confirm or contradict C1–C8 in `posts/post1/notes/feasibility.md`:** the three
global `onet_task::collaboration` frames with `_pct` and `_count`; the same-wave `onet_task_pct`
weights; the one-node gap between 2,617/3,169/3,259 intersection nodes and 2,616/3,168/3,258 named
nodes; the C5 task-text join de-duplicated for case variants; `wage_data.csv` at `MedianSalary > 100`
and the BLS-EP second source with its lower coverage; the Seychelles netting for November.

**Departures.** Two, both stated in the brief, not cited. Anthropic's $49.3 → $47.9 is recorded as a
known non-reproduction, so the design is rank-based on usage-weighted wage quartiles rather than on
dollar levels. The multi-holder primary rule is employment-weighted, as nearest to footnote 5 p. 11;
the ≤0.17 pp bound is on an occupational share, not on this gradient, and is reported as context.

**Amendment pass (steward's note, `posts/post1/notes/feasibility.md`).** All four corrections applied
in §8: C6's key is the full 10-character O\*NET-SOC code (970 of 974; `[:7]` withdrawn), C8 is `SC`
and nets weights only with a pre-registered drop of the tasks it dominates, C4 states the two frames'
different residuals, and §8(ii)'s tolerance is now "within 0.36 pp, positive in all three waves".
§9(4) names the conversation-level variance model (MDE 0.42–0.43 pp) and resets the equivalence
margin from ±3 pp to **±1 pp**, carried into H4 and §12. §8 also now states the O\*NET-SOC vintage
rule — wage on the shipped 2010 codes, occupational groupings on the 2019 recode — which post3 and
post8 cite. §9(3)(b) restated to the 7 / 8 / 6 groups that span the quartiles; question, title,
contribution and hypotheses unchanged. Brief at 398 lines.

---

**2026-09-17 · design pass on the referee's BLOCK** (`posts/post1/notes/referee-brief.md`, e2affe4), items 1–12, rewritten
from the record. **New title (human's decision, option A): "Is AI delegated more on low-wage work or on high-wage work?"**;
body rule "the wage of the work". Item 1: one size criterion — a pre-registered smallest effect of interest δ = 1 pp — and
an ordered five-step rule in §9(1) partitioning the outcomes between H1, H2, O-A (persistent gradient below the margin),
H4 and O-B (no persistent gradient), each with a §12 ending; H3 re-keyed to the fraction of D retained; the permutation
null demoted to a §10 task-level bound. Item 2: use case named as the most direct composition rival, with a confirmatory
work-mix leg and a work-dominant re-estimate (C9, Nov/Feb only). Items 4–12 applied, including the allocation statement
and the matched-window non-reproduction. Nothing declined. **Steward: please confirm C9 and C10 at column level before the
pre-registration.** 414 lines.
