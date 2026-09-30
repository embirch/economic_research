# Pull request · post1 (LL-07)

**Title:** Is AI delegated more on low-wage work or on high-wage work?

**Branch:** `post1-draft` → `main`. Opened and merged by the human; that is Gate 3.

## What this adds

The first cross in the corpus of Anthropic's collaboration facet with the wage of the work, at task
grain, usage-weighted, in three Claude.ai windows. Declared outcome on the pre-registered rule:
**O-A** — a persistent sign, not shown to clear the one-point margin in every window. **H3
declared** on legs (a) and (b), each firing in every wave: the excess is carried by Computer &
Mathematical tasks. H1's signature clause fails. The write-up is bounded by
`posts/post1/notes/claims.md`, which the human approved at Gate 2b as the boundary of what the post
may say.

## Gates passed, with commits

| Gate / step | Record | Commit |
|---|---|---|
| Gate 1b — brief approved by the human | brief design pass on the referee's BLOCK; re-verdict PASS WITH CHANGES | `9af7bad` / `b4ad871` |
| Brief items 14–20, 23 applied | `posts/post1/BRIEF.md` (question, title, contribution frozen) | `8fbffbd` |
| Replication re-checked against the brief pass | `posts/post1/notes/replication.md` — 75 cached files, all checksums OK; Fig 2.11 and the matched-window task values reproduce | `e9a2291` |
| Pre-registration committed before any primary test | `posts/post1/prereg/prereg.md` (content `c9b1b45`; referee PASS WITH CHANGES `37868c3`; second-read sign-off `0a6513f`) | `066b761` |
| Gate 2a — pre-registration approved by the human | `room/director-2026-09-17-gate-2a-post1-approved.md` | — |
| Analysis: 17 confirmatory + 3 exploratory, 24 robustness, 16 descriptive, 4 deviations | scripts 01–09, `data/processed/results.json` | `660dad5` |
| Referee verification of results — PASS WITH CHANGES, 0 blocking; three headline numbers re-derived from raw to ≤ 3 × 10⁻¹⁴ pp | `notes/referee-results.md`, `notes/rederivation/` | `1b621c0` |
| Analyst revision, 14 items applied | seeded placebo made reproducible; captions corrected | `698a2f1` |
| Referee second read — SIGN OFF | `notes/referee-results-2.md` | `09f05ab` |
| Claims list finalised (the boundary) | `notes/claims.md`, `notes/red-team.md` | `3556471` |
| Gate 2b — results approved by the human | `room/director-2026-09-17-gate-2b-post1-approved.md` | `cfe0064` |
| Lead's sharpened why-it-matters and close | `room/lead-2026-09-17-why-it-matters-post1.md` | `31898a5` |
| Referee verification of the draft — PASS WITH CHANGES, 4 blocking, 12 should, 6 could; all 44 mapped sentences audited against their own bindings | `notes/referee-draft.md` | `67f1d66` |
| Analyst's caption fix on main (draft items 1, 8, 22): `figures.json`, the `figures` block of `results.json`, new `facts.quartile_task_counts`, regenerated PNGs with descriptive in-image titles | `outputs/figures.json`, `data/processed/results.json` | `283f346` |
| Editor's revision pass — all 4 blocking and all 12 should items applied; 4 of 6 could items applied | this branch | `e98d27a` |
| Referee second read of the draft — **SIGN OFF**, one non-blocking recommendation on `figures.json` | `notes/referee-draft-2.md` | — |
| Gate 3 — **sent back by the human**: accurate and bound, but not readable cold and not written from the style corpus; second draft supplied as a starting point | `room/human-2026-09-18-post1-rewrite-brief.md`, `notes/human-draft-v2.md` | `0ea4690` |
| Editor's third draft — rewritten opening, plain-English hypothesis table, hyperlinked sources, bold reserved for findings, cold-reader test applied | `room/editor-2026-09-18-post1-rewrite-plan.md`, `room/editor-2026-09-18-post1-draft-3.md` | this branch |

## Files in this pull request

| File | Owner | What it is |
|---|---|---|
| `posts/post1/POST.md` | editor | the write-up, on `team/templates/POST.md`'s twelve sections |
| `posts/post1/notes/claims-map.json` | editor | every quantitative sentence → its `claims.md` id and its `results.json` key(s) and value(s) |
| `posts/post1/notes/verify_page.out.txt` | editor | the verifier's output on this commit |
| `posts/post1/notes/pr-description.md` | editor | this file |
| `site/tools/build_page.py` | editor | shared page builder: figures, evidence drawers, contents rail |
| `site/tools/verify_page.py` | editor | shared verifier: every number on the page against `results.json` |
| `site/tools/make_claims_map.py` | editor | generates post1's claims map from POST.md |
| `room/editor-2026-09-17-post1-draft-revised.md` | editor | the revision note: the 22 items, applied or left |
| `room/editor-2026-09-18-post1-rewrite-plan.md` | editor | the third draft's plan: opening move, the three corpus files, what was kept from each earlier draft, the sources linked |
| `room/editor-2026-09-18-post1-draft-3.md` | editor | the third draft's status note: the cold-reader test and its eight fixes, the three sentences withdrawn, what a referee should check |
| `site/posts/post1/index.html` | editor | the built page (replaces the earlier programme's page at this path) |
| `site/posts/post1/figures/*.png` | editor | the four figures, copied from `outputs/figures/` |
| `site/index.html` | editor | the post1 card retitled to this post |
| `.claude/skills/page-build/SKILL.md` | editor | rewritten from stub to the real procedure |
| `room/editor-2026-09-17-post1-draft.md` | editor | the editor's status note |

Nothing outside the editor's paths is touched. `results.json`, the scripts, the figures, the brief,
the pre-registration, `claims.md` and `red-team.md` are unchanged in this branch.

## Verifier

```
python3 site/tools/build_page.py post1
python3 site/tools/verify_page.py post1
```

**PASS.** 258 claims-map bindings resolved against `results.json`; 56 quantitative sentences in
POST.md checked, all mapped; 249 numbers in POST.md checked **against their own sentence's
bindings**, and 1,722 numbers in the built page's prose, captions, contents rail and generated
tables checked against the whole of `results.json`. Output kept at
`posts/post1/notes/verify_page.out.txt`. The build fails on any number that is not in
`results.json`; the rule is fix the text, never the numbers.

The per-sentence check (check 3) was added in the previous pass, after the referee's draft review
showed that matching a number against a global index of a 187 KB `results.json` is necessary and not
sufficient: small integers pass regardless of what they mean. Three changes to `verify_page.py` in
this pass, all declared in `room/editor-2026-09-18-post1-rewrite-plan.md`:

1. `EXCLUDE` gains `https?://\S+` — "URL in a hyperlink target or citation". This draft hyperlinks
   every Anthropic source at the point of use, and a link target's digits are not claims
   (`…a64d376.pdf` would otherwise be read as the number 376). The pattern matches only inside a
   link target and excludes no finding.
2. `EXCLUDE` gains `Table \d+` — a table locator in a citation, the same class as `Figure \d+`.
3. The sentence splitter now breaks a sentence that ends inside emphasis ("…0.7 points.** The
   intervals …"), which it previously merged with the next. Check 3 is strictly stronger for it:
   bindings that used to be pooled across a bolded finding and the caveat sentence after it are now
   resolved separately. This is why the sentence count rises from 45 to 56 and the binding count
   from 222 to 258; no claim was added.

## Revision after the referee's draft review

All **4 blocking** items applied (Figure 1's caption count; the opening's "establishes the sign";
the close's superlative and its missing attribution; the new construct in the close). All **12
should** items applied (Anthropic's bounding results carried into the opening and finding 2; the
modeller sentence fenced; three deviations, not four, with the disclosure of what had been seen;
Figure 3's "gradient"; Figure 4's August direction; "the correction exists"; "shows"; "an order of
magnitude"; limitation 2's conjecture; the claims-map binding; "higher than"; the caption count in
the assistance disclosure). **4 of 6 could** items applied (17, 18, 19, 21). Left: **20**, the
fourth window's result, which would be a new claim rather than wording; and **22**, the in-image
titles, which are the analyst's file and were applied by the analyst at `283f346`. Figure captions
bind to the analyst's corrected `figures.json`, except Figure 4's title, where draft item 9
prescribes text `figures.json` does not yet carry.

## The third draft, against the Gate 3 send-back

The send-back asked for six things. Where each is discharged:

1. **Why delegation against collaboration matters.** The opening's third, fourth and fifth
   paragraphs: Autor's distinction in Anthropic's own words; the delegation share as the closest
   signal the Index has of which is happening; the fork Anthropic states and leaves open
   (capability expansion and displacement risk against learning-by-doing and gains to adaptable
   workers); and the same number as a parameter in the observed-exposure measure and in the
   economic-scenario model, each quoted and linked.
2. **What is known and not known.** The opening's sixth paragraph enumerates who delegates more —
   the API, lower-usage countries, newer users, and the education null — each with its report, its
   page and its link; the seventh gives what is published about the price of the work; the eighth
   is the worked case where the missing cross decides the answer.
3. **Both stakes, raised and answered in order.** The stakes are enumerated (jobs, then
   measurement) before any number; each finding section ends on the one it bears on; "What this
   means" answers them in the same order under two bold run-ins.
4. **Recommendations that explain why.** Three, each an imperative to a named actor, then what it
   would look like, then the evidence with its number, then why it matters at the scale of the
   economy, then the circumstance in which it would not work. "Whoever maintains the
   observed-exposure measure should…" is gone.
5. **Language.** One bolded sentence per finding; hypothesis labels and unexplained field names out
   of the body; every term defined by a case before the abstraction; the eight cold-reader stops
   listed in `room/editor-2026-09-18-post1-draft-3.md` fixed.
6. **Referencing.** Eleven hyperlinks, all from `wiki/reports/<file>.md`, at the point of use, with
   the PDF linked from the page locator wherever a quotation carries a page.

Three sentences of the first draft were withdrawn as overreach that no review had caught: an
extrapolation from a cross-section to a scenario path, a claim that the API, country and tenure
results had been tested here, and a false statement that no hours are in the released facets.

## Length, declared

8,657 words excluding captions (9,814 with). The post proper — the opening through "What this
means" — is about 5,580 words, against about 3,300 in the first draft; the remaining 3,080 are the
template's own sections, which the corpus exports to appendices and the working criteria require as
sections a referee can test.

The growth is in the opening, which runs 1,530 words and carries no number of this post's own. Each
of its paragraphs discharges a numbered requirement of the send-back: the two kinds of conversation
as cases; the published split and how it moved; why the split matters, in Anthropic's words; the
fork left open; the two models in which the number is already a parameter; who delegates more, in
four linked findings; what is published about the price of the work; the worked case; the question;
the two stakes; the three findings without numbers; the two limits a reader thinks of first. Nothing
in it can be deleted without losing a fact the send-back asked for. Inside the finding sections the
excess over a corpus special report is still the caveats `claims.md` makes mandatory in the same
paragraph as each finding, plus the four side-estimates the claims list permits only beside the
primary they qualify (the within-coding contrast, the residual composition, the work-share
regression, and the two exploratory probes).

## What a reviewer should check first

1. That every quantitative sentence is a permitted sentence in `notes/claims.md`, or is bound to a
   `results.json` key it names, and that nothing on the forbidden list appears anywhere — including
   the captions, the headings and the close.
2. That the required caveats sit in the same paragraph as their finding: the corrected quartile
   rule and the between-window dispersion beside D; the country-mix sentence; the residual
   composition beside leg (a); "an hourly rate, not a bill" beside Δ_W.
3. That the close carries no number the body has not carried, and that the generalisation bound is
   the realised fourteen to twenty points and never "twelve". The size range "two thirds of a point
   to more than seven" was in the first draft's close and is now out of it, in finding 1 and
   limitation 3 only.
4. That the twenty-two items of `notes/referee-draft.md` still hold in rewritten prose; the
   item-by-item check is in `room/editor-2026-09-18-post1-draft-3.md`.

**Known gap, carried forward and not blocking.** `outputs/figures.json` and `results.json`'s
`figures.fig4.caption` still end "…and **not** in the same direction as the quartile gap in **two of
the three**", while POST.md and the page carry the referee's hedged title ("in only one of the three,
August's interval containing zero"). The record therefore still asserts a direction for a window
whose interval contains zero. The fix is one string in the analyst's `scripts/09_results_and_figures.py`
and a re-run; it is the analyst's file, and the referee's second read recommended it without
blocking (`notes/referee-draft-2.md`, "The Figure 4 departure").
