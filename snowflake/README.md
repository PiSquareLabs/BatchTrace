# Snowflake (placeholder)

Load steps come after trial activation (27 Sept 2026). Planned:

- `00_setup.sql` — database `BBT`, schemas `RAW / CORE / APP`, X-Small warehouse (60 s auto-suspend), resource monitor.
- `upload_to_stage.py` — `PUT` CDSCO PDFs to `@BBT.RAW.CDSCO_PDFS` and synthetic Parquet to `@BBT.RAW.HOSPITAL`
  (trial accounts cannot fetch URLs from inside Snowflake, so files live in git).
- In-Snowflake pipeline: `AI_PARSE_DOCUMENT` (LAYOUT, page_split) → per-page `AI_COMPLETE` with a JSON schema;
  accuracy measured against `data/gold/`.

**Never** load `data/synthetic/ground_truth/` into app schemas — it is the evaluation answer key.
