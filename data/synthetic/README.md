# Synthetic hospital: Sahyadri Synthetic General Hospital

> ## ⚠️ All patient data is synthetic. Batch numbers in seeded rows are real public CDSCO NSQ batches.
> No real person, patient or encounter is represented. Names come from Faker (`en_IN`). Phone numbers use the prefix `+91-00…`, which is not a valid Indian mobile prefix.

**Generator:** `scripts/generate_synthetic_hospital.py --seed 42`. The output is deterministic: re-running with the same seed gives byte-identical CSVs.

**The hospital:** a fictional 300-bed hospital with a main pharmacy (`MAIN`) and two satellite stores (`SAT1` for paediatrics, `SAT2` for obstetrics/gynaecology and orthopaedics). The time window runs from 2024-01-01 to 2025-07-31.

## `hospital/` (loaded into the app; Parquet and CSV)

| Table | Rows | Columns |
|---|---|---|
| `patients` | 5,000 | `patient_id`, `name`, `sex`, `dob`, `age_band` (`<1`, `1-4`, `5-11`, `12-17`, `18-39`, `40-64`, `65+`; about 18% are under 12), `district`, `phone` (fake), `preferred_language` (ml/en/ta/hi) |
| `wards` | 12 | `ward_id`, `name`, `store_id` |
| `encounters` | 20,000 | `encounter_id`, `patient_id`, `ward_id`, `type` (OPD/IPD/ER), `admit_ts`, `discharge_ts`, `primary_dx_text` |
| `products` | about 1,590 | `product_id`, `brand_name`, `generic_composition`, `dosage_form`, `manufacturer`, `is_nsq_seeded`, `schedule` (H/H1/OTC) |
| `stock_batches` | about 6,100 | `batch_uid`, `product_id`, `batch_no`, `mfg_date`, `exp_date`, `store_id`, `qty_received`, `qty_on_hand`, `received_date`, `supplier` |
| `prescriptions` | about 60,000 | `rx_id`, `encounter_id`, `patient_id`, `product_id`, `dose`, `frequency`, `days`, `prescriber_id` |
| `dispensing` | about 60,000 | `disp_id`, `rx_id`, `patient_id`, `batch_uid` (nullable), `batch_no_as_recorded` (nullable), `qty`, `dispensed_ts`, `store_id`, `capture_method` |
| `labs` | about 40,100 | `lab_id`, `patient_id`, `encounter_id`, `test` (creatinine, WBC, temperature, CRP, ALT), `value`, `unit`, `ref_low`, `ref_high`, `collected_ts` |

**Products:** non-seeded products come from the drug master subset (`data/raw/drug_master/`). Seeded products use the product name, brand and manufacturer text exactly as printed in the CDSCO list.

### How dispensing records batches

`capture_method` decides what the record contains:

| `capture_method` | Share | `batch_uid` | `batch_no_as_recorded` |
|---|---|---|---|
| `qr_scan` | ~40% | set (link to `stock_batches`) | the exact batch number |
| `manual` | ~45% | null | hand-typed. About 25% of **all** dispensing rows are noisy (lowercase, extra or missing hyphens and spaces), and about 3% have an O↔0 or I↔1 swap |
| `blank` | ~15% | null | null (the pharmacy left the batch column empty) |

For blank rows, exposure can only be inferred from product, store and dispensing date against the batches that were in stock.

**Seeded NSQ batches:**
- About 5% of `stock_batches` are real batches from the CDSCO NSQ lists: the baseline PDF parse plus the portal's July 2025 rows. `ground_truth/seeded_nsq_batches.csv` lists their source file and row.
- They are dispensed at 0.3× the normal rate, so about 1% of dispensing is a true exposure.
- Every dispensing time falls between the batch's `received_date` and its `exp_date`.

**Near-miss decoys:** about 60% of seeded products also stock a batch from the same manufacturer whose batch number differs by 1–2 characters. A good matcher must **not** flag these.

### Clinical scenarios

These are labelled only in the ground truth.
- **A (DEG-like):** batch `OL-032309`, KOFVON LS cough syrup, flagged in the Feb-2024 list with "Ethylene Glycol (EG) is exceeding the permissible limit". Six children are exposed. Three of them show creatinine rising to more than 2× their baseline within 3–10 days.
- **B (sterility):** batch `1I245476`, Ringer-Lactate infusion, flagged in the Apr-2025 central list with "Sterility". Twelve IPD patients are exposed. Four of them show temperature above 38.5 °C and a WBC rise within 48 hours.

Scenario batches are dispensed only to their scenario patients. All other lab values are normal noise, with about 4% random abnormal results unrelated to any batch.

## `ground_truth/`: evaluation only, NEVER load into the app schema

- **`exposures_truth.csv`:** one row per dispensing event of a seeded NSQ batch or a decoy. Columns:
  - `patient_id`, `disp_id`;
  - `true_batch_uid`, `true_batch_no`, `nsq_batch_no`;
  - `nsq_source_file`, `nsq_row_no`, `nsq_origin`;
  - `match_type`: `exact`, `noisy`, `blank_batch` or `decoy`;
  - `is_true_exposure` (false for decoys);
  - `capture_method`, `scenario`, `scenario_signal`.
- **`seeded_nsq_batches.csv`:** the real NSQ rows used as seeds.
- **`stock_batch_flags.csv`:** `batch_uid`, `is_nsq_batch`, `is_decoy`.
