#!/usr/bin/env python3
"""Extract the gender rows of the Korean 2025 Survey on the Internet Usage
generative-AI tables (English statistical-table volume).

Input: `2025_인터넷이용실태조사_통계표(영문).pdf`, the English statistical table
volume published by the National Information Society Agency (NIA) on the notice
https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=29580&cbIdx=99870
(public aggregate tables; no respondent microdata is read or required).

The script pins the exact file vintage by SHA-256, converts the relevant pages
with `pdftotext -layout` (poppler) and reads the Gender rows of the generative-AI
tables. It exits non-zero if the hash, page layout or expected labels differ.

Usage:
    python3 check_korea.py /path/to/2025_internet_usage_statistical_table_en.pdf

Requires: poppler-utils (`pdftotext`).
"""

import hashlib
import json
import re
import subprocess
import sys

EXPECTED_SHA256 = "12ec5ffec2596bed3162f671231ca3b166f2137031b76095f720d763a988bc00"
EXPECTED_BYTES = 4815170

# printed table number -> (first pdf page, last pdf page, expected table caption fragment)
TABLES = {
    "105": (222, 223, "Generative AI service experience status"),
    "106": (224, 225, "Generative AI service experience activity"),
    "133": (278, 279, "Reasons for not using Generative AI services"),
}

GENDER_LABELS = ("Male", "Female")


def page_text(path, first, last):
    return subprocess.run(
        ["pdftotext", "-layout", "-f", str(first), "-l", str(last), path, "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def parse(text, caption):
    if caption not in text:
        raise SystemExit(f"caption {caption!r} not found on the expected pages")
    base = None
    period = None
    rows = {}
    seen_gender_block = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("BASE:") and base is None:
            base = re.sub(r"\s+", " ", stripped[len("BASE:") :]).strip()
        if stripped.startswith("PERIOD:") and period is None:
            period = re.sub(r"\s+", " ", stripped[len("PERIOD:") :]).strip()
        if re.match(r"^Gender\b", stripped) or "Gender" in line:
            seen_gender_block = True
        for label in GENDER_LABELS:
            # The sex marginal rows appear before the Gender*Age block; keep the first.
            if re.search(rf"\b{label}\b", stripped) and label not in rows:
                numbers = re.findall(r"\d+\.\d+", stripped)
                if numbers:
                    rows[label] = [float(n) for n in numbers]
    if sorted(rows) != ["Female", "Male"]:
        raise SystemExit(f"expected Male/Female rows, found {sorted(rows)}")
    if not seen_gender_block:
        raise SystemExit("no Gender breakdown block found")
    return {"base": base, "period": period, "gender_rows": rows}


def main(path):
    raw = open(path, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256 or len(raw) != EXPECTED_BYTES:
        raise SystemExit(
            "file differs from the audited vintage: "
            f"{len(raw)} bytes, sha256 {digest}; expected {EXPECTED_BYTES} bytes, "
            f"sha256 {EXPECTED_SHA256}. Re-audit before reuse."
        )
    out = {
        "source_id_prefix": "KR_NIA",
        "sample_family": "KR_NIA_INTERNET_2025",
        "provider": "Ministry of Science and ICT / National Information Society Agency (fieldwork: Gallup Korea)",
        "survey": "2025 Survey on the Internet Usage (approved national statistics)",
        "retrieved": "2026-10-01",
        "source_url": "https://www.nia.or.kr/common/board/Download.do?bcIdx=29580&cbIdx=99870&fileNo=2",
        "file_sha256": digest,
        "file_bytes": len(raw),
        "unit_note": "percentages of the stated base; the volume reports no table-level standard errors",
        "tables": {},
    }
    for number, (first, last, caption) in TABLES.items():
        out["tables"][f"Table_{number}"] = dict(
            parse(page_text(path, first, last), caption),
            caption=caption,
            pdf_pages=[first, last],
        )
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
