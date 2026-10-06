---
name: triage
description: >
  Identify patients exposed to flagged batches and assign clinical priority.
  Joins matches through PAT_APPOINTMENT_DRUGS, reads doctor notes for context,
  and writes triage records to ALERT_TRIAGE.
---

After matching, run triage. The skill:

1. Finds directly exposed patients (drug line batch_id in ALERT_MATCHES)
2. Finds possibly exposed patients (NULL batch_id, same brand+manufacturer matched)
3. Reads doctor notes from PAT_APPOINTMENTS for clinical context
4. Assigns priority (CRITICAL, HIGH, MEDIUM, LOW) based on harm_type, severity, allergies, age
5. Extracts relevant quotes from doctor notes (quoted_note)
6. Writes triage records to ALERT_TRIAGE
