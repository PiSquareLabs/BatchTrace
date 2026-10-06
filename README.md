# BatchTrace

**Hospital drug-batch safety tracker powered by Snowflake Cortex AI.**

BatchTrace ingests CDSCO (Central Drugs Standard Control Organisation) drug-safety alert PDFs, extracts failed-batch information using Cortex AI functions, matches them against a hospital's inventory, identifies exposed patients, triages by clinical severity, and generates actionable reports for pharmacy and clinical staff.

## Architecture

```
CDSCO PDF  ──▶  @RAW.CDSCO_PDFS  ──▶  SP_INGEST  ──▶  ALERT_INGESTION / PAGES / ROWS_RAW
                                       SP_MATCH   ──▶  ALERT_ITEMS / MATCHES
                                       SP_TRIAGE  ──▶  ALERT_TRIAGE / EXPOSURES view
                                       SP_REPORT  ──▶  ALERT_REPORTS / REPORT_BATCHES / REPORT_PATIENTS
```

## Database layout

| Schema | Purpose |
|--------|---------|
| `RAW`  | Stages (`CDSCO_PDFS`, `SEED_DATA`) and file formats |
| `CORE` | 16 tables + 2 views: hospital data, alert pipeline, reports, audit |
| `APP`  | Streamlit app objects (future) |

## Quick start

```sql
-- 1. Run setup, tables, load, config in order:
--    sql/01_setup.sql
--    sql/02_tables.sql
--    sql/03_load_data.sql
--    sql/04_app_config.sql
```

## Data

- **data/load/**: Main hospital seed data (3,184 batches, 2,190 patients, 5,711 appointments, 8,805 drug lines)
- **data/demo/**: 5 demo patients (P90001–P90005) with 25 appointments and 21 drug lines that tell specific clinical stories
- **data/md/**: Source markdown files with embedded CSV and loading instructions
- **pdfs/**: CDSCO alert PDFs for ingestion testing

## Row counts after loading

| Table | Rows |
|-------|------|
| BAT_BATCHES | 3,184 |
| PAT_PATIENTS | 2,195 |
| PAT_APPOINTMENTS | 5,736 |
| PAT_APPOINTMENT_DRUGS | 8,826 |

All data is synthetic except for real CDSCO batch numbers, product names, and manufacturer names.

## CoCo Skills

Four pipeline skills in `.cortex/skills/` (CLI) and `.snowflake/cortex/skills/` (Snowsight):

| Skill | Purpose |
|-------|---------|
| `ingest` | Parse and extract rows from CDSCO alert PDFs |
| `match` | Match extracted alert items to hospital batch inventory |
| `triage` | Identify exposed patients and assign clinical priority |
| `report` | Generate summary reports with batch and patient details |
