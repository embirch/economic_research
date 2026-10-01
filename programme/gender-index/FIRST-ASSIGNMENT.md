# Proposed first assignment: verify the candidate indicator inventory

Status: prepared during setup on 30 September 2026; research execution and paid sessions are not authorised by this document.

Sequencing update, 1 October 2026: this original 14-candidate brief is a starting input, not the complete next assignment. Emily now wants a broader data/literature audit and landscape/index v1 before selecting new deep dives. Before commissioning, extend the scope to the regional leads and source gaps recorded in `GEOGRAPHIC-SCOPE.md`, address the pilot review and specify a bounded search protocol and cap. The original no-expansion rule below applies to the old brief, not the new programme-wide audit. See `EXECUTION-PROPOSAL.md` and `RESEARCH-AGENDA.md`; no new paid launch is authorised here.

## Assignment contract

- User authorisation: Emily authorised finishing project setup on 30 September 2026. This brief is a proposed next task, not a new study approval.
- Question: Which existing candidate indicators can support a reproducible Gender & AI evidence resource, with what coverage, interpretation and reuse restrictions?
- Task type: source verification and feasibility, followed by coordinator review.
- Inputs: the 14 indicator and 8 literature records in `evidence/`, the current concept and additional-source audit, and the authoritative article's existing pipeline as read-only context. Starting programme commit: `7228ed8`; record the actual checkout SHA before execution.
- Owner: Codex coordinates. If a paid specialist is commissioned, use the existing data-steward role and record its current deployed version; no director session is needed for this bounded task.
- Writable paths: `programme/gender-index/evidence/` only. The coordinator owns any assignment/run-ledger updates.
- Proposed work branch: `work/index-indicator-verification`, to be created from the integrated setup before execution. It has not been created or dispatched by this setup.
- Spending: no paid session or external purchase authorised. A specialist cap must be explicitly supplied before launch; do not pass a zero cap to the paid runner as a substitute for approval.
- Review/integration owner: Codex; Emily decides the index's scope and any publication.

## Work and stopping point

1. Reuse the existing register and local audit provenance. Assess all 14 candidate entries without restarting discovery or expanding the candidate list. Group shared sources so multiple outputs from one survey are not counted as independent evidence.
2. Start with the Eurostat family (`EU_USE`, `EU_PURPOSE`, `EU_NONUSE`). Link to the existing article's source version and code; check reuse terms, exact measures, denominators, coverage and limitations. Do not edit the article, rerun its write-up or silently refresh its data vintage.
3. For the other entries, verify the strongest permitted evidence available: source files where accessible, otherwise documentation. Keep people, messages, workers and modelled occupational exposure separate; retain broad-AI versus generative-AI distinctions and source-specific sex/gender measures.
4. Record retrieval date separately from fieldwork and publication dates, exact source version/URL, file hashes where acquired, variables and routing, weights/design, missingness/suppression, uncertainty, access and redistribution terms. Preserve earlier evidence and explicitly date each update. A report or catalogue does not prove respondent data access.
5. Mark each candidate as ready for a bounded calculation, documentation-only, blocked pending access/terms, or unsuitable for the proposed construct, with reasons. These are feasibility verdicts, not approval to publish an indicator.
6. Stop when each candidate has a supported verdict or a concrete unresolved blocker. Do not contact source owners, accept new terms, purchase data, start a pilot, fit new models, calculate a composite score or build a production dashboard under this assignment.

## Deliverables and acceptance

- Update `evidence/indicators.csv` in place, preserving stable IDs and sample families. Retain the meaning of `new_check_this_setup=false`: the original migration made no new checks. Record subsequent verification in dated source profiles and link those through the existing `audit_record` field.
- Add source-family profiles under `evidence/sources/` with evidence links, versions and the checks above. Store restricted/raw respondent files outside Git; do not redistribute third-party files merely because they can be downloaded.
- Add `evidence/VERIFICATION-REPORT.md`: supported verdicts for all 14 candidates, a proposed smallest useful first release, explicit exclusions and unresolved decisions. Update related literature records only where the bounded checks provide new evidence; no systematic-review claim.
- Validation: unique IDs; every candidate has a dated evidence trail or explicit blocker; compatible denominators and source families; no unsupported gender linkage, precision or licence claims; no changes to the article. Run `python3 team/validate_setup.py` and `git diff --check`.
- The coordinator reviews source evidence and any proposed calculations before recommending the next scope to Emily. No additional reviewer session is implied.

This task selects feasible evidence. Analysis, final indicator inclusion, further papers and publication follow separate decisions.
