# Setup readiness, 30 September 2026

Current follow-up to the original setup report in the parent workspace's `project-backups/setup-2026-09-30/SETUP-STATUS.md`. Emily asked to finish project setup so work on the Gender & AI Index can begin.

## Verified locally

- The programme started this check clean at `7228ed8`. Follow-up documentation is on `setup/index-readiness-2026-09-30`.
- Current programme scope, decisions, seven-role policy, imported-file hashes, evidence fields and available deployment receipts pass `python3 team/validate_setup.py`. Receipts match local source files; deployed agents were not queried again and no paid session was started.
- All three session budget/branch guard tests pass with `PYTHONDONTWRITEBYTECODE=1 python3 team/test_session_guards.py`. Running the module from the repository root with `python3 -m unittest team/test_session_guards.py` fails to resolve its sibling `run_agent` import; the documented direct-file command works.
- `core.hooksPath` points to `team/hooks`; its pre-push hook rejects direct pushes to `main`. This is a local safeguard, not remote enforcement.
- The first-paper repository remains on `setup/preserve-author-edits-2026-09-30` at `669b9ac`. Its untracked `output/` and `tmp/` folders were left untouched. The live manuscript hash still matches the preservation record: `c98f327ace493a24efae4ae12baa397dc3569e926779ae24661eb26e5f9097c5`.
- The evidence register remains 14 candidate indicators and 8 literature entries. No new source verification is claimed. The [first assignment](gender-index/FIRST-ASSIGNMENT.md) is prepared for a separate execution decision.

## Remaining remote setup

| Item | Current evidence | Required completion |
|---|---|---|
| Programme visibility | Emily subsequently instructed "ok just keep going with public for now". The repository remains public. | No visibility change pending under the current instruction. Keep restricted/raw data and credentials out of commits. |
| Branch protection | Emily explicitly authorised the prepared rule, completed GitHub email verification, and GitHub confirmed "Branch protection rule created" for `main` on 30 September 2026. It requires PRs and conversation resolution, applies to administrators, and disallows force pushes/deletion. | Complete. Formal approval count is zero to avoid preventing the sole maintainer from merging; scientific review requirements still apply. CI runs but is not configured as a required status check in this rule. |
| Article cloud backup | Authenticated repository API still returns 404. The preservation commit and safety backup remain local. | User checks repository selection/access for the existing credential; then push the preservation branch without rewriting author edits. Never put credentials in project files or messages. |
| Remote validation | The prepared template was committed through the authenticated GitHub browser to `.github/workflows/setup-validation.yml`; local comparison confirmed an exact match. [PR 3](https://github.com/embirch/economic_research/pull/3) passed its [final setup check](https://github.com/embirch/economic_research/actions/runs/36736629006) and was merged at `4d4b397`. | Complete. Future pull requests and pushes to main run these checks. No paid research calls occur in this workflow. |

No credentials were changed and repository visibility remains public at Emily's instruction. Setup documentation can now proceed through the public branch/PR workflow; restricted data remain local.

## Ready to begin, within limits

The local organisation and bounded research brief are ready. The first substantive task is verification of the existing evidence inventory, before selecting a production dashboard or final index coverage. A paid specialist run needs an explicit assignment approval and dollar cap. Existing setup approval does not supply either.

The programme repository is a public shared environment. The article's local preservation remains separate from its unresolved cloud backup. Index preparation can continue without changing the manuscript or starting a paid session.
