# Data sources

> **No real patient data is used anywhere in this repo.** The hospital side (`data/synthetic/`) is 100% synthetic. The only real-world identifiers in it are batch numbers, products and manufacturers copied from **public** CDSCO NSQ alerts.

**How the data was fetched:** all public data was fetched politely on **25 Sept 2026** (UTC):
- a custom User-Agent with a contact address (`CONTACT_EMAIL` in `.env`);
- at least 2 s between requests to CDSCO hosts;
- at most 3 retries with exponential backoff;
- TLS verification always on.

Nothing needed a login or CAPTCHA, and nothing was blocked. Every downloaded or derived file is recorded in `data/manifest.csv` (source URL, local path, sha256, bytes, UTC fetch time, HTTP status, content type, page count). `scripts/validate_data.py` re-checks every entry.

## Summary

| Source | Location | Files | Size | Rows | Terms |
|---|---|---|---|---|---|
| CDSCO monthly alert PDFs (Dec 2023 – Jun 2025) | `data/raw/cdsco_alerts/` | 52 PDFs + 2 index CSVs | 19.8 MB | ≈1,900 parsed records | Government of India public notices, redistributed unmodified with source URLs |
| CDSCO NSQ portal (2024-01 – 2026-08) | `data/raw/cdsco_portal/` | 46 JSON + 2 CSV + page snapshot | 3.8 MB | 2,555 (feed) + 1,828 (backfill) | Same public data, via the portal's public JSON endpoints |
| Indian medicine master (subset) | `data/raw/drug_master/` | 1 csv.gz | 0.1 MB | 3,000 | Upstream repo is MIT; see note below |
| CDSCO reference documents | `data/reference/` | 3 PDFs + 1 txt | 26.6 MB | — | Government of India public documents |
| Baseline parse | `data/interim/` | 1 CSV | 0.9 MB | 1,914 rows / 1,908 records | Derived |
| Gold template (June 2025 central) | `data/gold/` | 1 CSV | 20 KB | 57 rows / 55 records | Derived; **unverified** until hand-checked |
| Synthetic hospital | `data/synthetic/hospital/` | 8 tables × (Parquet + CSV) | 17.5 MB | see `data/synthetic/README.md` | Synthetic, seed 42 |
| Ground truth | `data/synthetic/ground_truth/` | 3 CSV | 0.4 MB | 1,309 exposure rows | Synthetic answer key; never loaded into app tables |

## 1. CDSCO monthly alert PDFs (`data/raw/cdsco_alerts/`)

**Source:** the listing pages https://cdsco.gov.in/opencms/opencms/en/Alerts/ and `/en/Latest-Alerts/`, merged and de-duplicated by `num_id`. The listing is saved to `alerts_index.csv` (300 rows).

**How the files are fetched:** each `download_file_division.jsp?num_id=…` link returns a small HTML page with an `<iframe src=…>` that points at the real PDF under `/opencms/resources/UploadCDSCOWeb/…`. The script resolves that iframe and downloads the PDF.

**Selection:**
- Titles must match `NSQ|Not of Standard|Not Standard|Drug Alert|Spurious|Revise` and be released between 2024-01-01 and the fetch date.
- Two named one-offs are always kept: "Samples declared NSQ 2017-2023" and the "NSQ Alert on New Link" notice.
- One title matched the regex only by accident ("…revised GST rate Structure") and was excluded.
- `alerts_selected.csv` records every selection and its status. All 52 were fetched and validated: each starts with `%PDF`, is over 5 KB and opens in pdfplumber.

**Naming:** files are named `YYYY-MM` after the month the alert is **for**, not the release month.
- From Aug 2024 to Dec 2024, CDSCO published "Drug Alert for the Month of …" alongside a separate "State Drug Alert". The non-state PDF is headed "A. CDSCO/Central Laboratories", so it is filed under `central/`.
- From Dec 2023 to Mar 2024 there was no separate state list, so those files are filed under `combined/`.

### Coverage
| Alert month | combined | central | state | spurious |
|---|---|---|---|---|
| 2023-12 | ✅ 12p | — | — | — |
| 2024-01 | ✅ 8p | — | — | — |
| 2024-02 | ✅ 12p | — | — | — |
| 2024-03 | ✅ 7p | — | — | — |
| 2024-04 | — | ✅ 11p | — | ✅ 3p |
| 2024-05 | — | ✅ 9p | ✅ 6p | — |
| 2024-06 | — | ✅ 6p | ✅ 9p | — |
| 2024-07 | — | ✅ 11p | ✅ 3p | — |
| 2024-08 | — | ✅ 8p | ✅ 3p | ✅ 2p |
| 2024-09 | — | ✅ 9p | ✅ 5p | ✅ 2p |
| 2024-10 | — | ✅ 9p | ✅ 9p | ✅ 2p |
| 2024-11 | — | ✅ 8p | ✅ 18p | ✅ 2p |
| 2024-12 | — | ✅ 9p | ✅ 18p | — |
| 2025-01 | — | ✅ 10p | ✅ 22p | — |
| 2025-02 | — | ✅ 6p | ✅ 16p | ✅ 1p |
| 2025-03 | — | ✅ 9p | ✅ 9p | ✅ 1p |
| 2025-04 | — | ✅ 7p | ✅ 22p | ✅ 1p |
| 2025-05 | — | ✅ 7p | ✅ 19p | ✅ 2p |
| 2025-06 | — | ✅ 6p | ✅ 15p | ✅ 2p |
| 2025-07 | — | — | — | — |

**other/** (revised lists, multi-year summary, notices):
- `availability_of_not_standard_quality_nsq_alert_on_new_link_in_cdsco_website.pdf` (1p)
- `drug_alert_for_the_month_of_revised_dec_2023.pdf` (1p)
- `drug_alert_for_the_month_of_revised_jan_2024.pdf` (1p)
- `drug_alert_for_the_month_of_revised_march_2023.pdf` (1p)
- `list_of_drugs_medical_devices_vaccine_and_cosmetics_declared_as_not_of_standard_quality_sp.pdf` (1p)
- `revise_list_drug_alert_january_2025.pdf` (1p)
- `revise_list_drug_alert_may_2025.pdf` (1p)
- `revise_list_drug_alert_november_2024.pdf` (1p)
- `samples_declared_nsq_2017_2023.pdf` (5p)

## 2. CDSCO NSQ portal (`data/raw/cdsco_portal/`)

**Source:** since Aug 2025, monthly lists are published only at https://cdscoonline.gov.in/CDSCO/viewPublicNSQDrug. That page is a jQuery DataTables page backed by **public GET JSON endpoints**, with no login and no CAPTCHA:
- `reportingYears`
- `publicReportingMonths`
- `filteredNsqDrugTable?month=Aug-2026&source=All&tab=nsq`
- `filteredSpuriousDrugTable?…`

**Evidence of the endpoints:** `_network_log.json` lists the endpoints and parameters, taken from the page's inline JS. `viewPublicNSQDrug.html` is a snapshot of the page. A headless-browser XHR capture was attempted but could not run here: the sandbox's Chromium does not trust the egress proxy's CA and fails on every site. TLS checks were not disabled to get around this.

**Outputs:**
- **Raw responses:** `json/YYYY-MM_all_<tab>.json`, one per month and tab.
- **`portal_nsq.csv`:** the product feed, **2025-07 → 2026-08**, 2,555 rows (2,508 NSQ + 47 spurious; 720 from central labs and 1,835 from state labs). It includes **July 2025**, which was never published as a PDF.
- **`portal_backfill_2024-01_2025-06.csv`:** 1,828 rows that overlap the PDF era. They are used **only** to cross-check the PDF parse; don't load them alongside the PDF-derived rows or the same failures will be counted twice.
- **Schema:** `alert_month, source (central | state:<lab or state as reported>), tab (nsq|spurious), product_name, batch_no_raw, mfg_date_raw, exp_date_raw, manufacturer_raw, nsq_result, reporting_lab, record_origin='portal', portal_file, portal_row_no`.

**Rows per month in `portal_nsq.csv`:**

| Month | NSQ | Spurious | | Month | NSQ | Spurious |
|---|---|---|---|---|---|---|
| 2025-07 | 143 | 8 | | 2026-02 | 217 | 4 |
| 2025-08 | 94 | 3 | | 2026-03 | 190 | 1 |
| 2025-09 | 112 | 1 | | 2026-04 | 121 | 2 |
| 2025-10 | 211 | 5 | | 2026-05 | 162 | 2 |
| 2025-11 | 216 | 2 | | 2026-06 | 193 | 0 |
| 2025-12 | 175 | 10 | | 2026-07 | 239 | 1 |
| 2026-01 | 218 | 4 | | 2026-08 | 220 | 1 |

The spurious tab has data only from 2025 onward. For 2026 it lists every month except June.

## 3. Indian medicine master (`data/raw/drug_master/`)

- **Source:** https://github.com/junioralive/Indian-Medicine-Dataset, file `DATA/indian_medicine_data.csv` (253,973 rows, 31.8 MB).
- **Licence:** the repo is **MIT** (`UPSTREAM_LICENSE.txt`). However, the rows appear to be scraped from a commercial e-pharmacy catalogue, and the upstream README doesn't say where they came from. Because redistribution of the underlying data is unclear, **the full CSV is gitignored and not committed.** `make fetch-drugs` re-downloads it.
- **Committed subset:** `drug_master_subset.csv.gz`, 3,000 rows (seed 42).
  - Only brands that are not discontinued.
  - Only five dosage forms: tablet 1,744, injection 480, syrup/suspension 398, capsule 283, drops 95.
  - About half the rows are deliberately drawn from compositions that recur in NSQ lists (paracetamol, telmisartan, pantoprazole, rabeprazole, amoxicillin + clavulanate, methylcobalamin, dexamethasone, ondansetron, cough-syrup combinations, and others).

## 4. Reference documents (`data/reference/`, for Cortex Search citations)

| File | Source | Pages |
|---|---|---|
| `cdsco_guideline_recall_rapid_alert.pdf` | https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/biologicals/4GuidelineRecalRapidAlert.pdf | 23 |
| `cdsco_guidance_document_2022.pdf` | https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/Guidance_doc/CDSCO%20Guidance%20Document.pdf | 1,103 |
| `drugs_and_cosmetics_act_1940_rules_1945.pdf` | CDSCO's official consolidated Act + Rules: https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/acts_rules/2016DrugsandCosmeticsAct1940Rules1945.pdf | 635 |
| `rule65_extract.txt` | Verbatim text of Rule 65 (Conditions of licences), extracted from the PDF above | — |

**Rule 65:** because the official PDF was available, the Indian Kanoon fallback wasn't needed. Rule 65(9)(a)(f) requires the prescription register for Schedule C, H and H1 drugs to record *"the name of the manufacturer of the drug, its batch number and the date of expiry of potency"*.

**Fetch notes:** `cdsco.gov.in` answers HEAD with 403, and `www.cdsco.gov.in` resets connections, so the scripts send GET to the bare host.

## 5. Baseline parse and gold set

**`data/interim/nsq_baseline_parsed.csv`:** the output of `scripts/parse_baseline.py`, a pdfplumber parse. It is **not** the product pipeline, which runs in Snowflake. The parser:
- maps table cells to columns by their x-position under header spans;
- merges continuation rows;
- explodes cells that hold several batches (`batch_group_id`);
- rejoins batches wrapped across lines (`batch_rejoined`);
- pulls out brand names;
- normalises dates to `YYYY-MM`;
- adds `manufacturer_norm`.

**Cross-check against the portal:**
- For the 18 overlapping months, 98.3% of the portal's batch numbers appear in the PDF parse.
- Most misses are rows the PDFs put in the separate spurious lists but the portal's NSQ tab includes.
- Record counts per month are within ±8% of the portal's counts for all 18 months.
- `parse_confidence` < 1 marks rows worth a second look: dates that wouldn't normalise, ambiguous two-line batch cells, text-fallback rows, and rows with no batch printed.

**`data/gold/nsq_2025-06_central_gold.csv`:** 57 rows covering 55 records, pre-filled from the baseline. `verified` and `notes` are **blank on purpose**, to be hand-checked against `central/2025-06_central_nsq.pdf`. `portal_batch_seen` is a hint only.

## Known gaps and caveats

- **CDSCO lists**
  - **July 2025** has no PDF; it exists only on the portal, and is included in `portal_nsq.csv`.
  - **Spurious lists** are missing as separate PDFs for 2024-05, 2024-06, 2024-07, 2024-12 and 2025-01. For 2024-01 to 2024-03, spurious items sit inside the combined list. For Jan 2025, the revised file in `other/` covers NSQ, spurious, adulterated and misbranded items.
  - **No separate state list before May 2024.**
  - **Many states don't submit state NSQ data every month.** State lists range from 3 to 22 pages, and the portal shows a "Pending States" list for each month.
  - **The portal (Aug 2025+) may be partial.** Its month lists can grow as late states report, so re-fetching later may add rows. Its `source` for state rows is the reporting lab or state as printed, not always a clean state name.
  - **Revised lists** in `other/` correct earlier months. The baseline parser does not apply them yet.
  - **Portal vs PDF batch numbers:** the portal sometimes drops leading zeros or keeps "B.No:" prefixes. Normalise both sides before matching.
- **Hospital records (real-world caveat, mirrored in the synthetic data):** batch numbers are often missing from real-world dispensing records. That is why about 15% of synthetic dispensing rows have a blank batch and about 45% are hand-typed.
