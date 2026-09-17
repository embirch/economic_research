# Ideas noticed while running post1, for a later post — none of them run

Written by the analyst while executing `posts/post1/prereg/prereg.md`. Everything here is **outside**
the pre-registration and outside the three named exploratory tests, so nothing below was estimated.
Each entry names what was seen in passing and what a later post would have to pre-register.

## 1. One small geography can move a published task-level statistic by a dozen points

Dropping the 23 November tasks where Seychelles exceeds 10% of the global conversation count (the
pre-registered X5 cut, 11.594 pp of the wave) moves that wave's top-minus-bottom difference from
**+7.38 to −4.58 pp** — a flagged unit that the report excludes and the file does not, reaching a
task-level rate that no netting can clean because intersections are global only. A methods post
could ask, across the whole Index, which published task-level statistics are sensitive to the two
units the reports exclude (Seychelles Nov 2025, Utah Aug 2025) and how a reader is meant to know.
Would need: the per-task country weights where they exist, and a pre-registered sensitivity grid.

## 2. Occupational wages are a mass point, not a continuum, and rank-based designs cut through them

`wage_data.csv` prices 974 occupations, and one value — $43.40/hr — is the third quartile boundary
in all three waves, carrying 8–11 pp of a wave across 99–111 tasks. Any quartile design on
occupational wage is therefore cutting a mass point, and which tied tasks land above the line is not
a function of the wage. A methods post could measure how much of the published wage-quartile
literature (Anthropic's Figure 1.3 among it) rests on tie-breaking, and propose the fractional
allocation this post reports beside its primary.

## 3. Required preparation orders delegation the other way from price

Exploratory (c) found the Job-Zone slope negative (−6.0 to −6.8 pp per zone) where the wage slope is
positive or flat. Job Zone is preparation, not price, and the two orderings disagree. A later post
would pre-register the two-ordering contrast properly — Job Zone, education, wage and `ChanceAuto`
as competing orderings of the same delegation measure, with the collinearity of the four reported —
rather than reading it off one exploratory slope.

## 4. The surface, not the work: the API's gradient has the opposite sign

Exploratory (a) found D negative on the 1P API in all three waves (−2.40 / −2.47 / −5.15) against
positive on Claude.ai. Since the API's automation share is 82–87% and Claude.ai's is 46–51%, the two
surfaces are not comparable levels; but a post that pre-registered the *interaction* — the same task
seen on both surfaces, with the surface as the treatment and the task as its own control — would be
a genuinely new cut, and the task sets overlap enough to identify it.

## 5. `feedback loop` is the pattern that moved, and it moved in the top quartile

Exploratory (b) found the whole of the positive gradient carried by `feedback loop` (+8.4 / +16.9 /
+10.6 pp Q4−Q1) while `directive` is negative in every wave. A later post on the agentic surface
could take `feedback loop` as its outcome across all six released waves and ask where it grew, with
the 2025-09 → 2026-06 comparability caveats stated.

## 6. A data note for the steward, not a post: BLS-EP is keyed on SOC-2018

`data.bls.gov/projections/occupationProj` prices 670 of the 775 7-character O\*NET-SOC **2010**
codes, and the codes it misses include the renumbered computer family (`15-1132` → `15-1252`). Any
employment-weighted rule built on BLS-EP is therefore unidentified for whole occupational families,
not just for the two tasks `feasibility.md` §1 C7 names. This belongs in `data/ATLAS.md`; it is
written to the steward in `room/analyst-2026-09-17-results-post1.md` rather than edited in.

## 7. A within-group permutation is a composition diagnostic, not a null

The pre-registered placebo permutes the wage within SOC major group, which preserves the
between-group composition; its distribution is centred on +3.4 to +8.9 pp rather than on zero. That
is a usable diagnostic — the gap between the observed statistic and the permutation mean is the
within-group part of the gradient — but it needs its own pre-registration, and a second permutation
scheme (unrestricted) beside it to separate the two.
