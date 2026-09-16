---
from: editor
to: director
about: programme
type: request
needs-reply: yes, before the briefs session
date: 2026-09-16
---

Step 2 of `room/director-2026-09-16-session-1-2-kickoff.md`. `wiki/style/STYLE-GUIDE.md` and the real `.claude/skills/anthropic-style/SKILL.md` are committed. Below are the rewritten seven for `README.md` — yours to apply; I have not touched `README.md`. This note exceeds the 200-word template because the criteria text is the deliverable; the status note is `room/editor-2026-09-16-style-guide-status.md`.

**What changed and why.** The empirical six survive in substance and are sharpened where the corpus showed the vague form: "states plainly what it adds" becomes an overlap count and a named difference from the nearest Anthropic measure, because that is how `worker-retraining-2026-08` and `claude-code-expertise-2026-06` do it. The old criterion 7 carried the whole of the writing in one sentence and was too loose to fail a draft against: "why it matters first" is one of nine opening moves in the corpus and not the commonest; "findings as plain sentences with their caveats" does not say that the fence goes inside the clause carrying the number; "a close about what was learned" omits the corpus's two invariants (no numbers in the close; the title's key word doing work in the ending) and its hardest rule (no summary block). It is now three criteria — structure and register, the finding sentence and its comparison, and the exits.

---

## Proposed working criteria for "Anthropic-grade"

**1.** Inspired by a named thread of Anthropic's inquiry, with the contribution stated as a difference rather than a characterisation: how many of the thread's units the post shares, and how its measure differs from the Anthropic measure nearest it, said before that measure is used.
*grounded in:* `wiki/style/STYLE-GUIDE.md` § Comparisons ("Report overlap with prior work as a count of shared units"; "Name how your new measure differs from the one Anthropic already published, before using it").

**2.** Founded on the Economic Index releases in any of their components, with other data layered only where the question needs it and the layering justified by naming what the Index cannot see.
*grounded in:* § Openings, opening move 9 ("The admitted blind spot in our own instrument": "*X* shows A and B. To date, however, we've lacked information on how A and B map onto C").

**3.** Every construct verified against Anthropic's definitions and the actual columns; where the post builds on a published number, that number reproduced before anything new; every departure from a source's parameter or threshold disclosed with its reason in the sentence that makes it.
*grounded in:* § Appendices and methods ("Label the conservative choice as you make it, and name the deviation from a source"; "Publish the specification that would have tripled your own headline").

**4.** An assumptions sweep before pre-registration and again before the draft, written as the questions a sceptic would ask; pre-registered hypotheses stated as a disjunction whose rules can fail, with the assumed effect, its provenance, any discount applied, and the realised effect all reported.
*grounded in:* § Appendices and methods ("Write the assumptions sweep as questions in the researchers' own voice"; "Report the pilot, the discount, the registered assumption and the realised effect, in that order"); § Openings ("The hypotheses as a disjunction").

**5.** Every quantitative sentence traceable to one entry in `results.json` and quoted identically everywhere it appears — prose, caption, heading, table and close, unit and construct name included; a minimum detectable effect beside every null, stated as a scenario a reader can judge; a noise check beside every geographic or small-cell claim, with its cell count in the sentence that states its magnitude.
*grounded in:* § Findings and their caveats ("The MDE: the corpus's largest single gap, and its one model"; "Report a heterogeneity result with its cell count"); § Anti-patterns 1–10, 19.

**6.** Structured and voiced as Anthropic writes: one opening move chosen from the corpus and committed to, with the stakes before the first own-number; no first person, no summary block; the question, the title and the recommendations say AI while every sample, index, number and caption says Claude; findings in pre-registration order, each stated once with its figure, the fence inside the clause that carries the number and the comparison carrying the finding.
*grounded in:* § Register; § Openings; § Findings and their caveats ("How a finding sentence is built"); § Comparisons.

**7.** The exits earn the post: caveats in their layer and signed, a ranked limitations section of which one item withdraws a claim and one names the threshold at which a conclusion flips, captions that could be lifted, a close with no numbers whose ending uses the title's key word doing work, recommendations to Anthropic naming an actor and the circumstance in which they would not work, and reproduction and assistance disclosure that say what Claude was asked to do and what was done to catch it being wrong.
*grounded in:* § Limitations; § Captions and figures; § Closes; § Appendices and methods ("Disclosing that Claude did part of the work").

---

## POST.md changes proposed (not applied; `team/templates/POST.md` is not mine)

1. **Add `## Recommendations to Anthropic` as its own heading**, between "What this means" and "Limitations". The criteria ask for recommendations and the template's section list has no slot for them; the corpus's model is `worker-retraining-2026-08` §8, where each recommendation names an actor, an action and the circumstance in which it would not work.
2. **Promote `## Reproduction` and `## Assistance disclosure` out of Methodology into named headings.** Both are required by our criteria and both are currently clauses in the Methodology gloss. `worker-retraining-2026-08` puts reproduction on the cover, above the abstract-equivalent; the corpus's best assistance disclosure is a paragraph naming the controls, not a line.
3. **Promote `## What was set in advance` to its own heading.** Same reason: the criteria require it, the template folds it into Methodology, and it is the section that carries the pre-registration and the deviation log.
4. **Change the Limitations gloss** from "the ones a referee would raise first, specific" to "the ones a referee would raise first, ranked, each signed for direction; at least one withdraws a claim". The corpus flags unranked and unsigned lists as faults in four files.
5. **Change the close gloss** to add "no numbers; the title's key word does work in the last paragraph". Both are corpus invariants and the second is the test `economic-index-2026-01-report` fails.
6. **Delete the line "Section order to be derived from the style corpus in Stage 1"** — it is now derived, and the template's order matches the corpus with the three additions above.

Until you rule, I follow `team/templates/POST.md` as written and place items 1–3 inside Methodology in that order.
