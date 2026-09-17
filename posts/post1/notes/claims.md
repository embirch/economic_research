# Claims list · post1 (LL-07) · written by the referee after verification, 2026-09-17

Every sentence below is bound to a key in `posts/post1/data/processed/results.json` (test id → `estimates.<term>`,
or `facts.<id>`). Numbers may be coarsened upward (a decimal in the body, "about" in the opening) but never changed in
unit or sign. Every finding sentence says **Claude.ai**; the question says **AI**. The body says **the wage of the
work**, never "cheap" or "expensive". "Delegated" means Anthropic's automation share — `directive` plus `feedback
loop` conversations over the five classified collaboration patterns — and the definition sits in the paragraph
before the first number. "Outright" may describe `directive` alone, in the exploratory section only.

Declared owner (`facts.declared_owner`): **O-A**, on the pre-registered quartile rule and on the corrected one.
H3 (`facts.H3_declaration`): **declared**, on legs (a) and (b), each firing in every wave in which it is testable;
literal and persistent rules agree. H1's signature clause fails (`facts.H1_signature_clause`). The §12 paragraph the
post writes is therefore **"If O-A holds"**, qualified by **"If H3 holds"** in the same section, with the P6
first-sentence rule for the second wage source.

## Sentences the post may state

### The headline (D)

1. "In each of the three Claude.ai windows the automation share of conversations on top-wage-quartile tasks
   exceeded that of conversations on bottom-quartile tasks: by 1.4 points (4–11 August 2025), 7.4 points (13–20
   November 2025) and 0.7 points (5–12 February 2026)." ← `D_aug2025.D` +1.3836 [+1.1006, +1.6667];
   `D_nov2025.D` +7.3854 [+7.1103, +7.6605]; `D_feb2026.D` +0.6689 [+0.3947, +0.9431]; MDE 0.40 / 0.39 / 0.39.
   **Bound:** the three numbers appear in the same sentence; no average, no "about a point", no "gradient" without
   "top-minus-bottom".
2. "The difference exceeds one percentage point in two of the three windows and not in the third; the
   pre-registered rule therefore records a persistent sign and does not record a gradient above the one-point
   margin in every window." ← `facts.declared_owner` (steps 1 F, 2 F, 3 T). **Bound:** "persistent sign", not
   "persistent gradient" and not "stable".
3. "On the corrected quartile rule, which shares the boundary wage between the two adjacent quartiles instead of
   letting sort order decide, the differences are 0.5, 7.2 and 0.3 points, and August no longer exceeds one
   point." ← `D_*.D_corrected_quartile_rule` +0.5434 [+0.2671, +0.8196] / +7.1793 [+6.9116, +7.4470] / +0.3387
   [+0.0696, +0.6077]; `facts.declared_owner_corrected_quartile_rule` O-A. **Required beside sentence 1** wherever
   August's or February's D is quoted.
4. "The third quartile boundary is $43.40 an hour in every window — the wage the file assigns to Computer
   Occupations, All Other — and the 99 / 106 / 111 tasks at that wage carry 8 to 11 percentage points of a window,
   so the top quartile's membership is decided partly inside the coding family." ←
   `facts.quartile_boundaries_*.boundary_tie_mass.b3_43.40` (tasks 99 / 106 / 111; mass 10.60 / 8.36 / 7.95),
   `q4_mass_from_boundary_tie` 7.33 / 4.93 / 6.14; `facts.quartile_boundaries_*.boundary_occupation` "15-1199
   Computer Occupations, All Other ($90,270 ÷ 2,080 = $43.40/hr)" — thirteen detailed `15-1199.xx` codes at one
   salary (`boundary_occupations.b3_43.40.detailed_codes` 13). **Bound:** "Computer Occupations, All Other" names the
   7-character group; the four titles listed in `results.json` are a truncated sample of the thirteen, not the set.
5. "The intervals are two-sided 95% under a conversation-level binomial with the task mix held fixed; no release
   carries a user, session or account identifier, so they are a lower bound on the sampling variance."
   ← `D_*.notes`. **Required at the first interval.**
6. "The size of the difference is not stable across windows: it varies from two thirds of a point to more than
   seven points, a spread twenty-six times the within-window standard error, so the intervals describe conversation
   sampling inside a window and not the variation between windows." ← `D_*.D.coef` and `.se` (SD 3.69 pp against
   mean SE 0.142; the arithmetic is the referee's from those six numbers). **Required in the same paragraph as
   sentence 1.**
7. "Read as a statement about tasks rather than about these windows' conversations, a design that resamples tasks
   resolves nothing below about fourteen to twenty percentage points." ← `rob_model_b_*.D` SE 5.03 / 7.20 / 5.76,
   MDE 14.07 / 20.16 / 16.12; `facts.generalisation_sentence` 20.16. **Required in the close; "twelve" is not the
   realised figure.**
8. "Dropping the 23 November tasks in which Seychelles exceeds a tenth of the global conversation count turns
   November's difference to −4.6 points; netting Seychelles from the task weights alone moves it to +6.5; the
   November rates themselves cannot be cleaned." ← `rob_X5_drop_sc_over_10pc_nov2025.D` −4.5815 [−4.9003, −4.2628];
   `rob_X4_sc_netted_weights_nov2025.D` +6.5463; `facts.november_is_corroborated_not_independent` (the 23 tasks
   carry 8.9 pp of the top quartile's 22.5). **Bound:** the sentence says that those 23 tasks include the two
   "modify existing software to correct errors…" tasks, which alone carry 8.5 of the top quartile's 22.5 pp in
   November (6.5 in August, 6.0 in February), so the flip is not attributed to Seychelles alone (red-team 1.5) ←
   `facts.composition_of_the_top_quartile.largest_software_tasks.<wave>.q4_mass_first` 6.5266 / 8.5413 / 5.9802,
   `q4_share_first` 28.8 / 37.9 / 26.6%. The post may also state the bound: "counting every Seychelles conversation
   on a top-quartile task as automation and every one on a bottom-quartile task as augmentation, with the weights
   netted, leaves November's difference at +4.5 points" ← `facts.seychelles_worst_case_bound` D_worst_case 4.5038,
   D_weights_netted 6.5463, D_observed 7.3854.
9. "Under the modal-holder wage rule the February difference is −0.2 points with an interval containing zero, and
   under the pre-registered rule the ordered chain would then record no persistent sign; under the equal-split rule
   the three differences are unchanged to a tenth of a point." ← `rob_W1_modal_holder_feb2026.D` −0.1701 [−0.4438,
   +0.1037]; `rob_W1_equal_split_*.D` +1.3770 / +7.3853 / +0.6581; `facts.owner_under_robustness.owners`
   (W1_modal_holder → O-B; X5 → O-B; X3 → H1). **Required beside sentence 2.**
10. "Dropping tasks with fewer than 100 classified conversations raises the differences to 2.6, 9.1 and 1.6
    points." ← `rob_X3_drop_under_100_classified_*.D` +2.6049 / +9.0725 / +1.5934.
11. "The quartile shares are not monotone in the wage: in every window the share falls from the bottom quartile to
    the second and rises to the top — 53.1, 47.0, 49.8 and 54.4% in August; 46.6, 41.3, 46.0 and 54.0% in
    November; 48.8, 41.6, 43.5 and 49.5% in February." ← `desc_quartile_shares_*.Q1..Q4.coef`, with `none_share`
    beside each (3.6 / 1.9 / 1.9 / 1.2 etc.). **Required before any sentence comparing top and bottom.**
12. "The continuous slope of the automation share in the hourly wage has no stable sign: −0.05 points per $10 (not
    distinguishable from zero) in August, +1.77 in November, −0.28 in February." ← `slope_*.slope` −0.0507
    [−0.1309, +0.0294], MDE 0.114; +1.7657 [+1.6915, +1.8399]; −0.2843 [−0.3559, −0.2127]. **Bound:** sign and
    significance only; no dollar level is Anthropic's.

### The H3 qualification (composition)

13. "The excess is carried by Computer & Mathematical tasks, which hold 73, 71 and 65% of the top quartile's usage
    in the three windows and 43, 40 and 36% of the analysis set's." ← `leg_a_*.coverage.dropped_share_q4` 73.06 /
    71.26 / 65.46; `dropped_share_analysis` 42.84 / 39.65 / 35.55.
14. "With Computer & Mathematical tasks excluded and the quartile boundaries kept, the top quartile's automation
    share was 13.0, 10.5 and 11.9 points *below* the bottom quartile's." ← `leg_a_*.D_L` −13.0319 [−13.4680,
    −12.5957], MDE 0.62; −10.4701 [−10.8805, −10.0598], MDE 0.59; −11.8952 [−12.2763, −11.5140], MDE 0.54.
    **Bound:** "with … excluded", never "outside coding, delegation falls with the wage" — the residual top quartile
    is managerial, scientific, engineering and clinical work (6–8 pp of mass) against clerical, educational and
    sales work in the bottom (red-team 2.1); the comparison is of task types and the post says so in the same
    paragraph.
15. "Within SOC major group — averaging the top-minus-bottom difference over the ten (August, November) or nine
    (February) groups that hold tasks in both extreme quartiles, weighted by their usage in those quartiles — the
    difference was −4.2, −1.9 and −6.2 points; those groups carry 80, 80 and 76% of the two quartiles' mass and the
    other twelve or thirteen groups are not identified." ← `leg_b_*.D_L` −4.1989 [−4.7094, −3.6884]; −1.8716
    [−2.4246, −1.3187]; −6.2169 [−6.6923, −5.7415]; `coverage.n_identified` 10 / 10 / 9;
    `identified_mass_share_q1_q4` 80.04 / 80.31 / 75.52.
16. "The pre-registered composition rule therefore fires: on both the SOC-15-excluded and the within-group leg the
    difference loses its sign in every window, and the post reads the relation between delegation on Claude.ai and
    the wage of the work as a mix that travels with wage — coding — rather than as a property of the wage."
    ← `facts.H3_declaration` (k_of_8_fired 6; a 3/3, b 3/3, e 0/2; literal rule agrees). **Bound:** "reads … as",
    not "shows that"; the price mechanism is not refuted (Interpretation table, H3 row).
17. "Removing any single major group other than Computer & Mathematical moves the difference by at most 3.2, 2.3
    and 2.9 points; removing Computer & Mathematical moves it by 14.4, 17.9 and 12.6 — the leave-one-group-out
    series and leg (a) are the same evidence." ← `desc_leave_one_group_out_*.leave_out_15.move` −14.4155 / −17.8556
    / −12.5641 and the next-largest `move`.
18. "Removing the ten largest tasks by usage — one fifth to one quarter of named mass — turns the difference to
    −11.6, −13.1 and −11.4 points." ← `desc_ten_largest_out_*.D` −11.6151 / −13.0770 / −11.4260.
19. "Restricting to work-dominant tasks (work at least half of a task's published use-case cells; 943 and 1,071
    tasks) leaves the difference at 3.7 points in November and 2.8 in February, keeping the sign and at least half
    the size, so the use-case leg does not fire — in November the retained fraction is 0.50 with a contrast interval
    straddling zero, so whether it keeps more or less than half is undetermined; August publishes no use-case facet
    and is untested." ← `leg_e_nov2025.D_L` +3.7160 [+3.2920, +4.1401], `r_L` 0.5032, `D_L_minus_half_D` +0.0233
    [−0.3264, +0.3730]; `leg_e_feb2026.D_L` +2.7916 [+2.2954, +3.2877], `r_L` 4.17. **Bound:** "does not fire" and
    "undetermined", never "the use-case mix does not explain the gradient".
20. "The work share of the bottom quartile's conversations is 33% (November) and 29% (February) against 61% in
    the top; the bottom quartile is 45–56% personal requests." ← `desc_use_case_mix_*` Q1_work 32.80 / 29.05,
    Q4_work 60.82 / 60.54, Q1_personal 44.52 / 56.33.
21. "With the task's work share added to the wage regression, the wage slope moves from +1.78 to −0.06 points per
    $10 in November and from −0.28 to −1.63 in February, at a variance inflation factor of 1.13–1.14." ←
    `desc_slope_work_share_*` (description; in no decision rule).

### Δ_W

22. "Weighting the published automation share by the hourly wage of the work would move it by −0.02 points in
    August (an interval containing zero), +0.84 in November and −0.15 in February — below one point in every
    window, and in the same direction as the quartile gap in one window of three." ← `DeltaW_*.Delta_W` −0.0222
    [−0.0572, +0.0129], MDE 0.050; +0.8352 [+0.8001, +0.8703]; −0.1466 [−0.1836, −0.1097]. **Bound:** the three
    numbers together; "an hourly rate, not a bill" in the same paragraph (`DeltaW_*.notes`).
23. "The published five-pattern automation shares of the analysis set are 51.1, 47.0 and 45.9%; wage-weighted they
    are 51.1, 47.8 and 45.7%." ← `DeltaW_*.unweighted_share` / `.wage_weighted_share`.

### Sample, construction, replication (facts)

24. "The analysis set is the 1,802 / 2,075 / 2,188 named global tasks with a wage and at least one classified
    collaboration cell — 97.2 / 96.2 / 96.5% of named-task usage mass, on 818,673 / 854,432 / 848,716 classified
    conversations; 805 / 1,079 / 1,056 tasks with a wage and no classified cell and 5 / 12 / 12 with a cell and no
    wage are dropped, never zeroed." ← `facts.sample_*`.
25. "The Kish effective number of tasks is 94 / 83 / 126 on the analysis set and 10.6 / 8.9 / 16.4 in the top
    quartile." ← `facts.kish_*.value`, `.by_quartile[3]`.
26. "The wave's own five-pattern automation share reproduces at 51.07 / 46.74 / 45.55% (published 49 / 45 / 44% on
    the all-conversation base) and Anthropic's released regression returns Figure 2.11 exactly (−3.112, partial R²
    0.394, N 111)." ← `facts.replication_*`, `facts.fig211_released_library`.
27. "The two implementations agree to 1.8 × 10⁻¹⁴ points; the bootstrap standard errors are within 0.9% of the
    closed form and cover 95.2–95.3%." ← `facts.second_implementation_agreement`.

### Side-estimates (description, in no decision rule; each cited only beside the primary it qualifies)

31. Leg (a) under the equal-split and modal allocation rules: "−13.7 / −11.1 / −12.4 and −14.1 / −11.4 / −12.6 points"
    ← `facts.A1_allocation_variants_of_the_legs.leg_a_equal_split_fractional`, `.leg_a_modal_holder` (−13.7133 /
    −11.0752 / −12.3739; −14.0697 / −11.3999 / −12.6167). The C7-frame legs: "inside the BLS-EP frame, excluding
    Computer & Mathematical leaves 0.97 / 0.93 / 0.98 of that frame's own difference" ← `facts.C7_legs.leg_a[*].r`
    0.9685 / 0.9267 / 0.9811. Leg (e) on the substantive-cell denominator: "+3.9 and +2.7 points, not firing" ←
    `facts.leg_e_substantive_cell_denominator` +3.8538 [+3.4345, +4.2731] / +2.7392 [+2.2466, +3.2318]. The
    2010-grouping leg table: "the same verdict on the 2010 O*NET-SOC grouping, 6 of 6 leg tests firing" ←
    `facts.leg_table_2010_grouping` (value 6). X7: "keeping the `none` task node moves the wave share from 51.20 to
    51.74% in August and leaves the difference unchanged" ← `facts.X7_none_node_variant`. The P3(b) all-four subset:
    "−4.1 / −1.8 / −6.1 points on the 8 / 9 / 8 groups spanning all four quartiles (the pre-registration expected
    7 / 8 / 6), firing either way" ← `leg_b_*.estimates.D_L_all_four_subset` −4.0541 [−4.5703, −3.5379] / −1.7940
    [−2.3520, −1.2361] / −6.0851 [−6.5615, −5.6087], `n_groups` 8 / 9 / 8. The within-SOC-15 contrast: "inside
    Computer & Mathematical alone the top-minus-bottom difference is −0.1 (interval containing zero), +6.5 and +0.8
    points, on 24 / 23 / 14 bottom-quartile tasks" ← `facts.composition_of_the_top_quartile.within_soc15_contrast`
    −0.1421 [−0.7180, +0.4339] / +6.4656 [+5.8658, +7.0654] / +0.8039 [+0.1631, +1.4447]. The residual quartiles after
    the SOC-15 exclusion: "what is left of the top quartile is 286 / 327 / 355 tasks and 6.1 / 6.5 / 7.8 points of
    usage, with an automation share of 38.7 / 34.8 / 36.0% against 51.7 / 45.2 / 47.9% in the bottom quartile's
    remainder" ← `facts.composition_of_the_top_quartile.residual_after_soc15_exclusion` (Kish 98 / 85 / 83 and
    75 / 57 / 54). **Bound on all of these:** description; none may headline, none is a decision, and the
    within-SOC-15 and residual figures are cited only with the composition reading of sentence 14 (red-team 2.1).

### Exploratory (labelled exploratory; not in any headline, heading, caption title or close)

28. "The `directive` pattern alone is lower in the top quartile in every window (−7.0, −9.5, −9.9 points) while
    `feedback loop` is higher (+8.4, +16.9, +10.6); the positive difference in the automation share is a
    feedback-loop difference." ← `exp_b_pattern_split.directive_*`, `.feedback loop_*`.
29. "On the 1P API the top-minus-bottom difference is negative in every window (−2.4, −2.5, −5.2 points); the API
    is automation-dominant and its February sample includes Claude Code, so this is context, not a replication." ←
    `exp_a_api_surface.D_*`.
30. "Against Job Zone, the ordering by required preparation, the slope is −6.7, −6.0 and −6.8 points per zone." ←
    `exp_c_jobzone.slope_*`.

## Sentences the post may not state

- "Delegation rises with the wage of the work" / "tracks the wage" / "the higher the wage, the more Claude is
  delegated to" — the shares are U-shaped in every window (`desc_quartile_shares_*`) and the slope's sign
  disagrees across windows (`slope_*`); only the top-minus-bottom contrast is positive.
- "A persistent gradient" or "a stable gradient" as a description of the size — 0.67 to 7.39 pp; only the sign
  persists (sentence 6).
- "Claude is delegated more on high-wage work" as a finding about the wage — H3 is declared; the sentence is
  licensed only with "and the excess is carried by Computer & Mathematical tasks" in the same sentence.
- "Outside coding, delegation falls with the wage" as a price statement — leg (a) compares task types (red-team
  2.1); permitted form is sentence 14.
- "Delegated outright" for the automation share, anywhere including the question sentence inherited from BRIEF §1
  — `directive` alone runs the other way in every window (`exp_b_pattern_split`); "outright" belongs to the
  exploratory split only.
- "Weighting by the wage moves the published share by about a tenth of a point per point of gap" — realised
  Δ_W / D is −0.016 / +0.113 / −0.219; the arithmetic holds in November only.
- "The correction is signed and small" — the sign changes across windows and August's interval contains zero.
- "The use-case mix does not explain the gradient" / "composition by use case is ruled out" — leg (e) not firing is
  nothing shown; November sits on the boundary; August is untested.
- "The second wage source disagrees with the first" as a statement about wage sources — C7 does not price the
  computer family (referee item 10); permitted form: "BLS-EP prices about 11% of Computer & Mathematical mass, so
  its rebuild is the SOC-15 exclusion again (−15.6 / −11.9 / −16.7) and is not an independent test."
- "The gradient survives every robustness check" — it does not survive X5, the modal-holder rule, or the ten-largest
  leave-out (`facts.owner_under_robustness`).
- Any number that is not in `results.json` at `698a2f1` (the side-estimates of referee item 12 are now in it; sentence
  31 gives their permitted form).
- "Resolves nothing below about twelve points" — the realised bound is 14–20 (sentence 7).
- Any statement about a country, about the wage bill, about displaced labour, about tasks automated, about AI
  autonomy, or about work in general (prereg "What no outcome may be read as").
- Any probability that the ordered rule would land where it did — the P2 figures assume a constant true D and the
  realised D is not constant (referee item 17); the post may cite the per-wave MDE (0.39–0.40 pp) as the
  within-window resolution and nothing more.
- "Significant" without the test named; "shows", "proves", "demonstrates", "causes".
- Any first-person construction; any summary block.

## Required caveats (same paragraph as the finding)

- **With sentence 1:** sentences 3, 5 and 6; the H3 qualification (13–16) in the same section, before any
  interpretation; the country-mix sentence ("a task's rate is a usage-weighted blend over countries that cannot be
  cleaned at this grain; the geography that can be bounded, Seychelles in November, moves the difference by up to
  three points and does not account for November's excess") ← `facts.country_mix_not_testable`, `rob_X4`, ⟨ref⟩.
- **With sentence 2 (the owner):** sentence 9's owner moves; the C7 sentence in the P6 form given above (first
  sentence of the O-A paragraph, per prereg P6), naming BLS-EP's coverage of SOC-15 as the reason.
- **With sentence 14 (leg (a)):** the residual top quartile's composition and mass (6–8 pp), and that the leg and
  the leave-one-group-out series are one piece of evidence (sentence 17).
- **With sentence 19 (leg (e)):** "nothing shown", the November boundary, August untested, and that the
  work-dominant Q4 is the coding Q4 (81–83% of Q4 mass kept against 20–30% of Q1's).
- **With sentence 22 (Δ_W):** "an hourly rate, not a bill: no hours enter"; the 1 pp materiality line named as the
  brief's, separate from the quartile margin.
- **With every interval:** lower bound under within-task dependence; **with every count:** the Kish N.
- **With any 'delegated':** the definition — directive plus feedback loop over the five classified patterns, the
  `none` share printed beside each quartile (`desc_quartile_shares_*.none_share`) — and Anthropic's bound that
  automation is not autonomy and one dialogue's shape does not show what happened outside the chat.
- **In the close:** sentence 7 (the generalisation bound at fourteen to twenty points) and no number otherwise.

## Title and opening claim

**Title (frozen):** "Is AI delegated more on low-wage work or on high-wage work?" — the evidence supports it *as a
question*, because the answer is two-sided and the post can give both sides with pre-registered numbers. The answer
sentence the close must reach, in words: *on Claude.ai the top wage quartile is delegated somewhat more than the
bottom, and the whole of that excess is coding; set the coding family aside and the top quartile is delegated less.*

**Strongest opening claim the evidence supports** (the editor may shorten, not strengthen):

> In each of three Claude.ai windows between August 2025 and February 2026, conversations on the top quarter of
> tasks by hourly wage were delegated — worked as directive or feedback-loop conversations — at a higher rate than
> conversations on the bottom quarter, by between two thirds of a point and seven points. That excess is carried
> by Computer & Mathematical tasks, which make up two thirds to three quarters of the top quarter's usage; with
> them excluded, the top quarter is delegated ten to thirteen points *less* than the bottom, and within occupational
> groups the difference is negative in every window. The wage of the work is not what orders delegation on
> Claude.ai; the kind of work is.

Bound on the last sentence: "on Claude.ai", "in these windows"; it may not become "the wage does not matter" (the
design cannot separate wage from task type, red-team 2.1) and may not extend to work in general (sentence 7).

**The §12 close the owner selects:** the O-A paragraph of BRIEF §12, with these substitutions required by the
results: "does track the wage of the work, in the direction stated" → "the top wage quartile is delegated more than
the bottom, in every window" (sentence 1 form); "D of X, Y and Z points" → 1.4, 7.4 and 0.7 (and 0.5, 7.2, 0.3 on the
corrected rule); "moves it by roughly a tenth of a point per point of gap, so the direction is the finding and the
correction is not a repair" → "moves it by less than a point in every window and not in a fixed direction, so the
correction is small and the direction is the finding — and the direction is coding" (sentence 22); "resolves nothing
below about twelve points" → "fourteen to twenty". The H3 paragraph follows as written in §12, with "coding" named,
the use-case clause reduced to "the use-case leg does not fire and does not settle it", and no August use-case claim.
The P6 first sentence: "The direction is not corroborated on the second wage source in any window, because BLS-EP
does not price the computer occupations; its rebuild is the coding exclusion again." No number appears in the close
that the body has not carried.

## Limitations a referee would raise first

1. **Composition, not price.** The top quartile is two thirds to three quarters coding; the finding reverses without
   it (legs (a), (b), the ten-largest leave-out). The design cannot separate the wage of the work from the kind of
   work at any grain, since the wage is the wage of the occupation a task resembles. This withdraws the sentence
   "delegation depends on the wage of the work".
2. **The country mix inside a task**, untestable at global grain; Seychelles in November as the one bounded case (up
   to three points on D, not enough to explain November).
3. **Between-window instability of the size** (0.7 to 7.4 pp) against within-window intervals of ±0.3 — the
   intervals are the wrong uncertainty for any statement beyond one window, and no probability of the observed
   outcome under a varying D has been computed.
4. **The top quartile's effective size** — 9 to 16 tasks; three software tasks are half of it; the Q3/Q4 boundary
   sits on one computer occupation's wage and alphabetical order places 5–7 pp of Q4's mass. Threshold at which the
   conclusion flips: the fractional rule takes August below one point; the modal-holder rule takes February below
   zero.
5. **The second wage source is not one.** BLS-EP omits the computer family, so no independent wage source has
   confirmed the sign; none is available while the O\*NET file carries 2010 codes.
6. **The use-case rival** is tested in two windows, sits on the boundary in one, and is untestable in August.
7. **The construct.** "Delegated" is directive plus feedback loop; the two move in opposite directions in wage
   (exploratory), so the finding is a feedback-loop finding; automation is not autonomy and not displaced labour;
   Δ_W is a rate re-weighting with no hours.
8. **The wage level does not reproduce Anthropic's** (task value $35 against $48 on matched windows), which is why
   the design is rank-based and no dollar level is Anthropic's.
9. **The generalisation bound**: as a statement about tasks, nothing below fourteen to twenty points is resolved.
