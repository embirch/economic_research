#!/usr/bin/env python3
"""Verify that every number on a post's page comes from its results.json.

    python3 site/tools/verify_page.py <post>            # e.g. post1

Three checks, all of which must pass; the script exits non-zero otherwise.

  1. **The claims map resolves.** Every binding in
     `posts/<post>/notes/claims-map.json` names a real path in
     `posts/<post>/data/processed/results.json`, and the value recorded in the
     map is that path's value (to the precision the map states).
  2. **Every quantitative sentence is mapped.** Every sentence of `POST.md`
     that carries a bindable number appears in the claims map, verbatim.
  3. **Every number is bound to its own sentence's entry.** Every bindable
     number in `POST.md` is a rounding (to between zero and four decimals) of a
     value the claims map binds *that sentence* to — of a numeric value, or of a
     number inside a bound string — or is declared for it in `as_printed`. A
     number that merely occurs somewhere in `results.json` does not pass; the
     referee's draft-review audit showed that a global index accepts small
     integers regardless of what they mean.
  4. **Every number on the built page is in `results.json`.** The page's prose,
     captions, contents rail and generated tables are scanned against the whole
     of `results.json`, which is the weaker global check and the right one
     there, because the generated tables print entries verbatim.

"Bindable" excludes what is not a finding: calendar years and window dates,
page and figure locators, section and hypothesis labels, SOC and O*NET codes,
release identifiers, script names, commit hashes and anything inside a code
span or fenced block. Those are listed in EXCLUDE below, each with its reason.

On the built page the prose, the captions, the contents rail and the generated
results tables are scanned; the evidence drawers' script source and check
output are not, because they are the analyst's artefacts reproduced verbatim
and are the provenance of the numbers rather than claims about them.

The rule this enforces: fix the text, never the numbers.
"""
import os, re, sys, json, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# Patterns removed before numbers are extracted, with the reason each is not a claim.
EXCLUDE = [
    (r"`[^`]*`", "code span: column, file, facet and commit identifiers"),
    (r"```.*?```", "fenced block: the rebuild command"),
    (r"\bp{1,2}\.\s?\d+(?:[–-]\d+)?", "page locator in a citation"),
    (r"\bfootnote\s+\d+", "footnote locator in a citation"),
    (r"\bLimitations?,?\s+\d+", "cross-reference to a numbered limitation"),
    (r"\bFigure\s+\d+(?:\.\d+)?", "figure locator"),
    (r"\bAppendix\s+[A-Z]\.?\d*(?:\.\d+)?", "appendix locator"),
    (r"\bH[1-4]\b|\bO-[AB]\b|\bQ[1-4]\b", "hypothesis, outcome and quartile labels"),
    (r"\bSOC-\d+\b|\bSOC-SOC\b|\b\d{2}-\d{4}(?:\.\w+)?\b", "SOC codes"),
    (r"O\\?\*NET(?:-SOC)?(?:\s+\d+(?:\.\d+)?)?", "O*NET and its database version"),
    (r"\b1P\s+API\b", "product surface name"),
    (r"\b\d{1,2}[\u2013-]\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d\d\b",
     "window dates"),
    (r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d\d\b",
     "month-year in a citation or window name"),
    (r"\b20\d\d\b", "calendar year"),
    (r"10⁻?[⁰¹²³⁴⁵⁶⁷⁸⁹]+", "scientific-notation exponent"),
]

NUM = re.compile(r"(?<![A-Za-z_\d])[\u2212-]?(?:\$)?\d[\d,]*(?:\.\d+)?(?![A-Za-z_])")
WORDS = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


PART = re.compile(r'''"([^"]+)"((?:\[\d+\])*)|([^.\[\]]+)((?:\[\d+\])*)''')


def resolve(obj, path):
    """Dotted path into results.json.

    `tests.D_aug2025.estimates.D.coef`, `facts.kish_aug2025.by_quartile[3]`, and
    `facts.q.boundary_tie_mass."b3_43.40".tasks` for a key containing a dot.
    """
    cur = obj
    for m in PART.finditer(path):
        key = m.group(1) if m.group(1) is not None else m.group(3)
        idxs = m.group(2) if m.group(1) is not None else m.group(4)
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(path)
        cur = cur[key]
        for i in re.findall(r"\[(\d+)\]", idxs or ""):
            cur = cur[int(i)]
    return cur


def norm_num(tok):
    tok = tok.replace("\u2212", "-").replace(",", "").replace("$", "")
    try:
        v = float(tok)
    except ValueError:
        return None
    return v


def keys_of(value, out):
    """Every rounding of a number that a writer may legitimately print."""
    v = abs(float(value))
    for nd in range(0, 5):
        out.add(f"{v:.{nd}f}")
    # a percentage written as its own complement is not allowed; only roundings are.


def index_results(node, out):
    """Every number in results.json, at every rounding, including inside strings."""
    if isinstance(node, dict):
        for v in node.values():
            index_results(v, out)
    elif isinstance(node, list):
        for v in node:
            index_results(v, out)
    elif isinstance(node, bool):
        pass
    elif isinstance(node, (int, float)):
        keys_of(node, out)
    elif isinstance(node, str):
        for tok in NUM.findall(node):
            v = norm_num(tok)
            if v is not None:
                keys_of(v, out)


def strip_excluded(text):
    for pat, _ in EXCLUDE:
        text = re.sub(pat, " ", text, flags=re.S)
    return text


def numbers_in(text):
    out = []
    for tok in NUM.findall(strip_excluded(text)):
        v = norm_num(tok)
        if v is not None:
            out.append((tok, v))
    return out


def sentences(text):
    """POST.md prose, split into sentences; headings and tables kept whole."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    out = []
    for block in text.split("\n\n"):
        lines = [ln for ln in block.split("\n") if ln.strip()]
        if not lines:
            continue
        if lines[0].lstrip().startswith("|") or lines[0].lstrip().startswith("#"):
            out.append(" ".join(" ".join(lines).split()))
            continue
        # a run of list items is a run of separate claims, one per item
        if all(re.match(r"^\s*(?:[-*]|\d+[.)])\s+", ln) for ln in lines):
            items = [re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", ln) for ln in lines]
        else:
            items = [" ".join(" ".join(lines).split())]
        for item in items:
            item = " ".join(item.split())
            parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\*\u201c\"`])", item)
            out += [p.strip() for p in parts if p.strip()]
    return out


def normalise(s):
    s = unicodedata.normalize("NFKC", " ".join(s.split()))
    return re.sub(r"[*_]", "", s)


def page_prose(html_text):
    """The page's prose, captions, rail and generated tables — not the drawers' code."""
    body = re.sub(r"<head>.*?</head>", " ", html_text, flags=re.S)
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r'<details class="code">.*?</details>', " ", body, flags=re.S)
    body = re.sub(r'<details class="out">.*?</details>', " ", body, flags=re.S)
    # the prereg / notebook / red-team drawers are other agents' documents, shown verbatim
    body = re.sub(r'<details class="evidence doc">.*?</details>', " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return body


def main(post):
    post_dir = os.path.join(ROOT, "posts", post)
    results = json.loads(read(os.path.join(post_dir, "data", "processed", "results.json")))
    cmap = json.loads(read(os.path.join(post_dir, "notes", "claims-map.json")))
    post_md = read(os.path.join(post_dir, "POST.md"))
    page_path = os.path.join(ROOT, "site", "posts", post, "index.html")

    failures, checked = [], {"bindings": 0, "sentences": 0, "numbers": 0, "page_numbers": 0}

    index = set()
    index_results(results, index)

    # ---- 1. the claims map resolves against results.json --------------------
    declared = {}
    for c in cmap["claims"]:
        key_sentence = normalise(c["sentence"])
        declared.setdefault(key_sentence, set())
        for b in c["bindings"]:
            checked["bindings"] += 1
            try:
                actual = resolve(results, b["key"])
            except (KeyError, IndexError, TypeError):
                failures.append(f"[map] {c['id']}: results.json has no key {b['key']}")
                continue
            if "value" in b:
                want = b["value"]
                wants = want if isinstance(want, list) else [want]
                acts = actual if isinstance(actual, list) else [actual]
                if len(wants) != len(acts):
                    failures.append(
                        f"[map] {c['id']}: {b['key']} has {len(acts)} value(s), map records {len(wants)}")
                    continue
                for w, a in zip(wants, acts):
                    if isinstance(w, (int, float)) and isinstance(a, (int, float)) \
                            and not isinstance(w, bool) and not isinstance(a, bool):
                        nd = len(str(w).split(".")[1]) if "." in str(w) else 0
                        if round(float(a), nd) != round(float(w), nd):
                            failures.append(
                                f"[map] {c['id']}: {b['key']} is {a}, map records {w}")
                    elif w != a:
                        failures.append(f"[map] {c['id']}: {b['key']} is {a!r}, map records {w!r}")
            index_results(actual, declared[key_sentence])
            for tok in b.get("as_printed", []):
                v = norm_num(str(tok))
                if v is not None:
                    keys_of(v, declared[key_sentence])

    # ---- 2. every quantitative sentence of POST.md is in the map ------------
    mapped = {normalise(c["sentence"]) for c in cmap["claims"]}
    for s in sentences(post_md):
        nums = numbers_in(s)
        if not nums:
            continue
        checked["sentences"] += 1
        if normalise(s) not in mapped:
            failures.append("[unmapped sentence] " + (s[:150] + ("…" if len(s) > 150 else "")))

    # ---- 3. every number in POST.md is bound to its own sentence's entry ----
    for s in sentences(post_md):
        allowed = declared.get(normalise(s), set())
        for tok, v in numbers_in(s):
            checked["numbers"] += 1
            nd = len(tok.split(".")[1]) if "." in tok else 0
            if f"{abs(v):.{nd}f}" not in allowed:
                failures.append(f"[number not bound to this sentence] {tok} in: {s[:110]}")

    if os.path.exists(page_path):
        all_declared = set().union(*declared.values()) if declared else set()
        for tok, v in numbers_in(page_prose(read(page_path))):
            checked["page_numbers"] += 1
            nd = len(tok.split(".")[1]) if "." in tok else 0
            if f"{abs(v):.{nd}f}" not in (index | all_declared):
                failures.append(f"[unbound number on page] {tok}")
    else:
        failures.append(f"[page] not built: {page_path}")

    print(f"verify_page {post}")
    print(f"  claims-map bindings resolved against results.json : {checked['bindings']}")
    print(f"  quantitative sentences in POST.md checked         : {checked['sentences']}")
    print(f"  numbers in POST.md checked against their own entry : {checked['numbers']}")
    print(f"  numbers in the built page's prose checked         : {checked['page_numbers']}")
    if failures:
        print(f"\nFAIL — {len(failures)} problem(s). Fix the text, never the numbers.\n")
        for f in failures:
            print("  " + f)
        return 1
    print("\nPASS — every number on the page is in results.json.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: verify_page.py <post>   e.g. verify_page.py post1")
    sys.exit(main(sys.argv[1]))
