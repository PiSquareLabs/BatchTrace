# Load APP_CONFIG

Settings that the procedures and the app read.

## Prompt for CoCo
```
Insert these rows into BATCHTRACE.CORE.APP_CONFIG with MERGE, so the load is safe to re-run.
Before you insert MODEL, test AI_COMPLETE with each candidate in order, and keep the first one that answers: claude-sonnet-4-5, claude-3-7-sonnet, mistral-large2, llama3.1-70b.
Then show me SELECT * FROM BATCHTRACE.CORE.APP_CONFIG.
```

## Data
| key | value | meaning |
|---|---|---|
| MODEL | (first working model from the test) | Model for AI_COMPLETE in every procedure |
| NOTIFY_EMAIL | your own email address | Where SP_NOTIFY sends reports |
| SNAPSHOT_DATE | 2025-07-18 | The "today" of the demo data (day the June-2025 alerts came out) |
| MATCH_MAKER_MIN | 85 | Minimum JAROWINKLER_SIMILARITY for a manufacturer match |
| OCR_MIN_CHARS | 200 | Pages with fewer characters than this are re-parsed with OCR |
| APP_BANNER | Synthetic demo data – not real patients | Banner text at the top of the app |

## Tables that start empty
These are filled by the pipeline when a PDF is processed, so you load nothing into them now:
ALERT_INGESTION, ALERT_INGESTION_STEPS, ALERT_PAGES, ALERT_ROWS_RAW, ALERT_ITEMS, ALERT_MATCHES, ALERT_TRIAGE, ALERT_REPORTS, ALERT_REPORT_BATCHES, ALERT_REPORT_PATIENTS, ALERT_ACTIONS.
