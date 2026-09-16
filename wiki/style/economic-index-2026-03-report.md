# economic-index-2026-03-report — style annotation

## Source

- **Title (PDF cover, and the document of record):** "The Anthropic Economic Index report: Learning curves", set over three lines on the cover. The web page H1 drops the leading article: "Anthropic Economic Index report: Learning curves". The browser/OG title is the same as the H1 ("Anthropic Economic Index report: Learning curves \ Anthropic"), and — unusually for this series — **the report's own citation block also drops the article**, giving the title as "Anthropic Economic Index report: Learning curves" in both the PDF and the web page. So the cover is the only place the full title appears.
- **Date:** PDF cover, "Published / March 24, 2026". Web page, "Mar 24, 2026". PDF creation timestamp 2026-03-24 22:18 UTC.
- **URLs fetched:**
  - PDF (document of record): https://cdn.sanity.io/files/4zrzovbb/website/4053bf3440c0c85b8852052770c5b4cf882689c3.pdf — 20 pages, letter, Adobe InDesign 21.2. Retrieved with `curl` (see `## Verification`); the fetch service refuses `cdn.sanity.io`.
  - Web page: https://www.anthropic.com/research/economic-index-march-2026-report
  - Not fetched: either copy of the separate appendix (https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf, linked from the introduction's stray anchors; https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf, linked from the "Appendix" pointer in both the PDF and the web page). The appendix has its own corpus slug, `economic-index-2026-03-appendix`.
- **Document type:** the fifth report of the standing series, and **the series' shortest and least self-contained report so far**. Two unnumbered chapters, a named author list with a lead-author tier, eleven footnotes, no abstract, no executive-summary block, no methods section, no limitations section, and a close headed "Discussion" rather than "Concluding remarks". The report never numbers itself; it says "This latest report", "our previous report", "our previous reports", "our first report".
- **Approximate length:** 20 PDF pages; roughly 4,300–4,600 words of body prose. Cover, p. 1; Introduction, pp. 2–4; Chapter 1, pp. 5–11; Chapter 2, pp. 12–18; Discussion, pp. 19–20; appendix pointer, data availability and citation, p. 20. Nine numbered figures (1.1–1.5, 2.1–2.4) and two numbered tables (1.1, 2.1) — eleven exhibits in twenty pages, i.e. an exhibit every other page.
- **Authors named on the cover:** "Maxim Massenkoff,\* Eva Lyubich,\* Peter McCrory,\* / Ruth Appel, Ryan Heller", with "\*Lead authors of the report". Two tiers again, but the starred tier is not asserted to have contributed equally — the September 2025 report's "Contributed equally" clause is gone. Twenty-four acknowledgees. The web page moves the cover matter to an "Authors and acknowledgements" section at the foot and gives the two tiers their own sub-headings, "First author block\*" and "Second author block", which is closer to a journal's byline convention than to a cover.
- **Audience, and a change worth naming.** There is **one external academic citation in the whole document**: the phrase "skill-biased technological change" in the Discussion, hyperlinked (web page only) to a *Journal of Economic Literature* article. The only other outside source is the BLS OEWS wage table in footnote 5 of Chapter 1. Where the September 2025 report cited Gallup, Bick–Blandin–Deming, Gordon, Pritchett, Kremer, Hall–Kahn and a dozen more, this report's comparison set is almost entirely **its own previous waves**. The reader it assumes is a reader of the series: two of the eleven footnotes send the reader to the appendix, three more refer back to an earlier report, and ten of the nineteen hyperlinks in the PDF point at the January 2026 report or at this report's appendix. A reader who has not read the January 2026 report cannot find out here what a "primitive", an "interaction type", "success" or "log-level data" is — each is defined only by reference to the appendix or the previous report.

### How the web page condenses the PDF

Again, very little is condensed: the web page carries the whole text. The differences that matter for style:

1. **Nothing is dropped and nothing is added, except one clause.** The web version of Figure 1.4's surrounding paragraph reads "the tasks we see on Claude tend to require higher education. The plot shows that these tasks also tend to earn higher wages **than the US national average**." The PDF reads "…tend to require higher levels of education. The plot shows that these tasks also tend to earn higher wages." The web adds the benchmark; the PDF leaves it to an annotation inside the chart. This is the only place where the two versions differ in content rather than typography, and the web is the better sentence — a comparison is worth more than a figure annotation.
2. **Caption typography inverts.** PDF: bold "Figure 1.1: Usage shares among top 10 tasks over time by platform, Claude.ai and 1P API" with **no terminal period**, then the gloss on the next line in plain roman. Web: the title takes a period **and the entire caption, gloss included, is bold**. Same words; the web page gives the gloss the same weight as the title, which the PDF deliberately does not.
3. **A figure cross-reference is off by one.** Web page: "The left panel of **Figure 1.6** shows that this convergence continued" — PDF, same sentence, "**Figure 1.5**". Both carry the caption "Figure 1.5: Geographic convergence", and there is no Figure 1.6 in either version. This is the same defect class as the September 2025 report's Chapter 3 drift, and again **the PDF is internally consistent and the web page is not**. Cite the PDF.
4. **Footnote numbering is restructured.** The PDF numbers footnotes **per chapter** and restarts: one footnote in the Introduction (¹, the 1P API definition, set on p. 4), seven in Chapter 1 (p. 11), three in Chapter 2 (p. 18). The web page renumbers all eleven in one continuous sequence. A quotation carrying a footnote marker therefore needs its chapter attached; this file labels them, e.g. "[2, Ch. 1]".
5. **Tables are text in the PDF and images on the web.** Tables 1.1 and 2.1 extract as live text from the PDF, with their ▼/▲ direction glyphs intact. On the web they are PNGs, so every number in them is available to a web reader only as a picture.
6. **Some web hyperlinks are misplaced.** On the web the bare word "than" in the Introduction's third paragraph, and the word "Claude.ai," in the sampling paragraph, are both hyperlinked to the appendix PDF; neither is a link in the PDF. And the anchor "previous report" in "Emergent automation patterns" points to a different document in each version — in the PDF it points to the January 2026 report, on the web to another Sanity-hosted PDF (`a42bc3fc…`), which was not fetched and is therefore not identified here.
7. **Citation keys differ.** PDF: `@online{massenkoff2026learning, …}`. Web: `@online{anthropic2026aeiv5, …}`. Same authors, same title, same date, same URL. The web key encodes the series position (v5) that the prose never states.
8. **Front matter moves to the back**, and chapter titles are unchanged (both versions use sentence case; there is no title-case cover-to-web recasing to undo this time).
9. **The web page carries a one-sentence abstract the PDF does not have**, in its meta description: "The March 2026 Anthropic Economic Index report finds Claude use cases diversifying and experienced users seeing higher conversation success rates." That sentence is the tightest statement of the report's two findings anywhere, and it exists only in the page's head.

## Section order

Headings in PDF order; page spans are the PDF's own numbering. **Neither chapter is labelled "Chapter"** — the headings are bare, and the chapter structure is visible only in the figure numbering (1.x, 2.x) and in prose ("In the first chapter", "In our second chapter", "In this chapter").

1. **Cover (p. 1).** Title, publication date, authors, lead-author note, acknowledgements. No abstract, no findings, no figure.
2. **Introduction (pp. 2–4), ~700 words.** Four moves: (i) two paragraphs establishing what the Index is, which month is measured, and which models were current; (ii) two paragraphs previewing the two chapters in prose; (iii) a bolded heading **"What has changed since our last report"** with a "We find that:" lead-in and three bullets; (iv) a bolded heading **"Learning curves"** — the report's own title — with three framing paragraphs and two bullets. Footnote 1 (the 1P API definition) sits alone on p. 4.
3. **Chapter 1: "What has changed since our last report" (pp. 5–11), ~1,700 words.**
   - *Diversification of use cases in Claude.ai* (pp. 5–9) — the sample is defined in the first paragraph; then concentration, the mechanism for the decline, the work/personal/coursework mix, novel-task coverage, collaboration mode, platform migration, task value in dollars, and the primitives. Figures 1.1–1.4 and Table 1.1.
   - *Emergent automation patterns* (p. 9) — two paragraphs and two bullets naming two API workflows whose share at least doubled.
   - *Revisiting geographic convergence* (pp. 10–11) — Figure 1.5, and the revised convergence horizon.
   - Footnotes 1–7 (p. 11), carrying the Claude Code inclusion, the O\*NET vintage change, the term-time decomposition, the interaction-type pointer, the whole wage construction, the emergent-pattern filter, and the weighted/unweighted range behind the horizon.
4. **Chapter 2: "Learning to use AI" (pp. 12–18), ~1,700 words.**
   - *Chapter opener* (p. 12, ~180 words) — two paragraphs, each stating what will be studied **and the prediction that would confirm it**.
   - *Model selection* (pp. 13–14) — Figures 2.1 and 2.2.
   - *Learning curves* (pp. 15–16) — Table 2.1, Figure 2.3, and the self-selection/survivorship paragraph.
   - *Experience effects* (pp. 17–18) — Figure 2.4, the three-specification ladder.
   - Footnotes 1–3 (p. 18): the log-level data and privacy thresholds; "These results are similar however we define high tenure"; the Super Bowl advertising overlap.
5. **Discussion (pp. 19–20), ~530 words.** Six paragraphs. No bolded thesis sentence, no policy paragraph, and — unlike the September 2025 close — numbers in it.
6. **Appendix ("Available here."), Data availability, Citation (p. 20).**

**Where the findings sit: in the Introduction, then in the chapters, then partly for the first time in the close.** The headline numbers are on pp. 2–4, before the sample paragraph on p. 5 — the series' settled architecture. But this report breaks the architecture at the other end: the Discussion's first paragraph reports that "the top 10 O\*NET tasks now [account] for 33% of traffic, up from 28%" for the 1P API, and **those two numbers appear nowhere in the body prose or in any caption** — their only support is the data labels printed inside Figure 1.1. A number making its first prose appearance in the close is a fault worth naming, because the close is where a reader stops being able to check.

**Where the methods sit: outside the document.** There is no methods section, and three times the reader is sent to the appendix — "See the Appendix for definitions of the interaction types", "See the Appendix for definitions of these primitives", "See the Appendix for more on the methodology" — plus once to the previous report for the definition of the success measure. The September 2025 report defined every construct at its point of use and documented the sample in footnotes; this report defines the sample (pp. 2 and 5) and **exports the constructs**. The consequence for a reader is exact: of the eleven exhibits, the four that carry the report's most interesting quantities (Table 1.1's primitives, Table 2.1's autonomy and education facets, Figure 2.3's education years, Figure 2.4's success measure) cannot be interpreted from this document alone. Our own posts define in the post.

**One layout fact with an editorial consequence.** Table 1.1 is the only exhibit in the report that the prose never cross-references: the paragraph it belongs to ("changes in several primitives between the previous and current report…", p. 8) names its numbers without pointing at it, and the table is printed a page later, below the next section's bullets. Table 2.1, by contrast, is introduced by name in its first sentence. The asymmetry shows what the cross-reference is for.

## Opening move

### The Introduction, first four paragraphs, verbatim

> The Anthropic Economic Index uses our privacy-preserving data analysis system to track how Claude is being used across the economy. It's part of our effort to understand the economic impacts of AI as early as possible, so that researchers and policymakers have adequate time to prepare.

> This latest report studies Claude usage in February 2026, building on the economic primitives framework introduced in our previous report (which used data from November 2025). Our sample covers February 5 to February 12, three months following the release of Claude Opus 4.5 and coincident with the release of Claude Opus 4.6.

> We first document how usage has changed relative to our previous reports: the rate of augmentation, collaborative interaction where the AI complements the user's abilities, increased slightly in both Claude.ai and API traffic. In Claude.ai, usage diversified, with the top 10 tasks accounting for a smaller share of usage last month than in November 2025. As a result of this diversification, the average conversation in Claude.ai had a slightly lower-wage task than in previous reports.

> We then focus on an important determinant of Claude's impact on the labor market and the broader economy: learning curves in Claude adoption. We present evidence that high-tenure users have developed habits and strategies that allow them to better harness Claude's capabilities. Indeed, we document that more experienced users not only attempt higher-value tasks, but are also more likely to elicit successful responses in their conversations.

("system" is hyperlinked to the Clio post; "previous report" to the January 2026 report PDF.)

### The first preview block, verbatim

> **What has changed since our last report**
>
> In the first chapter, we revisit findings from our previous Economic Index report, published in January 2026. We find that:
>
> - **Use cases on Claude.ai diversified**
>   Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic.[1] In this report, Claude.ai usage was less concentrated: the top 10 tasks made up 19% of all traffic in February, down from 24% in November. That said, almost all tasks in this sample appeared in at least one of our previous samples. About 49% of jobs have seen at least a quarter of their tasks performed using Claude.
> - **Claude adoption broadened to lower-wage tasks**
>   As use cases have diversified, the average economic value of work done on Claude—as measured by US wages paid to workers in the associated occupations—has decreased slightly. This is caused, mechanically, by a rise in personal queries around sports, product comparisons, and home maintenance. The pattern is consistent with a standard "adoption curve" story, in which early adopters favor specific high-value uses like coding, and later adopters take on a much wider range of tasks.
> - **Inequality in global usage has persisted**
>   Usage remains heavily concentrated: the top 20 countries account for 48% of all per-capita usage, up from 45%, underscoring a persistent gap in global adoption. However, Claude usage per capita continued to converge within the United States: the share of usage accounted for by the 10 highest usage states decreased from 40% to 38% since our last report.

### The second preview block, verbatim

> **Learning curves**
>
> A central finding in the Economic Index is that early adoption of Claude is very uneven: Claude is used more intensely in high-income countries, within the US in places with more knowledge workers, and for a relatively small set of specialized tasks and occupations.
>
> An important question is how inequality of adoption might determine where and to whom the benefits of AI will accrue. If, for example, effective AI use requires complementary skills and expertise—which we argued in our previous report—and if such skills can be acquired through use and experimentation, then the benefits from early adoption may be self-reinforcing.
>
> In our second chapter we investigate how users appear to shape the value that they get out of Claude: how they match model capability to the task at hand, and how usage patterns and outcomes shift with experience on the platform.
>
> - **Model selection matches the task**
>   We show that users choose our most intelligent model class, Opus, for tasks that normally receive higher wages in the labor market. For example, among paying Claude.ai users, Opus is used 4 percentage points more than average for coding tasks and 7 percentage points less than average for tutoring-related tasks. This model switching is about twice as stark for API users.
> - **Higher tenure, higher success**
>   In general, the most seasoned Claude users employ it more often for higher-education tasks and less often for personal use cases. For example, people who have been using Claude for 6 months or more have 10% fewer personal conversations and a 6% higher education level reflected in their inputs. Most strikingly, people in this higher-tenure group have a 10% higher success rate in their conversations, an association that is not explained by their task selection, country of origin, or other factors. While this could reflect sophistication of early adopters, it could also be evidence of learning-by-doing, where people get better at using Claude through experience.

### Annotation

- **What question is posed, and where.** Not in the first paragraph. The Introduction opens on the *instrument* — what the Index is, what it tracks, why it exists — and the first two paragraphs are pure series maintenance: which month, which window, which models were current. Compare the two openings already in the corpus: February 2025 opens *forecast → therefore measure*; September 2025 opens *anomaly → prior literature → bolded thesis*. This one opens **wave → window → what changed → what is new this time**. It is the opening of a report whose right to the reader's attention is assumed, and it is the weakest of the three as a piece of writing. The question does not arrive until p. 3, and when it arrives it is very good: "An important question is how inequality of adoption might determine where and to whom the benefits of AI will accrue."
- **The why-it-matters is a two-premise conditional.** "**If**, for example, effective AI use requires complementary skills and expertise—which we argued in our previous report—**and if** such skills can be acquired through use and experimentation, **then** the benefits from early adoption may be self-reinforcing." Both antecedents are named, one is sourced to the series' own earlier work, the second is exactly what this report tests, and the consequent is a distributional claim ("self-reinforcing") rather than a magnitude. This is the sentence the whole report hangs on and it is the single most transferable construction in the document: **state the stake as a conditional, name which antecedent you are about to test, and leave the other one cited.**
- **How soon the first number appears.** No outside number appears anywhere in the Introduction, and the first Anthropic number is "19% of all traffic in February, down from 24% in November", about 400 words in. The benchmark for every headline number in this report is **its own previous wave**, not a survey, not a history of technology, not an official statistic. That is the mature form of a series and it is also a narrowing: the September 2025 report could make its numbers anomalous by putting them beside Gallup and electrification, and this one cannot.
- **"This is caused, mechanically, by…"** is the only unhedged causal verb in the Introduction, and the adverb is what licenses it: the claim is arithmetic — a composition shift — not behavioural. Worth copying exactly. When causation is decomposition, say *mechanically* and drop the hedge; when it is behaviour, hedge and keep the verb weak.
- **The bullet form is the series' two-beat bullet, with a variation.** In the PDF the bold lead-in sits on **its own line with no terminal period** and the evidence follows as a paragraph; on the web the lead-in takes a period and runs in. Every bullet is *claim in words → claim in numbers → hedge*: "That said, almost all tasks in this sample appeared in at least one of our previous samples"; "The pattern is consistent with a standard 'adoption curve' story"; "an association that is not explained by their task selection, country of origin, or other factors"; "While this could reflect sophistication of early adopters, it could also be evidence of learning-by-doing".
- **Two blocks, not three, and the second is the title.** The preview headings are "What has changed since our last report" and "Learning curves" — which are also the report's two chapter titles (the second renamed to "Learning to use AI" as a chapter and kept as "Learning curves" for its middle section). The reader meets the title phrase three times before the chapter arrives.
- **The summary quotes the largest available version of its headline number.** The tenure bullet gives "10% fewer personal conversations", "a 6% higher education level" and "a 10% higher success rate" — all **relative** changes. Table 2.1 gives the same three quantities as 44.3% → 40.3% (▼ -4.0 pp), 11.5 → 12.3 (▲ +6.6%) and 66.7% → 73.1% (▲ +6.4 pp); the body's regressions give the success gap as "about 5 percentage points" raw, "closer to 3 percentage points" with task fixed effects, and "a 4 percentage point higher success rate" with full controls. So the single most quoted number in the report exists in four versions, **and the summary chose the one that reads largest by switching units**. Contrast September 2025's handling of the same problem, where Singapore's AUI was 4.6x / 4.5 / 4.57 at three depths but always in the same unit. Coarser at the top is house style; *changing the unit* at the top is not, and it is the first thing a referee will circle.
- **Naming.** The title says neither AI nor Claude. The first paragraph splits them cleanly in two sentences — "to track how **Claude** is being used across the economy" / "to understand the economic impacts of **AI**". The bullets keep the split: measurement takes Claude ("Claude.ai usage was less concentrated", "the average economic value of work done on Claude", "Claude usage per capita"), the general claim and the stake take AI ("where and to whom the benefits of AI will accrue", "effective AI use requires complementary skills"). The one place the rule slips is "learning curves in **Claude** adoption" where the phenomenon is general — and the slip is in the right direction, because what was measured is Claude tenure.
- **Both chapter openers state a prediction before the data.** "If users are aware of this and mindful of costs and usage limits, they should bring their most complicated and valuable tasks to Opus, while selecting other models for simpler tasks. This is broadly what we observe in the data." And: "If users are calibrating to the task at hand, we should see Opus concentrated on harder, higher-value work." That is the closest thing in the corpus to a stated hypothesis with a stated confirming pattern, written in two sentences and without notation. It is the shape our pre-registered findings should be introduced with.

## Findings and their caveats

### Chapter 1, Finding 1 — concentration fell on Claude.ai, and why

> We first look at the kinds of tasks that Claude is asked to perform. We use our privacy-preserving system, which allows us to describe behavior at an aggregated level without revealing the content of individual transcripts. We sample 1 million conversations from both Claude.ai, our consumer-facing web product, and our first-party API, the developer-facing interface for integrating Claude into products and workflows.[1, Ch. 1]

> Coding remains the most common use on our platforms, with tasks associated with Computer and Mathematical occupations accounting for 35% of conversations on Claude.ai (see Appendix).[2, Ch. 1] However, between November 2025 and February 2026, use cases on Claude.ai became less concentrated: the top 10 most common O\*NET tasks went from 24% of conversations to just 19% (Figure 1.1).

> This decline in concentration partly reflects coding tasks migrating from Claude.ai to our first-party API, where Claude Code has grown to represent a large share of sampled traffic. Claude Code's agentic architecture splits coding work into smaller API calls, which are labeled as distinct tasks. So while coding's overall share of API traffic has grown, it is spread across many task categories rather than concentrated in a few. As a result, task concentration in the API remained roughly flat despite the influx of coding activity.

And the footnote that a referee reaches for:

> [2, Ch. 1] This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage.

**Annotation.** The sample is stated in the finding's own first paragraph — one million conversations from each surface, the privacy system named, both surfaces glossed — which is better placement than September 2025's footnote 2 and worth keeping. The dominant category is conceded first ("Coding remains the most common use"), then the change is given as a pair with its window attached ("between November 2025 and February 2026… from 24% of conversations to just 19%"), which is the series' standard number-pair form.

The third paragraph is the best mechanical explanation in the report and it is *deflationary about the report's own headline*: the concentration decline is partly an artefact of where coding went and of how Claude Code's architecture is counted. Four clauses do it — migration, why the architecture splits tasks, what that does to the API's category spread, and what therefore happened to API concentration. A measurement artefact explained as a fact about the product, in plain words, immediately after the number it qualifies. That is the placement rule this corpus keeps arguing for.

The caveat that is *not* placed beside its number is footnote 2: the occupational share is computed on a **different O\*NET vintage** from the reports it is being compared with. September 2025 met the same problem with its classifier (Sonnet 3.7 vs Sonnet 4) and answered it — reran the data on the old instrument, reported the direction, reported the 4-point level discrepancy. Here the instrument change is disclosed in eleven words and never assessed. Every time comparison in Chapter 1 sits on top of it.

### Chapter 1, Finding 2 — the use-case mix, with a seasonal confound decomposed

> This migration of code out of Claude.ai is not the only factor driving decreased concentration. Part of the drop is due to changes in the mix of use cases between the two periods. Coursework fell from 19% to 12% of conversations, while personal use rose from 35% to 42% of conversations. Some of the drop in coursework can be explained by academic calendars in countries where students were on winter break during our sample period.[3, Ch. 1] At the same time, increasing signups beginning around February brought more casual AI users.

> [3, Ch. 1] The drop in coursework conversations was 5 percentage points in countries where the school term was active and 12 percentage points in the countries where most students were on break.

**Annotation.** "…is not the only factor driving decreased concentration" — the paragraph opens by refusing to let the previous paragraph's explanation stand alone, which is the same self-correcting move as September 2025's "But not all API usage is for coding". Two number pairs, same window, same unit.

Then the model instance of answering a confound with a split rather than with an assurance: the seasonal threat (winter break) is named in the body, and the footnote gives the decomposition — 5pp where term was active, 12pp where it was not. The reader can see both that the confound is real and that it does not explain the whole move. **This is how a seasonality caveat should be written**, and it costs one sentence plus one footnote. Note what it does not do: it does not report the share of the sample in each group, so the reader cannot reassemble the aggregate 7pp drop from the two halves.

"increasing signups beginning around February brought more casual AI users" is the report's quietest load-bearing sentence. It is the composition change that drives the task-value finding, the personal-use finding and the low-tenure half of the entire second chapter — and the reason for the surge is disclosed only on p. 18, in footnote 3 of the *other* chapter ("Our sampling period overlapped with the release of our Super Bowl advertisements, which brought many first-time users"). The cause and the consequence are eleven pages apart and are never joined.

### Chapter 1, Finding 3 — coverage barely moved

> While the spread of Claude's work tasks became more diverse, almost all of these had been seen before in our data. In our previous report, we noted that 49% of jobs had seen at least a quarter of their tasks performed using Claude. In this data pull, that cumulative estimate barely changed (Appendix Figure A.2). Our data from this report showed many fewer novel O\*NET tasks than in our previous report.

**Annotation.** A null reported as a finding, in four sentences, with the previous wave's number restated so the null has something to be null against. "barely changed" carries no number and needs none, because the level is given and the exhibit is pointed at. Note the concession-first construction ("While the spread… became more diverse") that stops the null from reading as a contradiction of Finding 1: the mix diversified *within* a task set that was already observed. The one weakness is that the exhibit is in the appendix, so the sentence cannot be checked inside the document.

### Chapter 1, Finding 4 — augmentation rose slightly

> Since our first report, we have classified conversations into one of five interaction types—directive, feedback loop, task iteration, validation, and learning—which we group into two broader categories: automation and augmentation.[4, Ch. 1] Figure 1.3 shows that augmentation in Claude.ai increased slightly. This was driven by small bumps in validation and learning patterns. In Appendix Figure A.3, we show that automation decreased sharply in the 1P API data.

**Annotation.** The taxonomy is listed in full (five types, two groups) and its definition exported to the appendix. Then three sentences, each with a magnitude word and no number: "increased slightly", "small bumps", "decreased sharply". The values are printed inside Figure 1.3 and are not in prose anywhere. So the report's headline claim from the Introduction — "the rate of augmentation… increased slightly in both Claude.ai and API traffic" — is supported in the body by adjectives plus a chart, and the sharper of the two moves ("decreased sharply") is in an appendix exhibit. **For our own posts this is the failure mode to avoid: a magnitude word is not a finding, and a number that lives only inside an image cannot be cited.** Compare September 2025's treatment of the same measure, which gave 27% → 39% in prose and put the crossing in a sentence.

Also note the reversal being reported without comment: augmentation rising on Claude.ai after three waves of automation rising is, on the series' own terms, a turn in the headline trend — and it is given "increased slightly" and moved past. The Discussion does not mention it either. Where September 2025 wrote "This is the first report where automation usage exceeds augmentation usage", this report declines the comparable sentence.

### Chapter 1, Finding 5 — the platform migration, and what it is said to imply

> Our API platform continued to gain a relatively higher share of Computer and Mathematical tasks (usage shares by job categories are shown in the Appendix). Since August 2025, the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai. As we note in our report on labor market impacts, we expect that this migration from Claude.ai to the API may signal more imminent transformation of work for the associated jobs. The increase in tasks associated with Management occupations in Claude.ai, which went from 3% to 5% of its traffic, comes from a mix of both analytical tasks (e.g., preparing an investment memo) and responding to customer questions.

**Annotation.** Two numbers in **relative** terms ("increased by 14%… decreased by 18%") sitting one sentence away from two in **levels** ("from 3% to 5% of its traffic"), with nothing marking the switch. A reader cannot tell without the appendix whether the 14% is 14 percent of a share or 14 percentage points. This is the report's recurring unit problem and it is worth stating as a rule for us: **within a paragraph, one unit; where the unit changes, say so in the same sentence.**

The inference is properly fenced — "we expect that this migration… **may signal** more imminent transformation of work for the associated jobs", with the concept borrowed from a named companion paper rather than argued here. And the Management move is given a mechanism in the same sentence as the number, with two concrete examples, one of which ("responding to customer questions") cuts against the "analytical" reading. Naming the less flattering half of your own composition change is cheap and buys a lot.

### Chapter 1, Finding 6 — the average value of a task, in dollars

> Another way to measure the change in the mix of tasks done on Claude is to look at the change in the average value of tasks, which we define as the average hourly wage of US workers who perform that task (Figure 1.4).[5, Ch. 1] This estimate of the value of tasks in Claude.ai has dropped slightly from $49.3 to $47.9, mostly due to an increase in simple factual questions (e.g., sports outcomes, weather) and a decrease in coding as it shifts to the API. As noted in our previous report, the tasks we see on Claude tend to require higher levels of education. The plot shows that these tasks also tend to earn higher wages.

> [5, Ch. 1] For example, the task "Compute moisture or salt content, percentages of ingredients, formulas, or other product factors, using mathematical and chemical procedures." is done only by Food Science Technicians, who have an average wage of $26.15, so this is the value of that task. The data source for this exercise is the May 2024 BLS Occupational Employment and Wage Statistics (OEWS) Tables. When multiple workers do the same task, we average their wages weighting by employment and the fraction of time spent on that task.

**Annotation.** The construct is defined in the sentence that introduces it ("which we define as the average hourly wage of US workers who perform that task"), the change is given as a pair in the unit a reader already understands (dollars per hour), and the mechanism is attached to the same sentence with two examples. "dropped slightly" plus "$49.3 to $47.9" is the right pairing: the adjective sizes the move so the reader does not over-read 1.4 dollars.

Footnote 5 is the best methodological footnote in the report and the model for defining a constructed quantity: **one worked example with a real task string and a real wage**, the exact external source with its vintage ("May 2024 BLS Occupational Employment and Wage Statistics (OEWS) Tables"), and the aggregation rule for the many-to-many case ("we average their wages weighting by employment and the fraction of time spent on that task"). A reader could rebuild the measure from this footnote. That is the standard.

What the footnote does not give, and what the caption does not either, is the weighting across conversations; the words "volume-weighted" appear only in Figure 1.4's in-image axis label. A construct whose weighting is visible only inside a chart is a construct a reader cannot reproduce.

### Chapter 1, Finding 7 — the primitives all move the same way, except one

> While slight, changes in several primitives between the previous and current report capture similar declines in task complexity on Claude.ai. The average years of education required for the human inputs declined from 12.2 to 11.9 years, users granted more autonomy to the AI, and the time required for the human to do the task alone fell by about 2 minutes. One change goes ostensibly in the opposite direction: the tasks performed by Claude were judged to be slightly less possible for a human without access to AI.

**Annotation.** Four primitives in one sentence, three with their direction and one with its magnitude rounded to the unit that matters ("fell by about 2 minutes"), then a separate sentence for the one that disagrees. **Reporting the primitive that points the other way, in its own sentence, flagged with "ostensibly", is the finding's own counterweight** and the thing that makes the composite claim ("similar declines in task complexity") credible. Contrast a draft that reports three of four.

"users granted more autonomy to the AI" is offered as part of a *decline in complexity*, which is at least arguable — more autonomy is elsewhere in the series a sign of more delegation, not of simpler work — and the report does not defend the grouping. Table 1.1 gives the autonomy move as +0.02 on a 1–5 scale; it is the only one of the four primitives in this sentence that the prose describes without a number.

### Chapter 1, Finding 8 — two API workflows that doubled

> As tasks migrate to the API, they may become more exposed to automation. API workflows are far more likely to be directive, with less need for a human in the loop. In a previous report, we highlighted that customer service tasks, including, for example, automated support for payment and billing issues, are prevalent in the API data. These contributed to a higher observed exposure for Customer Service Representatives—Claude was recorded doing a high share of their tasks in automated workflows, so these jobs may be more likely to change as AI diffuses.

> We highlight two API workflows that appeared more frequently in February as compared to three months prior, with their shares at least doubling in our latest sample:[6, Ch. 1]
>
> - **Business sales & outreach automation:** sales enablement generation, B2B lead qualification research, customer data enrichment, cold-email drafting.
> - **Automated trading & market ops:** monitor markets or positions, propose specific investments, inform traders of market conditions, and related tasks.

> [6, Ch. 1] To find the emerging patterns, we filtered for O\*NET tasks that (i) appeared at least 300 times in the current data and (ii) showed at least 2x growth compared to the previous report.

**Annotation.** A qualitative finding written so that it cannot be over-read: the selection rule is stated in the body ("appeared more frequently… with their shares at least doubling in our latest sample") and the exact filter — a count floor and a growth threshold, numbered (i) and (ii) — is in the footnote. No share is quoted for either workflow, so the reader gets the direction and the membership without a magnitude that would suggest more precision than a screen can give. **A screened list needs its screen; give both criteria and the floor.**

The two bullets are lists of concrete task strings, no adjectives. The reader is left to notice for themselves that "propose specific investments" and "cold-email drafting" are the kinds of automation that attract regulators — the report does not editorialise, and the restraint is what makes the bullets land.

The observed-exposure paragraph is careful in a way worth copying: "**Claude was recorded doing** a high share of their tasks in automated workflows, **so these jobs may be** more likely to change as AI diffuses". The measurement is stated in the passive with the verb of record, and the labour-market implication is stated as a possibility about jobs. Observation and conjecture are in the same sentence and are separated by "so… may".

### Chapter 1, Finding 9 — convergence within the US, divergence across countries

> In our previous report, we noted that the Anthropic AI Usage Index (AUI), which adjusts usage by a geography's working-age population, was converging rapidly across US states: states with initially lower usage per capita showed faster adoption.

> The left panel of Figure 1.5 shows that this convergence continued in our most recent data, but at a slower pace. From August 2025 to February 2026, the share of per-person usage going to the top five states has decreased from 30 to 24%. The Gini coefficient has fallen since August 2025, though the pace of convergence has slowed. When we update our estimates from the previous report, we find that at this rate states would arrive at roughly equal usage per capita in 5-9 years, rather than 2-5.[7, Ch. 1]

> Across countries (right panel), the pattern is reversed: usage has become slightly more concentrated, with the Gini rising over the same period. The countries using Claude the most (per capita) now account for a larger share of overall usage, with the top 20 countries going from 45% to 48% of usage adjusted for population.

> [7, Ch. 1] The range is given to reflect the different estimates from running the model in our previous report with (5 years) or without (9 years) weights.

**Annotation.** The construct is re-glossed in its first appearance even though it is four reports old ("the Anthropic AI Usage Index (AUI), which adjusts usage by a geography's working-age population"), and the previous report's claim is restated before being revised. Then the two geographies are given opposite signs in adjacent paragraphs — "this convergence continued… but at a slower pace" against "the pattern is reversed" — with the same measure, the same window and the same exhibit. **One claim measured at two levels, pointing two ways, reported in two paragraphs: the cleanest instance of the house rule in this report.**

The revision of the horizon is the most honest sentence in the document: "at this rate states would arrive at roughly equal usage per capita in **5-9 years, rather than 2-5**". A published extrapolation is doubled in the open, in the same construction as the original, and the footnote says exactly where the range comes from (weighted vs unweighted). See `## Comparisons`.

The Gini is asserted twice ("has fallen", "rising over the same period") and its values are printed only inside Figure 1.5's legend. Again: the statistic the sentence rests on is not in the sentence. The fix costs six characters.

### Chapter 2, Finding 1 — Opus is chosen for higher-wage domains

> The different Claude model classes (Haiku, Sonnet, and Opus) offer tradeoffs in terms of cost, speed, and performance. The Opus class of models uses the most tokens and excels at complex tasks, but at a higher per-token price on our API. If users are aware of this and mindful of costs and usage limits, they should bring their most complicated and valuable tasks to Opus, while selecting other models for simpler tasks. This is broadly what we observe in the data.

> Figure 2.1 below shows that, for paid Claude.ai accounts, which have access to all model classes, 55% of Computer and Mathematical tasks (like coding software) use Opus, compared to 45% of Educational tasks. Technical users may notice performance gains and actively switch away from Sonnet, the default. Or efficiency-minded users may learn to use Sonnet for simpler tasks to avoid hitting usage limits. Relatedly, the differences here could reflect that most educational tasks are already fairly easy for Sonnet, or that students are more likely to be mindful of usage limits.

**Annotation.** Prediction, then confirmation, then four candidate mechanisms and no choice among them. The prediction is derived from a price and a constraint the reader can verify ("a higher per-token price on our API", "usage limits"); the confirmation is hedged at the level of the whole claim rather than per-number ("This is **broadly** what we observe"); the sample restriction that makes the comparison meaningful is inside the sentence carrying the numbers ("for paid Claude.ai accounts, **which have access to all model classes**") — a restriction stated *with its reason*, which is the September 2025 caption discipline applied in prose.

Then the mechanism paragraph: "Technical users may notice performance gains…"; "Or efficiency-minded users may learn to…"; "the differences here could reflect that most educational tasks are already fairly easy for Sonnet, or that students are more likely to be mindful of usage limits." Four channels, two of them about capability demand and two about rationing, none tested, none ranked — the *confluence* device from September 2025 in a shorter form. Note that two of the four would make the finding *not* about task-model matching at all: if students are conserving their quota, the pattern is about budget constraints, not about calibrating intelligence to difficulty. The report puts the rival reading of its own finding in the same paragraph as the finding and does not resolve it. That is the right instinct; a stronger version would say which of the four the data could distinguish.

Two things the summary does that the body does not support. The Introduction's "Opus is used 4 percentage points more than average for coding tasks and **7 percentage points less than average for tutoring-related tasks**": the +4 corresponds to the caption's "+4.4pp" for Computer and Mathematical, but **no body sentence or caption anywhere gives the -7**, whose only home is a bar label inside Figure 2.1. And the category is renamed: the exhibit's leftmost group is "Educational instruction and library", which the summary calls "tutoring-related tasks". A number and a category that exist only in the summary and the image.

### Chapter 2, Finding 2 — the wage gradient in model choice, and the API is steeper

> Figure 2.2 below shows this in a more granular way. When users perform tasks associated with higher-paid jobs, they use Opus more often. For example, on Claude.ai, 34% of Software Developer tasks involve Opus compared to just 12% of Tutor tasks. Overall, for every additional $10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points for Claude.ai users. The 1P API traffic shows much more response to the complexity of the task. Its slope is about twice as large, with the Opus share increasing 2.8 percentage points for every $10 in task value. Users deploying programmatic workflows may have more reason to switch between models compared to web users.

**Annotation.** The claim from Finding 1 tested at a second level — occupations instead of occupational domains — and then at a second sample (API against Claude.ai), with the comparison given three ways in three sentences: a named-occupation contrast ("34% of Software Developer tasks… compared to just 12% of Tutor tasks"), a slope in decision units ("for every additional \$10 of hourly wage… 1.5 percentage points"), and the ratio of the two slopes ("about twice as large"). **Stating a slope per \$10 rather than per dollar or per log point is the move that makes an elasticity legible**, and giving the ratio before the second coefficient means the reader knows what to do with 2.8 before reading it.

The interpretation is one sentence, hedged, and is about *opportunity* rather than sophistication ("may have more reason to switch between models compared to web users") — the same restraint as September 2025's capabilities-over-product-surface reading.

Two referee points. The sentence "The 1P API traffic shows much more response to **the complexity of the task**" swaps the running variable: everything measured here is the wage of the associated occupation, and complexity is a different construct which the report elsewhere measures with primitives. Wage is being used as a proxy for complexity without the proxy being declared — compare September 2025's "output length does not capture all dimensions of task complexity, but it appears to be a sensible, easily measured proxy", which declares it in one sentence. And Figure 2.1's sample is restricted to paid accounts while Figure 2.2's caption says only "Claude.ai users"; whether the 34%/12% pair and the 1.5pp slope carry the same restriction is not stated, and the two exhibits' Opus shares are not on the same footing without it.

### Chapter 2, Finding 3 — the tenure table

> Table 2.1 shows differences between low tenure and high tenure users, where the latter group is defined as having signed up for Claude at least 6 months ago and the low tenure users are everyone else.[2, Ch. 2] High tenure users are more likely to use Claude to iterate on their work, and much less likely to delegate greater responsibility through directive use patterns. They are 7 percentage points more likely to be using Claude for work, and use Claude for tasks that tend to require higher levels of education. Finally, their usage is less concentrated in certain tasks. The top 10 O\*NET tasks account for a slightly lower (20.7% compared to 22.2%) share of usage for the high tenure group.

> [2, Ch. 2] These results are similar however we define high tenure.

The table itself (PDF text; the web page renders it as an image):

> Transcript characteristics by tenure
>
> | Category | Low tenure | High tenure | Difference |
> |---|---|---|---|
> | **Share of conversations** | | | |
> | **Collaboration mode** | | | |
> | directive | 38.1% | 29.4% | ▼ -8.7 pp |
> | feedback loop | 11.7% | 12.1% | ▲ +0.5 pp |
> | task iteration | 24.5% | 28.2% | ▲ +3.6 pp |
> | validation | 4.4% | 5.6% | ▲ +1.3 pp |
> | learning | 21.3% | 24.7% | ▲ +3.4 pp |
> | **Use case** | | | |
> | work | 41.6% | 48.9% | ▲ +7.3 pp |
> | personal | 44.3% | 40.3% | ▼ -4.0 pp |
> | coursework | 14.1% | 10.8% | ▼ -3.3 pp |
> | Task success rate | 66.7% | 73.1% | ▲ +6.4 pp |
> | Top 10 tasks' share of usage | 22.2% | 20.7% | ▼ -1.6 pp |
> | **Numeric facets (mean)** | | | |
> | AI autonomy (1-5) | 3.42 | 3.40 | ▼ -0.6% |
> | Human education (yr) | 11.5 | 12.3 | ▲ +6.6% |
> | AI education (yr) | 11.7 | 12.4 | ▲ +6.0% |

**Annotation.** The cut is defined in the sentence that introduces the table, including what the residual group is ("the low tenure users are everyone else") — a small thing that stops a reader assuming a symmetric split. The prose then reads the table selectively and in the order of the argument, not the order of the rows: collaboration mode first (because it is the claim the Discussion will use to retract an earlier hypothesis), then work share with its number, then education without one, then concentration with a parenthetical pair. **Reading three rows out of thirteen and saying which way the rest point is how a table is used rather than recited.**

The table's own conventions are worth copying: two-level row grouping, a Difference column whose direction is carried by a glyph (▼/▲) as well as a sign, percentage-point differences for shares and **percent** differences for the numeric facets, and units in the row label where the unit is not obvious ("AI autonomy (1-5)", "Human education (yr)"). Mixing pp and % in one Difference column is defensible here only because the row labels carry the units; it is also the origin of the Introduction's unit switch.

What the table does not have is any measure of uncertainty — no N, no standard error, no significance marker, nothing — while Table 1.1, whose differences are much smaller, carries p-values in its caption. Two tables in one report with two different standards of evidence.

And footnote 2 is the weakest caveat in the document: "These results are similar however we define high tenure." No alternative definition is named, no number is given, and the sentence cannot be checked. Compare September 2025's classifier footnote, which named the alternative instrument and reported the 45%-versus-49% discrepancy. **A robustness claim with no alternative and no number is an assertion.**

### Chapter 2, Finding 4 — the tenure gradient, and the report's own best caveat

> Below, we dig more into two of the primitives discussed above: the human years of schooling associated with each conversation, and the share of transcripts devoted to personal use.

> In the panel on the left, we show that the years of schooling needed to understand the human prompt increases by almost 1 year for every additional year of Claude usage. In the panel on the right, we show that at the same time, personal use decreases: people who signed up a year ago devote 38% of their conversations to personal use cases, compared to 44% for the newest users.

> Several factors could account for these patterns in the user base of a rapidly advancing all-purpose technology. The high-tenure users are self-selected and the differences here could reflect stable characteristics. They may be computer programmers, for example, who were more likely to be early adopters. Further, there's an inherent survivorship bias: people who signed up a year before our data pull may be seeing positive results from their usage. We do not observe people who signed up a year ago but are no longer using Claude.

> The findings mirror what we saw in our Economic Primitives report: lower income, less educated countries paradoxically showing more complex use in some cases. The earliest adopters often have high-value, technical use cases. In poorer countries with much lower adoption, these early adopters still dominate the user base.

> More casual usage emerges when AI has diffused to a broader share of the population. Indeed, among request clusters, tasks with highest mean tenure included: AI research, git operations, revising manuscripts, and startup fundraising. The tasks with the lowest average tenure have more simple workflows like writing haikus, checking sports scores, and suggesting food for a party.[3, Ch. 2]

> [3, Ch. 2] Our sampling period overlapped with the release of our Super Bowl advertisements, which brought many first-time users.

**Annotation.** The self-selection paragraph is **the best-placed caveat in the corpus**. It is in the body, it is the paragraph immediately after the exhibit, it is unprompted, it names two distinct threats by their technical names (selection on stable characteristics; survivorship), it gives a concrete instance of the first ("They may be computer programmers"), and it ends on the sentence that states what the data cannot contain: "**We do not observe people who signed up a year ago but are no longer using Claude.**" One sentence of the form *we do not observe X* does more for a reader's trust than a page of hedging, and it is the sentence our limitations sections should be built around.

The cross-report echo — "lower income, less educated countries paradoxically showing more complex use in some cases" — uses the series' own earlier anomaly as corroboration for the selection story rather than as a finding, which is a legitimate and underused move: *the same pattern appears where we have an independent reason to think the user base is early-adopter-dominated, so selection is probably part of what we are seeing here too.* "paradoxically" flags that the pattern reads oddly on its own.

The tenure-ranked task lists are the report's one vivid comparison, and they are built the September 2025 way: concrete, slightly absurd at the low end ("writing haikus, checking sports scores, and suggesting food for a party") against the technical high end ("AI research, git operations, revising manuscripts, and startup fundraising"). No shares, no ranks, just membership — which is all a list of clusters can honestly carry.

Footnote 3 is the caveat that should not have been a footnote. An advertising campaign that "brought many first-time users" during the sample week means the low-tenure comparison group is unusually casual for a reason that has nothing to do with tenure, which is precisely the direction that inflates every difference in Table 2.1 and every coefficient in Figure 2.4. The report discloses the fact and never joins it to the finding. **In our own posts this sits beside the finding, with its direction stated.**

The slope in the second paragraph — "increases by almost 1 year for every additional year of Claude usage" — is read off a binned scatter, with no coefficient, no interval and no sample reported. The figure is described in its caption as two binned scatterplots; it carries no fitted line in prose. A slope claimed from a binned scatter is a visual inference, and the September 2025 device for marking that ("Figure 2.7 suggests that…") would have cost nothing here.

### Chapter 2, Finding 5 — the specification ladder

> We explore these relationships more in Figure 2.4 below, using the log-level data to control granularly for features of the conversation. In the top panel, specification (1) shows a simple bivariate regression with task success as the outcome and the long-tenure indicator as the predictor. Success is Claude's assessment of whether the conversation was successful, described in our previous report. The plot shows that long-tenure users are about 5 percentage points more likely to have a successful conversation.

> This could reflect that higher tenure users are better at prompting. But what if it reflects that they bring different tasks to Claude—ones more likely to be successful?

> In specification (2), we include fixed effects for specific O\*NET tasks and request clusters. This amounts to comparing high- and low-tenure users within the same narrowly defined task, rather than across tasks. For instance, we have a request cluster called "Perform corporate financial analysis, valuation, and modeling for specific companies." The fixed effects compare high- and low-tenure users within that cluster, and likewise within every other cluster. We would only observe a positive coefficient if, on average, long-tenure users are more successful in these within-task comparisons. This control moderates the effect somewhat, bringing it closer to 3 percentage points.

> Finally, we ask whether this relationship is affected by higher tenure users selecting different models, communicating in different languages, having different use cases, or signing on in different countries. This regression yields a slightly higher impact of high tenure, suggesting a 4 percentage point higher success rate accounting for the full controls.

> These results suggest that high-tenure users have more success in their Claude conversations, and that this is not due to simple factors like language or the task being performed. One intriguing potential explanation is that these users have better learned to extract what they want from AI. Facility with these platforms may be a key determinant of success that appears to scale with experience.

> [1, Ch. 2] In this analysis, we use log-level data to estimate the models with the same privacy thresholds. See the Appendix for more on the methodology.

**Annotation.** The best-argued passage in the report, and the one to imitate when a finding is a sequence of specifications.

Four things it does. (i) **The outcome's provenance is stated in the same sentence it is first used**: "Success is Claude's assessment of whether the conversation was successful" — the measure is a model judgement, and the report says so plainly rather than treating success as observed. (ii) **The threat is posed as a question, in the reader's voice, in its own two-sentence paragraph**: "But what if it reflects that they bring different tasks to Claude—ones more likely to be successful?" That paragraph is the hinge of the chapter and it contains no numbers. (iii) **The fixed effect is explained by what it compares, not by what it absorbs**, and then made concrete with a real cluster name: "This amounts to comparing high- and low-tenure users within the same narrowly defined task… For instance, we have a request cluster called 'Perform corporate financial analysis, valuation, and modeling for specific companies.'" (iv) **The falsification condition is stated before the result**: "We would only observe a positive coefficient if, on average, long-tenure users are more successful in these within-task comparisons." A sentence that says what would have to be true for the number to appear is worth more than the number.

The coefficients are reported with deliberately coarse precision and with the direction of movement named — "about 5", "moderates the effect somewhat, bringing it closer to 3", "a slightly higher impact… suggesting a 4 percentage point higher success rate". The ladder is not presented as increasing certainty; the middle rung is the lowest estimate, and the report says so. That is honest reporting of a non-monotone specification chart.

What is missing is what the ladder cannot do, stated as such. The controls are task, cluster, model, use case and country; the confounds the report itself has already named — self-selection on stable characteristics, survivorship, and a week of advertising-driven signups — are none of them addressable by those fixed effects, and the closing sentence ("this is not due to simple factors like language or the task being performed") is scoped correctly while the chapter's last two sentences drift towards the causal reading ("these users have better learned to extract what they want from AI"). The Discussion pulls it back. In a post of ours, the pull-back belongs here, in the same section.

Note "log-level data", used three times and never glossed: it means conversation-log level, not logarithms. A term that can be read two ways in a quantitative paragraph needs four words of gloss the first time.

### The report's hedge vocabulary, graded

In descending confidence, collected from the passages above: *we find* · *we document* · *we show* · *the plot shows* · *we see* · *These results suggest* · *is consistent with* · *appear linked to* · *may signal* · *could reflect* · *may reflect* · *might* · *one intriguing potential explanation* · *ostensibly* · *paradoxically* · *broadly what we observe*. The report never uses *proves*, *demonstrates* or *causes*; the one bare causal verb is licensed by an adverb ("caused, mechanically"). Two rungs are occasionally stacked on one claim in the summary bullets ("While this could reflect… it could also be evidence of…"), which is the fork construction rather than a double hedge.

Compared with September 2025, two rungs are missing: there is no "we suspect", no "we speculate" and no "more research is needed here". Their replacement is a full paragraph of alternative interpretation in the Discussion, which is a better instrument.

### Claude versus AI across the whole report

- **Title:** "Learning curves" — neither word.
- **Chapter titles:** "What has changed since our last report"; "**Learning to use AI**". Section headings: "Diversification of use cases in **Claude.ai**", "Emergent automation patterns", "Revisiting geographic convergence", "Model selection", "Learning curves", "Experience effects".
- **First paragraph, split across two sentences:** "to track how **Claude** is being used across the economy" / "to understand the economic impacts of **AI**".
- **Inside one bullet:** "the average economic value of work done on **Claude**… has decreased slightly" beside "brought more casual **AI** users" a page later; "effective **AI** use requires complementary skills" beside "learning curves in **Claude** adoption".
- **Constructs:** the *Anthropic **AI** Usage Index*, again defined over Claude usage; "**AI** autonomy (1-5)" and "**AI** education (yr)" as the names of primitives measured on Claude transcripts.
- **Captions:** eight of the eleven say Claude, Claude.ai or 1P API (Figures 1.1–1.4, 2.1, 2.2; Tables 1.1, 2.1); three say neither word (Figure 1.5, which names the index instead; Figures 2.3 and 2.4, which name the variables instead). The one **in-image** chart title that says AI is Figure 1.5's, "Geographic convergence of **AI** usage" — plotting the AUI, i.e. Claude usage per working-age capita.
- **Discussion:** "how **Claude** is used"; "the more time one spends using **AI**, the more effective one becomes at harnessing it"; "**AI**-driven disruption"; "most aided by **AI**".

The rule holds where it matters — **the phenomenon, the stake and the mechanism say AI; the sample, the shares, the wages and the tenure say Claude** — and the one soft spot is the in-image title of Figure 1.5, where a quantity that is entirely Claude usage is labelled AI usage. That is the mistake to watch for in our own captions.

## Comparisons

### Against its own earlier waves

> This latest report studies Claude usage in February 2026, building on the economic primitives framework introduced in our previous report (which used data from November 2025). Our sample covers February 5 to February 12, three months following the release of Claude Opus 4.5 and coincident with the release of Claude Opus 4.6.

> the top 10 tasks made up 19% of all traffic in February, down from 24% in November

> Coursework fell from 19% to 12% of conversations, while personal use rose from 35% to 42% of conversations.

> Since August 2025, the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai.

> This estimate of the value of tasks in Claude.ai has dropped slightly from $49.3 to $47.9

> The average years of education required for the human inputs declined from 12.2 to 11.9 years

> the top 20 countries going from 45% to 48% of usage adjusted for population

> Since August 2025, 1P API usage has become more concentrated, with the top 10 O\*NET tasks now accounting for 33% of traffic, up from 28%.

**Annotation.** The V1/V2/V3 notation of the earlier reports is **gone**: every comparison is by calendar date ("in February, down from 24% in November", "Since August 2025", "between November 2025 and February 2026"), and the in-image axes label the waves by month. That is a real improvement — a wave label is a notation the reader has to learn, a month is not — and it costs the series the ability to say "V1 to V3" in one breath.

The window is always attached, in one of two forms: either both dates in the sentence, or a "since" clause. Two exceptions, and both matter: "decreased from 40% to 38% **since our last report**" in the Introduction, where the reader must go to p. 2 to learn that the last report measured November 2025; and the paired-but-unmarked units in "increased by 14%… decreased by 18%" against "from 3% to 5%".

The comparison the report declines to make is the one September 2025 made its headline: augmentation has now risen for the first time after three waves of automation rising, and no sentence marks the turn.

### Tenure cohorts

> Table 2.1 shows differences between low tenure and high tenure users, where the latter group is defined as having signed up for Claude at least 6 months ago and the low tenure users are everyone else.

> They are 7 percentage points more likely to be using Claude for work

> The top 10 O\*NET tasks account for a slightly lower (20.7% compared to 22.2%) share of usage for the high tenure group.

> people who signed up a year ago devote 38% of their conversations to personal use cases, compared to 44% for the newest users

> the years of schooling needed to understand the human prompt increases by almost 1 year for every additional year of Claude usage

> tasks with highest mean tenure included: AI research, git operations, revising manuscripts, and startup fundraising. The tasks with the lowest average tenure have more simple workflows like writing haikus, checking sports scores, and suggesting food for a party.

> long-tenure users are about 5 percentage points more likely to have a successful conversation

**Annotation.** The report's central comparison, and it is made **four different ways on purpose**: a binary split with a stated threshold (Table 2.1), a continuous gradient in days since signup (Figure 2.3), a ranking of task clusters by mean tenure (no numbers), and a regression ladder on the binary indicator (Figure 2.4). Four instruments, one claim, and each answers a different objection to the others — the binary is legible, the gradient shows it is not a threshold artefact, the cluster ranking shows it in the task content, the ladder shows it survives controls. **This is what "one claim tested at more than one level" looks like when it is done well, and it is the strongest structural thing in the report.**

What is not supplied is the cohort sizes, at any of the four levels. "High tenure" is everyone at six months or more, in a user base the report says is growing fast and was just advertised to at the Super Bowl; the share of the sample on each side of the line is never given, and it governs how much of every aggregate in Chapter 1 is a tenure-mix effect.

### Model classes

> The different Claude model classes (Haiku, Sonnet, and Opus) offer tradeoffs in terms of cost, speed, and performance. The Opus class of models uses the most tokens and excels at complex tasks, but at a higher per-token price on our API.

> 55% of Computer and Mathematical tasks (like coding software) use Opus, compared to 45% of Educational tasks

> on Claude.ai, 34% of Software Developer tasks involve Opus compared to just 12% of Tutor tasks

> for every additional $10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points for Claude.ai users

**Annotation.** A within-product comparison the series has not made before, and the reason it works is that the *price and the constraint are named first*: Opus costs more per token and consumes usage limits faster, so choosing it is a decision with a cost, so the pattern of choices is informative. That is the same identification-in-prose move as September 2025's token-pricing argument, in three sentences instead of five.

Three depths, coarsening upward: domain shares (55/45), named occupations (34/12), slope per \$10. The named-occupation pair is the memorable one and it is chosen for recognisability — software developer against tutor — exactly as September 2025 named Singapore and Canada rather than Israel.

### API against Claude.ai

> Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic.

> So while coding's overall share of API traffic has grown, it is spread across many task categories rather than concentrated in a few. As a result, task concentration in the API remained roughly flat despite the influx of coding activity.

> In Appendix Figure A.3, we show that automation decreased sharply in the 1P API data.

> Since August 2025, the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai.

> The 1P API traffic shows much more response to the complexity of the task. Its slope is about twice as large, with the Opus share increasing 2.8 percentage points for every $10 in task value.

> The average value of tasks… has declined on Claude.ai since our first report, while rising among API users. On both surfaces, users bring their most complex tasks to our more powerful model class, Opus. This inflection is stronger for API customers.

**Annotation.** The two-surface comparison is now the series' spine, and this report uses it four ways: as a *mechanism* (the concentration decline on one surface is partly a migration to the other), as a *divergence* (task value falling on one, rising on the other), as a *dose-response contrast* (the same slope, twice as steep on the API), and as a *similarity* ("On both surfaces, users bring their most complex tasks to… Opus"). The similarity is reported in the Discussion as the finding it is, with the difference stated as a modifier rather than a contradiction ("This inflection is stronger for API customers") — the September 2025 pattern of letting a same-shape result carry the general claim and the gap carry the surface-specific one.

The cost of leaning this hard on migration is that almost every Claude.ai time series in Chapter 1 has a composition explanation available, and the report supplies it for concentration and for task value but not for the primitives, the collaboration modes or the coursework share.

### Against the US labour market

> we define as the average hourly wage of US workers who perform that task

> Overall, Claude is used for high-value, complex work that is not broadly representative of the US economy.

> the tasks we see on Claude tend to require higher levels of education. The plot shows that these tasks also tend to earn higher wages. *(web page: "…tend to earn higher wages than the US national average.")*

**Annotation.** The report's only external benchmark, and in the PDF it is left to an annotation inside Figure 1.4; the web page's added clause is the better version. The Discussion's sentence — "high-value, complex work that is **not broadly representative** of the US economy" — is the representativeness caveat the series needs, written as a comparison rather than as a limitation, in one clause, in the close.

### A public revision of a published extrapolation

> When we update our estimates from the previous report, we find that at this rate states would arrive at roughly equal usage per capita in 5-9 years, rather than 2-5.

> [7, Ch. 1] The range is given to reflect the different estimates from running the model in our previous report with (5 years) or without (9 years) weights.

**Annotation.** Two reports ago the series published a convergence horizon; this report doubles it, in the same units, in one sentence, with the word "rather than" doing the whole job — no defence of the earlier estimate, no explanation of why it moved beyond "at this rate", and a footnote saying where the new range's width comes from. **The construction is exactly reusable: "we find that at this rate X would happen in [new], rather than [old]."** What is missing is the diagnosis: a reader cannot tell whether the earlier horizon was wrong or whether the world slowed down, and the report's own prose supports the second reading ("the pace of convergence has slowed") without saying so in the revision sentence.

### A public revision of a published hypothesis

> More experienced users tend to use Claude more collaboratively, for more work-related reasons, in more complex tasks, and with more success. This pushes back against a hypothesis we made last year that automated use may be more typical of more experienced, sophisticated users; instead, we find that the most advanced users are more likely to iterate with Claude.

**Annotation.** The most valuable sentence in the report for our purposes. An earlier report floated learning-by-doing as a possible driver of *rising directive use* — see the Chapter 1 fork annotated in `wiki/style/economic-index-2025-09-report.md` — and this report, having built a tenure measure, reports that the sign goes the other way and says so in the close, in the body voice, without hedging the retraction. Three features to copy: the retraction is stated as a conflict with a *hypothesis* rather than with a finding ("a hypothesis we made last year"); the verb is "pushes back against", not "refutes"; and the replacement claim is given in the same sentence ("instead, we find that the most advanced users are more likely to iterate with Claude"). One sentence, one retraction, one replacement.

It is also the clearest demonstration of why a series is worth maintaining: the hypothesis was checkable only because it had been written down, in public, with a mechanism attached.

### To economic theory

> The pattern is consistent with a standard "adoption curve" story, in which early adopters favor specific high-value uses like coding, and later adopters take on a much wider range of tasks.

> Economists have long noted the potential for skill-biased technological change: innovations that raise wages for high-skill workers while depressing them for others.

**Annotation.** Theory enters exactly twice, and both times as a **named story glossed in the same sentence** — the adoption curve with its two phases spelled out, skill-biased technological change with its distributional content spelled out ("raise wages for high-skill workers while depressing them for others"). No notation, no model, and the citation (web only) is a hyperlink on the phrase. Where September 2025 stated a theoretical prior before the data and then confirmed it, this report reaches for theory only to *interpret* results it already has. The gloss-in-the-same-sentence discipline is the transferable part: a reader who has never met the term can follow the sentence.

## Figure captions

Eleven exhibits: Figures 1.1–1.5, Table 1.1, Figures 2.1–2.4, Table 2.1.

**PDF form throughout:** **bold "Figure N.N: sentence-case title"** with **no terminal period**, then the gloss on the following line in plain roman, one or two sentences. Tables use the same form and also take no terminal period in the PDF (a change from September 2025, where table captions were the exception that *did* take a period). **Web form:** the title takes a period and the whole caption — title and gloss — is bold.

Every exhibit also carries an **in-image chart title** in small type above the plot, and the division of labour is the same as in the September 2025 report: the in-image title says *what this is*, the caption says *what it is made of*. In-image titles, panel titles, axis labels and legend entries are quoted below **marked as such**; per `room/director-2026-09-16-alt-text-ruling.md`, no number printed inside a chart image is recorded anywhere in this file.

### Chapter 1

> **Figure 1.1: Usage shares among top 10 tasks over time by platform, Claude.ai and 1P API** Share of conversations assigned to the 10 most prevalent O\*NET tasks, by platform and report version.

In-image chart title: "Share of usage in top 10 O\*NET tasks over time". Axis: "Top 10 task concentration (%)"; x-ticks by month from Jan 2025 to Feb 2026; the two series labelled "1P API" and "Claude.ai" at their right-hand ends, with a data label printed at every point. (Web gloss: "the **ten** most prevalent O\*NET tasks" — the only word that differs between the two versions.)

**Annotation.** Descriptive title, one-sentence gloss, and the gloss does exactly two jobs: the unit of observation ("Share of conversations assigned to…") and the two dimensions of the panel ("by platform and report version"). No sample, no floor, no N, no privacy note — and this is the exhibit the Discussion's two otherwise-unsupported numbers come from. Compare September 2025's Figure 1.1, whose four-element caption carried the panel ordering rule and an interpretation sentence. The template has been stripped, and the cost is visible: **a caption with no sample line cannot be lifted, and a series labelled only inside the image cannot be cited.**

> **Figure 1.2: Work, personal, and coursework usage on Claude.ai in November 2025 and February 2026** Share of conversations identified as work, personal, or coursework related on Claude.ai.

In-image chart title: "Claude.ai use case composition over time". Axis: "Share of conversations (%)"; two date groups, three series labelled "Work", "Personal", "Coursework" at their right-hand ends with a data label at each point.

**Annotation.** Title names the three categories and both dates; gloss restates the unit and adds the word that matters — "identified as", which concedes that the category is assigned by a classifier rather than observed. Three shares that do not sum to 100 and no residual category named, in either the caption or the body. September 2025's Figure 3.6 caption disclosed its residual in one clause ("'All Other' combines remaining occupational groups into a single category"); one clause would have done it here.

> **Figure 1.3: Collaboration mode share, Claude.ai** Collaboration mode frequencies across Anthropic Economic Index Reports in Claude.ai.

In-image chart title: "Automation vs. augmentation over time (Claude.ai)". Axis: "Percentage"; series labelled "Augmentation" and "Automation"; and — the part worth copying — a **definition line printed under the x-axis**: "Automation = directive + feedback loop    Augmentation = validation + task iteration + learning".

**Annotation.** The shortest caption in the report: a title that is a label and a gloss that is a paraphrase of the title. Everything a reader needs to interpret the two series — that they are built by summing three named interaction types against two — is **inside the image**, printed under the axis. That placement is good design and bad citation practice: the composition rule travels with the picture but not with the text, and the caption could have carried it in eleven words. The body's claims about this exhibit ("increased slightly", "small bumps in validation and learning") are the ones with no numbers in prose.

> **Figure 1.4: Shifts in the average task value across version and platform** This plot uses the O\*NET framework to estimate the dollar value of tasks performed on Claude.ai and the 1P API. Task value is estimated as the average hourly wage paid to workers who do that task.

In-image chart title: "Average task value over time". Axis: "Volume-weighted mean wage (Feb 2026 \$/hr)"; two series labelled "1P API" and "Claude.ai" with a data label at each point; a horizontal reference line annotated "US avg. hourly wage".

**Annotation.** The construct is defined in the caption, in the caption's own sentence, in words a reader can check against the footnote — "Task value is estimated as the average hourly wage paid to workers who do that task" — and the verb is "estimate" twice. This is the report's best caption and the only one that would survive being lifted.

Two things live only in the image and should not: the **weighting** ("Volume-weighted", a word that appears nowhere in the prose or the caption, and which determines what the series means), and the **US average wage reference line**, which is the exhibit's whole point of comparison. The web page's added clause ("than the US national average") repairs the second in prose; nothing repairs the first. The currency base ("Feb 2026 \$/hr") is also image-only, which matters for a series running from January 2025.

> **Table 1.1: Changes in key primitives** This table shows average primitives in Claude.ai compared to the previous Economic Index report. All differences are statistically significant with p<0.001, except Human-only time with p<0.05. See the Appendix for definitions of these primitives.

Table title above the table: "Shifts in primitives, Nov 2025 and Feb 2026". Columns: "Nov 2025", "Feb 2026", "Difference"; rows "Human education (yr)", "AI autonomy (1 – 5)", "Human time (min)", "Human and AI time (min)", "Human can't do alone (%)", each Difference cell carrying a ▼ or ▲ glyph with the signed value.

**Annotation.** The only caption in the report that carries a statistical statement, and it carries it well: one sentence, all rows covered, the exception named by row with its own threshold ("except Human-only time with p<0.05"). **Stating the significance of every row in one sentence and naming the one exception is the cheapest possible way to make a table of small differences readable** — and note that it is a table of *differences the report calls slight*, so the p-values are doing the work of saying "small but not noise".

Then the third sentence sends the reader out of the document for the definitions of all five quantities. A table whose rows cannot be defined from the caption, the body or the footnotes is a table a reader must take on trust; and the row the prose leans on — autonomy — is the one whose direction is hardest to interpret without the definition. Note also that the row label in the table reads "Human-only time" nowhere: the caption's exception names a row ("Human-only time") that the table calls "Human time (min)". A caption should use the exhibit's own row labels.

> **Figure 1.5: Geographic convergence** This figure shows Lorenz curves of the Anthropic Usage Index for US states (left panel) and countries (right panel).

In-image chart title: "Geographic convergence of AI usage". Axis: "Cumulative % of AUI" against "Cumulative % of US states" (left) and "Cumulative % of countries" (right); each panel's legend lists three dated series each annotated with its Gini, plus a "Perfect equality" reference line.

**Annotation.** Two panels, one sentence, and the sentence does its minimum: what kind of curve, what index, what each panel is over. The Gini values that both of the body's claims rest on ("The Gini coefficient has fallen since August 2025"; "with the Gini rising over the same period") are in the legend inside the image and nowhere else — the most consequential instance in the report of a statistic that exists only as a picture.

Two naming slips in four lines. The caption says "Anthropic Usage Index"; the body, the previous reports and the series' own construct are the **Anthropic AI Usage Index**. And the in-image title says "AI usage" for a quantity that is Claude usage per working-age capita. A caption is the one place a construct's name must be exact.

### Chapter 2

> **Figure 2.1: Model choice and occupational domains** This plot shows how much more or less paid Claude.ai users select the Opus class of models depending on which occupational domain the task is in. In this sample, 51% of overall usage is Opus, and 55% of Computer and Mathematical usage (+4.4pp) is Opus.

In-image chart title: "Opus shares by occupation group". Axis: "Opus over/under-representation (percentage points)"; eight occupational-domain categories along the x-axis, each bar carrying a signed data label.

**Annotation.** The best-constructed caption in the chapter, for one reason: **it gives the baseline the deviations are measured against** ("In this sample, 51% of overall usage is Opus") and then works one bar in full, in both units ("55% of Computer and Mathematical usage (+4.4pp) is Opus"). An over/under-representation chart is uninterpretable without the base rate, and the base rate is in the caption rather than the image. This is the same device as September 2025's Figure 3.3 worked example, improved: the worked value teaches the reader how to read the axis *and* supplies the null.

The sample restriction is in the first sentence ("paid Claude.ai users"), where it belongs. What is not in the caption is why paid accounts only — the reason is in the body ("which have access to all model classes") and it is the reason the exhibit is valid.

> **Figure 2.2: Model choice and occupation** This plot shows how often users select the Opus class of models depending on which occupation the task is associated with. Each point is an occupation (x-axis) and its Opus share (y-axis). The left panel shows Claude.ai users, the right panel shows 1P API users.

In-image chart title: "Opus shares by occupation". Panel titles print the fitted slope per \$10/hr for each surface — to two decimal places, where the body rounds to one. Axes: "Share of conversations using Opus (%)" against "Occupation hourly wage"; four occupations labelled in each panel.

**Annotation.** Three sentences, three jobs: what is plotted, **what a point is** ("Each point is an occupation (x-axis) and its Opus share (y-axis)"), and the panel logic. Saying what a point is, in a scatter whose unit of observation is neither a conversation nor a user, is the sentence that stops the commonest misreading of this kind of exhibit; September 2025's caption template calls for it and this caption delivers it in twelve words.

Missing: the sample restriction. Figure 2.1 says "paid Claude.ai users", this one says "Claude.ai users", and nothing states whether the two Opus shares are on the same footing. Missing also: any inclusion floor for an occupation to appear as a point, and the weighting of the fitted line — September 2025 put "The regression weights every country equally" in the corresponding caption. And the slope, the exhibit's actual finding, appears in the panel titles at higher precision than in the prose, with no coefficient in the caption at all.

> **Table 2.1: Differences between high and low tenure users** This table shows average characteristics for high and low tenure users. We define high-tenure users as those who signed up for Claude at least six months before our data pull.

Table title above the table: "Transcript characteristics by tenure". Columns: "Low tenure", "High tenure", "Difference"; two-level row grouping under "Share of conversations" and "Numeric facets (mean)", with ▼/▲ glyphs in the Difference column.

**Annotation.** The caption **repeats the group definition** rather than cross-referencing the sentence three lines above it, and spells "six months" out in words where the body used the numeral — the exhibit is independently readable, which is the September 2025 discipline of repeating verbatim rather than paraphrasing. Note "before our data pull": the threshold is relative to the sample window, not to a calendar date, which is the correct and less obvious way to state it.

No N, no uncertainty, no significance statement — in the report's central exhibit, whose sibling table one chapter earlier carries p-values for every row. If two tables in one document report differences, they should report them to the same standard.

> **Figure 2.3: How tenure correlates with years of education and personal use** This figure shows two binned scatterplots. The left panel shows human education years vs. days since signup. The right panel shows the percentage of personal use conversations vs. days since signup.

In-image chart title: "Usage by tenure". Axes: "Human education years" (left) and "Personal use (%)" (right), both against "Days since signup", whose ticks are labelled 0, 6 months, 1 year, 18 months.

**Annotation.** "correlates" in the title, which is the right verb for the exhibit and is not softened anywhere else in the report's discussion of it. "two binned scatterplots" names the method in three words — and then stops: the number of bins, the binning rule, the bin sizes and whether the points are equal-count or equal-width are all absent, and the body reads a slope off the panel ("increases by almost 1 year for every additional year of Claude usage") with no fitted line, no interval and no sample. A binned scatter is a smoothing choice; a caption that names the method without its parameters lets the reader see the choice was made and not what it was.

Note the axis-label mismatch: the axis is "Days since signup" and every tick is labelled in months or years.

> **Figure 2.4: The association between experience and success** This plot shows the results from regressing our binary success measure on an indicator for high tenure, with increasingly stringent controls. The coefficient is given in percentage points, and the whiskers give 95% confidence intervals. "Task FEs" indicates fixed effects for O\*NET task and request cluster. Full controls adds model, use case, and country fixed effects.

In-image chart title: "Tenure and task success". Axis: "Effect on task success (pp)"; three rows labelled "(1) Raw", "(2) + task FE", "(3) + full controls", each a point with whiskers. (Web caption: "95 percent confidence intervals".)

**Annotation.** The longest caption in the report and the only one that fully specifies its estimate: the outcome and its type ("our binary success measure"), the regressor ("an indicator for high tenure"), the design ("with increasingly stringent controls"), the units ("The coefficient is given in percentage points"), the uncertainty ("the whiskers give 95% confidence intervals"), and then **the two control sets enumerated by name**, including the second one stated as an increment on the first ("Full controls **adds** model, use case, and country fixed effects"). That is the September 2025 Figure 3.9 standard, met.

Two notes. The word "association" is in the title, doing the work the body's hedges do; the title is the only place in the chapter where the relationship is named as an association rather than an effect, while the axis label says "Effect on task success" — the caption and the image disagree about the causal status of the same quantity, and the caption is right. And the body's sentence "In the top panel, specification (1) shows…" refers to a panel this exhibit does not have; the three specifications are rows of one coefficient plot.

### The caption template, distilled

What this report keeps from the September 2025 template, and what it drops.

**Keeps:** bold numbered title, sentence case, no terminal period (PDF); gloss in plain roman, one sentence per job; the unit of observation first; the definition of any constructed quantity restated in the caption rather than cross-referenced (Figures 1.4, 2.4; Table 2.1); the baseline or null value the reader should compare against (Figure 2.1's 51%; Figure 1.5's "Perfect equality" line); the worked example that teaches the axis (Figure 2.1); "what a point is" for a scatter (Figure 2.2); the full control set enumerated (Figure 2.4); the significance statement with its named exception (Table 1.1); and the rule that tables repeat their own group definitions (Table 2.1).

**Drops, and each drop costs something:**
1. **No sample line on any of the eleven exhibits.** No conversation counts, no observation floors, no "Free and Pro"-style coverage boundary, no privacy-threshold note. September 2025 repeated its 200-observation sentence verbatim in four captions; this report repeats nothing.
2. **No declarative finding titles.** Ten of eleven titles are descriptive labels ("Geographic convergence", "Model choice and occupation"); September 2025's dominant style was a title that stated the finding, with the hedge in the bold title where the finding was noisy. Nothing here carries a hedge in its title except Figure 2.4's "association".
3. **No coefficient in the caption** where the exhibit is a fitted relationship (Figure 2.2), and no interpretation sentence in plain words ("each 1% increase is associated with…").
4. **Load-bearing quantities left inside the image:** the Gini values (Figure 1.5), the automation/augmentation composition rule (Figure 1.3), the weighting and the currency base (Figure 1.4), the slopes (Figure 2.2), the US wage reference (Figure 1.4). Seven sentences in the report depend on them: "augmentation in Claude.ai increased slightly"; "small bumps in validation and learning patterns"; "automation decreased sharply in the 1P API data"; "The Gini coefficient has fallen since August 2025"; "with the Gini rising over the same period"; the Introduction's "7 percentage points less than average for tutoring-related tasks"; and the Discussion's "33% of traffic, up from 28%". None can be checked without reading a picture.
5. **Construct names not exact** (Figure 1.5: "Anthropic Usage Index"; in-image "AI usage" for Claude usage).

For our own posts the rule that follows is blunt: **a caption must contain the sample, the unit, the construct, the null and, where there is one, the coefficient — and no sentence in the post may depend on a number that appears only inside an image.**

## Limitations

**There is no limitations section**, and no "Caveats", "Threats to validity" or equivalent in twenty pages. This is the series' settled practice (see September 2025) and it is the practice our posts do not copy. What is different here — and better — is that the two heaviest caveats are in the **body**, adjacent to the findings they threaten, rather than in footnotes.

### 1. In the body, beside the finding

> Several factors could account for these patterns in the user base of a rapidly advancing all-purpose technology. The high-tenure users are self-selected and the differences here could reflect stable characteristics. They may be computer programmers, for example, who were more likely to be early adopters. Further, there's an inherent survivorship bias: people who signed up a year before our data pull may be seeing positive results from their usage. We do not observe people who signed up a year ago but are no longer using Claude.

> This could reflect that higher tenure users are better at prompting. But what if it reflects that they bring different tasks to Claude—ones more likely to be successful?

> These results suggest that high-tenure users have more success in their Claude conversations, and that this is not due to simple factors like language or the task being performed.

> One change goes ostensibly in the opposite direction: the tasks performed by Claude were judged to be slightly less possible for a human without access to AI.

> While the spread of Claude's work tasks became more diverse, almost all of these had been seen before in our data.

> This decline in concentration partly reflects coding tasks migrating from Claude.ai to our first-party API… As a result, task concentration in the API remained roughly flat despite the influx of coding activity.

> Some of the drop in coursework can be explained by academic calendars in countries where students were on winter break during our sample period.

### 2. In the Discussion, as an alternative interpretation

> An alternative interpretation, of course, is that these results are driven by cohort effects or survivorship bias. Early adopters could be more technical. Those who continue using Claude could be those with tasks that it is distinctly well-equipped to do. But carefully controlled regressions rule out simple versions of this confounding, like that long-tenured users bring different kinds of tasks. Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing.

> Overall, Claude is used for high-value, complex work that is not broadly representative of the US economy.

### 3. In footnotes

> [2, Ch. 1] This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage.

> [3, Ch. 1] The drop in coursework conversations was 5 percentage points in countries where the school term was active and 12 percentage points in the countries where most students were on break.

> [6, Ch. 1] To find the emerging patterns, we filtered for O\*NET tasks that (i) appeared at least 300 times in the current data and (ii) showed at least 2x growth compared to the previous report.

> [7, Ch. 1] The range is given to reflect the different estimates from running the model in our previous report with (5 years) or without (9 years) weights.

> [1, Ch. 2] In this analysis, we use log-level data to estimate the models with the same privacy thresholds. See the Appendix for more on the methodology.

> [2, Ch. 2] These results are similar however we define high tenure.

> [3, Ch. 2] Our sampling period overlapped with the release of our Super Bowl advertisements, which brought many first-time users.

### 4. In captions

Table 1.1's p-values with the named exception; Figure 2.4's 95% confidence intervals and enumerated control sets; Figure 2.1's baseline Opus share; Table 2.1's tenure definition; Figure 2.3's "binned scatterplots"; Figure 1.2's "identified as".

### 5. As deferred work

> Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing.

### Annotation

- **Placement is much better than September 2025's, in one place and one place only.** The self-selection/survivorship paragraph sits directly under the exhibit it qualifies; the "But what if…" paragraph is given its own space in the middle of the argument; the Discussion returns to both and scopes what the controls achieved ("rule out **simple versions** of this confounding"). Everywhere else in the report the dispersal is worse than September 2025's, because there are only eleven footnotes and three of them are pointers to the appendix.
- **"We do not observe people who signed up a year ago but are no longer using Claude."** The single best caveat sentence in the corpus so far. It states an absence rather than a doubt, it is checkable, and it tells the reader the exact shape of the bias without arguing about its size. Our limitations sections should be built from sentences of this form.
- **Specificity is uneven, where September 2025's was uniformly high.** The term-time decomposition (5pp vs 12pp) and the emergent-pattern filter (≥300 appearances, ≥2× growth) are as particular as anything in the corpus. Against that: "These results are similar however we define high tenure" names no alternative and gives no number; the privacy thresholds are referred to but not stated ("the same privacy thresholds"); no exhibit carries an N; the O\*NET vintage change is disclosed and not assessed; and the sample is described once, as "1 million conversations from both Claude.ai… and our first-party API", with no exclusions, no geolocation note, no unit-of-observation statement and no trust-and-safety filter mentioned — all of which September 2025 gave in footnote 2.
- **The three caveats a referee would raise first, and where they are.**
  1. **The O\*NET vintage changed between waves** (footnote 2, Ch. 1). Every Chapter 1 comparison is across instruments, and the report reports no rerun on the old vintage. September 2025 faced the identical problem with its classifier and answered it properly, discrepancy included; the regression from that standard is the most serious thing in this report.
  2. **A Super Bowl advertising campaign landed inside the sample window** (footnote 3, Ch. 2). It is disclosed in a footnote whose sentence is about task clusters, on the page before the success regression, and it is never connected to the tenure finding — although it loads the low-tenure comparison group with exactly the users who would widen every gap in Table 2.1 and every coefficient in Figure 2.4. It is also the unstated mechanism behind Chapter 1's "increasing signups beginning around February brought more casual AI users", which is the report's explanation for the drop in task value. One footnote is doing load-bearing work in two chapters and is joined to neither.
  3. **The headline tenure effect is quoted in four sizes and two units** — "a 10% higher success rate" (Introduction), ▲ +6.4 pp (Table 2.1), "about 5 percentage points" (raw regression), "closer to 3" (task fixed effects), "a 4 percentage point higher success rate" (full controls) — with the largest-sounding version in the summary and no sentence anywhere reconciling them. The reconciliation is arithmetic and would take one clause.
- **Two more a referee would reach for.** Figure 2.2's sample is not stated as paid-only while Figure 2.1's is, so the two Opus shares may not be comparable; and the Introduction's "7 percentage points less than average for tutoring-related tasks" has no counterpart in any body sentence or caption, only in a bar label, and renames the exhibit's category.
- **One threat the report identifies and then does not carry through.** It says clearly that concentration fell partly because coding migrated to the API, and that signups brought casual users. Both are composition effects. It then reports changes in the primitives, in collaboration mode, and in task value over the same window without asking how much of each is the same composition effect — even though the tenure chapter, later in the same report, shows that all three quantities differ sharply by tenure. The report contains its own decomposition and does not run it.
- **Drafting tells.** Four, and they are worth listing because they are the kind that survive into a published document when definitions and exhibits live in several places at once.
  1. **A stray editorial note is rendered into the published PDF.** On p. 15 the words "It gets rounded to 3.4 and 3.4. Needs to be 3.42 and 3.40" are typeset across the paragraph beginning "Finally, their usage is less concentrated in certain tasks", colliding with the words "The top 10 O\*NET tasks". It is a production comment about Table 2.1's AI-autonomy row — the published table does show 3.42 and 3.40, so the fix was applied to the exhibit and the note was left on the page. The web page's text is clean.
  2. **The web page's cross-reference to Figure 1.6**, which does not exist (PDF: Figure 1.5).
  3. **"In the top panel"** for Figure 2.4, which has three rows and no panels.
  4. **Table 1.1's caption names a row ("Human-only time") that the table labels "Human time (min)"**, and Figure 1.5's caption drops the "AI" from the Anthropic AI Usage Index.
- **What the report gets right about the limitations it does have.** It names its own representativeness limit in the close, as a comparison rather than an apology ("not broadly representative of the US economy"); it flags the one primitive that moves against its composite claim; and it says what would resolve its central ambiguity and when ("Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing"). A limitation that names the design that would settle it is worth three that do not.

## Close

### "Discussion", verbatim and in full

> This report revisited the core measures we use to track Claude usage, and analyzed model selection and success for the first time. Since August 2025, 1P API usage has become more concentrated, with the top 10 O\*NET tasks now accounting for 33% of traffic, up from 28%. Claude.ai tasks, on the other hand, have diversified since our November 2025 data. Faster adoption among low usage states continued in the US, though at a slower pace than in the previous report. Low adoption countries fell slightly further behind.

> With this report, we can begin to trace out how various economic primitives have changed. Coursework fell as a share of usage while personal conversations increased. We also note a slight decrease in the aggregate complexity of prompts in Claude.ai, with conversations in Claude.ai exhibiting less sophisticated inputs and shorter estimated completion times.

> Overall, Claude is used for high-value, complex work that is not broadly representative of the US economy. But as the user base has grown, less remunerated tasks have become a slightly larger share of traffic. The average value of tasks, measured as the estimated wage paid to workers in occupations associated with those tasks, has declined on Claude.ai since our first report, while rising among API users. On both surfaces, users bring their most complex tasks to our more powerful model class, Opus. This inflection is stronger for API customers.

> More experienced users tend to use Claude more collaboratively, for more work-related reasons, in more complex tasks, and with more success. This pushes back against a hypothesis we made last year that automated use may be more typical of more experienced, sophisticated users; instead, we find that the most advanced users are more likely to iterate with Claude. It's also consistent with learning-by-doing: the more time one spends using AI, the more effective one becomes at harnessing it.

> An alternative interpretation, of course, is that these results are driven by cohort effects or survivorship bias. Early adopters could be more technical. Those who continue using Claude could be those with tasks that it is distinctly well-equipped to do. But carefully controlled regressions rule out simple versions of this confounding, like that long-tenured users bring different kinds of tasks. Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing.

> These observed differences in success rates could deepen inequalities in the labor market. Economists have long noted the potential for skill-biased technological change: innovations that raise wages for high-skill workers while depressing them for others. Our analysis in this report identifies a channel through which such skill-biased transformation may already be unfolding: early adopters with high-skill tasks have more successful interactions with Claude than later, less technical adopters. These early-adopting users may simultaneously be the most exposed to AI-driven disruption and most aided by AI in these initial, augmentative waves of adoption.

### Annotation

- **What was learned.** Stated as a set of directions, not a shape. The first paragraph is four sentences of results with their windows attached ("Since August 2025…", "since our November 2025 data", "than in the previous report"); the second names what the primitives did; the third states the level and the trend together ("high-value, complex work… But as the user base has grown, less remunerated tasks have become a slightly larger share"). Compare September 2025's close, whose whole report compressed into seven words ("early AI adoption is strikingly uneven"). **This close has no such sentence**, and the absence is the difference between a close that states a finding and one that lists them. The nearest candidate is in the fourth paragraph: "the more time one spends using AI, the more effective one becomes at harnessing it."
- **Numbers in the close, and one of them is new.** September 2025's Concluding remarks contained no figures at all. This Discussion opens with two ("33% of traffic, up from 28%") and they are **the first prose appearance of either**: no body sentence and no caption gives the 1P API top-10 share, only the data labels inside Figure 1.1. A number that a reader meets for the first time in the close is a number they cannot check, and the rule to take from this is the one September 2025 followed by accident: **the close carries no numbers that the body has not already carried.**
- **Why it matters.** One paragraph, built in four moves: the stake stated as a possibility ("These observed differences in success rates **could** deepen inequalities in the labor market"), a named body of theory glossed in the same sentence ("skill-biased technological change: innovations that raise wages for high-skill workers while depressing them for others"), the report's own contribution scoped precisely to a *channel* rather than to an effect ("identifies a channel through which such skill-biased transformation **may already be unfolding**"), and then a genuinely two-sided last sentence: "These early-adopting users may simultaneously be the most exposed to AI-driven disruption and most aided by AI in these initial, augmentative waves of adoption." That final clause is the best sentence in the close — the same population is named as both the most threatened and the most helped, which is the honest reading of a finding about skill complementarity and is the opposite of a policy-ready conclusion. **A why-it-matters that ends on a tension rather than a direction is harder to write and much harder to misquote.**
- **What comes next.** One sentence, about identification rather than results: "Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing." What makes it a commitment rather than a gesture is that the mechanism is implicit and real — more waves make the tenure cross-section into a panel. There is no dataset-expansion paragraph, no list of open questions for other researchers, and no "important area for future research" sentence; the only other forward-looking line in the document is the Introduction's statement of purpose.
- **No recommendations, to anybody.** Not to policymakers, not to businesses, not to researchers. September 2025 made three (attention for policymakers, information architecture for businesses, an open dataset and four questions for researchers). This report makes none — the closest thing is the diagnostic claim that a channel exists. Given the subject, that is a defensible choice and it is also a narrowing of the series' register: a report that identifies a mechanism for widening inequality and addresses no audience has left the last step to the reader.
- **How it avoids a template.** Five devices. (i) **It retracts its own earlier hypothesis in the body of the close** — the only close in the corpus that does — and supplies the replacement in the same sentence. (ii) **It gives the rival interpretation a whole paragraph, after the finding and before the stakes**, so the strongest version of the report's story is never the last thing said about it. (iii) **Every paragraph concedes something**: "on the other hand", "though at a slower pace", "But as the user base has grown", "An alternative interpretation, of course", "rule out **simple versions**". (iv) **It states what the report did, in the first sentence, in the past tense, with the novelty scoped to a method** ("analyzed model selection and success for the first time") rather than to a result. (v) **The last sentence is a two-sided conditional about one population**, not a summary and not a call to action.
- **What it does not do, and should.** There is no paragraph that names the shape of the whole report; there is no bolded thesis sentence (September 2025 had exactly one, and it was the document's thesis about its own role); and the Discussion never mentions the one turn in the series' headline trend that this wave recorded — augmentation rising after three waves of automation rising.
- **Title against ending.** Title: "Learning curves". Ending: "It's also consistent with learning-by-doing: the more time one spends using AI, the more effective one becomes at harnessing it" and then the skill-biased channel. The concept matches exactly and the *word* does not: "learning curves" appears in the Introduction, as a preview heading and as a section heading, but **not once in the Discussion**, which says "learning-by-doing" instead. By the house test — if the ending does not contain the title's key word doing work, one of the two is wrong — this close passes on substance and misses by a synonym. One sentence using the title's own phrase would have closed the loop.
- **First person.** Throughout, and for both kinds of act: institutional ("we use our privacy-preserving data analysis system", "We sample 1 million conversations", "we have classified conversations", "we will be able to"), and analytical ("We find that", "we show", "we ask whether", "we note", "we highlight two API workflows"). Our house style forbids it. The substitutes this report already supplies in places are the ones to borrow: attribute to the exhibit ("The plot shows that long-tenure users are about 5 percentage points more likely…", "Figure 1.3 shows that augmentation in Claude.ai increased slightly"), or to the analysis ("This control moderates the effect somewhat"), or to the result ("These results suggest that…"). Note that the report's own retraction sentence is first-person twice over ("a hypothesis **we** made last year", "**we** find") — a retraction written without the first person has to name the earlier report instead, which is more precise anyway.

## Verification

- **URLs fetched, both on 2026-09-16:**
  - https://cdn.sanity.io/files/4zrzovbb/website/4053bf3440c0c85b8852052770c5b4cf882689c3.pdf — **the fetch service refuses this host** (`url_not_allowed`, confirmed by one attempt; retrying variants does not help). Retrieved instead in the sandbox with `curl -sSL`: HTTP 200, 1,343,638 bytes, 20 pages, PDF 1.7, Adobe InDesign 21.2 (Macintosh), CreationDate 2026-03-24 22:18:55 UTC. Converted with `pdftotext` (both `-layout` and default reading order) and hyperlink targets read with `pypdf`. All 20 pages returned; every exhibit present as a page render. **This is the document of record and is the source for every quotation in this file unless a quotation is explicitly marked as web-page text.**
  - https://www.anthropic.com/research/economic-index-march-2026-report — returned in full (H1 "Anthropic Economic Index report: Learning curves", dated "Mar 24, 2026"). Used to establish how the web page condenses the PDF, and to confirm the figure-reference drift, the caption typography, the footnote renumbering, the citation key and the one added clause.
- **Fetch date:** 2026-09-16. **Fetch failures: one, expected and worked around** — `web_fetch` on `cdn.sanity.io` (see above). No other failure; the web page returned complete on the first attempt.
- **Not fetched, deliberately:** both copies of the separate appendix (`f065d6e6…`, `a3cdcd9e…`), which have their own corpus slug; the January 2026 report (`096d94c1…`); the Sanity-hosted PDF that the web page's "Emergent automation patterns" anchor points to (`a42bc3fc…`), which is therefore not identified in this file; the labor-market-impacts report; the Clio post and the Clio arXiv paper; the BLS OEWS tables; the *Journal of Economic Literature* page behind "skill-biased technological change"; and the Hugging Face dataset. Nothing from any of them is quoted here. Where this file compares the report to earlier entries in the corpus it points at `wiki/style/economic-index-2025-02-report.md` and `wiki/style/economic-index-2025-09-report.md` and quotes neither.
- **Every quotation was checked back against the extracted PDF text word by word after transcription.** Confirmed for all nine sections of this file.
- **Quotation caveats.**
  - Hyperlink URLs were stripped from quoted prose and the anchor text retained; the anchors in the Introduction are listed in `## Opening move`, and the full link inventory of both versions is summarised in `## Source`.
  - Typographic apostrophes, quotation marks, em dashes and en dashes in the sources were normalised to ASCII where quoting inline; the ▼ and ▲ glyphs in Tables 1.1 and 2.1 are reproduced as they appear. No word was changed.
  - **PDF line-break hyphenation was repaired.** The extraction joins words that the PDF broke across lines without a hyphen: "tutoringrelated", "highereducation", "learning-bydoing", "lowerwage", "percapita", "lowtenure". Quotations here restore the intended spacing; the web page's text was used as a check on every one, and all six are unambiguous.
  - Footnote numbering restarts per chapter in the PDF, so quotations are labelled with their chapter, e.g. "[3, Ch. 1]", "[2, Ch. 2]". The single Introduction footnote is labelled "[1]". The web page's continuous numbering (1–11) is not used.
  - Emphasis is reproduced as it appears in the PDF: bold caption titles with no terminal period, bold bullet lead-ins on their own line. Where the web page bolds an entire caption or adds a terminal period, the PDF form is used.
  - One paragraph on p. 15 has a production artefact typeset across it (see `## Limitations`, drafting tells). Where that paragraph is quoted in `## Findings and their caveats`, the intended sentence is given — the reading is unambiguous, and the web page's clean text confirms it — and the stray words are quoted separately and identified as an artefact, not as prose.
  - The Figure 2.4 quotation in `## Findings and their caveats` retains the PDF's "In the top panel", which is an error in the source (the exhibit has rows, not panels); it is annotated, not corrected.
  - **Alt text and chart-image numbers, per `room/director-2026-09-16-alt-text-ruling.md`.** The bold sentence(s) under an exhibit are the caption and are quoted as such. Text rendered *inside* a chart image — chart titles, table titles, panel titles, axis labels, legend entries, the composition line under Figure 1.3's axis — is quoted only where it bears on the caption pattern and is explicitly marked. **No number printed inside a chart image is recorded anywhere in this file.** In particular: the data labels on Figures 1.1, 1.2, 1.3 and 1.4; the Gini values and reference-line value in Figure 1.5's legend and panels; the US average hourly wage annotation in Figure 1.4; the bar labels in Figure 2.1 other than the one the caption itself states; the fitted slopes printed in Figure 2.2's panel titles; the axis ranges and tick values in Figure 2.3; and the coefficients and interval endpoints in Figure 2.4 are **not** recorded. Every number quoted in this file appears in the PDF's body prose, its footnotes, a caption, or Table 1.1 / Table 2.1 — both of which are live text in the PDF (and images on the web page, which is noted where it matters).
- **Scope.** This file annotates how the report is written: its section order, the grammar of its findings and caveats, how its comparisons are phrased, its caption template, where its limitations sit and how it closes. It makes no judgement about whether any finding is correct. Where this file says a caveat is misplaced, a number is unsupported in prose, a unit switches or a name is inexact, that is a statement about the writing, not about the analysis.
