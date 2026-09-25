"""Phase F: local pdfplumber baseline parse of the CDSCO alert PDFs.

NOT the product pipeline (that runs in Snowflake with AI_PARSE_DOCUMENT + AI_COMPLETE); this only
bootstraps the gold labels and gives a comparison baseline.

Handles the known quirks:
- header cells spanning several physical columns -> physical columns grouped under their header;
- continuation pages without a header row -> last layout of the same file is reused;
- wrapped cells split into continuation rows (empty S.No) -> merged into the previous record;
- several batches in one cell ("IEW1480C, IEW-1480B") -> exploded, shared batch_group_id;
- a batch split across lines ("DXT2024120" / "40") -> rejoined, batch_rejoined=true;
- brand in parentheses inside the product name -> brand_name;
- mixed / split date formats -> mfg_date / exp_date normalised to YYYY-MM (raw kept);
- manufacturer_norm (lowercase, no M/s., no punctuation, address after first comma dropped);
- definition paragraphs, totals and footers never become rows (a record needs a serial number
  and a batch or product).
Pages with no detectable table fall back to a text-line parse (low parse_confidence).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import pdfplumber

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, log, rel  # noqa: E402

ALERTS = DATA / "raw" / "cdsco_alerts"
OUT = DATA / "interim" / "nsq_baseline_parsed.csv"
CATEGORIES = ["central", "state", "spurious", "combined"]
FIELDS = ["alert_month", "category", "record_type", "declared_spurious", "source_file", "page_no", "row_no", "serial_no",
          "product_name", "brand_name", "batch_no_raw", "batch_no_norm", "batch_group_id", "batch_rejoined",
          "mfg_date", "exp_date", "mfg_date_raw", "exp_date_raw", "manufacturer_raw", "manufacturer_norm",
          "nsq_result", "reporting_lab", "drawn_by", "section", "extra_raw", "parse_confidence"]

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


# ---------------------------------------------------------------- header -> logical field
def header_field(h: str | None) -> str | None:
    if h is None:
        return None
    k = re.sub(r"[^a-z]", "", h.lower())
    if not k:
        return None
    if k.startswith("sno") or k in ("sn", "sno", "srno", "slno") or k.startswith("snoo"):
        return "serial_no"
    if "batch" in k or k.startswith("bno"):
        return "batch"
    if "expiry" in k:
        return "exp"
    if "manufacturedby" in k or k.startswith("manufacturer"):
        return "manufacturer"
    if "manuf" in k and ("dat" in k or "ing" in k or "actu" in k):
        return "mfg"
    if "nameofdrug" in k or "product" in k or k.startswith("name"):
        return "product"
    if "nsqresult" in k or "reasonforfailure" in k or k.startswith("reason"):
        return "nsq_result"
    if k.startswith("reportedby") or "nameoflab" in k or k == "from":
        return "reporting_lab"
    if k.startswith("drawnby"):
        return "drawn_by"
    if "firm" in k or "remark" in k or "response" in k or "salesoutlet" in k:
        return "extra"
    return None


# ---------------------------------------------------------------- cleaning helpers
def one_line(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def join_wrapped(s: str) -> str:
    """Join wrapped lines; a line ending in '-' is glued to the next without a space."""
    s = re.sub(r"(?<=[A-Za-z0-9])-\n(?=\S)", "-", s or "")
    return one_line(s)


def norm_date(raw: str) -> str:
    s = re.sub(r"\s+", "", raw or "")
    if not s or re.fullmatch(r"(?i)n/?a|nil|-+|notmentioned|notavailable", s):
        return ""
    m = re.search(r"(?i)(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?[-/.,']*(\d{2,4})", s)
    if m:
        y = int(m.group(2))
        y = y + 2000 if y < 100 else y
        return f"{y:04d}-{MONTHS[m.group(1).lower()]:02d}"
    m = re.fullmatch(r"(\d{1,2})[-/.](\d{1,2})[-/.](\d{2,4})", s)  # dd-mm-yyyy
    if m:
        y = int(m.group(3))
        y = y + 2000 if y < 100 else y
        if 1 <= int(m.group(2)) <= 12:
            return f"{y:04d}-{int(m.group(2)):02d}"
    m = re.fullmatch(r"(\d{1,2})[-/.](\d{4}|\d{2})", s)  # mm/yyyy
    if m and 1 <= int(m.group(1)) <= 12:
        y = int(m.group(2))
        y = y + 2000 if y < 100 else y
        return f"{y:04d}-{int(m.group(1)):02d}"
    m = re.fullmatch(r"(\d{4})[-/.](\d{1,2})(?:[-/.]\d{1,2})?", s)  # yyyy-mm(-dd)
    if m and 1 <= int(m.group(2)) <= 12:
        return f"{m.group(1)}-{int(m.group(2)):02d}"
    return ""


BATCH_PREFIX = re.compile(r"(?i)^\s*(?:b\.?\s*no\.?|batch\s*no\.?|batch|lot\s*no\.?)\s*[:.\-]?\s*")


def norm_batch(b: str) -> str:
    b = BATCH_PREFIX.sub("", b or "")
    return re.sub(r"[\s\-\u2010-\u2015\u2212/.]", "", b).upper()


def split_batches(cell: str) -> tuple[list[str], bool, float, str]:
    """Return (batches, rejoined_flag, confidence, notes_stripped_from_cell)."""
    text = re.sub(r"[\u2010-\u2015\u2212]", "-", (cell or "").strip())
    notes = " ".join(one_line(n) for n in re.findall(r"\(([^()]*)\)", text, flags=re.S))
    text = re.sub(r"\s*\([^()]*\)", "", text, flags=re.S)  # "(for Ifosfamide)", "(Two different samples ...)"
    text = BATCH_PREFIX.sub("", text)
    if not text:
        return [], False, 0.0, notes
    if re.search(r"(?i)not\s*(?:mentioned|available)|^n/?a$|^nil$", one_line(text)):
        return [one_line(text)], False, 0.3, notes
    lines = [BATCH_PREFIX.sub("", ln.strip()) for ln in text.split("\n") if ln.strip()]
    has_sep = bool(re.search(r"[,;&]|\band\b", text))
    rejoined, conf = False, 1.0
    merged: list[str] = []
    for ln in lines:
        if not merged:
            merged.append(ln)
            continue
        prev = merged[-1]
        prev_open = not re.search(r"(?:[,;&]|\band)$", prev)
        # With no separator anywhere in the cell, CDSCO lists never put two batches on
        # separate lines (they use commas / '&'), so a line break is a wrap.
        # Exception: two long lines where the second starts with letters looks like a second batch
        # ("MXDY0005" / "RL22070"); a digit-led tail is a wrap ("BT1205B0" / "4072023").
        two_batches = len(prev) >= 6 and len(ln) >= 6 and re.match(r"[A-Za-z]{2}", ln) and re.search(r"\d", ln)
        wrap = not has_sep and " " not in ln and not two_batches
        short = min(len(prev), len(ln)) <= 5 and " " not in ln
        if prev.endswith(("-", "/")) or wrap or (prev_open and short and not re.match(r"[,;&]", ln)):
            merged[-1] = prev + ln  # batch wrapped across lines
            rejoined = True
        else:
            merged.append(ln)
    joined = " , ".join(merged)
    parts = [p.strip(" .:") for p in re.split(r"\s*(?:,|;|&|\band\b)\s*", joined)]
    parts = [BATCH_PREFIX.sub("", p) for p in parts if p.strip(" .:")]
    parts = [p for p in parts if p]
    if len(lines) > 1 and min(len(x) for x in lines) > 5:
        conf = 0.8  # two long lines: wrap-vs-two-batches decided heuristically, worth a look
    return parts or [one_line(text)], rejoined, conf, notes


NON_BRAND = re.compile(r"(?i)^(?:i\.?p\.?|b\.?p\.?|u\.?s\.?p\.?|sr|er|ec|dt|md|er|oral|sugar free|"
                       r"[\d.,/%\s]+(?:mg|mcg|g|ml|iu|%|w/v|w/w|v/v)?.*|.*\b\d+(?:\.\d+)?\s*(?:mg|mcg|ml|iu|%)\b.*)$")


def brand_from_product(p: str) -> str:
    for m in reversed(re.findall(r"\(([^()]{2,60})\)", p or "")):
        cand = m.strip()
        if not NON_BRAND.match(cand) and re.search(r"[A-Za-z]{3,}", cand):
            return re.sub(r"(?i)\s*\b(?:tablets?|capsules?|inj(?:ection)?\.?|syrup|suspension)\s*$", "", cand).strip()
    return ""


def norm_manufacturer(m: str) -> str:
    s = one_line(m).lower()
    s = re.sub(r"^\s*(?:m\s*/\s*s\.?|m/s|messrs\.?)\s*", "", s)
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.split(",")[0]
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- per-file parse
def month_from_name(name: str) -> str:
    m = re.match(r"(\d{4}-\d{2})", name)
    return m.group(1) if m else ""


def section_marks(page) -> list[tuple[float, str]]:
    """Section headings like 'A. CDSCO/Central Laboratories' with their y position."""
    marks = []
    for ln in page.extract_text_lines() if hasattr(page, "extract_text_lines") else []:
        t = ln["text"].strip()
        if re.match(r"^[A-E]\.\s+\S", t) and len(t) < 120:
            marks.append((ln["top"], t))
    return marks


def header_ranges(row: list, cells: list) -> list[tuple[float, str | None]] | None:
    """Logical field start-x positions from a header row's cell bboxes."""
    fields = [header_field(c) for c in row]
    if "batch" not in fields or "serial_no" not in fields[:2]:
        return None
    return [(bbox[0], f) for c, f, bbox in zip(row, fields, cells) if bbox is not None and c and c.strip()]


def field_at(x0: float, x1: float, ranges: list[tuple[float, str | None]]) -> str | None:
    cx = (x0 + x1) / 2
    fld = None
    for start, f in ranges:
        if cx >= start - 1:
            fld = f
    return fld


def parse_file(path: Path, category: str) -> list[dict]:
    records: list[dict] = []
    ranges: list | None = None
    section = ""
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages, 1):
            marks = section_marks(page)
            tables = page.find_tables()
            if not tables:
                records.extend(text_fallback(page, pno, section))
                continue
            for tbl in tables:
                for top, label in marks:
                    if top < tbl.bbox[1]:
                        section = label
                texts = tbl.extract()
                for row, trow in zip(texts, tbl.rows):
                    if not row:
                        continue
                    hr = header_ranges(row, trow.cells)
                    if hr:
                        ranges = hr
                        continue
                    if ranges is None:
                        continue  # banner/total lines before the first header
                    rec = {"serial_no": "", "product": "", "batch": "", "mfg": "", "exp": "",
                           "manufacturer": "", "nsq_result": "", "reporting_lab": "", "drawn_by": "", "extra": ""}
                    for cell, bbox in zip(row, trow.cells):
                        if bbox is None or not cell or not cell.strip():
                            continue
                        fld = field_at(bbox[0], bbox[2], ranges)
                        if fld:
                            rec[fld] = (rec[fld] + "\n" + cell) if rec[fld] else cell
                    serial = one_line(rec["serial_no"]).rstrip(".")
                    has_data = any(one_line(rec[k]) for k in ("product", "batch", "manufacturer", "nsq_result"))
                    if re.fullmatch(r"\d{1,4}", serial) and has_data:
                        rec.update(page_no=pno, section=section, conf=1.0)
                        records.append(rec)
                    elif not serial and has_data and records and records[-1]["page_no"] in (pno, pno - 1):
                        prev = records[-1]  # continuation of a wrapped record
                        for k in ("product", "batch", "mfg", "exp", "manufacturer", "nsq_result",
                                  "reporting_lab", "drawn_by", "extra"):
                            if rec[k]:
                                prev[k] = (prev[k] + "\n" + rec[k]) if prev[k] else rec[k]
    return records


LINE_RE = re.compile(r"^(\d{1,4})\.?\s+(.+?)\s+([A-Z0-9][A-Z0-9\-/]{3,})\s+(\S+)\s+(\S+)\s+(.+)$")


def text_fallback(page, pno: int, section: str) -> list[dict]:
    out = []
    for ln in (page.extract_text() or "").split("\n"):
        m = LINE_RE.match(ln.strip())
        if m and (norm_date(m.group(4)) or norm_date(m.group(5))):
            out.append({"serial_no": m.group(1), "product": m.group(2), "batch": m.group(3), "mfg": m.group(4),
                        "exp": m.group(5), "manufacturer": m.group(6), "nsq_result": "", "reporting_lab": "",
                        "drawn_by": "", "extra": "", "page_no": pno, "section": section, "conf": 0.3})
    return out


def to_rows(recs: list[dict], path: Path, category: str) -> list[dict]:
    rows = []
    month = month_from_name(path.name)
    for n, r in enumerate(recs, 1):
        product = join_wrapped(r["product"])
        result = join_wrapped(r["nsq_result"])
        extra = join_wrapped(r["extra"])
        spurious_list = category == "spurious" or bool(re.search(r"(?i)spurious", r["section"]))
        declared = spurious_list or bool(re.search(r"(?i)spurious|misbrand|adulterat", result))
        batches, rejoined, bconf, bnotes = split_batches(r["batch"])
        if bnotes:
            extra = (extra + " | " if extra else "") + f"batch note: {bnotes}"
        conf = min(r["conf"], bconf if batches else 0.2)
        mfg_raw, exp_raw = join_wrapped(r["mfg"]), join_wrapped(r["exp"])
        mfg, exp = norm_date(mfg_raw), norm_date(exp_raw)
        if (mfg_raw and not mfg) or (exp_raw and not exp):
            conf = min(conf, 0.7)
        base = {
            "alert_month": month, "category": category, "record_type": "spurious" if spurious_list else "nsq",
            "declared_spurious": str(declared).lower(),
            "source_file": rel(path), "page_no": r["page_no"], "row_no": n, "serial_no": one_line(r["serial_no"]).rstrip("."),
            "product_name": product, "brand_name": brand_from_product(product),
            "batch_rejoined": str(rejoined).lower(), "mfg_date": mfg, "exp_date": exp,
            "mfg_date_raw": mfg_raw, "exp_date_raw": exp_raw,
            "manufacturer_raw": join_wrapped(r["manufacturer"]),
            "manufacturer_norm": norm_manufacturer(r["manufacturer"]),
            "nsq_result": result, "reporting_lab": join_wrapped(r["reporting_lab"]),
            "drawn_by": join_wrapped(r["drawn_by"]), "section": r["section"], "extra_raw": extra,
        }
        group = f"{path.stem}-p{r['page_no']}-r{n}"
        for b in batches or [""]:
            rows.append({**base, "batch_no_raw": b, "batch_no_norm": norm_batch(b),
                         "batch_group_id": group if len(batches) > 1 else "",
                         "parse_confidence": round(conf, 2)})
    return rows


def main() -> int:
    all_rows = []
    for cat in CATEGORIES:
        for path in sorted((ALERTS / cat).glob("*.pdf")):
            recs = parse_file(path, cat)
            rows = to_rows(recs, path, cat)
            all_rows.extend(rows)
            log.info("%-40s records=%3d rows=%3d", rel(path).split("cdsco_alerts/")[1], len(recs), len(rows))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(all_rows)
    log.info("wrote %d rows -> %s", len(all_rows), rel(OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
