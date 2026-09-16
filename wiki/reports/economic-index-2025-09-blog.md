# economic-index-2025-09-blog

## Source

- **Title:** "Anthropic Economic Index: Tracking AI's role in the US and global economy" (H1 on page). Browser/social title: "Economic Index: AI's role in the US and global economy".
- **Date:** Sep 15, 2025 (dateline on page).
- **URL:** https://www.anthropic.com/research/economic-index-geography
- **Document type:** Research blog post on anthropic.com/research, tagged "Economics". No PDF, no author byline, no citation block, no bibliography. Three numbered footnotes. One hero image, one embedded video, ten data figures, each with a one-line italic caption; several figures carry descriptive alt text containing numbers not stated in the body.
- **Approximate length:** ~1,900 words of body text plus 3 footnotes (wiki author's estimate from the fetched text).
- **What it accompanies:** the third Anthropic Economic Index report, "Anthropic Economic Index report: Uneven geographic and enterprise AI adoption" (same date, https://www.anthropic.com/research/anthropic-economic-index-september-2025-report; wiki slug `economic-index-2025-09-report`), which this page explicitly summarises: "We summarize [the report](http://anthropic.com/research/anthropic-economic-index-september-2025-report) below." It also accompanies the interactive Economic Index site (anthropic.com/economic-index) and the open data release ("we've made our dataset [openly available](https://huggingface.co/datasets/Anthropic/EconomicIndex)"), i.e. the `release_2025_09_15` folder of `Anthropic/EconomicIndex`.
- **Meta description (page head):** "New research from the Anthropic Economic Index exploring geographic patterns of AI use across the US and the global economy."
- **Section order on the page:** lead (untitled) → Geography (Across countries; Patterns within the United States) → Trends in Claude use (Tasks; Patterns of interaction) → Businesses → Conclusion → Open data → Work with us → Footnotes.

## Claims

Reference convention: the page has no page numbers, so each claim carries its H2/H3 heading, and "fig. caption" or "fig. alt text" where the number appears only there. Numbers are given exactly as published on this page.

**Lead (untitled)**

1. Travel planning in Hawaii, scientific research in Massachusetts and building web applications in India are "some of the *most overrepresented*" uses of Claude in those places. Comparison: a place's share of conversations containing a use against the share elsewhere / the global average. No values given on this page. *(Lead)*
2. "software engineering is still by far in the lead in almost every state and country in the world" — i.e. overrepresentation is not popularity. Comparison: within-place ranking of uses. *(Lead)*
3. Claude users in Brazil "use Claude for translation and language-learning about six times more than the global average" — **~6x**. Comparison: Brazil's share of conversations in that use against the global share. *(Lead)*
4. Within the US, "the composition of states' economies informs which states use Claude the most per capita – and, surprisingly, that the very highest-use states *aren't* the ones where coding dominates." Comparison: per-capita-use ranking of states against the coding share of each state's use. *(Lead, bullet 1)*
5. "countries' use of Claude is strongly correlated with income, and that people in lower-use countries use Claude to automate work *more* frequently than those in higher-use ones." Comparison: cross-country, AUI against GDP per capita, and automation share against per-capita use. *(Lead, bullet 2)*
6. "the proportion of 'directively' automated tasks increased sharply from **27% to 39%**, suggesting a rapid increase in AI's responsibility (and in users' trust)." Comparison: the Dec 2024–Jan 2025 wave against the August 2025 wave, with Feb–Mar 2025 in between. *(Lead, bullet 3)*
7. "API users are significantly more likely to automate tasks with Claude than consumers are, which suggests that major labor market implications could be on the horizon." Comparison: first-party API sample against Claude.ai sample. *(Lead, bullet 4)*
8. The interactive site covers "every US state and all occupations we track". *(Lead)*

**Geography → Across countries**

9. "The US uses Claude far more than any other nation. India is in second place, followed by Brazil, Japan, and South Korea, each with similar shares." Comparison: countries' shares of global Claude.ai use. *(Across countries)*
10. The US share of global Claude use is **21.6%**. This number appears on this page only in the figure alt text: "Top 30 countries by share of global Claude use: the US leads with 21.6%." The body text gives no share values; the caption reads "Leading countries in terms of global Claude.ai use share." *(Across countries, fig. alt text)*
11. The five highest-AUI countries are Israel, Singapore, Australia, New Zealand and South Korea — again only in the alt text: "The twenty countries that score highest on our Anthropic AI Usage Index: Israel, Singapore, Australia, New Zealand, and South Korea are the top five." No AUI values are given anywhere on this page except DC's 3.82. *(Across countries, fig. alt text)*
12. "some small, technologically advanced countries (like Israel and Singapore) lead in Claude adoption relative to their working-age populations." Comparison: AUI ranking. *(Across countries)*
13. "we found a strong correlation between GDP per capita and the Anthropic AI Usage Index (a **1%** higher GDP per capita was associated with a **0.7%** higher AUI)." Comparison: cross-country elasticity of AUI with respect to GDP per capita. No standard error, R², or country count on this page. *(Across countries; fig. caption "Claude use per capita is positively correlated with income per capita across countries. (Axes are on a log scale.)")*
14. Mechanism offered, not tested on this page: "the countries that use Claude most often generally also have robust internet connectivity, as well as economies oriented around knowledge work rather than manufacturing." *(Across countries)*

**Geography → Patterns within the United States**

15. "a **1%** higher per capita GDP inside the US is associated with a **1.8%** higher population-adjusted use of Claude" — i.e. the within-US elasticity (1.8) exceeds the cross-country one (0.7). Comparison: US states, AUI against state GDP per capita. *(Patterns within the United States)*
16. "income actually has *less* explanatory power within the US than across countries, as there's much higher variance within the overall trend." No R² given on this page. Comparison: fit of the within-US regression against the cross-country one. *(Patterns within the United States)*
17. "The highest AUI in the US is the District of Columbia (**3.82**), where the most disproportionately frequent uses of Claude are editing documents and searching for information, among other tasks associated with knowledge work in DC." The only AUI value stated in the body of this page. *(Patterns within the United States)*
18. "coding-related tasks are especially common in California (the state with the third-highest AUI overall), and finance-related tasks are especially common in New York (which comes in fourth)." Comparison: a state's share of a task category against the US as a whole; AUI rank. *(Patterns within the United States)*
19. Utah ranks second on AUI among US states. Stated only in the figure alt text ("with Utah and DC in the lead") and in footnote 1 ("As for Utah, in second"). *(Patterns within the United States, fig. alt text + footnote 1)*
20. "people in Hawaii request Claude's assistance for tourism-related tasks at **twice** the rate of the rest of America." Comparison: Hawaii's share of tourism-related tasks against the rest of the US. *(Patterns within the United States)*
21. Footnote 1 on Utah: "a notable fraction of its use appeared to be associated with indicators of coordinated abuse – which is also reflected in Utah's much higher "directive" automation score than average. However, we ran robustness checks and believe that this activity is not driving the results." No robustness check is described. *(Footnote 1)*

**Trends in Claude use → Tasks**

22. "Since December 2024, computer and mathematical uses of Claude have predominated among our categories, representing around **37-40%** of conversations." Comparison: across the three waves, share of conversations by O*NET/SOC group. *(Tasks)*
23. "educational instruction tasks have risen by **more than 40 percent** (from **9% to 13%** of all conversations)". Comparison: first wave against latest wave. *(Tasks)*
24. "the share of tasks associated with the physical and social sciences has increased by **a third** (from **6% to 8%**)". Comparison: as above. *(Tasks)*
25. "management-related tasks have fallen from **5%** of all conversations to **3%**". *(Tasks)*
26. "the share of tasks related to business and financial operations has halved, from **6% to 3%**". *(Tasks)*
27. "(In absolute terms, of course, the number of conversations in each category has still risen significantly.)" No absolute counts are published on this page. *(Tasks)*
28. "as the GDP per capita of a country increases, the use of Claude shifts *away* from tasks in the Computer and Mathematical occupation group, and towards a diverse range of other activities, like education, art and design; office and administrative support; and the physical and social sciences." Comparison: four panels, occupation-group share against AUI, across countries. Qualified in the same sentence: "The overall trend is noisy". *(Tasks; fig. caption "As we move from lower to higher adoption countries, Claude use appears to shift to a more diverse mix of tasks, although the overall pattern is noisy.")*
29. "software development remains the most common use in every single country we track." Comparison: within-country ranking of uses, all countries. *(Tasks)*
30. "The picture looks similar in the US, although our sample size limits our ability to explore in more detail how the task mix varies with adoption rates." *(Tasks)*

**Trends in Claude use → Patterns of interaction**

31. "Since December 2024, we've found that the share of directive conversations has risen sharply, from **27% to 39%**. The shares of other interaction patterns (particularly learning, task iteration, and feedback loops) have fallen slightly as a result." Comparison: wave 1 against wave 3. *(Patterns of interaction)*
32. "for the first time, automation (**49.1%**) has become more common than augmentation (**47%**) overall." Comparison: the two poles within the same wave, and against the previous two reports. The two figures sum to 96.1%; the page does not say what the residual is. *(Patterns of interaction; fig. caption "Automation appears to be increasing over time.")*
33. "in countries with higher Claude use per capita, Claude's uses tend towards augmentation, whereas people in lower-use countries are much more likely to prefer automation. Controlling for the mix of tasks in question, a **1%** increase in population-adjusted use of Claude is correlated with a roughly **3%** reduction in automation." Comparison: cross-country, automation share against AUI, conditional on task mix. *(Patterns of interaction; fig. caption "Countries with higher Claude use per capita tend to use Claude in a more collaborative manner.")*

**Businesses**

34. "44%" of API traffic in the sample "maps to computer or mathematical tasks, compared to **36%** of tasks on Claude.ai". Comparison: 1P API sample against Claude.ai sample, same O*NET top level. *(Businesses)*
35. "around **5%** of all API traffic focuses specifically on developing and evaluating AI systems." *(Businesses)*
36. Educational occupations: "**4%** in the API relative to **12%** on Claude.ai"; arts and entertainment: "**5%** relative to **8%**". Comparison: as above. *(Businesses)*
37. "**77%** of our API conversations show automation patterns, of which the vast majority are directive, while just **12%** show augmentation. On Claude.ai, the split is almost even." 77 + 12 = 89%; the page does not say what the residual 11% is. Comparison: API against Claude.ai. *(Businesses; fig. caption "Augmentation and automation with Claude on Claude.ai vs. the API.")*
38. "we find a *positive* correlation between price and use: higher-cost task categories tend to see more frequent use". Comparison: across occupational categories, average API cost per task against the category's share of conversations. No elasticity, sign test or category count given on this page. *(Businesses; fig. caption "Cost per task plotted against the task category's share of total conversations.")*
39. Inference drawn from claim 38: "This suggests to us that fundamental model capabilities, and the economic value generated by the models, matters more to businesses than the cost of completing the task itself." *(Businesses)*

**Conclusion**

40. "Across each of the measures we cover in this report, the adoption of AI appears remarkably uneven. People in higher-income countries are more likely to use Claude, more likely to seek collaboration rather than automation, and more likely to pursue a breadth of uses beyond coding." *(Conclusion)*
41. "Within the US, AI use seems to be strongly influenced by the dominant industries in local economies, from technology to tourism." No industry-composition variable is used anywhere on this page; the support is the DC/California/New York/Hawaii examples. *(Conclusion)*
42. "And businesses are more likely to entrust Claude with agency and autonomy than consumers are." The page's only measure behind this is the automation/directive share; no autonomy measure appears on the page. *(Conclusion)*
43. "it's especially notable to us that directive automation has become much more common in conversations on Claude.ai over the past nine months." *(Conclusion)*
44. **Open data:** the release includes "geographic data, task-level use patterns, automation/augmentation breakdowns by task, and an overview of API use." *(Open data)*

## Definitions (verbatim)

All quotations are from the page fetched 2026-09-16. Wording, punctuation marks and markdown emphasis markers (`*`, `**`) are reproduced as they appear in the fetched text, with one stated exception: the source's curly apostrophes and quotation marks (’ “ ”) are written here as ASCII (' " "). No other character is altered, and no word is paraphrased, reordered or elided; ellipses would be shown as `…` and there are none.

1. Overrepresentation (given by example, not by formula) — *Lead*: "But it turns out that they're the particular uses of Claude that are some of the *most overrepresented* in each of these places." And: "That doesn't mean these are the *most popular* tasks: software engineering is still by far in the lead in almost every state and country in the world. Instead, it means that people in Massachusetts have been more likely to ask Claude for help with scientific research than people elsewhere".

2. Anthropic AI Usage Index (AUI) — *Geography → Across countries*: "However, there is huge variation in population size across these countries. To account for this, we adjust each country's share of Claude.ai use by its share of the world's working population. This gives us our **Anthropic AI Usage Index**, or AUI. Countries with an AUI greater than 1 use Claude more often than we'd expect based on their working-age population alone, and vice-versa."

3. The classification method and taxonomy — *Trends in Claude use*: "We use a privacy-preserving [classification method](https://www.anthropic.com/research/clio) that categorizes anonymized conversation transcripts into task groups defined by O*NET, a US government database that classifies jobs and the tasks associated with them."

4. The bottom-up taxonomy — *Footnote 2*: "We supplement this with a 'bottom-up' task classification in which Claude classifies conversations according to its own taxonomy, in order to address any gaps in the O*NET categories. The full details of our privacy-preserving analysis methodology are available [here](https://www.anthropic.com/research/clio)."

5. Collaboration, as the thing being measured — *Trends in Claude use*: "the ways people choose to collaborate—how much oversight and input into Claude's work they choose to have".

6. Automation and augmentation — *Patterns of interaction*: "we generally distinguish between tasks that involve *automation* (in which AI directly produces work with minimal user input) and *augmentation* (in which the user and AI collaborate to get things done)."

7. Directive and feedback loop — *Patterns of interaction*: "We further break automation down into *directive* and *feedback loop* interactions, where directive conversations involve the minimum of human interaction, and in feedback loop tasks, humans relay real-world outcomes back to the model."

8. Learning, task iteration and validation — *Patterns of interaction*: "We also break augmentation down into *learning* (asking for information or explanations), *task iteration* (working with Claude collaboratively), and *validation* (asking for feedback)."

9. API customers, as a population — *Businesses*: "API customers, who tend to be businesses and developers, use Claude very differently to those who access it through [Claude.ai](http://claude.ai/redirect/website.v1.2b48e19c-4a1c-47c8-91ed-8da3c72ee841): they pay per token, rather than a fixed monthly subscription, and can make requests through their own programs."

10. The purpose of the Index — *Conclusion*: "The Economic Index is designed to provide an early, empirical assessment of how AI is affecting people's jobs and the economy."

## Data and methods

What the page states, in the wiki author's words, with references.

- **Platforms.** Two samples. Claude.ai conversations, used for the geography and over-time chapters; and, new in this release, Anthropic's first-party API: "we have begun sampling interactions from a subset of Anthropic's first-party API customers, in a first-of-its-kind analysis" (*Businesses*). The page contrasts the two by access mode and billing (per token versus fixed monthly subscription) and by who uses them ("businesses and developers") (*Businesses*).
- **Windows.** The Claude.ai over-time comparison is against "[December 2024-January 2025](https://www.anthropic.com/news/the-anthropic-economic-index)" and "[February–March 2025](https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7)" (*Lead*, bullet 3); tracking runs "since December 2024" and the elapsed span is described as "the past nine months" (*Tasks*; *Conclusion*). The page never states the date range of the latest Claude.ai sample. The API sample window is given only in footnote 3: "1 million transcripts from August 2025".
- **Sample size and sampling frame.** Given for the API only: "Data in this section covers 1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage" (*Footnote 3*). No sample size, geolocation method, VPN/hosting exclusion, subscription tier or conversation-versus-user unit of observation is stated anywhere on the page for the Claude.ai sample.
- **Classifier.** A "privacy-preserving [classification method](https://www.anthropic.com/research/clio)" applied to "anonymized conversation transcripts", mapping to O*NET task groups, supplemented by a Claude-generated bottom-up taxonomy (*Trends in Claude use*; *Footnote 2*). The same method is applied to the API: "Using the same privacy-preserving [methodology](https://www.anthropic.com/research/clio) we use for conversations on Claude.ai" (*Businesses*). No classifier model version is named for any wave; the page names a model only to date the first wave — "(In December 2024, when we first collected data for the Economic Index, the latest version of Claude was Sonnet 3.6.)" (*Patterns of interaction*), which refers to the model users had, not the classifier.
- **Geographic grain.** Countries and US states. The interactive site is said to cover "every US state and all occupations we track" (*Lead*); the country figures are described as "Top 30 countries" and "twenty countries that score highest" (fig. alt text). The page does not say how many countries are in the sample, nor that any minimum-observation floor was applied.
- **The AUI's denominator.** Stated twice and inconsistently within one paragraph: "its share of the world's working population" and then "based on their working-age population alone" (*Across countries*). No age band is given. For states the phrase is "relative to their working age populations" (fig. caption) with no source for the population data.
- **Thresholds.** None stated. No privacy-filter cell minimum, no minimum-observation floor per country or state, no significance threshold, no confidence interval anywhere on the page. The only robustness statement is footnote 1's unspecified "robustness checks" on Utah.
- **Controls.** One control is stated: the automation/AUI relationship is "Controlling for the mix of tasks in question" (*Patterns of interaction*). The two GDP elasticities (0.7 cross-country, 1.8 within-US) are stated without controls. The price/use correlation is stated without controls (*Businesses*).
- **Released data.** "we've made our dataset [openly available](https://huggingface.co/datasets/Anthropic/EconomicIndex), alongside the data from our previous Economic Index reports" (*Lead*); *Open data* names the contents as "geographic data, task-level use patterns, automation/augmentation breakdowns by task, and an overview of API use", with downloads pointed at anthropic.com/economic-index rather than at Hugging Face.
- **Interactive artefact.** "an [interactive website](http://anthropic.com/economic-index) where you can explore our data yourself", searchable by US state and occupation, promised to be updated "with more data in future" (*Lead*; *Conclusion*).

## Limitations (verbatim)

1. *Tasks*: "The overall trend is noisy, but generally, as the GDP per capita of a country increases, the use of Claude shifts *away* from tasks in the Computer and Mathematical occupation group".
2. *Tasks*, figure caption: "As we move from lower to higher adoption countries, Claude use appears to shift to a more diverse mix of tasks, although the overall pattern is noisy."
3. *Tasks*: "The picture looks similar in the US, although our sample size limits our ability to explore in more detail how the task mix varies with adoption rates."
4. *Patterns within the United States*: "That said, income actually has *less* explanatory power within the US than across countries, as there's much higher variance within the overall trend. That is: other factors, beyond income, must explain more of the variation in population-adjusted use."
5. *Patterns of interaction*, figure caption hedge: "Automation appears to be increasing over time."
6. *Footnote 1*: "As for Utah, in second: when further investigating Utah's activity, we discovered that a notable fraction of its use appeared to be associated with indicators of coordinated abuse – which is also reflected in Utah's much higher "directive" automation score than average. However, we ran robustness checks and believe that this activity is not driving the results."
7. *Footnote 2*: "We supplement this with a 'bottom-up' task classification in which Claude classifies conversations according to its own taxonomy, in order to address any gaps in the O*NET categories." (Stated as a gap in the O*NET taxonomy.)
8. *Footnote 3*: "Data in this section covers 1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage."
9. *Patterns within the United States*: "Our best guess is that it's differences in the composition of states' economies." (Offered as a guess, not a result.)
10. *Patterns of interaction*: "We're not yet sure why this is."

## Open questions, conjectures and promised follow-ups (verbatim)

1. *Across countries* — the divergence question: "But it does raise a question of economic divergence: previous general-purpose technologies, like electrification or the combustion engine, led to both vast economic growth and a [great divergence](https://www.aeaweb.org/articles?id=10.1257/jep.11.3.3) in living standards around the world. If the effects of AI prove to be largest in richer countries, this general-purpose technology might have similar economic implications."
2. *Patterns within the United States* — what explains within-US variation: "What else could explain this adoption gap? Our best guess is that it's differences in the composition of states' economies."
3. *Patterns of interaction* — why directive use rose: "One potential explanation for this is that AI is rapidly winning users' confidence, and becoming increasingly responsible for completing sophisticated work."
4. *Patterns of interaction* — the capability explanation: "This could be the result of improved model capabilities. (In December 2024, when we first collected data for the Economic Index, the latest version of Claude was Sonnet 3.6.) As models get better at anticipating what users want and at producing high-quality work, users are likely more willing to trust the model's outputs at the first attempt."
5. *Patterns of interaction* — why high-use countries augment more: "We're not yet sure why this is. It could be because early adopters in each country feel more comfortable allowing Claude to automate tasks, or it could be down to other cultural and economic factors."
6. *Lead*, bullet 4 — the labour-market conjecture: "We find that API users are significantly more likely to automate tasks with Claude than consumers are, which suggests that major labor market implications could be on the horizon."
7. *Businesses* — the automation/transition conjecture: "This could have significant economic implications: in the past, the automation of tasks has been associated with large economic transitions, as well as major productivity gains."
8. *Businesses* — the capability-over-cost conjecture: "This suggests to us that fundamental model capabilities, and the economic value generated by the models, matters more to businesses than the cost of completing the task itself."
9. *Conclusion* — the open question about settling, and the promised follow-up: "The nature of people's use of Claude is evidently still being defined: we're still collectively deciding how much confidence we have in AI tools, and how much responsibility we should give them. So far, though, it looks like we're becoming increasingly comfortable with AI, and willing to let it work on our behalf. We're looking forward to revisiting this analysis over time, to see where—or, indeed, *if*—users' choices settle as AI models improve."
10. *Conclusion* — promised data updates: "We'll update this website with more data in future, so you can continue to track the evolution of AI's effects on jobs and the economy in the ways that interest you."
11. *Conclusion* — the stated audience for follow-up work: "We hope it helps policymakers, economists and others more effectively prepare for the economic opportunities and risks that AI provides."
12. *Lead* — the open-data invitation: "Finally, if you'd like to build on our analysis, we've made our dataset [openly available](https://huggingface.co/datasets/Anthropic/EconomicIndex), alongside the data from our previous Economic Index reports."

## What it did not test

**This section is the wiki author's inference, not the page's text.** It records adjacent questions the page's own data could have addressed but did not, and framings the page uses without support *on this page*. Some are answered in the full report; those are marked, and the report's wiki file (`wiki/reports/economic-index-2025-09-report.md`) is authoritative on the report's content.

*Adjacent questions the data could have addressed*

1. **Composition versus behaviour in the automation trend.** The 27% → 39% directive rise is reported as a change in how people use Claude, but the user base grew and changed over the same nine months. The page has three cross-sections and no panel, so it cannot separate new users arriving with different habits from existing users delegating more — and it does not flag this. (The report does flag it: "This could also be due to changes in the underlying user base.")
2. **Classifier version as a rival explanation for the same trend.** The page attributes the directive rise to capability and trust and names no classifier version for any wave. (The report's Chapter 1 footnote 4 states the V3 classifier was Sonnet 4 against V2's Sonnet 3.7, and reports a re-run at 45% versus 49% automation. None of that appears here.)
3. **State industry composition, actually measured.** "the dominant industries in local economies" (*Conclusion*) is supported by four anecdotes. The state-level AUI could be regressed on BEA or BLS industry-employment shares; the page does not, and calls the mechanism "our best guess".
4. **Uncertainty on every geographic number.** No standard errors, confidence intervals, observation counts or minimum-cell rules appear anywhere on the page, including for DC's 3.82 and Hawaii's 2x. Both are small-population cells. Nothing on the page lets a reader tell a real difference from sampling noise.
5. **Multiple comparisons in the overrepresentation stories.** Hawaii/travel, Massachusetts/science, India/web apps, Brazil/languages (~6x) are the largest ratios found across a large grid of place × use cells. No selection correction, no cell sizes, no null distribution.
6. **The residuals in the shares.** Claude.ai automation 49.1% plus augmentation 47% is 96.1%; API automation 77% plus augmentation 12% is 89%. The page never names the remaining 3.9% and 11% or says whether they are unclassified, privacy-suppressed or a third category. The 89/96 difference alone could carry part of the platform gap.
7. **Decomposing the platform gap.** The country-level automation result is explicitly "Controlling for the mix of tasks in question"; the API-versus-Claude.ai automation gap (77% versus ~half) is not, even though the page's own numbers show the platforms have different task mixes (44% versus 36% computer/mathematical). How much of the gap is task mix and how much is the product surface is left untested.
8. **Window alignment between the two platforms.** The API sample is August 2025 (footnote 3); the Claude.ai window is never stated. The page compares shares across the two without saying whether the periods coincide.
9. **Reconciling its own Claude.ai numbers.** *Tasks* gives computer and mathematical at "around 37-40%" and educational instruction at 13%; *Businesses* gives the Claude.ai comparators as 36% and 12%. The page does not explain why the same quantities differ across its own sections.
10. **Claude's market position as a confound in the AUI.** AUI measures Claude use per working-age person, but Claude's availability, language coverage, pricing, local competitors and brand awareness all vary by country. The page does not test, bound or mention this, yet reads the index as AI adoption. (Availability is footnoted in the report and mapped as "Claude not available"; it is absent here.)
11. **Divergence, as a measurement.** The great-divergence analogy rests on one cross-section. The page has three waves and could have asked whether AUI gaps by income are widening or narrowing; it does not.
12. **Reverse causation in the price/use result.** Higher-cost categories are costlier largely because they consume more tokens. Whether costly tasks are used more, or heavily used complex tasks cost more, is not separated, and no conditional estimate is given. (The report reports a conditional elasticity of −0.29, opposite in sign to the raw correlation this page reports; the page's "capabilities matter more than cost" framing omits it.)
13. **Product surface within Claude.ai.** Subscription tier, model used, and agentic or coding surfaces are not separated in the over-time trend, so a shift in the product mix is indistinguishable from a shift in user behaviour.
14. **Geography below the state, and non-US subnational geography.** Neither is attempted, nor is the reason given.

*Framings used without support on this page*

15. **"users' trust" and "confidence".** Trust is asserted three times (*Lead* bullet 3; *Patterns of interaction*; *Conclusion*) from a single behavioural share. No attitudinal measure appears on the page.
16. **"agency and autonomy"** (*Conclusion*). The page measures only the automation/directive share. Autonomy is a separate construct in the Economic Index family (the 1–5 primitive), and the page neither uses nor mentions it; "directive" is about how little back-and-forth a conversation had, not how much decision-making was delegated.
17. **"AI's responsibility"** (*Lead*, bullet 3). Responsibility is not measured; directive share is.
18. **"the composition of states' economies informs which states use Claude the most"** (*Lead*, bullet 1) — stated as a finding in the lead, then downgraded to "our best guess" in the body.
19. **"occupations"** (*Lead*: "all occupations we track"). The unit classified is the task, and the occupation is inferred from the task, not from the user; the page does not say so.
20. **"a rapid increase"** and "remarkably uneven" — rate and unevenness language with no benchmark for what a slow increase or an even distribution would look like.

*Where this page frames things differently from the report (cross-check fetch of the report landing page, 2026-09-16)*

21. **Title and opening move.** The blog is titled "Tracking AI's role in the US and global economy" and opens on Hawaii, Massachusetts and India; the report is titled "Uneven geographic and enterprise AI adoption" and opens on adoption speed and historical technology diffusion. Unevenness is the report's thesis and the blog's closing observation.
22. **The report's fourth headline finding is absent here.** The report's "Context constrains sophisticated use" chapter (input/output token indices, elasticity 0.38, the data-modernisation bottleneck) has no counterpart on this page. So does the Census BTOS firm-adoption series, the Lorenz/Gini concentration result, and the AUI tier system.
23. **Rounding that changes a rate.** The blog says educational instruction rose "more than 40 percent (from 9% to 13%)"; the report's introduction gives 9.3% → 12.4%, which is about a third, and its Chapter 1 gives 9% → 12%. The blog's science figure, "6% to 8%", is 6.3% → 7.2% in the report.
24. **Elapsed time.** The blog says "the past nine months" twice; the report says "eight months".
25. **New York versus Florida on finance.** The blog says "finance-related tasks are especially common in New York (which comes in fourth)"; the report landing page attributes elevated financial-services use to Florida and mentions New York only in the AUI ranking (1.58). Whether the blog's New York claim appears anywhere in the report PDF should be checked by the report thread.
26. **Hawaii and Brazil's 6x are not on the report landing page.** Both are blog-only framings as far as today's fetch shows; the report's Brazil example is translation and legal services, without a multiple.
27. **AUI values are suppressed on the blog.** Only DC's 3.82 is given. Israel's 7, Singapore's 4.57, the US's 3.62, India's 0.27 and the rest appear only in the report.
28. **The cost result.** The blog reports the positive raw correlation and concludes capabilities beat cost; the report reports the same correlation *and* a conditional elasticity of −0.29 with the caveat "this should be viewed as a preliminary exploration". A reader of the blog alone would not know a negative conditional estimate exists.
29. **"roughly 3% reduction in automation" per 1% higher AUI** is given only on the blog; the report's Figure 2.11 shows the partial relationship without stating an elasticity. Note the collision risk: the report's Figure 3.8 elasticity of 3 is a different quantity (cost and usage share).
30. **Hedging.** The report says of the automation/AUI puzzle "more research is needed here"; the blog says "We're not yet sure why this is." The blog carries no equivalent of the report's labour-market fork (capability-driven displacement versus learning-by-doing) or its policy close.
31. **Authorship.** The report names lead authors (Appel, McCrory, Tamkin) and carries a citation block; the blog names no one.

## Verification

- **Fetched 2026-09-16.** Primary source: https://www.anthropic.com/research/economic-index-geography — fetched in full (lead through Footnotes, plus figure captions, figure alt text and page metadata). Every quotation in `Definitions (verbatim)`, `Limitations (verbatim)` and `Open questions, conjectures and promised follow-ups (verbatim)`, and every number in `Claims`, was checked word-by-word against that fetched text. Markdown emphasis markers and hyperlink targets inside quotations are reproduced as fetched; the source's curly apostrophes and quotation marks are written as ASCII, as stated at the head of `Definitions (verbatim)`. No quotation is paraphrased or elided.
- **Cross-check fetch, 2026-09-16:** https://www.anthropic.com/research/anthropic-economic-index-september-2025-report — the report's web version, fetched only to support items 21–31 of `What it did not test`. Nothing from it is treated as a claim of this page. Its own wiki file is `wiki/reports/economic-index-2025-09-report.md`, owned by a separate thread, which is authoritative for the report; items 21–31 should be reconciled against it, and item 25 (New York and finance) checked against the report PDF.
- **Not fetched:** the report PDF (https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf), the arXiv version, the interactive Economic Index site (anthropic.com/economic-index), the Hugging Face dataset card, and the Clio methods page (https://www.anthropic.com/research/clio) — all linked from this page, all out of scope for this file. No fetch failed.
- **Not available on this page:** page numbers (it is a web page, so references above are section headings, figure captions and figure alt text); author names; a citation block; any confidence interval, standard error, observation count or threshold; the date range of the Claude.ai sample.
- **Two numbers that appear only in figure alt text**, not in the body: the US's 21.6% share of global use, and the AUI top five. Both are recorded as such in `Claims` (items 10, 11). Utah's second place appears only in alt text and footnote 1 (item 19).
