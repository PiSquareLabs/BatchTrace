-- Kavach: roles, users, grants. Idempotent: safe to re-run.
-- Run as ACCOUNTADMIN (or SECURITYADMIN for the user/role parts).
-- Run this file with: snow sql -c kavach -f snowflake/01_rbac.sql
--
-- TODO before running: replace the two placeholder emails/usernames below with
-- the real values for Person A and Person B, and pick temporary passwords
-- out-of-band (Slack/DM) — never put a real password in this file or in git.

USE ROLE ACCOUNTADMIN;

-- ---------------------------------------------------------------------------
-- 1. Roles
-- ---------------------------------------------------------------------------
CREATE ROLE IF NOT EXISTS KAVACH_ADMIN
  COMMENT = 'Kavach — full account/platform admin (Person C).';

CREATE ROLE IF NOT EXISTS KAVACH_ENGINEER
  COMMENT = 'Kavach — builds pipelines, SQL objects, Cortex features (Persons A, B).';

CREATE ROLE IF NOT EXISTS KAVACH_APP
  COMMENT = 'Kavach — service role the Streamlit app / agent runs as.';

CREATE ROLE IF NOT EXISTS KAVACH_PHARMACIST
  COMMENT = 'Kavach — app end-user role, sees unmasked patient contact info.';

CREATE ROLE IF NOT EXISTS KAVACH_CLINICIAN
  COMMENT = 'Kavach — app end-user role, sees unmasked patient contact info.';

CREATE ROLE IF NOT EXISTS KAVACH_JUDGE_RO
  COMMENT = 'Kavach — read-only demo/judge role, masked + aggregated data only.';

-- Role hierarchy: admin sees everything an engineer can do; engineer inherits app-level read.
GRANT ROLE KAVACH_ENGINEER TO ROLE KAVACH_ADMIN;
GRANT ROLE KAVACH_APP TO ROLE KAVACH_ENGINEER;

-- SYSADMIN should also own these for object management outside the app.
GRANT ROLE KAVACH_ADMIN TO ROLE SYSADMIN;

-- ---------------------------------------------------------------------------
-- 2. Users for Person A and Person B.
--    TODO: replace placeholders. Each user gets a temp password (shared
--    out-of-band, not here) and must change it + set up MFA on first login.
-- ---------------------------------------------------------------------------
CREATE USER IF NOT EXISTS PERSON_A
  LOGIN_NAME = 'PERSON_A'
  EMAIL = 'REPLACE_WITH_SREEDEV_EMAIL'
  DEFAULT_ROLE = 'KAVACH_ENGINEER'
  DEFAULT_WAREHOUSE = 'WH_BUILD'
  MUST_CHANGE_PASSWORD = TRUE
  PASSWORD = 'REPLACE_WITH_TEMP_PASSWORD_SHARED_OUT_OF_BAND'
  COMMENT = 'Person A — Sreedev TS (data & pipeline engineer).';

CREATE USER IF NOT EXISTS PERSON_B
  LOGIN_NAME = 'PERSON_B'
  EMAIL = 'REPLACE_WITH_SAFAR_EMAIL'
  DEFAULT_ROLE = 'KAVACH_ENGINEER'
  DEFAULT_WAREHOUSE = 'WH_BUILD'
  MUST_CHANGE_PASSWORD = TRUE
  PASSWORD = 'REPLACE_WITH_TEMP_PASSWORD_SHARED_OUT_OF_BAND'
  COMMENT = 'Person B — Safar (matching & AI engineer).';

GRANT ROLE KAVACH_ENGINEER TO USER PERSON_A;
GRANT ROLE KAVACH_ENGINEER TO USER PERSON_B;

-- ---------------------------------------------------------------------------
-- 3. Warehouse usage
-- ---------------------------------------------------------------------------
GRANT USAGE ON WAREHOUSE WH_BUILD TO ROLE KAVACH_ENGINEER;
GRANT USAGE ON WAREHOUSE WH_APP TO ROLE KAVACH_APP;
GRANT USAGE ON WAREHOUSE WH_APP TO ROLE KAVACH_JUDGE_RO;

-- ---------------------------------------------------------------------------
-- 4. Cortex AI + CoCo CLI access.
--    SNOWFLAKE.CORTEX_USER: run Cortex AI functions (AI_PARSE_DOCUMENT, AI_CLASSIFY, ...).
--    SNOWFLAKE.COPILOT_USER: required for CoCo CLI / Copilot access.
-- ---------------------------------------------------------------------------
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE KAVACH_ENGINEER;
GRANT DATABASE ROLE SNOWFLAKE.COPILOT_USER TO ROLE KAVACH_ENGINEER;
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE KAVACH_ADMIN;
GRANT DATABASE ROLE SNOWFLAKE.COPILOT_USER TO ROLE KAVACH_ADMIN;

-- The app/agent also calls Cortex functions and the Cortex Agent at runtime.
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE KAVACH_APP;

-- ---------------------------------------------------------------------------
-- Verify
-- ---------------------------------------------------------------------------
SHOW ROLES LIKE 'KAVACH_%';
SHOW USERS LIKE 'PERSON_%';
SHOW GRANTS TO ROLE KAVACH_ENGINEER;
