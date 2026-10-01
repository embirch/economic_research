# Gender & AI research programme

An empirical research programme led by Emily Birch on gender differences in adoption, use and experience of generative AI, and their social and economic implications. The working output is a public evidence explorer supported by substantial research papers; its design follows what the data support.

## Start here

1. [Current project](PROJECT.md): scope, first-paper decision and immediate work.
2. [Decisions](programme/DECISIONS.md) and [file map](programme/FILE-MAP.md): what is current and where it lives.
3. [Operating model](team/SETUP.md): assignments, reviews, budgets, branches and authentication.
4. [Index concept and evidence](programme/gender-index/README.md).
5. [First paper repository](https://github.com/embirch/gender-gap-generative-ai): the authoritative Eurostat article, including Emily's live edits.

Anthropic's research bank under `wiki/` is supplementary material. Earlier research is retained for traceability; neither old handovers nor agent memories override current decisions. The alternative analysis in `posts/gender1/` is reference-only.

## Working criteria

- A useful question with a distinct contribution to the wider literature.
- Data checked at variable level before a study is commissioned.
- Measures, populations, fieldwork dates, gender coding and comparability stated explicitly.
- A proportionate analysis plan with prior inspection and later deviations disclosed.
- Reproducible calculations, independently checked key claims and clearly bounded uncertainty.
- Readable prose in Emily's voice, with source links, useful figures and substantive limitations.
- No automatic equation of use with benefit, occupational exposure with job loss, or name-associated message shares with population adoption.

## Quick verification

From the repository root: `python3 team/validate_setup.py`. This checks setup consistency and imported-file provenance without internet access, API credentials or paid agent work. It does not certify the empirical findings. The installed GitHub Actions workflow is `.github/workflows/setup-validation.yml`; it also checks billable-session guards on pull requests and pushes to main.

The [working landscape v1](programme/gender-index/landscape-v1/README.md) has separate source-extract and presentation checks. Its HTML can be rebuilt offline with `python3 programme/gender-index/landscape-v1/build_explorer.py`.

Research reproduction remains study-specific. Follow the first paper's README for its frozen data and analysis commands. New studies must document their own environment and reproduction command.

## File ownership

Assignments name writable paths. Roles and default ownership are in [team/SETUP.md](team/SETUP.md); the coordinator can make explicitly authorised cross-cutting setup changes. Agents work on assigned branches, not directly on `main`.

## Layout

`programme/gender-index/` current index work; `data/` source atlas and acquisition code; `wiki/` supplementary literature; `posts/` earlier and future studies; `room/` dated coordination notes; `team/` agents, templates and tooling; `.claude/skills/` active procedures.

Keep credentials, restricted respondent data and private application documents out of Git. Repository privacy is managed separately from publication decisions. The setup report records the verified GitHub state.
