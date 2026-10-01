#!/usr/bin/env python3
"""Validate the v1 audit deliverables.

Checks, for the four CSVs in the parent directory:
  * the file parses as CSV and no row is ragged (every row has the header's width);
  * identifier columns are unique and non-empty;
  * coverage.csv distinguishes countries from aggregates and separates
    no-source-found-in-dated-search from NOT-SEARCHED;
  * every URL-looking token in the register and search log is http(s) and well formed;
  * cross-references: every source_id used in coverage.csv and permitted-cells.csv
    exists in source-register.csv;
  * the 14 original indicator IDs from evidence/indicators.csv are all still present.

Exit status is non-zero if any check fails.

Usage:  python3 check_outputs.py
"""

import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
AUDIT = HERE.parent
REGISTER_OF_RECORD = AUDIT.parent / "indicators.csv"

URL_RE = re.compile(r"https?://[^\s;,\)]+")
failures = []


def load(name):
    path = AUDIT / name
    with path.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    for i, row in enumerate(body, start=2):
        if len(row) != len(header):
            failures.append(f"{name}: row {i} has {len(row)} fields, expected {len(header)}")
    dicts = [dict(zip(header, row)) for row in body]
    print(f"{name}: {len(dicts)} rows, {len(header)} columns")
    return header, dicts


def unique(name, rows, key):
    seen = set()
    for row in rows:
        value = row[key].strip()
        if not value:
            failures.append(f"{name}: empty {key}")
        if value in seen:
            failures.append(f"{name}: duplicate {key} {value!r}")
        seen.add(value)
    return seen


def check_urls(name, rows, columns):
    for row in rows:
        for column in columns:
            for url in URL_RE.findall(row.get(column, "")):
                if not url.startswith(("http://", "https://")) or " " in url:
                    failures.append(f"{name}: malformed URL {url!r}")
                if url.count("://") != 1:
                    failures.append(f"{name}: suspicious URL {url!r}")


def main():
    _, register = load("source-register.csv")
    ids = unique("source-register.csv", register, "indicator_id")
    check_urls("source-register.csv", register, ["source_url", "audit_record", "verification_status"])

    allowed_evidence = {
        "file-verified-aggregate", "file-verified-aggregate (incomplete column set)",
        "documentation-verified", "documentation-only", "documentation-only (blocked download)",
        "published-finding-only", "carried-forward-unverified", "blocked (access-gated)",
        "blocked (reuse terms)", "queued-lead", "queued-lead (secondary source)",
    }
    for row in register:
        if row["evidence_level"] not in allowed_evidence:
            failures.append(f"source-register.csv: unexpected evidence_level {row['evidence_level']!r}")
        if not row["sample_family"].strip():
            failures.append(f"source-register.csv: {row['indicator_id']} has no sample_family")

    slots = [row["lead_slot"] for row in register if row["lead_slot"].strip()]
    distinct_slots = sorted({s for s in slots})
    if len(distinct_slots) > 8:
        failures.append(f"more than eight lead slots used: {distinct_slots}")
    print(f"lead slots used: {distinct_slots}")

    _, coverage = load("coverage.csv")
    types = {row["entity_type"] for row in coverage}
    if not any("AGGREGATE" in t for t in types):
        failures.append("coverage.csv: no aggregate rows flagged")
    statuses = {row["status"] for row in coverage}
    for needed in {"NOT-SEARCHED", "no-source-found-in-dated-search", "file-verified-published-cells"}:
        if needed not in statuses:
            failures.append(f"coverage.csv: missing status {needed}")
    for row in coverage:
        for sid in filter(None, row["source_id"].split(";")):
            if sid not in ids:
                failures.append(f"coverage.csv: unknown source_id {sid!r}")
    print(f"coverage statuses: {sorted(statuses)}")

    _, searches = load("search-log.csv")
    unique("search-log.csv", searches, "search_id")
    check_urls("search-log.csv", searches, ["query_or_url"])
    for row in searches:
        for sid in filter(None, row["candidate_ids"].split(";")):
            if sid not in ids:
                failures.append(f"search-log.csv: unknown candidate id {sid!r}")

    _, cells = load("permitted-cells.csv")
    unique("permitted-cells.csv", cells, "cell_id")
    for row in cells:
        if row["source_id"] not in ids:
            failures.append(f"permitted-cells.csv: unknown source_id {row['source_id']!r}")
        for field in ("exact_cell_reference", "denominator", "period", "reuse_condition", "display_rule"):
            if not row[field].strip():
                failures.append(f"permitted-cells.csv: {row['cell_id']} missing {field}")

    with REGISTER_OF_RECORD.open(encoding="utf-8", newline="") as fh:
        original = {row["indicator_id"] for row in csv.DictReader(fh)}
    missing = sorted(original - ids)
    if missing:
        failures.append(f"original indicator IDs dropped: {missing}")
    print(f"original indicator IDs preserved: {len(original - set(missing))}/{len(original)}")

    if failures:
        print("\nFAILURES:")
        for failure in failures:
            print(" -", failure)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
