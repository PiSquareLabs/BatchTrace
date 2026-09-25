"""Phase G: synthetic hospital — "Sahyadri Synthetic General Hospital" (fictional, 300 beds).

ALL PATIENT DATA IS SYNTHETIC. Batch numbers in seeded rows are real public CDSCO NSQ batches.

Deterministic for a given --seed. Writes Parquet + CSV to data/synthetic/hospital/ and the
evaluation answer key to data/synthetic/ground_truth/ (never load that into app schemas).

Key modelling choices
- Only QR-scanned dispensing rows carry batch_uid (a link to stock). Manual rows carry a
  hand-typed batch_no_as_recorded (often noisy) and blank rows carry nothing, so the matcher
  has to work from the recorded string, or from product + store + date for blanks.
- ~5% of stock batches are real NSQ batches (seeded); they are dispensed at a reduced rate so
  exposure counts stay realistic. Near-miss decoy batches share product + manufacturer with an
  NSQ batch but differ by 1-2 characters in batch number.
- Scenario batches (A: paediatric oral liquid, B: sterility-failed injectable) are dispensed
  only to their scenario patients, with the lab signals described in the plan.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, log  # noqa: E402

OUT = DATA / "synthetic" / "hospital"
GT = DATA / "synthetic" / "ground_truth"
BASELINE = DATA / "interim" / "nsq_baseline_parsed.csv"
PORTAL = DATA / "raw" / "cdsco_portal" / "portal_nsq.csv"
DRUGS = DATA / "raw" / "drug_master" / "drug_master_subset.csv.gz"

START = pd.Timestamp("2024-01-01")
END = pd.Timestamp("2025-07-31 23:59")
REF_DATE = pd.Timestamp("2025-07-31")
STORES = ["MAIN", "SAT1", "SAT2"]

N_PATIENTS, N_ENCOUNTERS, N_RX = 5000, 20000, 60000
N_NORMAL_PRODUCTS, N_LABS = 1250, 40000
BATCHES_PER_PRODUCT = (3, 7)  # integers in [3, 7) -> mean 4.5
SEEDED_SHARE = 0.05
SEEDED_DISPENSE_WEIGHT = 0.3
DECOY_SHARE = 0.6  # share of seeded products that also get a near-miss decoy batch

WARDS = [  # ward_id, name, store, kind
    ("W01", "Paediatrics", "SAT1", "paed"), ("W02", "PICU", "SAT1", "paed"),
    ("W03", "General Medicine", "MAIN", "adult"), ("W04", "General Surgery", "MAIN", "adult"),
    ("W05", "ICU", "MAIN", "adult"), ("W06", "Obstetrics & Gynaecology", "SAT2", "adult"),
    ("W07", "Orthopaedics", "SAT2", "adult"), ("W08", "Cardiology", "MAIN", "adult"),
    ("W09", "Nephrology", "MAIN", "adult"), ("W10", "Emergency", "MAIN", "any"),
    ("W11", "OPD", "MAIN", "any"), ("W12", "Paediatric OPD", "SAT1", "paed"),
]
DISTRICTS = ["Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alappuzha", "Kottayam", "Idukki",
             "Ernakulam", "Thrissur", "Palakkad", "Malappuram", "Kozhikode", "Kannur", "Kanyakumari",
             "Coimbatore", "Kodagu", "Pune", "Satara"]
DX_ADULT = ["Type 2 diabetes mellitus", "Essential hypertension", "Community-acquired pneumonia",
            "Acute gastroenteritis", "Urinary tract infection", "Dengue fever", "Cellulitis",
            "Chronic kidney disease stage 3", "Acute coronary syndrome", "COPD exacerbation",
            "Fracture neck of femur", "Acute appendicitis", "Anaemia", "Peptic ulcer disease",
            "Post-operative care", "Normal delivery", "Lower segment caesarean section", "Migraine"]
DX_PAED = ["Acute upper respiratory infection", "Acute gastroenteritis with dehydration", "Bronchiolitis",
           "Febrile seizure", "Acute otitis media", "Viral fever", "Pneumonia (paediatric)",
           "Allergic rhinitis", "Worm infestation", "Iron deficiency anaemia (paediatric)"]
LAB_SPEC = {  # test: (unit, ref_low, ref_high, mean, sd)
    "creatinine": ("mg/dL", 0.6, 1.2, 0.9, 0.15),
    "WBC": ("10^9/L", 4.0, 11.0, 7.5, 1.6),
    "temperature": ("degC", 36.1, 37.5, 36.8, 0.3),
    "CRP": ("mg/L", 0.0, 5.0, 3.0, 1.5),
    "ALT": ("U/L", 7.0, 56.0, 28.0, 9.0),
}
PAED_CREAT = (0.2, 0.6, 0.4, 0.07)
H1 = re.compile(r"(?i)cefixime|cefpodoxime|ceftriaxone|cefotaxime|cefepime|ceftazidime|meropenem|imipenem|"
                r"ertapenem|levofloxacin|moxifloxacin|linezolid|alprazolam|tramadol|zolpidem|isoniazid|"
                r"rifampicin|pyrazinamide|ethambutol|clofazimine|piperacillin|colistin|buprenorphine")
OTC = re.compile(r"(?i)^(?:paracetamol|calcium|vitamin|multivitamin|ferrous|folic|zinc|antacid|"
                 r"cetirizine|chlorpheniramine|ors|oral rehydration|povidone|ascorbic)")
FORM_RE = [("injection", r"injection|infusion|\binj\b|vial|ampoule"), ("drops", r"\bdrops?\b"),
           ("syrup", r"syrup|suspension|oral solution|elixir|linctus"), ("capsule", r"capsule"),
           ("tablet", r"tablet")]


def form_of(text: str) -> str:
    t = (text or "").lower()
    for f, p in FORM_RE:
        if re.search(p, t):
            return f
    return "other"


# ------------------------------------------------------------------ helpers
def rand_ts(rng, lo: pd.Timestamp, hi: pd.Timestamp, n: int) -> pd.DatetimeIndex:
    span = (hi - lo).total_seconds()
    return pd.to_datetime(lo) + pd.to_timedelta(rng.random(n) * span, unit="s")


def month_ts(ym: str) -> pd.Timestamp | None:
    try:
        return pd.Timestamp(ym + "-01")
    except (ValueError, TypeError):
        return None


def synth_batch_no(rng, manu: str) -> str:
    letters = re.sub(r"[^A-Z]", "", manu.upper())[:3] or "BT"
    style = rng.integers(0, 5)
    if style == 0:
        return f"{letters}{rng.integers(1000, 99999)}"
    if style == 1:
        return f"{letters[:2]}{rng.integers(22, 26)}-{rng.integers(1, 999):03d}"
    if style == 2:
        return f"{rng.integers(22, 26)}{letters[:1]}{rng.integers(100, 9999)}"
    if style == 3:
        return f"{letters}{rng.integers(22, 26)}{chr(65 + rng.integers(0, 12))}{rng.integers(1, 400):03d}"
    return f"{letters[:1]}{rng.integers(1000000, 9999999)}"


def near_miss(rng, batch: str) -> str:
    """Change 1-2 characters (digit bump / char change) so it's close but not the same batch."""
    chars = list(batch)
    idx = [i for i, c in enumerate(chars) if c.isalnum()]
    if not idx:
        return batch + "1"
    for _ in range(rng.integers(1, 3)):
        i = idx[rng.integers(0, len(idx))]
        c = chars[i]
        if c.isdigit():
            chars[i] = str((int(c) + rng.integers(1, 9)) % 10)
        else:
            chars[i] = chr(65 + (ord(c.upper()) - 65 + rng.integers(1, 25)) % 26)
    out = "".join(chars)
    return out if re.sub(r"[\s\-/.]", "", out).upper() != re.sub(r"[\s\-/.]", "", batch).upper() else out + "A"


def noisify(rng, b: str) -> str:
    """Hand-typing noise: lowercase, hyphen/space changes."""
    ops = rng.permutation(4)[: rng.integers(1, 3)]
    for op in ops:
        if op == 0:
            b = b.lower()
        elif op == 1:
            b = b.replace("-", "") if "-" in b else (b[:3] + "-" + b[3:] if len(b) > 4 else b)
        elif op == 2:
            b = b.replace(" ", "") if " " in b else (b[:2] + " " + b[2:] if len(b) > 3 else b)
        else:
            b = b.replace("/", "-") if "/" in b else b + (" " if rng.random() < 0.5 else "")
    return b


def ocr_swap(rng, b: str) -> str:
    swaps = {"O": "0", "0": "O", "I": "1", "1": "I"}
    pos = [i for i, c in enumerate(b.upper()) if c in swaps]
    if not pos:
        return b
    i = pos[rng.integers(0, len(pos))]
    return b[:i] + swaps[b[i].upper()] + b[i + 1:]


# ------------------------------------------------------------------ NSQ candidates
def nsq_candidates() -> pd.DataFrame:
    b = pd.read_csv(BASELINE, dtype=str, keep_default_na=False)
    b = b[(b.record_type == "nsq") & (b.parse_confidence.astype(float) >= 0.99)
          & (b.batch_no_norm.str.len() >= 4) & ~b.batch_no_norm.str.contains(r"NIL|NOTMENTIONED|NA$", regex=True)]
    b = b.assign(nsq_source_file=b.source_file, nsq_row_no=b.row_no, origin="pdf")
    frames = [b]
    if PORTAL.exists():
        p = pd.read_csv(PORTAL, dtype=str, keep_default_na=False)
        p = p[(p.tab == "nsq") & (p.alert_month <= "2025-07")].copy()
        from parse_baseline import brand_from_product, norm_batch, norm_date, norm_manufacturer
        p = p.assign(batch_no_norm=p.batch_no_raw.map(norm_batch), mfg_date=p.mfg_date_raw.map(norm_date),
                     exp_date=p.exp_date_raw.map(norm_date), brand_name=p.product_name.map(brand_from_product),
                     manufacturer_norm=p.manufacturer_raw.map(norm_manufacturer),
                     nsq_source_file="data/raw/cdsco_portal/json/" + p.portal_file,
                     nsq_row_no=p.portal_row_no, origin="portal", category=p.source)
        p = p[(p.batch_no_norm.str.len() >= 4) & ~p.batch_no_raw.str.contains(r"[,&]")]
        frames.append(p)
    c = pd.concat(frames, ignore_index=True)
    c["mfg_ts"] = c.mfg_date.map(month_ts)
    c["exp_ts"] = c.exp_date.map(month_ts)
    c = c.dropna(subset=["mfg_ts", "exp_ts"])
    # usable inside the hospital window with >= 60 days of shelf time after receipt
    c = c[(c.mfg_ts <= END - pd.Timedelta(days=90)) & (c.exp_ts >= START + pd.Timedelta(days=90))
          & (c.exp_ts > c.mfg_ts)]
    c = c.drop_duplicates("batch_no_norm")
    c["dosage_form"] = c.product_name.map(form_of)
    return c.reset_index(drop=True)


# ------------------------------------------------------------------ main build
def build(seed: int) -> dict[str, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    fake = Faker("en_IN")
    Faker.seed(seed)

    # ---- patients
    n = N_PATIENTS
    paed = rng.random(n) < 0.18
    age_years = np.where(paed, rng.uniform(0.1, 11.99, n), rng.gamma(6.0, 7.5, n).clip(12, 95))
    dob = [(REF_DATE - pd.Timedelta(days=int(a * 365.25))).date() for a in age_years]
    sex = rng.choice(["F", "M"], n)
    names = [fake.name_female() if s == "F" else fake.name_male() for s in sex]
    bands = pd.cut(age_years, [0, 1, 5, 12, 18, 40, 65, 200], right=False,
                   labels=["<1", "1-4", "5-11", "12-17", "18-39", "40-64", "65+"]).astype(str)
    patients = pd.DataFrame({
        "patient_id": [f"P{i:05d}" for i in range(1, n + 1)], "name": names, "sex": sex, "dob": dob,
        "age_band": bands, "is_paediatric": paed,
        "district": rng.choice(DISTRICTS, n, p=np.r_[np.full(12, 0.07), np.full(5, 0.032)]),
        # +91 00xxx... is not a valid Indian mobile number (valid ones start with 6-9)
        "phone": [f"+91-00{rng.integers(0, 1000):03d}-{rng.integers(0, 100000):05d}" for _ in range(n)],
        "preferred_language": rng.choice(["ml", "en", "ta", "hi"], n, p=[0.55, 0.25, 0.12, 0.08]),
    })

    wards = pd.DataFrame(WARDS, columns=["ward_id", "name", "store_id", "kind"])

    # ---- encounters
    pidx = rng.integers(0, n, N_ENCOUNTERS)
    is_p = paed[pidx]
    etype = rng.choice(["OPD", "IPD", "ER"], N_ENCOUNTERS, p=[0.6, 0.28, 0.12])
    paed_w = {"OPD": "W12", "ER": "W10"}
    adult_ipd = ["W03", "W04", "W05", "W06", "W07", "W08", "W09"]
    ward = []
    for p_, t in zip(is_p, etype):
        if p_:
            ward.append(paed_w.get(t) or rng.choice(["W01", "W02"], p=[0.85, 0.15]))
        else:
            ward.append({"OPD": "W11", "ER": "W10"}.get(t) or adult_ipd[rng.integers(0, len(adult_ipd))])
    admit = rand_ts(rng, START, END - pd.Timedelta(days=12), N_ENCOUNTERS)
    los_h = np.where(etype == "IPD", rng.gamma(2.2, 40, N_ENCOUNTERS) + 24,
                     np.where(etype == "ER", rng.uniform(2, 10, N_ENCOUNTERS), rng.uniform(0.3, 2, N_ENCOUNTERS)))
    encounters = pd.DataFrame({
        "encounter_id": [f"E{i:06d}" for i in range(1, N_ENCOUNTERS + 1)],
        "patient_id": patients.patient_id.values[pidx], "ward_id": ward, "type": etype,
        "admit_ts": admit.floor("min"), "discharge_ts": (admit + pd.to_timedelta(los_h, unit="h")).floor("min"),
        "primary_dx_text": [rng.choice(DX_PAED) if p_ else rng.choice(DX_ADULT) for p_ in is_p],
    }).sort_values("admit_ts").reset_index(drop=True)
    encounters["encounter_id"] = [f"E{i:06d}" for i in range(1, len(encounters) + 1)]
    encounters = encounters.merge(wards[["ward_id", "store_id"]], on="ward_id")
    encounters = encounters.sort_values("encounter_id").reset_index(drop=True)

    # ---- products: normal (drug master) + seeded (real NSQ)
    dm = pd.read_csv(DRUGS, dtype=str, keep_default_na=False)
    dm = dm.sample(n=min(N_NORMAL_PRODUCTS, len(dm)), random_state=seed)
    prod_rows = []
    for _, r in dm.iterrows():
        prod_rows.append({"brand_name": r["name"], "generic_composition": r["generic_composition"],
                          "dosage_form": r["dosage_form"], "manufacturer": r["manufacturer_name"],
                          "is_nsq_seeded": False, "_src": "drug_master"})

    cand = nsq_candidates()
    n_normal_batches_est = int(N_NORMAL_PRODUCTS * sum(BATCHES_PER_PRODUCT) / 2)
    n_seeded = int(round(SEEDED_SHARE * n_normal_batches_est / (1 - SEEDED_SHARE * (1 + DECOY_SHARE))))
    # Scenario batches first, then a random draw (oral liquids and injectables over-sampled)
    scen_a = cand[(cand.dosage_form == "syrup") & (cand.exp_ts >= pd.Timestamp("2025-01-01"))
                  & (cand.mfg_ts <= pd.Timestamp("2024-09-01"))].sort_values("batch_no_norm")
    scen_a = scen_a[scen_a.product_name.str.contains(r"(?i)syrup|suspension")]
    scen_b = cand[(cand.dosage_form == "injection") & cand.nsq_result.str.contains(r"(?i)sterility")
                  & (cand.exp_ts >= pd.Timestamp("2025-01-01")) & (cand.mfg_ts <= pd.Timestamp("2024-09-01"))]
    scen_b = scen_b.sort_values("batch_no_norm")
    if scen_a.empty or scen_b.empty:
        raise SystemExit("no candidate NSQ batch for scenario A or B — check the baseline parse")
    # Prefer a real DEG/EG-contaminated syrup for the DEG-like scenario when one is usable
    glycol = scen_a.nsq_result.str.contains(r"(?i)ethylene glycol|\bD?EG\b")
    deg = scen_a[glycol & scen_a.nsq_result.str.contains(r"(?i)exceed|contaminat|found to contain [\d.]+ ?% ?w/v di")]
    a_row = deg.iloc[0] if len(deg) else scen_a.iloc[rng.integers(0, len(scen_a))]
    b_row = scen_b.iloc[rng.integers(0, len(scen_b))]
    rest = cand[~cand.batch_no_norm.isin([a_row.batch_no_norm, b_row.batch_no_norm])]
    w = rest.dosage_form.map({"syrup": 2.0, "injection": 1.5, "drops": 1.5, "tablet": 1.0, "capsule": 1.0}).fillna(0.5)
    picked = rest.sample(n=min(n_seeded - 2, len(rest)), weights=w, random_state=seed)
    seeded = pd.concat([a_row.to_frame().T, b_row.to_frame().T, picked], ignore_index=True)
    seeded["scenario"] = ["A", "B"] + [""] * (len(seeded) - 2)

    seeded_prod_idx = []
    for _, r in seeded.iterrows():
        seeded_prod_idx.append(len(prod_rows))
        prod_rows.append({"brand_name": r.brand_name or r.product_name, "generic_composition": r.product_name,
                          "dosage_form": r.dosage_form if r.dosage_form != "other" else "tablet",
                          "manufacturer": r.manufacturer_raw, "is_nsq_seeded": True, "_src": "nsq"})
    products = pd.DataFrame(prod_rows)
    products.insert(0, "product_id", [f"PR{i:05d}" for i in range(1, len(products) + 1)])

    def schedule(r):
        if r.dosage_form == "injection":
            return "H"
        if H1.search(r.generic_composition):
            return "H1"
        if OTC.search(r.generic_composition) and r.dosage_form in ("tablet", "syrup", "drops"):
            return "OTC"
        return "H"
    products["schedule"] = products.apply(schedule, axis=1)

    # ---- stock batches
    sb = []
    for i, r in products[~products.is_nsq_seeded].iterrows():
        for _ in range(rng.integers(*BATCHES_PER_PRODUCT)):
            recv = START - pd.Timedelta(days=60) + pd.Timedelta(days=int(rng.integers(0, 575)))
            mfg = recv - pd.Timedelta(days=int(rng.integers(30, 240)))
            exp = mfg + pd.DateOffset(months=int(rng.choice([18, 24, 36])))
            sb.append({"product_id": r.product_id, "batch_no": synth_batch_no(rng, r.manufacturer),
                       "mfg_date": mfg.date(), "exp_date": exp.date(), "received_date": recv.date(),
                       "store_id": rng.choice(STORES, p=[0.6, 0.2, 0.2]), "supplier": fake.company(),
                       "is_nsq_batch": False, "is_decoy": False, "_nsq_idx": -1})
    decoy_for = set(rng.choice(len(seeded), int(DECOY_SHARE * len(seeded)), replace=False).tolist())
    for k, (pi, (_, r)) in enumerate(zip(seeded_prod_idx, seeded.iterrows())):
        pid = products.product_id.iloc[pi]
        mfg, exp = r.mfg_ts, r.exp_ts
        lo = max(mfg + pd.Timedelta(days=30), START - pd.Timedelta(days=30))
        hi = min(exp - pd.Timedelta(days=60), END - pd.Timedelta(days=60))
        if r.scenario:  # scenarios need a long in-window shelf life
            hi = min(hi, pd.Timestamp("2024-10-01"))
        recv = lo + pd.Timedelta(days=int(rng.integers(0, max(1, (hi - lo).days))))
        store = "SAT1" if r.scenario == "A" else ("MAIN" if r.scenario == "B" else rng.choice(STORES, p=[0.6, 0.2, 0.2]))
        sb.append({"product_id": pid, "batch_no": r.batch_no_raw, "mfg_date": mfg.date(), "exp_date": exp.date(),
                   "received_date": recv.date(), "store_id": store, "supplier": fake.company(),
                   "is_nsq_batch": True, "is_decoy": False, "_nsq_idx": k})
        if k in decoy_for and not r.scenario:
            drecv = recv + pd.Timedelta(days=int(rng.integers(-90, 90)))
            dmfg = drecv - pd.Timedelta(days=int(rng.integers(30, 200)))
            sb.append({"product_id": pid, "batch_no": near_miss(rng, r.batch_no_raw), "mfg_date": dmfg.date(),
                       "exp_date": (dmfg + pd.DateOffset(months=24)).date(), "received_date": drecv.date(),
                       "store_id": store, "supplier": fake.company(), "is_nsq_batch": False, "is_decoy": True,
                       "_nsq_idx": k})
    stock = pd.DataFrame(sb)
    stock.insert(0, "batch_uid", [f"B{i:06d}" for i in range(1, len(stock) + 1)])
    stock["qty_received"] = rng.choice([100, 200, 250, 500, 1000], len(stock))

    # ---- prescriptions + dispensing
    prod_form = products.set_index("product_id").dosage_form
    stock["form"] = stock.product_id.map(prod_form).values
    stock["recv_ts"] = pd.to_datetime(stock.received_date)
    stock["exp_ts"] = pd.to_datetime(stock.exp_date)
    scen_uids = set(stock[stock._nsq_idx.isin([0, 1]) & stock.is_nsq_batch].batch_uid)
    weight = np.where(stock.batch_uid.isin(scen_uids), 0.0,
                      np.where(stock.is_nsq_batch | stock.is_decoy, SEEDED_DISPENSE_WEIGHT, 1.0))
    liquid = stock.form.isin(["syrup", "drops"]).values
    paed_weight = weight * np.where(liquid, 4.0, np.where(stock.form.isin(["injection"]), 1.0, 0.4))

    enc_w = encounters.type.map({"OPD": 2.0, "IPD": 5.0, "ER": 2.5}).values
    enc_pick = rng.choice(len(encounters), N_RX, p=enc_w / enc_w.sum())
    enc_pick.sort()
    e = encounters.iloc[enc_pick].reset_index(drop=True)
    paed_set = set(patients.patient_id[patients.is_paediatric])
    stay = (e.discharge_ts - e.admit_ts).dt.total_seconds().values
    disp_ts = e.admit_ts + pd.to_timedelta(rng.random(N_RX) * np.maximum(stay, 600), unit="s")
    disp_ts = disp_ts.dt.floor("min")
    recv_np, exp_np = stock.recv_ts.values, stock.exp_ts.values
    store_np = stock.store_id.values
    cache: dict[tuple, tuple] = {}
    chosen = np.empty(N_RX, dtype=np.int64)
    for i in range(N_RX):
        d = disp_ts.iloc[i].normalize()
        is_paed = e.patient_id.iloc[i] in paed_set
        key = (d, e.store_id.iloc[i], is_paed)
        if key not in cache:
            ok = (recv_np <= d.to_datetime64()) & (exp_np > d.to_datetime64()) & (store_np == key[1])
            ww = (paed_weight if is_paed else weight) * ok
            if ww.sum() == 0:  # store has nothing valid that day: fall back to MAIN
                ok = (recv_np <= d.to_datetime64()) & (exp_np > d.to_datetime64())
                ww = (paed_weight if is_paed else weight) * ok
            cache[key] = (np.flatnonzero(ww), ww[ww > 0] / ww[ww > 0].sum())
        idx, pw = cache[key]
        chosen[i] = idx[rng.choice(len(idx), p=pw)]
    rx = pd.DataFrame({
        "encounter_id": e.encounter_id, "patient_id": e.patient_id,
        "product_id": stock.product_id.values[chosen], "_batch": chosen, "dispensed_ts": disp_ts,
        "store_id": stock.store_id.values[chosen],
    })

    # scenario dispenses (appended, then everything re-sorted and re-keyed)
    scen_rows = []
    for tag, n_exp, kind in (("A", 6, "paed"), ("B", 12, "ipd")):
        bidx = int(stock.index[stock.batch_uid.isin(scen_uids) & (stock._nsq_idx == (0 if tag == "A" else 1))][0])
        brow = stock.loc[bidx]
        lo = max(brow.recv_ts + pd.Timedelta(days=5), START + pd.Timedelta(days=20))
        hi = min(brow.exp_ts - pd.Timedelta(days=15), END - pd.Timedelta(days=15))
        if kind == "paed":
            pool = encounters[encounters.patient_id.isin(paed_set) & encounters.ward_id.isin(["W01", "W12"])]
        else:
            pool = encounters[(encounters.type == "IPD") & encounters.ward_id.isin(["W03", "W04", "W05"])]
        pool = pool[(pool.admit_ts >= lo) & (pool.admit_ts <= hi)].drop_duplicates("patient_id")
        pick = pool.sample(n=n_exp, random_state=seed + (1 if tag == "A" else 2))
        for _, enc in pick.iterrows():
            scen_rows.append({"encounter_id": enc.encounter_id, "patient_id": enc.patient_id,
                              "product_id": brow.product_id, "_batch": bidx,
                              "dispensed_ts": (enc.admit_ts + pd.Timedelta(hours=int(rng.integers(1, 20)))).floor("min"),
                              "store_id": brow.store_id, "_scenario": tag})
    rx = pd.concat([rx, pd.DataFrame(scen_rows)], ignore_index=True)
    rx["_scenario"] = rx.get("_scenario", pd.Series(dtype=str)).fillna("")
    rx = rx.sort_values(["dispensed_ts", "encounter_id"]).reset_index(drop=True)
    n_rx = len(rx)
    rx["rx_id"] = [f"RX{i:06d}" for i in range(1, n_rx + 1)]
    rx["disp_id"] = [f"D{i:06d}" for i in range(1, n_rx + 1)]
    form = rx.product_id.map(prod_form)
    rx["dose"] = np.select([form.eq("syrup"), form.eq("drops"), form.eq("injection")],
                           ["5 ml", "10 drops", "1 amp"], "1 tab")
    rx.loc[form.eq("capsule"), "dose"] = "1 cap"
    rx["frequency"] = rng.choice(["OD", "BD", "TDS", "QID", "SOS", "HS"], n_rx, p=[0.3, 0.3, 0.2, 0.05, 0.1, 0.05])
    rx["days"] = rng.choice([1, 3, 5, 7, 10, 14, 30], n_rx, p=[0.1, 0.25, 0.25, 0.2, 0.08, 0.07, 0.05])
    rx["prescriber_id"] = [f"DR{v:03d}" for v in rng.integers(1, 61, n_rx)]
    prescriptions = rx[["rx_id", "encounter_id", "patient_id", "product_id", "dose", "frequency", "days",
                        "prescriber_id"]].copy()

    # capture method + recorded batch
    cap = rng.choice(["qr_scan", "manual", "blank"], n_rx, p=[0.40, 0.45, 0.15])
    true_batch = stock.batch_no.values[rx._batch.values]
    recorded, noisy_flag = [], []
    manual_idx = np.flatnonzero(cap == "manual")
    # 25% of ALL rows noisy -> drawn from manual rows; ~3% of all rows get an O/0 or I/1 swap
    noisy_pick = set(rng.choice(manual_idx, min(len(manual_idx), int(0.25 * n_rx)), replace=False).tolist())
    swap_pick = set(rng.choice(manual_idx, min(len(manual_idx), int(0.03 * n_rx)), replace=False).tolist())
    for i in range(n_rx):
        b = true_batch[i]
        if cap[i] == "blank":
            recorded.append(None)
            noisy_flag.append(False)
            continue
        if cap[i] == "manual":
            if i in noisy_pick:
                b = noisify(rng, b)
            if i in swap_pick:
                b = ocr_swap(rng, b)
        recorded.append(b)
        noisy_flag.append(b != true_batch[i])
    qty = np.where(form.isin(["syrup", "drops", "injection"]), rng.integers(1, 4, n_rx), rx.days.values *
                   pd.Series(rx.frequency).map({"OD": 1, "BD": 2, "TDS": 3, "QID": 4, "SOS": 1, "HS": 1}).values)
    dispensing = pd.DataFrame({
        "disp_id": rx.disp_id, "rx_id": rx.rx_id, "patient_id": rx.patient_id,
        "batch_uid": np.where(cap == "qr_scan", stock.batch_uid.values[rx._batch.values], None),
        "batch_no_as_recorded": recorded, "qty": qty, "dispensed_ts": rx.dispensed_ts,
        "store_id": rx.store_id, "capture_method": cap,
    })

    used = pd.Series(qty).groupby(rx._batch.values).sum()
    stock["qty_on_hand"] = (stock.qty_received - stock.index.map(used).fillna(0).astype(int)).clip(lower=0)
    stock_batches = stock[["batch_uid", "product_id", "batch_no", "mfg_date", "exp_date", "store_id",
                           "qty_received", "qty_on_hand", "received_date", "supplier"]].copy()

    # ---- labs (normal noise) + scenario signals
    lab_enc = encounters.sample(n=N_LABS, replace=True, random_state=seed).reset_index(drop=True)
    tests = rng.choice(list(LAB_SPEC), N_LABS, p=[0.28, 0.27, 0.2, 0.13, 0.12])
    stay = (lab_enc.discharge_ts - lab_enc.admit_ts).dt.total_seconds().values
    coll = lab_enc.admit_ts + pd.to_timedelta(rng.random(N_LABS) * np.maximum(stay, 900), unit="s")
    vals, units, lows, highs = [], [], [], []
    for t, pid in zip(tests, lab_enc.patient_id):
        unit, lo, hi, mu, sd = LAB_SPEC[t]
        if t == "creatinine" and pid in paed_set:
            lo, hi, mu, sd = PAED_CREAT
        v = rng.normal(mu, sd)
        if rng.random() < 0.04:  # ordinary abnormal results unrelated to any NSQ batch
            v = mu + rng.choice([-1, 1]) * rng.uniform(2.5, 4) * sd
        vals.append(round(max(v, 0.05), 2 if t == "creatinine" else 1))
        units.append(unit)
        lows.append(lo)
        highs.append(hi)
    labs = pd.DataFrame({"patient_id": lab_enc.patient_id, "encounter_id": lab_enc.encounter_id, "test": tests,
                         "value": vals, "unit": units, "ref_low": lows, "ref_high": highs,
                         "collected_ts": coll.dt.floor("min")})
    scen_labs, signal = [], {}
    for tag in ("A", "B"):
        sd_rows = rx[rx._scenario == tag]
        sig_patients = set(sd_rows.patient_id.sample(n=3 if tag == "A" else 4, random_state=seed).tolist())
        for _, d in sd_rows.iterrows():
            t0, enc, pid = d.dispensed_ts, d.encounter_id, d.patient_id
            has_signal = pid in sig_patients
            signal[pid] = has_signal
            if tag == "A":
                base = round(rng.uniform(0.3, 0.45), 2)
                scen_labs.append((pid, enc, "creatinine", base, t0 - pd.Timedelta(hours=int(rng.integers(6, 30)))))
                for day in (3, 6, 10) if has_signal else (4, 9):
                    v = base * (rng.uniform(2.2, 3.5) if has_signal and day >= 3 else rng.uniform(0.9, 1.15))
                    if has_signal and day == 3:
                        v = base * rng.uniform(2.05, 2.6)
                    scen_labs.append((pid, enc, "creatinine", round(v, 2), t0 + pd.Timedelta(days=day, hours=int(rng.integers(0, 12)))))
            else:
                scen_labs.append((pid, enc, "WBC", round(rng.uniform(6, 9), 1), t0 - pd.Timedelta(hours=int(rng.integers(2, 12)))))
                scen_labs.append((pid, enc, "temperature", round(rng.uniform(36.6, 37.2), 1), t0 - pd.Timedelta(hours=1)))
                for h in (12, 24, 40):
                    if has_signal:
                        temp = rng.uniform(38.6, 39.8) if h >= 24 else rng.uniform(37.8, 38.4)
                        wbc = rng.uniform(13, 19) if h >= 24 else rng.uniform(10, 12.5)
                    else:
                        temp, wbc = rng.uniform(36.5, 37.4), rng.uniform(5.5, 9.5)
                    ts = t0 + pd.Timedelta(hours=h)
                    scen_labs.append((pid, enc, "temperature", round(temp, 1), ts))
                    scen_labs.append((pid, enc, "WBC", round(wbc, 1), ts + pd.Timedelta(minutes=20)))
    sl = []
    for pid, enc, t, v, ts in scen_labs:
        unit, lo, hi, _, _ = LAB_SPEC[t]
        if t == "creatinine" and pid in paed_set:
            lo, hi = PAED_CREAT[0], PAED_CREAT[1]
        sl.append({"patient_id": pid, "encounter_id": enc, "test": t, "value": v, "unit": unit,
                   "ref_low": lo, "ref_high": hi, "collected_ts": ts.floor("min")})
    labs = pd.concat([labs, pd.DataFrame(sl)], ignore_index=True).sort_values("collected_ts").reset_index(drop=True)
    labs.insert(0, "lab_id", [f"L{i:06d}" for i in range(1, len(labs) + 1)])

    # ---- ground truth (answer key)
    gt = []
    nsq_meta = seeded.reset_index(drop=True)
    for i in range(n_rx):
        brow = stock.iloc[int(rx._batch.iloc[i])]
        if not (brow.is_nsq_batch or brow.is_decoy):
            continue
        m = nsq_meta.iloc[int(brow._nsq_idx)]
        if brow.is_decoy:
            mt = "decoy"
        elif cap[i] == "blank":
            mt = "blank_batch"
        elif noisy_flag[i]:
            mt = "noisy"
        else:
            mt = "exact"
        gt.append({"patient_id": rx.patient_id.iloc[i], "disp_id": rx.disp_id.iloc[i],
                   "true_batch_uid": brow.batch_uid, "true_batch_no": brow.batch_no,
                   "nsq_batch_no": m.batch_no_raw, "nsq_source_file": m.nsq_source_file,
                   "nsq_row_no": m.nsq_row_no, "nsq_origin": m.origin, "match_type": mt,
                   "is_true_exposure": not brow.is_decoy, "capture_method": cap[i],
                   "scenario": rx._scenario.iloc[i],
                   "scenario_signal": signal.get(rx.patient_id.iloc[i], "") if rx._scenario.iloc[i] else ""})
    truth = pd.DataFrame(gt)

    patients = patients.drop(columns=["is_paediatric"])
    wards = wards.drop(columns=["kind"])
    encounters = encounters[["encounter_id", "patient_id", "ward_id", "type", "admit_ts", "discharge_ts",
                             "primary_dx_text"]]
    products = products.drop(columns=["_src"])
    seeded_out = nsq_meta[["batch_no_raw", "batch_no_norm", "product_name", "manufacturer_raw", "mfg_date",
                           "exp_date", "nsq_result", "nsq_source_file", "nsq_row_no", "origin", "scenario"]]
    return {"patients": patients, "wards": wards, "encounters": encounters, "products": products,
            "stock_batches": stock_batches, "prescriptions": prescriptions, "dispensing": dispensing,
            "labs": labs, "_truth": truth, "_seeded": seeded_out,
            "_stock_flags": stock[["batch_uid", "is_nsq_batch", "is_decoy"]]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    t = build(args.seed)
    OUT.mkdir(parents=True, exist_ok=True)
    GT.mkdir(parents=True, exist_ok=True)
    for name in ["patients", "wards", "encounters", "products", "stock_batches", "prescriptions",
                 "dispensing", "labs"]:
        df = t[name]
        df.to_parquet(OUT / f"{name}.parquet", index=False)
        df.to_csv(OUT / f"{name}.csv", index=False)
        log.info("%-14s %6d rows", name, len(df))
    t["_truth"].to_csv(GT / "exposures_truth.csv", index=False)
    t["_seeded"].to_csv(GT / "seeded_nsq_batches.csv", index=False)
    t["_stock_flags"].to_csv(GT / "stock_batch_flags.csv", index=False)
    tr = t["_truth"]
    log.info("ground truth: %d rows, match_type=%s, scenarios=%s", len(tr), tr.match_type.value_counts().to_dict(),
             tr[tr.scenario != ""].groupby("scenario").size().to_dict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
