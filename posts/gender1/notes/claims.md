# Claims list · gender1 · written by the referee after verification (2026-09-21; refreshed at acda4f7)

Bound to `posts/gender1/data/processed/results.json` at `acda4f7`, in which every item of `notes/referee-results.md`
and `notes/referee-results-2.md` is applied (D3 logged with both H-composition counts; p-values renamed
not-for-citation; Figure 3 relabelled; `classes.sign_beyond_bound`, `eu27.age_profile_ratio`,
`internet_composition.eu27_decomposition` and `internet_composition.over_one_point_by_band` added; true medians).
Keys are paths in `results.json`. Rounding: rates and gaps to one decimal or to the integer, as the sentence needs;
counts exact. Every "supported" or "against" must carry its distinguishable count in the same sentence
(pre-registration, Hypotheses, first paragraph). "Men" and "women" are the source's categories; "gender gap" is the
framing. Nothing under thirty geographies is a percentage of geographies. No adjacent-rank statement anywhere,
including captions and the site card. Two keys the list asks for are still absent at acda4f7 and are marked
**[key missing]**; a sentence so marked may not appear in the post or in a caption until the key exists.

## Sentences the post may state

### The EU27 reference (disclosed values; not findings of a test)

- "In the three months before their 2025 interview, 35 % of men and 30 % of women aged 16–74 in the EU had used a
  generative-AI tool; the published rates are 34.9 and 30.5, a gap of 4.5 points." ← `eu27.overall` (M 34.91, F
  30.45, gap 4.46); `eu27.published_headline`. Bound: "used a generative-AI tool" or "used generative AI", never
  "adopted", "rely on" or "AI users" as a population; never "in early 2025" or "in the first quarter of 2025" —
  fieldwork ran mostly from late March to early August 2025, in Serbia in February and in Greece from July to
  September (notebook, "frame correction … fieldwork timing"; `notes/crosscheck-independent-draft.md` §4), so the
  reference window is "the three months before the interview", dated 2025 and no more finely.
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
  65–74 (0.53), where use is 4.6 % of women and 8.7 % of men." ← `eu27.age_profile_ratio.{Y16_24,Y65_74}` (1.027,
  0.525), `eu27.age_profile_rates.{Y16_24,Y65_74}` (F/M). The mid-life ratios are 0.91, 0.88, 0.90 at 25–34, 35–44,
  45–54 and 0.77 at 55–64 (`eu27.age_profile_ratio`).
- "By education, the EU27 gap is 3.8 points at low, 4.6 at medium and 7.0 at high attainment." ←
  `eu27.education_profile.*.gap`.

### The country map and the classes

- "Men's published rate exceeds women's in 22 of the 27 member states; in five — Estonia, Croatia, Lithuania,
  Malta and Slovenia — women's does." ← `classes.sign_beyond_bound.male_lead_countries` (22),
  `.female_lead_countries` (5), `classes.reversed_on_pc_ind`, `sets.eu27.N`. **Must be followed in the same
  paragraph by:** "None of the five female leads (1.3 to 1.7 points) exceeds its country's sampling bound; the
  male lead does in 17 of the 22, and in ten countries the published sign is not distinguishable from zero." ←
  `classes.sign_beyond_bound` (male 17, female 0, neither 10); the female leads are `countries.{EE,HR,LT,MT,SI}.
  overall.gap` (−1.56, −1.34, −1.35, −1.71, −1.50) against `countries.*.bound.gap_halfwidth95_pp` (3.15, 3.14,
  2.86, 4.71, 3.55). Bound: "published rate", "at the published rates"; never "women use AI more than men in five
  countries".
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
  ratio to the age-standardised gap, eight under the registered reading (seven if the ratio tercile is re-cut on
  the 26 countries with a standardised gap)." ← `classes.tercile_changes.gap_vs_ratio` (6),
  `.ratio_vs_standardised_registered_reading` (8), `.ratio_vs_standardised_recut_26` (7). Bound: both readings
  or the registered one; never the re-cut alone.
- "In the eight non-EU geographies the median published gap is 4.4 points and North Macedonia publishes a female
  lead; none is placed in a persistent class against the EU27 cut values." ← `sets.extension` (N 8, median 4.365,
  reversed MK), `extension.*.class` (six not distinguishable, MK and RS not classifiable). Bound: extension
  geographies are placed, never ranked among members.

### Age (H-age)

- "At 16–24, women's published rate exceeds men's in 20 of the 26 member states with usable cells; in eight the
  difference exceeds the band's sampling bound." ← `tests.H_age.rule_a.raw` (20), `.distinguishable` (8),
  `tests.H_age.N` (26). Bound: "published rate"; the 20 is also rule (a)'s count, and the post may say rule (a)
  "holds" only with the 8 in the same sentence and with "the EU27 profile, which was known before the test, predicted
  about 20" nearby (pre-registration, H-age, Expected resolution).
- "Poland is the exception the bound supports: a 13.8-point male lead at 16–24 against a band half-width of 5.2."
  ← `countries.PL.bands.Y16_24.gap` (13.80), `countries.PL.bound.bands.Y16_24.gap_halfwidth95_pp` (5.21).
- "From 25 upward men lead in 17 to 22 of the 26 countries, depending on the band." ← per-band positive counts
  (17, 18, 18, 20, 22; referee re-derivation) — **[key missing]** `tests.H_age.men_lead_by_band`. Until the key
  exists the sentence may not appear in the post, and the Figure 2 caption, which carries it now, is bound to the
  same rule.
- "No single age band holds the largest gap in a majority of countries: the largest gap lies at 25–34 or 35–44 in
  9 of 26, at 65–74 in 9, and elsewhere in 8. The registered rule for a mid-life peak is not declared, and, at
  the sampling bound, that shows nothing: the rule had power of about one half to four fifths against the EU27
  profile." ← `tests.H_age.rule_b.raw` (9), `.distinguishable` (1), `tests.H_age.verdict` ("partly declared");
  the 65–74 count of 9 and "no single band … majority" are **[key missing]** `tests.H_age.largest_band_counts`
  (referee re-derivation: 2, 5, 4, 3, 3, 9 by band). Bound: "not declared" and "shows nothing" together; never
  "mid-life is not where the gap is".

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
- "Under an even split, 19 or more of 27 in favour, or 23 or more against, each arises with one-sided probability
  0.026; the realised 23 of 27 against has probability 0.0002." ← `tests.H_work.reading`,
  `.one_sided_probability_of_realised_count_under_even_split` (0.000155).
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
  `tests.H_composition.median_change_pp` (−1.31, the true median; say "about 1.3"). Bound: points only; never a
  share.
- "Two countries change tercile between the crude and the standardised gap under the registered reading of the
  rule (Czechia, Latvia), three if the crude tercile is re-cut on the 26 countries with a standardised gap (adding
  France); none of the changes exceeds the sampling bound. The registered rule — at most eight changes — is
  supported, and at shifts of this size it had little chance of failing." ←
  `tests.H_composition.tercile_changes_registered_reading` (2), `.changed_registered_reading` (CZ, LV),
  `.tercile_changes` (3), `.changed` (CZ, FR, LV), `.distinguishable_changes` (0), `.raw_verdict` ("supported");
  the same two counts sit in `classes.tercile_changes.crude_vs_standardised_registered_reading` (2) and
  `.crude_vs_standardised_analyst_reading` (3); D3 in `deviations`. Bound: both counts in one sentence, the
  registered 2 first or beside the 3; "the ordering survives age structure" only as "the tercile ordering changes
  for two or three of 26"; never "the ranking is robust".

### Denominators

- "Measuring among recent internet users instead of all individuals changes the gap by under a point at the median
  in every age band; the change exceeds a point in ten countries at 65–74 and in five or fewer in every other band."
  ← `internet_composition.band_medians` (0.00 at 16–24 to −0.87 at 65–74), `internet_composition.N` (26),
  `internet_composition.over_one_point_by_band` (3, 1, 2, 1, 5, 10). **Must carry:** "The difference is negative
  because a gap among a base that includes non-users is smaller in points than the same gap among internet users
  alone; it is a rescaling, not a composition effect." ← `internet_composition.reading`. Bound: never "internet
  composition favours women", never "share" or "part of the gap that is an internet-use gap" for the negative
  values.
- "At the EU27 level the implied share of recent internet users differs between women and men by at most 1.1 points
  in any age band — 92.6 % of women and 91.5 % of men at 55–64, 78.6 and 79.6 % at 65–74, above 96 % of both
  sexes below 55 — and that difference moves the gap by under 0.3 points in every band, so the gap in generative-AI
  use is not a gap in recent internet use." ← `internet_composition.eu27_decomposition.*.implied_internet_use_F`,
  `.implied_internet_use_M` (55–64: 0.9261 / 0.9152; 65–74: 0.7856 / 0.7963), `.internet_use_gap_term` (−0.27 at
  16–24 to +0.09 at 65–74), `.rescaling_term` (−1.07 at 65–74); `internet_composition.reading`. Bound: "at most
  1.1 points", never "within a point" or "no difference"; "recent internet use", never "internet access"; the
  two terms sum to the registered share in every band (the identity is exact), and the post may say so.

### Triangulation

- "Across the 26 member states with a June 2025 value, the Spearman correlation between the Eurostat gap and OpenAI
  Signals' feminine share of ChatGPT messages is −0.17; the shares themselves span 0.46 to 0.59. The correlation is
  exploratory and shows no agreement in either direction." ← `triangulation.leg_i.spearman_gap_vs_feminine_share`
  (−0.174), `.N` (26), `.missing_eu27` (MT). Bound: no p-value (`scipy_p_not_for_citation_*` may not be cited); the
  ratio correlation (`spearman_ratio_vs_feminine_share_UNREGISTERED_ADDITION`, 0.04) may be named only as an
  unregistered addition (D4); the caveats key verbatim (name-inferred gender, messages not people, consumer
  ChatGPT, within-country share). "The second registered leg, Henseke's country gaps, was not run: the paper
  publishes them only as a figure." ← `triangulation.leg_ii`.

### Reproducibility and bound

- "Every gap, ratio, standardised rate, tercile, class, mark and hypothesis count was computed twice from the
  published file and agrees to 1e-9 (293 quantities); the referee's independent re-derivation reproduces every
  headline count." ← `second_implementation` (checked 293, max_abs_difference 0.0);
  `notes/rederivation/referee_results_gender1.out.txt` (185 of 186; the one mismatch, the cut label, fixed at
  a13ac3e as `classes.cuts.gap_27` / `.crude_26`).
- "The only uncertainty statement is a lower bound: under simple random sampling with the national net sample
  split equally by sex, the 95 % half-width of a country's overall gap has a median of 2.8 points (0.9 in Italy,
  4.7 in Malta) and, within an age band, medians of 7.8 points at 16–24 down to 3.7 at 65–74. For Austria,
  Bulgaria, Croatia, Romania and Slovakia the published error on Eurostat's reference indicator exceeds this bound
  by 1.3 to 2.9 times." ← `bound.class_rule.*` (median 2.8, min 0.88, max 4.71; by band 7.78 … 3.67),
  `bound.design_effect_check.above_1_3` (AT 1.32, BG 1.76, HR 1.34, RO 2.90, SK 1.31; BA, CH, RS, TR are also
  listed and are extension geographies).
- "No overall pair has a value carrying Eurostat's low-reliability flag, so the flagged-cell appendix is empty." ←
  `flagged_appendix_rows` (0).

## Sentences the post may not state

- "Women use generative AI less than men in every EU country but five" / "women lead in five countries" — the sign
  is not distinguishable from zero in ten countries and in none of the five reversed ones.
- "In early 2025" / "in the first quarter of 2025" / any sentence that places the 27 countries' reference windows in
  one calendar quarter — fieldwork ran mostly from late March to early August 2025, in Serbia in February and in
  Greece from July to September; "recent use" is a different three-month window in different countries.
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
  values — rescaling. "Recent internet use does not differ by sex" / "within a point" — it differs by up to 1.1
  points at 55–64 and 65–74.
- "The gap is closing" / "narrowing" / any trend — one wave.
- Any p-value, "significant", "confidence interval", or "statistically" — none is registered; the
  `scipy_p_not_for_citation_*` values must not appear.
- "Women are less confident", "training would close the gap", "education causes the difference", "AI is widening
  the wage gap", "equal uptake implies equal benefits", "this country is the worst" — brief §16.
- Anything about Claude, Anthropic's Economic Index or occupational exposure by sex — the data carry no sex within
  occupation and the Index carries no sex; the post may say so as a limitation, not as a finding.

## Required caveats (same paragraph as the finding)

1. EU27 gap and standardisation: participation in the three months before a 2025 interview, with fieldwork mostly
   late March to early August (Serbia February, Greece July to September), so no single quarter and no trend;
   points not shares; weights named and provisional; later-2025 evidence of narrowing (Bick et al. 2026, via
   Henseke 2026) cited as a reason not to carry the number forward.
2. Country map: the sign-beyond-bound counts (17 male, 0 female, 10 neither); the null figure for the class
   counts; the six marked countries as the only classed-at-the-bound set; the design-effect countries; no ranks;
   the country comparison is not a common calendar window.
3. H-age (a): the 8 beside the 20; the disclosed EU27 profile predicted about 20; Poland named. H-age (b): "not
   declared" with "shows nothing" and the power range. The band ratios (`eu27.age_profile_ratio`) beside the point
   gaps.
4. H-education: minimum majority, 0.025, no bound, monotone 8, reversed 4 — in one sentence or two adjacent ones.
5. H-work: the disclosure; points versus ratios with the base rates; all adults not workers.
6. H-composition: both counts (2 registered, 3 re-cut); "little chance of failing"; the shifts as the finding; 25 of
   26 down; the Baltic widening.
7. Internet denominator: rescaling, not composition; the implied-use difference stated as "at most 1.1 points",
   the term as "under 0.3 points".
8. Triangulation: exploratory, N, caveats, no p-value, leg (ii) not run, the ratio correlation unregistered.
9. Everywhere: the bound is a lower bound under SRS; Eurostat publishes no standard errors, counts or design
   variables; what Eurostat would need to publish for a country ranking to be supportable.

## Title and opening claim

**Title (the strongest the evidence supports; the editor may shorten, not strengthen):**
"Where is Europe's gender gap in generative AI use, and how much of it is measurement?"

**Opening claim:**
"In 2025, 35 % of men and 30 % of women in the EU had used generative AI in the three months before they were
interviewed. About one point of that 4.5-point gap is the two sexes' different age structures; the rest survives
every measurement choice tested here — the ratio in place of the difference, internet users in place of all adults,
a common age structure in place of each country's own. Below the EU average the gap is larger in private than in
work use in 23 of 27 countries, and it is absent or reversed among 16-to-24-year-olds at the published rates in 20 of
26. What the published cells cannot support is a country ranking: at a lower bound on sampling error, two countries
can be called large-gap and four small-gap, and for the other twenty-one no class survives the bound."

Every number in the opening is bound above; "survives every measurement choice tested here" is permitted because
the EU27 gap on `PC_IND_IU3` is 4.7 (`eu27.internet_users`), the ratio 0.87 (`eu27.overall.ratio`) and the
standardised gap 3.4 all keep the sign and the order of magnitude — the editor must not extend it to country-level
stability. "In 2025" may not become "in early 2025".

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
7. One wave and no common calendar window: fieldwork ran mostly from late March to early August 2025, in Serbia in
   February, in Greece from July to September, and Denmark's tables refer to August to December, so "the three
   months before the interview" is a different window in different countries and the country comparison mixes
   them; the pre-registration's "first quarter" frame was the ESMS convention, not the practice (notebook;
   `notes/crosscheck-independent-draft.md` §4). No trend; evidence elsewhere of narrowing later in 2025.
8. The internet-composition quantity is a rescaling; the strong form (the implied share of recent internet users
   differs by sex by at most 1.1 points in any band, moving the gap by under 0.3) is now in
   `internet_composition.eu27_decomposition` and must be stated with those two numbers, not as "no difference".
9. One exploratory triangulation leg only, uninformative; the other not run; a second, unregistered correlation
   was run and adds nothing citable.
10. What generalises: Eurostat's household survey of the EU27 in 2025; the source's female/male categories; not
    intensity, skill or benefit; nothing about Claude or any single provider.
