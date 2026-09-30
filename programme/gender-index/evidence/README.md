# Evidence register

`indicators.csv` and `literature.csv` are a starting inventory assembled from the existing concept and audits on 30 September 2026. **No new source verification or analysis was performed to populate this register.** Each entry records that status and its next check. Register entries are candidates, not approved dashboard indicators.

## Maintain the record

Each indicator has a stable ID, question, construct, population, geography, fieldwork/reference period, unit, denominator, gender measure, AI definition, source/sample family, access/reuse status, uncertainty and a comparability group. Unknown items remain explicit. Record actual fieldwork, publication and retrieval dates separately when acquired. Add file/version/hash, verified variable names, missingness and exclusions to the linked source profile; do not overwrite old release evidence.

The `audit_record` field points to the prior memo in the parent directory. `new_check_this_setup=false` distinguishes migration from verification. Replace this with a dated verification record only after performing the check, preserving history in Git. Access to a report, catalogue or metadata is not access to its respondent data.

Use `sample_family` to prevent counting purpose tables, multiple reports or a synthesis as independent surveys. Comparison groups limit compatible comparisons; do not pool incompatible measures into a worldwide rate. Survey sex categories and name-associated message categories must remain visibly different.

Before adding a live indicator, verify data and terms, define the estimand/denominator, establish usable coverage and uncertainty, reproduce the calculation, and obtain the relevant scientific review. A source-specific indicator can be useful without being comparable to all other sources.

Raw data and restricted text stay outside this shared repository. A future reproducible release records source snapshots, licensed downloads, software environment, derived outputs and a release-specific methods note.
