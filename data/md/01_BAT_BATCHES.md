# Load BAT_BATCHES

One row per batch of medicine on the hospital's shelves (3,184 rows). 54 of them are real failed batches from CDSCO June-2025 lists (4 written messily), and 12 are decoys: same medicine and maker, different batch, which must NOT be flagged.

- Target: `BATCHTRACE.CORE.BAT_BATCHES` (the table must already exist)
- Rows: **3,184**
- Columns: `batch_id, batch_no, brand_name, generic_composition, dosage_form, manufacturer, therapeutic_group, mfg_date, exp_date, store_location, qty_on_hand, unit, received_date, supplier`
- All data is synthetic, except the real CDSCO batch numbers, products and makers.

## Prompt for CoCo
```
Read data/md/01_BAT_BATCHES.md. Copy the CSV block under "## Data" into data/tmp/BAT_BATCHES.csv, exactly as it is.
PUT it to @BATCHTRACE.RAW.SEED_DATA/BAT_BATCHES/ (AUTO_COMPRESS=TRUE, OVERWRITE=TRUE).
TRUNCATE BATCHTRACE.CORE.BAT_BATCHES, then COPY INTO it, listing these columns explicitly: batch_id, batch_no, brand_name, generic_composition, dosage_form, manufacturer, therapeutic_group, mfg_date, exp_date, store_location, qty_on_hand, unit, received_date, supplier.
Use file format BATCHTRACE.RAW.CSV_FMT (SKIP_HEADER=1, FIELD_OPTIONALLY_ENCLOSED_BY='"', EMPTY_FIELD_AS_NULL=TRUE, UTF-8) and ON_ERROR=ABORT_STATEMENT.
mfg_date and exp_date are 'YYYY-MM' strings, so keep them VARCHAR. Do not load into QUARANTINED / QUARANTINED_AT / QUARANTINED_BY; they keep their defaults.
Then run the checks below and show me the results. Do not touch any other table.
```

## Checks
```sql
SELECT COUNT(*) FROM BATCHTRACE.CORE.BAT_BATCHES;  -- expect 3184
SELECT COUNT(DISTINCT batch_id) FROM BATCHTRACE.CORE.BAT_BATCHES;  -- expect 3184
SELECT batch_id, brand_name, manufacturer, qty_on_hand FROM BATCHTRACE.CORE.BAT_BATCHES WHERE batch_no IN ('TS24047','24460967','SIF2736A','L0372321C','3305');  -- expect 5 rows
```

## Data
```csv
batch_id,batch_no,brand_name,generic_composition,dosage_form,manufacturer,therapeutic_group,mfg_date,exp_date,store_location,qty_on_hand,unit,received_date,supplier
B00001,NII249007,Voveran AQ Injection,Diclofenac (75mg),Injection,Novartis India Ltd,Analgesic/Antipyretic,2024-12,2027-12,Ward Store (Paeds),60,vial/amp,2024-12-28,Kerala Medical Supplies Co.
B00002,22838644,Daparyl 10 Tablet,Dapagliflozin (10mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-03,2027-03,Ward Store (Paeds),20,strip,2024-04-29,Apollo Wholesale Pvt Ltd
B00003,T2512-798,Gertum 250mg Tablet,Cefuroxime (250mg),Tablet,Zydus Cadila,Antibiotic,2024-06,2026-06,Emergency Store,100,strip,2024-09-09,Kerala Medical Supplies Co.
B00004,LL24A652,Defenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-05,2028-05,OPD Pharmacy,100,strip,2025-07-15,Sanjivani Drug House
B00005,I2508-771,Xylocaine 2% Injection,Lidocaine (2%),Injection,Zydus Cadila,Other,2024-03,2025-09,Emergency Store,120,vial/amp,2024-06-10,"Medline Distributors, Thiruvananthapuram"
B00006,88642156,Herpex 100mg Tablet,Acyclovir (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antiviral,2024-05,2026-05,OPD Pharmacy,20,strip,2024-08-20,Apollo Wholesale Pvt Ltd
B00007,T2501-190,Epizam 0.25mg Tablet MD,Clonazepam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-05,2027-05,OT Store,0,strip,2024-06-14,"Medline Distributors, Thiruvananthapuram"
B00008,LLX258797,DexLuz Oral Solution Lemon,Lactulose (10gm),Oral Solution,Lupin Ltd,Gastro,2024-04,2026-04,Emergency Store,100,bottle,2024-06-15,Sanjivani Drug House
B00009,28491548,Glador M 1 Forte Tablet PR,Glimepiride (1mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2024-03,2027-03,Emergency Store,30,strip,2024-06-17,Apollo Wholesale Pvt Ltd
B00010,T2412-520,Sitaxa M 50/1000 Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-03,2027-03,Emergency Store,10,strip,2025-04-28,Malabar Pharma Distributors
B00011,APX257652,Naresol 0.65% Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Alembic Pharmaceuticals Ltd,IV Fluids,2024-08,2026-08,OPD Pharmacy,60,bottle,2024-10-24,Malabar Pharma Distributors
B00012,35606639,Wysolone 10 Tablet DT,Prednisolone (10mg),Tablet,Pfizer Ltd,Steroid,2024-01,2027-01,ICU Store,80,strip,2024-01-28,Apollo Wholesale Pvt Ltd
B00013,74914236,Tayo-M Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Eris Lifesciences Ltd,Supplement,2025-01,2027-01,Emergency Store,80,strip,2025-02-01,Sanjivani Drug House
B00014,17284695,Zentel Chewable Tablet,Albendazole (400mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2024-10,2027-10,ICU Store,80,strip,2024-11-23,Sanjivani Drug House
B00015,ILT258891,Perinorm Mps 5 mg/125 mg Tablet,Metoclopramide (5mg) + Simethicone (125mg),Tablet,Ipca Laboratories Ltd,Gastro,2024-07,2026-01,Emergency Store,200,strip,2024-08-14,Sree Pharma Agencies
B00016,10128848,Uniwarfin 1mg Tablet,Warfarin (1mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-07,2026-07,OT Store,300,strip,2024-07-31,Sree Pharma Agencies
B00017,58796232,Iverintas 12mg Tablet,Ivermectin (12mg),Tablet,Intas Pharmaceuticals Ltd,Anthelmintic,2024-02,2027-02,Ward Store (Paeds),50,strip,2024-04-09,Apollo Wholesale Pvt Ltd
B00018,24561556,Bendex 200mg Suspension,Albendazole (200mg),Suspension,Cipla Ltd,Anthelmintic,2024-07,2026-07,OPD Pharmacy,60,bottle,2024-08-10,"Medline Distributors, Thiruvananthapuram"
B00019,TP24F986,Maxizon 1gm Injection,Ceftriaxone (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-12,2026-06,Ward Store (Paeds),120,vial/amp,2025-02-12,"Medline Distributors, Thiruvananthapuram"
B00020,65044235,Sustameto 100mg Tablet,Metoprolol Succinate (100mg),Tablet,Zydus Cadila,Cardiovascular,2024-03,2025-09,Ward Store (Paeds),300,strip,2024-05-24,Sree Pharma Agencies
B00021,AP25H319,D 10% Infusion,Dextrose (10% w/v),Infusion,AXA Parenterals Ltd,IV Fluids,2024-09,2027-09,Main Pharmacy,30,bottle,2024-10-08,Sree Pharma Agencies
B00022,ZCT246558,Aceclodus P 100 mg/500 mg Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Zydus Cadila,Analgesic/Antipyretic,2025-01,2027-01,Main Pharmacy,120,strip,2025-03-14,Kerala Medical Supplies Co.
B00023,43407750,Fulsed 1mg Injection,Midazolam (1mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-05,2026-05,Ward Store (Paeds),50,vial/amp,2024-07-27,Apollo Wholesale Pvt Ltd
B00024,TPI243226,Domadol 100mg Injection,Tramadol (100mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-05,2026-11,Ward Store (Paeds),0,vial/amp,2025-06-09,Sree Pharma Agencies
B00025,CLX245465,Clocip Cream,Clotrimazole (1% w/w),Cream,Cipla Ltd,Antifungal,2024-03,2027-03,Ward Store (Paeds),30,tube,2024-05-05,Sree Pharma Agencies
B00026,34727844,Anofer 100mg Injection,Iron Sucrose (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2024-12,2026-12,Emergency Store,10,vial/amp,2025-01-18,"Medline Distributors, Thiruvananthapuram"
B00027,T2507-754,Azepress 250mg Tablet,Azithromycin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2024-01,2026-01,OT Store,30,strip,2024-02-26,"Medline Distributors, Thiruvananthapuram"
B00028,SPT248683,Hydroquin 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Sun Pharmaceutical Industries Ltd,Antimalarial,2024-06,2025-12,Emergency Store,0,strip,2024-07-28,"Medline Distributors, Thiruvananthapuram"
B00029,66950588,Troypofol 10mg Injection,Propofol (10mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-07,2026-07,ICU Store,100,vial/amp,2024-07-29,Sanjivani Drug House
B00030,IP25K806,Monoloc 150mg Tablet,Ranitidine (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-12,2027-12,Main Pharmacy,30,strip,2025-01-26,Apollo Wholesale Pvt Ltd
B00031,CL25B481,Tranfib 100mg/ml Injection,Tranexamic Acid (500mg),Injection,Cipla Ltd,Haematology,2024-08,2027-08,Main Pharmacy,200,vial/amp,2024-10-29,Kerala Medical Supplies Co.
B00032,SKV241064,Dex 25% Infusion,Dextrose (25% w/v),Infusion,Shree KrishnaKeshav Laboratories Ltd,IV Fluids,2024-02,2026-02,Main Pharmacy,40,bottle,2024-04-05,Apollo Wholesale Pvt Ltd
B00033,81362827,Gabator 100 Capsule,Gabapentin (100mg),Capsule,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-01,2026-07,Emergency Store,20,strip,2025-01-31,Malabar Pharma Distributors
B00034,A24B853,Rivotril 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Abbott,Neurology/Psychiatry,2025-03,2027-03,Emergency Store,80,strip,2025-04-13,Apollo Wholesale Pvt Ltd
B00035,MLT240454,Balgyl 400mg Tablet,Metronidazole (400mg),Tablet,Micro Labs Ltd,Antibiotic,2024-02,2027-02,Ward Store (Paeds),20,strip,2024-03-20,Malabar Pharma Distributors
B00036,64711545,Solu-Medrol 125mg Injection,Methylprednisolone (125mg),Injection,Pfizer Ltd,Steroid,2025-02,2028-02,Ward Store (Paeds),80,vial/amp,2025-04-16,Apollo Wholesale Pvt Ltd
B00037,99757409,Hicoly 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2025-03,2028-03,OPD Pharmacy,50,vial/amp,2025-04-03,Kerala Medical Supplies Co.
B00038,69839681,Fusys 150 Tablet,Fluconazole (150mg),Tablet,Zydus Cadila,Antifungal,2024-02,2026-02,OPD Pharmacy,30,strip,2024-05-31,Kerala Medical Supplies Co.
B00039,LLI253903,Basugine 100IU/ml Injection,Insulin Glargine (100IU),Injection,Lupin Ltd,Diabetes,2024-12,2026-12,OPD Pharmacy,60,vial/amp,2025-03-28,Apollo Wholesale Pvt Ltd
B00040,SPC250928,Mox 500mg Capsule,Amoxycillin (500mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-04,2025-10,OPD Pharmacy,200,strip,2024-06-11,Kerala Medical Supplies Co.
B00041,AL25C882,Phenykem 100mg Tablet,Phenytoin (100mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-04,2026-04,Ward Store (Paeds),80,strip,2024-05-19,Malabar Pharma Distributors
B00042,S2404-447,Bendex 200mg Suspension,Albendazole (200mg),Suspension,Cipla Ltd,Anthelmintic,2025-03,2026-09,OT Store,50,bottle,2025-06-12,Malabar Pharma Distributors
B00043,PLT245589,Medrol 32mg Tablet,Methylprednisolone (32mg),Tablet,Pfizer Ltd,Steroid,2025-01,2026-07,Ward Store (Paeds),80,strip,2025-03-03,Sanjivani Drug House
B00044,SL24A033,Dopar 200mg Injection,Dopamine (200mg),Injection,Samarth Life Sciences Pvt Ltd,Anaesthesia/Critical care,2024-01,2027-01,Main Pharmacy,20,vial/amp,2024-03-11,Kerala Medical Supplies Co.
B00045,SII249832,Apidra 100IU/ml Solution for Injection,Insulin Glulisine (100IU),Injection,Sanofi India Ltd,Diabetes,2024-05,2025-11,Main Pharmacy,300,vial/amp,2024-05-27,Sanjivani Drug House
B00046,T2403-084,Cetcip-L Tablet,Levocetirizine (5mg),Tablet,Cipla Ltd,Respiratory,2025-01,2027-01,Ward Store (Paeds),0,strip,2025-04-05,Sree Pharma Agencies
B00047,SPT240434,Contiflo Icon 0.4mg Tablet PR,Tamsulosin (0.4mg),Tablet,Sun Pharmaceutical Industries Ltd,Urology,2024-07,2026-01,ICU Store,300,strip,2024-09-13,Sanjivani Drug House
B00048,T2503-243,Angibloc 12.5mg Tablet ER,Metoprolol Succinate (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-10,2026-10,OT Store,100,strip,2025-01-15,"Medline Distributors, Thiruvananthapuram"
B00049,T2503-195,Telma 40 Tablet,Telmisartan (40mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-07,2027-07,Main Pharmacy,30,strip,2024-09-01,Sanjivani Drug House
B00050,61650472,Azimed 100mg Oral Suspension,Azithromycin (100mg),Suspension,Zydus Cadila,Antibiotic,2024-07,2026-01,OPD Pharmacy,20,bottle,2024-10-06,Apollo Wholesale Pvt Ltd
B00051,DRT248638,Tryptomer 50mg Tablet,Amitriptyline (50mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2025-04,2026-10,OT Store,30,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B00052,I2511-148,Solu-Medrol 250mg Injection,Methylprednisolone (250mg),Injection,Pfizer Ltd,Steroid,2024-03,2027-03,Ward Store (Paeds),150,vial/amp,2024-05-03,Malabar Pharma Distributors
B00053,23654808,Swich 100 DT Tablet,Cefpodoxime Proxetil (100mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-08,2026-08,Main Pharmacy,50,strip,2024-10-01,Sanjivani Drug House
B00054,ZC24G884,Vinglyn SR Tablet,Vildagliptin (100mg),Tablet,Zydus Cadila,Diabetes,2025-01,2027-01,Ward Store (Paeds),0,strip,2025-04-17,Sanjivani Drug House
B00055,UL25K777,Glycomet 250 Tablet,Metformin (250mg),Tablet,USV Ltd,Diabetes,2024-11,2026-05,OPD Pharmacy,30,strip,2024-12-15,Sree Pharma Agencies
B00056,CLT255481,Ciplox 500 Tablet,Ciprofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2024-10,2026-04,Ward Store (Paeds),150,strip,2024-11-11,Malabar Pharma Distributors
B00057,RKI243402,Glumig Injection,Calcium Gluconate (10mg),Injection,RSM Kilitch Pharma Pvt Ltd,Anaesthesia/Critical care,2024-09,2026-09,Emergency Store,150,vial/amp,2024-11-03,Sanjivani Drug House
B00058,I2512-071,Instavil 22.75mg Injection,Pheniramine (22.75mg),Injection,Intas Pharmaceuticals Ltd,Anti-allergic,2024-01,2027-01,Ward Store (Paeds),40,vial/amp,2024-02-22,Sanjivani Drug House
B00059,DJI255433,D5 IV Injection,Dextrose (5% w/v),Injection,D.J Laboratories Pvt Ltd,IV Fluids,2024-03,2027-03,Emergency Store,10,vial/amp,2024-05-03,Malabar Pharma Distributors
B00060,IPI251962,Amitas 100mg Injection,Amikacin (100mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-09,2026-03,OT Store,60,vial/amp,2024-09-30,Sree Pharma Agencies
B00061,NLI255457,Mezolam 5mg Injection,Midazolam (5mg),Injection,Neon Laboratories Ltd,Neurology/Psychiatry,2024-07,2027-07,ICU Store,100,vial/amp,2024-09-13,"Medline Distributors, Thiruvananthapuram"
B00062,60142505,Ultracet 500mg/50mg Tablet,Paracetamol/Acetaminophen (500mg) + Tramadol (50mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2024-02,2027-02,OT Store,150,strip,2024-05-26,Sanjivani Drug House
B00063,I2507-319,Vancomax 1g Injection,Vancomycin (1000mg),Injection,Johnlee Pharmaceuticals Pvt Ltd,Antibiotic,2024-09,2026-03,OPD Pharmacy,50,vial/amp,2024-12-29,"Medline Distributors, Thiruvananthapuram"
B00064,TPC245036,Dalcap 150mg Capsule,Clindamycin (150mg),Capsule,Torrent Pharmaceuticals Ltd,Antibiotic,2025-01,2027-01,OPD Pharmacy,10,strip,2025-03-06,Sree Pharma Agencies
B00065,T2504-585,Digitran 0.25mg Tablet,Digoxin (0.25mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2025-03,2028-03,Ward Store (Paeds),80,strip,2025-06-26,Kerala Medical Supplies Co.
B00066,IRI241253,Cyclopam 10mg Injection,Dicyclomine (10mg),Injection,Indoco Remedies Ltd,Gastro,2024-08,2026-08,ICU Store,200,vial/amp,2024-11-07,Apollo Wholesale Pvt Ltd
B00067,72306017,Doliza 500mg Tablet,Paracetamol (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-10,2026-10,OPD Pharmacy,150,strip,2025-01-14,Kerala Medical Supplies Co.
B00068,33966966,Monocef 125mg Injection,Ceftriaxone (125mg),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2025-01,2026-07,Main Pharmacy,40,vial/amp,2025-04-10,"Medline Distributors, Thiruvananthapuram"
B00069,ZLI248346,Frusizex 10mg Injection,Furosemide (10mg/ml),Injection,Zee Laboratories,Cardiovascular,2024-06,2026-06,ICU Store,60,vial/amp,2024-07-07,"Medline Distributors, Thiruvananthapuram"
B00070,MLT244814,Atepres 50mg Tablet,Atenolol (50mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-08,2026-08,ICU Store,100,strip,2024-10-11,Apollo Wholesale Pvt Ltd
B00071,41491128,Oleanz 2.5 Tablet,Olanzapine (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-11,2026-11,Ward Store (Paeds),40,strip,2025-02-18,Malabar Pharma Distributors
B00072,TP25D426,Azulix 1 Tablet,Glimepiride (1mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-08,2026-02,OPD Pharmacy,20,strip,2024-09-01,Kerala Medical Supplies Co.
B00073,LLT251637,Allerkast LC Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Lupin Ltd,Respiratory,2024-03,2025-09,OT Store,30,strip,2024-05-02,Sanjivani Drug House
B00074,ZC24H736,Gerpyrin 1000mg Injection,Paracetamol (1000mg),Injection,Zydus Cadila,Analgesic/Antipyretic,2024-06,2026-06,Emergency Store,150,vial/amp,2024-09-02,Kerala Medical Supplies Co.
B00075,CLC242743,Urimax 0.4 Capsule MR,Tamsulosin (0.4mg),Capsule,Cipla Ltd,Urology,2025-02,2026-08,Emergency Store,40,strip,2025-05-23,Malabar Pharma Distributors
B00076,TPT254175,Unimegyl 200mg Tablet,Metronidazole (200mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-05,2026-05,OT Store,150,strip,2024-08-20,Apollo Wholesale Pvt Ltd
B00077,T2504-266,Prazopill XL 2.5 Tablet,Prazosin (2.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-02,2026-02,OT Store,50,strip,2024-05-25,Apollo Wholesale Pvt Ltd
B00078,NIT256279,Galvus Met 50mg/850mg Tablet,Metformin (850mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2024-11,2026-05,Main Pharmacy,80,strip,2025-02-04,Malabar Pharma Distributors
B00079,35496811,Novotam 2mg Injection,Ondansetron (2mg/ml),Injection,Lupin Ltd,Gastro,2024-10,2026-10,ICU Store,150,vial/amp,2025-01-21,Malabar Pharma Distributors
B00080,AP25B784,Osteofit-HD Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Alembic Pharmaceuticals Ltd,Supplement,2025-04,2027-04,OT Store,80,strip,2025-07-06,Apollo Wholesale Pvt Ltd
B00081,T2512-745,Aldactone 100 Tablet,Spironolactone (100mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2024-06,2025-12,OPD Pharmacy,10,strip,2024-08-04,Sanjivani Drug House
B00082,SPI240640,Mecabalin 500mcg Injection,Methylcobalamin (500mcg),Injection,Sun Pharmaceutical Industries Ltd,Supplement,2024-09,2026-09,ICU Store,40,vial/amp,2024-11-13,Sanjivani Drug House
B00083,CPI241834,Humanext N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Cadila Pharmaceuticals Ltd,Diabetes,2024-12,2026-12,Ward Store (Paeds),50,vial/amp,2025-01-03,Sree Pharma Agencies
B00084,ILI251849,Perinorm Injection,Metoclopramide (5mg/ml),Injection,Ipca Laboratories Ltd,Gastro,2024-07,2026-07,ICU Store,200,vial/amp,2024-10-14,Apollo Wholesale Pvt Ltd
B00085,AL25C639,Bodygard Gel,Diclofenac (NA),Gel,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-06,2027-06,OT Store,50,tube,2024-08-03,Sree Pharma Agencies
B00086,DR24H369,Stamlo 2.5 Tablet,Amlodipine (2.5mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-02,2027-02,Ward Store (Paeds),30,strip,2024-05-28,Malabar Pharma Distributors
B00087,IP24K389,Merex 1000mg Injection,Methotrexate (1000mg),Injection,Intas Pharmaceuticals Ltd,Oncology,2024-07,2026-07,Ward Store (Paeds),80,vial/amp,2024-09-14,Sanjivani Drug House
B00088,T2407-072,Zomet 500mg Tablet,Metformin (500mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-05,2026-05,Emergency Store,200,strip,2024-07-08,Apollo Wholesale Pvt Ltd
B00089,RLT246561,Aldactone 50 Tablet,Spironolactone (50mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2025-02,2028-02,Emergency Store,120,strip,2025-03-07,"Medline Distributors, Thiruvananthapuram"
B00090,T2412-835,Bipacef 500 Tablet,Cefuroxime (500mg),Tablet,Micro Labs Ltd,Antibiotic,2024-10,2026-04,Ward Store (Paeds),80,strip,2024-12-15,Sanjivani Drug House
B00091,IPT245443,Acticin 500mg Tablet,Paracetamol (500mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-10,2026-10,OPD Pharmacy,10,strip,2024-11-24,Malabar Pharma Distributors
B00092,TP25L903,Nausinorm 5mg Injection,Metoclopramide (5mg),Injection,Torrent Pharmaceuticals Ltd,Gastro,2025-01,2027-01,Emergency Store,10,vial/amp,2025-03-22,Kerala Medical Supplies Co.
B00093,IPT258691,Intamox O 1500mg Tablet,Amoxycillin (1500mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-07,2026-07,Main Pharmacy,80,strip,2024-08-03,Kerala Medical Supplies Co.
B00094,I2405-871,Advent 1.2gm Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Cipla Ltd,Antibiotic,2025-02,2026-08,Main Pharmacy,60,vial/amp,2025-04-15,Sanjivani Drug House
B00095,19101846,Duphaston Pro Tablet,Dydrogesterone (10mg),Tablet,Abbott,Other,2024-11,2027-11,Ward Store (Paeds),100,strip,2025-02-05,"Medline Distributors, Thiruvananthapuram"
B00096,30017834,Candid Gold Dusting Powder,Allantoin (0.2% w/w) + Clotrimazole (1% w/w),Powder,Glenmark Pharmaceuticals Ltd,Antifungal,2024-01,2026-02,Emergency Store,300,pack,2024-02-06,"Medline Distributors, Thiruvananthapuram"
B00097,CLT254848,Metolar 50 Tablet,Metoprolol Tartrate (50mg),Tablet,Cipla Ltd,Cardiovascular,2024-01,2026-01,Emergency Store,0,strip,2024-02-26,Kerala Medical Supplies Co.
B00098,13953310,Bro Cofdex Plus Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Cipla Ltd,Respiratory,2024-04,2027-04,OT Store,200,bottle,2024-04-26,Kerala Medical Supplies Co.
B00099,T2405-562,Vomistop 10 DT Tablet,Domperidone (10mg),Tablet,Cipla Ltd,Gastro,2024-04,2025-10,OPD Pharmacy,60,strip,2024-06-25,Sree Pharma Agencies
B00100,48833650,Deplatt 150 Tablet,Clopidogrel (150mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,Emergency Store,40,strip,2025-02-07,Malabar Pharma Distributors
B00101,CL25E963,Aspin 300mg Tablet DT,Aspirin (300mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2027-10,OPD Pharmacy,100,strip,2025-01-03,Sanjivani Drug House
B00102,AT245373,Abtelmi 20 Tablet,Telmisartan (20mg),Tablet,Abbott,Cardiovascular,2024-10,2027-10,Ward Store (Paeds),20,strip,2024-12-23,Kerala Medical Supplies Co.
B00103,ALT245835,Olkem 20 Tablet,Olmesartan Medoxomil (20mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-11,2027-11,ICU Store,80,strip,2025-01-26,Kerala Medical Supplies Co.
B00104,NLT253979,Amlyse 30mg Tablet,Ambroxol (30mg),Tablet,Neon Laboratories Ltd,Respiratory,2024-11,2026-11,OPD Pharmacy,200,strip,2025-02-13,Sree Pharma Agencies
B00105,T2509-511,Kelac 10mg Tablet,Ketorolac (10mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-06,2026-06,OPD Pharmacy,10,strip,2024-09-27,Malabar Pharma Distributors
B00106,81612882,Bipacef 500 Tablet,Cefuroxime (500mg),Tablet,Micro Labs Ltd,Antibiotic,2025-05,2028-05,Main Pharmacy,20,strip,2025-07-15,Sree Pharma Agencies
B00107,P0831,ORS (Oral Rehydration Salts IP),Oral Rehydration Salts,Sachet,Quest Laboratories Ltd.,Paediatrics,2024-04,2026-03,Emergency Store,300,sachet,2024-07-30,Kerala Medical Supplies Co.
B00108,CL25K998,Dalcinex 150mg Injection,Clindamycin (150mg),Injection,Cipla Ltd,Antibiotic,2025-04,2027-04,OPD Pharmacy,100,vial/amp,2025-07-15,Sanjivani Drug House
B00109,66000400,Duphalac Fiber Oral Solution,Lactulose (2.5gm/5ml),Oral Solution,Abbott,Gastro,2024-09,2027-09,Ward Store (Paeds),40,bottle,2024-10-15,Sree Pharma Agencies
B00110,T2409-886,Amitor 10mg Tablet,Amitriptyline (10mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-03,2026-09,OT Store,20,strip,2025-06-25,Apollo Wholesale Pvt Ltd
B00111,IPT247533,Flolev 750mg Tablet,Levofloxacin (750mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-10,2027-10,ICU Store,150,strip,2025-01-15,Sree Pharma Agencies
B00112,T2403-650,Ascad 150mg Tablet,Aspirin (150mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-04,2025-10,Ward Store (Paeds),60,strip,2024-04-29,Sanjivani Drug House
B00113,SPT242509,Rosuvas 20 Tablet,Rosuvastatin (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-01,2026-01,Emergency Store,80,strip,2024-04-03,Sanjivani Drug House
B00114,CL24C600,Norflox Eye/Ear Drops,Norfloxacin (0.30%),Ear Drops,Cipla Ltd,Other,2025-03,2026-09,Main Pharmacy,80,bottle,2025-04-15,Sree Pharma Agencies
B00115,T2504-704,Ecosprin 75 Tablet,Aspirin (75mg),Tablet,USV Ltd,Cardiovascular,2024-05,2026-05,Emergency Store,40,strip,2024-08-15,Apollo Wholesale Pvt Ltd
B00116,LL24J212,Lupisit M 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2025-05,2028-05,OPD Pharmacy,50,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B00117,ZC25B592,Cadoxy 100mg Capsule,Doxycycline (100mg),Capsule,Zydus Cadila,Antibiotic,2024-02,2027-02,Emergency Store,20,strip,2024-03-07,Kerala Medical Supplies Co.
B00118,T2401-659,Lubrijoint 500 Tablet,Glucosamine Sulfate Potassium Chloride (500mg),Tablet,Wallace Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-07,2026-01,OT Store,50,strip,2024-08-20,Kerala Medical Supplies Co.
B00119,TPC255781,Mymox 250mg Capsule,Amoxycillin (250mg),Capsule,Torrent Pharmaceuticals Ltd,Antibiotic,2025-03,2026-09,ICU Store,200,strip,2025-06-23,Apollo Wholesale Pvt Ltd
B00120,X2503-401,Esivac Oral Solution,Lactulose (3.335gm/5ml),Oral Solution,Intas Pharmaceuticals Ltd,Gastro,2024-10,2027-10,Main Pharmacy,50,bottle,2024-11-19,"Medline Distributors, Thiruvananthapuram"
B00121,X2505-311,Silvasia 20gm Cream,Silver Sulfadiazine (1% w/w),Cream,Willow Pharmaceuticals Pvt Ltd,Dermatology,2024-08,2027-08,OPD Pharmacy,0,tube,2024-09-14,Sree Pharma Agencies
B00122,78300164,Sucrace Suspension,Sucralfate (1000mg),Suspension,Zydus Cadila,Gastro,2024-12,2027-12,Ward Store (Paeds),40,bottle,2025-02-03,Malabar Pharma Distributors
B00123,23900847,NT Spas 10mg Injection,Dicyclomine (10mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2025-01,2027-01,OT Store,300,vial/amp,2025-04-01,Sree Pharma Agencies
B00124,SP24K010,DEPOPRED 40 MG INJECTION,Methylprednisolone (40mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2025-03,2027-03,OPD Pharmacy,80,vial/amp,2025-05-03,Sree Pharma Agencies
B00125,CLI253007,Xylistin 0.5MIU Injection,Colistimethate Sodium (500000IU),Injection,Cipla Ltd,Antibiotic,2024-12,2026-12,ICU Store,120,vial/amp,2024-12-31,Sanjivani Drug House
B00126,I2503-520,Merenz 1000mg Injection,Meropenem (1000mg),Injection,Lupin Ltd,Antibiotic,2024-12,2026-12,OT Store,40,vial/amp,2025-02-06,Malabar Pharma Distributors
B00127,70097492,Atepres 50mg Tablet,Atenolol (50mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-09,2026-03,Emergency Store,20,strip,2024-10-09,"Medline Distributors, Thiruvananthapuram"
B00128,IHT246813,Zecal XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Indchemie Health Specialities Pvt Ltd,Supplement,2024-11,2027-11,Main Pharmacy,80,strip,2025-02-04,Sanjivani Drug House
B00129,15070029,Lupimox 125mg Tablet,Amoxycillin (125mg),Tablet,Lupin Ltd,Antibiotic,2024-06,2027-06,Main Pharmacy,40,strip,2024-06-27,Malabar Pharma Distributors
B00130,ALT259755,Bisokem 2.5mg Tablet,Bisoprolol (2.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-03,2027-03,Main Pharmacy,300,strip,2024-03-29,"Medline Distributors, Thiruvananthapuram"
B00131,AL25E414,Acecloflam XP 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-01,2026-01,OPD Pharmacy,50,strip,2024-04-20,Sanjivani Drug House
B00132,SPT259146,CEPOCOR 100MG TABLET,Cefpodoxime Proxetil (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-05,2027-05,OPD Pharmacy,20,strip,2025-06-10,"Medline Distributors, Thiruvananthapuram"
B00133,CLC253180,ROKO Capsule,Loperamide (2mg),Capsule,Cipla Ltd,Gastro,2024-10,2026-10,OPD Pharmacy,150,strip,2025-01-19,Apollo Wholesale Pvt Ltd
B00134,T2403-489,Medrol 4mg Tablet,Methylprednisolone (4mg),Tablet,Pfizer Ltd,Steroid,2025-02,2028-02,Main Pharmacy,30,strip,2025-04-08,Kerala Medical Supplies Co.
B00135,SP25F585,Azax 200 Suspension,Azithromycin (200mg/5ml),Suspension,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2027-01,Emergency Store,30,bottle,2024-04-15,Sree Pharma Agencies
B00136,CLT249241,Ciplox 500 Tablet,Ciprofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2024-11,2026-11,ICU Store,60,strip,2025-02-20,Kerala Medical Supplies Co.
B00137,47308143,Lizoran 600mg Infusion,Linezolid (600mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2027-01,ICU Store,60,bottle,2024-04-10,"Medline Distributors, Thiruvananthapuram"
B00138,NHV242589,Nirlife RL Infusion,Ringer's lactate (NA),Infusion,Nirlife Healthcare,IV Fluids,2024-07,2027-07,Ward Store (Paeds),10,bottle,2024-10-21,Apollo Wholesale Pvt Ltd
B00139,SPT240556,Cepoxim XP 500 mg/125 mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2026-03,Main Pharmacy,60,strip,2024-05-26,Sanjivani Drug House
B00140,X2510-944,Derihaler 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Zydus Cadila,Respiratory,2024-02,2027-02,OPD Pharmacy,150,inhaler,2024-05-28,Malabar Pharma Distributors
B00141,42016340,Azax 200 Suspension,Azithromycin (200mg/5ml),Suspension,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-07,2026-07,Main Pharmacy,10,bottle,2024-08-20,Apollo Wholesale Pvt Ltd
B00142,SPT247947,CLOPIDIL 75MG TABLET,Clopidogrel (75mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-02,2027-02,Ward Store (Paeds),40,strip,2024-04-30,Malabar Pharma Distributors
B00143,30691715,Theobid 300mg Tablet,Theophylline (300mg),Tablet,Cipla Ltd,Respiratory,2024-01,2027-01,Main Pharmacy,60,strip,2024-02-20,"Medline Distributors, Thiruvananthapuram"
B00144,72062977,Aldom 20mg Tablet DT,Domperidone (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-04,2027-04,OPD Pharmacy,80,strip,2024-05-27,Malabar Pharma Distributors
B00145,ML25E108,Forinem 500mg Injection,Meropenem (500mg),Injection,Micro Labs Ltd,Antibiotic,2024-04,2027-04,ICU Store,10,vial/amp,2024-05-24,Apollo Wholesale Pvt Ltd
B00146,14877451,Medrol 32mg Tablet,Methylprednisolone (32mg),Tablet,Pfizer Ltd,Steroid,2024-03,2027-03,OT Store,300,strip,2024-05-15,Sree Pharma Agencies
B00147,IP24L317,Ignalis 100 Tablet,Sitagliptin (100mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-03,2027-03,Main Pharmacy,0,strip,2024-05-14,Sanjivani Drug House
B00148,CLS248558,Bro Cofdex Plus Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Cipla Ltd,Respiratory,2024-07,2027-07,OPD Pharmacy,40,bottle,2024-08-30,Sree Pharma Agencies
B00149,LL25F203,Manilup 20% Infusion,Mannitol (20% w/v),Infusion,Lupin Ltd,Anaesthesia/Critical care,2024-08,2026-02,OPD Pharmacy,200,bottle,2024-11-21,"Medline Distributors, Thiruvananthapuram"
B00150,CL25G145,Theobid 300mg Tablet,Theophylline (300mg),Tablet,Cipla Ltd,Respiratory,2024-10,2026-10,OT Store,10,strip,2024-10-26,Kerala Medical Supplies Co.
B00151,CL24B418,Cizetol 200mg Tablet,Carbamazepine (200mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-08,2026-08,OT Store,20,strip,2024-10-05,Apollo Wholesale Pvt Ltd
B00152,TP24M848,Mofee Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Torrent Pharmaceuticals Ltd,Ophthalmology,2025-01,2028-01,Main Pharmacy,20,bottle,2025-03-25,Sree Pharma Agencies
B00153,TI204A002,Sodium Chloride Injection IP 0.9%,Sodium Chloride (0.9% w/v),Infusion,Puniska Injectables Pvt. Ltd.,IV Fluids,2024-09,2027-08,OT Store,60,bottle,2024-12-10,Kerala Medical Supplies Co.
B00154,T2511-939,Loxazin 500mg Tablet,Levofloxacin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-09,2026-03,OPD Pharmacy,100,strip,2024-10-29,Kerala Medical Supplies Co.
B00155,SP25A909,Gemer 0.5 Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-12,2026-06,OPD Pharmacy,300,strip,2025-01-21,"Medline Distributors, Thiruvananthapuram"
B00156,T2503-863,Janumet XR CP Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-11,2026-05,Main Pharmacy,30,strip,2025-02-14,Malabar Pharma Distributors
B00157,11843251,Sensorcaine 0.25% Injection,Bupivacaine (0.25%),Injection,AstraZeneca,Anaesthesia/Critical care,2024-04,2027-04,Main Pharmacy,200,vial/amp,2024-06-08,Kerala Medical Supplies Co.
B00158,T2506-990,Dolex Tablet DT,Tramadol (NA),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-02,2027-02,OPD Pharmacy,30,strip,2024-03-20,"Medline Distributors, Thiruvananthapuram"
B00159,SP24E074,Bectodine 5% Ointment,Povidone Iodine (5% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Dermatology,2024-01,2027-01,ICU Store,30,tube,2024-01-31,"Medline Distributors, Thiruvananthapuram"
B00160,T2502-203,Epsolin 150mg Tablet ER,Phenytoin (150mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2025-02,2027-02,OT Store,120,strip,2025-05-29,Kerala Medical Supplies Co.
B00161,61544630,Azimed 100mg Oral Suspension,Azithromycin (100mg),Suspension,Zydus Cadila,Antibiotic,2024-04,2027-04,Ward Store (Paeds),40,bottle,2024-06-27,Sanjivani Drug House
B00162,TP25G946,E Prin 75mg Tablet,Aspirin (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-06,2026-06,Main Pharmacy,100,strip,2024-07-13,Kerala Medical Supplies Co.
B00163,93177753,Lastair LC 5mg/10mg Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Cipla Ltd,Respiratory,2025-01,2026-07,OPD Pharmacy,120,strip,2025-04-14,Sree Pharma Agencies
B00164,42385743,Fluvia 75mg Capsule,Oseltamivir Phosphate (75mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Antiviral,2024-12,2027-12,Ward Store (Paeds),80,strip,2025-03-21,Apollo Wholesale Pvt Ltd
B00165,PLT251394,Wysolone 5 Tablet DT,Prednisolone (5mg),Tablet,Pfizer Ltd,Steroid,2024-05,2026-05,Ward Store (Paeds),80,strip,2024-07-09,Kerala Medical Supplies Co.
B00166,S2511-586,Alcid S Syrup,Sucralfate (NA),Syrup,Alkem Laboratories Ltd,Gastro,2024-05,2026-05,OPD Pharmacy,0,bottle,2024-06-06,Kerala Medical Supplies Co.
B00167,CL25B517,Cefoprox 100mg Dry Syrup,Cefpodoxime Proxetil (100mg/5ml),Syrup,Cipla Ltd,Antibiotic,2025-04,2028-04,OPD Pharmacy,80,bottle,2025-05-19,Sree Pharma Agencies
B00168,EW24B908,Bicarcid 270mg Tablet,Sodium Bicarbonate (270mg),Tablet,East West Pharma,Anaesthesia/Critical care,2025-02,2028-02,Emergency Store,30,strip,2025-03-24,Apollo Wholesale Pvt Ltd
B00169,SPX244192,Silver Sulfadiazine Cream,Silver Sulfadiazine (NA),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-04,2025-10,OPD Pharmacy,20,tube,2024-04-30,Kerala Medical Supplies Co.
B00170,IL25A047,Perinorm Mps 5 mg/125 mg Tablet,Metoclopramide (5mg) + Simethicone (125mg),Tablet,Ipca Laboratories Ltd,Gastro,2024-09,2026-09,ICU Store,0,strip,2024-11-08,Malabar Pharma Distributors
B00171,IP24L572,Lethyrox 100 Tablet,Thyroxine (100mcg),Tablet,Intas Pharmaceuticals Ltd,Endocrine,2024-02,2026-02,OT Store,60,strip,2024-05-10,Apollo Wholesale Pvt Ltd
B00172,I2403-971,Thrombiflo 20mg Injection,Enoxaparin (20mg),Injection,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-07,2027-07,ICU Store,200,vial/amp,2024-10-10,Apollo Wholesale Pvt Ltd
B00173,48576809,Cavit-XT Tablet,Calcium Carbonate (500mg) + Vitamin D3 (2000IU),Tablet,Cachet Pharmaceuticals Pvt Ltd,Supplement,2024-07,2027-07,OPD Pharmacy,20,strip,2024-08-20,Sree Pharma Agencies
B00174,62546836,Olimelt 10 Tablet MD,Olanzapine (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-02,2025-08,ICU Store,80,strip,2024-03-11,Sanjivani Drug House
B00175,CLT248655,Isomin 20mg Tablet,Isosorbide Mononitrate (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-03,2027-03,OPD Pharmacy,120,strip,2024-06-11,"Medline Distributors, Thiruvananthapuram"
B00176,SP25B604,Sucral Cream,Sucralfate (7% w/w),Cream,Strassenburg Pharmaceuticals.Ltd,Gastro,2025-01,2026-07,Main Pharmacy,200,tube,2025-03-28,Sree Pharma Agencies
B00177,ZCC248011,Adamon 50mg Capsule,Tramadol (50mg),Capsule,Zydus Cadila,Analgesic/Antipyretic,2025-03,2028-03,OPD Pharmacy,20,strip,2025-04-11,Sree Pharma Agencies
B00178,T2506-086,Cefpet XL 200mg Tablet,Cefpodoxime Proxetil (200mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-11,2026-11,ICU Store,100,strip,2025-02-24,Malabar Pharma Distributors
B00179,DRT255667,Omez 40 Tablet,Omeprazole (40mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2025-01,2027-01,OPD Pharmacy,0,strip,2025-03-11,Sree Pharma Agencies
B00180,ZCT243974,Amlodac 10 Tablet,Amlodipine (10mg),Tablet,Zydus Cadila,Cardiovascular,2024-07,2026-07,Ward Store (Paeds),30,strip,2024-09-21,Kerala Medical Supplies Co.
B00181,66468105,Alzolam 0.125mg Tablet,Alprazolam (0.125mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-02,2027-02,ICU Store,60,strip,2024-05-27,"Medline Distributors, Thiruvananthapuram"
B00182,ALT240615,TP Tablet,Telmisartan (NA),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-01,2028-01,Ward Store (Paeds),200,strip,2025-02-10,Sree Pharma Agencies
B00183,TP24K359,Izra 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-01,2026-01,Ward Store (Paeds),150,strip,2024-04-04,Sree Pharma Agencies
B00184,MP25J667,Labetamac Tablet,Labetalol (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2025-02,2027-02,OT Store,20,strip,2025-03-29,Kerala Medical Supplies Co.
B00185,AT240611,R-Ppi 20mg Tablet,Rabeprazole (20mg),Tablet,Abbott,Gastro,2024-02,2027-02,Main Pharmacy,0,strip,2024-05-15,Kerala Medical Supplies Co.
B00186,LL25G780,Lupicip 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Lupin Ltd,Analgesic/Antipyretic,2024-07,2026-07,Emergency Store,200,bottle,2024-08-29,Sanjivani Drug House
B00187,PT240376,Synramine 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psycormedies,Anti-allergic,2024-10,2027-10,OT Store,80,strip,2025-01-21,"Medline Distributors, Thiruvananthapuram"
B00188,SPT252518,Roles 10mg Tablet,Rabeprazole (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-11,2027-11,OT Store,150,strip,2025-01-22,Sanjivani Drug House
B00189,ZPT249676,Folizee 5mg Tablet,Folic Acid (5mg),Tablet,Zeelab Pharmacy Pvt Ltd,Haematology,2025-01,2026-07,OPD Pharmacy,0,strip,2025-02-05,Sanjivani Drug House
B00190,CPT251033,Calcirol XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cadila Pharmaceuticals Ltd,Supplement,2024-04,2025-10,Main Pharmacy,40,strip,2024-07-08,Sree Pharma Agencies
B00191,CLI259790,Merocrit 0.5gm Injection,Meropenem (500mg),Injection,Cipla Ltd,Antibiotic,2024-12,2026-12,Main Pharmacy,120,vial/amp,2025-03-13,Malabar Pharma Distributors
B00192,T2410-871,Encelin 50mg Tablet,Vildagliptin (50mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-07,2027-07,Ward Store (Paeds),200,strip,2024-09-10,Sree Pharma Agencies
B00193,32690870,Pansec 40mg Infusion,Pantoprazole (40mg),Infusion,Cipla Ltd,Gastro,2025-01,2028-01,OPD Pharmacy,40,bottle,2025-03-13,Sanjivani Drug House
B00194,MLT246959,Diapride M 0.5mg/500mg Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Micro Labs Ltd,Diabetes,2024-09,2026-09,OPD Pharmacy,150,strip,2024-10-04,Malabar Pharma Distributors
B00195,80579265,Mymox 250mg Capsule,Amoxycillin (250mg),Capsule,Torrent Pharmaceuticals Ltd,Antibiotic,2024-08,2026-02,OT Store,120,strip,2024-10-07,Apollo Wholesale Pvt Ltd
B00196,BIT241599,Jardiance Met 12.5mg/1000mg Tablet,Empagliflozin (12.5mg) + Metformin (1000mg),Tablet,Boehringer Ingelheim,Diabetes,2024-12,2027-12,OT Store,40,strip,2024-12-26,Kerala Medical Supplies Co.
B00197,CLT252836,Fluka 150 Tablet,Fluconazole (150mg),Tablet,Cipla Ltd,Antifungal,2025-05,2027-05,ICU Store,0,strip,2025-06-03,Kerala Medical Supplies Co.
B00198,TPX240716,Domstal Baby Oral Drops,Domperidone (10mg/ml),Drops,Torrent Pharmaceuticals Ltd,Gastro,2024-02,2027-02,Ward Store (Paeds),20,bottle,2024-05-12,Apollo Wholesale Pvt Ltd
B00199,IP24F589,Prexaron 250mg Injection,Citicoline (250mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2026-08,OPD Pharmacy,10,vial/amp,2024-11-02,Kerala Medical Supplies Co.
B00200,LH24J418,Dailyglim 1000mg Tablet SR,Metformin (1000mg),Tablet,Leeford Healthcare Ltd,Diabetes,2025-04,2026-10,Ward Store (Paeds),200,strip,2025-06-22,Sree Pharma Agencies
B00201,I2401-198,Perinorm Injection,Metoclopramide (5mg/ml),Injection,Ipca Laboratories Ltd,Gastro,2024-11,2027-11,Emergency Store,200,vial/amp,2024-11-29,Sree Pharma Agencies
B00202,55659001,Cosart 25 Tablet,Losartan (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2027-04,ICU Store,20,strip,2024-06-16,"Medline Distributors, Thiruvananthapuram"
B00203,85988361,Ondet 2mg Injection,Ondansetron (2mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2024-08,2027-08,Ward Store (Paeds),30,vial/amp,2024-09-16,Apollo Wholesale Pvt Ltd
B00204,SPT253185,Amx 125mg Tablet,Amoxycillin (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2027-10,ICU Store,10,strip,2024-12-25,Sanjivani Drug House
B00205,IPT256414,Depranex 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2025-09,Emergency Store,50,strip,2024-05-21,Malabar Pharma Distributors
B00206,82668051,Docmycin 100mg Tablet,Doxycycline (100mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-09,2027-09,Main Pharmacy,10,strip,2024-11-29,Kerala Medical Supplies Co.
B00207,T2505-474,Furakem 100mg Tablet MR,Nitrofurantoin (100mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-01,2027-01,Ward Store (Paeds),300,strip,2024-04-11,Kerala Medical Supplies Co.
B00208,BPT254528,Bioflaxacin Tablet,Chlorpheniramine Maleate (NA),Tablet,Biochem Pharmaceutical Industries,Anti-allergic,2024-11,2027-11,Main Pharmacy,150,strip,2024-12-14,Sree Pharma Agencies
B00209,IPT245380,Carca 12.5 Tablet,Carvedilol (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-08,2026-08,OPD Pharmacy,20,strip,2024-10-20,Malabar Pharma Distributors
B00210,67890079,Solonex DT Tablet,Isoniazid (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2024-08,2026-08,OPD Pharmacy,50,strip,2024-10-12,Kerala Medical Supplies Co.
B00211,C2407-831,Tramatas 50mg Capsule,Tramadol (50mg),Capsule,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-05,2028-05,OPD Pharmacy,120,strip,2025-07-12,Apollo Wholesale Pvt Ltd
B00212,T2509-596,Normaglim 2mg Tablet,Glimepiride (2mg),Tablet,Zydus Cadila,Diabetes,2024-02,2027-02,OT Store,20,strip,2024-03-08,Sanjivani Drug House
B00213,FL24M892,Zifi 200 Tablet,Cefixime (200mg),Tablet,FDC Ltd,Antibiotic,2024-03,2027-03,ICU Store,80,strip,2024-05-25,Sree Pharma Agencies
B00214,AT252877,Forxiga 5mg Tablet,Dapagliflozin (5mg),Tablet,AstraZeneca,Diabetes,2024-10,2027-10,ICU Store,40,strip,2024-11-12,Kerala Medical Supplies Co.
B00215,Z24-185,Tranexamic Acid Injection IP 500 mg/5 ml,Tranexamic Acid (100mg/ml),Injection,Zee Laboratories Ltd.,Haematology,2024-02,2026-01,OT Store,300,vial/amp,2024-05-20,Sanjivani Drug House
B00216,SPC244977,Clopilet A 75 Capsule,Aspirin (75mg) + Clopidogrel (75mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-10,2027-10,ICU Store,80,strip,2024-10-30,Kerala Medical Supplies Co.
B00217,I2504-081,Anawin 0.25% Injection,Bupivacaine (0.25%),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-04,2027-04,Main Pharmacy,200,vial/amp,2024-07-27,"Medline Distributors, Thiruvananthapuram"
B00218,13094200,Corpril 1.25mg Tablet,Ramipril (1.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-03,2027-03,ICU Store,30,strip,2025-05-17,Kerala Medical Supplies Co.
B00219,IPI242493,Ondet 2mg Injection,Ondansetron (2mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2024-10,2026-04,Emergency Store,20,vial/amp,2025-01-19,Sree Pharma Agencies
B00220,NIT252931,Voveran 50 GE Tablet,Diclofenac (50mg),Tablet,Novartis India Ltd,Analgesic/Antipyretic,2024-04,2027-04,OPD Pharmacy,30,strip,2024-06-10,Kerala Medical Supplies Co.
B00221,LLT248405,LNZ 600 Tablet,Linezolid (600mg),Tablet,Lupin Ltd,Antibiotic,2024-10,2026-10,Emergency Store,10,strip,2024-12-21,"Medline Distributors, Thiruvananthapuram"
B00222,HT24686,Pantrum-40 Tablet,Pantoprazole (40mg),Tablet,Habitare Pharma Pvt. Ltd.,Gastro,2024-08,2026-07,Main Pharmacy,300,strip,2024-08-26,Apollo Wholesale Pvt Ltd
B00223,80542438,Betavert 16 Tablet,Betahistine (16mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-02,2026-08,Main Pharmacy,0,strip,2025-04-21,Malabar Pharma Distributors
B00224,ALS255653,Ceriz 5mg Syrup,Cetirizine (5mg/ml),Syrup,Alkem Laboratories Ltd,Respiratory,2024-06,2026-06,OPD Pharmacy,200,bottle,2024-07-16,Apollo Wholesale Pvt Ltd
B00225,SI25J732,Clexane 40mg Injection (0.4ml Each),Enoxaparin (40mg),Injection,Sanofi India Ltd,Anticoagulant,2024-11,2026-11,OT Store,60,vial/amp,2024-12-30,Apollo Wholesale Pvt Ltd
B00226,72253115,Arvast F 10 Tablet,Fenofibrate (67mg) + Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-10,2026-10,Main Pharmacy,150,strip,2024-11-08,Kerala Medical Supplies Co.
B00227,I2411-923,Lofh 25000IU Injection,Heparin (25000IU),Injection,Abbott,Anticoagulant,2024-02,2025-08,OT Store,300,vial/amp,2024-04-20,Kerala Medical Supplies Co.
B00228,MLT246156,Bactoclav - DT Tablet,Amoxycillin (200mg) + Clavulanic Acid (28.5mg),Tablet,Micro Labs Ltd,Antibiotic,2024-06,2026-06,OPD Pharmacy,150,strip,2024-08-12,Sanjivani Drug House
B00229,CL24M017,Diacip 500mg Tablet,Metformin (500mg),Tablet,Cipla Ltd,Diabetes,2024-09,2026-09,Emergency Store,50,strip,2024-12-15,Kerala Medical Supplies Co.
B00230,37500238,Ondamac 2mg Injection,Ondansetron (2mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-03,2026-09,Emergency Store,150,vial/amp,2025-03-31,"Medline Distributors, Thiruvananthapuram"
B00231,SP25F091,Merixim 1000mg Injection,Meropenem (1000mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-01,2027-01,Emergency Store,100,vial/amp,2025-03-12,"Medline Distributors, Thiruvananthapuram"
B00232,TPT255018,Azulix 0.5 MF Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-03,2028-03,Emergency Store,10,strip,2025-06-03,Apollo Wholesale Pvt Ltd
B00233,UPI256261,Make FE 100mg Injection,Ferrous Ascorbate (100mg),Injection,Uniword Pharma,Haematology,2024-04,2027-04,OT Store,300,vial/amp,2024-07-15,Kerala Medical Supplies Co.
B00234,SI24M759,Valparin 200 Oral Solution Delicious Pineapple,Sodium Valproate (200mg/5ml),Oral Solution,Sanofi India Ltd,Neurology/Psychiatry,2025-03,2027-03,Main Pharmacy,50,bottle,2025-05-26,Sree Pharma Agencies
B00235,14767638,Aspent 60mg Tablet,Aspirin (60mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-02,2027-02,Main Pharmacy,50,strip,2025-03-31,Sree Pharma Agencies
B00236,ALX245142,Vigamox Ophthalmic Solution,Moxifloxacin (0.5% w/v),Solution,Alcon Laboratories,Ophthalmology,2024-12,2026-12,Emergency Store,100,bottle,2025-02-02,Kerala Medical Supplies Co.
B00237,SP24A045,Oleanz 5 Tablet,Olanzapine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-12,2026-12,ICU Store,50,strip,2025-03-20,Apollo Wholesale Pvt Ltd
B00238,40283277,Cepoxim XP 500 mg/125 mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-06,2025-12,Main Pharmacy,60,strip,2024-09-22,Sree Pharma Agencies
B00239,AP24J942,Folinal 5mg Tablet,Folic Acid (5mg),Tablet,Alembic Pharmaceuticals Ltd,Haematology,2024-02,2027-02,OT Store,300,strip,2024-04-13,Kerala Medical Supplies Co.
B00240,58841557,Razo A 200mg/20mg Capsule SR,Aceclofenac (200mg) + Rabeprazole (20mg),Capsule,Precise Lifescience,Gastro,2024-12,2027-12,OT Store,40,strip,2025-02-11,Apollo Wholesale Pvt Ltd
B00241,ALI247470,Acdof 40mg Injection,Pantoprazole (40mg),Injection,Alkem Laboratories Ltd,Gastro,2024-10,2027-10,Ward Store (Paeds),10,vial/amp,2025-01-19,Kerala Medical Supplies Co.
B00242,BIT257453,Jardiance Met 12.5mg/1000mg Tablet,Empagliflozin (12.5mg) + Metformin (1000mg),Tablet,Boehringer Ingelheim,Diabetes,2025-02,2027-02,Emergency Store,100,strip,2025-05-08,Apollo Wholesale Pvt Ltd
B00243,ILT245986,Folitrax 10 Tablet,Methotrexate (10mg),Tablet,Ipca Laboratories Ltd,Oncology,2024-10,2026-10,OT Store,200,strip,2024-11-05,Sree Pharma Agencies
B00244,51227645,Hycort 100mg Injection,Hydrocortisone (100mg),Injection,Alkem Laboratories Ltd,Steroid,2025-05,2028-05,OT Store,300,vial/amp,2025-06-12,"Medline Distributors, Thiruvananthapuram"
B00245,AL25K083,Hycort 100mg Injection,Hydrocortisone (100mg),Injection,Alkem Laboratories Ltd,Steroid,2025-04,2026-10,Ward Store (Paeds),20,vial/amp,2025-06-06,Kerala Medical Supplies Co.
B00246,A25C655,Tossex 12 Oral Suspension Orange,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Abbott,Respiratory,2025-03,2028-03,Ward Store (Paeds),10,bottle,2025-05-01,"Medline Distributors, Thiruvananthapuram"
B00247,ALT254476,Almet 10mg Tablet,Metoclopramide (10mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-03,2027-03,OPD Pharmacy,20,strip,2024-04-13,"Medline Distributors, Thiruvananthapuram"
B00248,I2403-999,Dexona Injection,Dexamethasone (4mg/ml),Injection,Zydus Cadila,Steroid,2024-08,2027-08,ICU Store,60,vial/amp,2024-09-07,Kerala Medical Supplies Co.
B00249,ALI240777,Mecobex 500mcg Injection,Methylcobalamin (500mcg),Injection,Alkem Laboratories Ltd,Supplement,2024-08,2026-02,OT Store,100,vial/amp,2024-09-17,Kerala Medical Supplies Co.
B00250,TPT249768,Hqtor 300mg Tablet,Hydroxychloroquine (300mg),Tablet,Torrent Pharmaceuticals Ltd,Antimalarial,2025-05,2026-11,Main Pharmacy,20,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B00251,73174275,LNZ 600 Tablet,Linezolid (600mg),Tablet,Lupin Ltd,Antibiotic,2024-05,2026-05,Main Pharmacy,120,strip,2024-07-02,Sree Pharma Agencies
B00252,AT245380,Thyronorm 125mcg Tablet,Thyroxine (125mcg),Tablet,Abbott,Endocrine,2024-03,2025-09,OT Store,300,strip,2024-04-15,"Medline Distributors, Thiruvananthapuram"
B00253,UL25B801,Glycomet 500 SR Tablet,Metformin (500mg),Tablet,USV Ltd,Diabetes,2024-01,2026-01,Ward Store (Paeds),50,strip,2024-03-01,Sanjivani Drug House
B00254,ZCT253344,CoviQ Tablet,Hydroxychloroquine (200mg),Tablet,Zydus Cadila,Antimalarial,2024-10,2026-10,OT Store,150,strip,2024-12-02,Apollo Wholesale Pvt Ltd
B00255,ZCT244710,Happi 20 Tablet,Rabeprazole (20mg),Tablet,Zydus Cadila,Gastro,2024-07,2026-07,ICU Store,100,strip,2024-08-29,Sanjivani Drug House
B00256,C2409-285,Urimax 0.2 Capsule MR,Tamsulosin (0.2mg),Capsule,Cipla Ltd,Urology,2025-02,2028-02,Emergency Store,150,strip,2025-05-16,Sree Pharma Agencies
B00257,V2409-913,D5 Infusion,Dextrose (5gm),Infusion,Infutec Healthcare Limited,IV Fluids,2024-05,2027-05,Main Pharmacy,300,bottle,2024-08-25,Malabar Pharma Distributors
B00258,T2404-621,Alevo 250 Tablet,Levofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-03,2027-03,Main Pharmacy,100,strip,2024-03-29,Sanjivani Drug House
B00259,T2507-724,Azepress 250mg Tablet,Azithromycin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2024-01,2026-01,Emergency Store,10,strip,2024-04-10,Sree Pharma Agencies
B00260,IP24F247,Histacet 10mg Capsule,Cetirizine (10mg),Capsule,Intas Pharmaceuticals Ltd,Respiratory,2024-06,2027-06,Ward Store (Paeds),20,strip,2024-06-27,Apollo Wholesale Pvt Ltd
B00261,LLT240583,L-Cin 250 Tablet,Levofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,20,strip,2024-06-06,"Medline Distributors, Thiruvananthapuram"
B00262,MLT241779,Dolo 650 Tablet,Paracetamol (650mg),Tablet,Micro Labs Ltd,Analgesic/Antipyretic,2024-12,2026-12,Emergency Store,200,strip,2025-03-22,"Medline Distributors, Thiruvananthapuram"
B00263,49320837,Biclar 250mg Tablet,Clarithromycin (250mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-08,2027-08,Main Pharmacy,200,strip,2024-10-15,Kerala Medical Supplies Co.
B00264,DR25H631,Osetron 4mg Injection,Ondansetron (4mg),Injection,Dr Reddy's Laboratories Ltd,Gastro,2025-04,2028-04,OPD Pharmacy,50,vial/amp,2025-05-22,Malabar Pharma Distributors
B00265,PFV242515,Compound Sodium Lacate Infusion,Ringer's lactate (NA),Infusion,Punjab Formulations Ltd,IV Fluids,2024-12,2026-06,OT Store,100,bottle,2025-03-16,"Medline Distributors, Thiruvananthapuram"
B00266,T2510-849,Bioflaxacin Tablet,Chlorpheniramine Maleate (NA),Tablet,Biochem Pharmaceutical Industries,Anti-allergic,2024-10,2026-10,Emergency Store,300,strip,2025-01-14,"Medline Distributors, Thiruvananthapuram"
B00267,90672745,Meroplan 500mg Injection,Meropenem (500mg),Injection,Abbott,Antibiotic,2024-12,2027-12,OPD Pharmacy,150,vial/amp,2025-02-16,"Medline Distributors, Thiruvananthapuram"
B00268,I404138,Thrombophob Ointment,Benzyl Nicotinate (2mg) + Heparin (50IU),Ointment,Zydus Cadila,Anticoagulant,2024-08,2027-07,Ward Store (Paeds),150,tube,2024-10-02,Malabar Pharma Distributors
B00269,SPI250372,Oframax 125mg Injection,Ceftriaxone (125mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2026-03,Main Pharmacy,50,vial/amp,2024-06-15,Malabar Pharma Distributors
B00270,APS252117,Ambrodil Syrup,Ambroxol (30mg/5ml),Syrup,Aristo Pharmaceuticals Pvt Ltd,Respiratory,2024-02,2027-02,Main Pharmacy,200,bottle,2024-05-09,Malabar Pharma Distributors
B00271,AT257165,Brufen 200 Tablet,Ibuprofen (200mg),Tablet,Abbott,Analgesic/Antipyretic,2024-07,2026-01,Main Pharmacy,30,strip,2024-07-31,"Medline Distributors, Thiruvananthapuram"
B00272,T2508-234,Jardiance 25mg Tablet,Empagliflozin (25mg),Tablet,Boehringer Ingelheim,Other,2025-04,2027-04,OT Store,100,strip,2025-06-10,Apollo Wholesale Pvt Ltd
B00273,A24B751,Nuavomin 2mg Injection,Ondansetron (2mg),Injection,Abbott,Gastro,2025-04,2028-04,Ward Store (Paeds),40,vial/amp,2025-07-15,Sree Pharma Agencies
B00274,SIF2676A,Rosuvas F 10 Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2027-05,OT Store,50,strip,2025-02-05,"Medline Distributors, Thiruvananthapuram"
B00275,IP25A901,Ondet 2mg Injection,Ondansetron (2mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2025-04,2027-04,OT Store,300,vial/amp,2025-06-06,"Medline Distributors, Thiruvananthapuram"
B00276,TP24A339,Apixator 2.5 Tablet,Apixaban (2.5mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2025-04,2028-04,ICU Store,0,strip,2025-07-15,Sree Pharma Agencies
B00277,IFMI415,Frusemide Injection IP 2 ml,Furosemide (10mg/ml),Injection,Regain Laboratories,Cardiovascular,2024-09,2026-08,OPD Pharmacy,300,vial/amp,2024-11-27,Malabar Pharma Distributors
B00278,T2411-239,Medrol 16mg Tablet,Methylprednisolone (16mg),Tablet,Pfizer Ltd,Steroid,2024-04,2025-10,OT Store,10,strip,2024-05-02,Kerala Medical Supplies Co.
B00279,10998405,Emty Oral Solution,Lactulose (10gm),Oral Solution,Alkem Laboratories Ltd,Gastro,2024-03,2026-03,OT Store,40,bottle,2024-04-16,"Medline Distributors, Thiruvananthapuram"
B00280,IPI246040,Instavil 22.75mg Injection,Pheniramine (22.75mg),Injection,Intas Pharmaceuticals Ltd,Anti-allergic,2025-03,2028-03,ICU Store,120,vial/amp,2025-05-14,Sanjivani Drug House
B00281,SP25E916,Corpril 1.25mg Tablet,Ramipril (1.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2026-04,OPD Pharmacy,60,strip,2024-05-07,Apollo Wholesale Pvt Ltd
B00282,80528349,Wysolone 20 Tablet DT,Prednisolone (20mg),Tablet,Pfizer Ltd,Steroid,2024-09,2026-09,OPD Pharmacy,50,strip,2024-11-13,Apollo Wholesale Pvt Ltd
B00283,ALC258246,Gabata 400mg Capsule,Gabapentin (400mg),Capsule,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-11,2026-11,OT Store,120,strip,2024-12-21,Sanjivani Drug House
B00284,CLX245314,Dexacip 0.1% Eye Drop,Dexamethasone (0.1% w/v),Eye Drops,Cipla Ltd,Steroid,2024-02,2026-02,Main Pharmacy,150,bottle,2024-04-22,Kerala Medical Supplies Co.
B00285,A24J901,Udiliv 300 Tablet,Ursodeoxycholic Acid (300mg),Tablet,Abbott,Gastro,2024-07,2027-07,ICU Store,0,strip,2024-09-19,Apollo Wholesale Pvt Ltd
B00286,SPT240548,Prazopress 1 Tablet,Prazosin (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2027-03,ICU Store,200,strip,2024-04-13,"Medline Distributors, Thiruvananthapuram"
B00287,MP25J308,Amlogift 5mg Tablet,Amlodipine (5mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-11,2027-11,ICU Store,20,strip,2025-02-16,Sanjivani Drug House
B00288,SPI248459,Emsetron 2mg Injection,Ondansetron (2mg),Injection,Sun Pharmaceutical Industries Ltd,Gastro,2024-12,2027-12,Emergency Store,10,vial/amp,2024-12-27,Malabar Pharma Distributors
B00289,T2405-493,Tryptomer 50mg Tablet,Amitriptyline (50mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2024-11,2026-05,OPD Pharmacy,40,strip,2025-02-15,Kerala Medical Supplies Co.
B00290,28818473,Amitor 10mg Tablet,Amitriptyline (10mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-01,2026-07,Ward Store (Paeds),20,strip,2025-03-07,Malabar Pharma Distributors
B00291,I2409-507,Dianora 1mg Injection,Adrenaline (1mg),Injection,Cachet Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-11,2027-11,Main Pharmacy,120,vial/amp,2025-02-05,Sree Pharma Agencies
B00292,T2509-194,Nitrofurantoin Tablets IP 100 mg,Nitrofurantoin (100mg),Tablet,Unicure India Ltd.,Antibiotic,2024-11,2026-11,Emergency Store,150,strip,2025-01-05,Sanjivani Drug House
B00293,LHT240396,Redotrex 500 Tablet,Tranexamic Acid (500mg),Tablet,Leeford Healthcare Ltd,Haematology,2024-07,2027-07,ICU Store,20,strip,2024-10-03,Sanjivani Drug House
B00294,ALPT-051,Telmisartan Tablets IP 40 mg,Telmisartan (40mg),Tablet,Alifecare Pharmacy Pvt. Ltd.,Cardiovascular,2024-07,2026-06,Main Pharmacy,60,strip,2024-07-30,Kerala Medical Supplies Co.
B00295,ZH24K671,Zu-C Injection,Vitamin C (100mg),Injection,Zuventus Healthcare Ltd,Supplement,2025-01,2026-07,ICU Store,10,vial/amp,2025-03-23,Sanjivani Drug House
B00296,LLT253563,Gluconorm SR 1gm Tablet,Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2024-09,2027-09,OT Store,120,strip,2024-09-28,Sanjivani Drug House
B00297,99783064,Folizee 5mg Tablet,Folic Acid (5mg),Tablet,Zeelab Pharmacy Pvt Ltd,Haematology,2025-04,2028-04,OPD Pharmacy,30,strip,2025-06-05,Malabar Pharma Distributors
B00298,SPC254855,Maxgalin 150 Capsule,Pregabalin (150mg),Capsule,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-12,2026-12,Ward Store (Paeds),30,strip,2025-02-26,"Medline Distributors, Thiruvananthapuram"
B00299,ALT252552,Losaral 50mg Tablet,Losartan (50mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-06,2025-12,Main Pharmacy,150,strip,2024-09-23,Kerala Medical Supplies Co.
B00300,28112562,Aldom 20mg Tablet DT,Domperidone (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-09,2027-09,OT Store,0,strip,2024-10-17,Sree Pharma Agencies
B00301,T2512-505,Medistat 0.5mg Tablet,Midazolam (0.5mg),Tablet,Alteus Biogenics Pvt Ltd,Neurology/Psychiatry,2024-07,2026-07,OPD Pharmacy,120,strip,2024-08-17,Malabar Pharma Distributors
B00302,TPT244094,Altipod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2025-03,2027-03,Ward Store (Paeds),100,strip,2025-04-02,Kerala Medical Supplies Co.
B00303,T2412-436,Abixim 100mg Tablet,Cefixime (100mg),Tablet,Abbott,Antibiotic,2024-07,2026-01,Ward Store (Paeds),100,strip,2024-10-23,Kerala Medical Supplies Co.
B00304,ALT253532,Alsita 100mg Tablet,Sitagliptin (100mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-03,2026-03,ICU Store,0,strip,2024-05-04,Malabar Pharma Distributors
B00305,IP25J860,Prexaron 250mg Injection,Citicoline (250mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2027-03,Main Pharmacy,100,vial/amp,2024-06-22,Sanjivani Drug House
B00306,AT246900,Lflox 500mg Tablet,Levofloxacin (500mg),Tablet,Abbott,Antibiotic,2024-06,2025-12,ICU Store,40,strip,2024-09-26,Kerala Medical Supplies Co.
B00307,I2511-312,Neomine 0.5mg Injection,Neostigmine (0.5mg),Injection,Zydus Cadila,Anaesthesia/Critical care,2024-02,2027-02,ICU Store,40,vial/amp,2024-04-12,Apollo Wholesale Pvt Ltd
B00308,T2508-162,Inditel 20 Tablet,Telmisartan (20mg),Tablet,Zydus Cadila,Cardiovascular,2024-05,2027-05,Ward Store (Paeds),100,strip,2024-08-10,Sanjivani Drug House
B00309,SP25G952,Rosuvas 10 Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2025-12,Ward Store (Paeds),10,strip,2024-07-06,Sree Pharma Agencies
B00310,T2509-011,Emeset 2mg Tablet MD,Ondansetron (2mg),Tablet,Cipla Ltd,Gastro,2025-05,2028-05,Main Pharmacy,30,strip,2025-07-15,Sree Pharma Agencies
B00311,66519645,Zynwin Tablet,Zinc Sulfate (137.232mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Supplement,2024-05,2027-05,Main Pharmacy,300,strip,2024-08-07,"Medline Distributors, Thiruvananthapuram"
B00312,SP24L428,Oncoplatin AQ 10mg Injection,Cisplatin (10mg),Injection,Sun Pharmaceutical Industries Ltd,Oncology,2024-07,2027-07,OPD Pharmacy,0,vial/amp,2024-09-15,Sanjivani Drug House
B00313,SPT248976,Etoshine 120 Tablet,Etoricoxib (120mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-08,2026-02,OPD Pharmacy,40,strip,2024-09-16,Sree Pharma Agencies
B00314,IPI258898,Chophos 1000mg Injection,Cyclophosphamide (1000mg),Injection,Intas Pharmaceuticals Ltd,Oncology,2024-11,2026-11,OT Store,150,vial/amp,2025-01-25,"Medline Distributors, Thiruvananthapuram"
B00315,52818511,CZ 3 Syrup,Cetirizine (5mg/5ml),Syrup,Lupin Ltd,Respiratory,2025-05,2028-05,Emergency Store,200,bottle,2025-07-01,Sanjivani Drug House
B00316,58393887,Dex 25% Infusion,Dextrose (25% w/v),Infusion,Shree KrishnaKeshav Laboratories Ltd,IV Fluids,2025-02,2026-08,ICU Store,100,bottle,2025-05-15,Malabar Pharma Distributors
B00317,TP24L794,Histanil Syrup,Chlorpheniramine Maleate (NA),Syrup,Troikaa Pharmaceuticals Ltd,Anti-allergic,2025-02,2028-02,OT Store,20,bottle,2025-03-26,"Medline Distributors, Thiruvananthapuram"
B00318,IPX259058,Clinka Gel,Clindamycin (1% w/w),Gel,Intas Pharmaceuticals Ltd,Antibiotic,2024-03,2026-03,Main Pharmacy,300,tube,2024-04-18,Apollo Wholesale Pvt Ltd
B00319,86120854,Bupizuva 2.5mg Injection,Bupivacaine (2.5mg/ml),Injection,Abbott,Anaesthesia/Critical care,2024-05,2026-05,OT Store,200,vial/amp,2024-05-31,Apollo Wholesale Pvt Ltd
B00320,92312475,Naresol 0.65% Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Alembic Pharmaceuticals Ltd,IV Fluids,2024-08,2027-08,ICU Store,150,bottle,2024-09-29,Malabar Pharma Distributors
B00321,ZCI258321,Xylocaine 2% Injection,Lidocaine (2%),Injection,Zydus Cadila,Other,2024-09,2027-09,Ward Store (Paeds),300,vial/amp,2024-11-20,Sree Pharma Agencies
B00322,59668381,Rostar 10 Tablet,Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-08,2027-08,Ward Store (Paeds),50,strip,2024-09-30,Sanjivani Drug House
B00323,TPT253261,Eldoflam 120mg Tablet,Etoricoxib (120mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2026-09,OPD Pharmacy,0,strip,2025-05-21,Malabar Pharma Distributors
B00324,CL24F327,Ciplox 500 Tablet,Ciprofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2024-06,2025-12,Ward Store (Paeds),200,strip,2024-09-17,Apollo Wholesale Pvt Ltd
B00325,DR25D912,Osetron 4mg Injection,Ondansetron (4mg),Injection,Dr Reddy's Laboratories Ltd,Gastro,2024-04,2025-10,OT Store,80,vial/amp,2024-07-21,Sanjivani Drug House
B00326,I2506-590,Unimika 100mg Injection,Amikacin (100mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-09,2027-09,ICU Store,120,vial/amp,2024-12-10,Malabar Pharma Distributors
B00327,T2411-949,Stromix 75mg Tablet,Clopidogrel (75mg),Tablet,Abbott,Cardiovascular,2024-09,2026-09,Ward Store (Paeds),20,strip,2024-10-25,Sree Pharma Agencies
B00328,SP24J196,Valtoval 1g Tablet,Valacyclovir (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Antiviral,2025-05,2028-05,OPD Pharmacy,100,strip,2025-07-15,Sree Pharma Agencies
B00329,78301185,Intazin L 5mg Tablet,Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2025-01,2028-01,ICU Store,50,strip,2025-01-26,Sanjivani Drug House
B00330,50810571,CV Sprin 75mg Tablet,Aspirin (75mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-07,OPD Pharmacy,0,strip,2024-10-26,Malabar Pharma Distributors
B00331,BI25B316,Jardiance 10mg Tablet,Empagliflozin (10mg),Tablet,Boehringer Ingelheim,Other,2025-01,2027-01,OPD Pharmacy,120,strip,2025-02-15,Sanjivani Drug House
B00332,T2506-833,Lflox 500mg Tablet,Levofloxacin (500mg),Tablet,Abbott,Antibiotic,2024-10,2027-10,OPD Pharmacy,30,strip,2024-12-05,"Medline Distributors, Thiruvananthapuram"
B00333,EHV253940,Fabitol 20% Infusion,Mannitol (20% w/v),Infusion,Elkos Healthcare Pvt Ltd,Anaesthesia/Critical care,2024-06,2027-06,Emergency Store,120,bottle,2024-09-21,Sanjivani Drug House
B00334,IP25E604,Clavix 150 Tablet,Clopidogrel (150mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,OPD Pharmacy,50,strip,2025-02-23,"Medline Distributors, Thiruvananthapuram"
B00335,81729149,Cadoxy 100mg Capsule,Doxycycline (100mg),Capsule,Zydus Cadila,Antibiotic,2025-02,2027-02,Emergency Store,30,strip,2025-05-10,Sanjivani Drug House
B00336,65127958,Sartel 20 Tablet,Telmisartan (20mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-02,2027-02,OT Store,30,strip,2024-03-02,Apollo Wholesale Pvt Ltd
B00337,CC24J884,Regimen Hand Rub (Aloevera 70% Alcohol),Alcohol hand rub,Solution,Chemstellar Chemicals Pvt. Ltd.,Infection control,2024-09,2026-09,OT Store,150,bottle,2024-11-03,Sanjivani Drug House
B00338,X2506-410,Eco Tears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2025-03,2027-03,OPD Pharmacy,100,bottle,2025-06-05,Apollo Wholesale Pvt Ltd
B00339,I2510-880,Chophos 1000mg Injection,Cyclophosphamide (1000mg),Injection,Intas Pharmaceuticals Ltd,Oncology,2024-11,2026-11,OT Store,80,vial/amp,2024-12-02,Malabar Pharma Distributors
B00340,IPT243974,Embeta 25 Tablet,Metoprolol Tartrate (25mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-02,2027-02,Ward Store (Paeds),50,strip,2025-03-19,Kerala Medical Supplies Co.
B00341,RL24H325,Aldactone F Tablet,Furosemide (20mg) + Spironolactone (50mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2025-01,2028-01,Main Pharmacy,40,strip,2025-03-26,"Medline Distributors, Thiruvananthapuram"
B00342,T2412-330,Amtas 10 Tablet,Amlodipine (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-02,2027-02,OT Store,80,strip,2025-03-04,Sree Pharma Agencies
B00343,CLC240817,Nifelat 10mg Capsule,Nifedipine (10mg),Capsule,Cipla Ltd,Cardiovascular,2025-01,2027-01,Emergency Store,50,strip,2025-02-27,Sanjivani Drug House
B00344,LLT242897,E Cef 100mg Tablet DT,Cefixime (100mg),Tablet,Lupin Ltd,Antibiotic,2024-08,2027-08,OT Store,300,strip,2024-10-05,Sree Pharma Agencies
B00345,T2405-277,Betavert 16 Tablet,Betahistine (16mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-01,2026-07,Ward Store (Paeds),200,strip,2025-04-12,Sree Pharma Agencies
B00346,LL25A545,Meflup 250mg Tablet,Mefenamic Acid (250mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-02,2026-08,ICU Store,10,strip,2025-03-17,Kerala Medical Supplies Co.
B00347,DRT250366,Stamlo 10 Tablet,Amlodipine (10mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2025-03,2026-09,OT Store,20,strip,2025-04-10,Apollo Wholesale Pvt Ltd
B00348,T2507-698,Abamlo 5 Tablet,Amlodipine (5mg),Tablet,Abbott,Cardiovascular,2025-04,2028-04,OT Store,80,strip,2025-05-11,Malabar Pharma Distributors
B00349,NI25J303,Galvus Met 50mg/1000mg Tablet,Metformin (1000mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2025-01,2026-07,Ward Store (Paeds),100,strip,2025-01-28,Malabar Pharma Distributors
B00350,MLT241611,Amlong-TL 40 Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-05,2027-05,Ward Store (Paeds),0,strip,2025-06-27,Malabar Pharma Distributors
B00351,T2404-541,Folvite 5mg Tablet,Folic Acid (5mg),Tablet,Pfizer Ltd,Haematology,2024-02,2026-02,OT Store,50,strip,2024-04-30,Sanjivani Drug House
B00352,IRI255791,Hepatag 25000IU Injection,Heparin (25000IU),Injection,Ikon Remedies Pvt Ltd,Anticoagulant,2024-08,2027-08,Ward Store (Paeds),30,vial/amp,2024-10-05,"Medline Distributors, Thiruvananthapuram"
B00353,CL24H078,Amicip 100mg Injection,Amikacin (100mg),Injection,Cipla Ltd,Antibiotic,2025-01,2027-01,Ward Store (Paeds),40,vial/amp,2025-01-26,Sree Pharma Agencies
B00354,CL25D653,Itracan 100mg Capsule,Itraconazole (100mg),Capsule,Cipla Ltd,Antifungal,2025-01,2028-01,OT Store,60,strip,2025-04-09,Sree Pharma Agencies
B00355,CL24H860,Imutrex 10 Tablet,Methotrexate (10mg),Tablet,Cipla Ltd,Oncology,2025-01,2028-01,Ward Store (Paeds),10,strip,2025-03-10,Sanjivani Drug House
B00356,SP24J050,Emsetron 2mg Injection,Ondansetron (2mg),Injection,Sun Pharmaceutical Industries Ltd,Gastro,2025-02,2027-02,OPD Pharmacy,30,vial/amp,2025-03-27,Kerala Medical Supplies Co.
B00357,CLS244781,Montair LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Cipla Ltd,Respiratory,2024-01,2026-01,ICU Store,40,bottle,2024-02-25,Kerala Medical Supplies Co.
B00358,28435232,Zorem 1.25 Capsule,Ramipril (1.25mg),Capsule,Intas Pharmaceuticals Ltd,Cardiovascular,2025-02,2026-08,OT Store,200,strip,2025-05-09,Sree Pharma Agencies
B00359,ZC24F366,Xylocaine 1% Injection,Lidocaine (1%),Injection,Zydus Cadila,Other,2025-01,2028-01,Main Pharmacy,60,vial/amp,2025-03-22,Sree Pharma Agencies
B00360,ALX244585,Almox 100mg Oral Drops,Amoxycillin (100mg),Drops,Alkem Laboratories Ltd,Antibiotic,2024-07,2026-01,ICU Store,100,bottle,2024-10-14,Malabar Pharma Distributors
B00361,ZLI258259,Frusizex 10mg Injection,Furosemide (10mg/ml),Injection,Zee Laboratories,Cardiovascular,2024-04,2026-04,Ward Store (Paeds),20,vial/amp,2024-06-10,"Medline Distributors, Thiruvananthapuram"
B00362,MPT253857,Labetamac Tablet,Labetalol (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-01,2026-07,ICU Store,10,strip,2024-04-26,"Medline Distributors, Thiruvananthapuram"
B00363,CLT242350,Norflox 400 Tablet,Norfloxacin (400mg) + Lactobacillus (120Million spores),Tablet,Cipla Ltd,Other,2024-07,2027-07,OT Store,50,strip,2024-08-20,Sanjivani Drug House
B00364,86045247,Rosugard 5mg Tablet,Rosuvastatin (5mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2028-01,Emergency Store,20,strip,2025-02-21,Sanjivani Drug House
B00365,NI24B710,Galvus Met 50mg/850mg Tablet,Metformin (850mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2024-04,2027-04,Emergency Store,100,strip,2024-05-31,Malabar Pharma Distributors
B00366,SPI244222,Oncoplatin AQ 10mg Injection,Cisplatin (10mg),Injection,Sun Pharmaceutical Industries Ltd,Oncology,2025-01,2027-01,Emergency Store,300,vial/amp,2025-03-18,Apollo Wholesale Pvt Ltd
B00367,CL24L627,Synclar 250mg Dry Syrup Mixed Fruit,Clarithromycin (250mg),Syrup,Cipla Ltd,Antibiotic,2024-04,2027-04,OPD Pharmacy,30,bottle,2024-06-21,Apollo Wholesale Pvt Ltd
B00368,T2503-936,Cosart 25 Tablet,Losartan (25mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2028-03,OPD Pharmacy,60,strip,2025-05-08,Sanjivani Drug House
B00369,I2406-442,Monocef 1gm Injection,Ceftriaxone (1gm),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2024-09,2027-09,ICU Store,150,vial/amp,2024-10-04,Sanjivani Drug House
B00370,83836812,Rabium 10 Tablet,Rabeprazole (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-03,2027-03,OT Store,150,strip,2025-03-29,Malabar Pharma Distributors
B00371,IP24L159,ZEN 100 Tablet DT,Carbamazepine (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2027-08,Ward Store (Paeds),30,strip,2024-09-07,Sanjivani Drug House
B00372,IPI248164,Evaparin -PFS 40 Injection,Enoxaparin (40mg),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2024-08,2026-02,ICU Store,200,vial/amp,2024-10-14,Sree Pharma Agencies
B00373,AI255324,Meroplan 500mg Injection,Meropenem (500mg),Injection,Abbott,Antibiotic,2025-04,2028-04,ICU Store,10,vial/amp,2025-07-15,Malabar Pharma Distributors
B00374,T2405-243,Azee 1000 Tablet,Azithromycin (1000mg),Tablet,Cipla Ltd,Antibiotic,2024-04,2025-10,OPD Pharmacy,60,strip,2024-07-29,Sanjivani Drug House
B00375,SIT253565,Valparin Alkalets 500 Tablet,Sodium Valproate (500mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2024-08,2026-08,OPD Pharmacy,20,strip,2024-09-14,Kerala Medical Supplies Co.
B00376,26143367,Cersar 20mg Tablet,Telmisartan (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2025-11,Emergency Store,150,strip,2024-06-30,Apollo Wholesale Pvt Ltd
B00377,T2403-317,Duphaston 10mg Tablet,Dydrogesterone (10mg),Tablet,Abbott,Other,2024-10,2027-10,Emergency Store,200,strip,2025-01-22,Sree Pharma Agencies
B00378,NLT240455,Amlyse 30mg Tablet,Ambroxol (30mg),Tablet,Neon Laboratories Ltd,Respiratory,2024-12,2026-06,ICU Store,10,strip,2025-03-09,Malabar Pharma Distributors
B00379,MPI251491,Venbruta 500mg Injection,Vancomycin (500mg),Injection,Mankind Pharma Ltd,Antibiotic,2024-07,2027-07,Emergency Store,10,vial/amp,2024-08-04,Malabar Pharma Distributors
B00380,A25C038,Flagyl ER Tablet,Metronidazole (600mg),Tablet,Abbott,Antibiotic,2025-01,2028-01,Main Pharmacy,80,strip,2025-03-03,Sanjivani Drug House
B00381,LLT244990,Dapaturn 10 Tablet,Dapagliflozin (10mg),Tablet,Lupin Ltd,Diabetes,2024-07,2026-07,Main Pharmacy,60,strip,2024-10-06,Sree Pharma Agencies
B00382,UB404B021,Sodium Chloride Injection IP 0.9%,Sodium Chloride (0.9% w/v),Infusion,Puniska Injectables Pvt. Ltd.,IV Fluids,2025-02,2028-01,OPD Pharmacy,30,bottle,2025-03-27,Malabar Pharma Distributors
B00383,IP24J330,Lethyrox 100 Tablet,Thyroxine (100mcg),Tablet,Intas Pharmaceuticals Ltd,Endocrine,2024-08,2027-08,Main Pharmacy,150,strip,2024-10-05,Apollo Wholesale Pvt Ltd
B00384,AP24M047,Folinal 5mg Tablet,Folic Acid (5mg),Tablet,Alembic Pharmaceuticals Ltd,Haematology,2025-01,2028-01,Emergency Store,0,strip,2025-02-09,Sanjivani Drug House
B00385,ZCI257761,Endoxan 1000mg Injection,Cyclophosphamide (1000mg),Injection,Zydus Cadila,Oncology,2024-07,2027-07,Ward Store (Paeds),120,vial/amp,2024-08-22,Kerala Medical Supplies Co.
B00386,SP25E420,Ceplox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2027-02,Ward Store (Paeds),120,strip,2024-04-18,Sree Pharma Agencies
B00387,96437170,Safoban Ointment,Fusidic Acid (NA),Ointment,Micro Labs Ltd,Dermatology,2024-02,2025-08,OT Store,40,tube,2024-04-08,"Medline Distributors, Thiruvananthapuram"
B00388,62036138,Cadvocet M 5mg/10mg Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Zydus Cadila,Respiratory,2024-08,2027-08,Emergency Store,60,strip,2024-09-24,"Medline Distributors, Thiruvananthapuram"
B00389,IP24E290,Intagenta 40mg Injection,Gentamicin (40mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,Main Pharmacy,50,vial/amp,2025-03-07,Kerala Medical Supplies Co.
B00390,EP24D679,Eprin 75mg Tablet,Aspirin (75mg),Tablet,Elder Pharmaceuticals Ltd,Cardiovascular,2025-02,2026-08,Emergency Store,120,strip,2025-04-10,Sree Pharma Agencies
B00391,SLI257263,Recosulin N 100IU Injection,Insulin Isophane (100IU),Injection,Shreya Life Sciences Pvt Ltd,Diabetes,2024-12,2027-12,OT Store,300,vial/amp,2025-03-26,Sree Pharma Agencies
B00392,S2409-608,Cerzin L 2.5mg/5ml Syrup,Levocetirizine (2.5mg/5ml),Syrup,Sun Pharmaceutical Industries Ltd,Respiratory,2025-02,2028-02,ICU Store,10,bottle,2025-04-11,Kerala Medical Supplies Co.
B00393,S2404-640,Bandy Suspension,Albendazole (200mg),Suspension,Mankind Pharma Ltd,Anthelmintic,2024-06,2027-06,Ward Store (Paeds),40,bottle,2024-09-25,Kerala Medical Supplies Co.
B00394,40409144,Mecabalin 500mcg Injection,Methylcobalamin (500mcg),Injection,Sun Pharmaceutical Industries Ltd,Supplement,2024-07,2027-07,OT Store,0,vial/amp,2024-10-21,Sanjivani Drug House
B00395,CL25A735,Emeset 4 Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-05,2026-05,ICU Store,20,strip,2024-08-02,"Medline Distributors, Thiruvananthapuram"
B00396,I2504-069,Cortilup 100mg Injection,Hydrocortisone (100mg),Injection,Lupin Ltd,Steroid,2025-04,2028-04,ICU Store,120,vial/amp,2025-07-07,Malabar Pharma Distributors
B00397,SPV248635,Lizoran 600mg Infusion,Linezolid (600mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-05,2026-11,Ward Store (Paeds),40,bottle,2025-06-24,Sanjivani Drug House
B00398,IP25B113,Sucragel Suspension,Sucralfate (500mg/5ml),Suspension,Intas Pharmaceuticals Ltd,Gastro,2024-06,2026-06,Ward Store (Paeds),10,bottle,2024-07-06,"Medline Distributors, Thiruvananthapuram"
B00399,I2510-901,Evaparin -PFS 40 Injection,Enoxaparin (40mg),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2025-03,2028-03,OPD Pharmacy,60,vial/amp,2025-06-16,Sree Pharma Agencies
B00400,S2507-187,Histanil Syrup,Chlorpheniramine Maleate (NA),Syrup,Troikaa Pharmaceuticals Ltd,Anti-allergic,2024-08,2026-08,Ward Store (Paeds),30,bottle,2024-11-09,Malabar Pharma Distributors
B00401,I2403-878,Cefaxone 0.25g Injection,Ceftriaxone (250mg),Injection,Lupin Ltd,Antibiotic,2024-12,2026-12,OT Store,200,vial/amp,2025-02-26,Kerala Medical Supplies Co.
B00402,T2501-686,Nuloc 20mg Tablet,Rabeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2025-01,2028-01,OT Store,200,strip,2025-04-27,Sanjivani Drug House
B00403,MP25E333,Texakind 500mg Injection,Tranexamic Acid (500mg),Injection,Mankind Pharma Ltd,Haematology,2025-05,2028-05,Emergency Store,300,vial/amp,2025-05-27,Sree Pharma Agencies
B00404,14344952,Mufect Ointment,Mupirocin (2%),Ointment,Sun Pharmaceutical Industries Ltd,Dermatology,2025-04,2028-04,Emergency Store,50,tube,2025-05-13,Kerala Medical Supplies Co.
B00405,IP25L053,Adiflox Ointment,Ciprofloxacin (0.3% w/w),Ointment,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2028-02,Main Pharmacy,150,tube,2025-05-16,Malabar Pharma Distributors
B00406,LH25D683,Edeflow 100 Tablet,Spironolactone (100mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-12,2026-06,Main Pharmacy,30,strip,2025-02-22,Malabar Pharma Distributors
B00407,I2506-121,Merinta 1000mg Injection,Meropenem (1000mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-10,2026-10,OT Store,60,vial/amp,2024-11-05,Sanjivani Drug House
B00408,T2405-880,Rantac 150 Tablet,Ranitidine (150mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-04,2026-04,Emergency Store,20,strip,2024-05-14,Kerala Medical Supplies Co.
B00409,66808785,Demisone 4mg Injection,Dexamethasone (4mg),Injection,Cadila Pharmaceuticals Ltd,Steroid,2024-07,2026-01,ICU Store,60,vial/amp,2024-10-26,"Medline Distributors, Thiruvananthapuram"
B00410,92035598,Metolar 50 Tablet,Metoprolol Tartrate (50mg),Tablet,Cipla Ltd,Cardiovascular,2025-05,2028-05,Main Pharmacy,200,strip,2025-07-15,Sree Pharma Agencies
B00411,X2408-209,Itchderm 1% Dusting Powder,Clotrimazole (1% w/w),Powder,Zydus Cadila,Antifungal,2024-06,2025-12,Ward Store (Paeds),60,pack,2024-08-04,Kerala Medical Supplies Co.
B00412,TP25G448,C-Pram S 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-02,2026-02,Emergency Store,80,strip,2024-05-06,Sree Pharma Agencies
B00413,16672885,Add Tears Lubricant Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Cipla Ltd,Ophthalmology,2024-09,2026-03,OT Store,120,bottle,2024-11-16,Sanjivani Drug House
B00414,TPT247462,Zedott 10 DT Tablet,Racecadotril (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-10,2027-10,ICU Store,200,strip,2024-11-20,Apollo Wholesale Pvt Ltd
B00415,NLI256917,Myostigmin 0.5mg Injection 1ml,Neostigmine (0.5mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-05,2025-11,ICU Store,150,vial/amp,2024-06-07,Sree Pharma Agencies
B00416,CL25M946,Asthalin Respirator Solution,Salbutamol (5mg),Solution,Cipla Ltd,Respiratory,2025-04,2027-04,OT Store,100,bottle,2025-04-26,Kerala Medical Supplies Co.
B00417,SII249920,Clexane 40mg Injection (0.4ml Each),Enoxaparin (40mg),Injection,Sanofi India Ltd,Anticoagulant,2024-08,2027-08,OPD Pharmacy,200,vial/amp,2024-10-30,"Medline Distributors, Thiruvananthapuram"
B00418,MPT251950,Nudiclo 100mg Tablet,Diclofenac (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-08,2027-08,OT Store,100,strip,2024-10-05,Apollo Wholesale Pvt Ltd
B00419,82468344,Glucreta 10mg Tablet,Dapagliflozin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-03,2026-03,Main Pharmacy,120,strip,2024-04-23,Malabar Pharma Distributors
B00420,IPT255237,Azerva 10 Tablet,Atorvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-01,Main Pharmacy,0,strip,2024-10-18,"Medline Distributors, Thiruvananthapuram"
B00421,T2508-532,Acuclav 1000mg Tablet,Amoxycillin (875mg) + Clavulanic Acid (125mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-09,2027-09,ICU Store,20,strip,2024-11-24,Malabar Pharma Distributors
B00422,GS24J572,Zentel Chewable Tablet,Albendazole (400mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2025-04,2026-10,Emergency Store,10,strip,2025-04-26,Sanjivani Drug House
B00423,LLT244475,Telect D 40mg/12.5mg Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Lupin Ltd,Cardiovascular,2024-06,2025-12,OPD Pharmacy,100,strip,2024-08-16,Sree Pharma Agencies
B00424,48909287,Evaparin -PFS 40 Injection,Enoxaparin (40mg),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2024-12,2027-12,OT Store,40,vial/amp,2025-02-01,"Medline Distributors, Thiruvananthapuram"
B00425,MPT255167,Doloban 100mg Tablet SR,Diclofenac (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-12,2026-12,ICU Store,200,strip,2025-03-17,Malabar Pharma Distributors
B00426,T2503-822,Hexapod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Micro Labs Ltd,Antibiotic,2024-01,2027-01,OT Store,30,strip,2024-04-18,Apollo Wholesale Pvt Ltd
B00427,TP24L416,Azulix 1 Tablet,Glimepiride (1mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-03,2027-03,ICU Store,20,strip,2025-03-27,Sree Pharma Agencies
B00428,SPT254326,Ceplox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-02,2026-08,OT Store,40,strip,2025-04-27,Malabar Pharma Distributors
B00429,96914605,Cefoprox 100mg Dry Syrup,Cefpodoxime Proxetil (100mg/5ml),Syrup,Cipla Ltd,Antibiotic,2024-10,2027-10,ICU Store,0,bottle,2024-12-01,Sree Pharma Agencies
B00430,MPI240187,Cefaclass 1000mg Injection,Ceftriaxone (1000mg),Injection,Mankind Pharma Ltd,Antibiotic,2024-11,2026-05,ICU Store,80,vial/amp,2025-02-05,"Medline Distributors, Thiruvananthapuram"
B00431,V2507-437,Aculife 25% Infusion,Dextrose (25% w/v),Infusion,Nirlife Healthcare,IV Fluids,2024-10,2027-10,Ward Store (Paeds),40,bottle,2024-11-04,Kerala Medical Supplies Co.
B00432,ZCS244748,Sucrace Suspension,Sucralfate (1000mg),Suspension,Zydus Cadila,Gastro,2025-03,2028-03,ICU Store,60,bottle,2025-03-30,Malabar Pharma Distributors
B00433,SP25J446,Rosuvas 10mg Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2026-09,OT Store,30,strip,2024-11-24,Malabar Pharma Distributors
B00434,CLT246636,Restyl 0.5mg Tablet,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-04,2027-04,ICU Store,200,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B00435,IP24D502,Decolite 0.10% Eye Drop,Dexamethasone (0.10% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Steroid,2024-02,2025-08,Emergency Store,120,bottle,2024-03-15,Sree Pharma Agencies
B00436,SPT258254,Carmaz 200mg Tablet,Carbamazepine (200mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2027-01,Ward Store (Paeds),150,strip,2024-04-06,"Medline Distributors, Thiruvananthapuram"
B00437,T2512-691,Happi 20 Tablet,Rabeprazole (20mg),Tablet,Zydus Cadila,Gastro,2024-04,2027-04,ICU Store,120,strip,2024-05-23,Kerala Medical Supplies Co.
B00438,SPI258715,Vecuron 10mg Injection,Vecuronium (10mg),Injection,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2025-03,2028-03,Ward Store (Paeds),200,vial/amp,2025-06-12,Sanjivani Drug House
B00439,87619624,Cetzine Syrup,Cetirizine (5mg/5ml),Syrup,Dr Reddy's Laboratories Ltd,Respiratory,2024-07,2026-07,OT Store,0,bottle,2024-08-04,Kerala Medical Supplies Co.
B00440,IP24G708,Levera 1000 Tablet,Levetiracetam (1000mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-10,2027-10,OPD Pharmacy,30,strip,2025-01-04,Kerala Medical Supplies Co.
B00441,T2508-567,Emeset 4 ODT Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-09,2026-09,OT Store,50,strip,2024-12-02,Malabar Pharma Distributors
B00442,MPI255129,Tranomac 500mg Injection,Tranexamic Acid (500mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Haematology,2025-04,2028-04,OT Store,150,vial/amp,2025-07-15,Kerala Medical Supplies Co.
B00443,ALT252977,Ondem -MD 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-02,2026-02,Emergency Store,20,strip,2024-03-22,Kerala Medical Supplies Co.
B00444,ZCI254009,Gerpyrin 1000mg Injection,Paracetamol (1000mg),Injection,Zydus Cadila,Analgesic/Antipyretic,2024-09,2026-09,Ward Store (Paeds),10,vial/amp,2024-12-04,Apollo Wholesale Pvt Ltd
B00445,CBT247324,Cgfru 40mg Tablet,Furosemide (40mg),Tablet,Cmg Biotech Pvt Ltd,Cardiovascular,2024-07,2026-07,OPD Pharmacy,60,strip,2024-09-19,Malabar Pharma Distributors
B00446,X2403-752,Potmeg 1.5gm Oral Solution Sugar Free,Potassium Chloride (1.5gm),Oral Solution,Ridhima Biocare,Anaesthesia/Critical care,2024-01,2027-01,ICU Store,60,bottle,2024-02-25,Kerala Medical Supplies Co.
B00447,SP24E711,Senorm LA Injection,Haloperidol Decanoate (50mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-10,2027-10,Main Pharmacy,20,vial/amp,2024-11-29,Sree Pharma Agencies
B00448,I2402-027,Magnesium Sulphate 0.25% Injection,Magnesium Sulphate (25% w/v),Injection,Hindustan Antibiotics Ltd,Anaesthesia/Critical care,2024-02,2026-02,Emergency Store,300,vial/amp,2024-03-24,Kerala Medical Supplies Co.
B00449,ZC24K946,Derinide 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Zydus Cadila,Respiratory,2024-04,2026-04,Ward Store (Paeds),120,respule,2024-07-29,Sanjivani Drug House
B00450,TP25C027,Zedott 10 DT Tablet,Racecadotril (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-05,2027-05,OT Store,150,strip,2025-06-25,Apollo Wholesale Pvt Ltd
B00451,T2401-689,Eldoflam 120mg Tablet,Etoricoxib (120mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-11,2026-05,Emergency Store,60,strip,2024-12-18,Malabar Pharma Distributors
B00452,AL24M965,Albekem 400mg Tablet,Albendazole (400mg),Tablet,Alkem Laboratories Ltd,Anthelmintic,2024-07,2027-07,Main Pharmacy,50,strip,2024-09-05,Sree Pharma Agencies
B00453,3305,Lorazepam Tablets IP 1 mg,Lorazepam (1mg),Tablet,Reliance Formulation Pvt. Ltd.,Neurology/Psychiatry,2024-04,2028-03,OT Store,30,strip,2024-07-18,"Medline Distributors, Thiruvananthapuram"
B00454,T2404-259,Cifran 250 Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-03,2027-03,ICU Store,300,strip,2025-06-11,Malabar Pharma Distributors
B00455,CL24H485,Dapasach 10mg Tablet,Dapagliflozin (10mg),Tablet,Cipla Ltd,Diabetes,2024-01,2027-01,Main Pharmacy,30,strip,2024-01-28,Apollo Wholesale Pvt Ltd
B00456,T2409-043,Ketanov 10mg Tablet,Ketorolac (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-10,2027-10,OPD Pharmacy,10,strip,2024-12-29,Malabar Pharma Distributors
B00457,CL24H987,Metolar 100 Tablet,Metoprolol Tartrate (100mg),Tablet,Cipla Ltd,Cardiovascular,2024-03,2026-03,Emergency Store,0,strip,2024-04-04,"Medline Distributors, Thiruvananthapuram"
B00458,IPT243228,Iverintas 12mg Tablet,Ivermectin (12mg),Tablet,Intas Pharmaceuticals Ltd,Anthelmintic,2024-12,2027-12,Ward Store (Paeds),30,strip,2025-03-08,Malabar Pharma Distributors
B00459,NLI240434,Fent 50mcg Injection,Fentanyl (50mcg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-05,2027-05,Main Pharmacy,100,vial/amp,2024-06-06,Apollo Wholesale Pvt Ltd
B00460,I2403-379,Ketam 10mg Injection,Ketamine (10mg),Injection,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2025-02,2027-02,OT Store,30,vial/amp,2025-05-14,Kerala Medical Supplies Co.
B00461,76445238,Ondamac 2mg Injection,Ondansetron (2mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2024-02,2026-02,Emergency Store,100,vial/amp,2024-04-24,Kerala Medical Supplies Co.
B00462,24314759,Dytor 20 Tablet,Torasemide (20mg),Tablet,Cipla Ltd,Cardiovascular,2025-05,2027-05,Emergency Store,60,strip,2025-06-25,Kerala Medical Supplies Co.
B00463,LLT243437,Aceclonac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-01,2027-01,OPD Pharmacy,20,strip,2025-03-03,Malabar Pharma Distributors
B00464,T2512-354,Ketof-DT Tablet,Ketorolac (10mg),Tablet,Abbott,Analgesic/Antipyretic,2024-10,2027-10,OPD Pharmacy,60,strip,2025-01-17,Kerala Medical Supplies Co.
B00465,AI071-L24,Folitrax-15 Injection,Methotrexate (15mg/ml),Injection,BDH Industrial Ltd.,Oncology,2024-11,2026-11,OT Store,100,vial/amp,2025-02-26,Apollo Wholesale Pvt Ltd
B00466,T2411-188,Glimikem 1mg Tablet,Glimepiride (1mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-03,2028-03,Ward Store (Paeds),150,strip,2025-05-18,Kerala Medical Supplies Co.
B00467,IP24D548,Pregabid 150 Capsule,Pregabalin (150mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-02,2026-02,Emergency Store,30,strip,2024-05-20,Malabar Pharma Distributors
B00468,T2504-046,Osteofit-HD Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Alembic Pharmaceuticals Ltd,Supplement,2024-09,2026-03,OPD Pharmacy,30,strip,2024-10-25,Kerala Medical Supplies Co.
B00469,AT254768,Acevah P 100 mg/325 mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Abbott,Analgesic/Antipyretic,2024-01,2026-01,Ward Store (Paeds),300,strip,2024-04-17,Sree Pharma Agencies
B00470,MLX256194,Levobact 0.5% Eye Drop,Levofloxacin (0.5%),Eye Drops,Micro Labs Ltd,Antibiotic,2024-06,2026-06,ICU Store,300,bottle,2024-07-14,"Medline Distributors, Thiruvananthapuram"
B00471,PLT259283,Wysolone 5 Tablet DT,Prednisolone (5mg),Tablet,Pfizer Ltd,Steroid,2024-10,2027-10,ICU Store,40,strip,2025-01-26,"Medline Distributors, Thiruvananthapuram"
B00472,73190952,Erkacin 100mg Injection,Amikacin (100mg),Injection,Micro Labs Ltd,Antibiotic,2025-05,2026-11,OT Store,150,vial/amp,2025-07-15,Apollo Wholesale Pvt Ltd
B00473,TPT241351,Nexpro Fast 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-05,2027-05,Main Pharmacy,150,strip,2025-07-15,Sanjivani Drug House
B00474,T2503-047,Eprin 75mg Tablet,Aspirin (75mg),Tablet,Elder Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-09,Main Pharmacy,60,strip,2024-11-11,"Medline Distributors, Thiruvananthapuram"
B00475,TP24J411,Sitaxa 100 Tablet,Sitagliptin (100mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-08,2026-08,OT Store,200,strip,2024-10-18,Kerala Medical Supplies Co.
B00476,48068331,Pregadoc 75 Capsule,Pregabalin (75mg),Capsule,Lupin Ltd,Neurology/Psychiatry,2024-09,2027-09,OPD Pharmacy,30,strip,2024-12-21,"Medline Distributors, Thiruvananthapuram"
B00477,SPI255393,Mecabalin 500mcg Injection,Methylcobalamin (500mcg),Injection,Sun Pharmaceutical Industries Ltd,Supplement,2024-12,2026-12,ICU Store,120,vial/amp,2025-01-12,"Medline Distributors, Thiruvananthapuram"
B00478,S2512-955,Lupicip 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Lupin Ltd,Analgesic/Antipyretic,2024-11,2026-05,Ward Store (Paeds),100,bottle,2024-12-03,Kerala Medical Supplies Co.
B00479,42865016,Synclar 250mg Dry Syrup Mixed Fruit,Clarithromycin (250mg),Syrup,Cipla Ltd,Antibiotic,2024-10,2026-10,Main Pharmacy,200,bottle,2024-12-24,"Medline Distributors, Thiruvananthapuram"
B00480,I2410-583,Monocef 1gm Injection,Ceftriaxone (1gm),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2024-07,2027-07,Emergency Store,60,vial/amp,2024-09-02,"Medline Distributors, Thiruvananthapuram"
B00481,IP25A219,Biselect 10 Tablet,Bisoprolol (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-03,2027-03,Main Pharmacy,100,strip,2024-04-10,Kerala Medical Supplies Co.
B00482,ZCT244389,Amgat 625 Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Zydus Cadila,Antibiotic,2024-09,2026-09,Ward Store (Paeds),0,strip,2024-10-08,Sree Pharma Agencies
B00483,IP25J787,Misolog 200mcg Tablet,Misoprostol (200mcg),Tablet,Intas Pharmaceuticals Ltd,Obstetrics,2024-03,2027-03,Ward Store (Paeds),60,strip,2024-05-31,Sanjivani Drug House
B00484,18459845,Rosugard 5mg Tablet,Rosuvastatin (5mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2026-04,OT Store,100,strip,2024-07-23,Apollo Wholesale Pvt Ltd
B00485,IP25A048,Omecap 20mg Capsule,Omeprazole (20mg),Capsule,Intas Pharmaceuticals Ltd,Gastro,2024-04,2025-10,OT Store,60,strip,2024-06-28,Apollo Wholesale Pvt Ltd
B00486,RK25E189,Glumig Injection,Calcium Gluconate (10mg),Injection,RSM Kilitch Pharma Pvt Ltd,Anaesthesia/Critical care,2025-03,2028-03,Ward Store (Paeds),30,vial/amp,2025-05-01,Sanjivani Drug House
B00487,GST255248,Zovirax 800 Tablet,Acyclovir (800mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2024-07,2027-07,Ward Store (Paeds),200,strip,2024-07-27,Sanjivani Drug House
B00488,SPT259509,Contiflo Icon 0.4mg Tablet PR,Tamsulosin (0.4mg),Tablet,Sun Pharmaceutical Industries Ltd,Urology,2025-03,2027-03,OPD Pharmacy,0,strip,2025-04-23,Malabar Pharma Distributors
B00489,ML24C212,Panflux 40mg Tablet,Pantoprazole (40mg),Tablet,Micro Labs Ltd,Gastro,2024-08,2026-08,Emergency Store,20,strip,2024-09-28,Sanjivani Drug House
B00490,IPI252468,Aquagest 25mg Injection,Progesterone (Natural Micronized) (25mg),Injection,Intas Pharmaceuticals Ltd,Obstetrics,2024-01,2026-01,ICU Store,100,vial/amp,2024-02-11,Sanjivani Drug House
B00491,IP25A414,Halo 5mg Capsule,Haloperidol (5mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-02,2028-02,Ward Store (Paeds),60,strip,2025-03-23,Sree Pharma Agencies
B00492,MPS242300,Zithrox 100 Rediuse Suspension,Azithromycin (100mg/5ml),Suspension,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-03,2026-03,OPD Pharmacy,80,bottle,2024-04-20,Sanjivani Drug House
B00493,37827407,Daparyl 10 Tablet,Dapagliflozin (10mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-02,2027-02,OPD Pharmacy,300,strip,2024-05-10,Sree Pharma Agencies
B00494,I2511-067,Ricetral 0.3gm Injection,Potassium Chloride (0.3gm),Injection,FDC Ltd,Anaesthesia/Critical care,2025-02,2026-08,ICU Store,60,vial/amp,2025-04-10,"Medline Distributors, Thiruvananthapuram"
B00495,T2511-927,Depotex 4mg Tablet,Methylprednisolone (4mg),Tablet,Zydus Cadila,Steroid,2025-04,2028-04,Ward Store (Paeds),40,strip,2025-05-27,Sanjivani Drug House
B00496,T2409-931,Stromix 75mg Tablet,Clopidogrel (75mg),Tablet,Abbott,Cardiovascular,2024-09,2027-09,OPD Pharmacy,80,strip,2024-12-09,Sanjivani Drug House
B00497,91546931,Levexx 100mg Injection,Levetiracetam (100mg),Injection,Zydus Cadila,Neurology/Psychiatry,2024-12,2027-12,OT Store,60,vial/amp,2025-01-22,Sanjivani Drug House
B00498,31030803,Ovit-Cee Injection,Vitamin C (250mg),Injection,Oscar Remedies Pvt Ltd,Supplement,2025-04,2028-04,Main Pharmacy,120,vial/amp,2025-07-13,Sree Pharma Agencies
B00499,MPT247359,Mefkind P 100mg Tablet,Mefenamic Acid (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2025-04,2028-04,Ward Store (Paeds),40,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B00500,T2412-052,Ketanov 10mg Tablet,Ketorolac (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-12,2027-12,OT Store,300,strip,2025-02-20,"Medline Distributors, Thiruvananthapuram"
B00501,T2509-389,Levocet 10mg Tablet,Levocetirizine (10mg),Tablet,Hetero Healthcare Limited,Respiratory,2024-05,2027-05,OT Store,30,strip,2024-06-24,Kerala Medical Supplies Co.
B00502,11339009,Glimpid 1 Tablet,Glimepiride (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-04,2028-04,OT Store,80,strip,2025-06-08,Sanjivani Drug House
B00503,IPC241253,Pregabid 150 Capsule,Pregabalin (150mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-03,2028-03,OPD Pharmacy,10,strip,2025-05-03,Sanjivani Drug House
B00504,SPT251456,Ceplox 750mg Tablet,Ciprofloxacin (750mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-04,2026-10,OPD Pharmacy,100,strip,2025-06-10,Malabar Pharma Distributors
B00505,88544364,Folvite 5mg Tablet,Folic Acid (5mg),Tablet,Pfizer Ltd,Haematology,2025-03,2028-03,ICU Store,30,strip,2025-04-21,"Medline Distributors, Thiruvananthapuram"
B00506,SPT246025,Rpitant 200mcg Tablet,Misoprostol (200mcg),Tablet,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-10,2026-04,OT Store,40,strip,2024-11-24,Sree Pharma Agencies
B00507,67308741,Drotin DS Tablet,Drotaverine (80mg),Tablet,Walter Bushnell,Gastro,2024-11,2027-11,ICU Store,150,strip,2025-02-22,Kerala Medical Supplies Co.
B00508,T2402-765,Omez 40 Tablet,Omeprazole (40mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2025-02,2027-02,OT Store,30,strip,2025-05-04,Apollo Wholesale Pvt Ltd
B00509,LL24B340,Lupenox 20mg Injection,Enoxaparin (20mg),Injection,Lupin Ltd,Anticoagulant,2024-11,2026-11,Main Pharmacy,30,vial/amp,2025-01-17,Sree Pharma Agencies
B00510,T2411-482,Teli 20 Tablet,Telmisartan (20mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,OPD Pharmacy,60,strip,2024-11-01,Sree Pharma Agencies
B00511,90492828,Imulast 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Cipla Ltd,Antimalarial,2024-06,2025-12,OPD Pharmacy,120,strip,2024-08-12,Apollo Wholesale Pvt Ltd
B00512,GS24G687,Zovirax 800 Tablet,Acyclovir (800mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2024-11,2026-11,OT Store,30,strip,2025-02-27,Kerala Medical Supplies Co.
B00513,I2401-411,Alcidic 75mg Injection,Diclofenac (75mg),Injection,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-11,2027-11,ICU Store,150,vial/amp,2024-12-21,Kerala Medical Supplies Co.
B00514,13420583,AMANAT 10MG TABLET,Amlodipine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-11,2026-11,OT Store,10,strip,2024-12-02,Sanjivani Drug House
B00515,SPV251868,Metronil 500mg Infusion,Metronidazole (500mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2026-04,Ward Store (Paeds),150,bottle,2024-11-30,Sanjivani Drug House
B00516,HD24F974,Levocet M Kid Tablet MD,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Hetero Drugs Ltd,Respiratory,2024-11,2027-11,OT Store,150,strip,2025-02-16,Sanjivani Drug House
B00517,59074470,Toride 20mg Tablet,Torasemide (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2026-12,ICU Store,0,strip,2025-03-21,Sanjivani Drug House
B00518,PLI251392,Magnex 1g Injection,Cefoperazone (500mg) + Sulbactam (500mg),Injection,Pfizer Ltd,Antibiotic,2024-06,2026-06,Ward Store (Paeds),30,vial/amp,2024-07-28,Sanjivani Drug House
B00519,P24C127,Synramine 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psycormedies,Anti-allergic,2024-04,2027-04,Ward Store (Paeds),300,strip,2024-07-15,Sanjivani Drug House
B00520,IPT240172,Amitone 10mg Tablet,Amitriptyline (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-05,2028-05,OPD Pharmacy,80,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B00521,AL25J927,Tobrex 2X Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alcon Laboratories,Ophthalmology,2025-01,2027-01,OT Store,80,bottle,2025-03-09,Malabar Pharma Distributors
B00522,CL25G405,Dytor 40 Tablet,Torasemide (40mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2026-07,Emergency Store,120,strip,2024-10-27,Apollo Wholesale Pvt Ltd
B00523,ALT254461,Ceriz-L Mont Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Alkem Laboratories Ltd,Respiratory,2024-05,2027-05,Main Pharmacy,150,strip,2024-06-03,"Medline Distributors, Thiruvananthapuram"
B00524,76848478,Gabantin 100 Capsule,Gabapentin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-06,2026-06,ICU Store,20,strip,2024-09-19,"Medline Distributors, Thiruvananthapuram"
B00525,X2409-106,Fucidin H Cream,Hydrocortisone (1% w/w) + Fusidic Acid (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Steroid,2024-11,2026-11,Main Pharmacy,200,tube,2025-01-16,Kerala Medical Supplies Co.
B00526,T2511-029,CV Sprin 75mg Tablet,Aspirin (75mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2025-03,2027-03,Main Pharmacy,150,strip,2025-04-24,"Medline Distributors, Thiruvananthapuram"
B00527,MLI244333,Divon 25mg Injection,Diclofenac (25mg),Injection,Micro Labs Ltd,Analgesic/Antipyretic,2024-04,2026-04,Emergency Store,150,vial/amp,2024-05-31,Sree Pharma Agencies
B00528,GC25F628,Crocin Advance Tablet,Paracetamol (500mg),Tablet,GlaxoSmithKline Consumer Healthcare,Analgesic/Antipyretic,2025-02,2026-08,Main Pharmacy,300,strip,2025-03-31,Malabar Pharma Distributors
B00529,T2501-177,Zerodol Spas Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Ipca Laboratories Ltd,Gastro,2025-05,2028-05,OPD Pharmacy,60,strip,2025-06-30,Sanjivani Drug House
B00530,SP25B091,Oleanz 2.5 Tablet,Olanzapine (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-03,2026-03,OPD Pharmacy,50,strip,2024-04-15,Kerala Medical Supplies Co.
B00531,I2505-470,Vancogram 500mg Injection,Vancomycin (500mg),Injection,Biochem Pharmaceutical Industries,Antibiotic,2024-03,2027-03,ICU Store,10,vial/amp,2024-04-20,Malabar Pharma Distributors
B00532,IPV243684,C Flox 200mg Infusion,Ciprofloxacin (200mg),Infusion,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,OT Store,60,bottle,2025-02-10,Sanjivani Drug House
B00533,GS24H936,T-Bact 2% Ointment,Mupirocin (2% w/w),Ointment,Glaxo SmithKline Pharmaceuticals Ltd,Dermatology,2024-04,2025-10,OPD Pharmacy,20,tube,2024-06-29,Kerala Medical Supplies Co.
B00534,T2511-739,Albekem 400mg Tablet,Albendazole (400mg),Tablet,Alkem Laboratories Ltd,Anthelmintic,2024-04,2026-04,OT Store,0,strip,2024-06-21,"Medline Distributors, Thiruvananthapuram"
B00535,T2510-004,Cardivas 12.5 Tablet,Carvedilol (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2027-12,Ward Store (Paeds),30,strip,2025-02-04,Malabar Pharma Distributors
B00536,AV256216,Flagyl 0.5% Solution for Infusion,Metronidazole (500mg),Infusion,Abbott,Antibiotic,2024-07,2027-07,Main Pharmacy,200,bottle,2024-08-27,Kerala Medical Supplies Co.
B00537,IPT250137,Prazopill XL 2.5 Tablet,Prazosin (2.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,Main Pharmacy,60,strip,2024-09-05,Sanjivani Drug House
B00538,T2506-739,Abmetop 25 XL Tablet,Metoprolol Succinate (23.75mg),Tablet,Abbott,Cardiovascular,2024-10,2026-10,Main Pharmacy,300,strip,2024-12-13,Malabar Pharma Distributors
B00539,SP24E803,Clopilet A 75 Capsule,Aspirin (75mg) + Clopidogrel (75mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-01,2027-01,Emergency Store,50,strip,2024-04-04,"Medline Distributors, Thiruvananthapuram"
B00540,ZC25M394,Cadvocet M 5mg/10mg Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Zydus Cadila,Respiratory,2025-05,2027-05,OT Store,100,strip,2025-06-05,Malabar Pharma Distributors
B00541,MPT240680,Metakind 1000mg Tablet SR,Metformin (1000mg),Tablet,Mankind Pharma Ltd,Diabetes,2024-03,2027-03,OT Store,40,strip,2024-04-19,Sanjivani Drug House
B00542,ALI255276,Becef 125mg Injection,Ceftriaxone (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-02,2027-02,OPD Pharmacy,40,vial/amp,2024-03-15,Apollo Wholesale Pvt Ltd
B00543,ZC25G182,Epsolin 150mg Tablet ER,Phenytoin (150mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-12,2027-12,OPD Pharmacy,50,strip,2024-12-26,Sree Pharma Agencies
B00544,AP24C577,D 10% Infusion,Dextrose (10% w/v),Infusion,AXA Parenterals Ltd,IV Fluids,2025-03,2028-03,ICU Store,50,bottle,2025-05-13,Sanjivani Drug House
B00545,IP24D758,Espin TM Tablet,S-Amlodipine (2.5mg) + Telmisartan (40mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-05,2028-05,OPD Pharmacy,50,strip,2025-06-08,Sanjivani Drug House
B00546,IPT241037,Daparyl 10 Tablet,Dapagliflozin (10mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2025-01,2028-01,Emergency Store,20,strip,2025-03-04,Sanjivani Drug House
B00547,20613757,Dytor 40 Tablet,Torasemide (40mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2026-07,ICU Store,50,strip,2024-08-17,Kerala Medical Supplies Co.
B00548,CL25B072,Amicip 100mg Injection,Amikacin (100mg),Injection,Cipla Ltd,Antibiotic,2024-12,2026-06,Emergency Store,80,vial/amp,2025-03-15,Sree Pharma Agencies
B00549,ML24J172,Fluza 150mg Tablet,Fluconazole (150mg),Tablet,Micro Labs Ltd,Antifungal,2024-12,2026-06,Emergency Store,10,strip,2025-03-01,Apollo Wholesale Pvt Ltd
B00550,70394471,Magnesium Sulphate 0.25% Injection,Magnesium Sulphate (25% w/v),Injection,Hindustan Antibiotics Ltd,Anaesthesia/Critical care,2024-04,2027-04,Emergency Store,100,vial/amp,2024-07-10,Sanjivani Drug House
B00551,CLX259088,Add Tears Lubricant Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Cipla Ltd,Ophthalmology,2025-02,2027-02,OT Store,60,bottle,2025-03-24,"Medline Distributors, Thiruvananthapuram"
B00552,CL24H726,Asthalin 2 Tablet,Salbutamol (2mg),Tablet,Cipla Ltd,Respiratory,2024-08,2026-02,ICU Store,300,strip,2024-09-27,Sree Pharma Agencies
B00553,WLI248269,Decadron Injection,Dexamethasone (4mg),Injection,Wockhardt Ltd,Steroid,2024-03,2027-03,OPD Pharmacy,150,vial/amp,2024-05-29,"Medline Distributors, Thiruvananthapuram"
B00554,SP25K550,Rosuvas 20 Tablet,Rosuvastatin (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2027-04,OPD Pharmacy,300,strip,2024-06-30,Malabar Pharma Distributors
B00555,I2406-418,Gerzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Zydus Cadila,Antibiotic,2024-05,2026-05,Main Pharmacy,100,vial/amp,2024-08-28,Sanjivani Drug House
B00556,NL25D435,Domin Injection,Dopamine (40mg/ml),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-11,2027-11,Emergency Store,30,vial/amp,2024-11-27,Sanjivani Drug House
B00557,T2501-250,Valparin Alkalets 500 Tablet,Sodium Valproate (500mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2024-10,2026-10,Emergency Store,20,strip,2024-10-31,Sanjivani Drug House
B00558,73598657,Folitrax 10 Tablet,Methotrexate (10mg),Tablet,Ipca Laboratories Ltd,Oncology,2024-05,2026-05,OPD Pharmacy,20,strip,2024-06-12,Sree Pharma Agencies
B00559,MLC242382,Microdox 100mg Capsule,Doxycycline (100mg),Capsule,Micro Labs Ltd,Antibiotic,2024-08,2026-08,Ward Store (Paeds),100,strip,2024-09-21,Kerala Medical Supplies Co.
B00560,MPI257696,Nupenta 40mg Injection,Pantoprazole (40mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2024-02,2027-02,OPD Pharmacy,80,vial/amp,2024-04-25,Sree Pharma Agencies
B00561,60874566,Presdown 40mg Tablet,Telmisartan (40mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-12,2026-12,Emergency Store,10,strip,2025-03-22,Malabar Pharma Distributors
B00562,TP25J403,Xamic 250mg Tablet,Tranexamic Acid (250mg),Tablet,Torrent Pharmaceuticals Ltd,Haematology,2024-12,2027-12,ICU Store,120,strip,2025-01-16,Sanjivani Drug House
B00563,T2503-447,Rovas 5mg Tablet,Rosuvastatin (5mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-05,2025-11,OPD Pharmacy,20,strip,2024-06-29,Sree Pharma Agencies
B00564,ZC24L730,Fusys 150 Tablet,Fluconazole (150mg),Tablet,Zydus Cadila,Antifungal,2025-04,2028-04,Emergency Store,40,strip,2025-05-29,Malabar Pharma Distributors
B00565,TPT249084,Cefiquik 100mg Tablet,Cefixime (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-02,2026-02,ICU Store,10,strip,2024-04-18,Malabar Pharma Distributors
B00566,CL24K857,Doxicip Injection,Doxycycline (100mg),Injection,Cipla Ltd,Antibiotic,2024-11,2027-11,ICU Store,100,vial/amp,2025-01-25,Kerala Medical Supplies Co.
B00567,TP24B246,Uniprest Tablet,Misoprostol (NA),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-06,2027-06,OPD Pharmacy,150,strip,2024-08-10,"Medline Distributors, Thiruvananthapuram"
B00568,T2511-438,Restyl 1mg Tablet,Alprazolam (1mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-01,2028-01,OPD Pharmacy,50,strip,2025-02-21,Sree Pharma Agencies
B00569,TPT242364,Corbis 1.25 Tablet,Bisoprolol (1.25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,Main Pharmacy,80,strip,2024-09-23,"Medline Distributors, Thiruvananthapuram"
B00570,X2411-796,Ocubion 5% Eye Drop,Sodium Chloride (5% w/v),Eye Drops,Ikon Remedies Pvt Ltd,IV Fluids,2024-02,2026-02,Emergency Store,0,bottle,2024-03-23,Sanjivani Drug House
B00571,T2405-366,Flagyl 200 Tablet,Metronidazole (200mg),Tablet,Abbott,Antibiotic,2025-05,2026-11,ICU Store,150,strip,2025-06-01,Kerala Medical Supplies Co.
B00572,14800151,Atorniz 10mg Tablet,Atorvastatin (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-06,2026-06,Ward Store (Paeds),300,strip,2024-09-23,Malabar Pharma Distributors
B00573,T2405-082,Vomistop 10 DT Tablet,Domperidone (10mg),Tablet,Cipla Ltd,Gastro,2024-02,2027-02,OT Store,40,strip,2024-05-03,Sree Pharma Agencies
B00574,IP24E130,Amitas 100mg Injection,Amikacin (100mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2025-03,2028-03,Ward Store (Paeds),40,vial/amp,2025-05-20,Malabar Pharma Distributors
B00575,CLT247485,Prazocip 2.5 XL Tablet,Prazosin (2.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2026-04,OT Store,120,strip,2025-01-25,Sanjivani Drug House
B00576,IP24L467,Clavitas 500mg/125mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-10,2027-10,Main Pharmacy,10,strip,2025-01-08,"Medline Distributors, Thiruvananthapuram"
B00577,IPV251087,C Flox 200mg Infusion,Ciprofloxacin (200mg),Infusion,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2026-06,Ward Store (Paeds),0,bottle,2025-01-22,Sree Pharma Agencies
B00578,TP24F607,Cocorex 10mg Syrup,Chlorpheniramine Maleate (10mg),Syrup,Taj Pharma India Ltd,Anti-allergic,2024-08,2026-08,OT Store,50,bottle,2024-09-03,Sanjivani Drug House
B00579,I2408-555,Tranarest 100mg Injection,Tranexamic Acid (100mg),Injection,Cadila Pharmaceuticals Ltd,Haematology,2024-09,2026-09,OT Store,40,vial/amp,2024-12-20,Apollo Wholesale Pvt Ltd
B00580,ALX254578,Bodygard Gel,Diclofenac (NA),Gel,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-12,2027-12,Emergency Store,120,tube,2025-01-03,Apollo Wholesale Pvt Ltd
B00581,CLT254168,Aceflex Plus 100 mg/500 mg Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-05,2026-05,Ward Store (Paeds),120,strip,2024-07-12,Malabar Pharma Distributors
B00582,48729652,Gluvilda 50 Tablet,Vildagliptin (50mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-10,2027-10,Emergency Store,40,strip,2025-01-03,"Medline Distributors, Thiruvananthapuram"
B00583,DRI253493,Osetron 4mg Injection,Ondansetron (4mg),Injection,Dr Reddy's Laboratories Ltd,Gastro,2024-10,2027-10,ICU Store,50,vial/amp,2024-11-22,Apollo Wholesale Pvt Ltd
B00584,MPI250992,Ondamac 2mg Injection,Ondansetron (2mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-01,2027-01,ICU Store,10,vial/amp,2025-01-31,"Medline Distributors, Thiruvananthapuram"
B00585,T2408-379,Klotfree Tablet,Clopidogrel (75mg),Tablet,Zydus Cadila,Cardiovascular,2024-07,2026-07,OPD Pharmacy,100,strip,2024-09-09,"Medline Distributors, Thiruvananthapuram"
B00586,T2406-443,Etrolup 90mg Tablet,Etoricoxib (90mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-01,2028-01,Main Pharmacy,40,strip,2025-03-19,Malabar Pharma Distributors
B00587,IP25J548,Celetoin 100 Tablet,Phenytoin (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-02,2028-02,OT Store,60,strip,2025-04-12,Sanjivani Drug House
B00588,MLT248379,Dolo 650 Tablet,Paracetamol (650mg),Tablet,Micro Labs Ltd,Analgesic/Antipyretic,2025-01,2026-07,Emergency Store,0,strip,2025-04-13,Sree Pharma Agencies
B00589,ALT245086,Ondem 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-03,2025-09,Main Pharmacy,10,strip,2024-05-28,Sree Pharma Agencies
B00590,SPT242855,Gemer 0.5 Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-08,2027-08,OPD Pharmacy,20,strip,2024-09-03,Malabar Pharma Distributors
B00591,AT254667,Stromix 75mg Tablet,Clopidogrel (75mg),Tablet,Abbott,Cardiovascular,2024-05,2025-11,Ward Store (Paeds),30,strip,2024-08-17,Sree Pharma Agencies
B00592,MP25M128,Bandy-Plus 12 Tablet,Ivermectin (12mg) + Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2024-12,2026-12,OT Store,100,strip,2025-02-09,Sanjivani Drug House
B00593,27995861,Spasidex Drop,Dicyclomine (NA),Drops,Wockhardt Ltd,Gastro,2025-04,2027-04,Emergency Store,120,bottle,2025-05-08,Sanjivani Drug House
B00594,SP24M325,Citelec 250mg Injection,Citicoline (250mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-02,2027-02,OT Store,150,vial/amp,2024-03-14,Sanjivani Drug House
B00595,SF24B867,Burnosaf Plus Cream,Silver Sulfadiazine (1% w/w),Cream,SAF Fermion Ltd,Dermatology,2025-02,2027-02,Main Pharmacy,100,tube,2025-03-12,Malabar Pharma Distributors
B00596,CLC256820,Endogest 100 Capsule,Progesterone (Natural Micronized) (100mg),Capsule,Cipla Ltd,Obstetrics,2024-05,2027-05,Emergency Store,0,strip,2024-08-04,Malabar Pharma Distributors
B00597,ZCT248524,Aten 100 Tablet,Atenolol (100mg),Tablet,Zydus Cadila,Cardiovascular,2024-01,2027-01,OPD Pharmacy,0,strip,2024-02-10,"Medline Distributors, Thiruvananthapuram"
B00598,CLI247293,Metaclopramide Injection,Metoclopramide (NA),Injection,Cipla Ltd,Gastro,2024-09,2026-09,OT Store,80,vial/amp,2024-10-28,Apollo Wholesale Pvt Ltd
B00599,CL24G102,Vanlid 250mg Capsule,Vancomycin (250mg),Capsule,Cipla Ltd,Antibiotic,2025-03,2028-03,ICU Store,50,strip,2025-06-24,Sanjivani Drug House
B00600,T2407-257,Nicopenta 40 Tablet,Pantoprazole (40mg),Tablet,Abbott,Gastro,2024-03,2027-03,OPD Pharmacy,200,strip,2024-05-09,Sanjivani Drug House
B00601,TPS247395,Lezyncet-M Suspension,Levocetirizine (5mg) + Montelukast (10mg),Suspension,Torrent Pharmaceuticals Ltd,Respiratory,2024-01,2026-01,ICU Store,40,bottle,2024-03-05,"Medline Distributors, Thiruvananthapuram"
B00602,MP25D450,Amlogift 5mg Tablet,Amlodipine (5mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-09,2027-09,Emergency Store,120,strip,2024-12-14,Kerala Medical Supplies Co.
B00603,88100019,Epsolin 300 Tablet,Phenytoin (300mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-12,2026-06,Emergency Store,60,strip,2025-03-10,Sree Pharma Agencies
B00604,CL25M408,Cofenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-11,2027-11,Main Pharmacy,300,strip,2025-01-27,Sanjivani Drug House
B00605,CLV251757,Levoflox 500 Infusion,Levofloxacin (500mg),Infusion,Cipla Ltd,Antibiotic,2024-04,2026-04,Emergency Store,300,bottle,2024-06-29,Malabar Pharma Distributors
B00606,T2408-963,Edeflow 100 Tablet,Spironolactone (100mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-01,2027-01,OPD Pharmacy,50,strip,2024-04-02,Sree Pharma Agencies
B00607,LLT255531,Clavidur 375mg Tablet,Amoxycillin (250mg) + Clavulanic Acid (125mg),Tablet,Lupin Ltd,Antibiotic,2024-08,2027-08,OPD Pharmacy,60,strip,2024-11-28,Apollo Wholesale Pvt Ltd
B00608,SP25A648,Abzorb 1% Cream,Clotrimazole (1% w/w),Cream,Sun Pharmaceutical Industries Ltd,Antifungal,2024-03,2025-09,Main Pharmacy,0,tube,2024-05-14,Sree Pharma Agencies
B00609,AL25J124,Dermikem Dusting Powder,Clotrimazole (1% w/w),Powder,Alkem Laboratories Ltd,Antifungal,2024-02,2027-02,Main Pharmacy,0,pack,2024-04-24,Apollo Wholesale Pvt Ltd
B00610,CLT247906,S Citadep 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-11,2026-11,ICU Store,200,strip,2024-12-01,"Medline Distributors, Thiruvananthapuram"
B00611,IR25J496,Ocubion 5% Eye Drop,Sodium Chloride (5% w/v),Eye Drops,Ikon Remedies Pvt Ltd,IV Fluids,2024-04,2027-04,ICU Store,0,bottle,2024-06-01,Sree Pharma Agencies
B00612,I2508-122,Vasocon Injection,Adrenaline (1mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-01,2026-01,Main Pharmacy,150,vial/amp,2024-04-21,Kerala Medical Supplies Co.
B00613,11418473,Raciper 20 Tablet,Esomeprazole (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-02,2028-02,ICU Store,120,strip,2025-05-26,Kerala Medical Supplies Co.
B00614,25193029,Losalife 25mg Tablet,Losartan (25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-01,2028-01,OT Store,120,strip,2025-03-28,Sree Pharma Agencies
B00615,AL24L622,Herpesafe Cream,Acyclovir (5% w/w),Cream,Alkem Laboratories Ltd,Antiviral,2025-04,2026-10,Ward Store (Paeds),30,tube,2025-06-25,Apollo Wholesale Pvt Ltd
B00616,77945312,Tossex 12 Oral Suspension Orange,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Abbott,Respiratory,2025-04,2027-04,OT Store,0,bottle,2025-07-15,Apollo Wholesale Pvt Ltd
B00617,93587401,Toride 20mg Tablet,Torasemide (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2027-09,Ward Store (Paeds),20,strip,2024-11-17,Sree Pharma Agencies
B00618,LL25C474,Dapaturn 10 Tablet,Dapagliflozin (10mg),Tablet,Lupin Ltd,Diabetes,2024-03,2027-03,Ward Store (Paeds),100,strip,2024-04-16,Kerala Medical Supplies Co.
B00619,AP25C953,Coxid 450mg Capsule,Rifampicin (450mg),Capsule,Aristo Pharmaceuticals Pvt Ltd,Anti-TB,2025-03,2027-03,Ward Store (Paeds),10,strip,2025-05-14,Kerala Medical Supplies Co.
B00620,94668837,Merocrit 0.5gm Injection,Meropenem (500mg),Injection,Cipla Ltd,Antibiotic,2024-02,2026-02,OT Store,200,vial/amp,2024-04-23,Kerala Medical Supplies Co.
B00621,I2507-446,Cortisum 100mg Injection,Hydrocortisone (100mg),Injection,Torrent Pharmaceuticals Ltd,Steroid,2025-01,2028-01,OPD Pharmacy,0,vial/amp,2025-02-04,Kerala Medical Supplies Co.
B00622,SPT242013,AMANAT 10MG TABLET,Amlodipine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2027-04,OPD Pharmacy,100,strip,2024-06-14,"Medline Distributors, Thiruvananthapuram"
B00623,X2401-396,Ketorol Gel,Ketorolac (20mg),Gel,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-06,2026-06,OT Store,200,tube,2024-08-21,Sree Pharma Agencies
B00624,TPI258477,Benzosed 1mg Injection,Midazolam (1mg),Injection,Troikaa Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2027-01,OT Store,120,vial/amp,2024-03-03,Sree Pharma Agencies
B00625,MLT240963,Udosis 500mg Tablet,Sodium Bicarbonate (500mg),Tablet,Micro Labs Ltd,Anaesthesia/Critical care,2024-09,2026-03,Main Pharmacy,30,strip,2024-12-12,Apollo Wholesale Pvt Ltd
B00626,LH25D185,Vomiford -MD Tablet,Ondansetron (4mg),Tablet,Leeford Healthcare Ltd,Gastro,2024-03,2025-09,Emergency Store,30,strip,2024-05-14,Sanjivani Drug House
B00627,AS250957,Tossex 12 Oral Suspension Orange,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Abbott,Respiratory,2024-01,2027-01,Main Pharmacy,60,bottle,2024-02-25,Kerala Medical Supplies Co.
B00628,I2411-450,Stedex 4mg Injection,Dexamethasone (4mg),Injection,Ind Swift Laboratories Ltd,Steroid,2024-02,2026-02,Emergency Store,10,vial/amp,2024-03-26,Apollo Wholesale Pvt Ltd
B00629,IR25F708,Cyclopam Plus Tablet,Dicyclomine (20mg) + Paracetamol (500mg),Tablet,Indoco Remedies Ltd,Analgesic/Antipyretic,2025-02,2028-02,Main Pharmacy,60,strip,2025-04-05,Malabar Pharma Distributors
B00630,ML24E529,Calvit 12 Injection,Calcium (137.5mg) + Vitamin D3 (5000IU),Injection,Marc Laboratories Pvt Ltd,Supplement,2025-03,2027-03,Ward Store (Paeds),40,vial/amp,2025-05-08,"Medline Distributors, Thiruvananthapuram"
B00631,T2503-562,Serenace 1.5 Tablet,Haloperidol (1.5mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-06,2026-06,ICU Store,30,strip,2024-07-29,Apollo Wholesale Pvt Ltd
B00632,NP24J067,Frusenat Injection,Furosemide (20mg/ml),Injection,Natco Pharma Ltd,Cardiovascular,2024-04,2025-10,Emergency Store,60,vial/amp,2024-06-11,Kerala Medical Supplies Co.
B00633,T2407-544,Doxcef 100mg Tablet,Cefpodoxime Proxetil (100mg),Tablet,Lupin Ltd,Antibiotic,2025-02,2026-08,OPD Pharmacy,120,strip,2025-04-09,Malabar Pharma Distributors
B00634,67521272,Lukotas 3D Tablet,Montelukast (10mg) + Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2025-03,2028-03,ICU Store,80,strip,2025-04-03,Kerala Medical Supplies Co.
B00635,TPT247706,Amlocor 10mg Tablet,Amlodipine (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,OPD Pharmacy,30,strip,2024-06-27,Malabar Pharma Distributors
B00636,T2405-627,Ramipres 1.25 Tablet,Ramipril (1.25mg),Tablet,Cipla Ltd,Cardiovascular,2024-09,2026-09,Emergency Store,60,strip,2024-10-11,Sanjivani Drug House
B00637,DRT242393,Stamlo 5 Tablet,Amlodipine (5mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-02,2026-02,Ward Store (Paeds),120,strip,2024-03-12,Apollo Wholesale Pvt Ltd
B00638,TP25L136,Eldoflam 120mg Tablet,Etoricoxib (120mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2026-08,Emergency Store,60,strip,2025-04-12,Kerala Medical Supplies Co.
B00639,T2508-911,Prazocip 2.5 XL Tablet,Prazosin (2.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-03,2025-09,OT Store,10,strip,2024-05-01,Kerala Medical Supplies Co.
B00640,L0372321C,Irolink Injection,Iron Sucrose (20mg/ml),Injection,Protech Telelinks,Haematology,2023-10,2025-09,OPD Pharmacy,30,vial/amp,2024-01-10,"Medline Distributors, Thiruvananthapuram"
B00641,I2406-211,Remtrex 15mg Injection,Methotrexate (15mg),Injection,Alkem Laboratories Ltd,Oncology,2025-05,2026-11,OT Store,10,vial/amp,2025-07-15,Kerala Medical Supplies Co.
B00642,DRI251815,Ketorol Injection,Ketorolac (30mg),Injection,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-01,2026-01,OPD Pharmacy,50,vial/amp,2024-02-04,Apollo Wholesale Pvt Ltd
B00643,62756521,Eltroxin 100mcg Tablet,Thyroxine (100mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2024-03,2027-03,OT Store,50,strip,2024-05-17,"Medline Distributors, Thiruvananthapuram"
B00644,TPT251472,Alprax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2027-05,OPD Pharmacy,40,strip,2024-06-05,Sanjivani Drug House
B00645,I2506-488,Ovit-Cee Injection,Vitamin C (250mg),Injection,Oscar Remedies Pvt Ltd,Supplement,2024-01,2026-01,OT Store,50,vial/amp,2024-02-09,Malabar Pharma Distributors
B00646,ALT257533,Losaral 50mg Tablet,Losartan (50mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-07,2026-07,ICU Store,50,strip,2024-08-08,Sree Pharma Agencies
B00647,AP24D571,Coxid 450mg Capsule,Rifampicin (450mg),Capsule,Aristo Pharmaceuticals Pvt Ltd,Anti-TB,2024-06,2026-06,ICU Store,150,strip,2024-07-15,"Medline Distributors, Thiruvananthapuram"
B00648,11523124,Levera 1000 Tablet,Levetiracetam (1000mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-12,2027-12,Emergency Store,60,strip,2025-01-22,Kerala Medical Supplies Co.
B00649,ML24D147,Meconerv Injection,Methylcobalamin (500mcg),Injection,Micro Labs Ltd,Supplement,2024-05,2026-05,Main Pharmacy,80,vial/amp,2024-07-16,Kerala Medical Supplies Co.
B00650,SPT253186,Cifran 500 Tablet,Ciprofloxacin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-06,2026-06,OPD Pharmacy,100,strip,2024-07-15,"Medline Distributors, Thiruvananthapuram"
B00651,CL24M730,Restyl 0.25mg Tablet,Alprazolam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-04,2027-04,Emergency Store,10,strip,2024-05-04,Kerala Medical Supplies Co.
B00652,MP25L671,Finamac 1000mg Infusion,Paracetamol (1000mg),Infusion,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-09,2026-09,Emergency Store,80,bottle,2024-11-06,Malabar Pharma Distributors
B00653,LL25B667,LNZ 600 Tablet,Linezolid (600mg),Tablet,Lupin Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,40,strip,2024-06-19,"Medline Distributors, Thiruvananthapuram"
B00654,CL24C203,Imulast 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Cipla Ltd,Antimalarial,2025-01,2028-01,OT Store,120,strip,2025-04-17,Sree Pharma Agencies
B00655,ALT250297,Formin PG 1 Forte Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-03,2026-09,OPD Pharmacy,50,strip,2025-04-03,Kerala Medical Supplies Co.
B00656,TPT259325,Loracalm 1mg Tablet,Lorazepam (1mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-04,2028-04,OPD Pharmacy,0,strip,2025-06-13,Kerala Medical Supplies Co.
B00657,TP25M812,Azukon MR Tablet,Gliclazide (30mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-04,2027-04,OPD Pharmacy,120,strip,2024-05-22,Sree Pharma Agencies
B00658,A25E195,Thyronorm 12.5mcg Tablet,Thyroxine (12.5mcg),Tablet,Abbott,Endocrine,2025-03,2027-03,Ward Store (Paeds),60,strip,2025-06-08,Apollo Wholesale Pvt Ltd
B00659,ML25B481,Rovas 5mg Tablet,Rosuvastatin (5mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-02,2027-02,ICU Store,80,strip,2024-04-28,Malabar Pharma Distributors
B00660,A24H119,Forxiga 5mg Tablet,Dapagliflozin (5mg),Tablet,AstraZeneca,Diabetes,2025-04,2028-04,Main Pharmacy,40,strip,2025-05-13,Apollo Wholesale Pvt Ltd
B00661,24798481,Aqsusten 25 Solution for Injection,Progesterone (Natural Micronized) (25mg),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-06,2027-06,OPD Pharmacy,300,vial/amp,2024-08-15,"Medline Distributors, Thiruvananthapuram"
B00662,ALT242525,Clear 250mg Tablet,Clarithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-08,2027-08,Main Pharmacy,40,strip,2024-10-31,Sree Pharma Agencies
B00663,CLT240285,Metolar 25 Tablet,Metoprolol Tartrate (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2026-05,ICU Store,80,strip,2024-06-15,Sanjivani Drug House
B00664,MP25C772,Mefomin 1000 SR Tablet,Metformin (1000mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Diabetes,2024-02,2025-08,Emergency Store,40,strip,2024-04-15,Apollo Wholesale Pvt Ltd
B00665,I2511-390,Calvit 12 Injection,Calcium (137.5mg) + Vitamin D3 (5000IU),Injection,Marc Laboratories Pvt Ltd,Supplement,2024-10,2026-04,Ward Store (Paeds),50,vial/amp,2025-01-01,Apollo Wholesale Pvt Ltd
B00666,X2408-197,Asthalin Respirator Solution,Salbutamol (5mg),Solution,Cipla Ltd,Respiratory,2024-02,2027-02,OPD Pharmacy,120,bottle,2024-05-10,Sanjivani Drug House
B00667,DRI244730,Doxt Injection Combipack,Doxycycline (100mg),Injection,Dr Reddy's Laboratories Ltd,Antibiotic,2024-01,2025-12,ICU Store,50,vial/amp,2024-01-31,Sanjivani Drug House
B00668,43003049,Oxytomed 5IU Injection,Oxytocin (5IU),Injection,Zydus Cadila,Obstetrics,2025-02,2027-02,Ward Store (Paeds),20,vial/amp,2025-05-08,Sanjivani Drug House
B00669,43059986,Intacoxia 120 Tablet,Etoricoxib (120mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2027-05,OPD Pharmacy,150,strip,2024-08-05,Kerala Medical Supplies Co.
B00670,48208680,Nexito 20 Tablet,Escitalopram Oxalate (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-09,2027-09,Emergency Store,200,strip,2024-12-18,Kerala Medical Supplies Co.
B00671,25050502,BIOFER S 100mg/5ml Injection,Iron Sucrose (100mg/5ml),Injection,Micro Labs Ltd,Haematology,2024-05,2027-05,ICU Store,10,vial/amp,2024-07-24,Sanjivani Drug House
B00672,LL25J783,DexLuz Oral Solution Lemon,Lactulose (10gm),Oral Solution,Lupin Ltd,Gastro,2024-07,2026-01,ICU Store,0,bottle,2024-09-22,Kerala Medical Supplies Co.
B00673,ALI243228,Platikem 20mg Injection,Cisplatin (20mg),Injection,Alkem Laboratories Ltd,Oncology,2024-04,2025-10,Main Pharmacy,60,vial/amp,2024-07-12,"Medline Distributors, Thiruvananthapuram"
B00674,55628196,Mefniwel 100mg Syrup,Mefenamic Acid (100mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2025-03,2028-03,OT Store,20,bottle,2025-05-20,"Medline Distributors, Thiruvananthapuram"
B00675,ZC24J640,Xylocaine 4% Injection,Lidocaine (4%),Injection,Zydus Cadila,Other,2024-10,2027-10,OPD Pharmacy,100,vial/amp,2025-01-28,Sree Pharma Agencies
B00676,69260945,DC 100mg Capsule,Doxycycline (100mg),Capsule,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2026-08,Ward Store (Paeds),120,strip,2025-04-14,"Medline Distributors, Thiruvananthapuram"
B00677,T2506-706,Serenace 0.5 Tablet,Haloperidol (0.5mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-08,2026-02,Ward Store (Paeds),0,strip,2024-08-27,Sree Pharma Agencies
B00678,48233775,Alzolam 0.125mg Tablet,Alprazolam (0.125mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-02,2027-02,ICU Store,60,strip,2024-04-08,Apollo Wholesale Pvt Ltd
B00679,SP24C614,Betavert 16 Tablet,Betahistine (16mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2027-01,ICU Store,60,strip,2024-03-11,"Medline Distributors, Thiruvananthapuram"
B00680,TP24D667,Xtrapred 0.25% Drop,Prednisolone (0.25%),Drops,Torrent Pharmaceuticals Ltd,Steroid,2025-04,2027-04,OPD Pharmacy,50,bottle,2025-05-18,Sanjivani Drug House
B00681,NL25C420,Anawin 0.25% Injection,Bupivacaine (0.25%),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-04,2026-04,OT Store,20,vial/amp,2024-06-10,Kerala Medical Supplies Co.
B00682,RBX254108,Potmeg 1.5gm Oral Solution Sugar Free,Potassium Chloride (1.5gm),Oral Solution,Ridhima Biocare,Anaesthesia/Critical care,2025-03,2026-09,Ward Store (Paeds),0,bottle,2025-05-12,Sanjivani Drug House
B00683,78027044,Safoderm Plus 1% Cream,Silver Sulfadiazine (1% w/w),Cream,Biochem Pharmaceutical Industries,Dermatology,2024-05,2025-11,Main Pharmacy,50,tube,2024-05-27,Apollo Wholesale Pvt Ltd
B00684,CB24A659,Cgglu 500 Tablet,Calcium Gluconate (500mg),Tablet,Cmg Biotech Pvt Ltd,Anaesthesia/Critical care,2024-12,2027-12,OT Store,30,strip,2025-01-17,Apollo Wholesale Pvt Ltd
B00685,53536830,Dytor 100 Tablet,Torasemide (100mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2027-03,ICU Store,40,strip,2025-04-02,Kerala Medical Supplies Co.
B00686,LL25A462,Aceclonac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-03,2028-03,Emergency Store,200,strip,2025-05-10,Apollo Wholesale Pvt Ltd
B00687,T2412-382,Warf 1 Tablet,Warfarin (1mg),Tablet,Cipla Ltd,Anticoagulant,2024-07,2027-07,OT Store,20,strip,2024-10-02,Sanjivani Drug House
B00688,PTI248722,Irolink Injection,Iron Sucrose (20mg/ml),Injection,Protech Telelinks,Haematology,2024-11,2026-11,ICU Store,60,vial/amp,2025-02-27,"Medline Distributors, Thiruvananthapuram"
B00689,IPT255766,Monit 10 Tablet,Isosorbide Mononitrate (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-01,OPD Pharmacy,200,strip,2024-03-10,Sanjivani Drug House
B00690,GP24D721,Candid Ear Drop,Lidocaine (2% w/v) + Clotrimazole (1% w/v),Ear Drops,Glenmark Pharmaceuticals Ltd,Antifungal,2024-09,2026-09,Main Pharmacy,150,bottle,2024-12-22,Kerala Medical Supplies Co.
B00691,28994170,Amitas 100mg Injection,Amikacin (100mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-06,2027-06,Ward Store (Paeds),100,vial/amp,2024-08-02,Sree Pharma Agencies
B00692,91179203,Derinide 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Zydus Cadila,Respiratory,2024-12,2026-06,OPD Pharmacy,60,respule,2025-03-03,Sree Pharma Agencies
B00693,I2503-204,Germero 1000mg Injection,Meropenem (1000mg),Injection,Zydus Cadila,Antibiotic,2024-08,2026-08,Emergency Store,10,vial/amp,2024-11-15,Malabar Pharma Distributors
B00694,28698551,NS – Sodium Chloride Injection IP,Sodium Chloride (0.9% w/v),Infusion,Pentagon Labs Ltd.,IV Fluids,2025-01,2027-01,Main Pharmacy,30,bottle,2025-02-06,"Medline Distributors, Thiruvananthapuram"
B00695,TP25E884,Izra 40 Tablet,Esomeprazole (40mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-12,2027-12,ICU Store,0,strip,2025-01-15,Sanjivani Drug House
B00696,83948598,Leemol 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-12,2027-12,Main Pharmacy,40,bottle,2025-01-09,Apollo Wholesale Pvt Ltd
B00697,IRI242935,Hepatag 25000IU Injection,Heparin (25000IU),Injection,Ikon Remedies Pvt Ltd,Anticoagulant,2024-05,2026-05,Emergency Store,200,vial/amp,2024-06-24,Sanjivani Drug House
B00698,C2403-369,Nifelat 10mg Capsule,Nifedipine (10mg),Capsule,Cipla Ltd,Cardiovascular,2024-07,2026-07,ICU Store,300,strip,2024-08-30,Apollo Wholesale Pvt Ltd
B00699,39339153,Acuclav 1000mg Tablet,Amoxycillin (875mg) + Clavulanic Acid (125mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-04,2027-04,OT Store,60,strip,2024-06-04,Sanjivani Drug House
B00700,DRT241018,Tryptomer 25mg Tablet,Amitriptyline (25mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2025-03,2027-03,OT Store,300,strip,2025-04-29,"Medline Distributors, Thiruvananthapuram"
B00701,40251937,Ceriz-L Mont Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Alkem Laboratories Ltd,Respiratory,2024-03,2026-03,OPD Pharmacy,300,strip,2024-05-13,Apollo Wholesale Pvt Ltd
B00702,MPT251779,Bandy-Plus 12 Tablet,Ivermectin (12mg) + Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2025-04,2028-04,Ward Store (Paeds),150,strip,2025-07-13,Sanjivani Drug House
B00703,T2511-420,Cifran 250 Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-04,2026-04,Ward Store (Paeds),0,strip,2024-06-30,"Medline Distributors, Thiruvananthapuram"
B00704,RL24C441,Serenace 10 Tablet,Haloperidol (10mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-12,2026-12,Ward Store (Paeds),20,strip,2025-02-27,Sanjivani Drug House
B00705,LLT249140,Verifica 100mg Tablet SR,Vildagliptin (100mg),Tablet,Lupin Ltd,Diabetes,2024-03,2025-09,Ward Store (Paeds),50,strip,2024-05-08,"Medline Distributors, Thiruvananthapuram"
B00706,T2506-880,Prazopress 1 Tablet,Prazosin (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-02,2026-02,Emergency Store,50,strip,2024-04-16,Malabar Pharma Distributors
B00707,14670638,Linid OD Tablet,Linezolid (1200mg),Tablet,Zydus Cadila,Antibiotic,2024-01,2026-01,OPD Pharmacy,10,strip,2024-02-11,Malabar Pharma Distributors
B00708,60458379,Emenorm 10mg Tablet,Metoclopramide (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-02,2028-02,Main Pharmacy,50,strip,2025-04-05,Kerala Medical Supplies Co.
B00709,X2409-458,Cetzine Oral Drops,Cetirizine (10mg),Drops,Dr Reddy's Laboratories Ltd,Respiratory,2024-10,2026-10,ICU Store,200,bottle,2025-01-01,"Medline Distributors, Thiruvananthapuram"
B00710,APS243527,Ambrodil Syrup,Ambroxol (30mg/5ml),Syrup,Aristo Pharmaceuticals Pvt Ltd,Respiratory,2025-03,2027-03,ICU Store,120,bottle,2025-04-26,Kerala Medical Supplies Co.
B00711,85432781,Wysolone 5 Tablet DT,Prednisolone (5mg),Tablet,Pfizer Ltd,Steroid,2025-04,2027-04,OPD Pharmacy,40,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B00712,S2502-746,Levtam 100mg Syrup,Levetiracetam (100mg),Syrup,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-10,2027-10,OT Store,10,bottle,2024-11-02,Apollo Wholesale Pvt Ltd
B00713,TS24047,Telmisartan Tablets IP 40 mg,Telmisartan (40mg),Tablet,Eurokem Laboratories Pvt. Ltd.,Cardiovascular,2024-10,2025-12,OT Store,20,strip,2025-01-08,Malabar Pharma Distributors
B00714,SPT248329,Metgem 1gm Tablet ER,Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-12,2027-12,Main Pharmacy,10,strip,2025-03-27,Kerala Medical Supplies Co.
B00715,T2411-917,Covance 25 Tablet,Losartan (25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2025-12,OT Store,300,strip,2024-08-11,Apollo Wholesale Pvt Ltd
B00716,90028838,ZEN 100 Tablet DT,Carbamazepine (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-05,2027-05,ICU Store,0,strip,2025-07-15,Kerala Medical Supplies Co.
B00717,22178177,Hydroquin 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Sun Pharmaceutical Industries Ltd,Antimalarial,2024-11,2027-11,OT Store,40,strip,2024-12-19,Sree Pharma Agencies
B00718,C2403-015,Altispor 100mg Capsule,Itraconazole (100mg),Capsule,Intas Pharmaceuticals Ltd,Antifungal,2024-12,2027-12,Main Pharmacy,150,strip,2025-01-13,Sree Pharma Agencies
B00719,PIT240688,Dexodil 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psychotropics India Ltd,Anti-allergic,2024-03,2026-03,OT Store,300,strip,2024-06-24,Kerala Medical Supplies Co.
B00720,93501427,Insucare N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Sun Pharmaceutical Industries Ltd,Diabetes,2024-10,2026-10,OPD Pharmacy,120,vial/amp,2024-11-07,Sree Pharma Agencies
B00721,MLT244760,Metapro -XL 25 Tablet,Metoprolol Succinate (23.75mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-03,2026-03,Emergency Store,300,strip,2024-03-28,Malabar Pharma Distributors
B00722,T2502-286,Ciplox 250 Tablet,Ciprofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2024-01,2026-01,Emergency Store,0,strip,2024-03-24,Sree Pharma Agencies
B00723,T2502-616,ASA 50mg Tablet,Aspirin (50mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2027-02,OPD Pharmacy,0,strip,2024-05-23,Kerala Medical Supplies Co.
B00724,SP25J886,Altiva 120mg Tablet,Fexofenadine (120mg),Tablet,Sun Pharmaceutical Industries Ltd,Respiratory,2024-02,2026-02,Ward Store (Paeds),40,strip,2024-03-13,"Medline Distributors, Thiruvananthapuram"
B00725,CLT243671,Clopicard 75mg Tablet,Clopidogrel (75mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2026-04,ICU Store,150,strip,2024-05-16,"Medline Distributors, Thiruvananthapuram"
B00726,V2403-364,D 10% Infusion,Dextrose (10% w/v),Infusion,AXA Parenterals Ltd,IV Fluids,2025-02,2028-02,OPD Pharmacy,50,bottle,2025-05-02,Kerala Medical Supplies Co.
B00727,C2404-707,Omecap 20mg Capsule,Omeprazole (20mg),Capsule,Intas Pharmaceuticals Ltd,Gastro,2024-05,2025-11,Main Pharmacy,300,strip,2024-07-22,Malabar Pharma Distributors
B00728,I2407-922,Monocef 125mg Injection,Ceftriaxone (125mg),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2024-06,2027-06,ICU Store,30,vial/amp,2024-09-07,"Medline Distributors, Thiruvananthapuram"
B00729,NI24D644,Galvus Met 50mg/500mg Tablet,Metformin (500mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2024-02,2025-08,ICU Store,40,strip,2024-05-03,Kerala Medical Supplies Co.
B00730,TPI242381,Bupitroy 0.5% Injection,Bupivacaine (0.5%),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-05,2026-05,ICU Store,120,vial/amp,2024-07-24,Malabar Pharma Distributors
B00731,86639453,Flucobig 150mg Tablet,Fluconazole (150mg),Tablet,Torrent Pharmaceuticals Ltd,Antifungal,2024-11,2026-11,ICU Store,20,strip,2025-02-20,Sree Pharma Agencies
B00732,ZC25F575,Endoxan 1000mg Injection,Cyclophosphamide (1000mg),Injection,Zydus Cadila,Oncology,2024-04,2026-04,Ward Store (Paeds),300,vial/amp,2024-04-28,Malabar Pharma Distributors
B00733,TPI244120,Nausinorm 5mg Injection,Metoclopramide (5mg),Injection,Torrent Pharmaceuticals Ltd,Gastro,2025-04,2028-04,Main Pharmacy,150,vial/amp,2025-05-14,Kerala Medical Supplies Co.
B00734,MPV240774,Finamac 1000mg Infusion,Paracetamol (1000mg),Infusion,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-03,2026-03,OPD Pharmacy,120,bottle,2024-05-05,Apollo Wholesale Pvt Ltd
B00735,TP24C411,Lezyncet 10 Tablet DT,Levocetirizine (10mg),Tablet,Torrent Pharmaceuticals Ltd,Respiratory,2024-11,2027-11,Emergency Store,20,strip,2025-01-06,Malabar Pharma Distributors
B00736,T2502-815,Deplatt A 75 Tablet,Aspirin (75mg) + Clopidogrel (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-12,2027-12,OPD Pharmacy,60,strip,2025-03-04,Apollo Wholesale Pvt Ltd
B00737,46190613,Bupizuva 2.5mg Injection,Bupivacaine (2.5mg/ml),Injection,Abbott,Anaesthesia/Critical care,2024-12,2027-12,ICU Store,300,vial/amp,2025-03-17,Malabar Pharma Distributors
B00738,LL24H234,Clavidur 375mg Tablet,Amoxycillin (250mg) + Clavulanic Acid (125mg),Tablet,Lupin Ltd,Antibiotic,2024-11,2026-05,OPD Pharmacy,150,strip,2024-11-26,Malabar Pharma Distributors
B00739,T2409-281,Lupidexa 0.5mg Tablet,Dexamethasone (0.5mg),Tablet,Lupin Ltd,Steroid,2024-09,2027-09,ICU Store,40,strip,2024-12-25,"Medline Distributors, Thiruvananthapuram"
B00740,IP25L956,Azintas 250 Tablet,Azithromycin (250mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-05,2025-11,ICU Store,20,strip,2024-08-22,Sree Pharma Agencies
B00741,47691414,Omecap 20mg Capsule,Omeprazole (20mg),Capsule,Intas Pharmaceuticals Ltd,Gastro,2024-01,2027-01,Ward Store (Paeds),40,strip,2024-04-25,Apollo Wholesale Pvt Ltd
B00742,CLC252304,Urimax 0.4 Capsule MR,Tamsulosin (0.4mg),Capsule,Cipla Ltd,Urology,2024-07,2027-07,ICU Store,200,strip,2024-08-10,Kerala Medical Supplies Co.
B00743,TPT245552,Izra 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-02,2028-02,OT Store,150,strip,2025-04-12,Apollo Wholesale Pvt Ltd
B00744,95758349,Azithral 250mg DT Tablet,Azithromycin (250mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-09,2026-03,OPD Pharmacy,120,strip,2024-11-29,Sree Pharma Agencies
B00745,62427912,Dynamox 250mg Capsule,Amoxycillin (250mg),Capsule,Micro Labs Ltd,Antibiotic,2024-08,2026-02,OT Store,40,strip,2024-11-22,"Medline Distributors, Thiruvananthapuram"
B00746,ALX244721,Mupikem Cream,Mupirocin (2% w/w),Cream,Alkem Laboratories Ltd,Dermatology,2025-02,2028-02,OPD Pharmacy,100,tube,2025-03-29,Malabar Pharma Distributors
B00747,MLT247503,Foly-Act Tablet,Folic Acid (5mg),Tablet,Morepen Laboratories Ltd,Haematology,2025-02,2027-02,Main Pharmacy,80,strip,2025-03-08,Kerala Medical Supplies Co.
B00748,71124923,Zifi 200 Tablet,Cefixime (200mg),Tablet,FDC Ltd,Antibiotic,2024-01,2026-06,Emergency Store,150,strip,2024-03-19,Sree Pharma Agencies
B00749,SPT240625,Amx 125mg Tablet,Amoxycillin (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-07,2026-01,OT Store,120,strip,2024-10-22,"Medline Distributors, Thiruvananthapuram"
B00750,I2402-952,Nexiron Injection,Iron Sucrose (100mg/5ml),Injection,Zydus Cadila,Haematology,2024-07,2026-07,OT Store,300,vial/amp,2024-10-25,Sree Pharma Agencies
B00751,SIT256346,Lasix Tablet,Furosemide (40mg),Tablet,Sanofi India Ltd,Cardiovascular,2024-07,2026-01,Ward Store (Paeds),150,strip,2024-09-13,Sree Pharma Agencies
B00752,MLC249223,Dolodol 50mg Capsule,Tramadol (50mg),Capsule,Micro Labs Ltd,Analgesic/Antipyretic,2024-07,2027-07,ICU Store,0,strip,2024-08-01,Kerala Medical Supplies Co.
B00753,CLT241789,Olexa 10mg Tablet,Olanzapine (10mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-03,2027-03,ICU Store,100,strip,2025-05-16,Apollo Wholesale Pvt Ltd
B00754,WB25F234,Drotin A Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Walter Bushnell,Gastro,2024-07,2026-01,ICU Store,40,strip,2024-10-26,Sree Pharma Agencies
B00755,22655004,Pregabid 50 Capsule,Pregabalin (50mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-12,2026-12,ICU Store,80,strip,2024-12-30,Sree Pharma Agencies
B00756,CLI243069,Lumet AT Injection,Artesunate (60mg),Injection,Cipla Ltd,Antimalarial,2024-11,2026-11,OT Store,150,vial/amp,2024-11-29,Malabar Pharma Distributors
B00757,TP25D050,Telday 80 AM Tablet,Telmisartan (80mg) + Amlodipine (5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-04,2027-04,Ward Store (Paeds),0,strip,2025-06-17,"Medline Distributors, Thiruvananthapuram"
B00758,26540343,Solu-Medrol 250mg Injection,Methylprednisolone (250mg),Injection,Pfizer Ltd,Steroid,2025-01,2028-01,Emergency Store,0,vial/amp,2025-01-31,Sanjivani Drug House
B00759,94790150,Flagyl 200 Tablet,Metronidazole (200mg),Tablet,Abbott,Antibiotic,2024-11,2027-11,OPD Pharmacy,300,strip,2024-12-19,"Medline Distributors, Thiruvananthapuram"
B00760,CLI244464,Tranfib 100mg/ml Injection,Tranexamic Acid (500mg),Injection,Cipla Ltd,Haematology,2024-05,2027-05,Main Pharmacy,300,vial/amp,2024-06-26,Sanjivani Drug House
B00761,CLT242276,Thyrocip 100 Tablet,Thyroxine (100mcg),Tablet,Cipla Ltd,Endocrine,2025-01,2028-01,OPD Pharmacy,100,strip,2025-04-04,Kerala Medical Supplies Co.
B00762,CLT244108,Glygard 40mg Tablet,Gliclazide (40mg),Tablet,Cipla Ltd,Diabetes,2024-04,2026-04,Main Pharmacy,10,strip,2024-06-10,Sree Pharma Agencies
B00763,S2507-104,Nam Cold DX Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Lincoln Pharmaceuticals Ltd,Respiratory,2024-03,2026-03,OPD Pharmacy,10,bottle,2024-04-11,Malabar Pharma Distributors
B00764,MP25C174,Omnacortil 0.1% Cream,Methylprednisolone (0.1% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Steroid,2024-07,2026-01,Main Pharmacy,40,tube,2024-10-08,Kerala Medical Supplies Co.
B00765,JBT257604,Rantac 300 Tablet,Ranitidine (300mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-09,2027-09,Main Pharmacy,0,strip,2024-12-17,Apollo Wholesale Pvt Ltd
B00766,10414016,Aziford 200 Oral Suspension,Azithromycin (200mg),Suspension,Leeford Healthcare Ltd,Antibiotic,2025-03,2027-03,OT Store,200,bottle,2025-05-23,Malabar Pharma Distributors
B00767,A24C832,Abtelmi 20 Tablet,Telmisartan (20mg),Tablet,Abbott,Cardiovascular,2024-01,2027-01,Ward Store (Paeds),200,strip,2024-02-23,"Medline Distributors, Thiruvananthapuram"
B00768,RBX254854,Potmeg 1.5gm Oral Solution Sugar Free,Potassium Chloride (1.5gm),Oral Solution,Ridhima Biocare,Anaesthesia/Critical care,2024-02,2027-02,ICU Store,20,bottle,2024-03-31,Sanjivani Drug House
B00769,X2409-647,Tobamist Respules,Tobramycin (300mg),Respules,Cipla Ltd,Ophthalmology,2024-07,2027-07,ICU Store,20,respule,2024-10-17,Apollo Wholesale Pvt Ltd
B00770,SP24M605,Aztor 10 Tablet,Atorvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-05,2028-05,Emergency Store,200,strip,2025-07-15,Sanjivani Drug House
B00771,MPI250296,Nupenta 40mg Injection,Pantoprazole (40mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2024-10,2027-10,Main Pharmacy,150,vial/amp,2025-01-29,Kerala Medical Supplies Co.
B00772,41692245,Dexacip 0.1% Eye Drop,Dexamethasone (0.1% w/v),Eye Drops,Cipla Ltd,Steroid,2024-02,2025-08,OPD Pharmacy,10,bottle,2024-05-30,Malabar Pharma Distributors
B00773,AT241159,Nicopenta 40 Tablet,Pantoprazole (40mg),Tablet,Abbott,Gastro,2024-11,2026-11,OT Store,10,strip,2024-12-03,Kerala Medical Supplies Co.
B00774,LL25J793,Ciprolup 250mg Tablet,Ciprofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-03,2026-03,OPD Pharmacy,10,strip,2024-05-07,Apollo Wholesale Pvt Ltd
B00775,TP24F979,Mofee Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Torrent Pharmaceuticals Ltd,Ophthalmology,2025-02,2026-08,Emergency Store,50,bottle,2025-04-12,Apollo Wholesale Pvt Ltd
B00776,SP24G530,Glytears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2024-07,2026-07,Emergency Store,200,bottle,2024-09-24,Malabar Pharma Distributors
B00777,10586580,Senorm LA Injection,Haloperidol Decanoate (50mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-05,2027-05,OPD Pharmacy,20,vial/amp,2024-06-18,Kerala Medical Supplies Co.
B00778,ML24J053,Atepres 50mg Tablet,Atenolol (50mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-06,2025-12,Main Pharmacy,80,strip,2024-08-17,Sree Pharma Agencies
B00779,IPX259241,Genfour 0.5% Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2024-12,2026-12,ICU Store,30,bottle,2025-03-24,Apollo Wholesale Pvt Ltd
B00780,T2406-867,Olmecip 20 Tablet,Olmesartan Medoxomil (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-03,2026-03,Ward Store (Paeds),200,strip,2024-05-30,Sree Pharma Agencies
B00781,T2506-604,Ativan 2mg Tablet,Lorazepam (2mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2025-04,2028-04,Ward Store (Paeds),300,strip,2025-07-15,Sanjivani Drug House
B00782,T2411-776,Telday 20 Tablet,Telmisartan (20mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-01,2027-01,Main Pharmacy,200,strip,2024-04-24,Apollo Wholesale Pvt Ltd
B00783,T2508-812,Emeset 4 ODT Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-09,2027-09,ICU Store,10,strip,2024-09-28,Sree Pharma Agencies
B00784,11055770,Doloban 100mg Tablet SR,Diclofenac (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-09,2026-09,ICU Store,40,strip,2024-11-15,"Medline Distributors, Thiruvananthapuram"
B00785,86391152,Aceflam P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Micro Labs Ltd,Analgesic/Antipyretic,2024-11,2027-11,Main Pharmacy,30,strip,2024-12-12,Malabar Pharma Distributors
B00786,ZCT251529,Gertum 250mg Tablet,Cefuroxime (250mg),Tablet,Zydus Cadila,Antibiotic,2024-11,2026-11,Ward Store (Paeds),20,strip,2024-12-09,Malabar Pharma Distributors
B00787,IP25K601,Emenorm 10mg Tablet,Metoclopramide (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-04,2027-04,OT Store,200,strip,2024-07-26,Kerala Medical Supplies Co.
B00788,IPI250170,Dorinta 20mg Injection,Drotaverine (20mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2024-04,2027-04,Main Pharmacy,30,vial/amp,2024-07-02,Sree Pharma Agencies
B00789,AL25J984,Gemcal-D3 Tablet,Calcium (500mg) + Vitamin D3 (500IU),Tablet,Alkem Laboratories Ltd,Supplement,2024-04,2025-10,Ward Store (Paeds),120,strip,2024-07-16,Apollo Wholesale Pvt Ltd
B00790,SP24E277,Roles 10mg Tablet,Rabeprazole (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-04,2028-04,ICU Store,20,strip,2025-05-22,"Medline Distributors, Thiruvananthapuram"
B00791,22539199,Glaritus 100IU/ml Injection,Insulin Glargine (100IU),Injection,Wockhardt Ltd,Diabetes,2024-06,2026-06,OPD Pharmacy,100,vial/amp,2024-08-29,Malabar Pharma Distributors
B00792,30284415,Meftal 250mg Tablet DT,Mefenamic Acid (250mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2024-08,2026-08,Main Pharmacy,150,strip,2024-11-23,"Medline Distributors, Thiruvananthapuram"
B00793,SP25D967,Aqsusten 25 Solution for Injection,Progesterone (Natural Micronized) (25mg),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2025-02,2028-02,Main Pharmacy,0,vial/amp,2025-05-29,Sanjivani Drug House
B00794,TPT244740,Nexpro 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-09,2026-03,Emergency Store,150,strip,2024-12-21,Apollo Wholesale Pvt Ltd
B00795,IR24H388,Vancobest 500mg Injection,Vancomycin (500mg),Injection,Ikon Remedies Pvt Ltd,Antibiotic,2024-10,2026-04,Main Pharmacy,120,vial/amp,2024-12-26,Malabar Pharma Distributors
B00796,SPI254172,Oframax 125mg Injection,Ceftriaxone (125mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2027-01,Emergency Store,80,vial/amp,2024-03-13,Malabar Pharma Distributors
B00797,TPI242947,Dopacin 40mg Injection,Dopamine (40mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-09,2027-09,Emergency Store,300,vial/amp,2024-09-30,Malabar Pharma Distributors
B00798,CL24J067,Cofenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-01,2027-01,OT Store,40,strip,2024-03-16,Sanjivani Drug House
B00799,IP24F802,Misolog 200mcg Tablet,Misoprostol (200mcg),Tablet,Intas Pharmaceuticals Ltd,Obstetrics,2024-04,2026-04,Emergency Store,150,strip,2024-07-19,Malabar Pharma Distributors
B00800,LHT253973,Dailyglim 1000mg Tablet SR,Metformin (1000mg),Tablet,Leeford Healthcare Ltd,Diabetes,2024-03,2025-09,OT Store,300,strip,2024-05-15,Malabar Pharma Distributors
B00801,T2407-145,Ivrix 12 Tablet DT,Ivermectin (12mg),Tablet,Cipla Ltd,Anthelmintic,2024-03,2026-03,Emergency Store,10,strip,2024-05-25,Malabar Pharma Distributors
B00802,S2502-564,Cefinta 50mg Dry Syrup,Cefixime (50mg),Syrup,Intas Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,OT Store,40,bottle,2025-06-27,Malabar Pharma Distributors
B00803,SI24D540,Clexane 20mg Injection,Enoxaparin (20mg),Injection,Sanofi India Ltd,Anticoagulant,2024-11,2027-11,OT Store,120,vial/amp,2025-01-11,Malabar Pharma Distributors
B00804,I2512-874,Magnesium Sulphate 0.25% Injection,Magnesium Sulphate (25% w/v),Injection,Hindustan Antibiotics Ltd,Anaesthesia/Critical care,2025-04,2028-04,OT Store,0,vial/amp,2025-07-15,Sanjivani Drug House
B00805,DRT244165,Stamlo 5 Tablet,Amlodipine (5mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-06,2026-06,Emergency Store,120,strip,2024-09-04,Malabar Pharma Distributors
B00806,CLT258752,Tenepla Tablet,Teneligliptin (20mg),Tablet,Cipla Ltd,Diabetes,2024-10,2026-10,OT Store,20,strip,2024-12-16,Sree Pharma Agencies
B00807,SPX248840,Fucidin Cream,Fusidic Acid (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-05,2026-05,OT Store,300,tube,2024-06-05,Sanjivani Drug House
B00808,SP25F287,Silver Sulfadiazine Cream,Silver Sulfadiazine (NA),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-08,2026-02,OT Store,300,tube,2024-10-17,Sree Pharma Agencies
B00809,T2510-030,Zovirax 400 Tablet,Acyclovir (400mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2024-02,2026-02,OPD Pharmacy,200,strip,2024-05-23,Apollo Wholesale Pvt Ltd
B00810,LH24F994,Alcipan 40mg Tablet,Pantoprazole (40mg),Tablet,Leeford Healthcare Ltd,Gastro,2024-03,2026-03,ICU Store,10,strip,2024-04-08,Malabar Pharma Distributors
B00811,18022803,Lupisolone 4mg Tablet,Methylprednisolone (4mg),Tablet,Lupin Ltd,Steroid,2024-01,2027-01,Ward Store (Paeds),200,strip,2024-02-07,Sanjivani Drug House
B00812,X2507-031,Levobact 0.5% Eye Drop,Levofloxacin (0.5%),Eye Drops,Micro Labs Ltd,Antibiotic,2024-03,2026-03,ICU Store,20,bottle,2024-04-09,Apollo Wholesale Pvt Ltd
B00813,DP2143,Flagorin Injection (Heparin 5000 IU/ml),Heparin (5000IU/ml),Injection,Divine Laboratories Pvt. Ltd.,Anticoagulant,2022-08,2025-06,Main Pharmacy,0,vial/amp,2022-11-23,Sree Pharma Agencies
B00814,C2503-800,Mox 500mg Capsule,Amoxycillin (500mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2026-02,Main Pharmacy,120,strip,2024-05-03,Sree Pharma Agencies
B00815,SPT254562,Corpril 1.25mg Tablet,Ramipril (1.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-08,2026-08,Emergency Store,60,strip,2024-11-06,Sree Pharma Agencies
B00816,T2506-317,Amipace 100 Tablet,Amiodarone (100mg),Tablet,Lupin Ltd,Cardiovascular,2025-04,2026-10,Emergency Store,0,strip,2025-05-20,Malabar Pharma Distributors
B00817,LL25K847,Glador 1 Tablet,Glimepiride (1mg),Tablet,Lupin Ltd,Diabetes,2024-03,2027-03,Emergency Store,200,strip,2024-05-03,"Medline Distributors, Thiruvananthapuram"
B00818,TP25B175,Metocard XL 100 Tablet,Metoprolol Succinate (95mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-01,2027-01,OPD Pharmacy,50,strip,2025-02-02,Malabar Pharma Distributors
B00819,T2401-391,Domel 10mg Tablet,Domperidone (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-04,2027-04,OPD Pharmacy,0,strip,2024-06-11,"Medline Distributors, Thiruvananthapuram"
B00820,C2512-102,Racedot 100mg Capsule,Racecadotril (100mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Gastro,2024-02,2026-02,Emergency Store,150,strip,2024-03-31,Kerala Medical Supplies Co.
B00821,SPX257725,Fucidin Cream,Fusidic Acid (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-02,2027-02,OPD Pharmacy,30,tube,2024-04-26,Sree Pharma Agencies
B00822,39387314,Monoloc 150mg Tablet,Ranitidine (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-05,2026-11,OPD Pharmacy,80,strip,2025-06-26,"Medline Distributors, Thiruvananthapuram"
B00823,I2506-987,Troypofol 10mg Injection,Propofol (10mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-03,2025-09,Ward Store (Paeds),200,vial/amp,2024-05-19,Malabar Pharma Distributors
B00824,AV253256,Floxip 100mg Infusion,Ciprofloxacin (100mg),Infusion,Abbott,Antibiotic,2024-10,2027-10,OT Store,150,bottle,2025-01-12,"Medline Distributors, Thiruvananthapuram"
B00825,MPT243231,Levomac 250 Tablet,Levofloxacin (250mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-06,2027-06,ICU Store,300,strip,2024-09-26,Sanjivani Drug House
B00826,X2501-911,Itchderm 1% Dusting Powder,Clotrimazole (1% w/w),Powder,Zydus Cadila,Antifungal,2024-06,2025-12,Ward Store (Paeds),0,pack,2024-08-25,Sree Pharma Agencies
B00827,CLT247953,Dilpres 50mg Tablet,Atenolol (50mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2028-01,OT Store,100,strip,2025-02-24,Kerala Medical Supplies Co.
B00828,SPT253658,Alzolam 0.125mg Tablet,Alprazolam (0.125mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-04,2025-10,OPD Pharmacy,200,strip,2024-05-13,"Medline Distributors, Thiruvananthapuram"
B00829,ZHI255059,Zu-C Injection,Vitamin C (100mg),Injection,Zuventus Healthcare Ltd,Supplement,2024-01,2027-01,ICU Store,10,vial/amp,2024-04-24,Sree Pharma Agencies
B00830,APT241503,Azithral 250mg DT Tablet,Azithromycin (250mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,Main Pharmacy,80,strip,2025-07-15,Sanjivani Drug House
B00831,TPT244923,Telday-H Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-09,Emergency Store,300,strip,2024-09-28,Kerala Medical Supplies Co.
B00832,AT254772,CAAT 10 Tablet,Atorvastatin (10mg),Tablet,Abbott,Cardiovascular,2024-01,2027-01,ICU Store,80,strip,2024-04-18,Malabar Pharma Distributors
B00833,95061828,Gluconorm SR 1gm Tablet,Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2025-03,2028-03,ICU Store,150,strip,2025-04-28,Apollo Wholesale Pvt Ltd
B00834,SIF2736A,Rosuvas F 20 Tablet,Fenofibrate (160mg) + Rosuvastatin (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2027-05,Ward Store (Paeds),120,strip,2025-01-24,Sree Pharma Agencies
B00835,APS256711,Zeet 12 Oral Suspension,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Alembic Pharmaceuticals Ltd,Respiratory,2024-04,2027-04,Ward Store (Paeds),60,bottle,2024-05-29,"Medline Distributors, Thiruvananthapuram"
B00836,MLI255568,Spasypen 10mg Injection,Dicyclomine (10mg),Injection,Morepen Laboratories Ltd,Gastro,2024-06,2025-12,OPD Pharmacy,10,vial/amp,2024-08-05,Sanjivani Drug House
B00837,67930109,Rosupil 10mg Tablet,Rosuvastatin (10mg),Tablet,Zydus Cadila,Cardiovascular,2024-03,2025-09,ICU Store,300,strip,2024-06-23,Apollo Wholesale Pvt Ltd
B00838,66638517,Lukotas 3D Tablet,Montelukast (10mg) + Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2024-05,2027-05,ICU Store,30,strip,2024-08-22,Sanjivani Drug House
B00839,AL24H029,Remtrex 15mg Injection,Methotrexate (15mg),Injection,Alkem Laboratories Ltd,Oncology,2024-04,2026-04,ICU Store,50,vial/amp,2024-06-11,Malabar Pharma Distributors
B00840,SP24E184,Susten 100 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-12,2026-06,OPD Pharmacy,40,vial/amp,2025-01-02,Malabar Pharma Distributors
B00841,SPT258823,Cepoxim XP 500 mg/125 mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-03,2027-03,Main Pharmacy,50,strip,2025-05-22,Apollo Wholesale Pvt Ltd
B00842,SP24E043,Clopilet A 150 Capsule,Aspirin (150mg) + Clopidogrel (75mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-03,2026-09,Emergency Store,30,strip,2025-04-30,Kerala Medical Supplies Co.
B00843,85833309,Galvus Met 50mg/500mg Tablet,Metformin (500mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2025-02,2027-02,OPD Pharmacy,200,strip,2025-03-29,Kerala Medical Supplies Co.
B00844,SP24K022,Acostin 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2026-01,Ward Store (Paeds),50,vial/amp,2024-02-28,Sanjivani Drug House
B00845,47026058,Fluvia 75mg Capsule,Oseltamivir Phosphate (75mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Antiviral,2025-01,2026-07,Emergency Store,150,strip,2025-02-27,Kerala Medical Supplies Co.
B00846,53712198,Flucobig 150mg Tablet,Fluconazole (150mg),Tablet,Torrent Pharmaceuticals Ltd,Antifungal,2024-07,2026-07,Ward Store (Paeds),80,strip,2024-09-30,Sanjivani Drug House
B00847,T2408-613,Istamet XR Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-12,2027-12,OT Store,120,strip,2025-02-25,Sanjivani Drug House
B00848,74212086,AMANAT 10MG TABLET,Amlodipine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-08,2026-02,Main Pharmacy,0,strip,2024-09-23,Malabar Pharma Distributors
B00849,ELI243941,Xsulin 30/70 Suspension for Injection,Human insulin (40IU),Injection,Eris Lifesciences Ltd,Diabetes,2024-04,2027-04,Emergency Store,120,vial/amp,2024-05-17,Sanjivani Drug House
B00850,RKI251779,Glumig Injection,Calcium Gluconate (10mg),Injection,RSM Kilitch Pharma Pvt Ltd,Anaesthesia/Critical care,2024-04,2026-04,OT Store,100,vial/amp,2024-07-29,Apollo Wholesale Pvt Ltd
B00851,S2403-625,Bioprim Syrup,Sulfamethoxazole (200mg) + Trimethoprim (40mg),Syrup,Zydus Cadila,Antibiotic,2024-03,2026-03,Main Pharmacy,100,bottle,2024-06-13,Sanjivani Drug House
B00852,ZC24F576,Dexona Injection,Dexamethasone (4mg/ml),Injection,Zydus Cadila,Steroid,2024-05,2025-11,OT Store,10,vial/amp,2024-07-01,Sanjivani Drug House
B00853,IP24L112,Olmark 10 Tablet,Olmesartan Medoxomil (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-11,2027-11,ICU Store,40,strip,2025-01-01,Sanjivani Drug House
B00854,I2511-510,Tranfib 100mg/ml Injection,Tranexamic Acid (500mg),Injection,Cipla Ltd,Haematology,2024-09,2027-09,Ward Store (Paeds),200,vial/amp,2024-10-18,"Medline Distributors, Thiruvananthapuram"
B00855,I2409-112,Folitrax 15 Injection,Methotrexate (15mg/ml),Injection,Ipca Laboratories Ltd,Oncology,2024-06,2027-06,Main Pharmacy,80,vial/amp,2024-08-22,Sree Pharma Agencies
B00856,10475894,Glycomet 1gm Tablet SR,Metformin (1000mg),Tablet,USV Ltd,Diabetes,2024-02,2027-02,OPD Pharmacy,300,strip,2024-04-08,Malabar Pharma Distributors
B00857,68507072,Jupiros 10 Tablet,Rosuvastatin (10mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-06,2025-12,OT Store,150,strip,2024-08-20,Apollo Wholesale Pvt Ltd
B00858,T2403-855,Bruriff 400mg Tablet,Ibuprofen (400mg),Tablet,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-11,2027-11,OT Store,60,strip,2025-01-10,Sree Pharma Agencies
B00859,KP24A169,Telmamet AM Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Kantil Pharmaceuticals Pvt. Ltd.,Cardiovascular,2024-10,2026-10,ICU Store,60,strip,2024-11-19,"Medline Distributors, Thiruvananthapuram"
B00860,SII244819,Clexane 20mg Injection,Enoxaparin (20mg),Injection,Sanofi India Ltd,Anticoagulant,2025-01,2027-01,OT Store,200,vial/amp,2025-03-23,"Medline Distributors, Thiruvananthapuram"
B00861,16808353,Betadine 5 % Solution,Povidone Iodine (5% w/v),Solution,Win-Medicare Pvt Ltd,Dermatology,2024-05,2027-05,OT Store,0,bottle,2024-06-11,Malabar Pharma Distributors
B00862,72207767,Clindac A 1% Gel,Clindamycin (1% w/w),Gel,Alkem Laboratories Ltd,Antibiotic,2024-04,2026-04,Main Pharmacy,30,tube,2024-07-25,Apollo Wholesale Pvt Ltd
B00863,ZCI253707,Germero 1000mg Injection,Meropenem (1000mg),Injection,Zydus Cadila,Antibiotic,2024-11,2026-05,ICU Store,30,vial/amp,2025-02-20,Apollo Wholesale Pvt Ltd
B00864,LL24D088,Manilup 20% Infusion,Mannitol (20% w/v),Infusion,Lupin Ltd,Anaesthesia/Critical care,2025-04,2027-04,Emergency Store,120,bottle,2025-06-25,Kerala Medical Supplies Co.
B00865,GPT251227,Telma H Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-09,ICU Store,50,strip,2024-10-27,Sree Pharma Agencies
B00866,CL24G851,Cefix 100 Tablet,Cefixime (100mg),Tablet,Cipla Ltd,Antibiotic,2024-10,2026-10,OT Store,50,strip,2024-11-14,Apollo Wholesale Pvt Ltd
B00867,PL24K495,Wysolone 10 Tablet DT,Prednisolone (10mg),Tablet,Pfizer Ltd,Steroid,2025-01,2028-01,Emergency Store,150,strip,2025-02-28,Sanjivani Drug House
B00868,A25C882,Duphalac Fiber Oral Solution,Lactulose (2.5gm/5ml),Oral Solution,Abbott,Gastro,2024-05,2025-11,ICU Store,0,bottle,2024-07-02,Sanjivani Drug House
B00869,ZCT258019,Biodexone 4 Tablet,Dexamethasone (4mg),Tablet,Zydus Cadila,Steroid,2024-02,2025-08,Ward Store (Paeds),150,strip,2024-03-03,"Medline Distributors, Thiruvananthapuram"
B00870,T2405-880,Epsolin ER 200 Tablet,Phenytoin (200mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-08,2026-02,Main Pharmacy,40,strip,2024-11-17,Sree Pharma Agencies
B00871,50836843,Gemcal-D3 Tablet,Calcium (500mg) + Vitamin D3 (500IU),Tablet,Alkem Laboratories Ltd,Supplement,2025-02,2026-08,Main Pharmacy,300,strip,2025-03-04,Sree Pharma Agencies
B00872,TPT247034,VASOTRATE 10MG TABLET,Isosorbide Mononitrate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-09,Emergency Store,10,strip,2024-11-19,Kerala Medical Supplies Co.
B00873,AL24D815,Aldom 20mg Tablet DT,Domperidone (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-11,2026-11,OPD Pharmacy,50,strip,2024-11-27,Kerala Medical Supplies Co.
B00874,65289687,Embeta 25 Tablet,Metoprolol Tartrate (25mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,Ward Store (Paeds),10,strip,2024-11-16,Apollo Wholesale Pvt Ltd
B00875,57621071,Combiflam Tablet,Ibuprofen (400mg) + Paracetamol (325mg),Tablet,Sanofi India Ltd,Analgesic/Antipyretic,2024-04,2027-04,OPD Pharmacy,20,strip,2024-05-18,Sanjivani Drug House
B00876,41872495,Fentoin 100mg Tablet ER,Phenytoin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-06,2026-06,OPD Pharmacy,50,strip,2024-07-06,Kerala Medical Supplies Co.
B00877,CLT259697,Restyl 1mg Tablet,Alprazolam (1mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-04,2027-04,OPD Pharmacy,10,strip,2024-05-15,Apollo Wholesale Pvt Ltd
B00878,52302682,Duphalac Oral Solution Lemon,Lactulose (3.335gm/5ml),Oral Solution,Abbott,Gastro,2024-08,2027-08,OT Store,30,bottle,2024-11-09,Kerala Medical Supplies Co.
B00879,MP25C980,Paragreat 250mg Suspension,Paracetamol (250mg),Suspension,Mankind Pharma Ltd,Analgesic/Antipyretic,2025-02,2026-08,OPD Pharmacy,50,bottle,2025-04-25,"Medline Distributors, Thiruvananthapuram"
B00880,CLT247836,Norflox 400 Tablet,Norfloxacin (400mg) + Lactobacillus (120Million spores),Tablet,Cipla Ltd,Other,2025-01,2028-01,Main Pharmacy,100,strip,2025-02-19,Malabar Pharma Distributors
B00881,T2406-830,Thyronorm 125mcg Tablet,Thyroxine (125mcg),Tablet,Abbott,Endocrine,2024-10,2027-10,OT Store,40,strip,2025-01-13,Kerala Medical Supplies Co.
B00882,JPT259754,Naari Cal Tablet,Calcium Citrate Malate (1000mg) + Vitamin D3 (100IU),Tablet,Jagsonpal Pharmaceuticals Ltd,Supplement,2025-03,2028-03,OT Store,200,strip,2025-04-18,"Medline Distributors, Thiruvananthapuram"
B00883,SPX259286,Susten 100 Soft Gelatin Capsule,Progesterone (Natural Micronized) (100mg),Gel,Sun Pharmaceutical Industries Ltd,Obstetrics,2025-02,2027-02,Main Pharmacy,0,tube,2025-05-28,Sree Pharma Agencies
B00884,T2510-875,Olymprix Tablet,Teneligliptin (20mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-10,2027-10,ICU Store,60,strip,2024-12-22,"Medline Distributors, Thiruvananthapuram"
B00885,11562947,Zovirax 800 Tablet,Acyclovir (800mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2025-03,2028-03,Emergency Store,20,strip,2025-06-16,Apollo Wholesale Pvt Ltd
B00886,T2509-670,Izra 40 Tablet,Esomeprazole (40mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-08,2026-08,ICU Store,0,strip,2024-11-26,Sanjivani Drug House
B00887,IPT254839,Intacoxia 120 Tablet,Etoricoxib (120mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-02,2025-08,Main Pharmacy,20,strip,2024-05-19,"Medline Distributors, Thiruvananthapuram"
B00888,ALC247130,Gabata 400mg Capsule,Gabapentin (400mg),Capsule,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-09,2026-03,ICU Store,10,strip,2024-12-01,Sanjivani Drug House
B00889,SPC243665,CARDICAP 40MG CAPSULE TR,Isosorbide Dinitrate (40mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-10,2026-10,Ward Store (Paeds),100,strip,2024-12-15,Malabar Pharma Distributors
B00890,18545050,Dolodol 50mg Capsule,Tramadol (50mg),Capsule,Micro Labs Ltd,Analgesic/Antipyretic,2024-11,2026-11,Main Pharmacy,60,strip,2025-01-08,Sanjivani Drug House
B00891,T2506-930,Euclide 40 Tablet,Gliclazide (40mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-08,2026-08,Emergency Store,120,strip,2024-11-12,Sree Pharma Agencies
B00892,T2505-901,Ciptab 250mg Tablet,Ciprofloxacin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2025-01,2027-01,ICU Store,40,strip,2025-04-20,Apollo Wholesale Pvt Ltd
B00893,13438797,Labepure 20mg Injection,Labetalol (20mg),Injection,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-12,2026-12,Emergency Store,80,vial/amp,2025-01-29,Kerala Medical Supplies Co.
B00894,I2507-494,Recosulin N 100IU Injection,Insulin Isophane (100IU),Injection,Shreya Life Sciences Pvt Ltd,Diabetes,2025-03,2026-09,Emergency Store,150,vial/amp,2025-04-11,Sree Pharma Agencies
B00895,EP24A246,Pause 1000mg Tablet,Tranexamic Acid (1000mg),Tablet,Emcure Pharmaceuticals Ltd,Haematology,2024-11,2026-11,ICU Store,40,strip,2024-12-30,Kerala Medical Supplies Co.
B00896,T2501-796,Amlovas 2.5 Tablet,Amlodipine (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-02,2027-02,OT Store,100,strip,2024-04-08,"Medline Distributors, Thiruvananthapuram"
B00897,T2405-373,Esomac 20 Tablet,Esomeprazole (20mg),Tablet,Cipla Ltd,Gastro,2024-01,2026-01,ICU Store,120,strip,2024-02-06,Apollo Wholesale Pvt Ltd
B00898,A25J760,Linoplus 2mg/ml Infusion,Linezolid (2mg/ml),Infusion,Abbott,Antibiotic,2024-04,2027-04,Main Pharmacy,100,bottle,2024-05-11,Sanjivani Drug House
B00899,SPI242030,Aqsusten 25 Solution for Injection,Progesterone (Natural Micronized) (25mg),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-07,2027-07,OT Store,120,vial/amp,2024-10-12,Apollo Wholesale Pvt Ltd
B00900,A25J226,Duphalac Fiber Oral Solution,Lactulose (2.5gm/5ml),Oral Solution,Abbott,Gastro,2024-06,2027-06,OT Store,20,bottle,2024-09-18,Sree Pharma Agencies
B00901,I2409-403,Amikef 100mg Injection,Amikacin (100mg),Injection,Lupin Ltd,Antibiotic,2025-05,2028-05,OT Store,300,vial/amp,2025-07-13,Malabar Pharma Distributors
B00902,94399027,Amicip 100mg Injection,Amikacin (100mg),Injection,Cipla Ltd,Antibiotic,2024-06,2027-06,ICU Store,30,vial/amp,2024-06-27,Kerala Medical Supplies Co.
B00903,ZCI241943,Xylocaine 4% Injection,Lidocaine (4%),Injection,Zydus Cadila,Other,2024-05,2027-05,OT Store,60,vial/amp,2024-08-19,Kerala Medical Supplies Co.
B00904,HHT258764,Levocet 10mg Tablet,Levocetirizine (10mg),Tablet,Hetero Healthcare Limited,Respiratory,2024-11,2026-11,OPD Pharmacy,200,strip,2024-12-12,"Medline Distributors, Thiruvananthapuram"
B00905,CLV253991,Levoflox 500 Infusion,Levofloxacin (500mg),Infusion,Cipla Ltd,Antibiotic,2024-12,2027-12,ICU Store,120,bottle,2025-02-20,Malabar Pharma Distributors
B00906,I2505-283,Resner 500mcg Injection,Methylcobalamin (500mcg),Injection,Lupin Ltd,Supplement,2025-03,2028-03,OPD Pharmacy,0,vial/amp,2025-04-16,Malabar Pharma Distributors
B00907,ALT258770,Losaral 50mg Tablet,Losartan (50mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-01,2026-01,Emergency Store,200,strip,2024-02-10,Sanjivani Drug House
B00908,LLT244376,Thyrodip 10mg Tablet,Carbimazole (10mg),Tablet,Lupin Ltd,Endocrine,2024-12,2026-12,OPD Pharmacy,100,strip,2025-03-20,Sree Pharma Agencies
B00909,CL24E750,Dalcinex 150mg Injection,Clindamycin (150mg),Injection,Cipla Ltd,Antibiotic,2024-03,2027-03,ICU Store,120,vial/amp,2024-05-12,Apollo Wholesale Pvt Ltd
B00910,MLI256474,Dexapen 4mg Injection,Dexamethasone (4mg),Injection,Morepen Laboratories Ltd,Steroid,2024-08,2027-08,OPD Pharmacy,80,vial/amp,2024-08-29,Kerala Medical Supplies Co.
B00911,68166960,Merenz 1000mg Injection,Meropenem (1000mg),Injection,Lupin Ltd,Antibiotic,2024-12,2026-12,Emergency Store,200,vial/amp,2025-01-07,Kerala Medical Supplies Co.
B00912,TPI251687,Ultiblast 1gm Injection,Meropenem (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-06,2027-06,OT Store,40,vial/amp,2024-07-25,Kerala Medical Supplies Co.
B00913,SI25B905,Lasix Tablet,Furosemide (40mg),Tablet,Sanofi India Ltd,Cardiovascular,2025-01,2027-01,Emergency Store,10,strip,2025-03-23,Apollo Wholesale Pvt Ltd
B00914,SII249148,Clexane 20mg Injection (0.2ml Each),Enoxaparin (20mg),Injection,Sanofi India Ltd,Anticoagulant,2024-12,2026-12,OPD Pharmacy,10,vial/amp,2025-02-16,"Medline Distributors, Thiruvananthapuram"
B00915,86261289,Amx 125mg Tablet,Amoxycillin (125mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2026-03,Emergency Store,300,strip,2024-06-14,Sanjivani Drug House
B00916,GSS245413,Calpol 250mg Paediatric Oral Suspension Strawberry,Paracetamol (250mg/5ml),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-08,2027-08,Main Pharmacy,30,bottle,2024-09-02,Kerala Medical Supplies Co.
B00917,T2404-732,Cardipin 20mg Tablet,Nifedipine (20mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,OPD Pharmacy,10,strip,2024-08-17,Sree Pharma Agencies
B00918,GST259677,Calpol 250mg Tablet,Paracetamol (250mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2027-03,OT Store,120,strip,2025-05-19,Kerala Medical Supplies Co.
B00919,LLT249032,Defidin 5mg Tablet,Amlodipine (5mg),Tablet,Lupin Ltd,Cardiovascular,2025-01,2027-01,ICU Store,40,strip,2025-03-04,Sanjivani Drug House
B00920,ZC24C608,Nexiron Injection,Iron Sucrose (100mg/5ml),Injection,Zydus Cadila,Haematology,2024-06,2026-06,OPD Pharmacy,40,vial/amp,2024-09-19,Malabar Pharma Distributors
B00921,LL24C812,Meflup 250mg Tablet,Mefenamic Acid (250mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-05,2027-05,Main Pharmacy,60,strip,2025-07-15,Kerala Medical Supplies Co.
B00922,CL24F365,Diacip 500mg Tablet,Metformin (500mg),Tablet,Cipla Ltd,Diabetes,2024-09,2027-09,OT Store,10,strip,2024-10-10,Kerala Medical Supplies Co.
B00923,CLC243187,IBUGESIC 300MG CAPSULE SR,Ibuprofen (300mg),Capsule,Cipla Ltd,Analgesic/Antipyretic,2024-11,2026-05,Ward Store (Paeds),120,strip,2025-02-05,Sanjivani Drug House
B00924,86133355,Halo 5mg Capsule,Haloperidol (5mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-04,2027-04,ICU Store,20,strip,2025-06-24,"Medline Distributors, Thiruvananthapuram"
B00925,CPI258341,Dianora 1mg Injection,Adrenaline (1mg),Injection,Cachet Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-05,2025-11,OT Store,80,vial/amp,2024-07-16,"Medline Distributors, Thiruvananthapuram"
B00926,LLT254989,Prednolone 5mg Tablet,Prednisolone (5mg),Tablet,Lupin Ltd,Steroid,2024-04,2026-04,OT Store,120,strip,2024-06-03,Apollo Wholesale Pvt Ltd
B00927,17188130,Ketorol Injection,Ketorolac (30mg),Injection,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-11,2027-11,OPD Pharmacy,50,vial/amp,2024-12-08,Sree Pharma Agencies
B00928,98032908,Deplatt 150 Tablet,Clopidogrel (150mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-03,2027-03,OPD Pharmacy,200,strip,2024-04-11,Sree Pharma Agencies
B00929,IRI252259,Hepatag 25000IU Injection,Heparin (25000IU),Injection,Ikon Remedies Pvt Ltd,Anticoagulant,2024-11,2026-11,Emergency Store,20,vial/amp,2024-12-01,Kerala Medical Supplies Co.
B00930,MPC249632,Macox 300mg Capsule,Rifampicin (300mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2024-03,2026-03,Ward Store (Paeds),100,strip,2024-05-04,Malabar Pharma Distributors
B00931,64523392,Tamica-H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-01,2028-01,ICU Store,300,strip,2025-04-11,Sanjivani Drug House
B00932,T2403-513,Nuloc 20mg Tablet,Rabeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-01,2026-01,OT Store,50,strip,2024-03-06,Malabar Pharma Distributors
B00933,BPI240160,Biospas 10mg Injection,Dicyclomine (10mg),Injection,Biochem Pharmaceutical Industries,Gastro,2025-04,2026-10,Main Pharmacy,50,vial/amp,2025-07-08,Malabar Pharma Distributors
B00934,CLS241280,Cefoprox 100mg Dry Syrup,Cefpodoxime Proxetil (100mg/5ml),Syrup,Cipla Ltd,Antibiotic,2024-07,2027-07,OT Store,30,bottle,2024-09-18,Malabar Pharma Distributors
B00935,IP25C122,Ceroxitum 1500mg Injection,Cefuroxime (1500mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-06,2027-06,Main Pharmacy,300,vial/amp,2024-07-09,Sree Pharma Agencies
B00936,LLT241664,Glador M 1 Forte Tablet PR,Glimepiride (1mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2024-03,2027-03,OPD Pharmacy,100,strip,2024-04-02,Kerala Medical Supplies Co.
B00937,IPI240952,Ceroxitum 1500mg Injection,Cefuroxime (1500mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-06,2027-06,OT Store,50,vial/amp,2024-09-20,Sanjivani Drug House
B00938,V2504-595,Metrokem IV 100mg Infusion,Metronidazole (100mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-07,2026-01,OPD Pharmacy,50,bottle,2024-09-29,Sanjivani Drug House
B00939,TP24L968,Ritebeat 100mg Tablet,Amiodarone (100mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-01,2027-01,Ward Store (Paeds),150,strip,2024-02-21,Sanjivani Drug House
B00940,SP24H616,Rosuvas 10mg Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2027-03,Main Pharmacy,60,strip,2024-05-19,Malabar Pharma Distributors
B00941,ZL24H205,Aldex 6mg Tablet SR,Dexchlorpheniramine (6mg),Tablet,Zee Laboratories,Anti-allergic,2024-12,2026-12,Main Pharmacy,20,strip,2025-02-03,Sree Pharma Agencies
B00942,FLX241010,Zioral Drops,Zinc Gluconate (20mg),Drops,FDC Ltd,Supplement,2024-10,2027-10,OT Store,40,bottle,2024-12-20,Apollo Wholesale Pvt Ltd
B00943,57570364,Ciplox 2mg Injection,Ciprofloxacin (2mg),Injection,Cipla Ltd,Antibiotic,2024-08,2026-02,OPD Pharmacy,30,vial/amp,2024-10-20,Apollo Wholesale Pvt Ltd
B00944,59597995,Erkacin 100mg Injection,Amikacin (100mg),Injection,Micro Labs Ltd,Antibiotic,2024-08,2027-08,Ward Store (Paeds),120,vial/amp,2024-08-29,Sree Pharma Agencies
B00945,EW24D313,Cofarin 1mg Tablet,Warfarin (1mg),Tablet,East West Pharma,Anticoagulant,2025-01,2028-01,Main Pharmacy,20,strip,2025-04-20,Sanjivani Drug House
B00946,T2403-230,Amlovas 2.5 Tablet,Amlodipine (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-12,2026-06,ICU Store,50,strip,2025-03-16,Malabar Pharma Distributors
B00947,MPT249936,Presdown 40mg Tablet,Telmisartan (40mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2025-05,2027-05,Emergency Store,120,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B00948,SP24E338,Istamet 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-02,2026-02,OPD Pharmacy,200,strip,2024-05-13,Apollo Wholesale Pvt Ltd
B00949,T2505-597,Cresar 80H Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-11,2026-05,Emergency Store,60,strip,2024-12-17,Malabar Pharma Distributors
B00950,SPT244944,Alzolam 0.125mg Tablet,Alprazolam (0.125mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-04,2028-04,Ward Store (Paeds),30,strip,2025-06-10,Sanjivani Drug House
B00951,LL25K851,E Cef 100mg Tablet DT,Cefixime (100mg),Tablet,Lupin Ltd,Antibiotic,2024-02,2026-02,Emergency Store,10,strip,2024-04-28,Kerala Medical Supplies Co.
B00952,CLX246344,Budecort 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Cipla Ltd,Respiratory,2024-04,2026-04,OT Store,300,respule,2024-06-16,Sanjivani Drug House
B00953,CL25C850,Nitrogard 2.6mg Tablet,Nitroglycerin (2.6mg),Tablet,Cipla Ltd,Cardiovascular,2024-03,2026-03,OPD Pharmacy,50,strip,2024-06-13,Kerala Medical Supplies Co.
B00954,AL25K351,Normal Saline 0.9% Infusion,Sodium Chloride (0.9% w/v),Infusion,Alkem Laboratories Ltd,IV Fluids,2024-03,2027-03,Emergency Store,300,bottle,2024-04-05,Malabar Pharma Distributors
B00955,57218427,Rimpacin 450mg Capsule,Rifampicin (450mg),Capsule,Zydus Cadila,Anti-TB,2024-11,2027-11,Ward Store (Paeds),100,strip,2025-02-12,Sree Pharma Agencies
B00956,A25H832,Meronem 1000mg Injection,Meropenem (1000mg),Injection,AstraZeneca,Antibiotic,2024-08,2026-02,Emergency Store,20,vial/amp,2024-11-04,"Medline Distributors, Thiruvananthapuram"
B00957,TPT259785,Hqtor 300mg Tablet,Hydroxychloroquine (300mg),Tablet,Torrent Pharmaceuticals Ltd,Antimalarial,2025-01,2027-01,Main Pharmacy,100,strip,2025-02-07,Malabar Pharma Distributors
B00958,SPT252671,Lonazep 0.25 Tablet,Clonazepam (0.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-08,2026-08,OPD Pharmacy,20,strip,2024-11-10,"Medline Distributors, Thiruvananthapuram"
B00959,MPT247977,Macsart 20 Tablet,Telmisartan (20mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-12,2027-12,Emergency Store,80,strip,2025-01-07,Malabar Pharma Distributors
B00960,ML24C623,Bipacef 500 Tablet,Cefuroxime (500mg),Tablet,Micro Labs Ltd,Antibiotic,2024-08,2027-08,OPD Pharmacy,200,strip,2024-09-30,Kerala Medical Supplies Co.
B00961,IP24L790,Atro Eye Drop,Atropine (1% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-01,2027-01,OT Store,40,bottle,2025-03-02,Malabar Pharma Distributors
B00962,BI248926,Basalog 100IU/ml Injection,Insulin Glargine (100IU/ml),Injection,Biocon,Diabetes,2024-01,2026-06,OPD Pharmacy,20,vial/amp,2024-04-14,Sree Pharma Agencies
B00963,MLI257704,Divon 25mg Injection,Diclofenac (25mg),Injection,Micro Labs Ltd,Analgesic/Antipyretic,2024-04,2025-10,OT Store,100,vial/amp,2024-06-27,Apollo Wholesale Pvt Ltd
B00964,ISI245530,Stedex 4mg Injection,Dexamethasone (4mg),Injection,Ind Swift Laboratories Ltd,Steroid,2024-12,2026-06,Ward Store (Paeds),50,vial/amp,2025-03-07,Malabar Pharma Distributors
B00965,ALX244497,Sunheal Pure Cream,Zinc Oxide (25% w/w),Cream,Alkem Laboratories Ltd,Supplement,2024-07,2027-07,Main Pharmacy,0,tube,2024-10-14,Malabar Pharma Distributors
B00966,WL24F445,Cpink XT 20mg Injection,Ferrous Ascorbate (20mg),Injection,Wanbury Ltd,Haematology,2024-02,2027-02,OPD Pharmacy,80,vial/amp,2024-05-23,Kerala Medical Supplies Co.
B00967,62855838,Rancort 6mg Tablet,Deflazacort (6mg),Tablet,Sun Pharmaceutical Industries Ltd,Steroid,2025-03,2027-03,ICU Store,200,strip,2025-05-20,Malabar Pharma Distributors
B00968,ALT252396,Taxim-O 200 Tablet,Cefixime (200mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-04,2026-04,ICU Store,20,strip,2024-06-19,Apollo Wholesale Pvt Ltd
B00969,GP24D379,Olsivir Capsule,Oseltamivir Phosphate (75mg),Capsule,Glenmark Pharmaceuticals Ltd,Antiviral,2024-10,2026-04,Ward Store (Paeds),150,strip,2025-01-08,Sanjivani Drug House
B00970,70570928,Fluza 150mg Tablet,Fluconazole (150mg),Tablet,Micro Labs Ltd,Antifungal,2024-02,2027-02,Ward Store (Paeds),20,strip,2024-05-30,Kerala Medical Supplies Co.
B00971,28703143,Ceftop 250 mg/250 mg Injection,Cefoperazone (250mg) + Sulbactam (250mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2025-08,OPD Pharmacy,80,vial/amp,2024-04-03,Sanjivani Drug House
B00972,ZCV249037,Linid IV 600mg Infusion,Linezolid (600mg),Infusion,Zydus Cadila,Antibiotic,2025-02,2028-02,Main Pharmacy,50,bottle,2025-04-04,"Medline Distributors, Thiruvananthapuram"
B00973,X2405-807,Burnosaf Plus Cream,Silver Sulfadiazine (1% w/w),Cream,SAF Fermion Ltd,Dermatology,2024-07,2027-07,OPD Pharmacy,120,tube,2024-08-10,Malabar Pharma Distributors
B00974,T2412-448,Cipbact 500mg Tablet,Ciprofloxacin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-01,2027-01,Emergency Store,200,strip,2024-03-11,Apollo Wholesale Pvt Ltd
B00975,T2408-388,Telista 20 Tablet,Telmisartan (20mg),Tablet,Lupin Ltd,Cardiovascular,2024-03,2026-03,ICU Store,20,strip,2024-03-26,"Medline Distributors, Thiruvananthapuram"
B00976,ZCX240945,Nasoclear Gel,Sodium Chloride (0.65% w/w),Gel,Zydus Cadila,IV Fluids,2024-04,2027-04,OT Store,200,tube,2024-05-20,Sree Pharma Agencies
B00977,34585821,Anawin 0.25% Injection,Bupivacaine (0.25%),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-09,2027-09,Main Pharmacy,50,vial/amp,2024-12-20,Malabar Pharma Distributors
B00978,CL25D165,Azee 1000 Tablet,Azithromycin (1000mg),Tablet,Cipla Ltd,Antibiotic,2024-01,2026-01,Ward Store (Paeds),30,strip,2024-03-14,"Medline Distributors, Thiruvananthapuram"
B00979,T2404-286,Wysolone 5 Tablet DT,Prednisolone (5mg),Tablet,Pfizer Ltd,Steroid,2024-05,2026-05,OPD Pharmacy,40,strip,2024-08-05,Kerala Medical Supplies Co.
B00980,30592253,Apigy 2.5 Tablet,Apixaban (2.5mg),Tablet,Cipla Ltd,Anticoagulant,2024-02,2027-02,Emergency Store,120,strip,2024-04-18,Sanjivani Drug House
B00981,47571801,Oleanz 7.5 Tablet,Olanzapine (7.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2027-01,Main Pharmacy,200,strip,2024-04-07,"Medline Distributors, Thiruvananthapuram"
B00982,I2502-135,Cezone 1000mg Injection,Ceftriaxone (1000mg),Injection,Zydus Cadila,Antibiotic,2025-05,2027-05,Emergency Store,300,vial/amp,2025-07-06,"Medline Distributors, Thiruvananthapuram"
B00983,ALT255784,Almet 10mg Tablet,Metoclopramide (10mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-08,2027-08,ICU Store,50,strip,2024-11-13,Kerala Medical Supplies Co.
B00984,MP25D031,Revidox 100mg Tablet,Doxycycline (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-11,2026-11,OPD Pharmacy,0,strip,2024-12-03,Sanjivani Drug House
B00985,ALX258307,Tobraject 0.3% Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alkem Laboratories Ltd,Ophthalmology,2025-03,2026-09,Ward Store (Paeds),150,bottle,2025-05-10,Apollo Wholesale Pvt Ltd
B00986,13074636,D5 IV Injection,Dextrose (5% w/v),Injection,D.J Laboratories Pvt Ltd,IV Fluids,2025-05,2026-11,Ward Store (Paeds),10,vial/amp,2025-07-15,Malabar Pharma Distributors
B00987,GPX253502,Candid Gold Dusting Powder,Allantoin (0.2% w/w) + Clotrimazole (1% w/w),Powder,Glenmark Pharmaceuticals Ltd,Antifungal,2024-03,2026-03,ICU Store,80,pack,2024-06-22,Sree Pharma Agencies
B00988,IP24B220,Genox 5IU Injection,Oxytocin (5IU),Injection,Intas Pharmaceuticals Ltd,Obstetrics,2024-04,2026-04,Main Pharmacy,150,vial/amp,2024-06-14,Apollo Wholesale Pvt Ltd
B00989,T2506-201,Happi 20 Tablet,Rabeprazole (20mg),Tablet,Zydus Cadila,Gastro,2025-03,2027-03,OT Store,40,strip,2025-05-06,"Medline Distributors, Thiruvananthapuram"
B00990,46726260,Levtam 100mg Syrup,Levetiracetam (100mg),Syrup,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2027-08,Main Pharmacy,300,bottle,2024-11-02,Kerala Medical Supplies Co.
B00991,RKI244917,Glumig Injection,Calcium Gluconate (10mg),Injection,RSM Kilitch Pharma Pvt Ltd,Anaesthesia/Critical care,2024-05,2026-05,OT Store,60,vial/amp,2024-05-26,Malabar Pharma Distributors
B00992,MP25D258,Atorvakind 20mg Tablet,Atorvastatin (20mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2025-02,2028-02,Ward Store (Paeds),40,strip,2025-05-22,Malabar Pharma Distributors
B00993,GPX246962,Candid Gold Cream,Clotrimazole (1% w/w),Cream,Glenmark Pharmaceuticals Ltd,Antifungal,2024-11,2027-11,Ward Store (Paeds),100,tube,2024-12-09,Sanjivani Drug House
B00994,P24L189,Ondson Injection,Ondansetron (2mg/ml),Injection,Paksons Pharmaceuticals Pvt. Ltd.,Gastro,2024-11,2026-10,ICU Store,30,vial/amp,2025-01-26,Apollo Wholesale Pvt Ltd
B00995,WLI245464,Cpink XT 20mg Injection,Ferrous Ascorbate (20mg),Injection,Wanbury Ltd,Haematology,2024-07,2027-07,OT Store,30,vial/amp,2024-10-27,Sanjivani Drug House
B00996,T2510-831,Metocard XL 100 Tablet,Metoprolol Succinate (95mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-07,Emergency Store,80,strip,2024-04-22,Sanjivani Drug House
B00997,T2406-733,Lasipen 40mg Tablet,Furosemide (40mg),Tablet,Morepen Laboratories Ltd,Cardiovascular,2025-04,2026-10,OT Store,30,strip,2025-07-11,Apollo Wholesale Pvt Ltd
B00998,TPS252846,Cocorex 10mg Syrup,Chlorpheniramine Maleate (10mg),Syrup,Taj Pharma India Ltd,Anti-allergic,2024-09,2027-09,OPD Pharmacy,100,bottle,2024-11-16,Sanjivani Drug House
B00999,I2402-171,Nexiron Injection,Iron Sucrose (100mg/5ml),Injection,Zydus Cadila,Haematology,2024-05,2026-05,Main Pharmacy,120,vial/amp,2024-08-23,"Medline Distributors, Thiruvananthapuram"
B01000,95825759,Rimpacin 450mg Capsule,Rifampicin (450mg),Capsule,Zydus Cadila,Anti-TB,2025-05,2026-11,Emergency Store,50,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B01001,26664623,Magnex 1g Injection,Cefoperazone (500mg) + Sulbactam (500mg),Injection,Pfizer Ltd,Antibiotic,2024-07,2027-07,ICU Store,20,vial/amp,2024-09-30,Sree Pharma Agencies
B01002,SI25M126,Valparin Alkalets 500 Tablet,Sodium Valproate (500mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2024-11,2026-11,OT Store,150,strip,2025-01-26,Apollo Wholesale Pvt Ltd
B01003,EPI253113,Encifer Injection,Iron Sucrose (100mg),Injection,Emcure Pharmaceuticals Ltd,Haematology,2025-04,2026-10,Main Pharmacy,150,vial/amp,2025-06-05,Kerala Medical Supplies Co.
B01004,SL25K051,Furoped Oral Solution Pineapple,Furosemide (10mg/ml),Oral Solution,Samarth Life Sciences Pvt Ltd,Cardiovascular,2024-07,2026-01,Ward Store (Paeds),120,bottle,2024-08-15,Sanjivani Drug House
B01005,ALT243815,Esokem 20 Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-10,2026-04,ICU Store,200,strip,2025-01-21,Apollo Wholesale Pvt Ltd
B01006,LH25H137,Vomiford -MD Tablet,Ondansetron (4mg),Tablet,Leeford Healthcare Ltd,Gastro,2024-03,2025-09,OT Store,30,strip,2024-04-07,Sree Pharma Agencies
B01007,EP24J079,Encifer Injection,Iron Sucrose (100mg),Injection,Emcure Pharmaceuticals Ltd,Haematology,2024-07,2026-01,OPD Pharmacy,300,vial/amp,2024-09-09,Apollo Wholesale Pvt Ltd
B01008,47551535,Ketof-DT Tablet,Ketorolac (10mg),Tablet,Abbott,Analgesic/Antipyretic,2024-07,2026-07,OPD Pharmacy,120,strip,2024-10-01,Malabar Pharma Distributors
B01009,PIT243705,Dexodil 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psychotropics India Ltd,Anti-allergic,2025-03,2027-03,Main Pharmacy,80,strip,2025-06-17,Apollo Wholesale Pvt Ltd
B01010,AL25A716,Ondem 8 Tablet,Ondansetron (8mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-08,2027-08,OT Store,30,strip,2024-10-12,Apollo Wholesale Pvt Ltd
B01011,81337227,Lopez 1mg Tablet,Lorazepam (1mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-11,2026-11,OPD Pharmacy,150,strip,2025-01-01,Sree Pharma Agencies
B01012,LL25M254,B-Cin 200mg Tablet,Balofloxacin (200mg),Tablet,Lupin Ltd,Antibiotic,2024-09,2027-09,Ward Store (Paeds),50,strip,2024-10-17,"Medline Distributors, Thiruvananthapuram"
B01013,AL25G858,Almetfor 500mg Tablet,Metformin (500mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-10,2026-10,ICU Store,0,strip,2024-11-28,"Medline Distributors, Thiruvananthapuram"
B01014,T2508-524,Concor 10 Tablet,Bisoprolol (10mg),Tablet,Merck Ltd,Cardiovascular,2024-05,2027-05,OT Store,0,strip,2024-07-11,Sanjivani Drug House
B01015,IPC250207,Pregabid 50 Capsule,Pregabalin (50mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-04,2028-04,OPD Pharmacy,30,strip,2025-06-03,Kerala Medical Supplies Co.
B01016,T2405-029,Cifran 100 Tablet,Ciprofloxacin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-11,2026-11,OPD Pharmacy,0,strip,2025-01-14,Sanjivani Drug House
B01017,SP24B445,Alfakim 100mg Injection,Amikacin (100mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2027-01,OT Store,10,vial/amp,2024-04-24,Sree Pharma Agencies
B01018,SP25F400,Dombax 10mg Tablet,Domperidone (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-08,2026-02,OT Store,80,strip,2024-08-28,Malabar Pharma Distributors
B01019,36786211,Glycomet 500 SR Tablet,Metformin (500mg),Tablet,USV Ltd,Diabetes,2024-07,2026-01,ICU Store,50,strip,2024-09-22,Sree Pharma Agencies
B01020,S2509-903,Bandy Suspension,Albendazole (200mg),Suspension,Mankind Pharma Ltd,Anthelmintic,2024-02,2027-02,Emergency Store,60,bottle,2024-04-15,Malabar Pharma Distributors
B01021,CLT250105,Acivir 200 DT Tablet,Acyclovir (200mg),Tablet,Cipla Ltd,Antiviral,2024-02,2026-02,Ward Store (Paeds),40,strip,2024-03-06,Sanjivani Drug House
B01022,70291054,Tegretol 100mg Tablet,Carbamazepine (100mg),Tablet,Novartis India Ltd,Neurology/Psychiatry,2024-12,2026-12,OT Store,80,strip,2025-03-13,Sree Pharma Agencies
B01023,WMX256521,Betadine 5 % Solution,Povidone Iodine (5% w/v),Solution,Win-Medicare Pvt Ltd,Dermatology,2024-02,2027-02,Emergency Store,200,bottle,2024-03-19,Sanjivani Drug House
B01024,IPI243326,Hicoly 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-04,2026-04,OT Store,80,vial/amp,2024-06-10,Sanjivani Drug House
B01025,T2511-126,Docmycin 100mg Tablet,Doxycycline (100mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-05,2026-05,Main Pharmacy,10,strip,2024-08-18,Kerala Medical Supplies Co.
B01026,CL24B101,Carloc 12.5 Tablet,Carvedilol (12.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-08,2026-02,OPD Pharmacy,0,strip,2024-10-17,Malabar Pharma Distributors
B01027,95787279,Angizaar 25 Tablet,Losartan (25mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-01,2026-01,Ward Store (Paeds),120,strip,2024-02-24,Sree Pharma Agencies
B01028,LL24A419,Lupisit 100mg Tablet,Sitagliptin (100mg),Tablet,Lupin Ltd,Diabetes,2024-06,2026-06,ICU Store,200,strip,2024-09-18,Kerala Medical Supplies Co.
B01029,ORI253336,Ovit-Cee Injection,Vitamin C (250mg),Injection,Oscar Remedies Pvt Ltd,Supplement,2024-11,2026-11,ICU Store,50,vial/amp,2025-02-14,Sanjivani Drug House
B01030,IP25B505,Intacoxia 120 Tablet,Etoricoxib (120mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-01,2027-01,Ward Store (Paeds),60,strip,2025-01-29,Sree Pharma Agencies
B01031,T2508-682,Diacip 500mg Tablet,Metformin (500mg),Tablet,Cipla Ltd,Diabetes,2025-02,2027-02,Ward Store (Paeds),10,strip,2025-03-29,Kerala Medical Supplies Co.
B01032,ALT240259,Actisprin 150mg Tablet,Aspirin (150mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-06,2027-06,Emergency Store,0,strip,2024-09-10,Kerala Medical Supplies Co.
B01033,80557676,Meronem 1000mg Injection,Meropenem (1000mg),Injection,AstraZeneca,Antibiotic,2024-05,2027-05,OT Store,300,vial/amp,2024-07-17,Sanjivani Drug House
B01034,MLT242171,Arbitel 20 Tablet,Telmisartan (20mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-01,2027-01,Emergency Store,0,strip,2024-02-25,Sanjivani Drug House
B01035,CLT253710,Restyl 0.5mg Tablet,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-08,2026-02,OPD Pharmacy,200,strip,2024-11-20,Kerala Medical Supplies Co.
B01036,LL24M170,Meflup 250mg Tablet,Mefenamic Acid (250mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2024-12,2026-12,Main Pharmacy,50,strip,2025-03-07,Sanjivani Drug House
B01037,T2512-745,Wysolone 20 Tablet DT,Prednisolone (20mg),Tablet,Pfizer Ltd,Steroid,2024-07,2027-07,OPD Pharmacy,200,strip,2024-08-02,Sanjivani Drug House
B01038,CL24D879,Ceruclean Drop,Prednisolone (NA),Drops,Cipla Ltd,Steroid,2024-01,2026-11,OPD Pharmacy,100,bottle,2024-04-29,Sree Pharma Agencies
B01039,CLV242495,Cefadur CA 250mg Infusion,Cefuroxime (250mg),Infusion,Cipla Ltd,Antibiotic,2024-07,2026-01,Emergency Store,0,bottle,2024-09-18,Sree Pharma Agencies
B01040,S2507-034,Rancotrim Suspension,Sulfamethoxazole (200mg/5ml) + Trimethoprim (40mg/5ml),Suspension,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-09,2026-09,Main Pharmacy,120,bottle,2024-12-19,Malabar Pharma Distributors
B01041,X2507-570,Derinide 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Zydus Cadila,Respiratory,2024-04,2026-04,Ward Store (Paeds),80,respule,2024-06-30,Apollo Wholesale Pvt Ltd
B01042,42458322,Lupisoz Tablet,Esomeprazole (40mg),Tablet,Lupin Ltd,Gastro,2024-08,2026-08,OPD Pharmacy,40,strip,2024-10-16,Sanjivani Drug House
B01043,AL25E387,Almox CV Syrup,Amoxycillin (200mg/5ml) + Clavulanic Acid (28.5mg/5ml),Syrup,Alkem Laboratories Ltd,Antibiotic,2024-12,2026-12,Emergency Store,100,bottle,2024-12-27,Malabar Pharma Distributors
B01044,AL24G497,Gluvilda 50 Tablet,Vildagliptin (50mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-03,2025-09,Ward Store (Paeds),50,strip,2024-06-26,Sanjivani Drug House
B01045,T2405-295,Acifac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-01,2026-06,OT Store,80,strip,2024-04-30,Sree Pharma Agencies
B01046,TPS248633,Azibold 100mg/5ml Syrup,Azithromycin (100mg/5ml),Syrup,Torrent Pharmaceuticals Ltd,Antibiotic,2024-06,2026-06,ICU Store,150,bottle,2024-08-18,"Medline Distributors, Thiruvananthapuram"
B01047,IP25L171,Pregabid 300mg Capsule,Pregabalin (300mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2026-03,OT Store,120,strip,2024-06-02,Kerala Medical Supplies Co.
B01048,I2408-394,Advent 1.2gm Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Cipla Ltd,Antibiotic,2025-04,2028-04,OT Store,300,vial/amp,2025-06-24,Sanjivani Drug House
B01049,TP24D723,Calbloc 10mg Capsule,Nifedipine (10mg),Capsule,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-10,2026-04,Main Pharmacy,40,strip,2024-12-02,Sanjivani Drug House
B01050,T2411-800,Azerva 10 Tablet,Atorvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-12,2027-12,OPD Pharmacy,50,strip,2025-02-25,Malabar Pharma Distributors
B01051,CLT253079,Emeset 2mg Tablet MD,Ondansetron (2mg),Tablet,Cipla Ltd,Gastro,2024-04,2026-04,ICU Store,30,strip,2024-06-27,Kerala Medical Supplies Co.
B01052,74954396,Pause 1000mg Tablet,Tranexamic Acid (1000mg),Tablet,Emcure Pharmaceuticals Ltd,Haematology,2024-10,2027-10,ICU Store,150,strip,2024-11-30,Apollo Wholesale Pvt Ltd
B01053,T2411-954,Oleanz 5 Tablet,Olanzapine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-02,2026-02,OPD Pharmacy,40,strip,2024-04-15,Sree Pharma Agencies
B01054,61314322,Basalog 100IU/ml Injection,Insulin Glargine (100IU/ml),Injection,Biocon,Diabetes,2025-02,2026-08,Main Pharmacy,200,vial/amp,2025-02-26,Apollo Wholesale Pvt Ltd
B01055,TPT244508,Domstal DT Tablet,Domperidone (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-10,2026-04,Main Pharmacy,100,strip,2024-11-17,Apollo Wholesale Pvt Ltd
B01056,LH24L582,Mefniwel 100mg Syrup,Mefenamic Acid (100mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-10,2026-10,Emergency Store,30,bottle,2024-11-05,Sanjivani Drug House
B01057,TPI242302,Cortisum 100mg Injection,Hydrocortisone (100mg),Injection,Torrent Pharmaceuticals Ltd,Steroid,2025-04,2027-04,Ward Store (Paeds),20,vial/amp,2025-05-12,Malabar Pharma Distributors
B01058,AL25K910,Merosure 125mg Injection,Meropenem (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-12,2026-12,Main Pharmacy,50,vial/amp,2025-03-14,Kerala Medical Supplies Co.
B01059,83617061,Afoglip Tablet,Teneligliptin (20mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-02,2027-02,OT Store,80,strip,2025-04-18,Malabar Pharma Distributors
B01060,DR24G775,Doxt Injection Combipack,Doxycycline (100mg),Injection,Dr Reddy's Laboratories Ltd,Antibiotic,2024-04,2025-10,Main Pharmacy,120,vial/amp,2024-07-03,"Medline Distributors, Thiruvananthapuram"
B01061,77441055,Cipmox 125mg Tablet DT,Amoxycillin (125mg),Tablet,Cipla Ltd,Antibiotic,2024-10,2027-10,OT Store,150,strip,2025-01-25,Kerala Medical Supplies Co.
B01062,RL25M780,Serenace 1.5 Tablet,Haloperidol (1.5mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-11,2027-11,OT Store,50,strip,2025-01-12,Kerala Medical Supplies Co.
B01063,ZCI246366,Cadicin 100mg Injection,Amikacin (100mg),Injection,Zydus Cadila,Antibiotic,2024-05,2027-05,Ward Store (Paeds),20,vial/amp,2024-07-12,"Medline Distributors, Thiruvananthapuram"
B01064,S2502-468,Perinorm Syrup,Metoclopramide (5mg),Syrup,Ipca Laboratories Ltd,Gastro,2024-01,2026-01,Emergency Store,20,bottle,2024-04-13,"Medline Distributors, Thiruvananthapuram"
B01065,ZCT252393,Epsolin 300 Tablet,Phenytoin (300mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-03,2027-03,ICU Store,30,strip,2024-06-02,Malabar Pharma Distributors
B01066,LP24C853,Nam Cold DX Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Lincoln Pharmaceuticals Ltd,Respiratory,2025-04,2027-04,OT Store,300,bottle,2025-06-18,Kerala Medical Supplies Co.
B01067,ZCI245234,Gervec 10mg Injection,Vecuronium (10mg),Injection,Zydus Cadila,Anaesthesia/Critical care,2024-01,2027-01,Main Pharmacy,30,vial/amp,2024-03-18,Apollo Wholesale Pvt Ltd
B01068,I2511-030,Citelec 250mg Injection,Citicoline (250mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-08,2027-08,OT Store,10,vial/amp,2024-11-27,Apollo Wholesale Pvt Ltd
B01069,23862208,Alprax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-10,2026-10,Emergency Store,150,strip,2024-12-27,Sree Pharma Agencies
B01070,ALT251354,Almetfor 500mg Tablet,Metformin (500mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-05,2027-05,Emergency Store,10,strip,2025-05-30,Malabar Pharma Distributors
B01071,43422272,Telsartan 20 Tablet,Telmisartan (20mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-11,2027-11,OT Store,30,strip,2025-01-31,Malabar Pharma Distributors
B01072,91165232,Vertipress 16 Tablet,Betahistine (16mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-03,2026-03,Ward Store (Paeds),10,strip,2024-04-21,Sanjivani Drug House
B01073,62601013,Alciflox 500mg Tablet,Ciprofloxacin (500mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-05,2026-05,OPD Pharmacy,10,strip,2024-07-15,Malabar Pharma Distributors
B01074,X2410-571,Safoderm Plus 1% Cream,Silver Sulfadiazine (1% w/w),Cream,Biochem Pharmaceutical Industries,Dermatology,2025-05,2028-05,OPD Pharmacy,300,tube,2025-07-13,Apollo Wholesale Pvt Ltd
B01075,IP25L239,Tramatas 50mg Capsule,Tramadol (50mg),Capsule,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2026-08,Ward Store (Paeds),150,strip,2025-05-19,Sree Pharma Agencies
B01076,T2509-495,FCN 150 Tablet,Fluconazole (150mg),Tablet,Intas Pharmaceuticals Ltd,Antifungal,2024-08,2027-08,Ward Store (Paeds),40,strip,2024-10-30,Kerala Medical Supplies Co.
B01077,IPT248121,Niftas 50 Tablet,Nitrofurantoin (50mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-01,2028-01,Main Pharmacy,50,strip,2025-03-25,Sanjivani Drug House
B01078,I2505-393,Basugine 100IU/ml Injection,Insulin Glargine (100IU),Injection,Lupin Ltd,Diabetes,2024-06,2026-06,Ward Store (Paeds),20,vial/amp,2024-07-09,"Medline Distributors, Thiruvananthapuram"
B01079,CL24F910,Thyrocip 100 Tablet,Thyroxine (100mcg),Tablet,Cipla Ltd,Endocrine,2025-04,2028-04,ICU Store,300,strip,2025-07-15,Malabar Pharma Distributors
B01080,SPT247228,Lonazep 0.25 Tablet,Clonazepam (0.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-04,2026-10,Ward Store (Paeds),20,strip,2025-06-15,Sanjivani Drug House
B01081,23985428,Dopar 200mg Injection,Dopamine (200mg),Injection,Samarth Life Sciences Pvt Ltd,Anaesthesia/Critical care,2025-01,2028-01,OT Store,30,vial/amp,2025-02-18,"Medline Distributors, Thiruvananthapuram"
B01082,T2402-140,Rosuvas F 10 Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2026-03,OT Store,10,strip,2024-05-18,Sanjivani Drug House
B01083,T2410-672,Prolomet XL 100 Tablet,Metoprolol Succinate (95mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2027-04,Main Pharmacy,20,strip,2024-07-09,Kerala Medical Supplies Co.
B01084,46728250,Taxim-O 400 Tablet,Cefixime (400mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-05,2027-05,OT Store,10,strip,2025-05-27,Sree Pharma Agencies
B01085,LH24L790,Rashcare Cream,Zinc Oxide (8.5% w/w),Cream,Leeford Healthcare Ltd,Supplement,2025-03,2027-03,OT Store,120,tube,2025-05-06,Malabar Pharma Distributors
B01086,T2402-093,Amlopres TL 80mg/5mg Tablet,Telmisartan (80mg) + Amlodipine (5mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2028-01,Emergency Store,200,strip,2025-02-07,Apollo Wholesale Pvt Ltd
B01087,GS25C126,Zovirax 200 Tablet,Acyclovir (200mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2024-08,2026-02,OT Store,60,strip,2024-10-16,Kerala Medical Supplies Co.
B01088,47363712,Budez CR Capsule,Budesonide (3mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2027-12,OPD Pharmacy,0,strip,2025-03-22,Apollo Wholesale Pvt Ltd
B01089,IPT254369,Intazin L 5mg Tablet,Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2024-12,2026-06,Emergency Store,200,strip,2025-01-29,Apollo Wholesale Pvt Ltd
B01090,47015631,Ramipres 1.25 Tablet,Ramipril (1.25mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2026-10,ICU Store,80,strip,2025-01-08,Sree Pharma Agencies
B01091,14072389,Imulast 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Cipla Ltd,Antimalarial,2024-09,2026-09,Emergency Store,0,strip,2024-12-14,"Medline Distributors, Thiruvananthapuram"
B01092,CLT256149,Cosart 25 Tablet,Losartan (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2027-04,Ward Store (Paeds),0,strip,2024-06-11,Apollo Wholesale Pvt Ltd
B01093,24890990,Alcoxib 120mg Tablet,Etoricoxib (120mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-01,2026-01,Emergency Store,120,strip,2024-03-01,Apollo Wholesale Pvt Ltd
B01094,T2402-714,Asthalin 4 Tablet,Salbutamol (4mg),Tablet,Cipla Ltd,Respiratory,2024-02,2027-02,Emergency Store,150,strip,2024-04-04,"Medline Distributors, Thiruvananthapuram"
B01095,T2501-346,Allercet-M Kid Tablet DT,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Micro Labs Ltd,Respiratory,2024-06,2027-06,Ward Store (Paeds),30,strip,2024-06-30,Sree Pharma Agencies
B01096,ZC24F424,Depotex 4mg Tablet,Methylprednisolone (4mg),Tablet,Zydus Cadila,Steroid,2025-03,2028-03,Ward Store (Paeds),50,strip,2025-04-06,Sree Pharma Agencies
B01097,SI24K710,Valparin 200 Oral Solution Delicious Pineapple,Sodium Valproate (200mg/5ml),Oral Solution,Sanofi India Ltd,Neurology/Psychiatry,2024-07,2026-07,Emergency Store,300,bottle,2024-08-16,Sree Pharma Agencies
B01098,T2511-368,Norflox 200 Tablet,Norfloxacin (200mg) + Lactobacillus (60Million spores),Tablet,Cipla Ltd,Other,2024-06,2026-06,OPD Pharmacy,40,strip,2024-08-29,Malabar Pharma Distributors
B01099,PL25J311,Lyrica 75mg Capsule,Pregabalin (75mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-05,2025-11,OT Store,200,strip,2024-08-03,Sree Pharma Agencies
B01100,28850770,Zentel Oral Suspension,Albendazole (400mg),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2025-01,2026-07,Ward Store (Paeds),200,bottle,2025-04-27,Apollo Wholesale Pvt Ltd
B01101,MPT244934,Bigclav CV 500mg/125mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Mankind Pharma Ltd,Antibiotic,2025-05,2028-05,ICU Store,100,strip,2025-07-15,Sree Pharma Agencies
B01102,ABGJ24032TH,Petalife-40 Injection,Pantoprazole (40mg),Injection,Associated Biopharma Pvt. Ltd.,Gastro,2024-10,2026-09,OT Store,10,vial/amp,2025-01-06,Malabar Pharma Distributors
B01103,T2407-564,Eltroxin 125mcg Tablet,Thyroxine (125mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2025-02,2028-02,OPD Pharmacy,0,strip,2025-04-15,Kerala Medical Supplies Co.
B01104,I2512-109,Tranarest 100mg Injection,Tranexamic Acid (100mg),Injection,Cadila Pharmaceuticals Ltd,Haematology,2024-10,2027-10,OT Store,50,vial/amp,2025-01-04,Sree Pharma Agencies
B01105,T2403-449,Ritebeat 100mg Tablet,Amiodarone (100mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-04,2026-10,Ward Store (Paeds),60,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01106,CLS256965,Montair LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Cipla Ltd,Respiratory,2025-01,2027-01,Ward Store (Paeds),200,bottle,2025-04-04,Sanjivani Drug House
B01107,APT249741,Azithral 500 Tablet,Azithromycin (500mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-02,2026-02,Main Pharmacy,0,strip,2024-03-25,Malabar Pharma Distributors
B01108,SP24F655,Teleact D 80 Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-03,2028-03,ICU Store,300,strip,2025-03-28,Sree Pharma Agencies
B01109,EPI248443,Enatrate Injection,Adrenaline (NA),Injection,Entod Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-02,2028-02,OPD Pharmacy,60,vial/amp,2025-03-12,Malabar Pharma Distributors
B01110,31905860,Azukon MR Tablet,Gliclazide (30mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-03,2026-03,OPD Pharmacy,60,strip,2024-06-09,"Medline Distributors, Thiruvananthapuram"
B01111,SP24G403,Lizoran 600mg Infusion,Linezolid (600mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-05,2027-05,OPD Pharmacy,0,bottle,2024-07-21,Sree Pharma Agencies
B01112,SP25C585,Pantocalm 40mg Tablet,Pantoprazole (40mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-03,2026-03,OT Store,150,strip,2024-06-04,Malabar Pharma Distributors
B01113,IPT250887,Prazopill XL 2.5 Tablet,Prazosin (2.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-02,2025-08,OPD Pharmacy,40,strip,2024-03-23,Sree Pharma Agencies
B01114,T2407-134,Ldtor 10mg Tablet,Atorvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-04,2027-04,ICU Store,300,strip,2025-05-27,Kerala Medical Supplies Co.
B01115,46923094,Levipil 1g Tablet,Levetiracetam (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-04,2028-04,Main Pharmacy,30,strip,2025-07-08,Sree Pharma Agencies
B01116,LLS246464,Lupibend 200mg Suspension,Albendazole (200mg),Suspension,Lupin Ltd,Anthelmintic,2025-04,2027-04,ICU Store,20,bottle,2025-05-28,Malabar Pharma Distributors
B01117,SP25G711,Clopilet A 150 Capsule,Aspirin (150mg) + Clopidogrel (75mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-07,2027-07,Ward Store (Paeds),60,strip,2024-09-26,Apollo Wholesale Pvt Ltd
B01118,DRT253658,Tryptomer 25mg Tablet,Amitriptyline (25mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2024-04,2025-10,ICU Store,60,strip,2024-06-08,Apollo Wholesale Pvt Ltd
B01119,S2412-860,Mefniwel 100mg Syrup,Mefenamic Acid (100mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-01,2026-01,Main Pharmacy,80,bottle,2024-04-09,Sanjivani Drug House
B01120,I2404-808,Adrelin Injection,Adrenaline (NA),Injection,Klar Sehen Pvt Ltd,Anaesthesia/Critical care,2025-02,2028-02,Emergency Store,100,vial/amp,2025-04-21,"Medline Distributors, Thiruvananthapuram"
B01121,ML25J700,Diapride 1 Tablet,Glimepiride (1mg),Tablet,Micro Labs Ltd,Diabetes,2024-03,2026-03,OPD Pharmacy,20,strip,2024-05-18,Apollo Wholesale Pvt Ltd
B01122,ALX242977,Vigamox Ophthalmic Solution,Moxifloxacin (0.5% w/v),Solution,Alcon Laboratories,Ophthalmology,2024-02,2026-02,ICU Store,50,bottle,2024-03-21,Malabar Pharma Distributors
B01123,VE4111,Ofloxacin + Dexamethasone Ophthalmic Solution,Ofloxacin (0.3%) + Dexamethasone (0.1%),Eye Drops,Alpa Laboratories Ltd.,Ophthalmology,2024-11,2026-10,OPD Pharmacy,50,bottle,2025-01-08,Sree Pharma Agencies
B01124,CL25C947,Aprovent Inhaler,Ipratropium (NA),Inhaler,Cipla Ltd,Respiratory,2024-10,2026-10,Emergency Store,300,inhaler,2025-01-06,"Medline Distributors, Thiruvananthapuram"
B01125,AL24E928,Hospilid 200mg Infusion,Linezolid (200mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-07,2026-01,ICU Store,100,bottle,2024-10-12,"Medline Distributors, Thiruvananthapuram"
B01126,21161254,Ascad 150mg Tablet,Aspirin (150mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-04,2027-04,Main Pharmacy,20,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01127,SPT245343,Etoshine 120 Tablet,Etoricoxib (120mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-12,2026-06,ICU Store,60,strip,2025-01-13,Kerala Medical Supplies Co.
B01128,X2508-264,Ipneb Solution for inhalation,Ipratropium (250mcg),Solution,Lupin Ltd,Respiratory,2024-05,2026-05,OPD Pharmacy,200,bottle,2024-06-10,Kerala Medical Supplies Co.
B01129,40323831,Electrolyte M 5% Infusion,Dextrose (5% w/v),Infusion,Baxter India Pvt Ltd,IV Fluids,2025-02,2026-08,Ward Store (Paeds),80,bottle,2025-05-01,Sree Pharma Agencies
B01130,T2406-291,Azukon MR Tablet,Gliclazide (30mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-03,2026-09,Ward Store (Paeds),300,strip,2025-05-07,Malabar Pharma Distributors
B01131,AL24E593,Tramef 50mg Injection,Tramadol (50mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-04,2028-04,ICU Store,0,vial/amp,2025-06-15,"Medline Distributors, Thiruvananthapuram"
B01132,13466904,Entofoam NF Cream,Hydrocortisone (10% w/w),Cream,Cipla Ltd,Steroid,2024-10,2027-10,Emergency Store,20,tube,2025-01-28,Malabar Pharma Distributors
B01133,CL25B528,Asthalin 4 Tablet,Salbutamol (4mg),Tablet,Cipla Ltd,Respiratory,2024-06,2027-06,Main Pharmacy,50,strip,2024-09-16,Apollo Wholesale Pvt Ltd
B01134,TPS248936,Azibold 100mg/5ml Syrup,Azithromycin (100mg/5ml),Syrup,Torrent Pharmaceuticals Ltd,Antibiotic,2024-12,2026-12,OPD Pharmacy,150,bottle,2025-01-01,Malabar Pharma Distributors
B01135,IPT250809,Acticin 500mg Tablet,Paracetamol (500mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-04,2028-04,Main Pharmacy,200,strip,2025-05-09,Sanjivani Drug House
B01136,NL24A790,Magneon 50% Injection,Magnesium Sulphate (50% w/v),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2025-02,2028-02,Emergency Store,300,vial/amp,2025-05-12,Kerala Medical Supplies Co.
B01137,TP24J903,Cathflush 10IU Injection,Heparin (10IU),Injection,Troikaa Pharmaceuticals Ltd,Anticoagulant,2024-05,2025-11,Ward Store (Paeds),20,vial/amp,2024-07-21,Apollo Wholesale Pvt Ltd
B01138,70549373,Metrogyl 200 Tablet,Metronidazole (200mg),Tablet,Lekar Pharma Ltd,Antibiotic,2024-07,2026-01,OT Store,0,strip,2024-09-08,"Medline Distributors, Thiruvananthapuram"
B01139,T2411-832,Astin 10 Tablet,Atorvastatin (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-12,2027-12,OPD Pharmacy,10,strip,2025-02-18,Malabar Pharma Distributors
B01140,IR24E621,Ocubion 5% Eye Drop,Sodium Chloride (5% w/v),Eye Drops,Ikon Remedies Pvt Ltd,IV Fluids,2024-08,2027-08,OPD Pharmacy,50,bottle,2024-10-21,Kerala Medical Supplies Co.
B01141,SPX256299,Bectodine 5% Ointment,Povidone Iodine (5% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Dermatology,2024-10,2027-10,Emergency Store,150,tube,2025-01-18,Sree Pharma Agencies
B01142,ZC24K327,Cadicin 100mg Injection,Amikacin (100mg),Injection,Zydus Cadila,Antibiotic,2024-08,2026-08,ICU Store,10,vial/amp,2024-10-07,Kerala Medical Supplies Co.
B01143,I2510-279,Troymag 50% Injection,Magnesium Sulphate (50% w/v),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-03,2028-03,Main Pharmacy,150,vial/amp,2025-05-26,Sree Pharma Agencies
B01144,A24H396,Neo-Mercazole 10 Tablet,Carbimazole (10mg),Tablet,Abbott,Endocrine,2024-07,2027-07,Emergency Store,200,strip,2024-08-13,Kerala Medical Supplies Co.
B01145,SPC249266,Gabantin 100 Capsule,Gabapentin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-01,2027-01,OPD Pharmacy,40,strip,2025-03-10,Sree Pharma Agencies
B01146,I2510-833,Domadol 100mg Injection,Tramadol (100mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-04,2027-04,Ward Store (Paeds),50,vial/amp,2024-07-13,Malabar Pharma Distributors
B01147,CLT253278,Levoflox 500 Tablet,Levofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2024-09,2026-09,Emergency Store,150,strip,2024-11-12,Apollo Wholesale Pvt Ltd
B01148,T2408-233,Glimp M 1mg/1000mg Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2024-08,2026-08,OPD Pharmacy,150,strip,2024-10-10,Apollo Wholesale Pvt Ltd
B01149,MLT256374,Concor 5 Tablet,Bisoprolol (5mg),Tablet,Merck Ltd,Cardiovascular,2024-01,2026-06,Main Pharmacy,20,strip,2024-02-14,Sanjivani Drug House
B01150,CP25L218,Tranarest 100mg Injection,Tranexamic Acid (100mg),Injection,Cadila Pharmaceuticals Ltd,Haematology,2024-04,2025-10,OT Store,50,vial/amp,2024-04-28,Kerala Medical Supplies Co.
B01151,MP25E031,Nudiclo 100mg Tablet,Diclofenac (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-05,2026-05,Main Pharmacy,120,strip,2024-08-16,Malabar Pharma Distributors
B01152,MLT254074,Concor AM 2.5 Tablet,Amlodipine (5mg) + Bisoprolol (2.5mg),Tablet,Merck Ltd,Cardiovascular,2025-01,2027-01,Emergency Store,50,strip,2025-03-26,Apollo Wholesale Pvt Ltd
B01153,39193682,Safoderm Plus 1% Cream,Silver Sulfadiazine (1% w/w),Cream,Biochem Pharmaceutical Industries,Dermatology,2025-03,2028-03,OT Store,20,tube,2025-06-08,Sanjivani Drug House
B01154,47955201,Amipace 100 Tablet,Amiodarone (100mg),Tablet,Lupin Ltd,Cardiovascular,2024-06,2027-06,OT Store,150,strip,2024-09-06,Kerala Medical Supplies Co.
B01155,ZC25C102,Cefabest 200 Tablet,Cefpodoxime Proxetil (200mg),Tablet,Zydus Cadila,Antibiotic,2024-01,2026-02,OPD Pharmacy,20,strip,2024-03-07,Apollo Wholesale Pvt Ltd
B01156,JBT253998,Rantac 150 Tablet,Ranitidine (150mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-02,2025-08,Main Pharmacy,50,strip,2024-05-11,Sree Pharma Agencies
B01157,CL25L796,Itracan 100mg Capsule,Itraconazole (100mg),Capsule,Cipla Ltd,Antifungal,2024-08,2027-08,ICU Store,50,strip,2024-10-30,Sree Pharma Agencies
B01158,CLT246465,Cizetol 200mg Tablet,Carbamazepine (200mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-01,2028-01,OT Store,60,strip,2025-03-09,Sree Pharma Agencies
B01159,LH24J536,Ceficlav 100mg Tablet DT,Cefixime (100mg),Tablet,Leeford Healthcare Ltd,Antibiotic,2024-02,2027-02,Main Pharmacy,60,strip,2024-03-16,Apollo Wholesale Pvt Ltd
B01160,64105718,Floxip 100mg Infusion,Ciprofloxacin (100mg),Infusion,Abbott,Antibiotic,2025-03,2028-03,OPD Pharmacy,100,bottle,2025-05-05,Apollo Wholesale Pvt Ltd
B01161,WLT244274,Phylobid 200mg Tablet,Theophylline (200mg),Tablet,Wockhardt Ltd,Respiratory,2024-01,2026-01,ICU Store,60,strip,2024-03-26,"Medline Distributors, Thiruvananthapuram"
B01162,NH25J508,Aculife 25% Infusion,Dextrose (25% w/v),Infusion,Nirlife Healthcare,IV Fluids,2024-03,2025-09,ICU Store,0,bottle,2024-06-19,Malabar Pharma Distributors
B01163,TPT247531,Alprax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-04,2026-10,OPD Pharmacy,300,strip,2025-06-08,Sanjivani Drug House
B01164,62884503,Montair LC Kid Tablet DT,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Cipla Ltd,Respiratory,2024-11,2027-11,Ward Store (Paeds),120,strip,2025-02-09,"Medline Distributors, Thiruvananthapuram"
B01165,80095741,Klotfree Tablet,Clopidogrel (75mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2026-02,Ward Store (Paeds),80,strip,2024-05-09,"Medline Distributors, Thiruvananthapuram"
B01166,LL25C224,R-Cin 300 Capsule,Rifampicin (300mg),Capsule,Lupin Ltd,Anti-TB,2025-03,2027-03,Emergency Store,300,strip,2025-06-05,Malabar Pharma Distributors
B01167,AI243439,Sensorcaine 0.25% Injection,Bupivacaine (0.25%),Injection,AstraZeneca,Anaesthesia/Critical care,2025-04,2027-04,ICU Store,100,vial/amp,2025-07-04,Sanjivani Drug House
B01168,IL24D308,Folitrax 15 Injection,Methotrexate (15mg/ml),Injection,Ipca Laboratories Ltd,Oncology,2025-03,2028-03,ICU Store,60,vial/amp,2025-05-21,Kerala Medical Supplies Co.
B01169,PLC241079,Lyrica 150mg Capsule,Pregabalin (150mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-11,2027-11,OPD Pharmacy,150,strip,2025-01-10,Malabar Pharma Distributors
B01170,SLX251195,Furoped Oral Solution Pineapple,Furosemide (10mg/ml),Oral Solution,Samarth Life Sciences Pvt Ltd,Cardiovascular,2024-02,2025-08,OT Store,60,bottle,2024-05-15,Sree Pharma Agencies
B01171,T2410-601,Voveran 150mg Tablet SR,Diclofenac (150mg),Tablet,Novartis India Ltd,Analgesic/Antipyretic,2024-07,2026-07,Main Pharmacy,10,strip,2024-08-28,"Medline Distributors, Thiruvananthapuram"
B01172,MP24J079,Omnacortil 10 Tablet DT,Prednisolone (10mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Steroid,2025-02,2027-02,OT Store,20,strip,2025-05-01,Sanjivani Drug House
B01173,IPI259724,Falciart 60mg Injection,Artesunate (60mg),Injection,Intas Pharmaceuticals Ltd,Antimalarial,2025-01,2028-01,Main Pharmacy,300,vial/amp,2025-02-10,Sanjivani Drug House
B01174,87324220,Levocet M Kid Tablet MD,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Hetero Drugs Ltd,Respiratory,2024-03,2027-03,Emergency Store,120,strip,2024-05-05,Malabar Pharma Distributors
B01175,TPT255752,Olmetor 10mg Tablet,Olmesartan Medoxomil (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-05,2028-05,OPD Pharmacy,100,strip,2025-05-29,Apollo Wholesale Pvt Ltd
B01176,ML24M192,Forinem 500mg Injection,Meropenem (500mg),Injection,Micro Labs Ltd,Antibiotic,2024-07,2026-01,Ward Store (Paeds),60,vial/amp,2024-07-30,Kerala Medical Supplies Co.
B01177,67469612,Atorstat 10mg Tablet,Atorvastatin (10mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-05,2026-05,Ward Store (Paeds),200,strip,2024-07-26,Apollo Wholesale Pvt Ltd
B01178,IP24G316,Zorem 1.25 Capsule,Ramipril (1.25mg),Capsule,Intas Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-09,ICU Store,10,strip,2024-10-26,Sanjivani Drug House
B01179,V2410-645,Cefadur CA 250mg Infusion,Cefuroxime (250mg),Infusion,Cipla Ltd,Antibiotic,2024-12,2027-12,OPD Pharmacy,20,bottle,2025-03-17,"Medline Distributors, Thiruvananthapuram"
B01180,I2410-643,Cefglobe S Injection,Cefoperazone (1000mg) + Sulbactam (1000mg),Injection,Micro Labs Ltd,Antibiotic,2024-04,2027-04,Main Pharmacy,10,vial/amp,2024-06-28,Sree Pharma Agencies
B01181,74343201,Januvia 25mg Tablet,Sitagliptin (25mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-02,2026-02,ICU Store,50,strip,2024-03-23,"Medline Distributors, Thiruvananthapuram"
B01182,TPI244687,Unimika 100mg Injection,Amikacin (100mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-10,2026-10,Emergency Store,40,vial/amp,2024-11-17,"Medline Distributors, Thiruvananthapuram"
B01183,CL24M718,Antiflu 12mg/ml Syrup,Oseltamivir Phosphate (12mg/ml),Syrup,Cipla Ltd,Antiviral,2024-11,2027-11,ICU Store,300,bottle,2025-01-27,Sree Pharma Agencies
B01184,LLT255206,Clopi 150mg Tablet,Clopidogrel (150mg),Tablet,Lupin Ltd,Cardiovascular,2024-11,2026-05,Main Pharmacy,60,strip,2024-12-17,Sree Pharma Agencies
B01185,23854626,Valparin Alkalets 250mg Tablet,Sodium Valproate (250mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2025-01,2026-07,Ward Store (Paeds),100,strip,2025-04-26,Kerala Medical Supplies Co.
B01186,16789850,Taxim-O 200 Tablet,Cefixime (200mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-02,2027-02,Main Pharmacy,100,strip,2024-05-19,"Medline Distributors, Thiruvananthapuram"
B01187,I2511-083,Panomp 40mg Injection,Pantoprazole (40mg),Injection,Torrent Pharmaceuticals Ltd,Gastro,2025-03,2027-03,Main Pharmacy,100,vial/amp,2025-05-07,Sree Pharma Agencies
B01188,I2406-704,Mepresso 1000mg Injection,Methylprednisolone (1000mg),Injection,Intas Pharmaceuticals Ltd,Steroid,2025-05,2028-05,Emergency Store,40,vial/amp,2025-07-15,Sree Pharma Agencies
B01189,68999002,Anofer 100mg Injection,Iron Sucrose (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2025-04,2027-04,OT Store,40,vial/amp,2025-04-29,Kerala Medical Supplies Co.
B01190,CPT244012,Onsett 8mg Tablet,Ondansetron (8mg),Tablet,Cadila Pharmaceuticals Ltd,Gastro,2024-03,2026-03,OT Store,40,strip,2024-06-19,Sanjivani Drug House
B01191,T2510-227,Ondem 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-08,2026-02,Ward Store (Paeds),10,strip,2024-11-16,Apollo Wholesale Pvt Ltd
B01192,SP25K624,Vecuron 10mg Injection,Vecuronium (10mg),Injection,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-01,2026-01,OPD Pharmacy,50,vial/amp,2024-02-02,Sree Pharma Agencies
B01193,SPT252872,Etoshine 120 Tablet,Etoricoxib (120mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2025-02,2027-02,ICU Store,120,strip,2025-03-05,Sree Pharma Agencies
B01194,84198767,Almox 100mg Oral Drops,Amoxycillin (100mg),Drops,Alkem Laboratories Ltd,Antibiotic,2024-12,2026-12,Main Pharmacy,50,bottle,2025-01-10,"Medline Distributors, Thiruvananthapuram"
B01195,49677387,Zovanta 20mg Tablet,Pantoprazole (20mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-10,2026-10,Ward Store (Paeds),0,strip,2025-01-27,Sree Pharma Agencies
B01196,MLT249502,Concor 10 Tablet,Bisoprolol (10mg),Tablet,Merck Ltd,Cardiovascular,2024-06,2026-06,Main Pharmacy,200,strip,2024-09-20,Sree Pharma Agencies
B01197,39517099,Rapifol 10mg Infusion,Propofol (10mg),Infusion,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-07,2026-07,Ward Store (Paeds),80,bottle,2024-10-22,"Medline Distributors, Thiruvananthapuram"
B01198,ZC25E559,Dexona 8mg Injection,Dexamethasone (8mg),Injection,Zydus Cadila,Steroid,2024-05,2027-05,OT Store,10,vial/amp,2024-05-27,Sree Pharma Agencies
B01199,16007154,Abd 200mg Suspension,Albendazole (200mg),Suspension,Intas Pharmaceuticals Ltd,Anthelmintic,2025-04,2027-04,Emergency Store,20,bottle,2025-05-15,Sree Pharma Agencies
B01200,31967075,Fulsed 1mg Injection,Midazolam (1mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-05,2025-11,OT Store,60,vial/amp,2024-08-23,Kerala Medical Supplies Co.
B01201,ALT248042,Almefkem 250 DT Tablet,Mefenamic Acid (250mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-03,2026-03,OPD Pharmacy,80,strip,2024-06-25,Malabar Pharma Distributors
B01202,LLS259445,Lupicip 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Lupin Ltd,Analgesic/Antipyretic,2024-08,2026-08,Main Pharmacy,120,bottle,2024-11-29,Apollo Wholesale Pvt Ltd
B01203,X2401-010,Candid Gold Dusting Powder,Allantoin (0.2% w/w) + Clotrimazole (1% w/w),Powder,Glenmark Pharmaceuticals Ltd,Antifungal,2024-06,2027-06,Ward Store (Paeds),150,pack,2024-07-13,Sree Pharma Agencies
B01204,SIX240801,Valparin 200 Oral Solution Delicious Pineapple,Sodium Valproate (200mg/5ml),Oral Solution,Sanofi India Ltd,Neurology/Psychiatry,2025-04,2026-10,Emergency Store,30,bottle,2025-07-15,Kerala Medical Supplies Co.
B01205,IPT256379,Levera 1000 Tablet,Levetiracetam (1000mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-11,2026-05,Emergency Store,40,strip,2025-02-25,Apollo Wholesale Pvt Ltd
B01206,AL25A790,Flukem 150mg Tablet,Fluconazole (150mg),Tablet,Alkem Laboratories Ltd,Antifungal,2024-07,2027-07,OT Store,0,strip,2024-09-15,Kerala Medical Supplies Co.
B01207,ALT251933,Esokem 20 Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-04,2027-04,Main Pharmacy,100,strip,2024-06-29,Sanjivani Drug House
B01208,IPT247334,T Glip 20 Tablet,Teneligliptin (20mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-02,2026-02,OT Store,0,strip,2024-03-10,Sree Pharma Agencies
B01209,ALT247340,Alsita 100mg Tablet,Sitagliptin (100mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-03,2027-03,OT Store,100,strip,2025-05-17,Sanjivani Drug House
B01210,S2502-921,Cetzine Syrup,Cetirizine (5mg/5ml),Syrup,Dr Reddy's Laboratories Ltd,Respiratory,2025-02,2027-02,Main Pharmacy,80,bottle,2025-05-02,Apollo Wholesale Pvt Ltd
B01211,T2412-266,LNZ 600 Tablet,Linezolid (600mg),Tablet,Lupin Ltd,Antibiotic,2025-01,2028-01,Ward Store (Paeds),0,strip,2025-02-27,Kerala Medical Supplies Co.
B01212,TPT250467,Conpres 12.5mg Tablet,Carvedilol (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-03,2026-09,Emergency Store,100,strip,2025-06-27,Malabar Pharma Distributors
B01213,MP24B594,Amlovas 2.5 Tablet,Amlodipine (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-12,2026-06,Emergency Store,50,strip,2025-01-12,Apollo Wholesale Pvt Ltd
B01214,ALT240609,Clavam 625 Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-03,2027-03,Emergency Store,80,strip,2025-05-16,Malabar Pharma Distributors
B01215,LH25H721,Alcidic 75mg Injection,Diclofenac (75mg),Injection,Leeford Healthcare Ltd,Analgesic/Antipyretic,2025-02,2027-02,Main Pharmacy,300,vial/amp,2025-03-01,Malabar Pharma Distributors
B01216,AT257654,Udiliv 450mg Tablet,Ursodeoxycholic Acid (450mg),Tablet,Abbott,Gastro,2025-05,2026-11,OPD Pharmacy,200,strip,2025-07-15,Malabar Pharma Distributors
B01217,CP25J163,Teli 20 Tablet,Telmisartan (20mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-06,2025-12,Emergency Store,60,strip,2024-08-16,"Medline Distributors, Thiruvananthapuram"
B01218,87666600,Tramef 50mg Injection,Tramadol (50mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-11,2027-11,Emergency Store,200,vial/amp,2025-02-10,Kerala Medical Supplies Co.
B01219,I2512-104,Merinta 1000mg Injection,Meropenem (1000mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2025-05,2028-05,OT Store,0,vial/amp,2025-06-11,"Medline Distributors, Thiruvananthapuram"
B01220,T2503-741,Metapro -XL 25 Tablet,Metoprolol Succinate (23.75mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-02,2027-02,Ward Store (Paeds),150,strip,2024-04-09,Sanjivani Drug House
B01221,ZC24C866,Aten 100 Tablet,Atenolol (100mg),Tablet,Zydus Cadila,Cardiovascular,2024-04,2026-04,OT Store,80,strip,2024-05-28,"Medline Distributors, Thiruvananthapuram"
B01222,T2405-941,Udcros 150mg Tablet,Ursodeoxycholic Acid (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-02,2028-02,Ward Store (Paeds),10,strip,2025-04-20,Kerala Medical Supplies Co.
B01223,IPC246392,DC 100mg Capsule,Doxycycline (100mg),Capsule,Intas Pharmaceuticals Ltd,Antibiotic,2024-09,2026-09,Main Pharmacy,10,strip,2024-11-18,Sanjivani Drug House
B01224,46840133,Dytor 20 Tablet,Torasemide (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2026-01,Ward Store (Paeds),120,strip,2024-07-27,Malabar Pharma Distributors
B01225,SP25H264,Budez CR Capsule,Budesonide (3mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2026-06,ICU Store,50,strip,2025-03-02,Malabar Pharma Distributors
B01226,TP24G362,Rostar-F Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,ICU Store,120,strip,2024-11-11,Kerala Medical Supplies Co.
B01227,CLT242076,Emeset 4 ODT Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-02,2026-02,ICU Store,30,strip,2024-05-28,"Medline Distributors, Thiruvananthapuram"
B01228,C2410-483,Microdox 100mg Capsule,Doxycycline (100mg),Capsule,Micro Labs Ltd,Antibiotic,2025-03,2028-03,Main Pharmacy,150,strip,2025-04-28,"Medline Distributors, Thiruvananthapuram"
B01229,IR25B157,Cyclopam 10mg Injection,Dicyclomine (10mg),Injection,Indoco Remedies Ltd,Gastro,2025-04,2028-04,OT Store,300,vial/amp,2025-07-04,Sree Pharma Agencies
B01230,WL25A956,Atrowok 0.6mg Injection,Atropine (0.6mg),Injection,Wockhardt Ltd,Anaesthesia/Critical care,2024-11,2027-11,ICU Store,120,vial/amp,2025-01-30,Sree Pharma Agencies
B01231,T2511-537,Covance 25 Tablet,Losartan (25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-08,2026-02,Ward Store (Paeds),60,strip,2024-08-26,Sree Pharma Agencies
B01232,I2507-134,Magnex Forte 1.5gm Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Pfizer Ltd,Antibiotic,2024-06,2026-06,Emergency Store,100,vial/amp,2024-08-12,"Medline Distributors, Thiruvananthapuram"
B01233,ZCT253320,Maxfor 1000mg Tablet SR,Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2025-03,2028-03,OT Store,150,strip,2025-03-28,Sanjivani Drug House
B01234,AT240747,Gluformin 500 Tablet,Metformin (500mg),Tablet,Abbott,Diabetes,2024-07,2026-07,Ward Store (Paeds),10,strip,2024-08-28,Sree Pharma Agencies
B01235,12483380,Zeet 12 Oral Suspension,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Alembic Pharmaceuticals Ltd,Respiratory,2025-03,2027-03,OT Store,150,bottle,2025-06-20,Apollo Wholesale Pvt Ltd
B01236,TPI248973,Tufzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-06,2025-12,OPD Pharmacy,10,vial/amp,2024-07-09,Sanjivani Drug House
B01237,AL25E849,Clindac A 1% Gel,Clindamycin (1% w/w),Gel,Alkem Laboratories Ltd,Antibiotic,2024-06,2026-06,OT Store,200,tube,2024-09-20,Sanjivani Drug House
B01238,31593455,Niftran 100mg Capsule,Nitrofurantoin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-11,2027-11,Emergency Store,20,strip,2025-01-05,Sanjivani Drug House
B01239,38935409,Amlodac T 40 mg/5 mg Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Zydus Cadila,Cardiovascular,2025-04,2027-04,Emergency Store,120,strip,2025-07-12,Sree Pharma Agencies
B01240,T2403-303,Vinglyn SR Tablet,Vildagliptin (100mg),Tablet,Zydus Cadila,Diabetes,2025-03,2027-03,Ward Store (Paeds),60,strip,2025-05-02,Kerala Medical Supplies Co.
B01241,MLT252034,Concor 10 Tablet,Bisoprolol (10mg),Tablet,Merck Ltd,Cardiovascular,2025-03,2027-03,OT Store,50,strip,2025-03-29,Kerala Medical Supplies Co.
B01242,LLT242697,Amipace 100 Tablet,Amiodarone (100mg),Tablet,Lupin Ltd,Cardiovascular,2025-03,2027-03,Main Pharmacy,120,strip,2025-04-10,Kerala Medical Supplies Co.
B01243,T2508-547,Januvia 50mg Tablet,Sitagliptin (50mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-09,2026-09,ICU Store,50,strip,2024-12-18,Kerala Medical Supplies Co.
B01244,I2402-374,Meconerv Injection,Methylcobalamin (500mcg),Injection,Micro Labs Ltd,Supplement,2025-01,2028-01,Main Pharmacy,200,vial/amp,2025-01-31,Sanjivani Drug House
B01245,CL25B258,Raniciz Junior Syrup,Ranitidine (75mg/5ml),Syrup,Cipla Ltd,Gastro,2024-04,2027-04,OT Store,120,bottle,2024-05-16,Malabar Pharma Distributors
B01246,CP24K142,Aciban 20 Tablet,Pantoprazole (20mg),Tablet,Cadila Pharmaceuticals Ltd,Gastro,2024-07,2027-07,ICU Store,40,strip,2024-10-01,Malabar Pharma Distributors
B01247,AL25L303,Swich 100 DT Tablet,Cefpodoxime Proxetil (100mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-04,2027-04,OT Store,150,strip,2024-05-24,Malabar Pharma Distributors
B01248,CL24E033,Amlip 10 Tablet,Amlodipine (10mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2027-03,Ward Store (Paeds),100,strip,2025-05-15,Sanjivani Drug House
B01249,81592930,Tonact 10 Tablet,Atorvastatin (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-02,2026-02,OT Store,150,strip,2024-05-02,"Medline Distributors, Thiruvananthapuram"
B01250,MPT255171,Mefomin 1000 SR Tablet,Metformin (1000mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Diabetes,2024-09,2026-03,OPD Pharmacy,150,strip,2024-10-08,Sree Pharma Agencies
B01251,TB24-0753A,Graficlav 625 Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Athens Life Sciences,Antibiotic,2024-11,2026-04,OT Store,200,strip,2025-02-06,Malabar Pharma Distributors
B01252,ML24E345,Spasypen 10mg Injection,Dicyclomine (10mg),Injection,Morepen Laboratories Ltd,Gastro,2025-05,2027-05,Main Pharmacy,200,vial/amp,2025-06-18,Sree Pharma Agencies
B01253,PF25A730,Compound Sodium Lacate Infusion,Ringer's lactate (NA),Infusion,Punjab Formulations Ltd,IV Fluids,2024-12,2026-12,OPD Pharmacy,20,bottle,2025-01-20,"Medline Distributors, Thiruvananthapuram"
B01254,SPI253545,Fulsed 1mg Injection,Midazolam (1mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-06,2027-06,Main Pharmacy,20,vial/amp,2024-09-01,"Medline Distributors, Thiruvananthapuram"
B01255,C2406-333,ROKO Capsule,Loperamide (2mg),Capsule,Cipla Ltd,Gastro,2025-03,2027-03,Ward Store (Paeds),60,strip,2025-05-17,Sanjivani Drug House
B01256,I2505-575,Unimika 100mg Injection,Amikacin (100mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-07,2026-07,Ward Store (Paeds),150,vial/amp,2024-10-03,Sree Pharma Agencies
B01257,IPT249755,Gabapin 100 Tablet,Gabapentin (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2025-12,Emergency Store,100,strip,2024-02-01,Sanjivani Drug House
B01258,13391969,Bandy-Plus 12 Tablet,Ivermectin (12mg) + Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2024-07,2027-07,Main Pharmacy,20,strip,2024-09-12,Malabar Pharma Distributors
B01259,DRT253332,Razo 10 Tablet,Rabeprazole (10mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-12,2026-12,OPD Pharmacy,120,strip,2025-01-17,Malabar Pharma Distributors
B01260,MP24G517,Acufix 100mg Tablet DT,Cefixime (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2025-03,2028-03,ICU Store,20,strip,2025-05-13,"Medline Distributors, Thiruvananthapuram"
B01261,WL25B649,Spasidex Drop,Dicyclomine (NA),Drops,Wockhardt Ltd,Gastro,2024-10,2026-10,Ward Store (Paeds),300,bottle,2024-10-30,Kerala Medical Supplies Co.
B01262,36136297,Tufzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-11,2026-05,Main Pharmacy,10,vial/amp,2024-12-30,"Medline Distributors, Thiruvananthapuram"
B01263,AL25F158,Flukem 150mg Tablet,Fluconazole (150mg),Tablet,Alkem Laboratories Ltd,Antifungal,2025-04,2027-04,Ward Store (Paeds),50,strip,2025-06-04,Kerala Medical Supplies Co.
B01264,75874779,Restyl 0.5mg Tablet SR,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-06,2027-06,Emergency Store,300,strip,2024-07-19,Kerala Medical Supplies Co.
B01265,IPT253337,Niftas 50 Tablet,Nitrofurantoin (50mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2027-02,Ward Store (Paeds),120,strip,2025-05-02,Apollo Wholesale Pvt Ltd
B01266,X2410-890,Omnacortil 0.1% Cream,Methylprednisolone (0.1% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Steroid,2025-03,2026-09,Ward Store (Paeds),30,tube,2025-05-21,Malabar Pharma Distributors
B01267,MP25J552,Januvia 100mg Tablet,Sitagliptin (100mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2025-01,2028-01,OPD Pharmacy,60,strip,2025-02-12,Kerala Medical Supplies Co.
B01268,I2406-521,Meronem 1000mg Injection,Meropenem (1000mg),Injection,AstraZeneca,Antibiotic,2025-05,2027-05,OPD Pharmacy,10,vial/amp,2025-06-23,Sree Pharma Agencies
B01269,IPX245212,Intadine 5% Ointment,Povidone Iodine (5%),Ointment,Intas Pharmaceuticals Ltd,Dermatology,2024-02,2027-02,Main Pharmacy,50,tube,2024-02-27,Malabar Pharma Distributors
B01270,T2407-069,Fentoin 100mg Tablet ER,Phenytoin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2027-07,ICU Store,100,strip,2024-09-16,Kerala Medical Supplies Co.
B01271,T2504-627,Linid Tablet,Linezolid (600mg),Tablet,Zydus Cadila,Antibiotic,2025-01,2027-01,OT Store,200,strip,2025-03-03,Sree Pharma Agencies
B01272,IPI249210,Valprol 100mg Injection,Sodium Valproate (100mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2027-03,Main Pharmacy,40,vial/amp,2024-04-14,Sanjivani Drug House
B01273,S2404-473,Sucrace Suspension,Sucralfate (1000mg),Suspension,Zydus Cadila,Gastro,2024-09,2026-09,OPD Pharmacy,200,bottle,2024-10-15,"Medline Distributors, Thiruvananthapuram"
B01274,I2508-880,Cydoxan 500mg Injection,Cyclophosphamide (500mg),Injection,Alkem Laboratories Ltd,Oncology,2024-02,2026-02,ICU Store,300,vial/amp,2024-03-26,Sanjivani Drug House
B01275,AP25J529,Supervac 10mg Injection,Vecuronium (10mg),Injection,Alembic Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-07,2027-07,Emergency Store,10,vial/amp,2024-08-04,Sree Pharma Agencies
B01276,ZC25G109,Ipramist 250mcg Inhaler,Ipratropium (250mcg),Inhaler,Zydus Cadila,Respiratory,2024-11,2026-11,OT Store,0,inhaler,2024-11-27,Apollo Wholesale Pvt Ltd
B01277,SP24G111,Oleanz 10 Tablet,Olanzapine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2026-07,Main Pharmacy,20,strip,2024-10-22,Sree Pharma Agencies
B01278,SPC250978,Clopilet A 150 Capsule,Aspirin (150mg) + Clopidogrel (75mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-05,2027-05,OT Store,0,strip,2025-07-10,Sree Pharma Agencies
B01279,IP24G588,Intacorlin 100mg Injection,Hydrocortisone (100mg),Injection,Intas Pharmaceuticals Ltd,Steroid,2024-03,2025-09,Ward Store (Paeds),10,vial/amp,2024-06-04,Kerala Medical Supplies Co.
B01280,T2501-376,Neurobion Alfa D Tablet,Methylcobalamin (1500mcg) + Alpha Lipoic Acid (100mg),Tablet,Merck Ltd,Supplement,2024-01,2027-01,Ward Store (Paeds),120,strip,2024-02-23,"Medline Distributors, Thiruvananthapuram"
B01281,97926734,Ranbiotic 40mg Injection,Gentamicin (40mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-09,2026-09,Main Pharmacy,200,vial/amp,2024-12-13,Kerala Medical Supplies Co.
B01282,60791859,Cortina DS 800mg/160mg Tablet,Sulfamethoxazole (800mg) + Trimethoprim (160mg),Tablet,Lupin Ltd,Antibiotic,2025-04,2028-04,Main Pharmacy,10,strip,2025-07-12,Apollo Wholesale Pvt Ltd
B01283,ALX245656,Tobrex Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alcon Laboratories,Ophthalmology,2025-02,2027-02,Emergency Store,150,bottle,2025-04-15,Sree Pharma Agencies
B01284,I2504-807,Enclex 40 Injection,Enoxaparin (40mg),Injection,Cipla Ltd,Anticoagulant,2024-05,2025-11,OT Store,80,vial/amp,2024-08-21,Kerala Medical Supplies Co.
B01285,37435471,Tromasol Infusion,Sodium Chloride (NA),Infusion,Intas Pharmaceuticals Ltd,IV Fluids,2025-05,2028-05,OPD Pharmacy,200,bottle,2025-07-01,Kerala Medical Supplies Co.
B01286,C2404-096,Macox 300mg Capsule,Rifampicin (300mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2024-11,2027-11,Emergency Store,200,strip,2024-12-07,Malabar Pharma Distributors
B01287,T2503-855,Esokem 20 Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2025-01,2027-01,OPD Pharmacy,300,strip,2025-04-24,Malabar Pharma Distributors
B01288,ZLT254479,Aldex 6mg Tablet SR,Dexchlorpheniramine (6mg),Tablet,Zee Laboratories,Anti-allergic,2025-02,2027-02,Ward Store (Paeds),100,strip,2025-05-24,Sree Pharma Agencies
B01289,V2505-890,Hospilid 200mg Infusion,Linezolid (200mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2025-03,2027-03,OPD Pharmacy,20,bottle,2025-05-28,Malabar Pharma Distributors
B01290,IPI251453,Ceroxitum 1500mg Injection,Cefuroxime (1500mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-07,2027-07,Emergency Store,30,vial/amp,2024-09-18,Sree Pharma Agencies
B01291,SPC250913,Gabantin 100 Capsule,Gabapentin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2026-01,Ward Store (Paeds),40,strip,2024-02-06,Malabar Pharma Distributors
B01292,88463726,Rapifol 10mg Infusion,Propofol (10mg),Infusion,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2025-01,2028-01,Main Pharmacy,50,bottle,2025-02-24,"Medline Distributors, Thiruvananthapuram"
B01293,SP24K712,Afenak Plus MR Tablet,Aceclofenac (NA) + Paracetamol (NA),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-03,2026-03,ICU Store,300,strip,2024-05-17,Apollo Wholesale Pvt Ltd
B01294,ALT243760,Esokem 20mg Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-11,2027-11,Emergency Store,150,strip,2025-01-08,Apollo Wholesale Pvt Ltd
B01295,ML24B317,Balgyl 400mg Tablet,Metronidazole (400mg),Tablet,Micro Labs Ltd,Antibiotic,2025-01,2028-01,OPD Pharmacy,80,strip,2025-03-18,Sree Pharma Agencies
B01296,A25C909,Meronem 500mg Injection,Meropenem (500mg),Injection,AstraZeneca,Antibiotic,2025-02,2028-02,Emergency Store,150,vial/amp,2025-05-07,Sree Pharma Agencies
B01297,89365865,Olymprix Tablet,Teneligliptin (20mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-05,2027-05,OPD Pharmacy,30,strip,2024-08-20,"Medline Distributors, Thiruvananthapuram"
B01298,30825995,Ufh 25000IU Injection,Heparin (25000IU),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2024-05,2026-05,ICU Store,100,vial/amp,2024-06-24,"Medline Distributors, Thiruvananthapuram"
B01299,UP25A804,Lyricare-GM Tablet,Gabapentin (300mg) + Methylcobalamin (500mcg),Tablet,Urvija Pharmaceuticals,Neurology/Psychiatry,2025-05,2027-05,OT Store,100,strip,2025-07-15,Malabar Pharma Distributors
B01300,T2508-599,Oropraz 20mg Tablet,Pantoprazole (20mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-01,2027-01,OT Store,20,strip,2024-04-08,"Medline Distributors, Thiruvananthapuram"
B01301,I2508-453,Monocef 250mg Injection,Ceftriaxone (250mg),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2024-07,2027-07,OPD Pharmacy,150,vial/amp,2024-09-20,Sanjivani Drug House
B01302,SP25D645,Fucidin Ointment,Sodium Fusidate (2% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Other,2024-05,2027-05,OPD Pharmacy,100,tube,2024-06-26,Apollo Wholesale Pvt Ltd
B01303,TPT257265,Alprax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-04,2025-10,Ward Store (Paeds),120,strip,2024-06-09,Malabar Pharma Distributors
B01304,S2404-806,Montek LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2026-12,Main Pharmacy,10,bottle,2025-02-16,Malabar Pharma Distributors
B01305,70779921,Bandy Suspension,Albendazole (200mg),Suspension,Mankind Pharma Ltd,Anthelmintic,2024-05,2027-05,OT Store,20,bottle,2024-06-12,Sanjivani Drug House
B01306,IP24M607,Intalol 50mg Tablet,Atenolol (50mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-04,2027-04,Main Pharmacy,0,strip,2024-06-28,Sree Pharma Agencies
B01307,BCT243571,Meftal 500 Tablet,Mefenamic Acid (500mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2024-02,2027-02,Main Pharmacy,20,strip,2024-03-21,Apollo Wholesale Pvt Ltd
B01308,ALX256308,Optibex Tear Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Alkem Laboratories Ltd,Ophthalmology,2025-05,2028-05,Ward Store (Paeds),100,bottle,2025-07-15,Apollo Wholesale Pvt Ltd
B01309,WMX251975,Betadine 10% Solution,Povidone Iodine (10% w/v),Solution,Win-Medicare Pvt Ltd,Dermatology,2025-01,2027-01,Emergency Store,120,bottle,2025-01-27,Sanjivani Drug House
B01310,I2403-037,Frusizex 10mg Injection,Furosemide (10mg/ml),Injection,Zee Laboratories,Cardiovascular,2024-11,2026-11,Main Pharmacy,30,vial/amp,2025-02-15,Kerala Medical Supplies Co.
B01311,DR24F618,Ketorol Injection,Ketorolac (30mg),Injection,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-12,2026-06,Ward Store (Paeds),80,vial/amp,2025-03-14,"Medline Distributors, Thiruvananthapuram"
B01312,PLI258033,Magnex Forte 1.5gm Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Pfizer Ltd,Antibiotic,2024-12,2026-06,ICU Store,30,vial/amp,2025-02-23,Sanjivani Drug House
B01313,BCT258661,Meftal 500 Tablet,Mefenamic Acid (500mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2024-09,2027-09,Ward Store (Paeds),100,strip,2024-11-18,Apollo Wholesale Pvt Ltd
B01314,SP24B462,Nexito 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2026-07,OT Store,50,strip,2024-09-03,Kerala Medical Supplies Co.
B01315,12782955,Afenak Plus MR Tablet,Aceclofenac (NA) + Paracetamol (NA),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-07,2027-07,Ward Store (Paeds),100,strip,2024-07-28,Sanjivani Drug House
B01316,X2401-707,Candid Ear Drop,Lidocaine (2% w/v) + Clotrimazole (1% w/v),Ear Drops,Glenmark Pharmaceuticals Ltd,Antifungal,2024-10,2026-04,OT Store,60,bottle,2024-11-09,Apollo Wholesale Pvt Ltd
B01317,SPI257540,Ivepred 1000mg Injection,Methylprednisolone (1000mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2024-06,2027-06,Ward Store (Paeds),60,vial/amp,2024-07-02,Sanjivani Drug House
B01318,T2404-592,Udiliv 300 Tablet,Ursodeoxycholic Acid (300mg),Tablet,Abbott,Gastro,2024-09,2027-09,Main Pharmacy,50,strip,2024-12-28,Malabar Pharma Distributors
B01319,T2508-974,Deplatt A 75 Tablet,Aspirin (75mg) + Clopidogrel (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-07,2027-07,Emergency Store,50,strip,2024-09-26,"Medline Distributors, Thiruvananthapuram"
B01320,ALV259181,Metrokem IV 100mg Infusion,Metronidazole (100mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-11,2026-11,ICU Store,40,bottle,2024-12-21,"Medline Distributors, Thiruvananthapuram"
B01321,SK24H936,Dex 25% Infusion,Dextrose (25% w/v),Infusion,Shree KrishnaKeshav Laboratories Ltd,IV Fluids,2024-03,2025-09,Main Pharmacy,40,bottle,2024-04-19,"Medline Distributors, Thiruvananthapuram"
B01322,58128991,R-Cin 300 Capsule,Rifampicin (300mg),Capsule,Lupin Ltd,Anti-TB,2024-12,2027-12,ICU Store,50,strip,2025-03-23,Sree Pharma Agencies
B01323,T2405-700,Bandy-Plus 12 Tablet,Ivermectin (12mg) + Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2024-04,2026-04,Main Pharmacy,20,strip,2024-05-28,Malabar Pharma Distributors
B01324,MP25B541,Accuzon 125mg Injection,Ceftriaxone (125mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2025-04,2028-04,Ward Store (Paeds),100,vial/amp,2025-07-09,Malabar Pharma Distributors
B01325,MP24E859,Mahapanta 40 Tablet,Pantoprazole (40mg),Tablet,Mankind Pharma Ltd,Gastro,2024-10,2026-04,OPD Pharmacy,40,strip,2025-01-04,Sree Pharma Agencies
B01326,ALT245170,Tamica-H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-11,2027-11,OPD Pharmacy,200,strip,2025-02-05,Sanjivani Drug House
B01327,CL25A261,Torodent-DT Tablet,Ketorolac (10mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-02,2026-02,ICU Store,50,strip,2024-04-26,Sanjivani Drug House
B01328,52869611,Cortina DS 800mg/160mg Tablet,Sulfamethoxazole (800mg) + Trimethoprim (160mg),Tablet,Lupin Ltd,Antibiotic,2025-04,2028-04,Main Pharmacy,150,strip,2025-06-11,Malabar Pharma Distributors
B01329,48931830,Acufix 100mg Tablet DT,Cefixime (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-09,2027-09,ICU Store,80,strip,2024-11-03,Kerala Medical Supplies Co.
B01330,SPT243099,Clopilet 150 Tablet,Clopidogrel (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2025-12,OPD Pharmacy,200,strip,2024-08-12,Sanjivani Drug House
B01331,T2402-235,Thyronorm 12.5mcg Tablet,Thyroxine (12.5mcg),Tablet,Abbott,Endocrine,2024-07,2026-07,Emergency Store,120,strip,2024-10-20,"Medline Distributors, Thiruvananthapuram"
B01332,MPX241320,Omnacortil 0.1% Cream,Methylprednisolone (0.1% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Steroid,2024-10,2026-10,Ward Store (Paeds),20,tube,2024-11-18,Sanjivani Drug House
B01333,S2507-612,Rantac Infant Syrup Mint,Ranitidine (75mg/5ml),Syrup,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-03,2026-03,OT Store,40,bottle,2024-06-01,Sanjivani Drug House
B01334,CL24B268,Exermet GM 0.5 Tablet SR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Cipla Ltd,Diabetes,2024-01,2027-01,Main Pharmacy,60,strip,2024-02-10,"Medline Distributors, Thiruvananthapuram"
B01335,V2501-703,Tromasol Infusion,Sodium Chloride (NA),Infusion,Intas Pharmaceuticals Ltd,IV Fluids,2025-02,2028-02,OT Store,60,bottle,2025-03-10,Malabar Pharma Distributors
B01336,65768929,Tamica-AM 40 Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-05,2027-05,Ward Store (Paeds),120,strip,2025-05-26,Sree Pharma Agencies
B01337,LH25A332,Amrox Oral Drops,Ambroxol (NA),Drops,Leeford Healthcare Ltd,Respiratory,2025-03,2026-09,OT Store,60,bottle,2025-06-23,"Medline Distributors, Thiruvananthapuram"
B01338,ALT253998,Amlogen 2.5mg Tablet,Amlodipine (2.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-01,2027-01,ICU Store,150,strip,2024-03-31,Sree Pharma Agencies
B01339,IP24H317,Tramatas 50mg Capsule,Tramadol (50mg),Capsule,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2027-02,Ward Store (Paeds),20,strip,2025-03-17,Kerala Medical Supplies Co.
B01340,65845729,Vida 25mg Tablet,Losartan (25mg),Tablet,Lupin Ltd,Cardiovascular,2024-11,2026-11,Emergency Store,50,strip,2024-12-03,Sanjivani Drug House
B01341,BGL24257,Azithromycin Suspension IP,Azithromycin (200mg/5ml),Suspension,Bestcare Formulations Pvt. Ltd.,Antibiotic,2024-10,2026-09,Ward Store (Paeds),120,bottle,2024-12-04,Sanjivani Drug House
B01342,20846331,Norflox Eye/Ear Drops,Norfloxacin (0.30%),Ear Drops,Cipla Ltd,Other,2025-03,2027-03,Ward Store (Paeds),50,bottle,2025-05-27,Sree Pharma Agencies
B01343,MPC248055,Fluvia 75mg Capsule,Oseltamivir Phosphate (75mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Antiviral,2024-08,2026-08,OT Store,120,strip,2024-09-26,Sree Pharma Agencies
B01344,CLI257642,Gentacip 40mg Injection,Gentamicin (40mg),Injection,Cipla Ltd,Antibiotic,2024-03,2025-09,OPD Pharmacy,200,vial/amp,2024-04-05,Kerala Medical Supplies Co.
B01345,TPT245421,Nexpro Fast 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-03,2026-03,Emergency Store,300,strip,2024-04-16,Apollo Wholesale Pvt Ltd
B01346,85554415,Wysolone 10 Tablet DT,Prednisolone (10mg),Tablet,Pfizer Ltd,Steroid,2024-06,2027-06,Main Pharmacy,80,strip,2024-08-03,Kerala Medical Supplies Co.
B01347,TPI252071,Benzosed 1mg Injection,Midazolam (1mg),Injection,Troikaa Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2027-05,OT Store,40,vial/amp,2024-05-28,Malabar Pharma Distributors
B01348,ALT248447,Almet 10mg Tablet,Metoclopramide (10mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-12,2027-12,Emergency Store,150,strip,2025-01-22,Kerala Medical Supplies Co.
B01349,MPT251206,Mefkind P 100mg Tablet,Mefenamic Acid (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-03,2027-03,OT Store,60,strip,2024-03-31,Sanjivani Drug House
B01350,T2509-616,Acivir 200 DT Tablet,Acyclovir (200mg),Tablet,Cipla Ltd,Antiviral,2024-01,2026-01,Emergency Store,120,strip,2024-02-14,Sanjivani Drug House
B01351,SP25K830,Sitared XR Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-11,2026-05,Main Pharmacy,100,strip,2025-01-18,Apollo Wholesale Pvt Ltd
B01352,I2510-514,Viatran 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Cipla Ltd,Antibiotic,2024-02,2027-02,OPD Pharmacy,200,vial/amp,2024-04-05,Apollo Wholesale Pvt Ltd
B01353,T2405-514,Flucobig 150mg Tablet,Fluconazole (150mg),Tablet,Torrent Pharmaceuticals Ltd,Antifungal,2024-04,2025-10,Emergency Store,50,strip,2024-06-04,Apollo Wholesale Pvt Ltd
B01354,AT247665,Lflox 500mg Tablet,Levofloxacin (500mg),Tablet,Abbott,Antibiotic,2024-10,2026-04,OT Store,20,strip,2024-12-01,"Medline Distributors, Thiruvananthapuram"
B01355,I2402-446,Cefbact 1000mg Injection,Ceftriaxone (1000mg),Injection,Cipla Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,0,vial/amp,2024-07-26,Kerala Medical Supplies Co.
B01356,CLT240478,Defshield Tablet,Deflazacort (6mg),Tablet,Cipla Ltd,Steroid,2024-12,2027-12,OPD Pharmacy,300,strip,2025-02-27,Apollo Wholesale Pvt Ltd
B01357,97241147,Stamlo 10 Tablet,Amlodipine (10mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-07,2026-07,ICU Store,20,strip,2024-09-02,"Medline Distributors, Thiruvananthapuram"
B01358,ALT255657,Acecloflam XP 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-10,2026-10,Main Pharmacy,20,strip,2024-12-24,Kerala Medical Supplies Co.
B01359,CLT243523,Amlopres TL 80mg/5mg Tablet,Telmisartan (80mg) + Amlodipine (5mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2027-03,Emergency Store,30,strip,2025-05-10,Kerala Medical Supplies Co.
B01360,69915762,Adrelin Injection,Adrenaline (NA),Injection,Klar Sehen Pvt Ltd,Anaesthesia/Critical care,2024-02,2026-02,Main Pharmacy,10,vial/amp,2024-03-19,Kerala Medical Supplies Co.
B01361,22730042,Mahapanta 40 Tablet,Pantoprazole (40mg),Tablet,Mankind Pharma Ltd,Gastro,2024-03,2027-03,OT Store,60,strip,2024-03-28,Sree Pharma Agencies
B01362,T2411-303,Voveran 50 GE Tablet,Diclofenac (50mg),Tablet,Novartis India Ltd,Analgesic/Antipyretic,2024-12,2026-06,Emergency Store,60,strip,2025-02-27,Apollo Wholesale Pvt Ltd
B01363,DR25H533,Novigan 400mg Tablet,Ibuprofen (400mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-08,2027-08,OT Store,20,strip,2024-09-30,"Medline Distributors, Thiruvananthapuram"
B01364,80270865,Urifast Capsule,Nitrofurantoin (100mg),Capsule,Cipla Ltd,Antibiotic,2025-05,2027-05,Main Pharmacy,80,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01365,T2410-536,Ativan 2mg Tablet,Lorazepam (2mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2025-04,2026-10,Main Pharmacy,100,strip,2025-05-11,Apollo Wholesale Pvt Ltd
B01366,ALT256677,Euclide 40 Tablet,Gliclazide (40mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-02,2026-02,OT Store,10,strip,2024-03-22,Apollo Wholesale Pvt Ltd
B01367,SP24B721,Astinol Inhaler,Salbutamol (NA),Inhaler,Sun Pharmaceutical Industries Ltd,Respiratory,2024-11,2026-11,ICU Store,0,inhaler,2025-01-23,Malabar Pharma Distributors
B01368,SPT242393,Trapex 1mg Tablet,Lorazepam (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2027-07,Ward Store (Paeds),30,strip,2024-09-09,"Medline Distributors, Thiruvananthapuram"
B01369,91034844,Manogyl 10% Infusion,Mannitol (10% w/v),Infusion,J B Chemicals and Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-03,2027-03,OPD Pharmacy,20,bottle,2024-06-14,Kerala Medical Supplies Co.
B01370,90622846,Gluvilda 50 Tablet,Vildagliptin (50mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-01,2026-08,ICU Store,0,strip,2024-02-04,Sree Pharma Agencies
B01371,AT257902,Udiliv 300 Tablet,Ursodeoxycholic Acid (300mg),Tablet,Abbott,Gastro,2025-02,2026-08,Ward Store (Paeds),80,strip,2025-04-05,Sanjivani Drug House
B01372,25319598,Dopar 200mg Injection,Dopamine (200mg),Injection,Samarth Life Sciences Pvt Ltd,Anaesthesia/Critical care,2024-01,2027-01,ICU Store,30,vial/amp,2024-03-21,Sanjivani Drug House
B01373,ZCS253306,Azimed 100mg Oral Suspension,Azithromycin (100mg),Suspension,Zydus Cadila,Antibiotic,2025-02,2027-02,Main Pharmacy,30,bottle,2025-03-17,"Medline Distributors, Thiruvananthapuram"
B01374,55504725,Flagyl 400 Tablet,Metronidazole (400mg),Tablet,Abbott,Antibiotic,2024-04,2027-04,Ward Store (Paeds),80,strip,2024-05-19,Apollo Wholesale Pvt Ltd
B01375,IP24E337,Genfour 0.5% Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2024-11,2027-11,Ward Store (Paeds),200,bottle,2024-12-23,Sanjivani Drug House
B01376,57216333,Doxt Injection Combipack,Doxycycline (100mg),Injection,Dr Reddy's Laboratories Ltd,Antibiotic,2024-08,2026-02,OT Store,50,vial/amp,2024-09-19,"Medline Distributors, Thiruvananthapuram"
B01377,ZCT247168,Klotfree Tablet,Clopidogrel (75mg),Tablet,Zydus Cadila,Cardiovascular,2024-04,2027-04,Main Pharmacy,20,strip,2024-07-24,Malabar Pharma Distributors
B01378,24EC721,NS – Sodium Chloride Injection IP,Sodium Chloride (0.9% w/v),Infusion,Pentagon Labs Ltd.,IV Fluids,2024-07,2026-06,ICU Store,10,bottle,2024-09-01,Kerala Medical Supplies Co.
B01379,AL25K451,Tprim Forte 800mg/160mg Tablet,Sulfamethoxazole (800mg) + Trimethoprim (160mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-03,2027-03,Main Pharmacy,300,strip,2024-05-18,Kerala Medical Supplies Co.
B01380,T2410-178,Maxfor 1000mg Tablet SR,Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2024-04,2026-04,Emergency Store,100,strip,2024-05-18,Kerala Medical Supplies Co.
B01381,ALI245713,Cydoxan 500mg Injection,Cyclophosphamide (500mg),Injection,Alkem Laboratories Ltd,Oncology,2024-06,2027-06,Ward Store (Paeds),150,vial/amp,2024-07-30,Malabar Pharma Distributors
B01382,ZCI258350,Gerpyrin 1000mg Injection,Paracetamol (1000mg),Injection,Zydus Cadila,Analgesic/Antipyretic,2024-12,2026-12,ICU Store,60,vial/amp,2025-03-23,"Medline Distributors, Thiruvananthapuram"
B01383,CPT254251,Calcirol XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cadila Pharmaceuticals Ltd,Supplement,2024-04,2025-10,OPD Pharmacy,300,strip,2024-07-04,Malabar Pharma Distributors
B01384,73650357,Rpitant 200mcg Tablet,Misoprostol (200mcg),Tablet,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-10,2026-10,Main Pharmacy,150,strip,2024-11-22,Sanjivani Drug House
B01385,X2502-189,Silver Sulfadiazine Cream,Silver Sulfadiazine (NA),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-06,2027-06,Ward Store (Paeds),10,tube,2024-08-11,Kerala Medical Supplies Co.
B01386,70942299,Aceclodus P 100 mg/500 mg Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Zydus Cadila,Analgesic/Antipyretic,2024-01,2027-01,Emergency Store,40,strip,2024-04-15,Malabar Pharma Distributors
B01387,PLT258927,Folvite 5mg Tablet,Folic Acid (5mg),Tablet,Pfizer Ltd,Haematology,2024-02,2027-02,ICU Store,40,strip,2024-03-07,Sanjivani Drug House
B01388,TP25L545,Unigenta Eye/Ear Drops,Gentamicin (15mg),Ear Drops,Torrent Pharmaceuticals Ltd,Antibiotic,2024-08,2026-08,Ward Store (Paeds),150,bottle,2024-10-22,Sree Pharma Agencies
B01389,EP25G203,Ibusoft 400mg Tablet,Dexibuprofen (400mg),Tablet,Emcure Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-02,2026-02,OT Store,300,strip,2024-03-05,Malabar Pharma Distributors
B01390,IPS250525,Lizintas 200mg Syrup,Linezolid (200mg),Syrup,Intas Pharmaceuticals Ltd,Antibiotic,2025-03,2027-03,ICU Store,300,bottle,2025-06-11,Kerala Medical Supplies Co.
B01391,S2401-155,Levtam 100mg Syrup,Levetiracetam (100mg),Syrup,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2026-08,OT Store,100,bottle,2024-04-02,Apollo Wholesale Pvt Ltd
B01392,T2506-897,Doxcef 100mg Tablet,Cefpodoxime Proxetil (100mg),Tablet,Lupin Ltd,Antibiotic,2025-03,2027-03,OT Store,40,strip,2025-04-08,Malabar Pharma Distributors
B01393,81722941,Fegold 100mg Injection,Iron Sucrose (100mg),Injection,Torrent Pharmaceuticals Ltd,Haematology,2025-03,2026-09,Main Pharmacy,50,vial/amp,2025-04-23,Apollo Wholesale Pvt Ltd
B01394,SPX253978,Sucral Cream,Sucralfate (7% w/w),Cream,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-07,2027-07,ICU Store,100,tube,2024-10-25,Apollo Wholesale Pvt Ltd
B01395,TPT250247,Xamic 250mg Tablet,Tranexamic Acid (250mg),Tablet,Torrent Pharmaceuticals Ltd,Haematology,2025-04,2028-04,ICU Store,200,strip,2025-06-21,Sree Pharma Agencies
B01396,T2408-605,Carca 12.5 Tablet,Carvedilol (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-01,Main Pharmacy,150,strip,2024-03-22,Apollo Wholesale Pvt Ltd
B01397,AL25D542,Mupikem Cream,Mupirocin (2% w/w),Cream,Alkem Laboratories Ltd,Dermatology,2024-10,2027-10,OPD Pharmacy,80,tube,2024-12-30,Kerala Medical Supplies Co.
B01398,MPT249154,Thyrox 100 Tablet,Thyroxine (100mcg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Endocrine,2024-11,2026-11,Emergency Store,150,strip,2025-02-16,"Medline Distributors, Thiruvananthapuram"
B01399,SP25G799,Niftran 100mg Capsule,Nitrofurantoin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2025-08,OT Store,40,strip,2024-03-03,Kerala Medical Supplies Co.
B01400,AL25L594,Remtrex 15mg Injection,Methotrexate (15mg),Injection,Alkem Laboratories Ltd,Oncology,2024-09,2026-09,OT Store,40,vial/amp,2024-11-25,Apollo Wholesale Pvt Ltd
B01401,CLX242323,Clearnoz 0.75% Nasal Drops,Sodium Chloride (0.75% w/v),Drops,Cipla Ltd,IV Fluids,2024-09,2027-09,ICU Store,200,bottle,2024-12-26,Sree Pharma Agencies
B01402,ZC24M783,Neomine 0.5mg Injection,Neostigmine (0.5mg),Injection,Zydus Cadila,Anaesthesia/Critical care,2025-02,2027-02,Emergency Store,100,vial/amp,2025-05-23,Apollo Wholesale Pvt Ltd
B01403,44014192,Abd 200mg Suspension,Albendazole (200mg),Suspension,Intas Pharmaceuticals Ltd,Anthelmintic,2025-05,2027-05,Ward Store (Paeds),0,bottle,2025-07-15,Malabar Pharma Distributors
B01404,IP25E897,Espin TM Tablet,S-Amlodipine (2.5mg) + Telmisartan (40mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-04,2026-04,OT Store,20,strip,2024-05-01,Sree Pharma Agencies
B01405,T2410-994,Amol 500mg Tablet,Paracetamol (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-04,2027-04,Main Pharmacy,30,strip,2025-07-05,Apollo Wholesale Pvt Ltd
B01406,MPT241275,Digitran 0.25mg Tablet,Digoxin (0.25mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2025-02,2028-02,OT Store,300,strip,2025-03-26,Sree Pharma Agencies
B01407,MLI244046,Gramocef 250mg Injection,Ceftriaxone (250mg),Injection,Micro Labs Ltd,Antibiotic,2025-03,2028-03,ICU Store,80,vial/amp,2025-05-15,Malabar Pharma Distributors
B01408,T2408-100,Pantocalm 40mg Tablet,Pantoprazole (40mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-09,2026-03,OT Store,20,strip,2024-10-01,Apollo Wholesale Pvt Ltd
B01409,53685675,Spironot 25 Tablet,Spironolactone (25mg),Tablet,Care Formulation Labs Pvt Ltd,Cardiovascular,2025-02,2026-08,Ward Store (Paeds),100,strip,2025-05-20,"Medline Distributors, Thiruvananthapuram"
B01410,TPT249984,Altipod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,OT Store,60,strip,2025-01-07,"Medline Distributors, Thiruvananthapuram"
B01411,MLT255959,Esofag 40 Tablet,Esomeprazole (40mg),Tablet,Micro Labs Ltd,Gastro,2024-03,2025-09,Emergency Store,60,strip,2024-05-25,Sree Pharma Agencies
B01412,CL25D968,Clocip Cream,Clotrimazole (1% w/w),Cream,Cipla Ltd,Antifungal,2024-05,2026-05,ICU Store,300,tube,2024-06-22,"Medline Distributors, Thiruvananthapuram"
B01413,22331322,Elate 5mg Tablet,Levocetirizine (5mg),Tablet,Lupin Ltd,Respiratory,2024-09,2026-09,OPD Pharmacy,150,strip,2024-10-21,Apollo Wholesale Pvt Ltd
B01414,70751681,Alerfex 120mg Tablet,Fexofenadine (120mg),Tablet,Cipla Ltd,Respiratory,2024-06,2027-06,OT Store,30,strip,2024-06-28,Sree Pharma Agencies
B01415,ML25E477,Diapride 1 Tablet,Glimepiride (1mg),Tablet,Micro Labs Ltd,Diabetes,2025-01,2026-07,Emergency Store,0,strip,2025-02-28,Malabar Pharma Distributors
B01416,T2504-763,Decotas 30mg Tablet,Deflazacort (30mg),Tablet,Intas Pharmaceuticals Ltd,Steroid,2025-02,2027-02,OPD Pharmacy,100,strip,2025-05-17,Kerala Medical Supplies Co.
B01417,T2506-216,Etozox 120mg Tablet,Etoricoxib (120mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2025-05,2027-05,ICU Store,120,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01418,IPT254857,Sartel H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-12,2027-12,Main Pharmacy,0,strip,2025-03-31,Sree Pharma Agencies
B01419,V2404-488,Fabitol 20% Infusion,Mannitol (20% w/v),Infusion,Elkos Healthcare Pvt Ltd,Anaesthesia/Critical care,2024-01,2026-01,Emergency Store,20,bottle,2024-04-21,Kerala Medical Supplies Co.
B01420,39222844,Weldinide 200mcg Inhaler,Budesonide (200mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-09,2026-03,Main Pharmacy,10,inhaler,2024-11-03,Sree Pharma Agencies
B01421,AL24H308,Becef 125mg Injection,Ceftriaxone (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-05,2027-05,Main Pharmacy,60,vial/amp,2024-08-24,Kerala Medical Supplies Co.
B01422,ZPT255827,Folizee 5mg Tablet,Folic Acid (5mg),Tablet,Zeelab Pharmacy Pvt Ltd,Haematology,2024-10,2027-10,Ward Store (Paeds),30,strip,2024-11-10,Apollo Wholesale Pvt Ltd
B01423,IPT244509,Domel 10mg Tablet,Domperidone (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-02,2028-02,OT Store,40,strip,2025-04-13,Sree Pharma Agencies
B01424,TP24F963,Aceclopure SP Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2026-08,ICU Store,80,strip,2025-03-28,Sanjivani Drug House
B01425,MPT254936,Janumet 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-12,2026-12,ICU Store,30,strip,2025-01-14,Sree Pharma Agencies
B01426,AL24A224,Levenue 1000 Tablet,Levetiracetam (1000mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-06,2026-06,Main Pharmacy,30,strip,2024-08-05,Apollo Wholesale Pvt Ltd
B01427,GP25K541,Olsivir Capsule,Oseltamivir Phosphate (75mg),Capsule,Glenmark Pharmaceuticals Ltd,Antiviral,2025-02,2028-02,Main Pharmacy,60,strip,2025-05-22,Sanjivani Drug House
B01428,ML24B112,Florobid 200mg Tablet,Ofloxacin (200mg),Tablet,Micro Labs Ltd,Antibiotic,2025-04,2028-04,Ward Store (Paeds),300,strip,2025-06-03,Kerala Medical Supplies Co.
B01429,A24A428,Thyronorm 100mcg Tablet,Thyroxine (100mcg),Tablet,Abbott,Endocrine,2024-04,2026-04,Emergency Store,200,strip,2024-06-22,Apollo Wholesale Pvt Ltd
B01430,T2404-608,Telday 80 AM Tablet,Telmisartan (80mg) + Amlodipine (5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-03,Ward Store (Paeds),150,strip,2024-10-07,Sree Pharma Agencies
B01431,CP24H112,CV Sprin 75mg Tablet,Aspirin (75mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-06,2025-12,OPD Pharmacy,200,strip,2024-08-21,Sree Pharma Agencies
B01432,53049249,Tromacyn Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2024-06,2026-06,Main Pharmacy,100,bottle,2024-07-25,Apollo Wholesale Pvt Ltd
B01433,SPT254657,Prazopress 1 Tablet,Prazosin (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-01,2026-01,ICU Store,60,strip,2024-04-07,Apollo Wholesale Pvt Ltd
B01434,C2407-525,Urifast Capsule,Nitrofurantoin (100mg),Capsule,Cipla Ltd,Antibiotic,2025-03,2027-03,ICU Store,10,strip,2025-06-26,Malabar Pharma Distributors
B01435,LLV244860,Lupigyl IV 500mg Infusion,Metronidazole (500mg),Infusion,Lupin Ltd,Antibiotic,2024-05,2025-11,Ward Store (Paeds),80,bottle,2024-08-06,Kerala Medical Supplies Co.
B01436,IP25G499,Monit GTN 2.6 Tablet CR,Nitroglycerin (2.6mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-03,2026-03,OT Store,50,strip,2024-04-20,Kerala Medical Supplies Co.
B01437,LHX253621,Welbusol 50mcg Inhaler,Levosalbutamol (50mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-12,2026-12,Main Pharmacy,120,inhaler,2025-02-16,Sanjivani Drug House
B01438,AL24D798,Gabata 400mg Capsule,Gabapentin (400mg),Capsule,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-11,2027-11,OPD Pharmacy,60,strip,2025-01-18,Sanjivani Drug House
B01439,84056415,Electrolyte M 5% Infusion,Dextrose (5% w/v),Infusion,Baxter India Pvt Ltd,IV Fluids,2025-05,2028-05,ICU Store,10,bottle,2025-07-15,Apollo Wholesale Pvt Ltd
B01440,CLX253902,Ceruclean Drop,Prednisolone (NA),Drops,Cipla Ltd,Steroid,2024-03,2026-03,OPD Pharmacy,20,bottle,2024-06-09,Malabar Pharma Distributors
B01441,IPI248653,NT Spas 10mg Injection,Dicyclomine (10mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2024-02,2026-02,OPD Pharmacy,100,vial/amp,2024-05-24,Apollo Wholesale Pvt Ltd
B01442,CLT246538,Dolex Tablet DT,Tramadol (NA),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-12,2027-12,OT Store,10,strip,2024-12-31,Malabar Pharma Distributors
B01443,T2502-390,Teleact 20 Tablet,Telmisartan (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-10,2027-10,OPD Pharmacy,120,strip,2024-12-25,Sree Pharma Agencies
B01444,51553395,Amrox Oral Drops,Ambroxol (NA),Drops,Leeford Healthcare Ltd,Respiratory,2024-07,2026-01,Main Pharmacy,60,bottle,2024-10-03,Apollo Wholesale Pvt Ltd
B01445,I2510-890,Gerzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Zydus Cadila,Antibiotic,2024-01,2027-01,OPD Pharmacy,40,vial/amp,2024-01-30,Sree Pharma Agencies
B01446,ALT256177,Jupiros 10 Tablet,Rosuvastatin (10mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-02,2026-08,Ward Store (Paeds),10,strip,2025-04-05,"Medline Distributors, Thiruvananthapuram"
B01447,T2505-782,Janumet 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-08,2027-08,Ward Store (Paeds),200,strip,2024-10-27,Malabar Pharma Distributors
B01448,SPS244858,Albaxy Suspension,Albendazole (200mg),Suspension,Sun Pharmaceutical Industries Ltd,Anthelmintic,2024-01,2027-01,Ward Store (Paeds),30,bottle,2024-01-26,Kerala Medical Supplies Co.
B01449,DR24E738,Zovanta 20mg Tablet,Pantoprazole (20mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-08,2026-02,Main Pharmacy,50,strip,2024-09-13,Apollo Wholesale Pvt Ltd
B01450,61154803,Angistat 2.5 Capsule TR,Nitroglycerin (2.5mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-02,2028-02,Main Pharmacy,10,strip,2025-03-02,Apollo Wholesale Pvt Ltd
B01451,42753017,Merixim 1000mg Injection,Meropenem (1000mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-08,2026-08,ICU Store,30,vial/amp,2024-10-07,Sree Pharma Agencies
B01452,DRT243146,Tryptomer 10mg Tablet,Amitriptyline (10mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2024-06,2025-12,ICU Store,40,strip,2024-07-09,Sree Pharma Agencies
B01453,AT253437,Rivotril 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Abbott,Neurology/Psychiatry,2024-05,2027-05,Emergency Store,100,strip,2024-07-17,Apollo Wholesale Pvt Ltd
B01454,CL25L745,Dytor 10 Tablet,Torasemide (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-06,2027-06,Main Pharmacy,100,strip,2024-08-27,Sanjivani Drug House
B01455,56665214,Safoban Ointment,Fusidic Acid (NA),Ointment,Micro Labs Ltd,Dermatology,2024-05,2026-05,OPD Pharmacy,60,tube,2024-07-27,"Medline Distributors, Thiruvananthapuram"
B01456,ZCT247471,Linid OD Tablet,Linezolid (1200mg),Tablet,Zydus Cadila,Antibiotic,2024-04,2027-04,OT Store,50,strip,2024-06-12,"Medline Distributors, Thiruvananthapuram"
B01457,CPI244575,Dianora 1mg Injection,Adrenaline (1mg),Injection,Cachet Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-11,2026-05,Ward Store (Paeds),150,vial/amp,2025-01-17,Apollo Wholesale Pvt Ltd
B01458,54434998,Omnacortil 2.5 Tablet DT,Prednisolone (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Steroid,2024-06,2026-06,OPD Pharmacy,40,strip,2024-08-11,Sanjivani Drug House
B01459,ZC24F385,Gerpyrin 1000mg Injection,Paracetamol (1000mg),Injection,Zydus Cadila,Analgesic/Antipyretic,2024-07,2026-07,Emergency Store,150,vial/amp,2024-08-17,Malabar Pharma Distributors
B01460,IPT251975,Veltam 0.2 Tablet MR,Tamsulosin (0.2mg),Tablet,Intas Pharmaceuticals Ltd,Urology,2025-04,2027-04,OT Store,120,strip,2025-07-15,Malabar Pharma Distributors
B01461,C2503-715,DC 100mg Capsule,Doxycycline (100mg),Capsule,Intas Pharmaceuticals Ltd,Antibiotic,2024-01,2027-01,Emergency Store,120,strip,2024-03-07,Kerala Medical Supplies Co.
B01462,CPT246793,Onsett 8mg Tablet,Ondansetron (8mg),Tablet,Cadila Pharmaceuticals Ltd,Gastro,2024-10,2026-10,OT Store,80,strip,2025-01-25,Sree Pharma Agencies
B01463,FLT247578,Zifi 200 Tablet,Cefixime (200mg),Tablet,FDC Ltd,Antibiotic,2025-01,2028-01,OT Store,300,strip,2025-02-12,Malabar Pharma Distributors
B01464,S2506-432,Ampoxin-CV 200mg/28.5mg Suspension,Amoxycillin (200mg) + Clavulanic Acid (28.5mg),Suspension,Torrent Pharmaceuticals Ltd,Antibiotic,2024-10,2026-10,Emergency Store,200,bottle,2024-12-26,Apollo Wholesale Pvt Ltd
B01465,C2403-210,TR Phyllin 125mg Capsule,Theophylline (125mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2025-02,2028-02,Ward Store (Paeds),100,strip,2025-04-24,Sanjivani Drug House
B01466,CL25F882,Asthalin 4 Tablet,Salbutamol (4mg),Tablet,Cipla Ltd,Respiratory,2024-01,2027-01,ICU Store,10,strip,2024-02-26,Apollo Wholesale Pvt Ltd
B01467,71608453,Tenepla Tablet,Teneligliptin (20mg),Tablet,Cipla Ltd,Diabetes,2025-05,2026-11,OT Store,20,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01468,LH25L087,Cavmox 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Leeford Healthcare Ltd,Antibiotic,2025-01,2027-01,ICU Store,10,vial/amp,2025-03-12,Sanjivani Drug House
B01469,AT258591,Abamlo 5 Tablet,Amlodipine (5mg),Tablet,Abbott,Cardiovascular,2024-07,2027-07,Main Pharmacy,300,strip,2024-08-13,Kerala Medical Supplies Co.
B01470,CL25C639,Urimax 0.4 Ecopack Capsule MR,Tamsulosin (400mcg),Capsule,Cipla Ltd,Urology,2024-06,2026-06,Emergency Store,80,strip,2024-09-06,Malabar Pharma Distributors
B01471,MLI248768,BIOFER S 100mg/5ml Injection,Iron Sucrose (100mg/5ml),Injection,Micro Labs Ltd,Haematology,2024-08,2026-02,ICU Store,0,vial/amp,2024-11-15,Kerala Medical Supplies Co.
B01472,I2402-754,Vancogram 500mg Injection,Vancomycin (500mg),Injection,Biochem Pharmaceutical Industries,Antibiotic,2025-01,2026-07,OT Store,300,vial/amp,2025-04-11,Sree Pharma Agencies
B01473,ALI249146,Merosure 125mg Injection,Meropenem (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,300,vial/amp,2024-06-30,"Medline Distributors, Thiruvananthapuram"
B01474,TP24A910,Domstal 5 DT Tablet,Domperidone (5mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-11,2027-11,Main Pharmacy,10,strip,2025-01-27,"Medline Distributors, Thiruvananthapuram"
B01475,ZCI245094,Xylocaine 4% Injection,Lidocaine (4%),Injection,Zydus Cadila,Other,2025-04,2027-04,Emergency Store,50,vial/amp,2025-05-17,Apollo Wholesale Pvt Ltd
B01476,78043121,Dalcinex 150mg Injection,Clindamycin (150mg),Injection,Cipla Ltd,Antibiotic,2025-05,2026-11,OT Store,60,vial/amp,2025-06-08,Kerala Medical Supplies Co.
B01477,30503941,Monit GTN 2.6 Tablet CR,Nitroglycerin (2.6mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-03,2026-03,Ward Store (Paeds),20,strip,2024-04-13,Sanjivani Drug House
B01478,LL25K631,Glador M 1 Forte Tablet PR,Glimepiride (1mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2024-03,2025-09,ICU Store,40,strip,2024-06-10,Sanjivani Drug House
B01479,LH25B996,Wellamo 10 Tablet,Amlodipine (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-01,2027-01,Ward Store (Paeds),10,strip,2024-04-13,Malabar Pharma Distributors
B01480,AI243930,Lofh 25000IU Injection,Heparin (25000IU),Injection,Abbott,Anticoagulant,2024-04,2026-04,Main Pharmacy,20,vial/amp,2024-04-27,Sree Pharma Agencies
B01481,55769312,TR Phyllin 125mg Capsule,Theophylline (125mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2025-05,2027-05,OT Store,200,strip,2025-07-15,Malabar Pharma Distributors
B01482,AP24L679,Azithral 500mg Injection,Azithromycin (500mg),Injection,Alembic Pharmaceuticals Ltd,Antibiotic,2024-03,2027-03,Main Pharmacy,10,vial/amp,2024-06-16,Apollo Wholesale Pvt Ltd
B01483,ALI252869,Drotanic Injection,Drotaverine (20mg),Injection,Alkem Laboratories Ltd,Gastro,2024-08,2026-02,Ward Store (Paeds),40,vial/amp,2024-11-18,Kerala Medical Supplies Co.
B01484,IPX257694,Esivac Oral Solution,Lactulose (3.335gm/5ml),Oral Solution,Intas Pharmaceuticals Ltd,Gastro,2024-05,2027-05,Ward Store (Paeds),60,bottle,2024-08-18,Kerala Medical Supplies Co.
B01485,LLT259169,Elate 5mg Tablet,Levocetirizine (5mg),Tablet,Lupin Ltd,Respiratory,2025-02,2026-08,Main Pharmacy,100,strip,2025-04-10,Kerala Medical Supplies Co.
B01486,T2510-552,Bestocef 100mg Tablet,Cefixime (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2027-10,Ward Store (Paeds),30,strip,2024-12-30,"Medline Distributors, Thiruvananthapuram"
B01487,42835306,Nitrogard 2.6mg Tablet,Nitroglycerin (2.6mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2026-07,Main Pharmacy,150,strip,2024-08-03,Sanjivani Drug House
B01488,CLX254130,Aprovent Inhaler,Ipratropium (NA),Inhaler,Cipla Ltd,Respiratory,2024-12,2026-06,OT Store,0,inhaler,2025-03-16,Sanjivani Drug House
B01489,LHS243297,Leemol 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-08,2026-08,OPD Pharmacy,100,bottle,2024-11-08,Kerala Medical Supplies Co.
B01490,AP24F592,Zeet 12 Oral Suspension,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Alembic Pharmaceuticals Ltd,Respiratory,2024-11,2027-11,OPD Pharmacy,60,bottle,2024-11-26,"Medline Distributors, Thiruvananthapuram"
B01491,29747600,Metrocip 500mg Infusion,Metronidazole (500mg),Infusion,Cipla Ltd,Antibiotic,2025-05,2026-11,OPD Pharmacy,150,bottle,2025-07-15,Sanjivani Drug House
B01492,39009803,Refresh Tears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Allergan India Pvt Ltd,Ophthalmology,2024-06,2027-06,OPD Pharmacy,40,bottle,2024-09-01,"Medline Distributors, Thiruvananthapuram"
B01493,SIT259400,Combiflam Tablet,Ibuprofen (400mg) + Paracetamol (325mg),Tablet,Sanofi India Ltd,Analgesic/Antipyretic,2024-05,2027-05,Emergency Store,20,strip,2024-08-06,Sree Pharma Agencies
B01494,TPT246091,Hqtor 300mg Tablet,Hydroxychloroquine (300mg),Tablet,Torrent Pharmaceuticals Ltd,Antimalarial,2024-11,2027-11,OT Store,30,strip,2024-12-14,Sree Pharma Agencies
B01495,SPC253742,Budez CR Capsule,Budesonide (3mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2026-12,OT Store,300,strip,2025-03-25,Kerala Medical Supplies Co.
B01496,CLC242165,Urifast Capsule,Nitrofurantoin (100mg),Capsule,Cipla Ltd,Antibiotic,2025-04,2027-04,Ward Store (Paeds),20,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B01497,T2406-501,Cifran 100 Tablet,Ciprofloxacin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-04,2025-10,OPD Pharmacy,80,strip,2024-07-11,Apollo Wholesale Pvt Ltd
B01498,AL25G734,Acdof 40mg Injection,Pantoprazole (40mg),Injection,Alkem Laboratories Ltd,Gastro,2024-04,2026-04,ICU Store,20,vial/amp,2024-06-08,Malabar Pharma Distributors
B01499,56000822,Fluka 150 Tablet,Fluconazole (150mg),Tablet,Cipla Ltd,Antifungal,2024-06,2027-06,OPD Pharmacy,50,strip,2024-08-27,Sree Pharma Agencies
B01500,MP24G272,Omnacortil 2.5 Tablet DT,Prednisolone (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Steroid,2024-11,2026-11,ICU Store,200,strip,2025-02-03,"Medline Distributors, Thiruvananthapuram"
B01501,T2504-671,Rivotril 2mg Tablet,Clonazepam (2mg),Tablet,Abbott,Neurology/Psychiatry,2024-10,2026-10,Main Pharmacy,20,strip,2024-10-26,Kerala Medical Supplies Co.
B01502,CL24C159,Rosugard 5mg Tablet,Rosuvastatin (5mg),Tablet,Cipla Ltd,Cardiovascular,2024-12,2027-12,Main Pharmacy,0,strip,2025-01-10,"Medline Distributors, Thiruvananthapuram"
B01503,LLT247672,Lupimox 125mg Tablet,Amoxycillin (125mg),Tablet,Lupin Ltd,Antibiotic,2024-02,2026-02,Ward Store (Paeds),10,strip,2024-02-29,Malabar Pharma Distributors
B01504,A24B064,R-Ppi 20mg Tablet,Rabeprazole (20mg),Tablet,Abbott,Gastro,2024-05,2027-05,Ward Store (Paeds),30,strip,2024-07-12,Sree Pharma Agencies
B01505,I2402-398,Susten 100 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2025-01,2028-01,Ward Store (Paeds),40,vial/amp,2025-04-20,Malabar Pharma Distributors
B01506,CL24M359,Antiflu 12mg/ml Syrup,Oseltamivir Phosphate (12mg/ml),Syrup,Cipla Ltd,Antiviral,2024-09,2027-09,OT Store,0,bottle,2024-10-30,Kerala Medical Supplies Co.
B01507,LA1TE012,Labetalol Tablets IP,Labetalol (100mg),Tablet,Unicure India Ltd.,Cardiovascular,2024-08,2026-07,Ward Store (Paeds),30,strip,2024-08-29,Sree Pharma Agencies
B01508,ML25B510,Atepres 50mg Tablet,Atenolol (50mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-09,2026-03,Emergency Store,60,strip,2024-10-16,"Medline Distributors, Thiruvananthapuram"
B01509,IPT256746,Olimelt 10 Tablet MD,Olanzapine (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-01,2027-01,ICU Store,100,strip,2025-03-16,"Medline Distributors, Thiruvananthapuram"
B01510,APT254081,Azithral 500 Tablet,Azithromycin (500mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2025-04,2028-04,OT Store,300,strip,2025-06-25,Sree Pharma Agencies
B01511,93806250,Rostar-F Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-02,2028-02,OPD Pharmacy,100,strip,2025-05-29,Apollo Wholesale Pvt Ltd
B01512,C2407-591,Stradol 50mg Capsule,Tramadol (50mg),Capsule,Lupin Ltd,Analgesic/Antipyretic,2024-01,2026-01,Main Pharmacy,100,strip,2024-03-06,Kerala Medical Supplies Co.
B01513,CL24D416,Urilosin 0.2mg Tablet,Tamsulosin (0.2mg),Tablet,Cipla Ltd,Urology,2024-12,2026-12,Emergency Store,20,strip,2025-03-05,Apollo Wholesale Pvt Ltd
B01514,TP24B345,Maxi 500mg Tablet,Mefenamic Acid (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-12,2027-12,OPD Pharmacy,120,strip,2025-03-02,Kerala Medical Supplies Co.
B01515,AL25G772,Normal Saline 0.9% Infusion,Sodium Chloride (0.9% w/v),Infusion,Alkem Laboratories Ltd,IV Fluids,2025-01,2027-01,OT Store,300,bottle,2025-02-17,Kerala Medical Supplies Co.
B01516,TPI254507,Troymag 50% Injection,Magnesium Sulphate (50% w/v),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-09,2026-09,Main Pharmacy,50,vial/amp,2024-10-22,Sanjivani Drug House
B01517,TPS254010,Lezyncet 2.5mg/5ml Syrup,Levocetirizine (2.5mg/5ml),Syrup,Torrent Pharmaceuticals Ltd,Respiratory,2024-07,2026-07,ICU Store,0,bottle,2024-09-19,"Medline Distributors, Thiruvananthapuram"
B01518,CLT255091,Forcan 100mg Tablet DT,Fluconazole (100mg),Tablet,Cipla Ltd,Antifungal,2024-11,2026-11,ICU Store,80,strip,2024-12-08,Malabar Pharma Distributors
B01519,SPT248176,Etoshine 120 Tablet,Etoricoxib (120mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2025-02,2026-08,Emergency Store,300,strip,2025-05-02,Apollo Wholesale Pvt Ltd
B01520,C2501-781,Pregalin 100mg Capsule,Pregabalin (100mg),Capsule,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2027-07,OT Store,50,strip,2024-08-09,Malabar Pharma Distributors
B01521,86187341,Acostin 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-07,2026-07,OT Store,40,vial/amp,2024-10-15,Malabar Pharma Distributors
B01522,ALI243561,Hycort 100mg Injection,Hydrocortisone (100mg),Injection,Alkem Laboratories Ltd,Steroid,2025-01,2027-01,ICU Store,300,vial/amp,2025-02-26,"Medline Distributors, Thiruvananthapuram"
B01523,S2407-059,Bro Cofdex Plus Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Cipla Ltd,Respiratory,2024-06,2026-06,OT Store,50,bottle,2024-08-21,Sanjivani Drug House
B01524,68900892,Doloban 100mg Tablet SR,Diclofenac (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-05,2026-05,Ward Store (Paeds),50,strip,2024-08-14,Apollo Wholesale Pvt Ltd
B01525,67713148,Tachyra 100 Tablet,Amiodarone (100mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2025-11,OT Store,60,strip,2024-08-13,Sanjivani Drug House
B01526,TP25J632,Cipride 200mg Infusion,Ciprofloxacin (200mg),Infusion,Torrent Pharmaceuticals Ltd,Antibiotic,2024-05,2026-05,OT Store,100,bottle,2024-07-28,"Medline Distributors, Thiruvananthapuram"
B01527,64764506,Doxicip Injection,Doxycycline (100mg),Injection,Cipla Ltd,Antibiotic,2024-01,2026-01,Main Pharmacy,100,vial/amp,2024-04-07,Kerala Medical Supplies Co.
B01528,ZC24F689,Angionox 40mg Injection,Enoxaparin (40mg),Injection,Zydus Cadila,Anticoagulant,2024-11,2026-05,Emergency Store,120,vial/amp,2024-12-29,"Medline Distributors, Thiruvananthapuram"
B01529,CP25K827,Labepure 20mg Injection,Labetalol (20mg),Injection,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,Ward Store (Paeds),150,vial/amp,2024-09-18,Apollo Wholesale Pvt Ltd
B01530,70933337,Oncotrex 2.5mg Tablet,Methotrexate (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Oncology,2024-09,2026-09,Emergency Store,50,strip,2024-11-08,Sree Pharma Agencies
B01531,X2407-465,Cipladine Ointment,Povidone Iodine (10% w/w),Ointment,Cipla Ltd,Dermatology,2025-04,2028-04,Ward Store (Paeds),40,tube,2025-05-08,Sanjivani Drug House
B01532,88429608,Glador 1 Tablet,Glimepiride (1mg),Tablet,Lupin Ltd,Diabetes,2024-05,2026-05,Main Pharmacy,50,strip,2024-08-03,Apollo Wholesale Pvt Ltd
B01533,54226861,Verifica 100mg Tablet SR,Vildagliptin (100mg),Tablet,Lupin Ltd,Diabetes,2024-09,2026-03,OPD Pharmacy,20,strip,2024-10-08,Sanjivani Drug House
B01534,MLT253848,Astin 10 Tablet,Atorvastatin (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-03,2025-09,OT Store,300,strip,2024-06-28,Kerala Medical Supplies Co.
B01535,IPT259062,Intaglip OD 100mg Tablet,Vildagliptin (100mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2025-01,2026-07,Ward Store (Paeds),150,strip,2025-01-27,Malabar Pharma Distributors
B01536,37663707,Foly-Act Tablet,Folic Acid (5mg),Tablet,Morepen Laboratories Ltd,Haematology,2025-05,2027-05,OPD Pharmacy,80,strip,2025-07-15,Sanjivani Drug House
B01537,66688023,Merocrit 0.5gm Injection,Meropenem (500mg),Injection,Cipla Ltd,Antibiotic,2024-03,2027-03,OT Store,20,vial/amp,2024-05-10,Malabar Pharma Distributors
B01538,PL24L674,Ativan 1mg Tablet,Lorazepam (1mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2024-12,2027-12,OT Store,100,strip,2025-02-19,Kerala Medical Supplies Co.
B01539,CPT255515,Isoniazid 300mg Tablet,Isoniazid (300mg),Tablet,Cadila Pharmaceuticals Ltd,Anti-TB,2025-04,2028-04,Emergency Store,120,strip,2025-05-25,Apollo Wholesale Pvt Ltd
B01540,LLS246449,Lupibend 200mg Suspension,Albendazole (200mg),Suspension,Lupin Ltd,Anthelmintic,2024-01,2027-01,OPD Pharmacy,10,bottle,2024-04-07,Malabar Pharma Distributors
B01541,I2506-845,Cathflush 10IU Injection,Heparin (10IU),Injection,Troikaa Pharmaceuticals Ltd,Anticoagulant,2025-01,2028-01,Main Pharmacy,60,vial/amp,2025-02-28,Sanjivani Drug House
B01542,LLI243604,Amikef 100mg Injection,Amikacin (100mg),Injection,Lupin Ltd,Antibiotic,2024-07,2027-07,ICU Store,150,vial/amp,2024-08-16,Malabar Pharma Distributors
B01543,IPT246294,Flolev 750mg Tablet,Levofloxacin (750mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-11,2026-11,Main Pharmacy,150,strip,2024-12-29,Kerala Medical Supplies Co.
B01544,T2505-158,Monit GTN 2.6 Tablet CR,Nitroglycerin (2.6mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-05,Ward Store (Paeds),100,strip,2025-01-09,Malabar Pharma Distributors
B01545,SPX257232,Fucidin Ointment,Sodium Fusidate (2% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Other,2025-02,2027-02,ICU Store,300,tube,2025-05-09,Sanjivani Drug House
B01546,IPC256448,Histacet 10mg Capsule,Cetirizine (10mg),Capsule,Intas Pharmaceuticals Ltd,Respiratory,2024-09,2027-09,OT Store,20,strip,2024-11-17,Sree Pharma Agencies
B01547,SPT242278,Histac 150 Tablet,Ranitidine (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-09,2026-03,Emergency Store,60,strip,2024-10-20,Sree Pharma Agencies
B01548,TPT244923,Telday-H Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-03,2026-03,OT Store,300,strip,2024-04-13,Apollo Wholesale Pvt Ltd
B01549,MLT254544,Concor 5 Tablet,Bisoprolol (5mg),Tablet,Merck Ltd,Cardiovascular,2025-04,2027-04,ICU Store,120,strip,2025-05-05,"Medline Distributors, Thiruvananthapuram"
B01550,98486242,Isomin 20mg Tablet,Isosorbide Mononitrate (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-12,2026-12,OPD Pharmacy,30,strip,2025-03-23,Sree Pharma Agencies
B01551,SII245253,Clexane 20mg Injection,Enoxaparin (20mg),Injection,Sanofi India Ltd,Anticoagulant,2024-04,2027-04,Main Pharmacy,50,vial/amp,2024-05-28,Apollo Wholesale Pvt Ltd
B01552,S2407-140,Lupidom 5mg Suspension,Domperidone (5mg),Suspension,Lupin Ltd,Gastro,2024-03,2027-03,OT Store,40,bottle,2024-03-26,Sanjivani Drug House
B01553,SI24A248,Combiflam Tablet,Ibuprofen (400mg) + Paracetamol (325mg),Tablet,Sanofi India Ltd,Analgesic/Antipyretic,2024-07,2026-07,Main Pharmacy,30,strip,2024-10-11,Sanjivani Drug House
B01554,IPT253460,Levera 1000 Tablet,Levetiracetam (1000mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2026-07,Main Pharmacy,120,strip,2024-08-19,Apollo Wholesale Pvt Ltd
B01555,TPT259167,Domstal 10mg Tablet,Domperidone (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-03,2028-03,OPD Pharmacy,80,strip,2025-04-16,Sanjivani Drug House
B01556,API251630,Monocef 250mg Injection,Ceftriaxone (250mg),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2024-11,2026-05,ICU Store,150,vial/amp,2024-12-26,Sree Pharma Agencies
B01557,36969824,Zithrox 100 Rediuse Suspension,Azithromycin (100mg/5ml),Suspension,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-08,2027-08,OPD Pharmacy,200,bottle,2024-09-02,Sree Pharma Agencies
B01558,95904169,Lonazep 0.25 Tablet,Clonazepam (0.25mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-11,2026-11,OPD Pharmacy,300,strip,2025-02-02,Sanjivani Drug House
B01559,MLT250205,Balgyl 400mg Tablet,Metronidazole (400mg),Tablet,Micro Labs Ltd,Antibiotic,2024-04,2026-04,Ward Store (Paeds),120,strip,2024-06-27,Sree Pharma Agencies
B01560,95434927,Recosulin N 100IU Injection,Insulin Isophane (100IU),Injection,Shreya Life Sciences Pvt Ltd,Diabetes,2025-05,2026-11,ICU Store,300,vial/amp,2025-07-15,Malabar Pharma Distributors
B01561,TPT255740,Ursetor 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-10,2027-10,Emergency Store,60,strip,2024-11-12,Apollo Wholesale Pvt Ltd
B01562,A25C163,Abmetop 25 XL Tablet,Metoprolol Succinate (23.75mg),Tablet,Abbott,Cardiovascular,2024-06,2025-12,OT Store,40,strip,2024-09-10,Sree Pharma Agencies
B01563,SP24K731,Dapefy 10mg Tablet,Dapagliflozin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-05,2027-05,Emergency Store,30,strip,2025-05-29,Kerala Medical Supplies Co.
B01564,CLT251522,Esomac 40 Tablet,Esomeprazole (40mg),Tablet,Cipla Ltd,Gastro,2024-01,2026-11,Emergency Store,40,strip,2024-03-26,"Medline Distributors, Thiruvananthapuram"
B01565,TPT249531,Telday 20 Tablet,Telmisartan (20mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-07,OT Store,0,strip,2024-08-30,Malabar Pharma Distributors
B01566,46738721,C One 1000mg Injection,Ceftriaxone (1000mg),Injection,Abbott,Antibiotic,2024-10,2027-10,Main Pharmacy,200,vial/amp,2025-01-22,Sanjivani Drug House
B01567,AT256411,Forxiga 10mg Tablet,Dapagliflozin (10mg),Tablet,AstraZeneca,Diabetes,2024-06,2027-06,OT Store,40,strip,2024-06-27,Apollo Wholesale Pvt Ltd
B01568,JBS254276,Rantac Infant Syrup Mint,Ranitidine (75mg/5ml),Syrup,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-03,2025-09,Ward Store (Paeds),20,bottle,2024-05-12,Apollo Wholesale Pvt Ltd
B01569,SI25H821,Valparin Alkalets 500 Tablet,Sodium Valproate (500mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2024-09,2027-09,Main Pharmacy,120,strip,2024-11-26,Sanjivani Drug House
B01570,I2512-829,Platikem 20mg Injection,Cisplatin (20mg),Injection,Alkem Laboratories Ltd,Oncology,2024-05,2027-05,ICU Store,30,vial/amp,2024-08-22,"Medline Distributors, Thiruvananthapuram"
B01571,TPX259924,Unidine Solution 100 ml,Povidone Iodine (NA),Solution,Torrent Pharmaceuticals Ltd,Dermatology,2024-03,2027-03,Main Pharmacy,300,bottle,2024-04-29,Apollo Wholesale Pvt Ltd
B01572,T2411-100,Lupimectin 12mg Tablet,Ivermectin (12mg),Tablet,Lupin Ltd,Anthelmintic,2024-08,2026-08,Main Pharmacy,10,strip,2024-09-03,"Medline Distributors, Thiruvananthapuram"
B01573,76632538,ESGIPYRIN DS INJECTION,Diclofenac (25mg/ml),Injection,Abbott,Analgesic/Antipyretic,2024-09,2027-09,Emergency Store,30,vial/amp,2024-10-07,"Medline Distributors, Thiruvananthapuram"
B01574,LLT244624,Verifica 100mg Tablet SR,Vildagliptin (100mg),Tablet,Lupin Ltd,Diabetes,2024-01,2026-01,ICU Store,60,strip,2024-03-29,Sree Pharma Agencies
B01575,18891570,Ibrumac 200mg Tablet,Ibuprofen (200mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-08,2026-02,Main Pharmacy,150,strip,2024-10-03,"Medline Distributors, Thiruvananthapuram"
B01576,ALI248590,Platikem 20mg Injection,Cisplatin (20mg),Injection,Alkem Laboratories Ltd,Oncology,2024-06,2027-06,OT Store,30,vial/amp,2024-09-25,Kerala Medical Supplies Co.
B01577,IPI240964,Mepresso 125mg Injection,Methylprednisolone (125mg),Injection,Intas Pharmaceuticals Ltd,Steroid,2024-12,2026-12,Main Pharmacy,30,vial/amp,2025-01-18,Sree Pharma Agencies
B01578,IP24L600,Pregabid 150 Capsule,Pregabalin (150mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-09,2027-09,OT Store,150,strip,2024-11-10,Malabar Pharma Distributors
B01579,83076970,Ondem 8 Tablet,Ondansetron (8mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-06,2025-12,Main Pharmacy,50,strip,2024-09-16,Apollo Wholesale Pvt Ltd
B01580,EW25F913,Bicarcid 270mg Tablet,Sodium Bicarbonate (270mg),Tablet,East West Pharma,Anaesthesia/Critical care,2025-03,2028-03,OT Store,100,strip,2025-06-08,Sree Pharma Agencies
B01581,86757382,Diapride 1 Tablet,Glimepiride (1mg),Tablet,Micro Labs Ltd,Diabetes,2024-08,2027-08,ICU Store,80,strip,2024-08-30,Sanjivani Drug House
B01582,T2412-143,Lupipan 20mg Tablet,Pantoprazole (20mg),Tablet,Lupin Ltd,Gastro,2024-06,2025-12,Main Pharmacy,200,strip,2024-07-21,Sree Pharma Agencies
B01583,91468439,Zygon 5IU Injection,Oxytocin (5IU),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2025-05,2028-05,Ward Store (Paeds),0,vial/amp,2025-07-08,Sanjivani Drug House
B01584,I2508-422,Viatran 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Cipla Ltd,Antibiotic,2024-12,2027-12,OT Store,50,vial/amp,2025-03-28,Malabar Pharma Distributors
B01585,32555671,Cefzone 1000mg Injection,Ceftriaxone (1000mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2027-02,OT Store,10,vial/amp,2025-04-24,Malabar Pharma Distributors
B01586,64914054,Istamet 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-08,2026-08,OPD Pharmacy,80,strip,2024-11-20,Malabar Pharma Distributors
B01587,CLT250363,Nova 150mg Tablet SR,Pregabalin (150mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-09,2026-09,Ward Store (Paeds),120,strip,2024-09-28,Kerala Medical Supplies Co.
B01588,T2402-136,Zovirax 200 Tablet,Acyclovir (200mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2024-01,2027-01,Main Pharmacy,200,strip,2024-04-24,Sree Pharma Agencies
B01589,52916049,Zerodol -CR Tablet,Aceclofenac (200mg),Tablet,Ipca Laboratories Ltd,Other,2025-04,2027-04,Main Pharmacy,300,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01590,DR25M560,Clamp 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Dr Reddy's Laboratories Ltd,Antibiotic,2024-09,2027-09,Emergency Store,50,vial/amp,2024-11-03,"Medline Distributors, Thiruvananthapuram"
B01591,CL25M734,Prazocip 2.5 XL Tablet,Prazosin (2.5mg),Tablet,Cipla Ltd,Cardiovascular,2025-04,2026-10,ICU Store,120,strip,2025-05-14,Apollo Wholesale Pvt Ltd
B01592,JP24K450,Silectone 100 Tablet,Spironolactone (100mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2024-04,2027-04,ICU Store,150,strip,2024-06-16,Apollo Wholesale Pvt Ltd
B01593,TP24D354,Furoxil 250mg Injection,Cefuroxime (250mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-07,2027-07,Main Pharmacy,80,vial/amp,2024-09-18,Sanjivani Drug House
B01594,LLT240994,Aceclonac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2024-09,2027-09,Main Pharmacy,20,strip,2024-10-25,Apollo Wholesale Pvt Ltd
B01595,CL24D355,Ivrix 12 Tablet DT,Ivermectin (12mg),Tablet,Cipla Ltd,Anthelmintic,2025-05,2028-05,Ward Store (Paeds),20,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B01596,T2506-303,Clear 250mg Tablet,Clarithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-08,2027-08,ICU Store,80,strip,2024-11-22,Apollo Wholesale Pvt Ltd
B01597,I2509-530,Melpred 1000mg Injection,Methylprednisolone (1000mg),Injection,Cipla Ltd,Steroid,2024-02,2026-02,ICU Store,120,vial/amp,2024-04-25,Sree Pharma Agencies
B01598,IPT249780,Celetoin 100 Tablet,Phenytoin (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-09,2026-03,Ward Store (Paeds),200,strip,2024-12-15,Kerala Medical Supplies Co.
B01599,79821206,Tamica-H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-06,2027-06,Emergency Store,150,strip,2024-07-13,"Medline Distributors, Thiruvananthapuram"
B01600,SP24C493,Crixan 250 Tablet,Clarithromycin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2026-10,ICU Store,30,strip,2025-01-25,Sree Pharma Agencies
B01601,I2403-623,Acostin 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-07,2026-07,ICU Store,60,vial/amp,2024-09-01,Malabar Pharma Distributors
B01602,I2406-701,Susten 200 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-01,2027-01,Ward Store (Paeds),50,vial/amp,2024-03-11,Kerala Medical Supplies Co.
B01603,NI24B026,Tegretol 300mg Tablet,Carbamazepine (300mg),Tablet,Novartis India Ltd,Neurology/Psychiatry,2025-02,2027-02,Emergency Store,100,strip,2025-03-23,Malabar Pharma Distributors
B01604,A24L963,Rivotril 2mg Tablet,Clonazepam (2mg),Tablet,Abbott,Neurology/Psychiatry,2024-03,2027-03,OPD Pharmacy,40,strip,2024-05-31,"Medline Distributors, Thiruvananthapuram"
B01605,ZC25B999,Derinide 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Zydus Cadila,Respiratory,2024-12,2026-06,Emergency Store,120,respule,2025-02-22,Apollo Wholesale Pvt Ltd
B01606,LH24E195,Edeflow 100 Tablet,Spironolactone (100mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2025-03,2027-03,ICU Store,10,strip,2025-05-14,"Medline Distributors, Thiruvananthapuram"
B01607,44901404,Conpres 12.5mg Tablet,Carvedilol (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-04,2026-10,OPD Pharmacy,100,strip,2025-06-03,Sree Pharma Agencies
B01608,T2402-603,Alcoxib 120mg Tablet,Etoricoxib (120mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-09,2026-09,Main Pharmacy,200,strip,2024-10-12,Sree Pharma Agencies
B01609,DR24F987,Mucolite Drops,Ambroxol (7.5mg),Drops,Dr Reddy's Laboratories Ltd,Respiratory,2024-06,2027-06,Main Pharmacy,150,bottle,2024-07-21,"Medline Distributors, Thiruvananthapuram"
B01610,SPT243142,Raciper 20 Tablet,Esomeprazole (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-01,2025-11,Main Pharmacy,10,strip,2024-04-22,Kerala Medical Supplies Co.
B01611,CLT243838,Valtec 300mg Tablet,Sodium Valproate (300mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-12,2027-12,Main Pharmacy,300,strip,2025-02-11,Malabar Pharma Distributors
B01612,CLT256364,Azee 1000 Tablet,Azithromycin (1000mg),Tablet,Cipla Ltd,Antibiotic,2024-01,2026-09,Ward Store (Paeds),150,strip,2024-03-31,Sree Pharma Agencies
B01613,T2507-985,Duphaston Pro Tablet,Dydrogesterone (10mg),Tablet,Abbott,Other,2024-06,2026-06,OT Store,40,strip,2024-08-17,Malabar Pharma Distributors
B01614,T2512-973,Rivotril 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Abbott,Neurology/Psychiatry,2024-11,2026-05,OPD Pharmacy,10,strip,2024-12-16,Sanjivani Drug House
B01615,MLC245766,Microdox 100mg Capsule,Doxycycline (100mg),Capsule,Micro Labs Ltd,Antibiotic,2024-04,2027-04,Emergency Store,60,strip,2024-05-05,Malabar Pharma Distributors
B01616,MLT251591,Arbitel 20 Tablet,Telmisartan (20mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-04,2027-04,Ward Store (Paeds),10,strip,2024-07-09,Sree Pharma Agencies
B01617,35894291,Gertum 250mg Tablet,Cefuroxime (250mg),Tablet,Zydus Cadila,Antibiotic,2024-01,2027-01,Main Pharmacy,80,strip,2024-04-25,"Medline Distributors, Thiruvananthapuram"
B01618,SPT249121,Carmaz 200mg Tablet,Carbamazepine (200mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-03,2027-03,Main Pharmacy,20,strip,2024-03-30,Malabar Pharma Distributors
B01619,GST247533,Augmentin 625 Duo Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antibiotic,2024-06,2025-12,Ward Store (Paeds),200,strip,2024-06-26,Kerala Medical Supplies Co.
B01620,C2510-658,TR Phyllin 125mg Capsule,Theophylline (125mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2026-12,ICU Store,60,strip,2025-02-11,Apollo Wholesale Pvt Ltd
B01621,T2507-226,Nexito 20 Tablet,Escitalopram Oxalate (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-09,2026-09,OT Store,10,strip,2024-10-29,Malabar Pharma Distributors
B01622,95076782,Aciban 20 Tablet,Pantoprazole (20mg),Tablet,Cadila Pharmaceuticals Ltd,Gastro,2024-06,2026-06,ICU Store,300,strip,2024-08-25,Sanjivani Drug House
B01623,SP25D119,Mecabalin 500mcg Injection,Methylcobalamin (500mcg),Injection,Sun Pharmaceutical Industries Ltd,Supplement,2025-05,2028-05,Ward Store (Paeds),120,vial/amp,2025-06-09,Sanjivani Drug House
B01624,ALV253716,Normal Saline 0.9% Infusion,Sodium Chloride (0.9% w/v),Infusion,Alkem Laboratories Ltd,IV Fluids,2025-03,2028-03,Main Pharmacy,200,bottle,2025-03-28,"Medline Distributors, Thiruvananthapuram"
B01625,T2406-753,Izra 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-06,2026-06,OT Store,50,strip,2024-09-15,Sree Pharma Agencies
B01626,B24F419,Basalog 100IU/ml Injection,Insulin Glargine (100IU/ml),Injection,Biocon,Diabetes,2024-09,2026-09,Main Pharmacy,60,vial/amp,2024-10-31,Malabar Pharma Distributors
B01627,A24H185,Lflox 500mg Tablet,Levofloxacin (500mg),Tablet,Abbott,Antibiotic,2025-03,2027-03,Emergency Store,50,strip,2025-06-10,Apollo Wholesale Pvt Ltd
B01628,DR24A415,Stamlo 10 Tablet,Amlodipine (10mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2025-05,2026-11,Ward Store (Paeds),40,strip,2025-07-15,Malabar Pharma Distributors
B01629,T2408-510,Abixim 100mg Tablet,Cefixime (100mg),Tablet,Abbott,Antibiotic,2025-01,2028-01,Ward Store (Paeds),150,strip,2025-04-01,Sanjivani Drug House
B01630,CLX255509,Inhalex Respules,Ambroxol (15mg),Respules,Cipla Ltd,Respiratory,2024-05,2027-05,OPD Pharmacy,60,respule,2024-07-15,Sree Pharma Agencies
B01631,33113253,Brufen 200 Tablet,Ibuprofen (200mg),Tablet,Abbott,Analgesic/Antipyretic,2025-03,2028-03,Main Pharmacy,40,strip,2025-06-24,Malabar Pharma Distributors
B01632,SP24L515,Histac 150 Tablet,Ranitidine (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-02,2027-02,Ward Store (Paeds),10,strip,2025-03-12,Apollo Wholesale Pvt Ltd
B01633,IP24B738,Carca 12.5 Tablet,Carvedilol (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-01,2028-01,OT Store,20,strip,2025-02-28,Malabar Pharma Distributors
B01634,SP24G138,Ivermectol 3mg Tablet,Ivermectin (3mg),Tablet,Sun Pharmaceutical Industries Ltd,Anthelmintic,2025-03,2026-09,OPD Pharmacy,50,strip,2025-06-14,Apollo Wholesale Pvt Ltd
B01635,67109058,Atorstat 10mg Tablet,Atorvastatin (10mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-05,2026-05,Main Pharmacy,20,strip,2024-06-15,Sree Pharma Agencies
B01636,62493261,Intamox O 1500mg Tablet,Amoxycillin (1500mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-03,2026-03,OPD Pharmacy,10,strip,2024-04-15,Sanjivani Drug House
B01637,ALT243541,Angibloc 12.5mg Tablet ER,Metoprolol Succinate (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-02,2028-02,Main Pharmacy,120,strip,2025-05-30,"Medline Distributors, Thiruvananthapuram"
B01638,AT254054,Ketof-DT Tablet,Ketorolac (10mg),Tablet,Abbott,Analgesic/Antipyretic,2024-06,2026-06,OT Store,200,strip,2024-08-03,Sanjivani Drug House
B01639,CL24M757,Sitacip M 100/1000 Tablet ER,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Cipla Ltd,Diabetes,2025-01,2027-01,OT Store,100,strip,2025-04-18,"Medline Distributors, Thiruvananthapuram"
B01640,RFT258770,Lorazepam Tablets IP 1 mg,Lorazepam (1mg),Tablet,Reliance Formulation Pvt. Ltd.,Neurology/Psychiatry,2025-05,2027-05,Ward Store (Paeds),80,strip,2025-06-10,Apollo Wholesale Pvt Ltd
B01641,ZCT249320,Espra 20mg Tablet,Esomeprazole (20mg),Tablet,Zydus Cadila,Gastro,2025-01,2026-07,OT Store,80,strip,2025-01-29,Kerala Medical Supplies Co.
B01642,S2507-475,Azimed 100mg Oral Suspension,Azithromycin (100mg),Suspension,Zydus Cadila,Antibiotic,2024-12,2027-12,ICU Store,80,bottle,2025-02-03,Apollo Wholesale Pvt Ltd
B01643,SPI248800,Ketam 10mg Injection,Ketamine (10mg),Injection,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-03,2026-03,Main Pharmacy,100,vial/amp,2024-06-05,Kerala Medical Supplies Co.
B01644,AT256999,Forxiga 5mg Tablet,Dapagliflozin (5mg),Tablet,AstraZeneca,Diabetes,2025-03,2026-09,Main Pharmacy,80,strip,2025-05-03,Kerala Medical Supplies Co.
B01645,34015248,Atorlip 10 Tablet,Atorvastatin (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2027-05,OT Store,40,strip,2024-06-01,Apollo Wholesale Pvt Ltd
B01646,I2404-950,DEPOPRED 40 MG INJECTION,Methylprednisolone (40mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2025-02,2027-02,Main Pharmacy,50,vial/amp,2025-05-07,Sree Pharma Agencies
B01647,NFDT1201,Nitrofurantoin Tablets IP 100 mg,Nitrofurantoin (100mg),Tablet,Unicure India Ltd.,Antibiotic,2024-10,2026-09,Emergency Store,120,strip,2024-11-21,Malabar Pharma Distributors
B01648,IPT259325,Zoryl 0.5 Tablet,Glimepiride (0.5mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-02,2027-02,OT Store,0,strip,2024-02-27,Sree Pharma Agencies
B01649,LL24B571,Lupimox 125mg Tablet,Amoxycillin (125mg),Tablet,Lupin Ltd,Antibiotic,2024-06,2027-06,Ward Store (Paeds),30,strip,2024-09-18,Apollo Wholesale Pvt Ltd
B01650,PLI245348,Solu-Medrol 125mg Injection,Methylprednisolone (125mg),Injection,Pfizer Ltd,Steroid,2024-02,2027-02,Main Pharmacy,10,vial/amp,2024-05-01,Sree Pharma Agencies
B01651,UL25J019,Glycomet 1gm Tablet SR,Metformin (1000mg),Tablet,USV Ltd,Diabetes,2025-03,2028-03,Ward Store (Paeds),10,strip,2025-04-09,Sree Pharma Agencies
B01652,54499873,Voveran 150mg Tablet SR,Diclofenac (150mg),Tablet,Novartis India Ltd,Analgesic/Antipyretic,2024-11,2027-11,OT Store,0,strip,2024-12-11,"Medline Distributors, Thiruvananthapuram"
B01653,ZHI249822,Zu-C Injection,Vitamin C (100mg),Injection,Zuventus Healthcare Ltd,Supplement,2024-08,2027-08,Emergency Store,50,vial/amp,2024-09-08,Malabar Pharma Distributors
B01654,T2510-317,Anxipar 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-02,2028-02,OT Store,200,strip,2025-02-26,Sanjivani Drug House
B01655,22550720,Cersar 20mg Tablet,Telmisartan (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-02,2026-02,Emergency Store,300,strip,2024-03-29,Sanjivani Drug House
B01656,TP25E485,Oncoden 4mg Tablet,Ondansetron (4mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-11,2026-05,ICU Store,300,strip,2025-02-17,Kerala Medical Supplies Co.
B01657,MLT245177,Helirab 20 Tablet,Rabeprazole (20mg),Tablet,Micro Labs Ltd,Gastro,2024-10,2026-10,OPD Pharmacy,30,strip,2024-10-27,Kerala Medical Supplies Co.
B01658,CLV254064,Dextrose 25% Infusion,Dextrose (25% w/v),Infusion,Claris Lifesciences Ltd,IV Fluids,2025-05,2026-11,OT Store,100,bottle,2025-07-15,Sree Pharma Agencies
B01659,PLI258012,Magnex 2gm Injection,Cefoperazone (1000mg) + Sulbactam (1000mg),Injection,Pfizer Ltd,Antibiotic,2024-08,2027-08,Ward Store (Paeds),300,vial/amp,2024-09-26,Apollo Wholesale Pvt Ltd
B01660,TP25K529,Xamic 250mg Tablet,Tranexamic Acid (250mg),Tablet,Torrent Pharmaceuticals Ltd,Haematology,2024-03,2026-03,OPD Pharmacy,120,strip,2024-06-09,Kerala Medical Supplies Co.
B01661,IPC243896,DC 100mg Capsule,Doxycycline (100mg),Capsule,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2026-08,Main Pharmacy,150,strip,2025-03-10,Apollo Wholesale Pvt Ltd
B01662,IPT241486,Espin TM Tablet,S-Amlodipine (2.5mg) + Telmisartan (40mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,ICU Store,60,strip,2025-01-25,Apollo Wholesale Pvt Ltd
B01663,C2411-569,Dalcap 150mg Capsule,Clindamycin (150mg),Capsule,Torrent Pharmaceuticals Ltd,Antibiotic,2024-07,2026-01,OT Store,0,strip,2024-09-11,Sree Pharma Agencies
B01664,DR25K676,Ketorol Injection,Ketorolac (30mg),Injection,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-05,2027-05,OPD Pharmacy,30,vial/amp,2024-08-21,Apollo Wholesale Pvt Ltd
B01665,I2406-747,Human Fastact 40IU/ml Injection,Human insulin (40IU),Injection,USV Ltd,Diabetes,2024-06,2025-12,OT Store,150,vial/amp,2024-09-18,Sree Pharma Agencies
B01666,LL25A148,Epilive 100mg Injection,Levetiracetam (100mg),Injection,Lupin Ltd,Neurology/Psychiatry,2024-12,2026-06,Ward Store (Paeds),80,vial/amp,2025-02-02,"Medline Distributors, Thiruvananthapuram"
B01667,T2507-606,Herpex 100mg Tablet,Acyclovir (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antiviral,2024-04,2027-04,ICU Store,30,strip,2024-05-20,"Medline Distributors, Thiruvananthapuram"
B01668,JB24E449,Metrogyl Compound 400mg/500mg Tablet,Metronidazole (400mg) + Diloxanide (500mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Antibiotic,2025-04,2028-04,ICU Store,120,strip,2025-04-26,Sree Pharma Agencies
B01669,SPI246390,Insucare N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Sun Pharmaceutical Industries Ltd,Diabetes,2025-05,2027-05,ICU Store,120,vial/amp,2025-06-18,Malabar Pharma Distributors
B01670,SII259716,Lasix Injection,Furosemide (10mg/ml),Injection,Sanofi India Ltd,Cardiovascular,2024-08,2026-02,OT Store,150,vial/amp,2024-11-08,Sree Pharma Agencies
B01671,T2403-007,Concor AM 2.5 Tablet,Amlodipine (5mg) + Bisoprolol (2.5mg),Tablet,Merck Ltd,Cardiovascular,2024-12,2027-12,OPD Pharmacy,0,strip,2025-02-16,Sanjivani Drug House
B01672,AL24H867,Levenue 1000 Tablet,Levetiracetam (1000mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-12,2027-12,OPD Pharmacy,10,strip,2025-03-11,Sanjivani Drug House
B01673,T2406-198,Melmet 1000 SR Tablet,Metformin (1000mg),Tablet,Micro Labs Ltd,Diabetes,2024-12,2026-06,OT Store,150,strip,2025-03-01,"Medline Distributors, Thiruvananthapuram"
B01674,MPT251751,Azikind 250mg Tablet,Azithromycin (250mg),Tablet,Mankind Pharma Ltd,Antibiotic,2025-01,2028-01,ICU Store,0,strip,2025-01-27,"Medline Distributors, Thiruvananthapuram"
B01675,LLT259768,Atenova 100mg Tablet,Atenolol (100mg),Tablet,Lupin Ltd,Cardiovascular,2024-07,2027-07,ICU Store,300,strip,2024-10-20,Kerala Medical Supplies Co.
B01676,26092896,Ceplox 750mg Tablet,Ciprofloxacin (750mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-05,2027-05,OPD Pharmacy,50,strip,2025-06-11,Sanjivani Drug House
B01677,X2506-831,Milflox 0.5% Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2024-12,2026-06,OPD Pharmacy,120,bottle,2025-01-29,Sanjivani Drug House
B01678,RLT242646,Aldactone F Tablet,Furosemide (20mg) + Spironolactone (50mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2024-02,2026-02,OT Store,20,strip,2024-03-10,Apollo Wholesale Pvt Ltd
B01679,I2412-480,Tufzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2025-03,2028-03,Ward Store (Paeds),50,vial/amp,2025-05-26,Malabar Pharma Distributors
B01680,SPT242851,Covance 25 Tablet,Losartan (25mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-02,2027-02,OPD Pharmacy,100,strip,2024-04-01,Malabar Pharma Distributors
B01681,IPC252071,Pregabid 75 Capsule,Pregabalin (75mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-02,2027-02,Emergency Store,120,strip,2024-05-22,Malabar Pharma Distributors
B01682,51883522,Ignalis 100 Tablet,Sitagliptin (100mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-06,2026-06,Main Pharmacy,200,strip,2024-08-13,Kerala Medical Supplies Co.
B01683,AFT248788,Azithromycin Tablets IP 500 mg,Azithromycin (500mg),Tablet,Apple Formulations Pvt. Ltd.,Antibiotic,2025-03,2027-03,OPD Pharmacy,20,strip,2025-06-04,"Medline Distributors, Thiruvananthapuram"
B01684,ZC25F929,Levoday 250 Tablet,Levofloxacin (250mg),Tablet,Zydus Cadila,Antibiotic,2024-10,2027-10,OT Store,10,strip,2025-01-14,Sree Pharma Agencies
B01685,MLI257943,Erkacin 100mg Injection,Amikacin (100mg),Injection,Micro Labs Ltd,Antibiotic,2024-10,2026-10,Ward Store (Paeds),0,vial/amp,2024-12-15,Malabar Pharma Distributors
B01686,T2510-724,Panflux 40mg Tablet,Pantoprazole (40mg),Tablet,Micro Labs Ltd,Gastro,2024-08,2026-08,ICU Store,80,strip,2024-09-18,Malabar Pharma Distributors
B01687,AI251096,Meroplan 500mg Injection,Meropenem (500mg),Injection,Abbott,Antibiotic,2025-05,2028-05,ICU Store,300,vial/amp,2025-07-15,Kerala Medical Supplies Co.
B01688,T2502-049,Mifucet 250mg Tablet,Mefenamic Acid (250mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-06,2026-06,OT Store,10,strip,2024-09-17,Kerala Medical Supplies Co.
B01689,CL24M326,Sitacip 100mg Tablet,Sitagliptin (100mg),Tablet,Cipla Ltd,Diabetes,2024-01,2026-01,ICU Store,20,strip,2024-03-28,Sree Pharma Agencies
B01690,LL24M460,Pinom 10 Tablet,Olmesartan Medoxomil (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-09,2026-03,OT Store,150,strip,2024-10-11,Sree Pharma Agencies
B01691,T2506-345,Prazopress 1 Tablet,Prazosin (1mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-04,2027-04,Emergency Store,300,strip,2025-06-25,Sree Pharma Agencies
B01692,SII242734,Clexane 20mg Injection,Enoxaparin (20mg),Injection,Sanofi India Ltd,Anticoagulant,2024-03,2026-03,Ward Store (Paeds),60,vial/amp,2024-05-07,Apollo Wholesale Pvt Ltd
B01693,LLT255597,Prednolone 5mg Tablet,Prednisolone (5mg),Tablet,Lupin Ltd,Steroid,2024-04,2026-04,ICU Store,150,strip,2024-06-17,Kerala Medical Supplies Co.
B01694,ELT253658,Tayo-M Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Eris Lifesciences Ltd,Supplement,2025-03,2028-03,Main Pharmacy,100,strip,2025-04-09,Kerala Medical Supplies Co.
B01695,ZC24K940,Adamon 50mg Capsule,Tramadol (50mg),Capsule,Zydus Cadila,Analgesic/Antipyretic,2024-08,2026-08,Emergency Store,50,strip,2024-11-21,Malabar Pharma Distributors
B01696,66586109,Amrox Oral Drops,Ambroxol (NA),Drops,Leeford Healthcare Ltd,Respiratory,2024-05,2027-05,OPD Pharmacy,0,bottle,2024-07-16,Sree Pharma Agencies
B01697,CLT246423,Ivrix 12 Tablet DT,Ivermectin (12mg),Tablet,Cipla Ltd,Anthelmintic,2025-03,2028-03,OPD Pharmacy,150,strip,2025-06-06,Kerala Medical Supplies Co.
B01698,14713027,Melmet 1000 SR Tablet,Metformin (1000mg),Tablet,Micro Labs Ltd,Diabetes,2024-02,2027-02,OPD Pharmacy,40,strip,2024-03-22,Sanjivani Drug House
B01699,NL25D966,Magneon 50% Injection,Magnesium Sulphate (50% w/v),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2025-03,2028-03,Ward Store (Paeds),40,vial/amp,2025-04-30,Malabar Pharma Distributors
B01700,MLT257361,Melmet 1000 SR Tablet,Metformin (1000mg),Tablet,Micro Labs Ltd,Diabetes,2024-09,2027-09,ICU Store,200,strip,2024-12-18,Sanjivani Drug House
B01701,CL25C846,Levoflox 500 Tablet,Levofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2025-05,2028-05,Emergency Store,300,strip,2025-06-20,Sree Pharma Agencies
B01702,TPT243490,Deplatt 150 Tablet,Clopidogrel (150mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-03,2028-03,ICU Store,120,strip,2025-04-02,Sanjivani Drug House
B01703,40410305,Brufen 200 Tablet,Ibuprofen (200mg),Tablet,Abbott,Analgesic/Antipyretic,2024-04,2026-04,OPD Pharmacy,20,strip,2024-06-04,Sree Pharma Agencies
B01704,MPT242625,Atormac 20 Tablet,Atorvastatin (20mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-02,2025-08,ICU Store,80,strip,2024-05-27,Sanjivani Drug House
B01705,CL25D410,LQuin 250 Tablet,Levofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2024-02,2025-08,Main Pharmacy,80,strip,2024-03-09,Apollo Wholesale Pvt Ltd
B01706,SP24K083,Cerzin L 2.5mg/5ml Syrup,Levocetirizine (2.5mg/5ml),Syrup,Sun Pharmaceutical Industries Ltd,Respiratory,2024-01,2027-01,Main Pharmacy,150,bottle,2024-03-26,Malabar Pharma Distributors
B01707,MLT248616,Balgyl 400mg Tablet,Metronidazole (400mg),Tablet,Micro Labs Ltd,Antibiotic,2024-02,2025-08,OPD Pharmacy,30,strip,2024-03-09,"Medline Distributors, Thiruvananthapuram"
B01708,CL24F087,Ceruclean Drop,Prednisolone (NA),Drops,Cipla Ltd,Steroid,2024-07,2027-07,Ward Store (Paeds),50,bottle,2024-08-27,Sanjivani Drug House
B01709,51181116,Ultracet Tablet,Paracetamol/Acetaminophen (325mg) + Tramadol (37.5mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2025-04,2028-04,ICU Store,200,strip,2025-07-15,Sree Pharma Agencies
B01710,56817408,CZ 3 Syrup,Cetirizine (5mg/5ml),Syrup,Lupin Ltd,Respiratory,2025-01,2027-01,Ward Store (Paeds),40,bottle,2025-03-30,Kerala Medical Supplies Co.
B01711,CLT256248,LQuin 250 Tablet,Levofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2024-08,2026-02,OT Store,150,strip,2024-10-05,Sree Pharma Agencies
B01712,A25B986,Flagyl 0.5% Solution for Infusion,Metronidazole (500mg),Infusion,Abbott,Antibiotic,2024-11,2026-05,Emergency Store,100,bottle,2025-02-01,Sanjivani Drug House
B01713,SPX259622,Suncros Soft 2% Cream,Zinc Oxide (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Supplement,2024-11,2026-11,Ward Store (Paeds),0,tube,2025-01-18,"Medline Distributors, Thiruvananthapuram"
B01714,LL25K242,Thormone 50mcg Tablet,Thyroxine (50mcg),Tablet,Lupin Ltd,Endocrine,2025-05,2027-05,Ward Store (Paeds),60,strip,2025-07-15,Sree Pharma Agencies
B01715,19246258,Oropraz 20mg Tablet,Pantoprazole (20mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-05,2026-05,Emergency Store,20,strip,2024-06-17,Kerala Medical Supplies Co.
B01716,AV250451,Anetol 1000mg Infusion,Paracetamol (1000mg),Infusion,Abbott,Analgesic/Antipyretic,2024-12,2027-12,Main Pharmacy,30,bottle,2025-02-01,"Medline Distributors, Thiruvananthapuram"
B01717,AT249922,Cortirowa OD 9mg Tablet PR,Budesonide (9mg),Tablet,Abbott,Respiratory,2024-09,2026-03,OPD Pharmacy,20,strip,2024-10-06,Apollo Wholesale Pvt Ltd
B01718,TPT248663,Encelin 50mg Tablet,Vildagliptin (50mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-01,2027-01,OPD Pharmacy,300,strip,2025-02-28,Kerala Medical Supplies Co.
B01719,69411958,Enatrate Injection,Adrenaline (NA),Injection,Entod Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-07,2027-07,OT Store,150,vial/amp,2024-08-22,Apollo Wholesale Pvt Ltd
B01720,71755566,Zynwin Tablet,Zinc Sulfate (137.232mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Supplement,2025-04,2026-10,OT Store,20,strip,2025-05-19,Kerala Medical Supplies Co.
B01721,IPT246216,Intacoxia 120 Tablet,Etoricoxib (120mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2028-02,OPD Pharmacy,20,strip,2025-05-06,Sanjivani Drug House
B01722,96786855,Cetcip-L Tablet,Levocetirizine (5mg),Tablet,Cipla Ltd,Respiratory,2024-10,2026-04,Main Pharmacy,80,strip,2024-12-27,"Medline Distributors, Thiruvananthapuram"
B01723,T2401-462,Apixator 2.5 Tablet,Apixaban (2.5mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-11,2027-11,Ward Store (Paeds),100,strip,2025-01-15,Apollo Wholesale Pvt Ltd
B01724,CLT249948,Ciplox 250 Tablet,Ciprofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2025-03,2027-03,ICU Store,0,strip,2025-05-13,Apollo Wholesale Pvt Ltd
B01725,IPT250485,Niftas 50 Tablet,Nitrofurantoin (50mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-05,2028-05,OPD Pharmacy,40,strip,2025-07-15,Kerala Medical Supplies Co.
B01726,CLT257350,Cofenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-07,2027-07,Main Pharmacy,0,strip,2024-09-22,Sree Pharma Agencies
B01727,LL24J807,Thyrodip 10mg Tablet,Carbimazole (10mg),Tablet,Lupin Ltd,Endocrine,2024-08,2027-08,Main Pharmacy,80,strip,2024-09-30,Kerala Medical Supplies Co.
B01728,CLT258932,S Citadep 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-10,2026-10,ICU Store,120,strip,2024-11-03,Apollo Wholesale Pvt Ltd
B01729,32270634,Xsulin 30/70 Suspension for Injection,Human insulin (40IU),Injection,Eris Lifesciences Ltd,Diabetes,2025-01,2027-01,Ward Store (Paeds),80,vial/amp,2025-03-10,Sanjivani Drug House
B01730,ZC24A162,Cadvocet M 5mg/10mg Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Zydus Cadila,Respiratory,2024-07,2026-01,Ward Store (Paeds),80,strip,2024-09-21,Sree Pharma Agencies
B01731,ZCT252953,Amgat 625 Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Zydus Cadila,Antibiotic,2025-01,2026-07,Ward Store (Paeds),40,strip,2025-02-23,Sree Pharma Agencies
B01732,21987653,Mefkind P 100mg Tablet,Mefenamic Acid (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-02,2026-02,Emergency Store,150,strip,2024-05-15,Apollo Wholesale Pvt Ltd
B01733,43907858,Arvast 10 Tablet,Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-04,2026-10,OPD Pharmacy,40,strip,2025-05-18,Sree Pharma Agencies
B01734,47670632,Spasidex Drop,Dicyclomine (NA),Drops,Wockhardt Ltd,Gastro,2024-12,2026-12,Main Pharmacy,60,bottle,2025-02-07,Sanjivani Drug House
B01735,IP24E537,Olimelt 10 Tablet MD,Olanzapine (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2026-06,OT Store,30,strip,2024-09-16,Kerala Medical Supplies Co.
B01736,85400080,Rosulip-F 10 Tablet,Fenofibrate (145mg) + Rosuvastatin (10mg),Tablet,Cipla Ltd,Cardiovascular,2025-05,2026-11,Ward Store (Paeds),50,strip,2025-07-15,Kerala Medical Supplies Co.
B01737,IPT240270,Cefpet XL 200mg Tablet,Cefpodoxime Proxetil (200mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-07,2027-07,Ward Store (Paeds),30,strip,2024-09-09,Kerala Medical Supplies Co.
B01738,CL24B606,Doxicip Injection,Doxycycline (100mg),Injection,Cipla Ltd,Antibiotic,2024-04,2026-04,Ward Store (Paeds),150,vial/amp,2024-04-29,"Medline Distributors, Thiruvananthapuram"
B01739,CLT242996,Warf 1 Tablet,Warfarin (1mg),Tablet,Cipla Ltd,Anticoagulant,2024-12,2026-12,OPD Pharmacy,10,strip,2025-01-14,"Medline Distributors, Thiruvananthapuram"
B01740,TP25H336,Thrombiflo 20mg Injection,Enoxaparin (20mg),Injection,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-05,2026-05,ICU Store,20,vial/amp,2024-06-16,Sanjivani Drug House
B01741,TP25J218,Hexidol 1.5 Tablet,Haloperidol (1.5mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2026-08,OPD Pharmacy,300,strip,2024-09-21,Apollo Wholesale Pvt Ltd
B01742,TPC240928,Gabator 100 Capsule,Gabapentin (100mg),Capsule,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2026-06,OPD Pharmacy,200,strip,2024-09-13,"Medline Distributors, Thiruvananthapuram"
B01743,GP24A479,Telma H Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,Main Pharmacy,120,strip,2025-02-13,"Medline Distributors, Thiruvananthapuram"
B01744,IP25B162,Carca 12.5 Tablet,Carvedilol (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-01,ICU Store,80,strip,2024-08-22,"Medline Distributors, Thiruvananthapuram"
B01745,SP25K135,Metronil 500mg Infusion,Metronidazole (500mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-04,2026-10,OT Store,300,bottle,2025-06-20,Sanjivani Drug House
B01746,TPT253077,Tide 10 Tablet,Torasemide (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-04,2027-04,Main Pharmacy,30,strip,2024-05-10,Apollo Wholesale Pvt Ltd
B01747,CFT240864,Spironot 25 Tablet,Spironolactone (25mg),Tablet,Care Formulation Labs Pvt Ltd,Cardiovascular,2025-01,2026-07,ICU Store,200,strip,2025-04-16,Sree Pharma Agencies
B01748,16554015,Nftor 100mg Tablet,Nitrofurantoin (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-10,2026-10,OT Store,120,strip,2024-12-12,Sree Pharma Agencies
B01749,T2402-788,Istamet XR Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-03,2027-03,Ward Store (Paeds),150,strip,2025-04-26,Kerala Medical Supplies Co.
B01750,SIT244385,Allegra 120mg Tablet,Fexofenadine (120mg),Tablet,Sanofi India Ltd,Respiratory,2025-05,2027-05,Ward Store (Paeds),50,strip,2025-07-15,Sree Pharma Agencies
B01751,CL25C300,Racotil 100mg Capsule,Racecadotril (100mg),Capsule,Cipla Ltd,Gastro,2024-07,2026-07,OT Store,20,strip,2024-08-30,"Medline Distributors, Thiruvananthapuram"
B01752,SPT249093,Udcros 150mg Tablet,Ursodeoxycholic Acid (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-04,2025-10,Emergency Store,200,strip,2024-07-08,Kerala Medical Supplies Co.
B01753,RPC259290,Omez 20mg Capsule,Omeprazole (20mg),Capsule,Ridgecure Pharma,Gastro,2024-05,2027-05,Ward Store (Paeds),120,strip,2024-08-13,Malabar Pharma Distributors
B01754,X2407-898,Candid Ear Drop,Lidocaine (2% w/v) + Clotrimazole (1% w/v),Ear Drops,Glenmark Pharmaceuticals Ltd,Antifungal,2024-02,2026-02,Emergency Store,40,bottle,2024-05-17,Sanjivani Drug House
B01755,T2408-780,Ecator 10mg Tablet,Ramipril (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-03,2026-09,ICU Store,80,strip,2025-03-31,Kerala Medical Supplies Co.
B01756,LL25G689,Defenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2025-02,2027-02,OPD Pharmacy,50,strip,2025-05-06,Apollo Wholesale Pvt Ltd
B01757,ALI249912,Becef 125mg Injection,Ceftriaxone (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2025-03,2028-03,Emergency Store,40,vial/amp,2025-05-05,Malabar Pharma Distributors
B01758,S2410-053,Sucral D Suspension,Domperidone (7.5mg) + Sucralfate (1000mg),Suspension,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-08,2026-02,Ward Store (Paeds),40,bottle,2024-11-18,Sanjivani Drug House
B01759,AL24J320,Alsita 100mg Tablet,Sitagliptin (100mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-01,2026-07,OT Store,120,strip,2025-03-31,Kerala Medical Supplies Co.
B01760,SI24C112,Combiflam Suspension,Ibuprofen (100mg) + Paracetamol (162.5mg),Suspension,Sanofi India Ltd,Analgesic/Antipyretic,2024-08,2027-08,OPD Pharmacy,150,bottle,2024-09-26,Kerala Medical Supplies Co.
B01761,SP24A038,Fendrop 25mcg Patch,Fentanyl (25mcg),Drops,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-01,2026-05,OPD Pharmacy,100,bottle,2024-03-01,Apollo Wholesale Pvt Ltd
B01762,ZCT242364,Losacar 25 Tablet,Losartan (25mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2026-02,ICU Store,200,strip,2024-04-29,Sanjivani Drug House
B01763,AL24G362,Almox CV Syrup,Amoxycillin (200mg/5ml) + Clavulanic Acid (28.5mg/5ml),Syrup,Alkem Laboratories Ltd,Antibiotic,2024-01,2026-01,Ward Store (Paeds),30,bottle,2024-02-20,Sree Pharma Agencies
B01764,TPV240905,Cipride 200mg Infusion,Ciprofloxacin (200mg),Infusion,Torrent Pharmaceuticals Ltd,Antibiotic,2025-01,2028-01,Ward Store (Paeds),60,bottle,2025-04-19,Apollo Wholesale Pvt Ltd
B01765,68475513,Nexpro Fast 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-02,2028-02,Emergency Store,60,strip,2025-05-12,"Medline Distributors, Thiruvananthapuram"
B01766,T2512-088,Altipod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-02,2027-02,OT Store,20,strip,2024-03-22,Sanjivani Drug House
B01767,SPI243319,Emsetron 2mg Injection,Ondansetron (2mg),Injection,Sun Pharmaceutical Industries Ltd,Gastro,2024-02,2025-08,Emergency Store,150,vial/amp,2024-04-23,Kerala Medical Supplies Co.
B01768,T2404-192,Panflux 40mg Tablet,Pantoprazole (40mg),Tablet,Micro Labs Ltd,Gastro,2024-12,2026-06,OPD Pharmacy,300,strip,2025-02-05,Sree Pharma Agencies
B01769,SP25E235,Toride 20mg Tablet,Torasemide (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-02,2028-02,ICU Store,100,strip,2025-03-23,Sree Pharma Agencies
B01770,MP24D930,Racedot 100mg Capsule,Racecadotril (100mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-01,2026-07,OPD Pharmacy,40,strip,2025-03-03,Malabar Pharma Distributors
B01771,51734908,Zerodol Spas Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Ipca Laboratories Ltd,Gastro,2025-01,2027-01,Ward Store (Paeds),80,strip,2025-03-02,Malabar Pharma Distributors
B01772,I2507-401,Ufh 25000IU Injection,Heparin (25000IU),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2024-03,2027-03,OT Store,20,vial/amp,2024-05-08,Kerala Medical Supplies Co.
B01773,IPT241145,Zevert 12 SR Tablet,Betahistine (12mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-02,2026-02,OT Store,100,strip,2024-05-18,Malabar Pharma Distributors
B01774,CL25G313,Cognolin 500 Tablet,Citicoline (500mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-02,2026-02,OPD Pharmacy,100,strip,2024-02-29,Sanjivani Drug House
B01775,APT245676,Folinal 5mg Tablet,Folic Acid (5mg),Tablet,Alembic Pharmaceuticals Ltd,Haematology,2024-09,2027-09,Ward Store (Paeds),10,strip,2024-10-16,"Medline Distributors, Thiruvananthapuram"
B01776,LLT241925,Elate 5mg Tablet,Levocetirizine (5mg),Tablet,Lupin Ltd,Respiratory,2024-07,2026-07,OT Store,150,strip,2024-10-10,"Medline Distributors, Thiruvananthapuram"
B01777,C2406-790,Lyrica 150mg Capsule,Pregabalin (150mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-01,2027-02,OPD Pharmacy,30,strip,2024-02-06,Apollo Wholesale Pvt Ltd
B01778,89299984,Nexito 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-02,2026-02,Ward Store (Paeds),80,strip,2024-05-12,Malabar Pharma Distributors
B01779,A25M991,Ipratop 200mcg Inhaler,Ipratropium (200mcg),Inhaler,AstraZeneca,Respiratory,2024-05,2027-05,OPD Pharmacy,60,inhaler,2024-08-02,Sree Pharma Agencies
B01780,24443322,Bicarcid 270mg Tablet,Sodium Bicarbonate (270mg),Tablet,East West Pharma,Anaesthesia/Critical care,2025-03,2028-03,Ward Store (Paeds),80,strip,2025-05-23,Sree Pharma Agencies
B01781,MP24G627,Azikind 250mg Tablet,Azithromycin (250mg),Tablet,Mankind Pharma Ltd,Antibiotic,2024-02,2026-02,ICU Store,300,strip,2024-05-02,Apollo Wholesale Pvt Ltd
B01782,67774765,Rosuvas 10 Sprinkle Capsule,Rosuvastatin (10mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-10,2027-10,Main Pharmacy,0,strip,2024-11-08,Kerala Medical Supplies Co.
B01783,CLT256238,Imutrex 10 Tablet,Methotrexate (10mg),Tablet,Cipla Ltd,Oncology,2024-10,2027-10,OPD Pharmacy,10,strip,2024-12-12,Sanjivani Drug House
B01784,SP24H393,Rosuvas 10 Sprinkle Capsule,Rosuvastatin (10mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2027-09,Ward Store (Paeds),80,strip,2024-11-15,Sanjivani Drug House
B01785,43077664,Levenue 1000 Tablet,Levetiracetam (1000mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2025-03,2026-09,Main Pharmacy,20,strip,2025-05-02,Sree Pharma Agencies
B01786,AL24C934,Tramef 50mg Injection,Tramadol (50mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-03,2028-03,Ward Store (Paeds),200,vial/amp,2025-04-14,Apollo Wholesale Pvt Ltd
B01787,ML25H245,BIOFER S 100mg/5ml Injection,Iron Sucrose (100mg/5ml),Injection,Micro Labs Ltd,Haematology,2024-05,2027-05,OPD Pharmacy,150,vial/amp,2024-07-11,Kerala Medical Supplies Co.
B01788,MT14501,Zinc Sulphate Dispersible Tablets IP,Zinc Sulphate (20mg),Tablet,McW Healthcare (P) Ltd.,Paediatrics,2025-04,2027-03,OT Store,10,strip,2025-05-26,Sree Pharma Agencies
B01789,IP24B926,Acticin 500mg Tablet,Paracetamol (500mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-03,2025-09,OT Store,200,strip,2024-04-25,Sanjivani Drug House
B01790,AL24G497,Losaral 50mg Tablet,Losartan (50mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-04,2026-04,Main Pharmacy,100,strip,2024-07-28,Sree Pharma Agencies
B01791,CLT245211,Asthalin 2 Tablet,Salbutamol (2mg),Tablet,Cipla Ltd,Respiratory,2024-03,2026-03,OT Store,150,strip,2024-06-07,Apollo Wholesale Pvt Ltd
B01792,69604527,Astin 10 Tablet,Atorvastatin (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-10,2027-10,ICU Store,300,strip,2024-10-27,Apollo Wholesale Pvt Ltd
B01793,41340071,Sitared XR Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-04,2026-10,ICU Store,30,strip,2025-06-04,Malabar Pharma Distributors
B01794,31307131,Clinka Gel,Clindamycin (1% w/w),Gel,Intas Pharmaceuticals Ltd,Antibiotic,2024-11,2026-11,ICU Store,80,tube,2025-01-18,Kerala Medical Supplies Co.
B01795,IP24F482,Ibutas 200mg Tablet,Ibuprofen (200mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2026-05,ICU Store,20,strip,2024-08-22,Sree Pharma Agencies
B01796,87480448,Frusizex 10mg Injection,Furosemide (10mg/ml),Injection,Zee Laboratories,Cardiovascular,2024-02,2027-02,OPD Pharmacy,200,vial/amp,2024-05-13,Malabar Pharma Distributors
B01797,ALX255971,Dermikem Dusting Powder,Clotrimazole (1% w/w),Powder,Alkem Laboratories Ltd,Antifungal,2024-03,2026-03,OT Store,50,pack,2024-06-29,Sree Pharma Agencies
B01798,T2511-569,Sitaxa M 50/1000 Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-02,2027-02,Ward Store (Paeds),0,strip,2024-04-19,"Medline Distributors, Thiruvananthapuram"
B01799,IPS253626,Cefinta 50mg Dry Syrup,Cefixime (50mg),Syrup,Intas Pharmaceuticals Ltd,Antibiotic,2024-04,2025-10,Emergency Store,120,bottle,2024-05-13,Sree Pharma Agencies
B01800,CL24D765,Cersar 20mg Tablet,Telmisartan (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-02,2027-02,ICU Store,30,strip,2024-03-24,"Medline Distributors, Thiruvananthapuram"
B01801,RPC253774,Omez 20mg Capsule,Omeprazole (20mg),Capsule,Ridgecure Pharma,Gastro,2024-10,2027-10,Emergency Store,50,strip,2024-11-08,Kerala Medical Supplies Co.
B01802,LLT257191,Lupisit 100mg Tablet,Sitagliptin (100mg),Tablet,Lupin Ltd,Diabetes,2024-12,2026-06,Ward Store (Paeds),120,strip,2025-01-27,Kerala Medical Supplies Co.
B01803,SPT247852,Oleanz 5 Tablet,Olanzapine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-03,2027-03,Main Pharmacy,0,strip,2024-06-04,Apollo Wholesale Pvt Ltd
B01804,S2511-466,Lupibend 200mg Suspension,Albendazole (200mg),Suspension,Lupin Ltd,Anthelmintic,2024-09,2027-09,OT Store,20,bottle,2024-11-26,Sanjivani Drug House
B01805,SP24J504,Rosuvas 10 Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-05,2027-05,Main Pharmacy,80,strip,2025-07-09,Apollo Wholesale Pvt Ltd
B01806,TPT259012,Lezyncet 10 Tablet DT,Levocetirizine (10mg),Tablet,Torrent Pharmaceuticals Ltd,Respiratory,2025-03,2026-09,Ward Store (Paeds),60,strip,2025-06-04,Kerala Medical Supplies Co.
B01807,MP24A255,Aerozest 0.31mg Respules (2.5 ml each),Levosalbutamol (0.31mg),Respules,Macleods Pharmaceuticals Pvt Ltd,Respiratory,2025-03,2026-09,OT Store,10,respule,2025-06-13,"Medline Distributors, Thiruvananthapuram"
B01808,CLT255857,Etozox 120mg Tablet,Etoricoxib (120mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2025-05,2028-05,Emergency Store,30,strip,2025-07-15,Sanjivani Drug House
B01809,ALT252200,Ursokem 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-07,2027-07,Ward Store (Paeds),20,strip,2024-10-07,Sanjivani Drug House
B01810,T2411-184,Telmisartan Tablets IP 40 mg,Telmisartan (40mg),Tablet,Eurokem Laboratories Pvt. Ltd.,Cardiovascular,2025-04,2027-04,Emergency Store,20,strip,2025-06-08,Sree Pharma Agencies
B01811,IHV256410,D5 Infusion,Dextrose (5gm),Infusion,Infutec Healthcare Limited,IV Fluids,2024-04,2027-04,OPD Pharmacy,40,bottle,2024-05-20,Malabar Pharma Distributors
B01812,LH25F744,Alcidic 75mg Injection,Diclofenac (75mg),Injection,Leeford Healthcare Ltd,Analgesic/Antipyretic,2025-02,2028-02,OPD Pharmacy,10,vial/amp,2025-04-21,Malabar Pharma Distributors
B01813,CL25J020,Cipcal-XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cipla Ltd,Supplement,2024-09,2027-09,OPD Pharmacy,120,strip,2024-10-14,Sree Pharma Agencies
B01814,NI25L509,Galvus Met 50mg/1000mg Tablet,Metformin (1000mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2024-09,2027-09,Emergency Store,0,strip,2024-09-28,Sanjivani Drug House
B01815,LLT248831,Etrolup 90mg Tablet,Etoricoxib (90mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2024-09,2026-09,Ward Store (Paeds),40,strip,2024-12-13,Sanjivani Drug House
B01816,I2412-068,Diclogesic RR 75mg Injection,Diclofenac (75mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-04,2026-04,ICU Store,10,vial/amp,2024-06-04,Sree Pharma Agencies
B01817,IP25F781,Nuzide 80mg Tablet,Gliclazide (80mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2025-05,2026-11,OPD Pharmacy,0,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B01818,X2510-382,DexLuz Oral Solution Lemon,Lactulose (10gm),Oral Solution,Lupin Ltd,Gastro,2025-01,2026-07,Main Pharmacy,0,bottle,2025-03-10,Apollo Wholesale Pvt Ltd
B01819,T2511-153,Mahapanta 40 Tablet,Pantoprazole (40mg),Tablet,Mankind Pharma Ltd,Gastro,2025-04,2027-04,Main Pharmacy,50,strip,2025-06-16,Apollo Wholesale Pvt Ltd
B01820,LHI246002,Cavmox 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Leeford Healthcare Ltd,Antibiotic,2024-05,2026-05,OPD Pharmacy,100,vial/amp,2024-05-30,Kerala Medical Supplies Co.
B01821,56155452,Nexito 15mg Tablet,Escitalopram Oxalate (15mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2027-01,Emergency Store,80,strip,2024-03-02,"Medline Distributors, Thiruvananthapuram"
B01822,LL25L133,Amikef 100mg Injection,Amikacin (100mg),Injection,Lupin Ltd,Antibiotic,2024-07,2027-07,Ward Store (Paeds),60,vial/amp,2024-10-05,Kerala Medical Supplies Co.
B01823,V2512-254,Cefadur CA 250mg Infusion,Cefuroxime (250mg),Infusion,Cipla Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,60,bottle,2024-07-20,Apollo Wholesale Pvt Ltd
B01824,63781664,Angiblock 10mg Capsule,Nifedipine (10mg),Capsule,Alkem Laboratories Ltd,Cardiovascular,2024-09,2027-09,OPD Pharmacy,100,strip,2024-11-24,"Medline Distributors, Thiruvananthapuram"
B01825,CLT240455,Epizam 0.25mg Tablet MD,Clonazepam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-02,2028-02,Emergency Store,200,strip,2025-03-21,Malabar Pharma Distributors
B01826,WM25E154,Betadine 10% Solution,Povidone Iodine (10% w/v),Solution,Win-Medicare Pvt Ltd,Dermatology,2024-04,2027-04,ICU Store,300,bottle,2024-07-25,Sanjivani Drug House
B01827,MLX241786,Levobact 0.5% Eye Drop,Levofloxacin (0.5%),Eye Drops,Micro Labs Ltd,Antibiotic,2025-05,2028-05,Ward Store (Paeds),40,bottle,2025-07-15,Sanjivani Drug House
B01828,T2503-408,Telday-H Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-07,2027-07,OT Store,10,strip,2024-10-15,Apollo Wholesale Pvt Ltd
B01829,CL24A618,Atorlip 10 Tablet,Atorvastatin (10mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2028-03,Emergency Store,150,strip,2025-06-17,Kerala Medical Supplies Co.
B01830,22033247,Cresar 80H Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2026-04,OPD Pharmacy,40,strip,2024-07-01,Sanjivani Drug House
B01831,63811222,Concor 5 Tablet,Bisoprolol (5mg),Tablet,Merck Ltd,Cardiovascular,2024-03,2026-03,ICU Store,80,strip,2024-04-03,Kerala Medical Supplies Co.
B01832,T2508-407,Levipil 1g Tablet,Levetiracetam (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-05,2027-05,Ward Store (Paeds),50,strip,2024-06-18,Kerala Medical Supplies Co.
B01833,CLX258596,Dexacip 0.1% Eye Drop,Dexamethasone (0.1% w/v),Eye Drops,Cipla Ltd,Steroid,2024-07,2027-07,OPD Pharmacy,30,bottle,2024-10-27,Kerala Medical Supplies Co.
B01834,L-24K-31H,Lamic-500 Injection,Amikacin (500mg/2ml),Injection,Inmac Laboratories,Antibiotic,2024-11,2026-10,OPD Pharmacy,60,vial/amp,2024-12-11,Kerala Medical Supplies Co.
B01835,LLT248318,Pixaflo 2.5mg Tablet,Apixaban (2.5mg),Tablet,Lupin Ltd,Anticoagulant,2024-09,2026-09,Ward Store (Paeds),60,strip,2024-12-13,Sree Pharma Agencies
B01836,PLC257287,Lyrica 150mg Capsule,Pregabalin (150mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-03,2027-03,Main Pharmacy,30,strip,2024-06-27,Malabar Pharma Distributors
B01837,TPT254265,Corbis 1.25 Tablet,Bisoprolol (1.25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,OT Store,60,strip,2024-12-20,Sree Pharma Agencies
B01838,IPT242969,Allegix 120mg Tablet,Fexofenadine (120mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2024-05,2026-05,ICU Store,40,strip,2024-06-27,"Medline Distributors, Thiruvananthapuram"
B01839,53042832,Lyricare-GM Tablet,Gabapentin (300mg) + Methylcobalamin (500mcg),Tablet,Urvija Pharmaceuticals,Neurology/Psychiatry,2024-01,2027-01,Ward Store (Paeds),10,strip,2024-04-27,Sanjivani Drug House
B01840,PLI250720,Solu-Medrol 125mg Injection,Methylprednisolone (125mg),Injection,Pfizer Ltd,Steroid,2025-02,2027-02,Main Pharmacy,10,vial/amp,2025-03-09,Sree Pharma Agencies
B01841,IR24G155,Labetag 100mg Tablet,Labetalol (100mg),Tablet,Ikon Remedies Pvt Ltd,Cardiovascular,2025-01,2027-01,Emergency Store,50,strip,2025-02-15,Sree Pharma Agencies
B01842,20080250,Cofarin 1mg Tablet,Warfarin (1mg),Tablet,East West Pharma,Anticoagulant,2024-12,2027-12,Main Pharmacy,20,strip,2025-01-19,Kerala Medical Supplies Co.
B01843,AL25M038,Actisprin 150mg Tablet,Aspirin (150mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-02,2026-08,Main Pharmacy,120,strip,2025-05-22,Sree Pharma Agencies
B01844,IPC244192,Altispor 100mg Capsule,Itraconazole (100mg),Capsule,Intas Pharmaceuticals Ltd,Antifungal,2024-12,2027-12,OPD Pharmacy,40,strip,2025-01-23,Malabar Pharma Distributors
B01845,21871327,Nicetamol 125mg Tablet,Paracetamol (125mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-06,2025-12,Ward Store (Paeds),60,strip,2024-06-26,Kerala Medical Supplies Co.
B01846,CL25M800,Dytor 40 Tablet,Torasemide (40mg),Tablet,Cipla Ltd,Cardiovascular,2024-06,2027-06,OPD Pharmacy,50,strip,2024-09-15,Kerala Medical Supplies Co.
B01847,AI054J24,Folitrax-15 Injection,Methotrexate (15mg/ml),Injection,BDH Industrial Ltd.,Oncology,2024-09,2026-08,Emergency Store,50,vial/amp,2024-11-26,Kerala Medical Supplies Co.
B01848,T2505-266,Cifran 500 Tablet,Ciprofloxacin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-06,2026-06,OT Store,60,strip,2024-08-18,Malabar Pharma Distributors
B01849,CLT250426,Vysov 50mg Tablet,Vildagliptin (50mg),Tablet,Cipla Ltd,Diabetes,2024-05,2027-05,OT Store,300,strip,2024-07-14,Malabar Pharma Distributors
B01850,D-0241,Lycitra MK Syrup,Montelukast + Levocetirizine,Syrup,Animus Healthcare,Respiratory,2023-11,2025-10,Emergency Store,40,bottle,2023-12-15,Apollo Wholesale Pvt Ltd
B01851,S2506-152,Paragreat 250mg Suspension,Paracetamol (250mg),Suspension,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-04,2027-04,Emergency Store,80,bottle,2024-06-12,Sree Pharma Agencies
B01852,ZCT245367,CoviQ Tablet,Hydroxychloroquine (200mg),Tablet,Zydus Cadila,Antimalarial,2025-02,2028-02,Emergency Store,80,strip,2025-05-08,Apollo Wholesale Pvt Ltd
B01853,S2410-651,Calpol 250mg Paediatric Oral Suspension Strawberry,Paracetamol (250mg/5ml),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-04,2027-04,Ward Store (Paeds),100,bottle,2025-05-17,Sree Pharma Agencies
B01854,I2512-037,Platin 10mg Injection,Cisplatin (10mg),Injection,Cadila Pharmaceuticals Ltd,Oncology,2025-04,2026-10,Emergency Store,80,vial/amp,2025-06-14,Malabar Pharma Distributors
B01855,T2402-540,Misoprost 100mg Tablet,Misoprostol (100mg),Tablet,Cipla Ltd,Obstetrics,2024-09,2026-09,OPD Pharmacy,20,strip,2024-10-23,Kerala Medical Supplies Co.
B01856,CPI255306,Dianora 1mg Injection,Adrenaline (1mg),Injection,Cachet Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-06,2026-06,OPD Pharmacy,0,vial/amp,2024-07-02,"Medline Distributors, Thiruvananthapuram"
B01857,S2401-990,Albaxy Suspension,Albendazole (200mg),Suspension,Sun Pharmaceutical Industries Ltd,Anthelmintic,2024-11,2026-11,OPD Pharmacy,60,bottle,2025-01-03,Kerala Medical Supplies Co.
B01858,AT256569,Neo-Mercazole 10 Tablet,Carbimazole (10mg),Tablet,Abbott,Endocrine,2025-01,2027-01,OT Store,80,strip,2025-03-04,"Medline Distributors, Thiruvananthapuram"
B01859,20340310,Alsita M 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-06,2026-06,ICU Store,80,strip,2024-07-22,Sree Pharma Agencies
B01860,SP24H660,Clopilet 150 Tablet,Clopidogrel (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2027-12,Ward Store (Paeds),200,strip,2025-03-04,Sree Pharma Agencies
B01861,CLI254803,Gentacip 40mg Injection,Gentamicin (40mg),Injection,Cipla Ltd,Antibiotic,2024-12,2026-12,OPD Pharmacy,40,vial/amp,2025-01-17,Sanjivani Drug House
B01862,T2504-713,Januvia 50mg Tablet,Sitagliptin (50mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-12,2026-06,OPD Pharmacy,200,strip,2025-03-13,Apollo Wholesale Pvt Ltd
B01863,38538251,Calpol 250mg Tablet,Paracetamol (250mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-04,2027-04,OT Store,80,strip,2024-07-18,Malabar Pharma Distributors
B01864,CL24B796,Urimax 0.4 Capsule MR,Tamsulosin (0.4mg),Capsule,Cipla Ltd,Urology,2024-08,2027-08,ICU Store,50,strip,2024-10-03,Apollo Wholesale Pvt Ltd
B01865,CL25J769,Ataron Eye Drop,Atropine (1% w/v),Eye Drops,Cipla Ltd,Anaesthesia/Critical care,2024-10,2026-10,ICU Store,150,bottle,2024-11-24,Malabar Pharma Distributors
B01866,DR25L956,Razo 10 Tablet,Rabeprazole (10mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-03,2027-03,Ward Store (Paeds),150,strip,2024-06-06,Sanjivani Drug House
B01867,68274194,Ataron Eye Drop,Atropine (1% w/v),Eye Drops,Cipla Ltd,Anaesthesia/Critical care,2024-11,2027-11,Emergency Store,40,bottle,2025-01-15,Kerala Medical Supplies Co.
B01868,91665930,Fusibact Cream,Fusidic Acid (2% w/w),Cream,Cipla Ltd,Dermatology,2025-01,2028-01,OPD Pharmacy,200,tube,2025-02-08,Apollo Wholesale Pvt Ltd
B01869,I2512-628,Oframax 125mg Injection,Ceftriaxone (125mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2026-02,OT Store,50,vial/amp,2024-03-07,Apollo Wholesale Pvt Ltd
B01870,63394430,Starcad-Beta 12.5 Tablet ER,Metoprolol Succinate (11.8mg),Tablet,Lupin Ltd,Cardiovascular,2025-02,2028-02,OPD Pharmacy,150,strip,2025-03-04,Malabar Pharma Distributors
B01871,I2507-825,Zygon 5IU Injection,Oxytocin (5IU),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-07,2026-07,Emergency Store,30,vial/amp,2024-08-12,Sanjivani Drug House
B01872,T2511-844,Alciflox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-02,2027-02,Ward Store (Paeds),200,strip,2024-05-29,Malabar Pharma Distributors
B01873,85864089,Leemol 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-07,2027-07,ICU Store,80,bottle,2024-10-27,Malabar Pharma Distributors
B01874,45437132,Tayo-M Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Eris Lifesciences Ltd,Supplement,2024-02,2026-02,Main Pharmacy,10,strip,2024-04-09,Kerala Medical Supplies Co.
B01875,ZCT250385,Glimp M 1mg/1000mg Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2025-03,2027-03,Main Pharmacy,40,strip,2025-03-27,Sree Pharma Agencies
B01876,ti 404b024,Sodium Chloride Injection IP 0.9%,Sodium Chloride (0.9% w/v),Infusion,Paschim Banga Pharmaceuticals,IV Fluids,2024-09,2026-09,OT Store,20,bottle,2024-12-19,Malabar Pharma Distributors
B01877,IP24K190,Zap 0.5mg Tablet,Clonazepam (0.5mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-11,2026-05,Emergency Store,60,strip,2025-01-16,Sree Pharma Agencies
B01878,I2408-886,C One 1000mg Injection,Ceftriaxone (1000mg),Injection,Abbott,Antibiotic,2024-11,2027-11,ICU Store,60,vial/amp,2025-02-17,Malabar Pharma Distributors
B01879,LL24F735,L-Cin 250 Tablet,Levofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-05,2026-05,ICU Store,150,strip,2024-08-04,Apollo Wholesale Pvt Ltd
B01880,T2502-277,Florobid 200mg Tablet,Ofloxacin (200mg),Tablet,Micro Labs Ltd,Antibiotic,2024-06,2027-06,Ward Store (Paeds),100,strip,2024-09-21,Malabar Pharma Distributors
B01881,A25A284,Meroplan 500mg Injection,Meropenem (500mg),Injection,Abbott,Antibiotic,2024-04,2027-04,OPD Pharmacy,200,vial/amp,2024-06-27,Kerala Medical Supplies Co.
B01882,12861726,Tromacyn Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2024-10,2026-04,Ward Store (Paeds),200,bottle,2024-12-09,Sree Pharma Agencies
B01883,T2508-760,Allerkast LC Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Lupin Ltd,Respiratory,2024-09,2026-09,Main Pharmacy,20,strip,2024-10-30,Apollo Wholesale Pvt Ltd
B01884,I2411-959,Vasocon Injection,Adrenaline (1mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-07,2026-07,OPD Pharmacy,120,vial/amp,2024-09-23,Apollo Wholesale Pvt Ltd
B01885,74043381,Lidoxin 0.25mg Tablet,Digoxin (0.25mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2024-01,2026-01,OPD Pharmacy,300,strip,2024-01-26,"Medline Distributors, Thiruvananthapuram"
B01886,LLI250238,Ceptidar S 1.5G Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Lupin Ltd,Antibiotic,2025-01,2026-07,ICU Store,300,vial/amp,2025-03-12,Apollo Wholesale Pvt Ltd
B01887,ZC25H738,Atorva 20 Tablet,Atorvastatin (20mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2027-02,OPD Pharmacy,100,strip,2024-04-29,Sree Pharma Agencies
B01888,SPC258576,Niftran 100mg Capsule,Nitrofurantoin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-05,2027-05,Main Pharmacy,80,strip,2024-06-08,Kerala Medical Supplies Co.
B01889,CLT245175,Cipmox 125mg Tablet DT,Amoxycillin (125mg),Tablet,Cipla Ltd,Antibiotic,2024-07,2026-07,Ward Store (Paeds),200,strip,2024-09-19,Apollo Wholesale Pvt Ltd
B01890,85760777,Cresar 80H Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Cipla Ltd,Cardiovascular,2025-04,2028-04,Main Pharmacy,200,strip,2025-07-09,Kerala Medical Supplies Co.
B01891,MLT243099,Ascad 150mg Tablet,Aspirin (150mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-02,2026-02,Ward Store (Paeds),300,strip,2024-04-10,Malabar Pharma Distributors
B01892,42801620,Mepresso 125mg Injection,Methylprednisolone (125mg),Injection,Intas Pharmaceuticals Ltd,Steroid,2024-03,2027-03,ICU Store,10,vial/amp,2024-06-26,Kerala Medical Supplies Co.
B01893,EPI247873,Ultimox CV 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Emcure Pharmaceuticals Ltd,Antibiotic,2024-07,2026-07,Emergency Store,100,vial/amp,2024-08-24,Sanjivani Drug House
B01894,SP25E710,Cifran 500 Tablet,Ciprofloxacin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-09,2026-09,Main Pharmacy,80,strip,2024-10-09,Kerala Medical Supplies Co.
B01895,SPC249246,Angistat 2.5 Capsule TR,Nitroglycerin (2.5mg),Capsule,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2027-03,Ward Store (Paeds),100,strip,2024-06-20,Sree Pharma Agencies
B01896,42800911,Tamica-AM 40 Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-09,2026-09,ICU Store,60,strip,2024-12-23,Apollo Wholesale Pvt Ltd
B01897,SP25M353,Niftran 100mg Capsule,Nitrofurantoin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2027-10,Main Pharmacy,50,strip,2025-01-02,Sree Pharma Agencies
B01898,AL25D461,Hospisone 40 Injection,Methylprednisolone (40mg),Injection,Alkem Laboratories Ltd,Steroid,2024-05,2025-11,OT Store,150,vial/amp,2024-07-28,Apollo Wholesale Pvt Ltd
B01899,59499531,Fulsed 1mg Injection,Midazolam (1mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2027-07,OPD Pharmacy,300,vial/amp,2024-08-03,Apollo Wholesale Pvt Ltd
B01900,DR24M957,Novigan 400mg Tablet,Ibuprofen (400mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-03,2027-03,ICU Store,10,strip,2024-04-16,Sree Pharma Agencies
B01901,67385552,Folitrax 10mg Injection,Methotrexate (10mg),Injection,Ipca Laboratories Ltd,Oncology,2024-01,2026-01,Main Pharmacy,300,vial/amp,2024-03-17,Sanjivani Drug House
B01902,CL24B763,Apigy 2.5 Tablet,Apixaban (2.5mg),Tablet,Cipla Ltd,Anticoagulant,2025-01,2027-01,Main Pharmacy,0,strip,2025-04-06,Sree Pharma Agencies
B01903,T2410-017,Phensedyl LM Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Abbott,Respiratory,2024-01,2027-01,Emergency Store,80,strip,2024-03-31,Malabar Pharma Distributors
B01904,CLI245132,Ciplox 2mg Injection,Ciprofloxacin (2mg),Injection,Cipla Ltd,Antibiotic,2025-04,2026-10,Main Pharmacy,150,vial/amp,2025-07-08,Sree Pharma Agencies
B01905,C2506-847,IBUGESIC 300MG CAPSULE SR,Ibuprofen (300mg),Capsule,Cipla Ltd,Analgesic/Antipyretic,2024-02,2027-02,ICU Store,300,strip,2024-05-23,Kerala Medical Supplies Co.
B01906,IPI241362,Ceprozone S 1000mg/500mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-03,2026-03,OT Store,120,vial/amp,2024-03-27,Sree Pharma Agencies
B01907,LHI247002,Femozer 100mg Injection,Iron Sucrose (100mg),Injection,Leeford Healthcare Ltd,Haematology,2024-04,2026-04,Main Pharmacy,300,vial/amp,2024-05-06,Malabar Pharma Distributors
B01908,LL25L494,Cefaxone 0.25g Injection,Ceftriaxone (250mg),Injection,Lupin Ltd,Antibiotic,2024-01,2027-01,OT Store,300,vial/amp,2024-03-10,Apollo Wholesale Pvt Ltd
B01909,JBT249091,Metrogyl 400 Tablet,Metronidazole (400mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Antibiotic,2024-02,2025-08,Emergency Store,120,strip,2024-05-29,Apollo Wholesale Pvt Ltd
B01910,ALX257601,Almox 100mg Oral Drops,Amoxycillin (100mg),Drops,Alkem Laboratories Ltd,Antibiotic,2024-07,2026-07,OPD Pharmacy,150,bottle,2024-09-13,Malabar Pharma Distributors
B01911,X2403-832,Atromet Eye Drop,Atropine (1% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-01,2027-02,OPD Pharmacy,300,bottle,2024-02-28,Apollo Wholesale Pvt Ltd
B01912,SPV246911,Rapifol 10mg Infusion,Propofol (10mg),Infusion,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2025-03,2028-03,OPD Pharmacy,30,bottle,2025-05-23,Apollo Wholesale Pvt Ltd
B01913,SP24H319,Cifran 250 Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-04,2026-04,Emergency Store,100,strip,2024-07-21,Apollo Wholesale Pvt Ltd
B01914,TP25C603,Metocard XL 100 Tablet,Metoprolol Succinate (95mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-05,OPD Pharmacy,100,strip,2024-04-06,Sree Pharma Agencies
B01915,IPI249034,NT Spas 10mg Injection,Dicyclomine (10mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2025-02,2027-02,Main Pharmacy,200,vial/amp,2025-03-30,Sanjivani Drug House
B01916,SP24L288,Encorate 100mg Injection,Sodium Valproate (100mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2026-12,OPD Pharmacy,80,vial/amp,2024-02-07,Sanjivani Drug House
B01917,CP24H643,Isoniazid 300mg Tablet,Isoniazid (300mg),Tablet,Cadila Pharmaceuticals Ltd,Anti-TB,2024-08,2026-08,Emergency Store,80,strip,2024-10-21,Apollo Wholesale Pvt Ltd
B01918,ZCX251117,Ipramist 250mcg Inhaler,Ipratropium (250mcg),Inhaler,Zydus Cadila,Respiratory,2025-04,2027-04,Main Pharmacy,60,inhaler,2025-05-24,Sanjivani Drug House
B01919,LLT241798,Tonact 10 Tablet,Atorvastatin (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-06,2027-06,ICU Store,20,strip,2024-07-06,Malabar Pharma Distributors
B01920,ALV251673,Metrokem IV 100mg Infusion,Metronidazole (100mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-02,2027-02,OT Store,100,bottle,2024-03-14,Malabar Pharma Distributors
B01921,IRX257185,Ambrocon 7.5mg Oral Drops,Ambroxol (7.5mg),Drops,Ikon Remedies Pvt Ltd,Respiratory,2024-01,2026-04,OPD Pharmacy,30,bottle,2024-03-28,Sree Pharma Agencies
B01922,LL25B109,Cetil 1.5gm Injection,Cefuroxime (1.5gm),Injection,Lupin Ltd,Antibiotic,2024-05,2027-05,Ward Store (Paeds),0,vial/amp,2024-08-19,Sanjivani Drug House
B01923,PL24B348,Medrol 32mg Tablet,Methylprednisolone (32mg),Tablet,Pfizer Ltd,Steroid,2025-03,2028-03,OT Store,200,strip,2025-04-15,Malabar Pharma Distributors
B01924,TP25G337,Maxizon 1gm Injection,Ceftriaxone (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2025-01,2028-01,Ward Store (Paeds),300,vial/amp,2025-03-13,Sree Pharma Agencies
B01925,ALT255812,Gblin 150mg Tablet,Pregabalin (150mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-01,2027-01,Ward Store (Paeds),120,strip,2024-04-06,Sree Pharma Agencies
B01926,CLV250374,Dextrose 25% Infusion,Dextrose (25% w/v),Infusion,Claris Lifesciences Ltd,IV Fluids,2024-06,2027-06,Emergency Store,150,bottle,2024-09-01,"Medline Distributors, Thiruvananthapuram"
B01927,LLI254932,Merenz 1000mg Injection,Meropenem (1000mg),Injection,Lupin Ltd,Antibiotic,2024-02,2027-02,Ward Store (Paeds),200,vial/amp,2024-03-11,"Medline Distributors, Thiruvananthapuram"
B01928,IL24B586,Zerodol PT Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Ipca Laboratories Ltd,Analgesic/Antipyretic,2025-03,2027-03,ICU Store,300,strip,2025-04-07,Sanjivani Drug House
B01929,SPX257255,Sucral Ano Cream,Lidocaine (4% w/w) + Metronidazole (1% w/w),Cream,Strassenburg Pharmaceuticals.Ltd,Antibiotic,2024-11,2026-05,OPD Pharmacy,10,tube,2024-12-13,Malabar Pharma Distributors
B01930,T2504-162,Eliwel 10mg Tablet,Amitriptyline (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2026-01,OT Store,20,strip,2024-03-25,Apollo Wholesale Pvt Ltd
B01931,61889106,Entofoam NF Cream,Hydrocortisone (10% w/w),Cream,Cipla Ltd,Steroid,2024-04,2026-04,Ward Store (Paeds),0,tube,2024-07-24,Sanjivani Drug House
B01932,T2507-341,Drotin DS Tablet,Drotaverine (80mg),Tablet,Walter Bushnell,Gastro,2024-02,2026-02,ICU Store,40,strip,2024-03-04,Sree Pharma Agencies
B01933,66812031,Gabantin 100 Capsule,Gabapentin (100mg),Capsule,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-08,2026-08,Emergency Store,20,strip,2024-10-11,Sree Pharma Agencies
B01934,C2507-047,Urimax 0.4 Ecopack Capsule MR,Tamsulosin (400mcg),Capsule,Cipla Ltd,Urology,2024-12,2026-12,Emergency Store,50,strip,2025-02-06,Malabar Pharma Distributors
B01935,V2506-022,Ciprobid 200mg Infusion,Ciprofloxacin (200mg),Infusion,Zydus Cadila,Antibiotic,2024-12,2026-06,Main Pharmacy,40,bottle,2025-01-17,Sree Pharma Agencies
B01936,MP25D418,Tranomac 500mg Injection,Tranexamic Acid (500mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Haematology,2024-05,2027-05,Emergency Store,120,vial/amp,2024-08-27,Sanjivani Drug House
B01937,IPI251475,Intagenta 40mg Injection,Gentamicin (40mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-04,2027-04,Main Pharmacy,80,vial/amp,2024-05-18,Kerala Medical Supplies Co.
B01938,IP25M341,Pregabid 300mg Capsule,Pregabalin (300mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2026-06,Emergency Store,30,strip,2024-09-11,Sanjivani Drug House
B01939,CP24F498,Isoniazid 300mg Tablet,Isoniazid (300mg),Tablet,Cadila Pharmaceuticals Ltd,Anti-TB,2024-03,2025-09,Main Pharmacy,20,strip,2024-06-24,Malabar Pharma Distributors
B01940,50961563,Alcef O 100mg Tablet DT,Cefixime (100mg),Tablet,Micro Labs Ltd,Antibiotic,2024-07,2026-07,ICU Store,10,strip,2024-10-15,Apollo Wholesale Pvt Ltd
B01941,AL25J558,Tobrex 2X Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alcon Laboratories,Ophthalmology,2024-09,2026-09,Emergency Store,30,bottle,2024-09-28,Malabar Pharma Distributors
B01942,DJ25G290,Paracetamol IV Infusion 1%,Paracetamol (10mg/ml),Infusion,D.J. Laboratories Pvt. Ltd.,Analgesic/Antipyretic,2025-04,2027-04,OPD Pharmacy,30,bottle,2025-04-27,Sree Pharma Agencies
B01943,CLI242823,Enclex 40 Injection,Enoxaparin (40mg),Injection,Cipla Ltd,Anticoagulant,2024-06,2025-12,Emergency Store,50,vial/amp,2024-06-27,Malabar Pharma Distributors
B01944,MPT248275,Anti-Thyrox 10 Tablet,Carbimazole (10mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Endocrine,2024-01,2026-12,ICU Store,0,strip,2024-02-13,Sanjivani Drug House
B01945,T2502-134,Naari Cal Tablet,Calcium Citrate Malate (1000mg) + Vitamin D3 (100IU),Tablet,Jagsonpal Pharmaceuticals Ltd,Supplement,2024-01,2027-01,OT Store,120,strip,2024-04-05,Sree Pharma Agencies
B01946,IP24M067,Halo 5mg Capsule,Haloperidol (5mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-04,2026-04,Ward Store (Paeds),200,strip,2024-07-07,Kerala Medical Supplies Co.
B01947,T2404-143,Azulix 0.5 MF Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-07,2027-07,OPD Pharmacy,80,strip,2024-10-21,Apollo Wholesale Pvt Ltd
B01948,51637850,Moxicip Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Cipla Ltd,Ophthalmology,2024-01,2026-01,OPD Pharmacy,20,bottle,2024-02-07,Kerala Medical Supplies Co.
B01949,I2506-074,Aqsusten 25 Solution for Injection,Progesterone (Natural Micronized) (25mg),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-09,2026-09,Ward Store (Paeds),300,vial/amp,2024-11-10,Apollo Wholesale Pvt Ltd
B01950,T2511-295,Losalife 25mg Tablet,Losartan (25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-06,2025-12,Main Pharmacy,30,strip,2024-07-29,Sree Pharma Agencies
B01951,X2507-561,Ambrocon 7.5mg Oral Drops,Ambroxol (7.5mg),Drops,Ikon Remedies Pvt Ltd,Respiratory,2024-01,2026-01,Ward Store (Paeds),50,bottle,2024-01-26,Apollo Wholesale Pvt Ltd
B01952,19769429,Torvate 1000mg Tablet,Sodium Valproate (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2026-01,Main Pharmacy,40,strip,2024-01-29,Sanjivani Drug House
B01953,T2410-422,Xamic 250mg Tablet,Tranexamic Acid (250mg),Tablet,Torrent Pharmaceuticals Ltd,Haematology,2024-08,2026-08,ICU Store,120,strip,2024-10-19,"Medline Distributors, Thiruvananthapuram"
B01954,T2506-460,Bipacef 500 Tablet,Cefuroxime (500mg),Tablet,Micro Labs Ltd,Antibiotic,2024-07,2027-07,Main Pharmacy,200,strip,2024-10-14,Apollo Wholesale Pvt Ltd
B01955,T2510-635,Rosuvas 20 Tablet,Rosuvastatin (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2026-09,Ward Store (Paeds),80,strip,2024-10-23,Sanjivani Drug House
B01956,MLT242263,Lasipen 40mg Tablet,Furosemide (40mg),Tablet,Morepen Laboratories Ltd,Cardiovascular,2024-04,2027-04,Main Pharmacy,150,strip,2024-05-05,Malabar Pharma Distributors
B01957,RV24012,Onvin-4 MD Tablet,Ondansetron (4mg),Tablet,Rivpra Formulation Pvt. Ltd.,Gastro,2024-05,2026-04,OPD Pharmacy,200,strip,2024-08-25,Sree Pharma Agencies
B01958,CL24C239,Ramipres 1.25 Tablet,Ramipril (1.25mg),Tablet,Cipla Ltd,Cardiovascular,2024-08,2026-02,ICU Store,120,strip,2024-09-01,Sanjivani Drug House
B01959,MLV245229,Linosept 200mg Infusion,Linezolid (200mg),Infusion,Micro Labs Ltd,Antibiotic,2025-03,2028-03,Ward Store (Paeds),200,bottle,2025-05-30,Sanjivani Drug House
B01960,LH24A623,Telvilite 40mg Tablet,Telmisartan (40mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2025-03,2028-03,Ward Store (Paeds),0,strip,2025-04-01,Kerala Medical Supplies Co.
B01961,IR24C574,Asthabon 2mg Syrup,Salbutamol (2mg/5ml),Syrup,Ikon Remedies Pvt Ltd,Respiratory,2024-04,2027-04,OT Store,120,bottle,2024-05-30,Apollo Wholesale Pvt Ltd
B01962,SP25G314,Teleact AM Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-11,2027-11,OPD Pharmacy,0,strip,2024-12-16,Apollo Wholesale Pvt Ltd
B01963,33260196,Unimegyl 200mg Tablet,Metronidazole (200mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2025-02,2027-02,Ward Store (Paeds),60,strip,2025-05-09,Kerala Medical Supplies Co.
B01964,I2502-586,Vitamin C Injection,Vitamin C (150mg),Injection,Mankind Pharma Ltd,Supplement,2024-12,2026-06,Main Pharmacy,0,vial/amp,2025-01-11,Sanjivani Drug House
B01965,38950113,Cadipar 250mg Oral Suspension,Paracetamol (250mg),Suspension,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-05,2028-05,Ward Store (Paeds),80,bottle,2025-07-15,Apollo Wholesale Pvt Ltd
B01966,CB25A319,Cgfru 40mg Tablet,Furosemide (40mg),Tablet,Cmg Biotech Pvt Ltd,Cardiovascular,2024-10,2026-10,OT Store,120,strip,2025-01-16,Sree Pharma Agencies
B01967,SPT247999,Dapefy 10mg Tablet,Dapagliflozin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-12,2026-12,Main Pharmacy,10,strip,2025-01-08,Apollo Wholesale Pvt Ltd
B01968,NP25C096,Frusenat Injection,Furosemide (20mg/ml),Injection,Natco Pharma Ltd,Cardiovascular,2024-02,2025-08,OT Store,100,vial/amp,2024-05-09,Kerala Medical Supplies Co.
B01969,IPT249173,Zolax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2025-09,Ward Store (Paeds),200,strip,2024-04-06,Kerala Medical Supplies Co.
B01970,CL24L409,Diaryl 1mg Tablet,Glimepiride (1mg),Tablet,Cipla Ltd,Diabetes,2025-03,2028-03,OPD Pharmacy,20,strip,2025-05-28,"Medline Distributors, Thiruvananthapuram"
B01971,AL24D336,Gblin 150mg Tablet,Pregabalin (150mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-06,2027-06,Emergency Store,100,strip,2024-08-01,Malabar Pharma Distributors
B01972,98027250,Cefabest 200 Tablet,Cefpodoxime Proxetil (200mg),Tablet,Zydus Cadila,Antibiotic,2025-02,2026-08,OPD Pharmacy,50,strip,2025-03-16,Apollo Wholesale Pvt Ltd
B01973,16727120,E Prin 75mg Tablet,Aspirin (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-01,2028-01,OT Store,50,strip,2025-03-17,Sanjivani Drug House
B01974,I2402-317,Dalcinex 150mg Injection,Clindamycin (150mg),Injection,Cipla Ltd,Antibiotic,2024-03,2026-03,ICU Store,300,vial/amp,2024-04-13,Apollo Wholesale Pvt Ltd
B01975,SF25D751,Burnosaf Plus Cream,Silver Sulfadiazine (1% w/w),Cream,SAF Fermion Ltd,Dermatology,2024-12,2026-12,OT Store,30,tube,2025-01-04,Sree Pharma Agencies
B01976,47557512,Aldactone 100 Tablet,Spironolactone (100mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2024-07,2027-07,OPD Pharmacy,0,strip,2024-08-06,Sanjivani Drug House
B01977,41026926,Susten 100 Soft Gelatin Capsule,Progesterone (Natural Micronized) (100mg),Gel,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-01,2026-01,Ward Store (Paeds),100,tube,2024-03-14,"Medline Distributors, Thiruvananthapuram"
B01978,SP25C790,Rancort 6mg Tablet,Deflazacort (6mg),Tablet,Sun Pharmaceutical Industries Ltd,Steroid,2024-06,2026-06,Emergency Store,300,strip,2024-09-15,Sanjivani Drug House
B01979,TP25E341,Uniprest Tablet,Misoprostol (NA),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-03,2027-03,OT Store,30,strip,2024-06-04,Kerala Medical Supplies Co.
B01980,TPT256269,Anxipar 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2026-07,Ward Store (Paeds),200,strip,2024-10-25,Kerala Medical Supplies Co.
B01981,28416939,Lukotas 3D Tablet,Montelukast (10mg) + Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2025-05,2026-11,Main Pharmacy,200,strip,2025-06-20,Apollo Wholesale Pvt Ltd
B01982,RLT256538,Aldactone 50 Tablet,Spironolactone (50mg),Tablet,RPG Life Sciences Ltd,Cardiovascular,2024-12,2026-12,ICU Store,200,strip,2025-03-25,Kerala Medical Supplies Co.
B01983,TP25D648,Pregalin 100mg Capsule,Pregabalin (100mg),Capsule,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-03,2025-09,OT Store,0,strip,2024-06-24,"Medline Distributors, Thiruvananthapuram"
B01984,66600975,Bupitroy 0.5% Injection,Bupivacaine (0.5%),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-04,2027-04,Emergency Store,50,vial/amp,2024-05-13,Kerala Medical Supplies Co.
B01985,MPI258120,Ondamac 2mg Injection,Ondansetron (2mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-04,2027-04,OT Store,10,vial/amp,2025-07-11,Apollo Wholesale Pvt Ltd
B01986,CLT254470,Metolar 50 Tablet,Metoprolol Tartrate (50mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2027-10,OT Store,10,strip,2024-12-18,Malabar Pharma Distributors
B01987,CLT245203,Cetcip-L Tablet,Levocetirizine (5mg),Tablet,Cipla Ltd,Respiratory,2025-01,2028-01,Main Pharmacy,40,strip,2025-03-07,Sanjivani Drug House
B01988,SPT251329,Ceplox 750mg Tablet,Ciprofloxacin (750mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-05,2025-11,Ward Store (Paeds),50,strip,2024-06-28,Sanjivani Drug House
B01989,MPI242547,Vitamin C Injection,Vitamin C (150mg),Injection,Mankind Pharma Ltd,Supplement,2024-09,2026-09,Main Pharmacy,80,vial/amp,2024-12-07,Kerala Medical Supplies Co.
B01990,X2502-342,Tromacyn Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2024-08,2026-02,ICU Store,80,bottle,2024-11-22,Kerala Medical Supplies Co.
B01991,EWT254219,Caxin 0.25mg Tablet,Digoxin (0.25mg),Tablet,East West Pharma,Cardiovascular,2024-08,2027-08,OPD Pharmacy,10,strip,2024-11-06,Malabar Pharma Distributors
B01992,10474177,Eltroxin 25mcg Tablet,Thyroxine (25mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2024-11,2026-05,ICU Store,300,strip,2025-02-13,"Medline Distributors, Thiruvananthapuram"
B01993,ZCT259220,Fusys 150 Tablet,Fluconazole (150mg),Tablet,Zydus Cadila,Antifungal,2024-08,2026-08,Ward Store (Paeds),40,strip,2024-11-01,"Medline Distributors, Thiruvananthapuram"
B01994,GSS246537,Zentel Oral Suspension,Albendazole (400mg),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2024-05,2027-05,OPD Pharmacy,80,bottle,2024-06-22,Malabar Pharma Distributors
B01995,64922351,Abd 200mg Suspension,Albendazole (200mg),Suspension,Intas Pharmaceuticals Ltd,Anthelmintic,2024-07,2026-07,OT Store,0,bottle,2024-10-22,Apollo Wholesale Pvt Ltd
B01996,TP25F217,Cocorex 10mg Syrup,Chlorpheniramine Maleate (10mg),Syrup,Taj Pharma India Ltd,Anti-allergic,2024-11,2027-11,Main Pharmacy,100,bottle,2025-02-09,Sanjivani Drug House
B01997,I2511-127,Cefbact 1000mg Injection,Ceftriaxone (1000mg),Injection,Cipla Ltd,Antibiotic,2025-05,2027-05,Emergency Store,20,vial/amp,2025-07-15,Malabar Pharma Distributors
B01998,ML25G359,Calvit 12 Injection,Calcium (137.5mg) + Vitamin D3 (5000IU),Injection,Marc Laboratories Pvt Ltd,Supplement,2025-05,2028-05,Emergency Store,20,vial/amp,2025-07-15,Sanjivani Drug House
B01999,IPT254418,T Glip 20 Tablet,Teneligliptin (20mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-09,2027-09,Emergency Store,80,strip,2024-12-18,Malabar Pharma Distributors
B02000,49613214,Ondem -MD 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2025-03,2027-03,Main Pharmacy,50,strip,2025-06-29,Apollo Wholesale Pvt Ltd
B02001,IP25M796,ZEN 100 Tablet DT,Carbamazepine (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2026-01,ICU Store,100,strip,2024-01-28,Sree Pharma Agencies
B02002,LL25C785,Ipneb Solution for inhalation,Ipratropium (250mcg),Solution,Lupin Ltd,Respiratory,2024-09,2027-09,Ward Store (Paeds),200,bottle,2024-12-18,Kerala Medical Supplies Co.
B02003,AYC-2407,Azithromycin Tablets IP 500 mg,Azithromycin (500mg),Tablet,Apple Formulations Pvt. Ltd.,Antibiotic,2024-01,2025-12,ICU Store,60,strip,2024-02-28,Apollo Wholesale Pvt Ltd
B02004,MPT253115,Janumet 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-11,2026-11,Main Pharmacy,150,strip,2025-02-03,Sanjivani Drug House
B02005,TP24B115,Ampoxin-CV 200mg/28.5mg Suspension,Amoxycillin (200mg) + Clavulanic Acid (28.5mg),Suspension,Torrent Pharmaceuticals Ltd,Antibiotic,2025-04,2028-04,Ward Store (Paeds),120,bottle,2025-04-27,"Medline Distributors, Thiruvananthapuram"
B02006,I2410-848,Merinta 1000mg Injection,Meropenem (1000mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-09,2027-09,OPD Pharmacy,100,vial/amp,2024-10-12,Apollo Wholesale Pvt Ltd
B02007,SP24E993,Teleact AM Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2027-06,OT Store,10,strip,2024-07-28,"Medline Distributors, Thiruvananthapuram"
B02008,ALX252678,Mupikem Cream,Mupirocin (2% w/w),Cream,Alkem Laboratories Ltd,Dermatology,2024-01,2026-01,Emergency Store,40,tube,2024-04-13,Sree Pharma Agencies
B02009,T2510-237,Nexito 15mg Tablet,Escitalopram Oxalate (15mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2026-01,ICU Store,100,strip,2024-07-26,Sree Pharma Agencies
B02010,95377710,Uniprest Tablet,Misoprostol (NA),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2025-05,2026-11,OT Store,100,strip,2025-07-02,Malabar Pharma Distributors
B02011,86166246,Ultracet Tablet,Paracetamol/Acetaminophen (325mg) + Tramadol (37.5mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2024-12,2026-06,Emergency Store,20,strip,2024-12-30,Kerala Medical Supplies Co.
B02012,ML25J560,Arbitel 20 Tablet,Telmisartan (20mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-04,2027-04,ICU Store,40,strip,2024-05-07,Kerala Medical Supplies Co.
B02013,S2512-764,Ambrodil Syrup,Ambroxol (30mg/5ml),Syrup,Aristo Pharmaceuticals Pvt Ltd,Respiratory,2024-08,2026-02,Main Pharmacy,30,bottle,2024-10-11,Malabar Pharma Distributors
B02014,96825012,Aneket 10mg Injection,Ketamine (10mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-08,2026-08,OT Store,30,vial/amp,2024-10-03,Sanjivani Drug House
B02015,LLS257707,Lupicip 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Lupin Ltd,Analgesic/Antipyretic,2025-03,2028-03,Main Pharmacy,150,bottle,2025-06-24,Malabar Pharma Distributors
B02016,T2508-877,Deviry 10mg Tablet,Medroxyprogesterone acetate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-07,2026-01,OT Store,200,strip,2024-08-29,Malabar Pharma Distributors
B02017,CL25D295,Acivir 200 DT Tablet,Acyclovir (200mg),Tablet,Cipla Ltd,Antiviral,2024-12,2026-12,ICU Store,60,strip,2025-01-01,Apollo Wholesale Pvt Ltd
B02018,56819717,Metrocare 500mg Infusion,Metronidazole (500mg),Infusion,Mankind Pharma Ltd,Antibiotic,2024-06,2027-06,OT Store,100,bottle,2024-09-24,Sanjivani Drug House
B02019,25604379,Intagenta 40mg Injection,Gentamicin (40mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2025-02,2028-02,Ward Store (Paeds),20,vial/amp,2025-03-09,"Medline Distributors, Thiruvananthapuram"
B02020,TP25M472,Cipbact 500mg Tablet,Ciprofloxacin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-02,2026-02,OPD Pharmacy,100,strip,2024-04-19,Malabar Pharma Distributors
B02021,12637090,Bisonext 10 Tablet,Bisoprolol (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-02,2025-08,ICU Store,150,strip,2024-05-31,Sanjivani Drug House
B02022,I2504-440,Ultimox CV 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Emcure Pharmaceuticals Ltd,Antibiotic,2024-02,2026-02,OPD Pharmacy,60,vial/amp,2024-05-25,Apollo Wholesale Pvt Ltd
B02023,57055917,Macox 300mg Capsule,Rifampicin (300mg),Capsule,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2025-04,2027-04,OT Store,300,strip,2025-06-08,Kerala Medical Supplies Co.
B02024,83674105,Olexa 10mg Tablet,Olanzapine (10mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-01,2028-01,Main Pharmacy,0,strip,2025-02-28,Sanjivani Drug House
B02025,PLC254610,Lyrica 75mg Capsule,Pregabalin (75mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-09,2026-09,OPD Pharmacy,100,strip,2024-12-11,"Medline Distributors, Thiruvananthapuram"
B02026,IPV249775,C Flox 200mg Infusion,Ciprofloxacin (200mg),Infusion,Intas Pharmaceuticals Ltd,Antibiotic,2024-10,2027-10,ICU Store,100,bottle,2025-01-01,Kerala Medical Supplies Co.
B02027,T2504-549,Nugrel Tablet,Clopidogrel (75mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-07,2026-01,Emergency Store,50,strip,2024-09-11,Sanjivani Drug House
B02028,21318464,Razo A 200mg/20mg Capsule SR,Aceclofenac (200mg) + Rabeprazole (20mg),Capsule,Precise Lifescience,Gastro,2024-08,2026-02,OPD Pharmacy,150,strip,2024-10-29,"Medline Distributors, Thiruvananthapuram"
B02029,IPT257647,Losartas 25 Tablet,Losartan (25mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-05,2027-05,OPD Pharmacy,60,strip,2025-07-15,Sree Pharma Agencies
B02030,SP24E494,Rancort 6mg Tablet,Deflazacort (6mg),Tablet,Sun Pharmaceutical Industries Ltd,Steroid,2024-10,2027-10,OPD Pharmacy,30,strip,2024-12-12,Apollo Wholesale Pvt Ltd
B02031,TP25G014,Dibeta SR 1gm Tablet,Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-09,2027-09,ICU Store,30,strip,2024-11-08,Sree Pharma Agencies
B02032,A25B418,Acevah P 100 mg/325 mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Abbott,Analgesic/Antipyretic,2024-12,2026-06,OPD Pharmacy,20,strip,2025-01-27,Apollo Wholesale Pvt Ltd
B02033,CL24L979,Defshield Tablet,Deflazacort (6mg),Tablet,Cipla Ltd,Steroid,2024-07,2026-01,Main Pharmacy,10,strip,2024-09-28,Apollo Wholesale Pvt Ltd
B02034,LLS259463,Lupibend 200mg Suspension,Albendazole (200mg),Suspension,Lupin Ltd,Anthelmintic,2024-10,2027-10,ICU Store,60,bottle,2025-01-16,Malabar Pharma Distributors
B02035,SPX255685,Toba Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2025-03,2027-03,Main Pharmacy,40,bottle,2025-05-15,"Medline Distributors, Thiruvananthapuram"
B02036,JBT249350,Rantac 150 Tablet,Ranitidine (150mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-01,2026-01,Emergency Store,10,strip,2024-02-21,Sree Pharma Agencies
B02037,73142083,Nugrel Tablet,Clopidogrel (75mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-12,2027-12,Ward Store (Paeds),200,strip,2025-01-16,"Medline Distributors, Thiruvananthapuram"
B02038,ZC24D979,CoviQ Tablet,Hydroxychloroquine (200mg),Tablet,Zydus Cadila,Antimalarial,2024-07,2026-01,Emergency Store,40,strip,2024-08-06,Malabar Pharma Distributors
B02039,IPI255422,Prexaron 250mg Injection,Citicoline (250mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2027-08,Emergency Store,20,vial/amp,2024-09-16,Malabar Pharma Distributors
B02040,AI243863,Lofh 25000IU Injection,Heparin (25000IU),Injection,Abbott,Anticoagulant,2025-01,2027-01,OPD Pharmacy,30,vial/amp,2025-01-28,Kerala Medical Supplies Co.
B02041,IPT246678,Zevert 12 SR Tablet,Betahistine (12mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2026-08,Emergency Store,150,strip,2024-11-18,Kerala Medical Supplies Co.
B02042,CLT243567,Epizam 0.25mg Tablet MD,Clonazepam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-02,2027-02,OPD Pharmacy,120,strip,2024-04-13,Apollo Wholesale Pvt Ltd
B02043,73360324,Cetzine Syrup,Cetirizine (5mg/5ml),Syrup,Dr Reddy's Laboratories Ltd,Respiratory,2024-09,2026-03,OT Store,40,bottle,2024-09-30,Sree Pharma Agencies
B02044,CL25J213,Vanlid 250mg Capsule,Vancomycin (250mg),Capsule,Cipla Ltd,Antibiotic,2024-11,2026-05,OT Store,100,strip,2024-12-16,Malabar Pharma Distributors
B02045,C2505-024,Omesec 20 Capsule,Omeprazole (20mg),Capsule,Sun Pharmaceutical Industries Ltd,Gastro,2024-08,2027-08,OT Store,120,strip,2024-11-23,"Medline Distributors, Thiruvananthapuram"
B02046,AL25E178,Azento 250mg Tablet,Azithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-09,2026-03,OPD Pharmacy,30,strip,2024-12-27,Apollo Wholesale Pvt Ltd
B02047,42331122,TOR 10 Tablet,Torasemide (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-05,2026-05,Ward Store (Paeds),10,strip,2024-06-04,Kerala Medical Supplies Co.
B02048,ALT259111,Dapanorm 10 Tablet,Dapagliflozin (10mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-05,2026-11,Ward Store (Paeds),10,strip,2025-07-06,Sanjivani Drug House
B02049,HLI380C,Dexasun Injection,Dexamethasone Sodium Phosphate (4mg/ml),Injection,Himalaya Meditek (P) Ltd.,Steroid,2024-03,2026-02,Main Pharmacy,100,vial/amp,2024-05-21,"Medline Distributors, Thiruvananthapuram"
B02050,T2503-277,CEPOCOR 100MG TABLET,Cefpodoxime Proxetil (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-05,2025-11,OPD Pharmacy,150,strip,2024-06-01,Sree Pharma Agencies
B02051,JP25A785,Naari Cal Tablet,Calcium Citrate Malate (1000mg) + Vitamin D3 (100IU),Tablet,Jagsonpal Pharmaceuticals Ltd,Supplement,2024-02,2027-02,Emergency Store,30,strip,2024-05-19,Sanjivani Drug House
B02052,ZC24L306,Ciprobid 10mg Injection,Ciprofloxacin (10mg),Injection,Zydus Cadila,Antibiotic,2024-11,2027-11,OPD Pharmacy,30,vial/amp,2025-01-18,Apollo Wholesale Pvt Ltd
B02053,38483372,Aceclopure SP Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-08,2026-08,Ward Store (Paeds),60,strip,2024-11-25,Apollo Wholesale Pvt Ltd
B02054,I2409-302,Amoxyclav 1000 mg/200 mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Abbott,Antibiotic,2024-09,2026-03,OPD Pharmacy,50,vial/amp,2024-10-15,"Medline Distributors, Thiruvananthapuram"
B02055,TPT242169,Olmetor 10mg Tablet,Olmesartan Medoxomil (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-12,2026-12,OPD Pharmacy,120,strip,2025-01-20,Malabar Pharma Distributors
B02056,CLX244698,Ataron Eye Drop,Atropine (1% w/v),Eye Drops,Cipla Ltd,Anaesthesia/Critical care,2024-09,2026-09,OT Store,150,bottle,2024-11-13,Sanjivani Drug House
B02057,C2403-103,Alcros SB 50 Capsule,Itraconazole (50mg),Capsule,Sun Pharmaceutical Industries Ltd,Antifungal,2024-09,2027-09,OPD Pharmacy,50,strip,2024-09-27,"Medline Distributors, Thiruvananthapuram"
B02058,T2411-137,Amlyse 30mg Tablet,Ambroxol (30mg),Tablet,Neon Laboratories Ltd,Respiratory,2024-12,2027-12,OT Store,120,strip,2025-01-21,Kerala Medical Supplies Co.
B02059,46218400,Cipbact 500mg Tablet,Ciprofloxacin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-01,2026-01,OPD Pharmacy,150,strip,2024-02-27,"Medline Distributors, Thiruvananthapuram"
B02060,TPI255822,Thrombiflo 20mg Injection,Enoxaparin (20mg),Injection,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-01,2027-01,OPD Pharmacy,10,vial/amp,2024-04-04,Sanjivani Drug House
B02061,TPI253370,Panomp 40mg Injection,Pantoprazole (40mg),Injection,Torrent Pharmaceuticals Ltd,Gastro,2024-12,2027-12,OT Store,60,vial/amp,2025-02-24,"Medline Distributors, Thiruvananthapuram"
B02062,I2409-657,Magnex 1g Injection,Cefoperazone (500mg) + Sulbactam (500mg),Injection,Pfizer Ltd,Antibiotic,2025-03,2027-03,Emergency Store,120,vial/amp,2025-04-16,Sree Pharma Agencies
B02063,ALT247774,Alert L 5mg Tablet,Levocetirizine (5mg),Tablet,Alkem Laboratories Ltd,Respiratory,2025-03,2027-03,Main Pharmacy,40,strip,2025-05-03,Sanjivani Drug House
B02064,T2502-478,Bruriff 400mg Tablet,Ibuprofen (400mg),Tablet,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-07,2026-01,OPD Pharmacy,100,strip,2024-08-09,Apollo Wholesale Pvt Ltd
B02065,TP24C765,Ursetor 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-11,2026-05,OPD Pharmacy,100,strip,2025-02-21,Apollo Wholesale Pvt Ltd
B02066,FI24B071,Otrilom-S Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Fawn Incorporation,IV Fluids,2024-01,2026-01,ICU Store,30,bottle,2024-04-29,Sanjivani Drug House
B02067,LL24L978,R-Cin 300 Capsule,Rifampicin (300mg),Capsule,Lupin Ltd,Anti-TB,2025-04,2027-04,ICU Store,10,strip,2025-06-07,Apollo Wholesale Pvt Ltd
B02068,CPT256716,Genmox CV 500 mg/125 mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Cadila Pharmaceuticals Ltd,Antibiotic,2025-01,2027-01,Ward Store (Paeds),120,strip,2025-03-18,"Medline Distributors, Thiruvananthapuram"
B02069,53081518,Oncotrex 2.5mg Tablet,Methotrexate (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Oncology,2025-03,2027-03,Ward Store (Paeds),300,strip,2025-06-26,Malabar Pharma Distributors
B02070,DR25H656,Razo 10 Tablet,Rabeprazole (10mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-06,2026-06,ICU Store,300,strip,2024-08-03,Sanjivani Drug House
B02071,V2402-731,Metrocip 500mg Infusion,Metronidazole (500mg),Infusion,Cipla Ltd,Antibiotic,2024-06,2026-06,Ward Store (Paeds),20,bottle,2024-07-30,Sree Pharma Agencies
B02072,V2412-210,Lupigyl IV 500mg Infusion,Metronidazole (500mg),Infusion,Lupin Ltd,Antibiotic,2024-02,2027-02,Emergency Store,20,bottle,2024-05-02,Malabar Pharma Distributors
B02073,29907683,Clavam 625 Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-03,2027-03,OPD Pharmacy,200,strip,2025-04-06,Kerala Medical Supplies Co.
B02074,CL24A975,Defshield Tablet,Deflazacort (6mg),Tablet,Cipla Ltd,Steroid,2024-07,2026-01,Emergency Store,40,strip,2024-08-07,Sanjivani Drug House
B02075,I2509-512,Alfakim 100mg Injection,Amikacin (100mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-01,2027-01,OPD Pharmacy,150,vial/amp,2025-03-07,Kerala Medical Supplies Co.
B02076,T2405-467,Roles 10mg Tablet,Rabeprazole (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-10,2027-10,Ward Store (Paeds),30,strip,2024-11-30,Sanjivani Drug House
B02077,35479101,Dexona 6mg Tablet,Dexamethasone (6mg),Tablet,Zydus Cadila,Steroid,2024-03,2026-03,Emergency Store,80,strip,2024-04-15,Apollo Wholesale Pvt Ltd
B02078,TPI243646,Unimika 100mg Injection,Amikacin (100mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2025-04,2027-04,Emergency Store,300,vial/amp,2025-05-07,Sree Pharma Agencies
B02079,13991574,Asthalin Respirator Solution,Salbutamol (5mg),Solution,Cipla Ltd,Respiratory,2025-02,2028-02,OPD Pharmacy,60,bottle,2025-04-19,Sree Pharma Agencies
B02080,75023164,Mox 500mg Capsule,Amoxycillin (500mg),Capsule,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-08,2026-08,Main Pharmacy,50,strip,2024-10-31,Sanjivani Drug House
B02081,ZC25E558,Nexiron Injection,Iron Sucrose (100mg/5ml),Injection,Zydus Cadila,Haematology,2024-11,2027-11,Ward Store (Paeds),100,vial/amp,2025-02-16,Sree Pharma Agencies
B02082,CLT241432,Levepsy 1000 Tablet,Levetiracetam (1000mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-10,2027-10,OPD Pharmacy,30,strip,2024-11-19,Kerala Medical Supplies Co.
B02083,58796241,Hicoly 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,OT Store,0,vial/amp,2025-03-21,Malabar Pharma Distributors
B02084,19510312,Azithral 500 Tablet,Azithromycin (500mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-04,2025-10,ICU Store,30,strip,2024-06-30,Malabar Pharma Distributors
B02085,27089453,Emeset 8 Tablet,Ondansetron (8mg),Tablet,Cipla Ltd,Gastro,2024-02,2027-02,Emergency Store,120,strip,2024-04-27,Apollo Wholesale Pvt Ltd
B02086,CL24F994,Restyl 0.5mg Tablet,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-02,2027-02,OT Store,150,strip,2024-04-24,Sanjivani Drug House
B02087,APT256487,Folinal 5mg Tablet,Folic Acid (5mg),Tablet,Alembic Pharmaceuticals Ltd,Haematology,2024-07,2026-07,Emergency Store,200,strip,2024-08-30,Sanjivani Drug House
B02088,T2401-579,Biselect 10 Tablet,Bisoprolol (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-03,2026-09,ICU Store,20,strip,2025-05-20,Sanjivani Drug House
B02089,CL24J772,Mupicip 2% Ointment,Mupirocin (2% w/w),Ointment,Cipla Ltd,Dermatology,2024-06,2026-06,Ward Store (Paeds),0,tube,2024-09-26,Sanjivani Drug House
B02090,T2401-748,Amlip 10 Tablet,Amlodipine (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2027-10,Ward Store (Paeds),30,strip,2024-12-12,Kerala Medical Supplies Co.
B02091,LLX259910,Salbair Resp 5mg Solution,Salbutamol (5mg),Solution,Lupin Ltd,Respiratory,2024-03,2027-03,Emergency Store,10,bottle,2024-04-17,Kerala Medical Supplies Co.
B02092,ML24L814,Gramocef 250mg Injection,Ceftriaxone (250mg),Injection,Micro Labs Ltd,Antibiotic,2024-12,2026-06,OT Store,60,vial/amp,2025-01-13,Malabar Pharma Distributors
B02093,T2505-546,Aldex 6mg Tablet SR,Dexchlorpheniramine (6mg),Tablet,Zee Laboratories,Anti-allergic,2024-10,2027-10,ICU Store,80,strip,2024-12-20,Sanjivani Drug House
B02094,25944033,Cefuroxime Sodium 750mg Injection,Cefuroxime (750mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2026-03,Emergency Store,80,vial/amp,2024-05-18,Apollo Wholesale Pvt Ltd
B02095,T2506-261,Dolex Tablet DT,Tramadol (NA),Tablet,Cipla Ltd,Analgesic/Antipyretic,2025-02,2028-02,Emergency Store,10,strip,2025-05-11,"Medline Distributors, Thiruvananthapuram"
B02096,CL25G014,Norflox Eye/Ear Drops,Norfloxacin (0.30%),Ear Drops,Cipla Ltd,Other,2024-03,2027-03,OPD Pharmacy,100,bottle,2024-03-30,Malabar Pharma Distributors
B02097,T2504-190,Happi 20 Tablet,Rabeprazole (20mg),Tablet,Zydus Cadila,Gastro,2025-04,2028-04,OT Store,0,strip,2025-05-10,"Medline Distributors, Thiruvananthapuram"
B02098,ALX247021,Tobraject 0.3% Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alkem Laboratories Ltd,Ophthalmology,2025-02,2027-02,Main Pharmacy,100,bottle,2025-03-01,Malabar Pharma Distributors
B02099,TPI245174,Cobasoft 500mcg Injection,Methylcobalamin (500mcg),Injection,Torrent Pharmaceuticals Ltd,Supplement,2025-04,2026-10,OT Store,50,vial/amp,2025-07-07,Sree Pharma Agencies
B02100,ALT253971,Angibloc 12.5mg Tablet ER,Metoprolol Succinate (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-04,2025-10,Main Pharmacy,150,strip,2024-06-14,Sanjivani Drug House
B02101,IPT245915,Zap 0.5mg Tablet,Clonazepam (0.5mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-01,2028-01,Main Pharmacy,30,strip,2025-01-30,Sree Pharma Agencies
B02102,AL24L067,Albekem 400mg Tablet,Albendazole (400mg),Tablet,Alkem Laboratories Ltd,Anthelmintic,2025-05,2027-05,OPD Pharmacy,60,strip,2025-07-15,Kerala Medical Supplies Co.
B02103,HSAL0050,Regimen Hand Rub (Aloevera 70% Alcohol),Alcohol hand rub,Solution,Chemstellar Chemicals Pvt. Ltd.,Infection control,2024-10,2026-10,OT Store,40,bottle,2025-01-06,Malabar Pharma Distributors
B02104,S2507-802,Lizintas 200mg Syrup,Linezolid (200mg),Syrup,Intas Pharmaceuticals Ltd,Antibiotic,2024-01,2026-01,Main Pharmacy,200,bottle,2024-04-28,"Medline Distributors, Thiruvananthapuram"
B02105,30011366,Teleact 20 Tablet,Telmisartan (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-11,2027-11,Ward Store (Paeds),50,strip,2024-11-28,Sanjivani Drug House
B02106,69945655,Ketorol Gel,Ketorolac (20mg),Gel,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2025-03,2026-09,OPD Pharmacy,40,tube,2025-03-27,Sree Pharma Agencies
B02107,MP25G722,Revidox 100mg Tablet,Doxycycline (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2025-04,2028-04,Ward Store (Paeds),60,strip,2025-05-12,Apollo Wholesale Pvt Ltd
B02108,65507111,Levocet M Kid Tablet MD,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Hetero Drugs Ltd,Respiratory,2025-04,2027-04,Main Pharmacy,40,strip,2025-06-03,Sanjivani Drug House
B02109,CP25F405,Cadipar 250mg Oral Suspension,Paracetamol (250mg),Suspension,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-11,2026-11,ICU Store,0,bottle,2025-01-12,Kerala Medical Supplies Co.
B02110,LL25G301,Ciprolup 250mg Tablet,Ciprofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-11,2027-11,Ward Store (Paeds),200,strip,2025-02-18,Apollo Wholesale Pvt Ltd
B02111,CLT243853,Vomistop 10 DT Tablet,Domperidone (10mg),Tablet,Cipla Ltd,Gastro,2025-03,2028-03,OPD Pharmacy,40,strip,2025-05-17,Sanjivani Drug House
B02112,T2406-561,Drotin A Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Walter Bushnell,Gastro,2024-09,2026-09,Main Pharmacy,150,strip,2024-09-27,"Medline Distributors, Thiruvananthapuram"
B02113,19792992,Albaxy Suspension,Albendazole (200mg),Suspension,Sun Pharmaceutical Industries Ltd,Anthelmintic,2024-08,2026-08,OT Store,30,bottle,2024-11-25,Sree Pharma Agencies
B02114,13817499,Ibubid 300mg Capsule TR,Ibuprofen (300mg),Capsule,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-11,2027-11,ICU Store,300,strip,2024-12-11,Apollo Wholesale Pvt Ltd
B02115,T2508-480,Ciplox 250 Tablet,Ciprofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2024-07,2027-07,OT Store,100,strip,2024-10-16,"Medline Distributors, Thiruvananthapuram"
B02116,53239585,Amlyse 30mg Tablet,Ambroxol (30mg),Tablet,Neon Laboratories Ltd,Respiratory,2025-01,2027-01,OPD Pharmacy,300,strip,2025-02-25,Apollo Wholesale Pvt Ltd
B02117,68742783,Labebet 100mg Injection,Labetalol (100mg),Injection,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2027-09,OPD Pharmacy,100,vial/amp,2024-09-27,"Medline Distributors, Thiruvananthapuram"
B02118,SP24J613,Flucomet Eye Drop,Fluconazole (0.3% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Antifungal,2024-08,2026-02,OT Store,120,bottle,2024-09-22,Kerala Medical Supplies Co.
B02119,LL25B698,Telect D 40mg/12.5mg Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Lupin Ltd,Cardiovascular,2024-01,2027-01,OPD Pharmacy,20,strip,2024-04-22,Sanjivani Drug House
B02120,17042688,Gramocef 250mg Injection,Ceftriaxone (250mg),Injection,Micro Labs Ltd,Antibiotic,2024-01,2026-10,Ward Store (Paeds),100,vial/amp,2024-02-10,Kerala Medical Supplies Co.
B02121,KTT24936,Telmamet AM Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Kantil Pharmaceuticals Pvt. Ltd.,Cardiovascular,2024-10,2026-09,Main Pharmacy,80,strip,2024-11-04,Sanjivani Drug House
B02122,T2509-050,Astin 10 Tablet,Atorvastatin (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-07,2026-07,ICU Store,100,strip,2024-09-23,Malabar Pharma Distributors
B02123,25460259,Cipride 200mg Infusion,Ciprofloxacin (200mg),Infusion,Torrent Pharmaceuticals Ltd,Antibiotic,2024-11,2026-11,Emergency Store,0,bottle,2024-12-02,Kerala Medical Supplies Co.
B02124,T2408-914,Aspent 60mg Tablet,Aspirin (60mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2026-04,Ward Store (Paeds),30,strip,2024-06-02,Kerala Medical Supplies Co.
B02125,CLT244866,Cognolin 500 Tablet,Citicoline (500mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2025-04,2027-04,OT Store,300,strip,2025-05-11,"Medline Distributors, Thiruvananthapuram"
B02126,SP24H185,Rosuvas F 10 Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-12,2026-12,ICU Store,20,strip,2025-01-22,Apollo Wholesale Pvt Ltd
B02127,26476859,Novigan 400mg Tablet,Ibuprofen (400mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2025-04,2028-04,Ward Store (Paeds),60,strip,2025-05-25,Apollo Wholesale Pvt Ltd
B02128,A25H179,Bupizuva 2.5mg Injection,Bupivacaine (2.5mg/ml),Injection,Abbott,Anaesthesia/Critical care,2024-10,2026-10,Main Pharmacy,0,vial/amp,2025-01-27,Apollo Wholesale Pvt Ltd
B02129,JPT245401,Ultracet 500mg/50mg Tablet,Paracetamol/Acetaminophen (500mg) + Tramadol (50mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2024-10,2026-10,OPD Pharmacy,0,strip,2024-11-02,Sanjivani Drug House
B02130,TP24A219,Nexpro 40 Tablet,Esomeprazole (40mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-01,2027-01,OPD Pharmacy,30,strip,2025-03-05,Kerala Medical Supplies Co.
B02131,ALX250878,Bodygard Gel,Diclofenac (NA),Gel,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-02,2028-02,OT Store,120,tube,2025-04-05,Sree Pharma Agencies
B02132,T2505-630,Contiflo Icon 0.4mg Tablet PR,Tamsulosin (0.4mg),Tablet,Sun Pharmaceutical Industries Ltd,Urology,2024-07,2026-07,ICU Store,80,strip,2024-09-18,"Medline Distributors, Thiruvananthapuram"
B02133,MPV252913,Finamac 1000mg Infusion,Paracetamol (1000mg),Infusion,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-07,2027-07,OT Store,30,bottle,2024-08-28,Kerala Medical Supplies Co.
B02134,CL24G892,Aspin 300mg Tablet DT,Aspirin (300mg),Tablet,Cipla Ltd,Cardiovascular,2024-06,2026-06,OT Store,100,strip,2024-07-30,"Medline Distributors, Thiruvananthapuram"
B02135,I2403-898,Merinta 1000mg Injection,Meropenem (1000mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-10,2027-10,OPD Pharmacy,0,vial/amp,2024-12-23,"Medline Distributors, Thiruvananthapuram"
B02136,CL24M272,Bendex 200mg Suspension,Albendazole (200mg),Suspension,Cipla Ltd,Anthelmintic,2025-02,2027-02,Ward Store (Paeds),200,bottle,2025-05-24,Apollo Wholesale Pvt Ltd
B02137,ZC25C981,Roxin 100mcg Tablet,Thyroxine (100mcg),Tablet,Zydus Cadila,Endocrine,2024-07,2026-01,OPD Pharmacy,60,strip,2024-10-19,Malabar Pharma Distributors
B02138,I2406-591,Trofentyl 50mcg Injection,Fentanyl (50mcg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-07,2026-07,OPD Pharmacy,200,vial/amp,2024-08-18,Malabar Pharma Distributors
B02139,SP25L639,Raciper 20 Tablet,Esomeprazole (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-10,2026-10,Ward Store (Paeds),0,strip,2025-01-09,Apollo Wholesale Pvt Ltd
B02140,FH25C364,Scorbix 1.5gm Injection,Vitamin C (1.5gm),Injection,Fusion Healthcare Pvt Ltd,Supplement,2025-04,2028-04,Emergency Store,10,vial/amp,2025-07-11,Sanjivani Drug House
B02141,85982862,Activa Plus Tablet,Diclofenac (NA),Tablet,Zydus Cadila,Analgesic/Antipyretic,2025-05,2028-05,Main Pharmacy,150,strip,2025-07-15,Sanjivani Drug House
B02142,22304198,Ondem 8 Tablet,Ondansetron (8mg),Tablet,Alkem Laboratories Ltd,Gastro,2025-04,2026-10,Ward Store (Paeds),30,strip,2025-07-15,Malabar Pharma Distributors
B02143,DRT259305,Zovanta 20mg Tablet,Pantoprazole (20mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-04,2025-10,ICU Store,300,strip,2024-05-14,Kerala Medical Supplies Co.
B02144,T2503-267,Epsolin ER 200 Tablet,Phenytoin (200mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-07,2027-07,Ward Store (Paeds),300,strip,2024-07-31,Sanjivani Drug House
B02145,25384377,Epsolin 100 Tablet,Phenytoin (100mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-04,2027-04,Emergency Store,150,strip,2024-05-19,"Medline Distributors, Thiruvananthapuram"
B02146,PLT246766,Medrol 16mg Tablet,Methylprednisolone (16mg),Tablet,Pfizer Ltd,Steroid,2025-02,2027-02,OT Store,80,strip,2025-05-20,Malabar Pharma Distributors
B02147,MLT249165,Rovas 5mg Tablet,Rosuvastatin (5mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-07,2026-01,Emergency Store,300,strip,2024-07-26,Kerala Medical Supplies Co.
B02148,ALX247607,Tobraject 0.3% Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alkem Laboratories Ltd,Ophthalmology,2025-04,2027-04,ICU Store,10,bottle,2025-06-20,"Medline Distributors, Thiruvananthapuram"
B02149,TPT240241,Amitor 10mg Tablet,Amitriptyline (10mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-04,2026-04,OPD Pharmacy,10,strip,2024-06-21,"Medline Distributors, Thiruvananthapuram"
B02150,DR24F861,Razo 20 Tablet,Rabeprazole (20mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-05,2027-05,Ward Store (Paeds),10,strip,2024-07-01,"Medline Distributors, Thiruvananthapuram"
B02151,CL25G817,Norflox 400 Tablet,Norfloxacin (400mg) + Lactobacillus (120Million spores),Tablet,Cipla Ltd,Other,2025-02,2027-02,ICU Store,50,strip,2025-04-09,Sanjivani Drug House
B02152,SPT258746,Rosuvas 10mg Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-08,2026-02,Emergency Store,50,strip,2024-11-15,Apollo Wholesale Pvt Ltd
B02153,X2405-186,Canditas Dusting Powder,Clotrimazole (75mg),Powder,Intas Pharmaceuticals Ltd,Antifungal,2024-12,2026-12,Emergency Store,0,pack,2025-01-07,Sanjivani Drug House
B02154,IPT243402,Allegix 120mg Tablet,Fexofenadine (120mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2025-05,2026-11,Emergency Store,60,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B02155,CL24H225,Add Tears Lubricant Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Cipla Ltd,Ophthalmology,2024-11,2026-11,ICU Store,60,bottle,2025-01-10,"Medline Distributors, Thiruvananthapuram"
B02156,CP24K807,Teli 20 Tablet,Telmisartan (20mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-02,2027-02,OPD Pharmacy,100,strip,2024-05-17,Sree Pharma Agencies
B02157,ML24E870,Forinem 500mg Injection,Meropenem (500mg),Injection,Micro Labs Ltd,Antibiotic,2024-09,2026-09,Ward Store (Paeds),40,vial/amp,2024-10-25,Apollo Wholesale Pvt Ltd
B02158,WBT249920,Drotin A Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Walter Bushnell,Gastro,2024-01,2027-01,Ward Store (Paeds),10,strip,2024-04-16,"Medline Distributors, Thiruvananthapuram"
B02159,62439278,Vysov 50mg Tablet,Vildagliptin (50mg),Tablet,Cipla Ltd,Diabetes,2025-03,2027-03,OT Store,0,strip,2025-06-08,Sanjivani Drug House
B02160,AI251280,Nuavomin 2mg Injection,Ondansetron (2mg),Injection,Abbott,Gastro,2024-02,2027-02,OT Store,10,vial/amp,2024-03-29,Sanjivani Drug House
B02161,68749531,Hycort 100mg Injection,Hydrocortisone (100mg),Injection,Alkem Laboratories Ltd,Steroid,2025-03,2026-09,OPD Pharmacy,100,vial/amp,2025-05-19,Apollo Wholesale Pvt Ltd
B02162,CL25D628,Esomac 40 Tablet,Esomeprazole (40mg),Tablet,Cipla Ltd,Gastro,2024-04,2025-10,ICU Store,0,strip,2024-06-25,Kerala Medical Supplies Co.
B02163,TP24C987,Amlocor 10mg Tablet,Amlodipine (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-04,2026-04,Ward Store (Paeds),50,strip,2024-06-05,Sree Pharma Agencies
B02164,LH25F846,Aziford 200 Oral Suspension,Azithromycin (200mg),Suspension,Leeford Healthcare Ltd,Antibiotic,2024-03,2026-03,Ward Store (Paeds),50,bottle,2024-04-25,Apollo Wholesale Pvt Ltd
B02165,SPI242445,Oframax 125mg Injection,Ceftriaxone (125mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-12,2027-12,Ward Store (Paeds),120,vial/amp,2025-03-02,Sanjivani Drug House
B02166,CLT254204,Linospan 100 DT Tablet,Linezolid (100mg),Tablet,Cipla Ltd,Antibiotic,2025-01,2028-01,Emergency Store,300,strip,2025-04-19,"Medline Distributors, Thiruvananthapuram"
B02167,T2504-380,Janumet 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2025-01,2028-01,Main Pharmacy,60,strip,2025-03-07,Sanjivani Drug House
B02168,TP24H019,Linox 200mg Infusion,Linezolid (200mg),Infusion,Torrent Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,ICU Store,0,bottle,2025-07-15,Apollo Wholesale Pvt Ltd
B02169,AL24H229,Almetfor 500mg Tablet,Metformin (500mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-04,2027-04,OPD Pharmacy,40,strip,2024-04-27,Apollo Wholesale Pvt Ltd
B02170,60418290,Levocet 10mg Tablet,Levocetirizine (10mg),Tablet,Hetero Healthcare Limited,Respiratory,2024-04,2027-04,Ward Store (Paeds),150,strip,2024-05-06,Sanjivani Drug House
B02171,IPT244783,Olimelt 10 Tablet MD,Olanzapine (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-09,2026-03,Main Pharmacy,150,strip,2024-10-28,"Medline Distributors, Thiruvananthapuram"
B02172,MP25A072,FT-Mac Cream,Fusidic Acid (2% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Dermatology,2024-07,2026-01,ICU Store,80,tube,2024-08-30,Sanjivani Drug House
B02173,LLT257579,Clopi 150mg Tablet,Clopidogrel (150mg),Tablet,Lupin Ltd,Cardiovascular,2024-10,2026-04,Emergency Store,300,strip,2024-12-07,Sanjivani Drug House
B02174,23417244,Calcirol XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cadila Pharmaceuticals Ltd,Supplement,2024-04,2026-04,Main Pharmacy,80,strip,2024-06-28,Apollo Wholesale Pvt Ltd
B02175,82091897,Bruriff 400mg Tablet,Ibuprofen (400mg),Tablet,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-12,2026-12,Main Pharmacy,200,strip,2024-12-26,Sree Pharma Agencies
B02176,T2507-617,Helirab 20 Tablet,Rabeprazole (20mg),Tablet,Micro Labs Ltd,Gastro,2024-08,2027-08,OT Store,80,strip,2024-09-16,Sanjivani Drug House
B02177,93935292,Omnacortil 10 Tablet DT,Prednisolone (10mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Steroid,2024-01,2026-01,ICU Store,150,strip,2024-04-13,Apollo Wholesale Pvt Ltd
B02178,45776413,Frusenex 100 Tablet,Furosemide (100mg),Tablet,Geno Pharmaceuticals Ltd,Cardiovascular,2024-12,2026-12,Main Pharmacy,20,strip,2025-03-22,Malabar Pharma Distributors
B02179,87520413,Glucreta 10mg Tablet,Dapagliflozin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-03,2027-03,OT Store,10,strip,2025-04-23,Sree Pharma Agencies
B02180,57684613,Apixator 2.5 Tablet,Apixaban (2.5mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2025-04,2028-04,OPD Pharmacy,200,strip,2025-07-05,Apollo Wholesale Pvt Ltd
B02181,GCT256025,Crocin Advance Tablet,Paracetamol (500mg),Tablet,GlaxoSmithKline Consumer Healthcare,Analgesic/Antipyretic,2025-01,2028-01,Ward Store (Paeds),30,strip,2025-04-09,"Medline Distributors, Thiruvananthapuram"
B02182,27466246,Otrilom-S Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Fawn Incorporation,IV Fluids,2025-04,2027-04,Main Pharmacy,60,bottle,2025-06-17,Malabar Pharma Distributors
B02183,T2506-369,Oleanz 10 Tablet,Olanzapine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-01,2028-01,ICU Store,100,strip,2025-04-07,Kerala Medical Supplies Co.
B02184,BII242379,Ringer Lactate R Injection,Ringer's lactate (NA),Injection,Baxter India Pvt Ltd,IV Fluids,2025-02,2026-08,Ward Store (Paeds),300,vial/amp,2025-05-21,Malabar Pharma Distributors
B02185,TP25B447,Cobasoft 500mcg Injection,Methylcobalamin (500mcg),Injection,Torrent Pharmaceuticals Ltd,Supplement,2024-08,2027-08,OPD Pharmacy,30,vial/amp,2024-08-27,Sree Pharma Agencies
B02186,SPT243385,Istavel 100mg Tablet,Sitagliptin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-08,2026-02,Ward Store (Paeds),120,strip,2024-09-11,Malabar Pharma Distributors
B02187,A24E856,Thyronorm 112mcg Tablet,Thyroxine (112mcg),Tablet,Abbott,Endocrine,2024-07,2026-01,Main Pharmacy,10,strip,2024-08-13,Sree Pharma Agencies
B02188,T2402-352,Alevo 250 Tablet,Levofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-03,2027-03,Emergency Store,80,strip,2024-05-09,Sanjivani Drug House
B02189,BC25G388,Meftal 250mg Tablet DT,Mefenamic Acid (250mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2025-02,2028-02,Main Pharmacy,80,strip,2025-03-21,Kerala Medical Supplies Co.
B02190,DRT246537,Ketorol SP Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-07,2026-07,OT Store,100,strip,2024-10-07,Sree Pharma Agencies
B02191,T2411-890,Emeset 4 Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-09,2026-09,Main Pharmacy,10,strip,2024-11-27,Sanjivani Drug House
B02192,IP25G452,Tromasol Infusion,Sodium Chloride (NA),Infusion,Intas Pharmaceuticals Ltd,IV Fluids,2025-02,2027-02,Main Pharmacy,50,bottle,2025-05-30,Malabar Pharma Distributors
B02193,ALT254140,Tamsukem 0.2mg Tablet,Tamsulosin (0.2mg),Tablet,Alkem Laboratories Ltd,Urology,2024-08,2026-08,OPD Pharmacy,120,strip,2024-09-03,Malabar Pharma Distributors
B02194,75539501,Ciprobid 200mg Infusion,Ciprofloxacin (200mg),Infusion,Zydus Cadila,Antibiotic,2024-10,2026-10,Main Pharmacy,80,bottle,2024-11-26,"Medline Distributors, Thiruvananthapuram"
B02195,CL24L141,Esomac 40 Tablet,Esomeprazole (40mg),Tablet,Cipla Ltd,Gastro,2025-04,2028-04,Main Pharmacy,150,strip,2025-07-10,Sanjivani Drug House
B02196,SPI242290,Cefuroxime Sodium 750mg Injection,Cefuroxime (750mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-10,2026-04,Ward Store (Paeds),60,vial/amp,2024-12-15,Kerala Medical Supplies Co.
B02197,CP25B028,Aciban 20 Tablet,Pantoprazole (20mg),Tablet,Cadila Pharmaceuticals Ltd,Gastro,2024-12,2026-12,OT Store,50,strip,2025-02-21,Sree Pharma Agencies
B02198,I2412-392,Susten 200 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-06,2027-06,Emergency Store,150,vial/amp,2024-08-31,Malabar Pharma Distributors
B02199,18155490,Allerfex 120mg Tablet,Fexofenadine (120mg),Tablet,Torrent Pharmaceuticals Ltd,Respiratory,2025-05,2027-05,Ward Store (Paeds),0,strip,2025-06-17,Kerala Medical Supplies Co.
B02200,CLT249774,Cofenac 100mg Tablet SR,Diclofenac (100mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-05,2026-05,ICU Store,20,strip,2024-05-31,Kerala Medical Supplies Co.
B02201,61214452,Tryptomer 25mg Tablet,Amitriptyline (25mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2025-03,2027-03,Ward Store (Paeds),10,strip,2025-03-27,Sree Pharma Agencies
B02202,63767131,Biodexone 4 Tablet,Dexamethasone (4mg),Tablet,Zydus Cadila,Steroid,2024-04,2026-04,Main Pharmacy,80,strip,2024-07-03,Kerala Medical Supplies Co.
B02203,MLI248330,BIOFER S 100mg/5ml Injection,Iron Sucrose (100mg/5ml),Injection,Micro Labs Ltd,Haematology,2024-12,2026-12,ICU Store,80,vial/amp,2025-02-05,Sanjivani Drug House
B02204,TP24H292,Rostar 10 Tablet,Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-09,2026-03,Emergency Store,300,strip,2024-11-18,Malabar Pharma Distributors
B02205,X2506-465,Fucidin Cream,Fusidic Acid (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-04,2026-04,Main Pharmacy,0,tube,2024-06-27,Apollo Wholesale Pvt Ltd
B02206,ZCT257131,Roxin 100mcg Tablet,Thyroxine (100mcg),Tablet,Zydus Cadila,Endocrine,2024-08,2026-02,Main Pharmacy,10,strip,2024-11-08,Sree Pharma Agencies
B02207,AT244973,R-Ppi 20mg Tablet,Rabeprazole (20mg),Tablet,Abbott,Gastro,2024-05,2025-11,ICU Store,10,strip,2024-05-30,Sree Pharma Agencies
B02208,A25M229,Thyronorm 125mcg Tablet,Thyroxine (125mcg),Tablet,Abbott,Endocrine,2025-05,2027-05,Ward Store (Paeds),50,strip,2025-06-18,Kerala Medical Supplies Co.
B02209,LLC259446,Pregadoc 75 Capsule,Pregabalin (75mg),Capsule,Lupin Ltd,Neurology/Psychiatry,2025-02,2028-02,Emergency Store,80,strip,2025-04-18,"Medline Distributors, Thiruvananthapuram"
B02210,AL24F959,Ondem 8mg Injection,Ondansetron (2mg/ml),Injection,Alkem Laboratories Ltd,Gastro,2025-05,2027-05,Emergency Store,30,vial/amp,2025-07-06,Sree Pharma Agencies
B02211,T2412-431,Ursetor 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-05,2027-05,Emergency Store,150,strip,2025-06-27,Apollo Wholesale Pvt Ltd
B02212,MT-25D59,Calcium and Vitamin D3 Tablets IP,Calcium (500mg) + Vitamin D3 (250IU),Tablet,Martin & Brown Bio-Sciences Pvt. Ltd.,Supplement,2025-04,2027-03,Ward Store (Paeds),80,strip,2025-07-13,Apollo Wholesale Pvt Ltd
B02213,T2405-092,Etozox 120mg Tablet,Etoricoxib (120mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2025-01,2027-01,Main Pharmacy,200,strip,2025-03-17,Sree Pharma Agencies
B02214,87499715,Itocin 5IU Injection,Oxytocin (5IU),Injection,Lupin Ltd,Obstetrics,2024-08,2027-08,OPD Pharmacy,0,vial/amp,2024-11-12,Sanjivani Drug House
B02215,77868292,Pixaflo 2.5mg Tablet,Apixaban (2.5mg),Tablet,Lupin Ltd,Anticoagulant,2024-08,2027-08,Main Pharmacy,150,strip,2024-10-08,Malabar Pharma Distributors
B02216,CPT244232,Cavit-XT Tablet,Calcium Carbonate (500mg) + Vitamin D3 (2000IU),Tablet,Cachet Pharmaceuticals Pvt Ltd,Supplement,2024-01,2026-01,Main Pharmacy,60,strip,2024-03-01,Apollo Wholesale Pvt Ltd
B02217,TPI253269,Nausinorm 5mg Injection,Metoclopramide (5mg),Injection,Torrent Pharmaceuticals Ltd,Gastro,2024-01,2027-02,OPD Pharmacy,100,vial/amp,2024-03-05,"Medline Distributors, Thiruvananthapuram"
B02218,TP24A783,Herpex 100mg Tablet,Acyclovir (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antiviral,2024-12,2027-12,OPD Pharmacy,20,strip,2025-02-16,Apollo Wholesale Pvt Ltd
B02219,WC24C941,DMR 10mg Tablet,Dextromethorphan Hydrobromide (10mg),Tablet,West-Coast Pharmaceutical Works Ltd,Respiratory,2024-03,2027-03,Emergency Store,120,strip,2024-04-19,Malabar Pharma Distributors
B02220,MPX240415,Aerozest 0.31mg Respules (2.5 ml each),Levosalbutamol (0.31mg),Respules,Macleods Pharmaceuticals Pvt Ltd,Respiratory,2025-05,2028-05,Emergency Store,20,respule,2025-07-15,Sanjivani Drug House
B02221,56885958,Trapic 100mg Injection,Tranexamic Acid (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2024-11,2027-11,Ward Store (Paeds),80,vial/amp,2024-12-19,Sanjivani Drug House
B02222,CLT242645,Metolar 25 Tablet,Metoprolol Tartrate (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2025-11,OT Store,50,strip,2024-08-02,Sanjivani Drug House
B02223,TPT249131,VASOTRATE 10MG TABLET,Isosorbide Mononitrate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-08,2027-08,Emergency Store,0,strip,2024-10-23,Sree Pharma Agencies
B02224,AL25E608,Almefkem 250 DT Tablet,Mefenamic Acid (250mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-06,2027-06,OT Store,150,strip,2024-08-28,Apollo Wholesale Pvt Ltd
B02225,CP24M622,Isoniazid 300mg Tablet,Isoniazid (300mg),Tablet,Cadila Pharmaceuticals Ltd,Anti-TB,2025-02,2027-02,Ward Store (Paeds),60,strip,2025-04-29,Sree Pharma Agencies
B02226,X2410-363,Naresol 0.65% Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Alembic Pharmaceuticals Ltd,IV Fluids,2024-05,2027-05,Ward Store (Paeds),80,bottle,2024-06-19,Apollo Wholesale Pvt Ltd
B02227,T2510-391,Ondem 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-08,2026-08,Main Pharmacy,50,strip,2024-11-15,Malabar Pharma Distributors
B02228,96836098,Lezyncet 2.5mg/5ml Syrup,Levocetirizine (2.5mg/5ml),Syrup,Torrent Pharmaceuticals Ltd,Respiratory,2024-12,2027-12,ICU Store,60,bottle,2025-03-17,"Medline Distributors, Thiruvananthapuram"
B02229,T2505-909,Oleanz 2.5 Tablet,Olanzapine (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2026-07,ICU Store,300,strip,2024-09-20,Malabar Pharma Distributors
B02230,E25B026,Paracetamol IV Infusion 1%,Paracetamol (10mg/ml),Infusion,D.J. Laboratories Pvt. Ltd.,Analgesic/Antipyretic,2025-02,2028-01,OPD Pharmacy,120,bottle,2025-05-08,Kerala Medical Supplies Co.
B02231,TP25M613,Oncoden 4mg Tablet,Ondansetron (4mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-05,2028-05,Ward Store (Paeds),100,strip,2025-07-15,Sanjivani Drug House
B02232,TPT255633,Deplatt A 75 Tablet,Aspirin (75mg) + Clopidogrel (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-08,2026-08,OPD Pharmacy,120,strip,2024-11-04,Sanjivani Drug House
B02233,76122740,Ursetor 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-11,2027-11,Main Pharmacy,30,strip,2025-02-04,Apollo Wholesale Pvt Ltd
B02234,SII256629,Apidra 100IU/ml Solution for Injection,Insulin Glulisine (100IU),Injection,Sanofi India Ltd,Diabetes,2024-11,2027-11,ICU Store,40,vial/amp,2024-11-26,"Medline Distributors, Thiruvananthapuram"
B02235,50001891,Cizetol 200mg Tablet,Carbamazepine (200mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-07,2027-07,Emergency Store,20,strip,2024-09-09,Sanjivani Drug House
B02236,ILI248570,Folitrax 15 Injection,Methotrexate (15mg/ml),Injection,Ipca Laboratories Ltd,Oncology,2025-03,2028-03,Ward Store (Paeds),80,vial/amp,2025-04-13,Apollo Wholesale Pvt Ltd
B02237,T2412-742,Jardiance 25mg Tablet,Empagliflozin (25mg),Tablet,Boehringer Ingelheim,Other,2024-06,2027-06,Ward Store (Paeds),100,strip,2024-07-06,Kerala Medical Supplies Co.
B02238,TPI256200,Fegold 100mg Injection,Iron Sucrose (100mg),Injection,Torrent Pharmaceuticals Ltd,Haematology,2025-05,2028-05,Emergency Store,30,vial/amp,2025-07-15,Apollo Wholesale Pvt Ltd
B02239,15226275,Spasidex Drop,Dicyclomine (NA),Drops,Wockhardt Ltd,Gastro,2024-05,2027-05,ICU Store,0,bottle,2024-06-08,Malabar Pharma Distributors
B02240,IL24H938,Perinorm Syrup,Metoclopramide (5mg),Syrup,Ipca Laboratories Ltd,Gastro,2024-12,2026-12,OPD Pharmacy,0,bottle,2025-03-15,Malabar Pharma Distributors
B02241,X2504-479,Lupigenta Eye/Ear Drops,Gentamicin (NA),Ear Drops,Lupin Ltd,Antibiotic,2025-02,2028-02,Main Pharmacy,0,bottle,2025-03-31,Sanjivani Drug House
B02242,T2502-905,Diapride M 0.5mg/500mg Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Micro Labs Ltd,Diabetes,2025-04,2027-04,OT Store,0,strip,2025-04-30,Sanjivani Drug House
B02243,45760499,Cyclopam Drops,Dicyclomine (10mg) + Simethicone (40mg),Drops,Indoco Remedies Ltd,Gastro,2025-03,2026-09,ICU Store,200,bottle,2025-04-14,Apollo Wholesale Pvt Ltd
B02244,IR24J597,Labetag 100mg Tablet,Labetalol (100mg),Tablet,Ikon Remedies Pvt Ltd,Cardiovascular,2025-05,2028-05,Emergency Store,40,strip,2025-06-23,Apollo Wholesale Pvt Ltd
B02245,IP25G683,Zorem 1.25 Capsule,Ramipril (1.25mg),Capsule,Intas Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,ICU Store,30,strip,2024-08-20,Kerala Medical Supplies Co.
B02246,SP25L703,Oleanz 7.5 Tablet,Olanzapine (7.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-12,2026-12,ICU Store,120,strip,2025-01-27,Apollo Wholesale Pvt Ltd
B02247,X2402-430,Aerozest 0.31mg Respules (2.5 ml each),Levosalbutamol (0.31mg),Respules,Macleods Pharmaceuticals Pvt Ltd,Respiratory,2024-11,2027-11,OT Store,0,respule,2025-02-03,Sanjivani Drug House
B02248,BCT248326,Meftal 500 Tablet,Mefenamic Acid (500mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2024-08,2026-08,Emergency Store,100,strip,2024-11-07,Malabar Pharma Distributors
B02249,T2405-370,Vida 25mg Tablet,Losartan (25mg),Tablet,Lupin Ltd,Cardiovascular,2024-10,2026-10,Emergency Store,30,strip,2024-11-11,Sanjivani Drug House
B02250,SI24G712,Allegra 120mg Tablet,Fexofenadine (120mg),Tablet,Sanofi India Ltd,Respiratory,2024-11,2026-05,ICU Store,200,strip,2025-01-29,Malabar Pharma Distributors
B02251,TP25F560,Ldtor 10mg Tablet,Atorvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-03,2026-03,OT Store,120,strip,2024-03-29,Kerala Medical Supplies Co.
B02252,ZC25K084,Rosupil 10mg Tablet,Rosuvastatin (10mg),Tablet,Zydus Cadila,Cardiovascular,2025-01,2028-01,ICU Store,0,strip,2025-03-13,Sanjivani Drug House
B02253,TPT253108,Clodrel Tablet,Clopidogrel (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-07,OT Store,10,strip,2024-08-31,Sanjivani Drug House
B02254,38197129,Clear 250mg Tablet,Clarithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-06,2026-06,ICU Store,10,strip,2024-07-29,Malabar Pharma Distributors
B02255,ZCT245417,Depotex 16mg Tablet,Methylprednisolone (16mg),Tablet,Zydus Cadila,Steroid,2024-02,2026-02,ICU Store,10,strip,2024-03-08,Sree Pharma Agencies
B02256,CLV255871,Metrocip 500mg Infusion,Metronidazole (500mg),Infusion,Cipla Ltd,Antibiotic,2024-01,2027-01,Main Pharmacy,0,bottle,2024-04-19,Kerala Medical Supplies Co.
B02257,FL24K562,Ricetral 0.3gm Injection,Potassium Chloride (0.3gm),Injection,FDC Ltd,Anaesthesia/Critical care,2025-02,2027-02,Main Pharmacy,200,vial/amp,2025-05-16,Sree Pharma Agencies
B02258,87383120,Starcad-Beta 12.5 Tablet ER,Metoprolol Succinate (11.8mg),Tablet,Lupin Ltd,Cardiovascular,2024-01,2027-01,Main Pharmacy,80,strip,2024-03-19,Sree Pharma Agencies
B02259,CLT253077,Montair LC Kid Tablet DT,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Cipla Ltd,Respiratory,2024-11,2027-11,OT Store,40,strip,2024-12-02,Kerala Medical Supplies Co.
B02260,T2402-471,Flolev 750mg Tablet,Levofloxacin (750mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-03,2025-09,Main Pharmacy,10,strip,2024-06-10,Sree Pharma Agencies
B02261,29347898,Metakind 1000mg Tablet SR,Metformin (1000mg),Tablet,Mankind Pharma Ltd,Diabetes,2024-06,2025-12,Main Pharmacy,40,strip,2024-07-19,Kerala Medical Supplies Co.
B02262,30761643,Decamycin 4mg Injection,Dexamethasone (4mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2025-02,2028-02,Emergency Store,150,vial/amp,2025-05-09,Sanjivani Drug House
B02263,T2505-108,Nitrogard 2.6mg Tablet,Nitroglycerin (2.6mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2027-05,OT Store,0,strip,2024-06-25,Malabar Pharma Distributors
B02264,ML25K199,Rovas 5mg Tablet,Rosuvastatin (5mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-11,2026-11,Emergency Store,10,strip,2024-12-05,Malabar Pharma Distributors
B02265,TP24M226,Tufzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2025-02,2028-02,Main Pharmacy,120,vial/amp,2025-04-18,Sree Pharma Agencies
B02266,X2512-839,Entofoam NF Cream,Hydrocortisone (10% w/w),Cream,Cipla Ltd,Steroid,2025-04,2028-04,Emergency Store,10,tube,2025-05-19,Sree Pharma Agencies
B02267,34393379,Ignalis-M 100/1000 Tablet ER,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-06,2025-12,ICU Store,20,strip,2024-07-07,Kerala Medical Supplies Co.
B02268,95852907,Labepure 20mg Injection,Labetalol (20mg),Injection,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-05,2025-11,OT Store,120,vial/amp,2024-07-01,Apollo Wholesale Pvt Ltd
B02269,39604115,Azax 200 Suspension,Azithromycin (200mg/5ml),Suspension,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-01,2026-01,Ward Store (Paeds),300,bottle,2024-02-07,Sree Pharma Agencies
B02270,I2508-131,Frusemide Injection IP 2 ml,Furosemide (10mg/ml),Injection,Regain Laboratories,Cardiovascular,2025-05,2027-05,OPD Pharmacy,150,vial/amp,2025-06-20,"Medline Distributors, Thiruvananthapuram"
B02271,EP24G778,Panpure 20mg Infusion,Pantoprazole (20mg),Infusion,Emcure Pharmaceuticals Ltd,Gastro,2025-01,2027-01,ICU Store,120,bottle,2025-02-13,"Medline Distributors, Thiruvananthapuram"
B02272,ZCT245019,Activa Plus Tablet,Diclofenac (NA),Tablet,Zydus Cadila,Analgesic/Antipyretic,2024-06,2027-06,ICU Store,60,strip,2024-08-20,"Medline Distributors, Thiruvananthapuram"
B02273,AL25G400,Chinsunate 60mg Injection,Artesunate (60mg),Injection,Alkem Laboratories Ltd,Antimalarial,2024-02,2027-02,OPD Pharmacy,80,vial/amp,2024-05-25,Kerala Medical Supplies Co.
B02274,95133372,Alciflox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-04,2028-04,Emergency Store,150,strip,2025-06-22,"Medline Distributors, Thiruvananthapuram"
B02275,IL24B833,Perinorm Syrup,Metoclopramide (5mg),Syrup,Ipca Laboratories Ltd,Gastro,2024-02,2027-02,ICU Store,60,bottle,2024-03-22,Malabar Pharma Distributors
B02276,T2512-810,Metocard XL 100 Tablet,Metoprolol Succinate (95mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-03,Emergency Store,0,strip,2024-04-27,Sree Pharma Agencies
B02277,T2510-049,Levomac 250 Tablet,Levofloxacin (250mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2025-02,2028-02,Ward Store (Paeds),40,strip,2025-04-17,Apollo Wholesale Pvt Ltd
B02278,ML25M713,Amlong 10 Tablet,Amlodipine (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-03,2028-03,OPD Pharmacy,80,strip,2025-06-11,Apollo Wholesale Pvt Ltd
B02279,T2507-456,Oncotrex 2.5mg Tablet,Methotrexate (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Oncology,2024-10,2026-10,Ward Store (Paeds),150,strip,2025-01-28,Sree Pharma Agencies
B02280,LLT258781,Telista AM 40mg/2.5mg Tablet,Telmisartan (40mg) + Amlodipine (2.5mg),Tablet,Lupin Ltd,Cardiovascular,2024-09,2026-09,Main Pharmacy,50,strip,2024-11-26,Sanjivani Drug House
B02281,88393811,Montair LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Cipla Ltd,Respiratory,2025-03,2027-03,Emergency Store,0,bottle,2025-06-23,Apollo Wholesale Pvt Ltd
B02282,ZCT254674,Inditel 20 Tablet,Telmisartan (20mg),Tablet,Zydus Cadila,Cardiovascular,2024-08,2027-08,Emergency Store,40,strip,2024-10-05,Sree Pharma Agencies
B02283,CL24C800,Glygard 40mg Tablet,Gliclazide (40mg),Tablet,Cipla Ltd,Diabetes,2024-10,2026-10,ICU Store,50,strip,2024-11-04,Sree Pharma Agencies
B02284,MLT254253,Florobid 200mg Tablet,Ofloxacin (200mg),Tablet,Micro Labs Ltd,Antibiotic,2024-05,2027-05,Main Pharmacy,80,strip,2024-07-11,Kerala Medical Supplies Co.
B02285,GST246974,Eltroxin 25mcg Tablet,Thyroxine (25mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2024-03,2026-03,Ward Store (Paeds),40,strip,2024-05-04,Apollo Wholesale Pvt Ltd
B02286,CBT249436,Cgglu 500 Tablet,Calcium Gluconate (500mg),Tablet,Cmg Biotech Pvt Ltd,Anaesthesia/Critical care,2024-03,2027-03,OPD Pharmacy,30,strip,2024-05-09,Sanjivani Drug House
B02287,T-2672,Sitajack-M Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Jackson Laboratories Pvt. Ltd.,Diabetes,2024-09,2026-08,Main Pharmacy,20,strip,2024-12-12,Malabar Pharma Distributors
B02288,IPT240622,Lopez 1mg Tablet,Lorazepam (1mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2026-05,OT Store,10,strip,2024-06-30,Malabar Pharma Distributors
B02289,55984239,Sartel H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-04,2028-04,OT Store,30,strip,2025-06-03,Malabar Pharma Distributors
B02290,ALT240581,Tamica-AM 40 Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-01,2026-01,ICU Store,10,strip,2024-04-10,Apollo Wholesale Pvt Ltd
B02291,72269929,Ciptab 250mg Tablet,Ciprofloxacin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2024-04,2027-04,Ward Store (Paeds),150,strip,2024-06-17,Malabar Pharma Distributors
B02292,ALI257291,Merosure 125mg Injection,Meropenem (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2025-03,2026-09,ICU Store,20,vial/amp,2025-04-23,Kerala Medical Supplies Co.
B02293,30560218,Cetzine Cold Tablet,Caffeine (30mg) + Diphenhydramine (25mg),Tablet,Dr Reddy's Laboratories Ltd,Other,2024-09,2026-09,Emergency Store,200,strip,2024-11-23,Kerala Medical Supplies Co.
B02294,IPT244308,Intaglip OD 100mg Tablet,Vildagliptin (100mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-02,2027-02,OPD Pharmacy,40,strip,2024-05-21,Sree Pharma Agencies
B02295,29120157,Tamica-H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-01,2027-01,Emergency Store,120,strip,2025-04-24,Apollo Wholesale Pvt Ltd
B02296,SP25E653,Ibubid 300mg Capsule TR,Ibuprofen (300mg),Capsule,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-10,2026-10,Ward Store (Paeds),80,strip,2025-01-21,"Medline Distributors, Thiruvananthapuram"
B02297,26301180,Voveran 150mg Tablet SR,Diclofenac (150mg),Tablet,Novartis India Ltd,Analgesic/Antipyretic,2024-08,2026-02,OPD Pharmacy,0,strip,2024-08-27,Sree Pharma Agencies
B02298,51464269,Ondem -MD 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-12,2026-06,Emergency Store,0,strip,2025-02-20,Kerala Medical Supplies Co.
B02299,MPI248358,Tranomac 500mg Injection,Tranexamic Acid (500mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Haematology,2024-07,2027-07,OT Store,10,vial/amp,2024-09-02,Apollo Wholesale Pvt Ltd
B02300,CL25M208,Actiflu 500mg Tablet,Paracetamol (500mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2025-03,2028-03,ICU Store,50,strip,2025-06-14,Sree Pharma Agencies
B02301,67953319,Udiliv 450mg Tablet,Ursodeoxycholic Acid (450mg),Tablet,Abbott,Gastro,2025-03,2026-09,ICU Store,150,strip,2025-06-12,Kerala Medical Supplies Co.
B02302,I2402-347,Alkem Ketorolac 100mg Injection,Ketorolac (100mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-08,2026-08,OPD Pharmacy,60,vial/amp,2024-10-05,Apollo Wholesale Pvt Ltd
B02303,X2505-276,Welbusol 50mcg Inhaler,Levosalbutamol (50mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-07,2026-07,Emergency Store,50,inhaler,2024-08-22,Apollo Wholesale Pvt Ltd
B02304,X2408-743,Derihaler 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Zydus Cadila,Respiratory,2024-01,2026-01,OT Store,10,inhaler,2024-04-03,Apollo Wholesale Pvt Ltd
B02305,13550019,Humanext N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Cadila Pharmaceuticals Ltd,Diabetes,2025-02,2028-02,Emergency Store,120,vial/amp,2025-02-26,Sree Pharma Agencies
B02306,31901903,Sitaxa 100 Tablet,Sitagliptin (100mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-02,2028-02,Main Pharmacy,300,strip,2025-04-07,Malabar Pharma Distributors
B02307,APS254842,Magadol Oral Suspension,Paracetamol (250mg/5ml),Suspension,Alembic Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-12,2026-12,Main Pharmacy,80,bottle,2025-03-06,Kerala Medical Supplies Co.
B02308,39566552,Gabata 400mg Capsule,Gabapentin (400mg),Capsule,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-08,2027-08,Main Pharmacy,10,strip,2024-09-04,Kerala Medical Supplies Co.
B02309,T2502-579,Mefomin 1000 SR Tablet,Metformin (1000mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Diabetes,2024-01,2027-02,ICU Store,20,strip,2024-02-22,Kerala Medical Supplies Co.
B02310,SP24J171,Gemer 0.5 Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-03,2026-03,Emergency Store,30,strip,2024-04-10,Sanjivani Drug House
B02311,T2405-191,Aldotone 50mg Tablet,Spironolactone (50mg),Tablet,Samarth Life Sciences Pvt Ltd,Cardiovascular,2024-08,2026-08,Ward Store (Paeds),80,strip,2024-10-05,Sree Pharma Agencies
B02312,ALX251754,Optibex Tear Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Alkem Laboratories Ltd,Ophthalmology,2025-02,2028-02,ICU Store,60,bottle,2025-03-08,Kerala Medical Supplies Co.
B02313,AL24M495,Olymprix Tablet,Teneligliptin (20mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-04,2027-04,OT Store,120,strip,2025-06-29,Apollo Wholesale Pvt Ltd
B02314,V2402-671,Hospilid 200mg Infusion,Linezolid (200mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-03,2027-03,Ward Store (Paeds),20,bottle,2024-03-30,Sanjivani Drug House
B02315,72265475,Bioprim Syrup,Sulfamethoxazole (200mg) + Trimethoprim (40mg),Syrup,Zydus Cadila,Antibiotic,2024-04,2026-04,OPD Pharmacy,80,bottle,2024-06-01,Sree Pharma Agencies
B02316,ZC25D284,Depotex 4mg Tablet,Methylprednisolone (4mg),Tablet,Zydus Cadila,Steroid,2024-05,2027-05,Main Pharmacy,200,strip,2024-06-17,Malabar Pharma Distributors
B02317,44699521,Cardipin 20mg Tablet,Nifedipine (20mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-10,2026-04,OPD Pharmacy,80,strip,2024-12-15,Sanjivani Drug House
B02318,86134053,Acifac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2026-09,Ward Store (Paeds),0,strip,2025-04-10,Sanjivani Drug House
B02319,ZCC250469,Cadoxy 100mg Capsule,Doxycycline (100mg),Capsule,Zydus Cadila,Antibiotic,2024-02,2027-02,ICU Store,40,strip,2024-03-25,Apollo Wholesale Pvt Ltd
B02320,IPT244349,Intalol 50mg Tablet,Atenolol (50mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-05,2027-05,OPD Pharmacy,200,strip,2025-06-04,"Medline Distributors, Thiruvananthapuram"
B02321,SPT254386,Rosuvas 20 Tablet,Rosuvastatin (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-03,2027-03,Main Pharmacy,60,strip,2025-04-28,Sanjivani Drug House
B02322,IPS257068,Cefinta 50mg Dry Syrup,Cefixime (50mg),Syrup,Intas Pharmaceuticals Ltd,Antibiotic,2024-07,2027-07,Emergency Store,20,bottle,2024-10-22,Sree Pharma Agencies
B02323,ZC25L747,Angionox 40mg Injection,Enoxaparin (40mg),Injection,Zydus Cadila,Anticoagulant,2024-04,2026-04,OT Store,150,vial/amp,2024-05-15,Sree Pharma Agencies
B02324,X2502-607,Fucidin Ointment,Sodium Fusidate (2% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Other,2024-03,2025-09,ICU Store,80,tube,2024-06-10,Sanjivani Drug House
B02325,T2410-290,Lyricare-GM Tablet,Gabapentin (300mg) + Methylcobalamin (500mcg),Tablet,Urvija Pharmaceuticals,Neurology/Psychiatry,2025-04,2028-04,Ward Store (Paeds),60,strip,2025-06-06,Kerala Medical Supplies Co.
B02326,ALT248698,Olymprix Tablet,Teneligliptin (20mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-09,2026-09,OPD Pharmacy,300,strip,2024-12-12,Apollo Wholesale Pvt Ltd
B02327,APS250356,Levocet LM Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Aarcin Pharmaceutical LLP,Respiratory,2024-12,2026-06,Main Pharmacy,30,bottle,2025-01-25,"Medline Distributors, Thiruvananthapuram"
B02328,T2402-688,Linid OD Tablet,Linezolid (1200mg),Tablet,Zydus Cadila,Antibiotic,2024-03,2026-03,ICU Store,60,strip,2024-06-15,Sanjivani Drug House
B02329,79704534,Teleact D 80 Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2027-03,Main Pharmacy,10,strip,2024-06-22,Malabar Pharma Distributors
B02330,IP25J361,Diclofam 100mg Tablet SR,Diclofenac (100mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2027-05,Main Pharmacy,100,strip,2024-08-03,"Medline Distributors, Thiruvananthapuram"
B02331,AL25E024,Dolocare 500mg Tablet,Paracetamol (500mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-04,2028-04,Ward Store (Paeds),60,strip,2025-07-15,Sree Pharma Agencies
B02332,04BF0660,Dextrose Injection IP 5%,Dextrose (5% w/v),Infusion,Paschim Banga Pharmaceuticals,IV Fluids,2023-09,2026-08,OT Store,300,bottle,2023-12-25,"Medline Distributors, Thiruvananthapuram"
B02333,T2401-930,Klotfree Tablet,Clopidogrel (75mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2025-08,Main Pharmacy,10,strip,2024-04-22,Kerala Medical Supplies Co.
B02334,CLT255761,Dytor 100 Tablet,Torasemide (100mg),Tablet,Cipla Ltd,Cardiovascular,2025-05,2028-05,Ward Store (Paeds),40,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B02335,65609016,Dexodil 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psychotropics India Ltd,Anti-allergic,2024-07,2026-07,Emergency Store,100,strip,2024-10-13,"Medline Distributors, Thiruvananthapuram"
B02336,LLX243479,Salbair Resp 5mg Solution,Salbutamol (5mg),Solution,Lupin Ltd,Respiratory,2024-07,2027-07,Emergency Store,200,bottle,2024-10-25,Sanjivani Drug House
B02337,SPI245758,Dexelex 100mg Injection,Hydrocortisone (100mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2024-08,2027-08,Emergency Store,150,vial/amp,2024-11-29,Kerala Medical Supplies Co.
B02338,PL24C446,Ativan 2mg Tablet,Lorazepam (2mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2024-12,2026-12,ICU Store,120,strip,2025-03-19,Kerala Medical Supplies Co.
B02339,24723458,Duphalac Fiber Oral Solution,Lactulose (2.5gm/5ml),Oral Solution,Abbott,Gastro,2024-01,2027-01,OPD Pharmacy,0,bottle,2024-03-02,Apollo Wholesale Pvt Ltd
B02340,TPT255710,Oncoden 4mg Tablet,Ondansetron (4mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-08,2026-08,Emergency Store,100,strip,2024-11-02,Malabar Pharma Distributors
B02341,T2508-181,Doliza 500mg Tablet,Paracetamol (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-04,2025-10,Main Pharmacy,150,strip,2024-05-16,"Medline Distributors, Thiruvananthapuram"
B02342,DRT255002,Stamlo 2.5 Tablet,Amlodipine (2.5mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2025-02,2026-08,OPD Pharmacy,60,strip,2025-03-15,Malabar Pharma Distributors
B02343,MP24F075,Accuzon 125mg Injection,Ceftriaxone (125mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-03,2026-03,Emergency Store,300,vial/amp,2024-06-25,Sree Pharma Agencies
B02344,LHT256232,Ceficlav 100mg Tablet DT,Cefixime (100mg),Tablet,Leeford Healthcare Ltd,Antibiotic,2024-03,2026-03,OT Store,50,strip,2024-05-03,Sree Pharma Agencies
B02345,94772931,Torolac 10mg Tablet DT,Ketorolac (10mg),Tablet,Micro Labs Ltd,Analgesic/Antipyretic,2024-11,2026-11,Ward Store (Paeds),300,strip,2025-02-25,Sanjivani Drug House
B02346,11772524,Sitaxa M 50/1000 Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-02,2025-08,OT Store,40,strip,2024-03-23,"Medline Distributors, Thiruvananthapuram"
B02347,CL24J920,Metolar 100 Tablet,Metoprolol Tartrate (100mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2027-01,ICU Store,50,strip,2025-01-27,Sree Pharma Agencies
B02348,35415894,Aceflex Plus 100 mg/500 mg Tablet,Aceclofenac (100mg) + Paracetamol (500mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-10,2026-10,OT Store,20,strip,2024-12-18,Sree Pharma Agencies
B02349,T2501-703,Dombax 10mg Tablet,Domperidone (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-04,2028-04,Ward Store (Paeds),30,strip,2025-07-07,Malabar Pharma Distributors
B02350,29597211,Ringer Lactate R Injection,Ringer's lactate (NA),Injection,Baxter India Pvt Ltd,IV Fluids,2025-03,2028-03,OPD Pharmacy,100,vial/amp,2025-03-29,Malabar Pharma Distributors
B02351,MP25C643,Finamac 1000mg Infusion,Paracetamol (1000mg),Infusion,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2025-01,2027-01,Emergency Store,200,bottle,2025-02-15,Kerala Medical Supplies Co.
B02352,17988778,Ascad 150mg Tablet,Aspirin (150mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-03,2027-03,OT Store,20,strip,2024-03-27,Malabar Pharma Distributors
B02353,80575394,Olmecip 20 Tablet,Olmesartan Medoxomil (20mg),Tablet,Cipla Ltd,Cardiovascular,2025-05,2027-05,OPD Pharmacy,300,strip,2025-06-22,Malabar Pharma Distributors
B02354,CLT252160,Atorlip 10 Tablet,Atorvastatin (10mg),Tablet,Cipla Ltd,Cardiovascular,2025-04,2028-04,Emergency Store,100,strip,2025-05-08,Kerala Medical Supplies Co.
B02355,TP25C142,Nexpro 40 Tablet,Esomeprazole (40mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-01,2026-07,Ward Store (Paeds),100,strip,2025-03-15,Sree Pharma Agencies
B02356,48728311,DEPOPRED 40 MG INJECTION,Methylprednisolone (40mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2025-02,2027-02,Emergency Store,40,vial/amp,2025-05-24,Apollo Wholesale Pvt Ltd
B02357,ML25B498,Osmogel Eye Drop,Sodium Chloride (5% w/v),Eye Drops,Micro Labs Ltd,IV Fluids,2024-04,2026-04,Main Pharmacy,200,bottle,2024-07-26,Apollo Wholesale Pvt Ltd
B02358,MLT243207,Bactoclav - DT Tablet,Amoxycillin (200mg) + Clavulanic Acid (28.5mg),Tablet,Micro Labs Ltd,Antibiotic,2025-02,2026-08,OT Store,100,strip,2025-03-22,Malabar Pharma Distributors
B02359,S2510-710,Almox CV Syrup,Amoxycillin (200mg/5ml) + Clavulanic Acid (28.5mg/5ml),Syrup,Alkem Laboratories Ltd,Antibiotic,2024-06,2026-06,Emergency Store,120,bottle,2024-08-07,Kerala Medical Supplies Co.
B02360,MP25J268,FT-Mac Cream,Fusidic Acid (2% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Dermatology,2024-07,2027-07,OT Store,10,tube,2024-09-30,"Medline Distributors, Thiruvananthapuram"
B02361,LP24F239,Metrogyl 200 Tablet,Metronidazole (200mg),Tablet,Lekar Pharma Ltd,Antibiotic,2024-05,2026-05,Main Pharmacy,50,strip,2024-05-29,Malabar Pharma Distributors
B02362,SPX241217,Don Gel,Diclofenac (NA),Gel,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-09,2026-09,Main Pharmacy,150,tube,2024-11-28,Sree Pharma Agencies
B02363,DR24F443,Mucolite Drops,Ambroxol (7.5mg),Drops,Dr Reddy's Laboratories Ltd,Respiratory,2025-04,2026-10,Emergency Store,50,bottle,2025-05-02,Apollo Wholesale Pvt Ltd
B02364,MPT248919,Solonex DT Tablet,Isoniazid (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2025-02,2027-02,Main Pharmacy,20,strip,2025-05-11,Sanjivani Drug House
B02365,T2410-105,Rosuvas 10mg Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-04,2026-04,ICU Store,20,strip,2024-07-03,Kerala Medical Supplies Co.
B02366,68246664,Dytor 10 Tablet,Torasemide (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-04,2026-04,Ward Store (Paeds),300,strip,2024-05-08,Malabar Pharma Distributors
B02367,MPT246441,Atorvakind 20mg Tablet,Atorvastatin (20mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-11,2027-11,ICU Store,0,strip,2024-12-27,Kerala Medical Supplies Co.
B02368,NHV242722,Nirlife RL Infusion,Ringer's lactate (NA),Infusion,Nirlife Healthcare,IV Fluids,2025-02,2026-08,OPD Pharmacy,40,bottle,2025-05-22,Malabar Pharma Distributors
B02369,90161060,Levoflox 500 Infusion,Levofloxacin (500mg),Infusion,Cipla Ltd,Antibiotic,2024-11,2026-11,OPD Pharmacy,20,bottle,2025-01-13,Sree Pharma Agencies
B02370,TP24F818,Ldtor 10mg Tablet,Atorvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-03,2027-03,OPD Pharmacy,40,strip,2024-05-20,"Medline Distributors, Thiruvananthapuram"
B02371,IP25F800,Pregabid 75 Capsule,Pregabalin (75mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-02,2028-02,OT Store,60,strip,2025-04-18,Apollo Wholesale Pvt Ltd
B02372,IPT241443,Golbi 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-01,2027-01,OPD Pharmacy,20,strip,2025-03-09,Malabar Pharma Distributors
B02373,SI24B490,Lasix Tablet,Furosemide (40mg),Tablet,Sanofi India Ltd,Cardiovascular,2024-12,2026-12,Emergency Store,50,strip,2025-01-28,Malabar Pharma Distributors
B02374,C2508-588,Olsivir Capsule,Oseltamivir Phosphate (75mg),Capsule,Glenmark Pharmaceuticals Ltd,Antiviral,2025-03,2027-03,OT Store,0,strip,2025-05-31,Malabar Pharma Distributors
B02375,95205708,Espra 20mg Tablet,Esomeprazole (20mg),Tablet,Zydus Cadila,Gastro,2025-01,2028-01,OT Store,10,strip,2025-04-05,Apollo Wholesale Pvt Ltd
B02376,IPT255982,Intalol 50mg Tablet,Atenolol (50mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-02,2027-02,Emergency Store,50,strip,2025-05-07,Kerala Medical Supplies Co.
B02377,LP25D872,Jink Syrup,Zinc Gluconate (20mg),Syrup,Lincoln Pharmaceuticals Ltd,Supplement,2025-05,2027-05,ICU Store,200,bottle,2025-07-15,Kerala Medical Supplies Co.
B02378,T2410-303,Jardiance 25mg Tablet,Empagliflozin (25mg),Tablet,Boehringer Ingelheim,Other,2024-11,2027-11,Main Pharmacy,200,strip,2024-12-27,"Medline Distributors, Thiruvananthapuram"
B02379,T2406-087,Udiliv 150mg Tablet,Ursodeoxycholic Acid (150mg),Tablet,Abbott,Gastro,2024-08,2026-08,OPD Pharmacy,120,strip,2024-09-13,Apollo Wholesale Pvt Ltd
B02380,25359560,Salbid 2mg Tablet,Salbutamol (2mg),Tablet,Micro Labs Ltd,Respiratory,2025-01,2027-01,Emergency Store,0,strip,2025-03-27,Sree Pharma Agencies
B02381,ALT242195,Acecloflam XP 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-03,2027-03,Ward Store (Paeds),40,strip,2025-05-28,Kerala Medical Supplies Co.
B02382,T2512-604,Emeset 4 Tablet,Ondansetron (4mg),Tablet,Cipla Ltd,Gastro,2024-04,2026-04,ICU Store,120,strip,2024-07-02,"Medline Distributors, Thiruvananthapuram"
B02383,ALT252688,Dapanorm 10 Tablet,Dapagliflozin (10mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-12,2027-12,Emergency Store,20,strip,2025-02-27,"Medline Distributors, Thiruvananthapuram"
B02384,CLT249200,Amlip 10 Tablet,Amlodipine (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-12,2027-12,OT Store,200,strip,2025-01-06,Malabar Pharma Distributors
B02385,GSX248556,T-Bact 2% Ointment,Mupirocin (2% w/w),Ointment,Glaxo SmithKline Pharmaceuticals Ltd,Dermatology,2024-07,2026-07,OPD Pharmacy,20,tube,2024-10-20,Malabar Pharma Distributors
B02386,CL25B453,Emeset 8 Tablet,Ondansetron (8mg),Tablet,Cipla Ltd,Gastro,2024-04,2027-04,OT Store,0,strip,2024-07-11,"Medline Distributors, Thiruvananthapuram"
B02387,T2402-130,Azukon MR Tablet,Gliclazide (30mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-06,2027-06,ICU Store,300,strip,2024-07-30,"Medline Distributors, Thiruvananthapuram"
B02388,IPT241850,Golbi 150 Tablet,Ursodeoxycholic Acid (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-03,2025-09,OT Store,0,strip,2024-05-26,Kerala Medical Supplies Co.
B02389,IP24M773,Cefpet XL 200mg Tablet,Cefpodoxime Proxetil (200mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-05,2025-11,Ward Store (Paeds),60,strip,2024-08-22,Kerala Medical Supplies Co.
B02390,I2402-322,ESGIPYRIN DS INJECTION,Diclofenac (25mg/ml),Injection,Abbott,Analgesic/Antipyretic,2024-12,2027-12,Main Pharmacy,40,vial/amp,2025-03-13,Apollo Wholesale Pvt Ltd
B02391,CPT24046,Ciprofloxacin Hydrochloride Tablets IP 250 mg,Ciprofloxacin (250mg),Tablet,Vivek Pharmachem (India) Ltd.,Antibiotic,2024-07,2026-06,ICU Store,100,strip,2024-10-18,Malabar Pharma Distributors
B02392,JB24H469,Rantac 300 Tablet,Ranitidine (300mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Gastro,2024-12,2027-12,Emergency Store,100,strip,2025-02-10,"Medline Distributors, Thiruvananthapuram"
B02393,53154591,Razo A 200mg/20mg Capsule SR,Aceclofenac (200mg) + Rabeprazole (20mg),Capsule,Precise Lifescience,Gastro,2025-03,2028-03,Emergency Store,80,strip,2025-06-11,Sree Pharma Agencies
B02394,X2506-993,Thrombophob Ointment,Benzyl Nicotinate (2mg) + Heparin (50IU),Ointment,Zydus Cadila,Anticoagulant,2025-02,2027-02,OT Store,200,tube,2025-04-07,"Medline Distributors, Thiruvananthapuram"
B02395,ZC25G620,Levoday 250 Tablet,Levofloxacin (250mg),Tablet,Zydus Cadila,Antibiotic,2024-12,2027-12,ICU Store,40,strip,2025-03-31,Sanjivani Drug House
B02396,BIT245680,Jardiance 25mg Tablet,Empagliflozin (25mg),Tablet,Boehringer Ingelheim,Other,2024-02,2027-02,Emergency Store,300,strip,2024-05-13,Sanjivani Drug House
B02397,ZCT247545,Cadvocet M 5mg/10mg Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Zydus Cadila,Respiratory,2024-01,2027-01,OT Store,100,strip,2024-04-18,"Medline Distributors, Thiruvananthapuram"
B02398,MLC255675,Dolodol 50mg Capsule,Tramadol (50mg),Capsule,Micro Labs Ltd,Analgesic/Antipyretic,2024-02,2027-02,Main Pharmacy,300,strip,2024-04-11,Sanjivani Drug House
B02399,T2411-708,Abtelmi 20 Tablet,Telmisartan (20mg),Tablet,Abbott,Cardiovascular,2025-01,2026-07,Ward Store (Paeds),300,strip,2025-01-29,"Medline Distributors, Thiruvananthapuram"
B02400,CL25J099,Dytor 40 Tablet,Torasemide (40mg),Tablet,Cipla Ltd,Cardiovascular,2024-09,2026-03,OT Store,20,strip,2024-11-08,Sanjivani Drug House
B02401,GST242124,Eltroxin 125mcg Tablet,Thyroxine (125mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2024-08,2026-02,Ward Store (Paeds),10,strip,2024-09-06,Apollo Wholesale Pvt Ltd
B02402,LHI250673,Biocef 1g Injection,Ceftriaxone (1000mg),Injection,Leeford Healthcare Ltd,Antibiotic,2024-11,2026-11,Emergency Store,10,vial/amp,2024-12-06,Kerala Medical Supplies Co.
B02403,X2504-019,Intabact 2% Ointment,Mupirocin (2% w/w),Ointment,Intas Pharmaceuticals Ltd,Dermatology,2024-04,2027-04,Main Pharmacy,30,tube,2024-07-21,Apollo Wholesale Pvt Ltd
B02404,IPT249861,Niftas 50 Tablet,Nitrofurantoin (50mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-04,2028-04,Ward Store (Paeds),50,strip,2025-05-10,"Medline Distributors, Thiruvananthapuram"
B02405,88294709,Glimikem 1mg Tablet,Glimepiride (1mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-02,2027-02,Ward Store (Paeds),40,strip,2025-04-01,Apollo Wholesale Pvt Ltd
B02406,CL25K285,Theobid 300mg Tablet,Theophylline (300mg),Tablet,Cipla Ltd,Respiratory,2025-04,2027-04,OT Store,300,strip,2025-07-07,Sree Pharma Agencies
B02407,LLT259295,Amipace 100 Tablet,Amiodarone (100mg),Tablet,Lupin Ltd,Cardiovascular,2025-01,2026-07,ICU Store,60,strip,2025-03-26,Kerala Medical Supplies Co.
B02408,AS-1460,Curopine Injection,Atropine Sulphate (0.6mg/ml),Injection,Pharma Cure Laboratories,Anaesthesia/Critical care,2025-01,2026-12,ICU Store,10,vial/amp,2025-02-16,Kerala Medical Supplies Co.
B02409,IPX252657,Eco Tears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Ophthalmology,2025-03,2028-03,OPD Pharmacy,80,bottle,2025-06-25,"Medline Distributors, Thiruvananthapuram"
B02410,54410181,Amlogift 5mg Tablet,Amlodipine (5mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-03,2026-03,Ward Store (Paeds),120,strip,2024-03-30,Malabar Pharma Distributors
B02411,AX244915,Ipratop 200mcg Inhaler,Ipratropium (200mcg),Inhaler,AstraZeneca,Respiratory,2025-01,2027-01,OT Store,40,inhaler,2025-03-06,Kerala Medical Supplies Co.
B02412,DR24E975,Clamp 1000mg/200mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Dr Reddy's Laboratories Ltd,Antibiotic,2024-06,2026-06,OT Store,0,vial/amp,2024-09-28,Malabar Pharma Distributors
B02413,34092638,Manogyl 10% Infusion,Mannitol (10% w/v),Infusion,J B Chemicals and Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-11,2026-11,OPD Pharmacy,200,bottle,2024-12-09,Malabar Pharma Distributors
B02414,MLC243410,Neurobion Alfa Capsule,Methylcobalamin (750mcg) + Alpha Lipoic Acid (100mg),Capsule,Merck Ltd,Supplement,2024-01,2026-01,OPD Pharmacy,80,strip,2024-02-08,"Medline Distributors, Thiruvananthapuram"
B02415,T2504-327,Valtec 300mg Tablet,Sodium Valproate (300mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-04,2026-04,OPD Pharmacy,20,strip,2024-06-21,Malabar Pharma Distributors
B02416,C2509-270,Itraclar 100mg Capsule,Itraconazole (100mg),Capsule,Torrent Pharmaceuticals Ltd,Antifungal,2024-02,2025-08,ICU Store,300,strip,2024-03-05,Apollo Wholesale Pvt Ltd
B02417,99029797,Derihaler 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Zydus Cadila,Respiratory,2024-07,2027-07,Main Pharmacy,150,inhaler,2024-08-23,Kerala Medical Supplies Co.
B02418,LL24G200,Lup Inh 300mg Tablet,Isoniazid (300mg),Tablet,Lupin Ltd,Anti-TB,2024-03,2027-03,OT Store,120,strip,2024-05-31,Malabar Pharma Distributors
B02419,ALT243517,Flukem 150mg Tablet,Fluconazole (150mg),Tablet,Alkem Laboratories Ltd,Antifungal,2024-08,2026-08,ICU Store,200,strip,2024-11-18,Kerala Medical Supplies Co.
B02420,T2411-770,Izra 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-02,2026-02,Emergency Store,150,strip,2024-04-29,Apollo Wholesale Pvt Ltd
B02421,AL25J682,Esokem 20 Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-06,2026-06,Emergency Store,30,strip,2024-08-15,Kerala Medical Supplies Co.
B02422,77034462,Alciflox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-01,2027-01,Ward Store (Paeds),10,strip,2025-03-07,Apollo Wholesale Pvt Ltd
B02423,53514076,Clearnoz 0.75% Nasal Drops,Sodium Chloride (0.75% w/v),Drops,Cipla Ltd,IV Fluids,2024-06,2025-12,ICU Store,150,bottle,2024-06-28,Apollo Wholesale Pvt Ltd
B02424,IEW1480C,Eldervit-12 Injection,Vitamin C + B12 + Folic Acid + Niacinamide,Injection,E.G. Pharmaceuticals,Supplement,2024-09,2026-08,OT Store,120,vial/amp,2024-11-26,Apollo Wholesale Pvt Ltd
B02425,TPT243731,Loracalm 1mg Tablet,Lorazepam (1mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2027-06,Emergency Store,20,strip,2024-09-18,Kerala Medical Supplies Co.
B02426,IPT255310,T Glip 20 Tablet,Teneligliptin (20mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-08,2026-02,Emergency Store,30,strip,2024-10-04,"Medline Distributors, Thiruvananthapuram"
B02427,CLT252133,Cresar 80H Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2026-01,Ward Store (Paeds),10,strip,2024-08-01,Kerala Medical Supplies Co.
B02428,V2401-241,Lizoran 600mg Infusion,Linezolid (600mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2026-02,Ward Store (Paeds),80,bottle,2024-05-25,Apollo Wholesale Pvt Ltd
B02429,ALI243868,Cytovan 500mg Injection,Vancomycin (500mg),Injection,Alkem Laboratories Ltd,Antibiotic,2025-03,2027-03,Ward Store (Paeds),300,vial/amp,2025-06-14,Sree Pharma Agencies
B02430,I2408-886,Metaclopramide Injection,Metoclopramide (NA),Injection,Cipla Ltd,Gastro,2024-04,2027-04,Ward Store (Paeds),300,vial/amp,2024-07-10,Sree Pharma Agencies
B02431,TP25M168,Rabemed 10mg Tablet,Rabeprazole (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-03,2028-03,OPD Pharmacy,10,strip,2025-06-04,Apollo Wholesale Pvt Ltd
B02432,22120246,Ondem 4 Tablet,Ondansetron (4mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-04,2027-04,ICU Store,0,strip,2024-06-15,Sanjivani Drug House
B02433,72150455,Brutacef 100mg Dry Syrup,Cefixime (100mg),Syrup,Mankind Pharma Ltd,Antibiotic,2025-04,2027-04,Main Pharmacy,80,bottle,2025-07-14,Kerala Medical Supplies Co.
B02434,36491961,Gemer 0.5 Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-07,2027-07,ICU Store,30,strip,2024-09-05,Sanjivani Drug House
B02435,T2411-458,Udiliv 150mg Tablet,Ursodeoxycholic Acid (150mg),Tablet,Abbott,Gastro,2025-01,2026-07,OPD Pharmacy,300,strip,2025-03-14,Kerala Medical Supplies Co.
B02436,27613681,Brufen 200 Tablet,Ibuprofen (200mg),Tablet,Abbott,Analgesic/Antipyretic,2024-07,2027-07,ICU Store,80,strip,2024-07-28,Kerala Medical Supplies Co.
B02437,20798726,Cyclopam Plus Tablet,Dicyclomine (20mg) + Paracetamol (500mg),Tablet,Indoco Remedies Ltd,Analgesic/Antipyretic,2024-06,2027-06,ICU Store,300,strip,2024-08-23,Malabar Pharma Distributors
B02438,AL25E078,Mecobex 500mcg Injection,Methylcobalamin (500mcg),Injection,Alkem Laboratories Ltd,Supplement,2024-12,2027-12,Emergency Store,40,vial/amp,2025-02-14,Apollo Wholesale Pvt Ltd
B02439,SP24J351,Teleact 20 Tablet,Telmisartan (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-01,2027-01,OT Store,30,strip,2025-03-30,Sanjivani Drug House
B02440,ALT249458,Olkem 20 Tablet,Olmesartan Medoxomil (20mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-08,2027-08,OPD Pharmacy,50,strip,2024-08-30,Sanjivani Drug House
B02441,S2502-921,Rantac Infant Syrup Mint,Ranitidine (75mg/5ml),Syrup,J B Chemicals and Pharmaceuticals Ltd,Gastro,2025-01,2028-01,Emergency Store,50,bottle,2025-02-05,Sree Pharma Agencies
B02442,LLT257278,F Con 150mg Tablet,Fluconazole (150mg),Tablet,Lupin Ltd,Antifungal,2024-01,2026-01,OT Store,10,strip,2024-03-02,Sree Pharma Agencies
B02443,68551203,Sartel H 40 Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-05,2025-11,OT Store,10,strip,2024-08-07,Malabar Pharma Distributors
B02444,X2505-855,Asthalin 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Cipla Ltd,Respiratory,2024-04,2026-04,Main Pharmacy,80,inhaler,2024-05-06,Malabar Pharma Distributors
B02445,EP24L029,Eprin 75mg Tablet,Aspirin (75mg),Tablet,Elder Pharmaceuticals Ltd,Cardiovascular,2024-07,2027-07,OT Store,120,strip,2024-09-14,Sanjivani Drug House
B02446,SPX259144,Sucral Cream,Sucralfate (7% w/w),Cream,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-03,2027-03,ICU Store,60,tube,2024-05-22,Sree Pharma Agencies
B02447,X2401-693,Norflox Eye/Ear Drops,Norfloxacin (0.30%),Ear Drops,Cipla Ltd,Other,2025-01,2027-01,Ward Store (Paeds),150,bottle,2025-01-26,Sree Pharma Agencies
B02448,LLS242137,CZ 3 Syrup,Cetirizine (5mg/5ml),Syrup,Lupin Ltd,Respiratory,2024-07,2026-07,Ward Store (Paeds),0,bottle,2024-10-05,Sanjivani Drug House
B02449,IP24E589,Decotas 30mg Tablet,Deflazacort (30mg),Tablet,Intas Pharmaceuticals Ltd,Steroid,2024-07,2026-01,Ward Store (Paeds),120,strip,2024-09-24,Sree Pharma Agencies
B02450,73625618,Ambrocon 7.5mg Oral Drops,Ambroxol (7.5mg),Drops,Ikon Remedies Pvt Ltd,Respiratory,2024-03,2026-03,Emergency Store,10,bottle,2024-06-27,Kerala Medical Supplies Co.
B02451,24097501,Sitaxa M 50/1000 Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-03,2025-09,Emergency Store,80,strip,2024-06-10,Sanjivani Drug House
B02452,SI24K760,Valparin 200 Oral Solution Delicious Pineapple,Sodium Valproate (200mg/5ml),Oral Solution,Sanofi India Ltd,Neurology/Psychiatry,2024-01,2026-01,OT Store,20,bottle,2024-03-03,Sanjivani Drug House
B02453,AL25M851,Dolocare 500mg Tablet,Paracetamol (500mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-03,2028-03,OT Store,80,strip,2025-04-07,Sree Pharma Agencies
B02454,PLT248806,Ativan 1mg Tablet,Lorazepam (1mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2024-10,2026-04,Main Pharmacy,300,strip,2024-12-29,"Medline Distributors, Thiruvananthapuram"
B02455,ZC24K301,Sucrace Suspension,Sucralfate (1000mg),Suspension,Zydus Cadila,Gastro,2025-02,2027-02,OT Store,10,bottle,2025-03-15,Sanjivani Drug House
B02456,A24F455,AB-Rozu 10 Tablet,Rosuvastatin (10mg),Tablet,Abbott,Cardiovascular,2024-07,2026-07,Main Pharmacy,20,strip,2024-09-28,Sanjivani Drug House
B02457,AL25G994,Metrokem IV 100mg Infusion,Metronidazole (100mg),Infusion,Alkem Laboratories Ltd,Antibiotic,2024-05,2027-05,Main Pharmacy,80,bottle,2024-07-17,Sanjivani Drug House
B02458,SP25C683,Citelec 250mg Injection,Citicoline (250mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-01,2028-01,OPD Pharmacy,100,vial/amp,2025-04-03,Apollo Wholesale Pvt Ltd
B02459,LHT253645,Alcipan 40mg Tablet,Pantoprazole (40mg),Tablet,Leeford Healthcare Ltd,Gastro,2024-07,2026-07,Main Pharmacy,80,strip,2024-09-17,Kerala Medical Supplies Co.
B02460,13930993,Levomac 250 Tablet,Levofloxacin (250mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2025-01,2027-01,Main Pharmacy,0,strip,2025-02-23,Sree Pharma Agencies
B02461,PCT1208,Paracetamol Tablets IP 500 mg (Jan Aushadhi),Paracetamol (500mg),Tablet,Unicure India Ltd. (Mkt: PMBI),Analgesic/Antipyretic,2024-08,2026-07,Main Pharmacy,200,strip,2024-10-14,Malabar Pharma Distributors
B02462,17433978,Teleact D 80 Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-07,2026-01,ICU Store,30,strip,2024-09-30,Apollo Wholesale Pvt Ltd
B02463,AT248627,Ketof-DT Tablet,Ketorolac (10mg),Tablet,Abbott,Analgesic/Antipyretic,2024-01,2027-01,OPD Pharmacy,40,strip,2024-04-04,"Medline Distributors, Thiruvananthapuram"
B02464,AL24C384,Sunheal Pure Cream,Zinc Oxide (25% w/w),Cream,Alkem Laboratories Ltd,Supplement,2024-05,2026-05,OPD Pharmacy,120,tube,2024-06-28,"Medline Distributors, Thiruvananthapuram"
B02465,ALI244037,Cefkem 1000mg/500mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Alkem Laboratories Ltd,Antibiotic,2025-04,2028-04,Emergency Store,10,vial/amp,2025-05-30,Sanjivani Drug House
B02466,SP24J747,Encorate 100mg Injection,Sodium Valproate (100mg),Injection,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2027-01,ICU Store,10,vial/amp,2024-02-09,Malabar Pharma Distributors
B02467,AT246396,Rivotril 0.5mg Tablet,Clonazepam (0.5mg),Tablet,Abbott,Neurology/Psychiatry,2025-04,2027-04,Ward Store (Paeds),120,strip,2025-06-16,Sanjivani Drug House
B02468,77298838,Telvilite 40mg Tablet,Telmisartan (40mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-03,2026-03,Main Pharmacy,300,strip,2024-06-13,Kerala Medical Supplies Co.
B02469,AT240786,Flagyl 200 Tablet,Metronidazole (200mg),Tablet,Abbott,Antibiotic,2025-01,2027-01,Emergency Store,40,strip,2025-03-07,Apollo Wholesale Pvt Ltd
B02470,CL24F326,Levoflox 500 Infusion,Levofloxacin (500mg),Infusion,Cipla Ltd,Antibiotic,2024-11,2027-11,ICU Store,30,bottle,2024-12-19,Apollo Wholesale Pvt Ltd
B02471,S2506-984,Sucral D Suspension,Domperidone (7.5mg) + Sucralfate (1000mg),Suspension,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-01,2027-01,OPD Pharmacy,40,bottle,2024-03-03,"Medline Distributors, Thiruvananthapuram"
B02472,ZC25C716,Linid IV 600mg Infusion,Linezolid (600mg),Infusion,Zydus Cadila,Antibiotic,2024-07,2026-07,OT Store,50,bottle,2024-09-20,"Medline Distributors, Thiruvananthapuram"
B02473,X2406-626,Rashcare Cream,Zinc Oxide (8.5% w/w),Cream,Leeford Healthcare Ltd,Supplement,2025-03,2028-03,ICU Store,200,tube,2025-06-01,Apollo Wholesale Pvt Ltd
B02474,SPX256941,Glytears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2024-02,2025-08,Main Pharmacy,10,bottle,2024-05-29,Malabar Pharma Distributors
B02475,T2411-239,Betavert 16 Tablet,Betahistine (16mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-01,2026-01,OPD Pharmacy,0,strip,2024-04-17,Sanjivani Drug House
B02476,SPS257380,Rancotrim Suspension,Sulfamethoxazole (200mg/5ml) + Trimethoprim (40mg/5ml),Suspension,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-04,2027-04,Ward Store (Paeds),80,bottle,2025-05-15,Apollo Wholesale Pvt Ltd
B02477,T2404-052,Pantodac 20 Tablet,Pantoprazole (20mg),Tablet,Zydus Cadila,Gastro,2024-01,2027-01,OT Store,10,strip,2024-04-26,Kerala Medical Supplies Co.
B02478,SPT249801,CEPOCOR 100MG TABLET,Cefpodoxime Proxetil (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2025-09,Emergency Store,0,strip,2024-06-23,Apollo Wholesale Pvt Ltd
B02479,CLX259626,Budecort 0.5mg Respules 2ml,Budesonide (0.5mg),Respules,Cipla Ltd,Respiratory,2025-05,2028-05,OT Store,120,respule,2025-07-04,Malabar Pharma Distributors
B02480,68548403,Nexpro 40 Tablet,Esomeprazole (40mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2025-02,2028-02,Main Pharmacy,80,strip,2025-02-28,Kerala Medical Supplies Co.
B02481,I2504-840,Enatrate Injection,Adrenaline (NA),Injection,Entod Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-12,2026-06,OPD Pharmacy,20,vial/amp,2025-03-15,"Medline Distributors, Thiruvananthapuram"
B02482,CL25G176,Amlip 10 Tablet,Amlodipine (10mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2028-01,OT Store,200,strip,2025-02-02,Sree Pharma Agencies
B02483,LLI244662,Merenz 1000mg Injection,Meropenem (1000mg),Injection,Lupin Ltd,Antibiotic,2024-01,2026-01,Main Pharmacy,150,vial/amp,2024-04-28,Kerala Medical Supplies Co.
B02484,T2401-251,Metolar 25 Tablet,Metoprolol Tartrate (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-05,2027-05,Main Pharmacy,60,strip,2024-06-06,Apollo Wholesale Pvt Ltd
B02485,59633035,TOR 10 Tablet,Torasemide (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-04,2027-04,Ward Store (Paeds),300,strip,2025-06-24,Apollo Wholesale Pvt Ltd
B02486,T2403-740,Stromix 75mg Tablet,Clopidogrel (75mg),Tablet,Abbott,Cardiovascular,2024-07,2026-01,Main Pharmacy,20,strip,2024-09-25,"Medline Distributors, Thiruvananthapuram"
B02487,CLI253164,Ciplox 2mg Injection,Ciprofloxacin (2mg),Injection,Cipla Ltd,Antibiotic,2025-02,2026-08,OT Store,0,vial/amp,2025-04-01,Malabar Pharma Distributors
B02488,TPT244485,Altipod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-01,2026-03,Emergency Store,150,strip,2024-02-13,"Medline Distributors, Thiruvananthapuram"
B02489,58319528,Pregabid 300mg Capsule,Pregabalin (300mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2027-07,OT Store,80,strip,2024-09-21,"Medline Distributors, Thiruvananthapuram"
B02490,CLC253271,Urimax 0.4 Ecopack Capsule MR,Tamsulosin (400mcg),Capsule,Cipla Ltd,Urology,2024-11,2027-11,Main Pharmacy,10,strip,2024-11-26,Apollo Wholesale Pvt Ltd
B02491,T2404-328,Gabapin 100 Tablet,Gabapentin (100mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2026-07,OPD Pharmacy,150,strip,2024-09-17,Apollo Wholesale Pvt Ltd
B02492,86866717,Cetzine Oral Drops,Cetirizine (10mg),Drops,Dr Reddy's Laboratories Ltd,Respiratory,2024-01,2027-01,OPD Pharmacy,20,bottle,2024-04-03,Kerala Medical Supplies Co.
B02493,T2508-744,Cerzin 10mg Tablet,Cetirizine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Respiratory,2025-05,2027-05,Main Pharmacy,300,strip,2025-07-15,Sanjivani Drug House
B02494,LLT244705,L-Cin 250 Tablet,Levofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-04,2026-04,Emergency Store,10,strip,2024-06-15,Sanjivani Drug House
B02495,IL25D792,Perinorm Syrup,Metoclopramide (5mg),Syrup,Ipca Laboratories Ltd,Gastro,2025-01,2028-01,OPD Pharmacy,120,bottle,2025-01-31,Kerala Medical Supplies Co.
B02496,I2403-296,Mepresso 125mg Injection,Methylprednisolone (125mg),Injection,Intas Pharmaceuticals Ltd,Steroid,2024-06,2025-12,Main Pharmacy,10,vial/amp,2024-09-28,Kerala Medical Supplies Co.
B02497,CLT259458,Levepsy 1000 Tablet,Levetiracetam (1000mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-01,2026-11,OT Store,10,strip,2024-01-29,Malabar Pharma Distributors
B02498,SP24K599,Oleanz 10 Tablet,Olanzapine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-07,2026-01,Emergency Store,150,strip,2024-10-17,Sree Pharma Agencies
B02499,IHV259508,D5 Infusion,Dextrose (5gm),Infusion,Infutec Healthcare Limited,IV Fluids,2024-05,2026-05,OPD Pharmacy,200,bottle,2024-07-24,"Medline Distributors, Thiruvananthapuram"
B02500,LLT257647,Nitrobest Tablet SR,Nitrofurantoin (100mg),Tablet,Lupin Ltd,Antibiotic,2024-01,2026-01,Ward Store (Paeds),60,strip,2024-04-10,Sanjivani Drug House
B02501,I2405-352,Bupitroy 0.5% Injection,Bupivacaine (0.5%),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-06,2025-12,OPD Pharmacy,150,vial/amp,2024-06-28,Sanjivani Drug House
B02502,63404755,Neuromet 500mcg Injection,Methylcobalamin (500mcg),Injection,Zydus Cadila,Supplement,2024-01,2026-01,Ward Store (Paeds),200,vial/amp,2024-04-03,"Medline Distributors, Thiruvananthapuram"
B02503,CLT250990,Actiflu 500mg Tablet,Paracetamol (500mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-07,2026-07,OPD Pharmacy,20,strip,2024-09-19,Sanjivani Drug House
B02504,82512113,Hexidol 1.5 Tablet,Haloperidol (1.5mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-04,2025-10,OT Store,60,strip,2024-07-12,Malabar Pharma Distributors
B02505,LL24C795,Cortina DS 800mg/160mg Tablet,Sulfamethoxazole (800mg) + Trimethoprim (160mg),Tablet,Lupin Ltd,Antibiotic,2024-04,2025-10,Emergency Store,60,strip,2024-07-29,Apollo Wholesale Pvt Ltd
B02506,30042306,Macralfate Suspension Sugar Free,Sucralfate (1000mg),Suspension,Macleods Pharmaceuticals Pvt Ltd,Gastro,2024-03,2025-09,ICU Store,10,bottle,2024-06-26,Kerala Medical Supplies Co.
B02507,CLC250701,Urimax 0.2 Capsule MR,Tamsulosin (0.2mg),Capsule,Cipla Ltd,Urology,2024-03,2026-03,Ward Store (Paeds),0,strip,2024-04-13,Sanjivani Drug House
B02508,EP25H011,Enatrate Injection,Adrenaline (NA),Injection,Entod Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-02,2026-08,ICU Store,150,vial/amp,2025-04-23,Kerala Medical Supplies Co.
B02509,MPS241407,Zithrox 100 Rediuse Suspension,Azithromycin (100mg/5ml),Suspension,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-02,2027-02,OT Store,10,bottle,2024-04-03,"Medline Distributors, Thiruvananthapuram"
B02510,IPC249127,Tramatas 50mg Capsule,Tramadol (50mg),Capsule,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-09,2027-09,Emergency Store,0,strip,2024-10-05,"Medline Distributors, Thiruvananthapuram"
B02511,ALT251720,Levenue 1000 Tablet,Levetiracetam (1000mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2025-01,2026-07,OT Store,10,strip,2025-04-25,"Medline Distributors, Thiruvananthapuram"
B02512,TPC251920,Itraclar 100mg Capsule,Itraconazole (100mg),Capsule,Torrent Pharmaceuticals Ltd,Antifungal,2024-09,2026-09,Ward Store (Paeds),100,strip,2024-10-11,Kerala Medical Supplies Co.
B02513,T2505-844,Encelin 50mg Tablet,Vildagliptin (50mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-06,2025-12,Main Pharmacy,60,strip,2024-07-14,"Medline Distributors, Thiruvananthapuram"
B02514,IPC248778,Halo 5mg Capsule,Haloperidol (5mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-03,2028-03,ICU Store,10,strip,2025-04-12,Apollo Wholesale Pvt Ltd
B02515,KSI241747,Adrelin Injection,Adrenaline (NA),Injection,Klar Sehen Pvt Ltd,Anaesthesia/Critical care,2024-04,2026-04,OPD Pharmacy,40,vial/amp,2024-07-04,Sree Pharma Agencies
B02516,FL24B545,Lastuss LA Syrup,Dextromethorphan Hydrobromide (15mg/5ml),Syrup,FDC Ltd,Respiratory,2025-05,2027-05,Ward Store (Paeds),120,bottle,2025-06-22,Sanjivani Drug House
B02517,LHX253903,Weldinide 200mcg Inhaler,Budesonide (200mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-01,2027-01,OT Store,120,inhaler,2024-01-29,Apollo Wholesale Pvt Ltd
B02518,ML24K978,Salbid 2mg Tablet,Salbutamol (2mg),Tablet,Micro Labs Ltd,Respiratory,2024-08,2026-08,OPD Pharmacy,100,strip,2024-10-18,Malabar Pharma Distributors
B02519,85170631,Arbitel 20 Tablet,Telmisartan (20mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-04,2027-04,Ward Store (Paeds),60,strip,2024-06-26,Sanjivani Drug House
B02520,I2511-879,Tramef 50mg Injection,Tramadol (50mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-08,2026-08,Main Pharmacy,30,vial/amp,2024-11-02,Kerala Medical Supplies Co.
B02521,T2410-460,Abixim 100mg Tablet,Cefixime (100mg),Tablet,Abbott,Antibiotic,2024-12,2027-12,Emergency Store,150,strip,2025-01-16,Sree Pharma Agencies
B02522,CLT250575,Montair LC Kid Tablet DT,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Cipla Ltd,Respiratory,2024-08,2026-08,Ward Store (Paeds),50,strip,2024-10-14,Malabar Pharma Distributors
B02523,69531177,Docmycin 100mg Tablet,Doxycycline (100mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-08,2026-08,ICU Store,40,strip,2024-11-25,Sanjivani Drug House
B02524,T2410-826,FCN 150 Tablet,Fluconazole (150mg),Tablet,Intas Pharmaceuticals Ltd,Antifungal,2025-02,2028-02,OT Store,120,strip,2025-05-18,"Medline Distributors, Thiruvananthapuram"
B02525,T2502-256,Ecator 10mg Tablet,Ramipril (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,Main Pharmacy,10,strip,2024-11-15,Sanjivani Drug House
B02526,SKV245545,Dex 25% Infusion,Dextrose (25% w/v),Infusion,Shree KrishnaKeshav Laboratories Ltd,IV Fluids,2024-04,2025-10,ICU Store,50,bottle,2024-07-17,Sree Pharma Agencies
B02527,C2507-854,Adamon 50mg Capsule,Tramadol (50mg),Capsule,Zydus Cadila,Analgesic/Antipyretic,2025-03,2027-03,Ward Store (Paeds),150,strip,2025-06-20,Kerala Medical Supplies Co.
B02528,S2510-055,Sucral D Suspension,Domperidone (7.5mg) + Sucralfate (1000mg),Suspension,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-11,2027-11,Main Pharmacy,100,bottle,2025-01-08,Apollo Wholesale Pvt Ltd
B02529,73889312,Domstal Baby Oral Drops,Domperidone (10mg/ml),Drops,Torrent Pharmaceuticals Ltd,Gastro,2024-12,2027-12,OPD Pharmacy,20,bottle,2025-03-24,Sree Pharma Agencies
B02530,SP25A145,Budez CR Capsule,Budesonide (3mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2024-04,2027-04,OT Store,30,strip,2024-06-02,Kerala Medical Supplies Co.
B02531,CLX243397,Entofoam NF Cream,Hydrocortisone (10% w/w),Cream,Cipla Ltd,Steroid,2024-09,2027-09,OPD Pharmacy,300,tube,2024-09-29,Apollo Wholesale Pvt Ltd
B02532,IPT255398,Azintas 250 Tablet,Azithromycin (250mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-01,2027-01,OT Store,0,strip,2025-02-17,Malabar Pharma Distributors
B02533,MLT257880,Melmet 1000 SR Tablet,Metformin (1000mg),Tablet,Micro Labs Ltd,Diabetes,2024-12,2026-12,ICU Store,0,strip,2025-02-21,"Medline Distributors, Thiruvananthapuram"
B02534,TPI247545,Beprin 500iu Injection,Heparin (500iu/5ml),Injection,Taj Pharma India Ltd,Anticoagulant,2024-03,2027-03,ICU Store,80,vial/amp,2024-04-01,Malabar Pharma Distributors
B02535,T2410-744,Isomin 20mg Tablet,Isosorbide Mononitrate (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-12,2026-06,OPD Pharmacy,80,strip,2025-03-16,Kerala Medical Supplies Co.
B02536,MPT251498,Thyrox 100 Tablet,Thyroxine (100mcg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Endocrine,2024-02,2027-02,OT Store,60,strip,2024-03-24,Sree Pharma Agencies
B02537,40885967,Dytor 20 Tablet,Torasemide (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-10,2027-10,ICU Store,300,strip,2025-01-11,Sree Pharma Agencies
B02538,S2410-641,Bioprim Syrup,Sulfamethoxazole (200mg) + Trimethoprim (40mg),Syrup,Zydus Cadila,Antibiotic,2025-01,2027-01,Main Pharmacy,150,bottle,2025-03-27,Kerala Medical Supplies Co.
B02539,AL25H984,Alkem Ketorolac 100mg Injection,Ketorolac (100mg),Injection,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-03,2027-03,Ward Store (Paeds),300,vial/amp,2024-05-31,Kerala Medical Supplies Co.
B02540,GPX243560,Candid Ear Drop,Lidocaine (2% w/v) + Clotrimazole (1% w/v),Ear Drops,Glenmark Pharmaceuticals Ltd,Antifungal,2025-01,2027-01,Emergency Store,0,bottle,2025-04-29,Sanjivani Drug House
B02541,ALT258087,Almet 10mg Tablet,Metoclopramide (10mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-09,2027-09,Emergency Store,300,strip,2024-11-20,"Medline Distributors, Thiruvananthapuram"
B02542,61839427,Rosugard 5mg Tablet,Rosuvastatin (5mg),Tablet,Cipla Ltd,Cardiovascular,2025-01,2026-07,Emergency Store,0,strip,2025-02-10,"Medline Distributors, Thiruvananthapuram"
B02543,T2501-940,Rostar 10 Tablet,Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-06,2027-06,Emergency Store,30,strip,2024-09-26,Kerala Medical Supplies Co.
B02544,T2504-339,Zovirax 800 Tablet,Acyclovir (800mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Antiviral,2025-03,2026-09,Emergency Store,0,strip,2025-04-30,Sree Pharma Agencies
B02545,14969146,Metapro -XL 25 Tablet,Metoprolol Succinate (23.75mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-04,2027-04,OPD Pharmacy,120,strip,2025-06-02,Apollo Wholesale Pvt Ltd
B02546,MP25D879,Januvia 100mg Tablet,Sitagliptin (100mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-12,2026-12,Ward Store (Paeds),40,strip,2025-01-23,Sree Pharma Agencies
B02547,T2508-479,Bigclav CV 500mg/125mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Mankind Pharma Ltd,Antibiotic,2024-08,2027-08,ICU Store,60,strip,2024-10-20,Apollo Wholesale Pvt Ltd
B02548,P24L199,Gentacos Injection,Gentamicin (40mg/ml),Injection,Paksons Pharmaceuticals Pvt. Ltd.,Antibiotic,2024-12,2026-11,OPD Pharmacy,120,vial/amp,2025-01-30,"Medline Distributors, Thiruvananthapuram"
B02549,T2408-928,C-Pram S 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-07,2027-07,ICU Store,80,strip,2024-10-23,Sanjivani Drug House
B02550,LL25F587,Lupigenta Eye/Ear Drops,Gentamicin (NA),Ear Drops,Lupin Ltd,Antibiotic,2024-08,2026-08,Emergency Store,150,bottle,2024-10-13,"Medline Distributors, Thiruvananthapuram"
B02551,IPT241181,Azintas 250 Tablet,Azithromycin (250mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-01,2028-01,Ward Store (Paeds),40,strip,2025-04-20,Sanjivani Drug House
B02552,X2506-245,Atro Eye Drop,Atropine (1% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-03,2027-03,Ward Store (Paeds),300,bottle,2025-05-25,Malabar Pharma Distributors
B02553,UP25C616,Make FE 100mg Injection,Ferrous Ascorbate (100mg),Injection,Uniword Pharma,Haematology,2025-02,2028-02,Main Pharmacy,120,vial/amp,2025-04-17,Kerala Medical Supplies Co.
B02554,EPT243614,Eprin 75mg Tablet,Aspirin (75mg),Tablet,Elder Pharmaceuticals Ltd,Cardiovascular,2024-01,2026-01,Emergency Store,0,strip,2024-03-20,Sanjivani Drug House
B02555,LL25E280,Novotam 2mg Injection,Ondansetron (2mg/ml),Injection,Lupin Ltd,Gastro,2025-04,2027-04,Ward Store (Paeds),60,vial/amp,2025-07-11,Malabar Pharma Distributors
B02556,T2404-489,Stamlo 10 Tablet,Amlodipine (10mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2024-07,2026-01,Emergency Store,20,strip,2024-08-04,Sree Pharma Agencies
B02557,TMI247240,Cleofol 10mg Injection,Propofol (10mg),Injection,Themis Medicare Ltd,Anaesthesia/Critical care,2024-10,2027-10,Main Pharmacy,80,vial/amp,2025-01-29,Kerala Medical Supplies Co.
B02558,LLT242118,Telista AM 40mg/2.5mg Tablet,Telmisartan (40mg) + Amlodipine (2.5mg),Tablet,Lupin Ltd,Cardiovascular,2025-03,2026-09,Emergency Store,150,strip,2025-06-01,Kerala Medical Supplies Co.
B02559,16356704,Manilup 20% Infusion,Mannitol (20% w/v),Infusion,Lupin Ltd,Anaesthesia/Critical care,2024-07,2027-07,OPD Pharmacy,300,bottle,2024-08-09,Malabar Pharma Distributors
B02560,90561864,Domin Injection,Dopamine (40mg/ml),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-11,2027-11,Ward Store (Paeds),80,vial/amp,2024-11-27,Sanjivani Drug House
B02561,MLT258302,Azepress 250mg Tablet,Azithromycin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2025-03,2028-03,OT Store,150,strip,2025-06-02,Sanjivani Drug House
B02562,AI245106,Bupizuva 2.5mg Injection,Bupivacaine (2.5mg/ml),Injection,Abbott,Anaesthesia/Critical care,2024-06,2027-06,Main Pharmacy,300,vial/amp,2024-08-05,Kerala Medical Supplies Co.
B02563,TPT243953,Conpres 12.5mg Tablet,Carvedilol (12.5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,Ward Store (Paeds),150,strip,2025-01-12,Sanjivani Drug House
B02564,T2505-299,Tprim Forte 800mg/160mg Tablet,Sulfamethoxazole (800mg) + Trimethoprim (160mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2025-02,2027-02,Ward Store (Paeds),80,strip,2025-04-07,Apollo Wholesale Pvt Ltd
B02565,22195959,Hepatag 25000IU Injection,Heparin (25000IU),Injection,Ikon Remedies Pvt Ltd,Anticoagulant,2025-02,2028-02,OPD Pharmacy,200,vial/amp,2025-04-25,Sree Pharma Agencies
B02566,96385345,Omnisec 20mg Tablet,Rabeprazole (20mg),Tablet,Cipla Ltd,Gastro,2024-06,2027-06,Emergency Store,50,strip,2024-08-01,Sanjivani Drug House
B02567,MPT259040,Amlogift 5mg Tablet,Amlodipine (5mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2025-02,2026-08,Main Pharmacy,80,strip,2025-05-01,Malabar Pharma Distributors
B02568,SP24H187,Montek LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Sun Pharmaceutical Industries Ltd,Respiratory,2025-01,2026-07,OT Store,40,bottle,2025-02-20,"Medline Distributors, Thiruvananthapuram"
B02569,BI25C012,Electrolyte M 5% Infusion,Dextrose (5% w/v),Infusion,Baxter India Pvt Ltd,IV Fluids,2025-03,2027-03,Emergency Store,50,bottle,2025-04-19,Kerala Medical Supplies Co.
B02570,MPT252880,Atorvakind 20mg Tablet,Atorvastatin (20mg),Tablet,Mankind Pharma Ltd,Cardiovascular,2024-08,2026-08,ICU Store,80,strip,2024-09-04,Malabar Pharma Distributors
B02571,DR24J483,Cetzine Syrup,Cetirizine (5mg/5ml),Syrup,Dr Reddy's Laboratories Ltd,Respiratory,2024-09,2027-09,ICU Store,300,bottle,2024-12-21,Malabar Pharma Distributors
B02572,CLX252297,Tobamist Respules,Tobramycin (300mg),Respules,Cipla Ltd,Ophthalmology,2024-01,2027-01,Ward Store (Paeds),150,respule,2024-02-04,Sanjivani Drug House
B02573,TPX241337,Xtrapred 0.25% Drop,Prednisolone (0.25%),Drops,Torrent Pharmaceuticals Ltd,Steroid,2024-12,2026-06,OPD Pharmacy,300,bottle,2025-01-09,Kerala Medical Supplies Co.
B02574,46871774,Dermikem Dusting Powder,Clotrimazole (1% w/w),Powder,Alkem Laboratories Ltd,Antifungal,2024-11,2027-11,ICU Store,150,pack,2025-02-27,"Medline Distributors, Thiruvananthapuram"
B02575,WPT251629,Lubrijoint 500 Tablet,Glucosamine Sulfate Potassium Chloride (500mg),Tablet,Wallace Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2025-05,2027-05,Emergency Store,150,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B02576,ZL24K337,Aldex 6mg Tablet SR,Dexchlorpheniramine (6mg),Tablet,Zee Laboratories,Anti-allergic,2024-01,2027-01,OT Store,100,strip,2024-04-17,Malabar Pharma Distributors
B02577,82015813,Cydoxan 500mg Injection,Cyclophosphamide (500mg),Injection,Alkem Laboratories Ltd,Oncology,2025-04,2026-10,OPD Pharmacy,20,vial/amp,2025-06-26,Kerala Medical Supplies Co.
B02578,SP24G575,Trapic 100mg Injection,Tranexamic Acid (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2025-03,2028-03,Main Pharmacy,300,vial/amp,2025-05-04,"Medline Distributors, Thiruvananthapuram"
B02579,95863598,Salbair Resp 5mg Solution,Salbutamol (5mg),Solution,Lupin Ltd,Respiratory,2024-02,2026-02,Main Pharmacy,200,bottle,2024-05-12,"Medline Distributors, Thiruvananthapuram"
B02580,56753777,Solonex DT Tablet,Isoniazid (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Anti-TB,2024-06,2025-12,Ward Store (Paeds),200,strip,2024-09-25,Sanjivani Drug House
B02581,IP24L605,Ceprozone S 1000mg/500mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,Emergency Store,80,vial/amp,2025-01-04,Sree Pharma Agencies
B02582,MLT242612,Ciptab 250mg Tablet,Ciprofloxacin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2024-01,2027-01,Ward Store (Paeds),100,strip,2024-03-13,Sanjivani Drug House
B02583,16904975,Omez 20mg Capsule,Omeprazole (20mg),Capsule,Ridgecure Pharma,Gastro,2024-07,2026-07,ICU Store,120,strip,2024-08-31,Kerala Medical Supplies Co.
B02584,V2409-663,Normal Saline 0.9% Infusion,Sodium Chloride (0.9% w/v),Infusion,Alkem Laboratories Ltd,IV Fluids,2024-11,2027-11,OPD Pharmacy,120,bottle,2025-01-01,Malabar Pharma Distributors
B02585,CL25D263,S Citadep 10 Tablet,Escitalopram Oxalate (10mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-12,2027-12,Emergency Store,150,strip,2025-03-10,Sanjivani Drug House
B02586,CP25H949,Humanext N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Cadila Pharmaceuticals Ltd,Diabetes,2025-04,2026-10,Ward Store (Paeds),80,vial/amp,2025-07-10,Sree Pharma Agencies
B02587,49238480,Pansec 40mg Infusion,Pantoprazole (40mg),Infusion,Cipla Ltd,Gastro,2024-02,2026-02,Main Pharmacy,300,bottle,2024-05-27,Kerala Medical Supplies Co.
B02588,MP25J935,Labetamac Tablet,Labetalol (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Cardiovascular,2024-08,2026-08,OT Store,20,strip,2024-10-29,Malabar Pharma Distributors
B02589,IRI243502,Vancobest 500mg Injection,Vancomycin (500mg),Injection,Ikon Remedies Pvt Ltd,Antibiotic,2024-12,2026-06,OPD Pharmacy,120,vial/amp,2025-02-26,"Medline Distributors, Thiruvananthapuram"
B02590,SPT248610,Bestocef 100mg Tablet,Cefixime (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-07,2026-01,Emergency Store,150,strip,2024-09-01,Apollo Wholesale Pvt Ltd
B02591,T2502-256,Linospan 100 DT Tablet,Linezolid (100mg),Tablet,Cipla Ltd,Antibiotic,2024-01,2026-01,ICU Store,40,strip,2024-04-04,Sanjivani Drug House
B02592,CLT248769,Imulast 200mg Tablet,Hydroxychloroquine (200mg),Tablet,Cipla Ltd,Antimalarial,2024-11,2026-11,ICU Store,0,strip,2024-11-27,Apollo Wholesale Pvt Ltd
B02593,V2506-083,Aculife 25% Infusion,Dextrose (25% w/v),Infusion,Nirlife Healthcare,IV Fluids,2025-02,2026-08,Main Pharmacy,100,bottle,2025-03-09,Malabar Pharma Distributors
B02594,39870720,Folitrax 10 Tablet,Methotrexate (10mg),Tablet,Ipca Laboratories Ltd,Oncology,2024-07,2026-01,OPD Pharmacy,150,strip,2024-10-29,Sree Pharma Agencies
B02595,MT403,Co-Trimoxazole Tablets IP,Sulfamethoxazole (400mg) + Trimethoprim (80mg),Tablet,Maxwell Life Science Pvt. Ltd.,Antibiotic,2024-01,2026-12,Main Pharmacy,30,strip,2024-03-12,"Medline Distributors, Thiruvananthapuram"
B02596,MPT248372,Ibrumac 200mg Tablet,Ibuprofen (200mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-05,2026-05,Main Pharmacy,10,strip,2024-08-06,Sanjivani Drug House
B02597,ML24D041,Salbid 2mg Tablet,Salbutamol (2mg),Tablet,Micro Labs Ltd,Respiratory,2024-07,2026-01,Emergency Store,150,strip,2024-09-29,"Medline Distributors, Thiruvananthapuram"
B02598,CLC252698,Racotil 100mg Capsule,Racecadotril (100mg),Capsule,Cipla Ltd,Gastro,2025-03,2027-03,Main Pharmacy,300,strip,2025-04-02,Malabar Pharma Distributors
B02599,IPI241700,Genox 5IU Injection,Oxytocin (5IU),Injection,Intas Pharmaceuticals Ltd,Obstetrics,2024-03,2027-03,Emergency Store,30,vial/amp,2024-06-27,Apollo Wholesale Pvt Ltd
B02600,ZC25B839,Linid Tablet,Linezolid (600mg),Tablet,Zydus Cadila,Antibiotic,2024-03,2025-09,Ward Store (Paeds),50,strip,2024-06-21,Kerala Medical Supplies Co.
B02601,NIT253049,Tegretol 100mg Tablet,Carbamazepine (100mg),Tablet,Novartis India Ltd,Neurology/Psychiatry,2024-10,2026-10,Emergency Store,60,strip,2024-12-31,Sanjivani Drug House
B02602,SPT244660,Doxy Plus 100mg Tablet,Doxycycline (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-06,2027-06,OT Store,40,strip,2024-09-18,"Medline Distributors, Thiruvananthapuram"
B02603,ZC24G164,Klinz 150mg Injection,Clindamycin (150mg),Injection,Zydus Cadila,Antibiotic,2025-02,2027-02,OT Store,40,vial/amp,2025-04-03,Malabar Pharma Distributors
B02604,38943676,Gerzone 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Zydus Cadila,Antibiotic,2025-02,2026-08,OPD Pharmacy,150,vial/amp,2025-05-24,Malabar Pharma Distributors
B02605,T2406-737,Atorniz 10mg Tablet,Atorvastatin (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-01,2027-01,OPD Pharmacy,100,strip,2024-04-04,Kerala Medical Supplies Co.
B02606,97630141,Nftor 100mg Tablet,Nitrofurantoin (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2025-04,2027-04,OT Store,10,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B02607,MP25C489,Metrocare 500mg Infusion,Metronidazole (500mg),Infusion,Mankind Pharma Ltd,Antibiotic,2025-01,2028-01,ICU Store,80,bottle,2025-04-28,"Medline Distributors, Thiruvananthapuram"
B02608,60028002,Vancobest 500mg Injection,Vancomycin (500mg),Injection,Ikon Remedies Pvt Ltd,Antibiotic,2024-07,2026-01,Main Pharmacy,200,vial/amp,2024-10-03,Apollo Wholesale Pvt Ltd
B02609,S2408-431,Histanil Syrup,Chlorpheniramine Maleate (NA),Syrup,Troikaa Pharmaceuticals Ltd,Anti-allergic,2024-04,2027-04,Emergency Store,40,bottle,2024-06-26,Sree Pharma Agencies
B02610,24787933,Aerozest 0.31mg Respules (2.5 ml each),Levosalbutamol (0.31mg),Respules,Macleods Pharmaceuticals Pvt Ltd,Respiratory,2024-12,2027-12,OT Store,300,respule,2025-01-16,Apollo Wholesale Pvt Ltd
B02611,SPX251615,Bectodine 5% Ointment,Povidone Iodine (5% w/w),Ointment,Sun Pharmaceutical Industries Ltd,Dermatology,2024-07,2026-01,Ward Store (Paeds),120,tube,2024-09-28,"Medline Distributors, Thiruvananthapuram"
B02612,CL25C993,Linospan 100 DT Tablet,Linezolid (100mg),Tablet,Cipla Ltd,Antibiotic,2024-02,2027-02,Ward Store (Paeds),80,strip,2024-04-14,Sree Pharma Agencies
B02613,LH24K637,Weldinide 200mcg Inhaler,Budesonide (200mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-12,2027-12,Ward Store (Paeds),60,inhaler,2025-03-05,Kerala Medical Supplies Co.
B02614,CLT251674,Tachyra 100 Tablet,Amiodarone (100mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2026-09,Ward Store (Paeds),200,strip,2025-04-12,"Medline Distributors, Thiruvananthapuram"
B02615,MPS251855,Brutacef 100mg Dry Syrup,Cefixime (100mg),Syrup,Mankind Pharma Ltd,Antibiotic,2024-10,2027-10,Ward Store (Paeds),50,bottle,2024-10-26,Sree Pharma Agencies
B02616,A24M598,AB-Rozu 10 Tablet,Rosuvastatin (10mg),Tablet,Abbott,Cardiovascular,2024-03,2026-03,Main Pharmacy,200,strip,2024-03-28,"Medline Distributors, Thiruvananthapuram"
B02617,45575298,Azithral 250mg DT Tablet,Azithromycin (250mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-03,2027-03,OT Store,120,strip,2024-06-01,Sree Pharma Agencies
B02618,ULT256074,Glycomet 250 Tablet,Metformin (250mg),Tablet,USV Ltd,Diabetes,2024-12,2027-12,OPD Pharmacy,50,strip,2024-12-31,Malabar Pharma Distributors
B02619,I2412-950,Glaritus 100IU/ml Injection,Insulin Glargine (100IU),Injection,Wockhardt Ltd,Diabetes,2024-06,2027-06,Emergency Store,40,vial/amp,2024-06-26,Apollo Wholesale Pvt Ltd
B02620,PLT241565,Medrol 16mg Tablet,Methylprednisolone (16mg),Tablet,Pfizer Ltd,Steroid,2024-05,2026-05,OPD Pharmacy,120,strip,2024-08-17,Sanjivani Drug House
B02621,T2509-799,CEPOCOR 100MG TABLET,Cefpodoxime Proxetil (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2027-03,Emergency Store,60,strip,2024-05-14,Kerala Medical Supplies Co.
B02622,AL24A711,Drotanic Injection,Drotaverine (20mg),Injection,Alkem Laboratories Ltd,Gastro,2024-06,2026-06,ICU Store,10,vial/amp,2024-08-19,Malabar Pharma Distributors
B02623,23498489,Lupin 10 Rheza Tablet,Rosuvastatin (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-05,2025-11,Emergency Store,120,strip,2024-07-16,Kerala Medical Supplies Co.
B02624,T2401-596,Allerkast LC Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Lupin Ltd,Respiratory,2025-04,2027-04,Emergency Store,80,strip,2025-05-24,"Medline Distributors, Thiruvananthapuram"
B02625,ZCT242170,Cadifix 100mg Tablet DT,Cefixime (100mg),Tablet,Zydus Cadila,Antibiotic,2024-12,2026-12,Emergency Store,60,strip,2025-01-13,Malabar Pharma Distributors
B02626,GD24L-27H,K Pan-IV Injection,Pantoprazole (40mg),Injection,Vellinton Healthcare,Gastro,2024-12,2026-11,Ward Store (Paeds),60,vial/amp,2024-12-29,Sanjivani Drug House
B02627,MLT250485,Diapride M 0.5mg/500mg Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Micro Labs Ltd,Diabetes,2024-04,2025-10,OPD Pharmacy,10,strip,2024-05-02,Sanjivani Drug House
B02628,PL24M609,Solu-Medrol 1gm Injection,Methylprednisolone (1000mg),Injection,Pfizer Ltd,Steroid,2024-07,2026-01,Main Pharmacy,200,vial/amp,2024-07-31,Kerala Medical Supplies Co.
B02629,62038466,Cofarin 1mg Tablet,Warfarin (1mg),Tablet,East West Pharma,Anticoagulant,2024-01,2026-01,ICU Store,60,strip,2024-04-16,Apollo Wholesale Pvt Ltd
B02630,42152047,Drotanic Injection,Drotaverine (20mg),Injection,Alkem Laboratories Ltd,Gastro,2024-02,2026-02,ICU Store,300,vial/amp,2024-03-05,Sree Pharma Agencies
B02631,TPT248797,Uniwarfin 1mg Tablet,Warfarin (1mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2024-07,2026-01,Emergency Store,40,strip,2024-09-05,Sanjivani Drug House
B02632,24460967,Taxim-O 200 Tablet,Cefixime (200mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-07,2026-06,Main Pharmacy,80,strip,2024-10-10,"Medline Distributors, Thiruvananthapuram"
B02633,IPT259555,Daparyl 10 Tablet,Dapagliflozin (10mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2025-02,2027-02,Main Pharmacy,30,strip,2025-05-07,Kerala Medical Supplies Co.
B02634,T2411-628,Lopez 1mg Tablet,Lorazepam (1mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-08,2027-08,ICU Store,40,strip,2024-10-15,Kerala Medical Supplies Co.
B02635,LLT250217,Rabifit 20mg Tablet,Rabeprazole (20mg),Tablet,Lupin Ltd,Gastro,2024-10,2026-04,Main Pharmacy,200,strip,2024-12-09,Sanjivani Drug House
B02636,46855423,Endogest 100 Capsule,Progesterone (Natural Micronized) (100mg),Capsule,Cipla Ltd,Obstetrics,2025-03,2026-09,OPD Pharmacy,300,strip,2025-03-27,Sree Pharma Agencies
B02637,90296988,Duphalac Bulk Oral Solution Lemon,Lactulose (10gm),Oral Solution,Abbott,Gastro,2025-03,2027-03,Emergency Store,150,bottle,2025-04-08,Apollo Wholesale Pvt Ltd
B02638,IPI252745,Prexaron 250mg Injection,Citicoline (250mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2025-11,OPD Pharmacy,60,vial/amp,2024-07-23,Sanjivani Drug House
B02639,14214307,Redotrex 500 Tablet,Tranexamic Acid (500mg),Tablet,Leeford Healthcare Ltd,Haematology,2025-01,2027-01,OPD Pharmacy,60,strip,2025-02-15,Apollo Wholesale Pvt Ltd
B02640,MLT246713,Diapride 1 Tablet,Glimepiride (1mg),Tablet,Micro Labs Ltd,Diabetes,2024-02,2027-02,Ward Store (Paeds),200,strip,2024-05-09,Sanjivani Drug House
B02641,GPT241549,Frusenex 100 Tablet,Furosemide (100mg),Tablet,Geno Pharmaceuticals Ltd,Cardiovascular,2024-03,2027-03,ICU Store,20,strip,2024-05-02,Sree Pharma Agencies
B02642,EP24G909,Pause 1000mg Tablet,Tranexamic Acid (1000mg),Tablet,Emcure Pharmaceuticals Ltd,Haematology,2025-04,2026-10,Main Pharmacy,300,strip,2025-07-15,"Medline Distributors, Thiruvananthapuram"
B02643,T2504-723,Genmox CV 500 mg/125 mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Cadila Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,Ward Store (Paeds),20,strip,2025-07-15,Malabar Pharma Distributors
B02644,22315737,Azento 250mg Tablet,Azithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-01,2026-01,Emergency Store,120,strip,2024-02-17,Sree Pharma Agencies
B02645,PL24J654,Wysolone 10 Tablet DT,Prednisolone (10mg),Tablet,Pfizer Ltd,Steroid,2024-12,2026-06,OT Store,120,strip,2025-03-28,Sree Pharma Agencies
B02646,78824758,Emty Oral Solution,Lactulose (10gm),Oral Solution,Alkem Laboratories Ltd,Gastro,2024-12,2026-06,ICU Store,80,bottle,2025-03-13,Sree Pharma Agencies
B02647,13412336,Clocip Cream,Clotrimazole (1% w/w),Cream,Cipla Ltd,Antifungal,2024-08,2026-02,Ward Store (Paeds),200,tube,2024-10-21,Sree Pharma Agencies
B02648,23922336,Levtam 100mg Syrup,Levetiracetam (100mg),Syrup,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2026-07,ICU Store,0,bottle,2024-03-17,Sanjivani Drug House
B02649,I2508-391,Solu-Medrol 1gm Injection,Methylprednisolone (1000mg),Injection,Pfizer Ltd,Steroid,2024-05,2026-05,Main Pharmacy,150,vial/amp,2024-07-15,Apollo Wholesale Pvt Ltd
B02650,APT253777,Osteofit-HD Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Alembic Pharmaceuticals Ltd,Supplement,2024-03,2025-09,Ward Store (Paeds),50,strip,2024-05-04,Malabar Pharma Distributors
B02651,72821834,Neurobion RF Forte Injection,Methylcobalamin (1000mcg) + Vitamin B6 (Pyridoxine) (100mg),Injection,Procter & Gamble Hygiene and Health Care Ltd,Supplement,2024-11,2027-11,ICU Store,0,vial/amp,2025-02-15,Sanjivani Drug House
B02652,IPC244839,Histacet 10mg Capsule,Cetirizine (10mg),Capsule,Intas Pharmaceuticals Ltd,Respiratory,2024-11,2026-11,Main Pharmacy,200,strip,2025-01-14,Sanjivani Drug House
B02653,T2409-956,Phensedyl LM Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Abbott,Respiratory,2024-07,2027-07,Ward Store (Paeds),20,strip,2024-08-12,Sree Pharma Agencies
B02654,T2511-048,Noplaq 75mg Tablet,Clopidogrel (75mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-01,2025-12,Main Pharmacy,30,strip,2024-03-11,Malabar Pharma Distributors
B02655,IP25K615,Valprol 100mg Injection,Sodium Valproate (100mg),Injection,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2026-06,Main Pharmacy,40,vial/amp,2024-09-10,"Medline Distributors, Thiruvananthapuram"
B02656,S2510-936,Lastuss LA Syrup,Dextromethorphan Hydrobromide (15mg/5ml),Syrup,FDC Ltd,Respiratory,2024-08,2027-08,OT Store,100,bottle,2024-11-24,"Medline Distributors, Thiruvananthapuram"
B02657,47766210,Montek LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Sun Pharmaceutical Industries Ltd,Respiratory,2024-08,2027-08,Emergency Store,200,bottle,2024-09-22,Malabar Pharma Distributors
B02658,AL24J917,Swich 100 DT Tablet,Cefpodoxime Proxetil (100mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-01,2026-02,Main Pharmacy,20,strip,2024-03-19,Sree Pharma Agencies
B02659,T2509-034,Serenace 0.5 Tablet,Haloperidol (0.5mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-01,2027-01,OT Store,50,strip,2024-03-30,Malabar Pharma Distributors
B02660,T2504-423,Epsolin 100 Tablet,Phenytoin (100mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2024-05,2026-05,OPD Pharmacy,100,strip,2024-08-16,Sree Pharma Agencies
B02661,CL25G612,Raniciz Junior Syrup,Ranitidine (75mg/5ml),Syrup,Cipla Ltd,Gastro,2024-05,2026-05,OT Store,60,bottle,2024-06-22,Sree Pharma Agencies
B02662,15602379,Revidox 100mg Tablet,Doxycycline (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-09,2027-09,OT Store,0,strip,2024-10-09,Sanjivani Drug House
B02663,EW25B089,Caxin 0.25mg Tablet,Digoxin (0.25mg),Tablet,East West Pharma,Cardiovascular,2024-06,2025-12,Ward Store (Paeds),300,strip,2024-09-06,Kerala Medical Supplies Co.
B02664,I2411-850,Atrowok 0.6mg Injection,Atropine (0.6mg),Injection,Wockhardt Ltd,Anaesthesia/Critical care,2024-11,2027-11,ICU Store,40,vial/amp,2025-02-17,Sree Pharma Agencies
B02665,96434410,Cefbact 1000mg Injection,Ceftriaxone (1000mg),Injection,Cipla Ltd,Antibiotic,2025-02,2027-02,Ward Store (Paeds),60,vial/amp,2025-04-10,Malabar Pharma Distributors
B02666,57937270,Demisone 4mg Injection,Dexamethasone (4mg),Injection,Cadila Pharmaceuticals Ltd,Steroid,2024-11,2026-11,ICU Store,100,vial/amp,2025-01-19,Kerala Medical Supplies Co.
B02667,MPX256635,Bunase 0.5 Respules,Budesonide (0.5mg),Respules,Macleods Pharmaceuticals Pvt Ltd,Respiratory,2024-02,2026-02,Ward Store (Paeds),120,respule,2024-03-15,Malabar Pharma Distributors
B02668,SPI246752,Trapic 100mg Injection,Tranexamic Acid (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2024-09,2027-09,OT Store,80,vial/amp,2024-11-26,"Medline Distributors, Thiruvananthapuram"
B02669,T2407-483,Phensedyl LM Tablet,Levocetirizine (5mg) + Montelukast (10mg),Tablet,Abbott,Respiratory,2024-10,2027-10,OT Store,120,strip,2024-11-21,Sree Pharma Agencies
B02670,91228073,Levexx 100mg Injection,Levetiracetam (100mg),Injection,Zydus Cadila,Neurology/Psychiatry,2024-04,2026-04,Emergency Store,30,vial/amp,2024-05-05,"Medline Distributors, Thiruvananthapuram"
B02671,NLI240872,Keparin 25000IU Injection,Heparin (25000IU),Injection,Neon Laboratories Ltd,Anticoagulant,2024-03,2025-09,OT Store,100,vial/amp,2024-04-10,Sanjivani Drug House
B02672,I2403-345,Xylocaine 2% Injection,Lidocaine (2%),Injection,Zydus Cadila,Other,2024-07,2026-07,Emergency Store,80,vial/amp,2024-08-05,Malabar Pharma Distributors
B02673,TP25L434,Deplatt A 150 Tablet,Aspirin (150mg) + Clopidogrel (75mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-04,2028-04,Main Pharmacy,80,strip,2025-06-13,Malabar Pharma Distributors
B02674,88111625,Losalife 25mg Tablet,Losartan (25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-04,2027-04,Main Pharmacy,40,strip,2024-05-26,"Medline Distributors, Thiruvananthapuram"
B02675,T2512-297,Atorstat 10mg Tablet,Atorvastatin (10mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2025-03,2027-03,OT Store,10,strip,2025-04-01,Malabar Pharma Distributors
B02676,CL24E025,Metrocip 500mg Infusion,Metronidazole (500mg),Infusion,Cipla Ltd,Antibiotic,2024-11,2026-11,OPD Pharmacy,0,bottle,2025-01-23,Kerala Medical Supplies Co.
B02677,TPX246649,Mofee Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Torrent Pharmaceuticals Ltd,Ophthalmology,2024-06,2025-12,OPD Pharmacy,20,bottle,2024-07-02,Sree Pharma Agencies
B02678,T2401-357,Apixator 2.5 Tablet,Apixaban (2.5mg),Tablet,Torrent Pharmaceuticals Ltd,Anticoagulant,2025-04,2027-04,OPD Pharmacy,200,strip,2025-05-21,Sanjivani Drug House
B02679,ULT242300,Ecosprin 75 Tablet,Aspirin (75mg),Tablet,USV Ltd,Cardiovascular,2025-04,2028-04,Main Pharmacy,10,strip,2025-05-29,Malabar Pharma Distributors
B02680,NIT255527,Galvus Met 50mg/850mg Tablet,Metformin (850mg) + Vildagliptin (50mg),Tablet,Novartis India Ltd,Diabetes,2024-12,2026-12,Emergency Store,10,strip,2025-03-08,"Medline Distributors, Thiruvananthapuram"
B02681,52886482,Emsetron 2mg Injection,Ondansetron (2mg),Injection,Sun Pharmaceutical Industries Ltd,Gastro,2025-04,2027-04,OPD Pharmacy,80,vial/amp,2025-05-27,Sree Pharma Agencies
B02682,CL25A231,Alergin 10mg Tablet,Cetirizine (10mg),Tablet,Cipla Ltd,Respiratory,2025-01,2027-01,OT Store,100,strip,2025-03-16,"Medline Distributors, Thiruvananthapuram"
B02683,93424048,Cipcal-XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cipla Ltd,Supplement,2024-09,2027-09,Main Pharmacy,10,strip,2024-12-16,Apollo Wholesale Pvt Ltd
B02684,AI256243,Nuavomin 2mg Injection,Ondansetron (2mg),Injection,Abbott,Gastro,2024-10,2026-10,OT Store,60,vial/amp,2024-11-26,Malabar Pharma Distributors
B02685,CL25L978,Etozox 120mg Tablet,Etoricoxib (120mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-10,2027-10,ICU Store,150,strip,2024-12-08,Malabar Pharma Distributors
B02686,C2404-740,Cystina Capsule,Methylcobalamin (1500mcg),Capsule,Intas Pharmaceuticals Ltd,Supplement,2024-04,2025-10,OPD Pharmacy,20,strip,2024-07-10,"Medline Distributors, Thiruvananthapuram"
B02687,SPX252668,Silver Sulfadiazine Cream,Silver Sulfadiazine (NA),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2024-10,2026-10,OPD Pharmacy,50,tube,2024-11-13,Apollo Wholesale Pvt Ltd
B02688,X2504-538,Otrilom-S Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Fawn Incorporation,IV Fluids,2024-04,2026-04,Ward Store (Paeds),150,bottle,2024-06-07,Apollo Wholesale Pvt Ltd
B02689,IP25A306,Ibutas 200mg Tablet,Ibuprofen (200mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2026-05,Ward Store (Paeds),100,strip,2024-07-02,"Medline Distributors, Thiruvananthapuram"
B02690,CL24H500,Bendex 200mg Suspension,Albendazole (200mg),Suspension,Cipla Ltd,Anthelmintic,2025-04,2027-04,OPD Pharmacy,10,bottle,2025-05-09,"Medline Distributors, Thiruvananthapuram"
B02691,T2510-670,Valparin Alkalets 250mg Tablet,Sodium Valproate (250mg),Tablet,Sanofi India Ltd,Neurology/Psychiatry,2024-11,2027-11,ICU Store,100,strip,2024-12-05,Apollo Wholesale Pvt Ltd
B02692,JBT252373,Metrogyl 400 Tablet,Metronidazole (400mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Antibiotic,2024-03,2025-09,OT Store,80,strip,2024-06-24,Sanjivani Drug House
B02693,IPT244003,Arvast 10 Tablet,Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,Main Pharmacy,300,strip,2025-01-06,Sree Pharma Agencies
B02694,SI25C671,Apidra 100IU/ml Solution for Injection,Insulin Glulisine (100IU),Injection,Sanofi India Ltd,Diabetes,2024-11,2027-11,OPD Pharmacy,10,vial/amp,2024-11-27,Sree Pharma Agencies
B02695,45638114,Fusibact Cream,Fusidic Acid (2% w/w),Cream,Cipla Ltd,Dermatology,2024-04,2026-04,Ward Store (Paeds),120,tube,2024-05-29,Sanjivani Drug House
B02696,LLT245689,Lupipan 20mg Tablet,Pantoprazole (20mg),Tablet,Lupin Ltd,Gastro,2024-02,2025-08,OPD Pharmacy,10,strip,2024-05-15,Sanjivani Drug House
B02697,I2410-402,Human Fastact 40IU/ml Injection,Human insulin (40IU),Injection,USV Ltd,Diabetes,2024-11,2026-11,OPD Pharmacy,100,vial/amp,2024-12-17,Sree Pharma Agencies
B02698,T2504-560,Sitared XR Tablet,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-02,2025-08,Emergency Store,10,strip,2024-05-06,Sree Pharma Agencies
B02699,ML24C724,Dolo 650 Tablet,Paracetamol (650mg),Tablet,Micro Labs Ltd,Analgesic/Antipyretic,2025-04,2028-04,ICU Store,50,strip,2025-06-19,Sree Pharma Agencies
B02700,87449461,Monoloc 150mg Tablet,Ranitidine (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-05,2027-05,Ward Store (Paeds),100,strip,2024-08-05,Kerala Medical Supplies Co.
B02701,41887353,Zerodol Spas Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Ipca Laboratories Ltd,Gastro,2025-01,2028-01,OT Store,200,strip,2025-02-01,Kerala Medical Supplies Co.
B02702,LL24H337,Resner 500mcg Injection,Methylcobalamin (500mcg),Injection,Lupin Ltd,Supplement,2024-01,2026-01,Main Pharmacy,200,vial/amp,2024-04-18,"Medline Distributors, Thiruvananthapuram"
B02703,89162732,Fusys 150 Tablet,Fluconazole (150mg),Tablet,Zydus Cadila,Antifungal,2024-06,2027-06,OPD Pharmacy,120,strip,2024-08-03,Sanjivani Drug House
B02704,CLI249998,Viatran 1000 mg/500 mg Injection,Cefoperazone (1000mg) + Sulbactam (500mg),Injection,Cipla Ltd,Antibiotic,2024-05,2025-11,OPD Pharmacy,100,vial/amp,2024-06-17,"Medline Distributors, Thiruvananthapuram"
B02705,T2402-116,Sustameto 100mg Tablet,Metoprolol Succinate (100mg),Tablet,Zydus Cadila,Cardiovascular,2024-02,2027-02,Main Pharmacy,60,strip,2024-04-14,Sree Pharma Agencies
B02706,CBT248976,Cgglu 500 Tablet,Calcium Gluconate (500mg),Tablet,Cmg Biotech Pvt Ltd,Anaesthesia/Critical care,2025-02,2028-02,Ward Store (Paeds),120,strip,2025-03-22,"Medline Distributors, Thiruvananthapuram"
B02707,T2406-379,Teli 20 Tablet,Telmisartan (20mg),Tablet,Cadila Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-07,ICU Store,0,strip,2024-10-18,Kerala Medical Supplies Co.
B02708,T2509-779,Lupin 10 Rheza Tablet,Rosuvastatin (10mg),Tablet,Lupin Ltd,Cardiovascular,2025-01,2028-01,OT Store,60,strip,2025-02-19,Sanjivani Drug House
B02709,AP25F469,Supervac 10mg Injection,Vecuronium (10mg),Injection,Alembic Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-03,2027-03,OT Store,200,vial/amp,2024-04-17,"Medline Distributors, Thiruvananthapuram"
B02710,RB25M044,Megma NS 0.9% Infusion,Sodium Chloride (0.9% w/v),Infusion,Ridhima Biocare,IV Fluids,2024-11,2026-05,OT Store,50,bottle,2025-01-17,Kerala Medical Supplies Co.
B02711,TPT253478,Deviry 10mg Tablet,Medroxyprogesterone acetate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-08,2026-08,ICU Store,200,strip,2024-10-15,Sanjivani Drug House
B02712,23001760,Azitough 250mg Tablet,Azithromycin (250mg),Tablet,Abbott,Antibiotic,2025-01,2027-01,Ward Store (Paeds),300,strip,2025-02-03,Apollo Wholesale Pvt Ltd
B02713,SPX241946,Fendrop 25mcg Patch,Fentanyl (25mcg),Drops,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-06,2026-06,Emergency Store,60,bottle,2024-09-10,Malabar Pharma Distributors
B02714,TPT259935,Lezyncet 10 Tablet DT,Levocetirizine (10mg),Tablet,Torrent Pharmaceuticals Ltd,Respiratory,2025-02,2028-02,Ward Store (Paeds),30,strip,2025-03-24,Sree Pharma Agencies
B02715,X2406-979,Mupicip 2% Ointment,Mupirocin (2% w/w),Ointment,Cipla Ltd,Dermatology,2024-03,2026-03,ICU Store,50,tube,2024-05-02,"Medline Distributors, Thiruvananthapuram"
B02716,TP24G129,Domadol 100mg Injection,Tramadol (100mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-01,2028-01,Ward Store (Paeds),20,vial/amp,2025-01-27,Apollo Wholesale Pvt Ltd
B02717,ZCT257963,Epsolin 150mg Tablet ER,Phenytoin (150mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2025-05,2027-05,ICU Store,80,strip,2025-07-15,Kerala Medical Supplies Co.
B02718,ILT255357,Zerodol Spas Tablet,Drotaverine (80mg) + Aceclofenac (100mg),Tablet,Ipca Laboratories Ltd,Gastro,2024-04,2026-04,OT Store,200,strip,2024-05-30,Sanjivani Drug House
B02719,WL25F521,Phylobid 200mg Tablet,Theophylline (200mg),Tablet,Wockhardt Ltd,Respiratory,2024-02,2027-02,OT Store,100,strip,2024-05-21,Kerala Medical Supplies Co.
B02720,IR25F407,Ambrocon 7.5mg Oral Drops,Ambroxol (7.5mg),Drops,Ikon Remedies Pvt Ltd,Respiratory,2024-07,2027-07,OPD Pharmacy,100,bottle,2024-08-10,Sree Pharma Agencies
B02721,87340546,Lidoxin 0.25mg Tablet,Digoxin (0.25mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2025-01,2028-01,Emergency Store,60,strip,2025-04-28,Sree Pharma Agencies
B02722,TP24H110,Neotroy 0.5mg Injection,Neostigmine (0.5mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-01,2026-01,Emergency Store,100,vial/amp,2024-02-20,Apollo Wholesale Pvt Ltd
B02723,52796441,Flucomet Eye Drop,Fluconazole (0.3% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Antifungal,2025-01,2028-01,OPD Pharmacy,10,bottle,2025-04-17,Apollo Wholesale Pvt Ltd
B02724,MLT247560,Metapro -XL 25 Tablet,Metoprolol Succinate (23.75mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-10,2027-10,ICU Store,150,strip,2025-01-17,Sanjivani Drug House
B02725,T2412-100,Telday 20 Tablet,Telmisartan (20mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-02,2027-02,Main Pharmacy,120,strip,2024-05-16,Malabar Pharma Distributors
B02726,IPT250483,Nuzide 80mg Tablet,Gliclazide (80mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-10,2027-10,Main Pharmacy,200,strip,2024-12-22,Sanjivani Drug House
B02727,LL24C431,Lupimectin 12mg Tablet,Ivermectin (12mg),Tablet,Lupin Ltd,Anthelmintic,2024-11,2027-11,OPD Pharmacy,80,strip,2025-01-05,Malabar Pharma Distributors
B02728,ML25A861,Fluza 150mg Tablet,Fluconazole (150mg),Tablet,Micro Labs Ltd,Antifungal,2024-02,2027-02,Emergency Store,0,strip,2024-05-03,Kerala Medical Supplies Co.
B02729,PLI253553,Magnex 2gm Injection,Cefoperazone (1000mg) + Sulbactam (1000mg),Injection,Pfizer Ltd,Antibiotic,2025-03,2026-09,Emergency Store,60,vial/amp,2025-06-07,Malabar Pharma Distributors
B02730,SPT254716,Afenak Plus MR Tablet,Aceclofenac (NA) + Paracetamol (NA),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-12,2026-12,OT Store,10,strip,2025-01-20,Kerala Medical Supplies Co.
B02731,AL24K674,Ceriz 5mg Syrup,Cetirizine (5mg/ml),Syrup,Alkem Laboratories Ltd,Respiratory,2024-02,2027-02,Main Pharmacy,60,bottle,2024-03-20,"Medline Distributors, Thiruvananthapuram"
B02732,20892939,Rabemed 10mg Tablet,Rabeprazole (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-02,2026-02,Main Pharmacy,50,strip,2024-04-18,Apollo Wholesale Pvt Ltd
B02733,TP24K106,Trofentyl 50mcg Injection,Fentanyl (50mcg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-05,2025-11,OT Store,100,vial/amp,2024-06-05,Sree Pharma Agencies
B02734,36018096,Thyrocip 100 Tablet,Thyroxine (100mcg),Tablet,Cipla Ltd,Endocrine,2024-04,2026-04,Main Pharmacy,0,strip,2024-07-13,Kerala Medical Supplies Co.
B02735,CL24D799,Clocip Cream,Clotrimazole (1% w/w),Cream,Cipla Ltd,Antifungal,2025-01,2028-01,Main Pharmacy,120,tube,2025-03-15,"Medline Distributors, Thiruvananthapuram"
B02736,33431904,Omesec 20 Capsule,Omeprazole (20mg),Capsule,Sun Pharmaceutical Industries Ltd,Gastro,2024-02,2025-08,Main Pharmacy,10,strip,2024-02-27,Malabar Pharma Distributors
B02737,AL24H654,Azento 250mg Tablet,Azithromycin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-10,2027-10,OT Store,10,strip,2024-10-26,"Medline Distributors, Thiruvananthapuram"
B02738,I2510-497,Instavil 22.75mg Injection,Pheniramine (22.75mg),Injection,Intas Pharmaceuticals Ltd,Anti-allergic,2024-10,2027-10,OPD Pharmacy,80,vial/amp,2025-01-07,Kerala Medical Supplies Co.
B02739,41680907,ESGIPYRIN DS INJECTION,Diclofenac (25mg/ml),Injection,Abbott,Analgesic/Antipyretic,2025-02,2028-02,Ward Store (Paeds),120,vial/amp,2025-03-12,Sanjivani Drug House
B02740,AI252655,Sensorcaine 0.25% Injection,Bupivacaine (0.25%),Injection,AstraZeneca,Anaesthesia/Critical care,2025-01,2027-01,Main Pharmacy,10,vial/amp,2025-04-29,Malabar Pharma Distributors
B02741,LL25B671,Clinlup 1% Gel,Clindamycin (1%),Gel,Lupin Ltd,Antibiotic,2025-04,2028-04,OT Store,20,tube,2025-05-25,Sree Pharma Agencies
B02742,SPX242147,Milflox 0.5% Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2024-12,2026-12,OT Store,120,bottle,2025-02-15,Sanjivani Drug House
B02743,CLT245725,Cosart 25 Tablet,Losartan (25mg),Tablet,Cipla Ltd,Cardiovascular,2024-07,2027-07,Ward Store (Paeds),120,strip,2024-10-01,Kerala Medical Supplies Co.
B02744,AL25M275,Formin PG 1 Forte Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Alkem Laboratories Ltd,Diabetes,2025-02,2028-02,OPD Pharmacy,100,strip,2025-04-09,Sanjivani Drug House
B02745,41649234,Serenace 10 Tablet,Haloperidol (10mg),Tablet,RPG Life Sciences Ltd,Neurology/Psychiatry,2024-10,2026-10,OT Store,60,strip,2025-01-05,Sree Pharma Agencies
B02746,47580770,Rosuvas F 10 Tablet,Fenofibrate (160mg) + Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-09,2026-09,Main Pharmacy,0,strip,2024-09-26,Apollo Wholesale Pvt Ltd
B02747,ALT250797,Alert L 5mg Tablet,Levocetirizine (5mg),Tablet,Alkem Laboratories Ltd,Respiratory,2024-07,2027-07,Main Pharmacy,20,strip,2024-10-10,Malabar Pharma Distributors
B02748,GP25E219,Telma 40 Tablet,Telmisartan (40mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-10,2026-04,ICU Store,200,strip,2025-01-19,Sree Pharma Agencies
B02749,I2404-498,Keparin 25000IU Injection,Heparin (25000IU),Injection,Neon Laboratories Ltd,Anticoagulant,2024-08,2027-08,OPD Pharmacy,150,vial/amp,2024-09-26,Apollo Wholesale Pvt Ltd
B02750,T2502-877,Maxfor 1000mg Tablet SR,Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2025-05,2027-05,ICU Store,30,strip,2025-07-15,Sanjivani Drug House
B02751,T2408-673,Sodinate 1GM Tablet,Sodium Bicarbonate (1000mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2025-04,2028-04,ICU Store,200,strip,2025-05-24,"Medline Distributors, Thiruvananthapuram"
B02752,X2406-256,Rashcare Cream,Zinc Oxide (8.5% w/w),Cream,Leeford Healthcare Ltd,Supplement,2024-01,2027-01,OPD Pharmacy,0,tube,2024-04-11,Sree Pharma Agencies
B02753,T2505-513,Thyronorm 12.5mcg Tablet,Thyroxine (12.5mcg),Tablet,Abbott,Endocrine,2025-01,2028-01,OT Store,80,strip,2025-04-05,"Medline Distributors, Thiruvananthapuram"
B02754,I2503-144,Cefuroxime Sodium 750mg Injection,Cefuroxime (750mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-02,2028-02,OT Store,200,vial/amp,2025-04-12,"Medline Distributors, Thiruvananthapuram"
B02755,A25E890,Thyronorm 100mcg Tablet,Thyroxine (100mcg),Tablet,Abbott,Endocrine,2024-09,2027-09,ICU Store,60,strip,2024-12-10,Sanjivani Drug House
B02756,X2405-931,Weldinide 200mcg Inhaler,Budesonide (200mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2025-05,2027-05,Emergency Store,50,inhaler,2025-05-27,Malabar Pharma Distributors
B02757,73288596,Dibeta SR 1gm Tablet,Metformin (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-11,2026-11,OT Store,20,strip,2025-01-27,"Medline Distributors, Thiruvananthapuram"
B02758,AT249746,Flagyl ER Tablet,Metronidazole (600mg),Tablet,Abbott,Antibiotic,2024-08,2027-08,Ward Store (Paeds),50,strip,2024-10-28,Kerala Medical Supplies Co.
B02759,LLT240224,Atenova 100mg Tablet,Atenolol (100mg),Tablet,Lupin Ltd,Cardiovascular,2024-06,2026-06,Ward Store (Paeds),200,strip,2024-07-24,Kerala Medical Supplies Co.
B02760,T2511-984,Ultracet Semi Tablet,Paracetamol/Acetaminophen (162.5mg) + Tramadol (18.75mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2024-12,2026-12,ICU Store,150,strip,2025-02-26,Sree Pharma Agencies
B02761,V2412-185,Dextrose 25% Infusion,Dextrose (25% w/v),Infusion,Claris Lifesciences Ltd,IV Fluids,2024-11,2026-11,OPD Pharmacy,200,bottle,2025-02-07,Apollo Wholesale Pvt Ltd
B02762,V2410-753,Flagyl 0.5% Solution for Infusion,Metronidazole (500mg),Infusion,Abbott,Antibiotic,2024-06,2026-06,Main Pharmacy,20,bottle,2024-08-07,Kerala Medical Supplies Co.
B02763,SPT240862,Rokamide 2mg Tablet,Loperamide (2mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2024-03,2025-09,Ward Store (Paeds),10,strip,2024-06-27,Apollo Wholesale Pvt Ltd
B02764,I2511-616,Divon 25mg Injection,Diclofenac (25mg),Injection,Micro Labs Ltd,Analgesic/Antipyretic,2025-05,2027-05,OPD Pharmacy,60,vial/amp,2025-06-25,"Medline Distributors, Thiruvananthapuram"
B02765,64695425,Diaryl 1mg Tablet,Glimepiride (1mg),Tablet,Cipla Ltd,Diabetes,2024-05,2026-05,Main Pharmacy,80,strip,2024-06-09,Sanjivani Drug House
B02766,ALT249244,Alsita M 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-11,2026-05,OT Store,150,strip,2025-02-01,Sanjivani Drug House
B02767,69816708,Formin PG 1 Forte Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-07,2026-01,Emergency Store,10,strip,2024-08-05,"Medline Distributors, Thiruvananthapuram"
B02768,LLT256744,Atenova 100mg Tablet,Atenolol (100mg),Tablet,Lupin Ltd,Cardiovascular,2024-04,2025-10,Ward Store (Paeds),120,strip,2024-06-28,Apollo Wholesale Pvt Ltd
B02769,LL25E762,Resner 500mcg Injection,Methylcobalamin (500mcg),Injection,Lupin Ltd,Supplement,2025-01,2028-01,OPD Pharmacy,300,vial/amp,2025-04-05,Sree Pharma Agencies
B02770,IPT240915,Acifac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-08,2026-08,OT Store,120,strip,2024-10-16,Sanjivani Drug House
B02771,T2502-214,Olmezest 10 Tablet,Olmesartan Medoxomil (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-03,2025-09,ICU Store,50,strip,2024-03-26,Apollo Wholesale Pvt Ltd
B02772,68968103,Cathflush 10IU Injection,Heparin (10IU),Injection,Troikaa Pharmaceuticals Ltd,Anticoagulant,2024-05,2025-11,ICU Store,60,vial/amp,2024-08-26,Malabar Pharma Distributors
B02773,SP24J618,Glytears Eye Drop,Carboxymethylcellulose (0.5% w/v),Eye Drops,Sun Pharmaceutical Industries Ltd,Ophthalmology,2024-10,2026-10,ICU Store,0,bottle,2024-11-21,Apollo Wholesale Pvt Ltd
B02774,T2504-287,F Con 150mg Tablet,Fluconazole (150mg),Tablet,Lupin Ltd,Antifungal,2025-01,2028-01,OT Store,120,strip,2025-04-13,"Medline Distributors, Thiruvananthapuram"
B02775,TPT241920,Amol 500mg Tablet,Paracetamol (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-12,2027-12,OT Store,80,strip,2025-02-23,Sree Pharma Agencies
B02776,LLX242397,Canazole 1% Ear Drop,Clotrimazole (1% w/v),Ear Drops,Lupin Ltd,Antifungal,2024-03,2027-03,Main Pharmacy,80,bottle,2024-06-22,"Medline Distributors, Thiruvananthapuram"
B02777,CL25C979,Restyl 0.5mg Tablet,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-08,2026-08,OPD Pharmacy,150,strip,2024-11-29,Apollo Wholesale Pvt Ltd
B02778,IL24M648,Zerodol PT Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Ipca Laboratories Ltd,Analgesic/Antipyretic,2024-06,2026-06,OT Store,100,strip,2024-09-09,"Medline Distributors, Thiruvananthapuram"
B02779,ZCT243270,Epsolin 150mg Tablet ER,Phenytoin (150mg),Tablet,Zydus Cadila,Neurology/Psychiatry,2025-03,2027-03,OT Store,80,strip,2025-05-05,Kerala Medical Supplies Co.
B02780,42310051,Dexona 8mg Injection,Dexamethasone (8mg),Injection,Zydus Cadila,Steroid,2025-04,2026-10,ICU Store,120,vial/amp,2025-05-23,"Medline Distributors, Thiruvananthapuram"
B02781,T2408-066,Omnisec 20mg Tablet,Rabeprazole (20mg),Tablet,Cipla Ltd,Gastro,2024-09,2026-03,OPD Pharmacy,20,strip,2024-10-04,"Medline Distributors, Thiruvananthapuram"
B02782,AL24C070,Ceriz 5mg Syrup,Cetirizine (5mg/ml),Syrup,Alkem Laboratories Ltd,Respiratory,2024-01,2026-01,Ward Store (Paeds),30,bottle,2024-04-29,"Medline Distributors, Thiruvananthapuram"
B02783,LHS258335,Mefniwel 100mg Syrup,Mefenamic Acid (100mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-10,2027-10,Ward Store (Paeds),10,bottle,2024-10-28,Sanjivani Drug House
B02784,TPI241905,Ketamax 10mg Injection,Ketamine (10mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-04,2027-04,ICU Store,50,vial/amp,2024-07-26,Sanjivani Drug House
B02785,LL24C022,Lup Inh 300mg Tablet,Isoniazid (300mg),Tablet,Lupin Ltd,Anti-TB,2024-04,2026-04,Main Pharmacy,30,strip,2024-06-02,Sanjivani Drug House
B02786,TP25F375,Diclogesic RR 75mg Injection,Diclofenac (75mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-11,2026-11,Main Pharmacy,50,vial/amp,2025-01-17,Malabar Pharma Distributors
B02787,SP24B760,Teleact 20 Tablet,Telmisartan (20mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2025-12,OT Store,200,strip,2024-08-04,Kerala Medical Supplies Co.
B02788,38939951,Ritebeat 100mg Tablet,Amiodarone (100mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2025-03,2028-03,OT Store,20,strip,2025-04-04,Apollo Wholesale Pvt Ltd
B02789,AL25F671,Gentaril Eye/Ear Drops,Gentamicin (NA),Ear Drops,Alkem Laboratories Ltd,Antibiotic,2025-03,2028-03,ICU Store,300,bottle,2025-06-21,Sree Pharma Agencies
B02790,MPT240944,Januvia 25mg Tablet,Sitagliptin (25mg),Tablet,MSD Pharmaceuticals Pvt Ltd,Diabetes,2024-08,2026-08,Ward Store (Paeds),60,strip,2024-09-29,Sanjivani Drug House
B02791,57941821,Florobid 200mg Tablet,Ofloxacin (200mg),Tablet,Micro Labs Ltd,Antibiotic,2024-03,2027-03,OPD Pharmacy,0,strip,2024-05-28,Sanjivani Drug House
B02792,ALT242448,Albekem 400mg Tablet,Albendazole (400mg),Tablet,Alkem Laboratories Ltd,Anthelmintic,2024-10,2027-10,Main Pharmacy,50,strip,2025-01-04,"Medline Distributors, Thiruvananthapuram"
B02793,T2411-624,Cadifix 100mg Tablet DT,Cefixime (100mg),Tablet,Zydus Cadila,Antibiotic,2025-01,2027-01,OT Store,200,strip,2025-03-20,Sree Pharma Agencies
B02794,I2509-015,Ranbiotic 40mg Injection,Gentamicin (40mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-11,2027-11,OT Store,60,vial/amp,2025-02-19,Malabar Pharma Distributors
B02795,26389894,Levacetam 1000 Tablet,Levetiracetam (1000mg),Tablet,Micro Labs Ltd,Neurology/Psychiatry,2025-05,2028-05,OPD Pharmacy,40,strip,2025-07-15,Sree Pharma Agencies
B02796,TP24G243,Atmost 25mg Tablet,Atenolol (25mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-08,2026-02,ICU Store,20,strip,2024-09-11,Sanjivani Drug House
B02797,T2403-136,Zolax 0.25 Tablet,Alprazolam (0.25mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2025-03,2028-03,Ward Store (Paeds),10,strip,2025-04-26,"Medline Distributors, Thiruvananthapuram"
B02798,FHI257465,Scorbix 1.5gm Injection,Vitamin C (1.5gm),Injection,Fusion Healthcare Pvt Ltd,Supplement,2024-12,2026-06,Ward Store (Paeds),300,vial/amp,2025-01-25,Apollo Wholesale Pvt Ltd
B02799,CL25F654,Torodent-DT Tablet,Ketorolac (10mg),Tablet,Cipla Ltd,Analgesic/Antipyretic,2024-02,2026-02,OPD Pharmacy,30,strip,2024-05-21,Sanjivani Drug House
B02800,AL24L173,Alsita 100mg Tablet,Sitagliptin (100mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-07,2027-07,Ward Store (Paeds),0,strip,2024-10-08,Sree Pharma Agencies
B02801,CLT243293,Prazocip 2.5 XL Tablet,Prazosin (2.5mg),Tablet,Cipla Ltd,Cardiovascular,2024-11,2026-11,ICU Store,80,strip,2025-01-04,Sree Pharma Agencies
B02802,LLT245432,F Con 150mg Tablet,Fluconazole (150mg),Tablet,Lupin Ltd,Antifungal,2025-05,2026-11,Ward Store (Paeds),80,strip,2025-07-15,Sanjivani Drug House
B02803,I2406-954,Dexona Injection,Dexamethasone (4mg/ml),Injection,Zydus Cadila,Steroid,2024-02,2026-02,OPD Pharmacy,50,vial/amp,2024-05-14,Apollo Wholesale Pvt Ltd
B02804,T2410-482,Lupisit M 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2025-01,2028-01,OPD Pharmacy,20,strip,2025-02-14,Malabar Pharma Distributors
B02805,T2401-071,Gblin 150mg Tablet,Pregabalin (150mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-06,2025-12,OPD Pharmacy,200,strip,2024-08-15,Apollo Wholesale Pvt Ltd
B02806,61965156,Susten 200 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-09,2026-09,ICU Store,100,vial/amp,2024-09-29,Sree Pharma Agencies
B02807,MLV248231,Dolo 1000mg Infusion,Paracetamol (1000mg),Infusion,Micro Labs Ltd,Analgesic/Antipyretic,2024-02,2026-02,Emergency Store,30,bottle,2024-03-16,Malabar Pharma Distributors
B02808,CLS249629,Cefoprox 100mg Dry Syrup,Cefpodoxime Proxetil (100mg/5ml),Syrup,Cipla Ltd,Antibiotic,2024-08,2026-08,OT Store,300,bottle,2024-11-14,Sree Pharma Agencies
B02809,AL24K929,Dolocare 500mg Tablet,Paracetamol (500mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-06,2027-06,Main Pharmacy,60,strip,2024-06-26,"Medline Distributors, Thiruvananthapuram"
B02810,CLT256387,Esomac 40 Tablet,Esomeprazole (40mg),Tablet,Cipla Ltd,Gastro,2024-05,2025-11,Main Pharmacy,300,strip,2024-08-02,Apollo Wholesale Pvt Ltd
B02811,C2403-225,Alcros SB 50 Capsule,Itraconazole (50mg),Capsule,Sun Pharmaceutical Industries Ltd,Antifungal,2024-08,2027-08,OPD Pharmacy,20,strip,2024-10-30,Sree Pharma Agencies
B02812,21718382,Dolo 1000mg Infusion,Paracetamol (1000mg),Infusion,Micro Labs Ltd,Analgesic/Antipyretic,2025-02,2027-02,OPD Pharmacy,60,bottle,2025-03-08,Kerala Medical Supplies Co.
B02813,ZC25C439,Itchderm 1% Dusting Powder,Clotrimazole (1% w/w),Powder,Zydus Cadila,Antifungal,2024-12,2026-12,Emergency Store,20,pack,2025-01-17,Sree Pharma Agencies
B02814,DRT257518,Tryptomer 10mg Tablet,Amitriptyline (10mg),Tablet,Dr Reddy's Laboratories Ltd,Neurology/Psychiatry,2024-03,2026-03,Emergency Store,200,strip,2024-04-29,Apollo Wholesale Pvt Ltd
B02815,57021454,Maxi 500mg Tablet,Mefenamic Acid (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-08,2026-08,Ward Store (Paeds),40,strip,2024-10-03,Malabar Pharma Distributors
B02816,GSS240135,Zentel Oral Suspension,Albendazole (400mg),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2024-05,2027-05,Ward Store (Paeds),50,bottle,2024-07-08,Kerala Medical Supplies Co.
B02817,P24L220,Dexacos Injection,Dexamethasone Sodium Phosphate (4mg/ml),Injection,Paksons Pharmaceuticals Pvt. Ltd.,Steroid,2024-12,2026-11,OPD Pharmacy,120,vial/amp,2025-01-26,Apollo Wholesale Pvt Ltd
B02818,APV252849,D 10% Infusion,Dextrose (10% w/v),Infusion,AXA Parenterals Ltd,IV Fluids,2025-02,2027-02,OT Store,10,bottle,2025-05-25,Sanjivani Drug House
B02819,IPX255077,Decolite 0.10% Eye Drop,Dexamethasone (0.10% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Steroid,2024-09,2026-09,Main Pharmacy,80,bottle,2024-12-12,Sree Pharma Agencies
B02820,LLT243569,Telista 20 Tablet,Telmisartan (20mg),Tablet,Lupin Ltd,Cardiovascular,2024-11,2027-11,OT Store,20,strip,2024-12-05,"Medline Distributors, Thiruvananthapuram"
B02821,TPX255894,Unidine Solution 100 ml,Povidone Iodine (NA),Solution,Torrent Pharmaceuticals Ltd,Dermatology,2024-02,2025-08,ICU Store,40,bottle,2024-04-15,Apollo Wholesale Pvt Ltd
B02822,PF24C634,Compound Sodium Lacate Infusion,Ringer's lactate (NA),Infusion,Punjab Formulations Ltd,IV Fluids,2024-05,2026-05,ICU Store,10,bottle,2024-07-09,Kerala Medical Supplies Co.
B02823,74119726,Levipil 500 Tablet,Levetiracetam (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-06,2026-06,OT Store,10,strip,2024-07-10,Apollo Wholesale Pvt Ltd
B02824,T2403-868,Biclar 250mg Tablet,Clarithromycin (250mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-02,2027-02,Emergency Store,300,strip,2024-03-30,"Medline Distributors, Thiruvananthapuram"
B02825,AL24G934,Taxim-O 200 Tablet,Cefixime (200mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-03,2027-03,OT Store,20,strip,2024-04-02,"Medline Distributors, Thiruvananthapuram"
B02826,MPI257485,Nupenta 40mg Injection,Pantoprazole (40mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-02,2028-02,OT Store,200,vial/amp,2025-04-12,Kerala Medical Supplies Co.
B02827,SP25B400,Oleanz 2.5 Tablet,Olanzapine (2.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-06,2027-06,OT Store,40,strip,2024-09-12,Malabar Pharma Distributors
B02828,GP25E485,Candid Gold Dusting Powder,Allantoin (0.2% w/w) + Clotrimazole (1% w/w),Powder,Glenmark Pharmaceuticals Ltd,Antifungal,2024-05,2026-05,OPD Pharmacy,10,pack,2024-06-01,"Medline Distributors, Thiruvananthapuram"
B02829,AL24A046,Cytovan 500mg Injection,Vancomycin (500mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-06,2026-06,Emergency Store,300,vial/amp,2024-06-28,"Medline Distributors, Thiruvananthapuram"
B02830,ZCI245331,Xylocaine 1% Injection,Lidocaine (1%),Injection,Zydus Cadila,Other,2024-11,2027-11,OPD Pharmacy,120,vial/amp,2025-02-03,Kerala Medical Supplies Co.
B02831,AT244147,Cortirowa OD 9mg Tablet PR,Budesonide (9mg),Tablet,Abbott,Respiratory,2024-06,2027-06,OPD Pharmacy,100,strip,2024-07-28,"Medline Distributors, Thiruvananthapuram"
B02832,90388981,Azithral 250mg DT Tablet,Azithromycin (250mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2025-03,2028-03,Main Pharmacy,80,strip,2025-05-06,"Medline Distributors, Thiruvananthapuram"
B02833,I2404-922,Trapic 100mg Injection,Tranexamic Acid (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2024-04,2026-04,Emergency Store,200,vial/amp,2024-05-24,Sree Pharma Agencies
B02834,MP24C696,Ibrumac 200mg Tablet,Ibuprofen (200mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-10,2026-10,Main Pharmacy,0,strip,2024-12-09,Sree Pharma Agencies
B02835,SPT242418,Teleact AM Tablet,Telmisartan (40mg) + Amlodipine (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-07,2026-07,Emergency Store,60,strip,2024-10-23,Malabar Pharma Distributors
B02836,54443931,Clearnoz 0.75% Nasal Drops,Sodium Chloride (0.75% w/v),Drops,Cipla Ltd,IV Fluids,2025-02,2028-02,ICU Store,10,bottle,2025-04-24,"Medline Distributors, Thiruvananthapuram"
B02837,X2406-206,Betadine 10% Ointment,Povidone Iodine (10% w/w),Ointment,Win-Medicare Pvt Ltd,Dermatology,2025-01,2028-01,ICU Store,40,tube,2025-02-19,Sanjivani Drug House
B02838,CL25M747,Amicip 100mg Injection,Amikacin (100mg),Injection,Cipla Ltd,Antibiotic,2024-08,2027-08,Emergency Store,20,vial/amp,2024-09-12,Malabar Pharma Distributors
B02839,T2404-848,TP Tablet,Telmisartan (NA),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-03,2026-03,OPD Pharmacy,30,strip,2024-04-21,Kerala Medical Supplies Co.
B02840,T2505-865,Silectone 100 Tablet,Spironolactone (100mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2024-07,2027-07,Ward Store (Paeds),150,strip,2024-10-21,Apollo Wholesale Pvt Ltd
B02841,X2504-624,Candid Gold Cream,Clotrimazole (1% w/w),Cream,Glenmark Pharmaceuticals Ltd,Antifungal,2024-05,2025-11,ICU Store,300,tube,2024-06-20,Sanjivani Drug House
B02842,74925522,Nexito 5 Tablet,Escitalopram Oxalate (5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-01,2028-01,OT Store,10,strip,2025-04-25,"Medline Distributors, Thiruvananthapuram"
B02843,AL25B454,Dermikem Dusting Powder,Clotrimazole (1% w/w),Powder,Alkem Laboratories Ltd,Antifungal,2025-01,2027-01,OPD Pharmacy,40,pack,2025-04-19,Malabar Pharma Distributors
B02844,T2510-495,Bandy Chewable Tablet,Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2025-01,2028-01,OPD Pharmacy,300,strip,2025-04-01,Malabar Pharma Distributors
B02845,AL25K770,Ondem 8 Tablet,Ondansetron (8mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-07,2027-07,OT Store,20,strip,2024-10-27,Malabar Pharma Distributors
B02846,LL24M242,Lupisit M 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Lupin Ltd,Diabetes,2025-03,2028-03,OT Store,10,strip,2025-05-24,"Medline Distributors, Thiruvananthapuram"
B02847,SP25C340,Alcros SB 50 Capsule,Itraconazole (50mg),Capsule,Sun Pharmaceutical Industries Ltd,Antifungal,2024-05,2027-05,ICU Store,100,strip,2024-08-18,Sanjivani Drug House
B02848,I2403-918,Ultiblast 1gm Injection,Meropenem (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-12,2026-12,Emergency Store,120,vial/amp,2024-12-26,Kerala Medical Supplies Co.
B02849,98189010,Linosept 200mg Infusion,Linezolid (200mg),Infusion,Micro Labs Ltd,Antibiotic,2025-04,2028-04,OT Store,20,bottle,2025-07-15,Malabar Pharma Distributors
B02850,SPT244433,Istavel 100mg Tablet,Sitagliptin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-02,2027-02,ICU Store,200,strip,2025-05-05,"Medline Distributors, Thiruvananthapuram"
B02851,SPI255600,Vecuron 10mg Injection,Vecuronium (10mg),Injection,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2024-08,2026-02,Emergency Store,50,vial/amp,2024-10-18,Malabar Pharma Distributors
B02852,IP25C552,Cystina Capsule,Methylcobalamin (1500mcg),Capsule,Intas Pharmaceuticals Ltd,Supplement,2025-03,2027-03,OPD Pharmacy,50,strip,2025-03-26,Apollo Wholesale Pvt Ltd
B02853,AP25H931,Azithral 500 Tablet,Azithromycin (500mg),Tablet,Alembic Pharmaceuticals Ltd,Antibiotic,2024-12,2026-12,Main Pharmacy,80,strip,2025-03-02,Sree Pharma Agencies
B02854,T2502-281,Arvast 10 Tablet,Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-01,2027-01,OPD Pharmacy,150,strip,2024-03-23,Kerala Medical Supplies Co.
B02855,ZC24E247,Derihaler 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Zydus Cadila,Respiratory,2025-04,2026-10,Ward Store (Paeds),100,inhaler,2025-07-06,Kerala Medical Supplies Co.
B02856,X2408-582,Levobact 0.5% Eye Drop,Levofloxacin (0.5%),Eye Drops,Micro Labs Ltd,Antibiotic,2024-06,2025-12,Emergency Store,30,bottle,2024-08-06,"Medline Distributors, Thiruvananthapuram"
B02857,IP24M673,Sucragel Suspension,Sucralfate (500mg/5ml),Suspension,Intas Pharmaceuticals Ltd,Gastro,2024-09,2027-09,Main Pharmacy,0,bottle,2024-10-15,Apollo Wholesale Pvt Ltd
B02858,CL24G469,Olmecip 20 Tablet,Olmesartan Medoxomil (20mg),Tablet,Cipla Ltd,Cardiovascular,2024-01,2026-01,OT Store,300,strip,2024-04-16,Malabar Pharma Distributors
B02859,MPT257593,Bandy Chewable Tablet,Albendazole (400mg),Tablet,Mankind Pharma Ltd,Anthelmintic,2025-01,2028-01,Emergency Store,120,strip,2025-04-20,Sree Pharma Agencies
B02860,76957784,Monoloc 150mg Tablet,Ranitidine (150mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-05,2027-05,Main Pharmacy,60,strip,2025-07-15,Sanjivani Drug House
B02861,93955206,Thyronorm 100mcg Tablet,Thyroxine (100mcg),Tablet,Abbott,Endocrine,2024-10,2026-04,Ward Store (Paeds),40,strip,2024-11-22,"Medline Distributors, Thiruvananthapuram"
B02862,SPX246964,Suncros Soft 2% Cream,Zinc Oxide (2% w/w),Cream,Sun Pharmaceutical Industries Ltd,Supplement,2024-10,2026-10,OT Store,50,tube,2025-01-23,Sree Pharma Agencies
B02863,ML24B120,Calvit 12 Injection,Calcium (137.5mg) + Vitamin D3 (5000IU),Injection,Marc Laboratories Pvt Ltd,Supplement,2024-07,2027-07,Emergency Store,80,vial/amp,2024-08-01,Apollo Wholesale Pvt Ltd
B02864,G25B016,Sodium Chloride Injection USP 3%,Sodium Chloride (3% w/v),Infusion,Inven Pharmaceuticals Pvt. Ltd.,IV Fluids,2025-02,2027-01,Ward Store (Paeds),100,bottle,2025-04-13,"Medline Distributors, Thiruvananthapuram"
B02865,36725847,Esokem 20mg Tablet,Esomeprazole (20mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-11,2026-11,OPD Pharmacy,80,strip,2025-01-26,"Medline Distributors, Thiruvananthapuram"
B02866,IPX244862,Adiflox Ointment,Ciprofloxacin (0.3% w/w),Ointment,Intas Pharmaceuticals Ltd,Antibiotic,2024-12,2027-12,Emergency Store,20,tube,2025-02-12,Apollo Wholesale Pvt Ltd
B02867,61019678,Calpol 120mg Suspension Strawberry,Paracetamol (120mg/5ml),Suspension,Glaxo SmithKline Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2025-11,Ward Store (Paeds),80,bottle,2024-06-30,Kerala Medical Supplies Co.
B02868,S2403-320,Ampoxin-CV 200mg/28.5mg Suspension,Amoxycillin (200mg) + Clavulanic Acid (28.5mg),Suspension,Torrent Pharmaceuticals Ltd,Antibiotic,2024-04,2026-04,Emergency Store,60,bottle,2024-07-09,Malabar Pharma Distributors
B02869,SPI243430,Ceftop 250 mg/250 mg Injection,Cefoperazone (250mg) + Sulbactam (250mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-12,2026-06,Emergency Store,50,vial/amp,2024-12-28,Apollo Wholesale Pvt Ltd
B02870,T2507-822,Glycomet 250 Tablet,Metformin (250mg),Tablet,USV Ltd,Diabetes,2025-01,2027-01,OPD Pharmacy,200,strip,2025-04-21,Kerala Medical Supplies Co.
B02871,49585149,Unigenta Eye/Ear Drops,Gentamicin (15mg),Ear Drops,Torrent Pharmaceuticals Ltd,Antibiotic,2024-04,2026-04,OT Store,200,bottle,2024-05-29,Kerala Medical Supplies Co.
B02872,I2402-253,Ketamax 10mg Injection,Ketamine (10mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-09,2026-09,OT Store,20,vial/amp,2024-10-28,Kerala Medical Supplies Co.
B02873,IPT259315,Arvast F 10 Tablet,Fenofibrate (67mg) + Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-01,2028-01,Main Pharmacy,200,strip,2025-04-18,"Medline Distributors, Thiruvananthapuram"
B02874,CL25C020,Tenepla Tablet,Teneligliptin (20mg),Tablet,Cipla Ltd,Diabetes,2025-01,2028-01,OT Store,150,strip,2025-03-24,Malabar Pharma Distributors
B02875,14887763,Emenorm 10mg Tablet,Metoclopramide (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2025-03,2028-03,Emergency Store,10,strip,2025-04-21,Kerala Medical Supplies Co.
B02876,72913088,Dexodil 2mg Tablet,Dexchlorpheniramine (2mg),Tablet,Psychotropics India Ltd,Anti-allergic,2024-06,2025-12,OPD Pharmacy,100,strip,2024-09-03,Kerala Medical Supplies Co.
B02877,23735568,Amlong 10 Tablet,Amlodipine (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-03,2025-09,ICU Store,30,strip,2024-06-14,Sanjivani Drug House
B02878,T2510-388,Telect D 40mg/12.5mg Tablet,Telmisartan (40mg) + Hydrochlorothiazide (12.5mg),Tablet,Lupin Ltd,Cardiovascular,2024-08,2026-02,Ward Store (Paeds),60,strip,2024-10-09,"Medline Distributors, Thiruvananthapuram"
B02879,C2501-172,Lyrica 150mg Capsule,Pregabalin (150mg),Capsule,Pfizer Ltd,Neurology/Psychiatry,2024-02,2026-02,Main Pharmacy,120,strip,2024-04-01,Apollo Wholesale Pvt Ltd
B02880,LL25C849,Azilup 100mg Oral Suspension,Azithromycin (100mg),Suspension,Lupin Ltd,Antibiotic,2025-03,2028-03,OT Store,0,bottle,2025-05-26,Apollo Wholesale Pvt Ltd
B02881,ALI246021,Drotanic Injection,Drotaverine (20mg),Injection,Alkem Laboratories Ltd,Gastro,2025-03,2028-03,ICU Store,300,vial/amp,2025-04-07,Kerala Medical Supplies Co.
B02882,TP25G107,Telday 80 AM Tablet,Telmisartan (80mg) + Amlodipine (5mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-10,2027-10,OT Store,100,strip,2024-12-24,Sanjivani Drug House
B02883,PLT241473,Ativan 2mg Tablet,Lorazepam (2mg),Tablet,Pfizer Ltd,Neurology/Psychiatry,2024-07,2026-07,Emergency Store,120,strip,2024-08-31,Apollo Wholesale Pvt Ltd
B02884,C2502-398,TR Phyllin 125mg Capsule,Theophylline (125mg),Capsule,Sun Pharmaceutical Industries Ltd,Respiratory,2025-01,2027-01,OT Store,0,strip,2025-04-02,Malabar Pharma Distributors
B02885,67723010,Rantac Infant Syrup Mint,Ranitidine (75mg/5ml),Syrup,J B Chemicals and Pharmaceuticals Ltd,Gastro,2025-02,2026-08,OT Store,30,bottle,2025-04-24,Kerala Medical Supplies Co.
B02886,SPT252233,Dapefy 10mg Tablet,Dapagliflozin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2024-03,2027-03,OPD Pharmacy,200,strip,2024-05-23,Sree Pharma Agencies
B02887,ALX255252,Tobrex Eye Drop,Tobramycin (0.3% w/v),Eye Drops,Alcon Laboratories,Ophthalmology,2025-03,2028-03,ICU Store,0,bottle,2025-06-24,Apollo Wholesale Pvt Ltd
B02888,IPT247632,Lukotas 3D Tablet,Montelukast (10mg) + Levocetirizine (5mg),Tablet,Intas Pharmaceuticals Ltd,Respiratory,2025-05,2027-05,OT Store,80,strip,2025-06-17,Malabar Pharma Distributors
B02889,T2506-816,Losacar 25 Tablet,Losartan (25mg),Tablet,Zydus Cadila,Cardiovascular,2024-08,2027-08,Ward Store (Paeds),300,strip,2024-10-05,Sanjivani Drug House
B02890,T2408-953,Restyl 0.25mg Tablet,Alprazolam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-08,2026-08,Main Pharmacy,120,strip,2024-10-16,Kerala Medical Supplies Co.
B02891,TPS255592,Lezyncet-M Suspension,Levocetirizine (5mg) + Montelukast (10mg),Suspension,Torrent Pharmaceuticals Ltd,Respiratory,2025-03,2027-03,OT Store,100,bottle,2025-04-20,Sanjivani Drug House
B02892,IPT245683,Clavitas 500mg/125mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,Emergency Store,50,strip,2025-06-01,Sree Pharma Agencies
B02893,65710670,Alcros SB 50 Capsule,Itraconazole (50mg),Capsule,Sun Pharmaceutical Industries Ltd,Antifungal,2025-02,2026-08,OPD Pharmacy,80,strip,2025-05-05,Sanjivani Drug House
B02894,CLT247021,Atorlip 10 Tablet,Atorvastatin (10mg),Tablet,Cipla Ltd,Cardiovascular,2024-06,2025-12,Main Pharmacy,200,strip,2024-09-21,Sree Pharma Agencies
B02895,T2512-854,Mefkind P 100mg Tablet,Mefenamic Acid (100mg),Tablet,Mankind Pharma Ltd,Analgesic/Antipyretic,2024-02,2026-02,OPD Pharmacy,20,strip,2024-05-13,Sanjivani Drug House
B02896,LLV247682,Lupigyl IV 500mg Infusion,Metronidazole (500mg),Infusion,Lupin Ltd,Antibiotic,2025-01,2028-01,Main Pharmacy,80,bottle,2025-04-02,"Medline Distributors, Thiruvananthapuram"
B02897,TPT258117,Torvate 1000mg Tablet,Sodium Valproate (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-01,2027-01,Emergency Store,0,strip,2024-04-06,Apollo Wholesale Pvt Ltd
B02898,SPX249836,Silverex SSD Cream,Chlorhexidine Gluconate (0.2% w/w) + Silver Sulfadiazine (0.5% w/w),Cream,Sun Pharmaceutical Industries Ltd,Dermatology,2025-01,2026-07,OT Store,50,tube,2025-02-06,"Medline Distributors, Thiruvananthapuram"
B02899,I2411-672,Neotroy 0.5mg Injection,Neostigmine (0.5mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-01,2027-01,ICU Store,300,vial/amp,2025-04-27,Malabar Pharma Distributors
B02900,54452330,Metronil 500mg Infusion,Metronidazole (500mg),Infusion,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-11,2026-11,OT Store,120,bottle,2025-01-15,Kerala Medical Supplies Co.
B02901,IPX258992,Atro Eye Drop,Atropine (1% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-01,2026-01,OPD Pharmacy,300,bottle,2024-03-29,Kerala Medical Supplies Co.
B02902,SPX254178,Mufect Ointment,Mupirocin (2%),Ointment,Sun Pharmaceutical Industries Ltd,Dermatology,2024-05,2027-05,Main Pharmacy,100,tube,2024-06-06,Malabar Pharma Distributors
B02903,IHV243624,D5 Infusion,Dextrose (5gm),Infusion,Infutec Healthcare Limited,IV Fluids,2024-07,2027-07,Main Pharmacy,30,bottle,2024-10-02,Sanjivani Drug House
B02904,AL25J267,PAN 40 Tablet,Pantoprazole (40mg),Tablet,Alkem Laboratories Ltd,Gastro,2025-02,2028-02,Ward Store (Paeds),0,strip,2025-05-07,Malabar Pharma Distributors
B02905,AI248115,C One 1000mg Injection,Ceftriaxone (1000mg),Injection,Abbott,Antibiotic,2025-04,2026-10,Emergency Store,150,vial/amp,2025-07-15,Sree Pharma Agencies
B02906,T2402-456,Folvite 5mg Tablet,Folic Acid (5mg),Tablet,Pfizer Ltd,Haematology,2024-01,2027-01,Main Pharmacy,120,strip,2024-03-25,Kerala Medical Supplies Co.
B02907,T2410-953,Oleanz 7.5 Tablet,Olanzapine (7.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-03,2026-03,Main Pharmacy,50,strip,2024-04-22,Malabar Pharma Distributors
B02908,82494849,Cyclopam Plus Tablet,Dicyclomine (20mg) + Paracetamol (500mg),Tablet,Indoco Remedies Ltd,Analgesic/Antipyretic,2024-03,2027-03,OT Store,0,strip,2024-04-23,Malabar Pharma Distributors
B02909,79244185,Levoflox 500 Tablet,Levofloxacin (500mg),Tablet,Cipla Ltd,Antibiotic,2025-01,2028-01,Main Pharmacy,40,strip,2025-02-10,Sree Pharma Agencies
B02910,IPT257309,FCN 150 Tablet,Fluconazole (150mg),Tablet,Intas Pharmaceuticals Ltd,Antifungal,2024-09,2026-09,OPD Pharmacy,300,strip,2024-10-10,Apollo Wholesale Pvt Ltd
B02911,ALT253573,Cef 250mg Tablet,Cefuroxime (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-03,2025-09,ICU Store,80,strip,2024-05-01,Sanjivani Drug House
B02912,I2503-500,Xylocaine 1% Injection,Lidocaine (1%),Injection,Zydus Cadila,Other,2024-12,2026-06,Emergency Store,200,vial/amp,2025-03-24,"Medline Distributors, Thiruvananthapuram"
B02913,ILT240529,Folitrax 10 Tablet,Methotrexate (10mg),Tablet,Ipca Laboratories Ltd,Oncology,2025-03,2027-03,ICU Store,120,strip,2025-06-12,Sanjivani Drug House
B02914,SPI251599,Labebet 100mg Injection,Labetalol (100mg),Injection,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-07,2027-07,Main Pharmacy,150,vial/amp,2024-10-16,Sree Pharma Agencies
B02915,AP25F422,Monocef 1gm Injection,Ceftriaxone (1gm),Injection,Aristo Pharmaceuticals Pvt Ltd,Antibiotic,2025-01,2027-01,Emergency Store,40,vial/amp,2025-04-25,Sree Pharma Agencies
B02916,SP25B338,Teleact D 80 Tablet,Telmisartan (80mg) + Hydrochlorothiazide (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-02,2026-08,Main Pharmacy,30,strip,2025-06-01,Sree Pharma Agencies
B02917,MP25L953,Acuclav 1000mg Tablet,Amoxycillin (875mg) + Clavulanic Acid (125mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Antibiotic,2024-01,2027-01,Main Pharmacy,150,strip,2024-04-09,Sree Pharma Agencies
B02918,CLS243605,Montair LC Kid Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Cipla Ltd,Respiratory,2024-03,2026-03,OT Store,60,bottle,2024-04-03,Kerala Medical Supplies Co.
B02919,I2509-042,Dexona Injection,Dexamethasone (4mg/ml),Injection,Zydus Cadila,Steroid,2025-03,2027-03,OPD Pharmacy,0,vial/amp,2025-03-31,Malabar Pharma Distributors
B02920,T2412-872,Sodinate 1GM Tablet,Sodium Bicarbonate (1000mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Anaesthesia/Critical care,2024-05,2026-05,Ward Store (Paeds),10,strip,2024-06-29,Sanjivani Drug House
B02921,IP24H580,Cystina Capsule,Methylcobalamin (1500mcg),Capsule,Intas Pharmaceuticals Ltd,Supplement,2025-05,2027-05,Emergency Store,100,strip,2025-07-15,Malabar Pharma Distributors
B02922,T2402-677,Diclofam 100mg Tablet SR,Diclofenac (100mg),Tablet,Intas Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2027-03,OT Store,300,strip,2025-05-31,Apollo Wholesale Pvt Ltd
B02923,AOX-2402,Oxytocin Injection IP 1 ml,Oxytocin (5IU/ml),Injection,Systochem Laboratories Ltd.,Obstetrics,2024-04,2026-03,Main Pharmacy,150,vial/amp,2024-06-23,Kerala Medical Supplies Co.
B02924,TP24J726,Uniprest Tablet,Misoprostol (NA),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-05,2026-05,ICU Store,80,strip,2024-08-13,Sanjivani Drug House
B02925,41271945,Pregabid 50 Capsule,Pregabalin (50mg),Capsule,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2026-05,ICU Store,300,strip,2024-06-27,"Medline Distributors, Thiruvananthapuram"
B02926,SPI244395,Zygon 5IU Injection,Oxytocin (5IU),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-05,2027-05,ICU Store,60,vial/amp,2024-05-27,Kerala Medical Supplies Co.
B02927,TPT255703,Cipbact 500mg Tablet,Ciprofloxacin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2025-03,2026-09,OPD Pharmacy,20,strip,2025-05-03,Kerala Medical Supplies Co.
B02928,T2411-463,Zoryl 0.5 Tablet,Glimepiride (0.5mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2025-02,2027-02,Main Pharmacy,20,strip,2025-03-19,"Medline Distributors, Thiruvananthapuram"
B02929,ML25F274,Udosis 500mg Tablet,Sodium Bicarbonate (500mg),Tablet,Micro Labs Ltd,Anaesthesia/Critical care,2024-02,2027-02,Ward Store (Paeds),30,strip,2024-03-09,Sanjivani Drug House
B02930,SP24A464,Ranbiotic 40mg Injection,Gentamicin (40mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-03,2025-09,Main Pharmacy,200,vial/amp,2024-06-15,Kerala Medical Supplies Co.
B02931,MLI246258,Dexapen 4mg Injection,Dexamethasone (4mg),Injection,Morepen Laboratories Ltd,Steroid,2024-04,2026-04,Main Pharmacy,50,vial/amp,2024-07-29,Sanjivani Drug House
B02932,CLT248343,Restyl 0.25mg Tablet,Alprazolam (0.25mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-07,2027-07,Main Pharmacy,50,strip,2024-09-01,Sanjivani Drug House
B02933,T2402-289,Apigy 2.5 Tablet,Apixaban (2.5mg),Tablet,Cipla Ltd,Anticoagulant,2024-05,2026-05,Emergency Store,80,strip,2024-08-27,Sanjivani Drug House
B02934,TPT258057,Nexpro 20 Tablet,Esomeprazole (20mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-11,2026-05,OT Store,80,strip,2025-02-11,Kerala Medical Supplies Co.
B02935,SIS245324,Combiflam Suspension,Ibuprofen (100mg) + Paracetamol (162.5mg),Suspension,Sanofi India Ltd,Analgesic/Antipyretic,2024-06,2027-06,Main Pharmacy,30,bottle,2024-09-10,Kerala Medical Supplies Co.
B02936,IPT242130,Rabium 10 Tablet,Rabeprazole (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-10,2026-10,Emergency Store,50,strip,2024-11-01,Apollo Wholesale Pvt Ltd
B02937,SPT251495,Levipil 500 Tablet,Levetiracetam (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2024-10,2026-04,Emergency Store,10,strip,2024-11-26,Apollo Wholesale Pvt Ltd
B02938,T2502-704,Thyronorm 112mcg Tablet,Thyroxine (112mcg),Tablet,Abbott,Endocrine,2024-05,2026-05,Ward Store (Paeds),40,strip,2024-06-24,Sanjivani Drug House
B02939,85008484,Compound Sodium Lacate Infusion,Ringer's lactate (NA),Infusion,Punjab Formulations Ltd,IV Fluids,2024-11,2027-11,OT Store,120,bottle,2025-01-08,Malabar Pharma Distributors
B02940,TP24G347,Trofentyl 50mcg Injection,Fentanyl (50mcg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2024-11,2026-11,ICU Store,30,vial/amp,2025-02-10,"Medline Distributors, Thiruvananthapuram"
B02941,CL25M837,Norflox 400 Tablet,Norfloxacin (400mg) + Lactobacillus (120Million spores),Tablet,Cipla Ltd,Other,2024-05,2025-11,OPD Pharmacy,300,strip,2024-08-05,Malabar Pharma Distributors
B02942,IP25C345,Altispor 100mg Capsule,Itraconazole (100mg),Capsule,Intas Pharmaceuticals Ltd,Antifungal,2024-02,2027-02,Ward Store (Paeds),50,strip,2024-04-20,Sree Pharma Agencies
B02943,73765142,Lupimectin 12mg Tablet,Ivermectin (12mg),Tablet,Lupin Ltd,Anthelmintic,2024-06,2027-06,OPD Pharmacy,200,strip,2024-08-08,Kerala Medical Supplies Co.
B02944,IP25J478,Canditas Dusting Powder,Clotrimazole (75mg),Powder,Intas Pharmaceuticals Ltd,Antifungal,2024-05,2026-05,OPD Pharmacy,150,pack,2024-08-17,Sanjivani Drug House
B02945,GLV233,Glavit Syrup 200ml,Vitamin B complex,Syrup,Glacier Pharmaceutical Pvt. Ltd.,Supplement,2024-07,2026-07,ICU Store,0,bottle,2024-10-17,"Medline Distributors, Thiruvananthapuram"
B02946,SPT249237,Doliza 500mg Tablet,Paracetamol (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-11,2026-11,Main Pharmacy,30,strip,2024-12-26,Sanjivani Drug House
B02947,SPT240470,Rosuvas 10 Tablet,Rosuvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-02,2027-02,Main Pharmacy,150,strip,2025-04-10,Malabar Pharma Distributors
B02948,82317772,Fluza 150mg Tablet,Fluconazole (150mg),Tablet,Micro Labs Ltd,Antifungal,2024-10,2027-10,Emergency Store,40,strip,2024-12-27,Kerala Medical Supplies Co.
B02949,81684347,Drotaverin Injection,Drotaverine (NA),Injection,Cipla Ltd,Gastro,2025-03,2028-03,ICU Store,100,vial/amp,2025-06-18,"Medline Distributors, Thiruvananthapuram"
B02950,IPT258191,Decotas 30mg Tablet,Deflazacort (30mg),Tablet,Intas Pharmaceuticals Ltd,Steroid,2024-03,2026-03,ICU Store,20,strip,2024-06-09,"Medline Distributors, Thiruvananthapuram"
B02951,38083391,Amoxyclav 1000 mg/200 mg Injection,Amoxycillin (1000mg) + Clavulanic Acid (200mg),Injection,Abbott,Antibiotic,2025-03,2028-03,OT Store,10,vial/amp,2025-06-27,Malabar Pharma Distributors
B02952,LH25J519,Wellamo 10 Tablet,Amlodipine (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-01,2027-01,OPD Pharmacy,20,strip,2024-04-26,Kerala Medical Supplies Co.
B02953,71695387,Nasoclear Gel,Sodium Chloride (0.65% w/w),Gel,Zydus Cadila,IV Fluids,2024-05,2026-05,OT Store,100,tube,2024-07-09,Apollo Wholesale Pvt Ltd
B02954,TPS257417,Cocorex 10mg Syrup,Chlorpheniramine Maleate (10mg),Syrup,Taj Pharma India Ltd,Anti-allergic,2025-01,2028-01,Ward Store (Paeds),50,bottle,2025-04-10,Kerala Medical Supplies Co.
B02955,JPT240514,Silectone 100 Tablet,Spironolactone (100mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2024-02,2027-02,OT Store,100,strip,2024-05-24,Kerala Medical Supplies Co.
B02956,93407203,Mecovit Plus Injection,Methylcobalamin (0.5mg),Injection,Cipla Ltd,Supplement,2024-08,2026-02,Emergency Store,50,vial/amp,2024-11-25,Apollo Wholesale Pvt Ltd
B02957,TPT256929,Deviry 10mg Tablet,Medroxyprogesterone acetate (10mg),Tablet,Torrent Pharmaceuticals Ltd,Obstetrics,2024-01,2026-10,OPD Pharmacy,50,strip,2024-01-28,Sanjivani Drug House
B02958,ZC25G852,Neomine 0.5mg Injection,Neostigmine (0.5mg),Injection,Zydus Cadila,Anaesthesia/Critical care,2025-03,2028-03,OPD Pharmacy,120,vial/amp,2025-04-09,Apollo Wholesale Pvt Ltd
B02959,T2407-757,Olmetor 10mg Tablet,Olmesartan Medoxomil (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-11,2026-11,Emergency Store,10,strip,2024-11-27,Sree Pharma Agencies
B02960,T2404-831,Deplatt 150 Tablet,Clopidogrel (150mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-08,2026-02,Ward Store (Paeds),120,strip,2024-11-28,Kerala Medical Supplies Co.
B02961,TMI255810,Bupicain 5mg Injection,Bupivacaine (5mg),Injection,Themis Medicare Ltd,Anaesthesia/Critical care,2024-09,2027-09,Main Pharmacy,50,vial/amp,2024-11-02,Kerala Medical Supplies Co.
B02962,SPT252880,Ceplox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-02,2028-02,Main Pharmacy,20,strip,2025-04-04,Kerala Medical Supplies Co.
B02963,AT256103,AB-Rozu 10 Tablet,Rosuvastatin (10mg),Tablet,Abbott,Cardiovascular,2025-02,2028-02,Main Pharmacy,20,strip,2025-04-01,Sanjivani Drug House
B02964,24937373,Thyrodip 10mg Tablet,Carbimazole (10mg),Tablet,Lupin Ltd,Endocrine,2024-06,2026-06,OPD Pharmacy,80,strip,2024-07-19,Sanjivani Drug House
B02965,41927492,Eltroxin 25mcg Tablet,Thyroxine (25mcg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Endocrine,2024-01,2027-01,Ward Store (Paeds),120,strip,2024-02-22,Apollo Wholesale Pvt Ltd
B02966,CL24J221,Vanlid 250mg Capsule,Vancomycin (250mg),Capsule,Cipla Ltd,Antibiotic,2024-05,2027-05,Emergency Store,10,strip,2024-08-14,Sanjivani Drug House
B02967,IPT244149,Ignalis-M 100/1000 Tablet ER,Sitagliptin (100mg) + Metformin (1000mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-11,2026-11,Ward Store (Paeds),10,strip,2024-11-29,Apollo Wholesale Pvt Ltd
B02968,59818487,Intabact 2% Ointment,Mupirocin (2% w/w),Ointment,Intas Pharmaceuticals Ltd,Dermatology,2024-01,2026-04,OT Store,100,tube,2024-03-02,Malabar Pharma Distributors
B02969,SPT249760,Cardivas 12.5 Tablet,Carvedilol (12.5mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2026-06,Emergency Store,150,strip,2024-08-03,Apollo Wholesale Pvt Ltd
B02970,CP25H642,Demisone 4mg Injection,Dexamethasone (4mg),Injection,Cadila Pharmaceuticals Ltd,Steroid,2025-02,2026-08,Main Pharmacy,100,vial/amp,2025-04-24,Sree Pharma Agencies
B02971,94946730,Istamet 50mg/1000mg Tablet,Sitagliptin (50mg) + Metformin (1000mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-03,2028-03,OPD Pharmacy,120,strip,2025-05-27,Kerala Medical Supplies Co.
B02972,GPT258338,Telma 40 Tablet,Telmisartan (40mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-12,2026-12,Main Pharmacy,20,strip,2025-03-03,Sanjivani Drug House
B02973,SP25E941,Susten 200 Injection,Progesterone (100mg/ml),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-07,2026-07,OT Store,50,vial/amp,2024-10-11,Sanjivani Drug House
B02974,IPT247148,Arvast F 10 Tablet,Fenofibrate (67mg) + Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-04,2025-10,Ward Store (Paeds),50,strip,2024-07-10,"Medline Distributors, Thiruvananthapuram"
B02975,ALT241896,PAN 40 Tablet,Pantoprazole (40mg),Tablet,Alkem Laboratories Ltd,Gastro,2024-09,2027-09,OPD Pharmacy,150,strip,2024-10-15,Malabar Pharma Distributors
B02976,T2509-321,Acecloflam XP 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2025-05,2027-05,ICU Store,20,strip,2025-07-15,Malabar Pharma Distributors
B02977,SPS244652,Sucral D Suspension,Domperidone (7.5mg) + Sucralfate (1000mg),Suspension,Strassenburg Pharmaceuticals.Ltd,Gastro,2024-05,2027-05,Emergency Store,20,bottle,2024-06-27,Kerala Medical Supplies Co.
B02978,S2404-743,Alminth 200mg Syrup,Albendazole (200mg),Syrup,Torrent Pharmaceuticals Ltd,Anthelmintic,2024-11,2027-11,Emergency Store,0,bottle,2025-01-05,"Medline Distributors, Thiruvananthapuram"
B02979,28889590,Glimp M 1mg/1000mg Tablet,Glimepiride (1mg) + Metformin (1000mg),Tablet,Zydus Cadila,Diabetes,2025-01,2027-01,ICU Store,100,strip,2025-01-30,Sanjivani Drug House
B02980,48286573,Ultiblast 1gm Injection,Meropenem (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-10,2027-10,ICU Store,60,vial/amp,2024-12-06,Sree Pharma Agencies
B02981,LLT253426,Lupimectin 12mg Tablet,Ivermectin (12mg),Tablet,Lupin Ltd,Anthelmintic,2024-06,2025-12,OPD Pharmacy,20,strip,2024-09-29,Kerala Medical Supplies Co.
B02982,82948912,Amlong 10 Tablet,Amlodipine (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-09,2026-09,OT Store,50,strip,2024-12-22,"Medline Distributors, Thiruvananthapuram"
B02983,I2409-831,Mecovit Plus Injection,Methylcobalamin (0.5mg),Injection,Cipla Ltd,Supplement,2025-04,2028-04,Emergency Store,120,vial/amp,2025-06-25,Apollo Wholesale Pvt Ltd
B02984,MLI254869,Gramocef 250mg Injection,Ceftriaxone (250mg),Injection,Micro Labs Ltd,Antibiotic,2024-11,2027-11,OPD Pharmacy,30,vial/amp,2024-12-14,Malabar Pharma Distributors
B02985,T2402-311,Starcad-Beta 12.5 Tablet ER,Metoprolol Succinate (11.8mg),Tablet,Lupin Ltd,Cardiovascular,2024-12,2027-12,ICU Store,80,strip,2025-01-20,Malabar Pharma Distributors
B02986,SPT255209,Fentoin 100mg Tablet ER,Phenytoin (100mg),Tablet,Sun Pharmaceutical Industries Ltd,Neurology/Psychiatry,2025-03,2027-03,OPD Pharmacy,0,strip,2025-04-04,Malabar Pharma Distributors
B02987,X2510-685,Intadine 5% Ointment,Povidone Iodine (5%),Ointment,Intas Pharmaceuticals Ltd,Dermatology,2024-03,2026-03,ICU Store,40,tube,2024-03-26,Apollo Wholesale Pvt Ltd
B02988,JPT252404,Ultracet Tablet,Paracetamol/Acetaminophen (325mg) + Tramadol (37.5mg),Tablet,Janssen Pharmaceuticals,Analgesic/Antipyretic,2024-11,2027-11,Main Pharmacy,200,strip,2025-01-07,Sree Pharma Agencies
B02989,TPT253723,Eldoflam 120mg Tablet,Etoricoxib (120mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-05,2026-05,ICU Store,80,strip,2024-06-24,"Medline Distributors, Thiruvananthapuram"
B02990,LHI240700,Femozer 100mg Injection,Iron Sucrose (100mg),Injection,Leeford Healthcare Ltd,Haematology,2025-04,2027-04,OT Store,30,vial/amp,2025-06-07,Sanjivani Drug House
B02991,29027158,Anofer 100mg Injection,Iron Sucrose (100mg),Injection,Sun Pharmaceutical Industries Ltd,Haematology,2024-11,2026-11,ICU Store,10,vial/amp,2024-12-12,Kerala Medical Supplies Co.
B02992,39416977,Endogest 100 Capsule,Progesterone (Natural Micronized) (100mg),Capsule,Cipla Ltd,Obstetrics,2025-04,2026-10,OPD Pharmacy,200,strip,2025-06-21,Kerala Medical Supplies Co.
B02993,I2503-507,Myostigmin 0.5mg Injection 1ml,Neostigmine (0.5mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-05,2026-05,Ward Store (Paeds),30,vial/amp,2024-07-19,Sree Pharma Agencies
B02994,T2412-372,Arvast F 10 Tablet,Fenofibrate (67mg) + Rosuvastatin (10mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-01,OT Store,300,strip,2024-08-24,"Medline Distributors, Thiruvananthapuram"
B02995,JBT244006,Metrogyl 400 Tablet,Metronidazole (400mg),Tablet,J B Chemicals and Pharmaceuticals Ltd,Antibiotic,2024-05,2026-05,Emergency Store,150,strip,2024-07-18,Apollo Wholesale Pvt Ltd
B02996,93646063,Tegretol 300mg Tablet,Carbamazepine (300mg),Tablet,Novartis India Ltd,Neurology/Psychiatry,2024-12,2027-12,ICU Store,100,strip,2025-03-20,Sree Pharma Agencies
B02997,EPT246404,Ibusoft 400mg Tablet,Dexibuprofen (400mg),Tablet,Emcure Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2026-09,Emergency Store,80,strip,2025-05-01,Malabar Pharma Distributors
B02998,T2503-276,Azitough 250mg Tablet,Azithromycin (250mg),Tablet,Abbott,Antibiotic,2025-02,2026-08,Ward Store (Paeds),30,strip,2025-06-01,Apollo Wholesale Pvt Ltd
B02999,TPT251700,Rostar 10 Tablet,Rosuvastatin (10mg),Tablet,Torrent Pharmaceuticals Ltd,Cardiovascular,2024-04,2026-04,OPD Pharmacy,0,strip,2024-04-30,Malabar Pharma Distributors
B03000,ZCI243754,Angionox 40mg Injection,Enoxaparin (40mg),Injection,Zydus Cadila,Anticoagulant,2025-02,2027-02,Main Pharmacy,100,vial/amp,2025-05-20,"Medline Distributors, Thiruvananthapuram"
B03001,C2410-748,Urimax 0.4 Capsule MR,Tamsulosin (0.4mg),Capsule,Cipla Ltd,Urology,2024-10,2026-10,Main Pharmacy,100,strip,2025-01-14,Apollo Wholesale Pvt Ltd
B03002,TPT258356,Afoglip Tablet,Teneligliptin (20mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2024-06,2027-06,Main Pharmacy,120,strip,2024-08-25,Apollo Wholesale Pvt Ltd
B03003,AL24L380,Phenykem 100mg Tablet,Phenytoin (100mg),Tablet,Alkem Laboratories Ltd,Neurology/Psychiatry,2024-08,2026-08,Main Pharmacy,50,strip,2024-10-16,Kerala Medical Supplies Co.
B03004,MLI250755,Cefglobe S Injection,Cefoperazone (1000mg) + Sulbactam (1000mg),Injection,Micro Labs Ltd,Antibiotic,2024-12,2026-12,Ward Store (Paeds),300,vial/amp,2025-03-27,Apollo Wholesale Pvt Ltd
B03005,75488223,Rancort 6mg Tablet,Deflazacort (6mg),Tablet,Sun Pharmaceutical Industries Ltd,Steroid,2024-06,2027-06,ICU Store,20,strip,2024-08-14,Sree Pharma Agencies
B03006,65592149,Cadipar 250mg Oral Suspension,Paracetamol (250mg),Suspension,Cadila Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-05,2027-05,Emergency Store,120,bottle,2025-06-12,"Medline Distributors, Thiruvananthapuram"
B03007,X2507-025,Astinol Inhaler,Salbutamol (NA),Inhaler,Sun Pharmaceutical Industries Ltd,Respiratory,2024-12,2027-12,Ward Store (Paeds),50,inhaler,2025-03-30,Kerala Medical Supplies Co.
B03008,FL24G342,Zioral Drops,Zinc Gluconate (20mg),Drops,FDC Ltd,Supplement,2024-12,2026-12,Ward Store (Paeds),0,bottle,2024-12-27,Sree Pharma Agencies
B03009,APX257382,Naresol 0.65% Nasal Drops,Sodium Chloride (0.65% w/v),Drops,Alembic Pharmaceuticals Ltd,IV Fluids,2025-03,2028-03,Ward Store (Paeds),50,bottle,2025-06-02,"Medline Distributors, Thiruvananthapuram"
B03010,SP25M373,Flothin 20mg Injection,Enoxaparin (20mg),Injection,Sun Pharmaceutical Industries Ltd,Anticoagulant,2024-10,2026-10,ICU Store,120,vial/amp,2024-11-17,Malabar Pharma Distributors
B03011,DRT259399,Omez 40 Tablet,Omeprazole (40mg),Tablet,Dr Reddy's Laboratories Ltd,Gastro,2024-11,2026-11,Main Pharmacy,10,strip,2025-02-10,Sree Pharma Agencies
B03012,28495379,Ceftop 250 mg/250 mg Injection,Cefoperazone (250mg) + Sulbactam (250mg),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2025-04,2027-04,Ward Store (Paeds),200,vial/amp,2025-05-11,Sree Pharma Agencies
B03013,84820714,Biospas 10mg Injection,Dicyclomine (10mg),Injection,Biochem Pharmaceutical Industries,Gastro,2025-02,2027-02,ICU Store,60,vial/amp,2025-04-25,Malabar Pharma Distributors
B03014,89568937,Panpure 20mg Infusion,Pantoprazole (20mg),Infusion,Emcure Pharmaceuticals Ltd,Gastro,2024-10,2026-10,OPD Pharmacy,30,bottle,2025-01-12,Apollo Wholesale Pvt Ltd
B03015,ZCT240524,Linid Tablet,Linezolid (600mg),Tablet,Zydus Cadila,Antibiotic,2024-06,2026-06,OT Store,20,strip,2024-09-28,Sanjivani Drug House
B03016,TPT240477,Azulix 0.5 MF Tablet PR,Glimepiride (0.5mg) + Metformin (500mg),Tablet,Torrent Pharmaceuticals Ltd,Diabetes,2025-05,2028-05,Emergency Store,120,strip,2025-07-15,Kerala Medical Supplies Co.
B03017,X2401-973,Asthalin 100mcg Inhaler,Salbutamol (100mcg),Inhaler,Cipla Ltd,Respiratory,2024-06,2026-06,Main Pharmacy,30,inhaler,2024-07-27,Sanjivani Drug House
B03018,DRC252231,Omez 10 Capsule,Omeprazole (10mg),Capsule,Dr Reddy's Laboratories Ltd,Gastro,2024-02,2027-02,Emergency Store,0,strip,2024-05-07,Sanjivani Drug House
B03019,LLT250591,Clavidur 375mg Tablet,Amoxycillin (250mg) + Clavulanic Acid (125mg),Tablet,Lupin Ltd,Antibiotic,2024-01,2026-01,OPD Pharmacy,10,strip,2024-04-06,Kerala Medical Supplies Co.
B03020,27117564,Clavitas 500mg/125mg Tablet,Amoxycillin (500mg) + Clavulanic Acid (125mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2024-07,2026-07,OT Store,300,strip,2024-08-02,"Medline Distributors, Thiruvananthapuram"
B03021,31368924,Mecobex 500mcg Injection,Methylcobalamin (500mcg),Injection,Alkem Laboratories Ltd,Supplement,2025-02,2027-02,Ward Store (Paeds),200,vial/amp,2025-05-30,"Medline Distributors, Thiruvananthapuram"
B03022,51808607,Cipcal-XT Tablet,Calcium Carbonate (1250mg) + Vitamin D3 (2000IU),Tablet,Cipla Ltd,Supplement,2024-09,2026-09,OT Store,40,strip,2024-11-08,Sanjivani Drug House
B03023,I2408-853,Merosure 125mg Injection,Meropenem (125mg),Injection,Alkem Laboratories Ltd,Antibiotic,2024-09,2027-09,OPD Pharmacy,50,vial/amp,2024-09-29,Kerala Medical Supplies Co.
B03024,T2404-684,Gluvilda 50 Tablet,Vildagliptin (50mg),Tablet,Alkem Laboratories Ltd,Diabetes,2024-07,2027-07,OPD Pharmacy,50,strip,2024-10-12,Kerala Medical Supplies Co.
B03025,TPT249237,Rabemed 10mg Tablet,Rabeprazole (10mg),Tablet,Torrent Pharmaceuticals Ltd,Gastro,2024-02,2026-02,Ward Store (Paeds),0,strip,2024-02-29,Malabar Pharma Distributors
B03026,T2504-136,Dolocare 500mg Tablet,Paracetamol (500mg),Tablet,Alkem Laboratories Ltd,Analgesic/Antipyretic,2024-09,2026-03,OPD Pharmacy,40,strip,2024-11-10,Malabar Pharma Distributors
B03027,T2504-927,Omnacortil 2.5 Tablet DT,Prednisolone (2.5mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Steroid,2025-04,2026-10,Emergency Store,120,strip,2025-07-15,Sree Pharma Agencies
B03028,PLI247050,Solu-Medrol 125mg Injection,Methylprednisolone (125mg),Injection,Pfizer Ltd,Steroid,2024-11,2026-05,Emergency Store,30,vial/amp,2024-12-09,Malabar Pharma Distributors
B03029,T2411-546,Losartas 25 Tablet,Losartan (25mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-07,2026-07,ICU Store,120,strip,2024-10-28,Apollo Wholesale Pvt Ltd
B03030,T2508-486,Atorniz 10mg Tablet,Atorvastatin (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-09,2026-03,Emergency Store,40,strip,2024-11-29,"Medline Distributors, Thiruvananthapuram"
B03031,TPT242582,Hexidol 1.5 Tablet,Haloperidol (1.5mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2025-04,2026-10,Ward Store (Paeds),0,strip,2025-04-29,Malabar Pharma Distributors
B03032,IP24L694,Esivac Oral Solution,Lactulose (3.335gm/5ml),Oral Solution,Intas Pharmaceuticals Ltd,Gastro,2024-12,2027-12,Ward Store (Paeds),100,bottle,2025-03-21,Sanjivani Drug House
B03033,CLV240952,Pansec 40mg Infusion,Pantoprazole (40mg),Infusion,Cipla Ltd,Gastro,2025-04,2028-04,Ward Store (Paeds),30,bottle,2025-07-15,Kerala Medical Supplies Co.
B03034,42914388,Sucral Cream,Sucralfate (7% w/w),Cream,Strassenburg Pharmaceuticals.Ltd,Gastro,2025-02,2028-02,Ward Store (Paeds),150,tube,2025-04-27,Malabar Pharma Distributors
B03035,16413678,Defidin 5mg Tablet,Amlodipine (5mg),Tablet,Lupin Ltd,Cardiovascular,2024-12,2026-12,ICU Store,60,strip,2025-01-13,Sanjivani Drug House
B03036,T2403-147,Foly-Act Tablet,Folic Acid (5mg),Tablet,Morepen Laboratories Ltd,Haematology,2024-12,2027-12,Ward Store (Paeds),80,strip,2025-01-04,Sanjivani Drug House
B03037,I2507-402,Zygon 5IU Injection,Oxytocin (5IU),Injection,Sun Pharmaceutical Industries Ltd,Obstetrics,2024-05,2025-11,OPD Pharmacy,40,vial/amp,2024-08-22,"Medline Distributors, Thiruvananthapuram"
B03038,50471241,Azintas 250 Tablet,Azithromycin (250mg),Tablet,Intas Pharmaceuticals Ltd,Antibiotic,2025-01,2026-07,Main Pharmacy,80,strip,2025-04-12,Malabar Pharma Distributors
B03039,FLT241846,Zifi 200 Tablet,Cefixime (200mg),Tablet,FDC Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,30,strip,2024-06-19,Malabar Pharma Distributors
B03040,SP24D869,Aztor 10 Tablet,Atorvastatin (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2025-05,2028-05,OPD Pharmacy,120,strip,2025-07-06,Apollo Wholesale Pvt Ltd
B03041,15303441,Alcid S Syrup,Sucralfate (NA),Syrup,Alkem Laboratories Ltd,Gastro,2025-02,2026-08,OPD Pharmacy,0,bottle,2025-05-15,Sree Pharma Agencies
B03042,C2408-367,Dynamox 250mg Capsule,Amoxycillin (250mg),Capsule,Micro Labs Ltd,Antibiotic,2024-11,2026-05,Ward Store (Paeds),30,strip,2024-12-18,"Medline Distributors, Thiruvananthapuram"
B03043,I2403-937,Cleofol 10mg Injection,Propofol (10mg),Injection,Themis Medicare Ltd,Anaesthesia/Critical care,2025-01,2027-01,Ward Store (Paeds),200,vial/amp,2025-04-22,Apollo Wholesale Pvt Ltd
B03044,LLT241548,Clopi 150mg Tablet,Clopidogrel (150mg),Tablet,Lupin Ltd,Cardiovascular,2024-08,2026-08,OT Store,60,strip,2024-10-14,Sree Pharma Agencies
B03045,SPT249112,Istamet 50mg/500mg Tablet,Sitagliptin (50mg) + Metformin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Diabetes,2025-01,2028-01,OT Store,200,strip,2025-01-29,Malabar Pharma Distributors
B03046,CLT246518,Metolar 100 Tablet,Metoprolol Tartrate (100mg),Tablet,Cipla Ltd,Cardiovascular,2024-11,2026-11,Main Pharmacy,150,strip,2025-01-02,Sree Pharma Agencies
B03047,25503345,Meftal 250 Tablet,Mefenamic Acid (250mg),Tablet,Blue Cross Laboratories Ltd,Analgesic/Antipyretic,2024-11,2026-11,OT Store,300,strip,2025-01-04,Apollo Wholesale Pvt Ltd
B03048,TP24C769,Neotroy 0.5mg Injection,Neostigmine (0.5mg),Injection,Troikaa Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-04,2028-04,OT Store,300,vial/amp,2025-06-16,Apollo Wholesale Pvt Ltd
B03049,T2511-295,Alciflox 500mg Tablet,Ciprofloxacin (500mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-10,2026-10,ICU Store,120,strip,2025-01-24,Malabar Pharma Distributors
B03050,SPI255346,Labebet 100mg Injection,Labetalol (100mg),Injection,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-05,2027-05,Main Pharmacy,150,vial/amp,2024-07-25,Sree Pharma Agencies
B03051,IPI259827,Chophos 1000mg Injection,Cyclophosphamide (1000mg),Injection,Intas Pharmaceuticals Ltd,Oncology,2024-05,2025-11,Main Pharmacy,80,vial/amp,2024-07-24,"Medline Distributors, Thiruvananthapuram"
B03052,68131630,Ciplox 250 Tablet,Ciprofloxacin (250mg),Tablet,Cipla Ltd,Antibiotic,2024-03,2025-09,ICU Store,60,strip,2024-04-20,"Medline Distributors, Thiruvananthapuram"
B03053,AX255010,Duphalac Enema Solution,Lactulose (3.35gm/5ml),Solution,Abbott,Gastro,2024-02,2026-02,Ward Store (Paeds),300,bottle,2024-05-08,Kerala Medical Supplies Co.
B03054,CLT259936,Larpose 1mg Tablet,Lorazepam (1mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-12,2026-12,Emergency Store,50,strip,2025-01-08,Kerala Medical Supplies Co.
B03055,CL24K240,Glygard 40mg Tablet,Gliclazide (40mg),Tablet,Cipla Ltd,Diabetes,2024-05,2026-05,ICU Store,20,strip,2024-06-17,Sree Pharma Agencies
B03056,49922369,Clopilet 150 Tablet,Clopidogrel (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Cardiovascular,2024-06,2026-06,Main Pharmacy,120,strip,2024-09-12,Malabar Pharma Distributors
B03057,S2409-380,Albaxy Suspension,Albendazole (200mg),Suspension,Sun Pharmaceutical Industries Ltd,Anthelmintic,2024-11,2027-11,Main Pharmacy,200,bottle,2025-02-21,Sree Pharma Agencies
B03058,ZC25H681,Bioprim Syrup,Sulfamethoxazole (200mg) + Trimethoprim (40mg),Syrup,Zydus Cadila,Antibiotic,2025-05,2026-11,Main Pharmacy,150,bottle,2025-06-17,Apollo Wholesale Pvt Ltd
B03059,75838904,Asthalin Respirator Solution,Salbutamol (5mg),Solution,Cipla Ltd,Respiratory,2024-11,2027-11,OPD Pharmacy,100,bottle,2024-12-11,Apollo Wholesale Pvt Ltd
B03060,T2407-837,Edeflow 100 Tablet,Spironolactone (100mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-10,2026-10,ICU Store,40,strip,2024-11-09,Kerala Medical Supplies Co.
B03061,MPI243837,Nupenta 40mg Injection,Pantoprazole (40mg),Injection,Macleods Pharmaceuticals Pvt Ltd,Gastro,2025-05,2028-05,Main Pharmacy,20,vial/amp,2025-07-15,Malabar Pharma Distributors
B03062,CL24K019,Bro Cofdex Plus Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Cipla Ltd,Respiratory,2025-02,2028-02,ICU Store,80,bottle,2025-05-23,Kerala Medical Supplies Co.
B03063,T2502-095,Maxi 500mg Tablet,Mefenamic Acid (500mg),Tablet,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-02,2027-02,OPD Pharmacy,60,strip,2025-03-05,Apollo Wholesale Pvt Ltd
B03064,BI250744,Basalog 100IU/ml Injection,Insulin Glargine (100IU/ml),Injection,Biocon,Diabetes,2024-10,2026-10,OPD Pharmacy,200,vial/amp,2024-10-28,Sanjivani Drug House
B03065,79227788,Angiblock 10mg Capsule,Nifedipine (10mg),Capsule,Alkem Laboratories Ltd,Cardiovascular,2024-08,2027-08,ICU Store,200,strip,2024-09-11,Sanjivani Drug House
B03066,SP24D769,Oncoplatin AQ 10mg Injection,Cisplatin (10mg),Injection,Sun Pharmaceutical Industries Ltd,Oncology,2025-01,2027-01,Ward Store (Paeds),150,vial/amp,2025-04-30,Kerala Medical Supplies Co.
B03067,TPI244867,Maxizon 1gm Injection,Ceftriaxone (1gm),Injection,Torrent Pharmaceuticals Ltd,Antibiotic,2024-03,2026-03,Main Pharmacy,10,vial/amp,2024-04-06,Kerala Medical Supplies Co.
B03068,ZC24K475,Rosupil 10mg Tablet,Rosuvastatin (10mg),Tablet,Zydus Cadila,Cardiovascular,2025-03,2027-03,Ward Store (Paeds),0,strip,2025-05-13,Sanjivani Drug House
B03069,JP25F170,Silectone 100 Tablet,Spironolactone (100mg),Tablet,Johnlee Pharmaceuticals Pvt Ltd,Cardiovascular,2024-06,2027-06,Ward Store (Paeds),50,strip,2024-07-22,Kerala Medical Supplies Co.
B03070,IEW 1480B,Eldervit-12 Injection,Vitamin C + B12 + Folic Acid + Niacinamide,Injection,E.G. Pharmaceuticals,Supplement,2024-07,2026-07,ICU Store,50,vial/amp,2024-08-14,Sree Pharma Agencies
B03071,X2410-204,Ipratop 200mcg Inhaler,Ipratropium (200mcg),Inhaler,AstraZeneca,Respiratory,2024-01,2026-01,OPD Pharmacy,80,inhaler,2024-04-01,Sree Pharma Agencies
B03072,SPI247058,Dexelex 100mg Injection,Hydrocortisone (100mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2025-02,2028-02,Main Pharmacy,80,vial/amp,2025-03-06,Kerala Medical Supplies Co.
B03073,IPT251103,Amitone 10mg Tablet,Amitriptyline (10mg),Tablet,Intas Pharmaceuticals Ltd,Neurology/Psychiatry,2024-05,2026-05,OPD Pharmacy,50,strip,2024-06-16,Sanjivani Drug House
B03074,71024383,Hqtor 300mg Tablet,Hydroxychloroquine (300mg),Tablet,Torrent Pharmaceuticals Ltd,Antimalarial,2024-10,2026-10,OT Store,100,strip,2025-01-18,Apollo Wholesale Pvt Ltd
B03075,I2509-384,Acostin 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-11,2026-11,Ward Store (Paeds),80,vial/amp,2025-01-13,Sree Pharma Agencies
B03076,SP24L197,DEPOPRED 40 MG INJECTION,Methylprednisolone (40mg),Injection,Sun Pharmaceutical Industries Ltd,Steroid,2024-06,2026-06,OT Store,150,vial/amp,2024-08-27,Apollo Wholesale Pvt Ltd
B03077,TP25F596,Diclogesic RR 75mg Injection,Diclofenac (75mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-04,2027-04,OT Store,300,vial/amp,2025-05-08,"Medline Distributors, Thiruvananthapuram"
B03078,GP24G132,Telma 40 Tablet,Telmisartan (40mg),Tablet,Glenmark Pharmaceuticals Ltd,Cardiovascular,2024-03,2025-09,Emergency Store,30,strip,2024-06-06,Sanjivani Drug House
B03079,AT257476,Gluformin 500 Tablet,Metformin (500mg),Tablet,Abbott,Diabetes,2024-02,2027-02,Main Pharmacy,20,strip,2024-04-25,Kerala Medical Supplies Co.
B03080,T2407-711,Stamlo 2.5 Tablet,Amlodipine (2.5mg),Tablet,Dr Reddy's Laboratories Ltd,Cardiovascular,2025-01,2026-07,Main Pharmacy,80,strip,2025-02-11,Sree Pharma Agencies
B03081,BPI259291,Vancogram 500mg Injection,Vancomycin (500mg),Injection,Biochem Pharmaceutical Industries,Antibiotic,2024-07,2027-07,ICU Store,80,vial/amp,2024-08-30,Malabar Pharma Distributors
B03082,IPI246009,Evaparin -PFS 40 Injection,Enoxaparin (40mg),Injection,Intas Pharmaceuticals Ltd,Anticoagulant,2024-09,2027-09,OPD Pharmacy,20,vial/amp,2024-11-02,"Medline Distributors, Thiruvananthapuram"
B03083,T2509-574,F Con 150mg Tablet,Fluconazole (150mg),Tablet,Lupin Ltd,Antifungal,2024-06,2027-06,OPD Pharmacy,30,strip,2024-09-28,Sanjivani Drug House
B03084,C2508-715,Adamon 50mg Capsule,Tramadol (50mg),Capsule,Zydus Cadila,Analgesic/Antipyretic,2025-01,2028-01,OPD Pharmacy,0,strip,2025-03-22,Kerala Medical Supplies Co.
B03085,29693143,Duphalac Enema Solution,Lactulose (3.35gm/5ml),Solution,Abbott,Gastro,2024-02,2026-02,OT Store,20,bottle,2024-05-20,Sanjivani Drug House
B03086,33788294,Amoxil Kid 125mg Tablet,Amoxycillin (125mg),Tablet,Zydus Cadila,Antibiotic,2025-03,2027-03,Emergency Store,10,strip,2025-05-02,Malabar Pharma Distributors
B03087,SII257560,Lasix Injection,Furosemide (10mg/ml),Injection,Sanofi India Ltd,Cardiovascular,2024-01,2026-01,Ward Store (Paeds),30,vial/amp,2024-03-07,Sree Pharma Agencies
B03088,58882805,Roxin 100mcg Tablet,Thyroxine (100mcg),Tablet,Zydus Cadila,Endocrine,2024-11,2026-05,ICU Store,60,strip,2025-02-14,Sanjivani Drug House
B03089,IPI241346,Dorinta 20mg Injection,Drotaverine (20mg),Injection,Intas Pharmaceuticals Ltd,Gastro,2025-04,2028-04,Emergency Store,100,vial/amp,2025-05-31,Apollo Wholesale Pvt Ltd
B03090,T2509-126,Drotikind 80mg Tablet,Drotaverine (80mg),Tablet,Mankind Pharma Ltd,Gastro,2025-01,2028-01,Emergency Store,150,strip,2025-03-28,Kerala Medical Supplies Co.
B03091,T2412-275,Thormone 50mcg Tablet,Thyroxine (50mcg),Tablet,Lupin Ltd,Endocrine,2024-03,2027-03,OPD Pharmacy,0,strip,2024-05-31,Malabar Pharma Distributors
B03092,29364653,Nudiclo 100mg Tablet,Diclofenac (100mg),Tablet,Macleods Pharmaceuticals Pvt Ltd,Analgesic/Antipyretic,2024-04,2026-04,OPD Pharmacy,20,strip,2024-05-09,Kerala Medical Supplies Co.
B03093,80944243,E Tel 20mg Tablet,Telmisartan (20mg),Tablet,Emcure Pharmaceuticals Ltd,Cardiovascular,2025-01,2026-07,Emergency Store,100,strip,2025-02-10,Malabar Pharma Distributors
B03094,92386462,Restyl 0.5mg Tablet SR,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-02,2025-08,Emergency Store,300,strip,2024-02-26,"Medline Distributors, Thiruvananthapuram"
B03095,CL24A150,IBUGESIC 300MG CAPSULE SR,Ibuprofen (300mg),Capsule,Cipla Ltd,Analgesic/Antipyretic,2025-02,2028-02,ICU Store,40,strip,2025-05-03,Apollo Wholesale Pvt Ltd
B03096,LLT252710,Lupin 10 Rheza Tablet,Rosuvastatin (10mg),Tablet,Lupin Ltd,Cardiovascular,2024-05,2027-05,OT Store,120,strip,2024-07-14,"Medline Distributors, Thiruvananthapuram"
B03097,MLT241634,Alcef O 100mg Tablet DT,Cefixime (100mg),Tablet,Micro Labs Ltd,Antibiotic,2025-02,2026-08,Main Pharmacy,120,strip,2025-03-19,"Medline Distributors, Thiruvananthapuram"
B03098,CL25C434,Raniciz Junior Syrup,Ranitidine (75mg/5ml),Syrup,Cipla Ltd,Gastro,2024-06,2025-12,ICU Store,0,bottle,2024-08-25,Kerala Medical Supplies Co.
B03099,SP24K499,Ceplox 750mg Tablet,Ciprofloxacin (750mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2025-08,ICU Store,80,strip,2024-05-20,Kerala Medical Supplies Co.
B03100,1-3098,Dextrose Injection IP 5% (D5),Dextrose (5% w/v),Infusion,Tam-Bran Pharmaceuticals Pvt. Ltd.,IV Fluids,2025-01,2027-12,ICU Store,60,bottle,2025-04-03,Malabar Pharma Distributors
B03101,67323574,Misoprost 100mg Tablet,Misoprostol (100mg),Tablet,Cipla Ltd,Obstetrics,2024-01,2027-01,ICU Store,200,strip,2024-04-03,Malabar Pharma Distributors
B03102,30534124,Asthalin 4 Tablet,Salbutamol (4mg),Tablet,Cipla Ltd,Respiratory,2025-02,2028-02,Ward Store (Paeds),20,strip,2025-04-22,Sanjivani Drug House
B03103,24877375,Drotin DS Oral Suspension Mango Sugar Free,Drotaverine (20mg/5ml),Suspension,Walter Bushnell,Gastro,2024-07,2027-07,ICU Store,20,bottle,2024-10-23,Kerala Medical Supplies Co.
B03104,90557330,Manogyl 10% Infusion,Mannitol (10% w/v),Infusion,J B Chemicals and Pharmaceuticals Ltd,Anaesthesia/Critical care,2025-02,2028-02,OPD Pharmacy,200,bottle,2025-05-26,Kerala Medical Supplies Co.
B03105,GS25B887,Zentel Chewable Tablet,Albendazole (400mg),Tablet,Glaxo SmithKline Pharmaceuticals Ltd,Anthelmintic,2024-09,2026-03,ICU Store,80,strip,2024-11-28,"Medline Distributors, Thiruvananthapuram"
B03106,ML24D037,Allercet-M Kid Tablet DT,Levocetirizine (2.5mg) + Montelukast (4mg),Tablet,Micro Labs Ltd,Respiratory,2025-05,2028-05,Ward Store (Paeds),80,strip,2025-07-15,Apollo Wholesale Pvt Ltd
B03107,42609677,Acdof 40mg Injection,Pantoprazole (40mg),Injection,Alkem Laboratories Ltd,Gastro,2024-01,2026-01,ICU Store,20,vial/amp,2024-02-04,"Medline Distributors, Thiruvananthapuram"
B03108,24115931,Ibusoft 400mg Tablet,Dexibuprofen (400mg),Tablet,Emcure Pharmaceuticals Ltd,Analgesic/Antipyretic,2025-03,2026-09,Emergency Store,80,strip,2025-05-15,Malabar Pharma Distributors
B03109,T2403-626,Medrol 4mg Tablet,Methylprednisolone (4mg),Tablet,Pfizer Ltd,Steroid,2024-01,2026-01,OT Store,60,strip,2024-04-16,Sanjivani Drug House
B03110,AI258163,Nicophen 22.75mg Injection,Pheniramine (22.75mg),Injection,Abbott,Anti-allergic,2025-01,2028-01,Main Pharmacy,100,vial/amp,2025-03-05,Sanjivani Drug House
B03111,01AF0301,Sodium Chloride Injection IP 0.9%,Sodium Chloride (0.9% w/v),Infusion,Paschim Banga Pharmaceuticals,IV Fluids,2023-12,2026-11,Emergency Store,40,bottle,2023-12-30,"Medline Distributors, Thiruvananthapuram"
B03112,IPT251392,Zomet 500mg Tablet,Metformin (500mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-07,2027-07,ICU Store,200,strip,2024-08-22,Sanjivani Drug House
B03113,T2504-491,Nugrel Tablet,Clopidogrel (75mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-03,2026-09,Ward Store (Paeds),300,strip,2025-06-02,Sanjivani Drug House
B03114,APS242623,Magadol Oral Suspension,Paracetamol (250mg/5ml),Suspension,Alembic Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-02,2026-02,Ward Store (Paeds),40,bottle,2024-03-30,Malabar Pharma Distributors
B03115,MLX254107,Osmogel Eye Drop,Sodium Chloride (5% w/v),Eye Drops,Micro Labs Ltd,IV Fluids,2025-04,2028-04,Emergency Store,10,bottle,2025-05-25,"Medline Distributors, Thiruvananthapuram"
B03116,SP25D010,Histac 150 Tablet,Ranitidine (150mg),Tablet,Sun Pharmaceutical Industries Ltd,Gastro,2025-03,2028-03,Main Pharmacy,20,strip,2025-04-03,Kerala Medical Supplies Co.
B03117,TPT252168,Torvate 1000mg Tablet,Sodium Valproate (1000mg),Tablet,Torrent Pharmaceuticals Ltd,Neurology/Psychiatry,2024-06,2026-06,Main Pharmacy,300,strip,2024-08-30,Malabar Pharma Distributors
B03118,S2404-759,Levocet LM Syrup,Levocetirizine (2.5mg/5ml) + Montelukast (4mg/5ml),Syrup,Aarcin Pharmaceutical LLP,Respiratory,2024-08,2027-08,OT Store,60,bottle,2024-08-31,Sree Pharma Agencies
B03119,NLI247805,Magneon 50% Injection,Magnesium Sulphate (50% w/v),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2025-05,2027-05,Main Pharmacy,50,vial/amp,2025-07-15,Kerala Medical Supplies Co.
B03120,58926292,Nova 150mg Tablet SR,Pregabalin (150mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-03,2026-03,OT Store,300,strip,2024-04-20,Sanjivani Drug House
B03121,NL24G594,Mct Rof Injection,Propofol (10mg),Injection,Neon Laboratories Ltd,Anaesthesia/Critical care,2024-11,2026-05,Emergency Store,10,vial/amp,2024-12-25,Apollo Wholesale Pvt Ltd
B03122,SPT249940,Cerzin 10mg Tablet,Cetirizine (10mg),Tablet,Sun Pharmaceutical Industries Ltd,Respiratory,2024-11,2026-11,Main Pharmacy,150,strip,2025-01-25,Apollo Wholesale Pvt Ltd
B03123,IPS241255,Abd 200mg Suspension,Albendazole (200mg),Suspension,Intas Pharmaceuticals Ltd,Anthelmintic,2025-01,2028-01,Main Pharmacy,10,bottle,2025-04-17,Sree Pharma Agencies
B03124,V2509-907,Aculife 25% Infusion,Dextrose (25% w/v),Infusion,Nirlife Healthcare,IV Fluids,2024-03,2027-03,Emergency Store,200,bottle,2024-04-13,"Medline Distributors, Thiruvananthapuram"
B03125,TPT254360,Biclar 250mg Tablet,Clarithromycin (250mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2024-01,2027-01,Main Pharmacy,100,strip,2024-04-26,Malabar Pharma Distributors
B03126,CL24F172,Acivir 200 DT Tablet,Acyclovir (200mg),Tablet,Cipla Ltd,Antiviral,2024-09,2026-09,OPD Pharmacy,150,strip,2024-10-08,Malabar Pharma Distributors
B03127,DR25L650,Ketorol SP Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Dr Reddy's Laboratories Ltd,Analgesic/Antipyretic,2024-06,2025-12,OPD Pharmacy,80,strip,2024-09-10,"Medline Distributors, Thiruvananthapuram"
B03128,T2404-809,Noplaq 75mg Tablet,Clopidogrel (75mg),Tablet,Alkem Laboratories Ltd,Cardiovascular,2024-11,2026-11,ICU Store,40,strip,2024-12-24,"Medline Distributors, Thiruvananthapuram"
B03129,C2512-009,Zorem 1.25 Capsule,Ramipril (1.25mg),Capsule,Intas Pharmaceuticals Ltd,Cardiovascular,2025-04,2026-10,ICU Store,50,strip,2025-05-18,"Medline Distributors, Thiruvananthapuram"
B03130,14415512,Dapasach 10mg Tablet,Dapagliflozin (10mg),Tablet,Cipla Ltd,Diabetes,2024-08,2026-02,OPD Pharmacy,120,strip,2024-10-02,Sree Pharma Agencies
B03131,IPI241017,Hicoly 1Million IU Injection,Colistimethate Sodium (1Million IU),Injection,Intas Pharmaceuticals Ltd,Antibiotic,2024-06,2027-06,Emergency Store,120,vial/amp,2024-08-22,Sree Pharma Agencies
B03132,CLT254261,Dytor 100 Tablet,Torasemide (100mg),Tablet,Cipla Ltd,Cardiovascular,2024-08,2027-08,Ward Store (Paeds),40,strip,2024-10-23,"Medline Distributors, Thiruvananthapuram"
B03133,LHT240774,Redotrex 500 Tablet,Tranexamic Acid (500mg),Tablet,Leeford Healthcare Ltd,Haematology,2025-01,2027-01,ICU Store,80,strip,2025-03-09,Malabar Pharma Distributors
B03134,DJI259896,D5 IV Injection,Dextrose (5% w/v),Injection,D.J Laboratories Pvt Ltd,IV Fluids,2024-10,2027-10,OPD Pharmacy,50,vial/amp,2024-11-29,"Medline Distributors, Thiruvananthapuram"
B03135,ILI249691,Lamic-500 Injection,Amikacin (500mg/2ml),Injection,Inmac Laboratories,Antibiotic,2024-11,2026-11,Emergency Store,30,vial/amp,2025-01-23,Kerala Medical Supplies Co.
B03136,CL24C189,Dytor 100 Tablet,Torasemide (100mg),Tablet,Cipla Ltd,Cardiovascular,2025-03,2027-03,OT Store,120,strip,2025-04-05,Sanjivani Drug House
B03137,LLT258326,Ciprolup 250mg Tablet,Ciprofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2024-06,2026-06,OT Store,200,strip,2024-07-11,Malabar Pharma Distributors
B03138,99560316,Amlong 10 Tablet,Amlodipine (10mg),Tablet,Micro Labs Ltd,Cardiovascular,2025-01,2027-01,OPD Pharmacy,20,strip,2025-04-01,"Medline Distributors, Thiruvananthapuram"
B03139,ZC24B061,Dexona 6mg Tablet,Dexamethasone (6mg),Tablet,Zydus Cadila,Steroid,2025-02,2027-02,Emergency Store,60,strip,2025-04-04,Apollo Wholesale Pvt Ltd
B03140,LL24E893,Azilup 100mg Oral Suspension,Azithromycin (100mg),Suspension,Lupin Ltd,Antibiotic,2024-05,2026-05,ICU Store,10,bottle,2024-07-26,Apollo Wholesale Pvt Ltd
B03141,MLT252514,Azepress 250mg Tablet,Azithromycin (250mg),Tablet,Micro Labs Ltd,Antibiotic,2025-04,2027-04,Emergency Store,30,strip,2025-05-28,Sanjivani Drug House
B03142,X2404-907,Clinlup 1% Gel,Clindamycin (1%),Gel,Lupin Ltd,Antibiotic,2024-06,2027-06,OPD Pharmacy,20,tube,2024-09-11,Kerala Medical Supplies Co.
B03143,CL25G728,Metolar 1mg Injection,Metoprolol Tartrate (1mg),Injection,Cipla Ltd,Cardiovascular,2024-01,2026-11,Ward Store (Paeds),10,vial/amp,2024-03-17,Sanjivani Drug House
B03144,40763714,Restyl 0.5mg Tablet SR,Alprazolam (0.5mg),Tablet,Cipla Ltd,Neurology/Psychiatry,2024-12,2026-12,Emergency Store,30,strip,2025-01-20,Kerala Medical Supplies Co.
B03145,A25E601,Rivotril 0.25mg Tablet,Clonazepam (0.25mg),Tablet,Abbott,Neurology/Psychiatry,2024-06,2027-06,Ward Store (Paeds),300,strip,2024-08-09,Apollo Wholesale Pvt Ltd
B03146,NLI249683,Keparin 25000IU Injection,Heparin (25000IU),Injection,Neon Laboratories Ltd,Anticoagulant,2025-02,2027-02,OT Store,50,vial/amp,2025-05-25,Apollo Wholesale Pvt Ltd
B03147,67459585,Angizaar 25 Tablet,Losartan (25mg),Tablet,Micro Labs Ltd,Cardiovascular,2024-05,2027-05,OPD Pharmacy,0,strip,2024-07-07,"Medline Distributors, Thiruvananthapuram"
B03148,IP25M741,Trizoryl 1 Tablet SR,Glimepiride (1mg) + Metformin (500mg),Tablet,Intas Pharmaceuticals Ltd,Diabetes,2024-09,2027-09,OPD Pharmacy,80,strip,2024-11-16,Sanjivani Drug House
B03149,10462685,Tamsukem 0.2mg Tablet,Tamsulosin (0.2mg),Tablet,Alkem Laboratories Ltd,Urology,2024-12,2026-12,Main Pharmacy,20,strip,2025-01-12,Apollo Wholesale Pvt Ltd
B03150,BI24B554,Electrolyte M 5% Infusion,Dextrose (5% w/v),Infusion,Baxter India Pvt Ltd,IV Fluids,2024-05,2025-11,Main Pharmacy,60,bottle,2024-07-14,Kerala Medical Supplies Co.
B03151,TS24042,Telmisartan Tablets IP 40 mg,Telmisartan (40mg),Tablet,Eurokem Laboratories Pvt. Ltd.,Cardiovascular,2024-10,2025-12,OPD Pharmacy,50,strip,2024-12-16,Malabar Pharma Distributors
B03152,LHT257433,Wellamo 10 Tablet,Amlodipine (10mg),Tablet,Leeford Healthcare Ltd,Cardiovascular,2024-06,2026-06,OPD Pharmacy,80,strip,2024-08-14,Sanjivani Drug House
B03153,IP25J777,Decotas 30mg Tablet,Deflazacort (30mg),Tablet,Intas Pharmaceuticals Ltd,Steroid,2025-04,2027-04,Ward Store (Paeds),30,strip,2025-06-19,Sanjivani Drug House
B03154,CLX253908,Moxicip Eye Drop,Moxifloxacin (0.5% w/v),Eye Drops,Cipla Ltd,Ophthalmology,2024-04,2026-04,OPD Pharmacy,50,bottle,2024-05-31,Malabar Pharma Distributors
B03155,ML24G095,Hexapod 100mg Tablet DT,Cefpodoxime Proxetil (100mg),Tablet,Micro Labs Ltd,Antibiotic,2024-01,2027-01,OT Store,200,strip,2024-04-09,Sanjivani Drug House
B03156,50326991,Fusibact Cream,Fusidic Acid (2% w/w),Cream,Cipla Ltd,Dermatology,2025-02,2027-02,OT Store,0,tube,2025-03-07,"Medline Distributors, Thiruvananthapuram"
B03157,CL24D268,Doxicip Injection,Doxycycline (100mg),Injection,Cipla Ltd,Antibiotic,2025-02,2028-02,Ward Store (Paeds),80,vial/amp,2025-04-29,Kerala Medical Supplies Co.
B03158,I2401-001,Tranarest 100mg Injection,Tranexamic Acid (100mg),Injection,Cadila Pharmaceuticals Ltd,Haematology,2024-03,2027-03,Ward Store (Paeds),0,vial/amp,2024-04-22,Kerala Medical Supplies Co.
B03159,SPX244200,Fendrop 25mcg Patch,Fentanyl (25mcg),Drops,Sun Pharmaceutical Industries Ltd,Anaesthesia/Critical care,2025-04,2028-04,OT Store,50,bottle,2025-06-14,Sanjivani Drug House
B03160,ALI242344,Amiject 100mg Injection,Amikacin (100mg),Injection,Alkem Laboratories Ltd,Antibiotic,2025-01,2027-01,OT Store,300,vial/amp,2025-04-01,Apollo Wholesale Pvt Ltd
B03161,22031000,Ciprolup 250mg Tablet,Ciprofloxacin (250mg),Tablet,Lupin Ltd,Antibiotic,2025-01,2026-07,Emergency Store,0,strip,2025-04-19,Apollo Wholesale Pvt Ltd
B03162,AL24K396,Alciflox 250mg Tablet,Ciprofloxacin (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-04,2026-04,OPD Pharmacy,50,strip,2024-05-23,Sree Pharma Agencies
B03163,T24H459A,Telapp MT 25 Tablet,Telmisartan (40mg) + Metoprolol Succinate (25mg),Tablet,Bajaj Formulation,Cardiovascular,2024-08,2026-07,OT Store,0,strip,2024-08-29,Apollo Wholesale Pvt Ltd
B03164,T2408-625,Espin TM Tablet,S-Amlodipine (2.5mg) + Telmisartan (40mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2024-05,2026-05,Ward Store (Paeds),0,strip,2024-08-23,Malabar Pharma Distributors
B03165,97087978,Decolite 0.10% Eye Drop,Dexamethasone (0.10% w/v),Eye Drops,Intas Pharmaceuticals Ltd,Steroid,2024-09,2026-09,OT Store,0,bottle,2024-11-27,Apollo Wholesale Pvt Ltd
B03166,80600592,Aceclonac P 100mg/325mg Tablet,Aceclofenac (100mg) + Paracetamol (325mg),Tablet,Lupin Ltd,Analgesic/Antipyretic,2024-10,2027-10,OT Store,20,strip,2025-01-07,"Medline Distributors, Thiruvananthapuram"
B03167,TPT246631,Nftor 100mg Tablet,Nitrofurantoin (100mg),Tablet,Torrent Pharmaceuticals Ltd,Antibiotic,2025-05,2027-05,ICU Store,150,strip,2025-06-18,Kerala Medical Supplies Co.
B03168,SPC246120,Dolotram 50mg Capsule,Tramadol (50mg),Capsule,Sun Pharmaceutical Industries Ltd,Analgesic/Antipyretic,2024-07,2027-07,OT Store,30,strip,2024-09-29,Apollo Wholesale Pvt Ltd
B03169,S2409-404,Leemol 125mg/5ml Syrup,Paracetamol (125mg/5ml),Syrup,Leeford Healthcare Ltd,Analgesic/Antipyretic,2024-01,2027-01,ICU Store,80,bottle,2024-02-19,Sanjivani Drug House
B03170,I2403-536,Xylistin 0.5MIU Injection,Colistimethate Sodium (500000IU),Injection,Cipla Ltd,Antibiotic,2025-02,2027-02,OPD Pharmacy,0,vial/amp,2025-04-05,Sree Pharma Agencies
B03171,CPI242386,Humanext N 40IU/ml Injection,Insulin Isophane (40IU),Injection,Cadila Pharmaceuticals Ltd,Diabetes,2025-04,2027-04,Ward Store (Paeds),120,vial/amp,2025-05-08,"Medline Distributors, Thiruvananthapuram"
B03172,T2408-818,Depotex 16mg Tablet,Methylprednisolone (16mg),Tablet,Zydus Cadila,Steroid,2024-03,2026-03,Emergency Store,10,strip,2024-06-04,Apollo Wholesale Pvt Ltd
B03173,LPS259314,Nam Cold DX Syrup,Dextromethorphan Hydrobromide (NA),Syrup,Lincoln Pharmaceuticals Ltd,Respiratory,2024-11,2026-05,ICU Store,30,bottle,2025-01-08,"Medline Distributors, Thiruvananthapuram"
B03174,SPT249820,Loxazin 500mg Tablet,Levofloxacin (500mg),Tablet,Sun Pharmaceutical Industries Ltd,Antibiotic,2024-02,2025-08,Emergency Store,0,strip,2024-03-16,Malabar Pharma Distributors
B03175,LHX250196,Welbusol 50mcg Inhaler,Levosalbutamol (50mcg),Inhaler,Leeford Healthcare Ltd,Respiratory,2024-11,2026-11,Main Pharmacy,20,inhaler,2024-12-06,Malabar Pharma Distributors
B03176,AT248348,CAAT 10 Tablet,Atorvastatin (10mg),Tablet,Abbott,Cardiovascular,2024-11,2026-11,ICU Store,40,strip,2025-01-06,Kerala Medical Supplies Co.
B03177,ALT255851,Cef 250mg Tablet,Cefuroxime (250mg),Tablet,Alkem Laboratories Ltd,Antibiotic,2024-05,2025-11,OPD Pharmacy,60,strip,2024-08-25,Kerala Medical Supplies Co.
B03178,AS252566,Tossex 12 Oral Suspension Orange,Dextromethorphan Hydrobromide (30mg/5ml),Suspension,Abbott,Respiratory,2024-11,2026-11,OT Store,80,bottle,2024-12-12,Apollo Wholesale Pvt Ltd
B03179,MP24D643,Emikind Pet Syrup,Ondansetron (2mg/5ml),Syrup,Mankind Pharma Ltd,Gastro,2024-08,2026-08,ICU Store,120,bottle,2024-11-11,Sanjivani Drug House
B03180,TPI259406,Diclogesic RR 75mg Injection,Diclofenac (75mg),Injection,Torrent Pharmaceuticals Ltd,Analgesic/Antipyretic,2024-09,2026-09,ICU Store,60,vial/amp,2024-11-30,"Medline Distributors, Thiruvananthapuram"
B03181,X2512-681,Omnacortil 0.1% Cream,Methylprednisolone (0.1% w/w),Cream,Macleods Pharmaceuticals Pvt Ltd,Steroid,2025-04,2028-04,OT Store,60,tube,2025-05-02,Apollo Wholesale Pvt Ltd
B03182,IPT241561,Cardipin 20mg Tablet,Nifedipine (20mg),Tablet,Intas Pharmaceuticals Ltd,Cardiovascular,2025-02,2028-02,OPD Pharmacy,10,strip,2025-04-05,"Medline Distributors, Thiruvananthapuram"
B03183,IP24M123,Loopra 10mg Tablet,Loperamide (10mg),Tablet,Intas Pharmaceuticals Ltd,Gastro,2024-05,2025-11,OT Store,0,strip,2024-08-23,"Medline Distributors, Thiruvananthapuram"
B03184,48832971,Epilive 100mg Injection,Levetiracetam (100mg),Injection,Lupin Ltd,Neurology/Psychiatry,2024-09,2027-09,OPD Pharmacy,10,vial/amp,2024-10-07,Sanjivani Drug House
```
