# Pre-registration · gender1 · "Where is the gender gap in generative AI use widest, and how much of that is measurement?"

**Date written.** 21 September 2026, after `scripts/01_sampling_bound.py` and before any country-level gap, ratio, purpose-by-age, education-by-country or standardised value is computed. **Revision 2**, after the referee's BLOCK verdict on revision 1 (`notes/referee-prereg.md`, content aef0b5d at 3d4ae45); every item applied, listed in `notes/lab-notebook.md`. **Committed as** ⟨the hash of the commit carrying this file; content hash recorded in the commit message⟩. Review of the brief: `notes/brief-review.md`. Brief: `posts/gender1/BRIEF.md` v1.1 (Gate 1b approved by the human, 21 September 2026; §4's ratio direction corrected to match §7, see notebook). Data profile: `data/releases/eurostat_isoc_ai_iaiu.md`.

## Disclosure: what has already been seen

**Seen by the human's assistant during the audit and the brief review, and declared in BRIEF §12:** the EU27 purpose gaps on the all-individual denominator (overall 4.5; private 5.5; work 3.0; education 0.05 points); the EU27 education-purpose share among AI users (30.5% of women, 26.8% of men); the EU27 age profile of the overall gap (−1.7 at 16–24; 4.7, 4.8, 2.8, 4.2, 4.1 at the five older bands); the EU27 education profile (3.8, 4.6, 7.0 points); the distribution of the overall 16–74 gap across the 36 geographies (median 4.0; range −3.8 to +9.3; six reversed: MK, MT, EE, SI, LT, HR; the three highest IE, DK, RS); the both-sex overall rates by country (Eurostat's published headline figures); and age-cell completeness (33 of 36 geographies; IE, MK, RS incomplete).

**Seen by script 01, this document's author:** the national sample sizes (`data/processed/national_sample_sizes_2025.csv`), the country both-sex overall rates (`overall_rate_pct` in `power_rules.json`), the EU27 both-sex band rates (63.8, 50.7, 39.0, 28.4, 16.5, 6.5), the EU27 2025 age weights (0.131, 0.158, 0.179, 0.189, 0.188, 0.155), and the sampling bound per country and per band (`data/processed/power_rules.json`).

**Committed by the audit and readable by every role:** `outputs/audit/isoc_ai_iaiu_gender_pairs.csv` (396 rows: 36 geographies by 11 indicator-by-denominator combinations; columns `geo, indic_is, unit, F, M, M_minus_F_pp`). Every overall (16–74) female rate, male rate and gap for all four indicators on all three denominators, in all 36 geographies, is in that file; all of it is treated as seen. This touches H-work's country inputs (reported with that caveat; referee item 5), the class rule's reversed leg on `PC_IND_IU3`, and the purpose-among-users comparison; it does not touch any band, education or standardised quantity.

**Seen by the referee at the pre-registration review, EU27 level only, excluded from tests as all EU27 values are:** the EU27 standardised gap with pooled demo_pjan weights, 3.36 points against a crude 4.46 (own-sex weights reproduce the published rates to 0.15 point). No country-level standardised value has been computed by anyone.

**Not seen by anyone:** any country-by-age gap; any country-by-education gap; any purpose gap by age; any ratio; any country-level standardised value; any internet-user or AI-user denominator value below the EU27 aggregate other than in the committed audit file above; either triangulation leg.

## Definitions, fixed

### 1 · Outcome cells

The published percentage `Value` in Eurostat table `isoc_ai_iaiu` (official TSV of 21 September 2026, `data/cache/eurostat/isoc_ai_iaiu.tsv`, sha256 `7f668f7b…`; the EIGE mirror of the same date agrees on every common cell), for indicator `indic_is ∈ {I_IUAI, I_IUAIPR, I_IUAIWP, I_IUAIFE}`, unit `unit ∈ {PC_IND, PC_IND_IU3, PC_IND_IUAI}`, geography `geo`, and population group `ind_type`. A cell is **usable** if its value is non-missing and its flag is not `u`. A **pair** is the female and male cells for the same geography, group suffix, indicator and unit; a pair is usable only if both cells are.

### 2 · Groups

- Overall: `F_Y16_74` and `M_Y16_74`.
- Age bands: `F_/M_` + `Y16_24, Y25_34, Y35_44, Y45_54, Y55_64, Y65_74`. Overlapping bands and `Y75_89` are never used.
- Education: `F_/M_` + `I0_2, I3_4, I5_8`.
- No other sex-prefixed group exists; employment, occupation, urbanisation, citizenship and age-by-education carry no sex prefix and are not used.

### 3 · Quantities

For a usable pair with female rate `p_F` and male rate `p_M` (percentages):

- **gap** `= p_M − p_F` in percentage points; positive means higher male use.
- **ratio** `= p_F / p_M`; missing if `p_M = 0`; a smaller ratio is a larger male lead.
- **standardised rate** for sex `s`: `Σ_b w_b p_{s,b}` over the six bands with the EU27 2025 sex-pooled population weights `w_b` from `demo_pjan` (script 01; provisional file, flag `ep`); defined only when all twelve band cells are usable; never renormalised over surviving bands; never imputed.
- **standardised gap** `= standardised male rate − standardised female rate`.
- **internet-composition share** by band `= gap on PC_IND − gap on PC_IND_IU3`.
- **purpose participation**: the purpose indicator on `PC_IND`; **purpose among users**: the same on `PC_IND_IUAI`.

### 4 · Sample rule, sets and exclusions

- **Primary set:** the EU27 member states (27 geographies). `EU27_2020` and `EA` are reference aggregates, never units in a count or a tercile.
- **Extension set:** AL, BA, CH, MK, NO, RS, TR, XK, reported separately and placed against the primary set's cut values, never inside them.
- **Usable-pair rule:** every comparison uses only geographies where every cell it needs is usable. Each figure and table states its geography count. Nothing under thirty geographies is reported as a percentage of geographies; counts only.
- **Flagged cells** enter one appendix table, marked, and no main result.
- **Common-geography rule:** any comparison of two measures (points against ratio, crude against standardised, one purpose against another, one denominator against another) is made on the intersection of usable geographies, stated.
- **Coverage at commit** (counts inspected without values; referee re-derivation §C): overall usable pairs 36 of 36; all twelve sex-by-age cells usable for `I_IUAI` `PC_IND` in 33 of 36 geographies (EU27 members 26 of 27, IE lacking a usable 16–24 pair; MK and RS also lack 16–24; six of eight extension geographies complete); H-work usable EU27 set 27 of 27 on `PC_IND` and 27 on `PC_IND_IUAI`; H-education usable EU27 set 26 of 27 (HR lacks a usable pair on one education group); internet-composition share by band available for 26 of 27; purpose-specific standardisation: EU27 geographies with all twelve band pairs usable are 7 for each purpose, below the registered floor of 15, so robustness item 8 is omitted by rule.

### 5 · Error type and the bound

Eurostat publishes no cell-level standard errors, counts or design variables. No confidence interval is computed from published cells and no bootstrap of cells is presented as sampling uncertainty. The only uncertainty statement is the **sampling bound** of script 01, with the national net sample `n` of individuals aged 16–74 (row [D] of section 13.3.3.1.1 of the national reference metadata, read for 30 geographies; implied by the reference indicator's yes-count and proportion for HU and TR, where the row gives households only, and for IE, whose row is not parseable and whose precision block is dated 2022–23 and is used with that caveat; none for MK and XK, whose pages are not served), half per sex (A1), simple random sampling (A2, a lower bound), the country's published overall both-sex rate for the overall bound and the EU27 both-sex band rate for the band bounds (A4), and EU27 band shares for the sex-by-age cells (A3). The reference indicator's published standard errors are within 9% of the SRS value at the median across 30 countries; the ratio is above 1.3 for AT, BG, HR, RO and SK among EU members and for BA, CH, RS and TR in the extension, where the SRS bound understates the true half-width by those factors; the bound is a lower bound everywhere and a loose one there.

Realised bound (script 01, revision 2): the 95% half-width of a country's overall gap has median 2.8 points across 33 geographies (IT 0.88, DE 1.63, NL 2.60, DK 3.15, MT 4.71); within an age band the median half-width runs from 7.8 points at 16–24 to 3.7 at 65–74. Two countries' overall gaps are distinguishable at this bound only if they differ by more than the root-sum-square of their half-widths.

### 6 · Frames, fixed

- Reference period: use in the three months before the interview; fieldwork by convention in the first quarter of 2025. No earlier wave exists; no trend statement is possible.
- "Gender gap" is the framing; the categories are the source's female and male.
- The EU27 aggregate is population-weighted and is reported as a reference, not compared with member states as a peer.

## Hypotheses and decision rules

Every rule is a count over geographies in the stated set and can fail. Each hypothesis is judged on its **raw count**, which is the registered verdict; beside it the **distinguishable count** is reported, defined per rule below, counting the geographies whose result would survive that geography's sampling bound (`power_rules.json`). Both counts share the usable set as denominator. A geography with no bound (at commit: none in the EU27; MK and XK in the extension) enters the raw count and is listed by name as "no bound" beside the distinguishable one. The verdict words "supported" and "against" attach to the raw count; the post may not use either without the distinguishable count in the same sentence, and the Interpretation section reads "declared" as the raw verdict so qualified. For a difference of two gaps from the same respondents (H-work) the bound is √2 × the overall half-width, the independence value, which is conservative when the two purposes are positively correlated within respondents, as multi-select purposes are; for a difference of two band gaps (H-age) it is the root-sum-square of the two band half-widths, exact under SRS because bands are disjoint respondents.

### H-work · the gap is larger in work use than in private use

- **Test:** for each EU27 geography with usable pairs for `I_IUAIWP` and `I_IUAIPR` on `PC_IND` (27 of 27 at commit), compare `gap_work` with `gap_private`.
- **Rule for support:** `gap_work > gap_private` in a majority of the usable EU27 geographies. **Against:** a majority the other way, or a tie.
- **Distinguishable count:** distinguishable in favour if `gap_work − gap_private` exceeds √2 × the overall half-width; distinguishable against if it is below −√2 × the half-width.
- **Disclosed prior evidence:** the EU27 aggregate has private 5.5 and work 3.0 points, against H-work; Henseke's work gap among workers (4.1 points) is on a different population and denominator. The country inputs are in the committed audit file (Disclosure). The test is kept because the country majority is unread, and its verdict is reported with both disclosures.
- **Secondary form:** the same comparison among AI users (`PC_IND_IUAI`), reported beside it, not in the rule.
- **Expected resolution:** under a null of no difference between the two gaps a raw majority obtains by chance with probability ½; a raw count of 19 or more of 27 arises under an even split with probability 0.026. A raw majority below 19 is reported as "not distinguishable from an even split" whatever the distinguishable count; if every country had the EU27 purpose gaps the expected count in favour would be about 2.6 of 27.

### H-age · the gap is smallest or reversed at 16–24 and largest between 25 and 44

- **Test:** for each EU27 geography with all twelve usable sex-by-age cells for `I_IUAI` on `PC_IND` (26 of 27 at commit: IE lacks a usable 16–24 pair; the 33-of-36 count includes EU27_2020 and six extension geographies; MK and RS also lack 16–24), compute the six band gaps.
- **Rule (a) for support:** the 16–24 gap is the smallest of the six, or negative, in a majority of usable geographies. **Rule (b) for support:** the largest of the six gaps lies in `Y25_34` or `Y35_44` in a majority. Each rule can fail on its own; H-age is **declared** only if both hold; **partly declared** if one holds; **not declared** otherwise. (The brief's "against" for H-age left a gap between support and refutation; this rule's complement closes it, a completion marked here.)
- **Distinguishable count:** (a) distinguishable if the 16–24 gap lies below every other band's gap by more than the root-sum-square of the two band half-widths, or below zero by more than its own band half-width; (b) distinguishable if the largest gap lies in 25–34 or 35–44 and exceeds every gap outside those two bands by more than the root-sum-square of the two band half-widths.
- **Expected resolution** (referee's simulation with the per-country band bounds, `notes/rederivation/referee_prereg_gender1.py` §E; refreshed by script 01 after the sample-size and band-rate corrections): under a null of six equal true band gaps the expected raw count for (a) is about 6 of 26 and a raw majority has probability below 0.001; if every country had the EU27 profile, about 20 and 0.999. For (b) the null gives about 8–10 of 26 (P(majority) 0.03–0.10) and the EU27 profile about 13–16 (P(majority) 0.5–0.8), because the EU27's 25–44 gaps exceed its 55–74 gaps by under one point against band half-widths of six to eight. So (a) can be declared or refuted; (b) "not declared" is nothing shown and the post says so. The distinguishable counts for both are expected to be small.

### H-education · the high-education gap is the largest of the three

- **Test:** for each EU27 geography with usable pairs for all three education groups on `I_IUAI` `PC_IND` (26 of 27 at commit), order the three gaps.
- **Rule for support:** the `I5_8` gap is the largest of the three in a majority. **Against:** otherwise. The rule tests "high is the largest", not monotonicity; the monotone count (low < medium < high) is reported as descriptive beside it.
- **Distinguishable count:** no education-cell bound exists (no education shares of the sample are published or approximated); H-education is judged on the raw count alone, with the null expectation below stated beside it.
- **Expected resolution:** under three equal true gaps P(high is largest) = ⅓ and a raw majority of 26 has probability 0.025; no education-cell bound exists, so the power against the EU27 profile (3.8, 4.6, 7.0) is not computed and the raw verdict is reported with that limit.
- **Specification risk:** education cannot be age-standardised (no sex-by-age-by-education cells), and women's tertiary lead among the young means the high-education group is younger for women than for men; this is named in the interpretation, not adjusted.

### H-composition · applying a common age structure changes the tercile of few countries

- **Test:** on the geographies with a standardised gap (all twelve cells usable; 26 at commit), assign each its per-measure tercile (class rule below) on the crude gap and on the standardised gap.
- **Rule for support:** at most 8 of the 26 change tercile (one third of 26 is 8.67). **Against:** 9 or more change.
- **Distinguishable count:** a tercile change is distinguishable if both the crude and the standardised gap lie further than the geography's overall half-width from the (k+1)-th value they cross; at this bound few changes will be, and the count is reported whichever way.
- **Calibration, disclosed:** at the EU27 level the pooled-weight standardisation moves the gap from 4.46 to 3.36 points (referee item 12); a shift of about a point is the order to expect, against tercile spacings and half-widths of similar size.
- **Companion quantity, descriptive:** the change in the gap in points per country, reported never as a percentage explained.

### The class rule (fixed here, used by H-composition and by every "largest" statement)

*Per-measure tercile.* For each of the three measures, the signed gap on `PC_IND`, the ratio `p_F / p_M`, and the standardised gap, order the EU27 geographies with a usable value so that a larger male lead ranks higher (gap descending; ratio **ascending**, since a smaller `p_F / p_M` is a larger male lead; standardised gap descending). With N usable geographies, k = round(N / 3) (N = 27 → 9; N = 26 → 9); the top tercile is the k highest-ranked and the bottom tercile the k lowest-ranked, except that a geography whose value is within 0.1 point (ratio: within 0.01) of the (k+1)-th value from that end is **not** in the tercile (the tie rule).

*Persistent class.* **large-gap** = top tercile on all three measures; **small-gap** = bottom tercile on all three; **reversed** = `p_F > p_M` on `PC_IND` and on `PC_IND_IU3`; **not classifiable** = no usable value on one of the three measures (at commit: IE, which has no standardised gap); otherwise **not distinguishable**.

*Distinguishable class.* A large-gap or small-gap class is marked distinguishable if the geography's crude gap lies further than its 95% half-width from the (k+1)-th value on the gap measure; a reversed class is marked distinguishable if `|gap| > half-width` on `PC_IND`. The class table carries both marks. Agreement across the three measures guards against the choice of measure, not against sampling noise (the same cells are re-expressed; under a null of one common true gap the joint rule still classes about four geographies large-gap and six small-gap of 26 by noise alone, referee re-derivation §E); the distinguishable mark is the only noise guard, and the post says so.

*Class changes.* "A geography changes class between two measures" means its per-measure tercile differs between them, on the intersection of the two usable sets; H-composition counts this between the crude and the standardised gap on the 26 geographies with both; the same count between gap and ratio, and between ratio and standardised, is reported. Extension geographies are placed against the EU27 cut values, never inside them.

### The confirmatory set, counted

Five confirmatory rules: H-work (1, with the disclosed exposure of its country inputs, see Disclosure), H-age (2), H-education (1), H-composition (1). No p-value is computed anywhere, so there is no multiple-testing correction; the exposure is five count rules on one dataset, stated. Descriptive, not confirmatory: the map (rates and gaps by geography), the class table with both marks, the internet-composition share by band, purpose among users, the education profile and its monotone count. Exploratory, labelled: the two triangulation legs.

### Two implementations

Every gap, ratio, standardised rate, tercile and class is computed twice: once with pandas on the long table, once in pure Python from the TSV by key; they must agree to 1e-9 (script 04). The check block fails otherwise.

### Synthetic recovery (script 04)

A synthetic table with known female and male rates per band and known EU weights is built; the standardised gap must recover the implanted value to 1e-9; a table with equal male and female rates must return zero gaps, ratio one, and every geography "not distinguishable"; a table with an implanted composition effect (identical band gaps, different age structures) must return a crude gap that differs from the standardised one by the implanted amount; a table with one implanted large-gap geography and the rest equal must class exactly that geography large-gap on all three measures.

## Robustness, fixed now

1. Flagged cells included, in an appendix table only.
2. Ratio against signed gap: tercile changes counted.
3. Internet-user denominator (`PC_IND_IU3`) for every overall and band comparison; the internet-composition share by band (26 of 27 at commit).
4. AI-user denominator (`PC_IND_IUAI`) for purposes.
5. EU27 against the extension set, and against the full 35.
6. Equal band weights as a sensitivity to the population weights, labelled as a sensitivity, never as the standardisation.
7. Triangulation, exploratory: Spearman rank correlation, with the geography count, between the EU27 ordering by Eurostat overall gap and (i) OpenAI Signals' feminine share of messages by country, June 2025 (26 of 27), (ii) Henseke's work-adoption gap by country, against the Eurostat work-use gap. Rank correlation only; no class is defined for a message share. Reported whichever way.
8. Purpose-specific standardisation: omitted by rule (7 usable EU27 geographies per purpose against a floor of 15), stated in the post.

Nothing is added to this list without a dated deviation.

## Interpretation, fixed now

"Declared" below means the raw verdict, always reported with its distinguishable count in the same sentence.

- **All four hypotheses declared and few tercile changes:** the European gender gap in AI use is concentrated in work and mid-life, smallest or reversed among the young, widens with education, and survives age structure; the map's classes are stable; the close names the returns question and the non-use post.
- **Hypotheses mixed or failed:** the gap is real at the EU level and its location below it depends on the purpose and the band asked about; the post reports where the literature's expectation failed and says that no single number should be carried into an opportunity model.
- **Most comparisons not distinguishable:** the finding is the bound: a country ranking of the gender gap cannot be supported from published cells at this precision, and the post states what Eurostat would need to publish (cell counts or standard errors) for it to be.
- **H-composition fails (many tercile changes):** the published country ordering is partly an age-structure ordering, which is the measurement finding this post was designed to catch.

In every outcome: the EU27 aggregate values disclosed above are reported as the reference; the reversed geographies are named as a class, not ranked; no adjacent-rank statement appears; the close carries no number the body has not.

## Scripts

`01_sampling_bound.py` (this document's inputs; run twice, revision 2 after the referee's corrections), `02_build.py` (load, validate, coverage, EU headline reproduced), `03_gaps.py` (gaps, ratios, terciles, classes with both marks), `04_second_implementation.py` (pure-Python path, synthetic recovery), `05_standardise.py`, `06_denominators_and_purposes.py`, `07_triangulation.py`, `08_results_and_figures.py` (`results.json`, four figures with captions, the verifier's inputs). Each ends in a check block that stops on a wrong number.

## Deviations

Logged in `notes/lab-notebook.md` with date and reason; where a rule proves mis-specified, the registered rule and the corrected rule are both run and both reported.
