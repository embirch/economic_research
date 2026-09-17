# Red-team memo · post1 (LL-07) · written after verification, 2026-09-17

The strongest case against each finding the results invite, as a referee would put it, followed by what
`results.json` answers and what the post must concede. Numbers are from `posts/post1/data/processed/results.json`
unless marked ⟨ref⟩, which are from `notes/rederivation/referee_results_post1*.py`. Findings are taken in the order
the post will meet them: the declared owner, the H3 qualification, Δ_W, leg (e), the exploratory probes.

## 1. Against the O-A declaration — "the top quartile is delegated more, in all three windows"

**1.1 The gradient is a coding gradient wearing a wage label.** Q4 is 73.1 / 71.3 / 65.5% Computer & Mathematical by
usage mass (`leg_a_*.coverage.dropped_share_q4`); three software tasks ("modify existing software to correct errors…"
×2, "write new programs or modify existing programs…") carry 11.4 / 12.2 / 8.8 pp of Q4's 22.5 pp ⟨ref⟩; Q4's Kish
effective N is 10.6 / 8.9 / 16.4 tasks (`facts.kish_*.by_quartile`). Coding tasks run at p ≈ 56–62 whatever their
wage — within SOC-15 alone the top-minus-bottom contrast is −0.1 / +6.5 / +0.8 pp ⟨ref⟩ — and everything else at
p ≈ 35–52. D > 0 because Q4 is mostly coding and Q1 mostly is not. The design was built to test exactly this (H3),
and H3 is declared: with SOC-15 out, D_L = −13.03 / −10.47 / −11.90 pp (`leg_a_*`); within major group, −4.20 /
−1.87 / −6.22 pp (`leg_b_*`); every contrast interval D_L − ½D excludes zero by ten or more standard errors.
**Answered, and the answer is the finding:** the post concedes that the O-A gradient is composition, in the same
paragraph as the O-A sentence, per the prereg's Interpretation table (H3 row).

**1.2 "Persistent" is true of the sign only.** D = +1.38 / +7.39 / +0.67 pp with SEs of 0.14: the SD across windows
is 3.69 pp, 26 times the within-window SE ⟨ref⟩. Whatever generated a 7-point gap in November and a two-thirds-point
gap in February, it was not conversation sampling, and the P1 interval does not describe it. The O-A label says "a
persistent gradient not shown to clear the margin in every window"; the magnitude is not persistent by any reading,
and the ordered rule's power figures (P2) assume a constant true D that the data refute (referee item 17).
**Partly answered:** `facts.rule_power` and the per-wave MDEs are correct as within-window statements; nothing in
`results.json` computes the probability of this outcome under a non-constant D, and the post must say none exists.
**Concession required:** the three point estimates in one sentence, no "stable", no average of the three.

**1.3 The owner does not survive two pre-registered cuts.** `facts.owner_under_robustness`: X5 (drop the 23 November
tasks where Seychelles exceeds 10% of the global count) → November −4.58 → **O-B**; the modal-holder wage rule →
February −0.17 [−0.44, +0.10] → **O-B**; X3 (drop tasks under 100 classified conversations) → **H1**. Two of seven
cuts move the owner to "no persistent gradient" and one moves it up. The registered rule declares O-A and the
sensitivity cuts are sensitivity, but a reader is entitled to know that the sign in February depends on how a
multi-holder task's wage is averaged, and the sign in November on two tasks. **Answered in the numbers; the post
must carry all three owner moves next to the declaration.**

**1.4 August's "clears a point" is a tie-order artefact.** The Q3/Q4 boundary is $43.40/hr in every wave, and
$43.40 is one occupation — Computer Occupations, All Other (`15-1199.xx`, $90,270 ÷ 2,080) ⟨ref⟩ — holding 99 / 106
/ 111 tasks and 10.6 / 8.4 / 8.0 pp of the wave (`facts.quartile_boundaries_*.boundary_tie_mass`). Which of those
computer tasks land in Q4 is decided by alphabetical order of the task text. Under the order-free fractional rule,
D = +0.54 / +7.18 / +0.34 (`D_corrected_quartile_rule`): August no longer clears +1 pp and the O-A/H1 boundary is
a matter of sorting. **Answered by the deviation, both readings reported.** **Concession:** both numbers wherever
August's or February's D appears; the boundary occupation named.

**1.5 The country mix — the rival that cannot be tested.** A task's global rate blends countries; Anthropic's own
Figure 2.11 (reproduced: −3.11, partial R² 0.39, N 111) says low-AUI countries delegate more, and India (coding-heavy,
7.2% of usage) sits in Q4. Intersections are global only, so no per-task rate can be cleaned
(`facts.country_mix_not_testable`). **Not answered; must be the first limitation.** The Seychelles case is the one
place a bound exists: netting SC from the weights moves November by −0.84 pp (`rob_X4`); counting every SC
conversation on a Q4 task as automation and every one on a Q1 task as augmentation, with weights netted, leaves
November at +4.50 pp ⟨ref⟩. So Seychelles does not explain November's excess over August and February — but it
also shows that a single anomalous geography of 2.5% of the wave can move D by up to three points when it lands on
Q4's largest tasks. The X5 "flip" is not a Seychelles result: it removes the two largest software tasks, which carry
p ≈ 70–74 in every wave; the ten-largest-tasks leave-out does the same in all three (−11.6 / −13.1 / −11.4,
`desc_ten_largest_out_*`).

**1.6 Cohort and window.** February carries the Super Bowl inflow (Q1 is 56% personal in Feb against 45% in Nov,
`desc_use_case_mix_*`); Anthropic reports its newer users doing lower-wage tasks. Each wave is estimated separately,
so cohort change is inside the "persistence" test rather than controlled. The magnitude swing in 1.2 is consistent
with it. **Not separable by this design; concede in the same paragraph as the three D's.**

**1.7 The SE is a lower bound.** No user, session or account identifier exists; one user's afternoon on "modify
existing software" is many conversations on one task (`facts.declared_owner` notes; prereg P1(a)). The intervals of
±0.28 pp are the floor. The realised between-window dispersion (1.2) says the floor is far below the uncertainty
that matters. **Concede at every interval, as the caption already does.**

**1.8 Not monotone.** The quartile shares are U-shaped in every wave — 53.1 / 47.0 / 49.8 / 54.4; 46.6 / 41.3 /
46.0 / 54.0; 48.8 / 41.6 / 43.5 / 49.5 (`desc_quartile_shares_*`) — and the continuous slope's sign disagrees across
waves (−0.05 n.s. / +1.77 / −0.28 pp per +$10/hr, `slope_*`). "Delegation tracks the wage of the work" (the §12 O-A
wording) implies an ordering the data do not show: the bottom quartile is delegated more than the second and third,
and nearly as much as the top. **Concession:** the post says "top quartile exceeds bottom quartile", never
"rises with", "tracks" or "gradient" without "top-minus-bottom" attached.

**1.9 The rate is not the bill; the wage is not the user's.** Δ_W re-weights by an hourly wage, no hours enter
(`DeltaW_*.notes`); the wage is that of US occupations whose tasks *resemble* the conversation's, not the user's
(2026-06 p. 7). A recipe request mapped to a Chef's task is priced at a chef's wage. **Conceded in the prereg;
must be in the definition paragraph.**

## 2. Against the H3 qualification — "the relation is composition: coding"

**2.1 Leg (a) trades one composition for another.** With SOC-15 out, Q4 keeps 6.1 / 6.5 / 7.8 pp of mass (286 / 327
/ 355 tasks, Kish 98 / 86 / 83): management (11), life and physical science (19), engineering (17), healthcare
practitioners (29), at p ≈ 21–46 ⟨ref⟩. Q1 is office and administrative support (43) at p 56–66, education (25) at
37–40, sales (41), plus 14–24 low-wage computer-support tasks at p 55–60. The −13 pp is "clerical and support tasks
are handed over; managerial, scientific and clinical tasks are worked through" — still a statement about task type,
not about price. The design cannot separate the wage of the work from the kind of work at any grain, because wage is
a property of the occupation the task resembles. **Not answered; the post may report leg (a)'s number as the H3
qualifier and may not read it as a negative *price* gradient.**

**2.2 Leg (b) is the cleaner statement but rests on nine or ten groups.** Within-group D_(b) is negative in every
wave, on 10 / 10 / 9 identified groups carrying 80.0 / 80.3 / 75.5% of Q1+Q4 mass; the all-four subset gives
−4.05 / −1.79 / −6.09 ⟨ref⟩. Within SOC-15 itself the contrast is ≈ 0 in Aug and Feb and +6.5 in Nov, so the
negative average comes from the non-coding groups. **Answered as far as the design allows; the post reports the
identified mass and the not-identified groups by name.**

**2.3 Leg (a) and the leave-one-group-out series are the same evidence.** SOC-15's removal moves D by −14.4 / −17.9
/ −12.6 pp; the next largest mover by 3.2 / 2.3 / 2.9 (`desc_leave_one_group_out_*`). Twenty-two re-estimates that
all say "SOC-15" are one observation. **Conceded in the prereg and the caption.**

**2.4 The H3 power caveat does not bite here.** The prereg says an H3 non-declaration in the O-A range is "nothing
shown" because the persistent-leg rule detects a three-quarters loss with probability 0.4–0.7. H3 *is* declared, on
sign reversals of 2–13 pp at SEs of 0.2–0.3 — nowhere near the boundary. The caveat that survives is leg (e)'s
(§4 below).

## 3. Against Δ_W — "weighting by the wage moves the published share by a tenth of a point per point of gap"

Δ_W = −0.022 [−0.057, +0.013] / +0.835 [+0.800, +0.870] / −0.147 [−0.184, −0.110] pp. The brief's 0.11–0.12 per
point of gap holds in November (0.113) and fails in August (−0.016) and February (−0.219) ⟨ref⟩, because Δ_W depends
on all four quartiles and the U-shape puts the trough in the middle. Its sign follows D's in one window of three.
**Answered by the numbers; the post may not state the per-point arithmetic as a realised relation and may not call
the correction "signed".** It may say: below one point in every window; smaller than the quartile gap by an order of
magnitude in November and of opposite sign in the other two; an hourly rate, not a bill.

## 4. Against leg (e) — "the use-case mix does not carry the gradient"

Leg (e) did not fire (Nov r = 0.503, Feb r = 4.17). In November it sits exactly on the boundary: D_L − ½D = +0.02
[−0.33, +0.37] pp, so whether the work-dominant set keeps more or less than half of D is a coin toss at this
precision. In February the restriction *raises* D (0.67 → 2.79) because the work-dominant Q4 is the coding Q4
(81–83% of Q4 mass kept against 20–30% of Q1's, `leg_e_*.coverage`) — leg (e) is not independent of leg (a). A
personal or coursework request is directive by construction, so the bottom quartile's ~50% is partly the use-case
rival the prereg named. **Not answered:** non-firing is "nothing shown", as the prereg's Interpretation table
requires; the post may not say the use-case mix has been ruled out, and may not test the rival in August at all.

## 5. Against reading the exploratory probes as findings

All three run against the headline's sign: the 1P API gradient is negative in every wave (−2.4 / −2.5 / −5.2 pp);
the JobZone slope is −6.0 to −6.8 pp per zone; and `directive` — the pattern the brief's own question calls
"delegated outright" — is *lower* in Q4 in every wave (−7.0 / −9.5 / −9.9 pp) while `feedback loop` carries the
whole positive gradient (+8.4 / +16.9 / +10.6). The temptation is a second headline: "outright delegation falls with
the wage of the work." **It is exploratory, three of three probes, none pre-registered as a decision, none may
headline.** What the post must concede instead: the confirmatory measure is directive + feedback loop, and the
positive gradient lives in feedback loops — Anthropic's "users automate tasks and provide feedback to Claude as
needed" — so the word "outright" may not describe the finding anywhere, including the question sentence inherited
from BRIEF §1.

## 6. The multiple-testing count

One ordered rule on three intervals declares the owner; one rule on eight leg tests declares H3; 24 robustness
entries and 16 descriptive entries are reported, not tested; 3 exploratory tests carry 27 sub-estimates. At
conversation-level SEs of 0.1–0.3 pp every difference larger than a point is "significant"; significance is never
the question in this design, composition is, and the sensible reader discounts every p-value and reads the sign
under each cut instead. `facts.owner_under_robustness` is the table that matters.

## 7. The smallest samples the claims rest on

- Q4: Kish 8.9 effective tasks in November; three software tasks are 39–54% of its mass.
- The $43.40 tie: 7.3 / 4.9 / 6.1 pp of Q4's mass placed by alphabetical order.
- February's owner under the modal-holder rule: 14 low-wage computer tasks in Q1 (2.6 pp) and 86 multi-holder tasks
  decide the sign.
- November under X5: 5 Q4 tasks (8.9 pp) removed.
- Leg (b): 9–10 groups; the within-15 contrast in Q1 rests on 14–24 tasks.
- Leg (e): 943 / 1,071 tasks, but Q1's work-dominant subset is 20–30% of Q1's mass.

## 8. What a later wave would need to show

For O-A to become more than a sign: a D whose sign survives the modal-holder rule, the drop of the ten largest
tasks, and the fractional quartile rule in the same wave; a magnitude inside the previous waves' range. For the H3
reading to be a price statement rather than a task-type statement: a within-occupation contrast (leg (b)) that
holds when the identified set is enlarged, or a wage source that prices the computer family so the second-source
test is a real one — BLS-EP cannot be that source while the O\*NET file is on 2010 codes. For the use-case rival: an
August-like wave with a `use_case` intersection. None of these is available in the released data as of
2026-06-26.

## 9. What the assumptions sweep (BRIEF §7) flagged, revisited

(1) *Value judgement*: the body says "the wage of the work"; the results add a reason — low-wage in this data is
clerical, educational and sales work plus personal and coursework requests, so any "cheap/expensive" reading would
be doubly wrong. (2) *Construct*: the finding is about `directive` + `feedback loop`; the split shows the two
components move in opposite directions in wage, so the construct's name ("delegated") must be fenced by its
definition at first use. (3) *Composition*: confirmed as the finding — coding is the mechanism, and the country
mix remains untestable. (4) *Anthropic's own results*: the U-shape agrees with the 2025-03 non-monotone category
cross; the reversal outside coding and the negative `directive` gradient are consistent with the 2026-06 turns
reading ("if the human remains involved in the highest-value tasks…") — consistent with, never confirmation; the
2026-01 education-level null is not extended, since this is not a null.
