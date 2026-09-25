# Kavach — Team Build Plan & GitHub Issues (for Claude Code)

> **How to use:** Put this file in the repo root next to `CLAUDE_CODE_DATA_PLAN.md`, then tell Claude Code:
> *"Read CLAUDE_CODE_TEAM_PLAN.md. Follow Section 9 to create the labels, milestones and issues on our GitHub repo. Stop at every ⛔ and ask me first."*
>
> The app name is **Kavach**. If the team picks another name, replace it everywhere before creating issues.

---

## 1. What we're building (one paragraph)

Every month, CDSCO publishes PDFs listing medicine batches that failed government lab tests ("Not of Standard Quality", NSQ). **Kavach** does the rest automatically:
- reads those PDFs inside Snowflake;
- matches the failed batches against a hospital's pharmacy stock and dispensing records;
- names the patients who received them;
- watches those patients' lab results for warning signs;
- gives staff an action list (quarantine stock, call patients, get clinician review), with every step citing the exact line of the government alert.

The patient data is 100% synthetic, as the track requires. The alert data is real and public.

**Hackathon:** Snowflake CoCo CLI Hackathon 2026, GCC Edition, Track 4 (Patient 360 & Clinical/Regulatory Copilot).

**Judging rubric:**
- Real-World Relevance: 30%
- Technical Execution: 40%
- Solution Completeness: 30%

**Mandatory submissions (due 4 Oct 2026):**
1. GitHub repo + deployed app link.
2. Prototype/MVP documentation.

---

## 2. Principles (apply to every ticket)

1. **Snowflake-first.** If Snowflake can do it, do it in Snowflake: SQL, Cortex AI functions, Snowpark, Dynamic Tables, Tasks, Streamlit in Snowflake. Code outside Snowflake is limited to data fetching, the synthetic generator, and the public app mirror.
2. **Build with CoCo CLI.** Each ticket's "CoCo CLI" section says how to use it. Log notable CoCo sessions in `docs/coco_log.md`: prompt, what CoCo generated, what you changed. Judges should see that CoCo was central, not decorative.
3. **Everything as code.**
   - All Snowflake objects live in numbered, idempotent SQL files under `snowflake/` (`CREATE OR REPLACE` / `IF NOT EXISTS`).
   - A fresh account must rebuild end to end from the repo.
4. **Cite, don't claim.** Every alert-derived fact shown to a user must link back to `source_file + page`.
5. **Clinical wording.** Flags say "needs clinician review", never a diagnosis.
6. **Protect the credits.**
   - X-Small warehouses, 60 s auto-suspend, one resource monitor.
   - Run AI_PARSE_DOCUMENT once per file and store the results; never re-parse in loops.
7. **Workflow.**
   - One branch per issue (`<issue#>-short-name`).
   - PRs reference `Closes #n`.
   - Another team member reviews every PR (keep reviews light).
   - `main` must always run.

---

## 3. Team roles

| Person | Role | Owns |
|---|---|---|
| **A: Data & Pipeline** | Alert ingestion engineer | CDSCO data, PDF → structured alerts pipeline, extraction accuracy, automation, Cortex Search, monthly brief, regulator insights |
| **B: Intelligence** | Matching & AI engineer | Synthetic hospital, matching engine, patient exposure, clinical watch, action list, semantic view, Cortex Agent |
| **C: Platform & Product** | Platform, app & delivery lead | Snowflake account/RBAC/governance, Streamlit app, public deployment, demo, docs, video, submission |

Placeholders `@PERSON_A`, `@PERSON_B` and `@PERSON_C` are replaced with real GitHub usernames at issue-creation time (⛔ ask me).

---

## 4. Account strategy

- **One team account.** Person C claims the $400 trial on **26 or 27 Sept (UTC)** (the claim window closes 27 Sept). Waiting until then pushes the 30-day end date as close as possible to the finale demo days (27–30 Oct).
- **Sign-up choices:** Enterprise edition, AWS US West (Oregon) or US East.
- **Users:** A and B get their own users in that account; don't share passwords.
- **Backup trials:** if A and B also received trial links, they can claim them as backup or sandbox accounts, but all real work goes to the team account.
- **Day-1 checks** (issue #6):
  - add a payment method, which lifts the Cortex AI daily cap on trials while still using the free credits first;
  - set up a resource monitor;
  - confirm **CoCo CLI works for all three users**. If not, email cococlihackgcc-support@hack2skill.com the same day.
- **No outbound calls from a trial.** Trial accounts can't call external URLs, so all data enters Snowflake through stage uploads from the repo.

---

## 5. Architecture (target)

```
GitHub repo ──(snow CLI PUT)──► @KAVACH.RAW.CDSCO_PDFS (internal stage, SSE, directory table)
                                         │  stream on directory table
                                         ▼
                        TASK: AI_PARSE_DOCUMENT (LAYOUT, page_split) ─► RAW.NSQ_PAGES
                                         ▼
                        AI_COMPLETE (JSON schema, per page) ─► RAW.NSQ_ROWS_EXTRACTED
                                         ▼
                 Snowpark UDFs: normalize batch / dates / manufacturer ─► CORE.NSQ_ALERT (1 row per batch)
                                         ▼
                 AI_CLASSIFY + rules ─► CORE.NSQ_ALERT (severity)
                                         │
Synthetic hospital (Parquet) ─► RAW.HOSPITAL.* ─► CORE.* (patients, stock, dispensing, labs)
                                         ▼
          DYNAMIC TABLE CORE.BATCH_MATCHES (exact / probable / watchlist)
                                         ▼
          CORE.PATIENT_EXPOSURE ─► CORE.CLINICAL_FLAGS ─► APP.ACTION_ITEMS (+ AI_TRANSLATE callback scripts)
                                         ▼
  Cortex Search (alerts + CDSCO guidance)  │  Semantic View KAVACH_SV + Cortex Analyst
                                         ▼
                          Cortex Agent "Kavach Assistant"
                                         ▼
      Streamlit in Snowflake app  ──mirror──►  Streamlit Community Cloud (public link, read-only role)
      Snowflake ALERT + SYSTEM$SEND_EMAIL → "new NSQ matches" email
      EVAL schema: extraction accuracy vs gold set, matching accuracy vs ground truth
      GOV: tags, masking policies, row access policy, RBAC
```

**Snowflake features we intend to show:**
- Internal stages with directory tables.
- Streams and Tasks.
- Dynamic Tables.
- AI_PARSE_DOCUMENT, AI_COMPLETE (structured output), AI_EXTRACT (comparison), AI_CLASSIFY, AI_AGG / AI_SUMMARIZE_AGG, AI_TRANSLATE.
- Snowpark Python UDFs.
- Built-in fuzzy matching (JAROWINKLER_SIMILARITY, EDITDISTANCE).
- Cortex Search, Semantic Views, Cortex Analyst, Cortex Agents.
- Streamlit in Snowflake, GET_PRESIGNED_URL.
- Snowflake Alerts + email notifications.
- Object tagging, masking policies, row access policies, RBAC.
- Resource monitors.
- Zero-copy clone (dev copies) and Time Travel (safe resets).
- CoCo CLI and a custom CoCo skill.

---

## 6. Repo layout additions

```
snowflake/
  00_account_setup.sql      01_rbac.sql            02_database_schemas.sql
  03_stages.sql             04_raw_tables.sql      10_parse_pages.sql
  11_extract_rows.sql       12_normalize_udfs.sql  13_nsq_alert.sql
  14_severity.sql           15_automation_tasks.sql
  20_hospital_core.sql      21_matching_dt.sql     22_exposure_flags.sql
  23_action_items.sql       30_cortex_search.sql   31_semantic_view.yaml / .sql
  32_agent.sql              40_governance.sql      50_eval.sql
  60_alerts_email.sql       99_teardown.sql
app/
  streamlit_app.py  pages/  lib/  requirements.txt  (same code runs in SiS and Community Cloud)
.cortex/skills/kavach-monthly-run/SKILL.md     ← custom CoCo skill
docs/ architecture.md  coco_log.md  MVP.md  demo_script.md  wireframes.md  eval_report.md
tests/ agent_questions.yaml  sql_checks/
issues/ issues.yaml                            ← generated from this plan, used to create issues
```

---

## 7. Milestones

| Milestone | Due (IST) | Goal |
|---|---|---|
| **M0 · Pre-activation** | 26 Sep | Data in repo, synthetic hospital, wireframes, repo conventions |
| **M1 · Snowflake foundation** | 27 Sep | Account, RBAC, schemas, stages, raw data loaded |
| **M2 · Core pipelines** | 30 Sep | Alerts extracted and scored; matching, exposure and flags working |
| **M3 · Intelligence & App** | 2 Oct | Search, semantic view, agent, Streamlit screens |
| **M4 · Ship** | 4 Oct | Public link, MVP doc, video, submission |

---

## 8. Issues

Format for each issue body (Claude Code must use this template):

```
## Context
## Tasks
- [ ] ...
## Snowflake features
## CoCo CLI
## Acceptance criteria
## Depends on
```

Labels on every issue: `owner:A|B|C`, `area:*`, `P0|P1|P2`. Add `coco` where CoCo CLI is the main build tool.

### M0 · Pre-activation

**#1 [A] Execute data acquisition plan (CDSCO PDFs, portal, drug master, reference docs)**
Labels: area:data, P0
- Tasks: run phases A–F of `CLAUDE_CODE_DATA_PLAN.md`. Produce the coverage table (months × central/state/spurious).
- Acceptance:
  - `data/manifest.csv` is complete;
  - `validate_data.py` passes for the alert files;
  - the coverage table is in `docs/DATA_SOURCES.md`.

**#2 [A] Hand-verify gold set: June 2025 central NSQ list (~55 rows)**
Labels: area:eval, P0
- Tasks: check every row of `data/gold/nsq_2025-06_central_gold.csv` against the PDF; fill `verified` and `notes`.
- Acceptance: 100% of rows verified by a human. Claude/CoCo must not mark rows verified.
- Depends on: #1

**#3 [B] Synthetic hospital generator (seed 42) + ground-truth exposures**
Labels: area:data, P0
- Tasks: phase G of `CLAUDE_CODE_DATA_PLAN.md`, including:
  - seeded real NSQ batches;
  - batch-string noise;
  - ~15% blank batches;
  - decoys;
  - scenario A (DEG-like) and scenario B (sterility).
- Acceptance: `validate_data.py` synthetic checks pass; `data/synthetic/README.md` is written.
- Depends on: #1 (needs parsed NSQ rows to seed)

**#4 [C] Repo conventions & CoCo setup guide**
Labels: area:platform, P0
- Tasks:
  - README skeleton, PR template and issue template;
  - `docs/coco_log.md` template;
  - `docs/setup_coco_cli.md` (install, connection config, role);
  - `.gitignore` for creds;
  - snow CLI `config.toml.example`.
- Acceptance: a new teammate can set up in 15 minutes by following the docs.

**#5 [C] Wireframes for 5 screens + demo storyline**
Labels: area:app, P1
- Tasks: low-fi wireframes (markdown or Excalidraw PNG) in `docs/wireframes.md` for:
  - (1) Alert Inbox;
  - (2) Batch Detail;
  - (3) Patient Card + Action List;
  - (4) Ask Kavach (agent chat);
  - (5) Regulator & Accuracy view.
  
  Plus a first draft of `docs/demo_script.md` (Coldrif-style story, 4 minutes).
- Acceptance: team agrees on the screens before M3.

### M1 · Snowflake foundation (27 Sep)

**#6 [C] Activate trial, account setup, RBAC, cost guardrails**
Labels: area:platform, P0
- Tasks:
  - activate the team trial (see Section 4) and add a payment method;
  - `ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION='ANY_REGION'` if needed;
  - warehouses `WH_BUILD` and `WH_APP` (X-Small, auto-suspend 60 s);
  - resource monitor (notify at 50/75/90%, suspend at 100% of a team-agreed quota);
  - users for A and B;
  - roles `KAVACH_ADMIN`, `KAVACH_ENGINEER`, `KAVACH_APP`, `KAVACH_PHARMACIST`, `KAVACH_CLINICIAN`, `KAVACH_JUDGE_RO`;
  - grant `SNOWFLAKE.CORTEX_USER` and CoCo access (`SNOWFLAKE.COPILOT_USER`) to the engineer roles.
- CoCo CLI: every member runs one trivial CoCo CLI session and logs it.
- Acceptance:
  - `snowflake/00_account_setup.sql` and `01_rbac.sql` committed;
  - all 3 can run CoCo CLI;
  - the resource monitor is active.

**#7 [A] Database, schemas, stages (SSE + directory tables)**
Labels: area:platform, P0
- Tasks:
  - `KAVACH` database with schemas `RAW`, `CORE`, `APP`, `EVAL`, `GOV`, plus personal dev schemas `DEV_A`, `DEV_B`, `DEV_C`;
  - stages `@RAW.CDSCO_PDFS`, `@RAW.REFERENCE_DOCS` and `@RAW.HOSPITAL`, using `ENCRYPTION=(TYPE='SNOWFLAKE_SSE')` and `DIRECTORY=(ENABLE=TRUE)`. Server-side encryption is required for Cortex document functions on internal stages.
- Acceptance: `02_*.sql` and `03_*.sql` run cleanly on a fresh account.
- Depends on: #6

**#8 [A] Upload PDFs & reference docs; load baseline + gold tables**
Labels: area:data, P0
- Tasks:
  - `snow stage copy` the PDFs, keeping the folder structure as a path prefix;
  - refresh the directory tables;
  - load `nsq_baseline_parsed.csv` into `EVAL.BASELINE_PARSE` and the gold CSV into `EVAL.GOLD_NSQ`;
  - add a `scripts/upload_to_stage.sh` wrapper.
- Acceptance: `SELECT COUNT(*) FROM DIRECTORY(@RAW.CDSCO_PDFS)` equals the PDF count in the manifest.
- Depends on: #1, #7

**#9 [B] Load synthetic hospital into RAW and model CORE hospital tables**
Labels: area:data, P0
- Tasks:
  - PUT the Parquet files;
  - `COPY INTO` with `INFER_SCHEMA`;
  - build CORE tables with primary/foreign keys (informational) and comments;
  - load `exposures_truth` into `EVAL` only, never into CORE or APP.
- CoCo CLI: ask CoCo to generate the DDL from the staged Parquet and to write column comments; review them.
- Acceptance: FK checks return 0 orphans; row counts match the generator output.
- Depends on: #3, #7

### M2 · Core pipelines

**#10 [A] Parse alert PDFs with AI_PARSE_DOCUMENT → RAW.NSQ_PAGES**
Labels: area:ingest, P0, coco
- Tasks:
  - run `AI_PARSE_DOCUMENT(TO_FILE(...), {'mode':'LAYOUT','page_split':true})` over the directory table;
  - store `source_file, page_index, content_markdown, parsed_at`;
  - parse each file exactly once (idempotent MERGE).
- CoCo CLI: have CoCo write and test the SQL against 2 PDFs first.
- Acceptance: every page of every PDF is present; 3 sampled pages spot-checked and readable.
- Depends on: #8

**#11 [A] Structured row extraction per page → RAW.NSQ_ROWS_EXTRACTED**
Labels: area:ingest, P0, coco
- Tasks:
  - per-page `AI_COMPLETE` with a JSON-schema response format. Fields: `product_name, brand_name, batch_no_raw, mfg_date_raw, exp_date_raw, manufacturer_raw, nsq_result, reporting_lab, row_no`;
  - also try `AI_EXTRACT` in table mode on one page for comparison, and document which is better and why;
  - do NOT extract a whole document in one call, because table output is capped at about 4k tokens;
  - skip non-table pages such as definitions and footers.
- Acceptance: row count per month is within ±5% of the baseline parse; the decision is noted in `docs/architecture.md`.
- Depends on: #10

**#12 [A] Normalization UDFs + CORE.NSQ_ALERT (one row per batch)**
Labels: area:ingest, P0
- Tasks: Snowpark Python UDFs for:
  - `normalize_batch()`: uppercase, strip spaces, hyphens, slashes and dots, remove "B.No:";
  - `split_batches()`: turn a multi-batch cell into an array, then FLATTEN;
  - `parse_alert_date()`: handle MM/YYYY, DD-MM-YYYY and broken lines;
  - `normalize_manufacturer()`.

  Then build `CORE.NSQ_ALERT` with `alert_id, alert_month, category (central/state/spurious), source_file, page_index, …normalized fields…, raw fields`.
- Acceptance:
  - unit tests in `tests/sql_checks/`;
  - the known tricky rows (multi-batch cell, split batch, date broken across lines) are handled correctly.
- Depends on: #11

**#13 [A] Extraction accuracy vs gold set → EVAL.EXTRACTION_METRICS**
Labels: area:eval, P0
- Tasks:
  - field-level exact-match accuracy plus row-level precision and recall for June 2025 central;
  - compare the Cortex pipeline against the pdfplumber baseline;
  - write `docs/eval_report.md`.
- Acceptance: the headline number exists (e.g. "batch number accuracy 97%"). Report honestly, whatever it is.
- Depends on: #2, #12

**#14 [A] Severity classification (AI_CLASSIFY + rules)**
Labels: area:ai, P0
- Tasks: `AI_CLASSIFY` on `nsq_result` into categories:
  - sterility / endotoxin;
  - particulate matter;
  - toxic contaminant (DEG/EG);
  - assay (strength);
  - dissolution;
  - description / labeling;
  - spurious;
  - other.

  Then rules combining the category with dosage form (injection, oral liquid, tablet…) give `severity` = critical / high / low, plus a one-line rationale. Examples: sterility or particulate in an injectable → critical; description only → low.
- Acceptance: a 30-row manual spot check shows ≥90% agreement; the rules are documented.
- Depends on: #12

**#15 [A] Automation: new PDF → processed end to end (stream + task)**
Labels: area:ingest, P1, coco
- Tasks:
  - stream on the `@RAW.CDSCO_PDFS` directory table;
  - a task (or task graph) running parse → extract → normalize → severity for new files only;
  - the Dynamic Tables downstream refresh automatically.
- CoCo CLI: turn this into the custom skill `.cortex/skills/kavach-monthly-run/SKILL.md` ("process a newly uploaded CDSCO month and report matches").
- Acceptance: uploading one held-back month (e.g. June 2025) triggers the full pipeline with no manual SQL. This is the demo moment.
- Depends on: #12, #14

**#16 [A] Ingest portal extracts (Aug 2025 → latest) into CORE.NSQ_ALERT**
Labels: area:ingest, P1
- Tasks: load `portal_nsq.csv` (from `CLAUDE_CODE_DATA_PLAN.md` phase C) with `record_origin='portal'` into the same normalized table.
- Acceptance: months from Aug 2025 onward appear in the app. If the portal fetch failed, close this as "won't do" with a note.
- Depends on: #1, #12

**#17 [B] Matching engine: Dynamic Table CORE.BATCH_MATCHES**
Labels: area:matching, P0
- Tasks: match `CORE.NSQ_ALERT` against `stock_batches` and `dispensing` in three tiers:
  - **exact:** normalized batch equal + `JAROWINKLER_SIMILARITY(manufacturer) ≥ 85` + expiry within ±1 month;
  - **probable:** normalized batch equal but weak manufacturer match, OR `EDITDISTANCE(batch) = 1` with the same composition and maker;
  - **watchlist:** same product and maker, different batch → no patient action;
  - **blank batch:** a patient got the same product and maker during the alert batch's validity window, but no batch was recorded → "possible exposure".

  Store `match_tier, match_score, reasons (array)`.
- Acceptance: the Dynamic Table refreshes on new alerts; decoys never land in exact or probable.
- Depends on: #9, #12

**#18 [B] Matching accuracy vs ground truth → EVAL.MATCH_METRICS**
Labels: area:eval, P0
- Tasks: precision and recall per tier against `EVAL.EXPOSURES_TRUTH`; a confusion table; add results to `docs/eval_report.md`.
- Acceptance: exact-tier precision ≥ 0.98; decoy false-positive rate reported.
- Depends on: #17

**#19 [B] Patient exposure + clinical watch → CORE.PATIENT_EXPOSURE, CORE.CLINICAL_FLAGS**
Labels: area:ai, P0
- Tasks:
  - build the exposure table: patient, dispense event, alert, tier, severity, days since dose;
  - add signal rules by failure category:
    - toxic contaminant in an oral liquid → creatinine >1.5× baseline within 3–10 days;
    - sterility or endotoxin in an injectable → temperature >38.5 °C or WBC rise within 48 h;
    - assay or dissolution failure in a chronic drug (e.g. telmisartan) → "efficacy review" flag;
  - produce a `flag_reason` in plain English using `AI_COMPLETE` with a strict template. Wording must be "needs clinician review".
- Acceptance: scenario A and B patients are flagged; normal-lab patients are not.
- Depends on: #17

**#20 [B] Action list + multilingual callback scripts → APP.ACTION_ITEMS**
Labels: area:ai, P0
- Tasks:
  - generate actions: `QUARANTINE_STOCK` (store, batch, qty), `CALL_PATIENT`, `CLINICIAN_REVIEW`, `REPORT_TO_REGULATOR`;
  - statuses: open / done / not reachable;
  - write a callback script with `AI_COMPLETE` (short, calm, non-alarming) and translate it with `AI_TRANSLATE` into the patient's preferred language (ml / hi / ta);
  - write-back from the app updates the status with the user and timestamp (audit trail).
- Acceptance: each exposed patient has exactly one callback action with a script in their language.
- Depends on: #19

**#21 [C] Governance: tags, masking, row access, judge role**
Labels: area:platform, P1
- Tasks:
  - tag PHI-like columns (`GOV.PII` tag);
  - masking policy: name and phone are masked except for `KAVACH_PHARMACIST` and `KAVACH_CLINICIAN`;
  - row access policy by `store_id` for pharmacist users;
  - `KAVACH_JUDGE_RO` sees masked data only.

  Show all of this in the MVP doc: the data is synthetic, but the product is built for real patient data.
- Acceptance: querying as the judge role shows masked values.
- Depends on: #9

### M3 · Intelligence & App

**#22 [A] Cortex Search service over alerts + CDSCO guidance (citations)**
Labels: area:ai, P0, coco
- Tasks:
  - chunk `RAW.NSQ_PAGES` and the parsed reference docs (recall guideline, guidance document, Rule 65) into `CORE.SEARCH_CHUNKS`, with `source_file, page_index, doc_type`;
  - create a Cortex Search service with attributes for filtering (`doc_type, alert_month`).
- Acceptance: the query "what must a hospital do when a batch is declared NSQ" returns the recall-guideline chunk with its page number.
- Depends on: #10

**#23 [B] Semantic view KAVACH_SV (built with CoCo CLI)**
Labels: area:ai, P0, coco
- Tasks: use CoCo's semantic-view skill to build `KAVACH_SV`:
  - **entities:** alerts, batches, stock, dispensing, patients, wards, exposures, flags, actions;
  - **metrics:** `exposed_patients`, `critical_matches`, `open_callbacks`, `blank_batch_rate`, `nsq_by_manufacturer`, `repeat_offender_count`;
  - **synonyms:** e.g. "bad batch" = NSQ, "syrup" = oral liquid;
  - **verified queries:** at least 10.
- Acceptance: all 10 verified queries answer correctly in Cortex Analyst; the CoCo session is logged.
- Depends on: #17, #19, #20

**#24 [B] Cortex Agent "Kavach Assistant" + evaluation set**
Labels: area:ai, P0, coco
- Tasks: build the agent via CoCo's agent-studio skill, with tools:
  - Cortex Analyst (`KAVACH_SV`);
  - Cortex Search (#22);
  - one custom tool: stored procedure `GET_PATIENT_TIMELINE(patient_id)`.

  The system prompt enforces three rules: cite sources, use "needs review" language, refuse diagnosis. Write `tests/agent_questions.yaml` with 15 questions and expected answers, e.g. "Which children got a failed syrup in the last 90 days?" or "Why was batch X flagged critical?".
- Acceptance: ≥13 of 15 correct, with citations; results in `docs/eval_report.md`.
- Depends on: #22, #23

**#25 [A] Monthly alert brief (AI_AGG / AI_SUMMARIZE_AGG) + email Alert**
Labels: area:ai, P1
- Tasks:
  - a view producing a one-paragraph "this month" brief for the pharmacy head: counts, critical items, top failure types, repeat manufacturers;
  - a Snowflake `ALERT` object that fires when new exact or probable matches appear and sends the brief via `SYSTEM$SEND_EMAIL` (notification integration, verified team emails).
- Acceptance: a test email is received after the #15 demo upload.
- Depends on: #15, #17

**#26 [A] Regulator insights views**
Labels: area:ai, P1
- Tasks: views for:
  - NSQ counts by state, manufacturer and failure type over time;
  - repeat-offender manufacturers;
  - **states not reporting** each month, parsed from the state-alert header notes;
  - time from manufacture to alert (how long bad batches circulate).
- Acceptance: data powers screen 5.
- Depends on: #12

**#27 [C] Streamlit in Snowflake scaffold (multi-page) + shared data layer**
Labels: area:app, P0, coco
- Tasks:
  - SiS app with pages 1–5, a shared `lib/queries.py`, and a theme;
  - the same code must run on Streamlit Community Cloud: branch on the environment to get the session (`get_active_session()` in SiS, a key-pair connection elsewhere).
- Acceptance: the app deploys in SiS and all pages load with placeholder queries.
- Depends on: #7

**#28 [C] Screens 1 & 2: Alert Inbox + Batch Detail (with PDF citation)**
Labels: area:app, P0
- Tasks:
  - **Inbox:** month selector; cards for "N batches in alert, X match your stock, Y patients exposed, Z critical"; the monthly brief (#25).
  - **Batch Detail:** alert fields, severity and rationale, match tier and reasons, stock locations to quarantine, exposed patient list, and an **"Open source PDF (page n)"** button using `GET_PRESIGNED_URL`.
- Acceptance: a click-through from inbox to batch to PDF page works.
- Depends on: #17, #20, #27

**#29 [C] Screen 3: Patient Card + Action workflow**
Labels: area:app, P0
- Tasks:
  - medication timeline with batch numbers, with the flagged dose highlighted;
  - lab trend chart with the flag window shaded;
  - callback script in the patient's language;
  - action buttons (done / not reachable / escalate) that write back to `APP.ACTION_ITEMS`;
  - masked view for non-clinical roles.
- Acceptance: completing a callback updates the status and the inbox counts.
- Depends on: #19, #20, #27

**#30 [C] Screen 4: Ask Kavach (agent chat)**
Labels: area:app, P0
- Tasks: chat UI calling the Cortex Agent (via the Agents REST API from SiS; check the current Snowflake docs for the supported call). Render tables, citations and follow-up suggestions. Provide 5 starter questions.
- Acceptance: the 5 starter questions work live, with citations shown.
- Depends on: #24, #27

**#31 [C] Screen 5: Regulator view + "How accurate is Kavach?" page**
Labels: area:app, P1
- Tasks:
  - state heatmap / bar charts, repeat offenders, non-reporting states (#26);
  - an accuracy page showing extraction metrics (#13) and matching metrics (#18) honestly.
- Acceptance: numbers match `docs/eval_report.md`.
- Depends on: #13, #18, #26, #27

**#32 [C] Public deployment for judges**
Labels: area:app, P0
- Tasks:
  - mirror the app to Streamlit Community Cloud;
  - key-pair auth for a service user holding `KAVACH_JUDGE_RO` and `WH_APP`;
  - secrets stored only in Streamlit secrets;
  - rate-limit the agent calls;
  - put a "synthetic data" banner on every page.

  Fallback: a judge login to the SiS app, documented in the submission.
- Acceptance: the public URL works in an incognito window on a phone; no credentials in the repo.
- Depends on: #21, #28–#30

### M4 · Ship

**#33 [A] One-command rebuild + fresh-account test**
Labels: area:platform, P0
- Tasks:
  - `make deploy` (or `scripts/deploy.sh`) runs `snowflake/*.sql` in order, uploads the data, and creates Search, Semantic View, Agent and the app;
  - test it into a **zero-copy clone or a fresh schema set**;
  - write `99_teardown.sql`.
- Acceptance: the README's rebuild steps work first time for another team member.
- Depends on: most of M2/M3

**#34 [C] End-to-end demo run-through (Coldrif-style story)**
Labels: area:docs, P0
- Tasks: finalize `docs/demo_script.md` and do 2 full dry runs. The story:
  1. "A new CDSCO month drops."
  2. Upload the PDF, and the task processes it (#15).
  3. The email alert arrives (#25).
  4. Inbox → critical syrup batch → 6 children exposed → 3 flagged kidney values → callback scripts in Malayalam.
  5. Ask Kavach a question.
  6. Show the accuracy page.

  Time the whole run at under 4 minutes.
- Acceptance: two clean dry runs; every step works without manual SQL.
- Depends on: #15, #25, #28–#31

**#35 [C] MVP / prototype documentation (mandatory submission)**
Labels: area:docs, P0
- Tasks: write `docs/MVP.md` (also export it to PDF) covering:
  - problem, with sources;
  - how it differs from existing tools (MedicineWatch India = consumer lookup; ECRI = US inventory recalls);
  - users;
  - architecture diagram;
  - the Snowflake feature list with *why each is used*;
  - CoCo CLI usage (from `coco_log.md`) and the custom skill;
  - accuracy results;
  - governance;
  - limitations: synthetic patients, state reporting gaps, missing batch capture in real pharmacies;
  - roadmap: QR scan at dispensing, pharmacy chains, state drug controllers.

  A and B contribute their sections as PRs.
- Acceptance: reviewed by all three; exported PDF committed.
- Depends on: #13, #18, #24

**#36 [C] Demo video (3–5 min)**
Labels: area:docs, P0
- Tasks: record the demo script with narration; upload it (YouTube unlisted or Drive); link it in the README and MVP doc.
- Acceptance: video link works, and the video is under 5 minutes.
- Depends on: #34

**#37 [A+B+C] CoCo CLI evidence pack**
Labels: area:docs, P1, coco
- Tasks:
  - each member adds at least 3 meaningful entries to `docs/coco_log.md` (prompt → generated → edited);
  - finish the custom skill in `.cortex/skills/kavach-monthly-run/`;
  - add a short "How we used CoCo CLI" section to the MVP doc.
- Acceptance: at least 9 log entries; the skill runs.
- Assignees: all three (owner A)

**#38 [C] Trial safety & finale readiness**
Labels: area:platform, P1
- Tasks:
  - suspend idle warehouses and check resource-monitor usage daily;
  - before the trial expires, unload key tables to the stage and download them (backup);
  - plan for the finale (27–30 Oct), since the trial ends at about that time: either add paid usage or have the video plus a rebuild path;
  - keep the public app working through judging (5–22 Oct).
- Acceptance: the backup exists in the repo release assets; the finale plan is written in the README.

**#39 [C] Final submission on Hack2skill portal (due 4 Oct)**
Labels: area:docs, P0
- Tasks: submit the GitHub repo link, the deployed app link and the MVP documentation; double-check every link in incognito; screenshot the confirmation.
- Acceptance: submission confirmed before the deadline.
- Depends on: #32, #35, #36

**#40 [C] EPIC: Kavach — tracking issue**
Labels: epic
- Body: checklist of #1–#39 grouped by milestone; the owner table; key dates. Pin this issue.

---

## 9. Instructions for Claude Code: creating the issues

1. **Check the environment.** `gh auth status` and `gh repo view`. ⛔ Ask me for:
   - the repo (`owner/name`);
   - the GitHub usernames for A, B and C;
   - whether to create a GitHub Project board (needs the `project` scope: `gh auth refresh -s project`).
2. **Generate `issues/issues.yaml`** from Section 8 (id, title, owner, labels, milestone, body using the template, depends_on). ⛔ Show me a summary table (id, title, owner, milestone, priority) and wait for approval.
3. **Create labels** (idempotent, `gh label create --force`):
   - `owner:A`, `owner:B`, `owner:C`;
   - `area:data`, `area:ingest`, `area:matching`, `area:ai`, `area:eval`, `area:app`, `area:platform`, `area:docs`;
   - `P0`, `P1`, `P2`;
   - `coco`, `epic`.
4. **Create milestones** M0–M4 with the due dates from Section 7 (`gh api repos/{owner}/{repo}/milestones -f title=... -f due_on=...T18:29:59Z`, which is 23:59 IST).
5. **Create the issues** in order #1 → #39 with `gh issue create --title --body-file --label --milestone --assignee`. Record the mapping from plan id to real GitHub issue number in `issues/created.json`.
6. **Second pass for dependencies:** edit each body so "Depends on" uses the real issue numbers (`#<real>`). Then create the EPIC (#40) with a task list of the real numbers, and pin it (`gh issue pin`).
7. **Optional:** create the Project board "Kavach Hackathon" with columns Todo / In progress / Review / Done, and add all issues.
8. **Report back:**
   - the table of created issues with links;
   - the per-person counts (a rough balance check);
   - anything that failed.

**Do not:** close, delete or edit existing issues that aren't from this plan; push code changes; or create issues twice (check `issues/created.json` first).

---

## 10. Daily rhythm (27 Sep – 4 Oct)

- **09:30 IST:** 10-minute stand-up (yesterday / today / blocked). Move cards on the board.
- **Before sleeping:** push the branch and open or update the PR; C checks credit usage.
- **Critical path:** #6 → #7 → #8/#9 → #10 → #11 → #12 → #17 → #19/#20 → #23 → #24 → #28–#30 → #32 → #34 → #39.

  If anything on this path slips by more than half a day, drop P1 items first: #16, #25's email, #26, #31's heatmap.
