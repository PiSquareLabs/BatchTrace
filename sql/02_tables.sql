-- BatchTrace: All 16 tables + 2 views in BATCHTRACE.CORE
-- Generated via GET_DDL('SCHEMA', 'BATCHTRACE.CORE')
-- Run after 01_setup.sql

USE SCHEMA BATCHTRACE.CORE;

-- ============================================================
-- Hospital tables
-- ============================================================

create or replace TABLE BAT_BATCHES (
	BATCH_ID VARCHAR(16777216) NOT NULL COMMENT 'Synthetic surrogate key (B00001…). Primary key.',
	BATCH_NO VARCHAR(16777216) COMMENT 'Manufacturer batch/lot number as printed on packaging.',
	BRAND_NAME VARCHAR(16777216) COMMENT 'Commercial brand name of the medicine.',
	GENERIC_COMPOSITION VARCHAR(16777216) COMMENT 'Active ingredient(s) and strength.',
	DOSAGE_FORM VARCHAR(16777216) COMMENT 'Form: Tablet, Injection, Syrup, etc.',
	MANUFACTURER VARCHAR(16777216) COMMENT 'Name of the pharmaceutical manufacturer.',
	THERAPEUTIC_GROUP VARCHAR(16777216) COMMENT 'Clinical category: Antibiotic, Cardiovascular, etc.',
	MFG_DATE VARCHAR(16777216) COMMENT 'Manufacturing date as YYYY-MM string.',
	EXP_DATE VARCHAR(16777216) COMMENT 'Expiry date as YYYY-MM string.',
	STORE_LOCATION VARCHAR(16777216) COMMENT 'Physical storage area in hospital: Main Pharmacy, OPD Pharmacy, ICU Store, etc.',
	QTY_ON_HAND NUMBER(38,0) COMMENT 'Current quantity in stock.',
	UNIT VARCHAR(16777216) COMMENT 'Unit of measure: strip, vial/amp, bottle, tube.',
	RECEIVED_DATE DATE COMMENT 'Date the batch was received from the supplier.',
	SUPPLIER VARCHAR(16777216) COMMENT 'Distributor/supplier who delivered the batch.',
	QUARANTINED BOOLEAN DEFAULT FALSE COMMENT 'TRUE if this batch has been quarantined after an alert match.',
	QUARANTINED_AT TIMESTAMP_NTZ(9) COMMENT 'Timestamp when quarantine was applied.',
	QUARANTINED_BY VARCHAR(16777216) COMMENT 'User who performed the quarantine action.',
	primary key (BATCH_ID)
) COMMENT='One row per batch of medicine on the hospital shelves. 54 are real failed batches from CDSCO June-2025 lists, 12 are decoys (same medicine/maker, different batch). quarantined/quarantined_at/quarantined_by are set by the pipeline when a batch is flagged.';

create or replace TABLE PAT_PATIENTS (
	PATIENT_ID VARCHAR(16777216) NOT NULL COMMENT 'Unique patient identifier (P00001… or P9000x for demo). Primary key.',
	PATIENT_NAME VARCHAR(16777216) COMMENT 'Full name of the patient.',
	SEX VARCHAR(16777216) COMMENT 'M or F.',
	DATE_OF_BIRTH DATE COMMENT 'Date of birth.',
	AGE NUMBER(38,0) COMMENT 'Age in years at time of data generation.',
	BLOOD_GROUP VARCHAR(16777216) COMMENT 'Blood group: A+, B-, O+, AB+, etc.',
	PHONE VARCHAR(16777216) COMMENT 'Phone number (synthetic, invalid).',
	DISTRICT VARCHAR(16777216) COMMENT 'District of residence in Kerala/Tamil Nadu.',
	KNOWN_ALLERGIES VARCHAR(16777216) COMMENT 'Known drug allergies or None known.',
	REGISTERED_ON DATE COMMENT 'Date the patient was registered at the hospital.',
	primary key (PATIENT_ID)
) COMMENT='Synthetic patients: 2190 main + 5 demo (P90001-P90005). Phone numbers deliberately invalid (+91-00000-xxxxx).';

create or replace TABLE PAT_APPOINTMENTS (
	APPOINTMENT_ID VARCHAR(16777216) NOT NULL COMMENT 'Unique appointment identifier. Primary key.',
	PATIENT_ID VARCHAR(16777216) COMMENT 'FK to PAT_PATIENTS.patient_id.',
	APPOINTMENT_DATE DATE COMMENT 'Date of the visit.',
	VISIT_TYPE VARCHAR(16777216) COMMENT 'OPD or IPD.',
	DEPARTMENT VARCHAR(16777216) COMMENT 'Hospital department: General Medicine, Cardiology, Surgery, etc.',
	DOCTOR VARCHAR(16777216) COMMENT 'Prescribing doctor name.',
	DIAGNOSIS VARCHAR(16777216) COMMENT 'Clinical diagnosis for this visit.',
	DOCTOR_NOTES VARCHAR(16777216) COMMENT 'Free-text clinical notes. May contain commas, quotes, degree symbols, en-dashes.',
	FOLLOW_UP_DATE DATE COMMENT 'Scheduled follow-up date, NULL if none.',
	SOURCE_INGESTION_ID NUMBER(38,0) COMMENT 'Links to ALERT_INGESTION when this appointment was created by the pipeline. NULL for seed data.',
	primary key (APPOINTMENT_ID),
	constraint FK_APPT_PATIENT foreign key (PATIENT_ID) references BATCHTRACE.CORE.PAT_PATIENTS(PATIENT_ID)
) COMMENT='Doctor visits with diagnosis and free-text notes: 5711 main + 25 demo. 47 main visits are not-responding follow-ups after an under-dose batch. source_ingestion_id links visits created by the pipeline.';

create or replace TABLE PAT_APPOINTMENT_DRUGS (
	LINE_ID VARCHAR(16777216) NOT NULL COMMENT 'Unique line item identifier. Primary key.',
	APPOINTMENT_ID VARCHAR(16777216) COMMENT 'FK to PAT_APPOINTMENTS.appointment_id.',
	PATIENT_ID VARCHAR(16777216) COMMENT 'FK to PAT_PATIENTS.patient_id.',
	DISPENSE_DATE DATE COMMENT 'Date the drug was dispensed.',
	BATCH_ID VARCHAR(16777216) COMMENT 'FK to BAT_BATCHES.batch_id. NULL when batch was not recorded.',
	BATCH_NO_RECORDED VARCHAR(16777216) COMMENT 'Batch number as written by pharmacist. May be messy or blank.',
	BRAND_NAME VARCHAR(16777216) COMMENT 'Brand name of the drug dispensed.',
	MANUFACTURER VARCHAR(16777216) COMMENT 'Manufacturer of the drug dispensed.',
	DOSE VARCHAR(16777216) COMMENT 'Dose per administration, e.g. 1 tab, 5 ml.',
	FREQUENCY VARCHAR(16777216) COMMENT 'Dosing frequency: OD, BD, TDS, QID, STAT, SOS, HS.',
	ROUTE VARCHAR(16777216) COMMENT 'Route of administration: Oral, IV/IM, Topical, etc.',
	DURATION_DAYS NUMBER(38,0) COMMENT 'Number of days prescribed.',
	QTY NUMBER(38,0) COMMENT 'Quantity dispensed.',
	UNIT VARCHAR(16777216) COMMENT 'Unit: tab, strip, bottle, vial/amp, tube, cap.',
	primary key (LINE_ID),
	constraint FK_DRUG_APPOINTMENT foreign key (APPOINTMENT_ID) references BATCHTRACE.CORE.PAT_APPOINTMENTS(APPOINTMENT_ID),
	constraint FK_DRUG_PATIENT foreign key (PATIENT_ID) references BATCHTRACE.CORE.PAT_PATIENTS(PATIENT_ID),
	constraint FK_DRUG_BATCH foreign key (BATCH_ID) references BATCHTRACE.CORE.BAT_BATCHES(BATCH_ID)
) COMMENT='Each drug dispensed at each visit with batch used: 8805 main + 21 demo lines. ~12% have NULL batch_id (batch not recorded), creating possible-exposure cases.';

-- ============================================================
-- Alert tables
-- ============================================================

create or replace TABLE APP_CONFIG (
	KEY VARCHAR(16777216) NOT NULL,
	VALUE VARCHAR(16777216),
	primary key (KEY)
) COMMENT='Key-value settings read by procedures and the app: model name, email, snapshot date, thresholds.';

create or replace TABLE ALERT_INGESTION (
	INGESTION_ID NUMBER(38,0) NOT NULL autoincrement start 1 increment 1 noorder,
	FILE_PATH VARCHAR(16777216),
	FILE_NAME VARCHAR(16777216),
	FILE_SIZE_BYTES NUMBER(38,0),
	SHA256 VARCHAR(16777216),
	UPLOADED_AT TIMESTAMP_NTZ(9) DEFAULT CURRENT_TIMESTAMP(),
	UPLOADED_BY VARCHAR(16777216) DEFAULT CURRENT_USER(),
	LIST_TYPE VARCHAR(16777216),
	ALERT_MONTH VARCHAR(16777216),
	ISSUER VARCHAR(16777216),
	CLASSIFY_CONFIDENCE FLOAT,
	STATUS VARCHAR(16777216),
	primary key (INGESTION_ID)
) COMMENT='One row per uploaded PDF. Tracks file metadata, classification result, and processing status.';

create or replace TABLE ALERT_INGESTION_STEPS (
	INGESTION_ID NUMBER(38,0),
	STEP_NO NUMBER(38,0),
	STEP_NAME VARCHAR(16777216),
	STATUS VARCHAR(16777216),
	STARTED_AT TIMESTAMP_NTZ(9),
	ENDED_AT TIMESTAMP_NTZ(9),
	ROWS_OUT NUMBER(38,0),
	MESSAGE VARCHAR(16777216),
	DETAILS VARIANT
) COMMENT='Step-level log for each ingestion: step name, status, timing, row counts, error details.';

create or replace TABLE ALERT_PAGES (
	INGESTION_ID NUMBER(38,0),
	PAGE_NO NUMBER(38,0),
	MODE_USED VARCHAR(16777216),
	CONTENT VARCHAR(16777216),
	CHAR_COUNT NUMBER(38,0)
) COMMENT='Extracted text content per page of each ingested PDF, with mode (text vs OCR) and char count.';

create or replace TABLE ALERT_ROWS_RAW (
	INGESTION_ID NUMBER(38,0),
	PAGE_NO NUMBER(38,0),
	ROW_NO NUMBER(38,0),
	DRUG_TEXT VARCHAR(16777216),
	BATCH_NO VARCHAR(16777216),
	MFG_DATE VARCHAR(16777216),
	EXP_DATE VARCHAR(16777216),
	MANUFACTURER VARCHAR(16777216),
	REASON VARCHAR(16777216),
	REPORTING_LAB VARCHAR(16777216),
	EXTRA VARIANT
) COMMENT='Raw rows extracted from PDF pages before normalization: drug text, batch, dates, manufacturer, reason.';

create or replace TABLE ALERT_ITEMS (
	ALERT_ITEM_ID NUMBER(38,0) NOT NULL autoincrement start 1 increment 1 noorder,
	INGESTION_ID NUMBER(38,0),
	PAGE_NO NUMBER(38,0),
	ROW_NO NUMBER(38,0),
	LIST_TYPE VARCHAR(16777216),
	BRAND_OR_DRUG VARCHAR(16777216),
	GENERIC_TEXT VARCHAR(16777216),
	BATCH_NO_RAW VARCHAR(16777216),
	BATCH_NO_NORM VARCHAR(16777216),
	MFG_DATE VARCHAR(16777216),
	EXP_DATE VARCHAR(16777216),
	MANUFACTURER VARCHAR(16777216),
	MAKER_CLEAN VARCHAR(16777216),
	FAILURE_TEXT VARCHAR(16777216),
	HARM_TYPE VARCHAR(16777216),
	SEVERITY VARCHAR(16777216),
	NEEDS_REVIEW BOOLEAN,
	primary key (ALERT_ITEM_ID)
) COMMENT='Normalized alert items with cleaned batch numbers, manufacturer names, harm type, severity, and review flag.';

create or replace TABLE ALERT_MATCHES (
	INGESTION_ID NUMBER(38,0),
	ALERT_ITEM_ID NUMBER(38,0),
	BATCH_ID VARCHAR(16777216),
	MATCH_TYPE VARCHAR(16777216),
	SCORE FLOAT,
	STATUS VARCHAR(16777216) DEFAULT 'AUTO'
) COMMENT='Matches between alert items and hospital batches. score is JAROWINKLER_SIMILARITY. status: AUTO, CONFIRMED, or REJECTED.';

create or replace TABLE ALERT_TRIAGE (
	INGESTION_ID NUMBER(38,0),
	PATIENT_ID VARCHAR(16777216),
	LINE_ID VARCHAR(16777216),
	ALERT_ITEM_ID NUMBER(38,0),
	PRIORITY VARCHAR(16777216),
	REASON VARCHAR(16777216),
	QUOTED_NOTE VARCHAR(16777216),
	CREATED_AT TIMESTAMP_NTZ(9) DEFAULT CURRENT_TIMESTAMP()
) COMMENT='Patient-level triage: which patients were exposed to matched batches, with priority and clinical note quotes.';

-- ============================================================
-- Report and history tables
-- ============================================================

create or replace TABLE ALERT_REPORTS (
	REPORT_ID NUMBER(38,0) NOT NULL autoincrement start 1 increment 1 noorder,
	INGESTION_ID NUMBER(38,0),
	CREATED_AT TIMESTAMP_NTZ(9) DEFAULT CURRENT_TIMESTAMP(),
	CREATED_BY VARCHAR(16777216) DEFAULT CURRENT_USER(),
	SOURCE_FILE VARCHAR(16777216),
	LIST_TYPE VARCHAR(16777216),
	ALERT_MONTH VARCHAR(16777216),
	ALERT_ITEMS NUMBER(38,0),
	AFFECTED_BATCHES NUMBER(38,0),
	UNITS_TO_QUARANTINE NUMBER(38,0),
	EXPOSED_PATIENTS NUMBER(38,0),
	POSSIBLE_EXPOSURES NUMBER(38,0),
	SUMMARY VARCHAR(16777216),
	REPORT_MD VARCHAR(16777216),
	STATUS VARCHAR(16777216) DEFAULT 'NEW',
	EMAILED_AT TIMESTAMP_NTZ(9),
	CLOSED_AT TIMESTAMP_NTZ(9),
	CLOSED_BY VARCHAR(16777216),
	primary key (REPORT_ID)
) COMMENT='Summary reports generated per ingestion: counts, affected batches/patients, markdown report, status lifecycle.';

create or replace TABLE ALERT_REPORT_BATCHES (
	REPORT_ID NUMBER(38,0),
	BATCH_ID VARCHAR(16777216),
	BATCH_NO VARCHAR(16777216),
	BRAND VARCHAR(16777216),
	MAKER VARCHAR(16777216),
	STORE_LOCATION VARCHAR(16777216),
	QTY_AT_REPORT NUMBER(38,0),
	EXP_DATE VARCHAR(16777216),
	HARM_TYPE VARCHAR(16777216),
	SEVERITY VARCHAR(16777216),
	REASON VARCHAR(16777216),
	SOURCE_PAGE NUMBER(38,0),
	SOURCE_ROW NUMBER(38,0)
) COMMENT='Batch-level detail rows within a report: batch info, harm type, severity, source page/row.';

create or replace TABLE ALERT_REPORT_PATIENTS (
	REPORT_ID NUMBER(38,0),
	PATIENT_ID VARCHAR(16777216),
	PATIENT_NAME VARCHAR(16777216),
	LINE_ID VARCHAR(16777216),
	BRAND VARCHAR(16777216),
	BATCH_NO VARCHAR(16777216),
	DATE_GIVEN DATE,
	PRESCRIBER VARCHAR(16777216),
	DEPARTMENT VARCHAR(16777216),
	HARM_TYPE VARCHAR(16777216),
	EXPOSURE VARCHAR(16777216),
	PRIORITY VARCHAR(16777216),
	NOTE_ADDED BOOLEAN DEFAULT FALSE,
	NOTE_APPOINTMENT_ID VARCHAR(16777216)
) COMMENT='Patient-level detail rows within a report: exposure, priority, prescriber, whether a note was added.';

create or replace TABLE ALERT_ACTIONS (
	ACTION_ID NUMBER(38,0) NOT NULL autoincrement start 1 increment 1 noorder,
	REPORT_ID NUMBER(38,0),
	INGESTION_ID NUMBER(38,0),
	ACTION_TYPE VARCHAR(16777216),
	TARGET_ID VARCHAR(16777216),
	DETAIL VARIANT,
	DONE_BY VARCHAR(16777216) DEFAULT CURRENT_USER(),
	DONE_AT TIMESTAMP_NTZ(9) DEFAULT CURRENT_TIMESTAMP(),
	primary key (ACTION_ID)
) COMMENT='Audit log of actions taken: quarantine, note addition, report closure, email sent.';

-- ============================================================
-- Views
-- ============================================================

create or replace view EXPOSURES (
	INGESTION_ID,
	ALERT_ITEM_ID,
	PATIENT_ID,
	LINE_ID,
	BATCH_ID,
	EXPOSURE,
	HARM_TYPE
) COMMENT='Union of Exposed (drug line batch_id matched an alert) and Possible (NULL batch_id but same brand+manufacturer has a matched batch) exposures.'
as
SELECT
    am.ingestion_id,
    am.alert_item_id,
    d.patient_id,
    d.line_id,
    d.batch_id,
    'Exposed'       AS exposure,
    ai.harm_type
FROM BATCHTRACE.CORE.PAT_APPOINTMENT_DRUGS d
JOIN BATCHTRACE.CORE.ALERT_MATCHES am
  ON d.batch_id = am.batch_id
  AND am.status IN ('AUTO','CONFIRMED')
JOIN BATCHTRACE.CORE.ALERT_ITEMS ai
  ON am.alert_item_id = ai.alert_item_id

UNION ALL

SELECT
    am.ingestion_id,
    am.alert_item_id,
    d.patient_id,
    d.line_id,
    NULL            AS batch_id,
    'Possible'      AS exposure,
    ai.harm_type
FROM BATCHTRACE.CORE.PAT_APPOINTMENT_DRUGS d
JOIN BATCHTRACE.CORE.BAT_BATCHES b2
  ON d.brand_name = b2.brand_name
  AND d.manufacturer = b2.manufacturer
JOIN BATCHTRACE.CORE.ALERT_MATCHES am
  ON b2.batch_id = am.batch_id
  AND am.status IN ('AUTO','CONFIRMED')
JOIN BATCHTRACE.CORE.ALERT_ITEMS ai
  ON am.alert_item_id = ai.alert_item_id
WHERE d.batch_id IS NULL;

create or replace view DOCTORS (
	DOCTOR,
	DEPARTMENT
) COMMENT='Distinct doctor and department pairs from PAT_APPOINTMENTS.'
as
SELECT DISTINCT doctor, department
FROM BATCHTRACE.CORE.PAT_APPOINTMENTS;
