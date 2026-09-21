"""Fetch the Eurostat generative-AI tables and the EU27 population-by-age file for posts/gender1.

    python data/fetch/eurostat_isoc_ai_iaiu.py

Writes to data/cache/eurostat/ (gitignored): the two tables as TSV from the Eurostat SDMX endpoint, the
population-by-age JSON, and a manifest with sha256 and fetch time. If the Eurostat endpoint returns an
HTML page instead of data (it did on 21 September 2026), the script says so and leaves the EIGE export
in place; the EIGE export procedure is recorded in posts/gender1/outputs/audit/eige_export_log.json.
"""
import hashlib, json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "cache", "eurostat")
os.makedirs(OUT, exist_ok=True)
SDMX = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/{table}/?format=TSV&compressed=false"
PJAN = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan"
        "?format=JSON&lang=EN&geo=EU27_2020&time=2025&sex=T&sex=M&sex=F"
        + "".join(f"&age=Y{a}" for a in range(16, 75)))


def fetch(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": "economic_research fetch (research use)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    if data[:200].lstrip().lower().startswith(b"<!doctype html") or b"<html" in data[:300].lower():
        return None, "html page returned instead of data"
    with open(path, "wb") as fh:
        fh.write(data)
    return hashlib.sha256(data).hexdigest(), "ok"


def main():
    manifest = {"fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "files": {}}
    for table in ("isoc_ai_iaiu", "isoc_ai_iaiuxr"):
        path = os.path.join(OUT, f"{table}.tsv")
        sha, status = fetch(SDMX.format(table=table), path)
        manifest["files"][f"{table}.tsv"] = {"url": SDMX.format(table=table), "sha256": sha, "status": status}
        print(table, status, sha or "")
    path = os.path.join(OUT, "demo_pjan_EU27_2025.json")
    sha, status = fetch(PJAN, path)
    manifest["files"]["demo_pjan_EU27_2025.json"] = {"url": PJAN, "sha256": sha, "status": status}
    print("demo_pjan", status, sha or "")
    if status == "ok":
        d = json.load(open(path))
        print("  demo_pjan status flags:", sorted(set(d.get("status", {}).values())) or "none", "| values:", len(d["value"]))
    json.dump(manifest, open(os.path.join(OUT, "MANIFEST.json"), "w"), indent=1)
    if any(v["status"] != "ok" for v in manifest["files"].values()):
        print("One or more fetches failed; the EIGE export (see posts/gender1/outputs/audit/) remains the extract of record.")
        sys.exit(1)


if __name__ == "__main__":
    main()
