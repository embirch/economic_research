# What 81,000 people want from AI

## Source

- **Slug:** `survey-81k-interviews-2026-03`
- **Title:** "What 81,000 people want from AI" (the H1 carries a hard line break after "people", which renders as a double space in extracted text; the bibtex title capitalises differently: "What 81,000 People Want from AI")
- **Type:** Institute feature (interactive web article). The page calls it "this research", "this post" (bibtex header: "If you'd like to cite this post"), "a new form of social science" and "qualitative research at a massive scale". It is not styled as a report or paper and carries no page numbers, so every reference below is to a **named section and element** of the page.
- **Primary URL:** https://www.anthropic.com/features/81k-interviews
- **Published:** the page carries **no visible dateline**. The bibtex key gives `date = {2026-03-18}`; the Corrections block is dated "Mar 19, 2026"; the social image asset embedded in the page was created 2026-03-17. `wiki/INDEX.md` records 2026-03-19, i.e. the correction date. Recorded as a discrepancy rather than resolved.
- **Lead author and credited roles (Authorship and acknowledgments):** "Saffron Huang led the project, designed and ran the analysis, and wrote the blog post. Shan Carter led data visualization, prototyped the interactive article, and helped with analysis. Jake Eaton led editorial development, and Sarah Pollack led communications strategy." The same section names Dexter Callender III (production), Nikki Makagiansar, Maria Gonzalez and Kelsey Nanan (design), Sylvie Carr (editorial), "Miles McCain and Kunal Handa helped with analysis", Jerry Hong (design), "Grace Yun, AJ Alt, and Thomas Millar implemented Anthropic Interviewer within Claude.ai", "Chelsea Larsson, Jane Leibrock, and Matt Gallivan contributed to survey and experience design", "Theodore Sumers contributed to the data processing and clustering infrastructure", and "Jack Clark, Michael Stern and Deep Ganguli provided critical feedback, direction and organizational support."
- **Bibtex key:** `huang2026interviewer`. Its author list is longer than the prose acknowledgement and adds Mo Julapalli, Esin Durmus, Matt Kearney and Judy Hanwen Shen.
- **Also thanked:** "David Saunders, Mengyi Xu, Katie Kennedy, Bianca Lindner, Meredith Callan, Tim Belonax, Jen Martinez, Peter McCrory, and Miriam Chaum". Peter McCrory is a co-author of the labour-market paper (`wiki/reports/labor-market-impacts-2026-03.md`); the economics team appears here only in the acknowledgements.
- **Separate appendix:** yes. The page's Appendix section reads "Available here." and links https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf. The page refers readers to it three times: for methods ("The Appendix describes our methods in more detail, as well as limitations and some additional analysis"), for the light-and-shade correlations, and for the "geographical breakdown of respondents". **It is a separate slug and is not summarised here** — see `wiki/reports/survey-81k-interviews-2026-03-appendix.md`. Everywhere this file says a threshold, a correlation or a sample rule "is in the Appendix", the content is deliberately left to that file.
- **Instrument:** Anthropic Interviewer, introduced in a separate publication — see `wiki/reports/anthropic-interviewer-2025-12.md` (slug `anthropic-interviewer-2025-12`). This page links it twice.
- **Companion analysis of the same interviews:** the economics write-up — see `wiki/reports/survey-81k-economics-2026-04.md` (slug `survey-81k-economics-2026-04`). This page does not mention it.
- **Other Anthropic pages linked from the body:** https://www.anthropic.com/news/protecting-well-being-of-users (user wellbeing safeguards), https://www.anthropic.com/news/ai-for-science-program, https://www.anthropic.com/news/claude-for-nonprofits, https://www.anthropic.com/research/economic-policy-responses (see `wiki/reports/programme-and-product-pages.md`), and https://www.anthropic.com/economic-index, the latter cited as the "usage analysis" complement to this instrument.
- **Terms it introduces into the Anthropic vocabulary:** "light and shade" (paired benefit/harm tension), light side / shade side, lived versus hypothetical (experienced versus anticipated), ambivalence / co-occurrence of light and shade, "the exposed middle" (freelancers), "capital bypass mechanism", "cognitive scarcity rather than time poverty" (quoted from a respondent), net positive sentiment, vision / experience / concern as the three classifier families.
- **Published data assets attached to the page.** The interactive charts are driven by JSON files served from the Anthropic CDN, not by images. Four are substantive: a statistics file (`a9cde041d15765c23813279f5ccde115bd40f29a.json`) holding global, by-region, by-country, by-US-state and light-and-shade figures plus the verbatim classifier label set; a quote file for the in-page charts (`9ac19583d019b85db5ca3af485f419f74f3fe4a5.json`); the Quote Wall file (`b9f944c5ea6207dd80c7204544457960642eda46.json`, 620 quotes with country, region, self-described job and tags); and three TopoJSON basemaps. Full URLs are in `Verification`. Numbers taken from the statistics file are marked **`(chart data asset)`** at the point of use and are never presented as prose or as a caption, by analogy with the director's alt-text ruling (`room/director-2026-09-16-alt-text-ruling.md`); that ruling does not cover published chart *data*, and a ruling is requested in `room/lead-2026-09-16-wiki-survey-81k-interviews-2026-03.md`. No number in this file was read off a chart image.
- **Corrections (verbatim, page):**
  > "Mar 19, 2026. \"Globally, 67% of people view AI positively\" changed to \"Globally, 67% of interviewees expressed net positive sentiment toward AI\" to more precisely describe the study's methodology."

### Three different denominators, never reconciled on the page

| Figure | Where it appears | What it counts |
|---|---|---|
| 81,000 | title; "To the 81,000 people who took the time to speak with us" | rounded headline |
| 80,508 | body ("80,508 people, across 159 countries and 70 languages, took the interview"); acknowledgements ("We thank the 80,508 Claude users") | took the interview |
| 79,734 | statistics file, `global.n` **(chart data asset)** | behind the vision, experience, concern and sentiment shares |
| 72,105 | statistics file, `lightShade[*].n_total` **(chart data asset)** | behind all five light-and-shade tensions |

The page states one filter — "we filter out those who don't answer the concerns question" — but never gives a number for it, and never states which denominator any published percentage uses. The appendix is the place that may reconcile these; see the appendix file.

## Claims

Numbers are reproduced as published. The page has no figure numbers; references are to the section heading and the element (ranked list, caption, chart card, paragraph). "Lead-in paragraph" below means the unheaded paragraph that begins "Public conversation about AI often centers on abstract projections", which sits between the opening scrolly quotes and the Quote Wall section and carries the study's design statement. Every claim names the comparison it rests on, because almost nothing here is a level that stands alone: the article's unit of argument is a share of respondents set against another share — hope against fear, region against region, lived against anticipated.

### Scale and standing

1. **The interview count.** "80,508 people, across 159 countries and 70 languages, took the interview" (lead-in paragraph). *Comparison:* against the largest prior qualitative studies, given in footnote 1 — "The largest qualitative studies we found in our research were the USC Shoah Foundation Visual History Archive and the World Bank \"Voices of the Poor Project,\" both of which included ~60,000 participants."

2. **The standing claim, twice stated and hedged both times.** "We believe this is the largest and most multilingual qualitative study ever conducted" (opening scrolly text, and again in the same lead-in paragraph with footnote 1 attached). *Comparison:* participant count and language count against the two named archives. Nothing else about those studies is compared.

3. **Why an AI interviewer at all.** "For the first time, AI has enabled us to collect rich, open-ended interviews at extraordinary scale" (opening scrolly text); "This approach bridges the typical tradeoff in qualitative research between depth and volume" (§"Seeing the forest and the trees"). *Comparison:* depth against volume — the stated tradeoff of conventional qualitative method.

4. **Fieldwork window and invited population.** "Over one week in December, we invited everyone with a Claude.ai account to sit down with Anthropic Interviewer" (lead-in paragraph). *Comparison:* none; a design statement. The **year is not stated** anywhere on the page — "Last December" is the only other marker, and the article is dated March 2026.

5. **The hero visualisation's unit.** "Each dot represents 4 respondents" (caption under the opening visualisation). *Comparison:* none; a scale device.

### What people want from AI (visions; one primary code per respondent)

6. **Nine vision categories and their shares**, from the ranked list in §"What people hope for": professional excellence **18.8%**; personal transformation **13.7%**; life management **13.5%**; time freedom **11.1%**; financial independence **9.7%**; societal transformation **9.4%**; entrepreneurship **8.7%**; learning & growth **8.4%**; creative expression **5.6%**. The caption adds: "1% of respondents did not articulate a vision." *Comparison:* rank across nine mutually exclusive categories, since "\"What people want from AI\" was classified into a single primary category per respondent". The statistics file carries the same nine values to three decimals and `visions_said_no: 1.139` **(chart data asset)**.

7. **The prose rounds the same figures differently.** "the largest group of people (19%) sought \"professional excellence\"" and "Another 9% envisioned AI as an entrepreneurial partner"; "Overall, 11% of people saw AI's productivity benefits as ultimately a way to free up time for personal relationships and leisure, while 10% took that logic farther, seeking to use AI to gain financial independence"; "many of the people grouped into the \"life management\" category (14%)"; "\"Personal transformation\" … also appeared frequently (14%)"; "nearly one in ten people described a positive vision of societal transformation" (§"Looking forward"). *Comparison:* the same ranking; recorded because a post quoting this page must choose between the chart's one-decimal figures and the prose's integers.

8. **Sub-structure inside one category.** "Within this category, the desires were diverse, ranging from cognitive partnership and collaboration (24%), to support with mental health (21%) or physical health (8%), and even romantic connection with AI (5%)" (§"What people want from AI", personal-transformation paragraph). *Comparison:* shares **within** the personal-transformation group, not of all respondents. These four sub-categories appear nowhere else on the page and are not in the published label set.

9. **The nine categories re-grouped into four motives.** "Roughly a third of visions are about making room for life—more time, money, mental bandwidth—by using AI to alleviate current burdens. Another quarter revolves around using AI to help people do better, more fulfilling work (not escaping work, but getting more out of it). About a fifth are about becoming someone better—learning, healing, growing. A smaller share want to make something (\"creative expression\") or fix the world (\"societal transformation\")." *Comparison:* a re-aggregation of the same nine shares; the mapping from category to motive is not stated.

10. **The re-framing that follows the follow-up question.** "Many others similarly started the interview talking about productivity, but after Anthropic Interviewer asked about their underlying hope behind it—what realizing this vision would enable for them—other priorities surfaced. It wasn't about doing better work, but increasing their quality of life outside of it." *Comparison:* first-stated answer against the answer after an adaptive probe. No number is attached to this shift; it is the clearest instance of the instrument's adaptivity being treated as a finding.

11. **The unifying reading.** "Across all these groups, the unifying ask was for AI to help them live better, more enjoyable lives"; restated in §"Looking forward" as "Most of the visions people described, ranging from personal transformation to cognitive support, collapse into an underlying desire: that AI helps them live *better*, not simply work *faster*." *Comparison:* work-centred against life-centred readings of the same nine categories.

12. **What societal-transformation hopes were about.** "Those that wanted societal transformation from AI often cited a vision for healthcare… Transformation in the form of education came next. Respondents in low and middle income countries were quick to cite the possibility that AI might break the association between educational quality and wealth." *Comparison:* healthcare against education against other public goods, within the 9.4% group; qualitative ordering only, no shares.

### Whether people are getting it (experiences)

13. **81% report a step toward their vision.** "When asked if AI had ever taken a step towards their stated vision, 81% of people said yes" (§"Are people getting what they want?"). *Comparison:* yes against no on one question. The statistics file records `experiences_said_no: 18.94` **(chart data asset)**, identical to the share of the "AI hasn't delivered" category — so on the published numbers the no-answers and that category are the same people, which the page never says.

14. **Seven experience categories presented as six.** The prose says "We grouped those experiences into six main areas", and the ranked list in §"Where AI has delivered on their vision" then shows **seven**: productivity **32.0%**; AI hasn't delivered **18.9%**; cognitive partnership **17.2%**; learning **9.9%**; technical accessibility **8.7%**; research synthesis **7.2%**; emotional support **6.1%**. *Comparison:* rank across categories of self-reported realised benefit. Recorded as published, including the six/seven mismatch: the second-largest item is the absence of a benefit.

15. **Prose roundings of the same list.** "The dominant story in the \"productivity\" bucket (32%) was technical acceleration"; "another kind of productivity story emerged in the technical accessibility responses (9%), which emphasized access rather than speed"; "The cognitive partnership (17%), learning (10%), and emotional support (6%) responses often mentioned the same core underlying AI affordances: patience, availability, and the absence of judgment"; "Research synthesis (7%) and information processing is also a significant affordance". *Comparison:* speed against access, and the three "affordance" categories against each other.

16. **Emotional support is small and treated as important anyway.** "Emotional support comprised only 6% of responses, but these were among the most affecting we encountered." *Comparison:* share against salience — an explicit statement that the article's weighting of a theme is not its frequency.

17. **The interpretive claim about what AI is being used as.** "These stories reveal AI operating across a spectrum—productivity tool, accessibility technology, educational resource, research assistant, emotional companion—and often filling multiple roles at once. AI offers unlimited patience without judgment, availability without inconvenience, and an incredible capacity to digest information, across many domains of life." *Comparison:* the categories against each other, read as roles rather than tasks.

### What people are concerned about (concerns; multi-label)

18. **Thirteen concern categories and their shares**, from the ranked list in §"What people worry about": unreliability **26.7%**; jobs & economy **22.3%**; autonomy & agency **21.9%**; cognitive atrophy **16.3%**; governance **14.7%**; misinformation **13.6%**; surveillance & privacy **13.1%**; malicious use **13.0%**; meaning & creativity **11.7%**; overrestriction **11.7%**; wellbeing & dependency **11.2%**; sycophancy **10.8%**; existential risk **6.7%**. *Comparison:* rank across categories that **can overlap** — "we used a multi-label classifier (response can map to multiple concerns)" — so these shares do not sum to 100 and cannot be read as a partition. The statistics file carries the same thirteen to three decimals **(chart data asset)**.

19. **Concern breadth.** "About 11% of people expressed no concern… But on average, respondents voiced 2.3 distinct concerns." *Comparison:* number of distinct codes per respondent, against the single code assigned for visions.

20. **The long tail, named but not charted.** "There was also a long tail of other concerns mentioned, e.g. concerns around bias and discrimination (5%), IP and data rights (4%), environmental costs (4%), harms to children and vulnerable groups (3%), democracy and political integrity (3%), or geopolitics (2%)." *Comparison:* tail against the charted thirteen. The published label set contains twenty-three concern categories: the thirteen charted, the six named here, and four more that appear nowhere on the page — including one, "Economic displacement", whose definition overlaps the charted "Jobs & economy" **(chart data asset)**; see `Definitions`.

21. **The economic concern is the one that moves sentiment.** "Concern about jobs and the economy was the strongest predictor of overall AI sentiment, suggesting it's more salient than any other issue" (§"What people are concerned about"), repeated in §"How perspectives vary around the world" as "Concern about jobs and the economy was the strongest predictor of AI sentiment overall". *Comparison:* the predictive strength of each concern category for the 1–7 sentiment rating. **No model, coefficient, specification or ranking is reported anywhere on the page**; this is the article's single most load-bearing statistical claim and its evidence is not shown. The appendix may carry it.

22. **Hopes are general, fears are specific.** "People's positive visions for AI seemed mostly to stem from a few basic desires: more time, more autonomy, more personal connection. Concerns were more varied and concrete, laying out specifics of what could go wrong." *Comparison:* dispersion of the vision distribution against the concern distribution; asserted, not quantified.

### Light and shade (five paired tensions)

23. **The framing claim.** "We found five recurring tensions between directly competing benefits and harms that were discussed… We call this the \"light and shade\" of AI: the same capabilities that lead to benefits also produce harms. The two sides are entangled." *Comparison:* benefit share against harm share within the same pair, and within the same person.

24. **The five tensions as charted** (§"Light and shade", paired bar charts; the bars give percentages of respondents, split into those speaking from experience and those anticipating):

| Tension | Light (benefit) | Shade (harm) | Light: seen / expect | Shade: seen / expect |
|---|---|---|---|---|
| Learning ↔ cognitive atrophy | 33% | 17% | 30% / 3% | 8% / 9% |
| Better decision-making ↔ unreliability | 22% | 37% | 19% / 3% | 29% / 8% |
| Emotional support ↔ emotional dependence | 16% | 12% | 13% / 3% | 5% / 7% |
| Time-saving ↔ illusory productivity | 50% | 18% | 37% / 13% | 17% / 1% |
| Economic empowerment ↔ economic displacement | 28% | 18% | 19% / 9% | 14% / 4% |

*Comparison:* light against shade, and lived against hypothetical, on a common denominator. The statistics file gives the same quantities to one decimal with counts — `pct_light`, `pct_shade`, `pct_either`, and the lived/hypothetical split as percentages **of the mentioners** (e.g. Time-saving `pct_light` 50.2, `light_pct_lived` 74.0; Economic `pct_light` 28.7, `pct_shade` 17.7, `shade_pct_lived` 23.3) on `n_total` 72,105 **(chart data asset)**. One prose/chart mismatch: the chart bar reads 18% for illusory productivity while the prose says "19% were wary of actually losing time due to AI".

25. **Co-occurrence within the person.** "Someone who values emotional support from AI, for example, is three times more likely to also fear becoming dependent upon it. This pattern held across every tension we measured—although the correlation was weakest in the economic tension". *Comparison:* rate of holding the shade view among those holding the light view, against the base rate. The correlations themselves are in the appendix.

26. **Where the benefit is lived and the harm imagined.** "Across most tensions, the benefit side is more grounded in experience, while the harm leans hypothetical. For example, 33% of people mentioned AI's benefits for learning, while 17% expressed worry about cognitive atrophy from AI use. 91% of those who mentioned learning benefits mentioned realizing those gains in some way, but 46% of those worried about atrophy had seen it firsthand." *Comparison:* conditional experience rate, light side against shade side.

27. **Education is where atrophy is witnessed.** "Students raised this particular tension the most—more than half had experienced learning benefits, but 16% also noted signs of cognitive atrophy, a rate exceeded only by their teachers (24%) and academics (19%). Troublingly, educators were 2.5-3 times more likely than average to report having witnessed cognitive atrophy firsthand, presumably in their students." *Comparison:* self-described job category against the overall average.

28. **Volitional learning against institutional learning.** "Tradespeople were among the most enthusiastic about AI-for-learning (45% reported having experienced learning benefits, second only to students), yet almost none had witnessed cognitive atrophy (4%—less than half the baseline). A similar pattern holds for self-employed researchers and people who said they weren't currently working. This suggests AI's benefits may be strongest when learning is volitional, compared to within institutional structures where AI is more likely to be used as a shortcut." *Comparison:* tradespeople and the self-employed against students and educators. The closing sentence is the page's own conjecture from the contrast.

29. **The one tension where the harm is larger.** "22% of people expressed excitement about AI as an aid in decision-making, while 37% lamented that AI impedes good decisions because of its unreliability (e.g. hallucinations). This is the only tension in which the negative overshadowed the positive. Both sides were deeply rooted in experience—88% of those talking about the decision-making benefits and 79% of those talking about the harms had witnessed it directly. Many people have both leaned on AI for judgment and been burned by it. This is mentioned by people in high-stakes professions—law, finance, government, and healthcare—at nearly twice the average rate. Nearly half of all lawyers, in particular, mention coming up against AI unreliability firsthand, yet they also report the highest rates of realized decision-making benefits." *Comparison:* light against shade; high-stakes occupations against the average; lawyers against all.

30. **The most entangled tension.** "Only 22% of people raised either the positives of emotional support or the negatives of emotional dependence on AI. But it's also the most entangled tension we found, with the strongest co-occurrence of light and shade in the same person (triple the baseline co-occurrence rate). People not currently working are twice as likely to raise it, and twice as likely to describe some experience of dependence. Healthcare professionals are overrepresented on both sides too, perhaps reflecting the fact that they talk about using Claude for emotional support at twice the rate of other professionals." *Comparison:* co-occurrence against baseline; the not-working and healthcare groups against the average. Note that 22% here is the share raising **either** side (`pct_either` 22.0 in the statistics file), not the light share.

31. **The most mentioned benefit of all, and its shadow.** "Time-saving was the most commonly cited benefit—half of all respondents raised it—but 19% were wary of actually losing time due to AI, e.g. due to the verification burden, or simply getting busier as expectations increase at work. Those who are self-employed—e.g. freelancers and small business owners—are the most likely to mention both sides at once. Without an institutional layer to buffer the new pace, they both get the gains and feel the squeeze." *Comparison:* light against shade; self-employed against employed. The last sentence is interpretation.

32. **The economic tension is the most speculative and the least entangled.** "The economic mobility tension—between those yearning for economic empowerment from AI and those fearing displacement from it—is the most speculative, with the highest rate of hypothetical hopes *or* fears. It's also the one where the co-occurrence of upside and downside is weakest (with a correlation score of +0.16 vs an average of +0.25). Usually the people most engaged with the upside of a tension tend to be similarly engaged with its downside; here, the groups diverge." *Comparison:* correlation for this pair against the mean across the five pairs. The "+0.16 vs +0.25" pair is the only correlation number on the page; the rest are in the appendix.

33. **Who is already gaining economically — the article's sharpest economic number.** "Worry about displacement is spread fairly evenly across job categories. What varies is who's already experiencing economic benefit from AI—and that skews heavily toward independent workers—entrepreneurs, small business owners, even people with side projects—half of whom report real economic empowerment, more than triple the rate of institutional employees (47% vs 14%). Employees with side projects benefited the most, with 58% stating some form of real economic gains. The same occupational patterns hold when you look at who's excited, regardless of experience, suggesting that optimism here is well-calibrated." *Comparison:* independent workers against institutional employees, on lived economic empowerment; and stated excitement against lived experience, within each group. No denominators are given for either group.

34. **Freelancers as the exposed middle.** "Freelancers are the exposed middle. They benefit from AI *while* feeling in a precarious situation because of it. Freelance creatives, in particular, sit at 23% lived benefit and 17% lived precarity—the one group where the upside and downside nearly cancel out. AI is both their tool and their competitor. Institutional employees, and especially academics, register low on both axes." *Comparison:* lived benefit against lived precarity within one occupational group, and that group against employees and academics.

35. **The generalisation across all five tensions.** "A pattern runs across all five tensions: the more personal and immediate the impact, the more likely people are speaking from experience. The more systemic or long-term the impact—economic displacement, cognitive atrophy—the more speculative they become. That the systemic concerns remain speculative is not a verdict on AI's ultimate impact as much as a reflection of how early we are in its adoption." *Comparison:* personal/immediate harms against systemic/long-term harms, on the lived-versus-anticipated split.

36. **No camps.** "It's easy to assume there are AI optimists and AI pessimists, divided into separate camps. But what we actually found were people organized around what they value—financial security, learning, human connection— watching advancing AI capabilities while managing both hope and fear at once." Stated earlier in the scrolly text as "Across interviews, hope and alarm didn't divide people into camps, so much as coexist as tensions within each person." *Comparison:* between-person variance against within-person variance. The statistics file carries an `ambivalence` field (global 42.95; 46.72 in North America, 24.38 in Central Asia) that is never named or defined on the page **(chart data asset)**.

### How perspectives vary around the world

37. **Global sentiment.** "Globally, 67% of interviewees expressed net positive sentiment toward AI" (§"How perspectives vary around the world"). *Comparison:* net-positive share against the rest of the 1–7 scale. This sentence is the corrected wording; the original read "Globally, 67% of people view AI positively".

38. **The regional gradient.** "Clear trends emerged in which people in South America, Africa, and much of Asia view AI with more optimism than those in Europe or the United States." *Comparison:* lower- and middle-income regions against Europe and the US.

39. **The country map caption.** "Rate of overall positive sentiment toward AI in each country. Bigger bubbles mean more respondents from that country; green means more positive about AI, blue means less. AI sentiment is majority-positive everywhere (no country dips below 60%) and the range is narrow, but lower and middle income countries are reliably more positive than average." *Comparison:* country against country, bubble size = respondents. **The map itself did not render in the fetched text** (the element reads "Loading data..."), so no country value is recorded from the visual. The statistics file behind it holds 125 countries, of which five sit below a 0.60 net-positive rate — the largest of them with 212 respondents — so the caption's parenthesis holds only under a minimum-respondent display rule that the page does not state **(chart data asset)**. Flagged, not resolved: a display threshold would be an appendix fact.

40. **Who says they have no concerns.** "When asked about concerns, respondents from Sub-Saharan Africa (18%), Central Asia (17%), and South Asia (17%) were the most likely to say they had none—roughly double the rate in North America (8%), Oceania (8%), and Western Europe (9%)." *Comparison:* regional no-concern rates against each other and against the global 11%.

41. **The regional card.** §"AI SENTIMENT BY REGION", subtitled "% sentiment on AI, and concern about jobs and economy", lists twelve regions with an approximate n: Western Europe n=~15,000, 35.6% / 22.5%; Oceania n=~2,000, 35.5% / 24.3%; North America n=~23,000, 34.5% / 24.6%; East Asia n=~10,000, 34.5% / 21.9%; Southern & Eastern Europe n=~9,000, 34.0% / 22.1%; Central Asia n=~0,000, 31.1% / 15.9%; South Asia n=~5,000, 30.8% / 21.5%; North Africa n=~1,000, 30.6% / 18.2%; Middle East n=~2,000, 29.2% / 19.9%; Southeast Asia n=~3,000, 28.3% / 19.3%; Latin America & Caribbean n=~8,000, 26.3% / 18.5%; Sub-Saharan Africa n=~2,000, 24.2% / 18.2%. *Comparison:* region against region on two axes. **Reading trap, recorded because it inverts the sign of every one of these numbers:** the column is headed "AI sentiment" but the values are rates of **negative** sentiment — the accompanying scatter labels its vertical axis "Rate of negative sentiment toward AI (%)" with "33% avg", the card is sorted with the most optimistic region last, and each value equals 100 minus that region's net-positive share in the statistics file (Western Europe 0.644 → 35.6; Sub-Saharan Africa 0.758 → 24.2) **(chart data asset)**. "Central Asia n=~0,000" is a rounding artefact of the card's thousands format; the statistics file gives 310 respondents **(chart data asset)**.

42. **The scatter's reading.** "Concern about jobs and the economy was the strongest predictor of AI sentiment overall, and it is especially apparent when grouping by region. Wealthier regions (pink) cluster in the top right (more concerned about the economy, more negative AI sentiment), split from less wealthy regions (green) which are in the bottom left (less concerned about AI's impact on the economy, and less negative AI sentiment). Bubble size reflects the number of respondents in each region." *Comparison:* regional economic-concern rate against regional negative-sentiment rate, at the region level — twelve points, no dispersion measure and no country-level version.

43. **Four candidate explanations for the income gradient, offered together.** "There are several possible explanations for the more positive AI sentiment in lower and middle income countries. Claude.ai users are likely biased towards early AI adopters who are more excited about new technologies, and in general emerging economies tend to view new technology as a ladder up rather than a threat. Concern about jobs and the economy was the strongest predictor of AI sentiment overall, and this was less of a concern among interviewees in these regions. But there is also less market penetration in these regions—if AI hasn't visibly entered your daily work yet, AI displacement likely feels abstract, especially when more immediate economic pressures already exist." *Comparison:* none tested against another; four mechanisms named side by side. This is the page's clearest open question and is recorded again below.

44. **Visions by region.** "While some aspirations—e.g. around professional excellence—are nearly universal, there are significant regional differences. It seems that wealthier, more AI-exposed regions more want AI to *manage the complexity of life*; developing regions more want AI to *create more opportunity.*" Named instances: "The vision of AI for entrepreneurship resonates most in Africa, South and Central Asia, the Middle East, and Latin America & the Caribbean. In these regions, AI is framed as a capital bypass mechanism—a way to start businesses without the funding, hiring, or infrastructure that would otherwise be required."; "Learning using AI is disproportionately important in Central and South Asia (14% and 13% respectively versus 8% globally)."; "AI for life management resonates the most in Western developed countries (particularly high in North America, Oceania), where workers experience, as one person described, \"cognitive scarcity rather than time poverty.\""; "East Asia stands out for wanting AI to help with personal transformation (19%, the highest of any region) as well as financial independence (15%, also the highest)." *Comparison:* regional share against the global share for the same vision. The slope charts that would give the full ranking read "Loading…" in the fetched text; their caption is "Comparative slope charts of the most common AI visions in each region, with lines connecting the same theme across both sides to show how rankings shift. Bolded visions were more often expressed in that region. Grey items were similarly or less often expressed."

45. **Concerns by region.** "Concerns about AI unreliability, the economy, and human autonomy and agency top the list in virtually every region—but there are distinctive regional trends. North America and Oceania are particularly worried about governance gaps for AI (18% and 19% respectively, versus 15% globally). Western Europe's standout concern is surveillance and privacy (17%). East Asia bucks the general global pattern; governance and surveillance drop to their lowest levels of any region (12% and 7%), overshadowed by concerns about cognitive atrophy (18%) and loss of meaning (13%). The West worries about who owns and controls AI; East Asia worries more about the personal implications of its use. In Africa, South & Southeast Asia, South & Central America, concerns broadly tend to drop. Their worries index more highly on things like unreliability and jobs, rather than more abstract concerns like governance, misinformation, loss of meaning, or existential risk." *Comparison:* regional concern share against the global share; abstract concerns against concrete ones.

46. **An East Asian sub-reading offered qualitatively.** "From a qualitative review of these users' quotes, one interesting trend is that people often connected financial independence explicitly to family obligations and filial piety—one Korean user described needing money to care for parents' retirement and ensure loved ones' happiness (vs. for personal consumption)." *Comparison:* one region's stated motive for a category against the category's general reading; explicitly a qualitative review of quotes, with n = 1 example.

### What Anthropic says it will do next

47. **A wellbeing panel study, already launching.** "Our next Anthropic Interviewer study, launching shortly to a small subset of Claude users, focuses on Claude's effects on people's wellbeing over time: whether Claude is actually making people's lives better in the ways they want, and how it could do so more effectively" (§"Looking forward"). *Comparison:* stated wants against realised wellbeing, over time rather than in one cross-section.

48. **Beneficial Deployments as the response to the societal-transformation vision.** "Additionally, nearly one in ten people described a positive vision of societal transformation—AI to cure diseases, democratize expertise, and strengthen institutions. Through our Beneficial Deployments program, we're collaborating with our AI for Science and nonprofit partners to understand how they use Claude and where it still needs to improve, to close the gap between the societal transformations people envision and today's reality." *Comparison:* envisioned societal transformation against "today's reality" — a gap the page names but does not measure.

49. **The economic concern is routed into the economics stream.** "We also take some of the most-cited concerns—e.g. around negative economic impacts of AI—seriously, as signals around which we are designing further research and updating our thinking" (§"Looking forward", linking https://www.anthropic.com/research/economic-policy-responses). *Comparison:* concern salience as an input to a research agenda. This is the explicit hand-off from this feature to the economics work.

50. **Where this instrument sits relative to the Economic Index.** "Surveys and usage analysis tell us *what* people are doing with AI, but the open-ended interview format helps us get at *why*" (§"Conclusion"; "analysis" links https://www.anthropic.com/economic-index). *Comparison:* what against why — observed usage against stated motive. This sentence is the load-bearing one for any post that wants to join interview data to Index data.

## Definitions (verbatim)

All quotations are the page's own words unless marked **(chart data asset)**, in which case they are the label text shipped in the page's published statistics file. References are to section headings.

### The instrument

**Anthropic Interviewer (lead-in paragraph):**
> "we invited everyone with a Claude.ai account to sit down with Anthropic Interviewer—a version of Claude prompted to conduct a conversational interview—and tell us about how they view AI."

**Interview design (§"Seeing the forest and the trees"):**
> "Anthropic Interviewer asked each interviewee a set list of questions about what they want and don't want from AI, then adapted follow-up questions based on responses. This approach bridges the typical tradeoff in qualitative research between depth and volume, and allows us to collect rich, open-ended interviews at a very large scale."

**The vision question, verbatim (caption under the visions chart):**
> "What respondents most wanted from AI, classified by Claude from their open-ended answers to \"If you could wave a magic wand, what would AI do for you?\" 1% of respondents did not articulate a vision. Hover to see example quotes."

**The follow-up probe, described not quoted (§"What people want from AI"):**
> "after Anthropic Interviewer asked about their underlying hope behind it—what realizing this vision would enable for them—other priorities surfaced"

**The experience question, verbatim (caption under the experiences chart):**
> "What respondents said AI had already done for them, classified from open-ended answers to the question \"Has AI ever taken a step towards that vision for you?\""

**The concern question, verbatim (caption under the concerns chart):**
> "What respondents worried about, classified from open-ended answers to the question , \"Are there any ways in which AI could be developed that would be contrary to your vision or what you value?\" Respondents tended to raise multiple concerns, so we used a multi-label classifier (response can map to multiple concerns)."

(The stray comma after "the question" is in the source.)

**Question order, as disclosed in the caveats paragraph (§"Light and shade"):**
> "our interview asked first for positive visions for AI and then for concerns that would counter their vision"

### Classification

**The classifier families (§"Seeing the forest and the trees"):**
> "To make sense of this huge amount of information, we built Claude-powered classifiers that categorized each conversation across a range of dimensions—what people want from AI, whether they're getting what they want, what they fear, what they do for a living (if mentioned), and their sentiment about AI overall. \"What people want from AI\" was classified into a single primary category per respondent, while concerns were multi-label—a single interview could receive multiple codes, since respondents tended to articulate several distinct worries rather than one."

**Quote selection (§"Seeing the forest and the trees"):**
> "We also used Claude to pull out representative quotes."

**Sentiment (§"How perspectives vary around the world"):**
> "We rated each transcript's overall sentiment toward AI on a 1-7 Likert scale, and then calculated the percentage of people with net positive sentiment (i.e. 5 or above) in various countries"

**Light and shade — the construct (§"Light and shade"):**
> "We call this the \"light and shade\" of AI: the same capabilities that lead to benefits also produce harms. The two sides are entangled."

**Light and shade — the measurement (§"Light and shade", paragraph before the paired charts):**
> "For each tension, we measured via classifiers how many people discussed the benefit (\"light\") or the harm (\"shade\") side substantively anywhere in their interview, and whether they were speaking from some personal experience (darker bars) or anticipation (lighter bars). We also looked at how this varied by stated job category."

**Light and shade — the chart definition and the experience rule (caption under the paired bar charts):**
> "In these paired bar charts, each bar shows the share of respondents who were excited about the benefit on the left, vs. worried about the harm on the right—split into those who've experienced it firsthand (darker) and those who anticipate it (lighter). Firsthand experience can also include firsthand observation, but does not include e.g. news reports."

**The nine vision categories, verbatim definitions (§"What people hope for"; identical text ships in the statistics file):**
> - Professional excellence — "Improve effectiveness and lean into more meaningful work by having AI handle routine tasks so they can focus on higher-value strategic work, complex problem-solving, and professional mastery."
> - Personal transformation — "Achieve personal growth, emotional wellbeing, or life transformation with AI as guide, coach, or support — e.g. self-understanding, behavior change, therapeutic support, companionship, improvements in physical or mental health."
> - Life management — "AI as comprehensive organizational support and cognitive scaffolding — e.g. managing schedules, reducing mental burden, executive function support."
> - Time freedom — "Reclaim time from work and chores to be present with family or friends, pursue hobbies, travel, rest."
> - Financial independence — "Achieve financial freedom or economic security through AI — e.g. income generation, business building, investments, passive income, or otherwise escaping economic constraints."
> - Societal transformation — "Solve major societal challenges — e.g. poverty, disease, climate, inequality — using AI for broad human flourishing rather than personal gain."
> - Entrepreneurship — "Build, launch, and scale businesses with AI as force multiplier — e.g. product development, business automation, or solopreneurship but with team-level capacity."
> - Learning & growth — "Use AI as learning accelerator and personalized teacher — acquire knowledge, develop skills, master complex subjects, satisfy intellectual curiosity."
> - Creative expression — "Use AI to help bring creative visions to life — e.g. art, games, music, films, books — by overcoming barriers between imagination and execution."

**The seven experience categories, verbatim definitions (§"Where AI has delivered on their vision"):**
> - Productivity — "AI dramatically sped up work and automated repetitive tasks — e.g. building features in hours instead of days, drafting, summarizing, data processing, streamlining routine operations."
> - AI hasn't delivered — "AI fell short of expectations (e.g. inaccurate or unreliable outputs) or isn't yet capable of — or being used for — what they envision."
> - Cognitive partnership — "AI served as a thinking partner or creative collaborator — e.g. brainstorming, refining ideas, working through problems together."
> - Learning — "AI helped learn a new skill or subject — e.g. adaptive explanations, patient tutoring, on-demand expertise in unfamiliar domains."
> - Technical accessibility — "AI enabled building something previously out of reach — e.g. non-developers shipping apps, solo creators doing team-scale work."
> - Research synthesis — "AI helped synthesize research or process large volumes of information — e.g. literature review, distilling sources, making sense of complex material."
> - Emotional support — "AI provided emotional support, personal guidance, or a judgment-free space to talk — e.g. processing difficult situations, advice, companionship."

**The thirteen charted concern categories, verbatim definitions (§"What people worry about"):**
> - Unreliability — "Concern about e.g. hallucinations, inaccuracy, fake citations, verification burden defeating the purpose."
> - Jobs & economy — "Concern about AI causing job displacement, unemployment, economic inequality, wage stagnation, or negative impacts on workers and the economy."
> - Autonomy & agency — "Concern about loss of human autonomy — e.g. AI making decisions without oversight, humans becoming passive, forced AI adoption."
> - Cognitive atrophy — "Concern about e.g. over-reliance causing skill loss, intellectual passivity, students bypassing learning, critical thinking decline."
> - Governance — "Concern about e.g. lack of legal/regulatory frameworks, no clear liability when AI causes harm, insufficient democratic oversight."
> - Misinformation — "Concern about e.g. deepfakes, AI-generated misinformation, erosion of shared reality, propaganda at scale."
> - Surveillance & privacy — "Concern about e.g. mass surveillance, privacy violations, data exploitation, authoritarian control, tracking and profiling."
> - Malicious use — "Concern about malicious use by bad actors — a wide-ranging category including hacking, cyberattacks, scams, fraud, weapons, autonomous military applications, bioweapons."
> - Meaning & creativity — "Concern about AI replacing life purpose and/or creative work — e.g. human expression devalued, what are humans for?"
> - Overrestriction — "Concern that AI is too restricted — e.g. excessive safety measures, paternalistic content filtering, blocking legitimate use cases."
> - Wellbeing & dependency — "Concern about e.g. social isolation, loneliness, negative psychological impacts, compulsive AI use, preferring AI companions to humans."
> - Sycophancy — "Concern that AI is too permissive or agreeable, and encourages delusions rather than pushing back."
> - Existential risk — "Concern about e.g. AI becoming uncontrollable, superintelligent, misaligned with humanity, or posing extinction risk."

**Ten further concern categories that exist in the published label set but are not charted or given a share on the page (chart data asset):**
> - Economic displacement — "Concern about e.g. job loss, unemployment, entry-level positions disappearing, being replaced by AI, wealth concentration, digital divide."
> - Underrestriction — "Concern that AI doesn't have enough guardrails — e.g. enables harmful outputs, insufficient ethical filters."
> - Bias & discrimination — "Concern about AI encoding social bias; unfair or discriminatory outputs."
> - Environmental — "Concern about e.g. energy consumption, carbon footprint, climate impact of AI infrastructure."
> - IP & data rights — "Concern about e.g. data ownership, training on copyrighted content."
> - Market concentration — "Concern about e.g. corporate monopolies, big tech power, lack of competition, profit over user welfare."
> - Children & vulnerable — "Concern about e.g. impact on children, youth, elderly, or other vulnerable populations."
> - Geopolitics — "Concern about e.g. international competition or geopolitical dynamics."
> - Democracy — "Concern about AI's impact on democratic processes, e.g. political polarization, manipulation of public opinion, erosion of institutional trust."
> - Other concern — "Concern about AI that doesn't fit any of the defined categories."

Note for anyone building on this taxonomy: **"Jobs & economy" (charted, 22.3%) and "Economic displacement" (uncharted) are two separate categories in the same label set**, and the light-and-shade tension uses the *name* "Economic displacement" for its shade side (17.7%). Whether the tension's shade side is that concern code, a purpose-built classifier, or the jobs-and-economy code restricted to displacement language is not stated on the page. The appendix is the place to check.

### Sample rules, consent and de-identification

**Sample frame (lead-in paragraph):**
> "Over one week in December, we invited everyone with a Claude.ai account to sit down with Anthropic Interviewer"

**Consent and publication (§"Seeing the forest and the trees"):**
> "Before choosing to participate, users were informed their responses would be used for research, and that Anthropic might publish responses with personally identifying information removed in findings. All responses were de-identified before being analyzed by a small team of researchers at Anthropic, and quotes selected for publication underwent further manual review for removal of any potentially identifying details, to help protect the privacy and public anonymity of interviewees."

**What "AI" means in the answers (§"Seeing the forest and the trees"):**
> "Answers were reflective of AI usage broadly (i.e. not just Claude), though we redacted names of other AI products."

This sentence is the single most consequential definitional statement on the page for our naming rule: respondents were talking about AI in general, while the sample is Claude users and many quotes name Claude.

**The one exclusion rule stated (§"Light and shade", caveats paragraph):**
> "though we filter out those who don't answer the concerns question, they may have put in less effort later in the interview"

**Occupation (§"Seeing the forest and the trees" and §"Light and shade"):**
> "what they do for a living (if mentioned)"

> "We also looked at how this varied by stated job category."

Job category is therefore self-described, optional and classified from free text. The page names these categories in prose and quote attributions — students, teachers, academics, tradespeople, lawyers, healthcare workers/professionals, high-stakes professions ("law, finance, government, and healthcare"), freelancers, freelance creatives, self-employed researchers, entrepreneurs, small business owners, "employees with side projects", institutional employees, "people not currently working" — but publishes **no list of categories and no counts**. The Quote Wall data file carries 33 distinct self-descriptions, including employment-form prefixes ("Freelance…", "Self-employed…") **(chart data asset)**; whether that is the classifier's taxonomy or only the quote metadata is not stated.

**Where the method detail lives (§"Seeing the forest and the trees"):**
> "The Appendix describes our methods in more detail, as well as limitations and some additional analysis."

## Data and methods

In the wiki author's words, with section references.

**One week, one instrument, one population.** Every Claude.ai account holder was invited during a single week in December (year unstated; December 2025 by inference from the March 2026 publication date and "Last December"). Those who accepted talked to Anthropic Interviewer, a Claude instance prompted to run a conversational interview with a fixed question spine and adaptive follow-ups. 80,508 people completed an interview, across 159 countries and 70 languages. There is no random sampling, no quota, no invitation-to-response accounting and no weighting: the sample is self-selected from a self-selected population, which the page acknowledges (see `Limitations`).

**Three questions carry almost all the quantities.** The vision share comes from "If you could wave a magic wand, what would AI do for you?"; the experience share from "Has AI ever taken a step towards that vision for you?"; the concern shares from "Are there any ways in which AI could be developed that would be contrary to your vision or what you value?" The order is fixed and disclosed — visions first, then concerns "that would counter their vision" — which the page itself names as a possible driver of the light-and-shade co-occurrence.

**Claude does the coding.** Claude-powered classifiers assign each transcript: one primary vision category out of nine; up to seven experience categories (the page says six areas and lists seven, one of which is the absence of a benefit); concern categories from a label set of at least twenty-three, multi-label, of which thirteen are charted; a self-described job category where the respondent mentioned one; and an overall sentiment score on a 1–7 Likert scale, dichotomised at ≥5 into "net positive". Claude also selects representative quotes. No inter-rater agreement, human-validation exercise, prompt text or classifier version is reported on the page; the appendix is where such detail would sit.

**The light-and-shade layer is a separate pass.** Five benefit/harm pairs were each measured by classifiers looking for substantive discussion of either side **anywhere in the interview** — not only in the answer to the corresponding question — together with a binary judgement of whether the speaker was drawing on personal experience (including observation, excluding news reports) or anticipating. That gives, per pair, a light share, a shade share, an either-side share, and a lived/hypothetical split within each side. Co-occurrence within the person is then compared to a baseline rate, and reported on the page as multiples (1.6× to 3.0×) and for one pair as a correlation (+0.16 against a +0.25 average). The correlations themselves are in the appendix.

**Geography.** Respondents are grouped into twelve regions; the page publishes a region-level card (negative-sentiment rate and jobs-and-economy concern rate), a region-level scatter of those two quantities, a country bubble map of net-positive sentiment, and slope charts of vision and concern rankings for selected region pairs. The country map and both slope-chart sets are client-rendered and showed "Loading data..." / "Loading…" in the fetched text, so their values are not available from the page text.

**What the published data assets contain.** The statistics file behind the charts carries, for the global sample, each of the twelve regions, 125 countries and 51 US state-level units (50 states plus DC): respondent count, net-positive sentiment rate, the thirteen concern shares, the nine vision shares, the seven experience shares, an `ambivalence` figure, and a `concernScores.jobs_economy` figure; plus the five light-and-shade rows with counts and lived/hypothetical splits, and the full verbatim label set for visions, experiences and concerns. Two grains in that file are **never used on the page**: US states, and per-country vision/experience/concern breakdowns. Whether respondent counts at those grains are large enough to support claims is a question for the data steward, not for this file — 60 of the 125 countries have fewer than 100 respondents and the smallest US state cell is in the teens. The page states no minimum-cell rule.

**What is not released.** No transcripts, no respondent-level records, no classifier outputs and no code. The 620 quotes in the Quote Wall file are the only respondent-level material published, each with country, region, optional self-described job, tag list and a `rough_mem_score` field that the page never explains. Unlike the Economic Index releases and the labour-market paper, this publication has **no Hugging Face dataset**: the separate Anthropic Interviewer publication has one (`https://huggingface.co/datasets/Anthropic/AnthropicInterviewer`), and whether these 80,508 interviews are covered by it is a question for the steward and the appendix, not answered here.

**Relation to the Economic Index.** None methodologically. The page draws the line itself: usage analysis says what people do, interviews say why. No respondent is linked to observed usage anywhere in this article, and no Index construct (task, occupation, collaboration pattern, AUI) appears in it. The linked economics write-up (`survey-81k-economics-2026-04`) is where those joins are attempted; this feature does not mention it.

## Limitations (verbatim)

**On the sample and the instrument — the page's own caveats paragraph (§"Light and shade"):**
> "There are some caveats worth naming. These are active Claude users who'd already found enough value to keep using AI, and our interview asked first for positive visions for AI and then for concerns that would counter their vision. Both factors may lead to interviewees lingering on explicit tensions, as well as on the positive (though we filter out those who don't answer the concerns question, they may have put in less effort later in the interview)."

**Its own defence against the instrument explanation, in the same paragraph:**
> "But the instrument can't explain everything. If interview structure were driving the co-occurrence, you'd expect it to be roughly uniform across all five tensions and all groups. Instead the co-occurrence ranges from 1.6 to 3.0 times, and some of the tensions are notably asymmetric across different groups of people. One might also expect enthusiasts to defend their desired use case, instead of acknowledging the downsides. Instead, those who were excited about emotional support from AI were more concerned about what would happen if their vision came *true*—if they got what they wanted, they might become *too* dependent on AI—than about being prevented from achieving that vision."

**On selection in the geographic result (§"How perspectives vary around the world"):**
> "Claude.ai users are likely biased towards early AI adopters who are more excited about new technologies"

**On adoption stage as an explanation for the same result:**
> "But there is also less market penetration in these regions—if AI hasn't visibly entered your daily work yet, AI displacement likely feels abstract, especially when more immediate economic pressures already exist."

**On what the speculative harms do and do not mean (§"Light and shade"):**
> "That the systemic concerns remain speculative is not a verdict on AI's ultimate impact as much as a reflection of how early we are in its adoption."

**On the ambiguity of the qualitative evidence (§"Are people getting what they want?"):**
> "There is real ambiguity about how to interpret the diversity of stories we heard: as wins for human wellbeing, as double-edged swords, or as band-aids for broader institutional failures. In truth, it's probably some combination of all three."

**On salience versus frequency (§"Are people getting what they want?"):**
> "Emotional support comprised only 6% of responses, but these were among the most affecting we encountered."

**On non-response to the vision question (caption under the visions chart):**
> "1% of respondents did not articulate a vision."

**On what "AI" refers to in the answers (§"Seeing the forest and the trees"):**
> "Answers were reflective of AI usage broadly (i.e. not just Claude), though we redacted names of other AI products."

**On occupation being optional (§"Seeing the forest and the trees"):**
> "what they do for a living (if mentioned)"

**On the maturity of the method (§"Conclusion"):**
> "This is a new form of social science. It is qualitative research at a massive scale, and we're in the early stages of learning how to do it."

**On the standing of the whole exercise (§"Conclusion"):**
> "One of our goals for this research is to offer a complement to the abstractions we all tend to use in speaking about AI; to capture the texture that more vividly renders exactly how we are already experiencing these opportunities and risks worldwide."

**On an inference drawn from one region, flagged as qualitative (§"Where do particular visions for AI most resonate?"):**
> "From a qualitative review of these users' quotes, one interesting trend is that people often connected financial independence explicitly to family obligations and filial piety"

**On a claim the page corrected after publication (Corrections):**
> "Mar 19, 2026. \"Globally, 67% of people view AI positively\" changed to \"Globally, 67% of interviewees expressed net positive sentiment toward AI\" to more precisely describe the study's methodology."

**Deferred by the page itself (§"Seeing the forest and the trees"):**
> "The Appendix describes our methods in more detail, as well as limitations and some additional analysis."

The appendix's limitations are not reproduced here; see `wiki/reports/survey-81k-interviews-2026-03-appendix.md`.

## Open questions, conjectures and promised follow-ups (verbatim)

**The gap this research says is missing from the debate (lead-in paragraph):**
> "Public conversation about AI often centers on abstract projections of its risks and benefits. What's largely missing is a vision for what \"AI going well\" means, grounded in the concrete aspirations of people around the world who already use AI and have begun developing a sense of what it might do for them."

**The promise of new questions (§"Looking forward"):**
> "These interviews give us a sense of what people want from AI broadly, which informs how we build Claude. They reinforced the importance of work we're already doing, and pointed us toward new questions to ask."

**Promised follow-up study, already launching (§"Looking forward"):**
> "Our next Anthropic Interviewer study, launching shortly to a small subset of Claude users, focuses on Claude's effects on people's wellbeing over time: whether Claude is actually making people's lives better in the ways they want, and how it could do so more effectively."

**Promised programme work against the societal-transformation vision (§"Looking forward"):**
> "Through our Beneficial Deployments program, we're collaborating with our AI for Science and nonprofit partners to understand how they use Claude and where it still needs to improve, to close the gap between the societal transformations people envision and today's reality."

**Promised economics research, with this article's concern data as the trigger (§"Looking forward"):**
> "We also take some of the most-cited concerns—e.g. around negative economic impacts of AI—seriously, as signals around which we are designing further research and updating our thinking."

**Untested conjecture about where AI-for-learning works (§"Light and shade"):**
> "This suggests AI's benefits may be strongest when learning is volitional, compared to within institutional structures where AI is more likely to be used as a shortcut."

**Untested conjecture about why educators see atrophy (§"Light and shade"):**
> "Troublingly, educators were 2.5-3 times more likely than average to report having witnessed cognitive atrophy firsthand, presumably in their students."

**Untested conjecture about why the self-employed feel both sides (§"Light and shade"):**
> "Without an institutional layer to buffer the new pace, they both get the gains and feel the squeeze."

**Untested conjecture about calibration (§"Light and shade"):**
> "The same occupational patterns hold when you look at who's excited, regardless of experience, suggesting that optimism here is well-calibrated."

**Four competing explanations offered for the income gradient in sentiment, none adjudicated (§"How perspectives vary around the world"):**
> "There are several possible explanations for the more positive AI sentiment in lower and middle income countries."

**Untested conjecture about what the regional vision differences mean (§"Where do particular visions for AI most resonate?"):**
> "It seems that wealthier, more AI-exposed regions more want AI to *manage the complexity of life*; developing regions more want AI to *create more opportunity.*"

**Untested conjecture about the regional concern split (§"Where do particular concerns around AI most resonate?"):**
> "The West worries about who owns and controls AI; East Asia worries more about the personal implications of its use."

**Untested conjecture about the mechanism behind the entrepreneurship vision (§"Where do particular visions for AI most resonate?"):**
> "In these regions, AI is framed as a capital bypass mechanism—a way to start businesses without the funding, hiring, or infrastructure that would otherwise be required."

**The unresolved interpretive question about emotional use (§"Are people getting what they want?"):**
> "These observations also hint at the duality of our experience with AI systems. While some see it as filling gaps in human connections, others see AI as a substitution—even a welcome replacement—for them."

**The question the article ends on (§"Conclusion"):**
> "The usefulness is real, and the question for all of us is how to claim the benefits without incurring undue costs."

**Method development stated as ongoing (§"Conclusion"):**
> "This is a new form of social science. It is qualitative research at a massive scale, and we're in the early stages of learning how to do it."

**The division of labour it proposes between instruments (§"Conclusion"):**
> "Surveys and usage *analysis* tell us *what* people are doing with AI, but the open-ended interview format helps us get at *why*."

## What it did not test

The wiki author's inference, **not** the page's claims. Each item is something the page's own text leaves open, or a cut its published quantities would permit and it does not take. Items whose answer might sit in the appendix are marked *(check appendix)*.

1. **Stated hopes and fears against observed behaviour.** Not one number here is joined to usage. The article never links a respondent's interview to that person's Claude usage — task mix, collaboration pattern, intensity, tenure or plan — even though both sides exist inside Anthropic and the article's closing sentence sets interviews beside "usage analysis". Whether any join is even possible at respondent level is a question for the steward and the appendix *(check appendix)*.

2. **Any external benchmark.** The sentiment result (67% net positive) is never set against a nationally representative survey of AI attitudes in any country, and the concern taxonomy is never mapped onto an existing instrument. Without that, the claim that emerging economies are "reliably more positive" cannot be separated from the composition of Claude's user base — which the page names as a candidate explanation and does not test.

3. **Non-response.** The invited population is "everyone with a Claude.ai account"; the respondent count is 80,508. The page gives **no invited total, no response rate, and no comparison of respondents to non-respondents** on any observable. A one-week, opt-in, conversation-length instrument plausibly selects on engagement, and nothing here bounds that *(check appendix)*.

4. **The one stated exclusion.** Interviews without an answer to the concerns question are filtered out; the count is never given, and neither is what those respondents looked like on the vision question they did answer.

5. **Reconciliation of its own denominators.** 80,508 took the interview, 79,734 sits behind the shares and 72,105 behind the light-and-shade rows **(chart data asset)**. The page publishes percentages without stating which base any of them uses, so no reader can recover a count from a published share *(check appendix)*.

6. **Classifier validity.** Nine visions, seven experiences, twenty-three-plus concerns, five tensions, one lived/anticipated binary and a 1–7 sentiment scale, all assigned by Claude, and no agreement statistic, human audit, confusion analysis or prompt text on the page. For a study whose every number is a classifier output, this is the largest untested link in the chain *(check appendix)*.

7. **Classifier behaviour across 70 languages.** The study's headline distinction is that it is the most multilingual qualitative study yet conducted, and it reports no per-language performance, no translation step, no check that "cognitive atrophy" or "sycophancy" are coded alike in Korean, Portuguese and Arabic. Since the regional findings are the paper's most quotable, differential classifier behaviour by language is a live alternative explanation for them *(check appendix)*.

8. **Where the taxonomies came from.** Whether the nine visions and the concern label set were induced from the transcripts, written in advance, or both, is not stated. Nor is why ten of the twenty-three concern categories receive no charted share, why six of those ten appear only in the prose "long tail" with integer percentages, and why the remaining four appear nowhere on the page at all.

9. **The relationship between its two economic categories.** "Jobs & economy" (22.3%), the uncharted "Economic displacement" code, and the shade side of the economic tension (17.7%) are three quantities with overlapping names, and the page never states how they relate. Any post building on the economic concern must settle this first *(check appendix)*.

10. **The predictor claim.** "Concern about jobs and the economy was the strongest predictor of overall AI sentiment" is asserted twice with no model, no competing coefficients, no controls and no fit statistic. Whether it survives controlling for region, income level, occupation or usage is untested — and the region-level scatter that illustrates it has twelve points *(check appendix)*.

11. **Whether the light-and-shade co-occurrence survives conditioning.** "Three times more likely" and the 1.6–3.0× range are unconditional. Occupation, region and adoption stage all shift both sides of every tension in this article's own numbers, so the within-person entanglement is not shown to be anything more than shared composition. The page argues against the instrument explanation; it does not argue against the composition explanation.

12. **Question order, tested rather than argued.** The article concedes that asking for hopes first and then counter-hopes may inflate the tensions, then rebuts it by noting the co-occurrence is not uniform. No randomisation of question order, no alternative phrasing, no split-sample and no control arm — all of which are available to an AI interviewer at this scale, and none of which was run here.

13. **Interviewer effects.** The interviewer is Claude, asking about AI, inside a Claude product, with adaptive follow-ups whose content is not published. Acquiescence toward the interviewing system, and the effect of the adaptive probe recorded in claim 10, are never bounded.

14. **The occupational findings' denominators.** The article's sharpest economic contrast — 47% of independent workers against 14% of institutional employees reporting lived economic empowerment, 58% for employees with side projects, 23%/17% for freelance creatives — rests on self-described, optionally mentioned job categories with **no published counts, no category list and no uncertainty**. Small-cell noise cannot be ruled out from the page *(check appendix)*.

15. **Whether "independent worker" is a category or a selection.** The same self-employment that predicts lived economic gain also predicts having something to gain from AI, being an early adopter, and interviewing at length about it. The page reads the pattern as calibrated optimism; the alternative reading — that the people who chose exposure to AI's upside are the ones who report it — is not addressed.

16. **The geography the data would support.** The published asset carries vision, experience, concern and sentiment shares for 125 countries and 51 US state-level units; the article uses only twelve regions, plus one uncoloured country map **(chart data asset)**. No country-level result, no US-state result, no test of the income gradient on country-level income data, and no minimum-cell rule are anywhere on the page. Sixty of those 125 countries have fewer than 100 respondents, which is precisely why the omission matters, and precisely what a noise check would have to establish. Cell sizes at those grains are the steward's to confirm.

17. **The caption's own "no country dips below 60%".** On the published asset, five countries sit below 0.60 net-positive sentiment, one of them with 212 respondents **(chart data asset)**. Either an unstated display threshold governs the map or the caption overstates; the page gives no way to tell *(check appendix)*.

18. **Anything over time.** One week, one cross-section. The article's central dynamic claim — that systemic harms are still anticipated rather than lived because "how early we are in its adoption" — is a statement about a trend measured once. The promised wellbeing panel is named as the follow-up, not run here.

19. **Whether stated visions predict anything.** Nobody's vision is tested against later retention, spend, task mix, occupational change or reported wellbeing. The nine categories are a description of what people say they want, and the article's interest in "AI going well" implies a criterion they are never scored against.

20. **The 81% as a satisfaction measure.** "Has AI ever taken a step towards that vision for you?" has an extremely low bar — *ever*, *a step* — and 81% clear it. No intensity, frequency, magnitude or counterfactual is asked, and the complement is reported as a content category ("AI hasn't delivered") rather than as a rate, which makes the two halves of the same question look like items on one list.

21. **Whether the 19% who say AI has not delivered are the disappointed or the ambitious.** The category mixes capability failure ("inaccurate or unreliable outputs") with scope mismatch ("isn't yet capable of — or being used for — what they envision"), and the page never splits them, though the distinction decides whether the number is about the product or about expectations.

22. **Composition behind the regional sentiment gradient.** No adjustment for occupation, age, education, plan type or usage intensity, none of which are published at any grain. The four candidate explanations the page lists are compatible with a purely compositional story.

23. **The quote-selection pipeline as a source of bias.** Claude selected representative quotes; 620 are published with a `rough_mem_score` the page never defines **(chart data asset)**. Whether the quoted material is representative of its category — and what that score measures — is untested and unexplained.

24. **Any link to the Economic Index constructs.** No task, occupation, SOC code, collaboration pattern or AUI appears here, so this article cannot be joined to any Index release without an intermediate mapping that nobody has built. That mapping — not this article's numbers — is the interesting gap for our programme, and the companion economics write-up (`survey-81k-economics-2026-04`) is where to check how far Anthropic has already closed it.

## Verification

- **Fetched 2026-09-16.**
  - https://www.anthropic.com/features/81k-interviews — HTTP 200. Fetched twice: once through `web_fetch` (rendered markdown, read in full: body, all category lists and definitions, all captions, every embedded quote, the authorship section, bibtex, footnote 1 and the Corrections block), and once with `curl` to the raw HTML (716,870 bytes; 1,215 lines of extracted visible text, read in full) to recover the region card's numbers, which the rendered fetch ran together, and to check for alt text.
  - Chart data assets, all HTTP 200: `https://cdn.sanity.io/files/4zrzovbb/website/a9cde041d15765c23813279f5ccde115bd40f29a.json` (279,115 bytes; global / byRegion / byCountry / byState / regionToCountries / countryToRegion / regionNames / concernKeys / visionKeys / experienceKeys / labels / lightShade); `…/9ac19583d019b85db5ca3af485f419f74f3fe4a5.json` (12,931 bytes; the quotes shown beside the vision, experience, concern and light-shade charts); `…/b9f944c5ea6207dd80c7204544457960642eda46.json` (217,629 bytes; 620 Quote Wall entries); and three TopoJSON basemaps, `…/c20ea6ec0dc231d3559c6d0fbcdae4f6a05fdd06.json` (114,554 bytes), `…/84a98701143179854ab37e32eac9c87611782429.json` (901,608 bytes), `…/cca8d23a9104ef0fc87b518ec18565aa8af41205.json` (885,646 bytes). The basemaps contain geometry only and no respondent data.
- **Fetch failures:** none.
- **Not fetched, by instruction:** the appendix PDF, https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf. It is a separate slug (`survey-81k-interviews-2026-03-appendix`); every deferral above is marked as such rather than filled in from it. Also not fetched: the four Anthropic pages linked from the body and the Anthropic Interviewer publication, each of which is its own slug or belongs to `programme-and-product-pages.md`.
- **Alt text:** none. The raw HTML contains **no `alt` attributes at all** — the only alt-like strings are the Open Graph and Twitter card metadata ("What 81,000 people want from AI"). The director's alt-text ruling therefore has nothing to bite on in this entry.
- **Images and client-rendered charts.** No number in this file was read off a chart image. Three page elements did not render in either fetch: the country sentiment bubble map (element text "Loading data..."), the vision slope charts and the concern slope charts (both "Loading…"). Their captions are recorded; their values are not. The hero visualisation is client-rendered and yields only its unit caption.
- **Use of the chart data assets — provenance and the applicable rulings.** Twenty places in this file carry a number or label from the statistics file, each marked `(chart data asset)`. The reasoning: these are published values shipped with the article, not numbers read off an image. `room/director-2026-09-16-figure-values-ruling.md` permits a value "printed as a data label inside a figure" to be recorded in `wiki/reports/` when marked `(figure label)`; a value shipped in the page's own data file is the same kind of object one step earlier in the pipeline, so `(chart data asset)` is used by direct analogy, and `room/director-2026-09-16-caption-amendment.md`'s bar on chart-read numbers is respected (nothing here was read off an image). The dependency matters: three of the entry's most useful facts — the taxonomy's ten uncharted concern categories, the three different denominators, and the inverted sign of the region card — cannot be established without them. No arithmetic was performed on them beyond the subtraction needed to establish that the region card's "AI sentiment" column is a negative-sentiment rate (Western Europe 0.644 → 35.6%, North America 0.655 → 34.5%, Sub-Saharan Africa 0.758 → 24.2%, each matching the card exactly). Confirmation is sought in `room/lead-2026-09-16-wiki-survey-81k-interviews-2026-03.md`; if the director rules these out of scope, the marked passages come out and `Claims` 39 and 41 and `What it did not test` 5, 16, 17 and 23 lose their support.
- **Quotation check.** Every passage in quotation marks in `Definitions`, `Limitations` and `Open questions`, and every quoted passage in `Claims`, was checked string-for-string against the fetched renderings after normalising whitespace, curly quotes, hyphens and dashes: 205 distinct quoted passages, all matched — 195 against the page text, and 10 (the uncharted concern definitions) against the label set in the statistics file, where they are the only place they appear. Where the page's own emphasis (italic *better*, *faster*, *why*, *what*, *true*, *while*, *manage the complexity of life*) falls inside a quotation it is preserved. Two source oddities are reproduced deliberately: the stray comma in "answers to the question , \"Are there any ways…\"" (concerns caption) and the non-breaking hyphen in "open-ended" in the opening scrolly text.
- **Internal discrepancies recorded, not resolved:** (i) no dateline on the page — bibtex 2026-03-18, correction 2026-03-19, `wiki/INDEX.md` 2026-03-19; (ii) 81,000 / 80,508 / 79,734 / 72,105; (iii) "six main areas" against a seven-item list; (iv) illusory productivity 18% (chart) against 19% (prose); (v) the region card headed "AI sentiment" carrying negative-sentiment rates; (vi) "Central Asia n=~0,000"; (vii) the map caption's "no country dips below 60%" against five sub-60% countries in the asset; (viii) the bibtex author list being longer than the prose acknowledgement; (ix) "Jobs & economy" against "Economic displacement" as separate codes with overlapping definitions.
- **No data files in the repository were opened**, and no released Economic Index file was touched, in keeping with `team/agents/programme-lead.md` and `room/director-2026-09-16-alt-text-ruling.md`. The two questions this entry raises that data would settle — whether these interviews appear in the `Anthropic/AnthropicInterviewer` dataset, and what respondent counts at country and US-state grain support — are put to the steward in the accompanying room note.
- **Cross-file consistency.** Slug, title, type, primary URL and appendix URL match the row for `survey-81k-interviews-2026-03` in `wiki/INDEX.md`; the date differs from the bibtex as recorded above. `wiki/INDEX.md` was not edited in this thread.
