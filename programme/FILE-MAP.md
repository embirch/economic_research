# Project file map

Updated 30 September 2026. Repository-relative paths below are portable; local roots are documented for this workstation only.

| Material | Authoritative location | Status |
|---|---|---|
| Current scope and operating decisions | `PROJECT.md`, `programme/DECISIONS.md` | Read first |
| Shared research and index | `embirch/economic_research` | This repository |
| First paper analysis and manuscript | `embirch/gender-gap-generative-ai` | Separate authoritative repository |
| Latest first-paper author edits | Article repo: `paper/author-edits/blog.html` | Preserve verbatim; overrides generated prose pending integration |
| Article generator and published-number bindings | Article repo: `paper/templates/blog.md`, `src/manuscript.py`, existing outputs and claim register | Integrate line edits carefully after author review; regeneration does not update the live editing copy |
| Current index concept and follow-up audit | `programme/gender-index/concept-and-feasibility.md`, `additional-sources-audit-2026-09-30.md` | Imported unchanged; source details in migration manifest |
| Dashboard concept | `programme/gender-index/prototype.html` | Illustrative prototype, not a validated published index |
| Indicator/literature register | `programme/gender-index/evidence/` | Seeded from prior audits; outstanding verification explicitly marked |
| Anthropic reading bank | `wiki/reports/`, `wiki/style/` | Supplementary material; verify source claims before use |
| Claude's alternative Eurostat work | `posts/gender1/` | Reference-only; do not replace the current article |
| Earlier programme and agent history | `HANDOVER.md`, `room/`, `programme/CALENDAR.md`, `team/handover/` | Historical context where superseded |
| Prior setup instructions | `team/archive/2026-09-30-before-gender-ai-setup/` | Historical; not active agent guidance |

## Local material and boundaries

Both repositories are under `/Users/emilybirch/Desktop/Anthropic/`. The parent is not a Git repository. Original index files remain under `research/gender-ai-index/`; the copies named above become the shared working versions. The migration manifest records source paths and SHA-256 hashes.

`research/gender-ai-index/audit-sources/` and `gender_ai_audit/raw/` remain local. Some sources are individual-level data or third-party material with unverified redistribution terms. No raw survey responses or complete third-party source archives are imported by this setup.

`project-backups/setup-2026-09-30/` is a local safety copy, not a cloud backup. Private application context remains outside this repository. Chat transcripts are not automatically stored in GitHub; durable decisions and research outputs are.

The readable prototype is available locally through the Codex file preview. It does not need a running server. The article's editing page still requires its existing local editor process.
