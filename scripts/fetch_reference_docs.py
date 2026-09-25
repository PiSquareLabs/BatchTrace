"""Phase E: CDSCO recall / guidance / D&C Rules reference PDFs (for Cortex Search citations).

Note: cdsco.gov.in answers HEAD with 403 and www.cdsco.gov.in resets connections, so we GET
from the bare host. Rule 65 is sourced from CDSCO's official consolidated Act + Rules PDF, and
its text is additionally extracted to rule65_extract.txt (page numbers noted) for easy chunking.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pdfplumber

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, already_have, log, polite_get, record_manifest  # noqa: E402

OUT = DATA / "reference"
DOCS = {
    "cdsco_guideline_recall_rapid_alert.pdf":
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/biologicals/4GuidelineRecalRapidAlert.pdf",
    "cdsco_guidance_document_2022.pdf":
        "https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/Guidance_doc/CDSCO%20Guidance%20Document.pdf",
    "drugs_and_cosmetics_act_1940_rules_1945.pdf":
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/acts_rules/2016DrugsandCosmeticsAct1940Rules1945.pdf",
}
RULES = "drugs_and_cosmetics_act_1940_rules_1945.pdf"


def extract_rule65(pdf_path: Path) -> Path:
    """Find the pages carrying Rule 65 ('Conditions of licences' for retail/wholesale sale)."""
    dest = OUT / "rule65_extract.txt"
    hits = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            t = page.extract_text() or ""
            if re.search(r"\b65\.\s*Conditions? of licences", t, re.I):
                hits.append(i)
        if not hits:
            raise RuntimeError("Rule 65 heading not found")
        start = hits[0]
        chunks = []
        for i in range(start, min(start + 8, len(pdf.pages) + 1)):
            t = pdf.pages[i - 1].extract_text() or ""
            chunks.append(f"--- page {i} ---\n{t}")
            if i > start and re.search(r"(?m)^\W{0,3}(?:65-?A|66)\.\s", t):
                break
    dest.write_text(
        "Drugs and Cosmetics Rules, 1945 — Rule 65 (Conditions of licences), extracted verbatim with pdfplumber\n"
        f"Source: {DOCS[RULES]} (CDSCO official consolidated Act + Rules)\n"
        "Relevant for Bad Batch Tracer: Rule 65 requires sale records of Schedule C/C(1)/H/H1/X drugs to carry\n"
        "the batch number (plus name/address of the purchaser/patient and prescriber for H1/X).\n\n"
        + "\n".join(chunks), encoding="utf-8")
    return dest


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    failed = 0
    for name, url in DOCS.items():
        dest = OUT / name
        if already_have(dest):
            continue
        try:
            r = polite_get(url)
            if r.status_code != 200 or r.content[:4] != b"%PDF":
                raise RuntimeError(f"HTTP {r.status_code} {r.headers.get('Content-Type')}")
            dest.write_bytes(r.content)
            with pdfplumber.open(dest) as pdf:
                pages = len(pdf.pages)
            record_manifest(url, dest, r.status_code, r.headers.get("Content-Type", ""), pages)
            log.info("OK %s (%d pages)", name, pages)
        except Exception as e:  # noqa: BLE001
            failed += 1
            log.error("FAILED %s: %s", name, e)
    rules = OUT / RULES
    if rules.exists():
        ex = extract_rule65(rules)
        record_manifest(DOCS[RULES], ex, 200, "text/plain", notes="derived: Rule 65 pages extracted from the PDF")
        log.info("Rule 65 extract -> %s", ex)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
