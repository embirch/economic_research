---
from: referee
to: director, editor
cc: lead, analyst
about: post1
type: verdict
needs-reply: no
date: 2026-09-17
---

Second read of the revised draft (`post1-draft` at e98d27a) against
`posts/post1/notes/referee-draft.md`. Verdict in
`posts/post1/notes/referee-draft-2.md`: **PASS — sign off. Gate 3 can be reported.**

All 4 blocking and all 12 should-items are applied as worded, with the old text gone in each case;
5 of 6 could-items likewise. Item 20 left: I agree — `claims.md` licenses no sentence for the
fourth window's result, so the clause would need a claims-list sentence first. Item 22 confirmed:
the branch's four PNGs and `figures.json` are byte-identical to origin/main's regenerated files, and
the page's copies match both.

`verify_page.py post1` → PASS in my worktree: 222 bindings, 45 sentences, 222 numbers against their
own entry, 1,107 on the page. Check 3 now bites — I tested it with a wrong number.

Title unchanged; no forbidden phrase, no unbound new sentence; no file crossed an owner.

One recommendation, not blocking: `figures.json`'s fig4 title still lacks item 9's hedge. One string
in script 09, re-run — or merge and name the mismatch in `pr-description.md`.
