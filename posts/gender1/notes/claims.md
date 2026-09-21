# Claims list · gender1 · written by the referee after verification (2026-09-21)

Bound to `posts/gender1/data/processed/results.json` at `9b54be0`, with the three blocking changes of
`notes/referee-results.md` assumed applied (D3 logged with both H-composition counts; p-values removed; Figure 3
relabelled). Keys are paths in `results.json`. Rounding: rates and gaps to one decimal or to the integer, as the
sentence needs; counts exact. Every "supported" or "against" must carry its distinguishable count in the same
sentence (pre-registration, Hypotheses, first paragraph). "Men" and "women" are the source's categories; "gender
gap" is the framing. Nothing under thirty geographies is a percentage of geographies. No adjacent-rank statement
anywhere, including captions and the site card.

## Sentences the post may state

### The EU27 reference (disclosed values; not findings of a test)

- "In the three months before their 2025 interview, 35 % of men and 30 % of women aged 16–74 in the EU had used a
  generative-AI tool; the published rates are 34.9 and 30.5, a gap of 4.5 points." ← `eu27.overall` (M 34.91, F
  30.45, gap 4.46); `eu27.published_headline`. Bound: "used a generative-AI tool" or "used generative AI", never
  "adopted", "rely on" or "AI users" as a population.
- "Under the EU27's own age structure applied to both sexes the gap is 3.4 points; about 1.1 points of the
  published 4.5 is the two sexes' different age structures." ← `eu27.standardised.std_gap` (3.36),
  `change_pp` (−1.10). Bound: points only; never "a quarter of the gap" or any share; name the weights (`demo_pjan`
  2025, sex-pooled, provisional) in the same paragraph; the equal-weight sensitivity (3.17,
  `eu27.standardised.equal_weights_gap`) may be given as a sensitivity, never as the standardisation.
- "The gap is 5.5 points for private use, 3.0 for work and 0.05 for formal education, all as shares of all
  individuals." ← `eu27.purposes_participation.{private,work,education}.gap` (5.51, 3.00, 0.05).
- "Among people who used generative AI, 30.5 % of women and 26.8 % of men used it for formal education; for private
  use the figures are 74.7 and 81.0 %, for work 45.6 and 48.3 %." ← `eu27.purposes_among_users.*` (F/M).
- "By age, the EU27 gap is −1.7 points at 16–24 (women ahead), then 4.7, 4.8, 2.8, 4.2 and 4.1 at the five older
  bands." ← `eu27.age_profile_gap`.
- "In relative terms the EU27 gap is closest to parity at 16–24 (women's rate 1.03 times men's) and widest at
  65–74 (0.53), where use is 4.6 % of women and 8.7 % of men." ← `eu27.age_profile_rates.{Y16_24,Y65_74}` (F/M),
  **once the analyst adds `eu27.age_profile_ratio`** (verdict item 14); until then the ratios may not appear.
- "By education, the EU27 gap is 3.8 points at low, 4.6 at medium and 7.0 at high attainment." ←
  `eu27.education_profile.*.gap`.

### The country map and the classes

- "Men's published rate exceeds women's in 22 of the 27 member states; in five — Estonia, Croatia, Lithuania,
  Malta and Slovenia — women's does." ← `classes.reversed_on_pc_ind` (5), `sets.eu27.N`. **Must be followed in the
  same paragraph by:** "None of the five female leads (1.3 to 1.7 points) exceeds its country's sampling bound; the
  male lead does in 17 of the 22." ← `countries.*.overall.gap` against `countries.*.bound.gap_halfwidth95_pp`,
  **once the analyst adds `classes.sign_beyond_bound`** (verdict item 5). Bound: "published rate", "at the published
  rates"; never "women use AI more than men in five countries".
- "The published gaps run from −1.7 (Malta) to +9.3 points (Ireland); the median member state's gap is 3.6." ←
  `countries.MT.overall.gap`, `countries.IE.overall.gap`, `sets.eu27.median` (3.57). Bound: a range and a median,
  not a ranking; Ireland may be named as the highest published value only with "not distinguishable from Denmark's
  or Poland's at the bound, and not classifiable because its 16–24 cells are flagged" in the same sentence.
- "Under the registered rule six countries are large-gap on all three measures — Germany, Denmark, Hungary,
  Poland, Sweden, Slovakia — and seven small-gap — Belgium, Estonia, Croatia, Lithuania, Malta, Portugal,
  Slovenia; thirteen sit in different terciles on different measures; Ireland cannot be classed." ←
  `classes.counts`, `classes.large_gap`, `classes.small_gap`, `classes.not_classifiable`. **Must carry in the same
  paragraph:** "Only two of the six and four of the seven — Denmark and Poland; Estonia, Croatia, Lithuania and
  Slovenia — are further from the tercile cut than their sampling bound; a table of 26 countries with one common
  true gap would show about five or six in each persistent class by noise alone." ←
  `classes.counts_distinguishable` (2, 4); the null figure is the pre-registration's disclosed "about four and six"
  or the referee's 5–6 (`_supp` §2) — cite the pre-registration's unless the analyst adds a simulation key.
- "Four of the small-gap countries — Estonia, Croatia, Malta, Slovenia — publish a female lead on both the
  all-individual and the internet-user denominator; Lithuania on the first only." ←
  `classes.reversed_on_both_denominators`, `classes.reversed_on_pc_ind`. Bound: "publish a female lead", with the
  bound sentence above already given.
- "Switching from points to the ratio of women's to men's rate moves six countries across a tercile cut; from the
  ratio to the age-standardised gap, eight." ← `classes.tercile_changes.gap_vs_ratio` (6),
  `ratio_vs_standardised` (8; state which reading, verdict item 2).
- "In the eight non-EU geographies the median published gap is 4.6 points and North Macedonia publishes a female
  lead; none is placed in a persistent class against the EU27 cut values." ← `sets.extension` (N 8, median 4.65,
  reversed MK), `extension.*.class`. Bound: extension geographies are placed, never ranked among members.

### Age (H-age)

- "At 16–24, women's published rate exceeds men's in 20 of the 26 member states with usable cells; in eight the
  difference exceeds the band's sampling bound." ← `tests.H_age.rule_a.raw` (20), `.distinguishable` (8),
  `tests.H_age.N` (26). Bound: "published rate"; the 20 is also rule (a)'s count, and the post may say rule (a)
  "holds" only with the 8 in the same sentence and with "the EU27 profile, which was known before the test, predicted
  about 20" nearby (pre-registration, H-age, Expected resolution).
- "Poland is the exception the bound supports: a 13.8-point male lead at 16–24 against a band half-width of 5.2."
  ← `countries.PL.bands.Y16_24.gap`, `countries.PL.bound.bands.Y16_24.gap_halfwidth95_pp`.
- "From 25 upward men lead in 17 to 22 of the 26 countries, depending on the band." ← per-band positive counts
  (17, 18, 18, 20, 22) — **not in `results.json`**; the analyst must add `tests.H_age.men_lead_by_band` or the
  sentence is dropped from the post (it may stay in the Figure 2 caption only if the key is added, since captions
  are bound too).
- "No single age band holds the largest gap in a majority of countries: the largest gap lies at 25–34 or 35–44 in
  9 of 26, at 65–74 in 9, and elsewhere in 8. The registered rule for a mid-life peak is not declared, and, at
  the sampling bound, that shows nothing: the rule had power of about one half to four fifths against the EU27
  profile." ← `tests.H_age.rule_b.raw` (9), `.distinguishable` (1), `tests.H_age.verdict` ("partly declared");
  the 65–74 count of 9 requires `tests.H_age.largest_band_counts` to be added. Bound: "not declared" and "shows
  nothing" together; never "mid-life is not where the gap is".

### Education (H-education)

- "The high-attainment gap is the largest of the three in 14 of the 26 member states with usable cells — the
  smallest possible majority, which three equal true gaps would produce with probability 0.025 — and the pattern
  is monotone (low < medium < high) in eight. No sampling bound exists for education cells, so no distinguishable
  count can be given." ← `tests.H_education.high_is_largest` (14), `.N` (26), `.monotone_low_lt_med_lt_high`
  (8), `.distinguishable` (null); the 0.025 is the pre-registration's registered null figure. Bound: "supported on
  the raw count" only with all of the above in the same sentence or the next; never "the gap widens with education
  in most countries" (the monotone count is 8).
- "Education cannot be age-standardised: no sex-by-age-by-education cell is published, and the tertiary group is
  younger among women than among men." — a stated limitation, no number.

### Purposes (H-work)

- "In 23 of 27 member states the private-use gap exceeds the work-use gap, and in nine the difference exceeds the
  sampling bound for a difference of two gaps; in no country is the reverse distinguishable. The registered
  hypothesis that the gap is larger in work use is against, at 4 of 27 in favour (0 distinguishable)." ←
  `tests.H_work.raw_favour` (4), `.N` (27), `.distinguishable_favour` (0), `.distinguishable_against` (9),
  `.verdict` ("against"). **Must carry, same paragraph:** (i) "The EU27 purpose gaps, and every country's, were
  readable before the pre-registration; the test confirms the aggregate country by country rather than discovering
  it" (pre-registration, Disclosure); (ii) "The comparison is in points; work use is 14–17 % of adults against
  23–28 % for private use, and in ratio terms the EU27 gaps are close (0.81 and 0.82)" ←
  `eu27.purposes_participation.{work,private}` (F, M, ratio); (iii) "'Work use' is work use among all adults
  16–74, not among the employed; no sex-by-employment cell exists."
- "Under an even split, 23 or more of 27 the same way arises with probability 0.026 or less." ← the
  pre-registration's 19-of-27 threshold read symmetrically (verdict item 10; the notebook must carry the clause).
- "Among generative-AI users the work-purpose gap is positive in 22 of 27 countries and the private-purpose gap in
  25; the work gap exceeds the private one in 7 of 27." ← `purposes.work.among_users.positive` (22),
  `purposes.private.among_users.positive` (25), `tests.H_work.among_users_favour` (7). Bound: "conditional on use".
- "For formal education the published gap runs the other way in 21 of 27 countries as a share of all individuals
  and in 26 of 27 as a share of users." ← `purposes.education.participation.negative` (21),
  `purposes.education.among_users.negative` (26). Bound: "published gap"; no bound exists for purpose cells beyond
  the overall one, so no distinguishable count; never "women use AI for study more than men do" as a population
  statement without "at the published rates".

### Age structure (H-composition)

- "Applying the EU27 age structure to every country lowers the published gap in 25 of 26 — by a median 1.3 points,
  by 3 to 4 in Lithuania, Latvia and Estonia, where the female lead widens — and raises it only in Czechia." ←
  `countries.*.standardised.change_pp` (25 negative; LT −4.03, LV −3.19, EE −3.11, CZ +0.95),
  `tests.H_composition.median_change_pp` (−1.30, an upper median; say "about 1.3"). Bound: points only; never a
  share.
- "Two countries change tercile between the crude and the standardised gap under the registered reading of the
  rule (Czechia, Latvia), three if the crude tercile is re-cut on the 26 countries with a standardised gap (adding
  France); none of the changes exceeds the sampling bound. The registered rule — at most eight changes — is
  supported, and at shifts of this size it had little chance of failing." ← `tests.H_composition.tercile_changes`
  (3), `.changed`, `.distinguishable_changes` (0), `.raw_verdict`, and `tercile_changes_registered_reading` (2) once
  added (D3). Bound: both counts in one sentence; "the ordering survives age structure" only as "the tercile
  ordering changes for two or three of 26"; never "the ranking is robust".

### Denominators

- "Measuring among recent internet users instead of all individuals changes the gap by under a point at the median
  in every age band; the change exceeds a point in ten countries at 65–74 and in five or fewer in every other band."
  ← `internet_composition.band_medians` (0.00 to −0.82), `internet_composition.N` (26); the per-band counts (3, 1,
  2, 1, 5, 10) require a key `internet_composition.over_one_point_by_band` to be added. **Must carry:** "The
  difference is negative because a gap among a base that includes non-users is smaller in points than the same gap
  among internet users alone; it is a rescaling, not a composition effect." Bound: never "internet composition
  favours women", never "share" or "part of the gap that is an internet-use gap" for the negative values.
- "At the EU27 level recent internet use differs between women and men by under a point in every band, so the AI
  gap is not an internet-access gap." — permitted **only if** the analyst adds the implied internet-use rates
  (`p_IND / p_IU3` by sex and band) to `results.json` (verdict item 12); otherwise the post states the registered
  quantity alone.

### Triangulation

- "Across the 26 member states with a June 2025 value, the Spearman correlation between the Eurostat gap and OpenAI
  Signals' feminine share of ChatGPT messages is −0.17; the shares themselves span 0.46 to 0.59. The correlation is
  exploratory and shows no agreement in either direction." ← `triangulation.leg_i.spearman_gap_vs_feminine_share`
  (−0.174), `.N` (26), `.missing_eu27` (MT). Bound: no p-value; the caveats key verbatim (name-inferred gender,
  messages not people, consumer ChatGPT, within-country share). "The second registered leg, Henseke's country
  gaps, was not run: the paper publishes them only as a figure." ← `triangulation.leg_ii`.

### Reproducibility and bound

- "Every quantity was computed twice from the published file and agrees to 1e-9; the referee's independent
  re-derivation reproduces every headline count." ← `second_implementation` (236 checked, max difference 0.0);
  `notes/rederivation/referee_results_gender1.out.txt`.
- "The only uncertainty statement is a lower bound: under simple random sampling with the national net sample
  split equally by sex, the 95 % half-width of a country's overall gap has a median of 2.8 points (0.9 in Italy,
  4.7 in Malta) and, within an age band, medians of 7.8 points at 16–24 down to 3.7 at 65–74. For Austria,
  Bulgaria, Croatia, Romania and Slovakia the published error on Eurostat's reference indicator exceeds this bound
  by 1.3 to 2.9 times." ← `bound.class_rule.*`, `bound.design_effect_check.above_1_3` and the ratios.
- "No overall pair has a value carrying Eurostat's low-reliability flag, so the flagged-cell appendix is empty." ←
  `flagged_appendix_rows` (0).

## Sentences the post may not state

- "Women use generative AI less than men in every EU country but five" / "women lead in five countries" — the sign
  is not distinguishable from zero in ten countries and in none of the five reversed ones.
- "Ireland has the largest gender gap in Europe" or any adjacent-rank sentence (Ireland–Denmark, Denmark–Poland,
  Malta–Estonia…) — forbidden by the pre-registration and inside the root-sum-square of the half-widths.
- "Thirteen countries have a stable class" or "six large-gap and seven small-gap countries" as findings about
  heterogeneity — the counts are what one common gap plus noise produces; only the six marked countries are findings.
- "The gap is concentrated in work" / "in mid-life" / "is a labour-market gap" / "is a consumption gap, not a
  labour-market gap" — H-work is against in points and unresolved in ratios; H-age (b) shows nothing; no
  sex-by-employment cell exists.
- "The gap widens with education" — the monotone count is 8 of 26; "high is largest" holds at the minimum majority
  with no bound.
- "Age structure explains a quarter of the gap" or any percentage explained — points only, by rule.
- "The country ranking is robust to age standardisation" / "stable at the bound" — the tercile rule could not
  realistically fail and no change or stability is shown at the bound.
- "Internet composition works in women's favour" / "part of the gap is an internet-use gap" for the negative
  values — rescaling.
- "The gap is closing" / "narrowing" / any trend — one wave.
- Any p-value, "significant", "confidence interval", or "statistically" — none is registered; the Spearman
  p-values must not appear.
- "Women are less confident", "training would close the gap", "education causes the difference", "AI is widening
  the wage gap", "equal uptake implies equal benefits", "this country is the worst" — brief §16.
- Anything about Claude, Anthropic's Economic Index or occupational exposure by sex — the data carry no sex within
  occupation and the Index carries no sex; the post may say so as a limitation, not as a finding.

## Required caveats (same paragraph as the finding)

1. EU27 gap and standardisation: participation in one quarter of 2025, no trend; points not shares; weights named
   and provisional; later-2025 evidence of narrowing (Bick et al. 2026, via Henseke 2026) cited as a reason not to
   carry the number forward.
2. Country map: the sign-beyond-bound counts (17 male, 0 female, 10 neither); the null figure for the class
   counts; the six marked countries as the only classed-at-the-bound set; the design-effect countries; no ranks.
3. H-age (a): the 8 beside the 20; the disclosed EU27 profile predicted about 20; Poland named. H-age (b): "not
   declared" with "shows nothing" and the power range. The band ratios beside the point gaps if the key is added.
4. H-education: minimum majority, 0.025, no bound, monotone 8, reversed 4 — in one sentence or two adjacent ones.
5. H-work: the disclosure; points versus ratios with the base rates; all adults not workers.
6. H-composition: both counts; "little chance of failing"; the shifts as the finding; 25 of 26 down; the Baltic
   widening.
7. Internet denominator: rescaling, not composition.
8. Triangulation: exploratory, N, caveats, no p-value, leg (ii) not run.
9. Everywhere: the bound is a lower bound under SRS; Eurostat publishes no standard errors, counts or design
   variables; what Eurostat would need to publish for a country ranking to be supportable.

## Title and opening claim

**Title (the strongest the evidence supports; the editor may shorten, not strengthen):**
"Where is Europe's gender gap in generative AI use, and how much of it is measurement?"

**Opening claim:**
"In early 2025, 35 % of men and 30 % of women in the EU had used generative AI in the previous three months. About
one point of that 4.5-point gap is the two sexes' different age structures; the rest survives every measurement
choice tested here — the ratio in place of the difference, internet users in place of all adults, a common age
structure in place of each country's own. Below the EU average the gap is larger in private than in work use in 23
of 27 countries, and it is absent or reversed among 16-to-24-year-olds at the published rates in 20 of 26. What the
published cells cannot support is a country ranking: at a lower bound on sampling error, two countries can be
called large-gap and four small-gap, and for the other twenty-one no class survives the bound."

Every number in the opening is bound above; "survives every measurement choice tested here" is permitted because
the EU27 gap on `PC_IND_IU3` is 4.7, the ratio 0.87 and the standardised gap 3.4 all keep the sign and the order of
magnitude — the editor must not extend it to country-level stability.

## Limitations a referee would raise first

1. No standard errors: the bound is a lower bound under SRS and equal sex split, loose for five members; every
   country-level statement is a single-sample statement; ten of 27 signs are not distinguishable from zero.
2. The class counts are indistinguishable from noise under one common gap; only six marks carry information; the
   ratio and standardised measures are the same cells re-expressed.
3. Disclosure: the H-work country inputs and every overall gap were readable before the pre-registration; the
   EU27 profiles predicted H-age (a) and H-work.
4. Points versus ratios: H-work's verdict is a points verdict; the age band with the widest relative gap (65–74)
   is not the one the brief's hypothesis named.
5. Composition the design cannot remove: employment, occupation, enrolment; "work use" is among all adults;
   education cannot be age-standardised.
6. H-education at the minimum majority with no bound; H-composition's rule with no realistic chance of failing;
   H-age (b) with power 0.5–0.8.
7. One wave, fieldwork Q1 2025, no trend; evidence elsewhere of narrowing later in 2025.
8. The internet-composition quantity is a rescaling; the strong form (no sex gap in recent internet use) is the
   referee's decomposition and needs its own key.
9. One exploratory triangulation leg only, uninformative; the other not run.
10. What generalises: Eurostat's household survey of the EU27 in 2025; the source's female/male categories; not
    intensity, skill or benefit; nothing about Claude or any single provider.
