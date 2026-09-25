"""Print a per-month coverage table (Markdown) of the CDSCO alert PDFs on disk."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, load_manifest, rel  # noqa: E402

ALERTS = DATA / "raw" / "cdsco_alerts"
CATS = ["combined", "central", "state", "spurious"]


def months(start: str = "2023-12", end: str = "2025-07") -> list[str]:
    y, m = map(int, start.split("-"))
    out = []
    while f"{y}-{m:02d}" <= end:
        out.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def table() -> str:
    man = load_manifest()
    lines = ["| Alert month | " + " | ".join(CATS) + " |", "|---|" + "---|" * len(CATS)]
    for mo in months():
        cells = []
        for c in CATS:
            hits = sorted((ALERTS / c).glob(f"{mo}_*.pdf"))
            if hits:
                pages = [man.get(rel(h), {}).get("pages", "?") for h in hits]
                cells.append("✅ " + ", ".join(f"{p}p" for p in pages))
            else:
                cells.append("—")
        lines.append(f"| {mo} | " + " | ".join(cells) + " |")
    others = sorted((ALERTS / "other").glob("*.pdf"))
    lines.append("")
    lines.append("**other/** (revised lists, multi-year summary, notices):")
    lines.extend(f"- `{o.name}` ({man.get(rel(o), {}).get('pages', '?')}p)" for o in others)
    return "\n".join(lines)


if __name__ == "__main__":
    print(table())
