# economic-index-2026-06-report — style annotation

## Source

- **Title (PDF cover, and the document of record):** "Anthropic Economic Index report: Cadences". The web page H1 is identical. The browser/OG title is the same string again ("Anthropic Economic Index report: Cadences"); the OG description is written for a general reader and is not in the document: "The latest Economic Index report looks at when people come to Claude, what they produce with it, and how they perceive AI's impact on their work."
- **Date:** PDF cover, "Published / June 26, 2026". Web page, "Jun 26, 2026".
- **URLs fetched:**
  - PDF (document of record): https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf — 33 pages.
  - Web page: https://www.anthropic.com/research/economic-index-june-2026-report
  - The appendix (`economic-index-2026-06-appendix`) was **not** fetched for this file; it has its own style entry. Note for the record that the report page links two different builds of it: the body and the "Appendix / Available here" line link `…03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf`, while footnote 5 links `…8eb31e1d187ff18146d248bbef8b2754971f0f5a.pdf`. Both are listed in `wiki/INDEX.md` as near-identical copies. Nothing in this file depends on either.
- **Document type:** the sixth wave of the standing report series, and the first to carry survey evidence. Three numbered chapters, a short "Discussion", a seven-name author list, 27 numbered footnotes, no abstract, no executive summary, no limitations section, no chapter-level conclusions.
- **Approximate length:** 33 PDF pages. Cover, p. 1; Introduction, pp. 2–3; Chapter 1, pp. 4–8; Chapter 2, pp. 9–18; Chapter 3, pp. 19–31; Discussion, p. 32; Appendix pointer and citation, p. 33. Eighteen numbered figures and one numbered table (1.1–1.4, 2.1–2.3, Table 2.4, 2.5, 2.6, 3.1–3.9). Roughly 5,000 words of body prose plus about 1,400 words of footnotes.
- **Authors named on the cover:** "Maxim Massenkoff, Eva Lyubich, Szymon Sacher, Zoe Hitzig, Shaoyi Zhang, Ryan Heller, Peter McCrory". One tier — no lead-author asterisks, no equal-contribution note, unlike the September 2025 report. Thirty-nine acknowledgees, roughly alphabetical by surname (with two transpositions) and "Jack Clark" appended last. The web page moves authors and acknowledgements from the cover to the foot of the article and appends a BibTeX `@online` block keyed `anthropic2026aeiv6` — the key is the only place either document numbers the wave.
- **Audience:** economists and policy readers, but the citation load is much lighter than the September 2025 report's. The only external works cited anywhere are a "rising tide" arXiv paper, Eloundou et al.'s theoretical-exposure paper, an IMF staff discussion note, World Bank WDI, UN World Population Prospects, IMF WEO, BLS OEWS, BLS JOLTS and a Federal Reserve well-being report. No diffusion-history literature, no theory citations, no economics of adoption. The reader is assumed to know what a geometric mean, a standard deviation, a linear regression coefficient and a correlation are; each is glossed only where the caption needs it.

### How the web page condenses the PDF

Barely at all: the web page carries the full text of all three chapters and the Discussion. As with the September 2025 report, the condensation is typographic and navigational rather than editorial. But unlike that report, the web version is **not** a faithful reprint: it silently corrects and re-words the PDF in at least nine places, and one of those changes a number. The differences that matter for style:

1. **A number changes, and the web version is the internally consistent one.** PDF, Chapter 1 opening: "people most often ask for sleep advice around **3 a.m.** and for recipes around 6 p.m." PDF, Introduction preview bullet: "sleep advice peaks around **5 a.m.**" The PDF contradicts itself two pages apart. The web page reads "around 5 a.m." in both places. The body prose in both versions hedges the same claim in words rather than hours ("people seek sleep advice in the few hours just before dawn"), which is how the contradiction survived. **Take the web page as governing for this one figure and the PDF for everything else; and treat the hour-level claim as reported in words, not in clock time.**
2. **A typo is fixed.** PDF: "By comparing the level of autonomy in Claude chat and Cowork to Claude Code, we show that is starting to change." Web: "…we show that this is starting to change."
3. **Surface terminology is updated in two footnotes.** PDF footnote 5 of Chapter 2 says "data and spreadsheets, where **Claude.ai** conversations involve more autonomy than Claude Code (3.09 vs 2.74)… On **Claude.ai** this output leans toward financial modeling… accounts for part of the **Claude.ai** lift." The web version of the same footnote (numbered 12) says "**chat and Cowork** conversations", "On **chat and Cowork**, this output leans…", "part of the **chat and Cowork** lift." Same substitution in PDF Chapter 3 footnote 9 → web footnote 22 ("more automated than those on Claude.ai" → "than those on chat or Cowork"). The web page is enforcing the report's own new naming convention that the PDF applies inconsistently.
4. **A caption's modal verbs are swapped.** PDF Figure 3.2: title "…the share of their work tasks AI **could** do to grow…", gloss "…respondents say AI **can** do today versus in 12 months." Web: title "…AI **can** do to grow…", gloss "…respondents say AI **could** do today…". The in-image chart title reads "Share of work tasks AI could do".
5. **Caption typography changes, in the opposite direction from September 2025.** PDF: bold "Figure 1.1: Personal conversations increase on the weekend**.**" — with a terminal period — running straight on into the plain-roman gloss on the same line. Web: the bold title is its own line, **loses** the terminal period, and the gloss is italicised beneath it. So the period that the September 2025 report added on the web and omitted in the PDF is added in the PDF and omitted on the web here. Do not treat the period as part of the house caption form; treat the *bold declarative title plus roman gloss* as the form.
6. **Chapter labels are dropped.** PDF: "CHAPTER 1 / Cadences", "CHAPTER 2 / Artifacts", "CHAPTER 3 / Perceptions". Web: "## Cadences", "## Artifacts", "## Perceptions" with no chapter number, while the Introduction still says "In Chapter 1…", "Chapter 2 explores…", "Chapter 3 presents…". A web reader has to count.
7. **Footnotes are renumbered from per-chapter to continuous.** PDF numbers footnotes 1 in the Introduction, 1–6 in Chapter 1, 1–6 in Chapter 2, 1–14 in Chapter 3, each block set on the chapter's last page. Web runs 1–27 in one list at the foot of the article. Cite this report's footnotes by chapter, not by number, or the two versions disagree.
8. **Links are added.** The web page hyperlinks every internal reference the PDF states in plain text — the January 2026 report, the March 2026 report, the labour-market paper, the 81k interviews and the 81k economics post, Anthropic Interviewer, Clio, the survey announcement, the Claude Code companion report, the Sonnet 3.7 report, the appendix — plus the external IMF note, World Bank, UN, IMF WEO, BLS JOLTS, Eloundou et al. and the "rising tide" paper. The PDF names them in prose and lets the reader find them. Nothing in the argument depends on a link.
9. **Small copy-edits throughout.** PDF "Today, with the rapid growth of Claude Code and Cowork, Claude sessions increasingly consist of long-running agentic tasks" → web "With the rapid growth of Claude Code and Cowork, Claude sessions **now** increasingly consist…". PDF "A chat transcript no longer fully captures how people are using AI, and our methods… have had to **rapidly** adapt" → web "**Chat transcripts** no longer fully **capture**… have had to adapt." PDF section heading "Cost tracks the value of **the** work" → web "Cost tracks the value of work". PDF "with the option to select from **5** bands" → web "**five** bands". Commas added in three places ("the relationship is noisy**,** and there are notable outliers"; "Across all conversations**,** the average difference"; "educational materials**,** and math-related queries"). None of these changes a claim.
10. **Front matter moves to the back, and the back grows.** The web page ends with the citation block, the author list, the 39 acknowledgees and three unrelated "Related content" cards. The PDF ends with "Appendix / Available here" and the citation.

Nothing is cut from the argument, no finding is softened, and no figure is dropped. But the web page is the later, cleaner text — which reverses the September 2025 pattern, where the PDF was the internally consistent document and the web page the one with drifting cross-references.

## Section order

Headings in PDF order. Page spans are the PDF's own numbering.

1. **Cover (p. 1).** Title, publication date, authors, acknowledgements. No abstract, no summary block, no figure, no wave number.
2. **Introduction (pp. 2–3), ~600 words.** Four moves: (i) one paragraph on what changed in the product — chat gave way to long-running agentic sessions — ending on the methodological consequence; (ii) a three-bullet list of what the data pipeline now does differently, with the appendix named for the rest; (iii) one paragraph opening the survey, posed as three questions; (iv) "We preview our main findings below" and three bullets, one per chapter. One footnote, defining the surfaces and restating the privacy and terms position.
3. **Chapter 1: Cadences (pp. 4–8), ~700 words.** The chapter's title is the report's title.
   - Untitled chapter opener (p. 4, ~130 words) — states the instrument change (continuous daily sampling versus the seven-day samples of every earlier report) and previews the three findings in one sentence each.
   - *The workweek* (pp. 4–5) — Figure 1.1.
   - *Daily rhythms* (pp. 6–7) — Figures 1.2, 1.3.
   - *Tax day* (pp. 7–8) — Figure 1.4.
   - Six footnotes (p. 8): the privacy-classifier statement, the chat-and-Cowork definition, the 1P API definition, the request-cluster pointer, the construction of "entrepreneurial activity" and "resume activity", and the IP-based time-of-day inference.
4. **Chapter 2: Artifacts (pp. 9–18), ~1,600 words.** The longest chapter.
   - Untitled opener (p. 9) — defines the artifact construct in one sentence, gives the classifier's coverage and the top three categories, then hands off: "We look at that split next." Figure 2.1.
   - *What is each artifact used for?* (pp. 10–12) — Figure 2.2.
   - *Cost tracks the value of the work* (pp. 12–14) — Figure 2.3, Table 2.4.
   - *How much autonomy does Claude have to decide on its own?* (pp. 14–16) — Figure 2.5.
   - *Claude answers above the level it was asked* (pp. 16–17) — Figure 2.6.
   - Six footnotes (p. 18), carrying the only sample window in the chapter, the "None" catch-all, the geometric-mean justification, the Claude Code pointer, the one exception to the autonomy result, and the reading-level prompt pointer.
5. **Chapter 3: Perceptions (pp. 19–31), ~2,000 words.** The survey chapter.
   - Untitled opener (pp. 19) — three paragraphs: what the previous 81k interviews showed, how the new survey is built and linked, and a preview that states the chapter's two-sided result.
   - *Who responded to the Economic Index Survey* (pp. 20–21) — the representativeness statement comes **first**, before any result. Figure 3.1.
   - *AI and work tasks* (pp. 21–25) — Figures 3.2, 3.3, 3.4.
   - *AI and jobs* (pp. 26–28) — Figures 3.5, 3.6, 3.7.
   - *How usage differs between genders* (pp. 29) — Figure 3.8.
   - *What do people hope for from an AI-transformed economy?* (pp. 30) — Figure 3.9.
   - Fourteen footnotes (p. 31).
6. **Discussion (p. 32), ~350 words.** Four paragraphs. No numbers except one ("over 35%"). No recommendations to anybody.
7. **Appendix pointer and citation (p. 33).**

**Where the findings sit: in the Introduction's three bullets, then once each in the chapters.** Unlike the September 2025 report there is no "We find:" block per chapter and no chapter conclusion, so each finding is stated exactly twice — once compressed into the preview bullet, once in the body where it is earned. The three-depth architecture (bullets / overview / chapter) collapses to two depths here, and the effect is that the chapters read faster and the report is 14 pages shorter.

**Where the methods sit.** Nowhere as a section, again, and the distribution is looser than in September 2025. The artifact construct is defined at first use (p. 9); the primitive split is imported from the January 2026 report by reference; automation and augmentation are defined at first use in Chapter 3 (p. 25) even though "automation share" is the organising variable of that whole chapter; the reading-level classifier is defined at first use (p. 16) and its prompt is outsourced to the March 2026 appendix; the survey's linkage, sampling and exclusion rules are in the body (p. 19), not a footnote — the one place this report is more forthcoming than its predecessor. **Chapter 1 never states its sample window at all.** The only dates attached to the cadence findings are the axis ticks inside Figures 1.1 and 1.4 and the April 15 deadline named in the prose; Chapter 2's footnote 1 ("sampled between April 10 and June 10, 2026") covers Chapter 2 only. That is the report's most serious documentation gap and it is invisible unless you look for it.

## Opening move

### The Introduction, verbatim and in full (PDF)

> One year ago, most Claude usage took the form of a conversation between a user and an assistant. Today, with the rapid growth of Claude Code and Cowork, Claude sessions increasingly consist of long-running agentic tasks. A chat transcript no longer fully captures how people are using AI, and our methods for studying Claude's economic impacts have had to rapidly adapt.

> To keep pace, we made several changes to our data pipeline for the Economic Index. In this version, we:
>
> - Sample data at a higher rate, allowing us to view usage patterns down to the hourly level.
> - Introduce a new classifier that labels the output of each conversation.
> - Share more granular data, breaking out results for chat and Cowork conversations (together, "Claude conversations") and the 1P API, aggregated at a monthly level.[1]

> We describe additional methodological changes in the Appendix. Together, these changes provide a clearer picture of how AI mirrors and diffuses into economic life.

> In addition, we've previously lacked visibility into Claude's impact *outside* of user sessions. How do people perceive AI to be changing their work, or the opportunities available to them? Does their usage of AI shape their expectations? In an ideal world, what would they want from AI? We report initial findings from the Anthropic Economic Index Survey, launched in April 2026.

> We preview our main findings below.

### The three preview bullets, verbatim

> - In Chapter 1, we show how the rhythms of the external world shape Claude usage. Work-related queries subside on the weekend, though less dramatically in the most highly paid occupations; people tend to ask for the news in the morning, and sleep advice peaks around 5 a.m.; tax-related requests surge around filing deadlines.
>
> - Chapter 2 explores the concrete outputs that people take away from their Claude sessions. These are highly dependent on what product they're using. Chat and Cowork provide more explanations than Claude Code, for example. The nature of the output also shapes people's interactions with Claude. Building a website leaves much more to Claude's judgment than translating a document, where the answer is largely determined by the text. We also see that more compute is associated with more valuable artifacts; the tokens a given output consumes rise with the estimated value of the work.
>
> - Chapter 3 presents the first results from the Anthropic Economic Index Survey, which we link to Claude usage data through our privacy-preserving system. Expectations and experiences vary systematically with how people use Claude: people who use Claude in the most automated way expect AI to take on more of their tasks in the next year, yet feel the most optimistic about what that means for their work, anticipating positive impacts on pay, job security, and meaning.

And the footnote hanging off the third pipeline bullet:

> [1] This includes chat conversations and Cowork sessions from consumer (Free/Pro/Max) accounts on both Claude.ai and the Claude desktop app. "First-party API" or 1P API refers to developer traffic routed directly through Anthropic's own programming interface, which is distinct from both Anthropic's consumer-facing Claude.ai application and third-party platforms such as Amazon Bedrock or Google Cloud Vertex. We continue to manage data according to our privacy and retention policies, and our analysis is consistent with our terms, policies, and contractual agreements.

### Annotation

- **There is no executive summary.** The preview bullets are the summary, and they are introduced by one flat sentence — "We preview our main findings below." No bolded lead-ins, no "We find:" header, no claim-plus-evidence two-beat. Compare September 2025, where every bullet was **bold claim in words** followed by the claim in numbers. Here the bullets are running prose, and they carry almost no numbers: three clock times, no percentages, no ratios. The only quantity in the entire opening is an hour of the day — and it is the one the PDF contradicts two pages later. **The lesson for our drafts is the September 2025 form, not this one: a summary bullet that carries no number cannot be checked against a chapter.**
- **What question is posed.** Not a question about the economy but a question about *measurement*: the instrument has stopped matching the object. "A chat transcript no longer fully captures how people are using AI, and our methods for studying Claude's economic impacts have had to rapidly adapt." The puzzle is the authors' own, stated in the first three sentences, and the three pipeline bullets are its answer. This is the opening move of a *methods wave* — the report's claim to novelty is the sampling rate, the classifier and the data release, not a finding.
- **Where the economics enters.** One sentence, at the end of the second move: "Together, these changes provide a clearer picture of how AI mirrors and diffuses into economic life." The two verbs are the whole thesis — *mirrors* is Chapter 1, *diffuses* is Chapters 2 and 3 — and neither is hedged, because neither is a claim about a quantity. A draft can do this: put the report's two-word thesis in the verbs of one sentence and then let the chapter titles carry it.
- **Who is said to be affected.** "People", throughout, and in the survey paragraph specifically people at work: "How do people perceive AI to be changing their work, or the opportunities available to them?" Nobody is named as harmed. The three survey questions are posed in the second person of the respondent's interest, ending on the one that is not about impact at all: "In an ideal world, what would they want from AI?" That question is the one the report closes on (Figure 3.9), which is how the opening and the ending are pinned together.
- **What the data is said uniquely to show.** Three novelty claims, all attached to instruments rather than results: sampling "at a higher rate, allowing us to view usage patterns down to the hourly level"; "a new classifier that labels the output of each conversation"; and "initial findings from the Anthropic Economic Index Survey". The word "first" appears once in the opening, in the third bullet, and it modifies *results from a survey*, not a fact about the world.
- **How soon the first number appears.** Not in the Introduction at all, unless "One year ago" counts. The first quantity in the report is "around 35% on weekdays to just under 50% on weekends", on page 4. This is the opposite of the September 2025 move (an outside survey number in the second sentence, used to pose a puzzle). Here the puzzle is internal, so no external benchmark is needed — and the cost is that a reader is given no way to judge whether the report's numbers are large.
- **Register of the opening.** First person plural for institutional and analytical acts only: "we made several changes", "we describe", "we report", "we show", "we preview". Findings inside the bullets are agentless ("Work-related queries subside on the weekend", "the tokens a given output consumes rise with the estimated value of the work"). Two italicised words in the whole opening, both doing scope work: "outside of user sessions" and, in the third bullet, "most" ("the *most* optimistic"). The hedging is light: "though less dramatically", "tend to", "is associated with", "vary systematically with".
- **Observation separated from conjecture, in the bullet.** The third bullet is the report's most careful sentence and it is worth reading as a template: "people who use Claude in the most automated way expect AI to take on more of their tasks in the next year, yet feel the most optimistic about what that means for their work". Two observed associations, joined by "yet" to mark that they are in tension, with no mechanism offered and no causal verb anywhere. The mechanism question ("A natural question is why automated usage and sentiment move together") is deferred 27 pages.
- **The naming rule in the opening.** "how **AI** mirrors and diffuses into economic life"; "how people perceive **AI** to be changing their work"; "what they would want from **AI**" — the questions and the stakes say AI. "most **Claude** usage", "**Claude** sessions", "usage patterns", "**Claude** conversations", "how people use **Claude**" — the object of measurement says Claude. One sentence carries both, correctly: "people who use **Claude** in the most automated way expect **AI** to take on more of their tasks." Measured behaviour, Claude; expectation about the technology, AI.

## Findings and their caveats

Findings in report order. Each is quoted from the PDF and annotated. Chapter 3's survey findings are phrased differently from Chapters 1–2's usage findings in a consistent way, described at the end of this section.

### Chapter 1, opening — the instrument, stated as the finding's precondition

> Our new privacy-preserving telemetry, which continuously samples a slice of conversations every day, allows us to study daily and hourly patterns in usage, in contrast to the seven-day samples each previous Economic Index report drew on. These analyses capture ebbs and flows in work patterns around the world.[1]

> We find that Claude usage mirrors the workweek, with personal prompts spiking on the weekend. The hourly data captures within-day patterns—people most often ask for sleep advice around 3 a.m. and for recipes around 6 p.m. We also see usage reflecting key dates. For instance, tax-related requests surged just before the US filing deadline on April 15.

**Annotation.** The chapter opens by naming what changed in the instrument and what the old instrument could not do — "in contrast to the seven-day samples each previous Economic Index report drew on" — which is the honest way to introduce a new cut: state the comparison to your own previous method before any result. Then three findings in three sentences, each with its own verb of evidence ("We find", "The hourly data captures", "We also see"). Note that the strongest claim in the chapter, "Claude usage mirrors the workweek", is unhedged and unnumbered, and that it is licensed by the figure rather than by a test. The 3 a.m./5 a.m. discrepancy against the Introduction bullet lives in this paragraph (see `## Source`).

### Chapter 1, Finding 1 — the weekday/weekend shift in personal use

> The share of chat and Cowork[2] conversations categorized as personal use spikes from around 35% on weekdays to just under 50% on weekends during the sample period (Figure 1.1). Outside the workweek, users' conversations shift from business correspondence, marketing copy, and slide decks to emotional support, medical questions, and investment advice. This shift is biggest for high-income countries.

> A similar pattern is present in Claude Code and the 1P API traffic (i.e., API traffic routed directly through Anthropic), though both have lower baseline rates of personal use.[3]

**Annotation.** Both numbers are approximations with the approximation marked twice over: "around 35%" and "just under 50%". A report that samples hourly could give these to a decimal and chooses not to, because the claim is a *shape* (a weekly cycle), not a level. "during the sample period" carries the whole temporal scope of the chapter and is never cashed out — no dates appear in the prose or the footnotes of Chapter 1, only on the axis of the figure.

The composition sentence is the best-made sentence in the chapter: three weekday categories against three weekend categories, in the same grammatical slot, with no numbers at all. "business correspondence, marketing copy, and slide decks" → "emotional support, medical questions, and investment advice." A reader learns more from that pairing than from six shares. **This is the device to copy for a composition shift: name three on each side, in the same order of prominence, and let the reader do the subtraction.**

Then "This shift is biggest for high-income countries" — a one-clause heterogeneity claim with no number, no figure, and no footnote. It is the weakest-supported sentence in Chapter 1 and it is not marked as weaker than its neighbours. The cross-surface replication that follows is exactly right in form (same pattern, different level, level difference named as "lower baseline rates") and is the only place in the chapter where a finding is tested at more than one level.

### Chapter 1, Finding 1b — which Claude Code tasks swing

> Request clusters[4] allow us to go one level deeper and see which specific Claude Code tasks swing most between weekdays and weekends. On weekends, the Claude Code usage clusters that fall the most include backend architecture, API debugging, and data storage. Those that increase the most include AI agent design, quant trading, and gaming.

> Weekends may also create space for people to pursue new ventures. Across countries, conversations related to starting a business are highest on Saturday and Sunday. However, job application activities drop on the weekend along with other work-related tasks.[5]

**Annotation.** A ranked claim reported as membership rather than as values: "the clusters that fall the most **include**" — three named, no magnitudes, and "include" licensing the selection. The same construction as September 2025's "Singapore and Canada are **among** the highest countries", and it does the same work.

The second paragraph is a two-sided result, and the "However" is doing the honest half: entrepreneurial conversations rise at the weekend, job-application conversations fall. A weaker draft would have reported the rise and called the weekend a window of opportunity. Note the epistemic ordering: conjecture first, marked ("Weekends **may also create space** for people to pursue new ventures"), then the two observations, then the footnote that makes both measurable — footnote 5 lists the nine request clusters that constitute "entrepreneurial activity" and states that resume activity is defined by the artifact classifier. **The construct is defined in a footnote and the footnote is checkable; the claim in the body is not overstated relative to it.**

### Chapter 1, Finding 2 — the within-day pattern

> Hour by hour, Claude usage reflects the rhythms of daily life. Figure 1.2 shows the hourly frequency of different request clusters relative to their overall average in global traffic.[6]

> People ask for news at 7 a.m. local time. Business correspondence (e.g., email drafting) traces the arc of the workday, with a slight peak at 10–11 a.m. One of the biggest spikes is recipe requests, which are 2.3 times more frequent at 6 p.m. compared to the average. Media recommendations are most concentrated in the evening, while people seek sleep advice in the few hours just before dawn.

**Annotation.** Four findings in four sentences, and only one carries a number — "2.3 times more frequent at 6 p.m. compared to the average", with its denominator named in the same clause. The other three are stated as times or as verbal shapes ("traces the arc of the workday", "most concentrated in the evening", "in the few hours just before dawn"). The escalation is deliberate: the sentence with the number is flagged as the extreme case ("One of the biggest spikes"), so the reader knows the unnumbered ones are smaller without being told how much smaller.

"at 7 a.m. **local time**" is the caveat and the method in three words; footnote 6 supplies the mechanism — "The time of day is based on inferring the state from the IP address of the conversation" — which is also the finding's main threat, since a mis-inferred location moves a conversation by hours, and the footnote does not say how often that happens. In our posts this belongs beside the finding.

### Chapter 1, Finding 3 — nights and weekends skew to higher-wage occupations

> On nights and weekends, when people do turn to Claude for work, the tasks skew toward higher-wage occupations (Figure 1.3). While we can't conclusively identify the jobs of the people making these requests, this could reflect the fact that people in higher-paying occupations—like marketing managers or computer programmers—are more likely to work outside traditional hours. In contrast, tasks related to jobs in the bottom two quartiles—like telemarketing and clerical work—fall to a smaller share of total conversations. This pattern isn't driven exclusively by computer and mathematical tasks: when we removed those occupations from the analysis in a robustness check, higher-quartile tasks still increased on nights and weekends.

**Annotation.** The single best-constructed finding in the report, and the only one with a robustness check in the body rather than in a footnote. Four moves in one paragraph:

1. **The observation, with its unit named as tasks, not people** — "the tasks skew toward higher-wage occupations". No number in the body at all; the magnitudes exist only as data labels printed inside Figure 1.3 (see `## Figure captions`).
2. **The identification caveat, placed before the interpretation it qualifies** — "While we can't conclusively identify the jobs of the people making these requests". This is the September 2025 "Though not adjusted for population" move: concession in the sentence-opening subordinate clause, strongest available position.
3. **The mechanism, offered and marked as offered** — "this **could** reflect the fact that people in higher-paying occupations… are **more likely** to work outside traditional hours", with two illustrative occupations. Then the mirror image on the other side of the distribution, also with illustrations ("telemarketing and clerical work"), which is how a monotone claim is shown to hold at both ends.
4. **The obvious confound, named and removed** — "This pattern isn't driven exclusively by computer and mathematical tasks: when we removed those occupations from the analysis in a robustness check, higher-quartile tasks still increased on nights and weekends." The confound a referee would raise first about any Claude wage gradient is that coders dominate; the sentence names it, says what was done, and reports the direction. It does not report the magnitude after removal, which is the one thing missing.

**The transferable pattern: observation → identification caveat → mechanism as conjecture → the confound removed, in that order, inside one paragraph.**

### Chapter 1, Finding 4 — tax day

> The sample period for this report covers tax filing deadlines for people in the United States. Figure 1.4 shows a large spike in the share of tax-related conversations around the deadline. On April 14, tax-related clusters were eight times as common as on the average day in May and remained about as high on April 15. On April 16, they dropped sharply.

**Annotation.** A three-date narrative with one ratio, and the ratio's baseline is named precisely — "eight times as common as on the average day in **May**", not "than average". Choosing a clean out-of-event month as the denominator, and saying so, is what makes the number interpretable; the figure's axis label repeats it ("relative to own May average"). The drop is stated qualitatively ("dropped sharply") rather than with a second ratio, so the sentence does not pretend the fall is measured as well as the rise. The opening sentence frames the finding as a validation exercise — the sample happens to span a known external shock, so the instrument can be checked against something the world already knows. **That is the strongest use of a cadence finding and the reason this chapter earns its place: a new instrument is credible when it reproduces an event you did not need it to discover.**

### Chapter 2, Finding 1 — the artifact classifier's coverage and the top categories

> In this chapter, we classify each conversation on chat and Cowork (hereafter "Claude conversations")[1] by its artifact, which we sort into more than 30 categories. We refer to the primary output Claude produces in a conversation—a document, an explanation, a piece of code, an academic paper, and so on, whether presented in a chat window or as a separate document—as an artifact. The full list of artifacts is in the Appendix.

> Our classifier identified 93% of Claude conversations as producing an artifact (Figure 2.1).[2] The most common artifacts are explanations (17% of conversations), documents and reports (15%), and guidance (11%). Conversational outputs (like explanations or guidance) and written deliverables (like documents or presentations) each account for about a third of conversations; code and technical work (like apps or scripts) for about a sixth.

> What an output is doesn't tell you what it's for: the same artifact could be a work deliverable or a personal project. We look at that split next.

And the footnote carrying the residual:

> [2] "None" is a catch-all for the conversations that didn't yield a prominent concrete output. This may include brief or abandoned exchanges, cases resulting in an error or cases where Claude asked a clarifying question and the user didn't continue.

**Annotation.** The construct is defined before it is used, in a sentence that names the four things an artifact can be and then adds the boundary that matters for a product with a canvas — "whether presented in a chat window or as a separate document". Coverage is reported before composition (93% first, then the shares), which is the right order for a new classifier: a reader needs to know how much of the sample the taxonomy explains before being told what is in it.

Two roundings in one paragraph, deliberately mismatched: exact-ish shares for the named categories (17%, 15%, 11%) and coarse shares for the groupings ("about a third", "about a third", "about a sixth"). The groupings are the authors' own aggregation of their own categories, and the coarseness signals that — an aggregation whose boundaries are a judgement call should not be quoted to the point.

Footnote 2 is the residual disclosure that September 2025 failed to make about its 77%/12% split, and it is done properly: the catch-all is named, and three distinct mechanisms that land in it are listed (abandoned exchanges, errors, unanswered clarifying questions). **It is also the report's clearest instance of a classifier's own uncertainty being reported as a category rather than dropped.** Note the mismatch between the footnote's term and the exhibit's: the footnote calls the category "None", the bar in Figure 2.1 is labelled "No clear output".

The hand-off sentence — "What an output is doesn't tell you what it's for… We look at that split next" — is the chapter's substitute for a conclusion. This report never closes a chapter; it pivots.

### Chapter 2, Finding 2 — what each artifact is used for

> Some categories of artifacts are almost always personal. More than 80% of conversations producing creative writing, guidance, and recipes were classified as personal. Within categories, the personal and work-related uses can look quite different. Personal creative writing, for instance, is dominated by fanfiction, worldbuilding, and poetry; the 13% that is work-related is mostly in the form of short-form video scripts, screenwriting, and speeches. Categories most likely to be work-related include creating marketing content (80%), creating blogs or articles (81%), and writing database queries (82%).

> Many outputs are equally likely to be used for personal and work reasons, including creating plans or strategies (44% work-related, 49% personal) or translation (42% work, 44% personal). For example, the most common types of personal planning artifacts include travel itineraries and workout schedules, while work-related plans most often pertain to entrepreneurial or content strategies.

> Finally, artifacts that are characteristic of coursework include creating academic papers and theses, educational materials and math-related queries, though a non-negligible share of each falls into both work and personal categories.

**Annotation.** The three-paragraph rank structure of September 2025's country lists, applied to categories: the personal pole, the work pole, the middle, then the third dimension. Every share is attached to a named category, and the two-number pairs for the middle group are given on both dimensions — "44% work-related, 49% personal" — so the reader can see that they do not sum to 100 and infer that coursework takes the remainder. Nothing forces the reader to; the coursework share is simply left out of the sentence, which is a small lapse: three-way shares should be given as three numbers or as two plus an explicit residual.

The qualitative colour inside each category is the chapter's signature device — "fanfiction, worldbuilding, and poetry" against "short-form video scripts, screenwriting, and speeches"; "travel itineraries and workout schedules" against "entrepreneurial or content strategies". This is the same three-against-three construction as Chapter 1's weekday/weekend sentence. It converts a bar into a picture without a number, and it is repeated four times in the chapter. **Where a classifier produces a category, one sentence naming what is inside it does more than a second decimal place.**

"a non-negligible share of each falls into both work and personal categories" is a caveat with no number and an awkward negative. It is the report's weakest hedge phrasing and should not be copied; the number exists (it is in Figure 2.2) and could have been given.

### Chapter 2, Finding 3 — the question flipped

> We can also flip the question. Instead of asking what each output is used for, we can ask what sort of artifacts work, personal, and coursework conversations each tend to produce. Work conversations most often produce documents and reports (20%), followed by explanations (9%), email drafts (7%), and analyses and summaries (6%). Coursework conversations look broadly similar, with documents and reports leading there too (21%), closely followed by explanations (20%), educational materials (11%), and academic papers (6%). In contrast—and unsurprisingly—only 6% of personal conversations produce a document. Instead, the most common results are explanations (25%) and recommendations (22%).

**Annotation.** The same cross-tabulation read the other way, announced as such in four words ("We can also flip the question"), and this is the clearest demonstration in the corpus of *one claim tested at more than one level*: row shares and column shares of the same table, reported separately, with the interpretation attached to each. Conditional on the artifact, creative writing is personal; conditional on the purpose, work produces documents. Neither statement can be derived from the other, and the report says why it is asking both.

Three-decimal discipline is consistent (all shares to the point, all in parentheses after the category), the ranking is given as a sequence with "followed by" / "closely followed by", and the one editorial intrusion is marked as such: "In contrast—and unsurprisingly—only 6%…". Flagging your own result as unsurprising is a way of spending the reader's attention carefully; September 2025 used "Surprisingly" four times in 47 pages for the same purpose in the other direction.

### Chapter 2, Finding 4 — tokens against wages

> Producing these outputs requires compute, and we find that compute tends to scale with the value of the work. We measure each conversation's computational costs in tokens—the amount of text processed and generated, including Claude's internal reasoning—and compare across occupations by mapping each conversation's classified task to the occupation that typically performs it. Throughout this section, we restrict our analysis to work-related conversations.

> The left panel of Figure 2.3 shows a positive relationship between the median conversation-level number of tokens and the median wage in mapped occupation.[3] For example, marketing managers earn roughly twice as much as editors ($80 vs. $37 per hour) and conversations mapping to their tasks consume approximately 2.5 times as many tokens. Admittedly, the relationship is noisy and there are notable outliers. Pharmacists, for example, earn nearly three times what statistical assistants do ($68 vs. $24 per hour), yet conversations mapped to pharmacist tasks use only about one twentieth as many tokens.

And the footnote:

> [3] We use geometric means for the conversation level token counts since that variable is extremely right-skewed–a small number of conversations use several orders of magnitude more tokens than a "typical" conversation. The relationship is very similar if we use medians or if we weight the tokens by their respective cost to account for the mix of models used. There are some notable exceptions, including physician occupations.

**Annotation.** The measurement chain is stated in one sentence and not compressed: conversation → classified task → occupation that typically performs it → that occupation's median wage. "the occupation that **typically** performs it" is the inference the whole finding rests on, and the word "typically" is the only caveat it gets in the body; the figure's axis says "Occupation median wage (OEWS)" and Chapter 2's footnote 1 dates the wage vintage ("BLS OEWS, May 2025 release"). The sample restriction is stated before any result and scoped explicitly to the section ("Throughout this section, we restrict our analysis to work-related conversations").

Then the exemplary move, and the reason this is the best finding in Chapter 2: **the confirming example and the disconfirming example are given the same amount of space, the same sentence form, and the same two-number-pair construction.** Marketing managers versus editors (≈2× the wage, ≈2.5× the tokens) is followed immediately by pharmacists versus statistical assistants (≈3× the wage, about one twentieth the tokens), with "Admittedly, the relationship is noisy and there are notable outliers" between them. The outlier is not relegated to a footnote; it is named, quantified and left unexplained. Footnote 3 then adds a second class of exceptions ("including physician occupations"), states the estimator and why it was chosen, and reports that two alternative estimators give the same relationship. A referee reading only the body and that footnote can see the shape of the evidence, the noise, and the two families of counter-examples.

Note the hedge ladder inside three sentences: "we find that compute **tends to** scale", "shows a **positive relationship**", "**approximately** 2.5 times", "**Admittedly**, the relationship is noisy", "**about** one twentieth". No causal verb anywhere; wages are never said to drive tokens.

### Chapter 2, Finding 5 — tokens by artifact, and how much of the gradient that explains

> The tokens consumed to generate different types of artifacts tell a similar story. More complicated and valuable outputs tend to consume significantly more tokens than simpler outputs. For example, conversations about building apps use more than three times the tokens of the median conversation. On the other end of the spectrum, a typical explanation uses about a fifth of the tokens of the median conversation. About 44% of the wage gradient in token consumption is explained by output mix—higher wage occupations are more likely to produce compute-intensive artifacts.

**Annotation.** Two poles of a distribution against a common denominator ("the median conversation"), stated as multiples rather than levels, which is the only way a token count is meaningful to a reader. Then the decomposition, which is the sentence that makes the whole section an argument rather than two correlations: 44% of the wage gradient is composition, so the majority is not. The report states the share explained and, in the same sentence, the mechanism that explains it — "higher wage occupations are more likely to produce compute-intensive artifacts" — and then does not claim the remainder for anything. **A decomposition reported without a story for the residual is a self-limiting finding, and it is the right way to report one.**

"More complicated and valuable outputs" slides between two different adjectives, only one of which is measured. Nothing in the report measures complexity; the wage of the mapped occupation is the value proxy. A referee would mark that sentence.

### Chapter 2, Finding 6 — why it matters economically (Table 2.4)

> Why does this matter economically? In conversations mapped to higher-wage occupations, Claude produces more (1.34 times as much output per turn), while users engage more (1.53 times as many turns) and enable extended thinking more frequently (34% of conversations versus 31%; Table 2.4). Crucially, these move together: more production from Claude does not mean less from the user. If the human remains involved in the highest-value tasks, the pattern looks more labor-augmenting than labor-displacing. It also shows that, to some extent, more valuable outputs cost more. The next section examines how much of the decision-making within each conversation is delegated to Claude.

**Annotation.** The why-it-matters paragraph of the chapter, and the only place in the report where a usage pattern is connected to the labour-market question. Its structure is worth copying exactly:

1. **The question asked in four words** — "Why does this matter economically?"
2. **Three quantities in one sentence, each with its comparison** — Claude's output per turn (1.34×), the user's turns (1.53×), extended thinking (34% versus 31%), all relative to the bottom tercile, with the table pointed at. The three are chosen so that two of them are about the *human's* behaviour, which is what the argument needs.
3. **The joint reading, marked as the point** — "Crucially, these move together: more production from Claude does not mean less from the user."
4. **The economic interpretation, as a conditional whose antecedent is not measured** — "**If** the human remains involved in the highest-value tasks, the pattern **looks more** labor-augmenting than labor-displacing." Two hedges on one clause: an if, and "looks more … than". The report does not claim augmentation; it claims the pattern resembles it, conditional on something it has not shown (that involvement persists).
5. **The lesser claim, scoped** — "It also shows that, **to some extent**, more valuable outputs cost more."
6. **The hand-off to the next section.**

Compare the September 2025 close, which used the same if-then form for its stakes paragraph. **This is the house form for converting a descriptive pattern into an economic claim: state the joint movement, then the conditional, then name the unmeasured antecedent.**

### Chapter 2, Finding 7 — autonomy is higher on Claude Code, and why

> We measure this on a 1-5 scale, from "none" to "extreme." Tasks that are easy to describe or specify involve little autonomy: the lowest-autonomy outputs are math or calculations, translations, and Q&As. High-autonomy tasks are those that require selection among many possible choices, e.g., creating apps and websites, games, or presentations. Such work, which requires sustained judgment, has historically been difficult to automate. By comparing the level of autonomy in Claude chat and Cowork to Claude Code, we show that is starting to change.

> Across almost all types of outputs (26 of 31 outputs shown) the level of AI autonomy is higher on Claude Code than chat or Cowork.[4] For example, conversations producing scripts and code snippets involve 0.53 points more autonomy (on average, on the 1-5 scale) when created with Claude Code than conversations producing the same output on chat or Cowork. Across all conversations the average difference in autonomy is 0.37 points, and it has two main sources.[5]

> Approximately two thirds of the difference is explained by the same tasks being executed with more delegation on Claude Code. Blog posts and articles illustrate this: the requests and tasks behind them are similar on the two surfaces, but the way people work with Claude differs sharply. The median chat and Cowork conversation producing a blog post or an article involves 13 rounds of back-and-forth, while the median blog-producing Claude Code session contains a single human prompt. The remaining third reflects the different mix of output types across the two surfaces.

And the footnote carrying the exception:

> [5] The largest exception is data and spreadsheets, where Claude.ai conversations involve more autonomy than Claude Code (3.09 vs 2.74). This is mostly compositional: about 70% of the gap reflects a different mix of tasks. On Claude.ai this output leans toward financial modeling and dashboards, where Claude designs the structure; on Claude Code it leans toward structured extraction and tagging, where the specification is precise. Cowork, where data and spreadsheet work is both over-represented and especially autonomous, accounts for part of the Claude.ai lift.

**Annotation.** The construct is defined by its poles and then by *examples at each pole* before any comparison is made, and the definition is anchored to a claim about the world rather than to the scale: "Such work, which requires sustained judgment, has historically been difficult to automate." That sentence is what makes the section economically interesting, and it is the only historical claim in the report — unsourced, unlike September 2025's footnoted diffusion history.

The count is given as a count, not a share: "26 of 31 outputs shown". With 31 categories and a small mean difference, a share would have hidden the five exceptions; the fraction advertises them, and footnote 5 then works the largest one through in four sentences — the values on both surfaces, the share of the gap that is compositional (about 70%), what each surface's version of the category actually contains, and the role of Cowork inside the combined series. **A reported exception that is explained more carefully than the main result is the strongest available signal that the main result was examined.**

The decomposition is stated in words rather than in a table ("Approximately two thirds… The remaining third…") and is illustrated with the single most vivid comparison in the report: 13 rounds of back-and-forth versus a single human prompt, for the same output type. Medians, both sides, one sentence. The number that makes the abstract claim ("more delegation") concrete is a count of turns, not a score on the 1–5 scale.

### Chapter 2, Finding 8 — the model-choice rebuttal

> One might suspect this difference simply reflects model choice. Claude Code sessions run on the most capable models far more often (54% are served by Opus, against 10% of chat and Cowork conversations). However, the gap persists when we compare conversations served by the same model. For example, among conversations using Sonnet, Claude Code sessions still show 0.26 points more autonomy, suggesting that the product used is likely more important than the underlying model.

**Annotation.** Four sentences: the alternative explanation, stated in the reader's voice ("One might suspect"); the fact that makes it plausible, quantified on both sides; the test; the residual effect after the test, with the conclusion double-hedged ("suggesting that the product used is **likely** more important"). The magnitude after conditioning (0.26 points) is given beside the unconditional magnitude (0.37 points), so the reader can see how much of the gap the confound absorbed. **This is the September 2025 classifier footnote done properly and in the body: name the threat, report the conditional estimate, and give both numbers so the reduction is visible.**

### Chapter 2, Finding 9 — autonomy and compute move together

> Stepping back from the surface comparison, the output types where users delegate the most are the same ones that consume the most compute: across artifacts, mean autonomy and median token use rise together (r = 0.68 on chat and Cowork; Appendix Figure A.2).

**Annotation.** One sentence, one correlation, with the unit of analysis named ("across artifacts" — so n is roughly 31, not millions of conversations), the sample named ("on chat and Cowork") and the exhibit outsourced to the appendix. No interpretation offered. Naming the unit is what stops a reader from mistaking a correlation across 31 category means for a correlation across conversations, and it is the single most common failure in this kind of sentence.

### Chapter 2, Finding 10 — reading level

> For each conversation, a classifier estimates two reading levels—one for the user's prompt, one for Claude's response—expressed as the years of education needed to understand the text.[6] We find that reading level varies widely depending on artifact type. An average query resulting in an academic paper would require more than 16 years of education, roughly equivalent to bachelor's level, and 15% of these conversations are at PhD level or above (20 or more years of education). On the other end of the spectrum are conversations resulting in recipes or guidance, where fewer than 10 years of education are required to understand the prompt.

> In general, artifact types with higher-reading-level outputs also have higher-reading-level prompts (a correlation of 0.87 across conversations). However, we also observe that in almost every category, Claude's output is at a higher comprehension level than the prompt, by roughly one year of education on average. The gap is widest where users describe something to be built, such as image and graphics (+2.6 years), games (+1.9), and apps and websites (+1.7). Some of the gap may simply be register; prompts are often terse and informal, while Claude tends to reply in polished prose. However, the gap is near zero for audience-facing writing (blogs −0.1, academic papers +0.0, email +0.3), possibly because prompts typically draft language or source material written in the same register as the intended output.

**Annotation.** The scale is translated into the reader's units twice ("roughly equivalent to bachelor's level"; "20 or more years of education" for PhD), which is necessary because "years of education" is a classifier output, not a measurement of anybody's schooling. The correlation is again given with its unit ("across conversations" — here the unit is the conversation, and the contrast with the previous finding's "across artifacts" is exact and deliberate).

The passage's real interest is its treatment of a mechanical explanation for its own headline. The finding is "Claude answers above the level it was asked". The obvious objection — that this is a stylistic artefact of prompts being terse — is raised by the authors ("Some of the gap may simply be register"), and then answered with a *within-sample contrast that the objection predicts*: if register drives the gap, the gap should vanish where prompts are already in the target register, and the report shows exactly that ("the gap is near zero for audience-facing writing (blogs −0.1, academic papers +0.0, email +0.3)"). The alternative explanation is not rebutted; it is *located*, and the sign pattern is used as evidence about where it applies. Three values are given including a zero and a negative, which is what makes the pattern credible.

"possibly because prompts typically draft language or source material written in the same register as the intended output" is conjecture, marked, and carries no evidential weight in the paragraph. The observation/conjecture boundary in this passage is the cleanest in the report.

### Chapter 3, opening — the survey, its linkage and its two-sided result

> The first two chapters show how people use Claude, but don't give much insight into the ways people experience AI at work—how they expect their jobs and workplaces to change, how they feel about AI's current and potential impact, and what they hope for from the technology. Our interviews with 81,000 Claude users, conducted in December 2025 with Anthropic Interviewer, gave a picture: respondents reported large productivity gains, but also expressed worry about displacement. Those worries were concentrated among early-career workers and occupations where we observe Claude doing the most work.[1]

> In April 2026, we launched the Anthropic Economic Index Survey to build on this work. The survey allows us to ask people directly about their experience with AI and work, and to explore how responses vary with Claude usage. We link survey responses to usage data from mid-May to early June using privacy-preserving methods. To characterize each respondent's usage patterns, we randomly sample up to 20 sessions per person within this time window (across Claude.ai, Cowork, and Claude Code, so that the mix of sessions reflects each person's typical usage across surfaces). We exclude respondents with fewer than five sessions to reduce sampling noise. Our final linked sample consists of about 9,700 survey respondents.

> We find that most respondents expect significant AI progress over the next year. While people's perception of AI capabilities depends on their experience, where they live, and how exposed their job is to AI, their expectations about the pace of future progress are strikingly uniform, consistent with a "rising tide," in which AI capabilities improve broadly.

> Views on what that progress means for their own careers are less uniform. Early-career workers report that AI can do the highest share of their work and express the most concern about job loss. Yet—contrary to a common concern—the people who delegate to Claude the most are the *most* optimistic about their future labor market outcomes, and feel their skills are growing in value. And despite (or perhaps because of) their proximity to AI's frontier, the average respondent's hopes for the next decade center not on replacement but on collaboration. They hope AI can preserve meaningful work and automate the drudgery, and that its gains will be shared widely.

**Annotation.** The sample construction is in the body, in five consecutive sentences, and every design choice comes with its reason: the linkage window, the cap of 20 sessions per person *with the reason for the cap* ("so that the mix of sessions reflects each person's typical usage across surfaces"), the exclusion rule *with its reason* ("to reduce sampling noise"), and the resulting n. This is the most transparent sample paragraph in the corpus and the one to imitate — September 2025 put the equivalent in footnote 2 of two different chapters.

The preview then does something the usage chapters never do: it states the result as a *tension between two of its own findings* and marks both sides. Early-career workers report the highest exposure and the most worry; heavy delegators are the most optimistic. "Yet—contrary to a common concern—" tells the reader that the second finding cuts against a prior the reader is assumed to hold, and the italicised "*most*" is the only emphasis in the paragraph. Nothing here is causal; every verb is a verb of reporting ("report", "express", "are", "feel", "hope").

### Chapter 3, Finding 1 — who responded, stated before any result

> The Economic Index Survey is not representative of the general population. We reach a random sample of Claude users, there may be selection in who completes the survey, and we filter out infrequent users from our analysis. Figure 3.1 shows the occupational mix of survey respondents (orange) alongside US employment (grey). Computer and Mathematical occupations are the most heavily over-represented, making up roughly 30% of survey respondents—comparable to their share of Claude usage, but far above their 4% share of US employment. Management, at 23% of respondents,[2] is also heavily over-represented relative to its 7% employment share, even though it accounts for only 4% of sessions. This gap is consistent with managers using Claude for tasks other than management itself: in the survey, judgment and management are named by many respondents (especially those with more experience) as capabilities AI lacks. Physical occupation categories like Transportation & Material Moving, Food Preparation & Serving Related, and Construction & Extraction are all under-represented in the survey, as they are in Claude sessions as well.

**Annotation.** **The limitation is the section's first sentence, in its own paragraph, unhedged, and it names all three of its sources** — user-base selection, response selection, and the analyst's own exclusion rule. No other finding anywhere in the report opens this way, and the reason it works is that the whole chapter's external validity turns on it. A survey chapter that puts this paragraph anywhere else is hiding it.

Then the report's most economical use of three-way comparison: for each occupation group, the share of respondents, the share of US employment, and the share of Claude sessions. Computer and Mathematical: over-represented relative to employment, in line with usage. Management: over-represented relative to *both*, and the gap between respondent share (23%) and session share (4%) is the interesting one. Rather than leave it as sampling noise, the report reads it as a substantive finding about what managers use Claude for, and supports that reading with a *different item in the same survey* ("judgment and management are named by many respondents… as capabilities AI lacks"). Two measurements from the same instrument, used to interpret each other, with the inference marked as consistency rather than proof ("This gap is **consistent with** managers using Claude for tasks other than management itself").

The under-represented groups get the same treatment as the over-represented ones, and the closing clause does the work a limitations section would: "as they are in Claude sessions as well" — the survey's skew is the product's skew, not an artefact of the survey.

### Chapter 3, Finding 2 — reported and anticipated exposure

> Research on AI impacts often focuses on occupational exposure, or what share of tasks within a given job are doable with AI. In prior work, we constructed a measure of *observed exposure*, which captures the share of occupational tasks we already see being done with Claude. We compared it to a commonly used measure of *theoretical exposure*, or the share of occupational tasks that a large language model could theoretically do.

> Another way to understand occupational exposure is to simply ask people how much of their job AI is capable of doing. We asked respondents what share of their work tasks AI could do entirely on its own today (hereafter *reported exposure*), and what share they expect it to handle in 12 months (*anticipated exposure*), with the option to select from 5 bands ranging between "almost none" and "nearly all." Close to 6 in 10 respondents chose a higher band for next year than for today. Over a third expect AI to be able to do most or nearly all of their work tasks next year (Figure 3.2).

**Annotation.** Two new constructs are introduced by italicising them at the point of definition and by positioning them against two existing ones — the report's own *observed exposure* and the literature's *theoretical exposure*. Four measures of the same underlying quantity, named and distinguished before any of them is plotted: this is the section's entire contribution and the naming does most of the work.

The survey item is quoted in substance, not paraphrased — "what share of their work tasks AI could do **entirely on its own** today" — which matters, because the answer means something different if the phrase is dropped. But the five bands are only *named* at their endpoints ("ranging between 'almost none' and 'nearly all'"); their numeric definitions appear nowhere in the prose and only inside Figure 3.2 as axis labels. The body then says "Over a third expect AI to be able to do **most or nearly all** of their work tasks" — a claim that cannot be interpreted without the band cut-offs, which the reader can only get from the image (and, indirectly, from footnote 4's "at least 60% of one's work tasks"). **If a finding is stated in the words of a response scale, the scale's numeric definition belongs in the prose or the caption, not in the chart.**

"Close to 6 in 10" and "Over a third" — two coarse fractions rather than percentages, appropriate for a within-person comparison of ordered bands.

### Chapter 3, Finding 3 — whether stated exposure lines up with measured exposure

> Figure 3.3 compares reported and anticipated exposure to observed and theoretical exposure. We ask whether what people report and anticipate AI can do lines up with the observed and theoretical exposure measures across occupations, and whether respondents whose occupations score higher on observed or theoretical exposure expect faster progress over the next year. On the first question, the answer is yes: reported exposure (grey dots) is positively correlated with both observed and theoretical exposure. On the second, the answer is no: the best-fit lines for reported and anticipated exposure 12 months from now (orange dots) are essentially parallel, meaning that people in roles with high observed or theoretical exposure expect roughly the same *increase* in the share of their work tasks AI can do over the next year as those in roles with less observed and theoretical exposure.[4] In other words, a software engineer and a construction manager anticipate roughly the same increment of progress within their profession.

> It is also worth noting that reported exposure systematically exceeds observed exposure. One explanation for this is that not everybody does every task in an occupation, and our survey disproportionately reaches those who use AI more.[5] Analogously, since theoretical exposure is an upper bound on what is possible instead of a measure of current use, theoretical exposure systematically overstates reported exposure.

And the two footnotes that carry the measurement caveats:

> [4] Because responses are binned—so the lowest possible coded response exceeds zero, and the highest possible response falls short of one—the slopes in this figure are biased towards zero. As a result, we interpret the comparison of slopes qualitatively rather than as precise estimates. However, the patterns (positive slopes and close to parallel lines) are robust to instead estimating the relationship using an indicator for reporting that AI can do at least 60% of one's work tasks, which is unaffected by midpoint coding.

> [5] The binned response scale likely also plays a role: because midpoint coding pulls reported task shares away from the extremes, observed exposure will tend to look as though it understates AI's capabilities in the least-exposed occupations and overstates them in the most-exposed ones, even absent any substantive difference.

**Annotation.** **Two questions posed explicitly, then answered "yes" and "no" in that order.** This is the clearest question-and-answer construction in the corpus: the design is stated, the two hypotheses are separated, and each gets a one-word verdict followed by the evidence that supports it. The null result is given the same weight and the same sentence length as the positive one, and it is then translated into a sentence a reader can picture: "a software engineer and a construction manager anticipate roughly the same increment of progress within their profession."

The evidence for the null is a comparison of slopes read off a scatter, and the report says so in the weakest available terms — "essentially parallel", "roughly the same" — before footnote 4 states why a precise version is unavailable (binning biases slopes toward zero), declares the intended standard of interpretation ("we interpret the comparison of slopes **qualitatively** rather than as precise estimates"), and reports a second specification that is immune to the problem and agrees. **That is the correct anatomy of a null: state the pattern, state why the estimate is not precise, state what you will and will not conclude from it, and report the check that does not share the flaw.** What is missing is the thing our own posts must supply: a minimum detectable difference in slopes. "Essentially parallel" is not a bound.

The second paragraph handles a level discrepancy between two measures of the same thing without resolving it: reported exposure exceeds observed exposure, two explanations are offered (task heterogeneity within occupations; selection into the survey), a third mechanical one is put in footnote 5 (midpoint coding), and the ordering relationship between all three measures is then stated as a chain — theoretical > reported > observed. Naming the direction of each bias, and never claiming a preferred measure, is what keeps the section honest.

### Chapter 3, Finding 4 — exposure against GDP, experience and automation share

> We also examine how perceptions of AI's current and future capabilities relate to the characteristics and usage patterns of respondents. The left panel of Figure 3.4 shows that perceptions of AI's capabilities are negatively correlated with country GDP:[6] The average share of tasks people report AI can do for them now is about 10 percentage points lower among high-income countries. This pattern is consistent with the possibility that AI substitutes for a larger share of the tasks that workers in lower-income countries do day-to-day, even if occupation-level exposure metrics—which tend to be higher in advanced economies—suggest otherwise. Indeed, the IMF has noted that while advanced economies face broader AI exposure overall, workers in lower-income countries may have less access to the complementary skills and infrastructure that allow AI to augment rather than replace their work. In earlier work we documented that lower-income economies tend to use Claude in more automated ways even when adjusting for differences in task mix.

> The middle panel shows that reported and anticipated exposure are also negatively correlated with years of work experience.[7] People with at least 15 years of experience put that share of tasks AI can do roughly 10 percentage points lower than those in their first year of work. We find evidence that this may be because experienced workers have accumulated tacit or context-specific expertise that is difficult for an AI to mimic. In follow-up questions, we asked people what tasks they thought AI would never be able to do and why; the most common responses emphasized that AI lacks the judgment, contextual awareness, and situational reasoning that their work requires. Respondents, and disproportionately those with at least 15 years of experience, also pointed to the relational and interpersonal dimensions of their jobs—building trust and managing people—as things AI cannot replicate.

> As with occupational exposure to AI, we find that perceptions about future improvements in AI capabilities are essentially uncorrelated with GDP per capita and years of experience. The expected share of tasks that AI will be able to do in 12 months is uniformly higher than perceptions about AI's capabilities today.

**Annotation.** Three panels, three paragraphs, one per panel, each naming the panel it describes. Both gradients are quantified in the same unit and at the same coarseness — "about 10 percentage points lower among high-income countries", "roughly 10 percentage points lower than those in their first year of work" — with the comparison groups named as the endpoints of the range rather than as coefficients. Reporting an endpoint contrast instead of a slope is the right choice for a binned survey outcome and it is consistent across both panels.

The GDP paragraph is the report's only extended piece of external reconciliation. The finding runs against occupation-level exposure measures, and the report says so in the same sentence ("even if occupation-level exposure metrics—which tend to be higher in advanced economies—suggest otherwise"), then cites an outside institution for the mechanism, then cites its own previous wave for a consistent pattern in behaviour rather than perception. Three kinds of support for one interpretation, each marked for what it is, and the interpretation itself hedged at the top: "This pattern is **consistent with the possibility** that…".

The experience paragraph does something rarer: **it supports a conjecture about a quantitative gradient with open-ended evidence from the same instrument.** "We find evidence that this **may be because** experienced workers have accumulated tacit or context-specific expertise" is followed by what respondents actually wrote — judgment, contextual awareness, situational reasoning, trust, managing people — and by the note that the experienced sub-group emphasised these disproportionately. The mechanism is not tested; the report is explicit that it is offering a reason people gave, not a reason it has identified.

The third paragraph reports the uniformity result twice over ("essentially uncorrelated with GDP per capita and years of experience"; "uniformly higher") and this is the finding the Introduction called a "rising tide". Note that a null is being asked to carry a positive interpretation — expectations are uniform, therefore beliefs about progress are broad-based — and the report never states a bound on how uniform "essentially uncorrelated" is.

### Chapter 3, Finding 5 — automation share and what it predicts

> We next examine the relationship between how people interact with Claude and their current perceptions of Claude's capabilities. As with past reports, we distinguish between "automation" and "augmentation" modes of collaborating with Claude. We identify conversations as automated when Claude is asked to complete a task with little to no input from the user. Concretely, automation share is the share of conversations whose pattern is either directive ("translate this document") or a feedback loop ("edit this email…make it more casual").[8]

> The right panel of Figure 3.4 shows that reported and anticipated exposure rise with automation share. This could be because delegation is informative about capabilities—people who hand over entire tasks observe directly what AI can complete on its own—or because people who already believe AI can do their work are the most willing to hand it over. The same patterns hold when we replace automation share with the share of sessions devoted to work tasks, or the share conducted in Claude Code.[9]

And the footnote that reports what the robustness check costs:

> [9] Work share and Claude Code share are both positively correlated with automation: Claude Code is an agentic tool whose sessions are on average more automated than those on Claude.ai, and work sessions likewise skew more automated than personal ones. Work usage also matters directly—the survey asks about work tasks, so people who use Claude for work may mechanically expect it to do a larger share of their work tasks. Conditioning on these measures therefore attenuates the relationship between automation share and task shares (today, in 12 months, and the change), but all three relationships remain positive and statistically significant.

**Annotation.** The construct is defined three times in four sentences, at three levels of precision: in words ("Claude is asked to complete a task with little to no input from the user"), in the taxonomy ("either directive or a feedback loop"), and by example inside the taxonomy ("translate this document"; "edit this email…make it more casual"). Footnote 8 then lists all five collaboration modes with their one-line definitions. This is the terminology discipline `/mnt/memory/standards/terminology.md` describes: automation is a *share over two of five patterns*, never a pole, and the report's own examples make the distinction between automation and autonomy legible — "translate this document" is the directive example here and the low-autonomy example in Chapter 2.

The result gets two candidate mechanisms and no adjudication — "This could be because delegation is informative about capabilities… or because people who already believe AI can do their work are the most willing to hand it over" — which is the September 2025 fork construction (state what would follow from each, choose neither). The difference is that here the fork is about the direction of causation between two measured variables, which is the harder case and the one where a fork is most honest.

Footnote 9 is the model for reporting a robustness check that *changes* the estimate: it names why the alternative regressors are correlated with the main one, identifies a mechanical channel that would produce the relationship without any belief effect ("the survey asks about work tasks, so people who use Claude for work may mechanically expect it to do a larger share"), and then states plainly that conditioning "**attenuates** the relationship… but all three relationships remain positive and statistically significant." Attenuation reported rather than robustness declared.

### Chapter 3, Finding 6 — expectations about jobs

> We also ask how people think their jobs will change in the next 12 months. More than a third of respondents said it was likely or very likely that responsibilities would significantly change (for themselves, a peer, a junior colleague, and a senior colleague). 10% rated losing their own jobs as likely or very likely. This is slightly below the annualized hazard rate of losing a job in the US;[10] however, since our respondents skew toward knowledge workers in stable employment (a group that plausibly faces below-average separation risk at baseline), this may still indicate elevated perceived risk. When asked an open-ended question about what was driving their forecasts, 38% of the respondents who rated their job loss as likely or very likely attributed their forecasts to AI.[11] Notably, respondents were on average more worried about job loss for others than for themselves.[12] Respondents were especially worried about job loss for their junior colleagues, with over one third stating that the probability of a junior colleague losing their job in the next year was over 60%. Respondents were also more concerned about job loss (for everyone) in lower-income countries.

And the three footnotes it leans on:

> [10] The US layoffs and discharges rate (BLS JOLTS, total nonfarm, seasonally adjusted) averaged ~1.1% of employment per month over the 12 months through April 2026, amounting to a ~13.4% annualized sum, so 10% is slightly below the realized annual incidence of involuntary separation events.

> [11] This question was asked about the job change forecast and job loss forecast together. The 38% is therefore an upper bound on the share of people who attribute their own job loss forecast to AI.

> [12] This mirrors a familiar pattern of people rating their own circumstances more favorably than other people's. A similar phenomenon was observed during Covid, when self-reported financial well-being exceeded perceptions about the national economy.

**Annotation.** The passage's central problem is that a stated probability of job loss means nothing on its own, and the report solves it the way an economist would: **benchmark the survey number against the realised rate in official statistics, then explain why the comparison does not settle the question.** "This is slightly below the annualized hazard rate of losing a job in the US; however, since our respondents skew toward knowledge workers in stable employment (a group that plausibly faces below-average separation risk at baseline), this may still indicate elevated perceived risk." One sentence contains the benchmark, the direction of the raw comparison, the selection argument that reverses its meaning, and a hedge on the conclusion. Footnote 10 then shows the arithmetic and names the series, so the benchmark is reproducible.

Footnote 11 is the most self-denying footnote in the report: the 38% is disclosed as an upper bound, because the survey item asked about two forecasts at once. **Reporting the exact reason a number overstates what the sentence claims, in the footnote attached to that number, is the discipline our claims list exists to enforce.**

Footnote 12 anchors the own-versus-others asymmetry to a known phenomenon rather than presenting it as a discovery. And the junior-colleague finding is the one place the chapter reports a threshold rather than a mean ("over one third stating that the probability… was over 60%"), which is what the response bands support.

### Chapter 3, Finding 7 — sentiment rises with automation share

> Are people who use Claude in more automated ways also more worried about losing work? We examine what people said about AI's expected impact over the next year on six dimensions of work: pay, job security, ability to find a new job (economic dimensions) and meaning, autonomy, and human interaction (intrinsic dimensions); and look at how these expectations differ by the automation share of Claude usage.

> Across all six dimensions, people with a higher share of automated sessions feel *more optimistic* about the effect of AI on their job outcomes next year compared to those who use Claude more augmentatively. We saw the largest effects on expectations about positive impacts on future pay and ability to find a job.[13]

> A natural question is why automated usage and sentiment move together. It's possible that this relationship is explained by selection, that the people most enthusiastic about AI are also the most willing to hand over entire tasks to it. We can't rule this out entirely, but these estimates don't meaningfully change when we control for user tenure on Claude.ai—which we can think of as a proxy for enthusiasm, because it captures early versus later adopters.

**Annotation.** The question is posed as a question, in the reader's terms, and answered against the reader's expectation. The six outcomes are enumerated once and grouped into two named families (economic, intrinsic) that then do the work in the figure — a two-level taxonomy introduced in a single sentence and never restated.

"Across all six dimensions" is the strongest form of this claim available without individual coefficients: the direction is uniform, and the two largest effects are named rather than quantified in the body. The magnitudes live in Figure 3.6, whose y-axis defines the units the caption does not (see `## Figure captions`).

The third paragraph is the report's second-best piece of causal hygiene. Selection is named as the alternative, stated in plain words, conceded as unresolvable ("We can't rule this out entirely"), and then partially addressed with a proxy whose logic is given ("user tenure on Claude.ai—which we can think of as a proxy for enthusiasm, because it captures early versus later adopters"). The control is not claimed to be adequate; the sentence says the estimates "don't meaningfully change", which is a statement about robustness to *one* proxy for *one* confound. **"We can't rule this out entirely, but…" is the phrase to use when a confound is addressed and not eliminated.**

### Chapter 3, Finding 8 — productivity, learning and skill value

> Another possibility is that people who use AI in more automated ways experience more of its benefits today. Consistent with our previous findings, large majorities of people report productivity gains in speed, scope, and quality of their work (86%, 82%, and 69%, respectively), while 27% report gains through cost savings on services they would otherwise have to purchase.

> In addition to significant productivity gains, the majority of people also report learning more with AI (68%) and feeling like AI has made their skills more valuable (57%). Figure 3.7 shows how these two outcomes vary with the share of automated sessions. We see that the share of people reporting that AI is increasing the market value of their skills rises with automation share, while the share reporting they learn more is roughly flat.

> A commonly voiced concern about delegation is that handing entire tasks to AI means offloading thinking, with gains in output coming at the cost of learning and skill atrophy. We do not see this pattern here: heavier delegators report learning at the same rate as everyone else. However, these are self-assessments, and skills can erode even as they become more valuable and as someone reports learning more, so the data do not rule out skill erosion.

**Annotation.** Four shares in one sentence with the dimensions in the same order as the numbers ("speed, scope, and quality… (86%, 82%, and 69%, respectively)"), and the odd one out given its own clause with its meaning spelled out ("27% report gains through cost savings on services they would otherwise have to purchase"). All four are prefaced "report", and the paragraph is anchored to the earlier wave ("Consistent with our previous findings").

The third paragraph is the most important sentence-level lesson in Chapter 3. A prior concern is stated in the concern-holder's own terms; the data are said not to show it; and then the null is immediately bounded: "**However, these are self-assessments, and skills can erode even as they become more valuable and as someone reports learning more, so the data do not rule out skill erosion.**" The instrument's limit (self-report), the logical gap (erosion is compatible with both reported outcomes), and the conclusion the report declines to draw, in one sentence. **This is the template for writing a null that a referee cannot mistake for a refutation.**

### Chapter 3, Finding 9 — gender differences in usage

> So far we have explored how usage patterns relate to expectations and behavior. Next, we study *who* uses Claude in various ways. The most striking differences are by gender. Women, who make up only 12% of our linked respondent sample, use Claude differently from men. Even after accounting for occupational differences, they are marginally less likely to use Claude for work, their share of sessions in Claude Code is 0.24 standard deviations lower (6.3 percentage points), and their automation share is 0.33 standard deviations lower (7.3 percentage points). Instead, women tend to use Claude more iteratively, and they log more active time on chat than men, a signal of more collaborative engagement.[14]

> [14] While this could be due to substitution between chat/Cowork and Claude Code, the pattern holds even when controlling for Claude Code session share. These patterns also survive controlling for occupation fixed effects.

**Annotation.** The sample share comes first and carries the word "only" — "Women, who make up **only** 12% of our linked respondent sample" — so the reader meets the precision problem before the estimates. Every effect is given twice, in standard deviations and in percentage points ("0.24 standard deviations lower (6.3 percentage points)"), which is the same double-reporting device as September 2025's "increased by 1.3pp, growing from a base of 0.2% to 1.5%": the standardised units make effects comparable across outcomes, the raw units make them mean something. The conditioning is stated before the numbers ("Even after accounting for occupational differences") and again in the footnote, with a second control and a second robustness statement.

"marginally less likely" for the work-use difference, against exact figures for the other two, grades the three findings by strength inside one sentence. The one soft link is "a signal of more collaborative engagement" — active minutes are not a measure of collaboration, and the word "signal" is the only marker that an interpretive step has been taken. Figure 3.8's caption supplies the confidence intervals the prose does not.

### Chapter 3, Finding 10 — what people hope for

> The Anthropic Economic Index Survey surfaces a mix of positive and negative experiences and sentiments with respect to AI, but we end the survey on a hopeful note. The final open-ended question asks respondents to "dream big: what do you hope an economy shaped by AI looks like in ten years?" We ran each survey response through a classifier which tagged responses with relevant themes. We show the top five most commonly cited themes below. Additional descriptions of each can be found in the Appendix.

> The most common theme expressed was one of AI *augmentation* of work. Over half of survey respondents expressed some version of wanting to collaborate with AI on work that feels meaningful, of wanting their career to still matter, and/or hoping that new industries arise and create new job opportunities. Simultaneously, just over half of respondents hoped for AI *automation*—specifically of the tedious parts of their jobs—so they could have more free time and more space for meaning outside of work. The third most common theme, expressed by about one third of survey respondents, was one of shared prosperity: the hope that the economic gains from AI will be widely shared.

**Annotation.** The survey question is quoted verbatim, including its framing instruction ("dream big"), because the framing determines the answers — the same discipline September 2025 applied to the Census BTOS question. The classification step is disclosed in one sentence, and the theme descriptions are outsourced to the appendix.

The two leading themes are the report's own two technical terms — augmentation and automation — italicised, and the finding is that respondents want both: "Over half… wanting to collaborate with AI on work that feels meaningful"; "just over half of respondents hoped for AI automation—specifically of the tedious parts of their jobs". The word "Simultaneously" is the hinge, and it is doing the same job as "Yet" in the chapter preview: telling the reader that two findings which look opposed are held by overlapping majorities. Shares are coarse ("Over half", "just over half", "about one third") and the themes are not mutually exclusive, which the coarseness implicitly concedes and the prose never states. Only three of the five themes are named in the body; the fourth and fifth exist only as labels inside Figure 3.9.

### Survey findings versus usage findings: the grammatical difference

The two kinds of evidence are phrased in consistently different ways, and the difference is worth stating as a rule the report follows without announcing it.

| | usage findings (Chapters 1–2) | survey findings (Chapter 3) |
|---|---|---|
| **subject of the sentence** | the conversation, the task, the artifact, the share — "the tasks skew toward higher-wage occupations", "conversations about building apps use more than three times the tokens" | the respondent — "Over a third expect", "10% rated", "large majorities of people report", "Respondents were especially worried" |
| **main verb** | verbs of measurement and of the world: *is, rise, consume, spike, fall, involve* | verbs of reporting: *report, say, expect, anticipate, rate, express, hope, put* |
| **what the number counts** | conversations, tokens, points on a scale, days | people |
| **denominator named?** | yes, and usually in the same clause ("relative to their overall average", "than on the average day in May", "of the median conversation") | yes, but as a share of respondents, with the sample's non-representativeness carried by the section's opening paragraph rather than by each sentence |
| **precision** | shares to the point, ratios to one or two significant figures | coarse fractions ("6 in 10", "over a third", "just over half") except where a single item is reported ("10%", "38%", "86%, 82%, and 69%") |
| **caveat type** | measurement and inference: classifier coverage, task-to-occupation mapping, geolocation, estimator choice | instrument and selection: who answered, midpoint coding of bands, self-assessment, question wording, upper bounds |
| **causal language** | none; "associated with", "tends to", "rise together" | none; and in addition the direction of causation is explicitly forked twice ("This could be because… or because…") |
| **who is the agent** | Claude and the user, symmetrically ("Claude produces more… users engage more") | the respondent only; Claude appears as the object of expectations |

Two consequences for our own drafting. First, **a survey number and a usage number should never be joined by a verb that suits only one of them**; the report's own best sentence about the two is a comparison of measures, not of facts ("reported exposure systematically exceeds observed exposure"). Second, the report never writes "workers believe X, and they are right/wrong" — it writes what each measure says and how the measures line up. That restraint is what makes Chapter 3 publishable beside Chapters 1–2.

### The report's hedge vocabulary, graded

In descending confidence, as used here: *we find* · *we show* · *the data captures* · *shows a positive relationship* · *we see* · *rise together* · *is consistent with* · *tends to* · *skew toward* · *appears* · *may be because* · *could reflect* · *this could be because … or because* · *it's possible that* · *possibly because* · *we can't rule this out entirely* · *the data do not rule out*. The report never uses *proves*, *demonstrates*, *causes* or *leads to*. Compared with September 2025 it has no bottom rung — no "we speculate", no "more research is needed here" — because the conjectures are all attached to mechanisms rather than to results.

### Claude versus AI across the whole report

- **Title:** "Anthropic Economic Index report: Cadences" — neither word appears.
- **Chapter titles:** "Cadences", "Artifacts", "Perceptions" — none names either.
- **Introduction:** questions and stakes say AI ("how AI mirrors and diffuses into economic life", "how people perceive AI to be changing their work"); measured objects say Claude ("most Claude usage", "Claude sessions", "Claude conversations").
- **Chapters 1–2:** Claude almost throughout, because almost every sentence is a measurement — "Claude usage mirrors the workweek", "conversations mapping to their tasks", "Claude produces more", "Claude's output is at a higher comprehension level than the prompt". The exceptions are the construct names, which say AI: "the level of **AI** autonomy", "**AI** Autonomy is rated on a 1-5 scale".
- **Chapter 3:** AI almost throughout, because almost every sentence is a report of a belief about the technology — "what share of their work tasks **AI** could do", "**AI** lacks the judgment, contextual awareness, and situational reasoning", "**AI** has made their skills more valuable". Claude appears only where usage is measured: "how responses vary with **Claude** usage", "the share of **Claude** sessions classified as automated", "their share of sessions in **Claude** Code".
- **The one sentence that carries both correctly:** "people who use **Claude** in the most automated way expect **AI** to take on more of their tasks in the next year."
- **Captions:** Chapters 1–2 say Claude (or name the surfaces); Chapter 3 says AI wherever the variable is a stated belief and Claude wherever it is measured usage — Figure 3.4's caption does both in one line ("Reported and anticipated exposure … and rise with automated **Claude** use").

**The rule this wave adds to the corpus:** the split is not only question-versus-number, it is *measured behaviour versus stated belief*. Usage is Claude even inside an interpretation; an expectation, a hope or a fear is AI even when the respondent was recruited from Claude's user base.

## Comparisons

Every place a comparison carries a finding, grouped by the dimension compared.

### Month to month, and across the series

> One year ago, most Claude usage took the form of a conversation between a user and an assistant. Today, with the rapid growth of Claude Code and Cowork, Claude sessions increasingly consist of long-running agentic tasks.

> Our new privacy-preserving telemetry, which continuously samples a slice of conversations every day, allows us to study daily and hourly patterns in usage, in contrast to the seven-day samples each previous Economic Index report drew on.

> On April 14, tax-related clusters were eight times as common as on the average day in May and remained about as high on April 15. On April 16, they dropped sharply.

> Share more granular data, breaking out results for chat and Cowork conversations (together, "Claude conversations") and the 1P API, aggregated at a monthly level.

> As these forms change, the user base is shifting as well. Early adopters were highly technical. Our most recent users apply Claude to tasks that command lower wages in the labor market.

**Annotation.** This wave makes no wave-to-wave numerical comparison at all — no V1/V2/V3 notation, no "up from", no share compared to an earlier report. The series comparisons it does make are of three kinds, and all three are about *method or composition* rather than about a level: the product has changed (one year ago versus today), the instrument has changed (continuous sampling versus seven-day samples), and the released data has changed (monthly aggregation, chat/Cowork and 1P API broken out). The one substantive claim about drift in the user base is stated without a number and with its evidence outsourced to the March 2026 report ("Our most recent users apply Claude to tasks that command lower wages in the labor market").

The within-sample month comparison is the one that carries a finding, and its construction is exact: a named day against *the average day of a named month*, with the comparison month chosen because it contains no tax deadline. The ratio (eight times) is given for the peak, the persistence is given qualitatively ("remained about as high"), and the collapse is given qualitatively ("dropped sharply"). **Where a series cannot yet be compared across waves, a within-sample event study against a clean baseline month is the substitute — and the baseline must be named in the sentence, not only on the axis.**

Cost of the missing comparison, for our own work: this report cannot say whether 35% personal use on weekdays is high or low, because no earlier wave measured it and no external benchmark is offered.

### Time of day and day of week

> The share of chat and Cowork conversations categorized as personal use spikes from around 35% on weekdays to just under 50% on weekends during the sample period (Figure 1.1).

> On weekends, the Claude Code usage clusters that fall the most include backend architecture, API debugging, and data storage. Those that increase the most include AI agent design, quant trading, and gaming.

> Across countries, conversations related to starting a business are highest on Saturday and Sunday. However, job application activities drop on the weekend along with other work-related tasks.

> People ask for news at 7 a.m. local time. Business correspondence (e.g., email drafting) traces the arc of the workday, with a slight peak at 10–11 a.m. One of the biggest spikes is recipe requests, which are 2.3 times more frequent at 6 p.m. compared to the average.

> On nights and weekends, when people do turn to Claude for work, the tasks skew toward higher-wage occupations (Figure 1.3). … In contrast, tasks related to jobs in the bottom two quartiles—like telemarketing and clerical work—fall to a smaller share of total conversations.

**Annotation.** Four different baselines are used for four different time comparisons, and each is named where it is used: weekdays (for the weekend shift), a cluster's own overall average (for the hourly figure — "relative to their overall average in global traffic"), weekday working hours (for the nights-and-weekends figure, stated in the caption), and the average day in May (for tax day). **Normalising each series to its own average is what makes nine request clusters with wildly different levels comparable on one grid, and the caption says so rather than leaving the reader to infer it from the dashed line at 1.0.**

The time-of-day comparisons are almost all *within-category, across-hour*, which is the comparison the instrument supports; the report never compares one cluster's level to another's. The one across-group comparison in the chapter — wage quartiles on nights and weekends — is expressed as a change in share relative to weekday working hours, so that the levels, which differ enormously across quartiles, drop out. That is the right transformation and the caption carries it ("the percent change in the share of work-related tasks coming from the specified wage quartile on nights and weekends versus weekday working hours").

### Wages

> For example, marketing managers earn roughly twice as much as editors ($80 vs. $37 per hour) and conversations mapping to their tasks consume approximately 2.5 times as many tokens.

> Pharmacists, for example, earn nearly three times what statistical assistants do ($68 vs. $24 per hour), yet conversations mapped to pharmacist tasks use only about one twentieth as many tokens.

> In conversations mapped to higher-wage occupations, Claude produces more (1.34 times as much output per turn), while users engage more (1.53 times as many turns) and enable extended thinking more frequently (34% of conversations versus 31%; Table 2.4).

> About 44% of the wage gradient in token consumption is explained by output mix—higher wage occupations are more likely to produce compute-intensive artifacts.

> the tasks skew toward higher-wage occupations … tasks related to jobs in the bottom two quartiles—like telemarketing and clerical work—fall to a smaller share

**Annotation.** The wage comparisons follow one template: **two named occupations, their two hourly wages in parentheses, the wage ratio in words, then the outcome ratio in words.** "roughly twice as much… approximately 2.5 times as many tokens"; "nearly three times… only about one twentieth as many". Naming the occupations rather than the quantiles is what makes the comparison stick, and pairing the confirming case with the contradicting case in identical grammar is what stops it from being a sales pitch. Both wage levels are given so the reader can check the ratio.

Three different aggregations of the same wage variable appear in the report — named occupations (Figure 2.3), terciles (Table 2.4), quartiles (Figure 1.3) — each matched to what the comparison needs: individual occupations for illustration, terciles for a mechanism table with six rows, quartiles for a bar chart of change. The unit of the wage is stated once per exhibit and the vintage once per chapter (footnote 1, "BLS OEWS, May 2025 release"). No sentence anywhere says that Claude's users earn these wages: every construction is "conversations **mapped to**" or "tasks related to jobs in".

### Claude conversations against Claude Code against the 1P API

> A similar pattern is present in Claude Code and the 1P API traffic (i.e., API traffic routed directly through Anthropic), though both have lower baseline rates of personal use.

> Chat and Cowork provide more explanations than Claude Code, for example.

> Across almost all types of outputs (26 of 31 outputs shown) the level of AI autonomy is higher on Claude Code than chat or Cowork. For example, conversations producing scripts and code snippets involve 0.53 points more autonomy (on average, on the 1-5 scale) when created with Claude Code than conversations producing the same output on chat or Cowork. Across all conversations the average difference in autonomy is 0.37 points, and it has two main sources.

> The median chat and Cowork conversation producing a blog post or an article involves 13 rounds of back-and-forth, while the median blog-producing Claude Code session contains a single human prompt.

> Claude Code sessions run on the most capable models far more often (54% are served by Opus, against 10% of chat and Cowork conversations). However, the gap persists when we compare conversations served by the same model. For example, among conversations using Sonnet, Claude Code sessions still show 0.26 points more autonomy, suggesting that the product used is likely more important than the underlying model.

> The largest exception is data and spreadsheets, where Claude.ai conversations involve more autonomy than Claude Code (3.09 vs 2.74). This is mostly compositional: about 70% of the gap reflects a different mix of tasks.

**Annotation.** The surface comparison is the spine of Chapter 2 and it is built in five moves that our posts should copy wholesale: (i) the aggregate difference with its count of categories (26 of 31); (ii) one category worked through in points on the scale (0.53); (iii) the all-conversation average (0.37) decomposed into within-task delegation (two thirds) and composition (one third); (iv) the same comparison expressed in a unit nobody can misread (13 turns versus one prompt); (v) the confound — model choice — quantified, conditioned on, and the residual reported (0.26).

Note that the surfaces are held to different sample definitions in different chapters and the report keeps saying which: Figure 1.1 spans four surfaces, Chapter 2's artifact analysis is chat and Cowork only, the autonomy comparison adds Claude Code "from the same period", the 1P API's artifact mix is pushed to the appendix, and footnote 3 of Chapter 1 states that the 1P API "does not include Claude Code". Five different scope statements for one set of surfaces, each attached to the claim it governs.

Two frictions worth flagging. First, the exception footnote reverts to "Claude.ai" for the combined chat-and-Cowork series (the web version fixes this) — the report's new umbrella term is not yet stable in its own footnotes. Second, Figure 1.1's caption lists four surfaces while the exhibit draws three lines; the caption's list and the exhibit's legend do not correspond (see `## Figure captions`).

### Survey against usage, and survey against other exposure measures

> Computer and Mathematical occupations are the most heavily over-represented, making up roughly 30% of survey respondents—comparable to their share of Claude usage, but far above their 4% share of US employment. Management, at 23% of respondents, is also heavily over-represented relative to its 7% employment share, even though it accounts for only 4% of sessions.

> Physical occupation categories like Transportation & Material Moving, Food Preparation & Serving Related, and Construction & Extraction are all under-represented in the survey, as they are in Claude sessions as well.

> On the first question, the answer is yes: reported exposure (grey dots) is positively correlated with both observed and theoretical exposure. On the second, the answer is no: the best-fit lines for reported and anticipated exposure 12 months from now (orange dots) are essentially parallel…

> It is also worth noting that reported exposure systematically exceeds observed exposure. One explanation for this is that not everybody does every task in an occupation, and our survey disproportionately reaches those who use AI more. Analogously, since theoretical exposure is an upper bound on what is possible instead of a measure of current use, theoretical exposure systematically overstates reported exposure.

> The right panel of Figure 3.4 shows that reported and anticipated exposure rise with automation share.

> We found that our survey respondents use AI for more than we give it credit for—they report AI can do a higher share of their work than the observed exposure measure for their occupation would suggest.

**Annotation.** This is the comparison the wave exists to make, and its discipline is that **the survey is never used to validate or to correct the usage data; the two are compared as measures, and every discrepancy is given a direction and a candidate cause.** Three-way comparisons (respondent share / employment share / session share) rather than two-way. An ordering of four measures (theoretical > reported > observed, with anticipated above reported by construction) rather than a preferred one. A correlation reported between a stated belief and a measured behaviour (exposure against automation share) with the causal direction explicitly forked.

The Discussion's version of the finding — "our survey respondents use AI for more than we give it credit for" — is the one place the report lets a survey number arbitrate against its own usage measure, and the sentence is carefully built so that the subject is the respondents' report, not the world: "**they report** AI can do a higher share of their work than the observed exposure measure for their occupation would suggest."

### Small vivid comparisons

> recipe requests, which are 2.3 times more frequent at 6 p.m. compared to the average

> On April 14, tax-related clusters were eight times as common as on the average day in May

> conversations about building apps use more than three times the tokens of the median conversation. On the other end of the spectrum, a typical explanation uses about a fifth of the tokens of the median conversation

> The median chat and Cowork conversation producing a blog post or an article involves 13 rounds of back-and-forth, while the median blog-producing Claude Code session contains a single human prompt

> An average query resulting in an academic paper would require more than 16 years of education, roughly equivalent to bachelor's level

> a software engineer and a construction manager anticipate roughly the same increment of progress within their profession

**Annotation.** Six devices, all converting a quantity into something a reader can hold, and five of the six state the baseline in the same sentence as the multiple. The sixth ("13 rounds of back-and-forth… a single human prompt") has no baseline because it needs none: the comparison *is* the two values. The last one is not a number at all — it is a null result rendered as two people — and it is the most memorable sentence in Chapter 3.

## Figure captions

Eighteen figures and one table. PDF form throughout: **bold "Figure N.N: sentence-case declarative title." with a terminal period**, running on directly into a plain-roman gloss of one to five sentences, on the same line. The sole exception is Figure 1.2, whose title takes no period. No "Source:" line anywhere and no "Note:" anywhere — provenance is a clause inside the gloss ("Wage quartiles are calculated using BLS data"; "from OEWS"). Web form: same words, bold title on its own line without the period, gloss italicised beneath.

Seventeen of the nineteen exhibits carry an **in-image chart title** in large black display type (e.g. "The workweek", "Tax day in Claude traffic"), two of those with an in-image subtitle (Figures 3.2 and 3.4). Only Figure 2.5 and Table 2.4 have none. These are part of the graphic, not the caption; they are quoted below marked as such, because the division of labour is the pattern: **the in-image title says what the exhibit is about in three or four words, the caption says what it is made of, and in this report the axis label often says what the unit is when the caption does not.**

### Chapter 1

> **Figure 1.1: Personal conversations increase on the weekend.** Daily share of conversations that are personal use across Claude.ai, Claude Desktop, Claude Code, and 1P API. Saturday and Sunday are shaded grey.

In-image chart title: "The workweek". Axis: "Share of conversations that are personal use (%)"; x-ticks are Monday dates; series labelled at the right-hand end of each line, "Claude.ai", "Claude Code", "1P API"; weekend bands annotated "Sat-Sun".

**Annotation.** Declarative title stating the direction of the finding, then the unit and the surfaces, then the one reading convention the exhibit needs ("Saturday and Sunday are shaded grey"). Two problems worth naming because both are easy to reproduce. **First, the caption lists four surfaces and the exhibit draws three lines** — Claude Desktop is presumably inside the Claude.ai series, as Chapter 1's footnote 2 implies, but the caption does not say so, and a reader matching legend to caption cannot tell. A caption that enumerates sources must enumerate the *series*. **Second, no sample window.** The dates exist only as axis ticks, and Chapter 1 gives them nowhere else; an exhibit lifted without its axis loses the period entirely. Our captions state the window in the gloss.

> **Figure 1.2: Request clusters over the course of the day**
> Normalized hourly share of conversations that fall into different request clusters, restricted to Claude chat and Cowork data.

In-image chart title: "Daily rhythms". Nine panels, each titled with its request cluster; shared y-axis label "Rate vs. own average"; x-ticks at three-hour intervals from "12am"; a dashed reference line at 1.0 in every panel.

**Annotation.** The one descriptive rather than declarative title in Chapter 1, and the only one without a terminal period — the exhibit has nine findings, so no single sentence could head it. The gloss carries the two things a reader must have: the normalisation ("Normalized hourly share… relative to their overall average", spelled out in the body) and the sample restriction ("restricted to Claude chat and Cowork data"). The baseline is drawn as a dashed line at 1.0 in each panel, which is the same device as the AUI's line at 1 in September 2025: **put the null value on the exhibit and the prose never has to repeat it.** What the caption does not say is which nine clusters were chosen, or why, out of a taxonomy with hundreds.

> **Figure 1.3: Change in share of work-related conversations during nights and weekends, split by occupation wage quartile.** Each bar shows the percent change in the share of work-related tasks coming from the specified wage quartile on nights and weekends versus weekday working hours. Wage quartiles are calculated using BLS data, weighted by number of transcripts.

In-image chart title: "Overtime". Axis: "Change in share of work conversations: nights & weekends vs. workday"; x-axis "Wage quartile" with ticks "Q1"–"Q4"; each bar carries a printed data label.

**Annotation.** The most complete gloss in the chapter: what each bar is (a percent change), the two periods being differenced ("nights and weekends versus weekday working hours"), the classification source ("BLS data") and the weighting ("weighted by number of transcripts"). Four facts, three sentences, no wasted words. The weighting clause is the one most drafts would omit and the one that determines what the quartiles mean.

Note that **the magnitudes of this finding exist only as data labels inside the image.** The body says the tasks "skew toward higher-wage occupations" and that the bottom two quartiles "fall to a smaller share"; no number appears in the prose or the caption. Per `room/director-2026-09-16-alt-text-ruling.md` the printed values are not recorded here. For our own posts the rule runs the other way: if a figure's bars are labelled, the body sentence carries at least the two extreme values.

> **Figure 1.4: Tax-related conversations spike just before the US filing deadline.** Share of conversations related to taxes in the US and the rest of the world.

In-image chart title: "Tax day in Claude traffic". Axis: "Tax-related share of conversations, relative to own May average"; series labelled "United States" and "Outside the US"; a dashed vertical rule annotated "Apr 15: US deadline".

**Annotation.** A short caption that works because the exhibit does the rest: **the normalisation the body's "eight times as common as on the average day in May" depends on is in the axis label, not the caption**, and the event date is annotated on the plot rather than described. The gloss's only job is to say that there are two series and what distinguishes them ("in the US and the rest of the world") — which is the comparison that turns a spike into an identification: the rest of the world is the control group, and the caption names it without calling it one.

### Chapter 2

> **Figure 2.1: Claude's outputs.** The share of conversations with a specific output. The figure shows the twelve most common output types in Claude conversations. The 1P API mix is in the Appendix.

In-image chart title: "Claude's outputs". Axis: "% of conversations"; horizontal bars, each labelled with its share; the catch-all bar is drawn in grey and labelled "No clear output" while the other bars are coral.

**Annotation.** Three sentences: the measure, the truncation rule ("the twelve most common output types") and a pointer to where the other surface's version lives. Stating the truncation is essential for a bar chart of a 30-plus-category taxonomy, and it is stated as a count rather than as a threshold. The colour convention — grey for the residual category, coral for real categories — is the exhibit's most useful feature and the caption does not mention it; nor does it reconcile the bar label "No clear output" with footnote 2's term "None". **Where a residual category is drawn differently from the others, say so in the caption and use one name for it.**

> **Figure 2.2: Share of artifacts by use case.** Share of conversations with a specific output classified by its purpose into work, personal, and coursework.

In-image chart title: "What each output is used for, Claude chat and Cowork". Axis: "Share of conversations (%)" running 0–100; stacked horizontal bars ordered from most personal to least; legend "Work / Coursework / Personal"; a dashed vertical rule at 50.

**Annotation.** The caption is one sentence and does not earn its exhibit. Missing: that the bars are stacked to 100% (so the three shares are exhaustive), that the rows are sorted by personal share (so the ordering is not alphabetical or by size), that the dashed line marks 50%, and the sample restriction — which is in the in-image title ("Claude chat and Cowork") but not in the caption. The body supplies none of these either. Compare September 2025's Figure 2.7 gloss, which spent one sentence each on panel logic, share construction, colour and size. **A stacked composition figure needs its sort order and its total in the caption; this one is the corpus's clearest example of what their absence costs.**

> **Figure 2.3: Conversations in higher-wage occupations consume more tokens.** Left panel: Relationship between median wage for a given occupation and the typical (geometric mean) number of tokens in conversations classified to one of the tasks belonging to that occupation, normalized by overall mean. Both variables are represented on a logarithmic scale. Right panel: Distribution of tokens used to generate given artifacts. Black line illustrates the median, box represents p25 and p75, whiskers represent p10 and p90. All numbers are normalized by the overall median number of tokens and presented on the logarithmic scale. Data in both panels is restricted to chat and Cowork and restricted to conversations classified as work-related. Token counts are not adjusted for which model served the conversation.

In-image chart title: "Token usage by occupation and by artifact". Left axis: "Geometric-mean tokens per conversation in the occupation, as a multiple of the overall average conversation", x-axis "Occupation median wage (OEWS)", both log-scaled, a dashed reference line at 1×, a fitted line, bubble area varying by usage, and a handful of occupations labelled by name. Right axis: "Tokens per conversation, as a multiple of the overall median conversation".

**Annotation.** The best caption in the report and the closest to the September 2025 template. Eight jobs done in order: what the left panel relates to what; the estimator named inside the sentence ("the typical (geometric mean) number of tokens"); the normalisation ("normalized by overall mean"); the transformation ("Both variables are represented on a logarithmic scale"); what the right panel shows; **the box-plot's four statistics enumerated** ("Black line illustrates the median, box represents p25 and p75, whiskers represent p10 and p90"); the right panel's own normalisation and transformation; the sample restriction, stated twice in one sentence because there are two restrictions; and a disclosure of what has *not* been adjusted for ("Token counts are not adjusted for which model served the conversation").

That last sentence is the caption's most valuable word-for-word borrowing: **a caption that names the adjustment it did not make tells a referee where to look and costs nine words.** The footnote adds that a price-weighted version gives a similar relationship, so the disclosure is not a loose end.

> **Table 2.4: What accounts for higher token consumption in higher-wage occupations.** Features of conversations that contribute to higher token consumption in conversations mapped to higher-wage occupations. Occupations were grouped into terciles by their median wage, weighted by the number of conversations matched to each. Compute-related measures were normalized by their bottom-tercile's geometric means. E.g. the first row shows that a typical conversation mapped to a top-tercile occupation consumes 2.07 times as many tokens as a typical conversation mapped to a bottom-tercile occupation.

In-image column headers: "Occupation median wage", "Bottom third", "Middle third", "Top third". In-image row labels: "Tokens per conversation", "Turns per conversation", "Tokens per turn", "Claude's response per turn", "Price-weighted compute cost", "Extended thinking enabled (% of conversations)".

**Annotation.** Unlike September 2025, where table captions were a bare noun phrase, this one is the longest gloss in the report and it does four things: names what the rows are (features that contribute), the grouping and its weighting ("grouped into terciles by their median wage, weighted by the number of conversations matched to each"), the normalisation ("normalized by their bottom-tercile's geometric means"), and then **reads one cell aloud as a worked example** ("E.g. the first row shows that a typical conversation mapped to a top-tercile occupation consumes 2.07 times as many tokens as…"). That last device — one value quoted in the caption purely to teach the grammar of the exhibit — is lifted straight from Figure 3.3 of the September 2025 report and is the most transferable caption move in the corpus. Note that the table carries a row the body never discusses ("Price-weighted compute cost"), which is the robustness check footnote 3 promises, sitting in plain sight.

> **Figure 2.5: AI Autonomy by output type.** Average level of AI Autonomy by conversation output and surface. AI Autonomy is rated on a 1-5 scale from "none" to "extreme".

No in-image title. Axis: "Mean AI autonomy in the exchange (1 = none, 5 = extreme)"; a dumbbell per output type with legend "Claude chat and Cowork" / "Claude Code"; rows sorted by Claude Code level; connectors drawn in a contrasting colour where the ordering reverses.

**Annotation.** Two sentences: what is plotted by what, and the scale with both its poles. The scale definition is repeated verbatim from the body two pages earlier, which is the right call — an exhibit on a constructed 1–5 index must carry the index's endpoints. The caption does not say that the rows are sorted by the Claude Code value, nor that the five reversals are colour-coded, and the reversals are precisely the "26 of 31" claim the body makes. **When an exhibit encodes the exception to your finding, the caption should say how to see it.** The capital-A "AI Autonomy" here and lower-case "AI autonomy" in the body are the report's only construct-casing inconsistency; the web page prefers lower case in the title and upper case in the gloss.

> **Figure 2.6: Reading level of user prompts and Claude's responses, by artifact.** Estimated number of years of education needed to understand the user's prompt and Claude's response. Restricted to chat and Cowork.

In-image chart title: "Claude answers above the level it was asked" (identical to the section heading). Axis: "Years of education needed to understand it"; dumbbells with legend "Claude's response (output sophistication)" / "User's request (prompt sophistication)"; two dashed vertical reference lines annotated "HS diploma" and "Bachelor's".

**Annotation.** A descriptive caption under a declarative in-image title: the finding is stated in the graphic, the construction in the caption, and the word "Estimated" concedes in one adjective that the years of education are a classifier's estimate rather than a measurement. The two annotated reference lines are what make an unfamiliar unit readable, and they are in the image rather than the caption — the same pattern as Figure 1.2's dashed 1.0. The legend's parenthetical glosses ("output sophistication", "prompt sophistication") name the constructs the caption does not.

### Chapter 3

> **Figure 3.1: Survey respondents skew heavily toward computer & mathematical and management occupations relative to US employment.** Share of survey respondents reporting their occupation in each of the 22 major SOC groups,[3] compared to each occupation's share of US employment from OEWS.

In-image chart title: "Survey occupational composition vs. US employment". Axis: "% share"; dumbbells per SOC major group with legend "US employment (OEWS)" / "Survey respondents". Footnote 3: "Excludes military."

**Annotation.** A declarative title that names both over-represented groups, and a gloss that does three things in one sentence: the survey measure and how it was obtained ("reporting their occupation" — self-reported, not inferred), the taxonomy and its size ("each of the 22 major SOC groups"), and the benchmark with its source ("share of US employment from OEWS"). **A footnote hanging off a caption to exclude one category ("Excludes military") is the right weight for that kind of scope note.** Worth contrasting with Chapters 1–2, where occupation is *inferred from the task*: here it is what the respondent says they do, and the caption's verb marks the difference.

> **Figure 3.2: Most respondents expect the share of their work tasks AI could do to grow over the next 12 months.** This figure shows the distribution of the share of their work tasks respondents say AI can do today versus in 12 months.

In-image chart title: "Share of work tasks AI could do", subtitle "Today vs. in 12 months". Axis: "% of respondents"; paired bars with legend "Today" / "Expected in 12 months"; x-tick labels give the five response bands with their numeric definitions.

**Annotation.** The caption tells the reader that a distribution is plotted and against what comparison, and that is all it can do in one sentence — but **the five response bands and their cut-offs appear only as x-tick labels inside the image**, and the body's headline claim ("Over a third expect AI to be able to do most or nearly all of their work tasks next year") cannot be interpreted without them. This is the report's clearest case of a definition that belongs in the caption sitting in the chart. The modal verbs also disagree between title and gloss, and disagree in the opposite direction on the web page (see `## Source`).

> **Figure 3.3: Reported and anticipated exposure vs other measures.** The share of tasks people say AI could do today (reported exposure, in grey) and in 12 months (anticipated exposure, in orange) plotted against observed exposure (left panel) and theoretical exposure (right panel). Each point is an occupation, with occupations containing small samples grouped with exposure neighbors to ensure privacy. Reported and anticipated exposure are computed as the midpoint of the bin selected by the survey respondent.

In-image chart title: "Share of work tasks AI could do". Left x-axis "Observed exposure", right x-axis "Eloundou et al. (2023) theoretical exposure", shared y-axis "Occupation-mean stated task share"; legend "Today" / "Expected in 12 months"; a 45-degree dashed line and a fitted line per series in each panel; marker area varying with sample size.

**Annotation.** The most careful caption in the report. Four jobs: the colour key given inside the definition of each construct ("reported exposure, in grey"; "anticipated exposure, in orange"); **the unit of observation stated explicitly** ("Each point is an occupation"), which is what stops a reader from treating a 100-point scatter as 9,700 respondents; **the privacy rule stated as an aggregation rule with its consequence** ("occupations containing small samples grouped with exposure neighbors to ensure privacy" — note that grouping neighbours *on the x-variable* mechanically tightens the very relationship being plotted, which the caption discloses and does not discuss); and **the coding rule for the outcome** ("computed as the midpoint of the bin selected by the survey respondent"), which is the assumption footnote 4 then shows biases the slopes toward zero. The 45-degree line — the benchmark against which "reported exceeds observed" is read — is in the image only.

> **Figure 3.4: Reported and anticipated exposure are lower in higher-GDP countries and among more experienced workers, and rise with automated Claude use.** Reported and anticipated (12 month) exposure against country GDP per working-age adult (left), years of experience (middle), and the share of Claude sessions classified as automated (right).

In-image chart title: "Reported and anticipated exposure", subtitle "Relationship with people's characteristics and usage". Shared y-axis "Share of tasks AI can do"; x-axes "GDP per working-age adult (15-64)" (log-spaced dollar ticks), "Years of experience" (bins "<1", "1-3", "4-7", "8-15", ">15"), "Automation share"; legend "Reported" / "Anticipated (in 12 months)"; scatter with fitted lines in the outer panels, paired bars in the middle.

**Annotation.** A three-clause declarative title, one clause per panel, each naming the sign of the relationship — the longest title in the report and the one that survives being read aloud without the exhibit. The gloss is a single sentence listing the three x-variables in panel order, with the working-age denominator specified for GDP and the construct named for automation ("the share of Claude sessions classified as automated"). What the caption omits is that the middle panel is a bar chart of experience bins while the outer two are scatters with fitted lines, and that the experience bins are unequal. The naming in this caption is exactly right: stated beliefs are "exposure" about AI, the usage variable is "**Claude** sessions".

> **Figure 3.5: Share of people reporting it is likely or very likely job responsibilities will change significantly or people will involuntarily lose a job next year.** Share of respondents that reported it was likely job responsibilities would change (left panel) or an individual would lose a job they wanted to keep (right panel) for themselves, a peer, a junior colleague, or a senior colleague.

In-image chart title: "Likelihood of jobs changing"; panel titles "Responsibilities change" and "Job loss". Axis: "Share answering Likely or Very Likely"; stacked bars over x-ticks "Self", "Peer", "Junior", "Senior"; legend defines the two stacked components with their numeric probability ranges.

**Annotation.** A descriptive title so long it repeats the whole survey item, and a gloss that is nearly the same sentence again with the panels assigned and the job-loss item stated in the respondent's terms ("an individual would lose a job they wanted to keep" — i.e. involuntary separation, defined without the term). The four referents are listed in the same order as the bars. Once again the numeric definitions of "Likely" and "Very Likely" are in the legend only, and the body's claim about junior colleagues depends on them.

> **Figure 3.6: The share of people reporting positive expected impacts of AI on economic and intrinsic dimensions of job quality is higher among more automated Claude users.** This figure shows coefficient estimates from linear regressions of an indicator for whether a person expected AI to have a positive effect on each of the six dimensions of job quality onto normalized AI automation share.

In-image chart title: "Relationship between job market sentiment and automation share". Axis: "Change in share positive about the dimension (pp) per +1 SD (22pp) increase in automation share"; two groups of bars labelled "Economic" and "Intrinsic"; x-tick labels name each dimension and give its mean; whiskers on every bar.

**Annotation.** The caption specifies the estimator, the left-hand variable (an indicator for a positive expectation) and the right-hand variable ("normalized AI automation share") — but **it never says what the normalisation is or what unit the bars are in.** Both live in the axis label, which reveals that a unit is one standard deviation of automation share and that this equals 22 percentage points. It also does not say that the whiskers are confidence intervals, nor at what level (Figure 3.8's caption does). Compare September 2025's Figure 3.9, whose caption ended on the coefficient's meaning in plain words. **A caption for a coefficient plot must state the units of the coefficient and what the error bars are; this one states neither, and it is the exhibit our own drafts are most likely to imitate badly.**

> **Figure 3.7: The share of people reporting positive expected returns to their skills is increasing in automation share, while the share reporting they're learning more is flat.** This figure shows the relationship between automation share of tasks and the share of people reporting AI increases the market value of their skills (blue) and they learn more when using AI (orange).

In-image chart title: "Skill value and learning versus automation share". Axis: "Share reporting positive effects" against "Automation share"; two series with fitted dashed lines; legend "Learning more" / "Skills more valuable".

**Annotation.** A two-clause declarative title carrying a positive result and a null in the same sentence, in that order, with the null given the plainer word ("is flat"). The gloss names both series with their colours. What is absent is the binning: the points are clearly group means along the automation-share axis rather than individual respondents, and neither caption nor body says how the bins were formed or how many respondents are in each — which is what a reader needs to judge whether "flat" is precise or merely noisy. The body's own bound on the null is verbal ("the data do not rule out skill erosion").

> **Figure 3.8: Women have distinctly different usage patterns, even after conditioning on occupational differences.** This figure shows women's usage patterns compared to men's. Each bar is the difference between women's and men's average on that usage measure, controlling for occupation (SOC minor groups), expressed in standard deviations of the outcome. Whiskers show 95% confidence intervals. The sample is restricted to respondents identifying as women or men. Women have significantly lower Claude Code and automation shares, while having higher total active minutes.

In-image chart title: "Gender gaps in usage". Axis: "Women — men difference standardized (outcome SDs)"; four bars labelled "Work-use share", "Claude Code share", "Automation share", "Total active minutes (log)"; whiskers on each.

**Annotation.** The report's most complete caption after Figure 2.3, and the model for a conditional estimate: the contrast ("the difference between women's and men's average on that usage measure"), **the control set with its level of aggregation** ("controlling for occupation (SOC minor groups)"), the units ("expressed in standard deviations of the outcome"), **the uncertainty and its level** ("Whiskers show 95% confidence intervals"), the sample restriction and its basis ("respondents identifying as women or men"), and a closing sentence of interpretation that states which differences are significant and in which direction. Everything Figure 3.6's caption lacks is present here, which is how you can tell the omission there is an oversight rather than a house convention.

> **Figure 3.9: People hope for human-AI collaboration, automation of drudgery and more free time, and that economic gains from AI are broadly shared.** This figure shows the five most common themes from people's responses to an open-ended question on what they hope an AI-transformed economy looks like in 10 years.

In-image chart title: "10-year vision themes". Axis: "% of respondents"; five horizontal bars whose labels name the five themes.

**Annotation.** The title names three themes; the caption says there are five; the remaining two are named only by the bar labels inside the image. The gloss states the truncation ("the five most common themes"), the instrument ("an open-ended question") and the horizon ("in 10 years"), but not that the themes are non-exclusive — which the body's "Over half… just over half… about one third" implies and neither says. **For a multi-label classifier output, the caption must say whether a respondent can appear in more than one bar.**

### The caption template this wave adds to the corpus

Relative to the September 2025 template, hold on to all of it and note the following changes and lessons:

1. **Terminal period after the bold title.** The PDF adds it; the web page drops it. Treat the period as optional and the *bold declarative title plus roman gloss* as the invariant.
2. **The declarative title now carries the sign or the direction, sometimes for three panels at once** (Figure 3.4). Where the exhibit has many findings the title goes descriptive and the in-image title carries the message (Figures 1.2, 2.6).
3. **The in-image title is doing more work than in 2025** — a short, memorable phrase ("The workweek", "Overtime", "Tax day in Claude traffic", "Gender gaps in usage") rather than a full description of the cut. That is a reasonable division of labour only if the caption remains self-sufficient. In four exhibits here it does not: the sample restriction (2.2), the response-band definitions (3.2, 3.5) and the coefficient units (3.6) exist only inside the graphic.
4. **Always state the unit of observation.** Figure 3.3's "Each point is an occupation" is the single most valuable clause in this report's captions.
5. **Always enumerate a box plot's statistics** (Figure 2.3) and **always name the error bars and their level** (Figure 3.8).
6. **Disclose what was not adjusted for** (Figure 2.3, "Token counts are not adjusted for which model served the conversation").
7. **Disclose the privacy aggregation where it bears on the estimate** (Figure 3.3, small occupations grouped with exposure neighbours).
8. **Read one cell aloud** where the exhibit's grammar is unusual (Table 2.4).
9. **Say Claude for usage and AI for stated beliefs**, in captions as in prose (Figure 3.4 does both in one line).
10. **Repeat rather than cross-reference.** The 1–5 scale is spelled out in Figure 2.5's caption though the body defined it two pages earlier; the sample restriction "restricted to chat and Cowork" recurs verbatim in 1.2, 2.3 and 2.6.

## Limitations

**There is no limitations section**, and no "Caveats", "Threats to validity" or discussion of them in the Discussion. As in September 2025 the caveats are dispersed — but the distribution is different: this report puts more of them in the body and fewer in footnotes, and the survey chapter opens on its own biggest one.

### 1. In the body, in the position of a finding

> The Economic Index Survey is not representative of the general population. We reach a random sample of Claude users, there may be selection in who completes the survey, and we filter out infrequent users from our analysis.

> While we can't conclusively identify the jobs of the people making these requests, this could reflect the fact that people in higher-paying occupations—like marketing managers or computer programmers—are more likely to work outside traditional hours.

> Admittedly, the relationship is noisy and there are notable outliers.

> It is also worth noting that reported exposure systematically exceeds observed exposure. One explanation for this is that not everybody does every task in an occupation, and our survey disproportionately reaches those who use AI more.

> This is slightly below the annualized hazard rate of losing a job in the US; however, since our respondents skew toward knowledge workers in stable employment (a group that plausibly faces below-average separation risk at baseline), this may still indicate elevated perceived risk.

> It's possible that this relationship is explained by selection, that the people most enthusiastic about AI are also the most willing to hand over entire tasks to it. We can't rule this out entirely, but these estimates don't meaningfully change when we control for user tenure on Claude.ai—which we can think of as a proxy for enthusiasm, because it captures early versus later adopters.

> However, these are self-assessments, and skills can erode even as they become more valuable and as someone reports learning more, so the data do not rule out skill erosion.

> Some of the gap may simply be register; prompts are often terse and informal, while Claude tends to reply in polished prose.

> Women, who make up only 12% of our linked respondent sample, use Claude differently from men.

### 2. In footnotes

> [1, Ch. 1] Throughout, all analyses are based on privacy-preserving classifiers: transcripts are only read by another instance of Claude. Then we filter out any cells with insufficient observations to ensure privacy-preserving analysis.

> [6, Ch. 1] The time of day is based on inferring the state from the IP address of the conversation.

> [1, Ch. 2] Data in this chapter cover chat and Cowork conversations sampled between April 10 and June 10, 2026. Where the autonomy discussion compares surfaces, Claude Code sessions from the same period are included. Wages are from the BLS OEWS, May 2025 release.

> [2, Ch. 2] "None" is a catch-all for the conversations that didn't yield a prominent concrete output. This may include brief or abandoned exchanges, cases resulting in an error or cases where Claude asked a clarifying question and the user didn't continue.

> [3, Ch. 2] We use geometric means for the conversation level token counts since that variable is extremely right-skewed–a small number of conversations use several orders of magnitude more tokens than a "typical" conversation. The relationship is very similar if we use medians or if we weight the tokens by their respective cost to account for the mix of models used. There are some notable exceptions, including physician occupations.

> [5, Ch. 2] The largest exception is data and spreadsheets, where Claude.ai conversations involve more autonomy than Claude Code (3.09 vs 2.74). This is mostly compositional: about 70% of the gap reflects a different mix of tasks.

> [4, Ch. 3] Because responses are binned—so the lowest possible coded response exceeds zero, and the highest possible response falls short of one—the slopes in this figure are biased towards zero. As a result, we interpret the comparison of slopes qualitatively rather than as precise estimates.

> [5, Ch. 3] The binned response scale likely also plays a role: because midpoint coding pulls reported task shares away from the extremes, observed exposure will tend to look as though it understates AI's capabilities in the least-exposed occupations and overstates them in the most-exposed ones, even absent any substantive difference.

> [11, Ch. 3] This question was asked about the job change forecast and job loss forecast together. The 38% is therefore an upper bound on the share of people who attribute their own job loss forecast to AI.

> [9, Ch. 3] Conditioning on these measures therefore attenuates the relationship between automation share and task shares (today, in 12 months, and the change), but all three relationships remain positive and statistically significant.

> [14, Ch. 3] While this could be due to substitution between chat/Cowork and Claude Code, the pattern holds even when controlling for Claude Code session share. These patterns also survive controlling for occupation fixed effects.

### 3. In captions

The unit of observation and the privacy grouping of small occupations (Figure 3.3); the midpoint coding of bands (Figure 3.3); the unadjusted model mix (Figure 2.3); the twelve-category truncation (Figure 2.1); the two sample restrictions on the token panels (Figure 2.3); the restriction to respondents identifying as women or men, and the 95% intervals (Figure 3.8); "Excludes military" (Figure 3.1's footnote).

### 4. As a forward-looking problem rather than a limitation

> Accurately classifying the work that Claude does will remain a moving target. For example, as AI capabilities increase, AIs may increasingly interact and exchange with each other, perhaps in ways inscrutable to humans or simple classifiers.

> This reveals how the cadences of daily life are etched into our usage logs and opens avenues for future research.

### Annotation

- **Placement is better than September 2025 and still not collected.** The survey chapter's representativeness paragraph is where a limitation should be — first, in the body, in its own paragraph, naming all three of its sources. The identification caveat on the wage-quartile finding is inside the sentence it qualifies. The outlier concession sits between the two occupation examples. But there is still no place a reader can go to ask "what are the limitations of this report?", and Chapters 1 and 2 have nothing resembling the survey chapter's opening paragraph.
- **Specificity is high where it exists.** The sample window for Chapter 2 is given to the day and the wage vintage to the release. The linkage window, the 20-session cap and the five-session exclusion are given with their reasons. The estimator choice is justified and two alternatives are reported. The JOLTS benchmark is computed in the footnote so the comparison can be checked. Two separate footnotes explain how binning biases the same figure's slopes, in two different directions, for two different claims.
- **Where a threat is answered, the answer reports its cost.** Three instances, all worth copying: the model-choice test (0.37 points unconditional, 0.26 within Sonnet); the robustness of the autonomy result's exception (about 70% compositional, and the direction reversed for that one category); and the automation-share conditioning ("attenuates the relationship… but all three relationships remain positive and statistically significant"). None of the three declares robustness without giving up a number.
- **Where a threat is not answered, the sentence says so.** "We can't rule this out entirely"; "the data do not rule out skill erosion"; "we interpret the comparison of slopes qualitatively rather than as precise estimates"; "The 38% is therefore an upper bound"; "this may still indicate elevated perceived risk".
- **The caveats a referee would raise first, and where they are.**
  1. **Chapter 1 has no stated sample window.** "during the sample period" appears in the finding; the dates appear only as axis ticks on Figures 1.1 and 1.4; Chapter 2's footnote covers Chapter 2. Every cadence finding is therefore undated in the text — including a weekend claim built on four weekends and a tax-day claim built on one deadline in one country. This is the report's largest documentation gap and it is not acknowledged anywhere.
  2. **One tax day, one country, one year.** The event study has a single treated date and a single control group (the rest of the world). The report presents it as illustration rather than as identification, which is the right register, but nothing marks that the estimate is n = 1 event.
  3. **The survey sample is small, selected and 12% women.** ~9,700 linked respondents, drawn from Claude users, filtered to those with at least five sessions, and the gender split is disclosed only when gender becomes the subject. Every heterogeneity result in Chapter 3 — GDP, experience, automation share, gender — is a cut of that sample, and the exclusion of infrequent users removes exactly the marginal users whose beliefs would discipline the optimism finding.
  4. **Reported exposure is a self-assessment coded at bin midpoints.** Two footnotes say what this does to the slopes. The body's most-quoted survey claim ("Over a third expect AI to be able to do most or nearly all of their work tasks") depends on band definitions that appear only inside a figure.
  5. **The occupation in Chapters 1–2 is inferred from the task, and in Chapter 3 is self-reported.** Both are used to talk about "higher-wage occupations" and "occupational exposure" and no sentence flags that the two chapters' occupation variables are not the same object. Figure 3.1's caption is the only place the difference surfaces ("respondents reporting their occupation").
  6. **The token–value argument rests on a wage proxy for value.** "More complicated and valuable outputs" is never measured as either; the mapped occupation's median wage carries both adjectives.
  7. **The internal contradiction on the sleep-advice hour** (3 a.m. in the PDF body, 5 a.m. in the PDF's own preview and throughout the web page). Small, but it is the only number in the Introduction, and it shows what happens when a headline quantity is carried in prose in two places rather than in one exhibit.
- **What our posts must add that this report does not have.** An MDE beside every null. "Essentially parallel", "roughly the same increment", "roughly flat", "essentially uncorrelated" and "marginally less likely" are five nulls doing load-bearing interpretive work, and not one carries a bound. The report's own footnote 4 shows the authors know the estimates are attenuated; the missing sentence is what difference the design could have detected.

## Close

### "Discussion", verbatim and in full

> AI is diffusing rapidly throughout the economy, across an increasing number of surfaces, with increasingly intelligent outputs. In earlier AI chat interfaces, usage was simple, contained in the chat window without web search, tool calls, artifacts, or other affordances. Now, Claude models can operate autonomously for hours through Claude Code and Cowork. As these forms change, the user base is shifting as well. Early adopters were highly technical. Our most recent users apply Claude to tasks that command lower wages in the labor market.

> In this report, we took several steps toward more informative measurement. First, we began measuring more and more frequently, processing data in hourly samples. This reveals how the cadences of daily life are etched into our usage logs and opens avenues for future research. Second, we began recording artifacts, or the outputs that people take away from Claude. These make Claude's work output more legible, and show some intuitive patterns.

> Finally, usage data only carries so much information. Our survey allowed us, for the first time, to ask people directly about how they use AI and what they feel about it. We found that our survey respondents use AI for more than we give it credit for—they report AI can do a higher share of their work than the observed exposure measure for their occupation would suggest. Asked to forecast next year's capabilities, over 35% predicted that AI would be able to do *most* of their work.

> Accurately classifying the work that Claude does will remain a moving target. For example, as AI capabilities increase, AIs may increasingly interact and exchange with each other, perhaps in ways inscrutable to humans or simple classifiers. Ultimately, Claude's impact on the economy will be visible in economic aggregates like employment and productivity as much as its usage logs. Still, AI is likely to have its earliest impacts in the areas where it does the most work, so shedding light on these ever-changing usage patterns will remain a key way to inform the public.

### Annotation

- **There are no chapter-level closes.** This is the structural difference from September 2025, which closed each of three chapters and then closed the report. Here each chapter ends on a pivot into the next section ("We look at that split next"; "The next section examines how much of the decision-making within each conversation is delegated to Claude") or simply on its last finding (Chapter 1 ends on "On April 16, they dropped sharply"; Chapter 3 ends on the shared-prosperity theme). The consequence is that the Discussion is the only place the three chapters are put together, and it does so in 350 words. **A multi-part post that closes only once must make the single close carry the synthesis; this one does, and the reason it can is that the three chapters share a subject — measurement — rather than three findings.**
- **What was learned, stated as three method steps and one substantive surprise.** "we took several steps toward more informative measurement", enumerated "First… Second… Finally", each step followed by what it revealed: hourly sampling → "how the cadences of daily life are etched into our usage logs"; artifacts → "make Claude's work output more legible, and show some intuitive patterns"; the survey → the exposure gap. The self-assessment is notably modest: the artifact chapter's results are described as "some intuitive patterns", which is a fair description and an unusual thing to publish about your own chapter.
- **One number in the close, and it is the one that contradicts a prior.** "over 35% predicted that AI would be able to do *most* of their work", with "most" italicised because it is a defined band and not a loose word. September 2025's concluding remarks carried no figures at all; this one carries exactly one, chosen because it is the report's most consequential survey result and the one a policy reader will quote. The rest of the close is number-free.
- **Why it matters, and the concession that comes with it.** The stakes paragraph is the last one, and it is built as a limit on the report's own method rather than as a claim about the world: "Accurately classifying the work that Claude does will remain a moving target… **Ultimately, Claude's impact on the economy will be visible in economic aggregates like employment and productivity as much as its usage logs.**" That sentence concedes that usage measurement is not the thing anyone finally cares about — the strongest possible statement of the series' own limit — and the "Still" that follows is what rescues the project: "AI is likely to have its earliest impacts in the areas where it does the most work, so shedding light on these ever-changing usage patterns will remain a key way to inform the public." Claim, concession, reason the work still matters, in three sentences. **This is the house form for a why-it-matters that has to survive a reader who thinks usage logs are the wrong measure.**
- **What comes next.** Committal about method, silent about results, and unusually specific about a future measurement problem: "as AI capabilities increase, AIs may increasingly interact and exchange with each other, perhaps in ways inscrutable to humans or simple classifiers." That is the next wave's problem named two waves early, and it is the only forward-looking sentence in the report that is not about the report. Note what is absent: no "we will continue to track these trends", no dataset enumeration, no open questions for other researchers. September 2025 ended by handing four questions to the field; this one does not, which is a loss.
- **No recommendations to anybody.** No policymaker sentence, no business sentence, no research agenda. The closest thing to an audience is "the public", in the last three words. Given that the report contains a finding about perceived job loss among junior colleagues and a finding about gender differences in delegation, the absence of a single sentence on what either implies for anyone is the most striking editorial choice in the document.
- **How it avoids a template summary.** Five devices. (i) **No recapitulation.** Not one of the three chapters' headline findings is restated; the close describes what each chapter *did*, not what it found. (ii) **Every paragraph opens on the world or the method, never on "this report"** — "AI is diffusing rapidly throughout the economy"; "In this report, we took several steps…" is the one exception and it is the paragraph about method; "Finally, usage data only carries so much information"; "Accurately classifying the work that Claude does will remain a moving target." (iii) **The close argues against its own instrument** — twice, in the last paragraph, which is the same self-undermining move as September 2025's refusal to extrapolate its concentration finding. (iv) **The one number is a forecast made by respondents, not a measurement by the authors**, so the report's last quantitative note is somebody else's belief. (v) **The first paragraph is about the product, not the findings** — usage was simple, now models run autonomously for hours, and the user base has shifted downmarket in task wage. Opening a close on what changed in the object of study rather than in the analysis is what makes it read as a situation report rather than a summary.
- **Title against ending.** Title: "Cadences". Ending: "This reveals how the **cadences** of daily life are etched into our usage logs". The title word appears once in the close, in the sentence that says what the new instrument revealed — and it appears nowhere else in the report except as Chapter 1's title. That is a thinner match than September 2025's (where the title's adjective was the close's predicate and its two nouns were the close's two paragraphs): "Cadences" names one of three chapters, and a reader who remembers only the title will not remember the artifact classifier or the survey. **By the standard we hold our own drafts to — the ending must contain the title's key word doing work — this passes, but the title under-describes the report.**
- **First person.** Used throughout for institutional and analytical acts ("we made several changes", "we took several steps", "we began measuring", "we began recording", "Our survey allowed us", "We found that"). Our house style forbids it. The substitutions this report makes available are the ones it already uses elsewhere: attribute to the exhibit ("The left panel of Figure 3.4 shows"), to the instrument ("Our classifier identified", "The hourly data captures"), or to the data ("the data do not rule out skill erosion"). The second and third are the ones to borrow; the first still says "our".

## Verification

- **URLs fetched, both on 2026-09-16:**
  - https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf — retrieved with `curl` (HTTP 200, 3,259,219 bytes), 33 pages, text layer complete. `web_fetch` refuses `cdn.sanity.io` URLs (`url_not_allowed`), as recorded in the research journal. Text extracted with `pdftotext -layout` and, as a cross-check, `pdftotext` without layout; both extractions agree. This is the document of record and the source of every quotation in this file unless a quotation is explicitly marked as web-page text.
  - https://www.anthropic.com/research/economic-index-june-2026-report — returned in full (H1 "Anthropic Economic Index report: Cadences", dated "Jun 26, 2026"), including all 27 footnotes. Used to establish how the web page differs from the PDF (see `## Source`) and for nothing else.
- **Fetch date:** 2026-09-16. **Fetch failures: none.** Both documents returned complete on the first attempt.
- **Not fetched, deliberately:** both builds of the appendix (`…03ed1410…` and `…8eb31e1d…`), which have their own style entry; the second appendix copy linked from footnote 5; and every internal and external work the report links — the January, March and September reports, the labour-market paper, the 81k interviews and economics posts, Anthropic Interviewer, Clio, the survey announcement, the Claude Code companion report, the Sonnet 3.7 report, the Anthropic Public Record, the "rising tide" arXiv paper, Eloundou et al., the IMF note, World Bank WDI, UN WPP, IMF WEO, BLS JOLTS and the Federal Reserve report. Nothing from any of them is quoted here.
- **Every quotation was checked back against the extracted PDF text** word by word after transcription, and the web-page variants were checked against the fetched page. Confirmed for all nine sections of this file.
- **Quotation caveats.**
  - Hyperlink URLs were stripped from quoted prose and the anchor text retained; the PDF, which is the source, carries no visible link text.
  - Typographic apostrophes and quotation marks were normalised to ASCII where they appear inside quoted prose; en and em dashes and the minus sign in "blogs −0.1" are reproduced as in the source. No word was changed.
  - **PDF line-break artefacts were repaired.** The extraction breaks words across lines without a hyphen in several places ("privacy- preserving", "context- specific", "day-  to-day", "higher- quartile", "back-and-forth" across a line end). Quotations here restore the intended spacing; no reading is uncertain.
  - Footnote numbering in quotations is given in square brackets, e.g. "[4]", where the source uses a superscript. **The PDF numbers footnotes per chapter and the web page numbers them 1–27 continuously**, so every footnote quoted here is labelled with its chapter where ambiguity is possible, e.g. "[5, Ch. 2]". The web equivalents are: Intro 1 → 1; Ch. 1 1–6 → 2–7; Ch. 2 1–6 → 8–13; Ch. 3 1–14 → 14–27.
  - Emphasis (bold, italic) is reproduced as it appears in the PDF. Where the PDF runs a bold caption title into a roman gloss and the web page splits them and italicises the gloss, the PDF form is used.
  - Section headings are quoted in the PDF's casing; the web page recases two of them (see `## Source`).
- **Alt text and chart-image text, per `room/director-2026-09-16-alt-text-ruling.md`.** The bold sentence under an exhibit is the caption and is quoted as such. **The web page supplies no alt text for any figure** — every figure is `![](…)` with an empty alt attribute, and only the decorative hero illustration carries alt text ("Anthropic Economic Index report: Cadences"). There is therefore **no number anywhere in this publication that exists only in image alt text**, and nothing in this file is marked "(alt text)".
- **In-image text and chart numbers**, per `room/director-2026-09-16-figure-values-ruling.md` (in `wiki/style/`, no chart-read numbers are recorded at all) and the caption amendment in `room/director-2026-09-16-caption-amendment.md` (the caption is the emphasised sentence under the image, bold here in the PDF and bold-italic on the web). All nineteen exhibits are raster images inside the PDF (JPEG and indexed PNG; `pdfimages -list` confirms no vector text layer), so no in-image text is extractable from the text layer. The images were rendered and read for chart type, in-image titles, panel titles, axis labels, legend entries and annotation labels only; each such string is quoted marked "In-image chart title", "panel titles", "Axis", "legend" or "annotated", and never presented as caption or as prose. **No number was read off a chart image and recorded anywhere in this file.** In particular, the data labels printed on the bars of Figures 1.3, 2.1 and Table 2.4, the numeric response-band definitions on the axes and legends of Figures 3.2 and 3.5, the per-dimension means on the axis of Figure 3.6, and every plotted value in Figures 1.1, 1.2, 1.4, 2.2, 2.3, 2.5, 2.6, 3.1, 3.3, 3.4, 3.7, 3.8 and 3.9 are not recorded. Every number quoted in this file appears in the PDF's body prose, its footnotes, or a caption. Where this file notes that a definition or a magnitude exists "only inside the image", that is a statement about where the publication put it, not a transcription of it.
- **Scope.** This file annotates how the report is written: its section order, the grammar of its findings and caveats, how its comparisons are phrased, its caption template, where its limitations sit, and how it closes. It makes no judgement about whether any finding is correct. Where this file says a caveat is misplaced, a caption is incomplete or a null is unbounded, that is a statement about the writing, not about the analysis.
