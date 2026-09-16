# Pre-registration · Post 2 · Job or place?

**Date written.** 15 September 2026, evening, after steps 01–03 (loading, replication, stage 1) and before any of steps 04–07 was run. Committed to git before running.

## What has already been seen (disclosure)
Step 02 reproduced Anthropic's 0.36 (log Usage Index on computer/math workforce share in points: 0.369, R² 0.62 on August 2025; 0.28–0.30 on later waves) and the Gini series (0.367, 0.318, 0.286; then 0.282 and 0.278 in April and May 2026: the convergence stalled after February). Step 03 (descriptive, pre-specified in PLAN §3) found the Claude user base is most unlike its state's workforce in low-adoption states (Wyoming, South Dakota, Alaska, West Virginia, Mississippi) and least in Colorado, and that the users' computer/math share *falls* with the workforce's (−0.5 points per point, R² 0.26). No model in steps 04–07 has been run.

## Research question
How much of where AI use is distinctive across US states is the jobs people hold, how much is the place itself (or the selection of users within jobs), and which of the two explains who caught up?

## Constructs, fixed
- **Level**: the state Usage Index (Anthropic's, or rebuilt to the verified convention). **Mix**: the state's artifact shares (32 categories, June 2026 `overall`), use-case shares (3) and collaboration-pattern shares (5); request level-2 shares only for the cross-provider comparison.
- **Workforce composition**: ACS 2023 C24010 shares by SOC-mappable group. **User composition**: Anthropic `soc_occupation` shares by state (April and May 2026 only; August 2025 is 74% unclassified and heavily suppressed). Suppressed small groups treated as zero.
- **Utah** excluded from every model (Anthropic flagged August 2025 as abuse-affected; its index fell from 3.8 to 1.1 by November). Shown separately.
- Standardised predictors, HC3 errors, at most three predictors per model, MDE = 2.8 × SE reported with every coefficient.

## H2 · Do jobs explain the mix? (step 04, stage 2)
Expected mix for state s = Σ_g user_share(g, s) × global within-group mix(g), using the June global `soc_occupation` rows (artifact, use-case and collaboration metrics per major group) and the state's user occupation shares. Observed = the state's `overall` shares.
Read-outs: (i) pooled R² of observed on expected across state × category cells after removing category means (how much of the between-state variation, category by category, the user occupation mix explains); (ii) per-state dissimilarity (half the absolute difference summed over categories) between observed and expected mix; (iii) the five largest residual states, profiled by which categories drive them.
**Decision rule:** user composition *explains the mix* if (i) ≥ 0.50 for the artifact mix; *does not* if (i) < 0.25; between is reported as partial. April 2026 is the replication; agreement of the five largest residual states across the two months is reported.
What this cannot separate: a residual is either the place or selection within occupations; the post says so.

## H3 · What is the place? (step 05)
Outcome: residual of log Usage Index (May 2026) after the workforce computer/math share (the January 2026 model). Models, each HC3: (a) z(bachelor's share) alone; (b) z(bachelor's) + z(median age) + z(broadband); (c) z(log GDP per working-age adult) alone; (d) z(bachelor's) + z(log GDP).
**Decision rule:** a covariate "explains the residual" if its interval excludes zero and |coefficient| ≥ its MDE in the model where it appears alone and in (b) or (d). Doms and Skinner–Staiger predict education yes, income and broadband no. Reported either way. Density (population per square mile, 2020 gazetteer) added as a fourth model if the file is available; otherwise omitted and said.

## H4 · Who caught up? (step 06)
Outcome: change in log Usage Index, August 2025 → May 2026, Utah excluded. Models: (a) on log Usage Index in August (β-convergence); (b) adding z(bachelor's) and z(workforce tech share).
**Decision rule:** convergence is "real across states" if the coefficient on the initial level is negative with interval excluding zero; catch-up "follows education" / "follows composition" if the respective coefficient in (b) is outside its MDE. The stall after February (Gini 0.286 → 0.278) and the February advertising influx are reported descriptively; the November → February change is shown separately as the influx wave.

## H5 · Three providers, one map? (step 07)
Levels: Spearman rank correlations among Anthropic (May 2026 Usage Index), Microsoft (Q1 2026 AI user share) and OpenAI (2025 messages-per-capita rank), raw; then between residuals after the workforce computer/math share (each series regressed on the share; OpenAI's rank regressed on the share).
Mix: OpenAI topic shares by state (2025) against Anthropic request level-2 shares mapped in advance to the same five topics (technical help; writing; practical guidance; seeking information; self-expression) for August 2025 and May 2026; the mapping list is fixed in the script before it runs and printed. Spearman across states per topic.
**Decision rule:** providers "agree on the place" if every pairwise residual level correlation ≥ 0.5; the mix is "a property of the place" if the median topic correlation ≥ 0.5. Caveat fixed now: Microsoft's state figures are small-area model estimates that use demographic covariates, so their residual is partly model-imposed; the Anthropic–OpenAI pair is the measured comparison.

## Robustness (all reported)
April 2026 replication for H2 and H3; without DC; usage-weighted regressions; level-1 request mapping for H5; H3 on the Usage Index residual after user (not workforce) tech share.

## Deviations
Logged in notes/lab-notebook.md with date and reason.
