# economic-index-2025-09-blog — style annotation

## Source

- **Title on page (H1):** "Anthropic Economic Index: Tracking AI's role in the US and global economy". Browser/OG title is shortened and drops the brand: "Economic Index: AI's role in the US and global economy". Meta description: "New research from the Anthropic Economic Index exploring geographic patterns of AI use across the US and the global economy."
- **Date on page:** "Sep 15, 2025" — the same day as the full report it condenses.
- **Primary URL fetched:** https://www.anthropic.com/research/economic-index-geography
- **PDF or appendix:** none. The `wiki/INDEX.md` row carries `—` in the PDF column. All depth is delegated to the report.
- **Other URLs it points at (not fetched for this file):** the full report at http://anthropic.com/research/anthropic-economic-index-september-2025-report (slug `economic-index-2025-09-report`), the interactive site at http://anthropic.com/economic-index, the February 2025 launch post at https://www.anthropic.com/news/the-anthropic-economic-index (slug `economic-index-2025-02-report`), the March 2025 report at https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7, the Clio post at https://www.anthropic.com/research/clio (twice), the Hugging Face dataset, Pritchett's *Divergence, Big Time* at the AEA, claude.ai, and one Research Engineer job posting.
- **Document type:** companion blog post to a 47-page report published the same day. Categorised on the page as "Economics"; filed under Research, not News. **No authors, no acknowledgements, no citation block, no abstract, no footnote-heavy apparatus** — three footnotes in total against the report's twenty-eight. Where the report's web version moves its author list to the foot of the article, this page has none at all: the companion is institutional speech, not attributed research.
- **Approximate length:** roughly 2,000–2,300 words of body prose against the report's 9,000–10,000. Ten captioned exhibits, one uncaptioned hero image (its alt text is the title), one embedded video, four H2 sections of substance plus Open data and Work with us, four H3s, three footnotes.
- **Audience:** a general reader who will not open the report. The page says so structurally: the very first interactive element above the hero is "Explore our data", the reader is addressed in the second person ("you can search for trends and results in Claude.ai use across every US state and all occupations we track, to see how AI is used where you live or by people in similar jobs"), and the only named external citation in the whole post is a hyperlink on the words "great divergence". Gallup, Bick–Blandin–Deming, Gordon, Kremer, Hall & Kahn, Gabaix, Zipf and the O-Ring model — every one of them cited in the report — are gone.

## Section order

Headings in page order, with what each does.

1. **Category label "Economics" + H1 + "Sep 15, 2025" + "Explore our data" link + hero image + video.** The data CTA sits *above* the article, in the position the February 2025 post gave to "Read the paper". The pointer to the report itself does not appear until the end of the fourth paragraph.
2. **Untitled opening (no heading)** — three paragraphs, a four-bullet block, then a paragraph of pointers (report, interactive site, open data). ~430 words. The bullets are organised by *cut of the data*, not by finding: within the US, across countries, over time, and by business users.
3. **H2 "Geography"** — two sentences of framing, then two H3s.
   - **H3 "Across countries"** — three paragraphs, three exhibits: total share, then the AUI defined and its leaders, then the income correlation and the divergence passage.
   - **H3 "Patterns within the United States"** — two paragraphs, one exhibit. The elasticity comparison, then the state-composition examples. Footnote 1 (Utah) hangs here.
4. **H2 "Trends in Claude use"** — one framing paragraph carrying the whole method (Clio, O\*NET, footnote 2), then two H3s.
   - **H3 "Tasks"** — four paragraphs, two exhibits: the dominant category, the composition shift, the task-diversity gradient, the "software development still leads everywhere" concession.
   - **H3 "Patterns of interaction"** — six paragraphs, two exhibits: the taxonomy defined, the crossover, its interpretation, then the automation-by-adoption result and its two candidate causes.
5. **H2 "Businesses"** — five paragraphs, two exhibits: what the API sample is (footnote 3), the category mix, the automation gap, the cost result.
6. **H2 "Conclusion"** — five paragraphs, opening on a question addressed to the post itself ("What have we found so far?").
7. **H2 "Open data"** — one paragraph, enumerating the release.
8. **H2 "Work with us"** — recruiting. Boilerplate.
9. **Footnotes** — three: Utah's abuse indicators, the bottom-up taxonomy plus a pointer to the Clio methodology, and the API sample definition.

**Where the findings sit.** In the bullets, before any method, exactly as in the report — but the *thesis* has moved. The report bolds its thesis in the fourth paragraph of the Introduction ("a hallmark of early technological adoption is that it is *concentrated*"); the blog has no thesis sentence at the top at all and states it only in the Conclusion ("the adoption of AI appears remarkably uneven"). The report front-loads the argument and lets the chapters earn it; the companion front-loads an *image* and lets the argument arrive last. That inversion is the single largest structural difference between the two documents and is the thing to understand about how the house writes a companion piece.

**Where the methods sit.** One paragraph, under "Trends in Claude use", four-fifths of the way down: Clio, anonymised transcripts, O\*NET, plus footnote 2 for the bottom-up taxonomy and footnote 3 for the API sample. The report's practice of *define at point of use, document in footnote* survives, but the documentation shrinks from twenty-eight footnotes to three, and the ones dropped are the load-bearing ones (below, `## Limitations`).

### What the companion keeps, drops and adds

Against `wiki/style/economic-index-2025-09-report.md`, section by section.

**Keeps** — one finding per chapter, plus one extra from the geography chapter. Total usage leadership; the AUI, its definition and the >1 rule; the income gradient at both levels with both elasticities (0.7% and 1.8%) and the reversal in explanatory power; the state-composition story; the task-diversity gradient; the directive crossover (27% to 39%); the automation-by-adoption result; the API category mix; the 77% API automation share; the cost-versus-usage association; the divergence stakes, with the same historical analogues (electrification, the combustion engine) and the same conditional grammar.

**Drops** — in rough order of how much is lost.
- **The report's entire third-chapter argument about context** ("The more Claude does, the more Claude needs to know"): the token indices, Table 3.1, the elasticity, the tacit-knowledge complementarity passage and the recommendation to businesses about data modernisation. The report's most argued section has no trace on this page.
- **The partial regression on cost.** The blog reports the *unconditional* positive correlation between task cost and task usage and stops there. The report's conditional version, which flips the sign, is absent — so the companion's cost result is the raw one, and a reader of the blog alone cannot know a conditional estimate exists. This is the compression that costs the most and the one our own posts should not imitate: the headline finding is kept, the specification that qualifies it is dropped.
- **The classifier-change caveat.** The report answers the first threat to its headline crossover in a footnote — V3 classified with Sonnet 4, V2 with Sonnet 3.7, reran and the direction holds at a different level. The blog carries the crossover as its most quotable claim and carries no version of that caveat. What it puts in the same rhetorical slot is a parenthetical about the *product* model of the day ("In December 2024 … the latest version of Claude was Sonnet 3.6"), which reads like a comparability note and is not one.
- **The Census benchmark section**, and with it the report's practice of establishing the external landscape before its own numbers.
- **The concentration machinery**: Gini coefficients, the power-law comparison, Zipf, the O-Ring mechanism.
- **Every country-level AUI value.** Israel's 7 and Singapore's 4.57 are nowhere in the prose; the countries are named, the values are not. DC's 3.82 is the only AUI value on the page.
- **The tier taxonomy and both tables**, the five candidate mechanisms for the income gradient, the three-bullet account of why coding leads.
- **The sample and privacy apparatus for Claude.ai**: the 1-million-conversation August 4–11 window, the 15-conversation/5-account privacy filter, IP geolocation, the VPN and hosting exclusions, the 200-observation floor that travels in every report caption. The API sample footnote survives verbatim; its Claude.ai twin does not.
- **The bolded policy-choices thesis** and the direct address to policymakers about digital divides; the Brynjolfsson/Gans footnote staging the substitution-versus-complementarity dispute; "History shows that the patterns of technological adoption aren't fixed".
- **The V1/V2/V3 notation.** Waves become dates and links.

**Adds** — five things not in the report's quoted text. The Hawaii, Massachusetts, India and Brazil overrepresentation examples; the split of the crossover into two decimals ("automation (49.1%) has become more common than augmentation (47%)"); the automation elasticity ("a 1% increase in population-adjusted use of Claude is correlated with a roughly 3% reduction in automation"); the AI-about-AI share ("around 5% of all API traffic focuses specifically on developing and evaluating AI systems"); and a closing question about whether user behaviour settles, which the report does not ask.

### Register, against the report

- **Contractions throughout**: "doesn't", "they're", "we've", "aren't", "it's", "We'll", "We're". The report uses almost none.
- **Conversational hedges in place of technical ones**: "Our best guess is", "We're not yet sure why this is", "This makes sense", "Perhaps surprisingly", "As it happens", "it turns out", "on the face of it", "All that said". The report's rungs — *we document*, *suggests*, *appears to*, *we speculate* — are still present, but the top of the ladder has been replaced by plain speech.
- **Second person.** "you can search", "how AI is used where you live", "if you'd like to explore our data yourself". The report never addresses a reader.
- **Rhetorical questions** used as section hinges: "What else could explain this adoption gap?", "What have we found so far?".
- **Single-word italics, used for two different jobs.** For defined terms, as the report does — *automation*, *augmentation*, *directive*, *feedback loop*, *learning*, *task iteration*, *validation*. And, unlike the report, for plain stress: *most overrepresented*, *most popular*, *aren't*, *more*, *away* (twice), *less*, *positive*, *if*. The report reserves its emphasis for the word that carries a caveat (*relative*); the blog spends it on whichever word a reader might skim past.
- **Coarser rounding, and not always in the same direction.** Education "from 9% to 13%", sciences "from 6% to 8%", the dominant category "around 37-40%", the interval "over the past nine months" — against the report's 9%/12%, 6%/7%, 36% and eight months as recorded in `wiki/style/economic-index-2025-09-report.md`. Two of these round the change upward, and both are then restated as a growth rate ("risen by more than 40 percent", "increased by a third") which the report does not compute. Rounding coarser at lower depth is house practice; rounding coarser *and* converting to a percentage-change is how a companion piece can make a change sound larger than the report does. Worth naming as the failure mode to avoid when writing a short version of our own work.
- **Numbers per thousand words** falls by roughly half, and the ones that survive are shares and ratios, never coefficients with their conditioning.

## Opening move

Verbatim, the first three paragraphs, the bullet block and the pointer paragraph (hyperlink URLs stripped; anchor text retained and listed below).

> Travel planning in Hawaii, scientific research in Massachusetts, and building web applications in India. On the face of it, these three activities share very little in common. But it turns out that they're the particular uses of Claude that are some of the *most overrepresented* in each of these places.

> That doesn't mean these are the *most popular* tasks: software engineering is still by far in the lead in almost every state and country in the world. Instead, it means that people in Massachusetts have been more likely to ask Claude for help with scientific research than people elsewhere – or, for instance, that Claude users in Brazil appear to be particularly enthusiastic about languages: they use Claude for translation and language-learning about six times more than the global average.

> These are statistics we found in our third Anthropic Economic Index report. In this latest installment, we've expanded our efforts to document the early patterns of AI adoption that are beginning to reshape work and the economy. We measure how Claude is being used differently…

> - **…within the US:** we provide the first-ever detailed assessment of how AI use differs between US states. We find that the composition of states' economies informs which states use Claude the most per capita – and, surprisingly, that the very highest-use states *aren't* the ones where coding dominates.
> - **…across different countries:** our new analysis finds that countries' use of Claude is strongly correlated with income, and that people in lower-use countries use Claude to automate work *more* frequently than those in higher-use ones.
> - **…over time:** we compare our latest data with December 2024-January 2025 and February–March 2025. We find that the proportion of 'directively' automated tasks increased sharply from 27% to 39%, suggesting a rapid increase in AI's responsibility (and in users' trust).
> - **…and by business users:** we now include anonymized data from Anthropic's first-party API customers (in addition to users of Claude.ai), allowing us to analyze businesses' interactions for the first time. We find that API users are significantly more likely to automate tasks with Claude than consumers are, which suggests that major labor market implications could be on the horizon.

> We summarize the report below. In addition, we've designed an interactive website where you can explore our data yourself. For the first time, you can search for trends and results in Claude.ai use across every US state and all occupations we track, to see how AI is used where you live or by people in similar jobs. Finally, if you'd like to build on our analysis, we've made our dataset openly available, alongside the data from our previous Economic Index reports.

Anchor text carrying links, in order: "Anthropic Economic Index report" → the September report; "December 2024-January 2025" → the February 2025 post; "February–March 2025" → the March 2025 post; "Claude.ai" → claude.ai; "the report" → the September report; "interactive website" → the Index site; "Claude.ai" → claude.ai; "openly available" → Hugging Face.

**Annotation.**

- **What question is posed.** None; and unlike the February 2025 launch post, not even a forecast. The opening is a **riddle**: three activities in three places, an assertion that they have nothing in common, and a resolution. The move is *concrete image → apparent puzzle → the construct that dissolves it*. The construct — overrepresentation relative to a global baseline — is never named, never given a symbol, and never given a value in these paragraphs. It is taught by example, twice, and only then does the AUI appear 600 words later with a definition.
- **The second sentence of the post is a caveat.** "That doesn't mean these are the *most popular* tasks: software engineering is still by far in the lead in almost every state and country in the world." The hook and its withdrawal are adjacent, and the withdrawal is the more emphatic of the two because it carries the italic. This is the strongest single device on the page and it is directly transferable: **when the finding is a relative measure, state what it is not, in the sentence after you state it.** The report makes the same move — "this concentration is affected by the population size of each country" — but three paragraphs and one figure later.
- **How soon the first number appears.** Second paragraph: "about six times more than the global average". Note what that number is not — it is not an index value, not a share, not a coefficient, and not sourced to an exhibit; it is a ratio to a baseline, rounded to one significant figure, attached to a named country and a named activity. The report's first number is somebody else's survey (Gallup's 40%), used to pose a puzzle. The companion's first number is its own, used to make a place vivid. Both defer their headline shares; neither opens on a table.
- **Who is said to be affected.** People in places, named one at a time: Hawaii, Massachusetts, India, Brazil. The report opens on "employees" in aggregate and widens to regions and firms; the blog opens on four localities and only reaches "work and the economy" in the third paragraph. The abstraction runs the opposite way.
- **The bullets are a claims list organised by data cut.** Four bullets, each opening with an em-dash-free ellipsis that completes the stem "We measure how Claude is being used differently…" — a syntactic device that makes the four cuts parallel without repeating the verb. Each bullet is bolded lead-in plus one or two sentences of evidence, exactly the report's two-beat form; but here the bold carries the *cut* ("…across different countries:") rather than the *claim*, so the claim has to be recovered from the sentence after it. That is the weaker of the two forms and the report's is the one to copy.
- **Hedges inside the bullets**, one per bullet: "surprisingly, that the very highest-use states *aren't* the ones where coding dominates" (an anti-expectation fence), "suggesting a rapid increase in AI's responsibility" (marks the interpretation as interpretation), "which suggests that major labor market implications could be on the horizon" (two rungs of hedge on the only bullet that reaches for a consequence). The country bullet is the only one with no hedge at all, and it is also the only one stating a correlation.
- **Naming, in the first bullet and on one line.** "how **AI** use differs between US states" and "which states use **Claude** the most per capita". The general claim takes AI; the measured quantity takes Claude. The rule survives compression intact, which is the most reassuring thing about this page.
- **Register detail worth copying.** "these three activities share very little in common" is deliberately ordinary prose; the post spends its first forty words earning attention with no technical content whatsoever, then spends the next forty taking back the reading it just invited. A short companion piece can afford exactly one such paragraph.

## Findings and their caveats

### Finding 1 — total usage concentration

> The US uses Claude far more than any other nation. India is in second place, followed by Brazil, Japan, and South Korea, each with similar shares.

> However, there is huge variation in population size across these countries. To account for this, we adjust each country's share of Claude.ai use by its share of the world's working population. This gives us our **Anthropic AI Usage Index**, or AUI. Countries with an AUI greater than 1 use Claude more often than we'd expect based on their working-age population alone, and vice-versa.

**Annotation.** Two sentences of finding with **no number in either** — the 21.6% that the report puts in the body appears here only in the exhibit's alt text, so a reader of the prose gets a rank order and nothing else. The caveat then arrives in the same position as in the report ("However, there is huge variation in population size") and does the same job: it withdraws the natural reading of a ranking before the reader can over-read it, and it motivates the next measure. The construct is defined in two sentences, its scale is glossed before any value is quoted ("Countries with an AUI greater than 1 use Claude more often than we'd expect"), and the formula is dropped — where the report shows an equation image, the blog gives the ratio in words. That substitution is the cleanest example on the page of *compressing by leaving out, not by compressing*: nothing about the construct is made vaguer, one exhibit is simply not shown.

### Finding 2 — the income gradient across countries

> From the AUI data, we can see that some small, technologically advanced countries (like Israel and Singapore) lead in Claude adoption relative to their working-age populations. This might to a large degree be explained by income: we found a strong correlation between GDP per capita and the Anthropic AI Usage Index (a 1% higher GDP per capita was associated with a 0.7% higher AUI). This makes sense: the countries that use Claude most often generally also have robust internet connectivity, as well as economies oriented around knowledge work rather than manufacturing.

**Annotation.** "some small, technologically advanced countries (like Israel and Singapore) lead" — the leaders are named without their values, and "some" plus "like" together carry the licence to illustrate rather than rank, which is the same device the report's Introduction uses with "among the highest countries". The elasticity is given in parentheses in its interpreted form ("a 1% higher GDP per capita was associated with a 0.7% higher AUI"), with "associated with" doing the causal fencing and no standard error, R², sample or specification anywhere. "This might to a large degree be explained by income" is a two-part hedge on a mechanism; "This makes sense:" then supplies the story — connectivity and sectoral composition — with no evidence and no marker that it is conjecture beyond the colloquialism itself. That is the page's weakest caveat construction: the report would have written "we speculate" or "one interpretation is". **"This makes sense" is a confidence claim disguised as a transition, and it is the one thing in the opening half not to copy.**

### Finding 3 — the gradient within the US, and where it weakens

> The link between per capita GDP and per capita use of Claude also holds when comparing between US states. In fact, use rises more quickly within income here than across countries: a 1% higher per capita GDP inside the US is associated with a 1.8% higher population-adjusted use of Claude. That said, income actually has *less* explanatory power within the US than across countries, as there's much higher variance within the overall trend. That is: other factors, beyond income, must explain more of the variation in population-adjusted use.

> What else could explain this adoption gap? Our best guess is that it's differences in the composition of states' economies. The highest AUI in the US is the District of Columbia (3.82), where the most disproportionately frequent uses of Claude are editing documents and searching for information, among other tasks associated with knowledge work in DC. Similarly, coding-related tasks are especially common in California (the state with the third-highest AUI overall), and finance-related tasks are especially common in New York (which comes in fourth).[1] Even among states with lower population-adjusted use of Claude, like Hawaii, use is closely correlated to the structure of the economy: people in Hawaii request Claude's assistance for tourism-related tasks at twice the rate of the rest of America.

**Annotation.** The same relationship at two levels, and the comparison of the two comparisons is the finding — steeper slope, worse fit — exactly as in the report, and stated with the same care to keep slope and fit apart ("use rises more quickly … That said, income actually has *less* explanatory power"). The italic falls on *less*, which is the word a fast reader would otherwise skip. Then the weaker fit is converted into a licence to look elsewhere, and the licence is labelled as a guess in plain words: "Our best guess is". That phrase is more honest than the report's "This suggests that other regional differences … play a larger role", because it says who is guessing.

Two things to flag. First, "other factors, beyond income, **must** explain more of the variation" is the only unhedged deductive claim on the page; it is true given the stated variance, and it is still the sentence a referee would circle, because "must" appears nowhere else. Second, the state examples are stated as *disproportionate frequency* — "the most disproportionately frequent uses", "especially common", "at twice the rate of the rest of America" — never as shares. The post never once says what fraction of DC's conversations are document editing. That is the overrepresentation construct from the opening, reused without being renamed, and it is why the opening had to teach it.

**On Utah.** Utah is second in the US ranking and is **never named in the body**. It appears in the exhibit's alt text and in footnote 1, which opens "As for Utah, in second:" and then gives the coordinated-abuse finding. The report puts Utah's 3.78x in its Introduction's headline bullet and its abuse caveat in footnote 7 of Chapter 2, twenty-five pages later. The companion's handling is better: the caveat is attached to the first and only mention. It is still a footnote hung off a sentence about California and New York, so a reader who skips footnotes meets Utah only in a chart label — but the number and its problem are no longer separated. **When a headline geography is contaminated, name it and its problem in the same place; do not let the number travel alone.**

### Finding 4 — the composition shift over time

> Since December 2024, computer and mathematical uses of Claude have predominated among our categories, representing around 37-40% of conversations.

> But a lot has changed. Over the past nine months, we've seen consistent growth in "knowledge-intensive" fields. For example, educational instruction tasks have risen by more than 40 percent (from 9% to 13% of all conversations), and the share of tasks associated with the physical and social sciences has increased by a third (from 6% to 8%). In the meantime, the relative frequency of traditional business tasks has declined: management-related tasks have fallen from 5% of all conversations to 3%, and the share of tasks related to business and financial operations has halved, from 6% to 3%. (In absolute terms, of course, the number of conversations in each category has still risen significantly.)

**Annotation.** The dominant category is conceded first and in its own paragraph, with a *range* rather than a point ("around 37-40%") because the claim spans three waves — a neat solution to quoting one number for a quantity that moved, and one the report does not use. Every change is then given as a level pair, and the word "relative" is reinstated for the declines ("the relative frequency of traditional business tasks has declined"). The parenthetical that closes the paragraph is the caveat, and it is doing the job the report's single italicised *relative* does, at more length and more plainly: "(In absolute terms, of course, the number of conversations in each category has still risen significantly.)" A share fell, a count rose, and the reader is told so in the same breath. **Copy this parenthetical wholesale whenever a composition share falls.**

Against that, two things to hold at arm's length. The growth rates — "risen by more than 40 percent", "increased by a third", "has halved" — are computed from rounded levels, so each is more precise than its inputs; 9 to 13 is "more than 40 percent" only because both endpoints moved outward in rounding relative to the report's 9% and 12% (per `wiki/style/economic-index-2025-09-report.md`). And "Over the past nine months" sits against the report's "eight months" for the same V1-to-V3 interval. Neither is material to the argument; both are what happens when a short version is written from the long one rather than from the numbers.

### Finding 5 — the crossover in collaboration mode

> Since December 2024, we've found that the share of directive conversations has risen sharply, from 27% to 39%. The shares of other interaction patterns (particularly learning, task iteration, and feedback loops) have fallen slightly as a result. This means that for the first time, automation (49.1%) has become more common than augmentation (47%) overall. One potential explanation for this is that AI is rapidly winning users' confidence, and becoming increasingly responsible for completing sophisticated work.

> This could be the result of improved model capabilities. (In December 2024, when we first collected data for the Economic Index, the latest version of Claude was Sonnet 3.6.) As models get better at anticipating what users want and at producing high-quality work, users are likely more willing to trust the model's outputs at the first attempt.

**Annotation.** The page's headline claim, and the place where compression has done the most damage. What survives is good: the direction is sourced before it is asserted ("The shares of other interaction patterns … have fallen slightly as a result"), the crossover sentence is short and unhedged because the sentence before it earned that, and the interpretation is quarantined and marked twice over ("One potential explanation", "This could be the result of").

What is lost is the fork. The report names two mechanisms — capability improvement and learning-by-doing — declines to choose, and states what would follow from each for the labour market; here only the capability story is offered, and the labour-market fork is gone. A companion that keeps one arm of a two-armed interpretation has changed the finding, not shortened it.

And the caveat a referee raises first — that V3 and V2 were classified by different models — is absent. The parenthetical in its place is about which Claude *users* had in December 2024, not which Claude did the *classifying*, and a reader could easily take it for the comparability note it is not.

Two smaller tells. "automation (49.1%) … augmentation (47%)" gives one decimal to one share and none to the other, and the two leave 3.9% unaccounted for with no explanation on the page — the report has the same unexplained residual on its API split. And "for the first time" is a comparison to the series' own history, which only a third wave can make; it is stated here without the wave labels that make it checkable.

### Finding 6 — collaboration mode against adoption

> Perhaps surprisingly, in countries with higher Claude use per capita, Claude's uses tend towards augmentation, whereas people in lower-use countries are much more likely to prefer automation. Controlling for the mix of tasks in question, a 1% increase in population-adjusted use of Claude is correlated with a roughly 3% reduction in automation. Similarly, increases in population-adjusted Claude use are associated with a shift *away* from automation (as in the chart below), not towards.

> We're not yet sure why this is. It could be because early adopters in each country feel more comfortable allowing Claude to automate tasks, or it could be down to other cultural and economic factors.

**Annotation.** The counter-intuitive result is flagged as counter-intuitive before it is stated ("Perhaps surprisingly"), the conditioning is stated before the coefficient rather than after ("Controlling for the mix of tasks in question, a 1% increase … is correlated with a roughly 3% reduction"), and the magnitude is rounded to one figure with "roughly" attached. Then the model paragraph for how to leave a mechanism open: **"We're not yet sure why this is."** Four hedged words, two candidate explanations, no adjudication, no preference signalled between them — the report's "We speculate that cultural and economic factors might affect the automation share … but more research is needed here", rewritten in the register of someone talking. Both are right; this one is shorter and does not lose anything. It is the best sentence on the page to imitate.

The third sentence, though, restates the second in different words ("Similarly, increases in population-adjusted Claude use are associated with a shift *away* from automation … not towards") and adds only the figure pointer. Compression rule, applied against the source: that sentence is the one to cut.

### Finding 7 — the API sample and its category mix

> These customers' use of Claude is especially concentrated in coding and administrative tasks: 44% of the API traffic in our sample maps to computer or mathematical tasks, compared to 36% of tasks on Claude.ai. (As it happens, around 5% of all API traffic focuses specifically on developing and evaluating AI systems.) This is offset by a smaller proportion of conversations related to educational occupations (4% in the API relative to 12% on Claude.ai), and arts and entertainment (5% relative to 8%).

**Annotation.** "in our sample" is inside the clause carrying the number, between the share and the denominator, so the fence cannot be dropped when the sentence is quoted. Every comparison is a matched pair with the same unit on both sides and the same rounding on both sides — 44/36, 4/12, 5/8 — and the direction word ("compared to", "relative to") is the same each time, which is what lets three comparisons run in two sentences without a table. Note that the blog says "compared to" where the report's parallel sentence says "drops from 12.3% to 3.6%": the companion has quietly fixed a phrasing in the report that reads as a time series when it is a cross-sample difference. The parenthetical about AI-about-AI usage is an aside with no caveat and no exhibit, and it is the one number on the page with nowhere to go.

### Finding 8 — the automation gap between surfaces

> We also find that our API customers use Claude for task automation much more often than Claude.ai users. 77% of our API conversations show automation patterns, of which the vast majority are directive, while just 12% show augmentation. On Claude.ai, the split is almost even. This could have significant economic implications: in the past, the automation of tasks has been associated with large economic transitions, as well as major productivity gains.

**Annotation.** A share, its complement, and a benchmark in three short sentences; the qualitative benchmark ("almost even") is enough because the reader has just been given 49.1/47. The consequence sentence is the most heavily fenced on the page and worth reading closely: "This **could** have significant economic implications: **in the past**, the automation of tasks **has been associated with** large economic transitions, as well as major productivity gains." Modal, historical rather than predictive, and associational — three fences in one sentence, and the sentence still lands, because the claim it is making is only that the question matters. The report's equivalent goes further ("potentially displacing those workers whose roles are most likely to face automation"); the blog stops short of naming who is displaced. A short piece is allowed to raise a stake it will not develop, provided it does not smuggle in the development.

### Finding 9 — cost and use

> Finally, given how API use is paid for, we can also explore whether differences in the cost of tasks (caused by differences in the number of tokens they consume) affect which tasks businesses choose to "buy". Here, we find a *positive* correlation between price and use: higher-cost task categories tend to see more frequent use, as in the graph below. This suggests to us that fundamental model capabilities, and the economic value generated by the models, matters more to businesses than the cost of completing the task itself.

**Annotation.** The measure is defined before it is used, in a parenthesis, in the reader's terms ("caused by differences in the number of tokens they consume"), and the scare quotes on "buy" concede that API customers are not choosing from a menu. The italic on *positive* marks the result as the one that runs against the expected sign, so the reader registers the surprise without the word "surprising" being spent twice on one page. "This suggests to us that" is a properly marked inference.

But this is the unconditional correlation, and the report's conditional version reverses it. The blog states the raw association and draws a mechanism conclusion from it — capabilities over cost — that in the report rests on the controlled specification. **A finding kept without the specification that qualifies it is a different finding.** Of everything on this page, this is the compression to argue against.

### Hedge vocabulary, and how it differs

In descending confidence, as used here: *we find* · *we can see* · *we've found* · *This means* · *tend to* · *appear to be* · *seems to be* · *suggests to us* · *This suggests* · *One potential explanation* · *might* · *could* · *Our best guess is* · *We're not yet sure why this is*. Two rungs of the report's ladder are missing at the top (*we document*, *reveals*) and two have been added at the bottom in plain speech (*our best guess*, *we're not yet sure*). The one rung the page uses that the report does not is **"This makes sense"**, which asserts plausibility rather than measuring it.

### Claude versus AI on this page

- **Title:** "Tracking **AI**'s role in the US and global economy." **Section headings:** "Trends in **Claude** use", "Geography", "Businesses".
- **Same bullet, both words:** "the first-ever detailed assessment of how **AI** use differs between US states … which states use **Claude** the most per capita".
- **The construct:** "**Anthropic AI Usage Index**", defined as a share of "**Claude.ai** use".
- **Every measured quantity says Claude** — "Claude use per capita", "countries' use of Claude", "our API customers use Claude for task automation", "computer and mathematical uses of Claude". No number on the page is attached to the word AI.
- **The interpretations say AI:** "a rapid increase in AI's responsibility", "AI is rapidly winning users' confidence", "the adoption of AI appears remarkably uneven", "how AI is used where you live".
- **Captions:** eight of ten say Claude. Two — "Automation appears to be increasing over time." and "Cost per task plotted against the task category's share of total conversations." — name neither Claude nor AI nor the sample, which is a lapse the report's captions never commit.

The rule the corpus derived from the report holds here under heavy compression: **the question, the title and the stakes say AI; the sample, the index, the numbers and (almost) every caption say Claude.**

## Comparisons

Every place a comparison carries the finding.

### Overrepresented against popular — the post's organising comparison

> That doesn't mean these are the *most popular* tasks: software engineering is still by far in the lead in almost every state and country in the world. Instead, it means that people in Massachusetts have been more likely to ask Claude for help with scientific research than people elsewhere

**Annotation.** Two baselines contrasted in one sentence — the within-place ranking and the across-place ratio — with the wrong one named first and dismissed. The construct never gets a name in the opening; it gets a paraphrase ("more likely … than people elsewhere") and two worked instances. This is how to introduce a location quotient to a reader who will not tolerate the phrase "location quotient", and it is the post's most reusable structural idea.

### A local rate against the global average

> Claude users in Brazil appear to be particularly enthusiastic about languages: they use Claude for translation and language-learning about six times more than the global average.

> people in Hawaii request Claude's assistance for tourism-related tasks at twice the rate of the rest of America.

**Annotation.** The template for a geographic claim, twice, with three features to copy. The baseline is named explicitly in the same clause ("the global average", "the rest of America") rather than implied. The multiple is rounded to one significant figure, so nobody mistakes it for an estimate with a standard error. And the subject is "Claude users in Brazil", not "Brazilians" — the sample is in the noun phrase, which is the cheapest possible place to put it. Note the hedge on the *characterisation* rather than the number: "appear to be particularly enthusiastic" softens the personality claim, not the six-fold.

### Countries against countries, without values

> The US uses Claude far more than any other nation. India is in second place, followed by Brazil, Japan, and South Korea, each with similar shares.

> some small, technologically advanced countries (like Israel and Singapore) lead in Claude adoption relative to their working-age populations

**Annotation.** Rank order carrying the finding with no quantities attached at all — and "each with similar shares" doing the work a dispersion statistic would do, which is to stop the reader treating second place as far ahead of fifth. The report gives all of these values. The companion's choice is defensible for a rank claim and not for the AUI, where the spread between 7 and 0.2 *is* the finding and a reader of prose alone never sees it.

### The same relationship at two levels

> In fact, use rises more quickly within income here than across countries: a 1% higher per capita GDP inside the US is associated with a 1.8% higher population-adjusted use of Claude. That said, income actually has *less* explanatory power within the US than across countries

**Annotation.** 1.8 against 0.7, and fit against fit, in adjacent sentences — the slope comparison and the fit comparison point opposite ways and are reported separately, so two regressions become one claim. "In fact" and "That said" are the hinges, and they are the plainest possible translation of the report's version. Reporting a steeper slope and a worse fit in the same breath, and refusing to let either stand for the relationship, is a house move.

### Against the null value of an index

> Countries with an AUI greater than 1 use Claude more often than we'd expect based on their working-age population alone, and vice-versa.

**Annotation.** The benchmark is built into the measure, so every subsequent value is a comparison without the prose having to say so. One sentence of scale-setting buys the rest of the section.

### Across waves of the same series

> the proportion of 'directively' automated tasks increased sharply from 27% to 39%

> educational instruction tasks have risen by more than 40 percent (from 9% to 13% of all conversations)

> This means that for the first time, automation (49.1%) has become more common than augmentation (47%) overall.

**Annotation.** Every change is a level pair, and the elapsed interval is restated each time the section opens ("Since December 2024", "Over the past nine months"), so no magnitude is quoted without its denominator. "For the first time" is a comparison to the series' own history and is the one claim on this page that a first-wave post could not make — the compounding value of keeping definitions stable across waves, stated in four words.

### Claude.ai against the API

> 44% of the API traffic in our sample maps to computer or mathematical tasks, compared to 36% of tasks on Claude.ai … (4% in the API relative to 12% on Claude.ai), and arts and entertainment (5% relative to 8%).

> 77% of our API conversations show automation patterns … while just 12% show augmentation. On Claude.ai, the split is almost even.

**Annotation.** One pair of samples compared on two dimensions, matched rounding on both sides of every pair, and the second comparison given qualitatively because the quantitative version is three paragraphs above. The compression is honest here: the report compares the two surfaces on five dimensions and the blog keeps the two that a reader can hold.

### To prior general-purpose technologies

> But it does raise a question of economic divergence: previous general-purpose technologies, like electrification or the combustion engine, led to both vast economic growth and a great divergence in living standards around the world. If the effects of AI prove to be largest in richer countries, this general-purpose technology might have similar economic implications.

**Annotation.** The report's stakes paragraph, compressed to two sentences and structurally intact: historical precedent stated as fact and hyperlinked to its source; application to the present stated as a conditional whose antecedent — that AI's effects are largest in richer countries — is precisely what the post has *not* measured. "might have similar economic implications" keeps the modal. This is the whole why-it-matters of a 47-page report in 62 words, and nothing load-bearing was dropped to get there. **This is the model for compressing a stakes paragraph.**

### Against expectation, twice

> and, surprisingly, that the very highest-use states *aren't* the ones where coding dominates

> Perhaps surprisingly, in countries with higher Claude use per capita, Claude's uses tend towards augmentation

**Annotation.** Both flag the surprise before the result, so the reader knows which way to lean. The post spends "surprising" exactly twice, on the two results that contradict a prior a reader would actually hold, and never as a decoration.

## Figure captions

Ten captioned exhibits plus one uncaptioned hero image and one embedded video. Captions on this page are **italic, unnumbered, set immediately below the image, no "Figure N" label, no source line, one sentence each** — against the report's bold-numbered-declarative-title-plus-roman-gloss. They are between six and twenty-six words; the report's run to five sentences. Alt text is not caption text; numbers appearing only in alt text are marked below and are never quoted as prose.

1. *Leading countries in terms of global Claude.ai use share.*
   — Alt text: "Top 30 countries by share of global Claude use: the US leads with 21.6%." **21.6% and the top-30 cut are alt text only (alt text).** The caption is the report's Figure 2.1 title with the gloss removed and a period added. No sample, no floor, no date.
2. *The twenty countries that score highest on our Anthropic AI Usage Index.*
   — Alt text: "The twenty countries that score highest on our Anthropic AI Usage Index: Israel, Singapore, Australia, New Zealand, and South Korea are the top five." **The top-five ordering is alt text only (alt text).** The caption names the exhibit's extent (twenty) and nothing else; the reader must read the chart to learn who leads, which is the failure mode the corpus flags for the February 2025 post's representation figure.
3. *Claude use per capita is positively correlated with income per capita across countries. (Axes are on a log scale.)*
   — The best caption on the page and the only one that is a declarative finding. The parenthetical is a genuine caveat in caption position: on a log-log plot the visual slope is an elasticity, and the reader is told so in six words. **Copy the parenthetical-axis-note device.**
4. *US states' Claude adoption relative to their working age populations.*
   — Alt text: "Graph showing US states' Claude adoption relative to their working age populations, with Utah and DC in the lead." **Utah's rank is in alt text (alt text)**; the body never names Utah. Caption states the measure without naming it as the AUI.
5. *Changes in Claude use over time, showing increases in use for scientific and educational tasks.*
   — Alt text adds "and decreases for arts, business, and architecture uses". The caption keeps the rises and drops the falls; the alt text is more complete than the caption, which is the wrong way round.
6. *As we move from lower to higher adoption countries, Claude use appears to shift to a more diverse mix of tasks, although the overall pattern is noisy.*
   — The only caption carrying a hedge, and the hedge is in the caption because the finding is noisy — the report's rule ("if the finding is noisy or conditional, the hedge goes in the title") applied faithfully in a different typographic form. The four panels are not explained; the body does that job ("Compare the trend line in the first graph below to the remaining three"), which splits panel logic across two places.
7. *Automation appears to be increasing over time.*
   — Six words. Names neither Claude nor the sample nor the units; lifted out of the page it means nothing. The one caption here that would fail the report's own template.
8. *Countries with higher Claude use per capita tend to use Claude in a more collaborative manner.*
   — A declarative finding with "tend to" as its fence, and it translates the technical pole ("augmentation") into plain words ("a more collaborative manner") for a reader who skips to the charts. Note that the controlling-for-task-mix condition, which the body states, is not in the caption — so the caption's claim is the unconditional one.
9. *Augmentation and automation with Claude on Claude.ai vs. the API.*
   — Descriptive rather than declarative, correctly: the exhibit is a two-panel comparison and the finding is in the body.
10. *Cost per task plotted against the task category's share of total conversations.*
    — Names both axes and nothing else. No units for cost, no sample, no Claude. Descriptive where the body's claim is a correlation, so the exhibit understates what it is showing.

**The companion caption pattern, distilled.** Italic, unnumbered, one sentence, no terminal-period discipline to speak of; declarative where a finding can be stated in a clause and descriptive otherwise; the hedge in the caption when the pattern is noisy; the sample, the floors, the construction and the provenance all dropped. Against the report's template this is a real loss — the report's captions are written to be lifted, and six of these ten are not. **The transferable part is the axis parenthetical in caption 3 and the plain-language gloss of a technical pole in caption 8; the rest is what a caption looks like when it is asked only to label.**

## Limitations

**There is no limitations section, and no "Caveats" heading.** As in the report, the caveats are dispersed — but from twenty-eight footnotes and a dozen in-sentence fences down to three footnotes and six in-sentence fences. Verbatim, everything on the page that does the work of a limitation.

### In the sentence carrying the finding

> That doesn't mean these are the *most popular* tasks: software engineering is still by far in the lead in almost every state and country in the world.

> However, there is huge variation in population size across these countries.

> (In absolute terms, of course, the number of conversations in each category has still risen significantly.)

> The overall trend is noisy, but generally, as the GDP per capita of a country increases, the use of Claude shifts *away* from tasks in the Computer and Mathematical occupation group

> All that said, software development remains the most common use in every single country we track. The picture looks similar in the US, although our sample size limits our ability to explore in more detail how the task mix varies with adoption rates.

> We're not yet sure why this is. It could be because early adopters in each country feel more comfortable allowing Claude to automate tasks, or it could be down to other cultural and economic factors.

### In footnotes

> [1] As for Utah, in second: when further investigating Utah's activity, we discovered that a notable fraction of its use appeared to be associated with indicators of coordinated abuse – which is also reflected in Utah's much higher "directive" automation score than average. However, we ran robustness checks and believe that this activity is not driving the results.

> [2] We supplement this with a 'bottom-up' task classification in which Claude classifies conversations according to its own taxonomy, in order to address any gaps in the O\*NET categories. The full details of our privacy-preserving analysis methodology are available here.

> [3] Data in this section covers 1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage. We continue to manage data according to our privacy and retention policies, and our analysis is consistent with our terms, policies, and contractual agreements.

**Annotation.**

- **Placement.** The best-placed caveats on the page are the three in-sentence ones, and all three are in the position the corpus recommends: immediately after the claim they qualify, inside the same paragraph, before the reader can over-read. The opening's "That doesn't mean these are the *most popular* tasks" is a whole caveat given the second sentence of the post.
- **Specificity, where it survives.** Footnote 3 is quoted from the report essentially word for word and is the most specific thing on the page: sample size, month, sampling method, and the coverage fraction quantified rather than described ("roughly half of our 1P API usage"). "our sample size limits our ability to explore in more detail how the task mix varies with adoption rates" names the constraint and the analysis it prevented, which is the useful form of a power caveat.
- **What a referee would raise first, and it is not on the page.** (i) *The Claude.ai sample is never described.* No window, no count, no privacy filter, no observation floor, no geolocation method, no VPN exclusion. Every geographic number on this page rests on IP geolocation of conversations, and the page does not say so — so a reader cannot know that the AUI measures where conversations originate rather than where people live. The report puts this in footnote 2 of Chapter 2; the companion drops it entirely. **This is the omission that matters most, because the post's headline construct is geographic.**
- (ii) *The classifier changed between waves.* Absent, and the crossover it threatens is the post's most quotable claim. See Finding 5.
- (iii) *The cost result is unconditional.* Absent, and the mechanism conclusion drawn from it belongs to the conditional version. See Finding 9.
- (iv) *The 3.9% residual* between 49.1% automation and 47% augmentation is unexplained, as the equivalent residual is in the report.
- **What the companion does better than the report.** Utah. The report puts 3.78x in a headline bullet on page 4 and the abuse caveat in footnote 7 on page 29; the blog never states Utah's value in prose and attaches the caveat to the only mention. The honesty is the same and the distance between claim and caveat is nearly zero. It is still a footnote, and "we ran robustness checks and believe that this activity is not driving the results" is still belief rather than demonstration — the word "believe" is doing the same honest work in both documents.
- **The lesson for a companion piece of our own.** Dropping the apparatus is legitimate; dropping the *sample* is not. A short version can lose the tier thresholds, the Gini and the equation; it cannot lose the sentence that says what was measured, over what window, and with what excluded. The form to use: keep the in-sentence fences, keep one sample footnote per data source, and keep every caveat whose absence would let a reader believe something the long version denies.

## Close

Verbatim, the Conclusion in full, and the first sentence of Open data.

> ## Conclusion

> The Economic Index is designed to provide an early, empirical assessment of how AI is affecting people's jobs and the economy. What have we found so far?

> Across each of the measures we cover in this report, the adoption of AI appears remarkably uneven. People in higher-income countries are more likely to use Claude, more likely to seek collaboration rather than automation, and more likely to pursue a breadth of uses beyond coding. Within the US, AI use seems to be strongly influenced by the dominant industries in local economies, from technology to tourism. And businesses are more likely to entrust Claude with agency and autonomy than consumers are.

> Beyond the fact of unevenness, it's especially notable to us that directive automation has become much more common in conversations on Claude.ai over the past nine months. The nature of people's use of Claude is evidently still being defined: we're still collectively deciding how much confidence we have in AI tools, and how much responsibility we should give them. So far, though, it looks like we're becoming increasingly comfortable with AI, and willing to let it work on our behalf. We're looking forward to revisiting this analysis over time, to see where—or, indeed, *if*—users' choices settle as AI models improve.

> If you'd like to explore our data yourself, you can do so on our dedicated Anthropic Economic Index website, which contains interactive visualizations of our country, state, and occupational data. We'll update this website with more data in future, so you can continue to track the evolution of AI's effects on jobs and the economy in the ways that interest you.

> Our full report is available here. We hope it helps policymakers, economists and others more effectively prepare for the economic opportunities and risks that AI provides.

> ## Open data

> As with our past reports, we're releasing a comprehensive dataset for this release, including geographic data, task-level use patterns, automation/augmentation breakdowns by task, and an overview of API use.

**Annotation.**

- **What was learned.** Stated as a shape and then as a parallel triple. "the adoption of AI appears remarkably uneven" is the report's "And yet early AI adoption is strikingly uneven" with one adverb swapped and one hedge added ("appears"). The next sentence is the whole geography chapter in three parallel clauses — "more likely to use Claude, more likely to seek collaboration rather than automation, and more likely to pursue a breadth of uses beyond coding" — one subject, three predicates, no numbers. **Three findings compressed into one sentence by holding the subject fixed and varying only the predicate.** That construction is the most efficient thing on the page and it is exactly the right tool when the close must carry several results and no figures.
- **No numbers in the close.** Not one, across five paragraphs. Same as the report, same as February 2025. This is now a corpus-wide invariant: **Anthropic's economics closes contain no quantities.**
- **Why it matters.** Not where the report puts it. The report's stakes are in its close ("These patterns risk creating divergence"); the blog spent its divergence paragraph in the middle of the countries section and its close is about something else — the *indeterminacy* of current behaviour. "The nature of people's use of Claude is evidently still being defined: we're still collectively deciding how much confidence we have in AI tools, and how much responsibility we should give them." The "we" there is not Anthropic; it is everybody, and the switch is unmarked and effective. A companion piece is allowed to end on a different note from its report, and this one ends on the note a general reader can act on.
- **What comes next.** Committal about method, silent about direction, and phrased as a question rather than a plan: "We're looking forward to revisiting this analysis over time, to see where—or, indeed, *if*—users' choices settle as AI models improve." The italicised *if* is the last emphasis on the page and it is spent undermining the post's own extrapolation — the same move as the report's "the patterns of technological adoption aren't fixed", in one word instead of a paragraph. **A close that italicises the word that admits the trend may not continue is doing the corpus's characteristic thing.**
- **Recommendations.** One, and it is delegated: "We hope it helps policymakers, economists and others more effectively prepare for the economic opportunities and risks that AI provides." The report tells policymakers to attend to local concentration and digital divides; the blog names the audience and hands them the report. No instrument, no direction of attention, no prescription. Between February 2025's explicit refusal and the report's three hedged recommendations, the companion sits closest to the refusal.
- **How it avoids a template summary.** Four devices. (i) The question "What have we found so far?" — a summary that asks itself the question is not a summary block; it is a section opening. (ii) The parallel triple, which restates three findings without restating any number. (iii) "Beyond the fact of unevenness" — the close names its own thesis and then goes past it, so the last substantive paragraph is about something the body only implied. (iv) The final sentence is a question about the future of behaviour, not a claim about the past.
- **Title against ending.** Title: "Tracking AI's role in the US and global economy." Ending: "revisiting this analysis over time", "We'll update this website with more data in future", "continue to track the evolution of AI's effects". The title's verb is *tracking*, and the close is three sentences of tracking. They match — though note what this means: the title promises an instrument, not a finding, so the close is allowed to end on continuation rather than on consequence. The report's title names a finding ("Uneven … adoption") and its close therefore has to end on that finding's consequence. **The rule the pair demonstrates: a tracking title licenses a tracking close; a finding title does not.**
- **First person.** Heavier than anywhere else in the corpus and used for three different jobs — institutional acts ("we're releasing", "We'll update"), analytical acts ("we found", "we cover"), and *the reader and author together* ("we're still collectively deciding", "we're becoming increasingly comfortable"). House style forbids all three. The first two have known substitutes (passive; attribute to the analysis or the exhibit). The third has no clean substitute and should not be reached for: the collective "we" is the companion form's signature move and it is also the point at which the writing stops being empirical.

## Verification

- **URL fetched:** https://www.anthropic.com/research/economic-index-geography — fetched 2026-09-16, returned in full (page title "Economic Index: AI's role in the US and global economy \ Anthropic", H1 "Anthropic Economic Index: Tracking AI's role in the US and global economy", dated "Sep 15, 2025", all three footnotes present). Every quotation in this file was copied from that fetch and checked back against it word by word after transcription.
- **Fetch date:** 2026-09-16. **Fetch failures: none.** The page returned complete on the first attempt.
- **PDF or appendix:** none exists for this slug; the `wiki/INDEX.md` row carries `—` in the PDF column. Nothing was missing.
- **Not fetched, deliberately:** the September 2025 report (its own slug, `economic-index-2025-09-report`); the February 2025 post (`economic-index-2025-02-report`); the March 2025 post; the Clio post; the interactive Economic Index site; the Hugging Face dataset card; the Pritchett JEP article; claude.ai; the job posting. No content from any of them is quoted here.
- **The embedded video** (https://cdn.sanity.io/files/4zrzovbb/website/1d6f559fc58ef744b30a15322e08e00c337bf3c9.mp4) was not opened. It sits directly below the hero image, carries no caption, and nothing in this file depends on it.
- **Comparisons to the report** in `## Section order`, `## Findings and their caveats` and `## Limitations` are drawn from `wiki/style/economic-index-2025-09-report.md`, our own corpus file, and not from a fetch of the report performed today. Where this file says the report's number differs from the blog's, that is a comparison against quotations recorded in that file on 2026-09-16; the report was not re-fetched to confirm it.
- **Quotation caveats.**
  - Hyperlink URLs were stripped from quoted prose and the anchor text retained; the anchors in the opening are listed in `## Opening move`. Where the source renders "Claude.ai" as a link inside a sentence, the link is stripped and the word kept.
  - Typographic apostrophes, quotation marks and ellipses in the source were normalised to ASCII. Dashes are reproduced as they appear (the page mixes "–" and "—"). No word was changed.
  - Footnote markers appear in the source as bare superscript digits run onto the preceding word ("fourth.1", "them.2", "analysis.3"); quotations here render them as "[1]", "[2]", "[3]" and the footnote texts are numbered to match.
  - Emphasis (bold, italic) is reproduced as it appears in the fetched text. Captions on this page are italic in the source; they are quoted in italic in `## Figure captions` and the italics are not an addition.
  - **Alt text and chart-image numbers, per `room/director-2026-09-16-alt-text-ruling.md`.** The italic sentence under an image is the caption and is quoted as such. Numbers and rankings that appear only in image alt text — the 21.6% US share, the top-30 cut, the top-five AUI ordering, Utah's rank, and the "decreases for arts, business, and architecture uses" in exhibit 5 — are recorded only in `## Figure captions`, each marked **(alt text)** at the point of use, and are never quoted as prose or as a caption. **No number was read off a chart image and recorded anywhere in this file.** Every number quoted here appears in the page's body prose or its footnotes.
- **Scope.** This file annotates how the companion post is written and how it compresses the report it accompanies: its section order, the grammar of its findings and caveats, how its comparisons are phrased, its caption pattern, where its limitations sit and how it closes. It makes no judgement about whether any finding is correct. Where this file says a caveat is missing or a result is stated without its qualifying specification, that is a statement about the writing, not about the analysis.
