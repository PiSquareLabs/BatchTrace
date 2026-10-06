-- BatchTrace: Upload CSVs and load into hospital tables
-- Run after 01_setup.sql and 02_tables.sql
-- Expects CSV files in data/load/ and data/demo/

USE SCHEMA BATCHTRACE.CORE;

-- ============================================================
-- PUT CSV files to internal stage
-- ============================================================

-- Main data (data/load/)
PUT file://data/load/BAT_BATCHES.csv          @BATCHTRACE.RAW.SEED_DATA/BAT_BATCHES/          AUTO_COMPRESS=TRUE OVERWRITE=TRUE;
PUT file://data/load/PAT_PATIENTS.csv         @BATCHTRACE.RAW.SEED_DATA/PAT_PATIENTS/         AUTO_COMPRESS=TRUE OVERWRITE=TRUE;
PUT file://data/load/PAT_APPOINTMENTS.csv     @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENTS/     AUTO_COMPRESS=TRUE OVERWRITE=TRUE;
PUT file://data/load/PAT_APPOINTMENT_DRUGS.csv @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENT_DRUGS/ AUTO_COMPRESS=TRUE OVERWRITE=TRUE;

-- Demo data (data/demo/)
PUT file://data/demo/PAT_PATIENTS.csv         @BATCHTRACE.RAW.SEED_DATA/PAT_PATIENTS_DEMO/         AUTO_COMPRESS=TRUE OVERWRITE=TRUE;
PUT file://data/demo/PAT_APPOINTMENTS.csv     @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENTS_DEMO/     AUTO_COMPRESS=TRUE OVERWRITE=TRUE;
PUT file://data/demo/PAT_APPOINTMENT_DRUGS.csv @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENT_DRUGS_DEMO/ AUTO_COMPRESS=TRUE OVERWRITE=TRUE;

-- ============================================================
-- COPY INTO: main data first, then demo data
-- Order matters for FK constraints: batches & patients first, then appointments, then drugs
-- ============================================================

-- 1. BAT_BATCHES (3,184 rows)
TRUNCATE TABLE BAT_BATCHES;
COPY INTO BAT_BATCHES (batch_id, batch_no, brand_name, generic_composition, dosage_form,
  manufacturer, therapeutic_group, mfg_date, exp_date, store_location,
  qty_on_hand, unit, received_date, supplier)
FROM @BATCHTRACE.RAW.SEED_DATA/BAT_BATCHES/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

-- 2. PAT_PATIENTS: main (2,190) + demo (5) = 2,195
TRUNCATE TABLE PAT_PATIENTS;
COPY INTO PAT_PATIENTS (patient_id, patient_name, sex, date_of_birth, age,
  blood_group, phone, district, known_allergies, registered_on)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_PATIENTS/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

COPY INTO PAT_PATIENTS (patient_id, patient_name, sex, date_of_birth, age,
  blood_group, phone, district, known_allergies, registered_on)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_PATIENTS_DEMO/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

-- 3. PAT_APPOINTMENTS: main (5,711) + demo (25) = 5,736
TRUNCATE TABLE PAT_APPOINTMENTS;
COPY INTO PAT_APPOINTMENTS (appointment_id, patient_id, appointment_date, visit_type,
  department, doctor, diagnosis, doctor_notes, follow_up_date)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENTS/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

COPY INTO PAT_APPOINTMENTS (appointment_id, patient_id, appointment_date, visit_type,
  department, doctor, diagnosis, doctor_notes, follow_up_date)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENTS_DEMO/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

-- 4. PAT_APPOINTMENT_DRUGS: main (8,805) + demo (21) = 8,826
TRUNCATE TABLE PAT_APPOINTMENT_DRUGS;
COPY INTO PAT_APPOINTMENT_DRUGS (line_id, appointment_id, patient_id, dispense_date,
  batch_id, batch_no_recorded, brand_name, manufacturer, dose, frequency,
  route, duration_days, qty, unit)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENT_DRUGS/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

COPY INTO PAT_APPOINTMENT_DRUGS (line_id, appointment_id, patient_id, dispense_date,
  batch_id, batch_no_recorded, brand_name, manufacturer, dose, frequency,
  route, duration_days, qty, unit)
FROM @BATCHTRACE.RAW.SEED_DATA/PAT_APPOINTMENT_DRUGS_DEMO/
FILE_FORMAT = (FORMAT_NAME = 'BATCHTRACE.RAW.CSV_FMT')
ON_ERROR = ABORT_STATEMENT;

-- ============================================================
-- Verification
-- ============================================================

SELECT 'BAT_BATCHES' AS tbl, COUNT(*) AS cnt FROM BAT_BATCHES          -- expect 3184
UNION ALL SELECT 'PAT_PATIENTS',          COUNT(*) FROM PAT_PATIENTS          -- expect 2195
UNION ALL SELECT 'PAT_APPOINTMENTS',      COUNT(*) FROM PAT_APPOINTMENTS      -- expect 5736
UNION ALL SELECT 'PAT_APPOINTMENT_DRUGS', COUNT(*) FROM PAT_APPOINTMENT_DRUGS -- expect 8826
ORDER BY 1;

-- Orphan batch_ids (expect 0)
SELECT COUNT(*) AS orphan_batch_ids
FROM PAT_APPOINTMENT_DRUGS d
LEFT JOIN BAT_BATCHES b USING (batch_id)
WHERE d.batch_id IS NOT NULL AND b.batch_id IS NULL;

-- Blank batch_id share (expect ~12%)
SELECT ROUND(100*AVG(IFF(batch_id IS NULL,1,0)),1) AS pct_blank_batch_id
FROM PAT_APPOINTMENT_DRUGS;

-- Batch TS24047 joins through to P90004
SELECT DISTINCT p.patient_id
FROM PAT_APPOINTMENT_DRUGS d
JOIN BAT_BATCHES b USING (batch_id)
JOIN PAT_PATIENTS p ON p.patient_id = d.patient_id
WHERE b.batch_no = 'TS24047';
