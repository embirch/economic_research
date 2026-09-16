# labor-market-impacts-2026-03 — style annotation

## Source

- **Title (PDF cover, and the document of record):** "Labor market impacts of AI: / A new measure / and early evidence", set over three lines — and set in **two colours**: the first line, the subject, in black; the second and third lines, the contribution, in grey. The web H1 runs the same words on one line. The browser/OG/Twitter title **truncates it**: "Labor market impacts of AI: A new measure \ Anthropic", with `og:title` and `twitter:title` both "Labor market impacts of AI: A new measure". The share card therefore promises the measure and drops the evidence. The citation block, in both versions, carries the full title.
- **Date:** PDF cover, "Published / March 5, 2026". Web dateline, "Mar 5, 2026". The primary PDF build's `/CreationDate` is 2026-03-09 22:15 UTC — four days after the stated publication date; a second, earlier build (`a42bc3fc…`, `/CreationDate` 2026-03-06) of the same 17 pages also resolves, and is what `economic-index-2026-03-report` links as "a previous report". Per `wiki/INDEX.md` Standing notes 4 the two are one publication; page references are interchangeable.
- **URLs fetched:**
  - PDF (document of record): https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf — 17 pages, letter, Adobe InDesign 21.2. Retrieved with `curl` (see `## Verification`); the fetch service refuses `cdn.sanity.io`. This is also the file the web page's "Read in PDF" button serves today.
  - Web page: https://www.anthropic.com/research/labor-market-impacts (its own `canonical` tag gives the same URL).
  - **Not fetched:** the separate appendix, https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf, reached from PDF footnote 7 ("Appendix available here") and from the page's Appendix section. It has its own corpus slug, `labor-market-impacts-2026-03-appendix`, and nothing from it is quoted or characterised here.
- **Document type:** a two-author economics paper published on the research namespace, tagged "Economics". It cannot decide what to call itself: "In this **paper**, we present a new framework" (p.3), "**This report** introduces a new measure" (p.13), and the cover's acknowledgement of external readers thanks them "for feedback on earlier versions of this **note**" (p.1) where the web page says "this **report**". No abstract, no executive summary, no methods section, no limitations section, no numbered sections; seven substantive headings, all of them labels.
- **Approximate length:** 17 PDF pages; roughly 3,000 words of body prose (pp.3–14), plus a ~120-word key-findings block, eleven footnotes (~700 words) and 22 references. Cover, p.1; Key findings and an unnumbered overview exhibit, p.2; body, pp.3–14; footnotes, pp.15–16; references, pp.16–17. Eight exhibits in twelve pages of prose: Figures 1–7 and the unnumbered overview.
- **Authors:** "Maxim Massenkoff and Peter McCrory" — one tier, no lead-author note, no "contributed equally" clause, no institutional byline. Eighteen acknowledgees, and then, in a separate sentence, four external economists thanked by name for feedback: "Martha Gimbel, Anders Humlum, Evan Rose, and Nathan Wilmers". **Naming your readers separately from your colleagues is a small thing that tells an economist the paper was refereed before it was posted**, and one of the four (Gimbel) is cited in the body as a competing approach.
- **Audience, and how it shows.** Economists, addressed as economists. There are 22 references and eighteen distinct outside works named in the prose or the footnotes — Eloundou et al., Blinder et al., Ozimek, Graetz and Michaels, Acemoglu and Restrepo, Acemoglu et al., Autor et al., Borusyak et al., Brynjolfsson et al., Johnston and Makridis, Hui et al., Hampole et al., Gimbel et al., Gans and Goldfarb, Autor and Thompson, Eckhardt and Goldschlag, Fujita et al., Massenkoff (2025). Nothing is glossed for a lay reader: "difference-in-differences", "O-ring model", "shift-share", "panel dimension of the CPS" and "binned scatterplot" all appear undefined. Compare the Economic Index reports, which define a primitive at every point of use. **The inverse is also true and is worth noticing: four of the 22 references are never cited anywhere in the text**, and three of those four are Anthropic's own — Appel et al. (2026), Handa et al. (2025), Tamkin and McCrory (2025), plus Tomlinson et al. (2025). The series lineage is in the bibliography; the argument is conducted in the outside literature.
- **Typography, since this file quotes emphasis.** Body: serif, 17 pt. Section headings: sans, 23 pt. Captions: sans, 12 pt, with the **title line in black and the gloss in grey (#414042)** and the two lines at the same size. There is **no bold anywhere in the document**. Italic is used in the body exactly twice: "*Observed Exposure*" at first definition (p.5) and "*concentration*" in the treatment-definition paragraph (p.10); the key-findings bullet italicises "*observed exposure*" too. So, per `room/director-2026-09-16-caption-amendment.md`, the caption here is the emphasised block under the exhibit — and the emphasis is carried by **typeface and colour rather than by weight**, which is a third convention beyond the corpus's bold (PDF) and italic (web) cases.
- **Live links in the PDF, in full:** five in the body — "O\*NET" → onetcenter.org, "Anthropic Economic Index" → anthropic.com/economic-index, "predicted" → data.bls.gov/projections/occupationProj, the Hugging Face dataset URL, and the citation URL — plus "here" in footnote 7 → the appendix PDF, and "Eckhart and Goldschlag (2025)" in footnote 8 → eig.org. That is the whole inventory. The paper links its three inputs and its output dataset and nothing else.
- **The web page carries a one-sentence abstract the PDF does not have**, in its meta description (identical in `description`, `og:description` and `twitter:description`): "We introduce 'observed exposure,' combining LLM capability with real Claude usage data, and share early evidence on employment effects." Note what the share card does that the document never does: it says **Claude** where key finding 1 says "real-world usage data".
- **Alt text: there is none.** All seven figures on the web page carry `alt=""`; only the hero image has alt text, and it is the title. Recorded here as an absence, per `room/director-2026-09-16-caption-amendment.md`.

### How the web page differs from the PDF

More than any other piece in the corpus so far. Eleven differences, all verified today; the PDF governs, per `room/director-2026-09-16-pdf-web-ruling.md`.

1. **The web page adds a heading the PDF does not have.** The body's first section is unheaded in the PDF; on the web it is "Introduction". The PDF's first prose therefore arrives with no label at all, straight under the key findings.
2. **The PDF's unnumbered overview exhibit is missing from the web page.** On p.2, under the key findings, sits a schematic captioned "An overview of our method and some of our main results / See below for how we measure task coverage and the impacts of AI on unemployment." The web page goes from the fifth bullet straight to "Introduction". The document's only summary diagram exists in one rendering.
3. **The measure is capitalised in one version and not the other.** PDF p.5: "Our new measure, *Observed Exposure*, is meant to quantify". Web: "Our new measure, *observed exposure*, is meant to quantify". The PDF is internally inconsistent about its own coinage: lower case in key finding 1 (p.2), capitalised at the definition (p.5), lower case in the same sentence four lines later ("observed exposure provides insight").
4. **A number changes what it is a share of.** PDF p.12: "If all workers within the top 10% **of coverage** were laid off". Web: "If all workers within the top 10% were laid off". Without the two words the sentence reads as the top 10% of workers.
5. **The outcome is renamed mid-paper, differently in each version.** PDF p.12: "Figure 7 shows the monthly **job start rate**". Web: "the monthly **job finding rate**". Both versions then use "Job finding rates" two sentences later, so the PDF uses both names for one quantity within a paragraph.
6. **A caption's glyph changes.** Figure 4, PDF: "The small **squares** mark individual example occupations". Web: "The small **diamonds**".
7. **A typo is fixed on the web and not in the PDF.** Footnote 9 (web footnote 8): "In **ni** extension do we find clear impacts on exposed jobs" / "In **no** extension…".
8. **Three captions lose their opening formula on the web.** PDF: "This figure shows the share of job tasks…" (Fig. 2), "This figure shows the top ten…" (Fig. 3), "This is a binned scatterplot…" (Fig. 4). Web: "Share of job tasks…", "Top ten most exposed occupations…", "Binned scatterplot…". **And Figure 5's gloss is dropped from the web page entirely** — the table appears with a title and nothing else.
9. **Footnote numbering differs by one after footnote 6.** The web drops PDF footnote 7 ("Appendix available here", which becomes an inline link) and renumbers: PDF 8/9/10/11 are web 7/8/9/10. Footnote numbers in this file are **the PDF's**.
10. **Small typographic and wording differences:** "trendlines" (PDF) / "trend lines" (web); en dashes in "6–16%" and "2024–2034" (PDF) become em dashes on the web; the acknowledgements add Kim Withee on the web and change "this note" to "this report".
11. **Only the web carries a correction.** "Updated Mar 8, 2026: Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates." The PDF of record, built 2026-03-09, carries no corrections block — so the reader of the document of record cannot learn that the paper's one positive finding was published with its two series swapped. See `## Limitations`.

One further difference is layout, not text: in the PDF the exhibits sit where the page breaks allow, so Figures 2, 3, 4, 6 and 7 are printed **before** the paragraphs that read them; on the web each figure is placed **after** its introducing paragraph. Where this file says a caption precedes or follows a passage, it means in the PDF.

## Section order

Headings in PDF order; spans are the PDF's own page numbers. Seven substantive headings, none of them a finding — every one is a label or a task ("Measuring exposure", "Prioritizing outcomes", "Initial results"). Compare `wiki/style/coding-agents-social-sciences-2026-05.md`, where five of seven headings assert the result. A reader who reads only this paper's table of contents learns the method and nothing about what was found.

1. **Cover (p.1).** Two-colour title, "Published / March 5, 2026", two authors, eighteen acknowledgees, four external readers. No abstract, no findings, no figure.
2. **Key findings (p.2), ~120 words.** Five bullets, then the unnumbered overview exhibit with its two-line caption.
3. **Unheaded opening (p.3), ~240 words.** Three paragraphs: the track record of past exposure measures; what this paper does, with its null stated; when the framework earns its keep.
4. **"Counterfactuals" (pp.3–4), ~170 words.** What class of effect is detectable at all — COVID as the easy case, the internet and the China shock as the hard cases — then the task-based literature (footnote 2) and where this paper sits in it.
5. **"Measuring exposure" (pp.4–5), ~300 words.** Three inputs as bullets; Figure 1; the β scale; why usage falls short of capability, with a named counterexample; the 97% overlap.
6. **"A new measure of occupational exposure" (pp.5–8), ~550 words.** The purpose sentence; five qualitative conditions as bullets; the construction, in one paragraph, with the formula exported to the appendix; Figure 2 and the category gap; the conjecture; Figure 3 and the top occupations; the zero-coverage group.
7. **"How exposure tracks with projected job growth and worker characteristics" (pp.8–9), ~300 words.** BLS projections; Figure 4; the regression and the β-alone null; Figure 5 and the pre-period differences between the groups.
8. **"Prioritizing outcomes" (p.10), ~210 words.** What other researchers measure, in one paragraph with four named designs; why this paper measures unemployment, in one paragraph of argument with no numbers.
9. **"Initial results" (pp.10–13), ~950 words.** Who counts as treated, with three cited theories and the assumption stated as an assumption; Figure 6 and the null; "What kind of scenarios can this framework identify?" — the power statement and two calibration scenarios; young workers; Figure 7 and the hiring result; alternative interpretations.
10. **"Discussion" (pp.13–14), ~250 words.** Three paragraphs: what the paper did and found; the paper's standing; three improvements.
11. **"Data availability" and "Bibtex citation" (p.14); footnotes 1–11 (pp.15–16); references (pp.16–17).**

**Where the findings sit: in the key findings, then once each in the body, then once each in the close — and nowhere else.** Nothing appears for the first time in the Discussion; no number appears in the Discussion at all. That is the rule the March 2026 Economic Index report broke and this paper keeps.

**Where the method sits: in the body, in prose, at the front.** Sections 5, 6 and 7 are the measure; sections 8 and 9 are the design. **Five of the twelve prose pages are spent on the instrument before a single labour-market outcome is shown, and two further sections argue about design before any estimate appears.** The order — what past measures got wrong, what would be detectable, how the measure is built, whether it tracks anything external, who the exposed are, which outcome to look at, what the outcome shows — is the order of a pre-registration, and it is the most transferable structural fact about this paper. A post that reports a null has to earn it in exactly this sequence.

**What is deferred, and how little.** One sentence sends the reader out: "We give mathematical details in the Appendix.⁷" Footnote 6 defers the robustness of the construction and footnote 9 defers three extensions. Everything else — the gate in words, the automation weighting, the two aggregation rules, the crosswalk, the treatment definition, the outcome, the power — is stated in the document. Against the March 2026 report, which exported the definition of every construct in its central exhibits, this is a document a reader can follow without leaving it, with the single exception of the formula itself.

**One layout fact with an editorial consequence.** Figure 5 is a *table* and is numbered as a figure, and its gloss says so ("This table shows exposure, demographics, education, and labor market outcomes"). A single exhibit sequence for tables and figures is defensible; a caption that has to correct its own number's noun is a sign the sequence was decided after the exhibits were made.

## Opening move

### The unheaded opening, verbatim and in full

> The rapid diffusion of AI is generating a wave of research measuring and forecasting its impacts on labor markets. But the track record of past approaches gives reason for humility.

> For example, a prominent attempt to measure job offshorability identified roughly a quarter of US jobs as vulnerable, but a decade on, most of those jobs maintained healthy employment growth. The government's own occupational growth forecasts, while directionally correct, have added little predictive value beyond linear extrapolation of past trends. Even in hindsight, the impact of major economic disruptions on the labor market is often unclear. Studies on the employment effects of industrial robots reach opposing conclusions, and the scale of job losses attributed to the China trade shock continues to be debated.[1]

> In this paper, we present a new framework for understanding AI's labor market impacts, and test it against early data, finding limited evidence that AI has affected employment to date. Our goal is to establish an approach for measuring how AI is affecting employment, and to revisit these analyses periodically. This approach won't capture every channel through which AI could reshape the labor market, but by laying this groundwork now, before meaningful effects have emerged, we hope future findings will more reliably identify economic disruption than post-hoc analyses.

> It is possible that the impacts of AI will be unmistakable. This framework is most useful when the effects are ambiguous—and could help identify the most vulnerable jobs before displacement is visible.

### The second move — "Counterfactuals" — verbatim

> Causal inference is easier when the effects are large and sudden. The COVID-19 pandemic and accompanying policy measures caused economic disruption so stark that sophisticated statistical approaches were unnecessary for many questions. For example, unemployment jumped sharply in the early weeks of the pandemic, leaving little room for alternative explanations.

> The impacts of AI, however, might be less like COVID and more like the internet or trade with China. The effects may not be immediately clear from aggregate unemployment data; factors like trade policy and the business cycle could cloud interpretations of trendlines.

### The key findings, verbatim

> **Key findings**
>
> - We introduce a new measure of AI displacement risk, *observed exposure*, that combines theoretical LLM capability and real-world usage data, weighting automated (rather than augmentative) and work-related uses more heavily
> - AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible
> - Occupations with higher observed exposure are projected by the BLS to grow less through 2034
> - Workers in the most exposed professions are more likely to be older, female, more educated, and higher-paid
> - We find no systematic increase in unemployment for highly exposed workers since late 2022, though we find suggestive evidence that hiring of younger workers has slowed in exposed occupations

### Annotation

- **The first noun that matters is "humility", and the first numbers are other people's — and wrong.** The opening does not begin on the phenomenon (February 2025's "forecast → therefore measure"), on an anomaly (September 2025), or on the instrument (March 2026). It begins on **the failure of the genre the paper is joining**: offshorability called a quarter of US jobs vulnerable and was not borne out; the official forecasts added little beyond extrapolation; the robots literature disagrees with itself; the China shock is still argued about. Four failures, one sentence each, all sourced in a single footnote. **Opening on the track record of the measures you are about to add to is the strongest available way to earn a null**, and it is the move to copy when a post's result is "we looked and did not find it".
- **The null is announced in the third paragraph and again in bullet 5.** "test it against early data, **finding limited evidence that AI has affected employment to date**". Nothing is held for the reveal. A paper whose contribution is an instrument can afford this; a paper whose contribution is a result cannot, and the difference is worth naming because our posts will usually be the second kind.
- **The why-it-matters is an option on future detection, not a claim about the present.** "by laying this groundwork now, before meaningful effects have emerged, we hope future findings will more reliably identify economic disruption than post-hoc analyses", and then "This framework is most useful when the effects are ambiguous—and could help identify the most vulnerable jobs before displacement is visible." The stake is that *later measurement will be better because this was built first*. For the programme lead's framing loop this is the construction to reach for when a brief's finding may well be a null: **the value is stated as what the instrument will make visible, and it survives whatever the data say today.**
- **"Counterfactuals" is the best structural idea in the paper.** Before any measure and any estimate, one section asks what kind of effect the design could see at all, and answers it with two historical regimes: COVID, where "sophisticated statistical approaches were unnecessary", against "the internet or trade with China", where "the effects may not be immediately clear". Naming an easy case and a hard case from economic history, and then saying which one you expect, does in two paragraphs what a power calculation does in a table — and the paper later returns and does the power calculation too (see `## Findings and their caveats`, finding 6). **A design section that comes before the results and asks "what would we be able to see?" is the thing our pre-registrations should read like in prose.**
- **The key findings carry no numbers at all.** Five bullets, zero magnitudes; the only digits are the years 2034 and 2022. Compare the March 2026 report, whose bullets quoted the largest available version of each number and switched units to do it. Here the summary is entirely qualitative and every number waits for the body — which means the summary cannot mis-size anything, and also that the reader gets no sense of the size of the gap the paper is about. Our house style has no summary block at all; of the two failure modes this is the safer one.
- **Bullet 4 is not a finding about AI.** "Workers in the most exposed professions are more likely to be older, female, more educated, and higher-paid" is the pre-treatment balance table, promoted into the findings list and phrased as a fact about people rather than about the comparison. It is useful and it is honest, and it is also the reason a referee reads the paper with the control group in mind from p.2 onward. Note that "older" has no supporting number anywhere in the text (see `## Limitations`).
- **Bullet 5 is a finding and its counterweight in one sentence**, joined by "though": "no systematic increase in unemployment for highly exposed workers since late 2022, **though** we find suggestive evidence that hiring of younger workers has slowed in exposed occupations". This is the same compression as the coding-agents headings built on "but", achieved inside a bullet. **A null and the one place it does not hold, in one sentence, is the shape to aim for.**
- **The bullet punctuation rule is consistent and worth copying.** Bullets that are full sentences take terminal periods (the three data-source bullets on p.4); bullets that are clauses or list items take none (the five key findings; the five exposure conditions on p.5).
- **Naming.** The title says AI. The key findings say AI five times and Claude never. The measure is "a new measure of **AI** displacement risk" whose usage half is Claude traffic, and the share card is the only place at the top of the document where that is said out loud. The body then splits the two cleanly and repeatedly (see finding 2). **The question says AI; every finding says Claude** — this paper does that in its body and not in its summary, and the gap between the two is exactly the thing our drafts get wrong.

## Findings and their caveats

### Finding 1 — usage sits on the tasks theory says are feasible

> Why might actual usage fall short of theoretical capability? Some tasks that are theoretically possible may not show up in usage because of model limitations. Others may be slow to diffuse due to legal constraints, specific software requirements, human verification steps, or other hurdles. For example, Eloundou et al. mark "Authorize drug refills and provide prescription information to pharmacies" as fully exposed (β=1). We have not observed Claude performing this task, although the assessment seems correct in that it could theoretically be sped up by an LLM.

> That said, these measures of theoretical capability and actual usage are highly correlated. As Figure 1 shows, 97% of the tasks observed across the previous four Economic Index reports fall into categories rated as theoretically feasible by Eloundou et al. (β=0.5 or β=1.0).

**Annotation.** The caveat comes **before** the finding, and it is a caveat about the measure rather than about the number: the question "Why might actual usage fall short of theoretical capability?" is asked in the reader's voice, answered with four mechanisms (model limits, legal constraints, software, human verification), and then made concrete with a **named false negative of the paper's own measure** — a task rated fully feasible that Claude has not been seen doing, quoted in full as an O\*NET string, with the concession that the outside rating is probably right ("although the assessment seems correct"). **One worked counterexample, quoted verbatim, does more to establish that a measure is understood than a paragraph about its limits.**

Then the finding, hedged only by its own construction: "these measures… are highly correlated", 97%, with the two β categories named so the reader knows what "feasible" means in the sentence. The number's denominator is stated ("the previous four Economic Index reports") — and it is **not the same denominator the measure uses** (footnote 5: "the previous two Anthropic Economic Index datasets, covering usage from August and November 2025"). Two windows, both disclosed, never reconciled. See `## Limitations`.

### Finding 2 — coverage is a fraction of capability

> Figure 2 shows observed exposure (in red) compared to β from Eloundou et al. (in blue), illustrating the difference between theoretical and actual use on our platform, grouped by broad occupational categories. We calculate this by first averaging to the occupation level weighting by our time fraction measure, then averaging to the occupation category weighting by total employment. For example, the β measure shows scope for LLM penetration in the majority of tasks in Computer & Math (94%) and Office & Admin (90%) occupations.

> The red area, depicting LLM use from the Anthropic Economic Index, shows how people are using Claude in professional settings. The coverage shows AI is far from reaching its theoretical capabilities. For instance, Claude currently covers just 33% of all tasks in the Computer & Math category.

> As capabilities advance, adoption spreads, and deployment deepens, the red area will grow to cover the blue. There is a large uncovered area too; many tasks, of course, remain beyond AI's reach—from physical agricultural work like pruning trees and operating farm machinery to legal tasks like representing clients in court.

**Annotation.** The paper's headline gap, and three things make it work. (i) **The aggregation rule is in the same paragraph as the number**, in one sentence, in words: average to the occupation weighting by time fraction, then to the category weighting by employment. A reader can say what 94% and 33% are averages of. (ii) **The comparison is carried by two colours named in both the caption and the prose** ("in red", "in blue", "The red area", "the blue"), so the figure and the text share one vocabulary — at the cost that the finding cannot be stated without the picture. (iii) The magnitudes are given as a pair in the same unit on the same category (94% against 33%), which is the whole finding in five words of contrast.

**The two sentences in the middle are the model for the house naming rule:** "The coverage shows **AI** is far from reaching its theoretical capabilities. For instance, **Claude** currently covers just 33% of all tasks in the Computer & Math category." General claim, AI; measurement, Claude; adjacent sentences, no hedge lost. Copy this pair.

The third paragraph is the paper's one unhedged sentence about the future — "the red area **will** grow to cover the blue" — stated in the future indicative with no mechanism, no rate and no test, in a paper that elsewhere hedges everything. It is immediately balanced by the uncovered area and by two pairs of concrete tasks ("pruning trees and operating farm machinery"; "representing clients in court"), which is the concrete-examples device doing its job. But the conjecture is about a *trend* and the paper has two usage waves in hand and never differences them. **A forecast in the indicative, in a paper that could have tested it with the data it already used, is the kind of sentence a referee circles first.**

### Finding 3 — the top of the ranking, and the bottom that becomes the control group

> Figure 3 shows the ten occupations most exposed under this measure. In line with other data showing that Claude is extensively used for coding, Computer Programmers are at the top, with 75% coverage, followed by Customer Service Representatives, whose main tasks we increasingly see in first-party API traffic. Finally, Data Entry Keyers, whose primary task of reading source documents and entering data sees significant automation, are 67% covered.

> At the bottom end, 30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold. This group includes, for example, Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers, and Dressing Room Attendants.

**Annotation.** Three of the ten occupations are named and **each is given its mechanism in the same clause as its rank** — the coding evidence for the first, the API surface for the second, the specific task for the third ("whose primary task of reading source documents and entering data sees significant automation"). Naming *why* an occupation ranks where it does, inside the sentence that ranks it, is what stops a ranking from being a list. The other seven occupations exist only inside the figure; per `room/director-2026-09-16-figure-values-ruling.md` nothing read off the image is recorded here, so what this file records is the **absence**: seven of the top ten are uncitable from the text.

The second paragraph is the most consequential sentence in the paper and it is written as an aside. "30% of workers have zero coverage, **as their tasks appeared too infrequently in our data to meet the minimum threshold**" — the zero-exposure group is defined by a *measurement floor*, not by an economic property, and the paper says so at the moment it introduces it. That group is the control group for every result that follows. **Stating the construction of a group in the sentence that introduces it, including the fact that it is an artefact of a threshold, is exactly right; what the paper then does not do is carry the admission forward into the design.** The six concrete occupations do the rest of the work: a reader who sees Cooks, Lifeguards and Dishwashers knows without being told that this is not a comparison group matched on anything.

### Finding 4 — the outside validation, with its strength in the same sentence

> A regression at the occupation level weighted by current employment finds that growth projections are somewhat weaker for jobs with more observed exposure. For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points. This provides some validation in that our measures track the independently derived estimates from labor market analysts, although the relationship is slight. Interestingly, there is no such correlation using the Eloundou et al. measure alone.

**Annotation.** Four sentences, and each does one job: the specification with its weighting; the slope in decision units ("For every 10 percentage point increase in coverage… drops by 0.6 percentage points" — the per-\$10 device from the March 2026 report, in percentage points); what the result licenses, scoped ("**some** validation in that our measures track the independently derived estimates"); and the size, conceded in the same sentence, in five words: "**although the relationship is slight**". A magnitude and its own deflation in one sentence, with no footnote and no hedge stacked on the verb. That is the cheapest correct way to report a weak but real relationship.

The last sentence is the only horse-race in the paper: the composite predicts what its own capability input does not. It is flagged with "Interestingly", given no explanation, and never returned to. The paper combines four adjustments (the feasibility gate, the usage gate, the work-related filter, the automation weight) and reports no result with one of them switched off, so the sentence establishes that *something* in the usage half carries the signal and not which thing. **A surprising result marked as surprising and left unexplained is honest; a surprising result whose decomposition is one regression away and is not run is a gap.**

### Finding 5 — who the exposed workers are, before anything happened

> Figure 5 shows characteristics of workers in the top quartile of exposure and the 30% of workers with zero exposure in the three months before ChatGPT was released, August to October 2022, using data from the Current Population Survey. The groups are very different. The more exposed group is 16 percentage points more likely to be female, 11 percentage points more likely to be white, and almost twice as likely to be Asian. They earn 47% more, on average, and have higher levels of education. For example, people with graduate degrees are 4.5% of the unexposed group, but 17.4% of the most exposed group, an almost fourfold difference.

**Annotation.** A balance table reported as a finding, in the pre-period, with the window and the reason for the window inside the sentence that introduces it ("in the three months before ChatGPT was released, August to October 2022"). Then four words on their own: "**The groups are very different.**" Flat, unhedged, before the numbers — and it is the sentence that tells the reader how to read everything after it.

The numbers are mixed units handled well: percentage points for two binary characteristics, a ratio for the third ("almost twice as likely"), a percentage for pay, and then one worked pair in levels with its ratio spelled out ("4.5% of the unexposed group, but 17.4% of the most exposed group, an almost fourfold difference"). **Giving the levels and the ratio in the same clause means the reader cannot over-read either.**

What the paper does with the admission is nothing: no reweighting, no matching, no parallel-trends test. The most exposed group is richer, more educated and more female than the control group, and the design assumes the two would have moved together absent AI. **Reporting imbalance and then not addressing it is the referee's first question on this paper** (see `## Limitations`).

### Finding 6 — the null, and the best power statement in the corpus

> The upper panel of Figure 6 shows raw trends in the unemployment rate since 2016 for workers in the top quartile of exposure and the unexposed group. During COVID, the less AI-exposed workers—who are more likely to have in-person jobs—saw a much larger increase in unemployment. Since then, the trends have been largely similar between the two groups. The lower panel measures the size of the gap between the most and least exposed workers in a difference-in-differences framework, mirroring the findings from the raw data. The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero.[9]

> What kind of scenarios can this framework identify? Based on the confidence interval of the pooled estimate, differential increases in unemployment on the order of 1 percentage point would be detectable (this will change as new data comes in, so it is merely a ballpark estimate). If all workers within the top 10% of coverage were laid off, it would increase unemployment within the top quartile group from 3% to 43%, and it would increase aggregate unemployment from 4% to 13%.

> A smaller but still concerning impact would be a scenario such as a "Great Recession for white-collar workers." During the 2007-2009 Great Recession, unemployment rates doubled from 5% to 10% in the US. Such a doubling in the top quartile of exposure would increase its unemployment rate from 3% to 6%. This should be visible in our analysis as well. Note that our core estimate is based on *differential* changes in the unemployment rate in the exposed group compared to the less exposed group. If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected.

**Annotation.** The passage to imitate whenever a pre-registered test comes back null. Six things it does, in order.

1. **The null is stated with its direction and its size**: "has increased slightly but the effect is indistinguishable from zero". Not "we find no effect" — the point estimate's sign is given and then disowned.
2. **The raw series and the estimator are both described, and said to agree** ("mirroring the findings from the raw data"). Two implementations of one claim, in one sentence.
3. **The question is asked in the reader's voice and answered immediately**: "What kind of scenarios can this framework identify?" It opens a paragraph, carries no heading, and is the hinge of the section.
4. **The MDE is given in the unit of the outcome** ("differential increases in unemployment on the order of 1 percentage point would be detectable") **and dated** ("this will change as new data comes in, so it is merely a ballpark estimate"). A power statement that says it will move is more useful than one that pretends to be fixed.
5. **The MDE is then calibrated against two named scenarios a reader can judge** — one deliberately extreme (everyone in the top decile of coverage laid off: the exposed group's unemployment goes 3% → 43%, aggregate 4% → 13%) and one historical and plausible (the Great Recession's doubling applied to the exposed group: 3% → 6%), with the verdict attached in five words: "**This should be visible in our analysis as well.**" **An MDE is not a number, it is a scenario a reader can judge** — this is the single most copyable passage in the paper and the thing our nulls have never done.
6. **What the design cannot see is stated as a fact about the design**: "If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected." One conditional, no apology. This is the same form as the March 2026 report's "We do not observe people who signed up a year ago but are no longer using Claude", and it is the form our limitations sections should be built from.

The COVID sentence is the other thing to notice, because the paper does not. "During COVID, the less AI-exposed workers—who are more likely to have in-person jobs—saw a much larger increase in unemployment" is a within-sample demonstration that the two groups respond differently to an aggregate shock, i.e. direct evidence against the comparison the whole design rests on. It is reported plainly, given a mechanism in an em-dashed clause, and treated as background rather than as a threat.

### Finding 7 — the one positive result, and the most hedged sentence in the paper

> One group of particular concern is young workers. Brynjolfsson et al. report a 6–16% fall in employment in exposed occupations among workers aged 22 to 25. They attribute this decrease primarily to a slowdown in hiring rather than an increase in separations.[10]

> We find that the unemployment rate for young workers in the exposed occupations is flat (see Appendix). But slowed hiring may not necessarily manifest as increased unemployment, since many young workers are labor market entrants without a listed occupation in the CPS data and may exit the labor force rather than appear as unemployed. To address hiring directly, we use the panel dimension of the CPS, counting the percent of young (22-25 year old) workers who begin a new job in a more vs. less exposed occupation over time.

> Apart from some large swings in 2020-2021, these series visually diverge in 2024, with young workers relatively less likely to be hired into exposed occupations. Job finding rates at the less exposed occupations remain stable at 2% per month, while entry into the most exposed jobs decreases by about half a percentage point. The averaged estimate in the post-ChatGPT era is a 14% drop in the job finding rate compared to that in 2022 in the exposed occupations, although this is just barely statistically significant. (There is no such decrease for workers older than 25.)

> This may provide some signal of the early effects of AI on employment, and echoes the findings from Brynjolfsson et al. But there are several alternative interpretations. The young workers who are not hired may be remaining at their existing jobs, taking different jobs, or returning to school. A further data-related caveat is that job transitions may be more vulnerable to mismeasurement in surveys.[11]

**Annotation.** The structure is exemplary and the units are not.

The structure: the outside result first, with its own range and, in footnote 10, the reason the range is wide ("The 6 percentage point drop compares to a counterfactual of flat employment growth. The 16 percentage point estimate comes from a design comparing similar workers in the same firm with different occupations"). **Quoting somebody else's range and explaining what makes it a range, rather than picking the end that suits you, is the honest way to carry a comparator.** Then the paper's own null on the obvious outcome (youth unemployment is flat), then the reason that null is uninformative (entrants have no listed occupation and may leave the labour force rather than be counted unemployed), then the switch to the margin where the effect would show, with the construction stated in one clause ("counting the percent of young (22-25 year old) workers who begin a new job in a more vs. less exposed occupation over time"). **A null, the reason the null cannot settle the question, and the second measure chosen for that reason — in three sentences.**

Then the hedging, which is the heaviest in the document and correctly so: "visually diverge", "about half a percentage point", "**although this is just barely statistically significant**", "may provide **some** signal", "echoes". Plus a placebo in parentheses, which is where a placebo belongs when it passes: "(There is no such decrease for workers older than 25.)" And then a whole paragraph of rival destinations for the un-hired — other jobs, existing jobs, school — none distinguished, plus a measurement caveat with a citation.

The units are the flaw. One finding, three quantities, three units, two sentences: a level in percent per month (2%), a change in percentage points ("about half a percentage point"), and the same change in relative terms ("a 14% drop in the job finding rate"). Nothing marks the switch, and 0.5pp on a 2% base is exactly the 25% that the 14% is not. **Within a finding, one unit; where the unit changes, say so in the same sentence** — the same rule the March 2026 report broke, broken here inside a single paragraph.

### The hedge vocabulary, graded

In descending confidence, collected from the passages above: *we present* · *we find* · *shows* · *we compare* · *finds* · *mirroring* · *suggesting* · *provides some validation* · *this may provide some signal* · *echoes* · *is consistent with*-by-implication · *tentative evidence* · *suggestive evidence* · *somewhat weaker* · *the relationship is slight* · *just barely statistically significant* · *small and insignificant* · *indistinguishable from zero* · *merely a ballpark estimate* · *visually diverge* · *may* · *might* · *could* · *arguably* · *seems correct* · *Interestingly*. The paper never writes *proves*, *demonstrates*, *causes* or *shows that AI has*. It has no *we speculate* and no *more research is needed*; the substitute for both is the alternative-interpretations paragraph after finding 7 and the three improvements in the close.

Two rungs are unusual and worth borrowing. **"limited evidence"** in the opening, which scopes a null without asserting a zero. And **"just barely statistically significant"**, written in plain words about the paper's own headline positive — a phrase that costs nothing and buys the reader's trust in every other number.

### Claude versus AI across the whole paper

- **Title:** "Labor market impacts of **AI**". **Key findings:** AI five times, Claude never.
- **Share card (web only):** "combining LLM capability with real **Claude** usage data".
- **The measure:** "a new measure of **AI** displacement risk"; "Our measure qualitatively captures several aspects of **AI** usage"; "Its tasks are theoretically possible with **AI**"; "Its **AI**-impacted tasks make up a larger share of the overall role" — the construct is named over AI throughout, while its usage half is "sufficient work-related usage in **Claude** traffic".
- **The measurement sentences say Claude:** "We have not observed **Claude** performing this task"; "how people are using **Claude** in professional settings"; "**Claude** currently covers just 33%"; "other data showing that **Claude** is extensively used for coding"; "Share of **Claude** usage" (Figure 1 title).
- **The general claims say AI:** "**AI** can grade homework but not manage a classroom"; "many tasks… remain beyond **AI's** reach"; "the early effects of **AI** on employment"; "we would not attribute this to **AI** advancements".
- **Where it slips:** Figures 6 and 7 are titled over "**no AI exposure**", and the body calls the same group "the unexposed group" and "the 30% of workers with zero exposure". That group is defined by not clearing a **Claude** usage floor in two Economic Index datasets. Calling it the no-AI-exposure group in a caption is the same class of slip as the March 2026 report's in-image "Geographic convergence of AI usage" for an index built on Claude usage — and it is worse here, because the label is in the caption rather than inside the picture, and because the group is a treatment arm rather than a series.

The rule to take: **the phenomenon, the stake and the mechanism say AI; the sample, the shares, the coverage and the groups say Claude.** This paper obeys it in prose and breaks it in two captions.

## Comparisons

Almost nothing in this paper is a level. Nine comparisons carry it.

### Theoretical capability against observed usage

> Our new measure, *Observed Exposure*, is meant to quantify: of those tasks that LLMs could theoretically speed up, which are actually seeing automated usage in professional settings? Theoretical capability encompasses a much broader range of tasks. By tracking how that gap narrows, observed exposure provides insight into economic changes as they emerge.

> the β measure shows scope for LLM penetration in the majority of tasks in Computer & Math (94%) and Office & Admin (90%) occupations

> Claude currently covers just 33% of all tasks in the Computer & Math category

**Annotation.** The measure *is* a comparison — a gap between what is possible and what is observed — and the paper defines it that way in a question, in the sentence that names it. **A construct defined as the distance between two existing quantities is easier to explain and harder to over-claim than one defined by a formula**, and the definition sentence carries its own reason for existing ("By tracking how that gap narrows…"). The same gap is then shown at three grains: all tasks (Figure 1), categories (94/90 against 33), occupations (Figure 3).

### The composite against its own input

> Interestingly, there is no such correlation using the Eloundou et al. measure alone.

**Annotation.** One sentence, and it is the only evidence in the paper that the new measure adds anything to the measure it is built from. That is a large claim resting on an unreported regression with no coefficient, no standard error and no figure. **When the point of a paper is a new measure, the comparison against the existing measure is the finding, and it should be the most heavily documented number in the document, not the least.**

### Against an outside forecast

> For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points. This provides some validation in that our measures track the independently derived estimates from labor market analysts, although the relationship is slight.

**Annotation.** The word doing the work is "independently derived": the BLS projections were made without reference to any AI usage data, so agreement is informative and the paper says why in six words. The strength is conceded in the same sentence. This is the cleanest "external validation" sentence in the corpus.

### Exposed against unexposed workers, before treatment

> The more exposed group is 16 percentage points more likely to be female, 11 percentage points more likely to be white, and almost twice as likely to be Asian. They earn 47% more, on average, and have higher levels of education.

**Annotation.** The comparison is run in the pre-period and reported as a description of the two arms. See finding 5.

### The same two groups over time, with COVID as an internal reference episode

> During COVID, the less AI-exposed workers—who are more likely to have in-person jobs—saw a much larger increase in unemployment. Since then, the trends have been largely similar between the two groups.

**Annotation.** The design's own history contains a shock whose sign is known, and the paper reports how the two groups moved through it. Used deliberately this is a falsification test; used as background, as here, it is the strongest available evidence against the design sitting unremarked in the paper's own figure. **If a comparison group has already been observed reacting differently to one shock, say what that implies for the next one.**

### Young workers against older workers

> (There is no such decrease for workers older than 25.)

**Annotation.** A placebo, in parentheses, at the end of the sentence carrying the estimate. One clause, no table, and it doubles the credibility of the result it follows.

### Against another team's result

> Brynjolfsson et al. report a 6–16% fall in employment in exposed occupations among workers aged 22 to 25. They attribute this decrease primarily to a slowdown in hiring rather than an increase in separations.

> [10] This range is wide because the authors provide estimates against multiple counterfactuals. The 6 percentage point drop compares to a counterfactual of flat employment growth. The 16 percentage point estimate comes from a design comparing similar workers in the same firm with different occupations.

**Annotation.** The comparator is quoted as a range, the mechanism of the range is explained in a footnote, and the paper's own weaker result is described as echoing it rather than confirming it ("**echoes** the findings from Brynjolfsson et al."). Note also that the comparator's outcome (employment) is not this paper's outcome (unemployment, then job starts), and the paper does not say so. A comparison across two different dependent variables needs one clause of warning.

### Counterfactual scenarios against the detection threshold

> If all workers within the top 10% of coverage were laid off, it would increase unemployment within the top quartile group from 3% to 43%, and it would increase aggregate unemployment from 4% to 13%.

> Such a doubling in the top quartile of exposure would increase its unemployment rate from 3% to 6%. This should be visible in our analysis as well.

**Annotation.** See finding 6. The construction is exactly reusable: *state the MDE; name a scenario with a historical precedent; do the arithmetic in the outcome's own unit; say whether the design would see it.*

### Past exposure measures against what actually happened, and COVID against the internet

> a prominent attempt to measure job offshorability identified roughly a quarter of US jobs as vulnerable, but a decade on, most of those jobs maintained healthy employment growth

> The impacts of AI, however, might be less like COVID and more like the internet or trade with China.

**Annotation.** Two comparisons that carry no data from this paper at all and do more framing work than any of the others. See `## Opening move`.

### What the set adds up to

**One claim, tested at five levels.** The exposure measure is checked against an official forecast (occupation level), a demographic profile (person level, pre-period), an unemployment series (person-month), a hiring transition rate (person-month, entrants only), and — in the appendix — alternative treatment cutoffs, an alternative age window and an administrative outcome. That is the house rule executed better than anywhere else in the corpus, and it is the shape our posts should be built in: **one measure, many levels, each answering a different objection to the others.**

What is missing from the set is the comparison the measure's own conjecture demands: the paper holds two usage waves (August and November 2025) and never compares coverage between them, so "the red area will grow to cover the blue" is asserted against data that could have tested it. There is also no comparison between the two Claude surfaces, although API presence is one of the five conditions that raise exposure.

## Figure captions

Eight exhibits: the unnumbered overview on p.2 and Figures 1–7. Figure 5 is a table.

**PDF form throughout:** sans face at 12 pt against a 17 pt serif body; **title line "Figure N: Sentence-case title" in black with no terminal period**, then the gloss on the following line(s) in grey, one to four sentences, each ending in a period. No bold anywhere. The unnumbered overview takes the identical form. **Web form:** same words, except that three glosses lose their opening formula and one gloss is dropped entirely (see `## Source`). Per `room/director-2026-09-16-figure-values-ruling.md`, **no number read off a chart image is recorded anywhere in this file**; all seven figures are images in both renderings, and the web page gives them empty alt text.

> **An overview of our method and some of our main results** See below for how we measure task coverage and the impacts of AI on unemployment.

**Annotation.** An unnumbered schematic directly under the key findings, captioned in the same style as the numbered exhibits, whose gloss does nothing but forward the reader ("See below"). It is the only exhibit in the paper that is not evidence, and it exists only in the PDF. A summary diagram whose caption cannot say what it shows is a diagram that has not decided what it is for.

> **Figure 1: Share of Claude usage by Eloundou et al. task exposure rating** This figure shows Claude usage distributed across O\*NET tasks grouped by their theoretical AI exposure. Tasks rated β=1 (fully feasible for an LLM alone) account for 68% of observed Claude usage, while tasks rated β=0 (not feasible) account for just 3%. Data on Claude usage comes from the previous four Economic Index reports.

**Annotation.** The fullest caption in the paper and the only one that carries numbers: the unit of observation, the grouping variable, **the two headline values with their β categories glossed in parentheses**, and the data window. Two consequences. First, 68% and 3% appear **nowhere in the body prose** — the caption is their only home, which is better than an image but still means a reader following the argument never meets them. Second, the window stated here ("the previous four Economic Index reports") is not the window the measure uses (footnote 5: the previous two datasets, August and November 2025). **A caption is the wrong place for a denominator that disagrees with the method section, because the caption is where a reader will believe it.**

> **Figure 2: Theoretical capability and observed exposure by occupational category** This figure shows the share of job tasks that LLMs could theoretically perform (blue area) and our own job coverage measure derived from usage data (red area).

**Annotation.** One sentence, two constructs, each tied to its colour. The gloss defines both series in the reader's terms ("could theoretically perform" / "our own job coverage measure derived from usage data") rather than by name, which is right. Missing: the two aggregation weightings that make the areas what they are — they are in the body paragraph, one page later, and the caption could have carried them in a dozen words. Also missing: what the horizontal axis is over and how many categories there are.

> **Figure 3: Most exposed occupations** This figure shows the top ten most exposed occupations using our task coverage measure.

**Annotation.** The shortest caption in the paper, and a paraphrase of its own title. No sample, no unit, no cutoff, no note that "coverage" here is the time-weighted occupation-level measure rather than the category measure of Figure 2. Seven of the ten occupations exist only in the image. **A ranking exhibit whose caption does not name the quantity being ranked is one line of text from being usable.**

> **Figure 4: BLS projected employment growth from 2024–2034 vs. observed exposure** This is a binned scatterplot with 25 equally-sized bins. Each solid dot shows the average observed exposure and projected employment change for one of the bins. The dashed line shows a simple linear regression fit, weighted by current employment levels. The small squares mark individual example occupations for illustration.

**Annotation.** The best caption in the paper and the standard for the corpus. Four sentences: the method and its one parameter ("25 equally-sized bins"), **what a dot is**, what the line is *and how it is weighted*, and what the second mark type means. The weighting in the caption is precisely what the March 2026 report left inside a chart image; here a reader can reconstruct the exhibit from its caption alone. What it still lacks is the coefficient — the −0.6pp per 10pp slope is in the body and not in the caption — and an interpretation sentence in plain words.

> **Figure 5: Differences between high and low exposure workers, Current Population Survey** This table shows exposure, demographics, education, and labor market outcomes.

**Annotation.** The title carries the data source, which is the right habit and is repeated in Figures 6 and 7. The gloss lists the row groups and nothing else: no sample period (the three pre-ChatGPT months are named only in the body), no N, no definition of either group, no note that "low exposure" means the 30% below the usage floor. **The paper's balance table — the exhibit a referee will read first — is the one whose caption cannot stand alone**, and on the web page it has no gloss at all.

> **Figure 6: Trends in the unemployment rate for workers in the top quartile of observed exposure and no AI exposure, Current Population Survey** The top panel shows the unemployment rate for workers in the top quartile of exposure (red line) and the 30% of workers with zero exposure. The bottom panel measures the gap between these two series in a difference-in-differences framework.

> **Figure 7: New job starts among workers age 22-25 in occupations with high observed exposure and no AI exposure, Current Population Survey** The top panel shows the percent of young workers starting new jobs in high vs. no exposure occupations. The bottom panel measures the gap between these two series in a difference-in-differences framework.

**Annotation.** Two captions built to one template, which is itself the point: **when two exhibits do the same thing to two outcomes, give them the same caption sentence structure** — title names outcome, groups and source; first gloss sentence says what the top panel plots and which line is which; second says what the bottom panel estimates. A reader who has understood Figure 6 can read Figure 7 without re-learning anything.

What the pair does not carry: the sample window (Figure 6's series start in 2016, stated only in the body); the event date the difference-in-differences is measured from; the confidence level; any N; and, in Figure 7, the definition of a "new job start", which is in the body's parenthesis ("when a worker reports a job that they did not have in the previous month"). And the group label — "no AI exposure" — is the naming slip discussed above. Figure 7 is also the exhibit whose two groups' labels were **published reversed** and corrected three days later, a fact recorded only on the web page.

### The caption template, distilled

**Keeps:** numbered title in sentence case with no terminal period; gloss in a second colour, one sentence per job; the data source in the title where the data are external (Figures 5, 6, 7); the unit of observation first; the method and its parameters stated where the exhibit is a construction (Figure 4); "what a dot is" for a scatter (Figure 4); the weighting of a fitted line (Figure 4); panel logic sentences, identically worded across sibling exhibits (Figures 6, 7); constructs glossed in the reader's terms rather than by name (Figure 2).

**Drops, and each drop costs something:**
1. **No sample line on any of the eight exhibits** — no N, no window, no exclusions, no privacy note, on a paper whose unit of observation changes four times (task, occupation, person, person-month).
2. **No group definitions in the captions of the three exhibits that compare groups**, except Figure 6's "the 30% of workers with zero exposure".
3. **No coefficient in any caption**, including the two exhibits (4, 6) whose whole content is a fitted relationship, and no confidence level anywhere.
4. **No declarative finding titles.** All eight titles are descriptive labels. The paper never uses the title line to say what the exhibit shows happened.
5. **A denominator in a caption that contradicts the method** (Figure 1).

For our own posts: **a caption must carry the sample, the unit, the construct, the window, the group definitions and, where there is one, the coefficient — and a pair of exhibits doing the same thing to two outcomes must be captioned to one template.**

## Limitations

**There is no limitations section**, and no "Caveats" or "Threats to validity" heading in seventeen pages. The caveats are distributed across six places, and — unusually for the corpus — the heaviest of them are in the body, in the sentence carrying the number.

### 1. In the opening, as scope

> This approach won't capture every channel through which AI could reshape the labor market

> The impacts of AI, however, might be less like COVID and more like the internet or trade with China. The effects may not be immediately clear from aggregate unemployment data; factors like trade policy and the business cycle could cloud interpretations of trendlines.

### 2. Beside the construct

> Some tasks that are theoretically possible may not show up in usage because of model limitations. Others may be slow to diffuse due to legal constraints, specific software requirements, human verification steps, or other hurdles.

> We have not observed Claude performing this task, although the assessment seems correct in that it could theoretically be sped up by an LLM.

> At the bottom end, 30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold.

### 3. Inside the sentence carrying the number

> This provides some validation in that our measures track the independently derived estimates from labor market analysts, although the relationship is slight.

> The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero.

> although this is just barely statistically significant

### 4. As an assumption, named as an assumption

> A key question in interpreting our coverage measure is which workers should be considered treated? Should changes in employment be expected from just 10% task coverage?

> If AI capabilities advance quickly, task coverage might be high for lower percentiles of coverage, which might make an absolute threshold more helpful. But we make the assumption that impacts should affect the most exposed workers first, and present results varying the cutoff we use to define treatment.

> Note that our core estimate is based on *differential* changes in the unemployment rate in the exposed group compared to the less exposed group. If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected.

> But slowed hiring may not necessarily manifest as increased unemployment, since many young workers are labor market entrants without a listed occupation in the CPS data and may exit the labor force rather than appear as unemployed.

> But there are several alternative interpretations. The young workers who are not hired may be remaining at their existing jobs, taking different jobs, or returning to school. A further data-related caveat is that job transitions may be more vulnerable to mismeasurement in surveys.

### 5. In footnotes

> [6] There are judgment calls involved at every step. Should the Eloundou et al. (2023) measure enter as {0, 0.5, 1} or something else? What determines "significant" use? How do we handle tasks which seem very similar to those with high usage, but are too rare to have been picked up specifically in the sampling for the Economic Index? How much more should automation workflows count compared to augmentation? A reassuring finding which we expand on in the Appendix is that the Spearman (rank-rank) correlation of job exposure across many resolutions to these questions is exceedingly high.

> [9] We explore this further in three ways in the Appendix. First, we ask whether the percentile cutoff that we use to define treatment matters, varying it from the median to the 95th percentile. In all cases, the impact is flat or negative (meaning that unemployment decreases for the exposed group). Next, we focus on young workers in particular, those aged 22 to 25 as in Brynjolfsson et al. (2025). Finally, we use data on unemployment insurance claimants from the Department of Labor to measure the unemployment, rather than CPS survey responses. In ni extension do we find clear impacts on exposed jobs.

> [5] We use the previous two Anthropic Economic Index datasets, covering usage from August and November 2025. For ONET tasks that are highly semantically similar, we split the counts across them.

### 6. In the close, and on the web page only

> Our work is a first step toward cataloging the impact of AI on the labor market.

> The Eloundou et al. metric could also be updated, to the extent that it is linked to LLM capabilities as of early 2023.

> Updated Mar 8, 2026: Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates. *(web page only; absent from the PDF of record)*

### Annotation

- **Footnote 6 is the best single caveat in the corpus so far, and it is a list of questions.** "There are judgment calls involved at every step" followed by four specific ones — how β should enter, what counts as "significant" use, how near-duplicate tasks are handled, how much more automation should count than augmentation. That is a researcher-degrees-of-freedom list written by the people who exercised the freedom, and it names every seam in the measure. **Writing the assumptions sweep as four questions in the researchers' own voice is more honest and more readable than a paragraph of prose**, and it is the form to copy in our pre-registrations. Its weakness is the answer: the only robustness reported is that the *rankings* survive ("the Spearman (rank-rank) correlation… is exceedingly high"), which is not the same as showing that any of the four choices is individually defensible, and the appendix carries the evidence.
- **Three caveats sit in the sentence that carries the number they qualify** — "although the relationship is slight", "indistinguishable from zero", "just barely statistically significant". No footnote, no hedging of the verb, no separate paragraph. This is the placement the corpus keeps arguing for and this paper does it three times.
- **Two sentences state what the design cannot see**, in the conditional, without apology: the parallel-movement sentence and the labour-force-exit sentence. Both are of the form *if X happened, we would not see it / would not attribute it*. Our limitations sections should be built from that sentence pattern.
- **The three a referee would raise first.**
  1. **The control group is a measurement artefact, and the paper proves it is unbalanced.** The zero-exposure 30% are workers whose tasks "appeared too infrequently in our data to meet the minimum threshold", and Figure 5 shows they differ from the treated group on sex, race, education and pay before ChatGPT existed. No reweighting, no matching, no parallel-trends test — and the paper's own Figure 6 shows the two groups diverging sharply under the last aggregate shock. The null and the MDE are both conditional on a comparison the document itself has undermined, and nothing joins the two facts.
  2. **The usage window is stated twice, differently, and the measure's central conjecture is about change over time.** Figure 1's caption says four Economic Index reports; footnote 5 says the previous two datasets, August and November 2025. The paper has two waves and never differences them, so "the red area will grow to cover the blue" is offered with no trend estimate and the level of coverage cannot be dated.
  3. **The one positive finding is the most fragile thing in the paper and its exhibit was published wrong.** It is "just barely statistically significant", it is reported in three units in two sentences, and Figure 7's group labels were reversed until 8 March 2026 — a correction that appears only on the web page, so a reader of the document of record cannot know. **When a correction bears on a paper's only positive result, the corrected document should say so.**
- **Two more a referee would reach for.** The key finding that exposed workers are "older" has no supporting number in any sentence or caption — its only home is the Figure 5 image, which this file does not read. And the claim that the composite outperforms β alone is made in one sentence with no reported estimate, in a paper whose entire contribution is that composite.
- **Drafting tells.** Six, listed because they are the kind that survive when a document exists in two renderings and a third file holds the formulas.
  1. **An orphan footnote marker.** On p.10 the sentence "Their argument is that any important restructuring of the economy from AI would show up as changes in distribution of jobs.**¹**" carries a superscript one that points to footnote 1 — which is the source note for offshorability, robots and the China shock, and has nothing to do with Gimbel et al. On the web page the same character is rendered as literal text rather than as one of the ten footnote links, which confirms it refers to nothing.
  2. **"In ni extension do we find clear impacts"** (footnote 9), fixed on the web and left in the PDF.
  3. **The crosswalk's author is spelled two ways**: "Eckhart and Goldschlag (2025)" in footnote 8, "Eckhardt, Sarah and Nathan Goldschlag" in the references.
  4. **The measure is capitalised once and lower-cased everywhere else**, including four lines later in the same paragraph.
  5. **The outcome is named twice in one paragraph** — "job start rate", then "Job finding rates" — and the two published versions choose different names for the first of them.
  6. **Four references are never cited**, three of them Anthropic's own.
- **What the paper gets right about the limitations it has.** It states its power and calibrates it against two scenarios; it names a false negative of its own measure with the task quoted; it converts "which workers are treated?" into an open question with three cited answers before choosing one; and it states its treatment rule as an assumption in the sentence that adopts it. **A limitation that names the design that would settle it, or the arithmetic that bounds it, is worth three that do not.**

## Close

### "Discussion", verbatim and in full

> This report introduces a new measure for understanding the labor market effects of AI and studies impacts on unemployment and hiring. Jobs are more exposed to AI to the extent that their tasks are theoretically feasible with LLMs and observed on our platforms in automated, work-related use cases. We find that computer programmers, customer service representatives, and financial analysts are among the most exposed. Using survey data from the US, we find no impact on unemployment rates for workers in the most exposed occupations, although there's tentative evidence that hiring into those professions has slowed slightly for workers aged 22-25.

> Our work is a first step toward cataloging the impact of AI on the labor market. We hope that the analytical steps taken in this report, especially around coverage and counterfactuals, will be easy to update as new data on employment and AI usage emerge. An established approach may help future observers separate signal from noise.

> There are several improvements to be made to the present work. Our usage data will be incorporated in future updates, forming an evolving picture of task and job coverage in the economy. The Eloundou et al. metric could also be updated, to the extent that it is linked to LLM capabilities as of early 2023. And, given the suggestive results around young workers and labor market entrants, a key next step might be to look at how recent graduates with educational credentials in exposed areas are navigating the labor market.

### Annotation

- **Three paragraphs, ~250 words, and not one number.** The only digits in the close are an age range and a year. Compare the March 2026 Economic Index report, whose Discussion opened with two figures that had never appeared in prose. **This close carries nothing the body has not already carried**, which is the rule, and it is easy to keep when the close is short.
- **What was learned, in four sentences.** The first paragraph does what a close should: says what the paper did (past tense, scoped to the method — "introduces a new measure… and studies impacts"), **restates the measure in one sentence a reader could repeat** ("Jobs are more exposed to AI to the extent that their tasks are theoretically feasible with LLMs and observed on our platforms in automated, work-related use cases"), names three occupations, and gives both results with their hedges intact ("no impact", "tentative evidence… slowed slightly"). The one-sentence restatement of the construct is the most useful thing in the paragraph and the hardest to write; it contains the gate, the capability half, the usage half, the automation weighting and the work-related filter, without notation.
- **A defect worth naming: the third occupation is new.** "computer programmers, customer service representatives, and **financial analysts**" — financial analysts are named nowhere else in the text; the Figure 3 paragraph names only the first two and Data Entry Keyers. The close introduces a result whose only support is a bar in an image. That is the same fault as a new number in the close, in a different currency.
- **Why it matters is not in the close.** There is no paragraph about workers, policy, or what the finding implies for anyone; the stake was stated on p.3 as an option on future measurement and is never returned to. What stands in its place is a claim about the *method's* durability: "We hope that the analytical steps taken in this report, especially around coverage and counterfactuals, will be easy to update as new data on employment and AI usage emerge. **An established approach may help future observers separate signal from noise.**" That last sentence is the best in the close and it is the one the title is answered by. For our own posts the choice is worth making deliberately: **a close that ends on the instrument is right when the instrument is the contribution, and wrong the rest of the time** — and most of our posts will be the rest of the time.
- **What comes next, in three parts, one of them a real question.** Update the usage data; update the capability metric, with the reason stated ("to the extent that it is linked to LLM capabilities as of early 2023"); and then a named next study — "how recent graduates with educational credentials in exposed areas are navigating the labor market" — which is derived from the paper's own weakest result and is specific enough that somebody could run it. **A "what comes next" that names a population, a variable and a reason is a commitment; "more research is needed" is not.**
- **No recommendations, to anybody.** Not to policymakers, not to firms, not to researchers — though the paper releases its measure and hopes others will use it, which is a recommendation in everything but name. A post of ours that builds a measure and publishes it should say plainly who should use it for what; this paper leaves that to the data-availability line.
- **Title against ending.** Title: "Labor market impacts of AI: **A new measure** and **early evidence**". Close: paragraph 1 delivers the measure and the evidence in that order; "early" is answered by "a first step"; and the closing image of the second paragraph — separating signal from noise — is the opening's humility paragraph returned to. By the house test the loop closes, and it closes because the title promised an instrument rather than a result. Note the one thing that does *not* match: the title says "impacts", and the paper's finding is that there are none yet that it can see.
- **First person, throughout.** Roughly thirty-one instances of *we* or *our* in 3,000 words, in both registers: institutional ("our own usage data", "our platforms", "our previous two datasets") and analytical ("we present", "we find", "we compare", "we make the assumption", "we would not attribute"). House style forbids it. The substitutes this paper already supplies elsewhere are the ones to borrow: attribute to the exhibit ("Figure 2 shows observed exposure (in red) compared to β", "The upper panel of Figure 6 shows raw trends"), to the estimator ("A regression at the occupation level weighted by current employment finds that…"), or to the result ("This provides some validation…"). The hardest sentences to convert are the two that state assumptions in the first person — "we make the assumption that impacts should affect the most exposed workers first" and "we would not attribute this to AI advancements" — and the conversion is worth the trouble, because naming the assumption rather than the assumer ("the analysis assumes…", "a parallel rise in all groups is not attributed to AI") makes the assumption easier to attack, which is the point.

## Verification

- **URLs fetched, both on 2026-09-16:**
  - https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf — retrieved with `curl -sSL` in the sandbox (the fetch service refuses `cdn.sanity.io`; `curl` was used from the start): HTTP 200, 2,419,969 bytes, 17 pages, PDF 1.7, Adobe InDesign 21.2 (Macintosh), `/CreationDate` 2026-03-09 22:15:06 UTC. Text extracted with `pdftotext` twice (default reading order and `-layout`) and read in full, including all eleven footnotes and the reference list. **This is the document of record and is the source for every quotation in this file unless a quotation is explicitly marked as web-page text.**
  - https://www.anthropic.com/research/labor-market-impacts — retrieved with `curl -sSL`, HTTP 200, 247,543 bytes; scripts and styles stripped and the full rendered text read, including the Corrections block, all ten page footnotes and the references. Used to establish how the page differs from the PDF, to confirm the footnote renumbering and the orphan marker, and to check every quotation against a clean text layer.
- **Typography and links.** Font family, size and colour for every text run were read with `pdftohtml -xml` on pages 1–14; this is the basis for the statements that the body is serif 17 pt, headings sans 23 pt, captions sans 12 pt with a black title and a grey (#414042) gloss, that there is no bold in the document, and that italic occurs exactly twice in the body. Hyperlink targets were read from the same extraction (`pypdf`'s annotation walk failed on this file with `TypeError: 'IndirectObject' object is not iterable`; `pdftohtml` supplied the hrefs instead). Web-page emphasis and metadata were read from the HTML source.
- **Fetch date:** 2026-09-16. **Fetch failures:** none; both documents returned complete on the first attempt.
- **Not fetched, deliberately:** the appendix PDF (`e5f77fc0…`, its own corpus slug); the earlier PDF build (`a42bc3fc…`, identified in `wiki/INDEX.md` Standing notes 4 as the same document); the Hugging Face dataset and its two files; the O\*NET database; the BLS projections table; the EIG crosswalk page; and every work in the reference list. Nothing from any of them is quoted or characterised here. Where this file compares the paper to other entries in the corpus it points at `wiki/style/economic-index-2026-03-report.md` and `wiki/style/coding-agents-social-sciences-2026-05.md` and quotes neither.
- **Every quotation was checked back against the extracted PDF text word by word after transcription**, and again against the web page's text where the two agree. Confirmed for all nine sections of this file.
- **Quotation caveats.**
  - Hyperlink URLs were stripped from quoted prose and the anchor text retained; the full link inventory of the PDF is in `## Source`.
  - Typographic apostrophes and quotation marks were normalised to ASCII when quoting inline; en dashes and em dashes are reproduced as the PDF sets them, and the two places where the web page uses a different dash are recorded in `## Source`.
  - **PDF line-break artefacts were repaired.** The extraction joins words the PDF breaks across lines without a hyphen: "AIexposed", "workrelated". Quotations here restore the intended spacing; the web page's text confirms both.
  - Footnote markers are given in square brackets, e.g. "[9]", and the numbering is **the PDF's**; the web page's numbering runs one lower from footnote 8 onward. One quotation retains a source typo, footnote 9's "In ni extension", which the web page renders as "In no extension".
  - The stray superscript "¹" on p.10 is quoted in `## Limitations` as it appears and identified as an orphan marker, not corrected.
  - Emphasis is reproduced as the PDF sets it: caption titles with no terminal period, the two italicised body terms, the key-findings bullets without terminal periods.
  - **Figure images and chart values, per `room/director-2026-09-16-caption-amendment.md` and `room/director-2026-09-16-figure-values-ruling.md`.** The sans-set block under each exhibit is the caption and is quoted as such. All seven figures are images in both renderings and carry empty alt text on the web page, so **no number read off a chart image is recorded anywhere in this file** — in particular, the seven unnamed occupations and their coverage values in Figure 3, every row of Figure 5, and every series value in Figures 1, 2, 4, 6 and 7. Every number quoted here appears in the PDF's body prose, its footnotes, or a caption.
- **Scope.** This file annotates how the paper is written: its section order, the grammar of its findings and caveats, how its comparisons are phrased, its caption template, where its limitations sit and how it closes. It makes no judgement about whether any finding is correct. Where it says a caveat is misplaced, a number is unsupported in prose, a unit switches or a label is inexact, that is a statement about the writing, not about the analysis. The paper's claims, definitions and open questions are recorded in the sibling file `wiki/reports/labor-market-impacts-2026-03.md`.
