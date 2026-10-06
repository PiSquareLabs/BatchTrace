# BatchTrace Design Specification

## Problem
Indian hospitals receive CDSCO (Central Drugs Standard Control Organisation) drug-safety alerts as PDF documents listing failed batches. Manually cross-referencing these against thousands of batches in inventory and identifying exposed patients is slow and error-prone.

## Solution
BatchTrace automates the full pipeline: PDF ingestion → AI extraction → batch matching → patient triage → report generation, using Snowflake Cortex AI functions and stored procedures.

## Data Model

### Hospital tables (seed data)
| Table | PK | Description |
|-------|-----|------------|
| BAT_BATCHES | batch_id | Medicine batches on hospital shelves |
| PAT_PATIENTS | patient_id | Patient demographics |
| PAT_APPOINTMENTS | appointment_id | Doctor visits with clinical notes |
| PAT_APPOINTMENT_DRUGS | line_id | Drugs dispensed per visit, FK to batches |

### Alert pipeline tables (filled by processing)
| Table | PK | Description |
|-------|-----|------------|
| APP_CONFIG | key | Runtime settings |
| ALERT_INGESTION | ingestion_id | One row per PDF upload |
| ALERT_INGESTION_STEPS | (ingestion_id, step_no) | Step-level processing log |
| ALERT_PAGES | (ingestion_id, page_no) | Extracted page text |
| ALERT_ROWS_RAW | (ingestion_id, page_no, row_no) | Raw extracted rows |
| ALERT_ITEMS | alert_item_id | Normalized, cleaned alert items |
| ALERT_MATCHES | (ingestion_id, alert_item_id, batch_id) | Batch matches with scores |
| ALERT_TRIAGE | (ingestion_id, patient_id, line_id) | Patient-level triage |

### Report tables
| Table | PK | Description |
|-------|-----|------------|
| ALERT_REPORTS | report_id | Summary report per ingestion |
| ALERT_REPORT_BATCHES | (report_id, batch_id) | Batch details in report |
| ALERT_REPORT_PATIENTS | (report_id, patient_id, line_id) | Patient details in report |
| ALERT_ACTIONS | action_id | Audit log of all actions |

### Views
| View | Description |
|------|------------|
| EXPOSURES | Exposed (direct match) + Possible (same brand/manufacturer, no batch recorded) |
| DOCTORS | Distinct doctor/department pairs |

## Pipeline stages

1. **Ingest**: Upload PDF → classify (NSQ/ASU) → extract pages (text + OCR fallback) → parse rows
2. **Match**: Normalize batch numbers → JAROWINKLER_SIMILARITY against BAT_BATCHES → score and filter
3. **Triage**: Join matches through PAT_APPOINTMENT_DRUGS → identify exposed/possible patients → assign priority using doctor notes
4. **Report**: Aggregate into summary → generate markdown report → quarantine batches → add clinical notes

## Key design decisions
- `batch_id` is a synthetic surrogate; `batch_no` is the manufacturer's printed lot number
- ~12% of drug lines have NULL batch_id (batch not recorded), creating "possible exposure" cases
- Manufacturer matching uses JAROWINKLER_SIMILARITY with configurable threshold (APP_CONFIG.MATCH_MAKER_MIN)
- OCR fallback when extracted text is below APP_CONFIG.OCR_MIN_CHARS characters
- APP_CONFIG.SNAPSHOT_DATE anchors the demo to 2025-07-18 (when June-2025 alerts were published)
