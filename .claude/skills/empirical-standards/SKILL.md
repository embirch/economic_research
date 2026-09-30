---
name: empirical-standards
description: Current gender-and-AI project procedure for empirical-standards; read PROJECT.md first.
---

# Empirical standards

Use the methods the question and data support. Descriptive studies need defined estimands, transparent comparisons and limitations; formal hypotheses, p-values and power calculations are not universal requirements.

1. Preserve source versions, retrieval/fieldwork dates, licences and checksums; never mutate raw inputs.
2. Verify population, unit, denominator, gender measure, routing, weights, flags and missingness. Name the actual survey or platform.
3. Record prior inspection and a dated plan; log changes. A plan after inspection is not untouched preregistration.
4. Build meaningful checks for source integrity, keys, ranges, denominators, joins and transformations. Stop on failure. Independently re-derive important claims.
5. Use design-appropriate uncertainty. Do not invent intervals from published aggregate cells, total sample counts or unspecified privacy noise. Assumption-based sensitivity scenarios are not verified sampling uncertainty.
6. Non-significance is not evidence of absence. MDE is a planning quantity under specified assumptions, not an upper confidence bound or a threshold for rejecting a hypothesis. Evidence of equivalence requires an appropriate prespecified design and interval.
7. For applicable models, inspect specification, identification, multiplicity and sensitivity; test recovery with known simulated processes where informative. A realised zero estimate is not required under a simulated null.
8. Keep measured outcomes, associations and causal claims distinct. Occupational exposure is not job loss; use is not benefit; unrelated samples do not trace a causal pathway.
9. Store derived results and provenance with stable IDs; manuscripts and dashboards should reuse these outputs. External contextual statistics require verified citations rather than being mistaken for own estimates.
10. Match checks to the actual risks. Do not run redundant tests or add complexity for appearances. Preserve inconclusive results, female advantages and explicit data gaps.
