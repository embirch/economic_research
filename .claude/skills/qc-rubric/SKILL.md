---
name: qc-rubric
description: The referee's checklist and verdict format for the four review points (brief, pre-registration, results, draft), including the assumptions sweep. Read before any review.
---

# Referee rubric

Use templates/VERDICT.md. Verdicts are PASS, PASS WITH CHANGES, or BLOCK. Be specific: file, section, what to change.

## At the brief
- **Assumptions sweep**, four items, each handled / newly flagged / needs a design change: (1) value judgement embedded in the framing; (2) construct mapping against Anthropic's verbatim definition (what the measure measures; which direction the sign could run); (3) composition or selection: who the users are in each unit, what mix could produce the pattern without the mechanism, whether occupation is inferred from tasks; (4) Anthropic's own results that cut against or bound the framing, quoted.
- Does each hypothesis have a signature that its rivals do not share, and a stated counter-result?
- Is the contribution stated for both outcomes? Can the closing section be imagined?
- Is any framing inherited rather than derived? Is the why-it-matters something an economist would care about?

## At the pre-registration
- Can every rule fail? Is its expected MDE stated and informative? Are collinear predictors, residual-on-covariate designs, small cells and flagged units handled by the rule rather than discovered later?
- Is the sample rule, exclusion list and error type fixed? Is "what has been seen" disclosed?

## At the results
- Re-derive three headline numbers from raw files with your own code (notes/rederivation/), and report match or cause of discrepancy.
- Judge every logged deviation: legitimate, or a rule rewritten to fit?
- Count the tests actually run against those registered; note multiple-testing exposure.
- Write the red-team memo (templates/RED-TEAM.md) and the claims list (templates/CLAIMS.md), including the strongest title and opening claim the evidence supports.

## At the draft
- Every quantitative sentence maps to results.json (check the claims map); no number appears that is not there.
- Title and opening claim no stronger than the claims list.
- Limitations name what you would raise first; caveats sit in the same paragraph as their findings.
- Register: questions about AI, findings about Claude; no first person; no summary block; figures captioned in Anthropic's style.
- Nothing forbidden by the claims list appears anywhere, including captions and the site card.
