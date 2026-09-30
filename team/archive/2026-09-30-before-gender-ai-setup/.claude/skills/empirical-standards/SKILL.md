---
name: empirical-standards
description: The standards every analysis script and every number in a post must meet: check blocks, two implementations, MDEs, noise checks, pre-registration discipline. Read before writing any script or pre-registration.
---

# Empirical standards

1. **Replication first.** Where the post builds on a published number, reproduce it with Anthropic's released code where it exists and with an independent implementation; state the match to the decimal or the discrepancy and its cause.
2. **Thresholds applied by us**, stated in the script and the post.
3. **Every script ends with a check block** that asserts known facts (counts, published values, ranges, shares summing to 100) and raises on failure. Nothing downstream runs on a failed check.
4. **Two implementations of every headline number**; they must agree to the reported precision.
5. **Synthetic recovery** for each estimator the post relies on: known effect recovered, zero effect reported as zero.
6. **Intervals and MDE beside every coefficient** that may be cited: MDE = 2.8 × SE (80% power, 5% two-sided). A null is reported as "nothing bigger than the MDE."
7. **Errors appropriate to the design**, stated: heteroskedasticity-robust for cross-sections, clustered by unit for panels.
8. **Collinearity reported** (VIF or pairwise correlations) whenever two predictors compete; never key a decision rule to a full model whose MDE is uninformative; never test a covariate on a residual that was formed without it.
9. **Noise checks**: leave-one-out on small samples with movers named; persistence across independent windows for any claim about a place or small cell; flagged or anomalous units excluded by rule and shown separately; placebo outcome where one exists.
10. **Merge audits printed**: rows in, matched, unmatched by name.
11. **Pre-registration discipline**: primary tests run once, after the commit; deviations logged with date and reason; if a rule proves mis-specified, report the registered rule and the corrected one.
12. **Results to files, summaries to the console**; every number the post may cite in results.json with its script.
13. **Plot before modelling**: histograms and scatters so a coding error shows as a shape.
14. **Name what the data cannot show** in the notebook as you go, so the referee and editor inherit it.
