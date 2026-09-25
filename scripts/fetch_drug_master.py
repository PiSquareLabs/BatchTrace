"""Phase D: Indian medicine master (junioralive/Indian-Medicine-Dataset) -> trimmed subset.

The full CSV (~32 MB, ~254k rows) is downloaded to data/raw/drug_master/ but gitignored:
the repo is MIT-licensed, yet the rows appear to be scraped from a commercial e-pharmacy
catalogue, so redistribution of the full table is unclear. Only a ~3,000-brand working
subset (drug_master_subset.csv.gz) is committed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, already_have, log, polite_get, record_manifest  # noqa: E402

URL = "https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/DATA/indian_medicine_data.csv"
LICENSE_URL = "https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/LICENSE"
OUT = DATA / "raw" / "drug_master"
FULL = OUT / "indian_medicine_data.csv"
SUBSET = OUT / "drug_master_subset.csv.gz"
TARGET_ROWS = 3000
SEED = 42

# (dosage_form, regex over name + pack label). Order matters: first match wins.
FORMS = [
    ("injection", r"injection|infusion|\bvial\b|ampoule|prefilled"),
    ("drops", r"\bdrops?\b"),
    ("syrup", r"syrup|suspension|oral solution|elixir|\blinctus\b|dry syrup"),
    ("capsule", r"capsule"),
    ("tablet", r"tablet"),
]
# Compositions that recur in CDSCO NSQ lists — deliberately over-represented.
PRIORITY = [
    "paracetamol", "telmisartan", "pantoprazole", "rabeprazole", "amoxycillin", "clavulanic",
    "methylcobalamin", "dexamethasone", "ondansetron", "dextromethorphan", "chlorpheniramine",
    "ambroxol", "cetirizine", "metformin", "glimepiride", "amlodipine", "atorvastatin", "azithromycin",
    "cefixime", "ceftriaxone", "cefpodoxime", "ofloxacin", "ciprofloxacin", "diclofenac", "aceclofenac",
    "ibuprofen", "calcium", "vitamin d3", "folic acid", "ferrous", "omeprazole", "domperidone",
    "montelukast", "levocetirizine", "metronidazole", "albendazole", "ranitidine", "famotidine",
    "sodium chloride", "ringer", "dextrose", "heparin", "oxytocin", "adrenaline", "salbutamol",
    "prednisolone", "methylprednisolone", "gentamicin", "amikacin", "losartan", "glibenclamide",
]


def dosage_form(text: str) -> str | None:
    t = text.lower()
    for form, pat in FORMS:
        if re.search(pat, t):
            return form
    return None


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    if not already_have(FULL):
        r = polite_get(URL)
        r.raise_for_status()
        FULL.write_bytes(r.content)
        record_manifest(URL, FULL, r.status_code, r.headers.get("Content-Type", ""),
                        notes="full upstream CSV — gitignored, not committed (licence of underlying data unclear)")
    lic = OUT / "UPSTREAM_LICENSE.txt"
    if not already_have(lic):
        r = polite_get(LICENSE_URL)
        r.raise_for_status()
        lic.write_bytes(r.content)
        record_manifest(LICENSE_URL, lic, r.status_code, r.headers.get("Content-Type", ""), notes="upstream repo licence")

    df = pd.read_csv(FULL, dtype=str, keep_default_na=False)
    log.info("full master: %d rows", len(df))
    df = df.rename(columns={"price(₹)": "price_inr", "Is_discontinued": "is_discontinued"})
    df = df[df["is_discontinued"].str.upper() == "FALSE"].copy()
    df["dosage_form"] = (df["name"] + " " + df["pack_size_label"]).map(dosage_form)
    df = df[df["dosage_form"].notna()].copy()
    df["generic_composition"] = df[["short_composition1", "short_composition2"]].apply(
        lambda r: " + ".join(x.strip() for x in r if x.strip()), axis=1)
    comp = df["generic_composition"].str.lower()
    df["is_priority"] = comp.map(lambda c: any(p in c for p in PRIORITY))

    # Half the subset from NSQ-relevant compositions (spread across them), half random.
    pri = df[df["is_priority"]]
    per = max(1, (TARGET_ROWS // 2) // len(PRIORITY))
    picks = []
    for p in PRIORITY:
        hit = pri[pri["generic_composition"].str.lower().str.contains(p, regex=False)]
        picks.append(hit.sample(n=min(per, len(hit)), random_state=SEED))
    chosen = pd.concat(picks).drop_duplicates("id")
    rest = df[~df["id"].isin(chosen["id"])]
    chosen = pd.concat([chosen, rest.sample(n=TARGET_ROWS - len(chosen), random_state=SEED)])
    cols = ["id", "name", "price_inr", "manufacturer_name", "type", "pack_size_label",
            "short_composition1", "short_composition2", "generic_composition", "dosage_form", "is_priority"]
    chosen = chosen[cols].sort_values("id", key=lambda s: s.astype(int))
    chosen.to_csv(SUBSET, index=False, compression={"method": "gzip", "mtime": 0})
    record_manifest(URL, SUBSET, 200, "application/gzip",
                    notes=f"{len(chosen)} rows; derived subset (not discontinued, 5 dosage forms, seed {SEED})")
    log.info("subset: %d rows, forms=%s", len(chosen), chosen["dosage_form"].value_counts().to_dict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
