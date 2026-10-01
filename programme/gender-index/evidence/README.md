# Evidence register

The current reviewed atlas is [source-register.csv](source-register.csv): 33 source/indicator records, with dated verification, definitions, uncertainty, access and next checks. Read the [v1 integration review](../landscape-v1/REVIEW.md) and [source-audit disposition](../landscape-v1/coordination/source-audit-review.md) before using specialist claims. A record is not automatically a displayed numerical indicator or an independent study.

`indicators.csv` preserves the original 14 stable IDs with reviewed metadata. `literature.csv` retains 11 foundational and interpretive records with updated reading limits; the specialist's proposed additions remain in [literature-updates.csv](../landscape-v1/research/literature-updates.csv). Some sources have newly inspected files, others primary documentation, and others explicitly carried-forward checks or access blockers. This is not a claim that every underlying dataset was freshly audited.

The 30 September migration itself performed no new verification. The [pilot](pilot-2026-10-01/) and [v1 specialist submission](v1-audit-2026-10-01/) preserve the subsequent evidence and scripts. Their reports carry notices linking to coordinator corrections. The unresolved Eurostat non-use reconstruction is withheld from the numerical explorer; corrections do not erase historical source vintages.

## Maintain the record

Each indicator has a stable ID, question, construct, population, geography, fieldwork/reference period, unit, denominator, gender measure, AI definition, source/sample family, access/reuse status, uncertainty and a comparability group. Unknown items remain explicit. Record actual fieldwork, publication and retrieval dates separately when acquired. Add file/version/hash, verified variable names, missingness and exclusions to the linked source profile; do not overwrite old release evidence.

The `audit_record` field resolves relative to `programme/gender-index/`. `new_check_this_setup=false` retains its historical meaning that the 30 September migration performed no verification. Add new dates and linked evidence to `verification_status` and `audit_record` after checking sources, preserving history in Git. Access to a report, catalogue or metadata is not access to its respondent data.

Use `sample_family` to prevent counting purpose tables, multiple reports or a synthesis as independent surveys. Comparison groups limit compatible comparisons; do not pool incompatible measures into a worldwide rate. Survey sex categories and name-associated message categories must remain visibly different.

Before adding a live indicator, verify data and terms, define the estimand/denominator, establish usable coverage and uncertainty, reproduce the calculation, and obtain the relevant scientific review. A source-specific indicator can be useful without being comparable to all other sources.

Raw data and restricted text stay outside this shared repository. A future reproducible release records source snapshots, licensed downloads, software environment, derived outputs and a release-specific methods note.
