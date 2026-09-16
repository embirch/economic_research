# survey-81k-interviews-2026-03 — style annotation

## Source

- **Title on page:** "What 81,000 people want from AI" (H1, with a hard line break after "people", so the rendered title is two lines and the extracted text runs "What 81,000 peoplewant from AI"). Browser and Open Graph titles are the same words on one line; the bibtex key title-cases it ("What 81,000 People Want from AI"). The title is a question restated as a noun phrase, and it names the respondents rather than the instrument or the finding — the only title in the corpus that does.
- **Date on page:** **none.** There is no dateline, no "Mar 2026" above or below the H1, and no author byline at the top. The only dates anywhere are the bibtex `date = {2026-03-18}` and the Corrections block, "Mar 19, 2026"; `wiki/INDEX.md` records 2026-03-19. Recorded as an absence, because it is a structural choice with a cost: a piece whose fieldwork is described only as "Last December" and "Over one week in December", with no year anywhere, cannot be dated by its reader at all.
- **Primary URL fetched:** https://www.anthropic.com/features/81k-interviews
- **Category label above the H1:** none. No eyebrow, no "Economics" or "Research" label, no "Read the paper" link above the article. The page sits under `/features/`, not `/research/` or `/news/`, and it is styled as a feature rather than as an instalment of a programme. It claims no lineage in its opening: no earlier publication is named until the Conclusion.
- **Authorship:** at the foot, under an H3 "Authorship and acknowledgments", credited role by role ("Saffron Huang led the project, designed and ran the analysis, and wrote the blog post. Shan Carter led data visualization…"), followed by a bibtex block whose author list is longer than the prose credit. Putting a named lead author at the *end* is the Institute-feature convention; the Economic Index reports name no authors at all and the papers name them at the top.
- **PDF or appendix:** a separate 14-page appendix PDF, linked from an H3 "Appendix" reading only "Available here." and pointed at three times from the body. The `wiki/INDEX.md` row treats it as its own slug (`survey-81k-interviews-2026-03-appendix`). The feature page is the document annotated here; the appendix was read only to check what the page's method paragraphs compress, and every use of it below is marked *(appendix)*.
- **Document type:** interactive Institute feature. It calls itself "this research", "this post" ("If you'd like to cite this post"), "a new form of social science" and "qualitative research at a massive scale". There are no page numbers, no figure numbers, no tables, no abstract, no key-findings box and no numbered sections. Every reference below is to a named heading and an element.
- **Approximate length:** 66 paragraphs, roughly 4,300 words of body prose, plus 29 category definitions inside the three ranked lists (~700 words), eight exhibit captions (~380 words), one footnote and the credits. Nine substantive sections plus a Conclusion, all at H2.
- **Exhibits and quotations:** eight captioned exhibits, all client-rendered SVG. **The page contains no `<img>` element, no `alt` attribute anywhere, and no `<figure>`/`<figcaption>`.** It carries 67 published respondent quotations in five different components: five in the opening scroll sequence, 29 as hover cards inside the three ranked lists, ten inside the light-and-shade panels, 21 as block quotes in the body, and two set inside running prose. Several are re-used across components at different lengths (below). A Quote Wall of further quotes is linked twice, from an identical card near the top and at the end.
- **Audience:** general, and further from an economist than anything else in the corpus. No model, no coefficient (one correlation pair excepted), no interval, no standard error, no sample size under any exhibit, no denominator stated beside any share, no discussion of weighting, and no statistical vocabulary beyond "predictor", "correlation", "multi-label" and "Likert scale". The unit of persuasion is a person's sentence; the unit of evidence is a share of respondents.

## Section order

Headings in order, with what each does. Everything is H2, including the chart cards; the credits, appendix and footnotes are H3s beneath nothing. The hierarchy is flat by accident, and the result is that a heading scan reads as one continuous question-and-answer spine.

1. **H1 + dek + scroll sequence.** No eyebrow, no date, no byline. One dek paragraph, then a full-screen respondent-dot visualisation with a unit legend ("Each dot represents 4 respondents") and a "Jump to story" button, then five narrative panels: the scale claim; "AI is already helping people, and inspiring hope…" with two quote cards; "But it's also costing people, and raising alarm…" with two quote cards; and the thesis panel with one. ~75 words of the authors' prose and five people's.
2. **Untitled lead-in** — three paragraphs, ~180 words: the gap in the public conversation; what was asked, of whom, when, and how many answered; what follows, plus the Quote Wall pointer. This is where the study's design statement sits, and it carries no heading at all.
3. **H2 "Quote Wall"** — a card, not a section: one line of description and a "See quotes" button. Interrupting the article before the method with an invitation to read raw material is a genre move with no analogue in the corpus.
4. **H2 "Seeing the forest and the trees"** — the method, four paragraphs, ~250 words, *before* any finding: the instrument and the adaptive follow-ups; the classifier families and the single-label/multi-label distinction; quote selection, consent, de-identification and the redaction of other products' names; and one sentence delegating the rest to the appendix. A metaphor for a heading where a report would say "Data and methods".
5. **H2 "What people want from AI"** → **H2 "What people hope for"** (ranked list of nine categories, each with a share, a definition sentence and a hover quote) → caption → six paragraphs of prose.
6. **H2 "Are people getting what they want?"** → **H2 "Where AI has delivered on their vision"** (ranked list of seven) → caption → eleven paragraphs, the most quote-dense stretch of the page.
7. **H2 "What people are concerned about"** → **H2 "What people worry about"** (ranked list of thirteen) → caption → three paragraphs.
8. **H2 "Light and shade"** — the analytical core: framing, the co-occurrence claim, a measurement paragraph, then five paired benefit/harm panels each followed by its own paragraph of prose, then a cross-tension generalisation, then the page's only pooled caveats paragraph, then the no-camps paragraph. One caption, under the first pair, governing all five.
9. **H2 "How perspectives vary around the world"** — the sentiment measure in one sentence, a country bubble map with caption, three paragraphs, then **H2 "AI SENTIMENT BY REGION"** (a twelve-region card, set in capitals) and a region-level scatter with caption.
10. **H2 "Where do particular visions for AI most resonate?"** — framing, slope charts, caption, four paragraphs carrying five quotations.
11. **H2 "Where do particular concerns around AI most resonate?"** — three paragraphs, then slope charts and a caption that is the previous one with one word changed.
12. **H2 "Looking forward"** — three paragraphs: what the interviews are for, the next study, and two programmes offered as responses.
13. **H2 "Conclusion"** — four paragraphs, ~425 words.
14. **H2 "Quote Wall"** again, then H3 "Authorship and acknowledgments", H4 bibtex, H3 "Appendix", H3 "Footnotes" (one), H4 "Corrections".

**The ordering principle, and the thing most worth copying.** The findings run in the order the questions were asked: what do you want (visions) → have you got it (experiences) → what could go wrong (concerns) → how the two sides sit together (tensions) → where you are (geography). The structure of the piece *is* the structure of the instrument, and the captions say so by quoting each question verbatim. A reader can reconstruct the questionnaire from the article. That is the non-technical equivalent of presenting findings in pre-registration order, and it does the same work: nobody can suspect the sections were chosen after the fact.

**Where the findings sit:** once each, after the method, under a heading that either asks the question or names the respondents' side of it. As in `economic-index-2026-01-blog`, **the headings are the summary block** — four of the nine are questions, and a reader who scans only headings carries away no number. Note the pairing device: a question heading for the section ("Are people getting what they want?"), then a plain-label heading for its exhibit ("Where AI has delivered on their vision"). The exhibit heading is in the respondents' register, not the analyst's; nothing on the page is headed "distribution" or "shares".

**Where the caveats sit:** mostly as single sentences beside their findings, plus one pooled paragraph in §"Light and shade" which is placed after that section's findings and before its conclusion. There is no limitations heading. See `## Limitations`.

## Opening move

Verbatim: the dek, the five narrative panels of the scroll sequence (attributions as they appear in the markup, which is inconsistently capitalised), and the three paragraphs of the untitled lead-in. Hyperlink URLs stripped, anchor text retained, footnote marker removed.

> Last December, tens of thousands of Claude users around the world had a conversation with our AI interviewer to share how they use AI, what they dream it could make possible, and what they fear it might do.

> Each dot represents 4 respondents

> For the first time, AI has enabled us to collect rich, open‑ended interviews at extraordinary scale.

> We heard from people across 159 countries in 70 languages. We believe this is the largest and most multilingual qualitative study ever conducted.

> AI is already helping people, and inspiring hope…

> "Claude put the historical pieces together, leading to my proper diagnosis after being misdiagnosed for over 9 years." — Freelancer, UNITED STATES

> "I live hand to mouth, zero savings. If I use AI smarter, it may help me craft solutions to that cycle. It still depends on me." — Entrepreneur, NIGERIA

> But it's also costing people, and raising alarm…

> "I got laid off from my job in May because my company wanted to replace me with an AI system." — Technical Support Specialist, UNITED STATES

> "Humanity has never dealt with something smarter than itself. We need to reflect on how to prepare for the AI age." — SOFTWARE ENGINEER, SOUTH KOREA

> Across interviews, hope and alarm didn't divide people into camps, so much as coexist as tensions within each person.

> "I use AI to review contracts, save time... and at the same time I fear: am I losing my ability to read by myself? Thinking was the last frontier." — LAWYER, ISRAEL

> Public conversation about AI often centers on abstract projections of its risks and benefits. What's largely missing is a vision for what "AI going well" means, grounded in the concrete aspirations of people around the world who already use AI and have begun developing a sense of what it might do for them.

> So we asked our users about their hopes and concerns with AI, as well as how their perspectives connect to their actual experiences with the technology. Over one week in December, we invited everyone with a Claude.ai account to sit down with Anthropic Interviewer—a version of Claude prompted to conduct a conversational interview—and tell us about how they view AI. 80,508 people, across 159 countries and 70 languages, took the interview. We believe this is the largest and most multilingual qualitative study ever conducted.

> What follows is what they said about the role they want AI to play in their lives, whether it's already filling it, and what they're afraid might go wrong along the way. We also built a Quote Wall where you can hear from people directly.

Anchor text carrying links, in order: "AI interviewer" and "Anthropic Interviewer" → the Anthropic Interviewer publication; "Quote Wall" → the in-page quote browser.

**Annotation.**

- **What question is posed.** None, explicitly — there is no question mark in the opening. The question is carried by the title and then answered structurally: the first thing the reader meets after the dek is a person's sentence, and the opening's argument is made by the *order* of three panels, hope → alarm → both at once. The thesis arrives in the third panel, roughly 200 words into the sequence: "hope and alarm didn't divide people into camps, so much as coexist as tensions within each person." Everything after it is evidence for that one sentence, and the Conclusion restates it in almost the same words. **This is the tightest title–opening–close match in the corpus**, and it is achieved by stating the thesis before any evidence, which only works because the thesis is about the *shape* of the distribution rather than a magnitude.
- **The why-it-matters sentence.** "Public conversation about AI often centers on abstract projections of its risks and benefits. What's largely missing is a vision for what 'AI going well' means, grounded in the concrete aspirations of people around the world who already use AI…" The gap is located in **the public conversation**, not in the literature — the right move for a general audience and the wrong one for us, where the gap has to be in the evidence and has to name the work it is a gap in. Note "often" and "largely": two hedges in two sentences, on a claim about discourse that nobody could check either way. Hedging an unfalsifiable framing claim is cheap and it is still right.
- **Who is said to be affected.** "people", throughout, and then immediately particular people with a job and a country attached. The opening names no occupation as harmed or helped in the authors' own voice; the four panel quotes do it instead — a laid-off support specialist and a misdiagnosed freelancer carry what a report would state as a share. Letting the respondents name who is affected, and keeping the authors' prose at "people", is the register of the whole piece.
- **What the data is said uniquely to show.** Two superlatives, both about the instrument and not the findings: "For the first time, AI has enabled us to collect rich, open-ended interviews at extraordinary scale" and "We believe this is the largest and most multilingual qualitative study ever conducted." The second is stated twice — once in the scroll sequence and once in the lead-in — and hedged both times with "We believe", with a footnote on the second occurrence naming the two studies it claims to beat and their size. **Superlative + explicit hedge + a footnoted comparator is the honest form of a first-of-its-kind claim**, and it is better than the corpus's usual practice of either omitting the superlative (`economic-index-2026-01-blog`) or asserting it without a comparator. What is missing is any dimension on which the comparison could go the other way: neither archive is described, and "largest" and "most multilingual" are the only two axes offered.
- **How soon the first number appears.** The dek says "tens of thousands"; the first exact quantities are "159 countries in 70 languages" in the second panel, ~60 words in; the respondent count arrives in the lead-in at ~300 words; the first *finding* share arrives only with the visions exhibit, roughly 750 words in, and the first share in the authors' own prose not until roughly 1,650. Breadth before size, size before findings.
- **The rounding in the title is never reconciled.** The title and the final thank-you say 81,000; the lead-in and the acknowledgements say 80,508. The page never states which base any published percentage uses, and two further denominators exist behind the charts (`wiki/reports/survey-81k-interviews-2026-03.md`, §Source). A general-audience piece may round in its title; it must then state the base once, beside the first share. This one never does, and that single omission is the most consequential thing missing from the opening.
- **Register details worth copying.** First person plural for institutional acts only — "we asked", "we invited", "We heard from", "We believe", "We also built". No finding is in the first person. Second person appears once in the whole piece, in the Conclusion. The dek says "our AI interviewer" in lower case and the lead-in names it "Anthropic Interviewer—a version of Claude prompted to conduct a conversational interview", i.e. the instrument is glossed in an apposition at first use and never explained again; the gloss is nine words and is enough. The em-dash apposition doing the whole definitional job is the device to copy.
- **What the opening does not say.** The year. The invited total. That the respondents are self-selected from an already self-selected population — which the page does concede, 3,000 words later, inside the light-and-shade caveats paragraph. The claim that the sample is "everyone with a Claude.ai account" is presented as breadth ("we invited everyone"), where the same sentence read as a sampling frame is the piece's largest limitation. **Do not let a sample frame be introduced as a boast.**

## Findings and their caveats

### How a category distribution is presented to a general reader

The three main exhibits are ranked lists, not charts in the usual sense, and each item is built the same way: a two-digit ordinal, the category name, its share, a one-sentence definition beginning with a verb or a noun phrase, then a hover quote with its attribution and a link reading "Read more quotes about \<category\>". Two examples of the definition sentences, from §"What people hope for" and §"What people worry about":

> Time freedom — Reclaim time from work and chores to be present with family or friends, pursue hobbies, travel, rest.

> Cognitive atrophy — Concern about e.g. over-reliance causing skill loss, intellectual passivity, students bypassing learning, critical thinking decline.

**Annotation.** Every category is defined at the point of measurement, inside the exhibit, in one sentence, in the reader's words, with "e.g." doing the work that a coding manual would do. The vision definitions are written from the respondent's point of view and begin with an infinitive ("Reclaim…", "Achieve…", "Build, launch, and scale…"); the concern definitions are written from the analyst's and begin with "Concern about…". Two registers for two kinds of construct, held consistently across 29 definitions. Because the exhibit defines, **the prose never defines** — it only compares. That division of labour is the reason 4,300 words can carry 29 categories without a glossary, and it is directly transferable to a post that has to carry a taxonomy.

The prose then re-tells each list selectively and in whole numbers, never reproducing it:

> AI is used heavily for work, and so it's perhaps unsurprising that the largest group of people (19%) sought "professional excellence"—wanting AI to handle mundane tasks so they can focus on strategic, higher-level problems. Another 9% envisioned AI as an entrepreneurial partner to help them build and scale businesses.

**Annotation.** Share in parentheses, category name in quotation marks to mark it as a code rather than a description, and a gloss in the reader's language after the dash. "perhaps unsurprising" concedes the reader's prior before the number arrives — the same work "really" does in the January 2026 opening. Two cautions. The exhibit carries one-decimal shares and the prose rounds them to integers, so **a post quoting this page must choose a convention and say which**; and in one place the prose integer disagrees with its own chart label (recorded in the wiki entry, not reproduced here, per `room/director-2026-09-16-figure-values-ruling.md`). Never let your prose and your exhibit round the same quantity differently.

### Re-aggregation as a finding, in fractions rather than percentages

> The nine clusters may look disparate, but they are underpinned by recognizably human desires. Roughly a third of visions are about making room for life—more time, money, mental bandwidth—by using AI to alleviate current burdens. Another quarter revolves around using AI to help people do better, more fulfilling work (not escaping work, but getting more out of it). About a fifth are about becoming someone better—learning, healing, growing. A smaller share want to make something ("creative expression") or fix the world ("societal transformation").

**Annotation.** Nine categories collapsed into four motives, stated as fractions in words ("Roughly a third", "Another quarter", "About a fifth", "A smaller share") with an approximation marker on each of the three that have one. This is the best sentence on the page for a general reader and the worst for a referee: **the mapping from the nine categories to the four motives is never given**, so the arithmetic cannot be checked, and the fractions do not obviously partition the same base as the list above them. The lesson is to keep the device and supply the mapping — a re-aggregation stated in fractions, with the member categories named in a parenthesis, costs nine words and becomes reproducible.

### A number, then one person's sentence

The standing pattern for every finding on the page: the share, then a quote as the instance, then the next share.

> But another kind of productivity story emerged in the technical accessibility responses (9%), which emphasized access rather than speed. Here, people are using AI to break technical and sometimes accessibility barriers:

> "AI can read past my [learning disorder], which is huge. I've always wanted to code but could never write it correctly on my own—with AI, I finally can." — Tradesworker, United States

> "I am mute, and [Claude and I] made this text-to-speech bot together—I can communicate with friends almost in live format without taking up their time reading… [this was] something I dreamed about and thought was impossible." — White collar worker, Ukraine

**Annotation.** The quotes are doing a job the number cannot: they establish *what the category contains*, which for an open-ended code is exactly the thing a share does not tell you. Note the discipline around them. Each carries a self-described occupation and a country and nothing else — no name, no age, no plan tier, no quotation number. Square brackets mark every editorial insertion, including de-identifying substitutions ("[learning disorder]", "[severe neurological disorder]", "[my child's]"), and ellipses mark every cut. The colon before a quote block always names what the quote is an instance of, so a reader cannot mistake it for the finding. And the piece never counts its quotes or implies that two quotes are two data points.

Two things it does that we should not. Several quotes are re-used in more than one component **at different lengths** — the Hamlet quote appears trimmed in the experiences list and fuller in the body two screens later, and the misdiagnosis quote appears in the opening scroll sequence and again in the body with its attribution capitalised differently. And the same attribution field is inconsistently cased across components ("Freelancer, UNITED STATES" in the scroll sequence, "Freelancer, United States" in the body). If a quotation is worth using twice, it is worth being identical both times.

### How a low bar is reported

> When asked if AI had ever taken a step towards their stated vision, 81% of people said yes.

**Annotation.** The finding is stated with its question attached in the same sentence, and the question is then given verbatim in the caption below the exhibit. That is the right instinct and it is not enough: "ever" and "a step" make this the loosest measure on the page, and nothing anywhere says so. The complement is worse — the 19% who said no are reported as a *content category* in the ranked list ("AI hasn't delivered"), so the two halves of one yes/no question appear as two items on the same list of themes. **A yes/no share and a thematic share must not be ranked against each other in one exhibit**; a reader takes the list for a partition of a single dimension, and it is not one.

### Salience stated as different from frequency

> Emotional support comprised only 6% of responses, but these were among the most affecting we encountered.

**Annotation.** One sentence, and it licenses the editorial architecture of the whole piece: the section spends several hundred words and four quotations on its smallest category, and says in advance that the weighting is not the frequency. Any piece that wants to dwell on a small cell should state the mismatch in the same sentence as the share, exactly like this. (What the sentence does not do is bound it — "among the most affecting we encountered" is a claim about the authors, and the reader is given no way to see how the selection was made. `wiki/reports/survey-81k-interviews-2026-03.md` records that quote selection was itself done by Claude.)

### Conjecture, marked and then left standing

The hedge vocabulary, in page order: "perhaps unsurprising"; "It seems that…"; "This suggests AI's benefits may be strongest when…"; "presumably in their students"; "perhaps reflecting the fact that…"; "There are several possible explanations"; "likely biased towards"; "likely feels abstract"; "may lead to"; "In truth, it's probably some combination of all three".

> These observations also hint at the duality of our experience with AI systems. While some see it as filling gaps in human connections, others see AI as a substitution—even a welcome replacement—for them. There is real ambiguity about how to interpret the diversity of stories we heard: as wins for human wellbeing, as double-edged swords, or as band-aids for broader institutional failures. In truth, it's probably some combination of all three.

**Annotation.** Observation is kept separate from conjecture throughout, and the separator is always a hedge verb at the front of the sentence. The paragraph above goes further than anything in the corpus: it enumerates three incompatible readings of its own evidence, refuses to choose, and says the refusal out loud. For a piece whose material is people's words, naming the interpretive ambiguity *is* the finding, and "as wins for human wellbeing, as double-edged swords, or as band-aids for broader institutional failures" is the most useful sentence in the file to steal the shape of: three named readings, in descending order of comfort, none endorsed.

Where the same discipline fails, it fails twice in the same way — a conclusion is drawn from a pattern that does not test it:

> Concern about jobs and the economy was the strongest predictor of overall AI sentiment, suggesting it's more salient than any other issue.

> The same occupational patterns hold when you look at who's excited, regardless of experience, suggesting that optimism here is well-calibrated.

**Annotation.** The first is asserted twice on the page, and **no model, specification, competing coefficient or fit statistic appears anywhere**; the only illustration is a twelve-point region-level scatter, and "predictor" is doing work that no reader can check. The second infers calibration from the fact that stated excitement tracks lived experience across groups, which is consistency, not calibration. Both sentences are hedged with "suggesting", and in both cases the hedge is attached to the interpretation while the underlying claim ("strongest predictor", "The same occupational patterns hold") is stated flat. **Hedge the claim, not only the gloss** — that is where this page's otherwise exemplary hedging breaks, and it breaks on its single most quotable statistical sentence.

### Naming: this page is the house rule inverted, and it half earns it

On the page, "AI" is the subject of nearly every finding — "What people want from AI", "if AI had ever taken a step towards their stated vision", "AI sentiment", "AI's benefits for learning" — while "Claude" names the instrument, the classifiers, the product and, in the Conclusion, the thing being praised. The warrant is one sentence in the method section:

> Answers were reflective of AI usage broadly (i.e. not just Claude), though we redacted names of other AI products.

**Annotation.** That sentence is doing a great deal of work and it is the right sentence to have: respondents were asked about AI, so their answers are about AI, and saying "Claude" would misdescribe the measurement. It is also the minimum: the respondents are all Claude users, the interviewer is Claude, the classifier is Claude, and many quotations name Claude. Our own rule — the question says AI, every finding says Claude (`/mnt/memory/standards/terminology.md`) — is unchanged by this page, because our findings are measurements of Claude traffic and this page's findings are reports of people's beliefs about AI. The transferable point is narrower and sharper: **state once, in the method, which of the two your measured object is, and then never drift.** This page states it once and then drifts in the Conclusion, where the object silently becomes Claude (see `## Close`).

The Corrections block is the same distinction caught in the act:

> Mar 19, 2026. "Globally, 67% of people view AI positively" changed to "Globally, 67% of interviewees expressed net positive sentiment toward AI" to more precisely describe the study's methodology.

**Annotation.** The best single lesson in this file. The correction replaces a claim about a population ("people view AI positively") with a claim about a measurement on a sample ("interviewees expressed net positive sentiment"), and gives the reason in six words. Both the direction of the fix and its published record are what we want: the population noun, the verb of belief and the unhedged adjective all go, and what replaces them names the respondents, the construct and the scale. Every finding sentence in one of our posts should already read like the corrected version.

## Comparisons

Every place where a comparison carries the finding. The page's characteristic form is **a multiple, in words, against a named baseline** — not a difference, not a coefficient.

### Hope against fear, inside one person

> Across interviews, hope and alarm didn't divide people into camps, so much as coexist as tensions within each person.

> Notably, we often see these tensions directly jockeying within the same person. Someone who values emotional support from AI, for example, is three times more likely to also fear becoming dependent upon it. This pattern held across every tension we measured—although the correlation was weakest in the economic tension (see more analysis of these correlations in the Appendix).

**Annotation.** The organising comparison of the whole piece, and it is a comparison of *variances*: between-person (camps) against within-person (tensions). It is stated as a shape before it is stated as a number, illustrated with the strongest of the five pairs, generalised ("held across every tension we measured"), and then immediately qualified by naming the pair where it is weakest — in the same sentence, with the evidence delegated to the appendix. **Name your weakest case in the sentence that states your general pattern.** Compare `economic-index-2026-01-blog`'s selection-bias passage; this is the same move in a non-technical register, and it costs one clause.

### Light against shade, and lived against anticipated

> For each tension, we measured via classifiers how many people discussed the benefit ("light") or the harm ("shade") side substantively anywhere in their interview, and whether they were speaking from some personal experience (darker bars) or anticipation (lighter bars). We also looked at how this varied by stated job category.

> Across most tensions, the benefit side is more grounded in experience, while the harm leans hypothetical.

> A pattern runs across all five tensions: the more personal and immediate the impact, the more likely people are speaking from experience. The more systemic or long-term the impact—economic displacement, cognitive atrophy—the more speculative they become. That the systemic concerns remain speculative is not a verdict on AI's ultimate impact as much as a reflection of how early we are in its adoption.

**Annotation.** A two-by-two — side (light/shade) × grounding (lived/anticipated) — carried entirely by bar position, bar shading, and two-word labels under the bars. The panel furniture is a category name plus a context line of the form "…% mention this as a benefit" or "…as a harm", with the split bars labelled "have seen it" and "expect it". Two defects to avoid: the order of the two split labels is not held constant across the five panels, and one panel says "saw it" where the others say "have seen it". A reader comparing panels has to re-read the labels each time, which is precisely what a consistent encoding is for.

The cross-tension paragraph is the model for a generalisation over several findings in a general-audience piece: a one-clause regularity ("the more personal and immediate the impact, the more likely people are speaking from experience"), the exception class named with instances, and then **a sentence saying what the pattern is not evidence of** — "not a verdict on AI's ultimate impact as much as a reflection of how early we are in its adoption." Stating the misreading you are refusing is worth more than a hedge.

### Against the prior literature, by scale only

> The largest qualitative studies we found in our research were the USC Shoah Foundation Visual History Archive and the World Bank "Voices of the Poor Project," both of which included ~60,000 participants.

**Annotation.** The entire literature comparison, in a single footnote, on one axis, with a tilde on the comparator and the hedge "we found in our research" fencing the search. Everything the archives did better goes unmentioned. Honest in form and thin in substance: a footnoted comparator makes a superlative checkable, and choosing the one axis on which you win makes it uninformative.

### Region against the global share

> Learning using AI is disproportionately important in Central and South Asia (14% and 13% respectively versus 8% globally).

> North America and Oceania are particularly worried about governance gaps for AI (18% and 19% respectively, versus 15% globally).

> East Asia bucks the general global pattern; governance and surveillance drop to their lowest levels of any region (12% and 7%), overshadowed by concerns about cognitive atrophy (18%) and loss of meaning (13%).

**Annotation.** The "X% and Y% respectively versus Z% globally" construction, used consistently: both arms and the benchmark in the same parenthesis, so the comparison never needs the reader to remember a number from an earlier section. This is the plainest device in the file and the most reusable. What it is missing everywhere is the count behind any regional share; no n appears in any of these sentences or in the exhibit captions.

### Occupation against a named baseline

> Troublingly, educators were 2.5-3 times more likely than average to report having witnessed cognitive atrophy firsthand, presumably in their students.

> Tradespeople were among the most enthusiastic about AI-for-learning (45% reported having experienced learning benefits, second only to students), yet almost none had witnessed cognitive atrophy (4%—less than half the baseline).

> What varies is who's already experiencing economic benefit from AI—and that skews heavily toward independent workers—entrepreneurs, small business owners, even people with side projects—half of whom report real economic empowerment, more than triple the rate of institutional employees (47% vs 14%).

> Freelance creatives, in particular, sit at 23% lived benefit and 17% lived precarity—the one group where the upside and downside nearly cancel out. AI is both their tool and their competitor.

**Annotation.** Four shapes worth having: a range as a multiple ("2.5-3 times more likely than average"); a level with the baseline comparison in the same parenthesis ("4%—less than half the baseline"); a multiple *and* both arms, which is the only fully checkable one on the page ("more than triple the rate … (47% vs 14%)"); and two levels set against each other with the reading supplied in a five-word sentence ("AI is both their tool and their competitor"). The last is the page's best compression: two numbers, one image, no adjective. Prefer the third shape — a multiple is memorable, both arms make it auditable, and giving both costs four characters.

The referee's objection applies to all four: the occupational categories are self-described, optional and classified from free text, and **no counts are published for any of them**. The appendix concedes the first two points and the feature does not carry the concession to the section that needs it. When we cut by a self-reported group, the cell size goes in the sentence.

### The exception, named as an exception

> 22% of people expressed excitement about AI as an aid in decision-making, while 37% lamented that AI impedes good decisions because of its unreliability (e.g. hallucinations). This is the only tension in which the negative overshadowed the positive.

**Annotation.** Both arms, then a sentence stating that this pair is unlike the other four. Naming the one case that runs against your pattern, immediately, in its own sentence, is what stops a reader discovering it themselves; it also implicitly reports that the author checked all five.

### The one correlation on the page, spent on the weakest result

> It's also the one where the co-occurrence of upside and downside is weakest (with a correlation score of +0.16 vs an average of +0.25). Usually the people most engaged with the upside of a tension tend to be similarly engaged with its downside; here, the groups diverge.

**Annotation.** The only coefficient in 4,300 words, and it is spent on the tension that least supports the thesis, against the mean of the five. That instinct is right — precision where the result is weak, words where it is strong — and it is the opposite of the usual failure. Note what it also reveals: four other correlations exist and are in the appendix, so the reader is given the weakest number and told the rest are elsewhere. A general-audience piece can do that; a post of ours must publish the whole vector or say why not.

### An alternative explanation rebutted by a prediction

> But the instrument can't explain everything. If interview structure were driving the co-occurrence, you'd expect it to be roughly uniform across all five tensions and all groups. Instead the co-occurrence ranges from 1.6 to 3.0 times, and some of the tensions are notably asymmetric across different groups of people.

**Annotation.** The most rigorous passage on the page and the one to copy verbatim in shape: name the rival explanation, state what the data would look like **if** it were true, then show what the data looks like. Two sentences, no statistics, and a falsifiable structure. This is how to argue against a confound in prose for a reader who will not read a robustness table.

### What against why — the comparison that positions the publication

> Surveys and usage *analysis* tell us *what* people are doing with AI, but the open-ended interview format helps us get at *why*.

**Annotation.** The instrument comparison, saved for the Conclusion, with the italics carrying it and the word "analysis" hyperlinked to the Economic Index. Two instruments, one clause each, no claim that either is better. For any post of ours that joins interview or survey material to usage data, this is the sentence that defines the division of labour, and it is the page's own invitation to attempt the join it does not attempt.

## Figure captions

Eight captions. **Format:** a plain paragraph in small type directly below the exhibit; no bold; no italic; no "Figure N"; no title sentence; no source line; no sample size; no period; no units. Nothing on the page is numbered, so nothing in the prose can cross-reference an exhibit — the text always says "below" or nothing at all. Three of the eight captions carry the interview question verbatim; two explain an encoding; two are the same boilerplate with one word changed; and two state a finding.

### The three ranked-list captions — the question as the provenance

> What respondents most wanted from AI, classified by Claude from their open-ended answers to "If you could wave a magic wand, what would AI do for you?" 1% of respondents did not articulate a vision. Hover to see example quotes.

> What respondents said AI had already done for them, classified from open-ended answers to the question "Has AI ever taken a step towards that vision for you?"

> What respondents worried about, classified from open-ended answers to the question , "Are there any ways in which AI could be developed that would be contrary to your vision or what you value?" Respondents tended to raise multiple concerns, so we used a multi-label classifier (response can map to multiple concerns).

**Annotation.** **Putting the prompt verbatim in the caption is the best thing on this page.** A share of an open-ended answer is meaningless without its question, and the caption is the only place any of these three questions appears. The pattern is: what is plotted ("What respondents most wanted from AI") → who classified it → the question in quotation marks → the one rule a reader needs to avoid misreading the exhibit → an interaction cue. The rules are chosen well: the first caption gives the non-response share, so nobody assumes the nine categories exhaust the sample; the third states that the codes are multi-label, so nobody adds them up. Both are limitations placed in the caption, where they cannot be skipped.

Three faults. Only the first caption says **"classified by Claude"**; the other two say "classified" with no agent, so the provenance fence is dropped in two of three — and, per `room/director-2026-09-16-caption-amendment.md` and the claims discipline, the provenance belongs in every caption that reports a model-generated code. The stray comma after "the question" in the third is in the source. And the seven-item experiences exhibit is introduced in prose as "six main areas", so the caption sits under a list whose own count the text gets wrong.

### The paired-bars caption — the measure defined inside the caption

> In these paired bar charts, each bar shows the share of respondents who were excited about the benefit on the left, vs. worried about the harm on the right—split into those who've experienced it firsthand (darker) and those who anticipate it (lighter). Firsthand experience can also include firsthand observation, but does not include e.g. news reports.

**Annotation.** One caption governing five exhibits, correctly — the encoding is identical, so it is explained once. Its parts: the plural subject that scopes it to all five ("In these paired bar charts"), position as the first encoding (left/right), shading as the second (darker/lighter), and then **a definition sentence that bounds the constructed variable at both ends**: firsthand includes observation, excludes news reports. That last sentence is the non-technical equivalent of `economic-index-2026-01-blog`'s Exhibit 4 caption, which defined both its axes before using them, and it is the detail to carry into house style: when an exhibit turns a judgement into a binary, the caption says what falls on each side of the line.

### The country map caption — a caption asserting what the prose never quantifies

> Rate of overall positive sentiment toward AI in each country. Bigger bubbles mean more respondents from that country; green means more positive about AI, blue means less. AI sentiment is majority-positive everywhere (no country dips below 60%) and the range is narrow, but lower and middle income countries are reliably more positive than average.

**Annotation.** Three sentences: what is plotted, the two encodings (size, colour), and then a finding — including a universal claim in a parenthesis and the word "reliably", which reads as a claim about sampling error that nothing on the page supports. **The body prose never states this finding with a number**, so the caption is carrying an assertion the text declined to make; that is the same fault as the January 2026 "predicts" caption, one degree worse because it is a universal. `wiki/reports/survey-81k-interviews-2026-03.md` records that the parenthesis does not hold on the page's own published data without a minimum-respondent display rule that the page never states. **A caption never states a relationship the prose has not already stated with its number, and never states a universal at all.**

### The region scatter caption — the unmodelled claim, placed in a caption

> Concern about jobs and the economy was the strongest predictor of AI sentiment overall, and it is especially apparent when grouping by region. Wealthier regions (pink) cluster in the top right (more concerned about the economy, more negative AI sentiment), split from less wealthy regions (green) which are in the bottom left (less concerned about AI's impact on the economy, and less negative AI sentiment). Bubble size reflects the number of respondents in each region.

**Annotation.** The caption opens with the page's most load-bearing statistical sentence, for which no model is shown anywhere, and then teaches the reader to see it in twelve points. The body of the caption is good practice — colour key, quadrant reading spelled out in plain words for both groups, bubble size glossed — and the first sentence should not be in a caption at all. Note also the label defect above this exhibit: the card headed "AI SENTIMENT BY REGION", subtitled "% sentiment on AI, and concern about jobs and economy", lists values that are rates of **negative** sentiment, as the scatter's own axis label states. A label that inverts the sign of every number under it is the single worst thing on the page; no value from it is recorded here, per `room/director-2026-09-16-figure-values-ruling.md`. **If an exhibit's short label and its axis disagree about which direction is good, the label is wrong.**

### The two slope-chart captions — one caption, twice, one word changed

> Comparative slope charts of the most common AI visions in each region, with lines connecting the same theme across both sides to show how rankings shift. Bolded visions were more often expressed in that region. Grey items were similarly or less often expressed.

**Annotation.** The concerns version is identical with "concerns" for "visions". Re-using one caption for two exhibits of the same type is right. Two details to copy: the caption says what the *connecting lines* are for ("to show how rankings shift"), and it explains the **de-emphasised** elements as well as the emphasised ones ("Grey items were similarly or less often expressed") — most captions gloss only the ink the author is proud of.

**The caption pattern in summary.** Plain small type below the exhibit; unnumbered; no title sentence; what is plotted, then every encoding in turn (position, colour, shading, size), then one rule that prevents the commonest misreading, then — for an open-ended instrument — the question verbatim. No exhibit caption on this page carries a sample size, a period, a unit, an uncertainty or a source line, and two carry findings they should not. Claude is named as the classifier in one caption of three where it should be named in three.

**Alt text.** There is none, anywhere: the page has **no `<img>` element and no `alt` attribute at all**, and no `<figure>`/`<figcaption>` markup; every exhibit is client-rendered SVG. The only alt-like strings in the document are the Open Graph and Twitter card fields, which repeat the title. So `room/director-2026-09-16-alt-text-ruling.md`'s `(alt text)` marking has no occasion to be used in this file — and the absence is worth recording twice over, because a piece whose whole argument is that people should be heard is unreadable at the level of every one of its eight exhibits by anyone using a screen reader.

## Limitations

**There is no limitations section.** The method section delegates once, early —

> The Appendix describes our methods in more detail, as well as limitations and some additional analysis.

— and everything else sits beside the finding it qualifies. In page order:

In the caption under the visions exhibit:

> 1% of respondents did not articulate a vision.

In the method section, on what "AI" refers to and on how occupation is known:

> Answers were reflective of AI usage broadly (i.e. not just Claude), though we redacted names of other AI products.

> what they do for a living (if mentioned)

On how to read the stories:

> There is real ambiguity about how to interpret the diversity of stories we heard: as wins for human wellbeing, as double-edged swords, or as band-aids for broader institutional failures. In truth, it's probably some combination of all three.

On weighting a small category heavily:

> Emotional support comprised only 6% of responses, but these were among the most affecting we encountered.

The one pooled paragraph, inside §"Light and shade", after that section's findings:

> There are some caveats worth naming. These are active Claude users who'd already found enough value to keep using AI, and our interview asked first for positive visions for AI and then for concerns that would counter their vision. Both factors may lead to interviewees lingering on explicit tensions, as well as on the positive (though we filter out those who don't answer the concerns question, they may have put in less effort later in the interview). But the instrument can't explain everything. If interview structure were driving the co-occurrence, you'd expect it to be roughly uniform across all five tensions and all groups. Instead the co-occurrence ranges from 1.6 to 3.0 times, and some of the tensions are notably asymmetric across different groups of people. One might also expect enthusiasts to defend their desired use case, instead of acknowledging the downsides. Instead, those who were excited about emotional support from AI were more concerned about what would happen if their vision came *true*—if they got what they wanted, they might become *too* dependent on AI—than about being prevented from achieving that vision.

On what the speculative harms mean:

> That the systemic concerns remain speculative is not a verdict on AI's ultimate impact as much as a reflection of how early we are in its adoption.

On selection and adoption stage, in the geography section:

> Claude.ai users are likely biased towards early AI adopters who are more excited about new technologies

> But there is also less market penetration in these regions—if AI hasn't visibly entered your daily work yet, AI displacement likely feels abstract, especially when more immediate economic pressures already exist.

On the maturity of the method, in the Conclusion:

> This is a new form of social science. It is qualitative research at a massive scale, and we're in the early stages of learning how to do it.

And after publication, in the Corrections block:

> Mar 19, 2026. "Globally, 67% of people view AI positively" changed to "Globally, 67% of interviewees expressed net positive sentiment toward AI" to more precisely describe the study's methodology.

**Annotation.**

- **The opener is the plainest available.** "There are some caveats worth naming." No "as with all studies", no apology, no hedge on the hedge. Four words of subject and verb. Copy it.
- **Two mechanisms, both named in the authors' own voice, both self-inflicted.** Selection into the sample ("active Claude users who'd already found enough value to keep using AI") and the design of the instrument ("our interview asked first for positive visions for AI and then for concerns that would counter their vision"). Naming your own question order as a threat to your headline result is the equivalent of the January 2026 post naming its own selection bias in the sentence after its largest number, and it is the standard to meet.
- **The rebuttal is the best passage on the page and it is longer than the concession.** Five sentences of argument against two of admission, ending with a second rebuttal ("One might also expect enthusiasts to defend their desired use case… Instead…"). The argument is genuinely good — a prediction, then the data — but the *shape* is advocacy: a reader who skims takes away that the caveat was answered. Concede in full, rebut in less, or split them into two paragraphs so the concession stands on its own.
- **Nothing on this page withdraws a claim.** Compare `economic-index-2026-01-blog`, where two limitations demoted a finding to an "indicator" and a counterfactual to a "signal". Here every finding survives its caveat intact, and the closest thing to a withdrawal — "not a verdict on AI's ultimate impact" — narrows what the *absence* of lived systemic harm means rather than what any positive finding means. A limitation that changes nothing you are willing to assert is decoration.
- **Placement fails in exactly one place, and it is the place that matters.** The caveats paragraph sits in §"Light and shade" and is scoped to the co-occurrence result ("If interview structure were driving the co-occurrence…"). But the question-order concession also threatens the thirteen concern shares and every regional concern comparison, which are in different sections, and it is never carried there. A caveat stated once, three sections away from half the findings it applies to, is the pooled-caveats problem in a new form.
- **Two of the four limitations the authors themselves wrote down are missing from the page.** The appendix's limitations are four bullets under "A few limitations are worth naming:" — self-reported occupational categories, label ambiguity, user sample, ordering effects *(appendix)*. The feature carries the last two and drops the first two, and the first two are precisely the ones the body leans on hardest: the sharpest economic contrasts on the page are cuts by self-described occupation, and every number on the page is a label. The method paragraph also drops one word the appendix uses — the appendix calls the classifiers "hand-validated" and reports an agreement check; the feature says only "Claude-powered classifiers" and reports no validation at all *(appendix)*. **The blog-only reader is left with less warrant than the authors have**, which is the same failure mode as delegating classifier validation to chapter two of a report.
- **The response funnel is in the appendix and not on the page.** The appendix states how many interviews were received before quality filtering and how many met the threshold *(appendix)*; the feature gives only the number who "took the interview". A general-audience piece can leave the funnel out of the body — but then the caption or a footnote has to say that a filter exists, and here only one filter is ever mentioned, in a parenthesis, three thousand words in.
- **What a referee raises first, in order.** (1) "the strongest predictor of overall AI sentiment" is asserted twice with no model, no competing coefficients and no controls, and it is the sentence the geography section rests on. (2) Every quantity is a Claude classifier output and the page reports no validation, no agreement rate and no per-language check — on a study whose distinguishing claim is that it spans 70 languages, differential classifier behaviour by language is a live alternative explanation for the regional findings. (3) Question order is conceded and then argued against rather than tested, when randomising it was available to an AI interviewer at this scale. (4) No denominator is stated beside any share, and the page's own numbers rest on more than one base. (5) The occupational cuts have no counts and no uncertainty. (6) The map caption's "no country dips below 60%" is a universal claim that the page's own published data does not support without an unstated display rule. Any one of these in a post of ours would be sent back.
- **The correction is the model.** Old wording quoted, new wording quoted, reason given, dated, left on the page permanently. That is what a limitation discovered after publication should look like.

## Close

Two closes. §"Looking forward" is what comes next; §"Conclusion" is what was learned. Verbatim, with the thesis restatement that precedes them both at the end of §"Light and shade":

> It's easy to assume there are AI optimists and AI pessimists, divided into separate camps. But what we actually found were people organized around what they value—financial security, learning, human connection— watching advancing AI capabilities while managing both hope and fear at once.

> ## Looking forward

> These interviews give us a sense of what people want from AI broadly, which informs how we build Claude. They reinforced the importance of work we're already doing, and pointed us toward new questions to ask.

> Most of the visions people described, ranging from personal transformation to cognitive support, collapse into an underlying desire: that AI helps them live *better*, not simply work *faster*. Our next Anthropic Interviewer study, launching shortly to a small subset of Claude users, focuses on Claude's effects on people's wellbeing over time: whether Claude is actually making people's lives better in the ways they want, and how it could do so more effectively.

> ## Conclusion

> AI poses both opportunities and risks. This is true—but also, at this point, a cliché. One of our goals for this research is to offer a complement to the abstractions we all tend to use in speaking about AI; to capture the texture that more vividly renders exactly how we are already experiencing these opportunities and risks worldwide. Before this research, it was hard for us to see any kind of broad qualitative picture—the way AI has already become intertwined with people's lives, nurturing aspirations but also feeding anxieties; how it feels to exist in a world on the precipice of sweeping technological change.

> This is a new form of social science. It is qualitative research at a massive scale, and we're in the early stages of learning how to do it. Surveys and usage analysis tell us *what* people are doing with AI, but the open-ended interview format helps us get at *why*. Conducting this research has moved us and challenged us. We did not expect so many deep, open, and thoughtful responses. By far the most common reflection from our team was that it was viscerally moving to see Claude impacting people's lives for the better, and equally motivating to hear their concerns.

> We don't usually get to hear from small business owners around the world using Claude to reclaim time to spend with their young children or aging parents, or from truck drivers and butchers building new careers with the help of Claude, or from teachers in under-resourced schools using Claude to surpass what they achieved when they taught in well-funded schools. We were surprised by the incredible volume of people who have been supported by Claude in their educational or personal growth endeavors, and the people finding in AI freedom from judgment in a way they hadn't experienced before. We were equally gripped by the fears and downsides—people saying that the same availability making Claude useful is what makes it hard to put down, or knowledge workers worrying about outrunning AI's economic impact. When you come into contact with this much raw human experience, it knocks you sideways. The usefulness is real, and the question for all of us is how to claim the benefits without incurring undue costs.

> To the 81,000 people who took the time to speak with us: thank you. It has been striking, and humbling, to see Claude form the basis of so many people's hopes, dreams, and fears. These interviews remind us what it means, and what it takes, to build AI that benefits everyone.

**Annotation.**

- **What was learned.** The finding sentence of the close is not in the Conclusion at all — it is the last paragraph of §"Light and shade", and it answers the opening thesis in the same vocabulary ("camps"), which is why the piece reads as closed before the Conclusion begins. The construction is *the reading you had → what was actually found*, with the alternative to camps given not as a number but as a principle of organisation: "people organized around what they value—financial security, learning, human connection— watching advancing AI capabilities while managing both hope and fear at once." Three values named, one participial clause, no digits. **When the finding is about the shape of a distribution rather than its level, the close can be entirely qualitative — and then the body must have carried the numbers.**
- **The cheapest honest opening to a close in the corpus.** "AI poses both opportunities and risks. This is true—but also, at this point, a cliché." Four words of thesis, then the author disqualifies it. It does the work of a paragraph of stakes-setting and it earns the rest of the paragraph, which says what the research adds to a cliché: not a correction, a texture ("to capture the texture that more vividly renders exactly how we are already experiencing these opportunities and risks"). Positioning a contribution *against your own headline* is available to any post whose headline is obvious.
- **Why it matters, as a question rather than a prescription.** "The usefulness is real, and the question for all of us is how to claim the benefits without incurring undue costs." The last sentence before the thanks, addressed to everyone, with no policy named — and the only sentence in the close that could have been a recommendation. Same refusal-to-prescribe as the rest of the corpus, and further: this close does not even displace the recommendation onto researchers or journalists, as `economic-index-2026-01-blog` does.
- **What comes next.** One named, scoped, falsifiable follow-up: "Our next Anthropic Interviewer study, launching shortly to a small subset of Claude users, focuses on Claude's effects on people's wellbeing over time: whether Claude is actually making people's lives better in the ways they want". The construct for the next study is derived from this one's central finding ("live *better*, not simply work *faster*" — the italics carry the derivation), which is how a follow-up should be justified: the finding names the measure.
- **Recommendations, and the problem with them.** All three are to Anthropic, by Anthropic, and two are presented as already running — the wellbeing study, the Beneficial Deployments programme, and "further research" on economic concerns. §"Looking forward" is in effect three paragraphs of programme announcement placed where a reader expects implications, which is the Rwanda-paragraph problem of `economic-index-2026-01-blog` at three times the length. For us: recommendations are *to* Anthropic, are named as recommendations, and nothing of ours is offered as the response.
- **The register that cannot survive the house rules.** "Conducting this research has moved us and challenged us." "it was viscerally moving to see Claude impacting people's lives for the better". "When you come into contact with this much raw human experience, it knocks you sideways." — the only second person on the page. These are the best-written sentences in the piece and they report a change in the researchers, not in the state of knowledge. House style forbids the first person and has no third-person form for any of this; the conversion is not a rewrite, it is a deletion. **Our close states what the evidence changed about the question, not what the work did to the team** — and where the felt weight of the material is the point, it has to arrive through the respondents' own words, which this page has 67 of and does not use in its close.
- **The naming rule inverts in the last two paragraphs, and inverts toward the product.** The body says AI ("What people want from AI", "AI sentiment", "AI's benefits for learning"), warranted by the method sentence that answers were about AI broadly. The Conclusion says Claude seven times, almost always as the subject of a benefit: "viscerally moving to see Claude impacting people's lives for the better", "small business owners around the world using Claude to reclaim time", "truck drivers and butchers building new careers with the help of Claude", "teachers in under-resourced schools using Claude to surpass what they achieved", "supported by Claude in their educational or personal growth endeavors", "the same availability making Claude useful is what makes it hard to put down", and "to see Claude form the basis of so many people's hopes, dreams, and fears". The measurement is about AI; the peroration is about Claude. **That is exactly backwards from the house rule and it is the clearest thing in this file to avoid**: if the findings cannot name Claude, the close cannot either.
- **No numbers in the close except one, and it is the rounded one.** "To the 81,000 people who took the time to speak with us: thank you." The acknowledgements two paragraphs later use the exact count. Thanking the respondents in the final paragraph is proper to this genre and has no analogue elsewhere in the corpus; using the headline rounding to do it, beside an exact count, is the page's denominator problem surfacing in its last sentence.
- **Title against ending.** Title: "What 81,000 people want from AI" — a question about the respondents. Ending: "These interviews remind us what it means, and what it takes, to build AI that benefits everyone." The title asks what people want; the ending says what the answer obliges the builder to do. The match is good but it is a step sideways: the title promises the respondents' answer and the last clause is about Anthropic's mission. The exact match is one paragraph earlier, at the no-camps sentence. **The inverse still holds for us:** a title that names the respondents must close on what the respondents said, not on what the finding implies for us.
- **How it avoids a summary block.** (1) No enumeration: not one of the nine visions, seven experiences, thirteen concerns or five tensions is named again after its own section. (2) One number, and it is the title's. (3) Each paragraph is in a different mode — what the research adds to a cliché, what the method is and is not, what the authors did not expect, and thanks. (4) The contribution claimed is for the instrument ("This is a new form of social science"), not for any finding, exactly as in `economic-index-2026-01-blog`.

## Verification

- **URL fetched:** https://www.anthropic.com/features/81k-interviews — fetched **2026-09-16**, HTTP 200, 716,870 bytes of HTML. `web_fetch` was not used; the page was retrieved with `curl -sL` and a desktop user-agent, and parsed locally.
- **Fetch date:** 2026-09-16.
- **Method.** The raw HTML was stripped of `<script>` and `<style>` content and reduced to 679 lines of visible text, which were read in full. Structure was then read off the markup rather than off the rendering: all `h1`–`h6` elements enumerated in document order (one H1, 20 H2s including the chart cards, the H3/H4 apparatus at the foot and the footer navigation); the eight captions extracted by their caption CSS classes (`HorizontalBarGraph…__caption` ×3, `Pairing…__caption`, `SentimentBubbleMap…__caption`, `ScatterPlot…__caption`, `RegionCompare…__caption` ×2); 31 `<blockquote>` elements with their attribution elements (21 in the body flow, ten in the light-and-shade panels), plus 29 quote cards in the three ranked lists (each duplicated in the markup for mobile and desktop layouts) and five in the opening scroll sequence; all 11 `<em>` elements enumerated with their surrounding context to locate the page's emphasis; body prose measured at 66 paragraphs and ~4,300 words from the `Body…__bodyText` class; all `<a>` elements enumerated to list outbound targets and anchor text. **Every quotation in this file was copied from that fetch and then checked back against it string-for-string after transcription**, with whitespace, curly quotation marks and dashes normalised for the comparison only.
- **Appendix.** The 14-page appendix PDF (https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf, HTTP 200, 263,879 bytes, read via `pdftotext -layout`) was consulted **only** to check what the feature's method and caveats paragraphs compress. Three places in this file rest on it and are marked *(appendix)*: its four-bullet limitations list against the feature's one-paragraph version; the word "hand-validated" and the agreement check that the feature omits; and the existence of a quality-filtering funnel the feature does not mention. No appendix sentence is quoted and no appendix number is reproduced here; the appendix is its own slug (`survey-81k-interviews-2026-03-appendix`) and is not annotated in this file.
- **Fetch failures:** none. The page returned on the first attempt and was not truncated.
- **Exhibits that did not render.** Three elements are client-rendered from external data and returned placeholder text in the fetch: the country sentiment bubble map ("Loading data...") and both sets of slope charts ("Loading…"). Their captions are recorded above; nothing was taken from the exhibits themselves.
- **No chart-read numbers.** Per `room/director-2026-09-16-figure-values-ruling.md`, no value printed inside an exhibit is recorded in this file. That covers the one-decimal shares in the three ranked lists, the share and split labels in the five light-and-shade panels (quoted above only with the number elided, as "…% mention this as a benefit"), and every value on the region card and the two scatter axes. Where a point above depends on such a value — the prose/exhibit rounding mismatch, the region card's inverted sign, the map caption's universal claim — the fact is stated and the number is left in `wiki/reports/survey-81k-interviews-2026-03.md`, which records them under its own marking. Numbers appearing in the page's prose and in its captions are quoted as published; those are text, not chart readings.
- **Alt text.** None to record. The document contains no `<img>` element and no `alt` attribute; the only alt-like strings are the Open Graph and Twitter card fields, which repeat the title. `room/director-2026-09-16-alt-text-ruling.md`'s `(alt text)` marking therefore has no occasion to be used, and the absence is annotated in `## Figure captions` because it is a property of the form.
- **Not fetched, deliberately:** the Anthropic Interviewer publication, the user-wellbeing post, the AI for Science and nonprofit programme pages, the economic-policy-responses page and the Economic Index landing page, each of which is its own row in `wiki/INDEX.md`; the Quote Wall's published quote file and the chart data assets behind the exhibits, which belong to the wiki entry and not to a style annotation. No content from any of them is quoted here.
- **Could not fetch:** nothing.
- **Quotation caveats.** Hyperlink URLs were stripped from quoted prose and the anchor text retained; the anchors for the opening are listed in `## Opening move`. The footnote marker was removed from the doubled standing claim. Typographic apostrophes and quotation marks in the source were normalised to ASCII, and where a double quotation mark is nested inside an inline quotation it is rendered as a single quotation mark ("a vision for what 'AI going well' means"); em dashes, the non-breaking hyphen (U+2011) in "open‑ended" in the scroll sequence, and all numerals are as fetched. Source emphasis is reproduced: italics as `*…*`. **In the opening scroll sequence the opening quotation mark of each of the five respondent quotations is a separate decorative element and no closing mark exists**, so the quotation marks around those five in `## Opening move` are this file's; the body block quotes carry both marks in the source. The same absence affects all ten light-and-shade panel quotations, which open with a quotation mark and never close it. Respondent attributions sit inside the `blockquote` element on the page with no separating punctuation, so extraction runs them onto the end of the quotation; where a respondent quotation is reproduced above, the attribution is set after an em dash, which is a rendering choice and not a change of text. The category definitions in `## Findings and their caveats` are shown as `Name — definition`; on the page the name, the share and the definition are three separate elements and the dash is this file's. **One space was inserted:** the scroll sequence's thesis line is marked up as "…hope and \<span\>alarm\</span\>didn't divide people into camps…", so the page renders "alarmdidn't" with no space; it is quoted above with the space and recorded here as a source defect. Elisions inside short inline quotations in the annotation prose are marked `…`; no block quotation is elided except the two panel labels where a chart value has been removed under the ruling above.
- **Source defects noted in passing**, all recorded here because they bear on form rather than on findings: the H1 carries a hard line break; there is no dateline anywhere; the scroll sequence's thesis line renders without a space between "alarm" and "didn't"; respondent attributions are inconsistently capitalised between the scroll sequence and the body, and two quotations are re-used at different lengths in different components; the five scroll-sequence and ten light-and-shade panel quotations all open with a quotation mark and none closes it; the split-bar labels are not in a consistent order across the five panels and one panel reads "saw it" where the others read "have seen it"; the concerns caption contains a stray comma; the prose says "six main areas" above a seven-item list; and the region card headed "AI SENTIMENT BY REGION" carries negative-sentiment rates. The numeric discrepancies behind the last of these are in `wiki/reports/survey-81k-interviews-2026-03.md`, §Verification.
- **Scope.** This file annotates how the piece is written — its section order, its use of respondents' words, how it frames hopes and fears, how it presents country and language breadth, and how caveats appear in a non-technical register. It makes no judgement about whether its findings are correct, it does not summarise them, and it reproduces no number from any released data file.
