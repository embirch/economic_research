---
name: page-build
description: How to build a post's page with evidence drawers from POST.md, the scripts, check outputs and tables, and how to verify every number on the page against results.json. The tools are site/tools/build_page.py and site/tools/verify_page.py; read before building or verifying any page.
---

# Page build

Two shared tools under `site/tools/`, which the editor owns. Both take the post
folder name and nothing else, and both are keyed to
`posts/<post>/data/processed/results.json` and
`posts/<post>/notes/claims-map.json` rather than to per-post wiring.

```
python3 site/tools/build_page.py  post1      # writes site/posts/post1/index.html
python3 site/tools/verify_page.py post1      # exits non-zero on any unbound number
```

Run them in that order. The page is not publishable until the verifier passes,
and the rule when it fails is **fix the text, never the numbers**.

## What the builder does

1. **Copies the figures** named in `posts/<post>/outputs/figures.json` into
   `site/posts/<post>/figures/`.
2. **Inserts each figure where its caption appears.** A POST.md paragraph
   beginning `**Figure N.` is wrapped in `<figure>` and the image file is
   resolved from `figures.json` by figure number. No filename is hard-coded in
   the builder, and a caption with no matching entry is left as prose — which
   is the signal that the figure number is wrong.
3. **Wraps each section's evidence in a collapsible drawer keyed to the section
   heading.** Which entries a section cites comes from `claims-map.json`: every
   binding carries its section, so the builder collects that section's
   `results.json` entries, renders them as a table (entry, quantity, estimate,
   95% interval, SE, MDE, unit), and then appends, for every script named in
   those entries' `script` fields, the script **in full** with syntax
   highlighting and **the check output it printed when it ran**
   (`outputs/checks/NN_*.out.txt`, matched on the script's number). Scripts are
   shown as the analyst wrote them and are never edited.
4. **Adds the documents under Methodology** — the pre-registration, the lab
   notebook and the red-team memo — in drawers of class `evidence doc`, with
   their headings demoted so they do not compete with the post's.
5. **Generates the contents rail** from the H2 headings.

Nothing on the page is typed by hand. If the research changes, rerun the
builder and the page changes with it.

## What the verifier does

Four checks; any failure exits non-zero and prints every problem.

1. **The claims map resolves.** Every binding names a real path in
   `results.json` and records that path's current value. This is the drift
   check: if the analyst re-runs and a number moves, the map stops matching.
2. **Every quantitative sentence is mapped.** POST.md is split into sentences;
   every sentence carrying a bindable number must appear in `claims-map.json`
   verbatim. Editing a mapped sentence therefore breaks the build until the map
   is regenerated — which is the point.
3. **Every number in POST.md is bound to its own sentence's entry.** Each
   bindable number must be a rounding (zero to four decimals) of a value that
   sentence's own bindings resolve to — a numeric value, or a number inside a
   bound string — or be declared for it in `as_printed`. A number that merely
   occurs somewhere in `results.json` does not pass. This is the referee's
   draft-review audit made part of the tool: a global index accepts small
   integers regardless of what they mean, so a PASS on it is necessary and not
   sufficient. When this check fires on a true number, the fix is usually to
   bind the sentence to the field that carries it (a floor named in a test's
   `label`, a unit named in an estimate's `unit`), not to add `as_printed`.
4. **Every number on the built page is in `results.json`.** The page's prose,
   captions, contents rail and generated tables are scanned against the whole
   of `results.json` — the weaker global check, and the right one there,
   because the generated tables print entries verbatim.

**Bindable** excludes what is not a claim, each exclusion listed with its
reason in `EXCLUDE` at the top of `verify_page.py`: code spans and fenced
blocks, page and figure and footnote locators, appendix references, hypothesis
and quartile labels, SOC codes, O\*NET and its database version, window dates
and calendar years, scientific-notation exponents, and any digits inside an
identifier (`fig211`, `D_aug2025`).

**Not scanned on the page:** the script source and check output in the drawers,
and the three embedded documents. They are the analyst's and the referee's
artefacts reproduced verbatim — the provenance of the numbers rather than
claims about them. Everything the reader reads as prose is scanned.

## The claims map

`posts/<post>/notes/claims-map.json` is the editor's file. Each entry is one
quantitative sentence:

```json
{"id": "S03", "claims_md": "1 and 5", "section": "...",
 "sentence": "**In each of the three Claude.ai windows …**",
 "bindings": [{"key": "tests.D_aug2025.estimates.D.coef", "value": 1.383646}]}
```

`key` is a dotted path into `results.json`; `[n]` indexes a list, and a key
containing a dot is quoted (`boundary_tie_mass."b3_43.40".tasks`). `claims_md`
is the sentence id in `notes/claims.md` the sentence is written under, so a
referee can go from any sentence to its permission and to its number in two
steps. `as_printed` records a rounding the sentence prints that is not a plain
rounding of the stored value — a mantissa (`1.8` for 1.8 × 10⁻¹⁴) or a ratio
printed as a percentage (`0.9` for 0.009323). Use it sparingly and never to
launder a number that is not in `results.json`.

`site/tools/make_claims_map.py` generates the map for post1: each sentence is
matched by a unique anchor substring, so editing the prose around a sentence
cannot silently re-point its bindings, and the generator fails if an anchor
matches no sentence, more than one, or if any sentence is unbound. Copy it and
change `SPEC` for a new post.

## Order of work, and the common failures

Draft POST.md → regenerate the claims map → build → verify → repeat. Four
failures account for most of the loop:

- **`[unmapped sentence]`** — a mapped sentence was edited. Regenerate the map.
- **`[number not bound to this sentence]`** — either the number is not in
  `results.json` at all (almost always one remembered from a note or a brief:
  write a room note to its owner, or cut the sentence), or it is real but the
  sentence is not bound to the field that carries it. Add the binding.
- **`[unbound number on page]`** — a number reached the page that is in no
  field of `results.json`.
- **A rounding that is not a rounding.** 97.15 does not round to 97.2 at one
  decimal place. Print the exact figure rather than the coarsening a memo used.
- **A number only a memo has.** Counts that live in the lab notebook (trial
  counts, intermediate SEs) are not in `results.json`; say it in words or leave
  it out.
