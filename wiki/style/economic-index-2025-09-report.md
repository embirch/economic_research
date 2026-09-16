# economic-index-2025-09-report — style annotation

## Source

- **Title (PDF cover, and the document of record):** "The Anthropic Economic Index report: Uneven geographic and enterprise AI adoption". The web page H1 drops the leading article: "Anthropic Economic Index report: Uneven geographic and enterprise AI adoption". Browser/OG title on the web page is shortened again to "Economic Index: Uneven AI adoption".
- **Date:** PDF cover, "Published: September 15, 2025". Web page, "Sep 15, 2025".
- **URLs fetched:**
  - PDF (document of record): https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf — 47 pages.
  - Web page: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
  - The `wiki/INDEX.md` row also lists an identical file at https://www-cdn.anthropic.com/7b76335c444876a93fa22a63aabb4aeb820aff25.pdf and an arXiv version at https://arxiv.org/abs/2511.15080. Neither was fetched for this file (see `## Verification`).
- **Document type:** the third wave of a standing report series ("This third iteration of the Anthropic Economic Index Report"). Not a launch post, not a paper: a three-chapter report with a named author list, chapter-level conclusions, 14 numbered footnotes in its longest chapter, and no abstract.
- **Approximate length:** 47 PDF pages. Cover, 1 p.; Introduction, pp. 2–6; Chapter 1, pp. 7–11; Chapter 2, pp. 12–29; Chapter 3, pp. 30–45; Concluding remarks, pp. 46–47. Twenty numbered figures, three numbered tables, one uncaptioned equation image. Roughly 9,000–10,000 words of body prose plus about 2,000 words of footnotes.
- **Authors named on the cover:** "Ruth Appel\*, Peter McCrory\*, Alex Tamkin\* / Miles McCain, Tyler Neylon, Michael Stern", with "\*Lead authors. Contributed equally to this report." Two tiers of authorship, contribution equality asserted for the starred tier only. Forty-seven acknowledgees, unsorted by role. The web page moves all of this from the cover to an "Authors and Acknowledgments" section at the foot of the article and appends a BibTeX `@online` citation block.
- **Audience:** economists and policymakers who will be asked to act on the findings. The Introduction cites Gallup, Bick–Blandin–Deming, Lewis & Severnini, Kalyani et al., Gordon, Pritchett, Kremer–Willis–You and Jones–Jones–Aghion in its first five pages; Chapter 3 cites Hall & Kahn, Gabaix, Kremer's O-Ring paper, Liu et al. and Ide & Talamás. The reader is assumed to know what a partial regression, a Lorenz curve, a Gini coefficient and an elasticity are — though every one of those four is glossed anyway, in a footnote or a parenthesis.

### How the web page condenses the PDF

Very little: the web page is close to the full text, not a summary. The differences that matter for style are:

1. **One exhibit is dropped.** Table 2.2 ("Claude per capita usage tiers with examples, number of states, and AUI range for each tier", PDF p. 20) has no counterpart on the web page, which goes straight from Figure 2.6 to "Task usage patterns across countries". The country-level Table 2.1 survives; its US twin does not.
2. **In-text figure references drift out of step in Chapter 3.** From Figure 3.5 onward the web page's cross-references sit one number above the captions it carries. Web page: "97% of tasks show automation-dominant patterns in API usage, compared to only 47% on Claude.ai (Figure 3.6)" — PDF, same sentence, "(Figure 3.5)". Web page: "Figure 3.7 shows that output length varies systematically across occupational categories as well" — PDF, "Figure 3.6 shows that…". Web page: "higher-cost tasks tend to have higher usage rates (Figure 3.9)" — PDF, "(Figure 3.8)". Web page: "a 0.29% reduction in usage frequency in our sample of API transcripts (Figure 3.10)" — PDF, "(Figure 3.9)". The captions themselves are numbered identically in both. The PDF is internally consistent; the web version is not. Take the PDF as the reference when citing a figure from this report.
3. **Caption typography changes.** PDF: bold "Figure 2.1: Leading countries in terms of global Claude.ai usage share" with **no period** after the title, then the gloss in plain roman. Web page: the bold title takes a period and the whole caption is italicised. Same words, different weight.
4. **Front matter moves to the back.** Authors and acknowledgements are the first thing a PDF reader sees and the last thing a web reader sees.
5. **Chapter titles are recased.** PDF "Chapter 1: Claude.ai Usage Over Time" (title case) → web "Chapter 1: Claude.ai usage over time" (sentence case).

Nothing is cut from the argument, no finding is softened, and no number changes. The condensation is typographic and navigational, not editorial — which is itself the house pattern: the report is the report, and the web page is the report with a different skin.

## Section order

Headings in PDF order. Page spans are the PDF's own numbering.

1. **Cover (p. 1).** Title, authors, acknowledgements, publication date. No abstract, no summary of findings, no figure.
2. **Introduction (pp. 2–6), ~1,400 words.** Runs in five moves: (i) three paragraphs on adoption speed and the history of diffusion, ending in a bolded thesis sentence; (ii) one paragraph naming what the report adds; (iii) three chapter previews, each a short framing paragraph followed by a bolded **"We find:"** bullet block carrying that chapter's headline numbers; (iv) two paragraphs on convergence that sit between the second and third preview and carry the report's stakes; (v) an "Open source data to catalyze independent research" block ending in four open questions for other researchers. Five footnotes, all to outside literature, set on their own page (p. 6).
3. **Chapter 1: Claude.ai Usage Over Time (pp. 7–11), ~1,300 words.**
   - *Overview* (p. 7, ~130 words) — defines the V1/V2/V3 waves and their dates, and states the chapter's interpretation up front.
   - *How Claude.ai usage for economic tasks has changed* with three sub-headings: *Educational and scientific tasks continue their rise in relative importance*; *New capabilities are shaping usage patterns*; *Directive automation is accelerating*. Figures 1.1 and 1.2.
   - *Looking Ahead* (p. 11, ~130 words) — chapter close.
   - Five footnotes, including the two longest methodological caveats in the chapter.
4. **Chapter 2: Claude usage across the United States and the globe (pp. 12–29), ~3,400 words.** The longest chapter.
   - *Overview* (p. 12) — four paragraphs; states what the data "confirmed" and what it "challeng[ed]".
   - *Claude diffusion across the globe* (pp. 13–18) — sub-headings *Total Claude usage is highest in the US*; *Per capita usage of Claude is concentrated in technologically advanced countries* (introduces and defines the AUI); *Zooming into leading and emerging countries in terms of per capita usage*. Figures 2.1–2.4, Table 2.1, plus the uncaptioned AUI equation. Ends in a five-bullet list of candidate mechanisms.
   - *Claude diffusion across the United States* (pp. 18–20) — Figures 2.5, 2.6, Table 2.2.
   - *Task usage patterns across countries* (pp. 20–24) — explains the two taxonomies (O\*NET and bottom-up), then *Higher per capita Claude usage is associated with more diverse task usage*. Figures 2.7, 2.8. Ends in a three-bullet list of why coding leads.
   - *Task usage patterns across the United States* (pp. 24–26) — Figures 2.9, 2.10.
   - *Geographic patterns in human-AI collaboration* (pp. 26–27) — Figure 2.11.
   - *Conclusion* (pp. 27–28, ~260 words) — chapter close, ending in the report's only direct address to policymakers.
   - Nine footnotes (pp. 28–29), carrying the privacy filters, the sample definition, the geolocation method, the tier thresholds, the map's disputed-territory policy, the Utah abuse finding and the partial-regression procedure.
5. **Chapter 3: API Enterprise Deployment of Claude (pp. 30–45), ~3,000 words.**
   - *Overview* (pp. 30–31) — four paragraphs plus a three-bullet findings block; states the theoretical prior ("Institutional inertia, alongside fixed costs of adoption, suggests…") before the data.
   - *Setting the stage: AI adoption patterns in public data* (pp. 31–32) — external benchmark first, own data second. Figure 3.1.
   - *Specialized use among Anthropic API customers* (pp. 32–34) — Figures 3.2, 3.3.
   - *Occupational segmentation vs. task specialization* (pp. 34–35) — Figure 3.4.
   - *Automation vs. augmentation among API transcripts* (pp. 36–37) — Figure 3.5.
   - *The more Claude does, the more Claude needs to know* (pp. 37–41) — Table 3.1, Figures 3.6, 3.7. The most argued section in the report: mechanism, measurement construction, incentive argument, elasticity, upshot.
   - *Cost per task and substitution patterns across tasks* (pp. 41–43) — Figures 3.8, 3.9.
   - *Conclusion* (pp. 43–44, ~250 words) — chapter close.
   - Fourteen footnotes (pp. 44–45).
6. **Concluding remarks (pp. 46–47), ~600 words.** Six paragraphs, one bolded single-sentence paragraph among them, and one footnote that stages two opposed readings of the same external evidence.

**Where the findings sit: before the methods, twice over, and then again after.** The headline numbers appear on pp. 3–5 in the three "We find:" blocks — before the word Clio, before the sample definition, before the AUI is defined. Each chapter then repeats the structure in miniature: an *Overview* that states the finding and its interpretation, then the sections that earn it. The sample definitions live in footnote 2 of Chapter 2 (1 million Claude.ai conversations, 4–11 August 2025) and footnote 2 of Chapter 3 (1 million API transcripts, August 2025, ~half of 1P usage) — that is, a reader reaches every number in the report before reaching the description of the data that produced it. This is the series' settled architecture, and it is worth naming as a choice rather than an accident: the report is written to be read in three depths (bullets, overviews, chapters), and each depth is self-consistent.

**Where the methods sit.** Nowhere as a section. There is no "Data and methods" heading in the 47 pages. Method is distributed: the AUI is defined where it is first used (p. 14), the two taxonomies where they are first used (pp. 20–21), the collaboration modes where they are first used (p. 9), the token indices where they are first used (p. 38), and everything about the sample, the privacy thresholds and the identification is in footnotes. The report's pattern is *define at point of use, document in footnote*.

## Opening move

### The Introduction, first four paragraphs, verbatim

> AI differs from prior technologies in its unprecedented adoption speed. In the US alone, 40% of employees report using AI at work, up from 20% in 2023 two years ago.[1] Such rapid adoption reflects how useful this technology already is for a wide range of applications, its deployability on existing digital infrastructure, and its ease of use—by just typing or speaking—without specialized training. Rapid improvement of frontier AI likely reinforces fast adoption along each of these dimensions.

> Historically, new technologies took decades to reach widespread adoption. Electricity took over 30 years to reach farm households after urban electrification. The first mass-market personal computer reached early adopters in 1981, but did not reach the majority of homes in the US for another 20 years. Even the rapidly-adopted internet took around five years to hit adoption rates that AI reached in just two years.[2]

> Why is this? In short, it takes time for new technologies—even transformative ones—to diffuse throughout the economy, for consumer adoption to become less geographically concentrated, and for firms to restructure business operations to best unlock new technical capabilities. Firm adoption, first for a narrow set of tasks, then for more general purpose applications, is an important way that consequential technologies spread and have transformative economic effects.[3]

> **In other words, a hallmark of early technological adoption is that it is *concentrated*—in both a small number of geographic regions and a small number of tasks in firms.** As we document in this report, AI adoption appears to be following a similar pattern in the 21st century, albeit on shorter timelines and with greater intensity than the diffusion of technologies in the 20th century.

> To study such patterns of early AI adoption, we extend the Anthropic Economic Index along two important dimensions, introducing a geographic analysis of Claude.ai conversations and a first-of-its-kind examination of enterprise API use. We show how Claude usage has evolved over time, how adoption patterns differ across regions, and—for the first time—how firms are deploying frontier AI to solve business problems.

("Anthropic Economic Index" is hyperlinked to the Index landing page; no other link in these paragraphs.)

### The three "We find:" blocks, verbatim

> **Changing patterns of usage on Claude.ai over time**
>
> In the first chapter of this report, we identify notable changes in usage on Claude.ai over the previous eight months, occurring alongside improvements in underlying model capabilities, new product features, and a broadening of the Claude consumer base.
>
> We find:
>
> - **Education and science usage shares are on the rise.** While the use of Claude for coding continues to dominate our total sample at 36%, educational tasks surged from 9.3% to 12.4%, and scientific tasks from 6.3% to 7.2%.
> - **Users are entrusting Claude with more autonomy.** "Directive" conversations, where users delegate complete tasks to Claude, jumped from 27% to 39%. We see increased program creation in coding (+4.5pp) and a reduction in debugging (-2.9pp)—suggesting that users might be able to achieve more of their goals in a single exchange.

> **The geography of AI adoption**
>
> For the first time, we release geographic cuts of Claude.ai usage data across 150+ countries and all U.S. states. To study diffusion patterns, we introduce the Anthropic AI Usage Index (AUI) to measure whether Claude.ai use is over- or underrepresented in an economy relative to its working age population.
>
> We find:
>
> - **The AUI strongly correlates with income across countries.** As with previous technologies, we see that AI usage is geographically concentrated. Singapore and Canada are among the highest countries in terms of usage per capita at 4.6x and 2.9x what would be expected based on their population, respectively. In contrast, emerging economies, including Indonesia at 0.36x, India at 0.27x and Nigeria at 0.2x, use Claude less.
> - **In the U.S., local economy factors shape patterns of use.** DC leads per-capita usage (3.82x population share), but Utah is close behind (3.78x). We see evidence that regional usage patterns reflect distinctive features of the local economy: For example, elevated use for IT in California, for financial services in Florida, and for document editing and career assistance in DC.
> - **Leading countries have more diverse usage.** Lower-adoption countries tend to see more coding usage, while high-adoption regions show diverse applications across education, science, and business. For example, coding tasks are over half of all usage in India versus roughly a third of all usage globally.
> - **High-adoption countries show less automated, more augmented use.** After controlling for task mix by country, low AUI countries are more likely to delegate complete tasks (automation), while high-adoption areas tend toward greater learning and human-AI iteration (augmentation).

> The uneven geography of early AI adoption raises important questions about economic convergence. Transformative technologies of the late 19th century and the early 20th centuries—widespread electrification, the internal combustion engine, indoor plumbing—not only ushered in the era of modern economic growth but accompanied a large divergence in living standards around the world.[4]

> If the productivity gains are larger for high-adoption economies, current usage patterns suggest that the benefits of AI may concentrate in already-rich regions—possibly increasing global economic inequality and reversing growth convergence seen in recent decades.[5]

> **Systematic enterprise deployment of AI**
>
> In the final chapter, we present first-of-its-kind insight on a large fraction of our first-party (1P) API traffic, revealing the tasks companies and developers are using Claude to accomplish. Importantly, API users access Claude programmatically, rather than through a web user interface (as with Claude.ai). This shows how early-adopting businesses are deploying frontier AI capabilities.
>
> We find:
>
> - **1P API usage, while similar to Claude.ai use, differs in specialized ways.** Both 1P API usage and Claude.ai usage focus heavily on coding tasks. However, 1P API usage is higher for coding and office/admin tasks, while Claude.ai usage is higher for educational and writing tasks.
> - **1P API usage is automation dominant.** 77% of business uses involve automation usage patterns, compared to about 50% for Claude.ai users. This reflects the programmatic nature of API usage.
> - **Capabilities seem to matter more than cost in shaping business deployment.** The most-used tasks in our API data tend to cost more than the less frequent ones. Overall, we find evidence of weak price sensitivity. Model capabilities and the economic value of feasibly automating a given task appears to play a larger role in shaping businesses' usage patterns.
> - **Context constrains sophisticated use.** Our analysis suggests that curating the right context for models will be important for high-impact deployments of AI in complex domains. This implies that for some firms costly data modernization and organizational investments to elicit contextual information may be a bottleneck for AI adoption.

> **Open source data to catalyze independent research**
>
> As with previous reports, we have open-sourced the underlying data to support independent research on the economic effects of AI. This comprehensive dataset includes task-level usage patterns for both Claude.ai and 1P API traffic (mapped to the O\*NET taxonomy as well as bottom-up categories), collaboration mode breakdowns by task, and detailed documentation of our methodology. At present, geographic usage patterns are only available for Claude.ai traffic.

> Key questions we hope this data will help others to investigate include:
>
> - What are the local labor market consequences for workers and firms of AI usage & adoption?
> - What determines AI adoption across countries and within the US? What can be done to ensure that the benefits of AI do not only accrue to already-rich economies?
> - What role, if any, does cost-per-task play in shaping enterprise deployment patterns?
> - Why are firms able to automate some tasks and not others? What implications does this have for which types of workers will experience better or worse employment prospects?

### Annotation

- **What question is posed.** Not "how is AI used?" but "**why is this?**" — asked in the third paragraph, in three words, on its own. The question is about a *puzzle in the literature*, not about the data: technologies have always taken decades, this one has taken two years, and the report's job is to say what that implies about the shape of early adoption. The answer is given before any Anthropic number appears, as a bolded thesis: adoption is *concentrated*, geographically and in tasks. Both halves of that thesis then name a chapter. This is the strongest opening in the corpus so far, and the reason is structural: the thesis is a prediction from prior diffusion literature, and the report is positioned as a test of it rather than a description of Claude. Compare the February 2025 launch post, which opens *forecast → therefore measure*; this opens *anomaly → prior literature's explanation → therefore these two cuts*.
- **Who is said to be affected.** In the first sentence, "employees" — and specifically US employees, with a number. By the fourth paragraph the affected unit has widened to "geographic regions" and "firms", which is exactly the report's two-chapter split. The convergence passage then names the largest affected party in the report: countries, and the gap between them. Nobody is named as harmed in the Introduction; the harm is stated conditionally and quarantined in one sentence ("possibly increasing global economic inequality and reversing growth convergence seen in recent decades").
- **What the data is said uniquely to show.** Three claims of novelty, all narrowly scoped: "For the first time, we release geographic cuts of Claude.ai usage data across 150+ countries and all U.S. states"; "a first-of-its-kind examination of enterprise API use"; "and—for the first time—how firms are deploying frontier AI to solve business problems". Each attaches to a *cut of data*, never to a result. The word "first" does not modify a finding anywhere in the Introduction.
- **How soon the first number appears.** Second sentence: "40% of employees report using AI at work, up from 20% in 2023 two years ago", footnoted to Gallup. The first number in the report is **somebody else's survey**, not Anthropic's data — and it is used to establish the puzzle, not to support a claim. Anthropic's own first number is "36%" in the first bullet, about 400 words in. So: outside number to pose the puzzle, historical comparisons to sharpen it, bolded thesis, then own numbers. A post that opens on its own data has skipped the first two moves.
- **Register of the opening.** First person plural for institutional and analytical acts ("we extend", "we document", "we release", "we introduce", "We show", "we identify", "We find"), never for findings — the findings inside the bullets are agentless ("usage shares are on the rise", "coding tasks are over half of all usage in India"). The bolded lead-in of each bullet is a **claim in words**; the sentences after it are the **claim in numbers**. That two-beat bullet is the single most transferable device in this document.
- **The "We find:" block as a form.** Three blocks, one per chapter, two to four bullets each, every bullet a bolded claim plus one or two sentences of evidence, and — critically — a hedge inside almost every one: "seem to matter more than", "Our analysis suggests that", "This implies that for some firms", "tend to see", "appears to play a larger role", "might be able to achieve". The bullets are not a summary of the report; they are the report's *claims list*, written so that each can be checked against one chapter.
- **One editorial choice worth noticing.** The AUI bullet names Singapore (4.6x) and Canada (2.9x) as "among the highest countries". Israel, which Chapter 2 reports as the actual leader at 7.00, is not named in the Introduction at all. The summary picks its illustrations for recognisability rather than rank, and the word "among" carries the whole licence for doing so.
- **Precision varies with depth, deliberately.** Singapore is "4.6x" in the Introduction, "4.5 times what its working-age population would suggest" in the Chapter 2 overview, and "4.57" in the Chapter 2 body. Three roundings of one quantity, each matched to how hard the surrounding prose is working. The pattern to copy is the direction: coarser at the top, exact in the body — never the reverse.
- **The Introduction ends by handing the work away.** Four open questions, phrased as questions, addressed to other researchers, two of them normative ("What can be done to ensure that the benefits of AI do not only accrue to already-rich economies?"). This is the Index's standing move: the report states what it found and then states what it could not answer, as an invitation rather than a limitation.

## Findings and their caveats

### Chapter 1, Finding 1 — the composition shift across waves

> While computer and mathematical tasks still dominate overall usage at 36%, we are seeing sustained growth in knowledge-intensive fields. Educational Instruction and Library tasks rose from 9% in V1 to 12% in V3. Life, Physical, and Social Science tasks increased from 6% to 7%. Meanwhile, the *relative* share of Business and Financial Operations tasks fell from 6% to 3%, and Management dropped from 5% to 3%.

> This divergence suggests AI usage may be diffusing especially quickly among tasks involving knowledge synthesis and explanation, compared to traditional business operations—possibly because these tasks benefit more from Claude's reasoning capabilities.

**Annotation.** The dominant category is conceded in the subordinate clause ("While computer and mathematical tasks still dominate… at 36%") so the growth story cannot be mistaken for a change in the ranking. Every number is a pair — 9% → 12%, 6% → 7%, 6% → 3%, 5% → 3% — and the wave labels V1/V3 are attached to the first pair only, on the assumption that the reader carries them forward. The one italic in the passage does the caveat work: the *relative* share fell, which forecloses the reading that business usage declined in level. The interpretation paragraph is separated, stacked with three hedges in sixteen words ("suggests", "may be", "possibly because"), and its mechanism — reasoning capability — is offered without evidence and marked as offered. Note the naming: the observation says "tasks", the interpretation says "AI usage", and the mechanism says "Claude's reasoning capabilities". The further the sentence gets from the data, the more general the subject; the mechanism, which is about the product, says Claude.

### Chapter 1, Finding 2 — feature launches visible in task composition

> At a more granular level, we document changes in task composition that appear linked to features launched between V2 and V3. For example, searching electronic sources and databases grew substantially (0.03% → 0.49%), likely reflecting our web search release in March. In addition, we also see a rise in internet-based research tasks (0.003% → 0.27%), which aligns with the Research mode we released in April.[1]

> We also see other kinds of changes. Tasks relating to developing instructional materials increased by 1.3pp, growing from a base of 0.2% to 1.5%—a more than 6-fold increase that may reflect growing adoption among educators.[2] Creating multimedia documents rose 0.4pp, nearly tripling from 0.16% to 0.55%, potentially driven by continued use of our Artifacts feature for building traditional and AI-powered apps within Claude.ai.[3]

> Interestingly, the share of tasks involving creating new code more than doubled, increasing by 4.5 percentage points (from 4.1% to 8.6%), while debugging and error correction tasks fell by 2.8 percentage points (from 16.1% to 13.3%)—a net 7.4pp shift toward creation over fixing code. This may suggest that models have become increasingly reliable, such that users spend less time fixing problems and more time creating things in a single interaction.

**Annotation.** Four causal attributions, four different hedges, graded by how confident the authors are: "appear linked to", "likely reflecting", "aligns with", "may reflect", "potentially driven by". None is "because". Each small number is given **twice** — once as a change in percentage points and once as a ratio or a level pair ("increased by 1.3pp, growing from a base of 0.2% to 1.5%—a more than 6-fold increase") — which is how the report stops a 6-fold increase from sounding large and a 1.3pp increase from sounding trivial. The phrase "growing from a base of" is doing explicit anti-overclaim work. The code-creation result is built as a two-sided comparison with the net stated for the reader ("a net 7.4pp shift toward creation over fixing code"), and its interpretation is the weakest-hedged sentence of the three ("This may suggest that…"). Footnote 3 then lists every underlying task string with its own before-and-after pair — the aggregate is in the body, the construction is in the footnote, and the footnote is where a referee would go first.

### Chapter 1, Finding 3 — the crossover in collaboration mode

> The share of *directive* conversations sampled from Claude.ai conversations jumped from 27% in V1 in late 2024 to 39% in V3. This increase came primarily at the expense of *task iteration* and *learning* interactions, implying a sizable net increase in the share of conversations exhibiting automative patterns of use – a notable increase in just eight months. This is the first report where automation usage exceeds augmentation usage.

> One interpretation is that this is a result of increasing model capabilities. As models improve at anticipating user needs and producing high-quality outputs on first attempts, users may need fewer follow-up refinements. The jump in directive usage could also signal growing confidence in delegating complete tasks to AI, a form of learning-by-doing.[4]

> Whether the growth in directive usage is attributable to improving model capabilities or learning-by-doing could signal very different labor market implications. If more advanced models simply expand the set of automated tasks, then the risk increases that workers performing such tasks will be displaced. However, if instead the rise in directive use reflects learning-by-doing, then workers most able to adapt to new AI-powered workflows are likely to see greater demand and higher wages. In other words, AI may benefit some workers more than others: it may lead to higher wages for those with the greatest ability to adapt to technological change, even as those with lower ability to adapt face job disruption.[5] This will be an important area of inquiry for future research.

And the footnote that carries the caveat:

> [4] We note that V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison. To address this, we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (though to a lower absolute level of 45% automation versus 49% with Sonnet 4). We also verified this trend is not driven by changes in task mix—the shift toward directive interactions appears across a wide range of occupational categories, suggesting it reflects genuine changes in how people interact with Claude rather than compositional effects.

**Annotation.** The headline sentence — "This is the first report where automation usage exceeds augmentation usage" — is the most quotable line in the document and it is placed last in its paragraph, unhedged, with no number attached. It survives unhedged only because the paragraph before it has done the work: the direction is sourced ("came primarily at the expense of *task iteration* and *learning*"), the magnitude is characterised rather than asserted ("a sizable net increase", "a notable increase in just eight months"), and the two poles are defined a page earlier.

The instructive part is what happens next, and it is the best passage in the corpus so far on **separating observation from conjecture**. Two mechanisms are named. Neither is chosen. Instead the paragraph states *what would follow from each* — displacement under the capabilities story, wage gains for adaptable workers under the learning-by-doing story — and then states that the discrimination between them is future work. The finding is one number; the interpretation is a fork; the fork is left open on the page. That construction ("Whether X is attributable to A or B could signal very different labor market implications") is directly transferable and is exactly what the house rule *one claim tested at more than one level* is for.

And the caveat that a referee would raise first — the classifier changed between waves, so the trend may be an instrument artefact — is in footnote 4, not the body. It is answered there properly: rerun on the old classifier, direction holds, absolute level differs (45% versus 49%), and a second check that the shift is not compositional. The substance is exemplary; the placement is not. **In our own posts this goes in the body beside the finding, because it is the finding's main threat.**

### Chapter 2, Finding 1 — total usage concentration

> Claude adoption overall is highly geographically concentrated. In terms of total global usage, the United States accounts for the highest share (21.6%), with the next highest usage countries showing significantly lower shares (India at 7.2%, Brazil at 3.7%, see Figure 2.1). However, this concentration is affected by the population size of each country[3] – larger countries may have larger usage shares purely because of their population size.

**Annotation.** Three sentences: claim, numbers with a figure pointer, and then a sentence that **withdraws the natural reading of the numbers**. The third sentence is not a hedge on the measurement; it is a hedge on the inference, and it sets up the next section's whole reason for existing. Note that the caveat is not deferred — it lands in the same paragraph, immediately, before the reader has had a chance to over-read 21.6%. This is the cleanest instance in the report of *state the number, then state what the number cannot mean*.

### Chapter 2, Finding 2 — the AUI and its leaders

> To account for differences in population size, we analyze usage adjusted for the working-age population, introducing a new measure called the **Anthropic AI Usage Index (AUI):** For each geography, we calculate its share of Claude usage, and its share of the working-age population (ages 15-64). We then calculate the AUI by dividing these shares:

> This index reveals whether countries use Claude more or less than expected relative to their working-age population. A region with an AUI > 1 has higher usage than expected after adjusting for population, while a region with an AUI < 1 has lower usage.

> The results reveal a striking pattern of concentration among small, technologically advanced economies. Israel leads global per capita Claude usage with an Anthropic AI Usage Index of 7 — meaning its working-age population uses Claude 7x more than expected based on its population. Singapore follows at 4.57, while Australia (4.10), New Zealand (4.05) and South Korea (3.73) round out the top five countries in terms of per capita Claude usage.

> Notable is the position of major developed economies in Claude usage. The United States (3.62) ranks among leading countries in terms of per capita adoption, with Canada (2.91) and the United Kingdom (2.67) having elevated but more moderate rates of adoption as compared to their population. Other major economies show lower adoption, including France at 1.94, Japan at 1.86, and Germany at 1.84.

> Meanwhile, many lower and middle-income economies show minimal Claude usage, with many countries across Africa, Latin America, and parts of Asia showing Claude adoption below what would be expected based on their working-age population. This includes Bolivia (0.48), Indonesia (0.36), India (0.27), and Nigeria (0.2).

**Annotation.** The construct is defined in the sentence that introduces it, the interpretation of the scale is given its own paragraph before any value is quoted ("A region with an AUI > 1 has higher usage than expected…"), and the first value quoted is immediately glossed in plain words ("an Anthropic AI Usage Index of 7 — meaning its working-age population uses Claude 7x more than expected based on its population"). A reader who has never seen a location quotient can follow every subsequent number. Then three paragraphs in rank order — leaders, major economies, low-adoption economies — each a list of country-and-value pairs with no interpretive adjectives beyond "elevated but more moderate" and "minimal".

**Naming, and this is the report's sharpest instance of it:** the construct is called the **Anthropic AI Usage Index** and is defined as a geography's "share of Claude usage" over its share of working-age population. The name says AI; the measurement says Claude; and the text never once says "AI usage in Israel is 7x". Every value in Chapter 2 is attached to the words "Claude usage" or "Claude adoption". The naming rule is not applied to this report from outside — it is built into the report's central construct.

Also worth copying: the sample floor travels with the exhibit, not with the prose. Every figure in Chapter 2 that reports an AUI carries "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample" in its caption. The prose never repeats it. The reader who reads only captions still cannot misuse the number.

### Chapter 2, Finding 3 — the income gradient

> This variation in usage is reflective of income differences across these economies. We see a strong positive correlation between Claude adoption and Gross Domestic Product per working-age capita (see Figure 2.4), with a 1% increase in GDP per capita being associated with a 0.7% increase in Claude usage per capita.

> The disparities in Claude usage likely reflect a confluence of factors, some of which are correlated with income:
>
> - **Digital infrastructure:** High-usage countries typically have robust internet connectivity and cloud computing access needed to access AI assistants.
> - **Economic structure:** As documented in this and previous reports, Claude capabilities are well-suited to various tasks typical of knowledge workers. Advanced economies tend to have a greater share of the workforce in such roles as compared to lower-income economies with a larger employment share in manufacturing.
> - **Regulatory environment:** Governments differ in how actively they encourage the use of AI across different industries and in how heavily they regulate the technology.
> - **Awareness and access:** Countries with stronger connections to Silicon Valley and AI research communities may have greater awareness of and access to Claude.
> - **Trust and comfort:** Public opinion on trust in AI varies substantially across countries.

**Annotation.** "associated with" carries the elasticity, never "causes" or "leads to" — and the elasticity is given to one significant figure in the body (0.7) though the figure's own annotation reports a fitted coefficient to three. The mechanism discussion is the report's standard device for an unidentified association: a bulleted **confluence** — five candidate channels, each one or two sentences, none tested, none ranked, and the whole list prefaced by "likely reflect a confluence of factors, some of which are correlated with income". Naming five and choosing none is a way of writing "we cannot separate these" that is more useful to a reader than the sentence "we cannot separate these", because the five are now on the table for someone else to test. Note that two of the five (regulatory environment, trust and comfort) are supported only by external links, and one (economic structure) is supported by the report's own earlier findings — the bullets are not all the same kind of claim, and the prose does not pretend they are.

### Chapter 2, Finding 4 — states, and where the gradient weakens

> Within the US, California overwhelmingly leads with 25.3% of usage. Other states with major tech centers like New York (9.3%), Texas (6.7%), and Virginia (4.0%) also rank highly. Though not adjusted for population, we suspect that these strong adoption figures partly reflect rapid adoption in technology hubs—in keeping with how economically consequential technologies have historically tended to diffuse.

> This narrative becomes more complex, however, when we adjust for the population size of each state. Surprisingly, the District of Columbia leads with an Anthropic AI Usage Index of 3.82, indicating that Claude usage in DC is 3.82x greater than its share of the country's working-age population. Closely following is Utah (3.78), notably ahead of California (2.13), New York (1.58) and Virginia (1.57).[7]

> We document a similar, but weaker correlation than at the global level between Claude adoption and income per capita across US states. Income differences explain less than half the variation in cross-state adoption rates. Despite this weaker correlation, we find that Claude adoption rises faster with income: Each 1% increase in state GDP per capita is associated with a 1.8% increase in the AI Usage Index.

And the footnote:

> [7] When further investigating Utah's activity, we discovered a notable fraction of its usage appeared to be possibly associated with coordinated abuse. This is also reflected in a much higher "directive" automation score than average. However, we ran robustness checks and believe that this activity is not driving the results.

**Annotation.** "Though not adjusted for population" is placed as a sentence-opening concession *before* the interpretation it qualifies, which is the strongest available position and the opposite of an appended caveat. "This narrative becomes more complex, however" is the report's signature transition: the unadjusted picture is allowed to form, then complicated, rather than being pre-empted. "Surprisingly" is the report's marker for a result that contradicts the authors' prior, and it is used sparingly (four times in 47 pages) — which is what makes it carry weight.

The third paragraph is a model of reporting two facts that point in opposite directions in one breath: the correlation is *weaker* than at the global level (less than half the variation explained) but the slope is *steeper* (1.8% versus 0.7%). Both are stated, neither is resolved, and the concessive "Despite this weaker correlation" tells the reader that the authors know the two facts look contradictory. A weaker draft would have reported only the steeper slope.

Footnote 7 is the most consequential caveat in the report and it is in the smallest type: Utah, the number-two state named in the Introduction bullet, has usage "possibly associated with coordinated abuse" and an anomalous directive score. The footnote does the right things — flags it, explains why it matters, reports that robustness checks were run, states the conclusion — but it does not say what the checks were or what Utah's AUI is without the suspect traffic, and the Introduction bullet quotes 3.78x with no marker at all. **This is the passage to point at when explaining why a caveat that bears on a headline number belongs beside that number.**

### Chapter 2, Finding 5 — task mix diversifies with adoption

> When analyzing O\*NET tasks aggregated at the highest level (in terms of the Standard Occupation Classification occupation groups they belong to), we notice strong variation across countries. While the overall pattern is noisy–especially for countries with fewer observations–Figure 2.7 suggests that as we progress from lower to higher per capita Claude adoption, usage shifts away from tasks in the Computer and Mathematical occupation group (e.g., programming) to more diverse tasks in areas such as education, office and administrative uses, and arts. We also see increased usage in the life, physical and social sciences.

**Annotation.** The noise warning is inside the same sentence as the claim, with its source named ("especially for countries with fewer observations"), and the claim's subject is the *figure*, not the authors: "Figure 2.7 suggests that". Attributing an inference to an exhibit rather than to yourself is a hedge with a specific function — it tells the reader the pattern is visual rather than tested. The report goes one step further and puts the same warning in the figure's own title (see `## Figure captions`), so the qualifier cannot be separated from the exhibit if the exhibit is lifted.

### Chapter 2, Finding 6 — collaboration mode by adoption tier

> We find that even when controlling for the task mix of a country, users from different countries show notably different preferences for autonomous delegation versus collaborative interaction. As Claude usage per capita increases, countries shift from automation-focused to augmentation-focused usage. This is somewhat counter-intuitive, since we are controlling for the more diverse task composition across different countries. We speculate that cultural and economic factors might affect the automation share, or perhaps that early adopters in each country tend to use AI in a more automotive way—but more research is needed here.

**Annotation.** The control is named before the result, twice. The result is then flagged as surprising *to the authors* ("This is somewhat counter-intuitive, since…"), with the reason given — an unusually candid move, because it tells the reader the finding is not what the design was set up to confirm. Then the verb changes gear: **"We speculate that"**. The report has a graded vocabulary for confidence and this is its bottom rung: "we find" → "suggests" → "may reflect" → "we suspect" → "we speculate" → "more research is needed here". Two candidate mechanisms are floated and neither is defended. Footnote 9 carries the full partial-regression procedure in six sentences, so the "controlling for" claim is checkable.

### Chapter 3, Finding 1 — API usage is more specialised

> Overall, software development dominates the landscape. Among the top 15 use clusters—representing about half of all API traffic—the majority relate to coding and development tasks. Debugging web applications and resolving technical issues each account for roughly 6% of usage, while building professional business software represents another significant chunk. Of note, around 5% of API traffic focuses specifically on developing and evaluating AI systems themselves (Figure 3.2).

> But not all API usage is for coding. API customers also deploy Claude to create marketing materials (4.7%) and to process business & recruitment data (1.9%). These two categories reveal that AI is being deployed not just for direct production of goods and services but also for talent acquisition and external communications.

> The O\*NET classification makes these patterns even clearer. Little less than half of all API traffic maps to computer and mathematical tasks—more than 8 percentage points higher than Claude.ai usage. Office and administrative tasks come second at roughly 10% of transcripts, reflecting their suitability for automation.

> On the other hand, several interaction-heavy tasks prominent on Claude.ai have a much smaller share in API usage: education and library tasks drop from 12.3% to 3.6%, while arts and entertainment fall from 8.2% to 5.2%.

> In many cases however, occupational categories are reasonably close between Claude.ai and API data, suggesting that underlying model capabilities, rather than the specific product surface, drives adoption in many instances.

**Annotation.** Precision is deliberately uneven and the unevenness is signposted: "roughly 6%", "around 5%", "Little less than half", "roughly 10%" for quantities the authors are reading off a distribution, but "4.7%", "1.9%", "12.3% to 3.6%", "8.2% to 5.2%" for quantities they are comparing across samples. Where a number carries a comparison it gets a decimal; where it carries an impression it gets a hedge. "But not all API usage is for coding" is a paragraph-opening self-correction that stops the coding story from swallowing the chapter, and the two small categories it rescues are then given an economic reading ("not just for direct production of goods and services but also for talent acquisition and external communications") that is larger than their 6.6% combined share would suggest — the report is explicit that it is interpreting, not measuring, by switching to "reveal that AI is being deployed".

The last paragraph is the finding's own counterweight, and it is the finding the section title does not advertise: the two surfaces are *mostly similar*, which supports a capabilities explanation over a product explanation. Reporting the null-ish result in the same section as the differences is what makes the differences interpretable.

### Chapter 3, Finding 2 — concentration is the same on both surfaces

> Despite serving different users with different interfaces, API and Claude.ai usage follows remarkably similar power law distributions across tasks. Among Claude.ai conversations, the bottom 80% of task categories account for only 12.7% of usage; for API customers it's somewhat more concentrated at 10.5% (Figure 3.4). These extreme concentrations (Gini coefficients[5] of 0.84 and 0.86) reveal massive variation in AI-task fit—the best-matched tasks see orders of magnitude more usage than poorly-matched ones.

> The similarity across platforms is particularly striking given their different user bases and use cases. Both converge on comparable concentration levels, suggesting a common matching process between AI capabilities and associated economic tasks.

> Tasks like code generation dominate because they hit a sweet spot where model capabilities excel, deployment barriers are minimal, and employees can adopt the new technology quickly. The long tail of rarely used tasks could reflect several factors.[6] For example, some tasks are simply less common—debugging software happens far more often than negotiating circus contracts. The extreme concentration also suggests the potential role of O-Ring[7] forces: if a task needs a level of reasoning Claude can't handle, internal data the firm can't access, or regulatory approval that doesn't exist, any single barrier could prevent adoption.

**Annotation.** A similarity reported as a finding, which is harder to write than a difference and is done here by naming what would have predicted a difference ("Despite serving different users with different interfaces", "given their different user bases and use cases"). Two concentration statistics are given for each sample — the bottom-80% share and the Gini — so the claim rests on more than one measure; the Gini is glossed in footnote 5 for a reader who does not know it. "reveal massive variation in AI-task fit" is the one immodest verb in the passage, and it is immediately cashed out in a comparative clause rather than left as an adjective.

The mechanism paragraph is the best writing in Chapter 3. Theory is named (O-Ring, footnoted to Kremer 1993) and then *translated into the report's own subject matter in the same sentence*: "if a task needs a level of reasoning Claude can't handle, internal data the firm can't access, or regulatory approval that doesn't exist, any single barrier could prevent adoption." And "debugging software happens far more often than negotiating circus contracts" is the device that makes the long tail memorable — a concrete, slightly absurd pair that does what no dispersion statistic can. Note that the vivid comparison is in service of the *boring* explanation (base rates), not the interesting one; the report uses its best sentence to defuse an over-reading.

### Chapter 3, Finding 3 — the automation gap between surfaces

> The clearest distinction between API and Claude.ai usage lies in *how* humans and AI divide the work. When businesses embed Claude into their applications, they largely delegate individual tasks rather than collaborate iteratively with models.

> In our data, 77% of API transcripts show automation patterns (especially full task delegation) versus just 12% for augmentation (e.g., collaborative refinement and learning). Based on a sample of conversations from Claude.ai, the split between automation and augmentation is nearly even. Looking across economic tasks, the degree of Claude automation through the API is even starker: 97% of tasks show automation-dominant patterns in API usage, compared to only 47% on Claude.ai (Figure 3.5).

> This makes intuitive sense. Programmatic API access naturally lends itself to automation: businesses provide context, Claude executes the task, and the output flows directly to end users or downstream systems.

> This pattern echoes how economically consequential technologies become transformative: becoming embedded in systems that let workers access productivity gains without needing specialized skills. While both augmented and automated approaches enhance human capabilities, system-level automation is likely to yield both larger productivity gains across the economy as well as more significant changes in the labor market: Fully automating some tasks, changing which tasks are important for various jobs, and even producing new forms of work altogether.

**Annotation.** "In our data" opens the sentence that carries the headline number, so the fence precedes the figure. The 77%/12% pair does not sum to 100 and the report does not explain the residual in the body — a referee's first question, and one the caption partly answers by noting that privacy-censored modes are set to 0%. The claim is then **tested at a second level**: shares of transcripts (77% versus roughly even) and shares of tasks that are automation-dominant (97% versus 47%), with "even starker" signalling that the second cut is the stronger version of the same claim. That is the *one claim at two levels* pattern, and it is why this finding is the most solid in the chapter.

"This makes intuitive sense" is a risky sentence — it invites the reader to stop asking — but it is followed immediately by the mechanism spelled out in a single clause chain, so the intuition is discharged rather than asserted. The final paragraph escalates from measurement to economic significance and does so with the report's standard machinery: an analogy to past technologies, a concession that both modes are valuable ("While both augmented and automated approaches enhance human capabilities"), a hedge on the consequence ("is likely to yield"), and a three-item list of what "more significant changes" means in labour-market terms. Note that automation is not called bad anywhere; the report consistently describes it as larger in both directions.

### Chapter 3, Finding 4 — context as the binding constraint

> There is considerable variation across tasks in how long Claude's API outputs are. For example, tasks at the 90th percentile of output length are more than 4x longer than tasks at the 10th percentile.

> What stands out from Claude's assessment of tasks is that longer output tasks tend to represent increasingly complex uses. Of course, output length does not capture all dimensions of task complexity, but it appears to be a sensible, easily measured proxy.

> Because API customers are priced on the margin for both input tokens and output tokens, they have an incentive to optimize model prompting to minimize both input and output tokens when using Claude. In turn, any systematic relationship between input length and output produced by Claude partly captures the underlying contextual constraints in deploying Claude for sophisticated tasks. Stated differently, API customers are incentivized to only provide Claude with just enough context to accomplish their objective and no more. And so we learn about contextual requirements for tasks with varying output length.

> Looking across tasks, we see a very stable relationship between how much context API customers provide to Claude and how much Claude actually produces. Across economic tasks, each 1% increase in input length is associated with a less-than-proportional 0.38% increase in output length (Figure 3.7). This elasticity of 0.38 suggests that there are strong diminishing marginal returns in translating longer contextual inputs into longer outputs for these economically useful tasks.[10]

> The upshot is that deploying AI for complex tasks might be constrained more by access to information than on underlying model capabilities. Companies that can't effectively gather and organize contextual data may struggle with sophisticated AI deployment, creating a potential bottleneck for broader enterprise adoption—particularly for occupations and in industries where tacit, diffuse knowledge is crucial to business operations.

**Annotation.** The proxy is defended and doubted in one sentence: "Of course, output length does not capture all dimensions of task complexity, but it appears to be a sensible, easily measured proxy." Two hedges and a concession, then a defence on the ground of measurability rather than validity — an honest reason to use a proxy, and a reusable formula.

The paragraph beginning "Because API customers are priced on the margin" is the only place in the report where an **identification argument** is made in prose, and it is made without notation: customers pay per token, so they minimise tokens, so the input they supply is the minimum the task needs, so the input–output relationship is informative about contextual requirements rather than about prompting habits. Four steps, each a clause, with "Stated differently" restating the whole chain in one sentence for a reader who lost it. Any post of ours that leans on a behavioural assumption should be written this way.

The elasticity is stated with its interpretation attached ("a less-than-proportional 0.38% increase"), then restated as a named quantity with its economic meaning ("This elasticity of 0.38 suggests that there are strong diminishing marginal returns"), then footnoted with an alternative explanation the authors did not test (footnote 10: long-context performance degradation, citing Liu et al.). Naming a rival explanation in a footnote and leaving it unresolved is the report's way of handling a threat it cannot close.

"The upshot is that…" is the sentence that would be quoted in a policy brief, and it is hedged twice ("might be constrained more", "creating a potential bottleneck") and scoped to a population ("particularly for occupations and in industries where tacit, diffuse knowledge is crucial").

### Chapter 3, Finding 5 — cost barely matters

> API customers pay per token, creating variation in the cost of deploying Claude for different tasks. More sophisticated tasks will tend to cost more, given their higher input and output token counts. This variation helps us explore whether cost is a major factor in determining which tasks businesses choose to automate with Claude.

> The data suggests it is not, at least relatively speaking.[11] For example, tasks typical of computer and mathematical occupations cost more than 50% more than sales-related tasks, yet dominate usage.[12] Overall, we find a positive correlation between cost and usage: higher-cost tasks tend to have higher usage rates (Figure 3.8).

> The positive correlation between cost and usage suggests that cost plays an immaterial role in shaping patterns of enterprise AI deployment. Instead, businesses likely prioritize use in domains where model capabilities are strong and where Claude-powered automation generates enough economic value in excess of the API cost.

> While this positive correlation holds overall, we next ask whether demand for Claude capabilities is lower among otherwise similar but costlier tasks. With the important caveat that this should be viewed as a preliminary exploration, this is what we find.

> Controlling for task characteristics, we find that each 1% cost increase is associated with a 0.29% reduction in usage frequency in our sample of API transcripts (Figure 3.9).[13] While consistent with standard economic theory that higher prices lead to lower demand, the implied increase in usage to a drop in cost is limited. According to this estimate, a 10% cost reduction for a particular task would only increase usage by around 3%.

> Other factors, beyond the cost of using Claude for particular tasks, appear to matter more for patterns of use.

**Annotation.** The question is posed before it is answered, in the form of the design that will answer it ("This variation helps us explore whether…"). The answer arrives as four words plus a scope restriction: "The data suggests it is not, at least relatively speaking", with footnote 11 defining precisely what "relatively speaking" excludes — "This is different from studying whether overall Claude usage is sensitive to external competitive pricing pressures." That footnote is a boundary marker on the claim, not a caveat about noise, and it is the kind a referee reaches for.

Then the report does something we should imitate exactly: it presents the raw correlation, draws the conclusion, and then **runs the conditional version that could overturn it** — and reports a coefficient of the opposite sign. The unconditional relationship is positive; the conditional one is negative. Both are reported, in that order, with the sign flip explained by what the controls absorb, and the caveat placed as a standalone sentence *before* the result rather than after: "With the important caveat that this should be viewed as a preliminary exploration, this is what we find." The elasticity is then translated into the units a decision-maker uses ("a 10% cost reduction for a particular task would only increase usage by around 3%"), which is how a small coefficient is made meaningful without inflating it. Footnote 13 lists the controls.

### The report's hedge vocabulary, graded

Collected from the passages above, in descending confidence: *we find* · *we document* · *we see* · *reveals* · *indicating that* · *suggests* · *appears to* · *tend to* · *may / might* · *could* · *likely reflects* · *potentially driven by* · *we suspect* · *we speculate* · *more research is needed here*. The report almost never uses two rungs for one claim, and it never uses *shows* or *proves*. The rung chosen is legible evidence of how much work the underlying analysis did.

### Claude versus AI across the whole report

- **Title:** "…Uneven geographic and enterprise **AI** adoption." **Chapter titles:** "**Claude.ai** Usage Over Time", "**Claude** usage across the United States and the globe", "API Enterprise Deployment of **Claude**."
- **Introduction:** almost entirely AI. Every measured quantity in it that comes from Anthropic's own data says Claude.
- **Inside a single bullet:** "As with previous technologies, we see that **AI** usage is geographically concentrated. Singapore and Canada are among the highest countries in terms of usage per capita at 4.6x and 2.9x what would be expected based on their population, respectively. In contrast, emerging economies, including Indonesia at 0.36x, India at 0.27x and Nigeria at 0.2x, use **Claude** less." The general claim takes AI; the numbers take Claude.
- **The construct:** *Anthropic **AI** Usage Index*, defined as a share of ***Claude*** usage.
- **Captions:** every one says Claude, except Figure 3.1, which plots Census data and therefore says AI.
- **Concluding remarks:** "early **AI** adoption is strikingly uneven" (phenomenon) beside "Early business adoption of **Claude**" (measurement).

The rule holds throughout and is worth stating as the corpus's finding: **the question, the title, the stakes and the policy sentence say AI; the sample, the index, the numbers and the captions say Claude.**

## Comparisons

Every place a comparison carries a finding.

### To the history of technology, with numbers

> Historically, new technologies took decades to reach widespread adoption. Electricity took over 30 years to reach farm households after urban electrification. The first mass-market personal computer reached early adopters in 1981, but did not reach the majority of homes in the US for another 20 years. Even the rapidly-adopted internet took around five years to hit adoption rates that AI reached in just two years.[2]

**Annotation.** Three technologies, three time-to-diffusion facts, escalating toward the closest analogue, and only the last one is put in a ratio with AI ("five years to hit adoption rates that AI reached in just two years"). The comparison is the argument: without it, "40% of employees" is a statistic; with it, it is an anomaly that needs explaining. Sourced in a single footnote to two papers, one for the benchmark method and one for the electrification history — the footnote says which paper does which job.

### To the history of technology, for the stakes

> The uneven geography of early AI adoption raises important questions about economic convergence. Transformative technologies of the late 19th century and the early 20th centuries—widespread electrification, the internal combustion engine, indoor plumbing—not only ushered in the era of modern economic growth but accompanied a large divergence in living standards around the world.[4]

> If the productivity gains are larger for high-adoption economies, current usage patterns suggest that the benefits of AI may concentrate in already-rich regions—possibly increasing global economic inequality and reversing growth convergence seen in recent decades.[5]

**Annotation.** The same comparison class as the opening, redeployed for consequence rather than puzzle. The historical claim is factual and footnoted (Gordon; Pritchett's *Divergence, Big Time*); the extension to AI is conditional and triple-hedged — "If the productivity gains are larger…", "may concentrate", "possibly increasing". The conditional's antecedent is something the report explicitly did **not** measure (productivity gains), which is why the sentence can carry so much weight without overclaiming. This is the structure of a why-it-matters paragraph: historical precedent stated as fact, application to the present stated as an if.

### Across waves of the same series

> With data spanning from December 2024 and January 2025 (from our first report, 'V1') to February and March 2025 ('V2') to our newest insights from August 2025 ('V3'), we can track how AI usage has shifted over the past eight months as capabilities and product features have improved, new kinds of users have adopted the technology, and uses have become more sophisticated.

> Educational Instruction and Library tasks rose from 9% in V1 to 12% in V3.

> The share of *directive* conversations sampled from Claude.ai conversations jumped from 27% in V1 in late 2024 to 39% in V3.

> This is the first report where automation usage exceeds augmentation usage.

**Annotation.** The waves are named once, with their calendar dates, and thereafter used as bare labels — a notation the series can reuse. The elapsed interval is restated whenever a magnitude is claimed ("in just eight months", "over the past eight months"), so no change is quoted without its denominator. And "This is the first report where…" is a comparison to the series' own history rather than to a benchmark: the finding is a crossing, and a crossing only exists relative to earlier waves. A first-wave post cannot write this sentence; that is the compounding value of a series, and the reason each wave's report invests in keeping the definitions stable.

### Against its own instrument

> [4] We note that V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison. To address this, we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (though to a lower absolute level of 45% automation versus 49% with Sonnet 4).

**Annotation.** The comparison that protects the series' headline finding: same data, two classifiers, both directions agree, levels differ by 4pp and the difference is stated. A report that compares waves must compare instruments too, and the honest form gives the discrepancy rather than declaring robustness.

### Countries against countries

> Israel leads global per capita Claude usage with an Anthropic AI Usage Index of 7 … Singapore follows at 4.57, while Australia (4.10), New Zealand (4.05) and South Korea (3.73) round out the top five countries in terms of per capita Claude usage.

> The United States (3.62) ranks among leading countries in terms of per capita adoption, with Canada (2.91) and the United Kingdom (2.67) having elevated but more moderate rates of adoption as compared to their population. Other major economies show lower adoption, including France at 1.94, Japan at 1.86, and Germany at 1.84.

> This includes Bolivia (0.48), Indonesia (0.36), India (0.27), and Nigeria (0.2).

**Annotation.** Compared to what? To 1.0 — the whole point of building an index whose null value is parity. The comparison is embedded in the measure, so the prose can list values without repeating the benchmark. The ordering is rank-descending across three paragraphs with different rhetorical jobs (the surprise leaders; the economies the reader expects to lead and does not; the economies below parity), and the only adjectives are relational ("elevated but more moderate", "lower", "minimal").

### Countries against US states

> We document a similar, but weaker correlation than at the global level between Claude adoption and income per capita across US states. Income differences explain less than half the variation in cross-state adoption rates. Despite this weaker correlation, we find that Claude adoption rises faster with income: Each 1% increase in state GDP per capita is associated with a 1.8% increase in the AI Usage Index.

> In this section we explore patterns of Claude usage across states within the US, giving us further insight into how local economic conditions shape usage patterns. As we discuss above, cross-state differences in the Anthropic AI Usage Index account for less than half of the variation in income differences across US states. This suggests that other regional differences—including the compatibility of Claude capabilities with the occupational composition of the local workforce—play a larger role in determining why usage is more concentrated in some states than others.

**Annotation.** The same relationship measured at two geographic levels, and the comparison of the two comparisons is the finding: income explains less between states than between countries, but the slope is steeper (1.8 versus 0.7). Reporting fit and slope separately — and noting that they point different ways — is what turns two regressions into one claim. The second passage then uses the weaker fit as a *licence to look elsewhere*, which is how a partial explanation is converted into the next section's motivation rather than presented as a disappointment.

### Claude.ai against the 1P API

> However, 1P API usage is higher for coding and office/admin tasks, while Claude.ai usage is higher for educational and writing tasks.

> Little less than half of all API traffic maps to computer and mathematical tasks—more than 8 percentage points higher than Claude.ai usage.

> education and library tasks drop from 12.3% to 3.6%, while arts and entertainment fall from 8.2% to 5.2%.

> Among Claude.ai conversations, the bottom 80% of task categories account for only 12.7% of usage; for API customers it's somewhat more concentrated at 10.5% … These extreme concentrations (Gini coefficients of 0.84 and 0.86)…

> In our data, 77% of API transcripts show automation patterns (especially full task delegation) versus just 12% for augmentation … Based on a sample of conversations from Claude.ai, the split between automation and augmentation is nearly even. Looking across economic tasks, the degree of Claude automation through the API is even starker: 97% of tasks show automation-dominant patterns in API usage, compared to only 47% on Claude.ai.

> Despite serving different users with different interfaces, API and Claude.ai usage follows remarkably similar power law distributions across tasks.

> In many cases however, occupational categories are reasonably close between Claude.ai and API data, suggesting that underlying model capabilities, rather than the specific product surface, drives adoption in many instances.

**Annotation.** The chapter's spine. One pair of samples, compared on five dimensions — category mix, category shares, concentration, collaboration mode, and cost sensitivity — with the same phrasing template each time: the two values, the direction word, and where relevant the gap in points. Note the discipline about what the comparison licenses: differences in mix support "businesses use Claude in similar but more specialized ways"; similarity in concentration supports "a common matching process between AI capabilities and associated economic tasks"; and similarity in categories supports capabilities over product surface as the driver. Three different conclusions from one comparison, each tied to the specific dimension that supports it. "Drops from 12.3% to 3.6%" is worth flagging as a small liberty: the two numbers are different samples, not a time series, and "drops" reads temporally.

### Against official statistics

> According to the Census Bureau's Business Trends and Outlook Survey, AI adoption among US firms has more than doubled in the past two years, rising from 3.7% in fall 2023 to 9.7% in early August 2025 (Figure 3.1).[3] Despite this rapid rate of growth, the vast majority of firms in the US do not report using AI in their production processes.

> But these aggregate numbers mask large variation across sectors. For example, in early August 2025, one in four businesses in the Information sector reported using AI, which is roughly ten times the rate for Accommodation and Food Services.[4]

> The picture from this public data is clear: enterprise use of AI is growing rapidly, but we are still in the early stages of AI adoption. Usage remains unevenly distributed across the economy, with the sectors most able to quickly adopt and benefit from this technology doing so.

> As we will see below, our 1P API data yields a complementary conclusion: early enterprise use of Claude is likewise unevenly distributed across the economy and primarily deployed for tasks typical of Information sector occupations.

**Annotation.** A whole section ("Setting the stage: AI adoption patterns in public data") given over to somebody else's numbers **before** any of Anthropic's, with the explicit purpose of establishing where the proprietary data sits: "it's worth grounding ourselves in the broader landscape". The Census series is described, its exact survey question is quoted in full in the caption and again in footnote 4, and a paper comparing BTOS to other adoption measures is cited. The rhetorical shape is *external benchmark → what it shows → what our data adds*, and the word "complementary" does the joining work: the claim is not that the API data is better, only that it agrees and goes further. A sector ratio ("roughly ten times the rate for Accommodation and Food Services") carries the dispersion claim that the two aggregate numbers cannot.

### Against its own other measure

> [3] Note that this is a different measure of adoption than in the introduction to this report. Reported adoption by consumers and employees of AI reached 40% in 2024 whereas when measured at the firm-level, nine out of ten businesses in the US report not using AI.

**Annotation.** The report catches its own apparent contradiction — 40% adoption on page 2, 9.7% adoption on page 31 — and reconciles it by naming the unit of observation in each. Reconciling two of your own numbers in a footnote, unprompted, is the single most credibility-earning move in the document, and it costs two sentences.

### To economic theory

> Institutional inertia, alongside fixed costs of adoption, suggests that early examples of enterprise use of AI is likely to be concentrated among specialized tasks where deployment is easy, capabilities are robust, and the economic benefits from adoption are high.

> [1] In the presence of fixed costs of adjustment, the question businesses face is not necessarily if they will adopt AI, but when. See Hall and Kahn 2003, *Adoption of New Technology*: "The most important thing to observe about this kind of decision is that at any point in time the choice being made is not a choice between adopting and not adopting but a choice between adopting now or deferring the decision until later."

> The extreme concentration also suggests the potential role of O-Ring[7] forces: if a task needs a level of reasoning Claude can't handle, internal data the firm can't access, or regulatory approval that doesn't exist, any single barrier could prevent adoption.

> Zipf's law, in which the coefficient of the best-fit-line is equal to -1, occurs with some regularity in various economic settings.

> While consistent with standard economic theory that higher prices lead to lower demand, the implied increase in usage to a drop in cost is limited.

**Annotation.** Theory enters three ways in this report and each has a distinct grammar. (i) **As a prior stated before the data** — "Institutional inertia… suggests that early examples of enterprise use of AI is likely to be concentrated", followed on the next page by "Indeed, we see evidence along these lines". Predict, then confirm, and say which you are doing. (ii) **As a named mechanism translated into the subject matter** — O-Ring, with its three barriers rewritten as reasoning, internal data and regulatory approval. (iii) **As a benchmark a coefficient is measured against** — Zipf's −1 for the rank–share slope, and textbook demand for the sign of the cost elasticity. In all three the citation is a footnote and the *use* is in the body, so no sentence requires the reader to know the reference to follow the argument.

### To the same evidence read two opposite ways

> [1] Brynjolfsson, Chandar, and Chen 2025, *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence* documents clear evidence that entry-level workers with high AI exposure have had relatively worse employment prospects since late 2022. Setting aside questions of causality, the straightforward interpretation is that this is due to AI substituting for work previously done by early-career workers. An alternative interpretation is presented by Gans 2025, *If AI and workers were strong complements, what would we see?*: That relatively faster employment growth for experienced workers reflects AI making such workers more productive and thus in high demand. Whether AI compliments or substitutes work is perhaps the most important question that we hope our data will help answer.

**Annotation.** A single footnote that stages a live disagreement in the literature, gives both readings of one empirical pattern, declines to adjudicate ("Setting aside questions of causality"), and then names the disagreement as the reason the report's data exists. This is how to cite a contested literature without pretending it is settled — and the last sentence is the report's own statement of purpose, hidden in a footnote on the final page.

### Small vivid comparisons

> some tasks are simply less common—debugging software happens far more often than negotiating circus contracts.

> tasks at the 90th percentile of output length are more than 4x longer than tasks at the 10th percentile.

> For example, tasks typical of computer and mathematical occupations cost more than 50% more than sales-related tasks, yet dominate usage.

> An index value of 1.5, for example, means that the API transcripts associated with that task are 50% longer than the average across tasks.

> For example, help with job applications is 1.84x as common in DC as in the US overall.

> coding tasks are over half of all usage in India versus roughly a third of all usage globally.

**Annotation.** Six devices, one purpose: convert an abstract quantity into a comparison a reader can hold. The last one is the template for a geographic claim — a local share against the global share, in the same sentence, with both rounded to the same coarseness ("over half" / "roughly a third") so neither looks more precisely known than the other.

## Figure captions

Twenty figures and three tables. PDF form throughout: **bold "Figure N.N: sentence-case declarative title"** with **no terminal period**, run on directly into a plain-roman gloss of one to five sentences. No "Source:" line anywhere — provenance, where it exists, is a clause inside the gloss. The only caption that uses the word "Note" is Figure 3.1, the only one plotting somebody else's data.

Alongside the captions, each exhibit carries an **in-image chart title** in small caps-ish coral type (e.g. "Top 30 countries by share of global Claude usage"). These are part of the graphic, not the caption; they are quoted below marked as such, because the division of labour between the two is itself the pattern: the chart title says *what this is*, the caption says *what it is made of*.

### Chapter 1

> **Figure 1.1: Claude.ai usage over time** Each panel shows the share of sampled conversations on Claude.ai associated with tasks from each SOC major group. We see notable increases in usage for scientific and educational tasks. SOC major groups ranked by usage in our first report.

In-image chart title: "Usage share trends across economic index reports (V1 to V3)". Axes labelled "Percentage"; x-ticks "Jan 2025 / Mar 2025 / Aug 2025".

**Annotation.** Four elements in three sentences: unit of observation and measure ("the share of sampled conversations on Claude.ai associated with tasks from each SOC major group"), the panel logic ("Each panel shows…"), **a sentence of interpretation inside the caption** ("We see notable increases in usage for scientific and educational tasks"), and the panel ordering rule ("SOC major groups ranked by usage in our first report"). That last clause matters more than it looks: the panels are not sorted by current size, and saying so stops a reader from inferring a ranking that is a year old. Note that the caption names the waves by calendar date only in the chart's x-axis, while the body calls them V1/V3 — the exhibit is readable without the notation.

> **Figure 1.2: Collaboration mode frequencies across Anthropic Economic Index Reports** The left panel calculates the share of conversations exhibiting either automation or augmentation forms of use. The right panel breaks this out by collaboration mode. Claude tends to be used in more automated ways over time, driven primarily by an increase in directive use.

In-image chart title: "Automation vs. augmentation evolution"; panel titles "Automation vs. augmentation trends" and "Individual interaction types".

**Annotation.** Two-panel template: one sentence per panel naming what it aggregates, then the takeaway sentence. "breaks this out by" is the report's standard phrase for a disaggregation panel. The takeaway carries a hedge ("tends to be used") and an attribution ("driven primarily by an increase in directive use") — the caption states both the pattern and its main driver, so the figure can be lifted without the body text.

### Chapter 2

> **Figure 2.1: Leading countries in terms of global Claude.ai usage share** The data includes Claude.ai Free and Pro conversations.

In-image chart title: "Top 30 countries by share of global Claude usage". Axis: "Share of global usage (%)".

**Annotation.** The shortest caption in the report: title plus one clause of sample definition. Everything else is in the chart title (that it is a top-30 cut) and the axis (the units). "Free and Pro" is the coverage boundary and it appears in this form in four separate captions — the same eight words, repeated verbatim rather than paraphrased, so the boundary reads as a fixed term of art.

> **Figure 2.2: Small, technologically advanced countries are leading in Claude adoption per capita** The figure shows the top 20 countries based on the Anthropic AI Usage Index. We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample. The underlying data includes Claude.ai Free and Pro usage.

In-image chart title: "Top 20 countries by Anthropic AI Usage Index". Axis: "Anthropic AI Usage Index (usage % / working-age population %)", with a dashed reference line at 1.

**Annotation.** The title is a **finding**, not a description — "Small, technologically advanced countries are leading" — which is the report's dominant caption style from here on. Then the sample rule with its **reason attached**: "at least 200 observations… because of the uncertainty of the measure for low-usage countries in our random sample". Giving the reason converts an arbitrary threshold into a statement about noise, and this exact sentence recurs, word for word, in Figures 2.4, 2.7 and 2.11 (and in a 100-observation variant in 2.5). Repeating a caveat verbatim across every exhibit it applies to is a deliberate choice: the reader learns the sentence and stops needing to re-read it, and no exhibit travels without it. The axis label carries the formula, so the index is self-documenting on the page.

> **Figure 2.3: Claude diffusion varies across countries, with countries in North America, Europe and Oceania leading in Claude adoption per working-age capita** The different tiers reflect a country's position within the global distribution of the Anthropic AI Usage Index as defined in this chapter.[5,6]

In-image chart title: "Anthropic AI Usage Index tiers by country". Legend: "Leading (top 25%) / Upper middle (50-75%) / Lower middle (25-50%) / Emerging (bottom 25%) / Minimal / Claude not available / No data".

**Annotation.** A choropleth caption with one job: say that the colours are *relative positions*, not levels ("a country's position within the global distribution… as defined in this chapter"). The two footnote markers hanging off a map caption carry the map's politics — Natural Earth's disputed-territory convention, the regions where Anthropic does not operate, and why the AUI cannot be computed for some territories. A map of a commercial product's usage needs that paragraph, and putting it in footnotes attached to the caption rather than in the body is the right call.

> **Table 2.1: Anthropic Economic Index tiers with examples, number of countries, and AUI range for each tier.**

> **Table 2.2: Claude per capita usage tiers with examples, number of states, and AUI range for each tier.**

**Annotation.** Table captions are the exception to the no-terminal-period rule and carry no gloss at all: a single noun phrase listing the columns in order. The reader is expected to read the table. Table 2.2 is the exhibit the web page drops.

> **Figure 2.4: Claude usage per capita is positively correlated with income per capita across countries** We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample. Axes are on a log scale, highlighting a power law distribution. Each country is represented by its 3-letter ISO code.

In-image chart title: "Income and Anthropic AI Usage Index by country". Axes: "ln(GDP per working-age capita in USD)" and "ln(Anthropic AI Usage Index)".

**Annotation.** Caption title states the relationship and its sign; gloss states the sample rule, the transformation ("Axes are on a log scale") with its interpretive consequence ("highlighting a power law distribution"), and the marker convention ("Each country is represented by its 3-letter ISO code"). No coefficient in the caption — that is in the body and in the chart's own annotation box. The template for a bivariate scatter: *relationship and sign · sample rule · transformation · marker key*.

> **Figure 2.5: Leading US states in terms of Claude adoption per working-age capita include the District of Columbia, Utah, California, New York and Virginia** The figure shows the top 20 US states based on the Anthropic AI Usage Index. We only include states with at least 100 observations in our sample for this figure because of the uncertainty of the measure for low-usage states in our random sample. The underlying data includes Claude.ai Free and Pro usage.

**Annotation.** The country template with the threshold changed from 200 to 100 and every other word held constant. Consistency across exhibits is itself the style: a reader comparing Figures 2.2 and 2.5 can see immediately that only the floor differs. The caption names five states in its title, which is long but means the exhibit's headline survives being read out loud.

> **Figure 2.6: Claude usage varies across US states, with high per-capita usage in the West Coast, but also higher usage in Nevada, Utah, Colorado, Missouri, and Virginia** The different tiers reflect a US state's position within the US distribution of the Anthropic AI Usage Index as defined in this chapter.

**Annotation.** "within the **US** distribution" — one word marks that the state tiers are computed against a different reference population than the country tiers, which is the only thing that could mislead a reader flipping between the two maps.

> **Figure 2.7: As we move from lower to higher adoption countries, Claude usage appears to shift away from programming-dominant tasks to a more diverse mix of tasks, though the overall pattern is noisy** This figure shows the relationship between the Anthropic AI Usage Index and the most frequent Standard Occupation Classification (SOC) occupation groups. Each panel shows a different SOC group. SOC share is based on how many O\*NET tasks in a given geography fall into a given SOC group. The color indicates which AUI tier a country falls into. The bubble size indicates the usage count for each country. We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample. The regression weights every country equally.

In-image chart title: "Occupation group shares vs Anthropic AI Usage Index". Panels titled by SOC group; legends for AUI tier and for "Claude usage count".

**Annotation.** The most instructive caption in the corpus so far, for one reason: **the hedge is in the title.** "…though the overall pattern is noisy" is inside the bold sentence, not the gloss, so an exhibit lifted into a slide deck carries its own noise warning in the headline. The gloss then does five separate jobs in five sentences — what is related to what, the panel logic, how the share is constructed, what colour encodes, what size encodes — and closes on the estimation detail that determines what the fitted line means ("The regression weights every country equally"). Three encodings (position, colour, area) each get exactly one sentence. This is the caption to imitate for any multi-encoding scatter.

> **Figure 2.8: Overrepresented request clusters for the United States, Brazil, Vietnam and India** A request is overrepresented in a country when the share of conversations containing that request is higher for that country than globally. For this figure, we focus on request clusters at the middle level of granularity, i.e. more aggregated than the lowest level request clusters, but less aggregated than the highest level request clusters. Only includes requests with at least 1% frequency globally and for that country.

In-image chart title: "Top overrepresented requests for the United States, Brazil, Vietnam and India".

**Annotation.** The caption **defines its own headline word**: "A request is overrepresented in a country when the share of conversations containing that request is higher for that country than globally." Then the granularity level, explained by its position in the hierarchy rather than by a level number, and the inclusion floor stated on both sides ("at least 1% frequency globally **and** for that country"). A ratio exhibit needs all three — definition, granularity, floor — and this caption is the template. It recurs almost verbatim in 2.9 and 2.10 with "globally" swapped for "in the US as a whole".

> **Figure 2.9: Overrepresented request categories for California, Texas, Florida and South Carolina** A request is overrepresented in a state when the share of conversations containing that request is higher for that state than in the US as a whole. For this figure, we focus on request clusters at the middle level of granularity, i.e. more aggregated than the lowest level request clusters, but less aggregated than the highest level request clusters. Only includes requests with at least 1% frequency in the United States and for that state.

> **Figure 2.10: Washington, DC has the highest Claude usage per capita, with disproportionate tasks and requests focusing on document editing, information provision and job applications** O\*NET tasks refer to tasks in the O\*NET taxonomy. Requests are based on the bottom-up request categories that describe what requests users make of Claude. A task or request is overrepresented in a state when the share of conversations containing that task or request is higher for that state than in the US as a whole. For this figure, we focus on request clusters at the middle level of granularity. Only includes requests with at least 1% frequency in the United States and for that state.

**Annotation.** 2.10 puts two taxonomies side by side and therefore opens by distinguishing them in two sentences before defining overrepresentation — the caption's first job is to stop the reader treating the left and right panels as the same kind of object. The "middle level of granularity" clause is shortened here because it was spelled out twice already; the report lets a definition wear down across repetitions rather than restating it at full length forever.

> **Figure 2.11: Countries with higher Anthropic AI Usage Index tend to use Claude in a more collaborative manner (augmentation), rather than have it operate independently (automation)** This figure shows the relationship between the Anthropic AI Usage Index and the automation share in a given country. We plot the relationship after accounting for a geography's task mix, thus we show the regression residuals. We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample. Each country is represented by its 3-letter ISO code.

In-image chart title: "Relationship between Anthropic AI Usage Index and automation". Axes: "Anthropic AI Usage Index residuals (per capita usage not explained by task mix)" and "Automation % residuals (automation not explained by task mix)".

**Annotation.** A residual plot, and the caption says so in plain words — "We plot the relationship after accounting for a geography's task mix, thus we show the regression residuals" — while the axis labels gloss what a residual *is* in this context ("per capita usage not explained by task mix"). Between them, a reader who does not know the term can still read the axes correctly. The title glosses both technical poles in parentheses ("(augmentation)", "(automation)") with plain-English equivalents in the surrounding clause ("a more collaborative manner", "have it operate independently"), which is the terminology discipline the whole series depends on.

Uncaptioned: the **AUI equation image** (PDF p. 14), which sits inside the defining sentence and has no figure number. A formula presented as part of a sentence rather than as an exhibit.

### Chapter 3

> **Figure 3.1: AI adoption rates among US firms, Business Trends & Outlook Survey (Census)** Note: AI adoption rates are calculated as the share of firms responding "yes" to the question "In the last two weeks, did this business use Artificial Intelligence (AI) in producing goods or services? (Examples of AI: machine learning, natural language processing, virtual agents, voice recognition, etc.)".

In-image chart title: "Census reported AI adoption rates among US businesses from the Business Trends and Outlook Survey". Series legend: "AI Adoption Rate Among US Businesses" and "3-Period Moving Average".

**Annotation.** The only caption in the report with a source in the title and the only one using "Note:". The gloss is the **survey question quoted in full**, including its parenthetical examples — because the question *is* the definition of the measure, and any reader wanting to compare this series to another needs the exact wording. This is also the only caption that says AI rather than Claude, and the reason is visible in the title: the data is the Census Bureau's. The smoothing series is named in the chart legend, not the caption.

> **Figure 3.2: Bottom-Up taxonomy of Claude usage among sampled 1P API transcripts** Using privacy-preserving methods we classified 1P API transcripts into a bottom-up taxonomy reflective of underlying usage. This figure reports the leading use cases at the broadest level of this taxonomy.

In-image chart title: "Top use cases among 1P API transcripts by usage share (broad grouping, bottom-up classification)". Axis: "Percentage of total request count".

**Annotation.** Two sentences: how the categories were made, and which level of the hierarchy is shown. The unit ("total request count") is left to the axis. "Using privacy-preserving methods" is the report's fixed formula and it appears in the caption, the body and a hyperlink to the Clio post — an ethical constraint restated at every level of the document.

> **Figure 3.3: Leading Occupational Categories by Overall Usage: Claude.ai vs 1P API** After determining usage shares for tasks, we calculate the share of traffic from Claude.ai and 1P API customers assigned to top-level occupations in the O\*NET taxonomy. For example, this figure shows that 44% of API traffic in our sample was matched to a task characteristic of a Computer and Mathematical occupation.

In-image chart title: "Usage shares across top occupational categories: Claude.ai vs 1P API". Axis: "Percentage of usage". Series legend: "Claude.ai" and "1P API".

**Annotation.** The caption **reads one value off the chart as a worked example** — "this figure shows that 44% of API traffic in our sample was matched to a task characteristic of a Computer and Mathematical occupation" — which teaches the reader how to read every other bar. One number in a caption, chosen to demonstrate the grammar of the exhibit rather than to make a point. Note "was matched to a task characteristic of a … occupation": the caption preserves the inference chain (conversation → task → occupation) that the axis label compresses. The colon-and-comparison title form ("X: Claude.ai vs 1P API") recurs in 3.4 and 3.5.

> **Figure 3.4: Visualizing concentration of usage among a small number of tasks: Claude.ai versus 1P API** The left panel of this chart calculates Lorenz curves across O\*NET tasks for both our Claude.ai and 1P API samples. The highlighted points on the curves indicate how much overall usage the bottom 80% of tasks account for. The right panel plots task rank against task usage share for tasks representing at least 0.1% of overall usage in our samples. Zipf's law, in which the coefficient of the best-fit-line is equal to -1, occurs with some regularity in various economic settings.

In-image chart title: "Lorenz curves and power law analysis across tasks: 1P API vs Claude.ai"; panel titles "Lorenz curves" and "Task rank versus usage share". Axes: "Cumulative percentage of tasks" / "Cumulative percentage of usage"; "ln(Share of usage)" / "ln(Rank by usage)".

**Annotation.** Two panels, one sentence each, plus a sentence on the annotated points and a closing sentence that **supplies the benchmark for the second panel** ("Zipf's law, in which the coefficient of the best-fit-line is equal to -1, occurs with some regularity in various economic settings"). Without that last sentence the fitted slopes are uninterpretable; with it the reader knows what value would be unremarkable. Putting the null value in the caption is the same move as the AUI's dashed line at 1. The inclusion floor for the right panel (0.1%) is stated for that panel only.

> **Figure 3.5: Automation versus augmentation collaboration modes across O\*NET tasks: Claude.ai versus 1P API** This figure reports the share of Claude.ai conversations and 1P API transcripts that exhibit automation or augmentation patterns of usage for each O\*NET task. Automation and augmentation modes are defined in Chapter 1. When for privacy-preserving reasons we do not observe usage shares for a particular collaboration mode we give that category a value of 0% in this figure. Automation dominance is defined as a task having a greater observed share of automation usage. Likewise for augmentation dominance.

In-image chart title: "Automation and augmentation dominance across tasks: Claude.ai vs. 1P API"; panel titles "1P API" and "Claude.ai". Axes: "Automation Share (%)" / "Augmentation Score (%)".

**Annotation.** The most careful caption in the report. It does four things the body does not: points back to where the taxonomy was defined ("defined in Chapter 1"), discloses an **imputation rule** ("we give that category a value of 0% in this figure"), defines the derived binary the body's 97%/47% claim depends on ("Automation dominance is defined as a task having a greater observed share of automation usage"), and extends the definition symmetrically in three words ("Likewise for augmentation dominance"). Disclosing that censored cells are set to zero is exactly the kind of thing that changes how a reader treats a share, and it is disclosed on the exhibit rather than in a footnote.

> **Table 3.1: Example O\*NET tasks with shorter and longer output lengths with Claude's summaries** For each O\*NET task matched to 1P API traffic we calculate an output token index: Dividing the average output length across transcripts associated with that task by the average (unweighted) value across all tasks in our sample. Claude was prompted to identify tasks at the 10th, 50th, and 90th percentile of the output token index distribution with the minimal guidance: "The columns should be 'Example tasks', 'Index Value', 'Summary' where you provide a summary". Claude associated output length with task complexity.

In-image title: "O\*NET tasks with shorter and longer outputs". Column headers: "Output token index", "Example tasks", "Claude summary of tasks".

**Annotation.** The construction of the index is given as a formula in words, and then — unusually and well — **the prompt is quoted verbatim** along with the claim that it was minimal guidance. The final sentence attributes the interpretation to the model rather than to the authors: "Claude associated output length with task complexity", not "output length measures task complexity". When a model has generated part of an exhibit, this caption is the standard: say what it was asked, quote the ask, and attribute the conclusion to it.

> **Figure 3.6: Average output token index across O\*NET tasks among leading occupational categories** For each O\*NET task matched to 1P API traffic we calculate an output token index: Dividing the average output length across transcripts associated with that task by the average (unweighted) value across all tasks in our sample. We then average across tasks for a given top-level occupational categories in the O\*NET taxonomy for top use occupational groups. 'All Other' combines remaining occupational groups into a single category.

In-image chart title: "Average output token index across leading occupational categories". Axis: "Average output token index for observed tasks in a given category".

**Annotation.** The index definition is repeated **verbatim** from Table 3.1 rather than cross-referenced, and again in Figures 3.7, 3.8 and 3.9 with the relevant numerator swapped. Four captions carrying the same twenty-eight words is a deliberate cost: each exhibit is independently readable. The last sentence discloses the residual category ("'All Other' combines remaining occupational groups into a single category"), which a reader needs before comparing bar heights.

> **Figure 3.7: Scatter plot of output token index and input token index across O\*NET Tasks** For each O\*NET task matched to 1P API traffic we calculate an output token index: Dividing the average output length across transcripts associated with that task by the average (unweighted) value across all tasks in our sample. The input token index is constructed similarly. The elasticity of 0.38 implies that each 1% increase in the input token index is associated with a 0.38% increase in the output token index.

In-image chart title: "Output Token Index vs Input Token Index across tasks". Axes: "ln(Input Token Index)" / "ln(Output Token Index)". Legend lists occupational categories with per-category N.

**Annotation.** A descriptive rather than declarative title — the only one of its kind in Chapter 3 — and the caption compensates by ending on the **interpretation of the coefficient in plain words** ("each 1% increase in the input token index is associated with a 0.38% increase in the output token index"). "associated with", not "produces", in a caption. The per-category sample sizes live in the chart legend, which is where N belongs when the exhibit is a scatter with colour-coded groups.

> **Figure 3.8: API cost per task and usage share across occupational categories** For each O\*NET task matched to 1P API traffic we calculate an API cost index: Dividing the average API cost across transcripts associated with that task by the average (unweighted) value across all tasks in our sample. This figure plots the average API cost index across tasks in a given occupational category against usage share. The estimated elasticity of 3 implies that each 1% increase in the average cost of a task is associated with a 3% increase in prevalence in our sample.

In-image chart title: "Usage share and average API cost index by occupational category". Axes: "ln(Average API Cost Index across tasks)" / "ln(Usage share (%))".

**Annotation.** Same four-part structure — index construction, what is plotted against what, elasticity in words — with the elasticity's meaning scoped to the sample in the final three words: "in our sample". An elasticity of 3 on cost is the report's most counter-intuitive number and the caption states it without editorialising; the interpretation is left to the body, which immediately restricts it.

> **Figure 3.9: Scatter plot of API cost per task and usage share controlling for task characteristics** For each O\*NET task matched to 1P API traffic we calculate an API cost index: Dividing the average API cost across transcripts associated with that task by the average (unweighted) value across all tasks in our sample. We then restrict the sample to tasks appearing in both our 1P API and Claude.ai samples. This partial scatter plot controls for the following task-level characteristics: fixed effects for occupational category, collaboration mode share from Claude.ai, and indicators for whether a given collaboration mode was censored for privacy-preserving reasons in the Claude.ai sample. The estimated elasticity of -0.29 implies that each 1% increase in the API cost index for a given task is associated with a 0.29% decrease in prevalence in our sample, after controlling for task characteristics.

In-image chart title: "Task usage share vs API Cost Index (partial regression after controlling for task characteristics)". Axes: "Residual ln(API Cost Index)" / "Residual ln(Usage share (%))".

**Annotation.** The longest caption, and every extra word earns its place: the sample restriction is stated ("tasks appearing in both our 1P API and Claude.ai samples"), **the full control set is enumerated** — including the missingness indicators, which most papers would leave to an appendix — and the coefficient's interpretation closes with the conditioning clause repeated ("after controlling for task characteristics"). When a coefficient flips sign relative to the unconditional version, the caption is where the reader finds out why. This is the model for a caption on any conditional estimate.

### The caption template, distilled

For any exhibit in this series:

1. **Bold, numbered, no terminal period; sentence case.** Title is a *declarative finding* where there is one to state, descriptive only where there is not.
2. **If the finding is noisy or conditional, the hedge goes in the bold title**, not the gloss (Figure 2.7).
3. **Gloss, plain roman, one sentence per job**, in this order where applicable: what is plotted and in what unit · how any index or share was constructed, restated in full rather than cross-referenced · the sample and any inclusion floor, **with the reason for the floor** · panel logic · what colour, size and marker encode · imputation and censoring rules · residual or "All Other" categories · the null value or benchmark the reader should compare against · the coefficient's meaning in plain words, with "associated with".
4. **No separate source line.** External provenance goes in the title (Figure 3.1) or in a clause; where a measure comes from a survey, quote the survey question.
5. **Tables** get a single noun phrase naming their columns, and a period.
6. **Say Claude.** Every caption in this report says Claude except the one plotting Census data, which says AI.
7. **Repeat verbatim rather than paraphrase.** The 200-observation sentence appears four times word for word; the token-index definition four times. Captions are written to be lifted.

## Limitations

**There is no limitations section.** No "Caveats", no "Limitations", no "Threats to validity" — nothing in 47 pages. This is the single largest structural difference from the February 2025 launch post, which gave its caveats an H3 of their own. Here the caveats are dispersed across four locations, and the dispersal is worth describing precisely, because it is the report's weakest editorial decision and the one our posts should not copy.

### 1. In footnotes, which is where the load-bearing ones are

> [1] For privacy reasons, our automated analysis system filters out any cells—e.g., countries, and (country, task) intersections—with fewer than 15 conversations and 5 unique user accounts. For bottom-up request clusters, we have an even higher privacy filter of at least 500 conversations and 250 unique accounts.

> [2] Data in this section covers 1 million Claude.ai Free and Pro conversations from August 4 to 11, 2025, randomly sampled from all conversations in that period that were not flagged as potential trust and safety violations. The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included, though our past work suggests that sampling conversations at random versus stratified by user does not yield substantively different results. Aggregate geographic statistics at the country and US state level were assessed and tabulated from the IP address of each conversation. For geolocation, we use ISO-3166 codes since our provider for IP geolocation uses this standard. International locations use ISO-3166-1 country codes, US state level data use ISO-3166-2 region codes, which include all 50 US states and Washington DC. We exclude conversations originating from VPN, anycast, or hosting services, as determined by our IP geolocation provider.

> [4] Tier thresholds (quartiles) are based on countries with at least 200 observations for the global level, and on US states with at least 100 observations for the US level. Countries with no observed usage are assigned to the Minimal tier since we do not know if they have exactly zero usage or little usage that our random sample did not capture. Future work, for example using stratified sampling, will allow us to explore these patterns with higher accuracy given limited observations for smaller countries and states.

> [7] When further investigating Utah's activity, we discovered a notable fraction of its usage appeared to be possibly associated with coordinated abuse. This is also reflected in a much higher "directive" automation score than average. However, we ran robustness checks and believe that this activity is not driving the results.

> [4, Ch. 1] We note that V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison. To address this, we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (though to a lower absolute level of 45% automation versus 49% with Sonnet 4). We also verified this trend is not driven by changes in task mix—the shift toward directive interactions appears across a wide range of occupational categories, suggesting it reflects genuine changes in how people interact with Claude rather than compositional effects.

> [2, Ch. 3] Data in this section covers 1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage. We continue to manage data according to our privacy and retention policies, and our analysis is consistent with our terms, policies, and contractual agreements. Each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions.

> [3, Ch. 3] Note that this is a different measure of adoption than in the introduction to this report. Reported adoption by consumers and employees of AI reached 40% in 2024 whereas when measured at the firm-level, nine out of ten businesses in the US report not using AI.

> [10] Another contributing factor could be the degradation in performance some models experience at longer context lengths. See Liu et al, 2023, *Lost in the Middle: How Language Models Use Long Contexts.*

> [11] The question we ask in this section is whether, all else equal, cost differences across tasks shapes relative usage patterns. This is different from studying whether overall Claude usage is sensitive to external competitive pricing pressures.

### 2. Inside the sentence carrying the finding

> While the overall pattern is noisy–especially for countries with fewer observations–Figure 2.7 suggests that…

> This is somewhat counter-intuitive, since we are controlling for the more diverse task composition across different countries. We speculate that cultural and economic factors might affect the automation share, or perhaps that early adopters in each country tend to use AI in a more automotive way—but more research is needed here.

> Of course, output length does not capture all dimensions of task complexity, but it appears to be a sensible, easily measured proxy.

> With the important caveat that this should be viewed as a preliminary exploration, this is what we find.

> Our API data captures enterprise AI adoption in its early stages: highly concentrated, automation-focused, and surprisingly price-insensitive (at least among the tasks our API customers use Claude for).

> Though not adjusted for population, we suspect that these strong adoption figures partly reflect rapid adoption in technology hubs…

> However, this concentration is affected by the population size of each country – larger countries may have larger usage shares purely because of their population size.

### 3. In captions

The 200-/100-observation floors with their stated reason; the 0% imputation for privacy-censored collaboration modes (Figure 3.5); the 1%-frequency inclusion floors (Figures 2.8–2.10); the "All Other" residual category (Figure 3.6); the full control set and the both-samples restriction (Figure 3.9).

### 4. As an open question rather than a limitation

> Key questions we hope this data will help others to investigate include: … What role, if any, does cost-per-task play in shaping enterprise deployment patterns? Why are firms able to automate some tasks and not others?

> Understanding the uneven labor market implications of AI adoption is an important area for future research.

> This will be an important area of inquiry for future research.

### Annotation

- **Placement.** Dispersed, never collected. The consequence is that the report's caveats are individually excellent and collectively invisible: a reader cannot answer "what are the limitations of this report?" without reading all 28 footnotes. The February 2025 post could be criticised for putting six caveats in one list and ranking none of them; this report can be criticised for the opposite. The form our posts should use takes the best of each — the specificity of these footnotes, in a section a referee can find.
- **Specificity.** Very high, and particular rather than ritual in every instance. Sample windows are given to the day (4–11 August 2025). The API sample's coverage is quantified ("roughly half of our 1P API usage") rather than described. The unit of observation is named and its consequence stated ("a conversation … not a user, so it is possible that multiple conversations from the same user are included"), with the check that addresses it cited. VPN, anycast and hosting traffic are excluded and the excluder is named ("as determined by our IP geolocation provider"). The geolocation standard is given with its version numbers. Privacy thresholds are given as two numbers each, twice, at two granularities. There is not one sentence of the form "as with all studies, there are limitations".
- **Where a threat is answered, the answer is reported with its discrepancy.** Footnote 4 of Chapter 1 is the model: the threat (classifier changed), the test (rerun on the old classifier), the result (direction holds), **the number that differs** (45% versus 49%), and a second, independent check (not compositional). Reporting the 4-point level difference rather than only the qualitative agreement is what makes the footnote trustworthy.
- **Where a threat is not answered, the report says so in the same breath.** "we ran robustness checks and believe that this activity is not driving the results" — belief, not demonstration, and the word "believe" is doing honest work. "but more research is needed here" appears verbatim. "With the important caveat that this should be viewed as a preliminary exploration" is placed before the result.
- **The two caveats a referee would raise first, and where they are.** (i) *Inferred geography.* Every geographic number rests on IP geolocation of conversations, with VPN traffic excluded — so the AUI measures where conversations originate, not where users live or work, and the exclusion itself is selective in a way that could bias exactly the high-adoption, technically sophisticated populations the report is ranking. This is in footnote 2, stated factually, never discussed. (ii) *Utah.* A state named in the Introduction's headline bullet has usage the authors themselves describe as "possibly associated with coordinated abuse", and the caveat is in footnote 7 while the number is on page 4 unmarked. Both belong in the body.
- **A third that is not raised at all.** The 77%/12% automation/augmentation split for API transcripts leaves 11% unaccounted for in the body; the caption for Figure 3.5 explains that privacy-censored modes are zeroed, which is adjacent to an explanation but is not one. A reader cannot tell from the report whether the residual is censoring, unclassified transcripts, or something else.
- **Drafting tells.** The tier definitions in the body read "*Leading* (top 25%), *Upper Middle* (50-75%), *Lower Middle* (25%-75%) and *Emerging* (bottom 25%)" while Table 2.1's own rows read "Lower middle (25-50%)". The prose and the exhibit disagree on one boundary. Minor, and mentioned only because it is the kind of thing that survives into a published report when the definitions live in three places.

## Close

### Chapter-level closes, verbatim

Chapter 1, "Looking Ahead":

> The V3 data reveals that AI capabilities and adoption are continuing to progress. Knowledge-based tasks, including educational and scientific applications, continue their fast growth rate, and new product features appear to be enabling different types of work rather than just accelerating existing tasks.

> Most strikingly, the data point toward increased delegation of tasks to AI systems–perhaps due to some combination of user trust in the technology as well as improvement of underlying model capabilities. This could also be due to changes in the underlying user base. The next chapter of this report for the first time breaks down usage across geography, allowing us to disentangle temporal vs. geographic changes more clearly going forward. We will continue to track these trends closely in future reports.

Chapter 2, "Conclusion":

> Our analysis of Claude usage patterns across geographies reveals several key insights. One of the most striking is the geographic concentration of Claude usage. The leadership of the US and California in terms of Claude usage overall, and the strong correlation of Claude usage and income per capita, suggest parallels to past technologies in which initial geographic concentration and specialized use were a key feature. Drawing parallels to the diffusion patterns of prior technologies may help us better understand the diffusion and impact of AI.

> Surprisingly, geography shapes not just *what* AI tools are used for, but *how* they are used. Users in economies with relatively low per capita usage have a relative preference for delegating tasks to Claude (automation), whereas users in economies with high per capita usage are somewhat more likely to prefer more collaborative or learning-based interactions with Claude (augmentation), even when controlling for the task mix. Similar to the local specialization in task use, the local specialization in AI collaboration patterns suggests that impact of AI could be very different in different regions.

> The geographic patterns of AI adoption—where it is used, for which tasks, and how—suggest that in order to realize the potential of AI to benefit people across the globe, policymakers need to pay attention to local concentration of AI use and adoption, and address the risk of deepening digital divides.

Chapter 3, "Conclusion":

> Our API data captures enterprise AI adoption in its early stages: highly concentrated, automation-focused, and surprisingly price-insensitive (at least among the tasks our API customers use Claude for).

> The 77% automation rate suggests enterprises use Claude to delegate tasks, rather than as a collaborative tool. Such systematic deployment is likely to be an important conduit by which AI delivers broader productivity gains within the economy. Given clear automation patterns in business deployment, this may also bring disruption in labor markets, potentially displacing those workers whose roles are most likely to face automation.

> But the implications for the labor market are not entirely clear. As we document above, complex tasks require disproportionately more context. Such information may be scattered across organizations. In such conditions, workers with tacit knowledge about business operations may stand to benefit as complements to sophisticated AI-powered automation.[14] Understanding the uneven labor market implications of AI adoption is an important area for future research.

> Businesses looking to adopt AI effectively may need to restructure how they organize and maintain the information that frontier systems rely on. Whether today's narrow, automation-heavy adoption evolves toward broader deployment will likely determine AI's future economic impacts.

### "Concluding remarks", verbatim and in full

> This third iteration of the Anthropic Economic Index Report captures AI adoption at a critical juncture. Existing capabilities of Claude and other frontier AI systems are already poised to transform economic activity, given how broadly applicable the technology is. Rapidly advancing AI capabilities only reinforce the conclusion that immense change is on the horizon.

> And yet early AI adoption is strikingly uneven. Usage currently clusters in a small set of tasks, with strong geographic variation that is highly correlated with income—particularly across countries. Such concentration reflects where AI capabilities, ease of deployment, and economic value align: coding and data analysis have high usage, while tasks requiring dispersed context or complex regulatory navigation are further behind.

> Early business adoption of Claude is at once both similar to consumer use (coding is the most common use for both), and different in several consequential ways. In particular, with programmatic access to Claude through the API, businesses tend to use Claude with greater automation. Such systematic enterprise deployment reflects how AI is poised to reshape economic activity: increasing overall productivity, but with uncertain implications for those workers whose existing responsibilities have been automated.

> These patterns risk creating divergence. If AI's productivity gains concentrate in already-prosperous regions and automation-ready sectors, existing inequalities could widen rather than narrow. If AI automation improves the productivity of workers with tacit organizational knowledge—as some of our evidence suggests—then more experienced workers could see rising demand and higher wages even as entry-level workers face worse labor market prospects.[1]

> Building on our previous releases, this iteration of the Index's reports marks a significant expansion in both scope and transparency. We are now open-sourcing comprehensive API usage data alongside our existing Claude.ai consumer data (now including geographic breakdowns at state and country levels), all intersected with detailed task-level classifications.

> By making this data public, we hope to enable others to investigate questions we haven't considered, test hypotheses about AI's economic impacts, and develop policy responses grounded in empirical evidence.

> **Ultimately, the economic effects of transformative AI will be shaped as much by technical capabilities as by the policy choices societies make.**

> History shows that the patterns of technological adoption aren't fixed: they shift as the technologies mature, as complementary innovations emerge, and as societies make deliberate choices about their deployment. The patterns of highly concentrated use that we observe today may yet evolve towards a broader distribution—one that captures more of AI's productivity-enhancing potential, accelerates innovation in lagging sectors, and enables new forms of economic value creation.

> We are still in the early stages of this AI-driven economic transformation. The actions that policymakers, business leaders and the public take now will shape the years to come. We'll continue tracking these patterns as AI capabilities advance, and provide empirical grounding for navigating one of the most significant economic transitions of our time.

### Annotation

- **What was learned.** Stated as a *shape*, not a list of numbers. "And yet early AI adoption is strikingly uneven" is the whole report in seven words, and it is the thesis the Introduction bolded ("a hallmark of early technological adoption is that it is *concentrated*") now written in the past tense of something established. Only one number survives into the close — the 77% automation rate, in Chapter 3's conclusion, not in the Concluding remarks, which contain no figures at all. The three chapters' findings are compressed into two sentences that name the *dimensions* of unevenness (tasks, geography, income) and one that names the mechanism ("Such concentration reflects where AI capabilities, ease of deployment, and economic value align"), with examples on both sides of the line ("coding and data analysis have high usage, while tasks requiring dispersed context or complex regulatory navigation are further behind").
- **Why it matters.** Two conditionals, both with antecedents the report did not measure, both stated in one paragraph: "**If** AI's productivity gains concentrate in already-prosperous regions and automation-ready sectors, existing inequalities could widen rather than narrow. **If** AI automation improves the productivity of workers with tacit organizational knowledge—as some of our evidence suggests—then more experienced workers could see rising demand and higher wages even as entry-level workers face worse labor market prospects." The second conditional has an interpolated evidence claim — "as some of our evidence suggests" — which marks precisely how much of that antecedent the report can support and how much it cannot. The paragraph opens on the stake and then earns it: "These patterns risk creating divergence." This is the corpus's best example of a why-it-matters that is genuinely conditional without being evasive: the reader is told what would follow, what it depends on, and how much of the dependency is evidenced.
- **What comes next.** Committal about method and data, silent about results. "We'll continue tracking these patterns as AI capabilities advance"; the dataset expansion is enumerated ("comprehensive API usage data alongside our existing Claude.ai consumer data (now including geographic breakdowns at state and country levels), all intersected with detailed task-level classifications"); and Chapter 1's close names the specific analytical gain the next wave unlocks ("The next chapter of this report for the first time breaks down usage across geography, allowing us to disentangle temporal vs. geographic changes more clearly going forward"). Three separate "important area for future research" sentences name the three questions the report opened and could not close. Nothing predicts which way a future number will move.
- **Recommendations, and who receives them.** This report *does* make recommendations, which is a change from February 2025's explicit refusal to offer policy prescriptions. There are three, each addressed to a different audience and each hedged:
  - *Policymakers*, at the end of Chapter 2: "in order to realize the potential of AI to benefit people across the globe, policymakers need to pay attention to local concentration of AI use and adoption, and address the risk of deepening digital divides." "Pay attention to" and "address the risk of" — a direction of attention, not an instrument. No tax, subsidy, programme or regulation is named anywhere in 47 pages.
  - *Businesses*, at the end of Chapter 3: "Businesses looking to adopt AI effectively may need to restructure how they organize and maintain the information that frontier systems rely on." A conditional recommendation that follows directly from the context finding — the one recommendation in the report traceable to a specific coefficient.
  - *Researchers*, in the Introduction and again in the close: four named questions and an open dataset. "we hope to enable others to investigate questions we haven't considered."
  The report's own limit is still stated, but as a division of labour rather than a refusal: "the economic effects of transformative AI will be shaped as much by technical capabilities as by the policy choices societies make." That is the one bolded, single-sentence paragraph in the document, and it is the report's thesis about its own role — measurement is necessary and not sufficient.
- **How it avoids a template summary.** Six devices, all worth copying. (i) **No numbers.** Not one figure in the Concluding remarks. (ii) **Every paragraph opens on the world, not the report** — "And yet early AI adoption is strikingly uneven"; "These patterns risk creating divergence"; "History shows that the patterns of technological adoption aren't fixed"; "We are still in the early stages of this AI-driven economic transformation." Only two of nine paragraphs open with "this report" or "we", and both are about the data release. (iii) **"And yet"** as the second paragraph's first two words: the close is built as a *tension* between capability and unevenness rather than as a recapitulation. (iv) **The report argues against its own reading of the future** — the concentration it documents is explicitly not projected forward ("the patterns of technological adoption aren't fixed: they shift as the technologies mature… The patterns of highly concentrated use that we observe today may yet evolve towards a broader distribution"). A close that undermines the extrapolation its own findings invite is the opposite of a summary. (v) **The contribution claim is about scope and transparency, not about results** — "marks a significant expansion in both scope and transparency", which is the same move as February 2025's "the most important contribution… is its new methodology". (vi) **The last sentence names the register the whole series is written in**: "provide empirical grounding for navigating one of the most significant economic transitions of our time." Grounding, not answers.
- **Title against ending.** Title: "Uneven geographic and enterprise AI adoption." Ending: "And yet early AI adoption is strikingly uneven… These patterns risk creating divergence." The title's adjective is the close's predicate, and the title's two nouns are the close's two paragraphs. They match exactly, and the match is tight enough that the title could have been written from the close or the close from the title. This is the standard to hold a draft to: **if the ending does not contain the title's key word doing work, one of the two is wrong.**
- **First person.** Used throughout for institutional acts and analytical moves ("We are now open-sourcing", "we hope to enable", "We'll continue tracking", "as we document above", "we find", "We speculate"). Our house style forbids it; the substitute for the *commitment* sentences is the passive or attribution to the series, and the substitute for the *analytical* sentences is to attribute to the analysis or the exhibit — which this report already does half the time ("Figure 2.7 suggests that…", "The data suggests it is not"). That second construction is the one to borrow.
- **Three chapter closes plus one report close.** Each chapter conclusion states that chapter's findings, its interpretation, and its open question; the Concluding remarks do not repeat them but re-describe all three as one pattern. A multi-part post should close each part and then close once more at a level of abstraction none of the parts reached. Note that each chapter close also **contains its own hedge on its own headline** — Chapter 1's "This could also be due to changes in the underlying user base", Chapter 3's "But the implications for the labor market are not entirely clear" — so no section ends on its strongest possible reading.

## Verification

- **URLs fetched, both on 2026-09-16:**
  - https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf — returned in full, 47 pages, all pages present including page renders of every figure and table. This is the document of record and is the source for every quotation in this file unless a quotation is explicitly marked as web-page text.
  - https://www.anthropic.com/research/anthropic-economic-index-september-2025-report — returned in full (page title "Economic Index: Uneven AI adoption", dated "Sep 15, 2025"). Used only to establish how the web page condenses the PDF (see `## Source`) and to confirm the figure-reference drift.
- **Fetch date:** 2026-09-16. **Fetch failures: none.** Both documents returned complete on the first attempt.
- **Not fetched, deliberately:** the mirror PDF at https://www-cdn.anthropic.com/7b76335c444876a93fa22a63aabb4aeb820aff25.pdf (listed in `wiki/INDEX.md` as an identical file; not independently verified as identical here, and nothing in this file depends on it) and the arXiv version at https://arxiv.org/abs/2511.15080 (a later posting of the same report; its section order, captions and abstract may differ, and no claim in this file should be taken to describe it). Also not fetched: the Clio post, the Global Innovation Index page, the interactive dashboard, the Stanford HAI and Ipsos pages, the Anthropic feature-launch posts, and every cited external paper. Nothing from any of them is quoted here.
- **Every quotation was checked back against the fetched text** word by word after transcription. Confirmed for all nine sections of this file.
- **Quotation caveats.**
  - Hyperlink URLs were stripped from quoted prose and the anchor text retained; anchors in the opening are listed in `## Opening move`.
  - Typographic apostrophes, quotation marks and arrows in the sources were normalised to ASCII. No word was changed.
  - **PDF line-break hyphenation was repaired.** The extracted text contains artefacts where the PDF broke a word across lines without a hyphen ("percapita", "backand-forth", "learning-bydoing", "opensourcing", "privacypreserving", "programmingdominant", "automative" where the source reads so, "RecentEmployment"). Quotations here restore the intended spacing. No other change was made, and the only case where the reading is even slightly uncertain is footnote 1 of the Concluding remarks ("RecentEmployment Effects"), where the title of the cited paper is unambiguous.
  - Footnote numbering in quotations is given in square brackets, e.g. "[4]", where the source uses a superscript. Where two chapters both number a footnote 4, the quotation is labelled with its chapter, e.g. "[4, Ch. 1]".
  - Emphasis (bold, italic) is reproduced as it appears in the PDF. Where the PDF bolds a caption title and the web page italicises the whole caption, the PDF form is used.
  - **Alt text and chart-image numbers, per `room/director-2026-09-16-alt-text-ruling.md`.** Bold captions under exhibits are the captions and are quoted as such. Text rendered *inside* a chart image — chart titles, panel titles, axis labels, legend entries — is quoted only where it bears on the caption pattern and is explicitly marked "in-image chart title", "panel titles", "axis", or "legend"; it is never presented as caption or prose. **No number was read off a chart image and recorded anywhere in this file.** In particular, the values printed inside Figures 1.1, 1.2, 2.1, 2.2, 2.4, 2.5, 2.7, 2.8, 2.9, 2.10, 2.11, 3.1–3.9 and Tables 2.1, 2.2, 3.1 — including the fitted coefficients, R², p-values, Gini values, per-category N and index values shown in their annotation boxes and legends — are not recorded. Every number quoted in this file appears in the PDF's body prose, its footnotes, or a caption.
- **Scope.** This file annotates how the report is written: its section order, the grammar of its findings and caveats, how its comparisons are phrased, its caption template, where its limitations sit, and how it closes. It makes no judgement about whether any finding is correct. Where this file says a caveat is misplaced or a residual is unexplained, that is a statement about the writing, not about the analysis.
