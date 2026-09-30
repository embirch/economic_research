---
from: editor
to: human (Emily Birch)
cc: director
about: post1
type: status
needs-reply: no
date: 2026-09-18
---

# Post 1, third draft: what changed, the cold-reader test, and what a referee should check

Plan note, read first: `room/editor-2026-09-18-post1-rewrite-plan.md` (corpus files, opening move,
sources, and the two declared tool changes). Draft: `posts/post1/POST.md`. Map:
`posts/post1/notes/claims-map.json`. Page: `site/posts/post1/index.html`. Verifier output:
`posts/post1/notes/verify_page.out.txt` — **PASS**, 258 bindings, 56 quantitative sentences, 249
numbers in POST.md each checked against its own sentence's entry, 1,722 numbers on the page.

## Cold-reader test, done on the built page from the top (139 words)

A reader with no statistics would say: **the question** is whether people hand work over to AI more
on well-paid or badly-paid work, and it matters because handing over and working alongside pull a
worker's pay in opposite directions. **The finding**: the best-paid quarter of the work brought to
Claude is handed over slightly more often, in all three weeks, but the difference is all software —
take software out and the best-paid work is handed over less; and weighting the published figure by
what the work pays barely moves it. **The stakes**: which workers look most exposed, and whether the
Index's published delegation share is the right input to a model. They would also say the bottom of
this pay scale is people asking for help with their own lives, not a workforce — which is the
sentence I expect to be quoted.

### Where that reader stopped, and what was done about it

All eight were fixed before this note was written.

1. "the ordered rule … stops at its third step" — no reader knew there were steps. The table section
   now says the rule takes the rows in the order printed and stops at the first one matched, and the
   rows are in the rule's own order (so "it stopped at the third" is checkable against the table).
2. "the Kish effective number of tasks" — now introduced as "a count that discounts a list of tasks
   for being dominated by a few large ones", at first use, before the number.
3. "$43.40 … is a mass point" — now "one wage shared by many tasks".
4. "global grain" — glossed in Figure 1's caption as the world total, and named as the only grain at
   which the release crosses a task with a collaboration pattern (which is limitation 2's premise).
5. "the retained fraction is 0.50 with a contrast interval straddling zero" — now "the fraction of
   the difference that survives the restriction is 0.50, exactly the halfway line, with an interval
   that straddles it".
6. "quarter" in the prose against "quartile" in the numbered sentences — one sentence in the
   definitions now says they are the same thing. The bound sentences keep `claims.md`'s word.
7. "variance inflation factor" — kept (it is the referee's number) but the sentence now says in plain
   words what it rules out, and is no longer bolded, because it is description and not a finding.
8. Hypothesis labels (H1, O-A, H3) — gone from the body. The table's rows are plain English; the
   internal names and the order the rule reads them in are named in "What was set in advance".

## What is different from the first draft, beyond the opening

- **Bold is now one sentence per finding**, the one that carries the result, plus a term at first
  definition and the run-in labels of enumerated items. Thirteen bolded sentences were unbolded,
  including the two exploratory ones, which should never have carried emphasis.
- **Every Anthropic publication the post draws on is hyperlinked at the point of use**, eleven links,
  and where a quotation carries a page number the locator itself links the PDF. URLs are only those
  in `wiki/reports/<file>.md`.
- **Three sentences were cut or weakened because they outran the evidence**, all of them mine, none
  of them flagged by the referee: "a scenario in which the delegation share rises is … a scenario in
  which software is a larger share of the work" (an extrapolation from a cross-section to a path);
  "where it has been tested here, the answer is the second", said of the API, country and tenure
  results, which this post does not test; and "the hours a task takes are not in the released facets
  at all", which is false — human time is a published primitive, and what is true is that no count of
  hours enters this cut.
- **"Window" is "week" in the body.** Each release carries one seven-day window
  (`data/releases/release_2025_09_15.md`: "Data window 2025-08-04 to 2025-08-11 (one week)"); the
  dates are in the captions and in Methodology, and the pre-registration's word is kept there.
- **"Automation share" is "delegation share" in the body**, with the identity stated at first use and
  Anthropic's column quoted verbatim in Methodology, per the terminology standard.

## What a referee should check first

1. That every one of the twenty-two draft items from `notes/referee-draft.md` still holds. They do,
   in the new text: Figure 1's count ("in one once the boundary wage is shared"), Figure 3's title
   without "gradient", Figure 4's August hedge, three deviations, limitation 2's conditional, "twice
   the largest … twenty to thirty times the smallest", the fenced modeller sentence (now the
   "reader who takes the Index's numbers into a model" paragraph), and the C7/P6 first sentence,
   which appears in finding 1's owner paragraph and again in the close.
2. The required same-paragraph caveats for `claims.md` 1, 2, 14, 19 and 22. Sentence 1's paragraph
   carries the interval bound, the corrected quartile rule, the between-week instability, the cohort
   clause and the country-mix clause; the composition qualification (13–16) is the next section and
   is reached before any interpretation, with caution (iii) pointing at it by name.
3. The close: no number the body has not carried, and none beyond what `claims.md` licenses there —
   "less than a point", "clearing a point" and "fourteen to twenty", all in words. The size range
   ("two thirds of a point to more than seven") was in my first close and is now out of it; it sits
   in finding 1 and limitation 3, where it belongs.
4. Two changes to my own tools, both declared in the plan note: `verify_page.py` gains an `EXCLUDE`
   pattern for URLs (a link target's digits are not claims) and one for `Table \d+` locators, and its
   sentence splitter now breaks a sentence that ends inside emphasis ("…0.7 points.** The intervals
   …"), which makes check 3 strictly stronger — bindings are now per half-sentence where they used to
   be per merged pair. Sentence count rose from 45 to 56 for that reason, not because claims were
   added.

## Still open, and not mine to close

- `outputs/figures.json` and `results.json`'s `figures.fig4.caption` still assert a direction for
  August, where the interval contains zero (the referee's non-blocking recommendation on the second
  read). POST.md and the page carry the hedge. The fix is one string in the analyst's script 09.
  Named again in `notes/pr-description.md` so the next reader meets it as a known gap, not a
  discrepancy.
- The in-image titles are the analyst's regenerated ones and are unchanged by this pass.
