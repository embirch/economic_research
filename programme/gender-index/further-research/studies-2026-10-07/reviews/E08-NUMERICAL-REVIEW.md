# E08 independent numerical verification

**Verdict: pass.** Independently reconstructed the analysis from the pinned analytical SAS file and its 1,000 public bootstrap weight vectors. All 776 comparisons pass; the largest absolute numerical discrepancy is 2.84×10⁻¹⁴. No unresolved numerical or release-layer error was found. The failed age-saturated target remains failed rather than being converted into an estimate with valid uncertainty.

This review did not read or review manuscript prose. It is a numerical audit, not editorial or external human peer review. No E08 production file was edited. Spending: $0.

## Independent implementation and execution

[e08-independent.py](e08-independent.py) sorts and joins both files by their unique complete PUMFID keys, reconstructs the employee target and outcomes, and uses replicate-wise weighted `bincount` tables for ratios and common-composition estimates. It imports no production or pilot helper. The production code was read to identify the exact specified output targets, not called as the reviewer estimator.

Additive adjustment is independently computed with weighted QR/SVD least squares after collapsing identical design patterns, instead of the producer's batched normal-equation solve. The 2,694 observed design patterns produce rank 25 in the full-weight fit and all 1,000 replicate fits. Maximum scaled normal-equation residual is 1.36×10⁻¹⁵. All coefficients, full covariance matrices and interaction estimates match the production results.

Executed from the repository root:

```sh
python programme/gender-index/further-research/studies-2026-10-07/reviews/e08-independent.py --cache data/cache/selected-studies/E08 --study programme/gender-index/further-research/studies-2026-10-07/E08
```

The machine-readable [review result](e08-independent.json) records source verification, code and production hashes, numerical errors, target support, failed replicate numbers, and public release checks. It contains only safe aggregate review information. No raw survey record or bootstrap weight is saved.

## Numerical findings

The whole-file benchmark and all four raw cells for both outcomes reproduce. Full five-category unpaid-work and four-category time-off distributions match, as do their covariance-derived contrasts. All 1,000 replicates use the shared weight vector for the four groups. Variance is centred on the full-weight estimate and divided by 1,000. The eight prespecified pointwise percentile sensitivities use linear interpolation and match both internal and rounded public values.

| Frequent unpaid-work interaction target | Women+ minus Men+ user-minus-nonuser difference, pp | Bootstrap SE, pp |
|---|---:|---:|
| Raw, all employees | 3.3979 | 1.5020 |
| Additive projection | 2.6884 | 1.4751 |
| Common occupation/sector composition | −1.7242 | 1.7529 |
| Raw on occupation/sector/education common support | 3.3537 | 1.5031 |
| Common occupation/sector/education composition | −0.9653 | 1.7809 |

Occupation/sector uses 16 common cells and retains all 20,538 employees, so its restriction component is exactly zero. Its frequent-work composition change is −5.1221 pp. Occupation/sector/education uses 44 common cells and retains 20,413 employees. For frequent work, its support restriction changes the interaction by −0.0441 pp and standardising the retained sample changes it by −4.3191 pp. Both components, the exact decomposition and the complete joint covariance reproduce for both outcomes. These are different descriptive targets, not corrections identifying one causal interaction.

The target mix was recomputed in every replicate, rather than fixed at the point-weight mix. Maximum cell-share changes are 0.01257 for occupation/sector and 0.01198 after education. All required denominators in those two targets are positive in every replicate.

The age-saturated diagnostic retains 17,665 employees across 143 observed common cells. It reproduces two zero cell denominators, in replicates **465 and 480**. Standardised uncertainty is accordingly undefined; no failed replicate is discarded. Its same-support raw estimates remain calculable, but they do not rescue the saturated standardised target.

## Quality, rounding and suppression

All 101 public table rows were checked against independently reconstructed aggregates. Displayed values and interval endpoints use one-decimal percent or percentage-point rounding. Every figure row matches this safe rounded layer. No fine standardisation cell estimate is released.

- `difficult.distribution.1.4`, Men+ users reporting **very difficult**, is F-quality and suppressed.
- Its paired **difficult** category, `difficult.distribution.1.3`, is also suppressed so that the combined difficult/very-difficult rate cannot reveal the F cell by subtraction. That companion row is E-quality but has no displayed estimate; its note correctly explains suppression rather than displaying an E-warning estimate.
- All displayed E-quality rows carry warnings: both Men+ daily unpaid-work shares and the Women+ user very-difficult share.
- All eight percentile sensitivity rows are A-quality, were checked, and do not replace the primary normal-approximation contrast intervals.

An initial reviewer assertion applied the displayed-E warning requirement to the suppressed E companion row. Inspection showed this was a reviewer-test error; the check was corrected to apply only to displayed estimates. No production fix was necessary. Reviewer summaries were kept to the eight prespecified percentile targets rather than exporting incidental percentile intervals for other contrasts.

The raw full-precision production JSON remains an internal verification layer and is not approved by this audit as a public download. This numerical pass does not remove the study's retrospective timing, public-bootstrap approximation, sparse-component, response or noncausal-interpretation limitations.
