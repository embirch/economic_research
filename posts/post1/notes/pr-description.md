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
| Editor's revision pass — all 4 blocking and all 12 should items applied; 4 of 6 could items applied | this branch | see below |

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

**PASS.** 222 claims-map bindings resolved against `results.json`; 45 quantitative sentences in
POST.md checked, all mapped; 222 numbers in POST.md checked **against their own sentence's
bindings**, and 1,107 numbers in the built page's prose, captions, contents rail and generated
tables checked against the whole of `results.json`. Output kept at
`posts/post1/notes/verify_page.out.txt`. The build fails on any number that is not in
`results.json`; the rule is fix the text, never the numbers.

The per-sentence check is new in this pass: the referee's draft review showed that matching a
number against a global index of a 187 KB `results.json` is necessary and not sufficient, since
small integers pass regardless of what they mean. `verify_page.py` check 3 now resolves each
sentence's own bindings and accepts only roundings of those. It found exactly the three numbers
the referee's audit found by hand — `23`, `100` and `$10` — each of which is a true number that
was passing by coincidence; all three are now bound to the field that carries them
(`facts.november_is_corroborated_not_independent.source_check`, the X3 test's `label`, the slope's
`unit`), and the one laundered binding (draft item 14) is gone, the placebo band being written in
words.

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

## Length, declared

6,001 words excluding captions (7,035 with). The post proper — the puzzle through "What this
means" — is about 3,300 words; the rest is the template's own additions, which the corpus exports
to appendices and the working criteria require as sections a referee can test. Inside the post
proper the excess over a special report is the caveats `claims.md` makes mandatory in the same
paragraph as each finding. This is the cost of the caveat rule, not an oversight; the referee's
draft review found no section to cut.

## What a reviewer should check first

1. That every quantitative sentence is a permitted sentence in `notes/claims.md`, or is bound to a
   `results.json` key it names, and that nothing on the forbidden list appears anywhere — including
   the captions, the headings and the close.
2. That the required caveats sit in the same paragraph as their finding: the corrected quartile
   rule and the between-window dispersion beside D; the country-mix sentence; the residual
   composition beside leg (a); "an hourly rate, not a bill" beside Δ_W.
3. That the close carries no number the body has not carried, and that the generalisation bound is
   the realised fourteen to twenty points and never "twelve".
