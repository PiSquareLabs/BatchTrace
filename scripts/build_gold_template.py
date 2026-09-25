"""Phase F: gold template for the June 2025 central NSQ list (to be verified BY HAND).

Pre-filled from the baseline parse. `verified` and `notes` are left blank on purpose — a human
checks each row against the PDF. `portal_batch_seen` is a hint only (does the same normalised
batch appear in the portal backfill for that month?), not a label.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, log  # noqa: E402

SRC = DATA / "interim" / "nsq_baseline_parsed.csv"
PORTAL = DATA / "raw" / "cdsco_portal" / "portal_backfill_2024-01_2025-06.csv"
OUT = DATA / "gold" / "nsq_2025-06_central_gold.csv"
COLS = ["source_file", "page_no", "row_no", "serial_no", "product_name", "brand_name", "batch_no_raw",
        "batch_no_norm", "batch_group_id", "batch_rejoined", "mfg_date", "exp_date", "manufacturer_raw",
        "manufacturer_norm", "nsq_result", "reporting_lab", "declared_spurious", "parse_confidence"]


def pnorm(s: str) -> str:
    s = re.sub(r"(?i)^\s*b\.?\s*no\.?\s*:?", "", s or "")
    return re.sub(r"[\s\-/.]", "", s).upper().lstrip("0")


def main() -> int:
    df = pd.read_csv(SRC, dtype=str, keep_default_na=False)
    g = df[(df.alert_month == "2025-06") & (df.category == "central")][COLS].copy()
    portal = pd.read_csv(PORTAL, dtype=str, keep_default_na=False)
    seen: set[str] = set()
    for raw in portal[portal.alert_month == "2025-06"].batch_no_raw:
        seen.update(pnorm(p) for p in re.split(r"[,&;]", raw) if p.strip())
    g["portal_batch_seen"] = g.batch_no_norm.map(lambda b: str(b.lstrip("0") in seen).lower())
    g.insert(0, "gold_id", [f"G{i:03d}" for i in range(1, len(g) + 1)])
    g["verified"] = ""
    g["notes"] = ""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    g.to_csv(OUT, index=False)
    log.info("gold template: %d rows (%d records) -> %s — UNVERIFIED, check by hand against the PDF",
             len(g), g.serial_no.nunique(), OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
