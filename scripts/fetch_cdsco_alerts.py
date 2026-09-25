"""Phase B: fetch CDSCO NSQ / spurious / drug-alert PDFs (Jan 2024 -> mid 2025).

1. Scrape the Alerts + Latest-Alerts listing pages -> data/raw/cdsco_alerts/alerts_index.csv
   (falls back to a hard-coded seed list of num_ids if scraping fails).
2. Filter to NSQ-related titles released 2024-01-01 -> today (+ two named one-offs).
3. Classify into central/state/spurious/combined/other and name by the month the alert is FOR.
4. Resolve the jsp wrapper page to the real PDF, download, validate, record in the manifest.

Idempotent: files already present with a matching manifest sha256 are skipped.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote, urljoin

import pdfplumber
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, already_have, load_manifest, log, polite_get, record_manifest, rel  # noqa: E402

BASE = "https://cdsco.gov.in"
LISTING_URLS = [
    f"{BASE}/opencms/opencms/en/Alerts/",
    f"{BASE}/opencms/opencms/en/Latest-Alerts/",
]
JSP = f"{BASE}/opencms/opencms/system/modules/CDSCO.WEB/elements/download_file_division.jsp?num_id="
OUT = DATA / "raw" / "cdsco_alerts"
INDEX_CSV = OUT / "alerts_index.csv"
SELECTED_CSV = OUT / "alerts_selected.csv"

TITLE_RE = re.compile(r"NSQ|Not of Standard|Not Standard|Drug Alert|Spurious|Revise", re.I)
# Titles that hit the regex only by accident (e.g. "revised GST rate") — logged, not fetched.
EXCLUDE_RE = re.compile(r"\bGST\b", re.I)
ALWAYS_KEEP = {"MTE5NTU=", "MTMyNDU="}  # Samples declared NSQ 2017-2023; NSQ-on-new-link notice
FORCE_OTHER = {"MTMyNDU="}
START = date(2024, 1, 1)

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
MONTH_RE = re.compile(
    r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\W{0,3}\s*[-–]?\s*(20\d\d)\b", re.I)

# Fallback if the listing cannot be scraped (verified 25 Sept 2026).
SEED = """
MTI5Mjc=|CDSCO NSQ ALERT FOR THE MONTH OF June 2025
MTI5MjY=|STATE NSQ ALERT FOR THE MONTH OF June 2025
MTI5NTk=|List of spurious Drugs for the month of June-2025
MTI5NjA=|Revise list drug alert May-2025
MTI4NDc=|NSQ ALERT FOR THE MONTH OF MAY-2025
MTI4NDY=|STATE NSQ ALERT FOR THE MONTH OF MAY-2025
MTI4NDU=|Spurious for the Month of May-2025
MTI3Mzg=|Not Of Standard of Quality (NSQ) ALERT FOR THE MONTH OF April-2025
MTI3Mzk=|State NSQ Alert For The Month April-2025
MTI3NDA=|Spurious for the Month of April-2025
MTI3Mzc=|Not of Standard Quality/Spurious for the Month of January 2025 Revised
MTI2NzE=|Revise list drug alert January-2025
MTI2Njk=|NOT OF STANDARD QUALITY (NSQ) ALERT FOR THE MONTH OF MARCH-2025
MTI2Njg=|State NSQ Alert For The Month March-2025
MTI2Njc=|Spurious for the Month of March- 2025
MTI2NzA=|Revise list drug alert November-2024
MTI2MTM=|NSQ ALERT FOR THE MONTH OF Feb-2025
MTI2MTQ=|STATE NSQ ALERT FOR THE MONTH OF FEBRUARY-2025
MTI2MTI=|Spurious for the Month of February-2025
MTI1NTU=|NSQ ALERT FOR THE MONTH OF JANUARY-2025
MTI1NTY=|STATE NSQ ALERT FOR THE MONTH OF JANUARY-2025
MTIzOTM=|Drug Alert for the Month of December 2024
MTIzOTQ=|State Drug Alert for the Month of December 2024
MTIyOTI=|Drug Alert for the Month of November 2024
MTIyOTA=|State Drug Alert for the Month of November 2024
MTIyOTE=|Spurious for the Month of November 2024
MTIyMDQ=|Drug Alert for the Month of October 2024
MTIyMDI=|State Drug Alert for the Month of October 2024
MTIyMDM=|Spurious for the Month of October 2024
MTIwODQ=|Drug Alert for the Month of September 2024
MTIwODM=|State Drug Alert for the Month of September 2024
MTIwODI=|Spurious for the Month of September 2024
MTIwMTA=|Drug Alert for the Month of August 2024
MTIwMTI=|State Drug Alert for the Month of August 2024
MTIwMTE=|Spurious Adulterated Misbranded for the Month of August-2024
MTE2MDA=|NSQ ALERT FOR THE MONTH OF JUlY-2024
MTE2MDE=|STATE NSQ ALERT FOR THE MONTH OF July-2024
MTE0Njg=|NSQ ALERT FOR THE MONTH OF JUNE 2024
MTE0Njc=|State NSQ ALERT FOR THE MONTH OF JUNE 2024
MTEzNzI=|NSQ May 2024 CDSCO Labs
MTEzNzM=|NSQ May 2024 State Labs
MTEyNTY=|NOT OF STANDARD QUALITY ALERT FOR THE MONTH OF APRIL 2024
MTEyNTU=|SPURIOUS ALERT FOR THE MONTH OF APRIL 2024
MTExMTU=|Drug Alert for the Month of March 2024
MTEwMTM=|Drug Alert for the Month of February 2024
MTEwMTQ=|Drug Alert for the Month of Revised Jan 2024
MTA5Mzk=|Drug Alert for the Month of January 2024
MTE5NTU=|Samples declared NSQ 2017-2023
"""


def scrape_listing() -> list[dict]:
    rows: dict[str, dict] = {}
    for url in LISTING_URLS:
        try:
            r = polite_get(url)
            r.raise_for_status()
        except Exception as e:  # noqa: BLE001
            log.error("listing %s failed: %s", url, e)
            continue
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, "lxml")
        for tr in soup.select("table tr"):
            tds = tr.find_all("td")
            a = tr.find("a", href=re.compile(r"num_id="))
            if len(tds) < 3 or not a:
                continue
            num_id = a["href"].split("num_id=")[-1].strip()
            title = re.sub(r"\s+", " ", fix_mojibake(tds[1].get_text(" ", strip=True)))
            rd = tds[2].get_text(strip=True)
            try:
                rd = datetime.strptime(rd, "%Y-%b-%d").date().isoformat()
            except ValueError:
                pass
            rows.setdefault(num_id, {"num_id": num_id, "title": title, "release_date": rd,
                                     "jsp_url": JSP + num_id, "listing": url})
    return list(rows.values())


def fix_mojibake(s: str) -> str:
    """Some listing titles are double-encoded UTF-8 (e.g. 'January\u00e2\u0080\u0093')."""
    if "\u00e2" in s:
        try:
            return s.encode("latin-1").decode("utf-8")
        except UnicodeError:
            pass
    return s


def seed_rows() -> list[dict]:
    out = []
    for line in SEED.strip().splitlines():
        num_id, title = line.split("|", 1)
        out.append({"num_id": num_id, "title": title, "release_date": "",
                    "jsp_url": JSP + num_id, "listing": "seed"})
    return out


def alert_month(title: str) -> str | None:
    m = MONTH_RE.search(title)
    if not m:
        return None
    return f"{m.group(2)}-{MONTHS[m.group(1).lower()[:3]]:02d}"


def slugify(s: str) -> str:
    s = s.encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:90]


def classify(row: dict, state_months: set[str]) -> tuple[str, str]:
    """Return (folder, filename)."""
    t = row["title"]
    month = alert_month(t)
    if row["num_id"] in FORCE_OTHER or re.search(r"revise|20\d\d\s*-\s*20\d\d", t, re.I) or not month:
        if not month and row["num_id"] not in FORCE_OTHER:
            log.warning("could not parse alert month from %r -> other/", t)
        return "other", f"{slugify(t)}.pdf"
    if re.search(r"\bstate\b", t, re.I):
        return "state", f"{month}_state_nsq.pdf"
    if re.search(r"spurious", t, re.I):
        return "spurious", f"{month}_spurious.pdf"
    if re.search(r"NSQ|Not of Standard|Not Standard", t, re.I):
        return "central", f"{month}_central_nsq.pdf"
    if re.search(r"drug alert", t, re.I):
        # Aug-Dec 2024 CDSCO split "Drug Alert" (central labs) and "State Drug Alert";
        # earlier months are one combined list.
        if month in state_months:
            return "central", f"{month}_central_nsq.pdf"
        return "combined", f"{month}_combined.pdf"
    return "other", f"{slugify(t)}.pdf"


def select(rows: list[dict]) -> list[dict]:
    today = date.today().isoformat()
    picked = []
    for r in rows:
        keep = r["num_id"] in ALWAYS_KEEP
        if not keep and TITLE_RE.search(r["title"]):
            if EXCLUDE_RE.search(r["title"]):
                log.info("excluded (off-topic regex hit): %s", r["title"])
                continue
            rd = r["release_date"]
            keep = (not rd) or (START.isoformat() <= rd <= today)
        if keep:
            picked.append(r)
    state_months = {alert_month(r["title"]) for r in picked
                    if re.search(r"\bstate\b", r["title"], re.I) and not re.search(r"revise", r["title"], re.I)}
    seen: dict[str, str] = {}
    for r in picked:
        folder, name = classify(r, state_months)
        path = f"{folder}/{name}"
        if path in seen:  # never overwrite a different alert with the same target name
            stem = name[:-4]
            path = f"{folder}/{stem}_{slugify(r['num_id'])}.pdf"
            log.warning("name clash for %s (%s vs %s) -> %s", name, seen[f'{folder}/{name}'], r["num_id"], path)
        seen[path] = r["num_id"]
        r["folder"], r["target"], r["alert_month"] = folder, path, alert_month(r["title"]) or ""
    return picked


def resolve_pdf_url(jsp_url: str) -> tuple[str, bytes | None, int, str]:
    """Return (pdf_url, pdf_bytes_if_jsp_was_pdf, status, content_type)."""
    r = polite_get(jsp_url)
    ctype = r.headers.get("Content-Type", "")
    if r.status_code != 200:
        return "", None, r.status_code, ctype
    if "pdf" in ctype.lower() or r.content[:4] == b"%PDF":
        return jsp_url, r.content, r.status_code, ctype
    soup = BeautifulSoup(r.text, "lxml")
    tag = soup.find(["iframe", "embed", "object", "a"], attrs={"src": True}) or soup.find(
        ["a", "object"], attrs={"href": True}) or soup.find("object", attrs={"data": True})
    href = tag and (tag.get("src") or tag.get("href") or tag.get("data"))
    if not href:
        m = re.search(r"['\"](/opencms/[^'\"]+\.pdf)['\"]", r.text, re.I)
        href = m.group(1) if m else ""
    if not href:
        return "", None, r.status_code, ctype
    return urljoin(BASE, quote(href.strip(), safe="/:%()&=?,+")), None, r.status_code, ctype


def validate_pdf(path: Path) -> int:
    with open(path, "rb") as f:
        if f.read(4) != b"%PDF":
            raise ValueError("not a PDF (magic bytes)")
    if path.stat().st_size <= 5 * 1024:
        raise ValueError("PDF smaller than 5 KB")
    with pdfplumber.open(path) as pdf:
        return len(pdf.pages)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed-only", action="store_true", help="skip scraping, use the seed list")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    rows = [] if args.seed_only else scrape_listing()
    if not rows:
        log.warning("listing scrape empty -> using seed list")
        rows = seed_rows()
    with open(INDEX_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["num_id", "title", "release_date", "jsp_url"], extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    picked = select(rows)
    log.info("%d listing rows, %d selected", len(rows), len(picked))
    manifest = load_manifest()
    failures = []
    for r in picked:
        dest = OUT / r["target"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        if already_have(dest):
            r["pdf_url"] = manifest.get(rel(dest), {}).get("source_url", "")
            r["status"] = "skipped (sha256 match)"
            continue
        try:
            pdf_url, content, status, ctype = resolve_pdf_url(r["jsp_url"])
            if not pdf_url:
                raise RuntimeError(f"no PDF link in jsp page (HTTP {status})")
            if content is None:
                resp = polite_get(pdf_url)
                status, ctype = resp.status_code, resp.headers.get("Content-Type", "")
                if status != 200:
                    raise RuntimeError(f"HTTP {status} for {pdf_url}")
                content = resp.content
            tmp = dest.with_suffix(".part")
            tmp.write_bytes(content)
            pages = validate_pdf(tmp)
            tmp.replace(dest)
            record_manifest(pdf_url, dest, status, ctype, pages,
                            notes=f"num_id={r['num_id']}; title={r['title']}; released={r['release_date']}")
            r["pdf_url"], r["status"] = pdf_url, f"ok ({pages} pages)"
            log.info("OK %s <- %s", r["target"], r["title"])
        except Exception as e:  # noqa: BLE001
            dest.with_suffix(".part").unlink(missing_ok=True)
            r["status"] = f"FAILED: {e}"
            failures.append(r)
            log.error("FAILED %s (%s): %s", r["num_id"], r["title"], e)

    with open(SELECTED_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["num_id", "title", "release_date", "alert_month", "folder",
                                          "target", "pdf_url", "status"], extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(picked, key=lambda x: x["target"]))
    record_manifest(LISTING_URLS[0], INDEX_CSV, 200, "text/csv", notes="scraped listing index")
    log.info("done: %d selected, %d failed", len(picked), len(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
