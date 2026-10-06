# BatchTrace Build Prompt

Summary of the build steps used to create this project.

## 1. Setup
- Enable cross-region Cortex: `ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION'`
- Warehouse `COMPUTE_WH`: XSMALL, auto-suspend 60s, auto-resume
- Database `BATCHTRACE` with schemas `RAW`, `CORE`, `APP`
- Stages: `RAW.CDSCO_PDFS` (SSE encryption, directory enabled), `RAW.SEED_DATA`
- File format: `RAW.CSV_FMT` (CSV, skip header, field enclosed by `"`, empty-as-null, UTF-8)

## 2. Hospital tables (CORE)
- `BAT_BATCHES` — batch inventory with quarantine columns
- `PAT_PATIENTS` — patient demographics
- `PAT_APPOINTMENTS` — visits with diagnosis and doctor notes
- `PAT_APPOINTMENT_DRUGS` — drugs dispensed per visit, linked to batches
- FK constraints: drugs → appointments, drugs → patients, drugs.batch_id → batches, appointments → patients

## 3. Alert tables (CORE)
- `APP_CONFIG` — key-value settings (model, email, thresholds)
- `ALERT_INGESTION` — one row per uploaded PDF
- `ALERT_INGESTION_STEPS` — step-level processing log
- `ALERT_PAGES` — extracted page text
- `ALERT_ROWS_RAW` — raw extracted rows
- `ALERT_ITEMS` — normalized alert items
- `ALERT_MATCHES` — batch matches with similarity scores
- `ALERT_TRIAGE` — patient-level triage with priority

## 4. Report tables (CORE)
- `ALERT_REPORTS` — summary reports per ingestion
- `ALERT_REPORT_BATCHES` — batch detail per report
- `ALERT_REPORT_PATIENTS` — patient detail per report
- `ALERT_ACTIONS` — audit log of actions taken

## 5. Views (CORE)
- `EXPOSURES` — Exposed (matched batch_id) + Possible (NULL batch_id, same brand+manufacturer matched)
- `DOCTORS` — distinct doctor/department pairs

## 6. Data loading
- PUT CSVs from `data/load/` and `data/demo/` to `@RAW.SEED_DATA`
- COPY INTO in FK order: batches & patients first, then appointments, then drugs
- APP_CONFIG loaded via MERGE (idempotent)

## 7. Comments
- Table and column comments added from `data/md/` descriptions

## 8. Verification
- Row counts: 3,184 / 2,195 / 5,736 / 8,826
- Zero orphan batch_ids, ~12% blank batch_id share
- Batch TS24047 traces through to patient P90004
- 16 tables + 2 views in BATCHTRACE.CORE
