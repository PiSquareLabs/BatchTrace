-- BatchTrace: Load APP_CONFIG settings (idempotent via MERGE)
-- Before running: test AI_COMPLETE with each candidate model in order and keep the first working one.

USE SCHEMA BATCHTRACE.CORE;

MERGE INTO APP_CONFIG AS tgt
USING (
  SELECT column1 AS key, column2 AS value FROM VALUES
    ('MODEL',           'claude-sonnet-4-5'),
    ('NOTIFY_EMAIL',    'CHANGE_ME@example.com'),
    ('SNAPSHOT_DATE',   '2025-07-18'),
    ('MATCH_MAKER_MIN', '85'),
    ('OCR_MIN_CHARS',   '200'),
    ('APP_BANNER',      'Synthetic demo data – not real patients')
) AS src
ON tgt.key = src.key
WHEN MATCHED THEN UPDATE SET tgt.value = src.value
WHEN NOT MATCHED THEN INSERT (key, value) VALUES (src.key, src.value);

SELECT * FROM APP_CONFIG ORDER BY key;
