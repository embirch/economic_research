# Referee verdict · post1 (LL-07) · draft, second read · 2026-09-17

Read, and nothing else: `posts/post1/notes/referee-draft.md` (the prior verdict, origin/main 67f1d66),
`posts/post1/POST.md` and `notes/claims-map.json` on branch `post1-draft` at e98d27a (worktree `/tmp/draft2`),
the diff `c148bbe..e98d27a`, `room/editor-2026-09-17-post1-draft-revised.md`,
`room/analyst-2026-09-17-figures-post1-answer.md`, and — only where the revision needed it — `notes/claims.md`'s
"Sentences the post may not state", `outputs/figures.json`, `results.json`'s `figures` block and the `DeltaW_*`
intervals, the four PNGs' checksums and `site/posts/post1/index.html`. By scope: no Anthropic source re-read, no
number re-derived, no statistic recomputed. Only two numbers were looked at again because the revision changed the
sentences that carry them (item 12's arithmetic and item 9's August interval), and only those.

## Verdict

**PASS — sign off.** All four blocking items are applied as worded; all twelve should-items and five of the six
could-items are applied as worded or in a form that preserves the claim boundary; in each case the old text is gone.
The two left items are acceptable: item 20 is a could-item whose text would state a result `claims.md` does not
license, and item 22 was done on main at 283f346 — the branch's four PNGs are byte-for-byte the regenerated ones.
The revision breaks nothing: the title is unchanged, the diff introduces no sentence that is not bound in
`claims-map.json` or licensed by `claims.md`, no forbidden phrase enters, and the verifier passes with a check 3
that is strictly stronger than the one it replaced. One non-blocking recommendation stands, on `figures.json`
(below, "The Figure 4 departure").

**Verifier, my run in the branch worktree:** `python3 site/tools/verify_page.py post1` → **PASS**, exit 0; 222
bindings resolved, 45 quantitative sentences mapped, 222 numbers in POST.md checked *against their own sentence's
entry*, 1,107 numbers in the built page's prose checked. The counts match the editor's note exactly. The editor has
built my §Method audit into check 3: a number now passes only as a rounding (0–4 decimals) of a value the map binds
*that sentence* to, or of a number inside a bound string, or as a declared `as_printed`; the old global index over
`results.json` is demoted to check 4, which is now used only for the built page, where the generated tables print
`results.json` entries verbatim and the global check is the right one. I tested that the new check bites: changing
"by 1.4 points (4–11 August 2025)" to "1.9" in my own worktree copy produced `FAIL — 5 problem(s)`, including
`[number not bound to this sentence] 1.9`; the worktree was restored. One new `EXCLUDE` pattern was added,
`\bLimitations?,?\s+\d+`, for item 17(c)'s cross-reference; it is a locator in the same class as `Figure \d+` and
excludes no finding.

## Item by item

**1 · Figure 1's count — applied as worded.** "…the difference clears a percentage point in two windows on the
pre-registered quartile rule **and in one once the boundary wage is shared, and under neither rule in every
window.**" The "in none" text is gone from POST.md, and `figures.json`/`results.json` carry the same sentence
(analyst, 283f346). The error that sat in three files is out of all three.

**2 · The opening's sign — applied as worded.** "This post measures that error in three windows and finds it small
and of no fixed sign — and then finds that its size and its sign are not the interesting part." "This post
establishes the sign" is gone.

**3 · The close's superlative — applied as worded, both halves.** Close: "coding, which is most of the best-paid
quarter of the work in this data and the work Anthropic's own gloss of automative use names." Body (finding 2,
first sentence): "…the coding family is most of the best-paid quarter of the work in this data and is the work
Anthropic's own gloss of automative use names — 'asking the model to directly complete a task or debug errors'
(Economic Index report, March 2025)." "the best-paid work in this data and the most fully handed over" appears
nowhere. The attribution is now in both places, and the close no longer says more than the body.

**4 · The new construct in the close — applied: the sentence is deleted.** "the coding family's own internal
contrast" does not occur in POST.md. The paragraph now ends on the three nameable things that would move the
reading, and "the price reading none" is gone with it.

**5 · Anthropic's bounding results — applied as worded, both sentences.** Opening: "It has been crossed with how
much back-and-forth the work took — in conversations mapped to higher-wage occupations users take more turns, a
pattern the June 2026 report reads, conditionally, as looking 'more labor-augmenting than labor-displacing' — but
not with the collaboration facet itself, the measure that defines delegation." Finding 2's exploratory paragraph
now closes: "Both the reversal outside coding and the lower `directive` share at the top are consistent with that
turns reading — consistent with, not confirmation of it — and the U-shape of Figure 2 echoes the one published
cross of the collaboration facet with occupational category, which was not monotone in wage either." "It has not
been crossed with how the work was done" is gone. No number entered (no "1.53"), so the verifier is untroubled and
the red-team's "consistent with, never confirmation" fence is in the sentence itself.

**6 · The modeller's fence — applied as worded.** "For a modeller reading these windows, the quantity to condition
on is the coding share of the task mix rather than its pay." The unfenced form is gone.

**7 · The deviation count and the disclosure — applied as worded, (a) and (b).** (a) "Three deviations were logged,
each with the registered rule and the corrected rule both run and both reported," and the tie-order bullet is
folded into the first: "…the registered rule was made reproducible by fixing the tie order on (wage, task text), an
order-free fractional rule was run beside it, and both declare the same owner." Three bullets follow three
`DEVIATION` headings. (b) Appended verbatim: "What had been seen, and is listed in the pre-registration, was the
shape of the quartiles without their outcome: the boundaries, the coding family's share of the top quartile, the
use-case mix by quartile, the Kish effective counts and the Seychelles figures."

**8 · Figure 3's "gradient" — applied as worded.** "**The top-minus-bottom difference does not survive either
composition leg: …**" in POST.md and in `figures.json` (283f346). "The gradient does not survive" is gone from
both, and the in-image title no longer reads "reverses the gradient".

**9 · Figure 4's hedge — applied as worded in POST.md and on the page.** "…and in the same direction as the
quartile gap in only one of the three, August's interval containing zero." The one number I re-checked: August's
`Delta_W` is −0.0222 on [−0.0572, +0.0129], so the interval does contain zero and the hedge is right.
`figures.json` still carries the old title; see below.

**10 · "The correction exists" — applied as worded.** "So the correction is small in every window,
indistinguishable from zero in one, and cannot be applied in a known direction from three windows: …" The
`claims.md` prohibition on "the correction is signed and small" is respected.

**11 · "Shows" as a finding's verb — applied as worded.** Limitation 7: "and in the exploratory split the two
components move in opposite directions across the wage distribution". No "shows" of a finding remains; the one
surviving "shows" is inside Anthropic's own bound, as before.

**12 · "An order of magnitude" — applied as worded.** Limitation 9: "— twice the largest difference reported here
and twenty to thirty times the smallest." The arithmetic I gave (14.1/20.2/16.1 against 1.4/7.4/0.7) is what the
sentence now says; the words carry no bindable number for the verifier, which is correct.

**13 · Limitation 2 — applied as worded, both halves.** "…the blend cannot be cleaned and a task's rate cannot be
rebuilt from the country files. Anthropic's own country regression reports lower-usage countries delegating more;
if top-quartile tasks are drawn relatively more from high-usage countries — which the global grain cannot confirm —
that would push the top quartile's share *down*, so the likelier direction of this bias is against the declared
sign." "no reverse construction is identified" and the unconditional "would push" are both gone.

**14 · The laundered binding — applied, and generalised.** The placebo band is now written in words — "widened
from plus or minus one to plus or minus two percentage points" — and `tasks_matching_first` occurs nowhere in
`claims-map.json` (grep: 0). The map was regenerated, so sentence ids have shifted; my three coincidence passes are
now bound to what they mean: "23" to `facts.november_is_corroborated_not_independent.source_check` (S12), the
"100" floor to `tests.rob_X3_drop_under_100_classified_aug2025.label` (S15), and the slope's "$10" to
`tests.slope_aug2025.estimates.slope.unit` (S18). Check 3 now makes such a pass impossible by construction, which
is the better fix.

**15 · "Higher than" a line of the same value — applied as worded.** "set separately from the one-point margin the
quartile difference is judged on."

**16 · The assistance disclosure's count — applied as worded.** "three figure captions were found to state a number
or a count the data did not support and were corrected — two at the results review and one, introduced by the
results review's own fix, at the draft review."

**17 · Figure 2's caption — applied, all three parts.** (a) The parenthesis is restored, and the condition I put on
it is met: the analyst added `facts.quartile_task_counts`, and the sentence "(the bottom quartile holds 600 / 699 /
649 tasks and the top 360 / 403 / 482)" is bound to `.Q1` and `.Q4` (S19). (b) "…and narrower than the markers at
this scale" is appended to the intervals sentence. (c) "…each quartile's usage-weighted mean hourly wage, this
post's levels, which do not reproduce Anthropic's task-value series (Limitations, 8)."

**18 · "Claude" in finding 2's heading — applied, both parts.** Heading: "…with that family excluded, the top wage
quartile on Claude.ai is delegated less than the bottom". The bold sentence took the optional clause too: "73, 71
and 65% of the top quartile's Claude.ai usage".

**19 · The lettered legs — applied as worded.** "— the pre-registration's (c), the leave-one-group-out series, and
(d), the use-case mix by quartile, are descriptive and are reported beside the legs, not as legs."

**20 · The fourth window — not applied; leaving it is acceptable, and I agree with the editor's reason.** This was
a could-item, offered at the editor's discretion, and the discretion was exercised the right way. My clause
"(positive in sign, unresolved at the task-level bound)" would have stated a *result* of `rob_fourth_window_*`, and
`claims.md` licenses no sentence for it: the fourth window appears in the claims list only as a stress test that
was run, which is exactly how POST.md's Methodology and Reproduction now carry it. Adding the reading would need a
`claims.md` sentence first, and a wording item is the wrong pass in which to widen the boundary. If the director
wants the clause in a later pass, the order is: claims-list sentence, then caption/prose, then verifier.

**21 · "Most conclusions standing" — applied as worded.** "close enough to the unweighted one, in these windows,
that the choice between them is not what a conclusion turns on".

**22 · The in-image titles — done on main at 283f346, and confirmed on the branch by checksum.** The four PNGs in
the branch's `posts/post1/outputs/figures/` are byte-identical to origin/main's regenerated files, and the page's
copies in `site/posts/post1/figures/` are identical to both (md5, all four: fig1 `6c442147…`, fig2 `86015966…`,
fig3 `c91b234e…`, fig4 `41d613f0…`). `outputs/figures.json` on the branch is also identical to main's. This closes
the fourth item of my "What I could not verify": the re-run of script 09 is the same artefact the page serves, and
the false Figure 2 title ("the bottom quartile is delegated nearly as often as the top") and Figure 3's "reverses
the gradient" are gone from the images.

## The Figure 4 departure

`figures.json` and `results.json`'s `figures.fig4.caption` still end "…and **not** in the same direction as the
quartile gap in **two of the three**", while POST.md and the built page carry item 9's hedged title. Three
findings.

1. **The departure is allowed as my §(b) wrote it.** §(b) asked the analyst for three things only — Figure 1's
count, Figure 3's title, and Figure 4's two deleted sentences — and item 9 was addressed to POST.md's caption, not
to `figures.json`. The analyst did what was asked and said so. The editor flagged the departure rather than
silently absorbing it, which is the right conduct.

2. **It is not a fault on the page.** The reader-facing artefacts are correct: POST.md, the `<figure>` block and
the page's prose all carry "in only one of the three, August's interval containing zero". The two deleted
sentences are gone from `figures.json` too, so the `claims.md`-forbidden wage-bill sentence is out of the record —
which was the serious half of §(b).

3. **A one-line analyst sync is recommended before merge; it does not block.** What remains is that the *record*
still asserts a direction for a window whose interval contains zero, which is the fault item 9 names. The
principle I applied to items 1 and 8 — `results.json` is the record, and the record may not state what the exhibit
does not establish — applies here in weaker form, because the count ("one of three" either way) is arithmetically
right and only the hedge is missing. So: recommend, do not block. The fix is one string in
`scripts/09_results_and_figures.py`'s fig4 caption, re-run, which rewrites `figures.json`, `results.json`'s
`figures` block and the four PNGs; POST.md needs no change and the verifier is unaffected. If the director prefers
to merge first and sync in the post2 phase, that is a defensible call, provided the mismatch is named in
`pr-description.md` so the next reader does not discover it as a discrepancy.

## Guard checks on the revision

- **Title unchanged.** "# Is AI delegated more on low-wage work or on high-wage work?" and the standfirst
  "*September 2026 · Evidence from Claude*" are byte-identical to c148bbe.
- **Every hunk is an item.** The POST.md diff is 22 changed passages and each one is an item above; nothing else
  moved. The claims-map diff is the regeneration.
- **No new unbound sentence.** The two sentences the revision *adds* beyond a replacement (item 5's two, item 19's
  clause) carry no bindable number. The two clauses *restored* into captions do, and both are bound: Figure 1's
  "$43.40/hr is a mass point carrying 8–11 pp of a window" to the three `boundary_tie_mass."b3_43.40".mass`
  values (8.36 / 7.95 / 10.60) at S07 — and it is not a new claim, since the body's S16 already states the same
  8-to-11 range under `claims.md` 4 — and Figure 2's per-quartile n to `facts.quartile_task_counts` at S19.
- **Forbidden phrases.** POST.md: no "wage bill", no "twelve points", no "cheap", no "expensive", no "delegated
  outright", no "the wage does not matter". "delegation rises with the wage of the work" occurs once and only
  once, in H1's own row of the hypotheses table, where the same row records that H1 failed — unchanged from
  c148bbe and allowed, as before. On the built page these phrases occur only inside evidence drawers that quote
  the claims list's own "may not say" column, the red-team memo, the lab notebook's CORRECTION entries and the
  assumptions sweep — mentions of the phrase, not claims made in it — and they are pre-existing, not introduced
  ("wage bill" in fact falls from 7 occurrences to 2). The site card is clean.
- **Ownership.** The editor's commit e98d27a touches POST.md, `claims-map.json`, `pr-description.md`,
  `verify_page.out.txt`, two `site/tools/` scripts, the `page-build` skill, the page and its figure copies, and
  two room files. It does not touch `results.json`, `figures.json`, `outputs/figures/`, the scripts or the lab
  notebook; those changed only in the analyst's 283f346, brought in by the rebase. No file crossed an owner.

## What this second read did not do

- No Anthropic source was re-read; the March 2025 and June 2026 quotations in items 3 and 5 are the text I
  prescribed and verified at the first read, and I checked only that the editor transcribed them exactly.
- No statistic was recomputed. Two stored values were re-read because the revision changed the sentences that
  carry them: `DeltaW_aug2025`'s interval (item 9) and the three `D` point estimates against the 14–20 pp bound
  (item 12).
- The page was checked by parsing `index.html`, not by rendering it; layout faults would not show. The PNGs were
  compared by checksum, not inspected as images, so the wording of the new in-image titles rests on the analyst's
  note and on the file identity with main.
- `pr-description.md` was read only for the length declaration my §(a) asked for; it is the editor's file and is
  outside this scope.
