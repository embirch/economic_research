---
name: anthropic-style
description: How Anthropic's economics research is structured and written, derived from the 23-file style corpus in wiki/style/. Read before drafting any POST.md, any figure caption, any limitations section or any close; read again before the referee's draft review. The full reference is wiki/style/STYLE-GUIDE.md.
---

# Anthropic style

Derived from `wiki/style/` (23 publications annotated for section order, opening moves, findings and their caveats, comparisons, captions, limitations and closes) and from `wiki/style/STYLE-GUIDE.md`, which carries the evidence for everything below. **Before drafting, re-read the three corpus files closest to the post in hand** — not this list. The closest three are usually: the Economic Index wave report nearest your data (`economic-index-2025-09-report` for a geographic or two-surface cut, `-2026-01-report` for a constructed measure, `-2026-06-report` for survey plus usage), plus `economic-index-2025-04-software-development` for a one-cut post and `labor-market-impacts-2026-03` for a post whose finding may be a null.

## Structure

Use `team/templates/POST.md`. It matches the corpus with one addition and one subtraction, both deliberate:

- **Limitations gets its own top-level section, between the last finding and the close.** The corpus's best placement (`economic-index-2025-04-software-development`); every report from September 2025 onward disperses its caveats and every one of those files calls that a fault: "**A caveat a skimmer cannot find is a caveat addressed to referees only.**" Keep the finding-level and number-level caveats adjacent to their findings *as well* — "the right lesson is to do both, not to choose."
- **No summary block.** The corpus shows the cost four times: a summary that says 13% where the body says 23.8%; a "40% more likely" that exists only in the summary; "about 25%" against a body's 27%; three published compressions of one result that disagree. Test: **if the close can stand as the summary, the summary block was never load-bearing.**

Rules the corpus keeps:

- **Findings in pre-registration order, each stated once in the body with its figure.** Where the piece has more than five findings, the headings are the navigation and each evidence block ends in a named summary sentence (`worker-retraining-2026-08`).
- **Every number arrives with its instrument attached.** Define at point of use; the construct's definition sits in the paragraph before its first number, so "no number can be quoted from this paper without passing the paragraph that defines it" (`claude-code-expertise-2026-06`).
- **Precision coarsens upward and never changes unit.** Coarse in the opening, exact in the body. Changing the *unit* at the top so the headline reads largest is a named fault (`economic-index-2026-03-report`).
- **Nothing new in the close.** No number, no construct, no occupation that the body has not already carried.
- **Headings.** Either the finding as a sentence with the qualifier inside it — "Coding agent users are posting more working papers … **but not submitting more to journals**" (`coding-agents-social-sciences-2026-05`) — or the question the section answers (`economic-index-2025-04-software-development`'s how/what/who ladder). A heading that asserts is a quantitative claim and maps to `results.json` like any sentence.

## Register

**No first person.** The corpus is written in the first person plural; it also supplies the substitutes, which are better than a bare passive:
- attribute to the exhibit — "Figure 2.7 suggests that…", "The plot shows that long-tenure users are about 5 percentage points more likely…";
- attribute to the analysis — "These results suggest…", "This control moderates the effect somewhat";
- attribute to the instrument — "Claude estimates that…", "Our classifier identified 93% of…";
- put the measure in subject position — "the task value estimator reaches…";
- passive with the definition named, not the definer — "A respondent was coded as indicating job threat if…".

Two constructions do not survive deletion, so rebuild rather than de-personalise: the institutional promise (attribute it to the series or to the reproduction section) and opinion ("we think X might overstate" → state the direction of the bias without a believer).

**Hedge ladder, in descending confidence:** *the data shows · we see→the exhibit shows · reveals · indicates · implies · suggests · appears to · tends to · is associated with · may reflect · could reflect · likely · perhaps · the message is unclear · considerable uncertainty remains.* Never *shows*, *proves*, *demonstrates* or *causes* of a causal claim. One rung per claim. The only licensed bare causal verb is decomposition: "This is caused, **mechanically**, by a rise in personal queries" (`economic-index-2026-03-report`).

**Attribution is not a hedge.** "Claude estimates", "coded using Claude", "being labeled as", "respondents reported" name the instrument. A sentence can be fully confident and still take one. For self-reports, use a speech verb instead of a hedge: "One fifth of the respondents in our survey **voiced concern**" (`survey-81k-economics-2026-04`).

**Naming.** The question, the title, the stakes and the recommendation say **AI**; the sample, the index, every number and every caption say **Claude**. A construct's *name* may say AI if its measurement says Claude — "Effective AI coverage tracks the share of a worker's time-weighted duties that AI could successfully perform, **based on Claude.ai data**". The model pair:

> "The coverage shows **AI** is far from reaching its theoretical capabilities. For instance, **Claude** currently covers just 33% of all tasks in the Computer & Math category." — `labor-market-impacts-2026-03`

The corpus breaks this rule in exactly three places — the summary, the caption and the close — so check those three.

**Conventions.** Approximate quantities in words, measured ones in numerals. Counts, not percentages, below about thirty observations. The n travels with the label, not with the exhibit ("**AI Delegation (n=4)**"). One quantity, one noun, everywhere including legends. Within a paragraph, one unit; where the unit changes, say so in the same sentence. A slope in decision units ("for every additional \$10 of hourly wage … 1.5 percentage points"). Never "significant" without a stated test. Never a magnitude word as the whole of a finding.

## Openings

Pick one move and commit to it. The four available to us, in order of fit:

1. **Anthropic's own published number, turned into a question.** "In an observational study of Claude.ai data, we found AI can speed up some tasks by 80%. But does this increased productivity come with trade-offs?" (`skill-formation-rct-2026-01`) — "cheaper and stronger than any framing that starts from the world."
2. **The admitted blind spot in the Index.** "*X* shows A and B. To date, however, we've lacked information on how A and B map onto C." (`survey-81k-economics-2026-04`). Or in two bolded nouns: "We've captured the **breadth** of uses … but not their **depth**", then one worked case where the missing distinction decides the answer (`productivity-gains-2025-11`).
3. **The gap made specific by enumeration.** Name the existing approaches, then the one property none of them has: "Existing methodologies—whether developing predictive models …, conducting controlled studies …, or administering periodic surveys of users—cannot track the dynamic relationship between advancing AI capabilities and their direct, real-world use" (`economic-index-2025-02-paper`).
4. **Concede the objection, then elevate** — for a narrow population. "Jobs that involve computer programming are a small sector of the modern economy, but an influential one." (`economic-index-2025-04-software-development`). Its close discharges it exactly.

Every opening in the corpus also does these, and so must ours:

- **Stakes before the first own-number.** The corpus waits 150–600 words. Where an external number poses the puzzle, use it ("40% of employees report using AI at work, up from 20% in 2023").
- **The hypotheses as a disjunction, with the outcomes numbered in the same order in the next sentence.** "Does AI provide a shortcut to *both* skill development and increased efficiency? Or do productivity increases from AI assistance undermine skill development?" then "we examined 1) … and 2) …" (`skill-formation-rct-2026-01`). This is the template's "how to tell the explanations apart", in prose.
- **State the two-sidedness before any finding**, where the answer is two-sided.
- **Grade your own evidence in the sentence that states the headline** — "provide initial evidence that … is correlated with".
- **Concede the external-validity problem in the opening, not the limitations**, where it is the first thing a reader will think of.
- **Pose the question larger than the design and disqualify it in the same paragraph** — "While we don't have full answers to these questions yet, we look to Claude Code usage data for early signals."
- **Claim novelty for the vantage point, never for the finding.**

## Findings with their caveats

The finding sentence:

- **The fence inside the clause carrying the number, between the superlative and its subject** — "the largest adoption of AI **in our dataset**".
- **The unit named in the units actually measured** — "37.2% **of queries sent to Claude**", not "of AI use". "79% of conversations involved **some form of** automation" — three fences in eleven words.
- **The magnitude characterised before it is quantified** — "a slight lean towards augmentation, with 57% … and 43% …". Only safe if both numbers follow immediately.
- **Both halves of a partition, or the residual named.** If the shares do not sum, say what is in the remainder.
- **Level pair, then ratio, each labelled, comparison group inside the sentence** — "around a quarter of a paper more … In percentage terms, around 10% (empirical projects started) to 75% (working papers posted) more productive than others in their discipline and career stage."
- **The baseline in the same sentence as the headline** — "increased employment by 1.7 percentage points, compared to a baseline employment rate of 63% in the control group."
- **Significance and size in two paragraphs, never one.** "If 'work' means … to a statistically significant degree, then job training has worked in the US. … However, the average training program does not make a big difference." (`worker-retraining-2026-08`) — the corpus's single most copyable passage.

Caveat placement, three layers:
- **number-level → a footnote at the number, with the direction of bias**;
- **finding-level → a preamble at the head of the finding, which ranks it against the others** ("We therefore treat these findings as more preliminary than the ones described above");
- **design-level → the Limitations section.**

Always **upstream of the exhibit, not downstream**; always **inside the definition** where the awkward fact belongs to the variable ("the age of the user's account — days since signup with Anthropic, not with Claude Code specifically"); **before the interpretation** in a sentence-opening subordinate clause ("Though not adjusted for population, …").

Prefer the caveat that **states an absence**: "We do not observe people who signed up a year ago but are no longer using Claude." And the construct **fenced by two counterexamples** rather than by a caveat: "A senior engineer asking their first Rust question is a beginner at Rust. An accountant who has never used Python, but tells Claude exactly which reconciliation rules a Python script must enforce … is an expert at that task."

Nulls:
- Give the sign and disown it — "has increased slightly but the effect is indistinguishable from zero."
- Or state the two-sided failure to exclude — "do not conclusively find a speed up or slow down."
- Supply the positive alternative, or two competing explanations, so the null is a finding about what the design cannot separate.
- **An MDE beside every null, as a scenario a reader can judge** (`labor-market-impacts-2026-03`): state the detectable difference in the outcome's unit, date it, name a scenario with a historical precedent, do the arithmetic, and say whether the design would see it. The corpus's largest gap; our rule.

Interpretive furniture: concede the expected part first ("Unsurprisingly", "While computer and mathematical tasks still dominate at 36%"); report the component that moves the other way in its own sentence ("One change goes ostensibly in the opposite direction"); give the confirming and disconfirming example equal space and identical grammar; state the fork and leave it open; name the rival explanation in the reader's voice and hedge the verb of the remedy ("we **partially** address this worry by comparing sessions doing the same kind of work, at the same estimated value, in the same month …"); state the falsification condition before the result ("We would only observe a positive coefficient if …"); check a conjecture on the spot where the data allow, and report the check whichever way it comes out.

**One claim at more than one level beats six claims at one.** Test it at two grains, on two samples, or with a second measure chosen because the first cannot settle the question — and where the levels disagree, **report the disagreement as the result**.

## Comparisons

The comparison is the finding. Baselines available: the previous wave named as a document or by calendar month; the index's null value; workforce or employment share; official statistics with the release named and the survey question quoted; the other platform; a clean out-of-event period; each series' own average; the control arm's level; the paper's own unadjusted estimate.

- Both levels, matched rounding, the same direction word through a run.
- The comparator in a parenthesis, so each sentence carries its own comparison — and **a difference reported in its units, with both levels given**.
- **Give the value that would be unremarkable before the estimate** (AUI = 1, Zipf's −1, σ = 1, the 45-degree line, the base rate a deviation chart needs).
- Slope and fit reported separately, and allowed to point opposite ways.
- To compare with a published number: **re-cut to the other study's threshold and put both thresholds in the sentence.**
- Report overlap with prior work as a count of shared units, not as a characterisation.
- Name how your measure differs from the Anthropic measure nearest it, before using yours.
- Corroboration is agreement in direction — *is consistent with*, *echoes*, *converges with*, *also favored* — never confirmation.
- State a structural confound as a property of the data before any number ("the API data we analyze is limited to single input-output pairs").
- Publish the control-side levels next to the effects, where the groups were not assigned.
- Name each column of a controls table by the alternative it kills: "First, that expert-rated users pick different kinds of work (column 2), work in different months (3) …".

Revising a published claim — four forms, four grammars: **revised** (separate trend from level: "the August spike overstated how quickly it was materializing"); **retracted** (name it as a hypothesis, supply the replacement in the same sentence: "This pushes back against a hypothesis we made last year … instead, we find…"); **superseded** (the old measure is incomplete, and in what respect); **re-estimated** (reproduce first, then let the critique move the number down). And: reconcile two of your own numbers unprompted; name a tension with an earlier Anthropic finding, locate it in the design, state the reconciliation as a conjecture, refuse to close it.

## Captions

The caption is the emphasised sentence(s) directly under the image. Bold title, then roman gloss. Title declarative where there is a finding, descriptive where there is not; **if the finding is noisy or conditional, the hedge goes in the title**.

Gloss order, as applicable: what is plotted, in what unit · **the unit of analysis, named** ("Each point is an occupation") · how the index or share was constructed, **restated in full, not cross-referenced** · the sample, the coverage boundary and the inclusion floor **with its reason** · panel logic · what colour, size and marker encode · the weighting **and its purpose** · imputation and censoring rules · the residual category · the full control set enumerated · what every line and mark is, and the estimator behind a fitted line · the uncertainty, its coverage and its clustering unit · the null value with the familiar number attached · the coefficient in plain words with "associated with" · the exclusion, verbatim in every caption it governs · where the full version lives.

Also: definitions in the caption where the figure carries a taxonomy; the coding rule of a classifier outcome with the model in a closing parenthesis ("coded using Claude"); **fence the grouping variable, not only the outcome** ("Both fields are inferred…"); the conditional base first, as a subordinate clause ("Among respondents who named a beneficiary…, the share identifying each destination"); the instrument quoted where the instrument is the measurement; one cell read aloud where the exhibit's grammar is unusual; **disclose what the exhibit is not** and **what was not adjusted for**; say whether a multi-label classifier lets a unit appear twice; **provenance verbs** — *Copied from* / *Based on* / *Reproduced from* / *Adapted from* — and what was added to a borrowed figure; sibling exhibits to one caption template; **the n**, which no piece in the corpus states and every file marks as missing.

A caption never states: a relationship the prose has not stated with its number; a universal; a significance family in one clause; a version vaguer than the exhibit; a mark the legend calls something else. **No sentence in the post may depend on a number that appears only inside an image.** One title per exhibit.

Tables: two-level row grouping, direction by glyph and sign, units in the row label, significance of every row in one sentence with the exception named, the group definition repeated rather than cross-referenced, absences explained ("Novice is the reference category, so its coefficient is not defined"), and a derived measure published three ways — prose, the expression the script implements, and one worked case.

## Limitations

Its own section, after the last finding, before the close; the referee's first questions first.

- **Framing sentence: three to six words.** "These findings are preliminary." / "There are some caveats worth naming." Or derive the limitation from the design's virtue, which replaces the ritual sentence: "Our analysis is grounded in real-world AI use… Although this approach gives our findings practical relevance, it also brings inherent limitations." Never "as with all studies"; never "these include".
- **Ordering: outward from the data to the world, strongest last, ranked by severity.** Label each by its dimension in two words, then the concession, then the study or analysis that would fix it.
- **Sign every limitation.** Which way does it push the estimate? Where both directions are live, give both with a mechanism each and grade them by modality ("could either understate … and possibly overstate it, if …"). A list where every item cuts the same way is an apology.
- **At least one limitation must withdraw a claim** — name the sentence the post is not entitled to write. "We only studied what developers delegate to AI—not how they ultimately use AI outputs in their codebase, the quality of the resulting code, or whether these interactions effectively improved productivity."
- **Best form: name the threshold at which the conclusion flips.** "Without that persistence, they would have a benefit-cost ratio under 1." (`worker-retraining-2026-08`).
- **Where a threat is answered, report the cost**: the discrepancy, the loss of precision, the specification that fails. Where it is not, say so in the same breath ("We can't rule this out entirely, but…"; "the key gradients **that we can measure** are similar"). Never "we ran robustness checks and believe…".
- **Every robustness claim points at a table in the drawer.** "Results are similar however we define X" with no alternative and no number is an assertion.
- **Convert a measurement limitation into an operating rule** where you can: "we generally use these task value estimates ordinally rather than … to get aggregate task values."

## Close

- **No numbers.** Corpus-wide invariant across thirteen files. Nothing new — no number, no construct, no occupation.
- **Every paragraph opens on the world or the method, not on the post.**
- **Restate what was learned in words, with every hedge intact.** Read the close's adjectives against the body's and check that none has been upgraded; check that every fence — including the *unit* of the construct — survives.
- **Compress several findings by holding the subject fixed and varying the predicate.** "People in higher-income countries are more likely to use Claude, more likely to seek collaboration rather than automation, and more likely to pursue a breadth of uses beyond coding."
- **Why it matters as a conditional with its antecedent named, and the modal kept**, ideally with the evidence for the antecedent graded: "**If** AI automation improves the productivity of workers with tacit organizational knowledge—**as some of our evidence suggests**—then…". Ending on a tension rather than a direction is harder to misquote.
- **Argue against your own extrapolation**, or restate the limitation of your own central measure, or invert honestly if the inversion is true.
- **What comes next: name the number that would have to move, in which direction, and what that would mean.** "if the returns to expertise begin to decrease over time, that would suggest that models are starting to supply the essential judgment that users currently bring." Commit rather than delegate.
- **Recommendations to Anthropic: who acts, what they do, and the circumstance in which it would not work.** One recommendation traceable to one number beats a list; negative framing corrects a specific prior ("expanding access alone will not suffice"); the product form states what the product should achieve in the study's own terms, without naming a feature. Never offer an Anthropic programme as the response to your own finding.
- **The title matches the ending.** The ending must contain the title's key word doing work; a title may not carry a word the findings do not test. If the title names a finding, the close ends on that finding's consequence.
- **Drop the weakest result rather than repeat its hedge.**

## Methods, reproduction, assistance disclosure

- Define the sample **in the post**: window to the day, counts, the unit of observation with its consequence, the exclusions enumerated, the privacy thresholds as numbers.
- Introduce a constructed measure in four moves: name it as coined, gloss it by count and purpose, enumerate its members, and **state the derivation in the defining sentence** ("which we generate by asking Claude specific questions about anonymized transcripts").
- Bound it in the same place: "confident in X, not in Y, here is an instance of each", and name the validation not done.
- Write your own hidden assumptions out — "this approach implicitly assumes…"; label the conservative choice as you make it; disclose and justify any deviation from a source's parameter.
- Justify a threshold by converting it into the units of the phenomenon. Show a built measure working on one case where the naive alternative fails. State the units of an index by giving the two extreme readings of one difference.
- **What was set in advance** reads like the pilot-discount-registered-assumption-realised-effect paragraph in `skill-formation-rct-2026-01`; write the assumptions sweep as questions in the researchers' own voice.
- **Reproduction** goes above the back matter, not in it.
- **Assistance disclosure** names what Claude was asked to produce and what was done to catch it being wrong (the reasoning table, the adversarial re-read against sources, the spot-checks) — not boilerplate.
- An appendix or a methodology section may end without a close. **A post may not.**

## Pre-submission checklist

1. Every quantitative sentence maps to one entry in `results.json`, and `notes/claims-map.json` records the mapping. Same entry quoted identically everywhere — prose, caption, heading, table, close.
2. No number, construct, occupation or claim appears for the first time in the close. No number appears only in a caption, an image or an alt string.
3. Every null carries its MDE as a scenario. Every geographic or small-cell claim carries its noise check. Every interval carries its coverage and its clustering unit.
4. One unit and one denominator noun throughout; every switch marked in the sentence that makes it.
5. Every finding sentence: unit in the clause, fence inside the clause, magnitude characterised before it is quantified, both levels of any difference, the comparison group named.
6. Every caveat in its layer — number-level at the number with its direction, finding-level at the head of the finding, design-level in Limitations — and every one of them signed.
7. At least one limitation withdraws a claim; at least one names the threshold at which a conclusion flips; the list is ranked and the strongest is last.
8. Every robustness claim points at a table in a drawer and reports what the check cost.
9. Every caption: sample, unit of analysis, construct, floor with its reason, the null, the estimator, the n, and the coefficient where there is one. One title per exhibit. No caption claims what the prose has not.
10. Naming: the question, title, stakes and recommendations say AI; every sample, index, number and caption says Claude. Check the close and the captions specifically — those are where the corpus itself drifts.
11. No first person anywhere. No summary block. No "significant" without a test. No superlative on a finding. No mechanism without a marker.
12. Nothing `notes/claims.md` forbids appears anywhere, including captions, headings and the close.
13. The title contains no word the findings do not test, and the ending uses the title's key word doing work.
14. Recommendations name an actor, an action and the circumstance in which they would not work. No Anthropic programme is offered as the response.
15. The page build passes: every number on the page is in `results.json`. Fix the text, never the numbers.

## The section order

`team/templates/POST.md`, twelve sections: the puzzle Anthropic left open · how to tell the explanations apart · one heading per finding, each with its figure · what this means · recommendations to Anthropic · limitations · methodology · what was set in advance · reproduction · assistance disclosure. Four of these were added after the corpus was read (`room/director-2026-09-16-criteria-answer.md`): recommendations, what was set in advance, reproduction and assistance disclosure now have headings of their own rather than sitting inside Methodology, because the criteria require each of them and a clause inside a methods gloss is not a section a referee can test. Methodology keeps the data, the measures verbatim, the models and the stress tests; the pre-registration, the assumed effect with its provenance and the deviation log go under "what was set in advance".
