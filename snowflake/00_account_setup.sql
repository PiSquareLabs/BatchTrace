-- Kavach: account-level setup — warehouses, resource monitor, cross-region Cortex.
-- Idempotent: safe to re-run. Run as ACCOUNTADMIN (or a role with MANAGE GRANTS / CREATE WAREHOUSE).
--
-- Prerequisites (do these in Snowsight first, not in SQL):
--   1. Claim the team trial (Enterprise edition, AWS US West/East).
--   2. Add a payment method — this lifts the Cortex AI daily cap on trial accounts while still
--      spending free credits first.
-- Run this file with: snow sql -c kavach -f snowflake/00_account_setup.sql

USE ROLE ACCOUNTADMIN;

-- ---------------------------------------------------------------------------
-- 1. Cross-region Cortex inference (needed if Cortex AI functions aren't
--    available in-region on this trial's region). Safe to run even if already set.
-- ---------------------------------------------------------------------------
ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION';

-- ---------------------------------------------------------------------------
-- 2. Warehouses — X-Small, 60s auto-suspend, auto-resume. Protect the credits.
-- ---------------------------------------------------------------------------
CREATE WAREHOUSE IF NOT EXISTS WH_BUILD
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE
  INITIALLY_SUSPENDED = TRUE
  COMMENT = 'Kavach — pipeline build/run (ingest, parsing, matching, eval).';

CREATE WAREHOUSE IF NOT EXISTS WH_APP
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE
  INITIALLY_SUSPENDED = TRUE
  COMMENT = 'Kavach — Streamlit in Snowflake app + Cortex Agent queries.';

-- ---------------------------------------------------------------------------
-- 3. Resource monitor — team-agreed quota: $350 (leaves a buffer under the
--    $400 trial credit). Notify at 50/75/90%, suspend at 100%.
--    TODO: revisit KAVACH_MONTHLY_QUOTA if the team agrees a different cap.
-- ---------------------------------------------------------------------------
SET KAVACH_MONTHLY_QUOTA = 350;

CREATE RESOURCE MONITOR IF NOT EXISTS KAVACH_RM
  WITH
    CREDIT_QUOTA = $KAVACH_MONTHLY_QUOTA
    FREQUENCY = MONTHLY
    START_TIMESTAMP = IMMEDIATELY
    TRIGGERS
      ON 50 PERCENT DO NOTIFY
      ON 75 PERCENT DO NOTIFY
      ON 90 PERCENT DO NOTIFY
      ON 100 PERCENT DO SUSPEND;

ALTER WAREHOUSE WH_BUILD SET RESOURCE_MONITOR = KAVACH_RM;
ALTER WAREHOUSE WH_APP SET RESOURCE_MONITOR = KAVACH_RM;

-- Also cap the account overall, in case other warehouses get created ad hoc.
ALTER ACCOUNT SET RESOURCE_MONITOR = KAVACH_RM;

-- ---------------------------------------------------------------------------
-- Verify
-- ---------------------------------------------------------------------------
SHOW WAREHOUSES LIKE 'WH_%';
SHOW RESOURCE MONITORS LIKE 'KAVACH_RM';
