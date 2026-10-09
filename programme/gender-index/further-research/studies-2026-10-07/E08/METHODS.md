# Methods: generative AI use and unpaid job work in Canada

## Question and population

The primary target is the difference between Women+ and Men+ in the association of reported workplace GenAI use with frequent unpaid personal-time job work. This is a pooled cross-sectional employee description from Statistics Canada's Canadian Survey on Working Conditions (CSWC) 2024–2025 public-use microdata file. The [public source package](https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm) contains the analytical file, public generalized bootstrap weights and documentation.

The study includes all 20,538 reference-job public/private employees, coded `COWMAIN3` 1 or 2, from 23,314 records. It excludes 2,776 self-employed respondents. All five released age groups, ages 15–69, are retained. The four groups contain 7,993 Men+ nonusers, 2,224 Men+ users, 8,080 Women+ nonusers and 2,241 Women+ users. Those are respondent counts, not population totals or effective sample sizes.

The ten-province frame excludes the territories, institutionalized people, full-time Armed Forces members, people on reserves and other Indigenous settlements in the provinces, and extremely remote low-density areas. Unpaid family workers are outside the employment frame. The survey draws from LFS households and requires respondents' own answers rather than proxies. Estimates do not describe all Canadian residents or all jobs.

Collection occurred in four periods from 23 September 2024 to 18 July 2025. No usable public wave field permits a joint use/gender/unpaid-work trend. This is not a worker panel. The guide states that 4.9% of the **whole survey sample** answered about a reference job or business already left. That is not an estimate for this employee subset. `CHG_05`, which identifies these respondents, is absent from the PUMF. For them, 12-month questions concern the last 12 months in that reference job; otherwise they concern the preceding 12 months. LFS-derived fields use its earlier reference week. Neither temporal order nor individual changes after adoption are observed.

## Exact variables

| Role | Coding |
|---|---|
| Link | `PUMFID`, validated unique and complete in each file; never released |
| Employees | Character `COWMAIN3` in `1`, `2` |
| Gender | Numeric `GENDER` 1 Men+, 2 Women+ |
| Any GenAI use | Numeric `G_AI_05A` 1 yes, 2 no |
| Primary Y | `WTQ_45` 1 daily or 2 several times a week |
| Full Y distribution | `WTQ_45` 1–5: daily, several times a week, several times a month, once a month or less, never |
| Adjustment | Character categories in `AGECAT`, `EDUC_G`, `NOC7`, `NAICS8`, `COWMAIN3` |
| Weights | `CSWCWT`; `BSW1`–`BSW1000` joined by the unique key |

Men+/Women+ are the source's confidentiality-protected gender categories. Some nonbinary respondents are redistributed into them. They are not biological-sex measurements and do not support a separate nonbinary estimate. Use means any reported GenAI use for the reference main job in its relevant 12-month period, not intensity, adoption date or employer provision. The unpaid-work question measures work to meet job demands, not domestic or caring labour, and categories cannot be converted to hours.

All required values match the frozen domains and are complete; no missing or skipped answers become zero. There are eight released `NOC7` codes (`00`–`07`), not seven. The guide describes nearest-neighbour donor imputation; imputation flags are not public, so an observed-only or multiple-imputation analysis is unavailable. No such analysis is fabricated.

## Estimands and shared-replicate covariance

For each gender/use group, the rate is the weighted sum of the outcome divided by that group's weight sum. The primary interaction is `(Women+ users − Women+ nonusers) − (Men+ users − Men+ nonusers)`. Positive values mean a larger percentage-point user/nonuser gap for Women+. This absolute-rate contrast is distinct from a ratio comparison or comparisons using other frequency thresholds. They do not establish that use changed anyone's work or that Women+ have the highest rate in every relevant population. All four rates and both within-gender gaps are therefore released.

Every statistic uses the full `CSWCWT` estimate and all 1,000 generalized public bootstrap replicates. Variance is `mean((replicate − full estimate)^2)`, with divisor 1,000 and full-estimate centring. For vectors, the mean outer product of those deviations gives covariance. Each contrast is formed within its common replicate before variance calculation. Replicate means are not the variance centre; independent row bootstraps and independent-binomial standard errors are not used.

Primary intervals use estimate ± 1.96 standard errors. The guide's illustrative multiplier is rounded to 2.0; 1.96 is used consistently here. These are pointwise public-bootstrap sampling intervals, not uncertainty about all measurement, imputation or model choices. They need not equal confidential master-file intervals.

The percentile sensitivity for unpaid job work calculates `numpy.quantile(replicates, [0.025, 0.975], method="linear")` for the four raw outcome proportions. The guide §10.2 permits percentile intervals. Both interval versions are retained in `percentile-sensitivity.csv`. None of these four is a boundary estimate, none has a normal interval outside [0,1], and none has degenerate replicates. No interval was clipped. Distribution intervals are pointwise descriptive additions, not simultaneous coverage of every category or a multiple-threshold hypothesis search.

## Additive projection

The article's proportional descriptions are calculated from the original unrounded raw rates using user rate divided by nonuser rate: about 2.7 for Men+ and 2.6 for Women+. `export_scale.py` exports this arithmetic and the absolute gaps to [scale-comparison.csv](scale-comparison.csv), recording the source hash in `scale-provenance.json`. No ratio uncertainty, ratio equality test or new primary target is claimed. All displayed rate and difference values retain the original one-decimal release rule.

Weighted least squares uses an intercept, Women+, use, their interaction and categorical main effects for age, education, broad occupation, broad industry and sector. For unpaid job work, it is fitted to the whole employee sample with exactly the same 25-column design in all 1,000 replicate refits. The interaction coefficient is the stated projection target. Shared additive covariate slopes allow model structure to bridge sparse combinations; this is not a nonparametric comparison of otherwise identical jobs or a causal adjustment.

All point and replicate weighted Gram matrices have rank 25. Normal-equation residuals are below 3 × 10⁻¹⁶. Full-sample maximum leverage is 0.0267 and leverage sums to 25. The unpaid-job-work fitted range is −0.060 to 0.300, with 1,015 negative fitted values. These are diagnostics of the linear projection, not individual probabilities. The predeclared model is retained without switching links. Coefficients and their joint covariance remain in internal `results.json`.

## Common composition and the same-support comparison

For occupation × sector, and then occupation × sector × education, common support is the set of strata with at least one record in every gender/use group. Support is chosen once from observed covariates and held fixed in every replicate. Each group-specific stratum mean is averaged using the pooled weight share of that stratum among all retained groups. Both stratum means and pooled target shares are recomputed under each bootstrap weight.

Occupation/sector retains all 20,538 employees across 16 strata. The education extension retains 20,413 across 44 of 48 observed strata, representing 99.4% of employee weight. Its retained weight shares are 99.5% for Men+ nonusers, 99.9% for Men+ users, 99.2% for Women+ nonusers and 99.9% for Women+ users. `support-summary.csv` gives these denominators and the failed finer target's support in a rounded release layer.

For each supported target, the script also computes raw group rates on exactly that support. The restriction contrast is same-support raw interaction minus full raw interaction; the composition contrast is standardized interaction minus same-support raw interaction. Their intervals use common replicates and the complete joint covariance, including covariance between the full raw and restricted targets. The two changes add to standardized minus full raw in every finite replicate within floating-point tolerance. The identical population in occupation/sector makes its restriction change exactly zero by construction; that is not an estimated absence of a substantive population effect.

The following results separate the effect of restricting the sample from changing its composition. Values are percentage points with pointwise 95% public-bootstrap intervals. The contrast in every row is the Women+ user–nonuser difference minus the Men+ user–nonuser difference.

| Comparison | Occupation and sector | Occupation, sector and education |
|---|---:|---:|
| Raw contrast among retained employees | 3.4 [0.5, 6.3] | 3.4 [0.4, 6.3] |
| Contrast at the common mix | −1.7 [−5.2, 1.7] | −1.0 [−4.5, 2.5] |
| Change from restricting the sample | 0.0, exactly zero by construction | 0.0 [−0.1, 0.0] |
| Change from applying the common mix to retained employees | −5.1 [−7.7, −2.6] | −4.3 [−7.2, −1.4] |

The education restriction change is slightly negative before rounding. Its displayed zero is not an equivalence finding. The large change arises mechanically from reweighting the comparison, while the small sample restriction contributes little here. Neither component identifies an occupational cause of unpaid work. The additive projection is a separate model-based comparison: its frequent-work contrast is 2.7 points [−0.2, 5.6]. It includes age, education and industry as well as occupation and sector, and assumes shared categorical adjustments. The occupation/sector common-mix target uses fewer covariates but allows separate rates for all four groups in each cell. Their difference therefore combines covariate and functional-form choices; no matched model experiment isolates their contributions. The figure retains the protocol's order of raw, additive, occupation/sector and occupation/sector/education targets.

The most granular internal group cells have only three records for occupation/sector and one after education. None of those component estimates is released. Pooled standardization should therefore be read with the sparse-component caveat, even though every required denominator stays positive in all 1,000 replicates. Inference remains conditional on observed support.

The age-saturated diagnostic retains 17,665 respondents and 84.8% of weight over 143 common strata. Required cell denominators are zero in replicates 465 and 480. The failure is reproduced and retained; standardized uncertainty is undefined, and neither a national estimate nor an interval based on only 998 surviving replicates is published. No pseudocounts or further stratum search are used.

## Bounded occupation/sector influence diagnostic

The additional diagnostic holds the original 16 occupation/sector strata and unpaid-work definition fixed. For stratum s and group g, let q_s be its pooled employee share, p_sg its within-group share, and m_sg the frequent-work rate. With group coefficients (1, −1, −1, 1), its contribution to the common-minus-raw contrast is the sum of a_g(q_s − p_sg)m_sg. Contributions add to the original −5.1-point shift under all 1,001 weight sets. This is a descriptive accounting identity, not an occupational causal decomposition.

The [public summary](influence-summary.json) records support and concentration. Ten strata contain a gender/use group with fewer than 75 respondents and together account for 41.5% of the pooled target weight. The largest stratum contribution is 46.8% of the sum of absolute contributions, and the largest three total 67.0%. Because positive and negative contributions offset, these percentages are not shares of the net change explained. Sparse support and influence are distinct: the largest contributor has at least 150 respondents in each group, although an outcome-event count remains below the study's release threshold. The most granular component still has only three respondents.

All 16 leave-one-stratum-out comparisons remove the selected stratum from all four groups together. Each recomputes raw and common-mix estimates on the remaining employee population. The common-minus-raw change ranges from −7.0 to −2.4 points and is negative in all 16. Fifteen pointwise change intervals exclude zero; one includes it. The common-mix gender contrast ranges from −2.6 to +0.1 points, and all 16 of its intervals include zero. These ranges describe point estimates across restricted targets, not sampling intervals or a new national estimate. The intervals are dependent and are not simultaneous coverage of the full diagnostic family.

Group rates, group-specific shares and pooled target shares are recomputed under all 1,000 public bootstrap weight sets. Each variance is centred on that target's full-weight estimate; differences from the original use paired replicates. No selective deletion, further coarsening or estimator replacement is performed. The result supports a downward shift under these specified comparisons, with concentration and sparse-component cautions. It does not establish a reversed population gender pattern, equal associations or a causal effect.

Run after the original analysis, keeping detailed outputs outside any served or public directory:

```sh
python /path/to/E08/influence_check.py --cache /path/to/E08-cache --private-out /path/to/private/E08-influence
```

The script verifies all five pinned source files and reconciles the original four raw rates, four common-mix rates and three contrasts, including standard errors and intervals. It releases only rounded aggregate summaries. Fine-cell rates, stratum identities and individual deletion results stay in the private directory. Small or singleton support-bucket quantities are withheld; target-weight summaries use pooled covariate support, while outcome-contribution summaries also require the conservative event-count check. Original analysis and estimates remain unchanged.

## Release rules and suppression

The pinned guide §9.5 table 1c, printed page 43, specifies national categorical sample thresholds: A at least 150, E 75–149, F below 75, with fewer than five expressly unacceptable. This analysis reports domain and outcome counts separately and conservatively uses the worse of their grades for release. This event-count safeguard is stated as the study's conservative implementation, not a distinct source theorem for nonlinear standardization. Contrasts inherit the relevant aggregate proportions' adequacy; sparse components remain a separate caveat.

All four main unpaid-job-work binary rates are A. Both Men+ daily-frequency proportions are E and require a use-with-caution warning. Public exports omit suppressed values, intervals and event counts. Fine component estimates and failed standardized targets are never exported as findings.

The public CSVs, figures and manuscript show rates and differences to one decimal, computed from unrounded components. The script uses decimal half-up rounding; any weighted counts would be rounded to the nearest hundred. Respondent n values are unweighted sample-size information and retain their exact values. Internal `results.json` contains full-precision aggregates and the finer failed-target diagnostics and must not be a public data download.

## Provenance, execution and interpretation

`source-manifest.json` pins five source hashes. All are verified before any estimate. The two files have identical 23,314-key sets, a one-to-one join, exact key alignment, finite nonnegative weights and positive point weights. The whole-file GenAI benchmark is 22.1%, with 95% interval [21.4%, 22.9%], matching the producer's published table to rounding. It includes self-employment and is not the employee adoption rate. A regression check matches the earlier independent benchmark and the primary raw interaction within 1e-12 for estimates and standard errors.

Run from any directory with Python, numpy and pandas:

```sh
python /path/to/E08/analysis.py --cache /path/to/ignored-or-external/E08-cache
```

The cache must contain the five manifest files. The pipeline has no historical-helper imports, hardcoded username, network access or paid dependency. It writes only aggregate outputs into its own directory. `environment.json` records runtime versions and the script hash. The presentation builders read `figure-specs.json` and the released aggregate tables.

The estimates establish co-occurrence in recorded job populations. Unmeasured tasks, managerial responsibilities, employment arrangements, preferences, reverse selection and recall can jointly affect use and unpaid work. Adjustment does not identify their contribution. Nothing here measures the causal effect of AI introduction, hours saved, productivity, wages, or redistribution of domestic work.

Adapted from Statistics Canada, Canadian Survey on Working Conditions, 2024–2025. This does not constitute an endorsement by Statistics Canada of this product. The [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence) and source quality guidance govern the adapted aggregate outputs.
