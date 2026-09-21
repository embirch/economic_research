# Red-team memo · gender1

The strongest case against each finding, written as a referee would, followed by the concession the post must
make. Numbers are from `data/processed/results.json` at `9b54be0` unless marked *(referee)*, in which case they
come from `notes/rederivation/referee_results_gender1_supp.out.txt` and this memo, and the post may use them only
if the analyst adds them to `results.json`. The design is a secondary analysis of published cells with no
standard errors; every point below is a version of that fact.

**Exposure.** Five registered count rules, each run once; one registered exploratory correlation (a second,
unregistered, was also run); no p-value governs any verdict. The smallest samples the claims rest on: a country's
overall gap rests on about 860 (MT) to 15,800 (IT) respondents per sex (95 % SRS half-width 0.9 to 4.7 points, median
2.8); a country-by-age cell on about 110 to 3,000 per sex under the EU age shares (band half-widths 1.4 to 12.6
points); an education cell has no bound at all. The bound is a lower bound under simple random sampling; for AT, BG, HR, RO and SK the published standard
error of the reference indicator exceeds the SRS value by 1.3 to 2.9 times.

## 1. The EU27 gap (men 34.9 %, women 30.5 %; 4.5 points; 3.4 after age standardisation)

*Against.* This is Eurostat's own number restated; the post's addition is the 1.1 points attributed to age
structure, and that attribution depends on (i) the resident population (`demo_pjan`, provisional, flag `ep`)
standing in for the survey's household population, (ii) sex-pooled EU27 weights being the right common structure,
and (iii) reading a difference between two weightings as "the part due to age". Own-sex weights reproduce the
published rates to 0.15 point, so (i) is fair; (ii) is a convention (equal band weights give 3.17, not 3.36);
(iii) is the standard direct-standardisation reading and no more. The measure is any use in three months, as the
respondent understood "generative AI"; it is not intensity, skill or benefit, and Pew's US result (ever-use
converged, daily use not) says participation is the weakest of the gender measures. Fieldwork is early 2025 with
no earlier wave; Henseke (2026) cites Bick et al. (2026) as finding "substantially smaller gender differences in
generative AI use by late 2025", so the gap may already be smaller than the one measured here.

*Concede.* State the 1.1 points as points, never as a share ("a quarter"); name the weights and the provisional
flag; say the sensitivity (equal weights 3.17); say the measure is participation in one quarter of 2025 with no
trend possible, and cite the later-2025 evidence of narrowing as a reason not to carry the number forward.

## 2. The country map and the persistent classes (6 large-gap, 7 small-gap, 13 not distinguishable, IE unclassifiable)

*Against, first form.* The class counts are what sampling noise alone produces. Under a null in which every
country has the same true gap and only its own SRS noise, the joint tercile rule — three re-expressions of the
same cells — classes on average 5 to 6 countries large-gap and 5 to 6 small-gap of 26, and returns 13 or more in
the two persistent classes about half the time *(referee, `_supp` §2; the pre-registration disclosed "about four
and six")*. Agreement across gap, ratio and standardised gap is agreement of a number with itself. The only
information in the table is in the distinguishable marks — DK and PL large-gap, EE, HR, LT and SI small-gap — and
the null produces 0.2 to 0.6 of those per class, so six marks is a real signal; six-and-seven is not.

*Against, second form.* "Reversed" is empty as a class (D1: the four countries reversed on both denominators are
classed small-gap) yet the map will be read as showing five countries where women lead. None of the five female
leads (−1.3 to −1.7 points) exceeds its country's SRS half-width (2.9 to 4.7) *(referee, `.out.txt` §G)*. The
small-gap ● marks mean "further than the half-width from the 2.51 cut", not "distinguishable from zero", and a
reader will take the mark on Estonia's negative bar as the latter. Of the 22 male leads, 17 exceed the country's
half-width; BE, BG, EL, FI and LV do not. So the published map has 17 countries with a male lead the bound
supports, 10 whose sign it does not, and no country with a female lead it supports.

*Against, third form.* Ireland has the highest published value (9.3) and cannot be classed because its 16–24 cells
are flagged; its lead over Denmark (1.5 points) is inside the root-sum-square of their half-widths (4.6). Any
sentence that puts Ireland first is a rank statement the pre-registration forbids.

*Concede.* Report the class table with the null figure beside it and the marks as the finding; name the six marked
countries and no others as classed at the bound; say that five countries publish a female lead and that none of
the five is distinguishable from zero; never rank adjacent countries; report the design-effect list as the
countries where even this bound is loose.

## 3. H-age: women lead at 16–24 in 20 of 26 (8 beyond the band bound); no band holds the largest gap in a majority

*Against (a).* The 16–24 band has the widest bounds (median half-width 7.5; up to 12.6) and the rule's first clause
("smallest of six") is satisfied by noise in one country in six under equal true gaps; the count of 20 is carried
entirely by the second clause — the gap is negative in all 20, and in no country is 16–24 smallest without being
negative *(referee, `_supp` §4)*. The EU27 aggregate (−1.7) was disclosed before the test, so "most countries look
like the aggregate" was the expected result (the pre-registration's own simulation: about 20 of 26 if every
country had the EU27 profile). Twelve of the twenty negatives are inside their band half-width; eight are not.
Six countries run the other way, and one of them is not marginal: Poland's 16–24 gap is +13.8 against a band
half-width of 5.2, the largest male lead in any band in any country in the table. The young are also the band where
the composition the design cannot remove is strongest: at 16–24 use is 63–65 % and is formal-education use for a
large share of it; women's tertiary enrolment lead is the likeliest mechanism, and the data cannot say.

*Against (b).* "Not declared" is nothing shown: the rule's power against the brief's own alternative was 0.5 to 0.8,
and 9 of 26 is the null expectation for two bands of six. The most frequent largest band is 65–74 (9 of 26), where
the bounds are tightest — a pattern the equal-gap null makes *less* likely, not more (P ≈ 0.02 for 9 or more at
one band of six) — and where in relative terms the EU27 gap is by far the widest (women's rate 0.53 of men's
against 0.88–0.91 at 25–54) *(referee; ratios of disclosed EU27 cells)*. The brief's hypothesis was framed in
points; in ratios the "mid-life peak" is not where the gap is largest at all.

*Concede.* Report (a) with the 8 beside the 20 and Poland named as the exception the bound supports; say the
result is the disclosed aggregate reproduced country by country, not a discovery; say (b) is not declared and that
this shows nothing; report the EU27 band ratios beside the point gaps and say the two measures locate the gap in
different bands; say the young band is where formal-education use and enrolment composition dominate.

## 4. H-education: the high-education gap is the largest of three in 14 of 26

*Against.* Fourteen is the minimum majority; the rule was one country from failing, and 14 of 26 has probability
0.025 under the ⅓ null — the least secure of the four "supported/against" verdicts. There is no education-cell
bound, so nothing can be said about which of the 14 would survive noise; if the three education groups were equal
thirds of the sample, their gap half-widths would run from about 2 points (IT) through 4 (NL) to 7.5 (MT) *(referee's
rough figure, not a registered bound)*, against within-country differences between the three gaps that are often
under 2. High is the *smallest* of three in 4 countries; the monotone pattern holds in
8. The EU27 profile (3.8, 4.6, 7.0) was disclosed. Education cannot be age-standardised (no sex-by-age-by-education
cells); the tertiary group is younger among women than among men, and the young band has a reversed gap — which,
if anything, works *against* H-education (it pulls the female tertiary rate up), so the observed gradient is not
an age artefact in the obvious direction, but the post cannot show this either way.

*Concede.* Report 14 of 26 with "the minimum majority", the 0.025 null probability and "no bound exists" in the
same sentence; report the monotone 8 and the 4 reversals; give the medians (3.2 / 4.8 / 7.3 *(referee)*) as the
descriptive gradient the count rule does not carry; name the age composition it cannot remove.

## 5. H-work: the private-use gap exceeds the work-use gap in 23 of 27 countries (9 beyond the bound)

*Against, first form.* The result was near-predetermined. The EU27 purpose gaps (private 5.5, work 3.0) were
disclosed, and every country's purpose gaps were in a committed audit file readable by every role before the
pre-registration; the pre-registration's own expectation if countries resembled the aggregate was "about 2.6 of
27 in favour", and the result is 4. The test confirms the aggregate's sign is general; it does not discover it.

*Against, second form.* The comparison is in points, and points scale with the base rate. Work use is 14–17 % of
adults, private use 23–28 %; equal relative gaps would give a work gap in points about half the private one. In
ratio terms the EU27 gaps are nearly the same (women's rate 0.805 of men's for private, 0.822 for work), and in
10 of 27 countries the work *ratio* shows the larger male lead *(referee, `_supp` §3, an unregistered check)*.
"The gap is in private use, not work" is true of points and not established for relative use.

*Against, third form.* "Work use" here is work use among all adults 16–74, not among workers; a lower female
employment rate lowers the female work-use rate mechanically. Henseke's 4.1 points among workers (13.8 % vs 9.7 %,
EWCS 2024, a broader AI question) is on a different population and is not a comparator. Among AI users the
work-purpose gap is 2.7 points at the EU27 level and positive in 22 of 27 countries, so the male lead in work
purpose is present conditional on use — it is simply smaller than the private one.

*Concede.* Report the verdict with the disclosure; state that the comparison is in points and that ratios do not
separate the two purposes at the EU27 level; state the all-adults population and that no sex-by-employment cell
exists; do not write "the gap is a consumption gap, not a labour-market gap".

## 6. H-composition: standardisation moves 2–3 of 26 across a tercile cut; the ordering survives age structure

*Against.* The rule could not realistically fail. Standardisation shifts every country by −4.0 to +1.0 points
(median −1.3, sd 1.0) across gaps spanning about 9.6 points; if those same shifts were reassigned at random across
countries the expected number of tercile changes is 4.5 and "at most 8" would hold 99 times in 100 *(referee)*.
The registered threshold was set by "one third" with no calibration, and the pre-registration said so ("at this
bound few changes will be"). So "supported" is not evidence that the ordering is robust to age; it is a statement
that the shifts are small relative to the spread of gaps, which the shifts themselves show directly. The
distinguishable count is 0: no tercile change survives the bound, and equally no *stability* is shown at the
bound. The count itself is 2 under the registered text and 3 under the analyst's re-cut (D3).

*What the shifts do show.* Twenty-five of 26 move down: the crude gap overstates the standardised one almost
everywhere because women are older and older bands use less. The largest downward shifts are in the reversed set
(LT −4.0, LV −3.2, EE −3.1): under a common age structure the female leads widen, so the reversals are not an
age-structure artefact. Czechia is the one country that moves up (+0.95) and into the top tercile.

*Concede.* Report the shifts (median, range, 25 of 26 down, the Baltic widening) as the finding and the tercile
count as the registered rule's outcome with "the rule had little chance of failing at shifts of this size" beside
it; give both counts; say nothing about stability "at the bound".

## 7. The internet-user denominator: "little of the gap is an internet-use gap"

*Against.* The registered quantity — gap on `PC_IND` minus gap on `PC_IND_IU3` — is negative in every band at the
EU27 level (−0.25 to −0.98) and in ten countries exceeds a point at 65–74. Read as "composition", that says
internet use works in women's favour, which is false: it is arithmetic. With `r` the internet-use rate of a sex-band,
`gap_IND = r̄ (q_M − q_F) + q̄ (r_M − r_F)`; the first term rescales the internet-user gap by the internet-use rate
(0.79 at 65–74, so a 4.1-point gap becomes 5.1 among internet users), and the second is the internet-use gap by
sex, which at the EU27 level is within ±0.3 in every band because `r_F` and `r_M` are within one point *(referee,
this memo and the verdict, item 12)*. The direction of the registered finding is right — none of the AI gap is a
recent-internet-use gap — and the reason is that recent internet use no longer differs by sex in any band, not that
composition offsets anything.

*Concede.* Report the registered quantity with its definition and say its negative sign is the denominator
rescaling; state the strong form plainly (recent internet use differs by sex by under a point in every band at the
EU27 level, so the AI gap is not an internet-access gap); do not call the values "composition" or "share".

## 8. Triangulation: Spearman −0.17 (N 26) between the Eurostat gap and OpenAI Signals' feminine message share

*Against.* Unregistered p-values were computed and the rank correlation is uninformative in both directions:
Signals measures messages, not people, with name-inferred gender on consumer ChatGPT, within-country shares that
run only 0.455 to 0.594 across the EU26, and June 2025 against fieldwork in Q1 2025. A near-zero Spearman on 26
points neither supports nor contradicts the map. Leg (ii) was not run (D2), so the promised "two independent
sources" is one, and Henseke's Figure 2 is the only country-level gender comparator in the literature.

*Concede.* Report the correlation as exploratory with N and the caveats and no p-value; say leg (ii) was not run
and why; say the post has no external check on the country ordering.

## What a later wave would need to show

A 2026 `isoc_ai_iaiu` wave with the same cells would allow: the trend statement this post cannot make (is the
4.5-point gap narrowing, as Bick et al. report for late 2025?); persistence of the six marked classes (DK, PL; EE,
HR, LT, SI) across two independent samples, which is the noise check the programme requires for any geographic
claim and which one wave cannot provide; whether Poland's young-male lead and the Baltic reversals recur; and, if
Eurostat publishes cell counts or standard errors, a bound that is not a lower bound under SRS. Without the second
wave every country-level statement in the post is a single-sample statement at a loose bound.
