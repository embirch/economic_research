# Referee verdict (second read) · post1 (LL-07) · pre-registration, revised · 2026-09-17

Second read, narrow by design. Read only: my own `posts/post1/notes/referee-prereg.md` (the verdict at
`origin/main` f859206), `posts/post1/prereg/prereg.md` at c9b1b45, `git diff 47faca0 c9b1b45 --
posts/post1/prereg/prereg.md` (the whole change set, +61 / −16, nine hunks) and
`room/analyst-2026-09-17-prereg-post1-revised.md`. The brief, the feasibility note, the replication
note and Anthropic's sources were **not** re-opened; no number was re-derived except the ones the
revision inserted, and those only against the files already in the record
(`posts/post1/data/processed/power_rules.json`, `posts/post1/notes/rederivation/referee_prereg_post1.out.txt`).
No data statistic was computed; **no value of D, Δ_W, any quartile automation share or any leg was
computed or seen.** Matching was done on whitespace-normalised text, so a line break inside a quoted
sentence counts as a match and a changed word does not.

## Verdict

**SIGN OFF** (PASS). All seven "should" items — 4, 5, 6, 7, 9, 11, 14 — are **applied in the
referee's exact words**, with the superseded text gone in every case; the four block quotations of the
verdict appear verbatim in the pre-registration and the five inline replacements are word-for-word.
The two applied "could" items, 15(a) and 15(b), are the verdict's own text and are pure wording: both
sit in an "Expected MDE" statement or a power-table row label, neither touches a rule, a threshold or
a declaration. The two unapplied "could" items, 10 and 15(c), are correctly identified by the analyst
as needing sentences the verdict did not supply; leaving them is acceptable (reasons in items 9 and 10
below) and both are carried to the results stage as reporting commitments, not as design changes. The
guard is clean: **the diff changes nothing outside those items** — no hypothesis, no ordered step, no
δ, no threshold, no exploratory test, no sample or exclusion rule, and the only Interpretation-table
change is item 6(ii)'s last row. Every inserted number reproduces the record exactly. "Committed as"
is still `<git hash, filled by the director>` and the six template headings remain in order. The
pre-registration is ready for the director to commit; nothing here is for the analyst.

## Items

### (a) The seven "should" items

**1. Item 4 — P4's justification. APPLIED, verbatim. (Prereg §H3, "The completion, marked", line ~413.)**
The verdict's replacement paragraph is present word for word: "BRIEF §6 does not settle it: §6 H3's
'against it' … and §6 H1's 'against it' (losing on any composition leg) are both complements of the
any-wave reading. The persistent-leg rule is nevertheless primary, for a reason of specification rather
than of text: … the any-wave reading declares H3 with no composition present in roughly 60 / 50 / 27 /
12% of declared gradients at a true D of 0.5 / 0.6 / 0.8 / 1.0 pp, whereas the persistent-leg rule does
so in at most 1–2% at any D … A rule that fires under the null in a quarter to two-thirds of cases in
the O-A range is not a test, so the literal reading is reported beside the primary rather than used as
it. Mirroring §9(1)'s all-three-waves persistence for D:". The old justification — "Mirroring §9(1)'s
persistence rule for D … and BRIEF §6 H3's 'against it' clause, which requires D to keep half its size
and its sign on all three legs 'in all three waves'" — is **gone**. The sentence that follows the colon
(the Primary bullet) is unchanged, so the rule itself is untouched: only its reason changed, which was
the item.

**2. Item 5 — H3's "rule against" and the "rule for support". APPLIED, verbatim, both halves.**
"**Rule against (H3).** No leg fires in every wave in which it is testable — the complement of the
support rule, so every declared gradient is either H3-qualified or not. The strongest form … is BRIEF
§6 H3's 'against it' and is reported as such when it obtains; a leg firing in some waves but not all is
'not declared' and is reported with the literal reading's verdict in the same sentence (above)." The old
bullet ("D keeping more than half its size and its sign on all three legs and across all 22
leave-one-group-out re-estimates, in all three waves.") is gone, so the 22 leave-outs no longer sit
inside a rule. Support now reads "As above, when H1, H2 or O-A has been declared (a declaration spans
the three waves)"; the old "on a wave in which H1, H2 or O-A has been declared" is gone. H3's outcome
space is now a stated partition (declared / not declared).

**3. Item 6 — the H3 rule's own power. APPLIED, both insertions, verbatim.**
(i) The new bullet "**Power of the H3 rule, per rule and not per leg**" is present in full, with the
covariance model, the script reference and the ±0.03 reproduction tolerance, and with the sentence the
item existed for: "in the O-A range an H3 non-declaration is 'nothing shown', not composition excluded".
It sits after the "Expected MDE" bullet, as specified, and before "Specification risks".
(ii) Interpretation table, row "H3 not declared, or not evaluated (H4 / O-B)": "what it may say" now
appends "; where the owner is O-A, that the pre-registered rule detects a three-quarters loss on a
single leg with a probability of roughly 0.4–0.7 at a true D of 0.5–1.0 pp, so non-declaration is
nothing shown, not composition excluded"; "what it may not say" now appends "; that composition has
been ruled out". Both columns, as specified.
*Numbers checked* (the revision inserted them, so they were checked, against
`referee_prereg_post1.out.txt` §C, loss = 0.75 rows, "pers" columns — not recomputed): leg (a) 0.370 /
0.459 / 0.601 / 0.721 / 0.915 → printed 0.37 / 0.46 / 0.60 / 0.72 / 0.92; leg (e) 0.544 / 0.628 / 0.749
/ 0.840 / 0.962 → 0.54 / 0.63 / 0.75 / 0.84 / 0.96; leg (b) 0.288 / 0.349 / 0.452 / 0.551 / 0.767 →
0.29 / 0.35 / 0.45 / 0.55 / 0.77; persistent false declaration 0.010 / 0.004 / 0.001 / 0.000 / 0.000
(harsh 0.024 / 0.013 / 0.003) → "≤ 0.01–0.02 at every true D"; any-wave false declaration 0.604 / 0.494
/ 0.266 / 0.116 / 0.009 → 0.60 / 0.49 / 0.27 / 0.12 / 0.01, and item 4's "roughly 60 / 50 / 27 / 12%";
SE(D_(a)) 0.247 / 0.237 / 0.226 → "≈ 0.23–0.25 pp", corr 0.61 / 0.63 / 0.68 → "≈ 0.6–0.7",
SE(D_(a) − ½D) 0.210 / 0.199 / 0.183 → "≈ 0.18–0.21 pp". Every figure matches the record; none was
rounded in a favourable direction.

**4. Item 7 — H1's and H2's "rule against". APPLIED, verbatim, both.**
H1: "losing more than half the size, or the sign, on a leg in every wave in which that leg is testable
(H3 qualifies the declaration, P4); a leg firing in some waves only is reported with both readings'
verdicts". H2: "losing more than half the size, or the sign, on a leg in every wave in which it is
testable (H3, P4)". The any-wave phrasings ("on any testable leg (H3 qualifies the declaration)", "on a
testable leg (H3)") are gone. H1's first clause (any wave whose lower bound does not clear +1 pp) and
its P6 clause are untouched, so step (1) is unchanged; the whole of the change is the leg language, now
consistent with H3's primary rule. No other "rule against" in the document was touched.

**5. Item 9 — model (a)'s SE as a lower bound. APPLIED, verbatim, in the right place.**
Inserted directly after "the task enters as a weight, not as a cluster of repeated observations.":
"Conversations within a task are not known to be independent — one user or one session may contribute
several — and no identifier exists to correct for it, so model (a)'s SE is a lower bound on the
sampling variance of D under within-task dependence and is stated as such wherever it appears." The
surrounding error-type paragraph ("No clustering is applied, and none is available", the two-sided 95%
/ 5% / δ = 1 pp / MDE = 2.8 × SE sentence) is unchanged.

**6. Item 11 — the C7 sign disagreement under H1 / H2 / O-A. APPLIED, verbatim, both parts.**
A new bullet under H1, "**P6 · The second wage source under H1 / H2.**", carries the full text
including "the owner is unchanged — the ordered rule runs on C6 —", the first-sentence obligation on
the §12 paragraph, C7's coverage 55.66 / 58.52 / 62.22% and "H3 is still evaluated". Its heading names
H2, which is the "H2 by reference" the verdict asked for; H2's own section is otherwise unchanged. The
O-A P6 bullet has the appended sentence word for word. The owner-selection chain still runs on C6 in
every case, so no rule moved.

**7. Item 14 — the work-share covariate. APPLIED, verbatim.**
"The confirmatory set", the "Reported beside them, in no decision rule" list, now includes "the
continuous slope with the task's work share as a covariate (§9(3)(e); Nov and Feb), with the
usage-weighted pairwise correlation and VIF of wage and work share printed beside it, since the two
predictors compete". It is in the no-decision-rule list, not in the confirmatory table: the count of
confirmatory estimates is still **17, of which 8 are the leg tests**, unchanged.

### (b) The two applied "could" items: pure wording, no rule effect

**8. Items 15(a) and 15(b). APPLIED as the verdict wrote them; no rule effect. Confirmed.**
15(a), O-A "Expected MDE": "80% power at a true |D| of ≈ 0.5 pp; per-wave MDE 0.42 / 0.42 / 0.43 pp" →
"O-A or stronger reaches 80% from ≈ 0.5 pp; O-A as declared is ≈ 1.00 near 1.0 pp and yields to H1
above ≈ 1.4 pp. Per-wave MDE 0.42 / 0.42 / 0.43 pp." This is a power statement inside an MDE bullet,
not a rule: O-A's "rule for support" and "rule against" are byte-identical to 47faca0, and the ordered
five-step chain is untouched. The three figures it introduces are read off the committed
`power_rules.json` and are right: `OA_or_stronger_80pc` = 0.5172 pp ("80% from ≈ 0.5"); on the steward
SE curve, P(O-A) at D = 1.0 is 0.99998 ("≈ 1.00 near 1.0 pp"); at D = 1.42, P(H1) = 0.5009 against
P(O-A) = 0.4991, so H1 overtakes O-A just above 1.4 pp ("yields to H1 above ≈ 1.4 pp"). Wording that
now distinguishes "O-A or stronger" from "O-A as declared" — the same clause-versus-declared
distinction the P2 table already carried for H4 — and nothing else.
15(b), the P2 table: the H4-clause row label gains "(the figure BRIEF §9(4) quotes)". Label text only;
the row's three numbers (0.483 / 0.485 / 0.486; 0.000; 0.133 at 0.70 pp) are unchanged, as is the "H4
as declared" row beneath it. Both are the verdict's own text, so neither introduces a formulation I had
not already ruled on.

### (c) The two unapplied "could" items

**9. Item 10 (the r_L ratio interval). NOT APPLIED. Acceptable; carried to the results stage.**
The analyst is right that the verdict gave no replacement text and that applying it would change which
interval a reader is *directed* to for the half judgement — that is an editorial instruction, not a
silence to be filled, and it is the sort of change a second read should not wave through unwritten. The
rule is unharmed: the H3 "Estimand of each leg" paragraph, unchanged at c9b1b45, states that "the
declaration is made on the point estimates, as §9(3) writes it" and that **both** the interval for
D_L − ½D and the interval for r_L are "reported beside every leg so that a leg firing on a point
estimate whose interval straddles ½D is visible as such". So no declaration depends on the unstable
object, and both intervals reach `results.json`. **Carried:** at the results review I will check that
the half judgement is discussed from D_L − ½D and that the r_L interval's instability as D̂ → 0 is
named wherever an r_L interval is printed. Not a design change and not a condition of sign-off.

**10. Item 15(c) (O-B's probabilities assume a constant true D). NOT APPLIED. Acceptable; carried, and
the one to watch.** The O-B "Expected MDE" bullet is unchanged and still prints 0.043 at 0.5 pp, 0.008
at 0.7 pp, 0.000 at 1.0 pp without saying that those are computed under a constant true D, while O-B
is the outcome a *non-constant* D (the §7(3) cohort shift) produces. Again a new sentence, not a
substitution, and the verdict marked it "could". The exposure is interpretive rather than procedural:
the figures are correctly attributed to `01_power_rules.py`, and the "assumptions" block of
`power_rules.json` states the constant-D model, so nothing in the record is wrong. **Carried:** if O-B
is the owner, the post may not read 0.043 as "O-B was unlikely"; the probability of O-B under a
non-constant D is not computed and must be said not to be. I will check that sentence at the results
and draft reviews. Not a condition of sign-off.

### (d) The guard: did anything else move?

**11. Nothing outside the items changed. CONFIRMED.**
The diff is nine hunks and each maps to an item and to nothing else: line ~179 → item 9; ~272 → 15(b);
~297 → item 7 (H1) + item 11 (H1's new P6 bullet); ~322 → item 7 (H2); ~413 → item 4; ~441 → item 5
(both bullets) + item 6(i); ~508 → 15(a) + item 11 (O-A); ~545 → item 14; ~696 → item 6(ii). No other
file in c9b1b45 belongs to me or to the pre-registration's rules (the commit also adds the analyst's
notebook entry and his room note, and carries my own verdict, re-derivation script and output, which
were written at 37868c3 / f859206). Specifically unchanged, checked line by line against 47faca0: the
ordered five steps and their first-match precedence; δ = 1 pp; z = 1.959964; the two-sided 5% error
type; H1's, H2's, H4's, O-A's and O-B's "rule for support"; H4's and O-B's bullets entire; the H3
primary and literal leg rules themselves; the 8 leg-wave tests and the "k of 8" reporting; the
confirmatory table and its 17 / 8 counts; the three-test exploratory allowance and the "any additional
cut is a logged deviation" sentence; S1–S3, X1–X8, W1, A1–A2, V1, E1; the P8 disclosure section; the
P3(a), P3(b) and P3(e) mechanics including the 10 / 10 / 8 and 7 / 8 / 6 sets, the ≥ 0.50 threshold,
the 943 / 1,071 counts and the 29 / 21 drops; P6's two-implementation table; the synthetic-recovery
list; the Robustness section; the Interpretation table's other six rows and the body-language
paragraph; the Deviations section. No hypothesis was added, dropped or re-worded.

**12. Template and commit line. CONFIRMED.** "**Committed as** `<git hash, filled by the director>`"
is still unfilled. The six template headings are present and in order: Disclosure: what has already
been seen · Definitions, fixed · Hypotheses and decision rules · Robustness, fixed now ·
Interpretation, fixed now · Deviations. Register spot-check on the added text only: no first person in
any inserted sentence; the inserted sentences say "Claude" or nothing about the subject and make no
claim about AI in general.

## Independent re-derivations

Not a results stage, and by scope this read re-derives nothing that did not change. Three inserted
number sets were checked against files already in the record, with no new code:

| inserted number | where | source checked | match |
|---|---|---|---|
| H3 rule power, legs (a) / (e) / (b), and both false-declaration rates (item 6 bullet, item 4 paragraph) | prereg §H3 | `posts/post1/notes/rederivation/referee_prereg_post1.out.txt` §C | exact at the printed precision (see item 3) |
| SE(D_(a)) ≈ 0.23–0.25, corr ≈ 0.6–0.7, SE(D_(a) − ½D) ≈ 0.18–0.21 | prereg §H3 | same, §C header rows | exact (0.247 / 0.237 / 0.226; 0.61 / 0.63 / 0.68; 0.210 / 0.199 / 0.183) |
| O-A: 80% from ≈ 0.5 pp; ≈ 1.00 near 1.0 pp; yields to H1 above ≈ 1.4 pp (15(a)) | prereg §O-A | `posts/post1/data/processed/power_rules.json` (`OA_or_stronger_80pc` 0.5172; P(O-A \| 1.0) 0.99998; P(H1 \| 1.42) 0.5009 vs P(O-A \| 1.42) 0.4991) | exact |

`posts/post1/scripts/01_power_rules.py` and `posts/post1/data/processed/power_rules.json` are unchanged
in the diff, so the check block re-run reported by the analyst was not repeated here.

## Assumptions sweep

Not a sweep stage. Carried unchanged from `referee-brief-2.md` and from the first pre-registration
verdict: (1) value judgement HANDLED; (2) construct mapping HANDLED; (3) composition HANDLED —
strengthened by this revision, since item 6's insertion now forbids reading an H3 non-declaration as
composition excluded; (4) Anthropic's own results HANDLED. Nothing in the revision reopens any of the
four.

## What I could not verify

- The covariance model behind items 4 and 6 remains mine and approximate (the caveats in
  `referee-prereg.md` §"What I could not verify" stand unchanged); the revision reproduces my figures,
  it does not validate the model. The pre-registered commitment is the realised SE, MDE and
  D_L − ½D interval printed beside every leg, and the ±0.03 reproduction tolerance in the new bullet.
- By scope I did not re-read BRIEF.md, so item 4's and item 7's fidelity to §6 and §9 rests on the
  first verdict's reading, not on a fresh one. The footnote the first verdict asked the director for —
  BRIEF §9(4)'s "up to about 0.5 pp" is the clause's figure, not H4-as-declared — is still outstanding
  and is not the analyst's to write.
- Whether the analyst changed anything in files he owns beyond the notebook entry and the room note was
  not audited; only `prereg.md` was diffed.
- Items 10 and 15(c) are unapplied by agreement, so the two commitments in items 9 and 10 above exist
  only in this verdict and in the first one. They are not pre-registered, and I will raise them at the
  results review.
