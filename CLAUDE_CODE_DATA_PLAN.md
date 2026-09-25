# Bad Batch Tracer — Data Acquisition Plan (for Claude Code)

> **How to use:** Put this file in the root of your repo and tell Claude Code:
> *"Read CLAUDE_CODE_DATA_PLAN.md and execute it phase by phase. Stop at every ⛔ checkpoint and ask me before continuing."*

---

## 0. Context for Claude Code (read first)

We are building **Bad Batch Tracer** for the Snowflake CoCo CLI Hackathon 2026 (GCC Edition), Track 4 (Patient 360 & Clinical/Regulatory Copilot).

The product reads India's monthly CDSCO "Not of Standard Quality" (NSQ) drug alerts and matches the failed batches against a hospital's dispensing records. It then lists exposed patients and flags them for follow-up.

This plan covers **only data acquisition and preparation**. It fetches the public data, builds a synthetic hospital, creates a hand-verified gold set, and commits all of it to GitHub so it is ready to load into Snowflake on activation day.

**Hard rules**
1. **Public data only**, fetched politely:
   - Custom User-Agent (`BadBatchTracer-Hackathon/0.1 (contact: <my email>)`).
   - **≥ 2 s delay** between requests to cdsco.gov.in.
   - Max 3 retries with exponential backoff.
   - Never bypass logins, CAPTCHAs or blocks. If blocked → log it and move on.
2. **No real patient data, ever.** The patient side is 100% synthetic (a track requirement).
3. **Reproducible.** Every download is recorded in `data/manifest.csv` (source URL, local path, sha256, bytes, fetched_at UTC, http status). Scripts are idempotent: they skip files already present with a matching sha256.
4. **Don't silently disable SSL verification.** If cdsco.gov.in has cert issues, stop and ask (⛔).
5. **Git hygiene:**
   - No file > 50 MB in git. Compress or use Git LFS, and ask first.
   - Never commit secrets (`.env`, Kaggle tokens, Snowflake creds).
6. Python 3.11+, `uv` or `pip`. Pin versions in `requirements.txt`.

---

## 1. Target repo layout

```
bad-batch-tracer/
├── README.md
├── CLAUDE_CODE_DATA_PLAN.md          ← this file
├── requirements.txt
├── Makefile                          ← make fetch / make synth / make validate
├── .gitignore                        ← .env, .venv, __pycache__, *.log, data/tmp/
├── .env.example                      ← placeholders only
├── docs/
│   └── DATA_SOURCES.md               ← provenance, licences, known gaps
├── data/
│   ├── manifest.csv
│   ├── raw/
│   │   ├── cdsco_alerts/
│   │   │   ├── central/              ← YYYY-MM_central_nsq.pdf
│   │   │   ├── state/                ← YYYY-MM_state_nsq.pdf
│   │   │   ├── spurious/             ← YYYY-MM_spurious.pdf
│   │   │   ├── combined/             ← pre-2025 "Drug Alert for the month of …" (central+state in one)
│   │   │   └── other/                ← revised lists, multi-year summaries, notices
│   │   ├── cdsco_portal/             ← Aug-2025 onward from new portal (json/html + csv)
│   │   └── drug_master/              ← Indian medicine master CSV
│   ├── reference/                    ← CDSCO recall guideline + guidance PDFs (for Cortex Search citations)
│   ├── interim/
│   │   └── nsq_baseline_parsed.csv   ← local pdfplumber parse (baseline, NOT the product pipeline)
│   ├── gold/
│   │   └── nsq_2025-06_central_gold.csv  ← hand-verified labels for accuracy eval
│   └── synthetic/
│       ├── hospital/                 ← patients, dispensing, stock, labs …
│       └── ground_truth/             ← exposures answer key (NOT loaded into app tables)
├── scripts/
│   ├── common.py                     ← http session, polite fetch, manifest writer, sha256
│   ├── fetch_cdsco_alerts.py
│   ├── fetch_cdsco_portal.py
│   ├── fetch_drug_master.py
│   ├── fetch_reference_docs.py
│   ├── parse_baseline.py
│   ├── build_gold_template.py
│   ├── generate_synthetic_hospital.py
│   └── validate_data.py
└── snowflake/
    └── README.md                     ← placeholder: load steps come after trial activation (27 Sept)
```

---

## 2. Phase A — Repo setup

1. `git init` (or clone mine; ⛔ ask me for the repo URL and confirm `gh auth status` works).
2. Create the layout above, plus `requirements.txt`: `requests`, `beautifulsoup4`, `lxml`, `pdfplumber`, `pandas`, `pyarrow`, `faker`, `numpy`, `rapidfuzz`, `playwright`, `python-dotenv`, `tqdm`.
3. Write `scripts/common.py` with:
   - `polite_get(url, **kw)`: a session with the User-Agent, 2 s delay for cdsco hosts, retries and timeout=60.
   - `record_manifest(...)`, `sha256(path)`.
4. Commit: `chore: scaffold repo and data tooling`.

**Done when:** the tree exists, `pip install -r requirements.txt` works, and the first commit is pushed.

---

## 3. Phase B — CDSCO alert PDFs (primary data, Jan 2024 → Jun/Jul 2025)

### How the site works (already verified)
- **Listing page:** `https://cdsco.gov.in/opencms/opencms/en/Alerts/`. It is an HTML table with columns *S.no | Title | Release Date | Download Pdf | Pdf Size*.
- **Download links** look like `https://cdsco.gov.in/opencms/opencms/system/modules/CDSCO.WEB/elements/download_file_division.jsp?num_id=<base64>`.
- ⚠️ **That jsp link returns a small HTML page, not the PDF.** The page contains a relative link to the real file, e.g. `/opencms/resources/UploadCDSCOWeb/2018/UploadAlertsFiles/CDSCO NSQ june25.pdf`.
  - Parse that href.
  - URL-encode spaces.
  - Prefix `https://cdsco.gov.in`.
  - Download.
  - If the jsp response is already `application/pdf`, save it directly.
- Also scrape `https://cdsco.gov.in/opencms/opencms/en/Latest-Alerts/` and merge, de-duplicating by `num_id`.

### Steps
1. Scrape both listing pages into `data/raw/cdsco_alerts/alerts_index.csv` with columns `num_id, title, release_date, jsp_url`.
2. **Filter** titles with the regex (case-insensitive) `NSQ|Not of Standard|Not Standard|Drug Alert|Spurious|Revise`.
   - Keep release dates **2024-01-01 → today**.
   - Also keep the one-off **"Samples declared NSQ 2017-2023"** (`num_id=MTE5NTU=`).
   - Also keep the notice **"Availability of NSQ Alert on New Link"** (`num_id=MTMyNDU=`), saved to `other/`.
3. **Classify and rename** each file:

   | Title pattern | Folder | Name |
   |---|---|---|
   | `STATE` + NSQ | `state/` | `YYYY-MM_state_nsq.pdf` |
   | `Spurious` | `spurious/` | `YYYY-MM_spurious.pdf` |
   | `NSQ` / `Not of Standard` (not state) | `central/` | `YYYY-MM_central_nsq.pdf` |
   | `Drug Alert for the Month` (pre-2025 combined) | `combined/` | `YYYY-MM_combined.pdf` |
   | `Revise…`, multi-year, notices | `other/` | slugified title |

   `YYYY-MM` is the month **the alert is for** (parsed from the title, e.g. "…MONTH OF June 2025" → `2025-06`), not the release date. If the title can't be parsed → put it in `other/` and log it.
4. Download, record each file in the manifest, and validate:
   - Each file starts with `%PDF`.
   - Size > 5 KB.
   - Opens with pdfplumber.
   - Record the page count in the manifest.
5. **Seed list fallback.** If scraping the listing fails, use these known `num_id`s (verified 25 Sept 2026):

   ```
   MTI5Mjc= CDSCO NSQ Jun-2025        MTI5MjY= STATE NSQ Jun-2025       MTI5NTk= Spurious Jun-2025
   MTI5NjA= Revised list May-2025      MTI4NDc= NSQ May-2025             MTI4NDY= STATE NSQ May-2025
   MTI4NDU= Spurious May-2025          MTI3Mzg= NSQ Apr-2025             MTI3Mzk= STATE NSQ Apr-2025
   MTI3NDA= Spurious Apr-2025          MTI3Mzc= Jan-2025 revised         MTI2NzE= Revised Jan-2025
   MTI2Njk= NSQ Mar-2025               MTI2Njg= STATE NSQ Mar-2025       MTI2Njc= Spurious Mar-2025
   MTI2NzA= Revised Nov-2024           MTI2MTM= NSQ Feb-2025             MTI2MTQ= STATE NSQ Feb-2025
   MTI2MTI= Spurious Feb-2025          MTI1NTU= NSQ Jan-2025             MTI1NTY= STATE NSQ Jan-2025
   MTIzOTM= Drug Alert Dec-2024        MTIzOTQ= State Drug Alert Dec-2024
   MTIyOTI= Drug Alert Nov-2024        MTIyOTA= State Drug Alert Nov-2024 MTIyOTE= Spurious Nov-2024
   MTIyMDQ= Drug Alert Oct-2024        MTIyMDI= State Drug Alert Oct-2024 MTIyMDM= Spurious Oct-2024
   MTIwODQ= Drug Alert Sep-2024        MTIwODM= State Drug Alert Sep-2024 MTIwODI= Spurious Sep-2024
   MTIwMTA= Drug Alert Aug-2024        MTIwMTI= State Drug Alert Aug-2024 MTIwMTE= Spurious/Adult./Misbr. Aug-2024
   MTE2MDA= NSQ Jul-2024               MTE2MDE= STATE NSQ Jul-2024
   MTE0Njg= NSQ Jun-2024               MTE0Njc= STATE NSQ Jun-2024
   MTEzNzI= NSQ May-2024 CDSCO labs    MTEzNzM= NSQ May-2024 State labs
   MTEyNTY= NSQ Apr-2024               MTEyNTU= Spurious Apr-2024
   MTExMTU= Drug Alert Mar-2024        MTEwMTM= Drug Alert Feb-2024
   MTEwMTQ= Drug Alert Jan-2024 (rev)  MTA5Mzk= Drug Alert Jan-2024
   MTE5NTU= Samples declared NSQ 2017-2023
   ```

6. Commit: `data: add CDSCO NSQ/spurious alert PDFs 2024-01..2025-07 + manifest`.

**Done when:**
- About 45–55 PDFs are saved, all valid, all in the manifest.
- `docs/DATA_SOURCES.md` lists which months are present or missing per category.
- Total size is well under 50 MB (expect about 15 MB).

⛔ **Checkpoint:** show me the per-month coverage table before moving on.

---

## 4. Phase C — New CDSCO NSQ portal (Aug 2025 → latest, e.g. Aug 2026)

Since August 2025, new monthly lists appear only on the portal at `https://cdscoonline.gov.in/CDSCO/viewPublicNSQDrug`. It is a JS-rendered page with filters for **Select Year, Select Month, Reporting Source** (plus NSQ Drugs / Spurious Drugs tabs). It has no export button. This is the freshest data (e.g. 220 NSQ samples for August 2026), so it's worth the effort, but it is **not blocking**.

**Steps**
1. `playwright install chromium`. Open the page **headed** first, with network logging on.
2. Apply one filter (e.g. 2026 / August / all sources) and **capture the XHR/fetch requests** the page makes. Save them to `data/raw/cdsco_portal/_network_log.json`.
3. **If a JSON endpoint exists:**
   - Replay it with `requests` for each (year, month, source, tab) from 2025-08 to the latest month.
   - Save the raw JSON to `data/raw/cdsco_portal/json/YYYY-MM_<source>_<tab>.json`.
   - Normalise to `data/raw/cdsco_portal/portal_nsq.csv`.
   - Keep the 2 s politeness delay.
4. **If there is no JSON endpoint:**
   - Drive the filters with Playwright.
   - Read the rendered table and handle pagination.
   - Save the HTML snapshot plus a CSV per month.
5. **If there's a CAPTCHA, a login, or an explicit block:**
   - ⛔ Stop and tell me. Do not work around it.
   - Fallback: I'll manually save the pages via my browser ("Save as HTML"), and you parse those.
6. Target CSV columns (same schema as the PDF baseline): `alert_month, source (central|state:<STATE>), tab (nsq|spurious), product_name, batch_no_raw, mfg_date_raw, exp_date_raw, manufacturer_raw, nsq_result, reporting_lab, record_origin='portal'`.
7. Commit: `data: add CDSCO NSQ portal extracts 2025-08..<latest>`.

⛔ **Checkpoint:** report which months and sources you got, and any that failed.

---

## 5. Phase D — Indian drug master (for realistic synthetic brands)

**Primary source (no auth needed):** GitHub `junioralive/Indian-Medicine-Dataset`.
- File: `https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/DATA/indian_medicine_data.csv`
- Columns: `id, name, price(₹), Is_discontinued, manufacturer_name, type, pack_size_label, short_composition1, short_composition2`.

**Alternative:** Kaggle "A-Z Medicine Dataset of India" (~250k rows, Nov 2022). It needs `~/.kaggle/kaggle.json`; ⛔ ask me before using Kaggle.

**Steps**
1. Download to `data/raw/drug_master/indian_medicine_data.csv`.
2. **Check the licence** in the source repo's LICENSE or README.
   - If redistribution is unclear, **don't commit the full file**. Commit the fetch script, gitignore the full CSV, and commit a trimmed working subset instead (`drug_master_subset.csv.gz`, see step 3).
3. Build `data/raw/drug_master/drug_master_subset.csv.gz`:
   - `is_discontinued == FALSE`.
   - Keep dosage forms relevant to the demo: tablets, capsules, syrups/suspensions, injections, drops.
   - Keep about 3,000 brands, deliberately **including** compositions that appear in the NSQ PDFs (paracetamol, telmisartan, pantoprazole, rabeprazole, amoxicillin+clavulanate, methylcobalamin, dexamethasone, ondansetron, cough syrups, etc.).
4. Record everything in the manifest and add the licence note to `docs/DATA_SOURCES.md`.
5. Commit: `data: add Indian drug master subset`.

---

## 6. Phase E — Reference documents (for Cortex Search citations)

Download to `data/reference/`:
- CDSCO *Guidelines on Recall and Rapid Alert System for Drugs*: `https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/biologicals/4GuidelineRecalRapidAlert.pdf`
- CDSCO *Guidance Document* (sampling / NSQ handling): `https://www.cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/Guidance_doc/CDSCO%20Guidance%20Document.pdf`
- Drugs & Cosmetics Rules 1945 text of **Rule 65** (batch number is a mandatory sale-record field for Schedule C/H/H1). Source it from an official government PDF if possible. If not, save the Indian Kanoon page `https://indiankanoon.org/doc/147665881/` as HTML, with its source noted.

Commit: `data: add CDSCO recall/guidance reference docs`.

---

## 7. Phase F — Baseline parse + gold set (for the accuracy number judges love)

**Purpose:** the product itself will parse PDFs **inside Snowflake** (AI_PARSE_DOCUMENT in LAYOUT mode, page-split, then per-page structured extraction). This local parse only serves to:
- (a) bootstrap the gold labels;
- (b) act as a comparison baseline.

It is not the product.

**Known PDF quirks** (seen in the June 2025 central list); handle them all:
- **Multi-line cells:** product name, manufacturer address and NSQ result wrap across lines.
- **Several batches in one cell:** `B.no: IEW1480C, IEW-1480B` → explode into 2 rows and keep `batch_no_raw` plus `batch_group_id`.
- **Batch split across lines:** `DXT2024120` / `40` → `DXT202412040` (flag `batch_rejoined=true`).
- **Brand in parentheses** inside the product name: `Dexamethasone Sodium Phosphate Injection I.P. (Dexacos)` → `brand_name=Dexacos`.
- **Mixed date formats:** `01/2025`, `12-09-2024`, and `11-09-` + `2026` split across lines.
- **Manufacturer typos:** keep the raw value; add `manufacturer_norm` (lowercase, strip `M/s.`, punctuation, address after the first comma).
- **Section headers and footers** (definitions of NSQ, "As part of continuous regulatory surveillance…") must not become rows.

**Steps**
1. `scripts/parse_baseline.py`: pdfplumber table extraction with a text-line fallback, applied to every file in `central/`, `state/`, `spurious/` and `combined/`. Output `data/interim/nsq_baseline_parsed.csv` with columns:
   - `alert_month, category, source_file, page_no, row_no, product_name, brand_name, batch_no_raw, batch_no_norm, batch_group_id, batch_rejoined, mfg_date, exp_date, manufacturer_raw, manufacturer_norm, nsq_result, reporting_lab, parse_confidence`.
   - `batch_no_norm` = uppercase, remove spaces, hyphens, slashes and dots, and strip `B.NO:` prefixes.
2. `scripts/build_gold_template.py`: take the **June 2025 central** rows (≈55 rows) and write `data/gold/nsq_2025-06_central_gold.csv`, pre-filled from the baseline plus `verified` (blank) and `notes` columns.
3. ⛔ **Checkpoint:** tell me the gold file is ready. **I will verify it by hand against the PDF.** Do not mark rows as verified yourself.
4. Commit: `data: baseline NSQ parse + gold template (unverified)`.

---

## 8. Phase G — Synthetic hospital generator

`scripts/generate_synthetic_hospital.py`: deterministic (`--seed 42`), with Faker `en_IN`. It writes Parquet **and** CSV to `data/synthetic/hospital/`.

**The hospital:** a fictional 300-bed hospital, "Sahyadri Synthetic General Hospital", with an in-house pharmacy and 2 satellite stores. Time window **2024-01-01 → 2025-07-31**, so it overlaps the alert months we have.

| Table | Rows (approx) | Key columns |
|---|---|---|
| `patients` | 5,000 | patient_id, name (fake), sex, dob, age_band (incl. paediatric <12 ≈ 18%), district, phone (fake, clearly invalid prefix), preferred_language (ml/en/ta/hi) |
| `wards` | 12 | ward_id, name (Paediatrics, Medicine, Surgery, ICU, OPD…), store_id |
| `encounters` | 20,000 | encounter_id, patient_id, ward_id, type (OPD/IPD/ER), admit_ts, discharge_ts, primary_dx_text |
| `products` | ~1,500 | product_id, brand_name, generic_composition, dosage_form, manufacturer, schedule (H/H1/OTC), is_nsq_seeded |
| `stock_batches` | ~6,000 | batch_uid, product_id, batch_no, mfg_date, exp_date, store_id, qty_received, qty_on_hand, received_date, supplier |
| `prescriptions` | 60,000 | rx_id, encounter_id, patient_id, product_id, dose, frequency, days, prescriber_id |
| `dispensing` | 60,000 | disp_id, rx_id, patient_id, batch_uid (nullable), batch_no_as_recorded (nullable), qty, dispensed_ts, store_id, capture_method (qr_scan / manual / blank) |
| `labs` | 40,000 | lab_id, patient_id, encounter_id, test (creatinine, WBC, temperature, CRP, ALT), value, unit, ref_low, ref_high, collected_ts |

**Realism rules (important for the demo)**
1. **Seed real failed batches.**
   - About **5% of `stock_batches`** use real `batch_no_raw`, manufacturer, product and mfg/exp values taken from `data/interim/nsq_baseline_parsed.csv` (and the portal CSV if available).
   - Set `is_nsq_seeded=true` on those products.
   - Dispensing dates must fall between the batch's `received_date` and `exp_date`.
2. **Messy recording.** In `dispensing.batch_no_as_recorded`, apply noise to about 25% of rows:
   - lowercase;
   - add or remove hyphens and spaces;
   - an O↔0 or I↔1 swap in about 3% of rows.
   Also:
   - About **15% of dispensing rows have a blank batch** (`capture_method='blank'`). This mirrors real pharmacies leaving the batch column empty.
   - QR-scanned rows (`capture_method='qr_scan'`, ~40%) always have exact batch numbers.
3. **Near-miss decoys.** Add batches with the same product and manufacturer but a *different* batch number than an NSQ batch, so the matcher must **not** flag them.
4. **Clinical signal scenarios** (small and clearly labelled in the ground truth only):
   - **Scenario A (DEG-like):** 1 seeded paediatric oral-liquid batch → 6 exposed children; 3 of them show creatinine rising >2× baseline within 3–10 days.
   - **Scenario B (sterility):** 1 seeded injectable with a "Sterility" NSQ result → 12 exposed IPD patients; 4 show temperature >38.5 °C / WBC rise within 48 h.
   - Everyone else has normal lab noise.
5. **Answer key.** Write `data/synthetic/ground_truth/exposures_truth.csv` with `patient_id, disp_id, nsq_source_file, nsq_row_no, match_type (exact/noisy/blank_batch/decoy), scenario`. This file is for evaluation only; note it in the README so it is never loaded into the app schema.
6. Add a `data/synthetic/README.md` data dictionary, with a banner: **"All patient data is synthetic. Batch numbers in seeded rows are real public CDSCO NSQ batches."**

Commit: `data: synthetic hospital (seed 42) + ground-truth exposures`.

---

## 9. Phase H — Validation and docs

`scripts/validate_data.py` must pass:
- Every file in the manifest exists and its sha256 matches.
- Every PDF opens and the page count matches the manifest.
- `nsq_baseline_parsed.csv`: no empty `batch_no_norm` in NSQ rows; `alert_month` is in range; rows-per-month roughly match the published counts (e.g. June 2025 central ≈ 55).
- Synthetic data:
  - foreign keys resolve;
  - dispensing timestamps sit inside batch validity;
  - blank-batch share is 13–17%;
  - the seeded NSQ batch share is 4–6%;
  - scenario patients exist.
- No file > 50 MB; no `.env` or secrets tracked (`git ls-files | grep -i -E "env|key|secret|token"` is empty).

`docs/DATA_SOURCES.md` must cover:
- each source, URL, licence or terms, fetch date and row counts;
- **known gaps:**
  - many states don't submit state NSQ data every month;
  - the portal (Aug 2025+) may be partial;
  - batch numbers are often missing in real-world dispensing;
- the statement that no real patient data is used.

`README.md`: a one-paragraph project pitch, a `make fetch && make synth && make validate` quick start, and the repo map.

Final commit: `docs: data sources, validation report`, then push to `main` (or open a PR if I ask for one).

⛔ **Final checkpoint:** give me
- a summary table (files, rows, sizes);
- the months covered and missing;
- the validation output;
- the GitHub URL.

---

## 10. After Snowflake trial activation (27 Sept) — NOT part of this run

These are listed only so the data layout supports them; don't implement them yet:
- `snowflake/00_setup.sql`: database `BBT`, schemas `RAW / CORE / APP`, X-Small warehouse with 60 s auto-suspend, resource monitor.
- `snowflake/upload_to_stage.py`: `PUT` the PDFs to `@BBT.RAW.CDSCO_PDFS`, and the synthetic Parquet to `@BBT.RAW.HOSPITAL`. (Trial accounts can't fetch URLs from inside Snowflake, which is why we store the files in git.)
- The in-Snowflake pipeline:
  - `AI_PARSE_DOCUMENT` (LAYOUT, page_split);
  - per-page structured extraction with `AI_COMPLETE` and a JSON schema. Don't use one `AI_EXTRACT` call per whole document: its table output is capped at 4,096 tokens.
  - accuracy is measured against `data/gold/`.
