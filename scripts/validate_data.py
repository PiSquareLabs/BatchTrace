"""Phase H: validate everything the plan promises. Exit 1 on any FAIL.

Writes the report to docs/validation_report.txt as well as stdout.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pdfplumber

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, ROOT, load_manifest, sha256  # noqa: E402

H = DATA / "synthetic" / "hospital"
GT = DATA / "synthetic" / "ground_truth"
REPORT = ROOT / "docs" / "validation_report.txt"
lines: list[str] = []
fails = 0


def check(ok: bool, msg: str, warn: bool = False) -> None:
    global fails
    tag = "PASS" if ok else ("WARN" if warn else "FAIL")
    if not ok and not warn:
        fails += 1
    lines.append(f"[{tag}] {msg}")


def section(t: str) -> None:
    lines.append(f"\n== {t}")


def manifest_checks() -> None:
    section("manifest")
    man = load_manifest()
    missing, bad, skipped, pdf_bad = [], [], [], []
    for path, row in man.items():
        p = ROOT / path
        if not p.exists():
            (skipped if "gitignored" in row.get("notes", "") else missing).append(path)
            continue
        if sha256(p) != row["sha256"]:
            bad.append(path)
        if p.suffix == ".pdf":
            try:
                with pdfplumber.open(p) as pdf:
                    if row.get("pages") and int(row["pages"]) != len(pdf.pages):
                        pdf_bad.append(f"{path} pages {len(pdf.pages)} != {row['pages']}")
            except Exception as e:  # noqa: BLE001
                pdf_bad.append(f"{path}: {e}")
    n_pdf = sum(1 for p in man if p.endswith(".pdf"))
    check(not missing, f"{len(man)} manifest entries exist on disk" + (f" — missing: {missing}" if missing else ""))
    if skipped:
        lines.append(f"[INFO] not in git by design (fetch to recreate): {skipped}")
    check(not bad, "sha256 matches for every file" + (f" — mismatched: {bad}" if bad else ""))
    check(not pdf_bad, f"{n_pdf} PDFs open with pdfplumber and page counts match" + (f" — {pdf_bad}" if pdf_bad else ""))
    alerts = [p for p in man if p.startswith("data/raw/cdsco_alerts/") and p.endswith(".pdf")]
    check(45 <= len(alerts) <= 60, f"{len(alerts)} CDSCO alert PDFs (plan expects ~45-55)")


def baseline_checks() -> None:
    section("baseline NSQ parse (data/interim/nsq_baseline_parsed.csv)")
    b = pd.read_csv(DATA / "interim" / "nsq_baseline_parsed.csv", dtype=str, keep_default_na=False)
    lines.append(f"[INFO] {len(b)} rows, {b.groupby(['source_file', 'row_no']).ngroups} records")
    nsq = b[b.record_type == "nsq"]
    empty = nsq[nsq.batch_no_norm == ""]
    no_batch_in_source = empty[empty.parse_confidence.astype(float) <= 0.2]
    check(len(empty) == len(no_batch_in_source),
          f"no unexplained empty batch_no_norm in NSQ rows ({len(no_batch_in_source)} row(s) have no batch printed "
          f"in the PDF and are flagged parse_confidence<=0.2)")
    check(b.alert_month.between("2023-12", "2025-07").all(), "alert_month within 2023-12..2025-07")
    jun = b[(b.alert_month == "2025-06") & (b.category == "central")]
    n_rec = jun.row_no.nunique()
    check(50 <= n_rec <= 60, f"June 2025 central: {n_rec} records / {len(jun)} rows (published ~55)")
    # rows per month vs. the portal's own count for the same month (central + state lists)
    p = pd.read_csv(DATA / "raw" / "cdsco_portal" / "portal_backfill_2024-01_2025-06.csv", dtype=str,
                    keep_default_na=False)
    pc = p[p.tab == "nsq"].groupby("alert_month").size()
    bc = nsq.groupby("alert_month").apply(lambda d: d.groupby(["source_file", "row_no"]).ngroups)
    sp = b[b.record_type == "spurious"].groupby("alert_month").apply(
        lambda d: d.groupby(["source_file", "row_no"]).ngroups)
    off = []
    for m, n in pc.items():
        got = int(bc.get(m, 0)) + int(sp.get(m, 0))  # portal NSQ tab also carries spurious-list rows
        if abs(got - n) > max(3, 0.08 * n):
            off.append(f"{m}: parsed {got} vs portal {n}")
    check(not off, f"records per month within ±8% of the portal's count for {len(pc)} months"
          + (f" — {off}" if off else ""), warn=True)
    lines.append(f"[INFO] parse_confidence: {b.parse_confidence.value_counts().sort_index().to_dict()}")


def synthetic_checks() -> None:
    section("synthetic hospital")
    t = {n: pd.read_parquet(H / f"{n}.parquet") for n in
         ["patients", "wards", "encounters", "products", "stock_batches", "prescriptions", "dispensing", "labs"]}
    for n, df in t.items():
        csv_rows = sum(1 for _ in open(H / f"{n}.csv", encoding="utf-8")) - 1
        lines.append(f"[INFO] {n}: {len(df)} rows")
        if n not in ("labs", "encounters", "products", "prescriptions", "dispensing"):
            check(csv_rows == len(df), f"{n}: CSV and Parquet row counts agree")
    fk = [("encounters", "patient_id", "patients"), ("encounters", "ward_id", "wards"),
          ("stock_batches", "product_id", "products"), ("prescriptions", "encounter_id", "encounters"),
          ("prescriptions", "patient_id", "patients"), ("prescriptions", "product_id", "products"),
          ("dispensing", "rx_id", "prescriptions"), ("dispensing", "patient_id", "patients"),
          ("labs", "patient_id", "patients"), ("labs", "encounter_id", "encounters")]
    keys = {"patients": "patient_id", "wards": "ward_id", "encounters": "encounter_id", "products": "product_id",
            "prescriptions": "rx_id", "stock_batches": "batch_uid"}
    bad = [f"{c}.{col}" for c, col, parent in fk if not t[c][col].isin(t[parent][keys[parent]]).all()]
    d = t["dispensing"]
    q = d[d.batch_uid.notna()]
    if not q.batch_uid.isin(t["stock_batches"].batch_uid).all():
        bad.append("dispensing.batch_uid")
    check(not bad, "foreign keys resolve" + (f" — broken: {bad}" if bad else ""))
    rxp = t["prescriptions"].set_index("rx_id").patient_id
    check((d.patient_id.values == rxp.loc[d.rx_id].values).all(), "dispensing.patient_id matches its prescription")

    sb = t["stock_batches"].set_index("batch_uid")
    truth = pd.read_csv(GT / "exposures_truth.csv", dtype=str, keep_default_na=False)
    link = pd.concat([q[["disp_id", "batch_uid"]],
                      truth.rename(columns={"true_batch_uid": "batch_uid"})[["disp_id", "batch_uid"]]])
    link = link.drop_duplicates("disp_id").merge(d[["disp_id", "dispensed_ts"]], on="disp_id")
    ts = pd.to_datetime(link.dispensed_ts)
    recv = pd.to_datetime(sb.loc[link.batch_uid, "received_date"].values)
    exp = pd.to_datetime(sb.loc[link.batch_uid, "exp_date"].values)
    outside = int(((ts.values < recv) | (ts.values >= exp)).sum())
    check(outside == 0, f"dispensed_ts inside batch validity for all {len(link)} batch-linked dispenses "
                        f"(QR scans + every seeded/decoy dispense)")
    blank = (d.capture_method == "blank").mean()
    check(0.13 <= blank <= 0.17, f"blank-batch share {blank:.1%} (13-17%)")
    check(d.loc[d.capture_method == "blank", "batch_no_as_recorded"].isna().all()
          and d.loc[d.capture_method != "qr_scan", "batch_uid"].isna().all(), "blank/manual rows carry no batch_uid")
    qr = d[d.capture_method == "qr_scan"]
    exact = (qr.batch_no_as_recorded.values == sb.loc[qr.batch_uid, "batch_no"].values).all()
    check(bool(exact), "QR-scanned rows record the exact batch number")
    flags = pd.read_csv(GT / "stock_batch_flags.csv")
    share = flags.is_nsq_batch.mean()
    check(0.04 <= share <= 0.06, f"seeded NSQ batch share {share:.1%} of stock_batches (4-6%)")
    check(flags.is_decoy.sum() > 0, f"{int(flags.is_decoy.sum())} near-miss decoy batches present")
    nsq_prod = t["products"].set_index("product_id").is_nsq_seeded
    seeded_ok = nsq_prod.loc[sb.loc[flags[flags.is_nsq_batch].batch_uid, "product_id"]].all()
    check(bool(seeded_ok), "every seeded batch belongs to an is_nsq_seeded product")
    noisy = (truth.match_type == "noisy").sum()
    lines.append(f"[INFO] ground truth match_type: {truth.match_type.value_counts().to_dict()} ({noisy} noisy)")

    labs = t["labs"]
    for tag, n_exp, n_sig in (("A", 6, 3), ("B", 12, 4)):
        s = truth[truth.scenario == tag]
        sig = s[s.scenario_signal == "True"]
        ok = len(s) == n_exp and len(sig) == n_sig and s.patient_id.isin(t["patients"].patient_id).all()
        detail = ""
        if tag == "A":
            child = t["patients"].set_index("patient_id").age_band.loc[s.patient_id].isin(["<1", "1-4", "5-11"]).all()
            rises = []
            for _, r in sig.iterrows():
                t0 = pd.Timestamp(d.set_index("disp_id").dispensed_ts[r.disp_id])
                c = labs[(labs.patient_id == r.patient_id) & (labs.test == "creatinine")]
                base = c[c.collected_ts < t0].value
                post = c[(c.collected_ts >= t0 + pd.Timedelta(days=3)) & (c.collected_ts <= t0 + pd.Timedelta(days=11))].value
                rises.append(len(base) > 0 and len(post) > 0 and post.max() > 2 * base.iloc[-1])
            ok = ok and child and all(rises)
            detail = f"; all children={child}; creatinine >2x baseline in 3-10 d for {sum(rises)}/{n_sig}"
        else:
            fev = []
            for _, r in sig.iterrows():
                t0 = pd.Timestamp(d.set_index("disp_id").dispensed_ts[r.disp_id])
                w = labs[(labs.patient_id == r.patient_id) & (labs.collected_ts > t0)
                         & (labs.collected_ts <= t0 + pd.Timedelta(hours=48))]
                fev.append((w[w.test == "temperature"].value > 38.5).any() and (w[w.test == "WBC"].value > 11).any())
            ok = ok and all(fev)
            detail = f"; fever >38.5 C + WBC rise within 48 h for {sum(fev)}/{n_sig}"
        check(ok, f"scenario {tag}: {len(s)} exposed (expect {n_exp}), {len(sig)} with signal (expect {n_sig}){detail}")


def git_checks() -> None:
    section("git hygiene")
    files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    big = [f for f in files if (ROOT / f).exists() and (ROOT / f).stat().st_size > 50 * 1024 * 1024]
    check(not big, f"no tracked file > 50 MB ({len(files)} tracked files)" + (f" — {big}" if big else ""))
    largest = max(files, key=lambda f: (ROOT / f).stat().st_size if (ROOT / f).exists() else 0)
    lines.append(f"[INFO] largest tracked file: {largest} ({(ROOT / largest).stat().st_size / 1e6:.1f} MB)")
    sus = [f for f in files if re.search(r"(?i)env|key|secret|token", f) and f != ".env.example"]
    check(not sus, "no .env / key / secret / token files tracked (.env.example placeholders only)"
          + (f" — {sus}" if sus else ""))
    ex = (ROOT / ".env.example").read_text(encoding="utf-8")
    check(all(not v.strip() or v.strip() == "you@example.com" for v in re.findall(r"=(.*)", ex)),
          ".env.example contains placeholders only")


def main() -> int:
    for fn in (manifest_checks, baseline_checks, synthetic_checks, git_checks):
        try:
            fn()
        except Exception as e:  # noqa: BLE001
            check(False, f"{fn.__name__} crashed: {e!r}")
    lines.append(f"\n{'ALL CHECKS PASSED' if fails == 0 else f'{fails} CHECK(S) FAILED'}")
    out = "\n".join(lines).lstrip()
    print(out)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(out + "\n", encoding="utf-8")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
