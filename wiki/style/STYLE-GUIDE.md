# The Anthropic economics style guide

Derived from the twenty-three annotated files in `wiki/style/`, read in full on 2026-09-16. Every pattern below is supported by at least one quotation, attributed to the corpus file that verified it against its source and, through that file, to the source and page. No number read off a chart image appears here (`room/director-2026-09-16-figure-values-ruling.md`). Where the corpus is inconsistent, the inconsistency is stated rather than averaged.

This guide is the reference; `.claude/skills/anthropic-style/SKILL.md` is the operational digest. Before drafting, read the three corpus files closest to the post in hand, not this guide alone.

---

## Scope and sources

Twenty-three files, one per publication, annotated under nine fixed H2 headings (`Source`, `Section order`, `Opening move`, `Findings and their caveats`, `Comparisons`, `Figure captions`, `Limitations`, `Close`, `Verification`) per `room/director-2026-09-16-session-1-1-kickoff.md` §B. Programme and product pages are excluded by ruling (`room/director-2026-09-16-index-rulings.md`, item 4): the corpus annotates research writing only.

**Seven kinds of piece, with different rules.** The commonest drafting error against this corpus is to copy a device from a piece of a different kind.

| Kind | Files | Defining property |
|---|---|---|
| **Launch post** | `economic-index-2025-02-report` | Announces an instrument and reports its first findings at once. ~1,700 words, no authors, categorical byline, four captioned exhibits, caveats under an H3 inside Results. |
| **Companion paper** | `economic-index-2025-02-paper` | NeurIPS-format preprint, 38 pp, fifteen authors, seven appendices. "**The appendix is longer than the paper.**" No Results section: findings live inside "3 Methods and analysis". |
| **Wave report** | `economic-index-2025-03-report` (web-only), `-2025-09-report`, `-2026-01-report`, `-2026-03-report`, `-2026-06-report` (PDF + web) | Numbered instalment of a standing series. Cover, Introduction with "We find:" blocks, chapters with overviews, "Concluding remarks". No abstract, no methods section, no limitations section. |
| **Companion blog** | `economic-index-2025-09-blog`, `-2026-01-blog` | Same-day summary of a PDF report for a reader who will not open it. "Below, we summarize its results." |
| **Special report** | `economic-index-2025-04-software-development` | Off-cycle, one cut of the data, a product surface as the subject. H3-only headings, Limitations promoted to its own section. |
| **Team paper** | `labor-market-impacts-2026-03`, `productivity-gains-2025-11`, `claude-code-expertise-2026-06`, `coding-agents-social-sciences-2026-05`, `skill-formation-rct-2026-01`, `worker-retraining-2026-08` | Named byline, references, a public repository or a linked appendix. Two to five authors; the mentor co-authors three of the six. |
| **Survey write-up and Institute feature** | `survey-81k-interviews-2026-03` (feature), `survey-81k-economics-2026-04` (report-length blog register) | Evidence is what people said. Respondent quotes are components of the argument; the instrument's question wording is the definition. |
| **Methodology appendix** | `economic-index-2026-03-appendix`, `-2026-06-appendix`, `labor-market-impacts-2026-03-appendix`, `coding-agents-social-sciences-2026-05-appendix`, `claude-code-expertise-2026-06-appendix` | Hands over machinery; argues nothing; ends without a close. Length runs from 1,019 words (`economic-index-2026-03-appendix`) to 27 pages, 66% of it prompt text (`claude-code-expertise-2026-06-appendix`). |

**Sizes, for calibration.** Launch post ~1,700 words; special report ~1,900–2,000; companion blogs ~2,000–2,300; the 2025-02 paper ~5,900 words of body plus ~4,900 of appendix; the September 2025 report 47 pp and ~9,000–10,000 words plus ~2,000 of footnotes; the January 2026 report 55 pp and ~14,200 words; the retraining review 124 pp and ~45,700 words. Our posts sit nearest the special report and the shorter team papers.

**One corpus-wide asymmetry worth knowing before drafting.** Every economic-index piece measures Claude usage. Four pieces do not, and their register differs accordingly: `productivity-gains-2025-11` measures what Claude *said* about its users' tasks; `skill-formation-rct-2026-01` measures a GPT-4o-based assistant in a trial; the two survey pieces measure what people said about AI; `worker-retraining-2026-08` measures other people's trials, with Claude used only as a literature-extraction instrument ("**'Claude' appears exactly five times in 124 pages, and every one of them is the research instrument**" — `worker-retraining-2026-08`).

---

## Structure

### The wave report, and the pattern our posts inherit

Cover → Introduction (puzzle or occasion, thesis, one "We find:" block per chapter) → chapters, each *Overview → sections → Conclusion* → "Concluding remarks". Three constants:

1. **Findings appear three or four times, at three or four depths, in the same order each time.** "Four times each, at four depths, in this order: the abstract (numbers, no figures, no sample); the numbered contributions in the Introduction …; §3.1–3.5 (number, figure, worked exemplars, and the procedure that produced it in the same subsection); the Conclusion (numbers again, stripped of figures and exemplars)" (`economic-index-2025-02-paper`). The report architecture is written "to be read in three depths (bullets, overviews, chapters), and each depth is self-consistent" (`economic-index-2025-09-report`).
2. **Precision increases with depth, never the reverse.** Singapore's index is "4.6x" in the Introduction, "4.5 times" in the chapter overview, "4.57" in the chapter body — "Three roundings of one quantity, each matched to how hard the surrounding prose is working. The pattern to copy is the direction: coarser at the top, exact in the body — never the reverse" (`economic-index-2025-09-report`). The failure mode is changing the *unit* at the top rather than the rounding: the March 2026 report's summary says "a 10% higher success rate" where the table says ▲ +6.4 pp and the regressions say 5, 3 and 4 percentage points — "the summary chose the one that reads largest by switching units" (`economic-index-2026-03-report`).
3. **The sample arrives after the headline numbers.** "a reader reaches every number in the report before reaching the description of the data that produced it" (`economic-index-2025-09-report`). This is the settled series architecture and it is *not* ours: our template puts the methodology section in the post and the sample in it.

### Where the method sits

The series rule is **define at point of use, document in footnote** (`economic-index-2025-09-report`). "There is no 'Data and methods' heading in the 47 pages."

Three variants, all defensible:
- **Split by function.** `productivity-gains-2025-11` puts the task-level method before its validation and the aggregation method immediately before the aggregate, so "each method sits directly above the numbers it produces, so neither is read in the abstract."
- **A methods chapter for a new instrument.** `economic-index-2026-01-report` adds Chapter 2 on the five primitives, placed before the chapters that use them: "**The transferable structure is the pair: a methods chapter for the instrument that is new, point-of-use definitions for everything derived from it.**"
- **Every number with its instrument attached.** `claude-code-expertise-2026-06` distributes six method passages, each immediately before the number it licenses: "**every number arrives with its instrument attached, and no number can be quoted from this paper without passing the paragraph that defines it.** This is the single most transferable structural fact about the piece."

The failure mode is exporting the constructs. `economic-index-2026-03-report` sends the reader out four times ("See the Appendix for definitions of the interaction types"), with the consequence that "of the eleven exhibits, the four that carry the report's most interesting quantities … cannot be interpreted from this document alone."

### Headings

Three devices, and the choice is a real one.

- **Declarative headings that assert the finding.** `coding-agents-social-sciences-2026-05` puts five of seven findings in its headings; "**A reader who reads only the table of contents has the paper.**" Two of them carry their own counter-clause: "Coding agent users are posting more working papers and sending out more grant proposals, **but not submitting more to journals**"; "Researchers expect AI tools to raise productivity, **but are less confident** that they will improve social science overall". "**A heading that contains the word 'but' is the most compressed form of number-plus-caveat available.**"
- **Question headings.** `economic-index-2025-03-report` uses three ("What's changed since the launch of Claude 3.7 Sonnet?"); `economic-index-2025-04-software-development` uses a **how / what / who ladder** ("How do developers interact with Claude?", "What are developers building with Claude?", "Who is using Claude for coding?"); `economic-index-2026-01-blog` makes the question headings the summary block: "a reader who scans only the H4s gets … three questions, no answers, and no number they could carry away wrongly. **This is the device to copy when house style forbids a summary block.**"
- **Sentence headings with the qualifier inside.** `worker-retraining-2026-08` §1 runs seven: "1.1 In the US, average impacts are positive but not transformative."; "1.2 Monetary benefits exceed costs on average, under reasonable but debatable assumptions."; "1.7 The sector approach can probably help society respond to AI's disruption of work. But the approach is not formulaic and will probably fail if treated as such." "**The qualifier is inside the heading** … **A heading may be two sentences** when the second one is the limit on the first … **the unit of the claim is in the heading** where it is the finding."

The corpus is inconsistent on whether a heading should assert. `claude-code-expertise-2026-06` asserts in only two of thirteen, and both are relations rather than magnitudes: "**Where a heading does assert here, it asserts a relation and not a magnitude**, which is the form that survives a reader who never reaches the section." `worker-retraining-2026-08` states the resolving rule for figures, which generalises: "**when a figure shows other people's estimates, the title says what is plotted; when it shows your own headline, a title that asserts is a claim you must own.**"

### Long pieces: the named summary subsection

`worker-retraining-2026-08` closes each evidence block with one — "4.5 Major American randomized evaluations: summary", "6.5.5 … summary", "7.4 Sector programs: Summary" — "which is how a long piece stays navigable without a summary block at the top." Multi-part closes work the same way: `economic-index-2025-09-report` closes each of three chapters and then once more at a level of abstraction none of the parts reached, and "each chapter close also **contains its own hedge on its own headline** … so no section ends on its strongest possible reading."

### Placement faults the corpus itself flags

- An appendix finding after the close: `economic-index-2025-04-software-development`'s software-versus-non-software comparison sits below "Looking ahead" — "**A benchmark that tells the reader whether the headline is large belongs beside the headline, not after the conclusion.**"
- A number making its first prose appearance in the close: `economic-index-2026-03-report`'s Discussion opens with "33% of traffic, up from 28%", supported only by data labels inside Figure 1 — "A number that a reader meets for the first time in the close is a number they cannot check."
- A caveat eleven pages from its finding: the Super Bowl footnote in `economic-index-2026-03-report`, which explains the composition of the low-tenure comparison group and is never joined to the tenure result.

---

## Register

### Person

Every piece in the corpus is written in the first person plural. Our house style forbids it, and the corpus supplies its own substitutes, which are better than a bare passive:

- **Attribute to the exhibit.** "Figure 2.7 suggests that…" (`economic-index-2025-09-report`); "The plot shows that long-tenure users are about 5 percentage points more likely…" (`economic-index-2026-03-report`); "The left panel in Figure 3 shows that…" (`survey-81k-economics-2026-04`).
- **Attribute to the analysis or the result.** "The data suggests it is not" (`economic-index-2025-09-report`); "These results suggest…"; "This control moderates the effect somewhat" (`economic-index-2026-03-report`).
- **Attribute to the instrument.** "Claude estimates that…", "Claude assesses…", "Claude classifies…" (`economic-index-2026-01-report`); "Our classifier identified 93% of Claude conversations as producing an artifact" (`economic-index-2026-06-report`).
- **Put the measure in subject position.** `claude-code-expertise-2026-06-appendix` does it half the time already — "the task value estimator reaches", "the pricer anchors", "the share of sessions judged Succeeded rises" — and the annotation draws the rule: "**put the measure in subject position and the researcher disappears without a passive.**"
- **Passive with the definition named, not the definer.** "as defined by the tasks Claude is observed performing" (`survey-81k-economics-2026-04`); "A respondent was coded as indicating job threat if…" (same, Figure 1 caption).

Four first-person constructions do **not** survive de-personalisation, and knowing that is the point of recording them.
1. **The institutional promise.** "we'll repeat many of the analyses above over time" (`economic-index-2025-02-report`) — "The rhetorical work being done — a promise that binds the author — has to be replaced, not merely de-personalised." Attribute the commitment to the series or to the post's own reproduction section.
2. **The disciplinary "we".** "how **we** study the economy and society" (`coding-agents-social-sciences-2026-05`) — the authors are members of the population they surveyed, and "the substitute is to name the population … which costs the sentence its implication of shared exposure."
3. **The collective "we".** "we're still collectively deciding how much confidence we have in AI tools" (`economic-index-2025-09-blog`) — "the collective 'we' is the companion form's signature move and it is also the point at which the writing stops being empirical."
4. **Opinion.** "we think these estimates might overstate current productivity effects" (`productivity-gains-2025-11`, four uses of "we think") — "the replacement is to state the direction of the bias without a believer, which is stronger."

### Hedge vocabulary, graded

The corpus files each collect their own ladder. Merged, in descending confidence: *we find · we document · the data shows · we replicate · we see · reveals · indicating · implies · suggests · appears to · tends to · skews toward · is associated with · may reflect · could reflect · might predict · likely · potentially driven by · perhaps · we suspect · we speculate · our best guess is · we're not yet sure why this is · the message is unclear · considerable uncertainty remains · more research is needed here.*

Rules the corpus keeps:
- **Never *shows*, *proves*, *demonstrates* or *causes* of a causal claim.** Confirmed in `economic-index-2025-09-report`, `-2026-01-report`, `-2026-03-report`, `-2026-06-report`, `labor-market-impacts-2026-03`.
- **One rung per claim.** "The report almost never uses two rungs for one claim … The rung chosen is legible evidence of how much work the underlying analysis did" (`economic-index-2025-09-report`).
- **The one licensed bare causal verb is decomposition.** "This is caused, mechanically, by a rise in personal queries" — "**When causation is decomposition, say *mechanically* and drop the hedge; when it is behaviour, hedge and keep the verb weak**" (`economic-index-2026-03-report`).
- **Attribution to the instrument is not a hedge.** "These are not hedges. They name the instrument. A sentence can be fully confident and still take one" (`economic-index-2026-01-report`).
- **Symbols as hedges.** The 2025-02 paper uses "∼" for every share whose *threshold* is arbitrary and no tilde on exact percentages (`economic-index-2025-02-paper`).
- **Speech verbs instead of hedges, for self-reports.** `survey-81k-economics-2026-04` runs eleven findings on eleven speech verbs — *voiced, mentioned, express, reported, conveyed, describe, indicated, cited, emphasized, talk about* — and "no sentence in the document says that a respondent *was* more productive or *was* at risk. The verb does the epistemic work that a hedge would otherwise have to do."

### Frequencies, where the corpus counted them

- `productivity-gains-2025-11`: `estimat*` **104** times in pp. 2–21, "roughly one word in forty"; "we" 79, "our" 42; `AI` 87, `Claude` 86 ("as close to parity as the corpus gets"); "could" 11, "might" 14, "may" 7, "likely" 7; `current*` 15; "in our sample" 9; "we think" 4; "implicitly assumes" 2; "exercise" 2; "significantly" 2 (neither of a measured effect); "should" 1; *policy*, *policymaker*, *recommend* **0**.
- `claude-code-expertise-2026-06`: "session" ~112, "Claude" 56, `\bAI\b` **2** in eighteen pages, "persistent" 19 printed occurrences — none inside a sentence.
- `survey-81k-economics-2026-04`: "estimate" **0**, "regression" **0**, "suggest" **0**, "weight" **0**, "p<" **0**, "N=" **0**; "significant" 1 and non-statistical; "sample" 1; "infer/inferred" 15; "respondent(s)" 35; "Claude" 30; `AI` 32. "**'Suggest' does not appear in the document** … The rungs the reports lean on … are replaced here by speech verbs."
- `labor-market-impacts-2026-03-appendix`: "limitation" **0**, "caveat" **0**, "robust" **0**; "In practice" 4, "seem/seems" 4, "likely" 4; ~30 "we"/"We", 13 "our".
- `economic-index-2025-09-report`: "Surprisingly" used four times in 47 pages — "which is what makes it carry weight."
- `claude-code-expertise-2026-06-appendix`: 7,678 words, of which 5,079 (66%) are monospace prompt text and 1,986 (26%) body prose — "The proportion is the document's editorial thesis: the instrument is the contribution, and prose exists to hand it over."

### Naming: AI, Claude, and the constructs

**The corpus finding, stated in five files:** the question, the title, the stakes and the policy sentence say **AI**; the sample, the index, the numbers and the captions say **Claude** (`economic-index-2025-09-report`, sharpened in `-2026-01-report`).

Constructs follow one rule: **the name says AI, the measurement says Claude.** "the construct is called the **Anthropic AI Usage Index** and is defined as a geography's 'share of Claude usage' … The naming rule is not applied to this report from outside — it is built into the report's central construct" (`economic-index-2025-09-report`). Likewise "**AI** autonomy … defined as 'the degree to which users delegate decision-making to **Claude**'" and "Effective **AI** coverage tracks the share of a worker's time-weighted duties that **AI** could successfully perform, **based on Claude.ai data**" (`economic-index-2026-01-report`, Figure 4.4 — "name says AI, sample says Claude — the correct form").

Two model sentence pairs:
> "The coverage shows **AI** is far from reaching its theoretical capabilities. For instance, **Claude** currently covers just 33% of all tasks in the Computer & Math category." — `labor-market-impacts-2026-03`, "General claim, AI; measurement, Claude; adjacent sentences, no hedge lost. Copy this pair."

> "people who use **Claude** in the most automated way expect **AI** to take on more of their tasks in the next year" — `economic-index-2026-06-report`. "**The rule this wave adds to the corpus:** the split is not only question-versus-number, it is *measured behaviour versus stated belief*."

**Three refinements the corpus adds.**
- `claude-code-expertise-2026-06` runs a three-step ladder instead of a binary: "**Claude / Claude Code** for everything measured · **coding agents / agentic coding / the agent** for the class the finding is about · **knowledge work** for the extrapolation. Each rung is a wider claim on thinner evidence, and the paper never uses a wider word for a measured sentence."
- Where the product under study is Anthropic's own and the population is the sponsor's, the measured construct is named as a *class*: `coding-agents-social-sciences-2026-05` measures "coding agent users", not Claude Code users — "**when the product under study is the sponsor's own, the measured construct is named as a class and the product appears only where it is the object of a sentence.**"
- Where the measured object is genuinely a belief about AI, the findings say AI, and the method says so once: "Answers were reflective of AI usage broadly (i.e. not just Claude)" (`survey-81k-interviews-2026-03`). "**State once, in the method, which of the two your measured object is, and then never drift.**"

**Where the corpus breaks its own rule, it breaks in three places: the summary, the caption and the close.** Recorded so a draft can be checked at exactly those points.
- `economic-index-2026-01-report` Chapter 4: "**AI** excels at what they spend most of their time doing"; "For data entry clerks, **AI** likely does substitute for tasks previously performed manually" — "Every one of these is a statement about what was observed in Claude.ai and 1P API data, and every one says AI." The file names it "the counter-example to hold a draft against."
- `economic-index-2026-03-report` Figure 1.5's in-image title reads "Geographic convergence of **AI** usage" for an index built entirely on Claude usage; `labor-market-impacts-2026-03` labels its control arm "no **AI** exposure" for a group defined by not clearing a Claude usage floor.
- `survey-81k-interviews-2026-03` inverts toward the product in its last two paragraphs, saying Claude seven times as the subject of a benefit where the body said AI: "The measurement is about AI; the peroration is about Claude. **That is exactly backwards from the house rule.**"

### Unit discipline

One quantity, one noun, everywhere including legends and captions. Two recorded failures:
- "The language shares are 'of all queries' …; the task shares are 'of conversations' … 'Interactions' is the unit in the opening …, and footnote 1 adds 'sessions' for Claude Code. Four nouns for the denominator across the report, never reconciled. Recorded as a writing fault worth avoiding absolutely: **one denominator, one noun, defined once**" (`economic-index-2025-04-software-development`).
- "'actions per prompt' (body) … 'actions per turn' (body and Figure 3's legend) … with '2,400 words of output' given per *turn* and '600 words of output' given per *prompt* one page later … **One quantity, one name, everywhere including the legend**" (`claude-code-expertise-2026-06`).

Relatedly, **within a paragraph, one unit; where the unit changes, say so in the same sentence** (`economic-index-2026-03-report`, on "increased by 14% in the API" sitting one sentence from "from 3% to 5% of its traffic").

### Sentence-level conventions

- **Approximate quantities in words, measured ones in numerals.** `survey-81k-economics-2026-04` writes "One fifth", "about half", "about a quarter" for shares whose base is loose and 1.3, 5.1, 42%, 48% for point estimates — "a consistent and useful convention: … so the reader can see which is which without being told."
- **Counts, not percentages, below about thirty observations.** `skill-formation-rct-2026-01`: "21 out of 25 participants", "11 of 15 sessions", and the annotation "**Below about thirty observations, report counts; a percentage of 25 people invites a comparison with a percentage of a million.**" `claude-code-expertise-2026-06-appendix` reports agreement as "11 of 15" for the same reason: "**Small denominators are published as fractions, not shares.**"
- **The n travels with the label, not with the exhibit.** `skill-formation-rct-2026-01` labels every cluster "**AI Delegation (n=4)**", "**Generation-Then-Comprehension (n=2)**" — "the minimum discipline that lets a two-person cluster be published at all."
- **Ranges rather than point estimates where two specifications disagree, with each end named.** "'2.6-2.8', '1.7–1.8', '\$1,000–1,100', '\$700–800' and says which end is which. **Where a finding is robust to a specification choice, publishing the range is shorter than publishing the sensitivity analysis**" (`worker-retraining-2026-08`).
- **A slope in decision units.** "for every additional \$10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points" (`economic-index-2026-03-report`) — "**Stating a slope per \$10 rather than per dollar or per log point is the move that makes an elasticity legible.**" Also "For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points" (`labor-market-impacts-2026-03`).
- **Sentence length.** The corpus's most quoted sentences are short and its openings are shortest: "Agentic coding has taken off." (four words, `claude-code-expertise-2026-06`); "The groups are very different." (`labor-market-impacts-2026-03`); "These findings are preliminary." (`claude-code-expertise-2026-06`); "There are some caveats worth naming." (`survey-81k-interviews-2026-03`); "We begin at the task level." (`labor-market-impacts-2026-03-appendix`); "Some of these inferences will be wrong." (`survey-81k-economics-2026-04`). Long sentences occur where a definition or a control set is being enumerated, not where a claim is being made.

### What is never done

- No statistical "significant" without a stated test. "A significant increase in Feedback Loops (+18.3%) — no test, no interval, no n anywhere in the report. In our posts the word is reserved for a stated test or not used" (`economic-index-2025-04-software-development`).
- No magnitude word standing in for a finding. "**a magnitude word is not a finding, and a number that lives only inside an image cannot be cited**" (`economic-index-2026-03-report`, on "increased slightly" / "decreased sharply").
- No superlative attached to a finding. Across the corpus, "first-of-its-kind", "largest", "most comprehensive" modify a *cut of data* or an instrument, never a result: "The word 'first' does not modify a finding anywhere in the Introduction" (`economic-index-2025-09-report`).
- No mechanism asserted without a marker. The one recorded lapse: "The researchers adopting coding agents are the juniors—more technologically fluent, more likely to be working directly with code and data, and facing stronger career pressures … **An explanation the data cannot see takes a modal or an adverb, even when it is obvious**" (`coding-agents-social-sciences-2026-05`).
- No "This makes sense" as a transition. "**'This makes sense' is a confidence claim disguised as a transition, and it is the one thing in the opening half not to copy**" (`economic-index-2025-09-blog`).

---

## Openings

Nine types, all attested. The choice is determined by what the post's contribution is.

**1. Forecast → therefore measure.** `economic-index-2025-02-report`:
> "In the coming years, AI systems will have a major impact on the ways people work. For that reason, we're launching the Anthropic Economic Index…"

"The move is *forecast → therefore measure*, not *question → therefore test*." Three paragraphs of stakes before the first number, which arrives at "roughly 36%" about 150 words in: "Three paragraphs of why-it-matters buy the right to a bare bullet of percentages with no method attached."

**2. The gap in the literature → therefore the instrument.** `economic-index-2025-02-paper`:
> "Despite widespread speculation about artificial intelligence's impact on the future of work, we lack systematic empirical evidence about how these systems are actually being used for different tasks."

The gap is made specific by enumeration, not assertion: three methodologies, each with its citations, "and then one verb phrase disqualifies all three at once: 'cannot track the dynamic relationship between advancing AI capabilities and their direct, real-world use across the economy.' One sentence, three literatures, one shared limitation. **This is the construction to copy when a post has to say what Anthropic left open: name the existing approaches, then name the one property none of them has.**"

**3. Anomaly → prior literature's explanation → bolded thesis.** `economic-index-2025-09-report`, the strongest in the corpus. "Why is this?" is asked in three words in the third paragraph; the answer is a bolded thesis — "**a hallmark of early technological adoption is that it is *concentrated***" — whose two halves each name a chapter. The first number in the report is somebody else's survey (Gallup's 40%), "used to establish the puzzle, not to support a claim … A post that opens on its own data has skipped the first two moves."

**4. Occasion → window → what is new.** `economic-index-2025-03-report`: "Last month, we launched… Today, we're releasing…". "**This is the move available to a wave report and to nothing else: the reason to look again is that the thing being measured changed.**" Note that its three headline bullets carry **no numbers at all**: "a wave report's opening can state its three findings in the direction-and-rank vocabulary alone … and defer every percentage to the section that earns it."

**5. Concede the objection, then elevate.** `economic-index-2025-04-software-development`:
> "Jobs that involve computer programming are a small sector of the modern economy, but an influential one."

"The opening move is *concede the objection, then elevate* … This is the most efficient opening in the corpus and the one to copy when a post studies a narrow population." Its close discharges it exactly: "software development might be a leading indicator… **The opening's concession and the closing's claim are the same argument, twenty-two hundred words apart.**"

**6. The riddle.** `economic-index-2025-09-blog`: "Travel planning in Hawaii, scientific research in Massachusetts, and building web applications in India. On the face of it, these three activities share very little in common." *Concrete image → apparent puzzle → the construct that dissolves it*, with the construct taught by example and named 600 words later. And the second sentence of the post is its own caveat: "That doesn't mean these are the *most popular* tasks" — "**when the finding is a relative measure, state what it is not, in the sentence after you state it.**"

**7. Questions → therefore instrument.** `economic-index-2026-01-blog`: "Is artificial intelligence really making people faster at work?…" — three questions in twenty-eight words, mapping one-to-one onto the three levels of the body. "Note 'really' in the first question: it concedes that the reader has heard the claim already and is entitled to doubt it. That single adverb does the work that a paragraph of stakes-setting does elsewhere, and it is the cheapest honest opening in the corpus."

**8. The house's own published number, turned into a question.** `skill-formation-rct-2026-01`, and the file names it as the one to steal:
> "In an observational study of Claude.ai data, we found AI can speed up some tasks by 80%. But does this increased productivity come with trade-offs?"

"**A post founded on an Anthropic release has exactly this move available, and it is cheaper and stronger than any framing that starts from the world.**"

**9. The admitted blind spot in our own instrument.** `survey-81k-economics-2026-04`:
> "To date, however, we've lacked information on how these usage patterns map onto people's thoughts and impressions of AI."

"**the only opening in the corpus built on an admitted blind spot in the team's own existing measurement**, and it is the best available model for a post that layers a second instrument onto the Index. The construction is reusable verbatim: *X shows A and B. To date, however, we've lacked information on how A and B map onto C.*" The same move in `productivity-gains-2025-11` uses two bolded nouns: "We've captured the **breadth** of uses … but not their **depth**", then makes the gap concrete twice — once as a definitional failure and once as a worked case (the ten pull requests, nine trivial and one critical). "**name the published instrument, name the distinction it cannot draw, then give one case where the distinction decides the answer.**"

**A tenth, for a review whose finding may be a null.** `worker-retraining-2026-08` opens on what other people believe: "Among experts and the public, worker retraining is the most popular policy for mitigating labor market disruption from AI." "The stake is that a popular policy may not work — which makes the paper's value independent of the sign of its results. **When the motivation is a decision other people are about to make, a null is as publishable as a positive.**" `labor-market-impacts-2026-03` reaches the same place by opening on the failures of the genre it is joining — offshorability, the official forecasts, the robots literature, the China shock — and the file's verdict is: "**Opening on the track record of the measures you are about to add to is the strongest available way to earn a null.**"

### What every opening in the corpus does

- **States the stakes before the first own-number.** First own-number: ~150 words (2025-02 report), ~190 (2025-04), ~230 (2025-03), ~400 (2025-09 report and 2026-01 report), ~480 (2026-01 blog), ~600 (survey-81k-economics). `economic-index-2026-06-report` has no number in its Introduction at all.
- **States the hypotheses and how to tell them apart, where there are two.** `skill-formation-rct-2026-01`: "Does AI provide a shortcut to *both* skill development and increased efficiency? Or do productivity increases from AI assistance undermine skill development?" — followed immediately by the two numbered outcomes in the same order. "**The rival hypotheses are stated as a disjunction and the outcome measures are numbered in the same order in the next sentence, so the reader can see which measurement discriminates which world.**"
- **States the two-sidedness of the answer before any finding, where the answer is two-sided.** "We learned that many people fear job displacement—though they also feel more productive and empowered at work" (`survey-81k-economics-2026-04`) — "**An opening that states the tension cannot be accused of burying it.**"
- **Grades its own evidence in the sentence that states the finding.** "The survey's results provide **initial evidence** that observed exposure … **is correlated with** economic concern" (`survey-81k-economics-2026-04`) — "the grading is not deferred to a limitations section, because there is no limitations section."
- **Concedes the external-validity problem before the findings, where it is large.** `worker-retraining-2026-08` spends its fourth paragraph entirely on the mismatch between its trials and an AI shock, then gives two reasons to proceed: "**The external-validity problem in a post like this is not a limitation, it is the opening**, because a reader who has not been told it will think of it before the first finding."
- **Names the question larger than the design and disqualifies it in the same paragraph.** `claude-code-expertise-2026-06`: two questions, then "While we don't have full answers to these questions yet, we look to Claude Code usage data for early signals." "**Posing a question larger than the design and disqualifying it in the same paragraph is what buys the paper a labour-market framing on product telemetry.**"
- **Claims novelty for the vantage point, not for the finding.** "the superlative never says *the findings are unprecedented*, only that the vantage point is" (`economic-index-2025-02-report`).

### On the summary block

Our template forbids one. The corpus shows the cost four times over.

- `economic-index-2025-04-software-development`: summary bullet 3 says "13%" where the body says "23.8%" — "**a finding written twice at two precisions is a finding written twice, and the two versions have to be reconciled by whoever writes the second one.**"
- `coding-agents-social-sciences-2026-05`: three of five bullets drift from the body, and the "40% more likely" figure exists **only** in the summary. "**A number that exists only in the summary has no section to be checked against.**"
- `claude-code-expertise-2026-06`: the bullets say "about 25% on average" where the body says 27%, and "debugging" where the measure is "fixing something broken" — "A summary that renames the measured category is a summary that cannot be checked against the figure."
- `worker-retraining-2026-08`: the exec summary, the web page and the arXiv abstract publish three different versions of the same five results, one of which silently switches the time horizon and one of which breaks the paper's own denominator rule. "**one entry per number, quoted identically in every place the institution publishes it** — including the page, the abstract and the citation block, which are written last and checked least."

The test to apply instead: "**if the close can stand as the summary, the summary block was never load-bearing**" (`coding-agents-social-sciences-2026-05`, `claude-code-expertise-2026-06`).

---

## Findings and their caveats

### How a finding sentence is built

**The fence goes inside the clause that carries the number, and preferably between the superlative and its subject.**
> "The tasks and occupations with by far the largest adoption of AI **in our dataset** were those in the 'computer and mathematical' category" — `economic-index-2025-02-report`. "the reader cannot take the superlative away without the fence."

**The unit is named in the clause, in the units actually measured.** "37.2% **of queries sent to Claude**, not '37.2% of AI use'" (same file). "**79% of conversations involved some form of automation** — three fences in eleven words. 'of conversations' states the unit …; 'some form of' widens the predicate …; and 'involved' is weaker than 'were'" (`economic-index-2025-04-software-development`).

**The magnitude is characterised before it is quantified.** "a slight lean towards augmentation, with 57% of tasks being augmented" (`economic-index-2025-02-report`) — "so a reader who mistakes 57/43 for a landslide has already been corrected." The same device in the other direction: "Claude Code showed dramatically higher automation rates—79% …" — "the device is only safe because both numbers follow immediately" (`economic-index-2025-04-software-development`).

**Both halves of a partition are given.** "57% of tasks being augmented and 43% of tasks being automated" — "the post states both rather than one plus a complement, so the reader does the subtraction and sees how close to even it is." Where shares do not sum, say what the residual is: `economic-index-2026-01-report` footnote 2 accounts for the 3.0% classified into neither category, repairing a named weakness in the prior wave, whose 77%/12% left 11% unexplained.

**The label is attributed to the classifier, not to the world.** "slightly more conversations being **labeled as** augmentative (57%) than automative (43%) … the paper says these conversations were *labelled* augmentative, not that they *were* augmentative, and that one participial phrase is the difference between a measurement and a claim" (`economic-index-2025-02-paper`). Nine such attributions in five short paragraphs in `economic-index-2026-01-report`; nine fences for seven constructs in `survey-81k-economics-2026-04`, which "never lets a classifier output appear naked."

**A level pair, then the ratio, each labelled.** "starting projects at a pace of around a quarter of a paper more … In percentage terms, coding agent users look around 10% (empirical projects started) to 75% (working papers posted) more productive than others in their discipline and career stage" — "**level, then ratio, each labelled, comparison group inside the sentence, hedge on every number**" (`coding-agents-social-sciences-2026-05`). And the corpus's cleanest three-part form: "increased by 1.3pp, growing from a base of 0.2% to 1.5%—a more than 6-fold increase" (`economic-index-2025-09-report`), "which is how the report stops a 6-fold increase from sounding large and a 1.3pp increase from sounding trivial."

**A headline carries its baseline in the same sentence.** "increased employment by 1.7 percentage points, compared to a baseline employment rate of 63% in the control group" (`worker-retraining-2026-08`) — kept in the *summary*, "which is where it is hardest."

**The denominator caveat is a full sentence, and it says why it matters.** "These figures are per person offered *treatment*, which matters because compliance in these studies is often low." The offer/trainee distinction is then restated at seven separate points of use: "**A construct that a reader will get wrong is restated at every point of use, not defined once**" (`worker-retraining-2026-08`).

**Significance and size are two paragraphs, never one.**
> "If 'work' means to increase employment and earnings on average, and to a statistically significant degree, then job training has worked in the US. … However, the average training program does not make a big difference."

"**Two paragraphs, two questions: is the effect real, and is it big. Never the same paragraph.** This is the single most copyable passage in the file, and it is the correct answer to the fault the corpus keeps finding" (`worker-retraining-2026-08`).

### Where the caveat sits

The corpus converges on a three-layer allocation, stated most explicitly in `economic-index-2025-04-software-development`:

> "**The rule: a caveat that applies to one number goes at that number; a caveat that applies to one finding goes at the head of that finding; only design-level limits go in the list.**"

- **Number-level, in a footnote at the number, with the direction of bias.** "The HTML numbers for Claude.ai are likely inflated slightly because Artifacts leverage HTML" — "Direction of bias ('inflated'), magnitude ('slightly'), mechanism …, and the processing decision with its reason. Four things in two sentences, placed where the number is."
- **Finding-level, as a preamble that ranks the finding against the others.** "Because we don't know the real-world context in which Claude's responses were being used, these analyses rely on uncertain inferences from incomplete data. We therefore treat these findings as more preliminary than the ones described above." — "a **section-level downgrade written as a preamble** … It is better than a bullet in a list because it is unavoidable, and better than a parenthetical because it ranks this finding against the others."
- **Design-level, in the list.**

**Upstream of the exhibit, not downstream.** `coding-agents-social-sciences-2026-05` puts its descriptive-only downgrade before Figure 5: "**here the downgrade is upstream of the exhibit, so a reader who looks at the chart before reading has already been told how to read it.** Copy the ordering." `skill-formation-rct-2026-01` does the opposite and the file marks it: "**A downgrade upstream of the exhibit tells the reader how to read it; a downgrade downstream asks them to reread it.**"

**Inside the definition of the variable, where the awkward fact belongs to the variable.** "For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions" — "**put the awkward fact in the sentence that defines the variable, not in a later list**" (`economic-index-2026-03-appendix`). Likewise "the age of the user's account (days since signup with Anthropic, not with Claude Code specifically)" — "**When a proxy is off-target, say what it is not, inside the definition**" (`claude-code-expertise-2026-06-appendix`).

**Before the interpretation it qualifies, in a sentence-opening subordinate clause.** "Though not adjusted for population, we suspect that these strong adoption figures partly reflect rapid adoption in technology hubs" (`economic-index-2025-09-report`) — "the strongest available position and the opposite of an appended caveat." Same move: "While we can't conclusively identify the jobs of the people making these requests, this could reflect…" (`economic-index-2026-06-report`).

**Two of the corpus's best caveats state an absence, not a doubt.**
> "We do not observe people who signed up a year ago but are no longer using Claude." — `economic-index-2026-03-report`. "**the single best caveat sentence in the corpus**. It states an absence rather than a doubt, it is checkable, and it tells the reader the exact shape of the bias without arguing about its size."

> "Some of these inferences will be wrong." — `survey-81k-economics-2026-04`. "Five words, flat, future tense, no hedge and no quantification … **a caveat that states a fact about the data rather than a doubt about the result.**"

**The construct fenced by two counterexamples rather than by a caveat.** `claude-code-expertise-2026-06` §2.3: "A senior engineer asking their first Rust question is a beginner at Rust. An accountant who has never used Python, but tells Claude exactly which reconciliation rules a Python script must enforce … is an expert at that task." — "**Define a derived construct by the two cases the reader would otherwise get wrong** … it costs forty words."

**Direction of bias, named.** The corpus's signed statements: "the true proportion of augmentative conversations may be even higher" (`economic-index-2025-02-paper`); "we may overestimate usage rates for certain tasks by classifying conversations from novice users" (same); "Claude is probably used far more for creating digital art than for painting or sculpture" (`economic-index-2025-03-report`); "likely undercounted because a significant amount of enterprise usage … occurs within the Claude For Work product" (`economic-index-2025-04-software-development`); "users bring tasks to Claude that they're more confident will work" (`economic-index-2026-01-blog`); "observed success rates will overstate true capability on the full distribution of potential tasks" (`economic-index-2026-01-report`); "this could skew usage patterns towards more experienced or technically adventurous users" (`economic-index-2025-04-software-development`); "This could make them more likely to report productivity benefits than the average user" (`survey-81k-economics-2026-04`); "This should be a lower bound for cognitive offloading since agentic AI coding tools would require even less human participation" (`skill-formation-rct-2026-01`, "**a signed limitation strengthens the finding it limits**").

**Grade two caveats against each other inside one sentence.** "It is possible that this sample is not representative of usage on Claude.ai across longer time windows, and quite likely that our sample differs in important ways from API data or data from other AI model providers…" — "*possible* for the within-platform problem, *quite likely* for the across-platform problem … Grading two limitations against each other inside one sentence tells the reader which one to worry about, and it costs three words. Copy this" (`economic-index-2025-02-paper`).

### How nulls are phrased

**State the direction and then disown it.** "The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero" (`labor-market-impacts-2026-03`). "Not 'we find no effect' — the point estimate's sign is given and then disowned."

**State the failure to exclude in both directions.** "Our results do not conclusively find a speed up or slow down using AI in this task" — "**A null stated as a two-sided failure to exclude is the honest form, and it is one clause longer than the dishonest one**" (`skill-formation-rct-2026-01`).

**Supply the positive alternative so the null does not read as a failure.** "there wasn't evidence in this dataset of jobs being entirely automated: instead, AI was diffused across the many tasks in the economy" (`economic-index-2025-02-report`).

**Give the null two competing explanations, not one.** "This could reflect the timeline of getting a paper to submission … But it could also reflect that coding agents are more useful at getting projects up and running than they are at the last mile" — "**a null with one explanation is an excuse; a null with two competing explanations is a finding about what the design cannot separate**" (`coding-agents-social-sciences-2026-05`).

**Bound the null in the same sentence, where the instrument is a self-report.** "However, these are self-assessments, and skills can erode even as they become more valuable and as someone reports learning more, so the data do not rule out skill erosion." — "**the template for writing a null that a referee cannot mistake for a refutation**" (`economic-index-2026-06-report`).

**Explain the null with a measured mechanism, not a story.** `skill-formation-rct-2026-01` explains its speed null with annotated screen-recording time — "**A null with a measured mechanism behind it is a finding; a null with a story is an excuse.**"

**Report a stable quantity as a finding.** "These gaps are stable: we see no evidence that low-use countries are catching up or that high-use countries are pulling away." — "**A series that reports its stable quantities as findings is a series whose moving quantities can be believed**" (`economic-index-2026-01-report`).

**The MDE: the corpus's largest single gap, and its one model.** No economic-index report states a minimum detectable effect anywhere. The one full treatment is `labor-market-impacts-2026-03`, finding 6, and it is the passage to imitate:

> "What kind of scenarios can this framework identify? Based on the confidence interval of the pooled estimate, differential increases in unemployment on the order of 1 percentage point would be detectable (this will change as new data comes in, so it is merely a ballpark estimate). If all workers within the top 10% of coverage were laid off, it would increase unemployment within the top quartile group from 3% to 43% … Such a doubling in the top quartile of exposure would increase its unemployment rate from 3% to 6%. This should be visible in our analysis as well."

"**An MDE is not a number, it is a scenario a reader can judge** — this is the single most copyable passage in the paper and the thing our nulls have never done." The construction: *state the MDE in the outcome's unit; date it; name a scenario with a historical precedent; do the arithmetic; say whether the design would see it.*

### How magnitudes are compared, and the interpretive furniture

- **Concede the expected part first, so attention goes to the unexpected.** "Unsurprisingly, occupations involving a high degree of physical labor … were least represented" (`economic-index-2025-02-report`); "Intuitively, skills requiring physical interaction … showed the lowest prevalence" (`economic-index-2025-02-paper`); "While computer and mathematical tasks still dominate overall usage at 36%, we are seeing sustained growth in knowledge-intensive fields" (`economic-index-2025-09-report`) — "so the growth story cannot be mistaken for a change in the ranking."
- **Report the component that moves the other way, in its own sentence.** "One change goes ostensibly in the opposite direction: the tasks performed by Claude were judged to be slightly less possible for a human without access to AI" — "**Reporting the primitive that points the other way, in its own sentence, flagged with 'ostensibly', is the finding's own counterweight**" (`economic-index-2026-03-report`). Same discipline: "the confirming example and the disconfirming example are given the same amount of space, the same sentence form, and the same two-number-pair construction" (`economic-index-2026-06-report`, marketing managers versus editors, then pharmacists versus statistical assistants).
- **Report an exception as a count, not a share.** "Across almost all types of outputs (26 of 31 outputs shown)…" — "With 31 categories and a small mean difference, a share would have hidden the five exceptions; the fraction advertises them" (`economic-index-2026-06-report`).
- **State the fork and leave it open.** "Whether the growth in directive usage is attributable to improving model capabilities or learning-by-doing could signal very different labor market implications. If more advanced models simply expand the set of automated tasks, then the risk increases that workers performing such tasks will be displaced. However, if instead the rise in directive use reflects learning-by-doing, then workers most able to adapt … are likely to see greater demand and higher wages." — "The finding is one number; the interpretation is a fork; the fork is left open on the page" (`economic-index-2025-09-report`).
- **The confluence list.** Three to five candidate channels, none tested, none ranked, prefaced by a sentence that says so: "The disparities in Claude usage likely reflect a confluence of factors, some of which are correlated with income" (`economic-index-2025-09-report`). "Naming five and choosing none is a way of writing 'we cannot separate these' that is more useful to a reader than the sentence 'we cannot separate these', because the five are now on the table for someone else to test."
- **Check the conjecture on the spot where the data allow it.** `worker-retraining-2026-08` names three mechanisms for its unemployment-rate correlate and then tests one, reporting the statistic *that failed its own significance rule*: "a 1-point increase in unemployment is associated with 3.4 more points of program participation; the standard error is 2.8, meaning that the finding, while suggestive, does not meet the statistical significance 'survival' criterion applied here." — "**A conjecture that can be checked against the same data is checked in the paragraph that raises it, and the check is reported whichever way it comes out.**"
- **Typography can separate observation from conjecture.** `economic-index-2025-04-software-development` builds each summary bullet as bold claim → roman numbers → *italic inference*: "Roman is what was measured; italic is what it might mean … **a reader can find every conjecture in the summary by looking at the slant of the type.**"
- **Report the robustness check as a finding, with its numbers and its effect quantified.** "This same trend holds—albeit in weaker form—when we adjust for tasks' success rates. Claude successfully completes tasks that require a college degree 66% of the time, compared to 70% … This reduces, but doesn't eliminate, the overall effect" (`economic-index-2026-01-blog`).
- **Report the cost of a robustness check.** "Conditioning on these measures therefore attenuates the relationship … but all three relationships remain positive and statistically significant" (`economic-index-2026-06-report`) — "Attenuation reported rather than robustness declared." And: "the gap persists when we compare conversations served by the same model … Claude Code sessions still show 0.26 points more autonomy" against an unconditional 0.37 — "give both numbers so the reduction is visible."
- **State the falsification condition before the result.** "We would only observe a positive coefficient if, on average, long-tenure users are more successful in these within-task comparisons." — "**A sentence that says what would have to be true for the number to appear is worth more than the number**" (`economic-index-2026-03-report`). The appendix form: "If unemployment risk were increasing for young workers in exposed jobs, we would expect the gap between the two series to shrink and possibly reverse … Instead, the gap has remained roughly constant." — "the falsifying pattern is described in advance and in the units of the picture" (`labor-market-impacts-2026-03-appendix`).
- **State the rival explanation in the reader's voice, then the remedy, with the verb hedged.** "One might worry that expertise isn't the real driver—perhaps experts simply pick different tasks … Throughout this section, we **partially** address this worry by comparing sessions doing the same kind of work, at the same estimated value, in the same month, on the same subject, from people in the same broad occupation group" — "**the corpus's best plain-language statement of an identification strategy**: name the alternative, list what was held fixed, hedge the verb" (`claude-code-expertise-2026-06`).
- **Publish the anti-circularity rule where a classifier could manufacture the finding.** "It is explicitly instructed not to treat the act of coding as evidence of a coding profession … A session in which a lawyer builds a script to automatically flag missing clauses … is mapped into Legal Occupations" — "**Where a classifier could manufacture the finding, the rule that stops it goes in the body, in the reader's language, with an example**" (`claude-code-expertise-2026-06`).
- **Report a heterogeneity result with its cell count in the sentence that states its magnitude.** "the apparently powerful impact of an employer committing to hire graduates—\$8,000–9,000 in year 2 and beyond—owes to three programs" (`worker-retraining-2026-08`), stated three times and every time with the count.
- **Small vivid comparisons.** The sentences that survive summarisation: "for example, debugging code or cutting hair"; "waiters and anesthesiologists (low- and high-wage occupations, respectively)"; "providing instructions for a basic omelette does not indicate culinary expertise" (`economic-index-2025-02-paper`); "shampooers and obstetricians" (`economic-index-2025-02-report`); "debugging software happens far more often than negotiating circus contracts" (`economic-index-2025-09-report`); "13 rounds of back-and-forth, while the median blog-producing Claude Code session contains a single human prompt" (`economic-index-2026-06-report`); "a software engineer and a construction manager anticipate roughly the same increment of progress within their profession" (same, a null rendered as two people); "writing haikus, checking sports scores, and suggesting food for a party" against "AI research, git operations, revising manuscripts, and startup fundraising" (`economic-index-2026-03-report`). Note the rule the January 2026 report adds: "**a worked example is cheapest and most valuable where a definition or a caveat is doing the work, not where a headline is.**"
- **One claim tested at more than one level.** The corpus's own standard, and its models. `economic-index-2025-02-paper` reports the same correlation at three grains and names the grain at which it fails ("strong" 0.95, "reasonable" 0.70, "relatively weak" 0.47) — "**One claim tested at more than one level, with the level at which it fails named.**" `labor-market-impacts-2026-03` tests its exposure measure at five levels — an official forecast, a demographic profile, an unemployment series, a hiring transition rate, and appendix variants — "**one measure, many levels, each answering a different objection to the others.**" `economic-index-2026-03-report` runs its tenure claim four ways (binary split, continuous gradient, cluster ranking, regression ladder): "each answers a different objection to the others." `economic-index-2026-01-report` reports a sign reversal across levels and *reports the disagreement as the result*: "**One claim tested at two levels, with the disagreement between the levels reported as the result rather than resolved in favour of the convenient level, is the house standard.**"
- **A comparison taken inside the unit survives selection into the sample.** "On average, people make about 70% of the planning decisions but only 20% of the execution decisions" — both shares from the same session (`claude-code-expertise-2026-06`); "70% of respondents are more optimistic about paper productivity than about broader field impact" — both items from the same respondent (`coding-agents-social-sciences-2026-05`). "**When a sample is selected on the attitude being measured, the level is not the finding and the within-person contrast is.**"

---

## Comparisons

The comparison is the finding. "Overall, we saw a slight lean towards augmentation, with 57% of tasks being augmented and 43% of tasks being automated." — "**The comparison *is* the finding: neither share means anything alone**" (`economic-index-2025-02-report`).

### Baselines the corpus uses

| Baseline | Example | File |
|---|---|---|
| Workforce share | "the percentage of relevant conversations with Claude is shown in orange compared to the percentage of workers in the U.S. economy with that job type" | `economic-index-2025-02-report` |
| The index's null value | AUI > 1; Zipf's −1; σ = 1; the 45-degree line; β = 0.99 | `-2025-09-report`, `-2026-01-report` |
| The previous wave, named as a document | "our original data sample", "our first report", "our last report" | `-2025-03-report` |
| Calendar dates, replacing wave labels | "in February, down from 24% in November" | `-2026-03-report` |
| A clean out-of-event month | "eight times as common as on the average day in **May**" | `-2026-06-report` |
| Each series' own average | "Normalized hourly share … relative to their overall average", dashed line at 1.0 | `-2026-06-report` |
| Official statistics | Census BTOS with the survey question quoted in full; BLS OEWS with its release named | `-2025-09-report`, `-2026-03-report` |
| The history of technology | electricity 30 years, the PC 20, the internet 5 against AI's 2 | `-2025-09-report` |
| An outside laboratory's threshold | METR's 50%-success horizon, adopted so 3.5 h and 19 h can sit beside 2 h and 5 h | `-2026-01-report` |
| The other platform | Claude.ai against 1P API, compared on five to eight dimensions | `-2025-09-report`, `-2026-01-report` |
| A realised rate in official statistics | 10% stated job-loss risk against the JOLTS annualised separation rate | `-2026-06-report` |
| The paper's own unadjusted estimate | Table A2's unadjusted and adjusted rates in adjacent columns | `claude-code-expertise-2026-06-appendix` |
| The control arms | "the long-term employment rate among controls is 60% compared to 80% for sector programs" | `worker-retraining-2026-08` |

### How differences are worded

- **Both levels, matched rounding, same direction word through a run.** "44% of the API traffic in our sample maps to computer or mathematical tasks, compared to 36% of tasks on Claude.ai … (4% in the API relative to 12% on Claude.ai), and arts and entertainment (5% relative to 8%)" — "matched rounding on both sides of every pair, and the direction word … is the same each time, which is what lets three comparisons run in two sentences without a table" (`economic-index-2025-09-blog`).
- **The comparator in a parenthesis, so each sentence carries its own comparison.** "32.9% of Claude Code conversations (nearly 20% higher than their Claude.ai usage)" — and the file flags the half of this that fails: "the sentence does not say whether the 20% is percentage points or a relative increase … **a difference is reported in its units, and both levels are given**" (`economic-index-2025-04-software-development`).
- **Wage comparisons: two named occupations, both wages in parentheses, the wage ratio in words, then the outcome ratio in words.** "marketing managers earn roughly twice as much as editors (\$80 vs. \$37 per hour) and conversations mapping to their tasks consume approximately 2.5 times as many tokens" (`economic-index-2026-06-report`).
- **Geographic comparisons: the local rate, the baseline named in the same clause, the multiple to one significant figure.** "they use Claude for translation and language-learning about six times more than the global average"; "people in Hawaii request Claude's assistance for tourism-related tasks at twice the rate of the rest of America" — "the subject is 'Claude users in Brazil', not 'Brazilians' — the sample is in the noun phrase, which is the cheapest possible place to put it" (`economic-index-2025-09-blog`). The regional form: "X% and Y% respectively versus Z% globally" (`survey-81k-interviews-2026-03`).
- **A multiple *and* both arms.** "more than triple the rate of institutional employees (47% vs 14%)" — "the only fully checkable one on the page … **a multiple is memorable, both arms make it auditable, and giving both costs four characters**" (`survey-81k-interviews-2026-03`).
- **Slope and fit reported separately, and allowed to point opposite ways.** "use rises more quickly within income here than across countries: a 1% higher per capita GDP inside the US is associated with a 1.8% higher population-adjusted use of Claude. That said, income actually has *less* explanatory power within the US" — "two regressions become one claim" (`economic-index-2025-09-blog`, `-2025-09-report`).
- **Give the value that would be unremarkable before the estimate.** β = 0.99 is interpreted as a 17-year half-life before any β̂ is quoted (`economic-index-2026-01-report`); Zipf's −1 is stated in the caption of the exhibit whose fitted slopes it interprets (`-2025-09-report`); "In this sample, 51% of overall usage is Opus" is the base rate an over/under-representation chart needs (`-2026-03-report`).
- **Re-cut your data to the other study's threshold and put both thresholds in the sentence.** "Eloundou et al. (2023) predicted that 80% of U.S. workers could have at least 10% of their work tasks affected …; by contrast, our empirical data shows current adoption at ∼ 57% of occupations using AI for at least 10% of their tasks" — "the ∼57% at 10% of tasks is a number that appears *nowhere else in the paper* — it is generated specifically to make the comparison commensurable" (`economic-index-2025-02-paper`).
- **Report overlap with prior work as a count of shared units.** "Thirty-seven of the 56 studies are in Smedslund et al. (2006), zero are in Haelermans and Borghans (2012), 2 are in Card, Kluve, and Weber (2018), and 26 are in Peck et al. (2021)." — "**Overlap with prior work is reported as a count of shared units, not as a characterisation**" (`worker-retraining-2026-08`). This is the "states plainly what it adds and where it overlaps" criterion done with arithmetic.
- **Name how your new measure differs from the one Anthropic already published, before using it.** "These measures complement the autonomy measures in our prior report … Those measures tracked how long the agent runs and how often people approve its actions automatically. Our decision attribution measure, by contrast, captures who makes the substantive decisions in a session as a whole" (`claude-code-expertise-2026-06`).
- **Corroboration is agreement in direction, never confirmation.** "is consistent with", "align with", "converge with", "echoes", "also favored", "mirrors a finding from our 3rd Economic Index report". "It echoes a previous Economic Index finding that also favored higher-paid workers: in tasks requiring greater levels of education, Claude tended to reduce the time taken to complete a task (relative to doing it without AI) by a higher percentage" — the earlier finding restated in its own units with its own counterfactual, "so the reader can see that the two results are about different things" (`survey-81k-economics-2026-04`).
- **State the confound as a property of the data before any number.** "Claude.ai transcripts can include multi-turn conversations, while the API data we analyze is limited to single input-output pairs. This is because API requests arrive independently, with no metadata linking them to prior exchanges." — "A comparison between two samples that differ structurally needs exactly this paragraph, once, early" (`economic-index-2026-01-report`).
- **Publish the control-side levels next to the effects.** "For experiments incorporating training, the long-term employment rate among controls is 60% compared to 80% for sector programs … **Sector programs draw from populations that are higher paid even without training.**" — "**the selection story is told with the untreated arms, which is the only place it can be seen**" (`worker-retraining-2026-08`).
- **Argue against a confound by stating what the data would look like if it were true.** "If interview structure were driving the co-occurrence, you'd expect it to be roughly uniform across all five tensions and all groups. Instead the co-occurrence ranges from 1.6 to 3.0 times…" — "**how to argue against a confound in prose for a reader who will not read a robustness table**" (`survey-81k-interviews-2026-03`).
- **Name each column of a controls table by the alternative it kills.** "Each column in the table below adds a control, testing a different hypothesis. First, that expert-rated users pick different kinds of work (column 2), work in different months (3), work on different subjects (4), hold different occupations (5), or run longer sessions on stronger models (6)." — "**A cumulative-controls table written this way *is* an argument**, and a reader who never looks at the numbers still knows what has been ruled out" (`claude-code-expertise-2026-06-appendix`).
- **Two measurements of one quantity are the strongest available check.** "the 1998 treatment-control difference is much larger going by self-report than by Social Security data, at \$972 versus \$218 … the contrast between the two is extraordinary: –\$4 versus –\$4,209." And then the move worth stealing: the report codes "outcome data from official records" as a study trait and uses it as a regressor — "**a data-quality concern that can be coded becomes a covariate, not a caveat**" (`worker-retraining-2026-08`).

### Revising a published claim

Four forms, all attested, and the corpus insists the grammar differ by form (`economic-index-2026-01-report`).

**Revised — separate the trend from the level.**
> "Nevertheless, the automation share was still elevated as compared to nearly one year ago … suggesting that the underlying trend is still toward greater automation even as the August spike overstated how quickly it was materializing."

"Nothing is retracted and nothing is defended … 'overstated' is applied to the *pace* rather than to the direction. **When a later result cuts against an earlier one, name the earlier claim, distinguish what survives (direction) from what does not (rate), and say which of the two the earlier claim over-read.**"

**Retracted — name it as a hypothesis and supply the replacement in the same sentence.**
> "This pushes back against a hypothesis we made last year that automated use may be more typical of more experienced, sophisticated users; instead, we find that the most advanced users are more likely to iterate with Claude."

"the retraction is stated as a conflict with a *hypothesis* rather than with a finding; the verb is 'pushes back against', not 'refutes'; and the replacement claim is given in the same sentence" (`economic-index-2026-03-report`).

**Superseded — the old measure is incomplete, and in what respect.** "Our earlier work found that 36% of jobs had AI usage for at least a quarter of their tasks … This measure was based only on the appearance of a task in our data, however." (`economic-index-2026-01-report`).

**Re-estimated under a critique — reproduce first, then let the critique move the number.** "we replicate our previous finding that current-generation AI models and current usage patterns imply a productivity effect of 1.8 percentage points per year" and only then "A salient critique of this analysis is that it fails to account for model reliability… implied productivity growth falls from 1.8 to 1.2 percentage points" (`economic-index-2026-01-report`). "Each critique is introduced in the voice of the critic … and then *answered with a number that is worse for the report*."

**A published extrapolation revised in the open.** "When we update our estimates from the previous report, we find that at this rate states would arrive at roughly equal usage per capita in 5-9 years, rather than 2-5." — "**The construction is exactly reusable: 'we find that at this rate X would happen in [new], rather than [old].'**" What the file marks as missing: the diagnosis of *why* it moved (`economic-index-2026-03-report`).

**Reconcile two of your own numbers, unprompted.** "Note that this is a different measure of adoption than in the introduction to this report. Reported adoption by consumers and employees of AI reached 40% in 2024 whereas when measured at the firm-level, nine out of ten businesses in the US report not using AI." — "**the single most credibility-earning move in the document, and it costs two sentences**" (`economic-index-2025-09-report`).

**Name the tension with an earlier finding, locate it in the design, refuse to close it.** The four-move paragraph in `skill-formation-rct-2026-01`, which the file says our posts "will need constantly" and should copy "nearly verbatim in shape": "a result that may seem in tension with the findings presented here. But the two studies ask different questions and use different methods: our earlier observational work measured productivity on tasks where participants already had the relevant skills, while this study examines what happens when people are learning something new. It is possible that AI both accelerates productivity on well-developed skills and hinders the acquisition of new ones, though more research is needed to understand this relationship."

---

## Captions and figures

### The emphasised-sentence convention

Per `room/director-2026-09-16-alt-text-ruling.md` and its amendment (`room/director-2026-09-16-caption-amendment.md`): **the caption is the emphasised sentence or sentences directly under the image, whether bold or italic.** Numbers found only in image alt text are marked `(alt text)` and never quoted as prose or caption; numbers read off a chart image are not recorded at all.

The corpus uses three emphasis conventions and one colour convention: bold (`economic-index-2025-02-report`, the PDF reports), italic (`-2025-04-software-development`, `-2025-09-blog`), bold title inside an italic run (`coding-agents-social-sciences-2026-05`), and **black title with grey gloss at the same size, with no bold anywhere in the document** (`labor-market-impacts-2026-03`). Terminal punctuation on a caption title is inconsistent across the corpus and between the two published versions of the same piece: treat the period as optional and **the bold declarative title plus roman gloss as the invariant** (`economic-index-2026-06-report`).

### The caption template

Distilled from `economic-index-2025-09-report` and extended by every later file.

1. **Label and title.** Numbered in PDFs, unnumbered on the web. Sentence case. **Declarative where there is a finding to state, descriptive where there is not.**
2. **If the finding is noisy or conditional, the hedge goes in the bold title, not the gloss.** "As we move from lower to higher adoption countries, Claude usage appears to shift away from programming-dominant tasks to a more diverse mix of tasks, **though the overall pattern is noisy**" — "an exhibit lifted into a slide deck carries its own noise warning in the headline" (`economic-index-2025-09-report`, Figure 2.7).
3. **Gloss, one sentence per job, in this order where applicable:**
   - what is plotted, in what unit;
   - **the unit of analysis, named explicitly** — "Each point is an occupation" (`economic-index-2026-06-report`, Figure 3.3, "the single most valuable clause in this report's captions"); "Each point is an occupation (x-axis) and its Opus share (y-axis)" (`-2026-03-report`); "by artifact" (`-2026-06-appendix`);
   - how any index, share or predicted variable was constructed, **restated in full rather than cross-referenced**;
   - the sample, the coverage boundary, and any inclusion floor **with the reason for the floor** — "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample" (`economic-index-2025-09-report`, repeated verbatim in four captions);
   - panel logic, with position cues;
   - what colour, size and marker encode;
   - the weighting scheme **and its purpose** — "We weight observations by number of records to construct a representative sample" (`-2026-01-report`, Figure 1.4);
   - imputation and censoring rules — "When for privacy-preserving reasons we do not observe usage shares for a particular collaboration mode we give that category a value of 0% in this figure" (`-2025-09-report`, Figure 3.5);
   - the residual or "All Other" category;
   - the full control set, enumerated, for any conditional estimate — nine controls named individually in `-2026-01-report` Figure 3.5; five in `claude-code-expertise-2026-06` Figure 5; "Full controls **adds** model, use case, and country fixed effects" in `-2026-03-report` Figure 2.4;
   - what any line is — fit, null or threshold — and the estimator behind a fitted line — "The dashed lines show the fit from a linear regression" (`-2026-01-report`); "The dashed line shows a simple linear regression fit, weighted by current employment levels" (`labor-market-impacts-2026-03`, Figure 4, "the best caption in the paper and the standard for the corpus");
   - **every graphical element that is not a data point** — "Black line illustrates the median, box represents p25 and p75, whiskers represent p10 and p90" (`-2026-06-report`, Figure 2.3); "The shaded band marks the maximum permitted stay in supported work… The dotted vertical line marks each group's average actual stay" (`worker-retraining-2026-08`, Figure 2);
   - the uncertainty, **its coverage and its clustering unit** — "Whiskers show 95% confidence intervals" (`-2026-06-report`, Figure 3.8); "clustered by user" (`claude-code-expertise-2026-06-appendix`, Table A1); "95% confidence intervals calculated using the robust standard errors scaled by the outcome mean" (`coding-agents-social-sciences-2026-05`, Figure 5);
   - the null or benchmark value the reader should compare against, with the familiar number attached — "An elasticity of σ =1 reproduces our unadjusted baseline result of 1.8 percentage point increase" (`-2026-01-report`, Figure 4.6); "In this sample, 51% of overall usage is Opus, and 55% of Computer and Mathematical usage (+4.4pp) is Opus" (`-2026-03-report`, Figure 2.1);
   - the coefficient's meaning in plain words, with "associated with" — "The elasticity of 0.38 implies that each 1% increase in the input token index is associated with a 0.38% increase in the output token index" (`-2025-09-report`, Figure 3.7);
   - **the exclusion**, repeated verbatim in every caption it governs — "Excludes sessions with no clear goal" (`claude-code-expertise-2026-06-appendix`, Tables A1 and A2);
   - where the full version lives, if the exhibit is an excerpt — "See online appendix at … for full prompt texts" (`-2026-01-report`, Table 2.1).
4. **Definitions in the caption where the figure carries a taxonomy.** The five collaboration subtypes in `economic-index-2025-02-report` Exhibit 5; the five modes in `-2025-03-report` Exhibit 5; the 1–5 autonomy scale with both poles in `-2026-06-report` Figure 2.5. "The definitions are given in the caption rather than the body so that the figure is self-contained if lifted — which is exactly what happens to this chart."
5. **The coding rule of a classifier-derived outcome, in the respondent's terms, with the model in a closing parenthesis.** "A respondent was coded as indicating job threat if they said their role was already being replaced or substantially reduced, or that such changes were likely in the near term (coded using Claude)." — "**A caption that carries its own coding rule can be lifted; this one can**" (`survey-81k-economics-2026-04`, Figure 1).
6. **Fence the grouping variable, not only the outcome.** "**Both fields** are inferred from free-form responses using Claude-powered classifiers" — "the only caption in the corpus that does" (same file, Figure 2).
7. **The conditional base first, as a subordinate clause.** "Among respondents who named a beneficiary of their AI productivity gains, the share identifying each destination." — "the best statement of a conditional base anywhere in [the corpus] … A reader cannot take the shares away from their denominator because the denominator is the sentence's opening" (same file, Figure 4).
8. **Quote the instrument in the caption where the instrument is the measurement.** Both prompt variants in `productivity-gains-2025-11` Figure 2; the survey item and its slider labels in `coding-agents-social-sciences-2026-05` Figure 6; the interview question verbatim in three `survey-81k-interviews-2026-03` captions ("**Putting the prompt verbatim in the caption is the best thing on this page.** A share of an open-ended answer is meaningless without its question"); the Census BTOS question in full in `-2025-09-report` Figure 3.1; the prompt Claude was given in `-2025-09-report` Table 3.1, with "Claude was prompted to identify tasks at the 10th, 50th, and 90th percentile … with the minimal guidance" and then "Claude associated output length with task complexity" — "When a model has generated part of an exhibit, this caption is the standard: say what it was asked, quote the ask, and attribute the conclusion to it."
9. **Read one cell aloud where the exhibit's grammar is unusual.** "this figure shows that 44% of API traffic in our sample was matched to a task characteristic of a Computer and Mathematical occupation" (`-2025-09-report`, Figure 3.3); "the top 20 percent of US states accounted for 40 percent of population-adjusted usage in the US" (`-2026-01-report`, Figure 1.6); "E.g. the first row shows that a typical conversation mapped to a top-tercile occupation consumes 2.07 times as many tokens as…" (`-2026-06-report`, Table 2.4). "One number in a caption, chosen to demonstrate the grammar of the exhibit rather than to make a point."
10. **Disclose what the exhibit is *not*, where its form invites a wrong inference.** "This analysis is not based on the words used in the underlying transcripts but rather groupings constructed using privacy-preserving methods." — "A word cloud on a page about private conversations invites exactly one wrong inference, and the caption forecloses it in its final sentence" (`-2026-01-report`, Figure 1.5).
11. **Disclose what was not adjusted for.** "Token counts are not adjusted for which model served the conversation." — "**a caption that names the adjustment it did not make tells a referee where to look and costs nine words**" (`-2026-06-report`, Figure 2.3).
12. **Say whether a multi-label classifier lets a respondent appear twice.** "Respondents can indicate multiple categories (the question is limited to research use cases)" (`coding-agents-social-sciences-2026-05`, Figure 4); "we used a multi-label classifier (response can map to multiple concerns)" (`survey-81k-interviews-2026-03`); "Working papers posted, journal submissions and journal resubmissions are mutually exclusive categories" (`coding-agents-social-sciences-2026-05`, Figure 5); "11 queries have multiple (two) labels" (`skill-formation-rct-2026-01`, Table 3). "**Where counts can double-count or a statistic is not a mean, the caption says so.**"
13. **Repeat verbatim rather than paraphrase.** The 200-observation floor appears four times word for word in the September 2025 report and five times in the January 2026 one; the coverage boundary "The underlying data includes Claude.ai Free, Pro and Max usage" five times — "the diff between 'Free and Pro' and 'Free, Pro and Max' is the only notice the reader gets that the sample changed. **That is exactly why the formula is repeated verbatim rather than paraphrased — the diff is legible.**"
14. **Sibling exhibits take one caption template.** The country/state pair in `-2026-01-report` Figures 3.3 and 3.4 is "identical word for word except for the four things that differ: the level …, the code standard …, the floor … and the noun". `labor-market-impacts-2026-03` Figures 6 and 7: "**when two exhibits do the same thing to two outcomes, give them the same caption sentence structure.**"
15. **Say Claude.** "'Claude' appears in every single caption; 'AI' appears only in the topic phrase of the first" (`economic-index-2025-02-report`). The only justified exception is an exhibit plotting someone else's data (`-2025-09-report` Figure 3.1, Census) or a measure whose *name* says AI and whose gloss says Claude (`-2026-01-report` Figure 4.4).

### Provenance verbs

`worker-retraining-2026-08` runs four consistently, and the corpus has nothing better: **"Copied from"** (the image is theirs), **"Based on"** (the data are theirs, the drawing is the paper's), **"Reproduced from"** (an excerpt), **"Adapted from"** (redrawn with changes). "**A one-word provenance verb in the caption tells the reader how much of the exhibit is the author's.** This is cheap, and our evidence drawers should adopt it." The same file adds: "**where a borrowed figure's conventions differ from the paper's, the caption says so**" — Figure 8's notes state the currency year and that the intervals are 90%, not the paper's 95%.

For borrowed figures with our own number added: "Figure reproduced from Filippucci, Gal, and Schief, 2024. The dotted line is 1.8%, derived from Claude's estimates." — "**When a figure is borrowed, the caption must say what was added to it**" (`productivity-gains-2025-11`, Figure 10). And the provenance of each component, itemised to the table and page: "Source: employment rates from MDRC (1980), Tables 4-1, 5-1, 6-1, and 7-1; maximum stay from p. 35; average length of participation from Table 2-7" (`worker-retraining-2026-08`, Figure 2).

### What a caption never claims

- **A relationship the prose has not already stated with its number.** "Per capita income predicts how Claude is used across countries" sits over the one finding the body declined to quantify — "In our own posts, a caption never states a relationship the prose has not already stated with its number" (`economic-index-2026-01-blog`, Exhibit 3).
- **A universal.** "AI sentiment is majority-positive everywhere (no country dips below 60%)" — a universal in a parenthesis, unsupported by the page's own published data without an unstated display rule. "**A caption never states a relationship the prose has not already stated with its number, and never states a universal at all**" (`survey-81k-interviews-2026-03`).
- **An unmodelled statistical claim.** "Concern about jobs and the economy was the strongest predictor of AI sentiment overall" — "the caption opens with the page's most load-bearing statistical sentence, for which no model is shown anywhere" (same file).
- **A significance family in one clause.** "All differences in adoption between groups are statistically significant with p < 0.05" — "A universal claim over an unspecified number of group contrasts, with no correction and no n per cell … the caption states a result it cannot show" (`coding-agents-social-sciences-2026-05`, Figure 3).
- **A vaguer version of what the exhibit shows.** "the caption says the right-hand panels show 'various definitions of success' and 'various definitions of failure' without enumerating either, while the legend inside the image names all six exactly … **a caption that says 'various definitions' where the exhibit lists them by name has thrown away information the author already had**" (`claude-code-expertise-2026-06`, Figure 5).
- **A mark the legend calls something else.** "the caption says 'White dots are geometric means', while the legend inside the image labels that mark simply 'Mean' … **Where a caption defines a mark, the legend has to use the caption's words for it**" (same, Figure 3).

### The corpus's own caption faults, to check a draft against

- **Three of five captions in `economic-index-2025-04-software-development` never say what is plotted.** "Captions on this page are an overflow channel for method, not a description of the exhibit … **The definitions are the optional part of a caption; the unit, the sample and the series are not.**"
- **A caption that states a conclusion without stating what was divided by what** — "The balance of augmentation and automation has stayed relatively constant…" — "a caption built this way cannot be lifted, because a reader who sees only the image and this sentence does not know what is being divided by what" (`-2025-03-report`, Exhibit 3).
- **No figure in `coding-agents-social-sciences-2026-05`, `claude-code-expertise-2026-06`, `survey-81k-economics-2026-04`, `labor-market-impacts-2026-03` or `worker-retraining-2026-08` states its n.** Five pieces, five files, the same verdict.
- **Load-bearing quantities left inside the image.** `economic-index-2026-03-report` lists seven sentences that depend on numbers visible only in pictures — the Gini values, the composition rule, the weighting, the currency base, the slopes, the US wage reference. "**a caption must contain the sample, the unit, the construct, the null and, where there is one, the coefficient — and no sentence in the post may depend on a number that appears only inside an image.**"
- **A caption whose base contradicts the body's.** Figure 5's "Share of respondents" against the body's "48% of users who explicitly mentioned productivity effects" — "**The caption's base and the body's base must be the same words**" (`survey-81k-economics-2026-04`).
- **Two titles on one exhibit.** The in-image chart title and the caption title differ on four of six figures in `claude-code-expertise-2026-06` and on Figure 1 of `worker-retraining-2026-08`: "**Two titles on one exhibit is one too many**; ours put the unit line in the caption." Where an exhibit will be lifted, the in-image title is the copy that travels, so it is the copy that must be reviewed — and in `claude-code-expertise-2026-06` it is the unreviewed one, restating the paper's slogan in different words and swapping "the agent" for "Claude".
- **Alt text is absent throughout.** Eight of the corpus's pieces carry empty alt attributes on every exhibit; `survey-81k-interviews-2026-03` has no `<img>` element at all. "a piece whose whole argument is that people should be heard is unreadable at the level of every one of its eight exhibits by anyone using a screen reader." Our pages carry the finding in the caption and the table in the drawer for exactly this reason.

### Tables

- **Two-level row grouping, a Difference column carrying direction by glyph as well as sign, percentage points for shares and percent for numeric facets, and units in the row label where the unit is not obvious** — "AI autonomy (1-5)", "Human education (yr)" (`economic-index-2026-03-report`, Table 2.1).
- **The significance of every row in one sentence, with the exception named by row.** "All differences are statistically significant with p<0.001, except Human-only time with p<0.05" — "**the cheapest possible way to make a table of small differences readable**" (same, Table 1.1). The file notes that the report's other table, whose differences are larger, carries no uncertainty at all: "If two tables in one document report differences, they should report them to the same standard."
- **Repeat the group definition in the caption rather than cross-referencing three lines up.** "We define high-tenure users as those who signed up for Claude at least six months **before our data pull**" — "the threshold is relative to the sample window, not to a calendar date, which is the correct and less obvious way to state it" (same, Table 2.1).
- **Publish a derived measure three ways at once.** `claude-code-expertise-2026-06` Tables 1 and 2: the rubric in the author's words, the formal expression the script implements (`outcome = success AND success signal = {4,5}`), and one real labelled case per measure. "**A derived measure is published three ways at once — in prose, as an expression, and as a case a reader can judge for themselves** — and that is a far stronger defence of a classifier than an accuracy statistic, because it lets a sceptic disagree with the labelling rather than with the label. Take this into the evidence drawers." The same table reproduces users' typographical errors intact, "which is what makes them read as evidence rather than as illustrations".
- **Explain an absence in the table.** "Novice is the reference category, so its coefficient is not defined" (`claude-code-expertise-2026-06-appendix`, Table A2).
- **Explain what the parentheses hold when they hold two different things.** "The numbers in parentheses are standard deviations of control-group values and standard errors of impact estimates" (`worker-retraining-2026-08`, Table 2). And pre-empt the attentive reader's objection in the caption: Table 3's notes explain why two columns with identical N give different results — "**A caption that anticipates the objection an attentive reader will raise is doing the work of a paragraph.**"
- **Label every exhibit, including the table.** `productivity-gains-2025-11` leaves its one table unnumbered, and the body then refers to it as "the below plots", which it is not: "**Label every exhibit, including the table; a caption that cannot be cited cannot be checked.**"

---

## Limitations

### Where the section sits

**The corpus has no settled answer, and the two ends of the range are both criticised in their own files.**

- **An H3 inside Results, after the findings and before the conclusion.** `economic-index-2025-02-report`: "the reader meets the caveats while the numbers are still on the screen, and the conclusion is read *through* them." Criticised for pooling six caveats and ranking none, and for putting the challenge to the 57/43 split 400 words from the number.
- **Its own top-level section, between the last finding and the close.** `economic-index-2025-04-software-development`: "**Limitations is promoted** out of the results and given its own section … so the close is read through it — same effect as February's placement, achieved with a heading of equal rank rather than a sub-heading." **This is the practice our template keeps.**
- **No section at all, dispersed.** Every report from September 2025 onward, every team paper, every appendix. `economic-index-2025-09-report`'s verdict on itself: "the report's caveats are individually excellent and collectively invisible: a reader cannot answer 'what are the limitations of this report?' without reading all 28 footnotes." And the summary judgment, repeated in four files: "**A caveat a skimmer cannot find is a caveat addressed to referees only.**"
- **Before the evidence, as instructions for reading it.** `worker-retraining-2026-08` §3 "Critical themes", five subsections placed ahead of sixty pages of studies and invoked by number at each use: "A limitations section at the end tells a reader how much to discount a conclusion they have already formed; §3 tells them how to read the 60 pages that follow." Its cost is the same one: "a reader who skims the table of contents sees 'Critical themes' and cannot tell that it is the limitations."

**The form our posts use takes the best of each:** the specificity of the dispersed footnotes, in a section a referee can find, with the finding-level and number-level caveats still adjacent to their findings. `economic-index-2025-09-report` states it: "The form our posts should use takes the best of each — the specificity of these footnotes, in a section a referee can find." And `economic-index-2026-01-blog`: "The right lesson is to do both — adjacent caveats *and* a gathered section — not to choose."

### The framing sentence

**Shortest honest version wins.**
- "These findings are preliminary." (`claude-code-expertise-2026-06`) — three words.
- "There are some caveats worth naming." (`survey-81k-interviews-2026-03`) — "No 'as with all studies', no apology, no hedge on the hedge. Four words of subject and verb. Copy it."
- "There are several caveats to the findings in this report." (`coding-agents-social-sciences-2026-05`) — "**The shortest honest framing sentence is the best one; the concession itself should be the second sentence.**"
- "There are key caveats to our analysis, **owing to the nature of the data**." (`survey-81k-economics-2026-04`) — attributes the caveats to the data rather than to the analysis.
- **Derive the limitation from the design's virtue, which replaces the ritual sentence entirely.** "Our analysis is grounded in real-world AI use—how developers are actually using Claude in their workflows. Although this approach gives our findings practical relevance, it also brings inherent limitations." — "observational data on real use buys relevance and costs control, and every bullet that follows is a cost of that same choice. **This is the stronger form of the ritual sentence and should replace it**" (`economic-index-2025-04-software-development`).

Never: "as with all studies it has important limitations" (`economic-index-2025-02-report`, whose own file calls this "the ritual part, and it is the only ritual part"). Never: "Some of these include" or "These include:" — "concedes the list is not exhaustive, which is honest and also unfalsifiable; a referee would ask which ones were left out."

### Ordering

**Outward from the data to the world, strongest last.** `economic-index-2025-04-software-development`: "Coverage of the sample (1) → validity of the central construct (2) → reliability of the secondary classifier (3) → who is in the sample (4) → when the sample is from (5) → what the sample represents (6) → what was not measured at all (7). Roughly outward from the data to the world, ending on the widest. The strongest bullet is last, as in February." `economic-index-2025-02-paper`: five bold run-ins "each naming a *source* of error rather than the error itself: the sample, the classifier, the queries, the taxonomy, the workflow … ordered roughly from the data inward to the interpretation."

**Name each limitation by a two-word dimension label, then the concession, then the study that would fix it.** `skill-formation-rct-2026-01` §7.1 does this six times — *Task Selection*, *Task Length*, *Participant Realism*, *Prompting Skills*, *Evaluation Design*, *Human Assistance* — "so the list is scannable as a research agenda … **Copy the shape: the dimension as a two-word label, the concession, then the study.**"

**Rank by severity, or the referee will.** Two files complain of unranked lists: "the list is not ordered by severity, which a referee would raise" (`economic-index-2025-02-report`); "the bullets are not ranked by severity, so the construct-validity problem in bullet 2 — which threatens the headline directly — sits level with the retention window" (`economic-index-2025-04-software-development`).

### Direction-of-bias statements

**Every limitation should be asked which way it pushes the estimate** (`skill-formation-rct-2026-01`). Three forms:

- **Signed in one direction.** "we may overestimate usage rates for certain tasks by classifying conversations from novice users" (`economic-index-2025-02-paper`).
- **Both directions, mechanised, with the modality grading them.** "this could either understate the productivity gains – since it takes additional resources we're not accounting for to hire an employee and communicate context, and possibly overstate it, if the quality of the AI's work is worse than a human's." — "Neither direction is asserted, both are mechanised, and the asymmetry in modality ('could either' / 'possibly') grades them" (`productivity-gains-2025-11`).
- **Numbered, signed, with one favourable to the paper.** `worker-retraining-2026-08` Appendix G: persistence (benefit overstated if absent), non-wage benefits ("would increase the benefits side of the ledger", so conservative), general equilibrium ("the benefits we measure are inflated"). "**A limitations list where every item cuts the same way is an apology; a list with directions is an error budget.**"

**A one-sided list is advocacy.** "Only the upside omissions are listed ('could push the number much higher'); no downside is named on this page … A sentence that lists the reasons an estimate could be too low must list the reasons it could be too high, or it is advocacy" (`economic-index-2026-01-blog`).

### The limitation that withdraws a claim

The corpus is unanimous that this is where a limitation earns its keep.

> "we don't argue that the uses in our dataset are a representative sample of AI use in general" — `economic-index-2025-02-report`. "A limitation that changes what the post is willing to assert is worth more than three that only describe noise. Copy this construction."

> "We only studied what developers delegate to AI—not how they ultimately use AI outputs in their codebase, the quality of the resulting code, or whether these interactions effectively improved productivity or code quality." — `economic-index-2025-04-software-development`. "**a limitation is worth most when it names the sentence the post is not entitled to write.**"

> "Finally, we only look here at the number of projects researchers report, and report nothing about their quality." — `coding-agents-social-sciences-2026-05`.

> "it remains out of reach to make definitive judgments as to how much Claude's outputs are actually incorporated by users in their tasks" — `economic-index-2025-02-paper`.

> "we generally use these task value estimates ordinally rather than using them to get aggregate task values." — `claude-code-expertise-2026-06-appendix`. "**the only sentence in the corpus that converts a measurement limitation into an operating rule for the paper that follows.** It is the best limitation sentence in the corpus for that reason."

And the strongest of all, which names the threshold at which the conclusion flips:

> "**Without that persistence, they would have a benefit-cost ratio under 1.**" — `worker-retraining-2026-08`. "**A limitation is worth most when it tells the reader what number would have to be different, and by how much, for the finding to reverse.** Our template's limitations section should be written to this standard; nothing else in the corpus reaches it."

### Where a threat is answered, report the cost

- "we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (**though to a lower absolute level of 45% automation versus 49% with Sonnet 4**)" — "Reporting the 4-point level difference rather than only the qualitative agreement is what makes the footnote trustworthy" (`economic-index-2025-09-report`).
- "The 2SLS estimates imply modestly slower convergence: β̂ ≈ 0.89 unweighted and β̂ ≈ 0.86 … **However, these estimates are less precise, and only the former is statistically distinguishable from 1 at the 10% level.**" — "the correction moves the answer away from the headline, the loss of precision [is] disclosed, and the specification that fails the significance test identified" (`economic-index-2026-01-report`).
- "conditioning on these measures therefore attenuates the relationship … but all three relationships remain positive and statistically significant" (`economic-index-2026-06-report`).
- The two-arm, two-model 2×2 grid in `claude-code-expertise-2026-06-appendix`, including the losing configuration with the size of its failure: "With a uniformly weighted draw, the pricer anchors to the small-job range and compresses everything above it: on the validation holdout it under-priced \$5,000+ jobs by roughly 12x (median prediction \$800)." — "**Publishing the losing configuration, with the mechanism named and the damage quantified, is what turns a design choice into evidence.**"

**Where a threat is not answered, say so in the same breath.** "considerable uncertainty remains"; "the message is unclear"; "we don't know if income or education are truly driving adoption"; "there's no guarantee that more performant models would show improvement in this plot" (`economic-index-2026-01-report`); "We can't rule this out entirely, but…" (`economic-index-2026-06-report`, "the phrase to use when a confound is addressed and not eliminated"); "the key gradients **that we can measure** are similar" (`coding-agents-social-sciences-2026-05-appendix`, a fence inside the sentence being defended); "(which we did not extensively verify here)" (`claude-code-expertise-2026-06-appendix`, "six words that hand a referee the exact hole and decline to fill it").

**The formula to avoid: "we ran robustness checks and believe that this activity is not driving the results"** (`economic-index-2025-09-report`, on Utah). Belief rather than demonstration. The series itself drops it: by January 2026 the contaminated geographies are excluded outright and the exclusion is stated — "**Excluding the contaminated geography and saying so beats keeping it and asserting robustness, and the series has moved from the second to the first.**"

**The robustness claim with no alternative and no number is an assertion.** "These results are similar however we define high tenure." (`economic-index-2026-03-report`); "A Poisson model specification gives similar results." (`coding-agents-social-sciences-2026-05-appendix`); "The exact cutoff has little impact on the job rankings." (`labor-market-impacts-2026-03-appendix`, in a document whose last three pages tabulate variants by rank correlation — "the machinery to support it was already built").

### The referee-first list

Every corpus file ends its Limitations section with "what a referee would raise first", in order. Written across twenty-three files, the recurring items are:

1. **No MDE beside a null.** Named in nineteen files. "a reader cannot tell whether 'not statistically significant' at the state level means 'no relationship' or '50 states'" (`economic-index-2026-01-report`).
2. **No n below the headline.** "not per expertise level, not per occupation group, not per panel, not per cell — while three captions assert intervals and significance" (`claude-code-expertise-2026-06`).
3. **No uncertainty of any kind.** "not one interval, standard error or minimum detectable effect in 38 pages, for percentages computed on samples of 500K–1M conversations" (`economic-index-2025-02-paper`).
4. **No classifier validation, or validation delegated.** "every primitive is Claude's estimate, validated only for direction, on a small non-representative set, with no reported accuracy … a single unquantified instrument carries three of the four headline results" (`economic-index-2026-01-report`).
5. **An instrument change between waves, asserted rather than re-run.** "September re-ran its comparison on the old classifier and reported the 4pp discrepancy; this report does not. **This is the passage to point at when explaining why an instrument change between waves must be re-run, not asserted**" (`economic-index-2026-01-report`); the O\*NET vintage change in `-2026-03-report`, "disclosed in eleven words and never assessed".
6. **A control group that is a measurement artefact, shown to be unbalanced and never addressed.** `labor-market-impacts-2026-03`: the zero-exposure 30% are workers whose tasks "appeared too infrequently in our data", Figure 5 shows they differ on sex, race, education and pay before ChatGPT existed, and Figure 6 shows the two groups diverging under the last aggregate shock. "The null and the MDE are both conditional on a comparison the document itself has undermined, and nothing joins the two facts."
7. **Selection that the design cannot separate.** Survivorship and cohort effects (`economic-index-2026-03-report`); recruitment for an experiment about the technology being measured (`coding-agents-social-sciences-2026-05-appendix`); a survey advertised with free Claude Max accounts.
8. **Shared-source dependence.** "The expertise rating and the outcome judgment are read from the same transcript by the same family of classifiers … The matching set addresses task selection, not this" (`claude-code-expertise-2026-06`); the 0.93 correlation between two education measures read from the same transcript by the same classifier (`economic-index-2026-01-report`).
9. **Multiple denominators, stated once each.** "Each finding conditions on a different classifiable subset, the four coverage figures are stated once each in four different places, and no finding is reported both ways" (`survey-81k-economics-2026-04`).
10. **A threshold chosen because it reproduces a prior result.** "We choose a threshold of 0.02% because it replicates our previous results" — "a threshold selected to reproduce a prior result is not an independent replication of it" (`economic-index-2026-01-report`).

---

## Closes

**Corpus-wide invariant: there are no numbers in the close.** Confirmed in `economic-index-2025-02-report`, `-2025-02-paper`'s launch-post comparison, `-2025-03-report`, `-2025-04-software-development`, `-2025-09-report` ("Not one figure in the Concluding remarks"), `-2025-09-blog` ("Not one, across five paragraphs. … **Anthropic's economics closes contain no quantities**"), `-2026-01-blog`, `-2026-01-report`, `labor-market-impacts-2026-03` ("The only digits in the close are an age range and a year"), `coding-agents-social-sciences-2026-05`, `claude-code-expertise-2026-06` ("one ratio and no percentages"), `survey-81k-economics-2026-04` ("Not one digit in 350 words"), `worker-retraining-2026-08`.

Two exceptions and both are named as faults: `economic-index-2026-03-report` opens its Discussion with "33% of traffic, up from 28%", neither of which appears in prose anywhere else; `economic-index-2026-06-report` carries one number, "over 35% predicted that AI would be able to do *most* of their work", chosen because it is the report's most consequential survey result. The rule to draw: **the close carries no number the body has not already carried** (`labor-market-impacts-2026-03`).

### Types of close

**1. The baseline / horizon close.** Findings are treated as a baseline to be monitored, not as conclusions. `economic-index-2025-02-report`: "Not one of the four findings is repeated with its number in the close; the 57/43 split and the 36%/4% pair appear only as *things that can now be monitored*." Its why-it-matters is a conditional extrapolation with two hedges and a stated antecedent:
> "If it remains the case that AI is used only for certain tasks, and only a few jobs use AI for the vast majority of their tasks, the future might be one where most current jobs evolve rather than disappear."

"**This is how to write why-it-matters without overclaiming: state the inference, state what it depends on, keep the modal verb.**"

**2. The summary close with hedge-matching.** `economic-index-2025-03-report`: "relatively modest increases", "no change in the balance", "used with the highest frequency" — each adjective matched to the body's. "**That is the test to apply to any summarising close — read the close's adjectives against the body's and check that none has been upgraded.**"

**3. The conditional-stakes close.** `economic-index-2025-09-report`:
> "These patterns risk creating divergence. **If** AI's productivity gains concentrate in already-prosperous regions and automation-ready sectors, existing inequalities could widen rather than narrow. **If** AI automation improves the productivity of workers with tacit organizational knowledge—**as some of our evidence suggests**—then more experienced workers could see rising demand and higher wages even as entry-level workers face worse labor market prospects."

"The second conditional has an interpolated evidence claim … which marks precisely how much of that antecedent the report can support and how much it cannot. … the corpus's best example of a why-it-matters that is genuinely conditional without being evasive: the reader is told what would follow, what it depends on, and how much of the dependency is evidenced."

**4. The questions-handed-on close.** `economic-index-2025-04-software-development`: "Our findings raise many questions", then three, none answered, each naming something the series could measure. "a wave report promises the next wave; a special report hands the questions on." The file's caution: "**the honest version of this close is questions *plus* the one thing the post commits to.**"

**5. The indeterminacy close.** `economic-index-2025-09-blog`: "The nature of people's use of Claude is evidently still being defined: we're still collectively deciding how much confidence we have in AI tools, and how much responsibility we should give them." Ends on an italicised word that undermines its own extrapolation: "to see where—or, indeed, *if*—users' choices settle as AI models improve." "**A close that italicises the word that admits the trend may not continue is doing the corpus's characteristic thing.**"

**6. The instrument close.** `economic-index-2026-01-blog`, `labor-market-impacts-2026-03`. The latter: "We hope that the analytical steps taken in this report, especially around coverage and counterfactuals, will be easy to update as new data on employment and AI usage emerge. **An established approach may help future observers separate signal from noise.**" The file's ruling, which matters to us: "**a close that ends on the instrument is right when the instrument is the contribution, and wrong the rest of the time** — and most of our posts will be the rest of the time."

**7. The tension close.** `economic-index-2026-03-report`: "These early-adopting users may simultaneously be the most exposed to AI-driven disruption and most aided by AI in these initial, augmentative waves of adoption." — "**A why-it-matters that ends on a tension rather than a direction is harder to write and much harder to misquote.**" `survey-81k-economics-2026-04` does the same inside a paragraph: the empowerment paragraph's last sentence is the finding that cuts against it.

**8. The two-sided thesis with one paragraph per side.** `claude-code-expertise-2026-06`: "how agentic coding amplifies some forms of knowledge and skills, while substituting for others", then one paragraph discharging each half. "**A two-sided thesis sentence followed by one paragraph per side is the cleanest close structure in the corpus.**"

**9. The decision close.** `worker-retraining-2026-08`, for a post that opened on a decision: not whether the programmes work but whether they would be enough — "the impacts are small enough that they would not leave a dent in a persistently high unemployment rate." And the move the file calls "the rarest and most useful thing in this file":
> "Some of these investigations are evergreen: yielding helpful evidence regardless of AI's impact on unemployment. Whether or not AI disrupts the labor market, we will not regret having learned how to best help workers adapt."

"**When the motivating uncertainty cannot be resolved, the close recommends what is worth doing under either resolution.**"

**10. The close that re-asks the question.** `productivity-gains-2025-11`: "Claude handles tasks of widely varying complexity … **But what is the aggregate effect of this work?**" — "**A close that re-asks the paper's question before answering it cannot read as a summary block**, and that is the device to take, since our template forbids one."

### What every good close in the corpus does

- **Every paragraph opens on the world, not on the report.** `economic-index-2025-09-report`: "Only two of nine paragraphs open with 'this report' or 'we', and both are about the data release." The counter-example: "Paragraphs open on the report more often than on the world — four of six begin with 'This fourth…', 'Our findings…', 'Equally important to the patterns documented here…', 'Building on prior releases…'" (`-2026-01-report`).
- **Argue against your own extrapolation.** "History shows that the patterns of technological adoption aren't fixed … The patterns of highly concentrated use that we observe today may yet evolve towards a broader distribution" — "A close that undermines the extrapolation its own findings invite is the opposite of a summary" (`economic-index-2025-09-report`). Twice in the last paragraph of `-2026-06-report`, including "Ultimately, Claude's impact on the economy will be visible in economic aggregates like employment and productivity as much as its usage logs" — "Claim, concession, reason the work still matters, in three sentences. **This is the house form for a why-it-matters that has to survive a reader who thinks usage logs are the wrong measure.**"
- **Restate the limitation of your own central measure.** `economic-index-2026-01-report`: "these measures are directionally accurate and, taken together, provide important signals even if individual classifications are imperfect." — "**A close that repeats the limitation of its own central measure, in its opening paragraph, is doing something almost no paper does and is the single most copyable move in this section.**"
- **Claim the contribution for scope, method or transparency, never for results.** "The most important contribution of this paper … is its new methodology" (`-2025-02-report`); "marks a significant expansion in both scope and transparency" (`-2025-09-report`); "this report has given us a new baseline" (`-2026-01-blog`); "analyzed model selection and success for the first time" (`-2026-03-report`).
- **Invert, if the inversion is honest.** "These productivity gains come from making existing tasks faster to complete. Historically, though, transformative productivity improvements—from electrification, computing, or the internet—came not from speeding up old tasks, but from fundamentally reorganizing production." — "A note that spent twenty pages measuring speed-ups ends by saying speed-ups are not where transformation comes from … **If the close can be inverted honestly, invert it; the sentence that concedes what your instrument cannot see is the one a reader remembers**" (`productivity-gains-2025-11`). The 2025-02 paper does the same: "A paper that has spent 38 pages insisting on measurement ends by saying measurement is not the point."
- **Compress several findings by holding the subject fixed and varying the predicate.** "People in higher-income countries are more likely to use Claude, more likely to seek collaboration rather than automation, and more likely to pursue a breadth of uses beyond coding." — "**Three findings compressed into one sentence by holding the subject fixed and varying only the predicate.** That construction is the most efficient thing on the page and it is exactly the right tool when the close must carry several results and no figures" (`economic-index-2025-09-blog`).
- **Drop the weakest result rather than repeat its hedge.** `coding-agents-social-sciences-2026-05`'s close omits conference submissions, the one outcome the body hedged with "possibly": "A close that drops its weakest result rather than repeating the hedge is making the right trade."
- **Check that every fence survives.** Two recorded failures: "Overall, early adoption of coding agents has tilted toward early career researchers, **men**, and those at higher status universities" where every measured sentence said "typically male names" — "**the close is where fences get dropped, so the close is where they have to be checked**" (`coding-agents-social-sciences-2026-05`); and three sentences in `claude-code-expertise-2026-06`'s close that turn a session-level rating into a person-level trait. "Our rule that every quantitative sentence maps to an entry in `results.json` has to cover the *unit* as well as the number: a session-level result closes as a session-level sentence." Also: "a doubling of the recent rate" in `productivity-gains-2025-11`'s close, where p. 15 says "nearly double" — "**The close is where hedges get lost; check every restated number against its first statement, word by word.**"

### What comes next

- **Committal about method, silent about the direction of the result.** "the *method* is promised, the *result* is not" (`economic-index-2025-02-report`, `-2025-02-paper`).
- **Two named falsifiable predictions with their interpretations attached** — the best in the corpus: "if the returns to expertise begin to decrease over time, that would suggest that models are starting to supply the essential judgment that users currently bring … If the share of coding sessions completed successfully by users outside software occupations continues to grow, it could indicate that software production is becoming a part of ordinary work in every field." — "**not a promise to publish more, but a statement of which number would have to move, in which direction, for the conclusion to change.** … Copy it exactly" (`claude-code-expertise-2026-06`).
- **Name the observable that would move and what it would be evidence of.** "We also expect that tasks might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it'll give us another possible indication of coming economic impacts, given the importance of business adoption for AI's effect on productivity." — "*expectation → what it would look like in the data → why anyone should care*, with the causal premise named at the end rather than assumed" (`economic-index-2026-01-blog`).
- **Name a population, a variable and a reason.** "a key next step might be to look at how recent graduates with educational credentials in exposed areas are navigating the labor market" — "**A 'what comes next' that names a population, a variable and a reason is a commitment; 'more research is needed' is not**" (`labor-market-impacts-2026-03`).
- **The next question is the one whose answer decides how to read this one.** "The answer will determine when AI makes the jump from providing significant but bounded productivity boosts, to representing the kind of structural transformation that has historically defined technological revolutions." — "the strongest available form of 'what comes next'" (`productivity-gains-2025-11`).
- **Commit rather than delegate.** "A close that delegates its follow-ups is honest; a close that commits to them is checkable. Ours should commit" (`skill-formation-rct-2026-01`).

### Recommendations

The corpus runs from explicit refusal to a scoped, traceable recommendation, and the refusals outnumber the recommendations.

- **Refusal, with the reasoning given and the recommendation displaced onto the reader.** "Our research gives data on how AI is being used, but it doesn't provide policy prescriptions. Answers … can't come directly from research in isolation; instead, they'll come from a combination of evidence, values, and experience from broad perspectives." (`economic-index-2025-02-report`).
- **None at all, and no refusal either.** `-2025-03-report`, `-2025-04-software-development`, `-2026-03-report`, `-2026-06-report`, `coding-agents-social-sciences-2026-05`, `claude-code-expertise-2026-06`. Four of those six files name the absence as a narrowing: "a report that identifies a mechanism for widening inequality and addresses no audience has left the last step to the reader."
- **Three, hedged, each with a named audience, all using *can* rather than *should*.** `-2025-09-report`: policymakers "need to pay attention to local concentration of AI use and adoption, and address the risk of deepening digital divides"; businesses "may need to restructure how they organize and maintain the information that frontier systems rely on" — "the one recommendation in the report traceable to a specific coefficient"; researchers get four named questions and an open dataset. "No tax, subsidy, programme or regulation is named anywhere in 47 pages."
- **One, scoped, negatively framed, traceable to one coefficient.** "For AI to benefit users globally, expanding access alone will not suffice—developing the human capital that enables effective use, particularly in lower-income economies, is essential." — "**A single recommendation that follows from a single coefficient beats a list**, and this one is scoped … and negatively framed … so that it corrects a specific prior rather than proposing a programme" (`-2026-01-report`).
- **Addressed to three actors, one of them the product team.** `skill-formation-rct-2026-01`'s page: managers ("should think intentionally about how to deploy AI tools at scale, and consider systems or intentional design choices that ensure engineers continue to learn as they work"); individuals; and designers — "AI assistance should enable humans to work more efficiently *and* develop new skills at the same time." — "**That last clause is the model for our template's 'recommendations to Anthropic': it states what the product should achieve, in the study's own terms, in one sentence, without naming a feature.**"
- **Named actor, action, object, instrument, and the circumstance in which it would not work.** `worker-retraining-2026-08` §8.3–8.4: "the TAA's trigger-based approach only works for people who can make the case that they lost their jobs to a disruptive force such as AI. When the labor market transforms not through firings, but by firms not hiring new people in certain roles… trigger-based aid will not fire." — "**A recommendation states who acts, what they do, and the circumstance in which it would not work.** This is the model for our posts' recommendations section." And its §8.2 recommends *against* the paper's own subject: "**A recommendation section that only recommends the thing the paper studied is a sales document**; this one names the population its evidence cannot help, which is what makes the other three credible."

**Never offer an Anthropic programme as the response to your own finding.** "the Rwandan partnership … a product programme presented as a response to the finding. It is the clearest thing in the corpus to avoid — a recommendation to ourselves, stated as already implemented, in the middle of the findings" (`economic-index-2026-01-blog`). Three paragraphs of the same in `survey-81k-interviews-2026-03`: "recommendations are *to* Anthropic, are named as recommendations, and nothing of ours is offered as the response."

### Title against ending

The house test, stated in `economic-index-2025-09-report`: "**if the ending does not contain the title's key word doing work, one of the two is wrong.**"

Passes: "Uneven geographic and enterprise AI adoption" against "And yet early AI adoption is strikingly uneven" — "the title's adjective is the close's predicate, and the title's two nouns are the close's two paragraphs." "Coding agents in the social sciences" against "coding agents are diffusing into the social sciences" — "The close takes the title's noun phrase and supplies its missing verb … **Three points — title, opening question, last two sentences — written to the same words.**" "Labor market impacts of AI: A new measure and early evidence" — "paragraph 1 delivers the measure and the evidence in that order". "What 81,000 people told us about the economics of AI" — the title's phrase returns verbatim in the penultimate sentence and its verb in the close's second sentence.

Fails, and the files name each failure:
- **Title names an instrument, close names a policy conclusion.** "Economic Primitives" against "developing the human capital that enables effective use … is essential." — "**the corpus's clearest example of a title–ending mismatch, and it is the specific failure our rule 'the title matches the ending' exists to prevent**" (`economic-index-2026-01-report`).
- **Misses by a synonym.** "Learning curves" appears three times before the Discussion and not once inside it, which says "learning-by-doing" instead — "this close passes on substance and misses by a synonym. One sentence using the title's own phrase would have closed the loop" (`-2026-03-report`).
- **The title carries a word the findings do not test.** "Agentic coding **and persistent returns to expertise**" — "persistence is a claim about time, the paper's only time-varying result is the occupation-gap null … **A title may not carry a word the findings do not test.**" (`claude-code-expertise-2026-06`).
- **The title under-describes the piece.** "Cadences" names one of three chapters (`-2026-06-report`).
- **Neither ending conjugates its title.** `skill-formation-rct-2026-01`, whose answer — "AI use impairs conceptual understanding, code reading, and debugging abilities, without delivering significant efficiency gains on average" — exists only in an abstract the general reader will not open. "**A title that names the question needs a close that answers it in the same words.**"

Two corollaries the corpus states: "**a tracking title licenses a tracking close; a finding title does not**" (`-2025-09-blog`), and the inverse, repeated in six files: **if the title names a finding, the close must end on that finding's consequence.**

---

## Appendices and methods

### How method detail is presented

**Define at point of use; document in footnote; print the instrument in the appendix.** The footnote carries the sample window, the privacy thresholds, the geolocation method, the exclusions and the unit of observation with its consequence:

> "Data in this section covers 1 million Claude.ai Free and Pro conversations from August 4 to 11, 2025, randomly sampled from all conversations in that period that were not flagged as potential trust and safety violations. **The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included**, though our past work suggests that sampling conversations at random versus stratified by user does not yield substantively different results. … We exclude conversations originating from VPN, anycast, or hosting services, as determined by our IP geolocation provider." — `economic-index-2025-09-report`, footnote 2.

"Sample windows are given to the day. The API sample's coverage is quantified ('roughly half of our 1P API usage') rather than described. The unit of observation is named and its consequence stated … There is not one sentence of the form 'as with all studies, there are limitations.'"

### Introducing a constructed measure

The four-move introduction (`economic-index-2026-01-blog`): **name it as coined** ("what we've called"); **gloss it by count and purpose**; **enumerate the members in one flat list**; **state the derivation in one sentence**. The derivation sentence is the one that matters: "We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample" — "so the reader knows immediately that these are model-generated estimates, not instrumented measurements."

And in the report's own version, with the provenance inside the defining clause: "These 'primitives'—simple, foundational measures of how Claude is used, **which we generate by asking Claude specific questions about anonymized Claude.ai and first-party (1P) API transcripts**—cover five dimensions…" — "The single most important thing about these measures — that Claude generates them — is not deferred to the methods chapter. It is in the defining sentence, unhedged, before any number. **That is the model for introducing a constructed measure**" (`-2026-01-report`).

Each primitive is then defined in three parts, always in the same order: **what the dimension is about · why an economist should care · how it is operationalised**. Two of the five carry a worked example instead of the middle clause, and both examples show what the *old* measure gets wrong: "'Translate this paragraph into French' is high automation (directive, minimal back-and-forth) but low AI autonomy". "**Defining a new measure by naming the case the old measure gets wrong is the strongest available form.**"

**Bound the measure in a named sub-section, promised in the introduction.**
> "While we are very confident in the directional accuracy of the new measures (e.g., tasks with higher average years of education needed to understand the human prompt are likely more complex), none of the measures should be taken as exact or definitive (e.g., Claude.ai may somewhat underestimate the human education years needed for many tasks)."

"Confidence and its limit, each with an example. **That construction — *confident in X, not in Y, here is an instance of each* — is the single most transferable sentence pattern in this file.**" The claim is then argued at three escalating levels — internal coherence, external correlation, predictive validity — with the strongest named and explicitly deferred: "**Naming the validation you have not done, and calling it the strongest one, is how to introduce a measure without overclaiming it**" (`-2026-01-report`).

**Where a measure is built rather than taken, show it working on one case where the naive alternative fails.** "Legal Secretaries is a 12-year education occupation, but the task 'Review legal publications and perform database searches…' is predicted to require 17.7 years because it resembles tasks typically performed by lawyers and paralegals" (`-2026-01-report`).

**Where a measure is a distance between two existing quantities, define it that way.** "Our new measure, *Observed Exposure*, is meant to quantify: of those tasks that LLMs could theoretically speed up, which are actually seeing automated usage in professional settings?" — "**A construct defined as the distance between two existing quantities is easier to explain and harder to over-claim than one defined by a formula**" (`labor-market-impacts-2026-03`).

**Name the construct after its proxy.** "typically male name" / "typically female name" rather than male and female — "**when a proxy is unavoidable, put the proxy into the name of the variable**" (`coding-agents-social-sciences-2026-05-appendix`). And "**expertise exhibited in a session**" rather than the user's expertise; "**apparent** expertise **at the task**" (`claude-code-expertise-2026-06`, `-appendix`).

**Grade the verb to the evidence.** "categorizes" for a partition, "measures" for a scale, "judges" for an outcome, and "**guesses** the user's likely occupation" for the weakest construct in the paper — "**grade the verb to the evidence, and let the reader meet the weakness before the instrument**" (`claude-code-expertise-2026-06-appendix`).

**State the units of an index by giving the two extreme readings of a difference.** "This measure can be loosely interpreted as the share of a job being performed or accelerated by an LLM, though the automation weighting means it is not a pure percentage of task coverage. Comparing two jobs that differ by 0.10 on the measure, the higher-coverage job could have a 10 percentage point higher share of their day covered by AI, or a 20 percentage point higher automation share in our data." — "**the model sentence pair in the document, and the one to copy whenever a post builds an index** … A reader now knows the index's units are an interval, not a point" (`labor-market-impacts-2026-03-appendix`).

**Justify a threshold by converting it into the units of the phenomenon.** Usage of 100 is 0.0025% of traffic, compared against "the median share of time spent on a particular O\*NET task … 0.0014%" — "**a cut-off is justified by showing what it equals in the thing being measured**, not by asserting that it is conventional" (same file).

**Identification arguments in prose, without notation.** "Because API customers are priced on the margin for both input tokens and output tokens, they have an incentive to optimize model prompting to minimize both … Stated differently, API customers are incentivized to only provide Claude with just enough context to accomplish their objective and no more." — "Four steps, each a clause, with 'Stated differently' restating the whole chain in one sentence for a reader who lost it. **Any post of ours that leans on a behavioural assumption should be written this way**" (`economic-index-2025-09-report`).

**Write your own hidden assumptions out.** "a modeling choice that **implicitly assumes** that capital investment will increase…"; "This approach **implicitly assumes** the time estimates that Claude produces represent reliable averages across all instances of each task, and that Claude or similar AI systems will be adopted across the entire US economy." — "**Writing your own hidden assumptions out in a sentence beginning 'this approach implicitly assumes' is the single most transferable sentence pattern in this document**, and it is what the assumptions sweep in our standards is for" (`productivity-gains-2025-11`).

**Label the conservative choice as you make it, and name the deviation from a source.** "conservatively assign tasks not observed in our sample a null improvement"; "Acemoglu 2024 calculates the labor share in AI-exposed industries as 0.57; we use the economy-wide share of 0.6 for simplicity given how close it is." — "**That is what a deviation log looks like in published prose**" (same file).

**Sweep an unidentified structural parameter and identify the value that reproduces the baseline.** σ = 0.5, 1, 1.5, with "An elasticity of σ =1 reproduces our unadjusted baseline result" and results on both sides. "The report does not pick a σ. It reports the sensitivity and leaves the choice with the reader" (`economic-index-2026-01-report`).

**Publish the specification that would have tripled your own headline.** "If we do not impose a restriction on our 1M sample … the implied aggregate labor productivity growth over the next decade would be roughly 5% percentage points per year—a mechanical increase" (same file, footnote 6) — "the most credibility-earning paragraph in the report".

**Report the pilot, the discount, the registered assumption and the realised effect, in that order.** `skill-formation-rct-2026-01`: a pilot found both effects; the power analysis halved the pilot's effect size, with the reason in the same sentence ("to account for the potential effect size inflation typical in pilot studies"); the main study came in below the halved assumption. "**Our pre-registration section should read like this paragraph:** the assumed effect, where it came from, why it was discounted, and what was actually observed."

**Publish the design failures with their rates.** Four pilots, two platforms, and the control arm's non-compliance quantified at 25–35%: "**A design decision justified by a published failure rate is unanswerable; the same decision asserted ('we used screen recording to ensure compliance') is not.**" And the file's warning: "**Publishing a failure rate creates an expectation that the same rate will be published for the study that matters**" — the main study's compliance rate is never given (`skill-formation-rct-2026-01`).

**Choose between two estimands on the grounds of the question, and publish the conversion factor.** "We default to the ITT in what follows since it's easier to define and seems just as likely to fit the future labor markets we imagine … But we also report the average increase in participation … so that interested readers can estimate the benefits in a world of fuller compliance." — "**A defensible estimand choice names the alternative, says why the alternative might be right, states the choice, and publishes the conversion factor.** Our pre-registrations should read like this paragraph" (`worker-retraining-2026-08`).

**Write the assumptions sweep as questions in the researchers' own voice.** "There are judgment calls involved at every step. Should the Eloundou et al. (2023) measure enter as {0, 0.5, 1} or something else? What determines 'significant' use? How do we handle tasks which seem very similar to those with high usage, but are too rare to have been picked up specifically in the sampling…? How much more should automation workflows count compared to augmentation?" — "**Writing the assumptions sweep as four questions in the researchers' own voice is more honest and more readable than a paragraph of prose**, and it is the form to copy in our pre-registrations" (`labor-market-impacts-2026-03`, footnote 6).

### Disclosing that Claude did part of the work

The corpus's best assistance disclosure is not boilerplate; it is a paragraph naming the risk, the controls and the human checks.

> "The humble warning in Card, Kluve, and Weber (2010)—'There are likely to be measurement errors and errors of interpretation in the extraction of information from the studies.'—applies as well to this AI-accelerated effort. The collection and collation of studies involves many judgment calls—some here made by humans and some by AI. Does an intervention involve training enough that it belongs in the sample? … To improve the extraction, we instruct Claude to: a) produce a 'reasoning table' documenting sources and logic for extracted values and b) perform an adversarial review of all extractions, by reading the reasoning table and returning to sources. As in analyses done without the aid of AI, as we learn our way around the data and analyze it, we spot-check and revise the extraction."

"**An automated extraction step is described by what it was asked to produce and what was done to catch it being wrong.** This is the paragraph our own posts should imitate whenever Claude touches the data, and it is more useful than any assistance-disclosure boilerplate" (`worker-retraining-2026-08`). Note the two further moves: the borrowed warning ("it says the new risk is the old risk") and the three judgment calls written as questions a sceptic would ask.

Where an instrument's own uncertainty is a category rather than a silence: "'None' is a catch-all for the conversations that didn't yield a prominent concrete output. This may include brief or abandoned exchanges, cases resulting in an error or cases where Claude asked a clarifying question and the user didn't continue." (`economic-index-2026-06-report`, footnote 2).

### The methodology appendix

Five in the corpus, and their shared grammar:

- **Opens on the fact that bounds the evidence, in one sentence, with no stakes.** "Our results are based on privacy-preserving analysis." (`economic-index-2026-03-appendix`); "The survey was fielded from February 20 to March 24, 2026." (`coding-agents-social-sciences-2026-05-appendix`); "We begin at the task level." (`labor-market-impacts-2026-03-appendix`); "Our sample covers interactive Claude Code sessions between October 2025 and April 2026 (inclusive)." (`claude-code-expertise-2026-06-appendix`); "With this release, we made several changes to how we sample and classify Claude traffic." (`economic-index-2026-06-appendix`).
- **The instrument is shown, not described, and every cut is marked.** Braces for variable content (`{up to 300 candidate Task texts, shuffled, one "- ..." line each}`), square brackets for editorial elision (`[Standard API-data disclaimer]`), an ellipsis line for a truncated enumeration, the output contract printed in full, and the model's own unrendered Markdown left in. "**in an appendix, show the instrument as the instrument was, and mark every cut**" (`economic-index-2026-06-appendix`). `claude-code-expertise-2026-06-appendix` prints the 23-item SOC list twice because the two runs differ in two entries: "**print the instrument twice if the two runs differ; never compress a taxonomy the reader is expected to check.**"
- **The response space is inside the prompt.** "Every non-open row ends with 'Choose from these options:' and then *both* options written out as full sentences, or with the range stated as a constraint on the answer … Nothing is left to a codebook. Note that the two-point scales spell out the negative option at the same length as the positive one, so neither is the default" (`economic-index-2026-03-appendix`).
- **Assumptions itemised into the instruction, not the surrounding text.** The counterfactual worker's endowment ("The necessary domain knowledge and skills … No access to AI tools to assist with the work") is written *into* the time-estimate prompt: "**The counterfactual that makes the measure meaningful is written into the instruction**, not into the surrounding text. A reader disputing the construct disputes a bullet, which is the point" (same file).
- **Coding rules a human coder would otherwise invent.** Forced choice stated as a prohibition ("There is NO 'Unclear' option — pick the BEST fit from the nine, even when evidence is thin"); boundaries as ordered pairs ("X vs Y" lines and a "NOT this:" clause); **named anti-signals** ("Generic asks ('please double-check', 'are you sure?') are EPISTEMIC HUMILITY, not expertise — a careful novice does this"); and traps with their resolutions ("a single intermediate tool error that the agent recovers from is at most a 1 — the FINAL state is what counts"). "**The confound is disclosed in the instrument rather than in the limitations**" (`claude-code-expertise-2026-06-appendix`).
- **The failure is shown, diagnosed and given its better answer.** "In Example 7, the question, 'Which Rust library is best for Natural Language Processing (NLP)?' is mapped to a sales occupation although the question is substantively about computer programming. The classifier focuses on what the Assistant is asked to do—'Recommend products'—and not on the topic of the request. This question might have been better assigned to a task like 'Consult with customers or other departments on project status, proposals, or technical issues…'" — "Naming the correct label, verbatim and with its occupation, converts a confession into a reproducible test that someone else could run" (`economic-index-2026-06-appendix`).
- **Deflate your own validation statistic.** "Note that the overall 0.38 largely reflects cross-tier ordering—because the holdout weights all four tiers equally, the pricer earns credit for placing \$50 jobs below \$8,000 jobs even where it cannot rank jobs within a tier. Within-tier discrimination is concentrated at the low end and is essentially zero above \$5,000." Then the bias in both directions ("Small jobs are over-priced about 2.4x, the largest under-priced about 7x") and the operating rule. "**A caveat that ends in a rule about what the number may be used for is worth ten that end in 'should be interpreted with caution'**" (`claude-code-expertise-2026-06-appendix`).
- **Report agreement as a range across classifiers, under both the lenient and the strict rule, each named.** "78-98% … on the categorical classifiers … 78-99% counting adjacent scale points as agreement, and 53-68% counting only exact matches" — "so the worst instrument is visible in every sentence … A reader can therefore take the number they think is right instead of the number the authors preferred" (same file).
- **Test the claim at a second level, against an outcome the classifier cannot see.** "We ran the same classifier prompts on internal Anthropic Claude Code sessions, where session IDs can be joined to observable engineering outcomes (whether the session's commits landed on the main branch). The expertise–success gradient replicates on this sample, including within-engineer…" — "**One claim tested at two levels, with an outcome the classifier cannot see, is worth more than six claims at one level** — this is the paragraph our own posts should be measured against" (same file).
- **Announce a departure from the house norm before the results it produces.** The paragraph arguing that human labels cannot serve as ground truth on hours-long agentic sessions: "the difficulty, with its cause stated concretely; the standing norm, credited and located ('pursued in previous reports'); why the norm does not transfer here; and the claim that follows, hedged in the only way that claim can honestly be hedged. **A method that breaks with the house norm earns a paragraph of its own, ahead of the results it produces**" (same file).
- **Write variants as one edit from a named baseline.** "Baseline, except tasks are aggregated to the DWA level…"; "Same task-level values as Baseline, but aggregated … using O\*NET coreweight instead of time fractions" — "a reader can see that exactly one thing changed and what it was … this is a list of edits, not a glossary" (`labor-market-impacts-2026-03-appendix`). And judge a variant by *which of the other measures it moves toward*: "the imputed measure looks very similar to β" — "more informative than 'results are robust', because it tells the reader what the variant has become."
- **Introduce a variant by the bias it repairs, with the direction named.** "This was to address the potential issue that some tasks may be implemented on our platforms but do not appear often enough in our sample to meet the privacy threshold for inclusion in the data, **which would underestimate the coverage of low-employment occupations**" (same file).
- **Frame a selection check as a question and answer it in two clauses.** `coding-agents-social-sciences-2026-05-appendix`: "How much is selection into the survey biasing results?"; the unhedged concession ("The main sample we use here **suffers from** its function as recruitment for an experiment on Claude Code access"); the pilot's identifying property ("we did not advertise the subsequent experiment in recruitment for it"); four imperfections listed before the result, the fifth set apart ("**Crucially**, it is missing our detailed coding agent question"); and the verdict in two clauses — "the full sample is composed of more pro-AI respondents, but the key gradients that we can measure are similar." "**levels differ, orderings do not** … A selection check that cannot show *no* bias can still show that the bias does not run along the dimension the finding uses."
- **The equation is introduced by the exhibit it produced, and its variables are words.** "The adjusted output comparisons in Figure 5b use OLS regressions of the form:" then `Output_i = β × CodingAgentUser_i + γ × X_i + ε_i`, with every control enumerated with its cardinality and the transformation from coefficient to reported quantity spelled out ("then divide by the control group's mean of each outcome to back out percent differences"). "**Every equation in our own posts should be introduced by the exhibit it explains, not by its own name**" (same file). And the appendix convention: colon, equation, then a sentence beginning with the symbol it defines — "Notation is never left to a glossary and never introduced twice" (`labor-market-impacts-2026-03-appendix`).
- **An appendix ends without a close.** Three of five end on a piece of exhibit furniture: a footnote withdrawing comparability, a table's *Notes* line, an exclusion rule. "**An appendix stops when it has handed over the last object it was holding.** Nothing is concluded because nothing was argued." All five files add the same warning: **a post may not end this way.**
- **The genre's closing move belongs where the problem arose.** "We are actively developing methods of validation that take seriously that human labels may no longer be the gold standard … We encourage others in the research community to take up this methodological challenge alongside us." — placed three pages before the end, attached to the section that departed from house method. "**A methodological open question is closed where it is opened, not in a concluding paragraph**" (`claude-code-expertise-2026-06-appendix`).

**Reproduction on the cover.** `worker-retraining-2026-08` puts the repository and the interactive results interface on the cover, above the abstract-equivalent: "**Reproduction is on the cover, above the abstract-equivalent, not in a back-matter note.**"

---

## Divergences and version handling

`room/director-2026-09-16-pdf-web-ruling.md`: **where a report exists as PDF and web page, the PDF is the document of record and page references point to it. Where the two disagree on a number or a cross-reference, both versions are recorded side by side with their locations and neither is treated as governing; no post quotes a number that its two published versions disagree on without saying so.**

Eight patterns the corpus found, worth knowing because our own page and PDF will diverge the same ways.

1. **Which version is the careful one is not fixed.** The PDF is internally consistent and the web page drifts in `economic-index-2025-09-report` (Chapter 3 cross-references off by one) and `-2026-03-report` (a reference to a non-existent Figure 1.6). The web page is the later, cleaner text in `-2026-06-report` (nine silent repairs, including the 3 a.m./5 a.m. contradiction the PDF has with itself) and in `claude-code-expertise-2026-06` ("**The PDF is the document of record and it is the less careful text**"), and it carries a paragraph the PDF lost in `-2026-01-report` — "**it is not complete. Where a caveat is missing from the PDF, check the web page.**"
2. **Content exists in one version only.** The PDF-only codebase-anchoring paragraph and the web-only looser-success sentence in `claude-code-expertise-2026-06`; the PDF-only overview exhibit in `labor-market-impacts-2026-03`; the whole appendix text and both prompts in `survey-81k-economics-2026-04`. "**A finding that exists in only one of a document's two published versions cannot be cited without saying which version it is from.**"
3. **A threshold differs.** "failure signals ≥ 3" (PDF) against "> 3" (web) — "Not the same subsample, and the caption is the only place the threshold appears" (`claude-code-expertise-2026-06`).
4. **A construct is renamed.** "the user" against "the person"; "Software engineers and users in other 'computer and mathematical occupations'" against "People in software-related occupations" (same file); "Observed Exposure" capitalised in one version and not the other (`labor-market-impacts-2026-03`).
5. **A number changes what it is a share of.** "the top 10% **of coverage**" against "the top 10%" — "Without the two words the sentence reads as the top 10% of workers" (`labor-market-impacts-2026-03`).
6. **The share card, the browser title and the citation block drift furthest, because they are written last.** Four titles for one piece (`worker-retraining-2026-08`, including two disagreeing BibTeX blocks); two titles in two registers (`claude-code-expertise-2026-06`: an academic title in the H1 and "How Claude Code is used in practice" in the OG title); a share-card description that asserts a conditional effect the page itself disclaims (`skill-formation-rct-2026-01`: "**A description field is a quantitative claim and takes the same discipline as a sentence.**")
7. **Caption typography and footnote numbering differ systematically.** Terminal periods added or dropped; per-chapter footnote numbering in the PDF against continuous numbering on the web (`-2025-09-report`, `-2026-01-report`, `-2026-03-report`, `-2026-06-report`). "**Cite this report's footnotes by chapter, not by number, or the two versions disagree.**"
8. **Only one version carries a correction, and it can be the one that is not the record.** "Updated Mar 8, 2026: Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates" — web only, on the paper's single positive finding. "**When a correction bears on a paper's only positive result, the corrected document should say so**" (`labor-market-impacts-2026-03`).

**Two further version facts.** Two copies of one appendix are live on the CDN with different last-page headings and no version marker (`economic-index-2026-06-appendix`) — "an argument, for our own work, for a version line and a content hash on anything republished." And the published correction is a model worth imitating: old wording quoted, new wording quoted, reason given in six words, dated, left on the page permanently (`survey-81k-interviews-2026-03`, which changed "67% of people view AI positively" to "67% of interviewees expressed net positive sentiment toward AI"). "Both the direction of the fix and its published record are what we want … **Every finding sentence in one of our posts should already read like the corrected version.**"

---

## Anti-patterns

Each is a fault the corpus found in itself. A draft is checked against this list before it goes to the referee.

**Numbers and units**
1. A number that exists only in a summary bullet, an image, a caption or an alt string, with no prose home.
2. One finding stated at two precisions or in two units, unreconciled. "a finding written twice at two precisions is a finding written twice."
3. A switch of unit at the top of the document so that the headline reads largest.
4. Four nouns for one denominator across a piece.
5. A relative change and a percentage-point change in adjacent sentences with nothing marking the switch.
6. A ratio published without either of its rates.
7. A percentage of a base under thirty.
8. Growth rates computed from rounded levels, so each is more precise than its inputs.
9. A base stated once and never repeated at a later point of use.
10. A caption whose base is not the body's words.

**Findings**
11. A magnitude word as the whole of a finding ("increased slightly", "decreased sharply", "notably higher use").
12. A significant estimate described in language that implies a large one.
13. "Significant" used colloquially where there is no test.
14. A superlative attached to a finding rather than to the vantage point.
15. A mechanism asserted without a modal or an adverb.
16. "This makes sense:" as a transition.
17. A conclusion drawn from a pattern that does not test it ("the strongest predictor", "well-calibrated").
18. A sentence at the wrong unit of observation, three sentences from the sentence at the right one.
19. A construct that widens between the finding and the close: session-level to person-level, "typically male names" to "men", "inferred" to observed.
20. An item dropped between the bullet and the body, or named in a bullet and never earned in a section.
21. A claim in the close whose construct and number appear nowhere in the body.
22. A shape claim — a U, a concavity, a parallel — with no slope comparison and no test.
23. A null and a positive trend asserted in the same clause with neither quantified.

**Caveats**
24. "As with all studies it has important limitations."
25. A pooled caveats block hundreds of words from the finding it undercuts.
26. A caveat and its finding in different chapters (the Super Bowl footnote).
27. A scope condition in the caption and the claim in the prose, so the sentence travels without its fence.
28. A one-sided list of the reasons an estimate could be wrong.
29. A robustness claim with no alternative named and no number.
30. "We ran robustness checks and believe that this activity is not driving the results."
31. A limitations section entirely about external validity, silent on what the piece's own numbers can support. "A limitations section that is entirely about external validity is a limitations section that has not been refereed."
32. A reassurance stated more vaguely than the doubt it answers ("in expected directions", "the majority of sessions").
33. An exclusion whose reason is given and whose size is not.
34. A concession about sample size followed by an assertion of magnitude, with no number on either side of the "but".

**Structure and closes**
35. A summary block, at all.
36. A number appearing for the first time in the close.
37. A hedge or a fence lost in the restatement.
38. An appendix finding, or a benchmark that sizes the headline, placed after the close.
39. A close that ends on the instrument when the instrument is not the contribution.
40. A close that ends on a quantity the post never measured.
41. A title carrying a word the findings do not test.
42. A title and an ending that do not share a working word.
43. An Anthropic programme offered as the response to the post's own finding.
44. A recommendation with no addressee, or a recommendations section that recommends only the thing the post studied.

**Captions and exhibits**
45. A caption that never says what is plotted.
46. A caption that states a conclusion without stating what was divided by what.
47. A caption stating a relationship the prose has not stated with its number, or a universal.
48. A caption vaguer than the exhibit it describes.
49. A caption defining a mark the legend calls something else.
50. Two titles on one exhibit that do not agree.
51. A figure with no n.
52. A two-panel figure whose caption describes one panel.
53. A significance family asserted in one clause, with no count and no correction.
54. Intervals described for a different estimator from the one that produced the points.
55. Star levels used in the exhibit that the key does not define.

**Process**
56. A threshold chosen because it reproduces a prior result, described as internally consistent.
57. An instrument change between waves disclosed and not re-run.
58. A sampling frame introduced as a boast ("we invited everyone with a Claude.ai account").
59. A decomposition the piece could run and does not, on a composition effect it has already named.
60. A construct exported to another document that the post's own exhibits depend on.

---

## Verification

**Files read in full, 2026-09-16** (all twenty-three in `wiki/style/`, 10,131 lines): `claude-code-expertise-2026-06.md`, `claude-code-expertise-2026-06-appendix.md`, `coding-agents-social-sciences-2026-05.md`, `coding-agents-social-sciences-2026-05-appendix.md`, `economic-index-2025-02-paper.md`, `economic-index-2025-02-report.md`, `economic-index-2025-03-report.md`, `economic-index-2025-04-software-development.md`, `economic-index-2025-09-blog.md`, `economic-index-2025-09-report.md`, `economic-index-2026-01-blog.md`, `economic-index-2026-01-report.md`, `economic-index-2026-03-appendix.md`, `economic-index-2026-03-report.md`, `economic-index-2026-06-appendix.md`, `economic-index-2026-06-report.md`, `labor-market-impacts-2026-03.md`, `labor-market-impacts-2026-03-appendix.md`, `productivity-gains-2025-11.md`, `skill-formation-rct-2026-01.md`, `survey-81k-economics-2026-04.md`, `survey-81k-interviews-2026-03.md`, `worker-retraining-2026-08.md`.

**Also read:** `README.md`, `team/SETUP.md`, `team/templates/POST.md`, `.claude/skills/room-protocol/SKILL.md`, `/mnt/memory/standards/{criteria,register,terminology,file-ownership}.md`, and the eight director rulings in `room/` that govern the corpus (`session-1-1-kickoff`, `session-1-2-kickoff`, `alt-text-ruling`, `caption-amendment`, `figure-values-ruling`, `chart-asset-ruling`, `pdf-web-ruling`, `index-rulings`).

**Provenance of every quotation here.** Every quoted passage is taken from the corpus file named beside it, where it is recorded as verified against its source on 2026-09-16 (each corpus file's own `## Verification` section states the URL, the fetch date, the extraction method and the quotation check). No source was re-fetched from this thread, and nothing is quoted from `wiki/reports/`, from `reference/`, or from memory. Where this guide characterises a pattern rather than quoting one, the characterisation is the corpus file's own annotation, and the file is named.

**Rulings applied.** No number read off a chart image appears anywhere in this guide (`room/director-2026-09-16-figure-values-ruling.md`). No number appears here that its corpus file marked `(alt text)`. Captions are quoted as the emphasised sentences under an image, bold or italic (`room/director-2026-09-16-caption-amendment.md`). Where two published versions of one piece disagree, both are recorded and neither is treated as governing (`room/director-2026-09-16-pdf-web-ruling.md`).

**Frequency counts** are reproduced from the corpus files that computed them (`productivity-gains-2025-11`, `claude-code-expertise-2026-06` and its appendix, `survey-81k-economics-2026-04`, `labor-market-impacts-2026-03-appendix`, `economic-index-2025-09-report`, `coding-agents-social-sciences-2026-05-appendix`, `economic-index-2026-03-appendix`), with the counting method each file states. No count was recomputed here.

**Where the corpus is inconsistent, this guide says so rather than averaging:** on whether a heading should assert (`Structure`); on where a limitations section sits (`Limitations`); on caption emphasis and terminal punctuation (`Captions and figures`); on whether the PDF or the web page is the more careful text (`Divergences and version handling`); on whether findings numbers belong in a summary block (`Openings`).

**Scope.** This guide records how Anthropic's economics research is structured and written. It makes no judgement about whether any finding in the corpus is correct, and it computes nothing from released data. Where it says a caveat is misplaced, an n absent, an MDE missing, a construct drifted or a claim uncheckable, that is the corpus file's statement about the writing, reproduced here.
