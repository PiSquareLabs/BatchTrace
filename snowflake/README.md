# Snowflake

Numbered, idempotent SQL files (`CREATE OR REPLACE` / `IF NOT EXISTS`) — a fresh account must
rebuild end to end from this folder. Run with `snow sql -c kavach -f snowflake/<file>.sql`
(see `docs/setup_coco_cli.md` for the connection setup).

| File | Status | What it does |
|---|---|---|
| `00_account_setup.sql` | done (#6) | Warehouses `WH_BUILD` / `WH_APP` (X-Small, 60s auto-suspend), resource monitor, cross-region Cortex. |
| `01_rbac.sql` | done (#6) | Roles `KAVACH_ADMIN/ENGINEER/APP/PHARMACIST/CLINICIAN/JUDGE_RO`, users for A/B, Cortex + CoCo grants. |
| `02_database_schemas.sql` | planned (#7) | Database `KAVACH`, schemas `RAW / CORE / APP / EVAL / GOV` + personal dev schemas. |
| `03_stages.sql` | planned (#7) | Stages `@RAW.CDSCO_PDFS`, `@RAW.REFERENCE_DOCS`, `@RAW.HOSPITAL` — SSE encryption + directory tables. |
| `04_raw_tables.sql`, `10_*`–`60_*` | planned (#8–#25) | See `CLAUDE_CODE_TEAM_PLAN.md` §6 for the full list. |
| `99_teardown.sql` | planned | Tears everything down for a clean re-run. |

Trial accounts can't fetch URLs from inside Snowflake, so all data enters via
`snow stage copy` from files already committed to this repo (CDSCO PDFs, synthetic Parquet).

**Never** load `data/synthetic/ground_truth/` into any Snowflake schema — it is the evaluation
answer key, used only by local `scripts/validate_data.py` and later `EVAL.MATCH_METRICS`.
