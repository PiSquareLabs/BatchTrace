---
name: match
description: >
  Match extracted alert items against the hospital's batch inventory.
  Normalizes batch numbers, computes JAROWINKLER_SIMILARITY on manufacturer
  names, and writes scored matches to ALERT_MATCHES.
---

After ingestion, run the match step. The skill:

1. Normalizes batch numbers from ALERT_ROWS_RAW into ALERT_ITEMS (batch_no_norm, maker_clean)
2. Joins ALERT_ITEMS against BAT_BATCHES on exact batch_no match
3. Validates manufacturer using JAROWINKLER_SIMILARITY >= APP_CONFIG.MATCH_MAKER_MIN
4. Classifies harm_type and severity from the failure reason text
5. Writes matches to ALERT_MATCHES with score and status='AUTO'
6. Flags items needing manual review (ALERT_ITEMS.needs_review)
