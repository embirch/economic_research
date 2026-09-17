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

**PASS.** 216 claims-map bindings resolved against `results.json`; 44 quantitative sentences in
POST.md checked, all mapped; 215 numbers in POST.md and 1,099 numbers in the built page's prose,
captions, contents rail and generated tables checked, all bound. Output kept at
`posts/post1/notes/verify_page.out.txt`. The build fails on any number that is not in
`results.json`; the rule is fix the text, never the numbers.

## What a reviewer should check first

1. That every quantitative sentence is a permitted sentence in `notes/claims.md`, or is bound to a
   `results.json` key it names, and that nothing on the forbidden list appears anywhere — including
   the captions, the headings and the close.
2. That the required caveats sit in the same paragraph as their finding: the corrected quartile
   rule and the between-window dispersion beside D; the country-mix sentence; the residual
   composition beside leg (a); "an hourly rate, not a bill" beside Δ_W.
3. That the close carries no number the body has not carried, and that the generalisation bound is
   the realised fourteen to twenty points and never "twelve".
