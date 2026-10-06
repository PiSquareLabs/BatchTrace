---
name: ingest
description: >
  Parse and extract structured rows from a CDSCO drug-safety alert PDF.
  Classifies the PDF type, extracts text per page (with OCR fallback),
  and parses tabular rows into ALERT_ROWS_RAW.
---

Upload a CDSCO alert PDF to `@BATCHTRACE.RAW.CDSCO_PDFS`, then run the
ingestion pipeline. The skill:

1. Registers the file in ALERT_INGESTION
2. Classifies the PDF as NSQ (Not of Standard Quality) or ASU (Spurious/Adulterated)
3. Extracts text from each page using AI_PARSE_DOCUMENT
4. Falls back to OCR mode if char_count < APP_CONFIG.OCR_MIN_CHARS
5. Parses each page into structured rows (drug, batch_no, dates, manufacturer, reason)
6. Logs every step in ALERT_INGESTION_STEPS
