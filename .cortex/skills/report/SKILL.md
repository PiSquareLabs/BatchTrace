---
name: report
description: >
  Generate a summary report for a completed ingestion, quarantine affected
  batches, and optionally add clinical notes to patient records.
---

After triage, generate the report. The skill:

1. Aggregates alert items, affected batches, exposed patients, possible exposures
2. Generates a markdown summary report (ALERT_REPORTS.report_md)
3. Populates ALERT_REPORT_BATCHES with batch-level details
4. Populates ALERT_REPORT_PATIENTS with patient-level details
5. Quarantines matched batches (sets BAT_BATCHES.quarantined = TRUE)
6. Logs all actions to ALERT_ACTIONS
7. Optionally sends email notification via NOTIFY_EMAIL
