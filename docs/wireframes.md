# Wireframes — 5 screens

Low-fi wireframes for the Streamlit-in-Snowflake app (issue #5). Each screen lists its purpose,
the data it shows, the actions it offers and the tables it reads. They follow the build specs in
#28–#31 and the demo story in #34 / [`demo_script.md`](demo_script.md).

Example values come from **scenario A** in the synthetic hospital: batch `OL-032309`, KOFVON LS
cough syrup, Feb-2024 CDSCO list, "Ethylene Glycol exceeding the permissible limit", 6 children
exposed, 3 with creatinine > 2x baseline. Counts shown are illustrative, **not** measured results.

## Rules for every screen

- **Cite, don't claim:** every alert-derived fact carries `source_file + page`, and the PDF opens
  via `GET_PRESIGNED_URL`.
- **Clinical wording:** flags say "needs clinician review", never a diagnosis.
- **Role-aware:** patient name and phone are masked except for `KAVACH_PHARMACIST` and
  `KAVACH_CLINICIAN` (masking policy, #21). `KAVACH_JUDGE_RO` always sees masked data.
- **App reads `CORE`/`APP`/`EVAL` only.** Never `RAW`, never ground truth.
- The sidebar has pages 1–5 plus the current role and month.

---

## Screen 1 — Alert Inbox (`app/pages/1_Alert_Inbox.py`, #28)

**Purpose:** the landing page. It answers "a new CDSCO month dropped — does it affect us?" in
one glance.

```
+----------------------------------------------------------------+
| Alert Inbox                              Month: [ Feb 2024  v ] |
+----------------------------------------------------------------+
| +------------+ +------------+ +------------+ +------------+     |
| | 64 batches | | 3 match    | | 9 patients | | 1 critical |     |
| | in alert   | | your stock | | exposed    | |            |     |
| +------------+ +------------+ +------------+ +------------+     |
+----------------------------------------------------------------+
| Monthly brief (AI_SUMMARIZE_AGG, #25)                           |
| "One critical match this month: EG-contaminated paediatric      |
|  syrup dispensed to 6 children ... needs clinician review."     |
+----------------------------------------------------------------+
| Sev.     | Product            | Batch     | Match tier | Pts |    |
| CRITICAL | KOFVON LS Syrup    | OL-032309 | exact      |  6  | >  |
| HIGH     | ...                | ...       | probable   |  2  | >  |
| MEDIUM   | ...                | ...       | watchlist  |  1  | >  |
| ...      | (non-matching batches collapsed: 61)            |    |
+----------------------------------------------------------------+
```

- **Data shown:**
  - KPI cards: batches in the alert, batches matching our stock, patients exposed, critical count.
  - The monthly brief.
  - Matched batches, sorted by severity and then patient count. Non-matching batches are
    collapsed.
- **Actions:**
  - pick a month;
  - open a row, which goes to Screen 2;
  - expand the non-matching batches.
- **Reads:** `CORE.NSQ_ALERT`, `CORE.BATCH_MATCHES`, `CORE.PATIENT_EXPOSURE` (for the counts)
  and the monthly brief table from #25.

---

## Screen 2 — Batch Detail (`app/pages/2_Batch_Detail.py`, #28)

**Purpose:** everything about one flagged batch. It shows why Kavach flagged it, where the
stock sits and who received it.

```
+----------------------------------------------------------------+
| < Inbox    KOFVON LS Syrup - batch OL-032309    [ CRITICAL ]    |
+----------------------------------------------------------------+
| Alert fields                      | Severity rationale          |
| Manufacturer: Sickcure Pharma...  | Contaminant (EG) + oral     |
| Mfg 2023-03  Exp 2025-02          | paediatric syrup -> CRITICAL|
| Result: Ethylene Glycol (EG)      | (AI_CLASSIFY + rules, #14)  |
|   exceeding permissible limit     |                             |
| [ Open source PDF (page n) ]      | 2024-02_combined.pdf, p. n  |
+----------------------------------------------------------------+
| Match tiers & reasons                                           |
|  exact     4  batch_no identical (3 QR scans, 1 manual)         |
|  probable  1  hand-typed "ol-032309" - matches after normalising|
|  watchlist 1  batch blank at dispensing; same product + window  |
+----------------------------------------------------------------+
| Quarantine stock                                                |
|  Store      | Batch     | Qty on hand                           |
|  SAT1       | OL-032309 | n                                     |
+----------------------------------------------------------------+
| Exposed patients (6)                                            |
|  Patient  | Age band | Dispensed   | Tier   | Flag              |
|  P03225   | child    | 2024-02-28  | exact  | needs review   >  |
|  P03993   | child    | 2024-03-05  | probable | needs review >  |
|  P03899   | child    | 2024-04-21  | watchlist | -           >  |
|  ...  (3 more, dispensed Aug-Oct 2024 - after the alert)        |
+----------------------------------------------------------------+
```

- **Data shown:**
  - the normalised alert fields;
  - severity with its rationale;
  - match-tier counts, each with the reason it matched;
  - stock locations and quantities to quarantine;
  - the exposed-patient list.
- **Actions:**
  - "Open source PDF (page n)", which uses `GET_PRESIGNED_URL` on `@RAW.CDSCO_PDFS`;
  - open a patient, which goes to Screen 3.
- **Reads:** `CORE.NSQ_ALERT`, `CORE.BATCH_MATCHES` (tier and reason), the `CORE` stock table
  (store and quantity on hand) and `CORE.PATIENT_EXPOSURE`.

---

## Screen 3 — Patient Card + Action workflow (`app/pages/3_Patient_Card.py`, #29)

**Purpose:** clinical follow-up for one exposed patient. It answers what they got, when, whether
their labs moved, and what to do next.

```
+----------------------------------------------------------------+
| < Batch    Patient P0xxxx  |  Age 0-4  |  Name: ****  Ph: ****  |
+----------------------------------------------------------------+
| Medication timeline                                             |
|  --o--------o==========[X]==========o---------->  time          |
|    Rx A     Rx B    KOFVON LS OL-032309 (flagged dose)          |
+----------------------------------------------------------------+
| Creatinine trend                        ░░░ flag window 3-10 d  |
|   2x baseline - - - - - - - - - - - - -░░░-/--------            |
|   baseline  ____________________________░░░/                    |
|                            dispensed ^                           |
|   [ needs clinician review ]                                    |
+----------------------------------------------------------------+
| Action item: recall + clinical review   Status: OPEN            |
| Callback script  [ Malayalam v ]                                |
|  "..."  (AI_TRANSLATE, #20)                         [ Copy ]    |
|                                                                 |
|  [ Done ]   [ Not reachable ]   [ Escalate to clinician ]       |
+----------------------------------------------------------------+
```

- **Data shown:**
  - a medication timeline with batch numbers, with the flagged dose highlighted;
  - a lab trend with the flag window shaded and the 2x-baseline line;
  - the clinical flag;
  - the action item and a callback script in the patient's preferred language (en / ml / ta /
    hi in the synthetic data).
- **Actions:**
  - switch the script language;
  - **Done / Not reachable / Escalate**, which write the status, user and timestamp back to
    `APP.ACTION_ITEMS`.
  - The masked view hides name and phone for non-clinical roles.
- **Reads:** the `CORE` patient, dispensing and lab tables, `CORE.PATIENT_EXPOSURE` and
  `CORE.CLINICAL_FLAGS`.
- **Writes:** `APP.ACTION_ITEMS`.

---

## Screen 4 — Ask Kavach (`app/pages/4_Ask_Kavach.py` + `app/lib/agent.py`, #30)

**Purpose:** free-text questions answered by the Cortex Agent, for anything the fixed screens
don't cover.

```
+----------------------------------------------------------------+
| Ask Kavach                                                      |
| Try: [Which critical batches match our stock this month?]       |
|      [Which children got OL-032309 and who has a lab flag?]     |
|      [What does CDSCO guidance say about recall timelines?]     |
|      [Which manufacturers appear most often in NSQ lists?]      |
|      [How many callbacks are still open?]                       |
+----------------------------------------------------------------+
| You: Which children got OL-032309 and who has a lab flag?       |
| Kavach:                                                         |
|  | Patient | Dispensed  | Tier  | Flag                  |        |
|  | P0xxxx  | 2024-xx-xx | exact | needs clinician review|        |
|  Source: 2024-02_combined.pdf, p. n                             |
|  Follow-ups: [Show callback status] [Where is the stock?]        |
+----------------------------------------------------------------+
| [ Ask a question...                                 ] [ Send ]  |
+----------------------------------------------------------------+
```

- **Data shown:**
  - answers rendered as text or tables;
  - citations (`source_file + page` for alerts, the document name for CDSCO guidance);
  - follow-up suggestion chips.
- **Actions:**
  - click a starter question, or type one;
  - click a citation to open the PDF;
  - click a follow-up chip.
- **Reads:** Cortex Agent "Kavach Assistant" (#24), which uses Cortex Analyst over `KAVACH_SV`
  (#23) and Cortex Search (#22). The page itself never queries tables directly.

---

## Screen 5 — Regulator view + "How accurate is Kavach?" (`app/pages/5_Regulator_Accuracy.py`, #31)

**Purpose:** the regulator-level picture from the CDSCO data across all months, plus an honest
account of how well the pipeline works.

```
+-------------------------------+--------------------------------+
| Regulator view                | How accurate is Kavach?         |
| Range: [ Aug-25 ] - [ Aug-26 ]|                                 |
| NSQ batches by state          | Extraction vs hand-verified     |
|  [ heatmap / bar chart ]      | gold set (Jun-2025, ~55 rows)   |
|                               |  field      precision  recall   |
| Repeat-offender manufacturers |  batch_no     --        --      |
|  Mfr         | Months | Batches|  mfg/exp      --        --      |
|  ...         |   ...  |   ...  |  mfr          --        --      |
|                               |                                 |
| Non-reporting states          | Matching vs synthetic truth     |
|  (states with no list in N m) |  tier       precision  recall   |
|                               |  exact        --        --      |
|                               |  probable     --        --      |
|                               |  decoys wrongly flagged: --     |
|                               | Known gaps & caveats: ...       |
+-------------------------------+--------------------------------+
```

- **Data shown:**
  - NSQ batches by state (a heatmap or bar chart);
  - repeat-offender manufacturers;
  - non-reporting states (#26);
  - extraction precision and recall per field against the gold set (#13);
  - matching precision and recall per tier, plus decoy false positives (#18);
  - known gaps, stated plainly.
- **No patient-level data on this screen.**
- **Actions:**
  - change the month range;
  - drill into a manufacturer, which shows its batches in Screen 2's format.
- **Reads:** the regulator insight views (#26), `EVAL.EXTRACTION_METRICS` and
  `EVAL.MATCH_METRICS`.
- The metric cells show `--` until #13 and #18 produce real numbers. Never hard-code numbers
  here.

---

## Open questions (agree before M3)

1. Should Screen 1 hide non-matching batches by default (as drawn) or list them all?
2. Screen 3 lab chart: show only the flagged lab (creatinine, or temp/WBC for scenario B), or
   every abnormal lab?
3. Should a non-clinical role reach Screen 3 at all, in masked form, or be blocked?
4. Screen 5: do we need a separate regulator role, or is `KAVACH_JUDGE_RO` enough for the demo?
