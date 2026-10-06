# Demo Patient Cases

Five synthetic patients (P90001–P90005) with scripted clinical stories for demonstrating BatchTrace.

## P90001 — Direct exposure, high severity
Elderly patient on multiple medications. Received a batch flagged for **potency failure** (sub-therapeutic dose). Follow-up notes show the condition was **not responding** to treatment — a clinical signal that the failed batch had real impact.

## P90002 — Direct exposure, allergy risk
Patient with known drug allergies who received a flagged batch. The alert's harm type combined with the allergy history elevates the triage priority to **CRITICAL**.

## P90003 — Possible exposure (no batch recorded)
The dispensing pharmacist did not record the batch number. The same brand and manufacturer have a matched alert batch, so this patient appears as a **possible exposure** — requiring manual follow-up to confirm or rule out.

## P90004 — Multiple flagged batches
Patient received drugs from batch **TS24047** (among others). This case tests that the pipeline correctly traces through drugs → batches → alert matches and identifies all affected prescriptions across multiple visits.

## P90005 — Paediatric patient, cascading harm
Young patient whose treatment course spans several visits. A flagged batch early in the course may have contributed to a cascade of follow-up visits. The doctor notes tell the clinical story across appointments.

---

These cases exercise the full pipeline: direct vs possible exposure, severity escalation, allergy interaction, missing batch numbers, and multi-visit tracing.
