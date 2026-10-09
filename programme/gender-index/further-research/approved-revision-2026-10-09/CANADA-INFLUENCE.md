# Canadian common-mix influence check

9 October 2026. Completed within the approved 16-stratum check. Only unpaid job work daily or several times a week is analysed. External spend $0. No original estimate, source pin, analysis script or manuscript was changed by this specialist.

## Conclusion

The result should be described as sensitivity to the comparison being made, not a stable reversed gender ordering or a broadly uniform within-job relationship. The common-mix minus raw shift stays negative at the point-estimate level in all 16 one-stratum deletions. Its magnitude varies, and the common-mix gender contrast ranges from −2.6 to +0.1 percentage points. Every common-mix deletion interval includes zero.

Contributions are concentrated: the largest stratum contributes 46.8% of the sum of absolute contributions to the raw-to-common-mix shift; the largest three contribute 67.0%. This is not simply a result driven by the smallest domain cell. The largest contributor has at least 150 respondents in each of its four gender/use groups, although at least one group has fewer than 75 outcome events. It cannot be described as uniformly well supported on every criterion.

The original contrasts remain +3.4 points [0.5, 6.3] for observed jobs and −1.7 [−5.2, 1.7] for the common occupation/sector mix, with their paired change −5.1 [−7.7, −2.6]. The check does not replace any of them with a selected restricted-population estimate. It gives specific evidence about their sensitivity and the limits of the stronger narrative.

## Outputs and reproducibility

- Portable diagnostic: `studies-2026-10-07/E08/influence_check.py`.
- Safe pooled release: `studies-2026-10-07/E08/influence-summary.json`.
- Private detailed aggregates: `data/cache/selected-studies/E08-influence-20261009/diagnostics-private.json` and `replicate-diagnostics-private.npz`. They contain labelled support, weights, fine-cell means, contributions and all 16 deletion results. **Do not serve, bundle or publish these files.**
- Independent array agreement record: `data/cache/selected-studies/E08-influence-20261009/independent-agreement.json`. Coordinator reconstruction is in the same private directory. These are internal validation files.

The private directory is under the repository's ignored `data/cache/` tree, outside the served programme directory, with directory permissions 0700 and private-file permissions 0600. The script writes no respondent records, identifiers or respondent-weight files. Its diagnostic arrays are private fine-cell aggregates, not safe public data.

Run from any directory using Python with numpy and pandas:

```sh
python /path/to/E08/influence_check.py \
  --cache /path/to/E08-source-cache \
  --private-out /path/to/private/E08-influence-20261009
```

The source cache must contain all five manifest files. The script reads the adjacent `source-manifest.json` and `results.json`, checks original-file hashes before and after execution, and defaults to writing only the safe `influence-summary.json` beside itself. `--summary` permits a separate summary location for reproducibility checking. The script contains no network calls, paid dependencies or imports from historical estimator code. Private output paths inside the article or served programme tree are rejected.

## What was calculated

The sample, outcome, gender/use categories, survey weights and 16 source-defined `NOC7 × COWMAIN3` strata are exactly those of the original common occupation/sector calculation. The four groups remain Men+ nonusers, Men+ users, Women+ nonusers and Women+ users. All 20,538 employees are retained in the original reconstruction.

Let `q_s` be stratum s's pooled employee weight share, `p_sg` its share within group g, and `m_sg` the outcome rate in that cell. With coefficients `a = (1, −1, −1, 1)`, the stratum's contribution to the difference between the common-mix and raw gender interactions is:

```text
C_s = sum_g a_g (q_s − p_sg) m_sg
sum_s C_s = common-mix interaction − raw interaction
```

This is an exact descriptive accounting identity. It is not an occupational causal decomposition. Raw and common-mix contributions were also reconstructed separately. All identities were checked for the full survey weight and all 1,000 public bootstrap weight sets.

For every stratum, the private record contains its pooled target share, four group-specific job shares, respondent and outcome-event support, source grades, cell rates, weighted denominators, minimum bootstrap denominators, and contribution estimates with sampling intervals. No stratum was selected for inspection after seeing its influence.

All 16 leave-one-stratum-out comparisons were then computed. Each deletion removes the same stratum from all four groups. Raw group shares and pooled target shares are recalculated among the 15 retained strata in every bootstrap replicate. Each resulting statistic concerns that restricted population. A second algebraic route checked the standardized deletion calculation; no pseudocounts, favourable exclusions, new coarsenings or new models were introduced.

## Support and concentration

Thin-domain checks were fixed at fewer than 5, 75 and 150 respondents, reflecting the existing source-quality boundaries. Outcome-event checks were recorded separately, retaining the original study's conservative event-count safeguard. The thresholds describe support; they were not exclusion rules.

| Support diagnostic | Strata affected | Share of the original common target |
|---|---:|---:|
| At least one gender/use domain below 75 respondents | 10 of 16 | 41.5% |
| At least one gender/use domain below 150 respondents | 11 of 16 | 43.3% |
| At least one gender/use cell with fewer than 5 outcome events | 7 of 16 | 31.0% |
| At least one gender/use cell with fewer than 75 outcome events | 16 of 16 | 100.0% |

These overlapping rows must not be added. “41.5%” is the target weight of whole strata containing at least one thin group; it is not the share of all employees who belong to a thin cell. The smallest component domain has three respondents, as already recorded in the original methods. Its singleton bucket's target mass and contribution are not released here. No component denominator is zero in any of the 1,000 bootstrap sets.

Target-mass summaries concern a pooled covariate-defined proportion and pass its aggregate sample-count rule. Outcome contribution summaries require separate outcome support. Several pooled thin-support buckets remain F under that rule, so their contribution quantities are withheld even where the target mass is releasable. Fine-cell rates are withheld regardless of grade. The public concentration percentages disclose no stratum identities or cell rates.

The contribution concentration denominator is the **sum of absolute contributions**, not the absolute value of the net −5.1-point shift. Ten contributions are negative and six positive, so cancellation matters. The largest contribution's 46.8% share and the top-three 67.0% share must not be presented as causal percentages of a gender gap “explained” by particular occupations.

The most influential contribution is not from a stratum with a domain below 150 in any group. This distinguishes small respondent support from large influence. Its event-support limitation still matters, and the broader common target includes substantial thin-domain coverage. Neither fact licenses an unqualified robustness claim.

## All-stratum deletion findings

| Statistic across all 16 restricted populations | Point-estimate range | Pointwise 95% interval pattern |
|---|---:|---|
| Common-mix Women+-minus-Men+ user/nonuser contrast | −2.6 to +0.1 points | All 16 intervals include zero. |
| Common-mix minus raw contrast within the same restricted population | −7.0 to −2.4 points | Fifteen intervals are wholly negative; one includes zero. |

Fifteen common-mix point estimates are negative and one is positive. All 16 common-minus-raw point estimates are negative. All pooled restricted-population outcome proportions pass the aggregate A release rule; their constituent sparse cells remain a separate limitation.

The first row rules out describing the negative common-mix ordering as insensitive to which broad job groups are included. The second gives a narrower reassurance: deleting any single stratum does not eliminate or reverse the negative reweighting shift at the point-estimate level. The shift's magnitude is sensitive, and its uncertainty does not exclude zero in every deletion.

The ranges are not confidence intervals. Their members concern different populations and are statistically dependent. The displayed sampling intervals are pointwise, not a simultaneous confidence statement for the deletion family. This diagnostic does not test every combination of exclusions, other adjustment choices or unobserved differences within jobs.

## Sampling uncertainty and release rules

Every statistic uses the original full survey weight and all 1,000 generalized public bootstrap weight sets. Variance is `mean((T_b − T_full_target)^2)`, with divisor 1,000 and a 1.96 normal multiplier. The centre is each statistic's full-weight estimate for its own population, not its replicate mean. Target shares, group shares, cell means and contrasts are recomputed in every replicate. Paired changes use the same replicate across their component statistics.

The original release rule is unchanged: A at least 150, E 75–149 and F below 75, with fewer than five expressly unacceptable; the study conservatively uses the worse domain/event grade for outcome release. These national categorical thresholds are not a theorem establishing precision for sparse standardized components. Only anonymous pooled summaries are public. Singleton bucket quantities and F-quality outcome summaries remain withheld. All 16 individually labelled deletion results remain private to avoid releasing a recoverable collection of component information.

Percentages and differences are rounded to one decimal. Signs and interval-inclusion counts use unrounded estimates. A displayed 0.0 in any supplementary range is not an equivalence finding. Sampling intervals do not cover confounding, recall, imputation uncertainty or alternate comparison definitions.

## Verification and integration recommendation

All five source hashes and sizes match `source-manifest.json`. Keys are complete, unique and aligned between analytical and bootstrap files; all weights are finite and nonnegative, and point weights are positive. The fixed variable domains and original group/sample counts match.

Eleven original statistics were reconciled: four raw rates, four common-mix rates, the raw interaction, the common-mix interaction and their paired change. Points, standard errors and interval endpoints agree with `results.json` within 3.75 × 10⁻¹⁶, below the 10⁻¹² tolerance. `analysis.py`, `results.json`, `source-manifest.json`, `public-tables.csv` and `PROTOCOL.md` retain their pre-run hashes.

The coordinator separately reconstructed the calculation from the pinned SAS inputs without importing the diagnostic estimator. Comparing stratum order, respondent/event counts, target shares, contributions and all 16 raw/common/change replicate vectors gives exact agreement in target shares and contributions, and a maximum difference of 4.17 × 10⁻¹⁷ across deletion vectors. This comparison covers all 1,001 weight sets. It is independent implementation agreement, not human peer review or validation of a causal interpretation.

Running the portable script from `/private/tmp` with explicit cache/output paths produced a byte-identical safe summary. No additional substantive analysis is required to finish the approved check.

Suggested bounded integration:

> Removing each occupation-and-sector group in turn leaves the common-mix gender contrast between −2.6 and +0.1 percentage points, with every interval including zero. The shift from the corresponding raw comparison remains negative in all 16 point estimates, but its magnitude varies. This supports sensitivity to how jobs are compared, rather than a stable reversed gender ordering.

Keep the original estimates and the separate additive comparison visible. In Methods, record the concentrated contributions, substantial target coverage of thin domains, the largest contributor's differing domain/event support, and the restricted-population interpretation of every deletion. No manuscript, figure, model or original result was replaced by this check.
