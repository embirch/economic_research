# Cross-check · the human's independent draft against the pre-registered results · 21 September 2026

The human ran the analysis separately (`notes/independent-draft-emily-2026-09-21.pdf`, 7 pages, "Research draft, September 2026", not pre-registered, exploratory inspection disclosed). Every number in it was checked against `data/processed/results.json` (referee-verified, 185/186 re-derived).

## Numbers: all agree

| Statement in the draft | results.json | Match |
|---|---|---|
| EU 30.45% women, 34.91% men, gap 4.46 | eu27.overall | yes |
| Ireland largest observed gap 9.32 (40.30 / 49.62); Denmark 7.87; Poland 7.29 | countries.IE/DK/PL.overall | yes |
| Denmark women 44.49%; Poland women 19.10% | idem | yes |
| Poland ratio 0.724 (largest proportional shortfall); Ireland 0.812 | countries.*.overall.ratio | yes (PL is the minimum ratio) |
| Five countries with higher female estimates, 1.34 to 1.71: MT, EE, SI, LT, HR | classes.reversed_on_pc_ind | yes |
| EU 16–24: 64.67% women, 63.00% men; largest gap 35–44 at 4.83 | eu27.age_profile_rates | yes |
| EU 65–74: 4.58 vs 8.72, gap 4.14, women's use about half of men's | eu27.age_profile_ratio.Y65_74 = 0.525 | yes |
| Ireland's youngest male estimate flagged; excluded | countries.IE.bands lacks Y16_24 | yes |
| Education gaps 3.76 / 4.61 / 6.97 | eu27.education_profile | yes |
| Private 5.51 vs work 3.00; education 9.30 vs 9.35; among users 30.53 vs 26.77, private 74.7/81.0, work 45.6/48.3 | eu27.purposes_* | yes |
| Private gap exceeds work gap in 23 of 27 | tests.H_work: 4 of 27 in favour of work | yes |
| Standardisation on 26 (Ireland excluded); median absolute change 1.31 | h_composition (median signed change −1.31; median absolute 1.31) | yes |
| Lithuania −1.35 → −5.38; Latvia +2.42 → −0.77 | standardised.LT / LV | yes |
| Internet-user denominator flips Lithuania's sign | countries.LT.internet_users.gap = +0.46 | yes |
| Heatmap cells (e.g. Ireland 25–34 +35.14; Slovenia 16–24 −18.55; Croatia −17.15; Denmark 35–44 +10.94) | countries.*.bands | yes |

## Where the two accounts differ (framing, not numbers)

1. **Ranks against classes.** The draft names Ireland the largest gap and Poland the largest proportional shortfall, with the caveat that "largest" means the largest published estimate. The pre-registered rule refuses ranks: Ireland is *not classifiable* (no standardised gap) and its 9.32 sits within its own bound (half-width 3.38) of Denmark's 7.87 (3.15); the persistent classes are six large-gap countries (Germany, Denmark, Hungary, Poland, Sweden, Slovakia) and seven small-gap, with 13 not distinguishable. The draft's caveat is right; the class table is the operational form of it.
2. **The sampling bound.** The draft says the extract gives no basis for confidence intervals. The pre-registered analysis derives a simple-random-sampling lower bound from the national net sample sizes (referee-corrected): the male lead exceeds it in 17 of the 22 countries where men lead; none of the five female leads does; within age bands almost nothing is distinguishable. The draft's "we cannot establish that women in these populations are more likely to use AI" is the same conclusion; the bound lets the post say how far from it each country is.
3. **Latvia's reversal under standardisation** (crude +2.42 to standardised −0.77) is a change of 3.2 points against Latvia's overall half-width of about 2.5; both values are inside noise of each other and of zero, which is why the class rule records Latvia as a tercile change but not a distinguishable one. The draft's own caveat ("does not establish a statistically significant reversal") is consistent.
4. **Fieldwork timing: the draft is right and the pre-registration's frame is wrong.** The draft's country register records that fieldwork differed across 2025 and that Greece ran July to September. The national metadata confirm it: most countries collected data between late March and early August 2025 (Germany 3 March–13 June; France 24 March–20 June; Spain 31 March–13 July; Czechia and Finland 7 April–3 August; Luxembourg 3 June–3 August), Serbia in February, Greece in July–September, Denmark's tables refer to August–December. The pre-registration's §6 ("fieldwork by convention in the first quarter") repeats the ESMS convention, not the practice; Figure 1's caption said "in early 2025" and now says "in the three months before their 2025 interview". Logged as a frame correction in the notebook; the post's methodology must carry the fieldwork spread and the limitation that the country comparison is not a common calendar window.
5. **What the draft does not carry:** the four pre-registered rules and their verdicts, the distinguishable counts, the class table, the two readings of the tercile-change count, the internet-use decomposition (none of the gap is an internet-use gap), the OpenAI Signals triangulation, and the extension geographies.
6. **What the pre-registered results do not carry and the draft does:** the explicit statement that the 65–74 gap is small in points but large in ratio (the post should use `eu27.age_profile_ratio`); the fieldwork register; the plain-language explanation of purposes among users.

## Recommendation

The draft is written in the register the write-up needs and every number in it is verified. The editor should build the post from it: keep its structure and language, bind every sentence to `results.json` through the claims map, replace ranks with classes where the claims list requires, add the bound, the rule verdicts and the fieldwork limitation, and hyperlink the sources.
