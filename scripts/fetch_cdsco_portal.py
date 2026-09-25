"""Phase C: fetch NSQ / spurious lists from the new CDSCO portal (cdscoonline.gov.in).

The page https://cdscoonline.gov.in/CDSCO/viewPublicNSQDrug is a jQuery DataTables page backed
by public GET endpoints (no login, no CAPTCHA):
  /CDSCO/reportingYears?tab=nsq|spurious                    -> ["2019", ...]
  /CDSCO/publicReportingMonths?year=YYYY&tab=nsq|spurious   -> ["Jan", ...]
  /CDSCO/filteredNsqDrugTable?month=Aug-2026&source=All&tab=nsq
  /CDSCO/filteredSpuriousDrugTable?month=Aug-2026&source=All&tab=spurious
`--capture-network` re-records the XHR calls the page makes (headless Playwright) into
data/raw/cdsco_portal/_network_log.json as evidence of how the endpoints were found.

Outputs:
  json/YYYY-MM_all_<tab>.json      raw responses (one per month and tab)
  portal_nsq.csv                   months >= 2025-07 (the product feed; post-PDF era + July 2025 gap)
  portal_backfill_2024-01_2025-06.csv  overlap with the PDF era, for cross-checking the PDF parse only
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, already_have, log, polite_get, record_manifest  # noqa: E402

BASE = "https://cdscoonline.gov.in/CDSCO"
PAGE = f"{BASE}/viewPublicNSQDrug"
OUT = DATA / "raw" / "cdsco_portal"
JSON_DIR = OUT / "json"
FEED_FROM = "2025-07"
BACKFILL_FROM = "2024-01"
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
FIELDS = ["alert_month", "source", "tab", "product_name", "batch_no_raw", "mfg_date_raw", "exp_date_raw",
          "manufacturer_raw", "nsq_result", "reporting_lab", "record_origin", "portal_file", "portal_row_no"]


def get_json(path: str, **params):
    r = polite_get(f"{BASE}/{path}", params=params)
    r.raise_for_status()
    return r, json.loads(r.text)


def capture_network() -> None:
    """Load the page headless, apply one filter, and log every XHR/fetch request."""
    from playwright.sync_api import sync_playwright

    log_rows = []
    with sync_playwright() as p:
        exe = "/opt/pw-browsers/chromium" if Path("/opt/pw-browsers/chromium").exists() else None
        try:
            browser = p.chromium.launch(headless=True, executable_path=exe) if exe else p.chromium.launch(headless=True)
        except Exception:  # noqa: BLE001
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent=__import__("common").USER_AGENT)

        def on_response(resp):
            if resp.request.resource_type in ("xhr", "fetch"):
                body = ""
                try:
                    body = resp.text()[:500]
                except Exception:  # noqa: BLE001
                    pass
                log_rows.append({"method": resp.request.method, "url": resp.url, "status": resp.status,
                                 "content_type": resp.headers.get("content-type", ""), "body_head": body})

        page.on("response", on_response)
        page.goto(PAGE, wait_until="networkidle", timeout=90_000)
        page.wait_for_function("document.querySelectorAll('#repYear option').length > 1", timeout=60_000)
        page.select_option("#repYear", "2026")
        page.wait_for_function("document.querySelectorAll('#repMonth option').length > 1", timeout=60_000)
        page.select_option("#repMonth", "Aug-2026")
        page.select_option("#reportingSource", "All")
        page.click("text=Apply Filter")
        page.wait_for_timeout(5_000)
        browser.close()
    dest = OUT / "_network_log.json"
    dest.write_text(json.dumps(log_rows, indent=1), encoding="utf-8")
    record_manifest(PAGE, dest, 200, "application/json", notes="headless Playwright XHR capture (2026/Aug/All)")
    log.info("captured %d XHR requests -> %s", len(log_rows), dest)


def snapshot_page() -> None:
    """Save the page HTML and the AJAX endpoints its inline JS calls (no-browser evidence)."""
    import re

    r = polite_get(PAGE)
    r.raise_for_status()
    html_dest = OUT / "viewPublicNSQDrug.html"
    html_dest.write_bytes(r.content)
    record_manifest(PAGE, html_dest, r.status_code, r.headers.get("Content-Type", ""), notes="page snapshot")
    endpoints = sorted(set(re.findall(r'url:\s*"(/CDSCO/[^"]+)"', r.text)) |
                       set(re.findall(r'"(/CDSCO/(?:view|filtered|public|states)[A-Za-z]+)"', r.text)))
    dest = OUT / "_network_log.json"
    if dest.exists() and json.loads(dest.read_text(encoding="utf-8")) and isinstance(
            json.loads(dest.read_text(encoding="utf-8")), list):
        return  # keep a real browser capture if one exists
    dest.write_text(json.dumps({
        "method": "static: endpoints parsed from the page's inline jQuery $.ajax calls",
        "why_not_browser_capture": "headless Chromium in the build sandbox does not trust the egress proxy CA "
                                   "(ERR_CERT_AUTHORITY_INVALID on every site); TLS checks were not disabled",
        "endpoints": endpoints,
        "params": {"reportingYears": "tab=nsq|spurious",
                   "publicReportingMonths": "year=YYYY&tab=nsq|spurious",
                   "filteredNsqDrugTable": "month=Mon-YYYY&source=All|State|CDL&tab=nsq",
                   "filteredSpuriousDrugTable": "month=Mon-YYYY&source=All|State|CDL&tab=spurious"},
    }, indent=1), encoding="utf-8")
    record_manifest(PAGE, dest, r.status_code, "application/json", notes="endpoint log from page JS")


def norm_row(r: dict, tab: str, ym: str, fname: str, i: int) -> dict:
    src = (r.get("str_reporting_source") or "").strip()
    lab = (r.get("str_reported_by_lab_or_state") or "").strip()
    source = "central" if "cdsco" in src.lower() else f"state:{lab}" if src else ""
    if tab == "nsq":
        product, manu, result = r.get("str_product_name"), r.get("str_manufactured_by"), r.get("str_nsq_result")
    else:
        product = r.get("product_name_from_dtl") or r.get("str_product_name")
        manu = " | ".join(x for x in (r.get("str_spurious_manufacturer_name"), r.get("str_spurious_manufactured_by")) if x)
        result = r.get("str_nsq_remarks")
    clean = lambda v: " ".join(str(v).split()) if v not in (None, "") else ""  # noqa: E731
    return {"alert_month": ym, "source": source, "tab": tab, "product_name": clean(product),
            "batch_no_raw": clean(r.get("str_batch_no")), "mfg_date_raw": clean(r.get("dt_manufacturing_date")),
            "exp_date_raw": clean(r.get("dt_expiry_date")), "manufacturer_raw": clean(manu),
            "nsq_result": clean(result), "reporting_lab": lab, "record_origin": "portal",
            "portal_file": fname, "portal_row_no": i}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture-network", action="store_true")
    ap.add_argument("--from", dest="start", default=BACKFILL_FROM)
    args = ap.parse_args()
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    if args.capture_network:
        try:
            capture_network()
        except Exception as e:  # noqa: BLE001
            log.warning("browser network capture failed (non-blocking): %s", e)
    snapshot_page()

    got, failed = [], []
    for tab, endpoint in (("nsq", "filteredNsqDrugTable"), ("spurious", "filteredSpuriousDrugTable")):
        _, years = get_json("reportingYears", tab=tab)
        for y in sorted(years):
            if int(y) < int(args.start[:4]):
                continue
            _, months = get_json("publicReportingMonths", year=y, tab=tab)
            for m in months:
                ym = f"{y}-{MON.index(m[:3].title()) + 1:02d}"
                if ym < args.start:
                    continue
                dest = JSON_DIR / f"{ym}_all_{tab}.json"
                if not already_have(dest):
                    try:
                        r, data = get_json(endpoint, month=f"{m}-{y}", source="All", tab=tab)
                        dest.write_text(json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
                        record_manifest(r.url, dest, r.status_code, r.headers.get("Content-Type", ""),
                                        notes=f"{len(data.get('aaData', []))} rows")
                    except Exception as e:  # noqa: BLE001
                        failed.append((ym, tab, str(e)))
                        log.error("FAILED %s %s: %s", ym, tab, e)
                        continue
                got.append((ym, tab, dest))

    feed, backfill = [], []
    for ym, tab, dest in sorted(got):
        rows = json.loads(dest.read_text(encoding="utf-8")).get("aaData", [])
        for i, r in enumerate(rows, 1):
            (feed if ym >= FEED_FROM else backfill).append(norm_row(r, tab, ym, dest.name, i))
    for name, rows in (("portal_nsq.csv", feed), (f"portal_backfill_{BACKFILL_FROM}_2025-06.csv", backfill)):
        p = OUT / name
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(rows)
        record_manifest(f"{BASE}/filtered*DrugTable", p, 200, "text/csv", notes=f"{len(rows)} rows, normalised")
        log.info("%s: %d rows", name, len(rows))

    summary = {}
    for ym, tab, dest in got:
        summary.setdefault(ym, {})[tab] = len(json.loads(dest.read_text(encoding="utf-8")).get("aaData", []))
    (OUT / "_coverage.json").write_text(json.dumps({"generated_utc": datetime.utcnow().isoformat() + "Z",
                                                    "months": dict(sorted(summary.items())),
                                                    "failed": failed}, indent=1), encoding="utf-8")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
