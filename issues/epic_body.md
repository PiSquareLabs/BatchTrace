Tracking issue for **Kavach** (Snowflake CoCo CLI Hackathon 2026 · GCC · Track 4). Plan: `CLAUDE_CODE_TEAM_PLAN.md` · generated issues: `issues/issues.yaml`.

**How to read the issues:** every issue title starts with its milestone (`[M0]`…`[M4]`) and owner. Each body has: **Goal**, a table (owner · due date · priority · critical path · step in the overall order and in your own queue), **You need before starting**, numbered **Tasks**, **Deliverables** (files/objects to create), **Acceptance criteria**, **Depends on** (with ✅ when done) and **Unblocks**.

## Team
| Person | Role | GitHub |
|---|---|---|
| A | Data & Pipeline | @xreedev |
| B | Intelligence (matching, AI, agent) | @safar-byte |
| C | Platform & Product (account, app, delivery) | @Fahad-Sajeem |

## Day-by-day plan (IST)
| Day | A · @xreedev | B · @safar-byte | C · @Fahad-Sajeem |
|---|---|---|---|
| **Sat 26 Sep** (M0) | #2 verify gold set | review synthetic data (#3 ✅), prep #9 DDL from Parquet | #4 conventions + CoCo guide, #5 wireframes |
| **Sun 27 Sep** (M1) | #7 schemas/stages → #8 uploads | #9 load hospital into CORE | **#6 claim trial (window closes 27 Sep UTC)**, RBAC, monitor; start #27 app shell |
| **Mon 28 Sep** | #10 parse → #11 extract | #9 FK checks; design #17 matching SQL on DEV_B | #27 app shell; #21 governance |
| **Tue 29 Sep** | #12 normalise → #14 severity | #17 matching Dynamic Table | #21 governance; #28 inbox with placeholder data |
| **Wed 30 Sep** (M2) | #13 accuracy, #15 automation, #16 portal | #19 exposure/flags → #20 actions, #18 match accuracy | #28 inbox + batch detail on real tables |
| **Thu 1 Oct** | #22 Cortex Search, #26 regulator views | #23 semantic view | #29 patient card |
| **Fri 2 Oct** (M3) | #25 brief + email | #24 agent + 15-question eval | #30 chat, #31 accuracy page, #32 public deploy |
| **Sat 3 Oct** | #33 one-command rebuild | agent fixes; MVP sections | #34 two dry runs, #35 MVP doc, #36 video |
| **Sun 4 Oct** (M4) | #37 CoCo log wrap-up | #37 | **#39 submit** (then #38 trial safety, ongoing) |

_#37 (CoCo log) and #38 (credit checks) are ongoing from 27 Sep. If the critical path slips > ½ day, drop P1 first: #16, #25's email, #26, #31's heatmap._

## Critical path
#6 → #7 → #8/#9 → #10 → #11 → #12 → #14 → #17 → #19 → #20 → #22/#23 → #24 → #28–#30 → #32 → #34 → #35/#36 → #39

## Work queue per person (in order)
### A · @xreedev
- [x] #1 Execute data acquisition plan (CDSCO PDFs, portal, drug master, reference docs) · P0 · due 09-26
- [ ] #2 Hand-verify gold set: June 2025 central NSQ list (~55 rows) · P0 · due 09-26
- [ ] #7 Database, schemas, stages (SSE + directory tables) · P0 · due 09-27 🔴
- [ ] #8 Upload PDFs & reference docs; load baseline + gold tables · P0 · due 09-27 🔴
- [ ] #10 Parse alert PDFs with AI_PARSE_DOCUMENT → RAW.NSQ_PAGES · P0 · due 09-30 🔴
- [ ] #11 Structured row extraction per page → RAW.NSQ_ROWS_EXTRACTED · P0 · due 09-30 🔴
- [ ] #12 Normalization UDFs + CORE.NSQ_ALERT (one row per batch) · P0 · due 09-30 🔴
- [ ] #14 Severity classification (AI_CLASSIFY + rules) · P0 · due 09-30 🔴
- [ ] #13 Extraction accuracy vs gold set → EVAL.EXTRACTION_METRICS · P0 · due 09-30
- [ ] #15 Automation: new PDF → processed end to end (stream + task) · P1 · due 09-30
- [ ] #16 Ingest portal extracts (Aug 2025 → latest) into CORE.NSQ_ALERT · P1 · due 09-30
- [ ] #22 Cortex Search service over alerts + CDSCO guidance (citations) · P0 · due 10-02 🔴
- [ ] #25 Monthly alert brief (AI_AGG / AI_SUMMARIZE_AGG) + email Alert · P1 · due 10-02
- [ ] #26 Regulator insights views · P1 · due 10-02
- [ ] #33 One-command rebuild + fresh-account test · P0 · due 10-04
- [ ] #37 CoCo CLI evidence pack · P1 · due 10-04

### B · @safar-byte
- [x] #3 Synthetic hospital generator (seed 42) + ground-truth exposures · P0 · due 09-26
- [ ] #9 Load synthetic hospital into RAW and model CORE hospital tables · P0 · due 09-27 🔴
- [ ] #17 Matching engine: Dynamic Table CORE.BATCH_MATCHES · P0 · due 09-30 🔴
- [ ] #19 Patient exposure + clinical watch → CORE.PATIENT_EXPOSURE, CORE.CLINICAL_FLAGS · P0 · due 09-30 🔴
- [ ] #20 Action list + multilingual callback scripts → APP.ACTION_ITEMS · P0 · due 09-30 🔴
- [ ] #18 Matching accuracy vs ground truth → EVAL.MATCH_METRICS · P0 · due 09-30
- [ ] #23 Semantic view KAVACH_SV (built with CoCo CLI) · P0 · due 10-02 🔴
- [ ] #24 Cortex Agent "Kavach Assistant" + evaluation set · P0 · due 10-02 🔴
- [ ] #37 CoCo CLI evidence pack · P1 · due 10-04

### C · @Fahad-Sajeem
- [ ] #4 Repo conventions & CoCo setup guide · P0 · due 09-26
- [ ] #5 Wireframes for 5 screens + demo storyline · P1 · due 09-26
- [ ] #6 Activate trial, account setup, RBAC, cost guardrails · P0 · due 09-27 🔴
- [ ] #21 Governance: tags, masking, row access, judge role · P1 · due 09-30
- [ ] #27 Streamlit in Snowflake scaffold (multi-page) + shared data layer · P0 · due 10-02
- [ ] #28 Screens 1 & 2: Alert Inbox + Batch Detail (with PDF citation) · P0 · due 10-02 🔴
- [ ] #29 Screen 3: Patient Card + Action workflow · P0 · due 10-02 🔴
- [ ] #30 Screen 4: Ask Kavach (agent chat) · P0 · due 10-02 🔴
- [ ] #32 Public deployment for judges · P0 · due 10-02 🔴
- [ ] #31 Screen 5: Regulator view + "How accurate is Kavach?" page · P1 · due 10-02
- [ ] #34 End-to-end demo run-through (Coldrif-style story) · P0 · due 10-04 🔴
- [ ] #35 MVP / prototype documentation (mandatory submission) · P0 · due 10-04 🔴
- [ ] #36 Demo video (3–5 min) · P0 · due 10-04 🔴
- [ ] #39 Final submission on Hack2skill portal (due 4 Oct) · P0 · due 10-04 🔴
- [ ] #37 CoCo CLI evidence pack · P1 · due 10-04
- [ ] #38 Trial safety & finale readiness · P1 · due 10-04

🔴 = critical path

## All issues by milestone
**M0 · Pre-activation** (due 2026-09-26): #1, #2, #3, #4, #5
**M1 · Snowflake foundation** (due 2026-09-27): #6, #7, #8, #9
**M2 · Core pipelines** (due 2026-09-30): #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21
**M3 · Intelligence & App** (due 2026-10-02): #22, #23, #24, #25, #26, #27, #28, #29, #30, #31, #32
**M4 · Ship** (due 2026-10-04): #33, #34, #35, #36, #37, #38, #39

## Key dates
- **26–27 Sep:** C claims the team Snowflake trial (claim window closes 27 Sep UTC)
- **4 Oct:** submission due (repo + deployed app + MVP doc)
- **5–22 Oct:** judging (keep the public app up)
- **27–30 Oct:** finale