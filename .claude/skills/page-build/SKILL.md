---
name: page-build
description: How to build a post's page with evidence drawers from POST.md, the scripts, check outputs and tables, and how to verify every number on the page against results.json. STUB until the editor generalises reference/posts/post2/build_page.py in Stage 1.
---

# Page build (to be generalised in Stage 1)

The reference implementation is reference/posts/post2/build_page.py: it reads POST.md, inserts figures where captions appear, wraps each section's evidence (script source with syntax highlighting, the check output, tables from CSV) in collapsible drawers keyed to section headings, adds a contents rail, and writes site/posts/<post>/index.html. The verification step compares every number in POST.md with results.json and fails the build on a mismatch. The editor rewrites this as a shared tool under team/ in Stage 1, keyed to results.json rather than to per-post JSON files.
