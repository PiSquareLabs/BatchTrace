# Load PAT_PATIENTS

Synthetic patients: 2,190 from the main data plus 5 demo cases (P90001–P90005). Phone numbers are deliberately invalid (+91-00000-xxxxx).

- Target: `BATCHTRACE.CORE.PAT_PATIENTS` (the table must already exist)
- Rows: **2,195**
- Columns: `patient_id, patient_name, sex, date_of_birth, age, blood_group, phone, district, known_allergies, registered_on`
- All data is synthetic, except the real CDSCO batch numbers, products and makers.

## Prompt for CoCo
```
Read data/md/02_PAT_PATIENTS.md. Copy the CSV block under "## Data" into data/tmp/PAT_PATIENTS.csv, exactly as it is.
PUT it to @BATCHTRACE.RAW.SEED_DATA/PAT_PATIENTS/ (AUTO_COMPRESS=TRUE, OVERWRITE=TRUE).
TRUNCATE BATCHTRACE.CORE.PAT_PATIENTS, then COPY INTO it, listing these columns explicitly: patient_id, patient_name, sex, date_of_birth, age, blood_group, phone, district, known_allergies, registered_on.
Use file format BATCHTRACE.RAW.CSV_FMT (SKIP_HEADER=1, FIELD_OPTIONALLY_ENCLOSED_BY='"', EMPTY_FIELD_AS_NULL=TRUE, UTF-8) and ON_ERROR=ABORT_STATEMENT.

Then run the checks below and show me the results. Do not touch any other table.
```

## Checks
```sql
SELECT COUNT(*) FROM BATCHTRACE.CORE.PAT_PATIENTS;  -- expect 2195
SELECT patient_id, patient_name, age FROM BATCHTRACE.CORE.PAT_PATIENTS WHERE patient_id LIKE 'P9%';  -- expect 5 rows
```

## Data
```csv
patient_id,patient_name,sex,date_of_birth,age,blood_group,phone,district,known_allergies,registered_on
P00001,Varsha Shroff,F,1978-04-27,47,AB-,+91-00000-92559,Kottayam,None known,2023-10-11
P00002,Varsha Trivedi,F,1997-09-24,27,A-,+91-00000-69374,Kanyakumari,NSAIDs,2022-03-21
P00003,Ikshita Goyal,F,2007-07-05,18,AB+,+91-00000-41711,Kottayam,None known,2021-11-10
P00004,Yashvi Soni,F,1946-09-14,78,O-,+91-00000-75506,Thiruvananthapuram,None known,2022-10-04
P00005,Idika Chandra,F,1947-08-10,77,O-,+91-00000-51324,Kollam,None known,2023-03-26
P00007,Ekavir Chana,M,1953-01-03,72,B+,+91-00000-84218,Kanyakumari,None known,2021-11-09
P00008,Anvi Randhawa,F,1985-12-31,39,B+,+91-00000-27641,Kollam,None known,2024-01-04
P00009,Varsha Dugar,F,1975-12-14,49,AB+,+91-00000-27166,Alappuzha,None known,2023-09-18
P00010,Abhimanyu Wadhwa,M,1994-07-16,31,AB+,+91-00000-34550,Alappuzha,NSAIDs,2022-03-29
P00011,Azad Bhargava,M,2013-07-17,12,B-,+91-00000-48839,Alappuzha,None known,2023-10-31
P00012,Andrew Gupta,M,1970-01-23,55,AB-,+91-00000-26675,Kottayam,None known,2021-09-15
P00013,Jai Balan,M,1983-04-04,42,AB+,+91-00000-34877,Kollam,Penicillin,2023-06-28
P00014,Vedika Narain,F,2015-05-29,10,B+,+91-00000-15072,Kottayam,None known,2023-05-16
P00015,Thomas Hayre,M,1982-03-01,43,A+,+91-00000-19014,Kollam,None known,2022-09-12
P00018,Aahana Chada,F,1947-07-29,78,AB-,+91-00000-56854,Kanyakumari,None known,2023-12-12
P00019,Veer Mall,M,1967-02-20,58,A+,+91-00000-19493,Thiruvananthapuram,None known,2022-07-05
P00020,Tanvi Chacko,F,1937-02-16,88,B-,+91-00000-21131,Kanyakumari,None known,2023-10-28
P00021,Joshua Murty,M,2019-01-07,6,O+,+91-00000-89805,Thiruvananthapuram,None known,2023-10-15
P00022,Ishwar Varghese,M,1991-01-10,34,AB-,+91-00000-67740,Alappuzha,Penicillin,2023-10-22
P00023,Maanas Balan,M,2006-07-12,19,AB+,+91-00000-24796,Alappuzha,NSAIDs,2022-03-11
P00024,Bhavya Chokshi,F,2006-10-31,18,A+,+91-00000-54895,Kanyakumari,None known,2022-08-23
P00025,Sai Chokshi,M,1982-04-18,43,AB+,+91-00000-60386,Kollam,Sulfa drugs,2023-02-25
P00026,Mohini Raju,F,1998-07-26,26,B+,+91-00000-46280,Kollam,None known,2022-10-11
P00027,Bahadurjit Badal,M,1993-08-16,31,B-,+91-00000-91890,Alappuzha,None known,2023-10-31
P00028,Aadi Kala,M,1968-10-13,56,B-,+91-00000-50505,Kanyakumari,Sulfa drugs,2023-12-27
P00029,Henry Ben,M,2012-03-22,13,A+,+91-00000-16152,Kanyakumari,None known,2022-10-15
P00030,Wahab Prashad,M,1973-06-22,52,AB+,+91-00000-36128,Alappuzha,None known,2023-07-17
P00031,Sneha Saini,F,1977-04-06,48,O-,+91-00000-55316,Kottayam,None known,2022-08-21
P00032,Bina Issac,F,1938-06-26,87,A-,+91-00000-60852,Kollam,None known,2022-10-08
P00033,Krishna Nayar,M,2006-11-28,18,B-,+91-00000-95370,Kollam,None known,2022-01-06
P00034,Caleb Mukhopadhyay,M,2000-06-10,25,O-,+91-00000-80379,Pathanamthitta,None known,2022-01-10
P00035,Ojas Aurora,M,2024-10-10,0,A-,+91-00000-46078,Alappuzha,None known,2023-06-06
P00036,Tara Dalal,F,2004-11-25,20,A+,+91-00000-77701,Kanyakumari,None known,2021-09-07
P00037,Ekani Koshy,F,1935-04-19,90,AB-,+91-00000-79030,Kottayam,None known,2021-09-16
P00038,Chandresh Apte,M,1967-02-24,58,A-,+91-00000-89879,Kollam,None known,2021-08-27
P00039,Bhanumati Shroff,F,1974-01-02,51,B+,+91-00000-75952,Thiruvananthapuram,NSAIDs,2022-12-25
P00040,Widisha Goel,F,1948-11-28,76,B+,+91-00000-31859,Thiruvananthapuram,Penicillin,2022-10-03
P00041,Ijaya Sem,F,1990-02-04,35,A-,+91-00000-72460,Kottayam,None known,2023-09-26
P00042,Yashoda Halder,F,1964-08-08,60,O+,+91-00000-14669,Kollam,None known,2023-05-28
P00043,Ekaja Saini,F,1988-09-13,36,AB-,+91-00000-23747,Alappuzha,Sulfa drugs,2023-09-12
P00044,Rehaan Dada,M,2009-07-11,16,A-,+91-00000-92969,Alappuzha,None known,2022-04-25
P00045,Siya Salvi,F,1993-10-28,31,AB+,+91-00000-81164,Kottayam,Sulfa drugs,2021-08-21
P00046,Jagvi Acharya,F,1967-02-22,58,B-,+91-00000-35517,Kollam,None known,2023-10-08
P00048,Advaith Kade,M,2008-01-20,17,B+,+91-00000-76280,Kanyakumari,None known,2022-08-19
P00049,Idika Ramesh,F,2014-10-12,10,AB-,+91-00000-29209,Kollam,None known,2023-09-20
P00050,Daksha Basak,F,1955-10-13,69,O+,+91-00000-27622,Kanyakumari,None known,2023-10-28
P00051,Elijah Kala,M,1981-12-21,43,AB+,+91-00000-88765,Pathanamthitta,None known,2022-04-06
P00052,Timothy Kuruvilla,M,1995-01-18,30,A-,+91-00000-35575,Kottayam,None known,2023-10-10
P00054,Neelima Raju,F,1999-12-30,25,A+,+91-00000-53242,Kottayam,None known,2021-11-21
P00055,Bina Borde,F,1982-02-05,43,O-,+91-00000-71451,Thiruvananthapuram,None known,2023-01-16
P00056,Chakradev Joshi,M,2004-02-02,21,AB+,+91-00000-96476,Alappuzha,Sulfa drugs,2023-07-13
P00057,Keya Aurora,F,1948-08-12,76,B+,+91-00000-61822,Kottayam,None known,2023-09-20
P00058,Raksha Prabhu,F,1992-04-17,33,A-,+91-00000-11412,Thiruvananthapuram,None known,2023-05-04
P00059,Vasana Datta,F,1971-09-09,53,AB-,+91-00000-94496,Thiruvananthapuram,Penicillin,2022-05-14
P00060,Wyatt Deshmukh,M,1935-12-12,89,A+,+91-00000-74948,Kottayam,NSAIDs,2022-05-15
P00061,Reyansh Goswami,M,1975-09-28,49,O-,+91-00000-57916,Kottayam,None known,2022-09-08
P00062,Faraj Mukhopadhyay,M,1972-07-18,53,O+,+91-00000-42115,Kottayam,None known,2022-04-07
P00063,Ishaan Krish,M,1964-07-08,61,B-,+91-00000-19634,Kollam,None known,2022-01-09
P00064,Girish Dutt,M,1992-05-14,33,AB+,+91-00000-89118,Kanyakumari,None known,2023-11-25
P00066,Wyatt Brar,M,1978-01-25,47,A+,+91-00000-48027,Kanyakumari,None known,2023-05-16
P00067,Shivansh Batta,M,1975-03-13,50,O-,+91-00000-89928,Kanyakumari,Sulfa drugs,2022-01-30
P00068,Damini Chopra,F,1967-03-28,58,AB+,+91-00000-99544,Thiruvananthapuram,None known,2024-01-06
P00070,Lakshmi Khare,F,1984-02-06,41,B-,+91-00000-74802,Kanyakumari,None known,2021-09-09
P00071,Shivani Kurian,F,1939-12-25,85,A-,+91-00000-43826,Alappuzha,None known,2023-01-03
P00072,Ucchal Swaminathan,F,1968-12-26,56,B-,+91-00000-86099,Thiruvananthapuram,None known,2021-08-02
P00073,Manan Venkatesh,M,1972-08-15,52,AB-,+91-00000-49173,Thiruvananthapuram,None known,2023-03-04
P00074,Gagan Biswas,M,1968-08-11,56,B-,+91-00000-47082,Kollam,None known,2023-01-14
P00075,Dev Kari,M,1953-08-07,71,AB-,+91-00000-84615,Kottayam,None known,2022-10-24
P00076,Wakeeta Borah,F,1978-06-17,47,B-,+91-00000-57915,Thiruvananthapuram,None known,2022-02-21
P00077,Logan Kala,M,2009-01-04,16,A+,+91-00000-87482,Kottayam,None known,2023-07-19
P00078,Ishani Babu,F,2023-10-14,1,A+,+91-00000-84378,Pathanamthitta,None known,2022-03-20
P00079,Bhavya Luthra,F,1970-02-11,55,B+,+91-00000-45867,Kanyakumari,None known,2023-02-28
P00080,Samesh Sehgal,M,2024-03-15,1,AB+,+91-00000-74095,Kottayam,None known,2021-11-23
P00081,Jeet Bhasin,M,1954-08-26,70,A+,+91-00000-74705,Alappuzha,Penicillin,2021-10-13
P00082,Arin Goda,M,2014-07-20,11,A-,+91-00000-21698,Alappuzha,Penicillin,2022-03-31
P00085,Radhika Devi,F,2014-06-20,11,AB-,+91-00000-12250,Kottayam,None known,2021-10-18
P00087,Ekaraj Banerjee,M,1960-05-07,65,O-,+91-00000-92150,Kottayam,Penicillin,2022-09-12
P00088,Adya Soman,F,1935-12-06,89,AB+,+91-00000-62353,Thiruvananthapuram,None known,2023-08-31
P00089,Rachita Muni,F,1973-08-29,51,AB+,+91-00000-11425,Alappuzha,None known,2022-10-12
P00090,Anay Bail,M,1946-05-19,79,B-,+91-00000-28971,Pathanamthitta,None known,2023-09-03
P00091,Bishakha Subramaniam,F,1968-05-16,57,A+,+91-00000-10178,Kollam,None known,2021-09-26
P00092,Bhavna Mukhopadhyay,F,1984-11-25,40,AB-,+91-00000-20860,Kanyakumari,Sulfa drugs,2022-07-08
P00093,Odika Deshpande,F,2010-08-07,14,B+,+91-00000-67696,Kollam,None known,2022-07-08
P00094,Balhaar Borra,M,1960-02-24,65,O-,+91-00000-63144,Thiruvananthapuram,Penicillin,2023-03-08
P00095,Varsha Pillai,F,2018-05-27,7,A-,+91-00000-98586,Alappuzha,None known,2022-03-17
P00096,Anya Dayal,F,1983-03-01,42,B+,+91-00000-70042,Thiruvananthapuram,None known,2022-04-25
P00098,Brijesh Solanki,M,2022-03-01,3,AB-,+91-00000-93928,Pathanamthitta,None known,2021-09-21
P00099,Brinda Sahni,F,2000-08-12,24,A+,+91-00000-33576,Kollam,None known,2023-12-09
P00100,Amruta Tata,F,2002-05-22,23,A-,+91-00000-63325,Thiruvananthapuram,None known,2021-09-24
P00101,Advika Raja,F,2008-08-03,16,A-,+91-00000-73274,Pathanamthitta,None known,2022-04-18
P00102,Sachi Arora,F,1981-08-25,43,O+,+91-00000-44172,Pathanamthitta,None known,2023-01-30
P00103,Bimala Buch,F,1978-11-12,46,B-,+91-00000-48466,Thiruvananthapuram,NSAIDs,2022-01-15
P00104,Chandani D’Alia,F,1973-02-01,52,A+,+91-00000-85255,Kanyakumari,None known,2022-08-05
P00105,Lavanya Saha,F,1947-06-26,78,A+,+91-00000-42060,Alappuzha,Sulfa drugs,2022-11-14
P00106,Noah Rama,M,1963-03-20,62,AB-,+91-00000-26256,Alappuzha,None known,2023-05-16
P00107,Veer Sastry,M,2016-04-25,9,B-,+91-00000-88840,Kollam,None known,2021-09-23
P00108,Vihaan Chacko,M,1984-05-05,41,A+,+91-00000-88326,Kottayam,None known,2022-10-07
P00109,Yochana Varkey,F,1940-03-04,85,A-,+91-00000-90638,Kottayam,None known,2023-08-06
P00110,Alexander Mukherjee,M,2022-05-20,3,A-,+91-00000-32765,Pathanamthitta,None known,2023-09-03
P00111,Chameli Srivastava,F,1970-08-23,54,A+,+91-00000-62845,Alappuzha,NSAIDs,2023-10-03
P00113,Daksh Tank,M,1961-11-08,63,A-,+91-00000-65096,Thiruvananthapuram,None known,2023-11-21
P00114,Xavier Kumer,M,1967-10-01,57,B-,+91-00000-49944,Kottayam,None known,2023-05-10
P00115,Aashi Pillai,F,1948-12-06,76,B+,+91-00000-78972,Kollam,Penicillin,2023-03-08
P00116,Matthew Dhar,M,2014-10-15,10,A-,+91-00000-83919,Kollam,None known,2022-03-21
P00117,Isha Vasa,F,1961-11-10,63,A+,+91-00000-26226,Kottayam,Sulfa drugs,2022-10-08
P00118,Frado Oommen,M,1992-04-29,33,B+,+91-00000-67772,Alappuzha,None known,2022-12-05
P00120,Kavya Narain,F,1956-04-26,69,B-,+91-00000-56419,Alappuzha,None known,2023-07-23
P00121,Tanmayi Krishna,F,1972-04-24,53,O+,+91-00000-95211,Thiruvananthapuram,None known,2022-01-02
P00122,Hardik Sankar,M,1942-08-17,82,AB-,+91-00000-64417,Thiruvananthapuram,None known,2023-06-01
P00123,Irya Kala,F,2012-11-07,12,O-,+91-00000-45821,Pathanamthitta,None known,2023-09-19
P00124,Sanaya Kanda,F,1955-08-29,69,AB+,+91-00000-46285,Kollam,None known,2022-09-29
P00125,Nitara Kadakia,F,1974-07-28,51,O-,+91-00000-80419,Pathanamthitta,None known,2021-10-15
P00126,Ekanta Desai,F,1956-04-01,69,A+,+91-00000-46582,Kanyakumari,Penicillin,2023-12-17
P00127,Yuvraj Panchal,M,2005-07-22,20,AB-,+91-00000-17892,Kollam,None known,2022-06-25
P00128,Anusha Bhatt,F,1986-11-06,38,O-,+91-00000-76273,Kanyakumari,None known,2021-12-14
P00129,Manya Gara,F,1940-10-01,84,A-,+91-00000-40847,Kanyakumari,None known,2022-07-04
P00130,Dayita Seshadri,F,1991-10-03,33,AB-,+91-00000-44253,Thiruvananthapuram,None known,2022-05-14
P00132,Jalsa Sachdev,F,1979-06-23,46,B+,+91-00000-33359,Kottayam,Penicillin,2022-06-01
P00133,Rayaan Venkatesh,M,2014-06-30,11,B-,+91-00000-91421,Kanyakumari,None known,2021-11-07
P00134,Xiti Murty,F,1976-01-19,49,O-,+91-00000-42524,Kollam,None known,2022-02-07
P00135,Upkaar Nagi,M,1978-01-25,47,AB+,+91-00000-15520,Kollam,None known,2021-12-03
P00136,Bishakha Balay,F,1998-07-24,27,AB+,+91-00000-63720,Kottayam,None known,2023-10-14
P00137,Maya Barman,F,1988-07-10,37,AB+,+91-00000-48758,Pathanamthitta,None known,2022-06-29
P00138,Logan Pandya,M,1963-02-26,62,B-,+91-00000-90071,Kollam,None known,2023-08-04
P00139,Nilima Bahl,F,1965-12-09,59,A-,+91-00000-37960,Alappuzha,None known,2021-11-06
P00140,Ekanta Ravel,F,1980-11-26,44,AB+,+91-00000-62457,Kollam,NSAIDs,2022-09-24
P00141,Vasana Gupta,F,1949-11-30,75,AB+,+91-00000-80821,Alappuzha,None known,2023-11-02
P00142,Amaira Lata,F,1953-11-13,71,A+,+91-00000-44384,Kottayam,None known,2022-06-14
P00143,Kashish Dhaliwal,F,2015-05-04,10,B-,+91-00000-27968,Kollam,None known,2023-12-26
P00144,Arjun D’Alia,M,1963-02-18,62,O-,+91-00000-78065,Kanyakumari,None known,2023-03-12
P00145,Vansha Chopra,F,2018-10-30,6,A+,+91-00000-14164,Kollam,None known,2022-11-21
P00146,Qarin Brahmbhatt,M,2019-02-10,6,AB-,+91-00000-97316,Alappuzha,None known,2023-06-20
P00147,Hardik Iyengar,M,2021-03-26,4,B+,+91-00000-48282,Pathanamthitta,None known,2022-04-30
P00148,Wazir Kunda,M,2021-10-03,3,O+,+91-00000-49071,Kanyakumari,None known,2021-08-25
P00149,Gaurav Apte,M,2022-03-21,3,O-,+91-00000-21782,Alappuzha,None known,2022-12-10
P00150,Warinder Warrior,M,1952-11-24,72,O-,+91-00000-39049,Kollam,None known,2023-06-23
P00151,Anita Gola,F,1985-02-03,40,A-,+91-00000-29764,Alappuzha,Sulfa drugs,2023-04-27
P00153,Oscar Zacharia,M,1970-03-25,55,B+,+91-00000-13083,Thiruvananthapuram,None known,2023-02-18
P00154,Yoshita Tella,F,1956-09-10,68,AB-,+91-00000-60385,Kottayam,None known,2023-01-09
P00156,Isaac Chahal,M,1953-07-17,72,A+,+91-00000-99577,Kottayam,None known,2023-03-05
P00157,Tripti Rama,F,2018-03-04,7,AB+,+91-00000-43836,Kanyakumari,None known,2023-05-20
P00158,Dhruv Seshadri,M,2016-08-22,8,B+,+91-00000-91839,Kottayam,None known,2023-04-20
P00159,Vasana Hegde,F,1954-08-14,70,A-,+91-00000-99987,Kollam,None known,2021-09-23
P00160,Aarush Puri,M,1986-01-20,39,A-,+91-00000-47448,Pathanamthitta,Penicillin,2022-08-23
P00161,Yashasvi Oza,F,1991-11-06,33,A+,+91-00000-18288,Thiruvananthapuram,None known,2022-01-24
P00162,Vincent Narain,M,1949-07-17,76,A+,+91-00000-91471,Alappuzha,None known,2023-11-22
P00164,David Kala,M,2019-08-26,5,A+,+91-00000-91656,Kanyakumari,None known,2021-10-17
P00165,Jairaj Ramakrishnan,M,1995-03-30,30,A+,+91-00000-11797,Alappuzha,Sulfa drugs,2022-02-04
P00166,Caleb Mukherjee,M,1990-01-11,35,A+,+91-00000-16383,Kollam,None known,2021-08-07
P00167,Oeshi Lala,F,1989-01-01,36,B-,+91-00000-13475,Kottayam,None known,2023-07-24
P00168,Abhiram Pall,M,1951-04-14,74,A-,+91-00000-90971,Alappuzha,None known,2022-06-04
P00169,Yashawini Butala,F,1993-12-12,31,A+,+91-00000-24040,Kottayam,None known,2022-09-03
P00170,Anirudh Sastry,M,1954-10-20,70,A+,+91-00000-45884,Kanyakumari,None known,2023-04-10
P00172,Laksh Sura,M,2008-05-12,17,AB+,+91-00000-63551,Alappuzha,None known,2022-11-17
P00173,Akshay Kamdar,M,2020-02-29,5,AB+,+91-00000-48116,Kollam,None known,2022-06-10
P00174,Bhavika Sanghvi,F,2013-10-19,11,B+,+91-00000-98451,Thiruvananthapuram,None known,2023-01-13
P00175,Anika Ghose,F,1988-04-11,37,B+,+91-00000-57777,Thiruvananthapuram,None known,2023-04-19
P00176,Zinal Nayak,F,1975-11-27,49,A-,+91-00000-63547,Pathanamthitta,NSAIDs,2023-12-22
P00177,Ekaraj Singhal,M,1997-11-08,27,O-,+91-00000-57799,Kanyakumari,None known,2023-01-18
P00178,Falguni Varty,F,2003-03-11,22,B-,+91-00000-37998,Kanyakumari,None known,2023-06-13
P00179,Yochana Sarraf,F,1999-04-26,26,B-,+91-00000-23870,Kollam,None known,2022-12-30
P00180,Xiti Chadha,F,2019-12-26,5,B+,+91-00000-52139,Kottayam,None known,2023-12-25
P00181,Indrajit Sarna,M,2002-12-16,22,AB-,+91-00000-38787,Alappuzha,None known,2021-11-07
P00182,Maanav Gala,M,1990-04-25,35,B-,+91-00000-78824,Thiruvananthapuram,None known,2021-12-29
P00183,Yutika Varkey,F,1982-09-17,42,B-,+91-00000-67601,Kanyakumari,None known,2022-08-17
P00186,Max Dhaliwal,M,1987-03-19,38,B-,+91-00000-34680,Kanyakumari,None known,2022-06-30
P00187,Laban Tank,M,1941-06-13,84,AB+,+91-00000-34500,Kanyakumari,None known,2021-09-18
P00188,Irya Roy,F,1957-05-02,68,O+,+91-00000-54882,Pathanamthitta,None known,2021-10-11
P00190,Aahana Purohit,F,1979-06-24,46,AB-,+91-00000-17332,Kottayam,None known,2021-10-22
P00191,Akshay Yohannan,M,1996-04-04,29,O-,+91-00000-25388,Alappuzha,None known,2022-04-26
P00192,Anya Varty,F,1951-06-22,74,AB+,+91-00000-79762,Kanyakumari,None known,2021-08-01
P00193,Sai Dara,M,1944-07-31,81,B-,+91-00000-51331,Kanyakumari,None known,2022-03-12
P00194,Xalak Chander,F,1993-08-05,31,AB-,+91-00000-15420,Kollam,None known,2023-09-19
P00195,Geetika Bhatti,F,1968-07-28,57,B+,+91-00000-36943,Kanyakumari,None known,2021-08-07
P00196,Veer Sachdev,M,2020-12-14,4,B-,+91-00000-90312,Alappuzha,None known,2022-10-05
P00197,Saksham Luthra,M,2023-03-21,2,AB-,+91-00000-85925,Thiruvananthapuram,None known,2023-09-11
P00198,Jatin Solanki,M,1966-01-16,59,AB+,+91-00000-64268,Kottayam,None known,2022-10-13
P00199,Yatin Datta,M,1983-08-26,41,O-,+91-00000-48398,Kanyakumari,None known,2022-02-26
P00200,Omkaar Saraf,M,2007-01-06,18,A-,+91-00000-46480,Pathanamthitta,None known,2021-09-27
P00202,Nitara Chopra,F,1936-09-01,88,A+,+91-00000-71497,Thiruvananthapuram,None known,2023-07-25
P00205,Dhruv Bajaj,M,2022-05-31,3,B+,+91-00000-10472,Kollam,NSAIDs,2021-11-01
P00206,Andrew Hari,M,1940-12-12,84,A+,+91-00000-12070,Pathanamthitta,None known,2021-09-15
P00207,Garima Karan,F,1985-06-10,40,O-,+91-00000-76495,Kottayam,None known,2023-11-07
P00209,Oeshi Pant,F,1993-12-03,31,A+,+91-00000-23676,Kottayam,None known,2023-08-21
P00210,Krisha Tara,F,1995-12-27,29,O+,+91-00000-40000,Kollam,None known,2021-12-24
P00211,Damini Tata,F,1983-01-03,42,B+,+91-00000-74675,Pathanamthitta,Penicillin,2022-03-28
P00212,Darsh Uppal,M,2024-10-17,0,B+,+91-00000-96134,Alappuzha,None known,2022-09-02
P00213,Ladli Hora,F,2021-12-30,3,O-,+91-00000-45050,Kanyakumari,NSAIDs,2023-04-26
P00214,Tejas Bajaj,M,1952-02-04,73,A-,+91-00000-53760,Alappuzha,None known,2023-11-26
P00217,Harsh Walla,M,1985-02-24,40,AB+,+91-00000-89848,Kottayam,None known,2023-02-27
P00218,Ikbal Wagle,M,2000-06-27,25,B+,+91-00000-37958,Pathanamthitta,Sulfa drugs,2023-04-14
P00219,Janaki Deshpande,F,2019-06-07,6,A-,+91-00000-39530,Pathanamthitta,None known,2023-12-13
P00220,Jackson Palan,M,1998-06-26,27,AB-,+91-00000-16284,Alappuzha,NSAIDs,2023-10-22
P00221,Hemangini Mutti,F,1985-10-05,39,O+,+91-00000-72805,Alappuzha,None known,2022-02-19
P00222,Nisha Hayer,F,2015-01-09,10,AB-,+91-00000-98760,Alappuzha,None known,2022-10-17
P00223,Ikbal Hayer,M,2019-08-13,5,B+,+91-00000-25517,Alappuzha,None known,2022-02-07
P00224,Chasmum Desai,F,1936-01-10,89,B-,+91-00000-80297,Kollam,None known,2023-08-10
P00225,Jagdish Deo,M,1964-04-22,61,AB-,+91-00000-74700,Alappuzha,None known,2022-08-10
P00226,Chaitanya Lad,M,1942-04-27,83,O+,+91-00000-55385,Kollam,None known,2022-12-25
P00227,Rishi Chatterjee,M,1983-01-27,42,A+,+91-00000-72976,Kanyakumari,None known,2023-02-14
P00228,Teerth Sama,M,1976-01-02,49,O+,+91-00000-43692,Thiruvananthapuram,None known,2022-12-25
P00229,Edhitha Iyer,F,1951-10-24,73,A+,+91-00000-64232,Kottayam,None known,2022-12-15
P00230,Tamanna Badami,F,1992-08-13,32,O-,+91-00000-75617,Kollam,None known,2022-01-30
P00231,Chanakya Iyer,M,1997-05-09,28,AB-,+91-00000-56765,Pathanamthitta,None known,2023-05-08
P00232,Praneel Patel,M,1995-05-26,30,A+,+91-00000-34918,Kottayam,None known,2023-01-03
P00233,Dalbir Tiwari,M,1961-09-26,63,O-,+91-00000-24473,Kollam,None known,2023-12-26
P00234,Onveer Thakkar,M,1990-10-13,34,A+,+91-00000-44421,Alappuzha,None known,2023-04-11
P00236,Wridesh Cherian,M,1973-02-25,52,O+,+91-00000-65983,Pathanamthitta,Penicillin,2023-05-21
P00237,Advik Barad,M,1983-10-13,41,B-,+91-00000-40433,Thiruvananthapuram,Penicillin,2023-09-25
P00238,Yasti Srivastava,F,1955-10-20,69,B+,+91-00000-35598,Pathanamthitta,None known,2023-01-18
P00240,Hiral Contractor,F,1984-08-02,40,B+,+91-00000-64693,Kollam,None known,2023-07-02
P00241,Ishani Gera,F,1976-05-22,49,O-,+91-00000-43562,Pathanamthitta,None known,2022-01-27
P00242,Gaurangi Mandal,F,1935-01-04,90,O+,+91-00000-89814,Alappuzha,Sulfa drugs,2022-02-12
P00243,Charvi Bhatia,F,1954-11-13,70,A+,+91-00000-14174,Thiruvananthapuram,None known,2023-03-16
P00245,Brinda Chatterjee,F,1993-01-30,32,A-,+91-00000-11959,Kollam,None known,2023-11-28
P00246,Nihal Raman,M,1973-12-11,51,AB+,+91-00000-64289,Kollam,None known,2023-08-15
P00247,Vivaan Sandhu,M,1979-04-27,46,AB+,+91-00000-98879,Kanyakumari,NSAIDs,2023-04-24
P00248,Yasti Pant,F,1971-04-29,54,O-,+91-00000-40437,Thiruvananthapuram,None known,2022-08-12
P00249,Upasna Kade,F,2019-10-17,5,B+,+91-00000-20298,Kanyakumari,None known,2023-05-10
P00251,Anusha Iyer,F,1955-01-23,70,O-,+91-00000-83694,Kottayam,None known,2022-09-15
P00252,Hemangini Reddy,F,1975-12-26,49,A+,+91-00000-28804,Thiruvananthapuram,None known,2023-08-05
P00253,Vasana Parsa,F,2018-05-09,7,B-,+91-00000-15608,Kollam,None known,2023-08-30
P00254,Qasim Ravi,M,1937-02-02,88,B-,+91-00000-25747,Pathanamthitta,None known,2021-08-07
P00255,Gunbir Gandhi,M,2024-02-05,1,A+,+91-00000-86344,Thiruvananthapuram,None known,2022-07-25
P00256,Champak Vala,M,1971-06-15,54,B+,+91-00000-95665,Kollam,None known,2023-10-29
P00257,Abhimanyu Naik,M,2007-08-31,17,B+,+91-00000-48591,Alappuzha,NSAIDs,2022-10-02
P00258,Chaman Ravel,F,2019-11-22,5,O+,+91-00000-67527,Kottayam,None known,2022-07-08
P00260,Panini Kuruvilla,F,2013-04-27,12,O-,+91-00000-15445,Pathanamthitta,None known,2021-08-30
P00261,Logan Dada,M,1984-05-04,41,B-,+91-00000-28830,Kottayam,Sulfa drugs,2022-04-28
P00262,Fariq Ravi,M,1972-11-22,52,AB+,+91-00000-98822,Kottayam,None known,2022-09-23
P00263,Ekalinga Narayan,M,2009-03-24,16,A-,+91-00000-30658,Kanyakumari,None known,2023-03-31
P00264,Qasim Sankaran,M,2014-10-08,10,B+,+91-00000-75172,Kanyakumari,None known,2022-03-20
P00266,Ishanvi Goyal,F,2015-02-28,10,AB-,+91-00000-16590,Thiruvananthapuram,None known,2021-10-18
P00267,Bimala Om,F,1970-03-24,55,AB+,+91-00000-92992,Kottayam,None known,2022-11-05
P00268,Matthew Singh,M,2020-05-03,5,O-,+91-00000-51420,Kanyakumari,None known,2022-08-18
P00269,Chandresh Anne,M,1966-03-03,59,A+,+91-00000-99799,Kollam,None known,2021-10-08
P00270,Rachana Bawa,F,2000-07-02,25,O+,+91-00000-77084,Kanyakumari,None known,2022-09-20
P00271,Kala Mahajan,F,1935-09-03,89,A+,+91-00000-24336,Pathanamthitta,None known,2021-08-06
P00272,Mason Nazareth,M,1990-07-30,34,A+,+91-00000-97703,Thiruvananthapuram,None known,2021-08-10
P00274,Hemani Walia,F,1939-09-09,85,B+,+91-00000-30092,Kottayam,None known,2023-02-26
P00275,Brinda Ramachandran,F,1996-02-07,29,B-,+91-00000-17116,Thiruvananthapuram,None known,2022-07-19
P00277,Jalsa Dar,F,2000-11-24,24,AB+,+91-00000-47788,Kollam,Sulfa drugs,2023-01-08
P00278,Siya Bajaj,F,2022-01-19,3,O-,+91-00000-79063,Kanyakumari,Penicillin,2022-11-17
P00279,Deepa Chokshi,F,1992-05-25,33,A-,+91-00000-66752,Alappuzha,None known,2021-11-26
P00280,Jagat Kunda,M,1935-10-14,89,A-,+91-00000-11604,Kottayam,None known,2023-07-06
P00281,Tristan Ratti,M,2012-09-25,12,B-,+91-00000-45148,Kanyakumari,None known,2022-01-23
P00282,Zayyan Bedi,M,1952-04-28,73,O-,+91-00000-17351,Kottayam,None known,2024-01-13
P00283,Guneet Prashad,M,1950-11-24,74,AB+,+91-00000-62824,Kanyakumari,None known,2022-02-17
P00284,Aashi Chaudhari,F,2005-03-20,20,O+,+91-00000-84752,Alappuzha,None known,2023-12-29
P00285,Leela Krishna,F,1982-04-14,43,AB+,+91-00000-73786,Kottayam,None known,2022-04-02
P00286,Lakshit Om,M,1988-01-05,37,AB+,+91-00000-43740,Thiruvananthapuram,None known,2022-01-20
P00287,Yashoda Sagar,F,1993-12-07,31,A-,+91-00000-51358,Kollam,NSAIDs,2023-12-23
P00288,Chandresh Saxena,M,2018-09-03,6,AB-,+91-00000-96413,Alappuzha,None known,2021-10-18
P00290,Reyansh Dutta,M,1946-10-23,78,A-,+91-00000-12193,Alappuzha,None known,2021-11-22
P00291,Reyansh Sodhi,M,2002-02-21,23,AB+,+91-00000-66837,Thiruvananthapuram,None known,2022-05-29
P00292,Frado Tandon,M,2025-01-13,0,AB-,+91-00000-42973,Pathanamthitta,Penicillin,2022-11-24
P00294,Yug Salvi,M,1996-08-20,28,AB-,+91-00000-47898,Alappuzha,None known,2023-10-07
P00295,Lucky Vyas,M,1977-10-12,47,O+,+91-00000-48041,Pathanamthitta,None known,2021-11-29
P00296,Sudiksha Muni,F,2006-08-04,18,B-,+91-00000-38313,Alappuzha,None known,2023-08-19
P00297,Qadim Wali,M,2019-12-29,5,A-,+91-00000-29477,Pathanamthitta,NSAIDs,2023-05-05
P00298,Mekhala Subramanian,F,1962-04-28,63,O-,+91-00000-12740,Alappuzha,None known,2022-02-02
P00299,Krishna Mander,M,1988-08-03,36,B-,+91-00000-54179,Kollam,None known,2022-01-27
P00300,Manbir Bala,M,1935-10-03,89,B-,+91-00000-39281,Kottayam,None known,2022-05-09
P00301,Abhimanyu Konda,M,1944-12-25,80,A-,+91-00000-33018,Kollam,Sulfa drugs,2022-02-21
P00303,Tara Ramakrishnan,F,2003-08-10,21,O+,+91-00000-22480,Pathanamthitta,None known,2022-05-18
P00304,Avni Murty,F,1948-06-15,77,A-,+91-00000-12740,Kanyakumari,NSAIDs,2023-07-19
P00305,Rushil Bedi,M,2017-06-23,8,AB-,+91-00000-47885,Kollam,Penicillin,2023-12-25
P00306,Nathaniel Borah,M,1984-02-26,41,O-,+91-00000-11965,Thiruvananthapuram,None known,2023-03-04
P00307,Jasmit Sanghvi,F,2009-06-03,16,AB-,+91-00000-98789,Kottayam,None known,2023-03-02
P00308,Waida Krishna,F,1978-12-31,46,A-,+91-00000-57481,Kottayam,None known,2022-09-23
P00309,Keya Bath,F,1948-03-14,77,O+,+91-00000-48822,Pathanamthitta,None known,2023-12-14
P00310,Yutika Chaudhari,F,1968-01-26,57,AB-,+91-00000-58668,Kanyakumari,None known,2023-10-15
P00311,Vinaya Dhawan,F,1958-06-27,67,B+,+91-00000-42365,Kottayam,None known,2022-07-08
P00312,Jason Contractor,M,2018-10-29,6,B-,+91-00000-19902,Kottayam,None known,2024-01-02
P00314,Vedant Dalal,M,1991-08-28,33,B-,+91-00000-85728,Kanyakumari,NSAIDs,2023-12-28
P00315,Harsh Ben,M,2025-01-29,0,A+,+91-00000-83237,Kottayam,None known,2022-04-03
P00316,Rachana Wable,F,1939-05-17,86,O+,+91-00000-55065,Thiruvananthapuram,None known,2021-10-28
P00317,Faras Dash,M,2007-08-27,17,B-,+91-00000-43990,Kanyakumari,None known,2023-02-22
P00318,Rajata Savant,F,1964-10-18,60,O-,+91-00000-60180,Kanyakumari,None known,2022-12-15
P00319,Ekiya Saha,F,1996-03-25,29,O-,+91-00000-45448,Kollam,None known,2023-11-09
P00320,Vasatika Lala,F,1991-09-06,33,A-,+91-00000-51935,Alappuzha,None known,2023-11-16
P00321,Shaurya Patla,M,2019-06-26,6,B+,+91-00000-13660,Pathanamthitta,NSAIDs,2022-12-31
P00322,Zilmil Devan,F,1961-04-21,64,O+,+91-00000-75496,Kanyakumari,Sulfa drugs,2022-04-14
P00323,Mohini Dave,F,1994-10-22,30,O+,+91-00000-27042,Kollam,None known,2022-09-23
P00324,Jagdish Srivastava,M,1968-07-06,57,B-,+91-00000-18794,Kollam,None known,2023-08-02
P00325,Dakshesh Thakur,M,1958-05-22,67,B+,+91-00000-16116,Kollam,None known,2022-05-09
P00326,Nilima Tripathi,F,1999-12-07,25,B+,+91-00000-67276,Kollam,None known,2022-03-31
P00327,Praneel Maharaj,M,1960-01-07,65,A+,+91-00000-59567,Kottayam,None known,2023-10-09
P00328,Madhavi Gupta,F,2019-04-12,6,B-,+91-00000-11218,Alappuzha,Sulfa drugs,2021-08-26
P00329,Maya Khatri,F,1956-05-14,69,A-,+91-00000-58772,Kanyakumari,None known,2022-03-18
P00330,Ikshita Kothari,F,1988-08-03,36,A+,+91-00000-92323,Alappuzha,None known,2021-11-23
P00331,Zayan Hayre,M,1971-10-03,53,O-,+91-00000-40690,Alappuzha,None known,2022-06-09
P00332,Anusha Bhat,F,1981-08-28,43,O+,+91-00000-66927,Kanyakumari,Sulfa drugs,2023-04-04
P00333,Aayush Madan,M,2010-08-15,14,O+,+91-00000-44414,Kollam,None known,2022-08-15
P00334,Leela Sandal,F,1948-01-25,77,B-,+91-00000-10143,Thiruvananthapuram,None known,2022-02-10
P00335,Amara Barad,F,1986-06-25,39,A-,+91-00000-40469,Alappuzha,None known,2022-01-06
P00336,Charan Kapadia,M,1981-03-28,44,B-,+91-00000-70683,Kottayam,NSAIDs,2023-08-13
P00337,Maya Bora,F,1998-12-22,26,A-,+91-00000-34020,Kottayam,None known,2022-06-08
P00338,Caleb Dyal,M,1985-06-08,40,O+,+91-00000-28229,Alappuzha,None known,2022-02-14
P00339,Kamya Prakash,F,1938-07-11,87,O+,+91-00000-72394,Kollam,None known,2023-12-16
P00340,Warhi Srinivas,F,2003-06-07,22,B-,+91-00000-25772,Pathanamthitta,None known,2022-11-05
P00341,Peter Kade,M,1958-03-11,67,AB-,+91-00000-47492,Kanyakumari,None known,2022-09-23
P00342,Omkaar Oza,M,1949-10-03,75,A+,+91-00000-76901,Pathanamthitta,None known,2022-07-13
P00343,Yug Deol,M,1969-06-25,56,AB-,+91-00000-89753,Kottayam,None known,2021-10-14
P00344,Baljiwan Dar,M,1977-01-29,48,B+,+91-00000-25428,Thiruvananthapuram,None known,2022-07-18
P00345,Udarsh Kala,M,2024-05-29,1,AB+,+91-00000-29415,Alappuzha,None known,2023-03-03
P00346,Vamakshi Samra,F,2019-11-15,5,A+,+91-00000-27338,Kollam,None known,2023-09-21
P00347,Leela Ramakrishnan,F,2003-02-04,22,AB-,+91-00000-34006,Kottayam,None known,2023-04-02
P00348,Forum Pillay,F,1951-10-27,73,O+,+91-00000-95456,Pathanamthitta,None known,2022-11-30
P00349,Faraj Nanda,M,1969-02-25,56,A-,+91-00000-37324,Kanyakumari,None known,2022-11-12
P00350,Maanav Gour,M,1968-07-12,57,AB+,+91-00000-28341,Kottayam,None known,2022-07-05
P00351,Unni Pingle,F,1996-09-24,28,O-,+91-00000-41781,Pathanamthitta,None known,2021-08-09
P00352,Chasmum Shere,F,2014-03-25,11,A+,+91-00000-41908,Alappuzha,None known,2021-09-01
P00353,Ojasvi Brar,F,1984-04-04,41,AB+,+91-00000-26860,Thiruvananthapuram,None known,2022-05-13
P00354,Benjamin Sankaran,M,1940-01-13,85,AB+,+91-00000-94980,Pathanamthitta,None known,2021-11-06
P00355,Xavier Sheth,M,1965-10-19,59,O-,+91-00000-98634,Kollam,None known,2022-12-16
P00356,Netra Andra,F,2005-04-26,20,O-,+91-00000-87546,Alappuzha,None known,2022-01-29
P00357,Baljiwan Mukherjee,M,1973-11-23,51,AB+,+91-00000-22375,Thiruvananthapuram,None known,2022-01-29
P00359,Nidra Talwar,F,2020-06-07,5,O+,+91-00000-41741,Alappuzha,None known,2022-05-12
P00360,Nihal Mandal,M,1987-01-28,38,O-,+91-00000-27470,Pathanamthitta,NSAIDs,2021-12-01
P00361,Eshana Kanda,F,2000-04-25,25,B+,+91-00000-76047,Thiruvananthapuram,None known,2022-11-21
P00362,Praneel Narain,M,1988-06-17,37,AB-,+91-00000-94640,Thiruvananthapuram,None known,2023-09-02
P00363,Qadim Dalal,M,1999-11-04,25,AB-,+91-00000-22107,Kollam,None known,2021-08-16
P00364,Ojasvi Sastry,F,2022-10-04,2,O-,+91-00000-92368,Kottayam,None known,2023-10-01
P00365,Maya Sarma,F,2007-04-06,18,B+,+91-00000-55614,Pathanamthitta,Sulfa drugs,2021-11-30
P00366,Zilmil Mody,F,1980-12-22,44,AB-,+91-00000-15456,Pathanamthitta,None known,2022-02-23
P00367,Veer Nadkarni,M,1972-07-30,53,AB+,+91-00000-95344,Alappuzha,None known,2022-09-15
P00368,Indrajit Ratta,M,1995-09-30,29,AB+,+91-00000-94654,Thiruvananthapuram,None known,2023-07-31
P00369,Yauvani Kothari,F,2019-01-21,6,B+,+91-00000-41608,Pathanamthitta,Penicillin,2021-11-12
P00370,Brijesh Pathak,M,1977-12-09,47,B-,+91-00000-84298,Kanyakumari,None known,2023-08-11
P00372,Rajata Randhawa,F,2002-02-15,23,A+,+91-00000-17718,Kottayam,NSAIDs,2022-12-21
P00373,Rishi Hayer,M,1996-03-29,29,A+,+91-00000-20934,Kollam,None known,2022-12-24
P00374,Raksha Ramakrishnan,F,1941-12-20,83,AB-,+91-00000-56542,Thiruvananthapuram,None known,2023-10-05
P00375,Garima Goel,F,1988-05-01,37,B-,+91-00000-36287,Kollam,None known,2022-10-03
P00377,Vasana Manda,F,1988-09-26,36,A-,+91-00000-19344,Alappuzha,None known,2022-11-28
P00378,Alka Kant,F,1986-07-02,39,O-,+91-00000-64047,Pathanamthitta,Penicillin,2023-03-23
P00379,Ayush Dutt,M,1972-08-20,52,O+,+91-00000-54001,Kottayam,None known,2021-10-22
P00380,Manbir Bains,M,2019-02-18,6,A+,+91-00000-25062,Kollam,None known,2021-10-14
P00381,Siddharth Bhatt,M,1942-08-05,83,AB-,+91-00000-80251,Kottayam,None known,2023-12-22
P00382,Michael Chad,M,1940-06-20,85,B-,+91-00000-60617,Pathanamthitta,None known,2022-12-12
P00384,Mahika Cheema,F,1996-11-17,28,B+,+91-00000-93075,Pathanamthitta,None known,2024-01-08
P00385,Naksh Chad,M,1983-06-18,42,A-,+91-00000-70508,Kanyakumari,None known,2022-05-23
P00386,Amara Dhawan,F,2003-02-01,22,A+,+91-00000-23675,Kottayam,None known,2022-09-29
P00387,Chasmum Sami,F,1999-04-23,26,B-,+91-00000-60387,Alappuzha,None known,2022-09-18
P00388,Krisha Kannan,F,1998-10-27,26,AB+,+91-00000-42039,Kollam,None known,2022-03-28
P00389,Yash Vig,M,1943-09-08,81,O+,+91-00000-26975,Thiruvananthapuram,None known,2021-12-28
P00390,Pallavi Sharaf,F,1992-03-14,33,B+,+91-00000-68259,Pathanamthitta,Sulfa drugs,2022-09-19
P00391,Ronith Palla,M,1940-11-13,84,B-,+91-00000-93793,Kollam,None known,2023-04-27
P00392,Pahal Natarajan,F,1941-08-14,83,A-,+91-00000-95931,Pathanamthitta,Sulfa drugs,2022-02-18
P00394,Yagnesh Yogi,M,1945-01-12,80,AB-,+91-00000-36885,Kollam,None known,2022-10-20
P00395,Balhaar Batra,M,2015-03-18,10,AB+,+91-00000-27981,Kollam,None known,2021-09-28
P00396,Tripti Palla,F,1944-03-03,81,A+,+91-00000-56435,Thiruvananthapuram,None known,2022-04-01
P00397,Aadhya Radhakrishnan,F,2003-08-17,21,AB-,+91-00000-89457,Alappuzha,None known,2021-10-05
P00399,Amaira Viswanathan,F,1975-09-27,49,AB+,+91-00000-70593,Kanyakumari,None known,2022-01-20
P00400,Pratyush Anne,M,1987-02-17,38,O-,+91-00000-18467,Kanyakumari,None known,2022-06-05
P00401,Christopher Sama,M,2021-01-18,4,O+,+91-00000-54494,Kottayam,None known,2022-06-04
P00402,Shivansh Dhingra,M,2016-12-19,8,O-,+91-00000-54426,Alappuzha,None known,2022-04-29
P00403,Jason Gaba,M,2021-02-24,4,A+,+91-00000-50712,Kanyakumari,None known,2023-11-20
P00404,Riya Ganesh,F,2019-10-03,5,B+,+91-00000-91827,Alappuzha,NSAIDs,2022-09-28
P00405,Oeshi Jayaraman,F,1948-12-24,76,A-,+91-00000-19171,Kanyakumari,None known,2023-04-25
P00406,Robert Sandal,M,1997-02-12,28,AB+,+91-00000-43182,Pathanamthitta,None known,2022-05-11
P00407,Zarna Master,F,1977-04-07,48,O+,+91-00000-27210,Thiruvananthapuram,None known,2021-08-21
P00408,Mahika Bhargava,F,2005-08-25,19,O+,+91-00000-71264,Kanyakumari,None known,2023-02-13
P00409,Vrishti Morar,F,1980-12-30,44,O-,+91-00000-47639,Kanyakumari,None known,2023-01-23
P00410,Deepa Mitter,F,2010-06-01,15,B+,+91-00000-87204,Alappuzha,None known,2022-09-19
P00411,Faras Gola,M,1968-03-15,57,AB+,+91-00000-21077,Kollam,None known,2023-08-18
P00412,Azaan Shanker,M,1975-10-24,49,B-,+91-00000-50167,Kollam,Penicillin,2022-11-01
P00413,Adweta Srivastava,F,2006-03-21,19,A+,+91-00000-40471,Pathanamthitta,None known,2023-05-10
P00415,Chatura Hora,M,1965-06-21,60,B-,+91-00000-16072,Kollam,None known,2023-05-16
P00416,George Parmer,M,1993-06-28,32,A+,+91-00000-67874,Thiruvananthapuram,None known,2022-10-22
P00417,Ikbal Keer,M,1953-08-04,72,A-,+91-00000-80332,Kollam,None known,2023-08-23
P00418,Warinder Trivedi,M,2014-03-29,11,B+,+91-00000-76756,Kanyakumari,None known,2022-11-15
P00419,Isaac Sathe,M,1964-01-16,61,AB+,+91-00000-32288,Thiruvananthapuram,None known,2022-06-20
P00420,George Mand,M,1991-09-20,33,AB-,+91-00000-64561,Thiruvananthapuram,None known,2023-08-28
P00421,Tamanna Gera,F,2005-09-27,19,O-,+91-00000-69174,Kollam,None known,2022-08-31
P00423,Leena Sundaram,F,1978-03-04,47,O-,+91-00000-66508,Pathanamthitta,None known,2021-11-19
P00424,Tamanna Oommen,F,2020-10-08,4,B+,+91-00000-58025,Alappuzha,None known,2021-12-02
P00425,Chakradhar Subramanian,M,2018-11-28,6,AB-,+91-00000-17211,Thiruvananthapuram,Sulfa drugs,2022-04-19
P00426,Janya Ratta,F,2018-11-02,6,B+,+91-00000-95730,Alappuzha,None known,2023-08-28
P00427,Arya Kalla,F,1963-03-15,62,O+,+91-00000-12946,Kollam,None known,2022-10-31
P00428,Ekani Rajan,F,2024-06-25,1,AB+,+91-00000-83244,Pathanamthitta,None known,2021-09-02
P00429,Laksh Bhardwaj,M,2012-07-07,13,B+,+91-00000-62507,Kollam,None known,2023-01-21
P00430,Jagat Apte,M,1991-09-20,33,O-,+91-00000-44435,Kollam,None known,2021-12-15
P00431,Vrishti Prabhu,F,2012-03-12,13,O+,+91-00000-50701,Kanyakumari,None known,2021-11-17
P00432,Varenya Koshy,F,1968-04-26,57,A+,+91-00000-71284,Pathanamthitta,None known,2023-01-08
P00433,Ucchal Dugar,F,1995-09-11,29,AB+,+91-00000-86304,Kottayam,None known,2023-10-05
P00434,Sarthak Dugar,M,1971-05-08,54,AB+,+91-00000-97166,Thiruvananthapuram,None known,2023-01-05
P00435,Naveen Dhillon,M,1937-11-17,87,O+,+91-00000-98887,Kollam,Penicillin,2021-11-01
P00436,Kai Varty,M,2017-02-11,8,B+,+91-00000-48430,Thiruvananthapuram,Sulfa drugs,2022-12-06
P00437,Ekaja Lata,F,1959-08-14,65,AB+,+91-00000-99433,Pathanamthitta,None known,2024-01-08
P00438,Yauvani Warrior,F,2001-09-28,23,AB-,+91-00000-71755,Kottayam,None known,2023-03-19
P00439,Avi Dora,M,1974-06-10,51,O-,+91-00000-90777,Pathanamthitta,Penicillin,2021-12-04
P00440,Gaurav Agarwal,M,1987-10-20,37,A+,+91-00000-56671,Kollam,None known,2022-08-26
P00441,Ishani Dixit,F,1968-06-01,57,O+,+91-00000-51550,Kottayam,NSAIDs,2023-05-25
P00442,Devansh Butala,M,1945-08-31,79,O-,+91-00000-21869,Kanyakumari,Penicillin,2022-01-25
P00443,Qushi Madan,F,1977-01-11,48,B-,+91-00000-49072,Kollam,None known,2023-08-11
P00445,Wakeeta Sidhu,F,1945-02-06,80,B-,+91-00000-67817,Pathanamthitta,None known,2022-04-27
P00446,Benjamin Toor,M,1965-02-18,60,AB+,+91-00000-88500,Kanyakumari,None known,2023-01-31
P00448,Girindra Saha,M,1978-12-04,46,AB-,+91-00000-93270,Kollam,None known,2022-04-21
P00449,Gopal Chand,M,1985-11-16,39,O-,+91-00000-89646,Kottayam,None known,2022-12-20
P00450,Thomas Joshi,M,1981-10-15,43,AB+,+91-00000-29939,Kanyakumari,None known,2023-10-13
P00451,Anirudh Sachdev,M,2020-07-04,5,A+,+91-00000-74910,Thiruvananthapuram,None known,2023-12-26
P00452,Yug Dugar,M,2022-11-19,2,AB-,+91-00000-90872,Kanyakumari,None known,2022-05-21
P00454,Nachiket Ravi,M,1941-04-12,84,O+,+91-00000-21999,Kottayam,None known,2023-11-20
P00455,Bishakha Mohan,F,1975-07-26,50,O-,+91-00000-14220,Pathanamthitta,None known,2022-09-09
P00456,Vinaya Bhavsar,F,2011-08-26,13,B+,+91-00000-14558,Thiruvananthapuram,None known,2023-12-02
P00457,Pranit Borde,M,1995-02-09,30,A+,+91-00000-70586,Kanyakumari,Penicillin,2022-04-19
P00458,Ekaraj Cherian,M,1972-11-03,52,AB+,+91-00000-12482,Thiruvananthapuram,None known,2023-10-23
P00460,Darsh Saxena,M,2024-07-31,0,A-,+91-00000-51541,Thiruvananthapuram,None known,2021-09-10
P00461,Abeer Purohit,M,1993-02-23,32,A+,+91-00000-70059,Kanyakumari,Sulfa drugs,2023-05-01
P00462,Wazir Khanna,M,1991-08-11,33,A-,+91-00000-78192,Pathanamthitta,Penicillin,2022-01-14
P00463,Manan Comar,M,1975-12-24,49,AB-,+91-00000-20284,Kanyakumari,None known,2023-08-09
P00464,Vasudha Anne,F,2000-07-12,25,A+,+91-00000-83055,Pathanamthitta,None known,2021-12-31
P00466,Mohini Puri,F,1964-11-07,60,A+,+91-00000-39312,Thiruvananthapuram,None known,2023-03-27
P00467,Manthan Nazareth,M,1976-01-02,49,AB-,+91-00000-79667,Pathanamthitta,None known,2023-10-22
P00468,Shivani Chahal,F,1973-08-27,51,O-,+91-00000-42529,Kanyakumari,NSAIDs,2023-08-14
P00470,Irya Puri,F,1978-10-20,46,A-,+91-00000-68805,Kanyakumari,None known,2022-08-05
P00471,Christopher Narayan,M,1959-04-07,66,A-,+91-00000-57730,Pathanamthitta,None known,2021-10-08
P00472,Nilima Mahal,F,1948-06-29,77,B+,+91-00000-99286,Pathanamthitta,None known,2022-03-16
P00473,Vrinda Narula,F,1953-11-20,71,B+,+91-00000-59662,Kollam,None known,2023-02-08
P00474,Vansha Raja,F,1997-10-01,27,A-,+91-00000-72850,Alappuzha,None known,2022-06-12
P00475,Charita Chaudry,F,1973-09-28,51,B-,+91-00000-99018,Alappuzha,None known,2023-01-30
P00476,Ekta Chandra,F,1993-09-23,31,O-,+91-00000-43493,Kottayam,None known,2023-05-13
P00477,Ekaja Gola,F,1985-03-21,40,AB+,+91-00000-25526,Alappuzha,None known,2022-03-31
P00478,Gautam Hans,M,1938-09-06,86,B-,+91-00000-47511,Kanyakumari,None known,2021-12-15
P00479,Sai Bansal,M,1995-04-26,30,B+,+91-00000-24357,Kollam,None known,2022-12-17
P00480,Vedika Chana,F,1992-05-05,33,A+,+91-00000-62451,Kanyakumari,None known,2023-03-24
P00481,Daksha Karan,F,1952-06-13,73,AB-,+91-00000-45385,Alappuzha,None known,2022-11-18
P00483,Diya Saraf,F,1942-05-25,83,B-,+91-00000-40815,Kanyakumari,NSAIDs,2023-08-09
P00486,Yashodhara Dewan,F,1996-01-17,29,O+,+91-00000-98884,Kottayam,None known,2022-02-25
P00487,Harshil Divan,M,1976-05-10,49,O-,+91-00000-67210,Kottayam,None known,2022-02-10
P00488,Sanya Subramanian,F,2017-01-02,8,AB+,+91-00000-23885,Kanyakumari,None known,2022-07-24
P00489,Noah Sachar,M,1950-12-26,74,A+,+91-00000-45056,Kottayam,None known,2022-09-14
P00490,Advika Rattan,F,1966-07-30,59,O-,+91-00000-84730,Thiruvananthapuram,None known,2022-09-12
P00491,Nathan Konda,M,1992-02-04,33,A-,+91-00000-71269,Thiruvananthapuram,None known,2023-11-15
P00492,Aditya Lad,M,1934-11-05,90,O+,+91-00000-80701,Kanyakumari,None known,2022-06-03
P00493,Noah Gulati,M,2018-12-02,6,AB+,+91-00000-74170,Alappuzha,None known,2023-05-22
P00494,Pavani Mohanty,F,1991-11-26,33,B-,+91-00000-77369,Kottayam,None known,2022-12-22
P00496,Ranbir Jayaraman,M,1936-03-15,89,O+,+91-00000-63975,Kollam,None known,2023-06-27
P00497,Ojas Memon,M,2004-08-24,20,A+,+91-00000-72066,Thiruvananthapuram,None known,2021-08-14
P00498,Charan Dutt,M,2011-11-12,13,A+,+91-00000-31965,Pathanamthitta,None known,2022-03-25
P00499,Jonathan Yohannan,M,1993-12-05,31,A+,+91-00000-25636,Kanyakumari,Penicillin,2022-09-25
P00500,Neha Kaur,F,2013-08-04,11,O+,+91-00000-25336,Kollam,None known,2023-07-20
P00501,Qushi Tella,F,1968-01-28,57,B+,+91-00000-92494,Thiruvananthapuram,None known,2022-11-18
P00502,Yashvi Dhar,F,1967-01-17,58,AB+,+91-00000-61166,Alappuzha,None known,2021-09-15
P00503,Ira Varty,F,2010-12-10,14,O-,+91-00000-30824,Thiruvananthapuram,None known,2021-08-24
P00504,Guneet Bala,M,1946-11-23,78,AB-,+91-00000-10821,Alappuzha,None known,2022-10-16
P00505,Ira Chacko,F,1986-03-11,39,AB-,+91-00000-74916,Pathanamthitta,None known,2023-03-17
P00506,Ekanta Konda,F,1936-05-15,89,AB-,+91-00000-38336,Pathanamthitta,None known,2021-12-24
P00507,Waida Sahni,F,1955-07-04,70,O-,+91-00000-70642,Thiruvananthapuram,None known,2022-09-14
P00508,Osha Narayan,F,2007-04-05,18,O+,+91-00000-94856,Kottayam,NSAIDs,2022-05-07
P00509,Chandani Patel,F,2003-02-19,22,A+,+91-00000-39244,Kottayam,None known,2022-06-10
P00510,Kiaan Sheth,M,1984-04-21,41,A-,+91-00000-43861,Pathanamthitta,None known,2022-05-17
P00511,David Sethi,M,1983-02-16,42,B-,+91-00000-10569,Pathanamthitta,None known,2022-04-14
P00513,Bhavika Lalla,F,1982-12-21,42,O-,+91-00000-59836,Kottayam,None known,2022-10-09
P00514,Hamsini Natt,F,1977-02-07,48,B+,+91-00000-98849,Kottayam,None known,2022-04-11
P00515,Elijah Das,M,1951-06-21,74,O-,+91-00000-26047,Kottayam,None known,2021-11-05
P00516,Aadhya Mani,F,1946-10-12,78,B+,+91-00000-61447,Alappuzha,None known,2023-03-26
P00517,Rajata Khosla,F,2004-06-17,21,B+,+91-00000-72085,Alappuzha,None known,2023-05-18
P00518,Pratyush Gandhi,M,1970-05-22,55,B-,+91-00000-11616,Kottayam,None known,2021-09-29
P00519,Idika Bose,F,2001-09-26,23,AB-,+91-00000-35820,Alappuzha,None known,2023-08-21
P00520,Vasana Balay,F,2024-12-27,0,AB+,+91-00000-74771,Kottayam,None known,2022-12-09
P00521,Tamanna Gole,F,1977-05-03,48,A-,+91-00000-48132,Kanyakumari,None known,2023-10-10
P00522,Ekantika Morar,F,1992-09-03,32,AB-,+91-00000-33818,Kottayam,None known,2022-09-08
P00523,Sai Babu,F,1991-07-27,34,AB+,+91-00000-41379,Kottayam,None known,2022-07-09
P00524,Gauri Iyengar,F,1988-02-20,37,O-,+91-00000-82492,Kollam,None known,2023-05-16
P00525,Samesh Sidhu,M,1991-06-13,34,A+,+91-00000-46598,Kollam,None known,2022-08-18
P00526,Amol Dhar,M,2007-04-22,18,O-,+91-00000-18805,Kollam,None known,2023-12-29
P00527,Reyansh Dani,M,1968-04-21,57,AB-,+91-00000-69591,Pathanamthitta,None known,2021-11-10
P00528,Tanmayi Ghose,F,2023-12-17,1,A-,+91-00000-24897,Pathanamthitta,None known,2023-05-03
P00529,Pahal Venkatesh,F,2005-01-14,20,AB-,+91-00000-11391,Kanyakumari,None known,2021-08-18
P00530,Dominic Lall,M,1972-04-01,53,AB+,+91-00000-18147,Kottayam,Sulfa drugs,2023-03-02
P00531,Jairaj Natarajan,M,1984-04-13,41,A+,+91-00000-91154,Alappuzha,None known,2022-02-18
P00532,Avi Barad,M,1962-02-16,63,B+,+91-00000-80927,Kottayam,None known,2022-04-27
P00533,Elijah Rau,M,1975-03-20,50,AB-,+91-00000-19355,Kollam,None known,2023-05-23
P00534,Yadavi Chaudry,F,1993-04-04,32,B+,+91-00000-18707,Thiruvananthapuram,None known,2023-09-04
P00535,Wahab Pai,M,1976-05-13,49,A+,+91-00000-78373,Thiruvananthapuram,None known,2021-12-19
P00538,Vincent Rege,M,2002-05-10,23,AB-,+91-00000-76533,Thiruvananthapuram,None known,2023-10-23
P00539,Urishilla Dalal,F,1959-04-04,66,O-,+91-00000-96479,Kottayam,None known,2022-05-12
P00540,Deepa Vora,F,1970-06-16,55,O+,+91-00000-51213,Kollam,None known,2023-02-08
P00541,Oni Vohra,F,2015-08-31,9,A+,+91-00000-77450,Kottayam,None known,2023-07-07
P00542,Yoshita Sankaran,F,1997-12-13,27,AB+,+91-00000-21188,Kottayam,None known,2023-12-31
P00543,Ucchal Bajwa,F,1966-06-05,59,O-,+91-00000-39912,Kottayam,None known,2023-11-18
P00544,Oeshi Bhagat,F,1999-10-27,25,B+,+91-00000-17293,Pathanamthitta,None known,2022-07-27
P00545,Manbir Sant,M,1938-02-11,87,AB+,+91-00000-41420,Kanyakumari,None known,2023-12-04
P00546,Raghav Nagy,M,1994-09-14,30,AB+,+91-00000-71796,Kollam,Sulfa drugs,2021-08-19
P00547,Michael Boase,M,1979-04-14,46,O-,+91-00000-24206,Pathanamthitta,None known,2023-02-03
P00549,Udant Kibe,M,2025-04-18,0,B+,+91-00000-12275,Thiruvananthapuram,None known,2023-02-05
P00552,Damini Vora,F,1970-01-07,55,B+,+91-00000-73759,Pathanamthitta,None known,2022-04-11
P00553,Kashvi Mohan,F,2005-04-08,20,O-,+91-00000-96768,Kanyakumari,None known,2022-02-17
P00554,Siya Keer,F,1973-01-11,52,AB+,+91-00000-32953,Pathanamthitta,None known,2021-12-28
P00555,Bakhshi Pillay,M,1966-11-30,58,A+,+91-00000-18080,Pathanamthitta,None known,2023-10-11
P00556,Shivansh Gala,M,2018-10-09,6,B-,+91-00000-63362,Alappuzha,None known,2022-02-07
P00557,Indrajit Sama,M,1947-10-11,77,AB+,+91-00000-27029,Alappuzha,None known,2022-08-24
P00558,Darsh Bora,M,1971-01-24,54,B-,+91-00000-39687,Thiruvananthapuram,Sulfa drugs,2023-08-28
P00560,Dhruv Dasgupta,M,1982-09-09,42,B+,+91-00000-75231,Kollam,None known,2022-11-24
P00561,Vasana Acharya,F,1966-02-18,59,A-,+91-00000-21912,Kanyakumari,None known,2023-11-14
P00562,Neelima Kohli,F,2018-06-27,7,AB+,+91-00000-54128,Pathanamthitta,None known,2022-04-06
P00564,Nicholas Gera,M,2004-02-05,21,B+,+91-00000-66641,Kanyakumari,None known,2022-08-16
P00565,Azad Sastry,M,1971-08-20,53,AB+,+91-00000-56527,Kanyakumari,NSAIDs,2022-07-26
P00567,Sneha Dhaliwal,F,1958-06-27,67,AB-,+91-00000-48482,Kottayam,NSAIDs,2021-08-03
P00568,Pranav Kashyap,M,1989-09-26,35,B-,+91-00000-92571,Pathanamthitta,None known,2023-02-12
P00569,Arin Mohan,M,1944-09-19,80,O-,+91-00000-96013,Thiruvananthapuram,None known,2023-06-19
P00572,Nicholas Tara,M,1969-10-30,55,B-,+91-00000-61090,Pathanamthitta,None known,2021-09-07
P00573,Ekbal Sodhi,M,1985-09-25,39,AB+,+91-00000-63204,Kollam,None known,2023-12-05
P00574,Ishanvi Jain,F,2025-06-27,0,B-,+91-00000-72290,Thiruvananthapuram,None known,2022-07-15
P00575,Neelima Bhargava,F,1964-10-24,60,AB+,+91-00000-10478,Kollam,None known,2021-12-15
P00578,Abhiram Gera,M,1989-04-04,36,O+,+91-00000-67884,Thiruvananthapuram,None known,2023-10-13
P00579,Isha Walia,F,2000-04-04,25,A+,+91-00000-95167,Thiruvananthapuram,None known,2021-10-22
P00580,Jacob Handa,M,1972-06-22,53,AB-,+91-00000-78193,Kanyakumari,None known,2021-08-25
P00582,Niharika Munshi,F,1949-11-26,75,O+,+91-00000-25832,Alappuzha,Penicillin,2022-07-02
P00583,Mahika Salvi,F,1979-06-06,46,B-,+91-00000-90913,Kottayam,None known,2021-09-18
P00584,Ekanta Natt,F,1989-02-13,36,A-,+91-00000-87471,Kanyakumari,None known,2023-11-10
P00585,Vamakshi Sagar,F,1939-12-16,85,A+,+91-00000-18770,Kollam,None known,2021-10-02
P00586,Chaaya Gara,F,1985-01-12,40,B+,+91-00000-39041,Kollam,Sulfa drugs,2023-01-15
P00587,Isaac Mohanty,M,2018-08-11,6,AB-,+91-00000-43989,Kottayam,None known,2022-02-07
P00588,Darpan Hegde,M,1950-04-30,75,AB-,+91-00000-28075,Thiruvananthapuram,None known,2023-06-25
P00589,Krish Golla,M,1977-05-10,48,A-,+91-00000-75788,Kanyakumari,Sulfa drugs,2022-08-20
P00590,Kamya Thaker,F,2007-12-16,17,AB+,+91-00000-58472,Thiruvananthapuram,None known,2022-06-18
P00592,Quincy Viswanathan,M,1982-01-05,43,B-,+91-00000-79820,Thiruvananthapuram,None known,2023-02-03
P00593,Dalbir Varty,M,1949-01-09,76,O-,+91-00000-87694,Thiruvananthapuram,None known,2023-06-21
P00594,Ishwar Mitra,M,1990-10-26,34,B-,+91-00000-76525,Kollam,None known,2022-05-18
P00595,Hemangini Kara,F,1995-03-13,30,O+,+91-00000-79782,Kottayam,None known,2022-06-06
P00596,Manya Deo,F,1977-09-02,47,AB-,+91-00000-67778,Thiruvananthapuram,None known,2022-06-30
P00597,Chandani Shere,F,1972-02-07,53,B+,+91-00000-65222,Kottayam,None known,2021-08-23
P00598,Balvan Sarraf,M,1968-05-09,57,B+,+91-00000-68058,Pathanamthitta,None known,2022-06-27
P00599,Balhaar Wali,M,1987-04-28,38,AB-,+91-00000-57205,Kottayam,None known,2022-11-10
P00600,Arin Amble,M,1975-03-22,50,AB-,+91-00000-68099,Alappuzha,None known,2022-01-13
P00601,Lucky Yogi,M,2000-12-23,24,B+,+91-00000-31897,Kottayam,None known,2021-10-21
P00602,Jeremiah Sampath,M,1989-09-02,35,O+,+91-00000-94738,Kottayam,None known,2022-12-11
P00603,Chameli Gala,F,2010-06-19,15,AB+,+91-00000-27058,Kanyakumari,NSAIDs,2022-10-23
P00604,Lucky Gupta,M,1995-10-25,29,A+,+91-00000-90833,Alappuzha,None known,2022-01-23
P00605,Krisha Gola,F,1976-11-23,48,B+,+91-00000-19595,Alappuzha,None known,2022-02-17
P00606,Liam Balakrishnan,M,1967-11-18,57,AB+,+91-00000-30144,Pathanamthitta,None known,2021-10-13
P00607,Idika Dora,F,1983-08-19,41,AB-,+91-00000-45388,Kottayam,None known,2023-05-09
P00608,Anika Shenoy,F,2001-06-26,24,AB+,+91-00000-52612,Kollam,None known,2022-04-05
P00609,Sanaya Agate,F,1976-02-01,49,O-,+91-00000-33544,Pathanamthitta,None known,2021-09-03
P00610,Zaid Bhasin,M,1988-07-02,37,A+,+91-00000-55863,Kottayam,None known,2022-06-04
P00611,Hemangini Bhatt,F,2016-01-07,9,O-,+91-00000-64646,Alappuzha,None known,2023-06-14
P00612,Radha Nagi,F,2015-06-17,10,A-,+91-00000-37061,Kollam,Penicillin,2022-05-20
P00614,Madhav Tiwari,M,2017-05-04,8,A-,+91-00000-26695,Kanyakumari,None known,2022-01-03
P00615,Yoshita Wali,F,2024-03-17,1,O+,+91-00000-45266,Alappuzha,None known,2022-08-16
P00616,Harita Gandhi,F,1971-08-30,53,O-,+91-00000-53335,Kollam,None known,2023-05-17
P00618,Kamya Sastry,F,1977-01-15,48,AB-,+91-00000-28283,Pathanamthitta,None known,2023-12-29
P00619,Lavanya Keer,F,2004-01-24,21,B-,+91-00000-31366,Thiruvananthapuram,None known,2021-08-16
P00620,Kai Suresh,M,1955-10-25,69,AB-,+91-00000-85281,Kanyakumari,None known,2022-09-17
P00621,Indrajit Tara,M,2007-03-15,18,A+,+91-00000-27622,Kottayam,None known,2021-07-30
P00622,Leena Banik,F,2005-10-15,19,O-,+91-00000-76325,Kanyakumari,None known,2023-05-02
P00623,Harrison Ben,M,1969-02-09,56,O-,+91-00000-23126,Pathanamthitta,None known,2023-08-08
P00624,Vanya Gole,F,2007-01-29,18,AB-,+91-00000-38128,Pathanamthitta,None known,2021-08-02
P00625,Omaja Doshi,F,1985-10-13,39,B-,+91-00000-73865,Alappuzha,None known,2023-04-14
P00627,Urishilla Thakur,F,1972-02-27,53,AB-,+91-00000-79714,Thiruvananthapuram,None known,2023-11-19
P00628,Timothy Lall,M,1956-11-15,68,B+,+91-00000-46024,Kottayam,Penicillin,2023-02-14
P00630,Dakshesh Gokhale,M,2000-11-01,24,B+,+91-00000-44304,Thiruvananthapuram,None known,2021-12-27
P00631,Kashish Dhingra,F,1939-02-26,86,A+,+91-00000-24088,Alappuzha,None known,2022-06-17
P00633,Unnati Basak,F,2025-07-17,0,O-,+91-00000-35939,Kanyakumari,None known,2021-11-25
P00634,Nirja Vora,F,2000-01-14,25,B-,+91-00000-63605,Kollam,Sulfa drugs,2022-03-21
P00635,Kevin Tara,M,2010-11-19,14,A+,+91-00000-68574,Kottayam,None known,2022-10-16
P00636,Chanchal Uppal,F,2016-03-13,9,A+,+91-00000-99661,Kollam,None known,2022-03-08
P00637,Harinakshi Radhakrishnan,F,1975-05-15,50,A+,+91-00000-89183,Alappuzha,Sulfa drugs,2021-12-20
P00638,Joshua Kothari,M,1972-03-04,53,A-,+91-00000-60012,Pathanamthitta,None known,2023-12-07
P00640,Vasana Bhat,F,1997-08-13,27,A+,+91-00000-99011,Kottayam,None known,2023-05-01
P00641,Nakul Roy,M,1985-12-30,39,O-,+91-00000-36616,Alappuzha,None known,2022-01-02
P00642,Vinaya Patla,F,1972-08-31,52,A-,+91-00000-31782,Alappuzha,None known,2021-08-28
P00644,Devansh Suri,M,2005-05-23,20,O+,+91-00000-78541,Alappuzha,Sulfa drugs,2023-07-31
P00645,Ekalinga Dhillon,M,1955-02-01,70,O-,+91-00000-30411,Alappuzha,None known,2022-01-10
P00648,Jai Rout,M,2010-03-28,15,A-,+91-00000-53188,Pathanamthitta,None known,2021-11-02
P00649,Ekavir Chand,M,1962-05-10,63,B-,+91-00000-91412,Thiruvananthapuram,None known,2023-09-15
P00650,Shravya Misra,F,1976-07-06,49,O-,+91-00000-50548,Thiruvananthapuram,None known,2023-11-13
P00651,Vrishti Samra,F,1993-11-02,31,O+,+91-00000-37995,Kottayam,Sulfa drugs,2023-09-01
P00652,Brinda Banerjee,F,1988-12-20,36,O-,+91-00000-57552,Kollam,None known,2022-04-04
P00653,Ishwar Merchant,M,1974-11-05,50,B+,+91-00000-71544,Kottayam,None known,2022-10-18
P00654,Jonathan Dani,M,1974-04-29,51,AB+,+91-00000-78913,Kottayam,None known,2023-09-19
P00655,Jai Sahota,M,2002-02-06,23,A-,+91-00000-21343,Thiruvananthapuram,None known,2023-04-16
P00656,Vedhika Chadha,F,2020-06-28,5,B-,+91-00000-40517,Alappuzha,None known,2022-04-09
P00657,Jhalak Patla,F,2011-03-19,14,A+,+91-00000-80409,Thiruvananthapuram,None known,2021-08-31
P00659,Janani Baral,F,1995-09-15,29,B-,+91-00000-38004,Pathanamthitta,None known,2023-06-05
P00660,Gaurika Rau,F,2025-04-19,0,O-,+91-00000-48816,Kanyakumari,None known,2023-07-07
P00661,Barkha Oza,F,2018-04-19,7,O+,+91-00000-73546,Kottayam,None known,2023-03-12
P00662,Hema Shere,F,1990-07-28,34,A-,+91-00000-93300,Kanyakumari,Penicillin,2022-02-15
P00663,Shravya Kala,F,1996-12-14,28,O+,+91-00000-50855,Kollam,None known,2023-04-12
P00664,Rayaan Radhakrishnan,M,1962-10-14,62,B-,+91-00000-59974,Pathanamthitta,Penicillin,2023-01-15
P00665,Aryan Kale,M,2010-04-28,15,A+,+91-00000-42077,Kanyakumari,None known,2023-08-12
P00666,Ubika Palan,F,2000-01-22,25,AB+,+91-00000-96214,Alappuzha,None known,2022-08-21
P00667,Jatin Gour,M,1968-09-18,56,A+,+91-00000-13242,Kollam,None known,2023-08-22
P00668,Finn Srinivasan,M,1966-03-14,59,A-,+91-00000-81789,Kottayam,Sulfa drugs,2023-09-02
P00669,Ishani Ratta,F,1967-06-13,58,B-,+91-00000-19159,Alappuzha,None known,2022-07-15
P00670,Jalsa Sibal,F,2022-07-04,3,A+,+91-00000-10652,Kottayam,Sulfa drugs,2023-12-05
P00671,Nikita Sodhi,F,2022-07-05,3,A-,+91-00000-93716,Thiruvananthapuram,None known,2023-11-11
P00672,Vansha Suri,F,1991-06-03,34,B+,+91-00000-11802,Kottayam,None known,2023-03-18
P00674,Ishani Zachariah,F,1949-10-23,75,AB-,+91-00000-98688,Kollam,None known,2021-10-19
P00675,Rehaan Saini,M,1960-09-22,64,A+,+91-00000-57125,Kanyakumari,None known,2022-09-23
P00676,Balhaar Batta,M,1965-11-22,59,AB-,+91-00000-97306,Kottayam,None known,2022-03-16
P00678,Mahika Bahl,F,1975-12-21,49,A+,+91-00000-14063,Alappuzha,None known,2022-07-31
P00679,Yochana Gopal,F,2022-10-25,2,O-,+91-00000-46538,Thiruvananthapuram,None known,2022-03-14
P00680,Lekha Vala,F,1964-03-18,61,O-,+91-00000-16915,Kottayam,None known,2023-09-23
P00681,Shravya Kalla,F,1980-06-03,45,O-,+91-00000-36925,Thiruvananthapuram,None known,2022-07-02
P00682,Lipika Chauhan,F,1947-12-31,77,B-,+91-00000-40262,Pathanamthitta,None known,2022-10-24
P00683,Radha Bhandari,F,1985-12-16,39,B-,+91-00000-67675,Kanyakumari,None known,2023-01-19
P00684,Faraj Parsa,M,1957-11-08,67,O-,+91-00000-44989,Thiruvananthapuram,Penicillin,2023-05-08
P00685,Ekantika Khosla,F,2024-02-22,1,B-,+91-00000-72357,Kollam,None known,2022-04-30
P00686,Darpan Bahri,M,1995-07-29,29,O+,+91-00000-48319,Thiruvananthapuram,None known,2023-06-10
P00687,Naveen Rajagopalan,M,1935-07-26,90,B-,+91-00000-89663,Pathanamthitta,Penicillin,2021-10-26
P00688,Varenya Chacko,F,2015-02-06,10,AB-,+91-00000-95055,Kollam,None known,2021-09-18
P00689,Sai Nanda,F,2023-06-17,2,O+,+91-00000-87971,Pathanamthitta,None known,2022-10-17
P00690,Kabir Venkataraman,M,2022-01-22,3,B+,+91-00000-45258,Kollam,None known,2023-08-01
P00691,Baghyawati Mittal,F,2024-02-05,1,AB+,+91-00000-70954,Kanyakumari,None known,2023-10-30
P00692,Ronith Khare,M,1934-09-03,90,A+,+91-00000-54791,Alappuzha,None known,2022-08-18
P00693,Yash Baria,M,2003-01-29,22,AB+,+91-00000-31596,Alappuzha,None known,2023-04-11
P00694,Ijaya Dora,F,1938-01-03,87,O+,+91-00000-99001,Kollam,NSAIDs,2022-02-01
P00695,Devansh Balay,M,1977-01-23,48,AB+,+91-00000-89549,Pathanamthitta,None known,2023-06-10
P00696,Ishita Muni,F,1942-05-06,83,B-,+91-00000-10920,Alappuzha,None known,2022-06-23
P00697,Samesh Samra,M,1941-09-13,83,A+,+91-00000-20018,Kanyakumari,None known,2023-02-11
P00698,Wakeeta Deshpande,F,2005-01-17,20,B-,+91-00000-64192,Thiruvananthapuram,None known,2023-06-14
P00699,Yauvani Lad,F,2006-10-10,18,AB-,+91-00000-74105,Kottayam,None known,2023-08-30
P00700,Nirja Seth,F,1978-03-30,47,A+,+91-00000-72894,Pathanamthitta,None known,2022-07-07
P00701,Saanvi Din,F,2014-06-06,11,AB-,+91-00000-28673,Alappuzha,None known,2023-09-04
P00702,Ishani Mand,F,1953-03-15,72,O-,+91-00000-62412,Alappuzha,None known,2022-10-06
P00703,Varenya Ravi,F,1973-03-03,52,A+,+91-00000-45961,Alappuzha,None known,2022-11-13
P00704,Ekanta Raju,F,2023-08-25,1,A-,+91-00000-87796,Pathanamthitta,None known,2021-12-29
P00705,Pranav Kara,M,1976-03-18,49,O-,+91-00000-69021,Thiruvananthapuram,None known,2022-02-23
P00706,Dalaja Master,F,2016-03-07,9,A+,+91-00000-56473,Thiruvananthapuram,None known,2023-03-06
P00707,Reva Pai,F,2006-05-28,19,AB-,+91-00000-58414,Kottayam,None known,2022-05-04
P00708,Janaki Dey,F,1939-06-04,86,A-,+91-00000-34400,Thiruvananthapuram,None known,2023-10-15
P00709,Anusha Bakshi,F,1995-12-11,29,B+,+91-00000-71963,Kollam,NSAIDs,2023-01-04
P00710,Wyatt Apte,M,1960-06-23,65,B-,+91-00000-71893,Pathanamthitta,None known,2022-03-06
P00711,Neha Bhavsar,F,1968-01-24,57,AB-,+91-00000-60532,Kanyakumari,None known,2021-10-03
P00712,Janaki Pandit,F,2022-03-18,3,AB+,+91-00000-51276,Kollam,None known,2022-07-18
P00713,Divya Prasad,F,1988-01-18,37,O+,+91-00000-49070,Kanyakumari,None known,2021-11-30
P00714,Jacob Lad,M,2021-06-21,4,B+,+91-00000-11517,Kottayam,NSAIDs,2023-10-26
P00716,Darpan Ramanathan,M,1991-10-02,33,A-,+91-00000-45591,Kanyakumari,None known,2023-08-31
P00717,Xiti Bhasin,F,1972-01-01,53,O+,+91-00000-22160,Kollam,Penicillin,2023-12-01
P00718,Yash Rajagopal,M,1949-07-20,76,A+,+91-00000-95983,Kanyakumari,None known,2022-01-26
P00719,Nitesh Mane,M,2023-10-09,1,A+,+91-00000-52824,Kollam,None known,2023-05-22
P00721,Indrajit Dutt,M,1995-02-20,30,B-,+91-00000-61756,Alappuzha,None known,2022-05-27
P00722,Saksham Jaggi,M,1960-02-29,65,O+,+91-00000-13050,Alappuzha,None known,2023-07-04
P00723,Wazir Ganesan,M,1985-10-15,39,B+,+91-00000-97698,Pathanamthitta,Sulfa drugs,2023-05-02
P00724,Parth Khatri,M,1983-02-22,42,AB+,+91-00000-66065,Alappuzha,None known,2023-10-18
P00725,Chakradhar Oommen,M,1988-12-19,36,AB-,+91-00000-12322,Alappuzha,NSAIDs,2023-08-02
P00726,Udyati Dora,F,2004-08-14,20,A-,+91-00000-54085,Kanyakumari,None known,2022-07-09
P00727,Waida Kurian,F,1939-07-23,86,AB-,+91-00000-99617,Kanyakumari,None known,2023-11-06
P00728,Mitesh Bajaj,M,1972-09-08,52,B-,+91-00000-72194,Kanyakumari,None known,2023-08-15
P00729,Shivani Dara,F,1958-12-25,66,O-,+91-00000-77528,Pathanamthitta,None known,2021-10-03
P00731,Samaksh Magar,M,2018-01-17,7,AB-,+91-00000-74203,Pathanamthitta,None known,2023-09-04
P00732,Avi Purohit,M,2017-05-23,8,O-,+91-00000-38467,Pathanamthitta,None known,2022-09-04
P00733,Yachana Mital,F,1982-07-28,43,B+,+91-00000-94992,Alappuzha,None known,2023-11-14
P00734,Wahab Nanda,M,1944-02-12,81,B+,+91-00000-62470,Kanyakumari,None known,2022-09-09
P00735,Jonathan Bora,M,1999-06-28,26,B+,+91-00000-77474,Kollam,Penicillin,2023-11-19
P00736,Amaira Banik,F,1944-02-19,81,B-,+91-00000-16800,Kollam,None known,2021-10-07
P00737,Oscar Naik,M,1990-11-03,34,AB+,+91-00000-67765,Pathanamthitta,None known,2022-08-01
P00738,Ridhi Mishra,F,1955-07-16,70,AB+,+91-00000-93078,Kottayam,None known,2022-12-18
P00739,Lekha Grewal,F,1990-06-05,35,O+,+91-00000-38497,Kottayam,Penicillin,2023-12-12
P00740,Vrinda Rajagopalan,F,1978-04-22,47,O-,+91-00000-18710,Pathanamthitta,None known,2023-11-03
P00741,Panini Patil,F,1976-04-08,49,AB-,+91-00000-32962,Thiruvananthapuram,None known,2023-10-09
P00742,Alexander Kalita,M,1982-10-22,42,O-,+91-00000-83560,Kollam,None known,2022-06-24
P00744,Samesh Sagar,M,1942-04-10,83,O+,+91-00000-83583,Kottayam,None known,2023-06-11
P00745,Bhavika Majumdar,F,2018-07-31,6,AB+,+91-00000-36651,Pathanamthitta,None known,2023-03-06
P00746,Bhavna Shetty,F,1973-03-01,52,B-,+91-00000-31940,Kanyakumari,None known,2021-09-24
P00747,Varenya Raja,F,2003-06-30,22,AB+,+91-00000-31060,Thiruvananthapuram,None known,2023-07-26
P00748,Reyansh Barad,M,1950-01-30,75,A-,+91-00000-92315,Thiruvananthapuram,None known,2022-11-19
P00749,Ekanta Tripathi,F,1995-10-11,29,O-,+91-00000-63908,Alappuzha,None known,2022-04-30
P00750,Madhavi More,F,1937-03-23,88,A-,+91-00000-91064,Kottayam,None known,2023-11-01
P00752,Warjas Bail,M,1970-09-03,54,O-,+91-00000-71209,Kanyakumari,None known,2024-01-07
P00753,Falguni Hans,F,2017-08-01,7,B+,+91-00000-65671,Thiruvananthapuram,None known,2022-09-04
P00754,Krishna Kari,M,1987-09-27,37,AB-,+91-00000-59619,Thiruvananthapuram,None known,2023-06-27
P00755,Leela Kannan,F,1975-04-22,50,AB-,+91-00000-11376,Kollam,None known,2023-02-03
P00756,Jacob Verma,M,1982-08-09,42,B-,+91-00000-92677,Alappuzha,None known,2022-06-14
P00757,Aadi Ramesh,M,2019-07-06,6,B+,+91-00000-60537,Alappuzha,None known,2023-10-27
P00758,Aarav Khatri,M,1985-01-11,40,A+,+91-00000-43432,Kottayam,None known,2022-07-10
P00759,Yatin Brar,M,1973-03-31,52,B+,+91-00000-97157,Kanyakumari,None known,2022-04-21
P00760,Osha Lalla,F,1977-03-06,48,A+,+91-00000-68654,Thiruvananthapuram,None known,2021-10-25
P00761,Prisha Chawla,F,1952-05-01,73,AB-,+91-00000-55712,Kottayam,None known,2023-12-05
P00762,Aditya Munshi,M,1972-07-15,53,A-,+91-00000-88987,Kollam,None known,2023-01-27
P00764,Gaurangi Handa,F,1963-03-24,62,AB+,+91-00000-58148,Kanyakumari,None known,2022-11-30
P00765,Faris Dutta,M,2003-05-24,22,AB-,+91-00000-86085,Alappuzha,None known,2021-09-30
P00767,Nandini Pingle,F,1976-12-29,48,AB-,+91-00000-23047,Kottayam,None known,2022-03-11
P00768,Sarthak Mangal,M,1994-12-03,30,O+,+91-00000-89579,Pathanamthitta,None known,2022-03-31
P00769,Qadim Walla,M,1984-03-11,41,B-,+91-00000-77556,Kollam,None known,2022-11-04
P00770,Zaid Khalsa,M,2011-08-20,13,O-,+91-00000-99994,Kanyakumari,Sulfa drugs,2022-05-08
P00771,Kritika Pathak,F,2016-07-24,8,AB+,+91-00000-71155,Kollam,None known,2022-04-17
P00772,Nicholas Gokhale,M,1996-08-10,28,O-,+91-00000-97718,Kollam,None known,2021-08-30
P00773,Yasti Date,F,1974-05-27,51,B-,+91-00000-66221,Alappuzha,NSAIDs,2023-02-02
P00774,Azad Biswas,M,2021-05-27,4,O-,+91-00000-91438,Kanyakumari,None known,2023-12-31
P00775,Dalaja Mukherjee,F,1942-04-23,83,AB-,+91-00000-74759,Thiruvananthapuram,None known,2021-08-09
P00776,Dayita Seth,F,1936-04-17,89,B+,+91-00000-59559,Thiruvananthapuram,None known,2022-01-09
P00777,Wridesh Baria,M,1947-08-23,77,A+,+91-00000-77674,Thiruvananthapuram,None known,2023-03-12
P00778,Gautami Sachar,F,1975-09-10,49,O+,+91-00000-17975,Kollam,None known,2022-09-23
P00779,Warda Bera,F,1968-10-11,56,AB+,+91-00000-29391,Kottayam,None known,2021-10-04
P00782,Rohan Kulkarni,M,1993-07-06,32,AB-,+91-00000-63778,Kottayam,None known,2022-04-08
P00783,Jeremiah Pillai,M,1970-04-30,55,AB+,+91-00000-59250,Kanyakumari,None known,2023-09-21
P00784,Nihal Goswami,M,1991-12-04,33,B+,+91-00000-75326,Pathanamthitta,None known,2023-05-21
P00785,Osha Jayaraman,F,1998-05-27,27,O+,+91-00000-87420,Pathanamthitta,None known,2023-01-09
P00786,Eiravati Salvi,F,1970-10-24,54,A+,+91-00000-68611,Thiruvananthapuram,None known,2022-07-16
P00788,Faris Dass,M,1992-10-24,32,B+,+91-00000-48014,Pathanamthitta,None known,2023-10-03
P00789,Harish Puri,M,2009-01-15,16,O+,+91-00000-49935,Kollam,None known,2022-08-27
P00793,Lipika Madan,F,1977-03-13,48,AB-,+91-00000-74089,Pathanamthitta,None known,2021-12-17
P00795,Rushil Raju,M,1988-08-19,36,A-,+91-00000-36219,Pathanamthitta,None known,2024-01-05
P00796,Ekaraj Bava,M,1957-11-03,67,O+,+91-00000-79553,Thiruvananthapuram,None known,2023-11-27
P00797,Farhan Dani,M,1972-07-27,53,B+,+91-00000-92696,Pathanamthitta,None known,2022-02-14
P00798,Ansh Hari,M,1983-03-28,42,A+,+91-00000-17739,Pathanamthitta,Sulfa drugs,2022-07-29
P00799,Mekhala Parikh,F,1979-05-21,46,O-,+91-00000-82560,Pathanamthitta,None known,2023-09-07
P00800,Darpan Ravel,M,2001-11-09,23,B-,+91-00000-64331,Pathanamthitta,None known,2023-07-01
P00801,Omya Bala,F,1966-08-14,58,A+,+91-00000-44878,Kanyakumari,None known,2022-11-21
P00803,Ridhi Bhavsar,F,1997-11-11,27,AB-,+91-00000-41788,Kottayam,None known,2024-01-12
P00804,Nilima Sarna,F,1997-10-16,27,A-,+91-00000-52340,Kollam,None known,2023-04-12
P00805,Meghana Kapur,F,1960-07-12,65,B+,+91-00000-75886,Kollam,None known,2022-05-30
P00806,Rohan Reddy,M,2012-09-25,12,AB+,+91-00000-54660,Kollam,None known,2021-10-14
P00807,Ekta Ramachandran,F,2023-05-20,2,B-,+91-00000-75849,Kanyakumari,None known,2023-07-14
P00808,Janaki Mandal,F,2019-05-02,6,AB+,+91-00000-44836,Pathanamthitta,None known,2023-12-08
P00809,Ethan Sathe,M,1950-01-08,75,B+,+91-00000-78760,Pathanamthitta,NSAIDs,2022-06-02
P00810,Harita Chhabra,F,1975-01-10,50,O-,+91-00000-96036,Kanyakumari,None known,2023-07-01
P00811,Jeremiah Sura,M,1947-03-26,78,B-,+91-00000-30990,Pathanamthitta,None known,2023-02-02
P00812,Tarak Dara,M,1951-02-10,74,A+,+91-00000-62314,Kollam,None known,2023-06-22
P00813,Forum Naik,F,1957-12-18,67,AB+,+91-00000-77377,Pathanamthitta,Sulfa drugs,2023-10-26
P00815,Eshana Mahal,F,2001-01-16,24,O+,+91-00000-91537,Kollam,None known,2023-01-06
P00816,Ryan Mahal,M,1961-11-03,63,B-,+91-00000-20253,Thiruvananthapuram,NSAIDs,2023-03-14
P00817,Naveen Kari,M,1956-11-20,68,O+,+91-00000-25357,Kottayam,None known,2022-10-21
P00818,Banjeet Subramaniam,M,1997-08-31,27,B-,+91-00000-29073,Pathanamthitta,None known,2023-01-27
P00820,Kai Behl,M,1998-01-29,27,AB-,+91-00000-28151,Kanyakumari,None known,2023-01-11
P00821,Faqid Bhatt,M,1936-12-04,88,A+,+91-00000-53842,Kanyakumari,Sulfa drugs,2021-11-29
P00822,Aarini More,F,1945-04-24,80,A+,+91-00000-76201,Kottayam,None known,2024-01-01
P00823,Balveer Agrawal,M,1987-10-11,37,A+,+91-00000-28423,Kanyakumari,None known,2022-07-14
P00824,Gavin Nayar,M,2019-04-15,6,AB+,+91-00000-52277,Kottayam,Penicillin,2023-12-18
P00825,Wyatt Dey,M,1979-02-09,46,AB+,+91-00000-32299,Alappuzha,None known,2022-04-27
P00827,Wyatt Balay,M,2022-08-29,2,O+,+91-00000-65463,Kanyakumari,None known,2022-08-25
P00829,Rudra Bhardwaj,M,1979-08-30,45,AB-,+91-00000-67345,Kanyakumari,NSAIDs,2023-04-14
P00830,Janaki Krishnan,F,1949-02-12,76,A-,+91-00000-66281,Kottayam,NSAIDs,2023-10-02
P00831,Lakshit Gulati,M,1999-06-18,26,AB+,+91-00000-17998,Kanyakumari,None known,2022-05-19
P00832,Mohini Krish,F,1991-02-08,34,O-,+91-00000-33140,Alappuzha,Sulfa drugs,2023-07-14
P00833,Vaishnavi Batta,F,2012-10-15,12,O-,+91-00000-59311,Pathanamthitta,None known,2021-07-30
P00834,Gaurang Bala,M,2023-11-10,1,B+,+91-00000-58957,Kollam,None known,2023-04-05
P00835,Hamsini Yohannan,F,1954-12-27,70,A+,+91-00000-84273,Thiruvananthapuram,None known,2021-10-13
P00836,Daniel Borde,M,1989-04-12,36,O+,+91-00000-97376,Kollam,Penicillin,2022-07-10
P00837,Lopa Parmer,F,1992-06-26,33,O+,+91-00000-90951,Kottayam,None known,2022-07-22
P00839,Azad Varkey,M,1968-07-01,57,A+,+91-00000-67924,Kottayam,None known,2021-11-20
P00840,Viraj Anne,M,2006-11-05,18,B-,+91-00000-45874,Alappuzha,None known,2023-09-28
P00841,Henry Bhatt,M,1967-01-27,58,A+,+91-00000-33127,Kanyakumari,Sulfa drugs,2023-08-04
P00843,Kevin Konda,M,1953-08-07,71,A+,+91-00000-23596,Kanyakumari,Penicillin,2023-02-01
P00844,Yachana Rastogi,F,1991-06-01,34,B+,+91-00000-57801,Kollam,None known,2023-08-03
P00845,Mitesh Wali,M,2023-07-17,2,AB+,+91-00000-24020,Kanyakumari,None known,2023-02-19
P00847,Sai Rege,M,1992-09-28,32,A-,+91-00000-90818,Kottayam,None known,2023-12-19
P00848,Ladli Bajwa,F,1974-06-23,51,B+,+91-00000-65093,Pathanamthitta,Sulfa drugs,2022-02-02
P00849,Aayush Dhaliwal,M,2018-08-06,6,AB-,+91-00000-50181,Pathanamthitta,None known,2023-03-30
P00850,Jhalak Naik,F,1938-09-17,86,AB+,+91-00000-37758,Kanyakumari,None known,2021-10-31
P00851,Sara Pingle,F,1995-05-05,30,B+,+91-00000-69505,Kottayam,None known,2022-03-12
P00853,Qabil Sengupta,M,2011-03-19,14,AB+,+91-00000-47252,Pathanamthitta,None known,2021-12-18
P00855,Liam Bhavsar,M,1942-06-01,83,AB-,+91-00000-83129,Alappuzha,NSAIDs,2021-12-28
P00856,Oeshi Chandra,F,1949-11-30,75,O+,+91-00000-65500,Kottayam,None known,2022-09-05
P00857,Kevin Natt,M,1974-04-24,51,AB+,+91-00000-68432,Kollam,None known,2022-09-07
P00858,Jalsa Gole,F,1984-11-23,40,AB+,+91-00000-22166,Kottayam,None known,2022-09-24
P00859,Jagvi Batta,F,2015-06-23,10,A-,+91-00000-46064,Thiruvananthapuram,None known,2022-01-20
P00860,Eiravati Modi,F,1998-01-31,27,AB-,+91-00000-26901,Kanyakumari,None known,2023-04-24
P00861,Harshil Goel,M,1990-12-04,34,B+,+91-00000-95005,Kottayam,None known,2022-11-08
P00862,Prisha Cherian,F,1948-05-23,77,A-,+91-00000-34712,Kollam,Sulfa drugs,2022-10-17
P00864,Ria Palla,F,2009-01-17,16,A-,+91-00000-75050,Kollam,None known,2023-11-12
P00865,Hemani Sankar,F,1965-11-21,59,A+,+91-00000-59390,Alappuzha,None known,2022-02-15
P00866,Alka Andra,F,2018-03-20,7,A-,+91-00000-60987,Kollam,NSAIDs,2023-01-04
P00867,Ryan Thakkar,M,1972-04-11,53,B-,+91-00000-70688,Thiruvananthapuram,None known,2021-10-27
P00869,Champak Nagy,M,1935-02-15,90,AB+,+91-00000-83491,Kottayam,None known,2023-04-16
P00870,Ishani Bail,F,1998-05-12,27,B+,+91-00000-93183,Alappuzha,Penicillin,2023-01-10
P00871,Harita Nagi,F,2000-05-29,25,B+,+91-00000-72711,Kanyakumari,NSAIDs,2023-12-10
P00872,Bhavna Chokshi,F,1938-12-19,86,AB-,+91-00000-64172,Kanyakumari,None known,2023-09-22
P00873,Naveen Sani,M,2020-01-22,5,A+,+91-00000-87172,Alappuzha,None known,2023-03-02
P00875,Zaid Rege,M,2000-04-03,25,A-,+91-00000-72905,Kollam,None known,2022-06-27
P00876,Gaurav Mahajan,M,2020-12-11,4,B-,+91-00000-11834,Kanyakumari,None known,2023-03-18
P00877,Bakhshi Ramakrishnan,M,1973-05-11,52,O+,+91-00000-66362,Kottayam,None known,2022-04-28
P00878,Naveen Goswami,M,1962-02-26,63,AB+,+91-00000-75079,Kanyakumari,None known,2023-02-18
P00879,Pranav Vohra,M,1968-05-12,57,AB+,+91-00000-25316,Kottayam,None known,2022-06-08
P00880,Abdul Divan,M,1994-10-05,30,AB+,+91-00000-25830,Kanyakumari,None known,2021-11-15
P00881,Ranbir Bhakta,M,2024-07-10,1,O-,+91-00000-99554,Kollam,None known,2023-01-24
P00883,Urvi Samra,F,1948-12-04,76,AB+,+91-00000-93301,Pathanamthitta,None known,2023-09-16
P00884,Zayyan Comar,M,1975-06-27,50,B-,+91-00000-39163,Kollam,None known,2021-11-23
P00885,Darsh Setty,M,1975-07-09,50,B-,+91-00000-93816,Kottayam,None known,2022-12-18
P00886,Urmi Sibal,F,2013-05-24,12,B+,+91-00000-91072,Pathanamthitta,None known,2022-08-05
P00888,Zashil Karpe,M,1935-03-02,90,AB+,+91-00000-17247,Alappuzha,None known,2022-06-20
P00889,Raghav Basak,M,1963-10-18,61,AB-,+91-00000-40709,Pathanamthitta,None known,2022-11-24
P00890,Yasti Balay,F,2023-08-29,1,O-,+91-00000-87478,Pathanamthitta,Sulfa drugs,2023-06-20
P00891,Upkaar Sekhon,M,1936-07-04,89,B-,+91-00000-35663,Kollam,None known,2023-07-04
P00892,Lucky Batra,M,1963-03-03,62,AB-,+91-00000-77626,Kottayam,None known,2023-06-15
P00893,Avni Nair,F,1961-03-03,64,AB+,+91-00000-37840,Pathanamthitta,None known,2022-10-03
P00895,Vinaya Narasimhan,F,1965-10-04,59,AB+,+91-00000-33028,Kottayam,None known,2021-08-06
P00896,Kabir Munshi,M,1938-01-27,87,O+,+91-00000-78040,Kottayam,Sulfa drugs,2023-03-19
P00897,Ijaya Singh,F,1980-09-07,44,A+,+91-00000-15228,Thiruvananthapuram,None known,2023-12-16
P00898,Sai Ben,M,1988-02-24,37,A-,+91-00000-31474,Thiruvananthapuram,None known,2022-09-11
P00899,Dev Swaminathan,M,1940-02-08,85,AB+,+91-00000-21198,Thiruvananthapuram,None known,2021-10-12
P00900,Dayamai Kaur,F,1990-09-09,34,B+,+91-00000-12863,Thiruvananthapuram,None known,2023-05-10
P00901,Idika Dhar,F,1945-09-30,79,A+,+91-00000-86782,Thiruvananthapuram,NSAIDs,2022-10-13
P00902,Deepa Chawla,F,1978-06-23,47,O-,+91-00000-64610,Alappuzha,None known,2022-11-16
P00903,Yashodhara Krishnamurthy,F,2014-01-25,11,O+,+91-00000-21456,Thiruvananthapuram,None known,2023-01-29
P00904,Leena Bhattacharyya,F,1957-11-17,67,AB+,+91-00000-29454,Alappuzha,None known,2022-01-06
P00905,George Barad,M,1990-12-10,34,AB-,+91-00000-32490,Alappuzha,None known,2023-04-23
P00906,Pavani Krishna,F,1955-03-08,70,B+,+91-00000-36483,Kottayam,NSAIDs,2024-01-02
P00907,Owen Setty,M,2022-10-25,2,AB-,+91-00000-35049,Kollam,None known,2021-08-13
P00908,Ishita Yadav,F,1950-07-27,75,O+,+91-00000-56960,Pathanamthitta,NSAIDs,2022-03-02
P00909,Advika Sane,F,1992-03-17,33,AB-,+91-00000-77273,Thiruvananthapuram,None known,2022-08-03
P00910,Indira Suresh,F,2021-09-14,3,A-,+91-00000-89411,Kanyakumari,None known,2024-01-02
P00911,Logan Khare,M,1989-07-28,35,AB+,+91-00000-27187,Thiruvananthapuram,None known,2022-11-03
P00912,Bina Chhabra,F,1961-09-21,63,AB-,+91-00000-85256,Pathanamthitta,None known,2022-12-17
P00913,Urvi Swaminathan,F,2004-07-07,21,AB-,+91-00000-41952,Kanyakumari,None known,2023-07-04
P00914,Jai Bora,M,1990-02-14,35,A-,+91-00000-68459,Kollam,None known,2021-10-30
P00915,Yuvraj Bhalla,M,1981-09-03,43,B-,+91-00000-13771,Alappuzha,None known,2021-11-03
P00916,Bhavini Doshi,F,2003-04-01,22,AB-,+91-00000-58980,Kollam,None known,2021-08-12
P00918,Chandresh Nath,M,1988-07-03,37,B-,+91-00000-74675,Kanyakumari,None known,2021-10-02
P00919,Andrew Pal,M,1980-07-21,45,A-,+91-00000-80596,Kanyakumari,None known,2022-07-27
P00920,Imaran Mani,M,1993-09-30,31,O-,+91-00000-16607,Thiruvananthapuram,Sulfa drugs,2021-10-10
P00921,Dhriti Saha,F,1965-03-12,60,O+,+91-00000-45340,Kollam,None known,2023-10-02
P00922,Gavin Rama,M,2000-01-21,25,AB+,+91-00000-77166,Kollam,None known,2021-10-04
P00923,Amruta Shroff,F,1966-10-03,58,A+,+91-00000-87134,Kanyakumari,None known,2021-07-30
P00924,Yash Bora,M,2016-10-31,8,O+,+91-00000-93589,Pathanamthitta,None known,2022-06-02
P00925,Chaitanya Jhaveri,M,1955-10-13,69,A+,+91-00000-45281,Kanyakumari,None known,2021-12-19
P00927,Guneet Sankar,M,2013-03-21,12,O+,+91-00000-59827,Kollam,None known,2022-10-07
P00928,Saanvi Aurora,F,1951-08-02,74,A+,+91-00000-44605,Thiruvananthapuram,None known,2021-09-21
P00929,Omkaar Murty,M,1947-06-04,78,AB-,+91-00000-88294,Alappuzha,None known,2022-01-18
P00930,Maya Joshi,F,1954-04-07,71,AB+,+91-00000-34326,Pathanamthitta,None known,2022-08-27
P00931,Henry Golla,M,1977-12-26,47,B+,+91-00000-24643,Thiruvananthapuram,Penicillin,2022-03-13
P00932,Eesha Garg,F,2006-12-14,18,B-,+91-00000-10813,Kollam,None known,2023-02-03
P00933,Viraj Barman,M,1963-01-09,62,B+,+91-00000-58030,Kottayam,None known,2023-06-03
P00934,Dhruv Mall,M,1943-08-19,81,AB-,+91-00000-53959,Kollam,None known,2023-11-11
P00935,Dalbir Kuruvilla,M,1988-05-28,37,B+,+91-00000-91120,Kanyakumari,None known,2023-12-07
P00936,Pooja Parmar,F,2024-06-25,1,AB+,+91-00000-60686,Kanyakumari,None known,2023-07-29
P00937,Nikita Hayre,F,2000-06-11,25,A-,+91-00000-50434,Thiruvananthapuram,None known,2021-09-06
P00938,Aarna Biswas,F,1985-11-19,39,B+,+91-00000-84202,Thiruvananthapuram,None known,2023-01-06
P00939,Harshil Parsa,M,2024-10-16,0,AB+,+91-00000-98335,Thiruvananthapuram,None known,2023-09-27
P00940,Nilima Rege,F,1979-10-13,45,O-,+91-00000-74941,Pathanamthitta,None known,2022-12-01
P00941,Irya Dhingra,F,1950-11-13,74,AB-,+91-00000-40598,Kollam,None known,2021-11-19
P00942,Balendra Lata,M,1976-06-19,49,A-,+91-00000-61315,Pathanamthitta,None known,2021-10-15
P00943,Unnati Prasad,F,1985-08-16,39,O-,+91-00000-71079,Kanyakumari,None known,2023-10-01
P00944,Tara Mallick,F,2007-09-13,17,AB-,+91-00000-59127,Thiruvananthapuram,None known,2021-08-07
P00945,Vasatika Deol,F,1992-07-10,33,O-,+91-00000-50095,Kottayam,None known,2021-11-09
P00946,Yashica Dasgupta,F,2001-12-07,23,A-,+91-00000-47004,Kollam,None known,2022-08-11
P00947,Champak Pal,M,1963-12-09,61,AB-,+91-00000-92003,Thiruvananthapuram,None known,2021-08-15
P00948,Sathvik Keer,M,2004-10-12,20,O+,+91-00000-71426,Kottayam,None known,2023-12-15
P00949,Xiti Dalal,F,1937-09-27,87,B-,+91-00000-31449,Kanyakumari,None known,2022-05-12
P00950,Lucky Dasgupta,M,2014-07-10,11,AB-,+91-00000-30410,Pathanamthitta,None known,2022-03-21
P00951,Luke Brar,M,2019-06-23,6,O+,+91-00000-23371,Kanyakumari,None known,2022-01-02
P00952,Utkarsh Kara,M,2024-12-20,0,B-,+91-00000-97104,Kottayam,None known,2023-04-08
P00953,William Ram,M,2005-02-02,20,AB-,+91-00000-63562,Alappuzha,None known,2023-10-16
P00954,Ira Sachdev,F,1970-12-27,54,AB-,+91-00000-37524,Thiruvananthapuram,None known,2021-12-03
P00955,Januja Sen,F,1999-06-10,26,A-,+91-00000-64689,Pathanamthitta,None known,2022-05-08
P00956,Azad Peri,M,2002-01-08,23,AB+,+91-00000-19381,Alappuzha,None known,2023-09-16
P00958,Lohit Sastry,M,1974-02-01,51,B-,+91-00000-24777,Thiruvananthapuram,None known,2021-11-12
P00960,Abeer Konda,M,2003-04-20,22,B-,+91-00000-31470,Kanyakumari,None known,2022-06-26
P00961,Advika Sabharwal,F,1957-11-16,67,AB-,+91-00000-53724,Kanyakumari,None known,2022-12-01
P00962,Rachit Deo,M,1990-11-16,34,A+,+91-00000-20097,Thiruvananthapuram,None known,2022-01-20
P00963,Ladli Rama,F,1947-02-15,78,AB+,+91-00000-80927,Kottayam,None known,2023-10-24
P00964,Shivansh Mallick,M,2014-12-06,10,AB-,+91-00000-21805,Alappuzha,None known,2023-05-20
P00965,Panini Chaudry,F,1979-04-13,46,O+,+91-00000-15889,Thiruvananthapuram,None known,2023-04-26
P00966,Damini Chaudhary,F,1960-09-04,64,O+,+91-00000-44503,Alappuzha,None known,2022-05-31
P00967,Utkarsh Kadakia,M,1991-06-25,34,AB+,+91-00000-48618,Kanyakumari,None known,2022-05-09
P00968,Chaitanya Patla,M,1985-10-04,39,A+,+91-00000-95566,Pathanamthitta,None known,2023-10-24
P00969,Adweta Prasad,F,1935-08-20,89,A-,+91-00000-40435,Thiruvananthapuram,None known,2022-08-21
P00970,Amruta Padmanabhan,F,1939-03-24,86,AB+,+91-00000-91118,Thiruvananthapuram,None known,2021-11-23
P00972,Wahab Bora,M,2012-08-23,12,AB+,+91-00000-36809,Alappuzha,None known,2022-05-14
P00973,Pratyush Garde,M,2000-12-14,24,AB+,+91-00000-22979,Kanyakumari,None known,2022-08-20
P00974,Vincent Tiwari,M,1996-11-10,28,A+,+91-00000-91243,Pathanamthitta,None known,2023-01-18
P00975,Nakul Srinivasan,M,1958-07-30,67,AB-,+91-00000-54406,Kanyakumari,None known,2023-12-05
P00976,Bhavani Kapadia,F,2003-03-01,22,B+,+91-00000-69728,Pathanamthitta,None known,2023-03-30
P00977,Aishani Rana,F,2000-09-17,24,AB-,+91-00000-35825,Kollam,None known,2022-01-30
P00978,Upma Karpe,F,1970-02-07,55,AB-,+91-00000-29306,Alappuzha,Penicillin,2022-09-01
P00979,Dayamai Bhandari,F,1984-08-07,40,B-,+91-00000-74701,Kottayam,NSAIDs,2023-04-12
P00980,Bhavna Shere,F,1980-01-08,45,AB+,+91-00000-53964,Thiruvananthapuram,Penicillin,2023-06-15
P00982,Yochana Kadakia,F,1992-12-05,32,AB+,+91-00000-11521,Alappuzha,None known,2023-06-20
P00983,Yadavi Pingle,F,1988-06-19,37,A-,+91-00000-55045,Kottayam,None known,2022-07-26
P00984,Ekbal Varma,M,1972-05-23,53,A-,+91-00000-56839,Alappuzha,None known,2022-09-28
P00985,Rudra Char,M,1974-02-19,51,B-,+91-00000-98643,Kanyakumari,None known,2022-05-15
P00986,Benjamin Aggarwal,M,1998-08-21,26,B-,+91-00000-31543,Kottayam,None known,2022-08-08
P00987,Fiyaz Kulkarni,M,1999-01-09,26,A+,+91-00000-36356,Kollam,None known,2023-07-01
P00988,Warjas Dar,M,1975-05-08,50,B+,+91-00000-65697,Alappuzha,None known,2021-10-02
P00990,Faras Babu,M,1975-09-08,49,AB+,+91-00000-73735,Kollam,None known,2023-10-22
P00991,Qasim Pau,M,1958-03-28,67,AB+,+91-00000-45458,Thiruvananthapuram,None known,2021-12-07
P00992,Amaira Chopra,F,1942-01-04,83,B+,+91-00000-47142,Pathanamthitta,None known,2023-01-30
P00993,Pushti Sachar,F,2003-10-13,21,A+,+91-00000-76226,Pathanamthitta,None known,2023-05-07
P00994,Dayamai Chandra,F,2009-12-08,15,B-,+91-00000-25372,Alappuzha,None known,2022-10-01
P00995,Matthew Tripathi,M,1997-03-27,28,AB-,+91-00000-81949,Thiruvananthapuram,None known,2021-09-29
P00996,Diya Bir,F,1961-01-29,64,AB+,+91-00000-62567,Alappuzha,None known,2022-05-02
P00998,Chaitanya Upadhyay,M,1938-12-05,86,O+,+91-00000-94902,Kollam,None known,2023-11-18
P01002,Samuel Shukla,M,2020-05-27,5,B-,+91-00000-53683,Pathanamthitta,None known,2023-02-19
P01003,Avni Kalla,F,2018-03-30,7,A+,+91-00000-63039,Thiruvananthapuram,None known,2023-03-04
P01004,Upkaar Garde,M,1948-10-26,76,A+,+91-00000-50947,Kollam,None known,2023-06-30
P01005,Damini Sharaf,F,2017-06-26,8,O-,+91-00000-37921,Kanyakumari,None known,2022-12-26
P01006,Ekapad Chawla,M,1955-09-04,69,A+,+91-00000-76346,Kollam,None known,2023-02-03
P01007,Zayan Dubey,M,1984-02-15,41,AB-,+91-00000-90604,Kottayam,None known,2023-10-26
P01008,Ekbal Vohra,M,2020-08-11,4,B+,+91-00000-68898,Pathanamthitta,Penicillin,2023-10-11
P01009,Harini Ray,F,2006-10-30,18,O-,+91-00000-86167,Pathanamthitta,None known,2023-02-21
P01010,Daniel Sachdev,M,1999-08-30,25,A+,+91-00000-77971,Pathanamthitta,None known,2023-02-10
P01011,Aashi Karnik,F,1965-06-11,60,O-,+91-00000-20747,Alappuzha,None known,2023-05-20
P01013,Raghav Dugar,M,1939-03-05,86,B+,+91-00000-65202,Kottayam,None known,2022-07-07
P01014,Manan Wali,M,1963-03-02,62,B+,+91-00000-26836,Thiruvananthapuram,None known,2023-08-13
P01015,Akshay Ravel,M,1970-01-12,55,B-,+91-00000-62360,Alappuzha,None known,2021-11-13
P01016,Christopher Tak,M,2005-08-09,19,B+,+91-00000-41923,Kanyakumari,None known,2022-04-20
P01017,Netra Batra,F,1996-07-08,29,B-,+91-00000-48133,Alappuzha,None known,2023-01-16
P01018,Saumya Saha,F,2025-02-27,0,B+,+91-00000-74448,Pathanamthitta,None known,2023-09-28
P01019,Netra Brar,F,1947-04-11,78,A+,+91-00000-46869,Pathanamthitta,None known,2023-05-01
P01021,Dayita Saini,F,1954-02-28,71,A-,+91-00000-68103,Kottayam,None known,2022-10-30
P01022,Omya Suresh,F,1948-06-18,77,B+,+91-00000-82376,Thiruvananthapuram,None known,2023-12-08
P01023,Harsh Devi,M,2020-06-05,5,O-,+91-00000-53937,Kottayam,None known,2022-03-15
P01024,Yamini Chatterjee,F,1979-04-16,46,O+,+91-00000-45354,Alappuzha,Sulfa drugs,2023-08-13
P01025,Ronith Mistry,M,1955-10-24,69,AB+,+91-00000-15767,Pathanamthitta,None known,2021-10-01
P01026,Lila Kuruvilla,F,1977-02-01,48,A+,+91-00000-42107,Alappuzha,None known,2023-06-28
P01027,Imaran Pillai,M,1973-04-15,52,AB+,+91-00000-78422,Thiruvananthapuram,None known,2021-11-10
P01028,Chaman Sanghvi,F,1975-02-27,50,AB+,+91-00000-77670,Pathanamthitta,None known,2022-07-24
P01029,William Rajagopalan,M,1990-05-22,35,B+,+91-00000-56569,Kottayam,None known,2021-08-24
P01030,Praneel Sani,M,1974-08-23,50,B+,+91-00000-25884,Kollam,None known,2021-12-10
P01031,Osha Seshadri,F,1998-11-19,26,A-,+91-00000-81901,Kollam,None known,2022-05-15
P01032,Devika Bawa,F,1981-02-09,44,AB+,+91-00000-30097,Pathanamthitta,None known,2023-08-09
P01033,Nimrat Wali,F,1978-11-06,46,AB+,+91-00000-17115,Pathanamthitta,None known,2023-09-27
P01034,Azaan Gade,M,1936-10-13,88,B+,+91-00000-11424,Kollam,None known,2022-05-14
P01035,Zarna Raja,F,1985-01-28,40,B-,+91-00000-51016,Kollam,Penicillin,2022-02-26
P01036,Ojasvi Ratta,F,2014-08-17,10,O-,+91-00000-55424,Kollam,None known,2021-11-19
P01038,Ria Bali,F,2007-03-31,18,AB-,+91-00000-31920,Alappuzha,None known,2023-11-28
P01039,Naksh Parsa,M,2005-08-29,19,A+,+91-00000-26646,Kottayam,None known,2023-03-25
P01040,Warhi Karpe,F,2014-02-16,11,A-,+91-00000-66846,Kollam,NSAIDs,2023-03-08
P01041,Yoshita Vyas,F,2019-09-05,5,AB-,+91-00000-32359,Thiruvananthapuram,None known,2023-02-10
P01042,Yagnesh Andra,M,2012-07-26,12,A+,+91-00000-15359,Kottayam,None known,2023-05-08
P01043,Rachit Ray,M,1947-04-26,78,B-,+91-00000-79372,Thiruvananthapuram,None known,2022-11-27
P01044,Charles Amble,M,1959-09-29,65,A-,+91-00000-39429,Pathanamthitta,None known,2022-06-19
P01045,Rachana Koshy,F,1966-12-29,58,A+,+91-00000-48368,Kottayam,None known,2021-08-27
P01046,Qadim Pillay,M,1958-02-16,67,AB+,+91-00000-80177,Kollam,None known,2023-09-23
P01047,Nidhi Kadakia,F,1940-08-18,84,AB-,+91-00000-64580,Alappuzha,None known,2023-07-12
P01048,Ayaan Murty,M,1988-04-26,37,B-,+91-00000-96235,Kottayam,None known,2023-09-08
P01049,George Tank,M,2000-06-11,25,AB+,+91-00000-78229,Kanyakumari,Sulfa drugs,2023-07-07
P01051,Orinder Bera,M,1982-03-10,43,O-,+91-00000-81201,Kollam,None known,2024-01-04
P01052,Chakradhar Kala,M,2016-01-16,9,AB-,+91-00000-12795,Thiruvananthapuram,None known,2021-11-11
P01053,Lajita Madan,F,2002-11-05,22,A-,+91-00000-16778,Kottayam,None known,2022-06-02
P01054,Simon Prakash,M,1987-10-15,37,A-,+91-00000-53154,Kottayam,None known,2023-05-19
P01055,Suhani Chakraborty,F,1961-12-28,63,B-,+91-00000-46314,Kottayam,None known,2023-05-04
P01056,Mekhala Chatterjee,F,1937-01-10,88,AB+,+91-00000-14032,Pathanamthitta,None known,2023-09-17
P01057,Brijesh Ranganathan,M,1956-07-22,69,AB-,+91-00000-92722,Kanyakumari,None known,2022-10-28
P01058,Jeevika Krishna,F,1971-09-10,53,AB+,+91-00000-98452,Alappuzha,None known,2023-10-31
P01059,Nitesh Bali,M,1989-05-23,36,A+,+91-00000-49330,Thiruvananthapuram,None known,2022-06-28
P01060,Nathan Dixit,M,2004-02-20,21,A+,+91-00000-69865,Thiruvananthapuram,None known,2023-12-11
P01061,Garima Mangal,F,1966-04-12,59,A+,+91-00000-66983,Pathanamthitta,None known,2023-12-31
P01062,Megha Bhandari,F,1985-09-20,39,AB-,+91-00000-59464,Thiruvananthapuram,None known,2022-09-23
P01063,Xalak Bava,F,1956-12-18,68,B-,+91-00000-87883,Kottayam,None known,2022-01-22
P01065,Ekantika Oak,F,1956-06-22,69,B+,+91-00000-34309,Thiruvananthapuram,None known,2022-11-10
P01066,Alka Kakar,F,1946-09-21,78,B+,+91-00000-28660,Thiruvananthapuram,None known,2022-10-14
P01067,Aarnav Srinivas,M,1960-03-02,65,O+,+91-00000-62444,Kottayam,None known,2022-02-21
P01068,Ubika Nayak,F,2002-09-09,22,AB+,+91-00000-35247,Kottayam,None known,2024-01-10
P01069,Baljiwan Gera,M,2000-09-05,24,B-,+91-00000-67245,Kollam,None known,2023-10-29
P01070,Chakrika Sastry,F,1995-05-13,30,A+,+91-00000-84193,Kanyakumari,None known,2022-10-25
P01071,Ekiya Purohit,F,2012-06-27,13,AB-,+91-00000-16182,Alappuzha,None known,2023-06-13
P01072,Udarsh Sarkar,M,2020-06-13,5,B+,+91-00000-70319,Thiruvananthapuram,None known,2023-09-23
P01073,Dhriti Saxena,F,1980-06-15,45,AB+,+91-00000-64724,Thiruvananthapuram,None known,2022-01-31
P01074,Nathaniel Bora,M,1966-02-09,59,B-,+91-00000-99778,Kollam,None known,2022-07-25
P01076,Daksh Dani,M,2015-10-19,9,O+,+91-00000-36283,Kanyakumari,None known,2022-05-23
P01078,Dakshesh Kakar,M,1994-07-13,31,A-,+91-00000-28446,Thiruvananthapuram,None known,2023-11-16
P01079,Chasmum Sachdeva,F,1974-03-02,51,A+,+91-00000-41513,Alappuzha,None known,2023-12-13
P01080,Ojasvi Yadav,F,1967-10-08,57,O-,+91-00000-83375,Alappuzha,None known,2023-05-15
P01081,Ekaraj Dasgupta,M,1972-03-04,53,O+,+91-00000-13120,Alappuzha,None known,2021-09-04
P01082,Faras Mahal,M,1962-01-08,63,B-,+91-00000-42668,Pathanamthitta,None known,2023-10-01
P01083,Vrishti Reddy,F,1980-06-13,45,O+,+91-00000-21272,Alappuzha,None known,2021-10-01
P01084,Anamika Sankaran,F,2017-08-21,7,B+,+91-00000-68164,Thiruvananthapuram,None known,2021-08-25
P01085,Ranbir Iyer,M,1954-05-28,71,A-,+91-00000-26966,Alappuzha,None known,2022-07-04
P01086,Yug Tak,M,1992-09-24,32,B+,+91-00000-63155,Kollam,None known,2023-03-26
P01087,Urmi Rama,F,1963-05-17,62,B+,+91-00000-21680,Kanyakumari,None known,2023-07-25
P01088,Wridesh Cheema,M,2020-12-20,4,O-,+91-00000-79016,Kollam,None known,2023-05-10
P01089,Fiyaz Naik,M,2008-11-22,16,A+,+91-00000-39503,Thiruvananthapuram,None known,2023-12-04
P01090,Isha Aurora,F,1971-02-08,54,O-,+91-00000-62373,Kanyakumari,NSAIDs,2021-12-26
P01092,Pushti Purohit,F,1990-09-19,34,A+,+91-00000-74775,Kanyakumari,None known,2023-01-06
P01093,Yoshita Rama,F,2019-05-04,6,O+,+91-00000-66163,Thiruvananthapuram,Sulfa drugs,2023-05-25
P01095,Rachita Divan,F,1937-03-25,88,O+,+91-00000-88689,Thiruvananthapuram,None known,2022-08-11
P01096,Warda Randhawa,F,1944-04-20,81,B-,+91-00000-59517,Pathanamthitta,None known,2022-01-10
P01097,Omisha Chana,F,2005-06-23,20,A+,+91-00000-41936,Pathanamthitta,None known,2022-06-28
P01098,Yash Kaur,M,2006-07-01,19,B+,+91-00000-77121,Kottayam,None known,2023-05-19
P01099,Leena Panchal,F,1985-05-31,40,O+,+91-00000-94669,Kollam,None known,2023-08-15
P01101,Lavanya Bhatt,F,1987-07-04,38,A-,+91-00000-25147,Alappuzha,None known,2022-10-24
P01103,Jairaj Kala,M,1991-11-07,33,B+,+91-00000-16407,Thiruvananthapuram,None known,2023-06-29
P01104,Tarak Bhattacharyya,M,2000-10-03,24,O+,+91-00000-26536,Thiruvananthapuram,None known,2022-04-29
P01105,Gautam Sachdev,M,1992-06-11,33,AB+,+91-00000-91173,Alappuzha,None known,2022-11-11
P01106,Vedant Ram,M,1963-02-06,62,AB+,+91-00000-48592,Kanyakumari,None known,2023-01-16
P01107,Widisha Dalal,F,1945-04-30,80,AB-,+91-00000-17573,Kollam,Sulfa drugs,2022-04-17
P01108,Jack Grewal,M,2001-01-20,24,A+,+91-00000-12297,Pathanamthitta,None known,2021-08-26
P01110,Zashil Doctor,M,2015-12-21,9,B-,+91-00000-97521,Alappuzha,None known,2021-10-31
P01111,Anika Pandey,F,2007-07-05,18,AB+,+91-00000-10340,Pathanamthitta,None known,2023-03-31
P01112,Fariq Suri,M,2002-11-10,22,O+,+91-00000-50555,Kanyakumari,None known,2023-10-13
P01113,Osha Suri,F,1966-05-12,59,B+,+91-00000-68697,Kottayam,None known,2022-04-06
P01114,Faqid Sekhon,M,1977-04-09,48,AB-,+91-00000-57171,Kottayam,Sulfa drugs,2022-01-15
P01115,Pranav Mittal,M,1988-03-04,37,A-,+91-00000-24993,Kanyakumari,Sulfa drugs,2021-09-20
P01116,Chandran Koshy,M,1966-11-10,58,O+,+91-00000-17435,Kanyakumari,None known,2022-08-05
P01117,Faras Kamdar,M,2016-01-03,9,A-,+91-00000-72470,Pathanamthitta,None known,2023-08-26
P01119,Pooja Dara,F,2000-05-19,25,B-,+91-00000-13774,Kottayam,Penicillin,2022-04-16
P01120,Gautami Gupta,F,2017-07-13,8,AB+,+91-00000-70224,Thiruvananthapuram,None known,2022-05-07
P01121,Frado Pillay,M,2022-05-20,3,AB-,+91-00000-72112,Kollam,None known,2023-02-04
P01122,Omaja Patla,F,1965-04-04,60,AB+,+91-00000-58560,Kanyakumari,Sulfa drugs,2022-12-07
P01123,Chatura Mannan,M,1989-10-29,35,A+,+91-00000-45250,Alappuzha,None known,2023-09-18
P01124,Kevin Choudhry,M,2013-02-11,12,B+,+91-00000-85110,Pathanamthitta,None known,2023-04-19
P01126,Advaith Gera,M,1969-02-09,56,A-,+91-00000-33851,Thiruvananthapuram,None known,2023-05-30
P01127,Lajita Memon,F,1967-09-08,57,AB+,+91-00000-57269,Kottayam,Sulfa drugs,2023-07-15
P01128,Luke Krishnan,M,1958-10-18,66,O-,+91-00000-45305,Kollam,None known,2022-06-16
P01129,Ekaja Lala,F,2001-09-20,23,B-,+91-00000-78899,Thiruvananthapuram,None known,2023-05-07
P01130,Watika Borra,F,1995-01-07,30,O-,+91-00000-63521,Pathanamthitta,None known,2022-03-27
P01133,Faqid Ramakrishnan,M,1996-09-27,28,B-,+91-00000-48302,Kollam,None known,2021-12-10
P01134,Gauri Deep,F,1975-11-27,49,A+,+91-00000-23232,Kollam,None known,2022-05-13
P01135,Chaitanya Gaba,M,1971-09-21,53,A-,+91-00000-86621,Thiruvananthapuram,None known,2022-06-05
P01136,Kalpit Mohan,M,2010-06-23,15,B-,+91-00000-65641,Alappuzha,None known,2023-12-16
P01137,Avni Sane,F,2005-10-01,19,O+,+91-00000-96624,Kottayam,None known,2023-01-19
P01138,Radhika Kaur,F,2001-11-18,23,B-,+91-00000-85519,Pathanamthitta,None known,2023-06-04
P01139,Warda Sethi,F,2015-03-06,10,O+,+91-00000-74801,Kanyakumari,None known,2023-01-06
P01140,Qasim Pai,M,2004-04-25,21,A-,+91-00000-83863,Thiruvananthapuram,None known,2023-06-16
P01141,Janaki Tiwari,F,1949-12-29,75,B-,+91-00000-29940,Kanyakumari,None known,2021-08-04
P01142,Lopa Palla,F,1987-12-05,37,B-,+91-00000-90043,Thiruvananthapuram,None known,2023-04-08
P01143,Jack Borra,M,1935-05-23,90,A+,+91-00000-81278,Thiruvananthapuram,None known,2022-08-25
P01144,Christopher Bora,M,1935-03-13,90,O-,+91-00000-55060,Pathanamthitta,None known,2023-01-19
P01146,Charan Dar,M,1992-05-15,33,A+,+91-00000-26458,Thiruvananthapuram,None known,2022-01-17
P01147,Indali Pillai,F,2017-07-19,8,B-,+91-00000-82342,Alappuzha,NSAIDs,2022-01-17
P01148,Nilima Pandya,F,2001-12-21,23,O-,+91-00000-39223,Kollam,None known,2023-01-18
P01149,Ekta Bhat,F,1983-05-28,42,AB-,+91-00000-16951,Kollam,None known,2023-02-07
P01151,Amruta Sachdev,F,2009-04-06,16,O-,+91-00000-69425,Kanyakumari,None known,2022-08-21
P01152,Eshana Verma,F,2016-07-12,9,AB+,+91-00000-75993,Thiruvananthapuram,None known,2023-08-12
P01153,Brinda Sarkar,F,2019-07-25,5,AB-,+91-00000-43280,Kottayam,None known,2023-08-22
P01154,George Chadha,M,2009-01-22,16,AB-,+91-00000-14405,Alappuzha,None known,2022-08-15
P01155,Zansi Pandya,F,2013-09-22,11,A-,+91-00000-53199,Kottayam,None known,2023-05-17
P01156,Yahvi Hora,F,2003-02-13,22,O-,+91-00000-56691,Alappuzha,None known,2022-11-17
P01157,Dalaja Sahni,F,1996-07-01,29,AB+,+91-00000-96008,Kollam,None known,2023-08-24
P01158,Ekiya Sunder,F,1989-08-12,35,AB+,+91-00000-10520,Thiruvananthapuram,None known,2023-09-13
P01159,Gopal Brar,M,1997-02-05,28,AB+,+91-00000-45490,Pathanamthitta,None known,2022-04-07
P01160,Widisha Balan,F,1958-10-17,66,O-,+91-00000-67005,Thiruvananthapuram,None known,2023-03-12
P01161,Chanchal Deshmukh,F,1995-03-23,30,AB-,+91-00000-76628,Kollam,None known,2022-01-17
P01162,Netra Kunda,F,1996-12-23,28,A-,+91-00000-56085,Alappuzha,Penicillin,2021-11-23
P01164,Laban Dora,M,1947-03-29,78,B-,+91-00000-50308,Thiruvananthapuram,None known,2023-06-14
P01165,Faras Sane,M,1972-04-10,53,O+,+91-00000-56917,Kottayam,None known,2022-08-03
P01168,Chameli Venkataraman,F,1989-11-16,35,B-,+91-00000-28217,Kottayam,None known,2021-11-26
P01169,Farhan Balay,M,2006-12-16,18,AB-,+91-00000-95936,Kottayam,Penicillin,2022-07-01
P01170,Chatura Choudhury,M,2006-04-12,19,AB-,+91-00000-29853,Alappuzha,Sulfa drugs,2022-08-01
P01171,Manthan Mitra,M,1988-09-20,36,AB+,+91-00000-51784,Kollam,None known,2021-12-07
P01172,Amaira Sachdeva,F,1973-07-13,52,B+,+91-00000-81828,Kottayam,None known,2022-10-26
P01173,Amol Dixit,M,1992-04-29,33,A+,+91-00000-16527,Kanyakumari,None known,2023-10-19
P01174,Idika Venkatesh,F,2014-02-23,11,B+,+91-00000-40724,Kollam,None known,2023-01-18
P01175,Chakrika Acharya,F,2017-10-15,7,O+,+91-00000-78211,Kollam,Sulfa drugs,2022-12-30
P01177,Hritik Rana,M,1943-04-19,82,A-,+91-00000-61729,Thiruvananthapuram,None known,2023-02-15
P01178,Jack Reddy,M,1982-11-09,42,O+,+91-00000-93545,Pathanamthitta,Penicillin,2022-08-31
P01179,Parth Nayak,M,2020-07-29,4,O+,+91-00000-49379,Kanyakumari,None known,2023-04-03
P01180,Januja Palan,F,1972-11-02,52,B+,+91-00000-52156,Kollam,Penicillin,2023-04-02
P01181,Rohan Aurora,M,1981-02-08,44,O-,+91-00000-28075,Kanyakumari,NSAIDs,2022-04-01
P01182,Jai Lala,M,1975-01-16,50,AB-,+91-00000-25645,Kollam,None known,2022-11-30
P01183,Arunima Pingle,F,1943-09-08,81,AB-,+91-00000-47930,Kottayam,None known,2023-08-30
P01185,Patrick Sha,M,1981-09-24,43,AB+,+91-00000-16791,Kollam,None known,2022-11-04
P01186,Kamya Sachdeva,F,1984-10-12,40,A-,+91-00000-71944,Alappuzha,None known,2023-09-03
P01187,Harita Iyer,F,1965-04-24,60,O+,+91-00000-35673,Thiruvananthapuram,None known,2022-06-06
P01188,Falan Kakar,M,1982-07-13,43,B+,+91-00000-93762,Kottayam,None known,2023-12-27
P01189,Lajita Seth,F,1975-01-12,50,AB-,+91-00000-78308,Pathanamthitta,Penicillin,2021-08-30
P01190,Wakeeta Kant,F,1947-09-02,77,B+,+91-00000-44396,Thiruvananthapuram,None known,2021-12-12
P01191,Osha Goyal,F,1969-12-31,55,O-,+91-00000-65303,Pathanamthitta,None known,2023-11-13
P01192,Kashish Lad,F,2002-09-22,22,O+,+91-00000-19698,Thiruvananthapuram,None known,2021-08-22
P01193,Joshua Bains,M,2022-04-27,3,A-,+91-00000-66928,Pathanamthitta,None known,2022-03-25
P01194,George Mukhopadhyay,M,1966-08-20,58,B-,+91-00000-29728,Kollam,None known,2022-09-09
P01195,Jack Bhatti,M,1964-03-21,61,B+,+91-00000-99490,Alappuzha,None known,2022-04-08
P01196,Nidhi Upadhyay,F,1963-07-24,62,AB-,+91-00000-42536,Pathanamthitta,None known,2022-07-13
P01197,Nitesh Jayaraman,M,2016-01-30,9,AB+,+91-00000-42490,Kanyakumari,None known,2021-12-24
P01198,Anika Kota,F,1956-11-08,68,B+,+91-00000-86713,Thiruvananthapuram,None known,2023-09-08
P01199,Chakradhar Brar,M,1935-01-09,90,B+,+91-00000-50018,Kottayam,None known,2022-09-03
P01200,Zayan Konda,M,1995-04-28,30,O+,+91-00000-12044,Alappuzha,None known,2022-05-06
P01201,Vaishnavi Kamdar,F,1975-12-01,49,B+,+91-00000-22264,Kottayam,None known,2022-02-12
P01202,Anthony Sachdeva,M,2007-12-03,17,B-,+91-00000-79797,Kollam,None known,2021-08-03
P01203,Ekantika Prabhakar,F,1947-12-14,77,AB-,+91-00000-75726,Kottayam,None known,2023-11-23
P01204,Rachana Boase,F,1986-04-18,39,B-,+91-00000-39148,Kollam,Penicillin,2022-05-27
P01205,Bina Ram,F,1978-04-11,47,AB-,+91-00000-50864,Pathanamthitta,None known,2022-04-08
P01206,Ekansh Saini,M,1979-12-15,45,A+,+91-00000-28688,Kollam,None known,2021-12-08
P01207,Jackson Nigam,M,1996-07-06,29,AB+,+91-00000-29160,Alappuzha,None known,2022-04-08
P01208,Ishanvi Raghavan,F,1966-05-02,59,AB-,+91-00000-49007,Alappuzha,None known,2023-06-20
P01209,Mekhala Bir,F,2010-03-26,15,A-,+91-00000-42229,Alappuzha,None known,2023-01-05
P01210,Wazir Atwal,M,1994-09-18,30,B+,+91-00000-97760,Kollam,None known,2023-05-25
P01211,Ati Tara,F,2005-05-21,20,O+,+91-00000-81045,Kollam,None known,2022-02-06
P01212,Amol Rai,M,1979-06-03,46,AB+,+91-00000-54018,Thiruvananthapuram,None known,2021-08-12
P01214,Gauri Dhar,F,1936-09-27,88,O-,+91-00000-25364,Thiruvananthapuram,None known,2023-04-26
P01215,Bahadurjit Jha,M,2002-12-09,22,AB+,+91-00000-20428,Alappuzha,None known,2023-05-02
P01216,Gauri Tailor,F,1948-11-14,76,B-,+91-00000-34702,Kottayam,None known,2022-03-22
P01217,Isaiah Nagar,M,1948-02-26,77,B+,+91-00000-17071,Kanyakumari,None known,2023-05-29
P01218,Onveer Devi,M,1955-08-17,69,A+,+91-00000-13840,Kottayam,Sulfa drugs,2023-01-13
P01219,Ekanta Dhar,F,1979-09-21,45,B-,+91-00000-95326,Kottayam,None known,2021-11-26
P01220,Odika Basak,F,2009-02-02,16,A-,+91-00000-39815,Thiruvananthapuram,None known,2023-08-07
P01221,Gopal Khalsa,M,1977-03-04,48,A+,+91-00000-24856,Kollam,None known,2022-09-15
P01222,Ekanta Khalsa,F,2018-10-15,6,O+,+91-00000-84664,Kanyakumari,None known,2021-10-01
P01223,Utkarsh Pillai,M,1936-07-11,89,AB-,+91-00000-98937,Alappuzha,NSAIDs,2022-12-23
P01226,Bimala Goyal,F,1953-02-08,72,AB+,+91-00000-55224,Kanyakumari,None known,2023-03-06
P01227,Oscar Bawa,M,2003-10-31,21,O+,+91-00000-80710,Kanyakumari,None known,2022-07-03
P01228,David Mohanty,M,2014-03-26,11,B+,+91-00000-67923,Kanyakumari,None known,2021-11-01
P01229,Naveen Goswami,M,1972-06-12,53,O+,+91-00000-54406,Pathanamthitta,None known,2021-09-05
P01230,Darsh Mahal,M,1962-02-20,63,B-,+91-00000-29895,Pathanamthitta,None known,2022-07-26
P01231,Timothy Vyas,M,1936-01-14,89,AB-,+91-00000-51029,Kanyakumari,None known,2023-03-27
P01232,Karan Chanda,M,1939-04-09,86,AB-,+91-00000-29384,Kollam,None known,2022-05-24
P01233,Chaitaly Kapoor,F,1984-01-26,41,O+,+91-00000-83021,Kanyakumari,None known,2023-03-07
P01234,Abhiram Bose,M,2008-12-23,16,A+,+91-00000-96123,Kanyakumari,None known,2022-03-16
P01235,Nilima Thakur,F,1973-03-06,52,AB+,+91-00000-57008,Pathanamthitta,None known,2023-08-17
P01236,Girik Dyal,M,1983-02-08,42,A-,+91-00000-54260,Kollam,None known,2023-10-31
P01237,Noah Cheema,M,1988-08-28,36,O+,+91-00000-70406,Kollam,None known,2023-09-28
P01238,Manan Sule,M,2014-12-29,10,AB-,+91-00000-66598,Kollam,None known,2023-09-30
P01239,Victor Palla,M,2022-01-21,3,B+,+91-00000-80252,Thiruvananthapuram,None known,2021-12-13
P01240,Yash Shroff,M,1993-08-19,31,AB+,+91-00000-53003,Alappuzha,None known,2023-01-15
P01243,Advik Sarna,M,2021-08-22,3,AB+,+91-00000-38676,Kottayam,None known,2023-06-01
P01244,Sai Ben,M,1982-01-23,43,AB+,+91-00000-71708,Pathanamthitta,None known,2022-01-14
P01246,Aradhana Ghose,F,1993-03-23,32,B-,+91-00000-10491,Kanyakumari,None known,2023-04-12
P01247,Sai Kakar,M,1968-10-03,56,O-,+91-00000-63741,Kollam,None known,2022-06-30
P01249,Imaran Samra,M,1968-11-05,56,B+,+91-00000-49059,Alappuzha,Penicillin,2023-09-11
P01250,Zaid Bhatnagar,M,1977-03-25,48,B-,+91-00000-91909,Pathanamthitta,None known,2021-11-19
P01251,Viraj Bakshi,M,2013-07-29,11,A-,+91-00000-97563,Kottayam,NSAIDs,2021-11-21
P01252,Gavin Oommen,M,2018-09-12,6,B+,+91-00000-58712,Kanyakumari,None known,2022-02-05
P01253,Advika Ganesan,F,1981-01-30,44,A-,+91-00000-62015,Kanyakumari,None known,2021-12-21
P01254,Max Barman,M,2001-03-04,24,AB+,+91-00000-98244,Kottayam,None known,2023-11-04
P01255,Pahal Lad,F,1989-01-14,36,A+,+91-00000-72142,Kottayam,None known,2022-04-18
P01256,Qasim Solanki,M,1986-08-03,38,B-,+91-00000-61010,Kanyakumari,None known,2023-09-11
P01258,Geetika Parikh,F,1940-06-01,85,B-,+91-00000-54558,Kanyakumari,None known,2021-09-04
P01259,Ekbal Saha,M,1958-03-29,67,AB+,+91-00000-82833,Pathanamthitta,Sulfa drugs,2023-05-05
P01260,Tanish Zachariah,M,1971-01-12,54,B-,+91-00000-70439,Kanyakumari,NSAIDs,2022-11-26
P01261,Veda Kunda,F,1994-09-24,30,A-,+91-00000-63423,Kollam,None known,2024-01-04
P01263,Jackson Gaba,M,1960-01-09,65,O-,+91-00000-71698,Kanyakumari,None known,2023-12-14
P01264,Vinaya Upadhyay,F,2025-07-18,0,A+,+91-00000-87449,Kanyakumari,None known,2022-10-24
P01265,Mitali Garg,F,1982-08-22,42,A+,+91-00000-53811,Thiruvananthapuram,None known,2022-01-24
P01266,Naksh Keer,M,1972-05-24,53,O+,+91-00000-43312,Kottayam,None known,2023-09-02
P01268,Pallavi Mander,F,1942-02-28,83,O-,+91-00000-45388,Alappuzha,None known,2022-03-07
P01269,Chasmum Aggarwal,F,2013-10-27,11,O-,+91-00000-43008,Alappuzha,None known,2022-04-04
P01270,Prisha Srinivas,F,1981-04-26,44,B+,+91-00000-28200,Kollam,None known,2021-12-16
P01271,Daksh Tank,M,1941-03-16,84,B+,+91-00000-82788,Kanyakumari,None known,2023-10-04
P01272,Yasti Raghavan,F,1949-07-08,76,A+,+91-00000-73548,Kottayam,None known,2023-07-23
P01273,Aadi Taneja,M,1939-04-10,86,B-,+91-00000-25132,Kottayam,None known,2022-06-19
P01274,Suhani Luthra,F,1980-09-28,44,B-,+91-00000-48244,Alappuzha,None known,2022-09-30
P01275,Yuvraj Shere,M,1951-07-29,74,O-,+91-00000-68446,Pathanamthitta,None known,2023-05-03
P01276,Baghyawati Chana,F,1945-05-31,80,AB+,+91-00000-83820,Kollam,None known,2023-10-04
P01277,Odika Tank,F,1938-12-30,86,A+,+91-00000-79455,Kanyakumari,None known,2021-09-17
P01278,Warda Bhatia,F,2019-05-03,6,B-,+91-00000-70741,Pathanamthitta,None known,2021-12-06
P01279,Eshana Bala,F,1972-02-27,53,A+,+91-00000-29914,Thiruvananthapuram,None known,2022-02-15
P01280,Logan Yohannan,M,1971-06-19,54,O-,+91-00000-55991,Thiruvananthapuram,None known,2021-08-01
P01281,Vaishnavi Bedi,F,2024-04-05,1,O-,+91-00000-37445,Alappuzha,None known,2021-10-05
P01282,Brijesh Mammen,M,1936-05-14,89,B-,+91-00000-60904,Kanyakumari,None known,2022-12-23
P01283,Arya Keer,F,1999-11-28,25,O+,+91-00000-35102,Kottayam,None known,2022-07-09
P01284,Ryan Barman,M,1979-07-03,46,B+,+91-00000-15170,Alappuzha,None known,2023-03-05
P01285,Lakshmi Hayer,F,1977-06-03,48,O-,+91-00000-73910,Pathanamthitta,None known,2022-07-07
P01287,Unni Pandit,F,1998-05-27,27,B-,+91-00000-62767,Alappuzha,None known,2022-01-11
P01288,Barkha Bora,F,1996-03-21,29,O-,+91-00000-99196,Kanyakumari,None known,2023-05-30
P01289,Wishi Subramaniam,F,1939-01-02,86,O+,+91-00000-57309,Thiruvananthapuram,None known,2022-08-12
P01290,Forum Mannan,F,2010-01-16,15,AB-,+91-00000-27598,Alappuzha,None known,2023-06-01
P01291,Nakul Thakur,M,2022-10-18,2,B+,+91-00000-99191,Kottayam,None known,2022-01-02
P01292,Yashasvi Oommen,F,1954-06-20,71,AB+,+91-00000-13312,Alappuzha,None known,2022-10-28
P01293,Guneet Kale,M,2020-04-19,5,B-,+91-00000-45441,Pathanamthitta,None known,2022-02-27
P01295,Eesha Koshy,F,1971-03-25,54,B-,+91-00000-88518,Alappuzha,None known,2022-04-29
P01296,Laksh Mishra,M,1983-08-10,41,O+,+91-00000-66511,Pathanamthitta,None known,2021-11-17
P01298,Wazir Mitter,M,1977-02-19,48,B+,+91-00000-80876,Pathanamthitta,None known,2023-08-19
P01299,Jairaj Basu,M,2005-01-31,20,AB+,+91-00000-76167,Kottayam,None known,2023-05-03
P01301,Pavani Sinha,F,2011-01-18,14,B-,+91-00000-86618,Kanyakumari,None known,2022-04-12
P01302,Sudiksha Bhattacharyya,F,1999-01-20,26,AB-,+91-00000-75326,Pathanamthitta,None known,2022-08-13
P01303,Gauri Choudhary,F,1978-09-27,46,AB+,+91-00000-37296,Thiruvananthapuram,None known,2022-02-02
P01304,Leela Mani,F,1941-09-23,83,B-,+91-00000-24396,Kanyakumari,Penicillin,2021-10-24
P01306,Joshua Grewal,M,1938-01-03,87,O-,+91-00000-98200,Kottayam,NSAIDs,2023-07-16
P01307,Kalpit Dass,M,1955-03-03,70,A-,+91-00000-57872,Thiruvananthapuram,None known,2022-05-09
P01308,Barkha Sarin,F,1967-06-07,58,AB-,+91-00000-16632,Kottayam,None known,2023-06-08
P01309,Tanvi Ramesh,F,2023-08-09,1,O+,+91-00000-48536,Kollam,None known,2023-07-26
P01310,Aarav Lalla,M,1954-06-12,71,A-,+91-00000-27708,Thiruvananthapuram,None known,2021-10-05
P01311,Xiti Swamy,F,1988-03-30,37,B+,+91-00000-59282,Kanyakumari,None known,2022-12-31
P01312,Isaiah Rajagopalan,M,2006-06-05,19,B-,+91-00000-10233,Kottayam,None known,2021-12-08
P01313,Patrick Baral,M,1954-12-04,70,AB-,+91-00000-97271,Kottayam,None known,2022-03-18
P01314,Advay Dyal,M,1971-02-23,54,B-,+91-00000-89487,Thiruvananthapuram,None known,2022-10-03
P01315,Zaid Karnik,M,1985-04-18,40,A+,+91-00000-54451,Kottayam,None known,2022-11-24
P01316,Jack Dalal,M,1979-10-01,45,B-,+91-00000-49113,Kollam,None known,2023-07-30
P01317,Faraj Varty,M,1994-10-29,30,A-,+91-00000-96715,Kollam,None known,2022-02-21
P01318,Tanveer Mutti,M,2004-08-03,20,O-,+91-00000-21807,Thiruvananthapuram,None known,2023-10-17
P01320,Girik Bala,M,1993-09-03,31,A-,+91-00000-58525,Kottayam,None known,2023-01-17
P01321,Lila Chauhan,F,2002-10-27,22,O-,+91-00000-24726,Alappuzha,Sulfa drugs,2022-11-13
P01322,Noah Narasimhan,M,1965-06-05,60,B-,+91-00000-57525,Pathanamthitta,None known,2022-12-19
P01324,Maanav Walia,M,1934-08-29,90,AB+,+91-00000-31214,Kanyakumari,None known,2023-08-05
P01325,Nidra Shetty,F,1994-04-17,31,AB+,+91-00000-30322,Kollam,None known,2022-02-13
P01326,Barkha Nath,F,1994-08-16,30,A+,+91-00000-50442,Pathanamthitta,None known,2022-05-26
P01327,Chatura Mammen,M,1977-02-06,48,B-,+91-00000-51553,Pathanamthitta,None known,2021-08-16
P01328,Janani Virk,F,1938-10-04,86,O+,+91-00000-99258,Kollam,Sulfa drugs,2022-08-22
P01330,Andrew Char,M,1971-06-01,54,B+,+91-00000-12229,Pathanamthitta,Sulfa drugs,2023-08-31
P01331,Arya Solanki,F,2017-08-28,7,AB-,+91-00000-74822,Kanyakumari,None known,2022-01-25
P01332,Zansi Krish,F,1993-10-08,31,AB+,+91-00000-83863,Kanyakumari,Sulfa drugs,2022-10-12
P01333,Mitali Iyengar,F,1983-04-27,42,O-,+91-00000-84565,Kanyakumari,None known,2022-06-06
P01334,Qabil Khurana,M,1969-12-19,55,A+,+91-00000-79748,Kanyakumari,None known,2021-12-31
P01336,Rushil Boase,M,1946-11-14,78,A+,+91-00000-72753,Kollam,Sulfa drugs,2022-07-24
P01337,Pallavi Ben,F,1969-11-07,55,A-,+91-00000-45858,Kanyakumari,None known,2023-11-06
P01338,Peter Merchant,M,1969-03-27,56,AB-,+91-00000-15861,Kottayam,Penicillin,2022-07-23
P01339,Zansi Wali,F,1966-01-18,59,B+,+91-00000-73122,Pathanamthitta,Penicillin,2021-07-31
P01340,Sarthak Kale,M,1966-12-09,58,A+,+91-00000-61927,Thiruvananthapuram,Penicillin,2022-05-04
P01341,Samar Keer,M,1973-10-25,51,B-,+91-00000-14944,Pathanamthitta,None known,2022-04-25
P01342,Warjas Brar,M,1998-06-13,27,A+,+91-00000-56926,Kottayam,None known,2023-07-02
P01343,Darsh Sanghvi,M,1963-02-05,62,B-,+91-00000-54829,Pathanamthitta,None known,2023-02-26
P01344,Upma Soni,F,2002-10-09,22,B+,+91-00000-33117,Alappuzha,None known,2022-03-09
P01345,Sarthak Tella,M,1994-04-03,31,O+,+91-00000-68288,Kottayam,None known,2023-09-19
P01348,Caleb Gulati,M,1989-03-26,36,AB+,+91-00000-92108,Kanyakumari,None known,2023-12-20
P01351,Madhavi Nagar,F,1947-05-18,78,O+,+91-00000-26705,Alappuzha,NSAIDs,2022-12-23
P01352,Krish Barman,M,1991-08-17,33,A-,+91-00000-91953,Thiruvananthapuram,None known,2023-08-19
P01353,Ayush Shan,M,1952-11-06,72,AB-,+91-00000-70516,Kollam,Sulfa drugs,2023-12-22
P01355,Damyanti Soman,F,2018-07-24,6,B+,+91-00000-38566,Kanyakumari,None known,2022-07-01
P01356,Gunbir Krishnan,M,1977-04-03,48,AB+,+91-00000-67930,Thiruvananthapuram,None known,2023-09-15
P01357,Baghyawati Bobal,F,1989-03-31,36,A+,+91-00000-69989,Kanyakumari,None known,2022-12-27
P01358,Aarav Luthra,M,1984-06-17,41,O-,+91-00000-19101,Alappuzha,None known,2023-06-23
P01359,Vedika Sarma,F,1994-09-07,30,AB-,+91-00000-74329,Kollam,None known,2023-04-14
P01361,Yahvi Konda,F,1945-12-20,79,B+,+91-00000-25790,Alappuzha,None known,2023-01-07
P01363,Samarth Batra,M,2019-12-18,5,B-,+91-00000-70216,Kollam,Penicillin,2021-08-26
P01365,Jason Bhakta,M,1965-12-10,59,B-,+91-00000-47152,Pathanamthitta,None known,2022-08-22
P01366,Warjas Rau,M,1953-01-26,72,O+,+91-00000-85564,Kottayam,None known,2021-08-24
P01367,Abhiram Rajagopal,M,1994-05-03,31,O+,+91-00000-65299,Kanyakumari,None known,2021-12-06
P01368,Bina Raman,F,2017-01-11,8,B-,+91-00000-38137,Thiruvananthapuram,None known,2022-07-11
P01369,Vivaan Cherian,M,1978-01-15,47,AB-,+91-00000-55384,Pathanamthitta,None known,2023-03-09
P01370,Hemang Korpal,M,2010-03-05,15,O+,+91-00000-64385,Thiruvananthapuram,None known,2022-06-23
P01371,Yagnesh Mutti,M,2014-08-22,10,AB+,+91-00000-18827,Kottayam,None known,2023-10-05
P01372,Dipta Nayak,F,1966-07-03,59,B-,+91-00000-32140,Pathanamthitta,None known,2023-03-18
P01373,Nidra Bains,F,2014-05-01,11,A+,+91-00000-43465,Alappuzha,None known,2021-10-11
P01374,Janya Upadhyay,F,1953-06-05,72,AB-,+91-00000-54164,Pathanamthitta,Penicillin,2022-10-02
P01375,Tripti Rastogi,F,1968-09-02,56,A+,+91-00000-14392,Thiruvananthapuram,None known,2021-11-21
P01376,Inaya Kurian,F,1937-05-09,88,A+,+91-00000-16563,Kanyakumari,None known,2023-04-17
P01377,Anay Chanda,M,2019-06-09,6,B-,+91-00000-24297,Kanyakumari,None known,2023-12-06
P01378,Lipika Sen,F,1968-08-05,56,B-,+91-00000-10822,Kollam,Sulfa drugs,2022-02-18
P01379,Ishita Pau,F,2017-04-22,8,A-,+91-00000-41307,Alappuzha,Sulfa drugs,2022-03-15
P01380,Urmi Jayaraman,F,1975-01-29,50,O+,+91-00000-98350,Kanyakumari,None known,2022-01-18
P01381,Upkaar Saran,M,1969-10-14,55,AB-,+91-00000-62236,Kollam,None known,2022-03-19
P01382,Nakul Kakar,M,1982-03-08,43,O-,+91-00000-91593,Pathanamthitta,None known,2021-12-15
P01383,Alka Sabharwal,F,1970-11-06,54,O+,+91-00000-35485,Alappuzha,None known,2023-09-13
P01384,Max Chakraborty,M,1934-08-12,90,B+,+91-00000-23740,Pathanamthitta,None known,2023-08-05
P01385,Vedant Solanki,M,1934-12-24,90,AB+,+91-00000-91411,Thiruvananthapuram,None known,2022-10-06
P01386,Vasana Puri,F,1962-12-26,62,B-,+91-00000-49997,Kanyakumari,None known,2022-01-23
P01387,Zayyan Ratti,M,1940-11-20,84,A-,+91-00000-23534,Pathanamthitta,None known,2023-12-07
P01388,Bishakha Karan,F,1991-05-24,34,A+,+91-00000-83796,Alappuzha,None known,2023-07-31
P01389,Neelima Karnik,F,1974-08-25,50,O-,+91-00000-58810,Kollam,None known,2023-09-22
P01391,Jagvi Misra,F,1963-05-19,62,AB+,+91-00000-41499,Thiruvananthapuram,NSAIDs,2023-08-18
P01392,Isaiah Chada,M,1950-04-11,75,AB+,+91-00000-63081,Kottayam,Penicillin,2023-02-19
P01394,Adweta Saha,F,1973-11-07,51,B-,+91-00000-23484,Alappuzha,None known,2023-03-20
P01395,Pooja Sandhu,F,1962-05-02,63,B+,+91-00000-43290,Kanyakumari,None known,2021-12-22
P01396,Leela Chana,F,1953-04-24,72,B+,+91-00000-26206,Alappuzha,None known,2022-08-31
P01397,Sachi Kant,F,2003-06-24,22,B+,+91-00000-94733,Kanyakumari,None known,2022-04-05
P01398,Sneha Mistry,F,1970-07-23,55,AB-,+91-00000-76899,Pathanamthitta,None known,2022-03-20
P01399,Guneet Saraf,M,1995-07-04,30,A-,+91-00000-20869,Kottayam,None known,2023-09-23
P01400,Ayushman Tara,M,1956-04-03,69,A-,+91-00000-44467,Kottayam,None known,2023-02-11
P01402,Shivani Bhavsar,F,1942-01-13,83,B-,+91-00000-76219,Kottayam,None known,2022-09-01
P01403,Pallavi Patla,F,1989-11-03,35,A+,+91-00000-10743,Kanyakumari,None known,2023-07-28
P01404,Waida Krishnamurthy,F,2014-01-27,11,O+,+91-00000-78325,Thiruvananthapuram,Penicillin,2023-07-02
P01405,Kabir Reddy,M,1965-04-07,60,O-,+91-00000-34427,Thiruvananthapuram,Sulfa drugs,2022-12-09
P01406,Gaurangi Bakshi,F,2001-07-05,24,B+,+91-00000-32873,Thiruvananthapuram,None known,2021-12-26
P01407,Ekanta Nair,F,1992-12-03,32,B+,+91-00000-79464,Alappuzha,None known,2021-09-11
P01409,Laksh Oza,M,1956-05-13,69,A+,+91-00000-91837,Kollam,None known,2023-11-17
P01410,Yug Narain,M,2012-01-31,13,AB-,+91-00000-56900,Pathanamthitta,None known,2023-04-15
P01411,Geetika Talwar,F,1954-09-10,70,A+,+91-00000-43256,Thiruvananthapuram,None known,2022-03-29
P01413,Ucchal Dhillon,F,1986-04-14,39,O+,+91-00000-61417,Alappuzha,None known,2021-08-14
P01414,Chandran Bava,M,1949-01-16,76,A+,+91-00000-16321,Thiruvananthapuram,None known,2022-07-25
P01415,Victor Shere,M,1968-09-24,56,B-,+91-00000-68417,Alappuzha,None known,2022-04-04
P01416,Thomas Bajaj,M,2001-12-28,23,B+,+91-00000-11921,Pathanamthitta,None known,2022-12-02
P01417,Mohini Pandit,F,1999-12-14,25,AB+,+91-00000-34452,Thiruvananthapuram,None known,2023-03-19
P01418,Tarak Ben,M,1989-01-31,36,B-,+91-00000-38667,Kollam,NSAIDs,2021-12-12
P01419,Baljiwan Andra,M,1981-10-11,43,O+,+91-00000-96769,Thiruvananthapuram,None known,2023-09-15
P01420,Netra Ganguly,F,1944-12-16,80,A-,+91-00000-30710,Kottayam,None known,2023-09-13
P01421,Rajata Kalita,F,1949-04-25,76,O-,+91-00000-98476,Kollam,Penicillin,2023-12-28
P01422,Ranveer Mahal,M,1970-03-21,55,O-,+91-00000-27765,Alappuzha,None known,2023-02-10
P01423,Elijah Parmer,M,1981-03-09,44,O-,+91-00000-24882,Pathanamthitta,Sulfa drugs,2023-10-12
P01424,Yashvi Bajwa,F,1994-12-30,30,O+,+91-00000-77007,Kollam,None known,2023-07-23
P01425,Rachit Rao,M,2005-03-13,20,O+,+91-00000-64636,Alappuzha,Penicillin,2022-09-10
P01426,Samaksh Dixit,M,1974-11-11,50,O+,+91-00000-27512,Thiruvananthapuram,Sulfa drugs,2022-07-18
P01427,Nachiket Krish,M,1976-02-04,49,A-,+91-00000-21123,Pathanamthitta,None known,2022-02-27
P01428,Harshil Gokhale,M,1954-12-20,70,AB-,+91-00000-21042,Kollam,None known,2022-12-16
P01429,Agastya Dalal,M,1990-10-30,34,AB+,+91-00000-45539,Thiruvananthapuram,None known,2023-06-14
P01430,Chaman Bala,F,1985-09-09,39,O+,+91-00000-37028,Thiruvananthapuram,Penicillin,2023-09-09
P01431,Girish Lalla,M,1998-12-10,26,A-,+91-00000-15162,Pathanamthitta,None known,2021-08-10
P01432,Aishani Suresh,F,1955-07-21,70,A+,+91-00000-17351,Kanyakumari,None known,2023-10-04
P01433,Ayush Bala,M,1955-07-12,70,AB+,+91-00000-37234,Pathanamthitta,None known,2022-08-08
P01434,Mugdha Narayanan,F,1992-05-18,33,O-,+91-00000-89825,Kanyakumari,None known,2023-08-15
P01435,Jagvi Patil,F,1991-11-01,33,O+,+91-00000-88200,Kanyakumari,None known,2021-12-20
P01436,Oeshi Nazareth,F,2006-01-30,19,A+,+91-00000-37984,Kottayam,Penicillin,2023-12-06
P01437,Ikbal Som,M,2002-08-10,22,A+,+91-00000-93577,Kottayam,None known,2023-07-30
P01438,Naksh Bala,M,2010-12-20,14,A+,+91-00000-82910,Kottayam,None known,2023-07-15
P01439,Vaishnavi Manda,F,2022-06-27,3,AB-,+91-00000-96238,Pathanamthitta,NSAIDs,2022-07-26
P01440,Zayyan Parmer,M,1950-11-08,74,A-,+91-00000-35355,Alappuzha,None known,2022-02-12
P01442,Odika Doctor,F,2020-08-08,4,AB-,+91-00000-12403,Pathanamthitta,None known,2021-10-23
P01443,Onkar Sarraf,M,1942-07-03,83,AB+,+91-00000-87241,Kanyakumari,None known,2023-02-14
P01444,Upasna Gill,F,1972-11-06,52,B-,+91-00000-79938,Kollam,Sulfa drugs,2023-02-02
P01445,Gavin Garg,M,2011-10-26,13,AB+,+91-00000-12150,Kollam,None known,2022-09-17
P01446,Vritti Pant,F,2018-07-04,7,O+,+91-00000-94860,Thiruvananthapuram,None known,2021-09-10
P01447,Priya Kalita,F,1955-06-26,70,A-,+91-00000-26542,Pathanamthitta,None known,2023-02-22
P01448,Nathaniel Kara,M,1990-12-25,34,A+,+91-00000-49631,Kottayam,None known,2022-09-22
P01449,Wriddhish Patla,M,1947-06-25,78,A+,+91-00000-50543,Thiruvananthapuram,None known,2021-08-01
P01450,Bhanumati Karnik,F,1966-08-09,58,B-,+91-00000-40106,Kottayam,None known,2023-06-22
P01451,Xiti Batta,F,2006-03-03,19,AB-,+91-00000-22492,Thiruvananthapuram,None known,2021-11-21
P01452,Azad Bakshi,M,1995-09-14,29,O+,+91-00000-75451,Alappuzha,None known,2021-09-22
P01453,Champak Naik,M,1989-07-27,36,B+,+91-00000-65245,Pathanamthitta,None known,2022-05-19
P01454,Anya Pandit,F,2016-04-18,9,AB+,+91-00000-61427,Kollam,None known,2021-10-13
P01455,Yatan Walla,M,2004-07-02,21,AB+,+91-00000-84504,Thiruvananthapuram,NSAIDs,2023-10-19
P01456,Reyansh Bhatnagar,M,1971-11-19,53,O+,+91-00000-55171,Pathanamthitta,None known,2023-09-24
P01457,Charan Sahni,M,1992-12-17,32,A+,+91-00000-39354,Kollam,None known,2023-11-28
P01458,Aishani Goda,F,2001-12-13,23,O+,+91-00000-47005,Kanyakumari,None known,2022-06-19
P01459,Madhavi Bassi,F,1950-10-22,74,AB+,+91-00000-26809,Kottayam,None known,2023-09-08
P01460,Faraj Naidu,M,1987-12-15,37,A+,+91-00000-56191,Pathanamthitta,None known,2023-09-16
P01461,Avni Sibal,F,1978-08-08,46,AB-,+91-00000-10639,Kanyakumari,None known,2023-01-26
P01462,Mitali Kant,F,1949-06-02,76,AB-,+91-00000-38033,Kanyakumari,None known,2021-08-22
P01463,Advaith Parekh,M,2006-02-14,19,B+,+91-00000-99375,Kollam,None known,2022-04-17
P01464,Kritika Parsa,F,2010-10-20,14,O+,+91-00000-70806,Kollam,None known,2023-06-28
P01465,Aadhya Kothari,F,1985-07-13,40,O+,+91-00000-11781,Alappuzha,Sulfa drugs,2021-09-27
P01466,Madhav Mistry,M,1968-09-06,56,AB-,+91-00000-25397,Kottayam,None known,2021-08-26
P01467,Kalpit Aurora,M,1965-03-27,60,AB+,+91-00000-61439,Kottayam,None known,2023-05-24
P01469,Mohammed Saha,M,1990-11-02,34,B-,+91-00000-47966,Kottayam,Sulfa drugs,2022-11-21
P01470,Gabriel Luthra,M,2009-06-23,16,O+,+91-00000-78162,Kottayam,None known,2022-04-01
P01471,Harini Chowdhury,F,2007-03-01,18,B+,+91-00000-95242,Kottayam,None known,2023-10-27
P01472,Gautami Char,F,1982-09-14,42,AB-,+91-00000-59500,Thiruvananthapuram,None known,2021-08-05
P01473,Wahab Vala,M,1940-01-26,85,A-,+91-00000-58196,Kanyakumari,None known,2022-09-01
P01474,Ikshita Muni,F,2013-05-10,12,AB-,+91-00000-14617,Kanyakumari,None known,2021-11-25
P01475,Vamakshi Tella,F,1968-06-13,57,A+,+91-00000-37867,Pathanamthitta,None known,2021-10-30
P01476,Jason Sachdev,M,1986-01-17,39,AB-,+91-00000-21655,Thiruvananthapuram,None known,2021-12-14
P01477,Saumya Pathak,F,1952-09-27,72,B+,+91-00000-78925,Kollam,None known,2022-10-22
P01478,Zayyan Lanka,M,1983-01-28,42,A-,+91-00000-31665,Alappuzha,None known,2022-03-28
P01479,Vinaya Sawhney,F,1937-12-01,87,A-,+91-00000-16652,Thiruvananthapuram,None known,2021-12-15
P01480,Zarna Walia,F,2009-09-01,15,AB+,+91-00000-56141,Pathanamthitta,None known,2023-06-01
P01481,Jasmit Mane,F,1942-02-01,83,AB-,+91-00000-70578,Kottayam,None known,2021-08-08
P01482,Advay Minhas,M,1991-12-05,33,A-,+91-00000-17826,Kottayam,None known,2023-02-24
P01483,Nidhi Ramanathan,F,1983-08-23,41,O+,+91-00000-99287,Pathanamthitta,None known,2023-10-24
P01484,Amol Baral,M,1978-07-21,47,A-,+91-00000-88718,Kottayam,Sulfa drugs,2022-06-10
P01485,Vedant Mangal,M,1990-03-16,35,O-,+91-00000-29640,Pathanamthitta,None known,2021-12-30
P01486,Girish Pillai,M,2014-12-22,10,B-,+91-00000-83368,Thiruvananthapuram,None known,2023-05-26
P01487,Vedhika Prabhu,F,1962-07-09,63,AB+,+91-00000-29197,Alappuzha,None known,2022-05-01
P01488,Utkarsh Chana,M,1949-04-25,76,B+,+91-00000-47255,Kollam,None known,2021-09-14
P01489,Rushil Thaker,M,1936-10-21,88,AB+,+91-00000-67651,Kottayam,None known,2022-06-13
P01490,Ishaan Hayer,M,1996-09-21,28,A-,+91-00000-46605,Pathanamthitta,None known,2021-10-15
P01491,Baljiwan Choudhary,M,1986-09-05,38,O+,+91-00000-36154,Kottayam,None known,2022-12-01
P01492,Jatin Warrior,M,2022-04-04,3,A-,+91-00000-50224,Thiruvananthapuram,NSAIDs,2022-08-16
P01493,Oviya Sandhu,F,1944-07-05,81,B-,+91-00000-36393,Kollam,None known,2022-02-28
P01494,Yasti Mukherjee,F,1993-04-30,32,O-,+91-00000-18439,Alappuzha,None known,2021-11-09
P01495,Anirudh Mann,M,2006-01-27,19,AB-,+91-00000-98161,Kollam,NSAIDs,2022-03-18
P01496,Yauvani Parikh,F,2010-07-08,15,A+,+91-00000-71761,Kollam,None known,2022-08-07
P01497,Bishakha Wali,F,2000-07-20,25,O-,+91-00000-65320,Alappuzha,None known,2023-11-02
P01498,Daksh Arya,M,1962-02-17,63,A+,+91-00000-31826,Kottayam,Sulfa drugs,2022-10-04
P01499,Falak Ramachandran,F,2004-10-06,20,B+,+91-00000-69728,Kanyakumari,None known,2023-04-08
P01501,Urishilla Bhalla,F,1972-05-06,53,B+,+91-00000-15626,Kottayam,None known,2021-08-13
P01502,Gabriel Biswas,M,1999-03-21,26,B-,+91-00000-45850,Kottayam,Penicillin,2023-04-10
P01503,Vedika Kibe,F,1950-12-03,74,A-,+91-00000-78298,Pathanamthitta,None known,2022-11-17
P01504,Zaid Kalita,M,1995-12-24,29,AB+,+91-00000-71389,Thiruvananthapuram,None known,2021-08-16
P01505,Udant Nayar,M,1995-01-05,30,AB+,+91-00000-53967,Pathanamthitta,None known,2022-10-08
P01506,Adya Arora,F,2019-04-12,6,B+,+91-00000-68612,Alappuzha,None known,2022-01-20
P01507,Imaran Kala,M,1974-05-29,51,AB-,+91-00000-99122,Kanyakumari,Penicillin,2022-06-16
P01508,Balhaar Kibe,M,2018-07-06,7,B+,+91-00000-36904,Alappuzha,None known,2023-10-26
P01509,Nachiket Nath,M,1982-01-06,43,O-,+91-00000-85822,Kottayam,None known,2021-09-02
P01510,Hema Virk,F,2022-06-03,3,AB-,+91-00000-23015,Alappuzha,None known,2022-01-02
P01511,Daksha Gour,F,1992-07-29,32,AB-,+91-00000-23720,Kottayam,None known,2022-07-01
P01512,Karan Guha,M,2013-04-19,12,B+,+91-00000-80757,Pathanamthitta,None known,2023-05-02
P01513,Isaac Gandhi,M,1985-04-21,40,A+,+91-00000-20472,Pathanamthitta,None known,2023-12-05
P01514,Ayush Padmanabhan,M,1968-04-22,57,O+,+91-00000-29655,Thiruvananthapuram,None known,2022-09-01
P01515,Anay Dey,M,2021-11-28,3,AB-,+91-00000-86566,Kottayam,None known,2023-12-23
P01516,Harrison Balan,M,1980-06-27,45,A-,+91-00000-92442,Kottayam,None known,2023-01-25
P01517,Gautami Solanki,F,1949-10-08,75,O-,+91-00000-41936,Alappuzha,None known,2023-02-17
P01518,Naveen Lad,M,1993-07-01,32,O-,+91-00000-98699,Kanyakumari,None known,2022-03-16
P01519,Hiral Nagarajan,F,1949-08-21,75,O+,+91-00000-48531,Alappuzha,None known,2023-07-11
P01520,Dakshesh Ahuja,M,2019-07-01,6,O+,+91-00000-88700,Pathanamthitta,None known,2023-07-13
P01522,Rehaan Krishnan,M,2022-01-08,3,AB-,+91-00000-21201,Kanyakumari,NSAIDs,2022-08-29
P01523,Rishi Goyal,M,1994-07-31,30,A+,+91-00000-86661,Pathanamthitta,Sulfa drugs,2023-12-02
P01524,Sarthak Talwar,M,1955-09-10,69,A-,+91-00000-19939,Thiruvananthapuram,None known,2021-08-20
P01526,Maya Madan,F,1966-10-12,58,O+,+91-00000-72390,Kollam,None known,2021-09-01
P01527,Irya Butala,F,1975-01-25,50,B+,+91-00000-91222,Alappuzha,None known,2023-02-25
P01528,Bachittar Krishnamurthy,M,1985-03-02,40,AB+,+91-00000-58283,Kollam,None known,2023-06-14
P01529,Girik Khalsa,M,2001-05-11,24,A+,+91-00000-82729,Pathanamthitta,None known,2023-02-24
P01530,Rayaan Mann,M,1967-03-27,58,O+,+91-00000-67541,Kanyakumari,None known,2021-09-10
P01531,Darpan Rajagopal,M,1940-07-13,85,O+,+91-00000-96441,Kanyakumari,None known,2023-07-30
P01532,Nathaniel Tak,M,1976-10-07,48,O+,+91-00000-45687,Pathanamthitta,None known,2021-10-13
P01534,Samesh Swamy,M,1972-09-22,52,A+,+91-00000-53974,Thiruvananthapuram,None known,2023-07-27
P01535,Sanaya Dara,F,2013-09-01,11,A+,+91-00000-73728,Kollam,None known,2022-03-30
P01536,Jonathan Bava,M,1998-12-03,26,B+,+91-00000-35302,Thiruvananthapuram,None known,2021-09-19
P01537,Dalbir Bala,M,1941-10-10,83,A+,+91-00000-80382,Alappuzha,None known,2022-11-20
P01538,Pranit Prabhu,M,1941-09-05,83,B-,+91-00000-45620,Pathanamthitta,None known,2022-09-26
P01539,Nitesh Ramachandran,M,1966-05-29,59,A-,+91-00000-83275,Kanyakumari,None known,2021-12-08
P01540,Falak Gole,F,1992-08-14,32,A+,+91-00000-96339,Thiruvananthapuram,None known,2023-07-31
P01541,Harsh Tella,M,1985-01-01,40,AB-,+91-00000-48753,Kottayam,None known,2022-08-04
P01542,Abdul Tata,M,1967-04-22,58,O-,+91-00000-30900,Kanyakumari,NSAIDs,2022-08-06
P01543,Jagdish Sen,M,2003-10-11,21,B+,+91-00000-24039,Kanyakumari,None known,2022-07-18
P01546,Anay De,M,1983-04-18,42,AB-,+91-00000-62305,Kollam,None known,2022-03-23
P01547,Ikshita Rajagopal,F,1961-11-13,63,AB+,+91-00000-85882,Pathanamthitta,None known,2021-08-23
P01548,Vivaan Kar,M,1983-12-14,41,B-,+91-00000-58155,Kanyakumari,None known,2022-04-13
P01549,Tejas Prashad,M,2021-10-11,3,B+,+91-00000-33292,Pathanamthitta,None known,2021-09-01
P01550,Gautami Patla,F,2001-12-18,23,O+,+91-00000-59134,Kottayam,None known,2022-09-11
P01551,Atharv Panchal,M,1982-05-29,43,AB+,+91-00000-26668,Kanyakumari,None known,2022-07-25
P01552,Bhavna Divan,F,2012-03-27,13,O-,+91-00000-84709,Kollam,None known,2024-01-04
P01553,Lakshit Gaba,M,1950-03-10,75,AB-,+91-00000-54874,Pathanamthitta,None known,2021-10-16
P01555,Jai Raj,M,1999-10-18,25,A+,+91-00000-98719,Alappuzha,None known,2023-06-08
P01557,Arin Dewan,M,1982-11-01,42,O+,+91-00000-98826,Kanyakumari,None known,2022-11-04
P01558,Onveer Barad,M,2018-03-21,7,B+,+91-00000-63558,Kanyakumari,None known,2023-06-04
P01559,Dayita Karpe,F,2022-07-24,2,O+,+91-00000-56349,Kollam,None known,2023-01-21
P01560,Mekhala Gole,F,2002-04-11,23,AB+,+91-00000-40215,Kollam,None known,2023-02-11
P01561,Ikshita Seshadri,F,1993-03-12,32,O-,+91-00000-80214,Thiruvananthapuram,None known,2022-04-07
P01562,Dayita Sarkar,F,2001-06-12,24,O+,+91-00000-42787,Kanyakumari,None known,2022-01-14
P01563,Harish Borah,M,1977-01-27,48,AB+,+91-00000-58568,Thiruvananthapuram,None known,2022-06-23
P01564,Frado Bobal,M,1999-04-16,26,AB+,+91-00000-40960,Kottayam,None known,2023-07-30
P01565,Hamsini Wason,F,2000-08-08,24,B+,+91-00000-92133,Alappuzha,None known,2021-08-23
P01566,Raghav Rout,M,1971-05-20,54,B+,+91-00000-24776,Kanyakumari,None known,2023-11-28
P01567,Falguni Radhakrishnan,F,1941-12-28,83,O-,+91-00000-87461,Kanyakumari,None known,2023-11-30
P01568,Chanakya Rama,M,1953-10-20,71,O-,+91-00000-65274,Alappuzha,None known,2023-10-20
P01569,Aarnav Som,M,1967-09-06,57,O-,+91-00000-40448,Kottayam,None known,2021-12-04
P01570,Mitesh Baral,M,2025-04-27,0,A-,+91-00000-52255,Pathanamthitta,None known,2023-08-15
P01571,Akshay Hari,M,2001-01-23,24,O-,+91-00000-66076,Kollam,None known,2023-07-06
P01572,Oliver Andra,M,1986-01-21,39,B+,+91-00000-36580,Kottayam,None known,2022-06-12
P01573,Siddharth Ramanathan,M,1969-12-19,55,A+,+91-00000-49444,Pathanamthitta,Sulfa drugs,2022-01-13
P01574,Maanav Mangal,M,2003-10-15,21,B+,+91-00000-30134,Kottayam,None known,2023-04-18
P01576,Sanaya Pradhan,F,1967-05-09,58,O-,+91-00000-31176,Pathanamthitta,None known,2022-10-10
P01577,Darika Baria,F,2000-11-17,24,B-,+91-00000-69407,Alappuzha,None known,2022-08-30
P01578,Libni Mane,F,1947-05-21,78,A+,+91-00000-56100,Kottayam,NSAIDs,2024-01-15
P01579,Neha Master,F,1979-02-26,46,A+,+91-00000-35006,Thiruvananthapuram,None known,2021-12-07
P01580,Jason Chaudhary,M,1981-04-18,44,AB+,+91-00000-14716,Kanyakumari,NSAIDs,2022-09-30
P01581,Idika Ramaswamy,F,1995-09-27,29,A+,+91-00000-80542,Kollam,None known,2021-09-12
P01582,Onkar Krishnamurthy,M,2022-07-29,2,AB+,+91-00000-83240,Kanyakumari,Penicillin,2022-10-18
P01584,Triya Pathak,F,2005-06-17,20,AB+,+91-00000-15141,Kollam,None known,2022-07-19
P01585,Maya Kaur,F,1984-02-09,41,B+,+91-00000-68896,Kanyakumari,None known,2023-02-10
P01586,Warhi Madan,F,1939-12-27,85,B-,+91-00000-90865,Alappuzha,None known,2023-04-29
P01587,Eshana Lad,F,1972-02-26,53,B-,+91-00000-70632,Kottayam,None known,2022-08-23
P01588,Saksham Taneja,M,1972-10-26,52,A+,+91-00000-69513,Thiruvananthapuram,None known,2021-09-02
P01589,Chakradev Deep,M,1939-06-15,86,O+,+91-00000-48800,Pathanamthitta,None known,2023-03-15
P01590,Azaan Saraf,M,1976-04-25,49,B-,+91-00000-19214,Thiruvananthapuram,None known,2023-11-13
P01591,Meera Joshi,F,2015-10-23,9,AB+,+91-00000-97675,Thiruvananthapuram,None known,2023-10-20
P01592,Neel Ramachandran,M,2005-06-11,20,AB+,+91-00000-80876,Kanyakumari,None known,2021-11-02
P01593,Inaya Loyal,F,1976-09-21,48,B+,+91-00000-61973,Pathanamthitta,None known,2022-03-07
P01594,Vanya Balan,F,1966-12-22,58,B+,+91-00000-62375,Kottayam,NSAIDs,2021-10-14
P01595,Lekha Grover,F,1987-01-14,38,O-,+91-00000-57782,Kottayam,Penicillin,2021-09-28
P01596,Qadim Toor,M,2021-02-06,4,O+,+91-00000-82439,Pathanamthitta,None known,2022-03-17
P01597,Girish Lall,M,1971-06-22,54,O-,+91-00000-22308,Alappuzha,NSAIDs,2023-02-16
P01598,Hardik Rai,M,2006-01-13,19,A+,+91-00000-48505,Kottayam,None known,2021-09-18
P01599,Pallavi Agarwal,F,1944-09-19,80,AB-,+91-00000-93227,Kollam,None known,2023-08-16
P01600,Deepa Agarwal,F,1982-12-25,42,B-,+91-00000-53018,Pathanamthitta,None known,2023-11-17
P01601,Aadhya Narasimhan,F,1985-06-14,40,AB-,+91-00000-37825,Alappuzha,NSAIDs,2022-09-11
P01602,Mahika Singh,F,1983-08-28,41,B+,+91-00000-45585,Pathanamthitta,Sulfa drugs,2022-05-23
P01603,Yashica Bala,F,1946-01-14,79,A+,+91-00000-64158,Kollam,None known,2022-07-29
P01604,Bachittar Sankar,M,2014-07-11,11,AB+,+91-00000-27000,Pathanamthitta,None known,2021-12-16
P01605,Jackson Subramaniam,M,1970-01-24,55,O+,+91-00000-40304,Kottayam,None known,2021-10-02
P01606,Hemal Sheth,F,1995-08-16,29,A-,+91-00000-60546,Thiruvananthapuram,None known,2023-06-09
P01607,Vritti Sama,F,1978-09-11,46,B+,+91-00000-49565,Kottayam,None known,2023-01-21
P01608,Lipika Nadkarni,F,2012-05-08,13,AB+,+91-00000-84202,Alappuzha,None known,2023-07-10
P01609,Rushil Khurana,M,1969-07-04,56,O-,+91-00000-86926,Thiruvananthapuram,NSAIDs,2023-03-23
P01610,Naksh Sheth,M,1967-05-12,58,A+,+91-00000-30451,Pathanamthitta,None known,2023-11-19
P01611,Faqid Jain,M,2014-07-11,11,A-,+91-00000-92833,Alappuzha,None known,2022-10-07
P01612,Dev Edwin,M,1962-12-01,62,A-,+91-00000-45297,Kanyakumari,None known,2022-07-13
P01613,Andrew Sama,M,1979-03-05,46,B-,+91-00000-12752,Thiruvananthapuram,None known,2023-02-10
P01614,Samuel Goswami,M,1997-01-01,28,A-,+91-00000-93919,Pathanamthitta,None known,2022-12-22
P01615,Indali Parmer,F,2006-05-09,19,O+,+91-00000-80430,Pathanamthitta,None known,2023-08-09
P01616,Barkha Pingle,F,1957-03-19,68,AB+,+91-00000-56685,Kottayam,None known,2021-10-20
P01618,Ekaraj Sharaf,M,1957-06-26,68,AB+,+91-00000-49938,Kollam,None known,2021-08-26
P01619,Kabir Kumer,M,1993-06-07,32,O-,+91-00000-37062,Kanyakumari,None known,2022-08-29
P01620,Vasatika Pradhan,F,1983-09-26,41,O-,+91-00000-83790,Thiruvananthapuram,None known,2022-02-05
P01621,Dayita Bhandari,F,1990-08-10,34,B+,+91-00000-12573,Alappuzha,None known,2022-07-23
P01622,Agastya Soni,M,1957-04-06,68,O-,+91-00000-27798,Kollam,None known,2022-02-16
P01623,Ishwar Chaudhuri,M,1991-03-14,34,AB+,+91-00000-38232,Kottayam,None known,2021-09-05
P01624,Alexander Edwin,M,1962-08-23,62,B-,+91-00000-81470,Alappuzha,None known,2022-05-07
P01625,Bhavika Dyal,F,2018-06-05,7,B-,+91-00000-44037,Thiruvananthapuram,None known,2021-10-29
P01626,Zinal Pall,F,2005-05-24,20,O+,+91-00000-31095,Kottayam,None known,2023-11-06
P01628,Orinder Dara,M,1981-08-13,43,AB-,+91-00000-75629,Kottayam,None known,2022-12-22
P01629,Quincy Prabhu,M,1968-12-13,56,A+,+91-00000-78611,Pathanamthitta,None known,2023-03-08
P01630,Unni Khosla,F,1943-05-27,82,B+,+91-00000-98840,Alappuzha,None known,2022-10-06
P01631,Avi Zacharia,M,1982-09-29,42,B+,+91-00000-55795,Kanyakumari,Sulfa drugs,2023-09-15
P01632,Omisha Mangat,F,1984-04-26,41,AB-,+91-00000-12946,Thiruvananthapuram,Penicillin,2023-05-09
P01633,Vamakshi Mangal,F,2022-07-19,3,B-,+91-00000-24973,Kollam,None known,2022-01-24
P01634,Simon Sidhu,M,1938-09-16,86,AB+,+91-00000-27176,Kollam,Penicillin,2022-05-28
P01635,Jagvi Apte,F,1997-01-07,28,B+,+91-00000-23329,Alappuzha,None known,2022-10-31
P01637,Karan Subramaniam,M,1962-07-12,63,AB+,+91-00000-81874,Alappuzha,None known,2023-12-13
P01638,Farhan Uppal,M,2010-11-26,14,B-,+91-00000-82337,Kanyakumari,None known,2023-04-08
P01640,Dominic Parsa,M,1995-12-24,29,A-,+91-00000-53006,Alappuzha,None known,2022-11-08
P01641,Rajeshri Chatterjee,F,2004-02-07,21,B+,+91-00000-39631,Alappuzha,Penicillin,2021-10-17
P01642,Mohini Borah,F,2001-03-21,24,B+,+91-00000-64087,Kollam,None known,2022-03-31
P01643,Vedant Tiwari,M,1936-03-08,89,AB-,+91-00000-70590,Pathanamthitta,None known,2024-01-09
P01644,Ucchal Mammen,F,2003-02-19,22,AB+,+91-00000-43797,Kanyakumari,None known,2023-01-11
P01645,Ronith Sule,M,2014-05-03,11,B+,+91-00000-77087,Alappuzha,None known,2023-05-17
P01646,Sneha Srinivasan,F,1947-08-03,78,O+,+91-00000-97593,Alappuzha,None known,2021-10-06
P01647,Rachana Buch,F,1984-06-08,41,B-,+91-00000-13003,Kottayam,Penicillin,2022-06-29
P01649,Ryan Walla,M,1998-11-14,26,AB+,+91-00000-79166,Pathanamthitta,None known,2023-01-31
P01650,Chaaya Dora,F,1992-11-29,32,B-,+91-00000-55484,Kanyakumari,None known,2023-02-21
P01651,Tristan Dixit,M,2021-04-19,4,A+,+91-00000-87727,Kollam,Penicillin,2022-10-16
P01652,Udyati Chaudhari,F,1985-09-01,39,AB+,+91-00000-97097,Alappuzha,None known,2022-12-22
P01653,Ishwar Divan,M,1958-03-09,67,B-,+91-00000-28290,Thiruvananthapuram,None known,2021-10-01
P01655,Nimrat Pillai,F,2016-01-03,9,B+,+91-00000-47024,Kanyakumari,None known,2021-10-07
P01656,Sanaya Kala,F,1995-05-09,30,O-,+91-00000-57362,Kollam,None known,2023-12-24
P01658,Frado Subramanian,M,1967-01-01,58,A+,+91-00000-19005,Pathanamthitta,Sulfa drugs,2021-09-30
P01659,Ekavir Deo,M,2006-03-11,19,B-,+91-00000-23167,Thiruvananthapuram,None known,2021-09-22
P01660,Finn Deshpande,M,1973-03-16,52,AB+,+91-00000-40598,Kottayam,None known,2023-03-11
P01661,Deepa Bhatt,F,1947-03-29,78,AB-,+91-00000-52956,Kottayam,None known,2021-09-16
P01662,Faras Kala,M,2023-03-19,2,AB-,+91-00000-67840,Kottayam,None known,2022-07-01
P01664,Gavin Behl,M,1972-03-07,53,A+,+91-00000-74866,Kottayam,Sulfa drugs,2021-12-19
P01665,Lohit Bava,M,2023-03-11,2,A+,+91-00000-22575,Pathanamthitta,None known,2022-04-29
P01667,Unnati Borde,F,1951-06-19,74,AB-,+91-00000-31785,Kanyakumari,Sulfa drugs,2023-03-27
P01668,Darika Barad,F,1993-07-19,32,O+,+91-00000-67284,Kanyakumari,None known,2023-12-04
P01670,Suhani Jhaveri,F,1974-08-03,50,AB-,+91-00000-50968,Pathanamthitta,Penicillin,2022-06-04
P01671,Aradhana Gokhale,F,1962-08-22,62,AB+,+91-00000-92255,Pathanamthitta,None known,2023-10-14
P01672,Vrinda Talwar,F,1969-02-10,56,AB+,+91-00000-74670,Pathanamthitta,None known,2023-03-29
P01673,Nidhi Mohanty,F,1959-11-28,65,A-,+91-00000-83342,Pathanamthitta,None known,2022-03-24
P01674,Turvi Joshi,F,1937-05-08,88,O-,+91-00000-50241,Kollam,None known,2023-08-26
P01676,Farhan Shankar,M,1992-03-30,33,O-,+91-00000-51878,Kanyakumari,Penicillin,2023-05-30
P01677,Hemangini Nagi,F,2012-07-25,12,AB+,+91-00000-57064,Pathanamthitta,None known,2022-05-30
P01678,Bhanumati Saha,F,1962-06-11,63,A-,+91-00000-71111,Kollam,None known,2024-01-12
P01679,Anmol Thaman,M,1998-04-26,27,A+,+91-00000-74837,Pathanamthitta,None known,2023-09-20
P01680,Kashvi Dey,F,1986-12-15,38,O-,+91-00000-69597,Pathanamthitta,None known,2022-03-13
P01681,Lucky Kothari,M,1993-10-04,31,B+,+91-00000-56078,Kollam,None known,2023-12-21
P01682,Harinakshi Varughese,F,1961-10-22,63,AB-,+91-00000-99024,Thiruvananthapuram,None known,2021-11-26
P01683,Nathan Ganguly,M,2020-07-20,4,O-,+91-00000-18234,Alappuzha,None known,2023-02-15
P01684,Lekha Kibe,F,1976-06-25,49,A+,+91-00000-26272,Kottayam,NSAIDs,2024-01-05
P01686,Isaac Sheth,M,1953-01-12,72,A-,+91-00000-52948,Thiruvananthapuram,None known,2023-09-05
P01687,Bhavika Dani,F,1960-02-08,65,O+,+91-00000-74817,Kollam,None known,2022-03-29
P01688,Yashoda Chandran,F,2017-11-13,7,A-,+91-00000-98943,Kanyakumari,None known,2023-11-14
P01689,Kala Gara,F,1999-03-29,26,AB-,+91-00000-54677,Kollam,None known,2022-05-29
P01690,Keya Sama,F,1996-05-10,29,B+,+91-00000-61581,Thiruvananthapuram,Penicillin,2023-07-31
P01692,Rajata Issac,F,1977-05-22,48,A-,+91-00000-30297,Kanyakumari,None known,2023-10-06
P01693,Raksha Bose,F,1999-03-27,26,A-,+91-00000-69972,Kollam,NSAIDs,2023-12-24
P01695,Krishna Dave,F,1987-03-15,38,A+,+91-00000-51946,Pathanamthitta,None known,2023-04-30
P01697,Tarak Ray,M,1986-05-17,39,AB+,+91-00000-11828,Kollam,None known,2023-12-26
P01698,Jagat Prasad,M,1935-05-03,90,A-,+91-00000-80107,Kottayam,NSAIDs,2021-09-22
P01699,Tripti Pau,F,1993-04-05,32,AB+,+91-00000-79873,Thiruvananthapuram,None known,2021-12-29
P01700,Diya Krishna,F,1995-05-04,30,B-,+91-00000-20624,Alappuzha,None known,2022-04-02
P01701,Qushi Shroff,F,1937-01-26,88,O+,+91-00000-81717,Kanyakumari,None known,2022-02-05
P01702,Qushi Loyal,F,2021-10-01,3,AB-,+91-00000-55732,Kanyakumari,None known,2022-06-14
P01703,Faraj Mani,M,1996-05-06,29,O-,+91-00000-81811,Alappuzha,None known,2021-09-03
P01706,Nakul Chaudhuri,M,1947-12-13,77,B-,+91-00000-19485,Pathanamthitta,None known,2023-07-04
P01707,Gabriel Mittal,M,1938-11-17,86,A+,+91-00000-83680,Pathanamthitta,None known,2022-11-07
P01708,Ranbir Dada,M,1960-03-13,65,A+,+91-00000-37532,Pathanamthitta,None known,2021-11-19
P01709,Ekavir Wali,M,1994-05-15,31,O-,+91-00000-81952,Thiruvananthapuram,None known,2021-11-29
P01711,Joshua Suri,M,1976-06-12,49,O+,+91-00000-69572,Kanyakumari,None known,2022-04-05
P01712,Jeevika Chandra,F,2021-01-18,4,O+,+91-00000-99101,Thiruvananthapuram,None known,2022-04-29
P01713,Bhavna Pandit,F,2001-10-24,23,AB-,+91-00000-48534,Kanyakumari,None known,2023-08-14
P01714,Warjas Jaggi,M,1974-01-17,51,A+,+91-00000-82151,Kottayam,None known,2022-05-02
P01715,Mohini Samra,F,2023-04-27,2,AB-,+91-00000-16646,Kanyakumari,NSAIDs,2022-06-15
P01716,Liam Mody,M,1953-05-11,72,A+,+91-00000-15288,Alappuzha,None known,2022-08-12
P01717,Wriddhish Balan,M,1976-06-18,49,B+,+91-00000-92463,Alappuzha,None known,2021-10-31
P01718,Jagrati Nanda,F,1955-01-11,70,A-,+91-00000-35033,Alappuzha,None known,2021-12-19
P01720,Abeer Dar,M,2015-06-26,10,B-,+91-00000-86789,Kottayam,NSAIDs,2023-01-17
P01721,Ubika Brahmbhatt,F,1964-12-12,60,A+,+91-00000-91815,Thiruvananthapuram,None known,2022-04-19
P01723,Jai Setty,M,2005-12-23,19,A-,+91-00000-48646,Kollam,None known,2021-10-17
P01725,Nathaniel Nagar,M,1958-06-20,67,O-,+91-00000-93676,Thiruvananthapuram,None known,2021-11-29
P01726,Anika Varty,F,2006-01-28,19,B-,+91-00000-39852,Kottayam,NSAIDs,2023-07-17
P01727,Shivansh Sarma,M,1975-08-07,49,A-,+91-00000-36279,Kottayam,Sulfa drugs,2023-05-20
P01728,Peter Kuruvilla,M,1981-07-17,44,AB+,+91-00000-56741,Pathanamthitta,None known,2022-11-25
P01729,Ekani Parsa,F,2000-08-24,24,A+,+91-00000-22346,Kottayam,None known,2023-10-27
P01730,Diya Dass,F,2023-07-05,2,B+,+91-00000-70513,Kanyakumari,None known,2023-11-10
P01731,Panini Chana,F,2003-12-25,21,B+,+91-00000-25050,Alappuzha,None known,2022-01-31
P01732,Gaurang Chatterjee,M,2017-12-15,7,B+,+91-00000-46940,Kanyakumari,None known,2023-10-22
P01735,Farhan Mistry,M,1969-02-21,56,B+,+91-00000-50841,Alappuzha,None known,2022-01-17
P01736,Nitara Minhas,F,1983-08-31,41,O-,+91-00000-37205,Kollam,None known,2021-08-02
P01737,Nandini Brar,F,1990-03-31,35,A+,+91-00000-19638,Kollam,Sulfa drugs,2022-12-06
P01738,Vasana Banik,F,2015-11-08,9,A-,+91-00000-98783,Pathanamthitta,None known,2023-10-01
P01739,Vritti Deo,F,1988-02-20,37,O-,+91-00000-32227,Kottayam,None known,2022-08-11
P01740,Nirja Dar,F,1984-11-05,40,AB+,+91-00000-47585,Pathanamthitta,None known,2023-02-09
P01741,Farhan Venkataraman,M,1992-08-08,32,A-,+91-00000-54132,Thiruvananthapuram,None known,2023-10-21
P01742,Zilmil Sachdev,F,2013-10-03,11,B-,+91-00000-46822,Pathanamthitta,NSAIDs,2021-11-10
P01743,Tristan Chanda,M,1997-10-01,27,A+,+91-00000-81415,Kottayam,None known,2023-09-12
P01744,Eta Batta,F,1987-05-21,38,O+,+91-00000-32016,Kollam,None known,2023-04-26
P01746,Dakshesh Sarna,M,1982-07-03,43,B+,+91-00000-93206,Kottayam,NSAIDs,2022-06-24
P01747,Ekaraj Shroff,M,2017-07-01,8,A+,+91-00000-45675,Thiruvananthapuram,None known,2023-04-25
P01748,Frado Mammen,M,2004-02-22,21,AB-,+91-00000-10583,Alappuzha,None known,2023-10-20
P01750,Oviya Sahota,F,2017-07-02,8,AB+,+91-00000-57939,Kottayam,None known,2023-07-04
P01752,Saanvi Chander,F,1967-11-27,57,B-,+91-00000-80781,Kollam,None known,2022-07-28
P01753,Hitesh Boase,M,1977-02-11,48,B-,+91-00000-80776,Kottayam,None known,2023-11-22
P01754,Owen Loke,M,1977-04-07,48,A+,+91-00000-18287,Thiruvananthapuram,None known,2023-06-01
P01756,Omya Verma,F,1968-03-07,57,A+,+91-00000-86369,Kottayam,None known,2022-10-19
P01757,Harsh Sangha,M,1996-12-22,28,B-,+91-00000-54161,Pathanamthitta,Penicillin,2021-12-27
P01758,Vihaan Barman,M,1952-02-02,73,A+,+91-00000-80887,Kottayam,Sulfa drugs,2022-10-10
P01760,Vidhi Chhabra,F,1942-09-19,82,O+,+91-00000-63752,Kollam,None known,2022-03-11
P01761,Ekantika Hora,F,1960-02-20,65,A-,+91-00000-53573,Pathanamthitta,Sulfa drugs,2023-08-26
P01762,Yash Aggarwal,M,1945-02-25,80,AB-,+91-00000-23154,Thiruvananthapuram,None known,2023-03-29
P01763,Jalsa Raghavan,F,1976-06-28,49,A+,+91-00000-15614,Pathanamthitta,None known,2022-06-10
P01764,Fariq Soni,M,1976-02-26,49,O-,+91-00000-98345,Alappuzha,Penicillin,2022-05-05
P01765,Urvi Gokhale,F,1943-08-28,81,AB+,+91-00000-90619,Thiruvananthapuram,None known,2021-12-13
P01766,Yug Joshi,M,1978-07-13,47,A+,+91-00000-25785,Pathanamthitta,NSAIDs,2022-10-12
P01768,Gayathri Sane,F,1992-10-23,32,AB-,+91-00000-62561,Thiruvananthapuram,None known,2022-04-11
P01769,Jack Chand,M,1988-06-17,37,AB+,+91-00000-59665,Kanyakumari,None known,2022-12-24
P01770,Aarnav Som,M,1967-09-27,57,A+,+91-00000-28299,Kottayam,Sulfa drugs,2021-09-17
P01771,Eesha Pandit,F,2002-03-02,23,A-,+91-00000-40696,Alappuzha,None known,2023-06-14
P01772,Chakradev Khosla,M,1973-03-11,52,A+,+91-00000-85604,Pathanamthitta,None known,2022-01-12
P01774,Priya Sarkar,F,2008-02-03,17,A-,+91-00000-35325,Kottayam,None known,2022-02-11
P01778,Nihal Dhillon,M,1941-09-07,83,B+,+91-00000-45881,Kanyakumari,None known,2022-03-16
P01779,Faraj Bath,M,1947-07-11,78,B+,+91-00000-56275,Thiruvananthapuram,None known,2022-01-16
P01780,Rishi Parmer,M,2023-12-16,1,A+,+91-00000-28295,Thiruvananthapuram,NSAIDs,2022-04-10
P01782,Unnati Kapur,F,1934-11-05,90,O+,+91-00000-18044,Pathanamthitta,None known,2022-08-11
P01783,Pushti Balan,F,1968-05-16,57,B-,+91-00000-65340,Thiruvananthapuram,None known,2022-05-12
P01786,Deepa Mukhopadhyay,F,2000-05-14,25,AB-,+91-00000-90005,Kanyakumari,NSAIDs,2022-09-12
P01787,Ekantika Bhargava,F,1990-08-22,34,A+,+91-00000-41404,Kollam,None known,2022-01-03
P01788,Sai Nayar,F,1940-08-09,84,O+,+91-00000-32280,Pathanamthitta,None known,2021-12-21
P01789,Hema Gour,F,1981-10-19,43,O+,+91-00000-85205,Pathanamthitta,None known,2023-02-11
P01790,Damini Om,F,2008-01-01,17,AB-,+91-00000-83762,Kanyakumari,None known,2023-09-27
P01791,Abhimanyu Sawhney,M,1995-03-24,30,O-,+91-00000-97036,Kottayam,None known,2023-01-15
P01792,Kala Grewal,F,2004-11-21,20,AB+,+91-00000-56599,Pathanamthitta,None known,2021-12-13
P01793,Chakrika Iyengar,F,1983-03-02,42,AB+,+91-00000-33903,Thiruvananthapuram,None known,2022-05-02
P01794,Girindra Radhakrishnan,M,1942-10-26,82,B+,+91-00000-88470,Thiruvananthapuram,None known,2021-10-27
P01795,Nakul Singhal,M,1955-09-18,69,AB-,+91-00000-18245,Pathanamthitta,None known,2023-06-21
P01796,Chakradev Mitter,M,1991-10-21,33,A-,+91-00000-53902,Kottayam,None known,2022-09-08
P01797,Anya Seth,F,1986-05-06,39,AB-,+91-00000-44409,Kollam,None known,2022-06-28
P01798,Yash Pant,M,1975-02-09,50,O-,+91-00000-63085,Kanyakumari,Penicillin,2022-08-05
P01799,Chaitanya Sodhi,M,1951-05-16,74,A-,+91-00000-53053,Kollam,None known,2023-09-08
P01800,Chandresh Lala,M,1976-06-18,49,AB+,+91-00000-87460,Kottayam,Sulfa drugs,2022-02-12
P01801,Bhavika Misra,F,2008-11-08,16,O-,+91-00000-70061,Pathanamthitta,None known,2022-03-20
P01802,Pavani Wali,F,1945-07-03,80,B-,+91-00000-31879,Kollam,None known,2023-07-04
P01803,Charvi Garg,F,1973-07-07,52,A-,+91-00000-96224,Kanyakumari,None known,2023-04-15
P01804,Omya Iyer,F,1978-07-08,47,AB+,+91-00000-76247,Kanyakumari,Penicillin,2023-08-12
P01805,Jasmit Dara,F,1974-06-14,51,B-,+91-00000-40551,Pathanamthitta,Sulfa drugs,2022-12-18
P01806,Veer Mittal,M,2021-11-29,3,A-,+91-00000-15279,Thiruvananthapuram,None known,2023-04-14
P01807,Vaishnavi Borra,F,1980-11-20,44,A-,+91-00000-40596,Alappuzha,None known,2023-12-07
P01808,Odika Jani,F,1934-09-26,90,AB+,+91-00000-23971,Pathanamthitta,Sulfa drugs,2023-11-29
P01810,Anay Bedi,M,2018-05-02,7,B+,+91-00000-52695,Thiruvananthapuram,None known,2021-11-18
P01811,Manbir Mangal,M,1994-04-02,31,AB+,+91-00000-13236,Kottayam,None known,2022-02-26
P01813,Ryan Bose,M,1955-07-24,70,AB+,+91-00000-86833,Alappuzha,None known,2022-06-26
P01814,Triya Bora,F,1995-09-26,29,B+,+91-00000-11553,Thiruvananthapuram,None known,2023-03-02
P01815,Samesh Korpal,M,1974-02-15,51,O-,+91-00000-86398,Kottayam,None known,2023-07-30
P01816,Tamanna Oak,F,1985-01-23,40,AB+,+91-00000-51748,Kottayam,None known,2022-11-20
P01817,Theodore Karan,M,2009-12-25,15,AB-,+91-00000-97514,Kollam,None known,2022-04-28
P01818,Yahvi Bhatnagar,F,1987-05-12,38,O+,+91-00000-54199,Pathanamthitta,None known,2023-08-21
P01819,Atharv Mohanty,M,1996-07-02,29,B-,+91-00000-83859,Kottayam,None known,2023-10-09
P01820,Samuel Madan,M,1975-01-21,50,A+,+91-00000-99175,Kanyakumari,None known,2021-12-04
P01821,Madhav Ratta,M,1978-08-10,46,AB+,+91-00000-24715,Alappuzha,None known,2022-11-22
P01822,Maanav Pillay,M,2023-07-07,2,AB-,+91-00000-97636,Thiruvananthapuram,None known,2023-09-20
P01823,Adweta Shan,F,1979-07-25,46,A+,+91-00000-34571,Alappuzha,None known,2021-10-26
P01824,Arin Nayak,M,2015-05-18,10,B+,+91-00000-81877,Kottayam,None known,2023-06-24
P01825,Yatan Purohit,M,1987-09-04,37,B-,+91-00000-13183,Alappuzha,None known,2022-05-20
P01826,Charita Madan,F,1956-08-31,68,A+,+91-00000-43203,Pathanamthitta,None known,2023-12-28
P01827,Atharv Amble,M,2024-10-12,0,O-,+91-00000-34084,Pathanamthitta,None known,2023-12-18
P01828,Neelima Misra,F,1988-08-09,36,A+,+91-00000-73103,Pathanamthitta,None known,2021-09-16
P01829,Gaurangi Contractor,F,2024-02-29,1,AB-,+91-00000-26322,Pathanamthitta,None known,2021-10-14
P01830,Jagat Balan,M,2003-09-09,21,AB-,+91-00000-45677,Kollam,None known,2022-10-16
P01831,Wridesh Bahri,M,1996-03-05,29,O-,+91-00000-55881,Kanyakumari,None known,2023-03-31
P01832,Amrita Parsa,F,1980-04-02,45,B-,+91-00000-81223,Kollam,None known,2023-02-22
P01833,Aarini Sawhney,F,1960-05-05,65,AB-,+91-00000-83186,Kottayam,None known,2022-02-10
P01834,Zansi Gaba,F,1942-09-10,82,AB-,+91-00000-44780,Kottayam,None known,2023-07-09
P01835,Advik Saini,M,1962-08-13,62,A-,+91-00000-29338,Kollam,NSAIDs,2021-10-25
P01837,Yatin Chatterjee,M,1996-09-06,28,AB+,+91-00000-68440,Thiruvananthapuram,None known,2023-10-15
P01838,Orinder Raju,M,1980-07-11,45,AB-,+91-00000-89972,Alappuzha,None known,2023-08-21
P01840,Saumya Dhar,F,1965-08-05,59,AB+,+91-00000-63832,Kanyakumari,None known,2023-04-08
P01842,Atharv Yadav,M,2009-07-23,15,O-,+91-00000-91426,Thiruvananthapuram,Penicillin,2023-03-21
P01843,Aryan Soman,M,1954-10-14,70,A+,+91-00000-42316,Kollam,NSAIDs,2023-12-15
P01844,Dominic Prashad,M,1986-10-16,38,A+,+91-00000-67891,Kollam,None known,2022-03-12
P01845,Aarush Gala,M,1945-04-11,80,A+,+91-00000-84163,Kottayam,None known,2021-09-23
P01846,Lopa Dhawan,F,2005-03-28,20,AB+,+91-00000-71349,Pathanamthitta,None known,2023-09-27
P01847,Yash Chowdhury,M,1968-09-26,56,AB-,+91-00000-84658,Pathanamthitta,None known,2023-02-26
P01848,Mitesh Sankar,M,1992-09-16,32,A+,+91-00000-36068,Alappuzha,None known,2023-02-12
P01849,Aarini Narasimhan,F,2020-11-08,4,B+,+91-00000-71183,Kanyakumari,None known,2023-08-05
P01850,Isaiah Radhakrishnan,M,1985-12-15,39,A+,+91-00000-30178,Thiruvananthapuram,None known,2023-11-29
P01851,Mahika Buch,F,1957-07-26,68,O-,+91-00000-11202,Alappuzha,None known,2022-05-11
P01852,Samarth Shenoy,M,1992-04-15,33,A+,+91-00000-73819,Kollam,None known,2023-08-22
P01853,Bhavani Wable,F,1939-11-11,85,AB-,+91-00000-42824,Kollam,Penicillin,2022-06-26
P01854,Brinda Bandi,F,2018-09-29,6,B+,+91-00000-43954,Kanyakumari,None known,2023-06-28
P01855,Vaishnavi Srinivasan,F,2018-06-25,7,AB+,+91-00000-46775,Alappuzha,None known,2023-08-25
P01856,Jeet Nigam,M,1989-03-20,36,A+,+91-00000-71036,Thiruvananthapuram,None known,2022-02-15
P01857,Harinakshi Chawla,F,1998-08-31,26,B-,+91-00000-39078,Kollam,None known,2023-08-02
P01858,Rayaan Shere,M,1963-06-04,62,B-,+91-00000-43670,Alappuzha,None known,2022-10-07
P01859,Diya Sehgal,F,1968-10-24,56,AB-,+91-00000-34370,Alappuzha,None known,2023-03-23
P01861,Yamini Choudhary,F,1973-11-17,51,A+,+91-00000-60923,Pathanamthitta,None known,2022-09-01
P01862,Gavin Nath,M,1973-09-21,51,A-,+91-00000-49103,Thiruvananthapuram,None known,2021-08-22
P01863,Sanaya Roy,F,1978-03-25,47,A+,+91-00000-54737,Kottayam,None known,2023-05-08
P01864,Warjas Vohra,M,1940-06-18,85,O-,+91-00000-70582,Pathanamthitta,None known,2021-09-19
P01865,Urishilla Deol,F,1950-08-10,74,B+,+91-00000-70585,Alappuzha,None known,2023-09-07
P01866,Nachiket Bahl,M,1960-03-05,65,A+,+91-00000-63693,Kottayam,None known,2023-02-24
P01867,Zilmil Kari,F,1976-03-01,49,B-,+91-00000-51386,Kollam,None known,2021-10-02
P01868,Jason Hora,M,1977-01-11,48,AB+,+91-00000-46750,Kanyakumari,None known,2021-11-03
P01869,Veda Subramaniam,F,2020-07-24,4,A+,+91-00000-10444,Kollam,None known,2023-12-11
P01870,Priya Menon,F,1957-03-06,68,B+,+91-00000-54769,Kottayam,None known,2021-11-29
P01872,Eiravati Chana,F,1969-10-21,55,O+,+91-00000-13262,Kanyakumari,None known,2023-10-16
P01873,Jagrati Barman,F,1980-12-27,44,B+,+91-00000-74948,Alappuzha,None known,2023-12-07
P01874,Kashish Chaudhry,F,1973-04-01,52,O-,+91-00000-68680,Pathanamthitta,Penicillin,2023-05-28
P01875,Keya Dani,F,1993-06-25,32,O+,+91-00000-98666,Alappuzha,None known,2023-09-01
P01877,Charan Saxena,M,1946-12-14,78,O+,+91-00000-70708,Thiruvananthapuram,None known,2022-01-24
P01878,Liam Sodhi,M,1947-12-30,77,B-,+91-00000-86053,Alappuzha,NSAIDs,2023-06-24
P01879,Devansh Panchal,M,2002-03-12,23,O+,+91-00000-78928,Kanyakumari,None known,2023-12-30
P01880,Krishna Vohra,M,2018-10-29,6,AB-,+91-00000-64511,Alappuzha,Penicillin,2022-01-10
P01881,Nicholas Deshpande,M,1948-12-18,76,A-,+91-00000-21605,Kanyakumari,Penicillin,2022-05-24
P01882,Falak Kurian,F,1940-05-16,85,B+,+91-00000-73218,Kanyakumari,NSAIDs,2021-10-02
P01883,Hitesh Ghosh,M,1970-09-05,54,AB+,+91-00000-42755,Kollam,None known,2021-10-20
P01884,Jeevika D’Alia,F,1993-09-02,31,O-,+91-00000-88461,Pathanamthitta,None known,2023-10-23
P01885,Anjali Rout,F,1970-11-08,54,B+,+91-00000-32943,Pathanamthitta,None known,2022-11-22
P01886,Oviya Borde,F,1985-10-23,39,A+,+91-00000-88539,Thiruvananthapuram,None known,2023-09-23
P01887,Ayushman Bassi,M,1978-10-15,46,B+,+91-00000-33599,Kollam,NSAIDs,2022-05-15
P01888,Shravya Bhat,F,1999-03-08,26,AB+,+91-00000-10621,Pathanamthitta,None known,2023-11-15
P01889,Yagnesh Batta,M,1968-10-21,56,B-,+91-00000-29944,Pathanamthitta,None known,2022-09-14
P01890,Udant Iyengar,M,1972-02-17,53,B-,+91-00000-34235,Thiruvananthapuram,None known,2021-09-13
P01891,Nitara Saran,F,1990-07-25,35,AB-,+91-00000-34291,Pathanamthitta,None known,2023-03-11
P01892,Qarin Bhargava,M,2008-01-22,17,AB-,+91-00000-12427,Kanyakumari,Sulfa drugs,2022-11-26
P01893,Bhavna Radhakrishnan,F,2024-02-04,1,O-,+91-00000-37986,Kottayam,Sulfa drugs,2023-01-02
P01894,Tanmayi Shere,F,1943-06-21,82,A-,+91-00000-14463,Alappuzha,None known,2023-11-29
P01895,Ishanvi Doctor,F,1961-05-09,64,A+,+91-00000-93046,Kollam,None known,2023-05-10
P01896,Varsha Sathe,F,1968-08-14,56,O+,+91-00000-87963,Pathanamthitta,Sulfa drugs,2023-12-04
P01898,Aadhya Rao,F,1969-02-27,56,O+,+91-00000-77190,Kottayam,None known,2023-11-18
P01900,Ekantika Kant,F,1992-04-25,33,A-,+91-00000-61479,Alappuzha,None known,2023-10-22
P01901,Sarthak Desai,M,1970-11-06,54,O+,+91-00000-27863,Kollam,None known,2023-09-27
P01904,Raagini Chacko,F,1947-03-13,78,AB+,+91-00000-31042,Thiruvananthapuram,Penicillin,2022-12-29
P01907,Atharv Sibal,M,1959-06-04,66,A+,+91-00000-50610,Kottayam,None known,2023-04-09
P01909,Vedhika Sharaf,F,1967-09-28,57,AB-,+91-00000-31528,Pathanamthitta,None known,2023-01-10
P01910,Advika Garde,F,1967-03-06,58,A-,+91-00000-65175,Pathanamthitta,None known,2023-11-16
P01911,Rajeshri Patla,F,1995-05-15,30,O+,+91-00000-66632,Kottayam,None known,2023-09-17
P01912,Bhavani Agrawal,F,1991-06-12,34,O-,+91-00000-67286,Thiruvananthapuram,None known,2022-09-10
P01913,Ojasvi Swamy,F,1976-01-20,49,AB-,+91-00000-54498,Kollam,None known,2022-01-17
P01914,Xavier Hora,M,1979-01-17,46,A-,+91-00000-32104,Alappuzha,None known,2021-11-25
P01916,Vedhika Ranganathan,F,1988-12-28,36,O-,+91-00000-88519,Kanyakumari,None known,2021-11-04
P01917,Abdul Nanda,M,1971-06-05,54,A+,+91-00000-89965,Kottayam,Penicillin,2023-02-08
P01918,Parth Bhat,M,2009-02-03,16,O-,+91-00000-85502,Pathanamthitta,Sulfa drugs,2022-04-04
P01919,Rudra Mutti,M,1988-05-24,37,AB+,+91-00000-46149,Kollam,None known,2023-06-16
P01920,Mahika Bhattacharyya,F,2014-02-08,11,AB+,+91-00000-82210,Kollam,None known,2023-11-22
P01921,Chanakya Mody,M,2019-03-29,6,B-,+91-00000-50728,Kanyakumari,None known,2022-09-18
P01922,Rudra Dash,M,1942-12-16,82,A-,+91-00000-96638,Pathanamthitta,None known,2023-01-05
P01923,Chakradev Uppal,M,2024-07-16,1,O+,+91-00000-26172,Thiruvananthapuram,None known,2023-10-06
P01924,Siddharth Parikh,M,2015-11-14,9,O+,+91-00000-10712,Pathanamthitta,None known,2023-11-01
P01925,Arin Nori,M,1977-06-03,48,A-,+91-00000-29272,Pathanamthitta,Penicillin,2023-01-03
P01926,Indira Wali,F,1936-03-22,89,B-,+91-00000-48118,Kottayam,None known,2022-11-22
P01927,Nidhi Kara,F,1939-12-15,85,AB+,+91-00000-84294,Kollam,None known,2022-05-18
P01928,Nicholas Atwal,M,1967-06-18,58,B+,+91-00000-16781,Kanyakumari,None known,2021-12-13
P01929,Zaitra Mitra,F,1955-09-05,69,A-,+91-00000-95932,Thiruvananthapuram,None known,2022-02-04
P01930,Turvi Manne,F,1935-01-12,90,O-,+91-00000-26658,Kottayam,None known,2022-05-31
P01931,Pallavi Suresh,F,1991-07-05,34,A+,+91-00000-60859,Kollam,None known,2023-05-12
P01932,Zaitra Lata,F,1985-12-31,39,B+,+91-00000-30696,Kollam,None known,2023-09-19
P01934,Samar Palla,M,2000-12-19,24,AB+,+91-00000-10949,Thiruvananthapuram,None known,2022-09-13
P01936,Nimrat Purohit,F,1969-05-12,56,O+,+91-00000-17442,Kottayam,Penicillin,2023-07-03
P01937,Baghyawati Pal,F,1973-12-11,51,B+,+91-00000-44542,Pathanamthitta,NSAIDs,2022-09-23
P01938,Dhruv Kota,M,1941-08-03,84,AB-,+91-00000-16281,Alappuzha,None known,2022-11-26
P01939,Chasmum Warrior,F,1997-09-09,27,A-,+91-00000-86997,Kollam,None known,2023-05-06
P01940,Farhan Chopra,M,1952-12-26,72,AB+,+91-00000-97135,Thiruvananthapuram,None known,2022-06-21
P01942,Ekani Rajagopal,F,1940-08-14,84,B+,+91-00000-10175,Alappuzha,Penicillin,2022-01-13
P01943,Naksh Uppal,M,1935-04-01,90,A+,+91-00000-87774,Pathanamthitta,None known,2023-05-11
P01944,Krish Bhargava,M,2000-06-19,25,AB+,+91-00000-63403,Pathanamthitta,None known,2022-02-19
P01945,Thomas Rajan,M,1996-04-24,29,O-,+91-00000-59213,Kanyakumari,None known,2023-09-26
P01946,Bakhshi Bajaj,M,1991-10-15,33,A-,+91-00000-30829,Thiruvananthapuram,Sulfa drugs,2023-04-02
P01947,Leela Chandran,F,2016-02-19,9,O+,+91-00000-34264,Alappuzha,None known,2021-11-06
P01948,Janani Garde,F,1994-06-22,31,AB+,+91-00000-53222,Kollam,NSAIDs,2021-12-05
P01949,Matthew Setty,M,1998-10-18,26,A-,+91-00000-89984,Kollam,None known,2022-06-06
P01950,Unni Nagarajan,F,1975-02-09,50,AB-,+91-00000-50113,Kottayam,None known,2021-12-31
P01951,Henry Kulkarni,M,1973-07-02,52,B-,+91-00000-48020,Alappuzha,None known,2023-12-11
P01952,Praneel Chakraborty,M,1972-05-05,53,AB+,+91-00000-83261,Kottayam,Penicillin,2021-10-01
P01953,Bishakha Subramaniam,F,1975-10-19,49,AB-,+91-00000-94080,Kanyakumari,None known,2022-07-06
P01954,Chavvi Vala,F,1997-12-04,27,AB+,+91-00000-70868,Kanyakumari,None known,2023-06-26
P01955,Edhitha Kapur,F,1965-09-01,59,AB-,+91-00000-39231,Kottayam,None known,2024-01-03
P01956,Zansi Agarwal,F,1965-01-13,60,A-,+91-00000-32426,Thiruvananthapuram,NSAIDs,2023-01-01
P01957,Dominic Bhat,M,1993-12-09,31,A-,+91-00000-12003,Kollam,None known,2021-10-20
P01958,Yadavi Sekhon,F,1978-06-25,47,O-,+91-00000-60523,Pathanamthitta,None known,2023-03-27
P01959,Yug Bala,M,1979-06-24,46,A+,+91-00000-33181,Pathanamthitta,NSAIDs,2022-02-08
P01961,Anmol Vora,M,2008-02-28,17,A-,+91-00000-78788,Kanyakumari,None known,2022-03-08
P01962,Aarnav Sibal,M,1950-10-03,74,O-,+91-00000-21583,Alappuzha,None known,2022-10-15
P01963,Devika Narasimhan,F,2018-02-20,7,AB+,+91-00000-58918,Kanyakumari,None known,2022-06-11
P01964,Hema Sachdeva,F,1948-02-11,77,B-,+91-00000-24576,Kollam,None known,2023-09-21
P01965,Omya Date,F,1977-08-01,47,AB+,+91-00000-77111,Alappuzha,None known,2022-06-03
P01967,Lakshit Mani,M,1986-12-22,38,O-,+91-00000-50786,Pathanamthitta,None known,2021-12-23
P01969,Brijesh Randhawa,M,1963-06-23,62,B+,+91-00000-52640,Kottayam,None known,2023-04-01
P01970,Rajeshri Jayaraman,F,1989-10-09,35,B-,+91-00000-49074,Kollam,None known,2023-05-24
P01971,Ikshita Agarwal,F,1966-07-18,59,AB-,+91-00000-32530,Pathanamthitta,None known,2023-09-12
P01974,Warinder Gade,M,2020-01-28,5,AB+,+91-00000-99350,Thiruvananthapuram,None known,2021-11-05
P01975,Aryan Natt,M,1959-10-16,65,O-,+91-00000-81900,Pathanamthitta,None known,2021-11-02
P01976,Robert Minhas,M,1955-12-14,69,O+,+91-00000-51570,Kottayam,None known,2022-07-10
P01977,Laban Kaul,M,1995-04-15,30,B+,+91-00000-59285,Kanyakumari,None known,2023-02-08
P01978,Brijesh Kant,M,1979-11-06,45,B+,+91-00000-94507,Thiruvananthapuram,None known,2022-02-02
P01979,Adya Din,F,2009-12-08,15,AB-,+91-00000-36382,Kollam,None known,2022-07-17
P01980,Akshay Dutta,M,1994-11-18,30,A+,+91-00000-58839,Alappuzha,None known,2023-10-24
P01981,Yatin Salvi,M,1944-10-13,80,O+,+91-00000-53599,Thiruvananthapuram,None known,2022-09-30
P01982,Samuel Pillai,M,1973-05-16,52,O+,+91-00000-95842,Kollam,None known,2022-06-25
P01983,Naksh Mohan,M,1942-09-22,82,AB+,+91-00000-34401,Kollam,None known,2022-03-06
P01984,Girindra Walia,M,1993-06-25,32,AB-,+91-00000-31418,Kollam,None known,2022-07-27
P01985,Upasna Chauhan,F,1938-01-04,87,O+,+91-00000-84404,Kollam,None known,2023-07-09
P01986,Vincent Balan,M,2019-05-18,6,A+,+91-00000-67792,Pathanamthitta,NSAIDs,2021-08-27
P01987,Pranav Varma,M,1971-01-09,54,AB+,+91-00000-94139,Kottayam,None known,2023-08-21
P01988,Arya Kohli,F,1988-03-07,37,O+,+91-00000-66875,Kanyakumari,None known,2023-06-03
P01989,Edhitha Kaul,F,1990-05-24,35,AB+,+91-00000-19351,Kottayam,None known,2023-05-28
P01990,Ojasvi Jain,F,2016-12-02,8,B-,+91-00000-51344,Kanyakumari,None known,2022-12-01
P01991,Jason Merchant,M,1964-12-24,60,B-,+91-00000-54673,Kanyakumari,None known,2022-05-31
P01992,Faras Thakur,M,2018-09-22,6,A-,+91-00000-45305,Kanyakumari,None known,2021-08-23
P01993,Yadavi Chhabra,F,1986-06-11,39,A-,+91-00000-83551,Thiruvananthapuram,None known,2023-09-22
P01994,Janaki Tailor,F,1947-01-02,78,O-,+91-00000-15012,Thiruvananthapuram,NSAIDs,2021-08-04
P01995,Ati Pillay,F,1992-11-22,32,A+,+91-00000-94794,Pathanamthitta,None known,2021-12-13
P01996,Hritik Bhavsar,M,1981-06-04,44,O-,+91-00000-21674,Alappuzha,None known,2021-07-31
P01997,Harinakshi Merchant,F,2023-04-03,2,AB+,+91-00000-14903,Pathanamthitta,None known,2022-05-05
P01998,Ansh Agate,M,2011-01-08,14,B-,+91-00000-48521,Kottayam,None known,2024-01-02
P01999,Peter Butala,M,1995-06-07,30,A+,+91-00000-73033,Pathanamthitta,None known,2022-04-20
P02000,Rachana Batra,F,1935-07-20,90,AB+,+91-00000-11863,Pathanamthitta,None known,2022-06-02
P02001,Ishani Sant,F,1993-04-12,32,A-,+91-00000-74830,Kanyakumari,None known,2021-09-12
P02003,Chasmum Parmer,F,2003-08-03,21,A-,+91-00000-15506,Kollam,None known,2022-12-26
P02004,Manthan Bhalla,M,1954-03-14,71,A-,+91-00000-39976,Kanyakumari,None known,2022-11-14
P02005,Edhitha Sathe,F,1991-07-09,34,AB-,+91-00000-97396,Kottayam,None known,2023-07-06
P02006,Chandran Lala,M,2020-03-25,5,B+,+91-00000-38975,Thiruvananthapuram,None known,2023-12-24
P02007,Urvi Dash,F,2021-12-06,3,A+,+91-00000-87579,Kottayam,None known,2023-01-02
P02008,Jairaj Ramaswamy,M,1989-11-17,35,A-,+91-00000-93857,Kollam,None known,2023-08-20
P02009,Libni Aggarwal,F,1954-08-24,70,AB+,+91-00000-66281,Pathanamthitta,None known,2021-12-16
P02010,Riya Yadav,F,2011-09-21,13,B-,+91-00000-74510,Kanyakumari,None known,2023-10-31
P02011,Jai Sen,M,1952-04-30,73,O-,+91-00000-59558,Kollam,None known,2022-08-21
P02012,Ekta Sunder,F,1967-04-21,58,B-,+91-00000-33848,Kollam,None known,2021-08-18
P02013,Jasmit Issac,F,1992-01-03,33,O-,+91-00000-74826,Pathanamthitta,None known,2023-02-25
P02014,David Subramaniam,M,1947-04-24,78,AB+,+91-00000-34330,Pathanamthitta,None known,2022-07-21
P02015,Lohit Kapoor,M,1944-06-17,81,AB+,+91-00000-62007,Kanyakumari,None known,2023-06-17
P02016,Chaitanya Upadhyay,M,1980-08-12,44,B+,+91-00000-14161,Kollam,None known,2022-04-18
P02017,Orinder Saha,M,1938-09-30,86,B-,+91-00000-66866,Kottayam,None known,2022-02-27
P02019,Darpan Behl,M,1968-12-24,56,O+,+91-00000-99861,Kanyakumari,None known,2022-03-05
P02020,Vedhika Ramakrishnan,F,2017-11-12,7,B-,+91-00000-26782,Kottayam,None known,2023-01-28
P02021,Jacob Garde,M,2019-08-25,5,A-,+91-00000-91535,Alappuzha,None known,2023-09-30
P02022,Azad Seshadri,M,1959-07-27,66,AB-,+91-00000-36205,Alappuzha,None known,2021-12-26
P02023,Ishita Agrawal,F,1968-04-21,57,O+,+91-00000-53320,Kottayam,None known,2022-07-31
P02024,Jairaj Date,M,2018-11-30,6,A+,+91-00000-54594,Thiruvananthapuram,None known,2023-04-18
P02025,Vrishti Chacko,F,1994-10-16,30,B+,+91-00000-10530,Thiruvananthapuram,None known,2022-01-21
P02026,Oscar Soni,M,1972-08-09,52,AB-,+91-00000-86798,Thiruvananthapuram,None known,2022-12-02
P02027,Sathvik Contractor,M,2016-05-31,9,O+,+91-00000-63198,Pathanamthitta,None known,2022-04-29
P02028,Abhimanyu Devan,M,2023-07-21,1,A-,+91-00000-78809,Pathanamthitta,None known,2022-02-21
P02029,Meghana Deol,F,1989-08-06,35,O-,+91-00000-22762,Thiruvananthapuram,None known,2021-10-18
P02030,Advik Kumer,M,1994-09-19,30,O-,+91-00000-15599,Kollam,None known,2022-09-01
P02031,Ekapad Modi,M,2020-03-21,5,AB+,+91-00000-87713,Kanyakumari,None known,2022-01-08
P02032,Varsha Dhawan,F,1983-01-21,42,AB-,+91-00000-99769,Kollam,None known,2021-12-14
P02033,Ryan Swaminathan,M,1939-01-08,86,O-,+91-00000-10985,Thiruvananthapuram,None known,2022-05-24
P02034,Yutika Balakrishnan,F,1965-02-21,60,AB+,+91-00000-34267,Pathanamthitta,None known,2023-03-16
P02035,Fariq Suresh,M,2010-08-23,14,AB+,+91-00000-11390,Alappuzha,None known,2021-11-09
P02036,Girik Tailor,M,2004-10-09,20,AB-,+91-00000-18093,Kottayam,None known,2022-09-06
P02037,Janaki Nadig,F,1975-06-21,50,B+,+91-00000-54032,Thiruvananthapuram,Penicillin,2022-02-05
P02038,Orinder Jaggi,M,1983-09-01,41,B+,+91-00000-51509,Pathanamthitta,None known,2021-11-25
P02039,Baghyawati Saxena,F,1988-03-05,37,B+,+91-00000-31165,Kottayam,None known,2023-08-03
P02040,Veer Solanki,M,1983-08-28,41,AB-,+91-00000-60312,Kottayam,None known,2022-08-16
P02041,Theodore Deshmukh,M,1988-05-23,37,O+,+91-00000-16301,Thiruvananthapuram,None known,2022-01-27
P02042,Mohini Mahal,F,1941-01-06,84,AB-,+91-00000-44412,Kottayam,None known,2023-06-05
P02043,Tanveer Master,M,1974-10-01,50,B-,+91-00000-31721,Kollam,None known,2022-02-06
P02044,Gopal Magar,M,2016-03-27,9,B-,+91-00000-50145,Kanyakumari,None known,2022-01-17
P02045,Nidhi Bhatt,F,1937-01-17,88,A+,+91-00000-49494,Pathanamthitta,None known,2023-03-05
P02046,Yashawini Dhingra,F,1936-03-15,89,B+,+91-00000-31604,Thiruvananthapuram,None known,2021-09-02
P02047,Bachittar Peri,M,1999-03-19,26,A-,+91-00000-16532,Thiruvananthapuram,None known,2022-06-28
P02048,Vihaan Buch,M,1955-11-16,69,AB-,+91-00000-11791,Alappuzha,None known,2022-11-18
P02049,Sathvik Srinivasan,M,1947-01-30,78,AB-,+91-00000-57703,Kottayam,None known,2021-08-08
P02050,Ishita Chada,F,1997-09-10,27,A+,+91-00000-43601,Pathanamthitta,None known,2021-08-06
P02051,Ranbir Shankar,M,1951-04-28,74,A-,+91-00000-89296,Pathanamthitta,None known,2023-08-24
P02053,Baghyawati Das,F,1961-08-27,63,AB-,+91-00000-71070,Kanyakumari,None known,2023-03-15
P02054,Tanvi Dhillon,F,1965-10-29,59,O-,+91-00000-72546,Alappuzha,None known,2021-08-23
P02055,Veer Bhatnagar,M,2013-11-28,11,B-,+91-00000-44942,Kottayam,None known,2023-03-28
P02056,Ekapad Dar,M,1992-01-10,33,B+,+91-00000-83192,Kottayam,Sulfa drugs,2022-04-22
P02057,Balveer Sandal,M,2006-06-12,19,A+,+91-00000-90980,Kanyakumari,None known,2022-06-08
P02058,Chatura Devan,M,1975-09-22,49,B-,+91-00000-75816,Kottayam,None known,2022-03-23
P02059,Chatresh Brahmbhatt,M,1955-07-07,70,AB-,+91-00000-13982,Alappuzha,None known,2021-08-12
P02060,Balhaar Saxena,M,2004-11-30,20,A+,+91-00000-49321,Kollam,None known,2023-04-16
P02061,Gauri Majumdar,F,2013-09-05,11,A+,+91-00000-98539,Alappuzha,None known,2023-12-17
P02062,Arjun Bajaj,M,1989-12-12,35,B-,+91-00000-68484,Pathanamthitta,None known,2023-08-06
P02063,Irya Palan,F,2002-12-06,22,A+,+91-00000-17958,Alappuzha,None known,2023-05-13
P02064,Upasna Char,F,2000-06-30,25,B-,+91-00000-43520,Kollam,None known,2023-02-11
P02066,Kai Dutt,M,1980-03-04,45,O-,+91-00000-16472,Pathanamthitta,None known,2023-12-31
P02067,Aradhana Kalla,F,1960-10-16,64,O-,+91-00000-78106,Kollam,None known,2023-06-15
P02068,Orinder Rege,M,1968-02-13,57,AB-,+91-00000-90581,Kanyakumari,None known,2022-08-16
P02070,Wahab Jayaraman,M,1970-05-09,55,B+,+91-00000-12652,Pathanamthitta,None known,2022-02-25
P02071,Hitesh Babu,M,1977-05-12,48,A-,+91-00000-34448,Alappuzha,None known,2022-05-27
P02072,Samesh Balakrishnan,M,1939-02-02,86,A+,+91-00000-85289,Pathanamthitta,None known,2023-10-11
P02073,Charita Rattan,F,1957-09-05,67,B+,+91-00000-36353,Alappuzha,None known,2022-10-26
P02074,Faraj Aurora,M,1969-10-04,55,B+,+91-00000-35354,Kollam,None known,2023-03-23
P02075,Parth Oza,M,2019-03-15,6,O-,+91-00000-50120,Kottayam,None known,2022-04-13
P02076,Jatin Grewal,M,1988-02-19,37,A+,+91-00000-95307,Pathanamthitta,NSAIDs,2023-10-31
P02077,Harish Wadhwa,M,1945-09-15,79,A+,+91-00000-84536,Kottayam,None known,2022-12-16
P02078,Logan Mann,M,1953-09-06,71,B+,+91-00000-65597,Kollam,Penicillin,2022-01-24
P02079,Lekha Hora,F,1997-09-25,27,B+,+91-00000-98716,Kottayam,None known,2022-10-28
P02080,Kai Kakar,M,1942-03-01,83,AB+,+91-00000-71020,Kottayam,None known,2022-07-05
P02081,Oscar Ganguly,M,2010-05-03,15,B+,+91-00000-13183,Kollam,None known,2022-07-17
P02082,Agastya Kurian,M,1968-01-07,57,AB+,+91-00000-34490,Thiruvananthapuram,None known,2021-08-19
P02083,Anjali Mukherjee,F,2024-09-29,0,AB+,+91-00000-20094,Pathanamthitta,None known,2023-07-07
P02084,Dakshesh Baral,M,2005-09-14,19,A+,+91-00000-77521,Alappuzha,None known,2022-11-14
P02085,Krishna Khurana,F,1994-07-14,31,AB+,+91-00000-33810,Kollam,None known,2022-02-19
P02086,Bahadurjit Chaudhry,M,2010-01-26,15,A+,+91-00000-79096,Pathanamthitta,None known,2022-09-02
P02087,Girish Dhar,M,1993-08-16,31,O+,+91-00000-12039,Pathanamthitta,None known,2023-06-05
P02088,Vivaan Mahajan,M,1981-04-27,44,B-,+91-00000-72007,Kollam,None known,2021-09-29
P02089,Girindra Patla,M,2021-06-30,4,O+,+91-00000-27666,Thiruvananthapuram,None known,2022-12-23
P02091,Keya Kata,F,1962-03-18,63,B-,+91-00000-69720,Alappuzha,None known,2023-04-20
P02092,Neel Chaudhry,M,1939-05-20,86,AB+,+91-00000-69861,Pathanamthitta,None known,2021-12-09
P02093,Sachi Mander,F,1969-04-25,56,A+,+91-00000-97836,Kottayam,None known,2022-11-21
P02094,Jatin Ramanathan,M,1970-12-15,54,AB+,+91-00000-93972,Pathanamthitta,None known,2022-10-21
P02095,Fiyaz Kar,M,1943-11-14,81,O-,+91-00000-79864,Thiruvananthapuram,None known,2021-08-18
P02096,Amrita Kibe,F,2015-05-16,10,B+,+91-00000-52022,Pathanamthitta,None known,2022-09-12
P02097,Rajeshri Dalal,F,1951-12-07,73,AB+,+91-00000-59436,Alappuzha,None known,2022-11-13
P02098,Teerth Deshpande,M,1979-08-02,45,A-,+91-00000-29981,Thiruvananthapuram,None known,2022-06-23
P02099,Manbir Vasa,M,2019-08-18,5,B+,+91-00000-91695,Pathanamthitta,None known,2021-08-01
P02100,Anita Garg,F,1995-11-13,29,B-,+91-00000-47312,Kottayam,None known,2022-02-28
P02101,Kamya Master,F,1974-04-15,51,B+,+91-00000-92240,Thiruvananthapuram,None known,2023-05-11
P02102,David Sarraf,M,1959-12-03,65,O-,+91-00000-67814,Kanyakumari,None known,2022-06-12
P02103,Nimrat Cherian,F,1958-11-17,66,O+,+91-00000-47402,Pathanamthitta,None known,2023-01-26
P02104,Nandini Bail,F,1978-11-17,46,B-,+91-00000-84929,Alappuzha,None known,2022-09-16
P02105,Siya Vasa,F,1994-05-08,31,A+,+91-00000-93482,Kollam,None known,2021-08-17
P02106,Utkarsh Sinha,M,1955-05-20,70,O-,+91-00000-38753,Alappuzha,None known,2022-10-21
P02107,Hemal Chada,F,1992-04-12,33,A+,+91-00000-18614,Kanyakumari,None known,2023-05-07
P02108,Jhalak Mallick,F,1971-05-02,54,A+,+91-00000-95728,Kanyakumari,None known,2021-10-05
P02109,Isha Amble,F,1981-06-16,44,B+,+91-00000-84935,Alappuzha,None known,2021-11-25
P02110,Indali Buch,F,2021-07-19,4,AB+,+91-00000-98777,Kanyakumari,None known,2021-12-18
P02111,Gaurav Viswanathan,M,2012-04-05,13,A-,+91-00000-90401,Kollam,None known,2022-07-27
P02112,Gabriel Srinivasan,M,2015-04-25,10,A+,+91-00000-87664,Pathanamthitta,None known,2022-11-08
P02113,Vrishti Dhaliwal,F,2010-03-02,15,B-,+91-00000-72805,Thiruvananthapuram,None known,2023-02-10
P02114,Neelima Toor,F,2007-06-11,18,O-,+91-00000-16525,Pathanamthitta,None known,2023-07-24
P02115,Vedika Vohra,F,1976-11-29,48,A-,+91-00000-41159,Kanyakumari,Sulfa drugs,2023-07-04
P02116,Hritik Majumdar,M,2011-10-09,13,AB+,+91-00000-49317,Kollam,Sulfa drugs,2023-10-23
P02117,Daksha Mistry,F,1992-02-24,33,A-,+91-00000-93218,Kottayam,None known,2022-07-02
P02118,Lipika Joshi,F,1979-01-16,46,A-,+91-00000-31473,Kottayam,None known,2023-10-08
P02119,Mitali Morar,F,1976-02-28,49,AB+,+91-00000-91098,Thiruvananthapuram,None known,2024-01-14
P02122,Pranav Dhingra,M,1997-06-17,28,O+,+91-00000-95184,Kollam,None known,2022-02-10
P02123,Zayyan Tandon,M,1971-05-27,54,O-,+91-00000-86527,Thiruvananthapuram,None known,2022-02-05
P02125,Sanaya Sarna,F,2024-07-29,0,O-,+91-00000-60321,Kollam,None known,2023-12-25
P02126,Caleb Dar,M,1953-03-20,72,A-,+91-00000-34980,Alappuzha,None known,2023-11-29
P02127,Abhiram Nadig,M,2000-03-07,25,O+,+91-00000-98987,Thiruvananthapuram,None known,2021-11-09
P02128,Ishwar Sarin,M,2025-07-02,0,A+,+91-00000-77565,Thiruvananthapuram,None known,2023-01-29
P02130,Krish Chana,M,2020-05-29,5,AB+,+91-00000-70146,Kanyakumari,None known,2022-10-24
P02131,Arya Sangha,F,2020-11-27,4,AB-,+91-00000-81052,Thiruvananthapuram,None known,2022-08-08
P02133,Fiyaz Ramanathan,M,2014-11-02,10,B+,+91-00000-49367,Kollam,None known,2021-08-15
P02134,Praneel Misra,M,1944-11-05,80,AB-,+91-00000-65338,Kollam,None known,2023-05-13
P02135,Fitan Bala,M,2017-09-18,7,B-,+91-00000-16205,Kottayam,None known,2023-04-14
P02136,Ganga Goel,F,1978-04-28,47,O-,+91-00000-99246,Alappuzha,None known,2022-07-23
P02137,Gavin Garde,M,1942-12-05,82,O-,+91-00000-21934,Alappuzha,None known,2022-04-30
P02138,Yauvani Kapadia,F,1987-04-30,38,AB+,+91-00000-80683,Alappuzha,None known,2024-01-07
P02140,Varsha Ahuja,F,1966-01-19,59,A+,+91-00000-67849,Kottayam,NSAIDs,2022-01-09
P02142,Balvan Sharaf,M,2014-05-18,11,AB-,+91-00000-39242,Kottayam,None known,2022-05-13
P02143,Finn Parekh,M,1971-09-29,53,B+,+91-00000-11429,Thiruvananthapuram,None known,2022-07-23
P02144,Reva Sastry,F,1948-07-13,77,B+,+91-00000-83882,Kollam,None known,2022-12-20
P02145,Luke Comar,M,1966-05-21,59,A-,+91-00000-30251,Alappuzha,None known,2023-09-23
P02147,Simon Naik,M,1977-02-14,48,AB-,+91-00000-38541,Kollam,None known,2022-07-06
P02148,Ijaya Madan,F,1984-09-28,40,B-,+91-00000-27203,Kollam,None known,2023-11-11
P02150,Aradhana Khanna,F,2001-11-22,23,O+,+91-00000-64072,Kottayam,Sulfa drugs,2022-10-22
P02151,Widisha Padmanabhan,F,2013-03-31,12,A+,+91-00000-30893,Kottayam,None known,2022-01-15
P02152,Maanas Tak,M,1964-07-24,61,AB+,+91-00000-40435,Kottayam,None known,2022-08-25
P02153,Gauri Savant,F,1999-05-27,26,A-,+91-00000-98864,Alappuzha,None known,2022-06-04
P02154,Jack Joshi,M,1976-04-18,49,A+,+91-00000-71100,Kottayam,None known,2023-11-17
P02155,Theodore Kashyap,M,1979-02-15,46,AB+,+91-00000-47996,Alappuzha,None known,2022-12-13
P02156,Siddharth Palla,M,1985-11-11,39,B-,+91-00000-57215,Kollam,None known,2021-10-28
P02157,Lopa Shukla,F,1983-05-25,42,AB+,+91-00000-26012,Kanyakumari,None known,2023-12-01
P02159,Jagat Nayak,M,1985-06-30,40,A-,+91-00000-95547,Kanyakumari,None known,2021-11-29
P02161,Teerth Sarkar,M,1935-03-04,90,B-,+91-00000-36943,Thiruvananthapuram,None known,2022-02-24
P02162,Yuvraj Kunda,M,1969-09-19,55,AB-,+91-00000-38640,Kottayam,None known,2022-12-05
P02167,Urishilla Kaur,F,2000-04-09,25,O-,+91-00000-77262,Pathanamthitta,None known,2023-03-23
P02168,Forum Hari,F,1989-04-03,36,B+,+91-00000-24190,Kanyakumari,None known,2022-08-06
P02169,Chakradhar Parekh,M,1977-04-12,48,A+,+91-00000-18821,Thiruvananthapuram,Penicillin,2022-09-24
P02170,David Aurora,M,1979-01-25,46,AB-,+91-00000-27491,Kanyakumari,None known,2021-12-28
P02171,Zansi Bera,F,2020-07-26,4,O-,+91-00000-34859,Kanyakumari,None known,2023-12-06
P02172,Lakshit Balan,M,2004-05-30,21,B-,+91-00000-73228,Kottayam,None known,2022-01-08
P02174,Damini Shenoy,F,1969-05-18,56,AB-,+91-00000-52342,Kanyakumari,None known,2022-03-05
P02176,Omisha Arya,F,1973-06-14,52,B+,+91-00000-94418,Kanyakumari,None known,2022-03-27
P02177,Avi Raman,M,1967-04-07,58,B-,+91-00000-74055,Pathanamthitta,NSAIDs,2021-09-14
P02178,Nakul Som,M,1985-02-24,40,O-,+91-00000-28141,Pathanamthitta,None known,2023-05-23
P02179,Yatan Khatri,M,2008-08-06,16,A-,+91-00000-91091,Kanyakumari,None known,2023-07-07
P02180,Damyanti Bandi,F,1995-09-01,29,A+,+91-00000-56575,Thiruvananthapuram,None known,2023-07-03
P02181,Kashvi Soman,F,1983-06-20,42,A-,+91-00000-76509,Kanyakumari,None known,2021-09-24
P02182,Ria Pathak,F,1987-03-19,38,O+,+91-00000-96803,Kottayam,None known,2022-11-07
P02183,Wakeeta Choudhary,F,1978-09-16,46,A+,+91-00000-48752,Thiruvananthapuram,None known,2021-09-19
P02184,Sarthak Sane,M,2022-01-04,3,AB-,+91-00000-21577,Alappuzha,None known,2022-11-02
P02185,Warhi Kapur,F,1989-11-12,35,A-,+91-00000-89064,Thiruvananthapuram,None known,2022-03-10
P02186,Harish Dutt,M,1948-03-16,77,A+,+91-00000-99959,Kollam,Penicillin,2022-04-06
P02187,Yatan Sunder,M,1992-03-16,33,AB-,+91-00000-70994,Kanyakumari,Penicillin,2023-10-09
P02188,Madhavi Kata,F,2002-05-18,23,O-,+91-00000-65262,Kollam,None known,2022-04-09
P02189,Barkha Chand,F,1990-11-03,34,AB-,+91-00000-54205,Kanyakumari,None known,2022-01-24
P02190,Kavya Bhakta,F,2006-03-21,19,O+,+91-00000-22236,Pathanamthitta,None known,2023-11-03
P02192,Yashawini Rao,F,1985-03-19,40,A+,+91-00000-83422,Kottayam,None known,2024-01-09
P02193,Dalaja Karan,F,1966-10-29,58,AB-,+91-00000-40291,Kottayam,None known,2022-02-20
P02194,Abdul Lall,M,2014-06-13,11,AB+,+91-00000-53906,Pathanamthitta,Sulfa drugs,2021-09-07
P02195,Anamika Nath,F,2014-04-27,11,B-,+91-00000-50872,Pathanamthitta,Sulfa drugs,2023-08-21
P02196,Jai Subramaniam,M,2019-01-26,6,AB-,+91-00000-37319,Alappuzha,None known,2021-11-27
P02197,Vasatika Hayre,F,1972-12-12,52,O-,+91-00000-86548,Pathanamthitta,None known,2023-10-06
P02198,Yashoda Goel,F,1978-08-10,46,AB+,+91-00000-67602,Kottayam,None known,2023-04-02
P02199,Jeremiah Chad,M,2006-12-17,18,O-,+91-00000-85904,Pathanamthitta,None known,2023-09-09
P02200,Dalaja Banerjee,F,1980-01-06,45,A-,+91-00000-36730,Kollam,NSAIDs,2022-06-17
P02201,Christopher Chad,M,1979-01-25,46,B+,+91-00000-45657,Kanyakumari,None known,2023-11-18
P02202,Anthony Balan,M,1989-12-09,35,A-,+91-00000-26826,Kollam,None known,2021-09-09
P02203,Guneet Lall,M,1976-10-26,48,B+,+91-00000-57579,Alappuzha,NSAIDs,2023-05-17
P02204,Udant Narang,M,2017-12-16,7,A+,+91-00000-27508,Kollam,None known,2023-12-27
P02205,Ethan Shere,M,2000-10-10,24,AB-,+91-00000-75950,Kottayam,None known,2022-06-04
P02206,Jack Saxena,M,1939-12-25,85,AB+,+91-00000-39071,Thiruvananthapuram,None known,2022-03-09
P02207,Hardik Sani,M,2013-07-18,12,A-,+91-00000-96636,Thiruvananthapuram,None known,2023-09-15
P02208,Jeet Bahl,M,2011-07-14,14,O+,+91-00000-95716,Thiruvananthapuram,None known,2022-02-12
P02209,Damini Dave,F,1995-07-02,30,B+,+91-00000-27977,Alappuzha,None known,2024-01-03
P02210,Chakrika Tripathi,F,1978-08-15,46,B+,+91-00000-61639,Thiruvananthapuram,NSAIDs,2022-10-14
P02211,Isaac Goyal,M,1997-05-05,28,AB+,+91-00000-78133,Kollam,None known,2021-11-22
P02212,Lajita Mander,F,1984-04-04,41,B-,+91-00000-47197,Thiruvananthapuram,None known,2021-12-13
P02213,Aarini Prabhakar,F,2025-04-16,0,A-,+91-00000-30911,Pathanamthitta,None known,2022-07-27
P02214,Tarak Sethi,M,2007-08-06,17,AB+,+91-00000-67750,Pathanamthitta,None known,2023-01-13
P02215,Kai Anne,M,1994-06-24,31,AB-,+91-00000-33281,Kanyakumari,None known,2024-01-09
P02216,Yatin Rastogi,M,2024-10-11,0,O+,+91-00000-74190,Kollam,None known,2023-10-02
P02217,Kevin Dash,M,1937-08-31,87,AB+,+91-00000-31770,Kollam,None known,2022-12-21
P02218,Samaksh Nanda,M,2014-01-28,11,AB+,+91-00000-97891,Thiruvananthapuram,None known,2023-02-09
P02219,Tanvi Nadig,F,1955-09-19,69,O-,+91-00000-11589,Pathanamthitta,NSAIDs,2023-08-26
P02220,Bakhshi Vohra,M,1963-04-22,62,O+,+91-00000-15119,Alappuzha,None known,2023-05-01
P02221,Pranav Raman,M,1956-06-19,69,O-,+91-00000-15415,Thiruvananthapuram,None known,2022-04-24
P02222,Imaran Pandya,M,2016-03-25,9,O+,+91-00000-89323,Kollam,None known,2023-10-09
P02223,Aarush Subramaniam,M,1986-08-17,38,B+,+91-00000-68275,Alappuzha,None known,2021-09-20
P02225,Falak Shanker,F,1945-04-17,80,B-,+91-00000-23948,Thiruvananthapuram,None known,2022-04-02
P02226,Lajita Raval,F,2009-08-17,15,AB+,+91-00000-15186,Pathanamthitta,None known,2021-08-05
P02227,Adya Kota,F,1987-04-05,38,B-,+91-00000-31439,Thiruvananthapuram,None known,2022-09-08
P02228,Odika Verma,F,1935-05-31,90,AB+,+91-00000-71156,Kottayam,None known,2021-08-09
P02229,Tanveer Sandal,M,1989-11-25,35,A+,+91-00000-53723,Thiruvananthapuram,None known,2022-10-14
P02230,Yoshita Pillay,F,1985-01-12,40,O-,+91-00000-48669,Kanyakumari,None known,2023-07-19
P02232,Yatan Kulkarni,M,1967-09-22,57,A-,+91-00000-12166,Pathanamthitta,None known,2022-04-14
P02233,Manthan Sanghvi,M,1995-06-08,30,AB+,+91-00000-99645,Kottayam,None known,2021-08-13
P02234,Wriddhish Brar,M,1991-05-04,34,O-,+91-00000-99012,Kollam,None known,2022-04-28
P02235,Peter Dugal,M,1986-08-21,38,AB+,+91-00000-83756,Pathanamthitta,None known,2022-11-02
P02236,Daniel Rana,M,1936-05-20,89,B+,+91-00000-95362,Thiruvananthapuram,None known,2023-02-27
P02237,Janya Datta,F,1975-12-31,49,B+,+91-00000-81973,Pathanamthitta,Penicillin,2022-09-02
P02238,Advik Deshpande,M,1970-05-17,55,AB+,+91-00000-11027,Kottayam,None known,2023-02-23
P02239,Nidhi Pillai,F,1995-11-11,29,B-,+91-00000-63082,Kanyakumari,None known,2023-08-19
P02240,Abeer Tandon,M,1984-11-01,40,B+,+91-00000-50554,Pathanamthitta,None known,2022-05-24
P02241,Harinakshi Bath,F,1999-10-07,25,B-,+91-00000-47996,Pathanamthitta,None known,2023-08-01
P02243,Umang Kaul,M,2016-06-12,9,B-,+91-00000-51514,Kollam,Sulfa drugs,2023-11-21
P02245,Jackson Shukla,M,2005-07-28,19,AB-,+91-00000-46015,Kanyakumari,None known,2022-09-30
P02246,Abhiram Goyal,M,2016-04-07,9,O-,+91-00000-69465,Thiruvananthapuram,None known,2021-11-05
P02247,George Kapur,M,1943-06-30,82,O+,+91-00000-71102,Kanyakumari,None known,2022-02-23
P02248,Bhavna Guha,F,2015-06-16,10,B-,+91-00000-69748,Pathanamthitta,None known,2023-02-13
P02249,Mitali Vohra,F,1985-04-11,40,AB-,+91-00000-56601,Kollam,None known,2023-10-21
P02250,Yachana Sharma,F,1974-06-15,51,A+,+91-00000-31720,Kottayam,None known,2023-01-19
P02252,Tripti Shenoy,F,1994-09-18,30,A-,+91-00000-71547,Thiruvananthapuram,None known,2023-09-15
P02253,Zinal Pau,F,1968-04-22,57,AB+,+91-00000-43419,Kottayam,None known,2022-12-26
P02254,Irya Chacko,F,2015-03-29,10,B-,+91-00000-63137,Kottayam,None known,2023-07-15
P02255,Jatin Chaudry,M,2018-01-25,7,A-,+91-00000-73883,Pathanamthitta,None known,2022-08-16
P02256,Bhavya Mani,F,2004-07-21,21,O+,+91-00000-12503,Kollam,None known,2023-03-18
P02257,Jeet Dora,M,1978-09-19,46,O-,+91-00000-22467,Pathanamthitta,None known,2023-04-20
P02258,Urmi Pandit,F,1951-04-20,74,A-,+91-00000-96727,Kanyakumari,None known,2023-01-30
P02259,Tanish Khatri,M,1936-05-21,89,A-,+91-00000-31428,Kanyakumari,None known,2022-11-08
P02261,Aarush Devi,M,2000-12-07,24,O-,+91-00000-77366,Kottayam,None known,2022-07-28
P02262,Odika Sibal,F,1956-02-23,69,O+,+91-00000-46400,Thiruvananthapuram,None known,2021-12-31
P02263,Nirja Toor,F,1993-10-11,31,O-,+91-00000-90457,Thiruvananthapuram,None known,2023-05-30
P02266,Samar Sen,M,1944-02-27,81,A+,+91-00000-82461,Kanyakumari,None known,2021-12-19
P02267,Udant Varty,M,2010-09-20,14,B+,+91-00000-37503,Kollam,None known,2023-09-10
P02268,Lucky Murthy,M,1959-09-21,65,O-,+91-00000-19643,Alappuzha,None known,2023-05-13
P02269,Ishita Loyal,F,2015-11-18,9,O-,+91-00000-49851,Pathanamthitta,None known,2021-11-10
P02270,Sathvik Kaul,M,1954-07-19,71,AB+,+91-00000-33506,Kanyakumari,None known,2023-02-04
P02271,Yoshita Sanghvi,F,1964-10-27,60,AB-,+91-00000-24210,Kanyakumari,NSAIDs,2023-05-07
P02272,Rajata Mand,F,1983-08-02,41,AB+,+91-00000-83794,Pathanamthitta,None known,2021-11-28
P02273,Aashi Mall,F,1996-10-29,28,A-,+91-00000-78665,Kottayam,Sulfa drugs,2023-12-21
P02274,Wazir Yohannan,M,2018-01-27,7,AB-,+91-00000-66693,Kanyakumari,None known,2022-09-26
P02275,Ekapad Borde,M,2023-04-30,2,A+,+91-00000-30096,Kollam,None known,2023-09-22
P02276,Brinda Mammen,F,1944-02-16,81,AB+,+91-00000-45200,Thiruvananthapuram,None known,2022-01-18
P02277,Aditya Dubey,M,2019-08-24,5,B-,+91-00000-96636,Kottayam,Penicillin,2022-02-14
P02278,Bhavya Misra,F,1977-01-02,48,O-,+91-00000-74350,Kollam,Penicillin,2023-07-10
P02280,Hemal Thaman,F,1951-10-06,73,B-,+91-00000-68377,Thiruvananthapuram,None known,2023-03-29
P02281,Champak Radhakrishnan,M,1974-04-28,51,AB-,+91-00000-22495,Alappuzha,None known,2023-04-14
P02282,Jeevika Tandon,F,1978-06-23,47,AB-,+91-00000-18419,Kanyakumari,None known,2022-05-19
P02283,Ojas Mann,M,2023-10-12,1,O-,+91-00000-99128,Thiruvananthapuram,Sulfa drugs,2022-03-22
P02284,Ekta Seth,F,2013-02-07,12,O+,+91-00000-64768,Pathanamthitta,None known,2023-10-23
P02285,Kabir Bhargava,M,1991-08-23,33,AB-,+91-00000-13863,Thiruvananthapuram,None known,2023-07-28
P02286,Shaurya Srinivasan,M,2016-03-05,9,O-,+91-00000-70038,Kollam,NSAIDs,2023-09-01
P02287,Ranveer Biswas,M,2007-05-23,18,A+,+91-00000-39860,Kollam,None known,2022-01-11
P02288,Hemangini Vig,F,1974-11-10,50,AB+,+91-00000-91581,Kollam,Sulfa drugs,2023-10-16
P02289,Madhav Bhatt,M,1983-02-05,42,B-,+91-00000-39178,Thiruvananthapuram,NSAIDs,2022-09-29
P02290,Raksha Talwar,F,1944-01-21,81,AB-,+91-00000-13571,Kollam,None known,2022-11-13
P02291,Arin Oommen,M,1940-01-16,85,AB+,+91-00000-26234,Kanyakumari,None known,2023-07-02
P02292,Vivaan Karnik,M,1943-07-16,82,AB-,+91-00000-81883,Thiruvananthapuram,None known,2023-07-23
P02293,Harshil Vasa,M,1994-04-02,31,A+,+91-00000-29248,Thiruvananthapuram,None known,2023-09-16
P02294,Ekanta Loke,F,1955-09-19,69,A+,+91-00000-33548,Thiruvananthapuram,None known,2023-05-19
P02295,Joshua Singhal,M,1950-03-26,75,O-,+91-00000-48656,Pathanamthitta,None known,2023-11-10
P02296,Kavya Shukla,F,2019-06-16,6,AB+,+91-00000-17961,Pathanamthitta,None known,2022-12-20
P02297,Anya Pandey,F,1951-10-28,73,A-,+91-00000-66120,Pathanamthitta,None known,2021-10-24
P02298,Ubika Dixit,F,1993-09-06,31,AB+,+91-00000-85969,Kollam,Sulfa drugs,2023-07-30
P02299,Lajita Halder,F,1953-01-30,72,AB-,+91-00000-63620,Kollam,None known,2023-08-17
P02300,Daniel Ramachandran,M,1967-10-02,57,AB-,+91-00000-30777,Kanyakumari,None known,2022-11-16
P02301,Amara Vohra,F,2004-01-15,21,A+,+91-00000-33418,Alappuzha,None known,2023-02-05
P02302,Utkarsh Rau,M,1968-05-13,57,O-,+91-00000-21892,Thiruvananthapuram,None known,2021-12-14
P02303,Ekaraj Prasad,M,1940-11-25,84,A-,+91-00000-93569,Kollam,Sulfa drugs,2023-01-08
P02304,Omisha Mangat,F,1952-08-22,72,B+,+91-00000-55099,Alappuzha,None known,2022-04-27
P02305,Priya Kohli,F,1966-01-11,59,A+,+91-00000-22352,Pathanamthitta,Sulfa drugs,2022-06-01
P02306,Guneet Sant,M,2018-06-25,7,O-,+91-00000-34236,Pathanamthitta,NSAIDs,2023-04-08
P02307,Suhani Gokhale,F,1997-09-06,27,A-,+91-00000-32541,Pathanamthitta,None known,2023-11-10
P02309,Faras Mitra,M,1935-08-03,90,AB-,+91-00000-17771,Kanyakumari,None known,2023-12-18
P02310,Reyansh Pillay,M,2020-05-14,5,O+,+91-00000-62910,Kanyakumari,None known,2023-06-26
P02311,Saanvi Korpal,F,1935-10-03,89,AB-,+91-00000-91442,Kottayam,Penicillin,2021-11-22
P02312,Oviya Mitter,F,2023-10-29,1,B-,+91-00000-34859,Pathanamthitta,None known,2023-11-19
P02314,Gaurika Dugar,F,1979-05-21,46,AB+,+91-00000-46571,Alappuzha,None known,2021-12-09
P02315,Ryan Chander,M,1987-08-26,37,O+,+91-00000-32191,Kottayam,None known,2021-12-17
P02316,Mohini Pandya,F,1991-08-13,33,AB+,+91-00000-89623,Kanyakumari,None known,2022-02-14
P02317,Kevin Goda,M,1941-04-22,84,A-,+91-00000-37591,Kanyakumari,None known,2023-01-10
P02318,Tanish Jhaveri,M,2024-04-21,1,A+,+91-00000-53869,Pathanamthitta,None known,2023-05-11
P02319,Charles Tandon,M,1952-10-29,72,O+,+91-00000-32901,Kottayam,None known,2023-03-13
P02320,Krishna Rajagopalan,M,2002-01-23,23,B-,+91-00000-99614,Alappuzha,Penicillin,2023-04-20
P02321,Varsha Sachdev,F,2005-11-23,19,O+,+91-00000-23677,Kollam,None known,2022-08-13
P02322,Hamsini Shanker,F,1999-02-20,26,O-,+91-00000-50937,Alappuzha,None known,2023-12-25
P02323,Bhavya Bala,F,1955-10-05,69,AB+,+91-00000-88592,Alappuzha,NSAIDs,2021-11-12
P02324,Qabil Narang,M,1973-10-16,51,A-,+91-00000-16179,Kottayam,None known,2023-01-25
P02325,Sudiksha Parsa,F,1935-08-26,89,O+,+91-00000-75993,Alappuzha,None known,2021-08-26
P02327,Baljiwan Sami,M,2015-07-10,10,B+,+91-00000-36605,Pathanamthitta,None known,2022-10-15
P02328,Aashi Sundaram,F,1983-12-15,41,B+,+91-00000-97374,Kollam,None known,2023-09-26
P02329,Atharv Buch,M,1942-04-01,83,O-,+91-00000-41099,Kanyakumari,NSAIDs,2022-10-26
P02330,Falak Nagar,F,2000-05-08,25,B+,+91-00000-18252,Pathanamthitta,None known,2021-09-04
P02331,Jacob Dugal,M,2007-12-15,17,B+,+91-00000-39255,Alappuzha,NSAIDs,2021-11-18
P02332,Samuel Sen,M,1950-01-21,75,B-,+91-00000-72767,Kollam,None known,2023-04-07
P02333,Keya Magar,F,2007-03-31,18,B+,+91-00000-52030,Kottayam,None known,2023-06-10
P02336,Keya Bhat,F,1982-11-28,42,B-,+91-00000-90213,Kanyakumari,None known,2023-02-21
P02337,Chaaya Narayan,F,1963-10-31,61,AB-,+91-00000-87466,Thiruvananthapuram,None known,2023-07-22
P02338,Yachana Chanda,F,1981-01-29,44,B-,+91-00000-67984,Kottayam,None known,2022-10-09
P02339,Arya Goel,F,1974-02-09,51,A-,+91-00000-59299,Kanyakumari,None known,2022-05-16
P02340,Raghav Modi,M,1939-09-09,85,O+,+91-00000-24955,Thiruvananthapuram,None known,2022-04-13
P02343,Deepa Pradhan,F,1967-08-12,57,A-,+91-00000-26167,Kollam,None known,2022-12-08
P02344,Amara Vohra,F,2005-08-02,19,O-,+91-00000-10061,Kollam,None known,2022-12-02
P02345,Gauri Chandra,F,2011-01-22,14,A+,+91-00000-47298,Thiruvananthapuram,None known,2022-02-19
P02346,Watika Buch,F,2001-10-17,23,O+,+91-00000-50907,Thiruvananthapuram,None known,2022-01-24
P02347,Zinal Dey,F,2016-01-26,9,O-,+91-00000-31182,Thiruvananthapuram,None known,2021-09-14
P02349,Manthan Sarin,M,1998-02-22,27,B+,+91-00000-73449,Kanyakumari,None known,2023-06-05
P02350,Zehaan Virk,M,1969-03-12,56,B-,+91-00000-63027,Kottayam,None known,2021-11-06
P02351,Mohammed Prasad,M,2016-01-06,9,B+,+91-00000-27450,Kanyakumari,None known,2022-10-26
P02352,Lohit Bala,M,1971-02-28,54,AB+,+91-00000-28379,Kottayam,NSAIDs,2022-03-07
P02353,Anay Ramachandran,M,1999-12-30,25,AB+,+91-00000-84873,Alappuzha,None known,2022-08-07
P02354,Inaya Cherian,F,1937-08-14,87,O-,+91-00000-58514,Alappuzha,None known,2023-03-07
P02355,Tarak Wable,M,2008-07-28,16,AB-,+91-00000-88513,Pathanamthitta,None known,2022-12-25
P02356,Faras Borde,M,1954-02-10,71,O-,+91-00000-33815,Kollam,None known,2022-03-24
P02357,Vasatika Lall,F,1940-11-23,84,AB-,+91-00000-27957,Pathanamthitta,None known,2022-03-04
P02358,Tejas Deshmukh,M,1981-10-22,43,A+,+91-00000-76981,Pathanamthitta,None known,2022-04-22
P02359,Lila Divan,F,2016-09-23,8,AB+,+91-00000-73619,Kollam,None known,2022-12-10
P02360,Waida Chawla,F,1963-01-08,62,A-,+91-00000-96172,Pathanamthitta,None known,2023-07-06
P02361,Harinakshi Shan,F,1962-02-11,63,O-,+91-00000-79978,Kanyakumari,Sulfa drugs,2023-09-15
P02363,Ansh Amble,M,1971-01-02,54,B-,+91-00000-87939,Kollam,None known,2023-08-15
P02364,Nandini Chowdhury,F,2002-12-27,22,O+,+91-00000-54373,Thiruvananthapuram,None known,2023-05-02
P02365,Robert Srinivas,M,1937-04-25,88,O-,+91-00000-41996,Kollam,None known,2022-08-02
P02366,Neel Mangat,M,1985-01-16,40,O+,+91-00000-78652,Kollam,None known,2022-07-31
P02367,Jagdish Mutti,M,1984-12-28,40,B+,+91-00000-61538,Kollam,None known,2023-08-10
P02368,Yoshita Mannan,F,2002-06-01,23,A+,+91-00000-92609,Pathanamthitta,Penicillin,2023-01-24
P02369,Pallavi Ramanathan,F,1955-12-23,69,A+,+91-00000-11848,Pathanamthitta,None known,2023-01-25
P02372,Andrew Raju,M,1984-09-05,40,B-,+91-00000-53649,Pathanamthitta,None known,2023-04-03
P02373,Nidra Bawa,F,1990-04-24,35,O-,+91-00000-29554,Kollam,None known,2023-03-04
P02374,Damini Sarin,F,2000-02-25,25,O+,+91-00000-86721,Kanyakumari,None known,2023-06-26
P02375,Tara Chatterjee,F,2000-05-09,25,O+,+91-00000-25765,Kanyakumari,None known,2023-06-20
P02376,Onveer Sengupta,M,1956-09-15,68,B-,+91-00000-57776,Pathanamthitta,None known,2022-10-31
P02377,Ishita Suri,F,1983-04-30,42,A+,+91-00000-22498,Pathanamthitta,Penicillin,2022-02-10
P02379,Jackson Vora,M,1962-05-19,63,B-,+91-00000-88842,Kottayam,None known,2023-01-24
P02380,Ayaan Kibe,M,1969-07-07,56,B-,+91-00000-41783,Pathanamthitta,NSAIDs,2022-09-16
P02381,Fiyaz Soni,M,1990-08-16,34,B+,+91-00000-61021,Kollam,None known,2022-11-13
P02382,Noah Varkey,M,1971-04-25,54,O+,+91-00000-12121,Kottayam,None known,2022-11-15
P02383,Rishi Rai,M,2017-07-24,7,AB+,+91-00000-68076,Kollam,None known,2023-07-12
P02384,Siya Sengupta,F,2008-06-30,17,O+,+91-00000-25765,Kollam,None known,2023-03-24
P02385,Amara Sidhu,F,2011-04-04,14,A-,+91-00000-13549,Kollam,None known,2022-10-16
P02386,Hamsini Madan,F,2009-04-06,16,AB+,+91-00000-56041,Kanyakumari,None known,2022-07-21
P02387,Falguni Butala,F,1954-02-23,71,O+,+91-00000-55541,Thiruvananthapuram,Sulfa drugs,2023-11-30
P02388,Zehaan Shah,M,1967-03-02,58,AB+,+91-00000-36283,Alappuzha,None known,2023-01-03
P02389,Balveer Bath,M,1986-05-21,39,A-,+91-00000-98861,Pathanamthitta,None known,2022-02-12
P02390,Xalak Mani,F,1995-10-31,29,AB+,+91-00000-31341,Pathanamthitta,None known,2022-09-25
P02391,Yashodhara Bava,F,2014-08-07,10,AB+,+91-00000-32626,Pathanamthitta,None known,2022-10-06
P02392,Tripti Gola,F,1959-01-05,66,O+,+91-00000-71170,Kanyakumari,None known,2021-12-10
P02393,Nakul Hora,M,1942-02-06,83,B+,+91-00000-75060,Kottayam,None known,2023-12-26
P02394,Yahvi Varty,F,1949-03-26,76,O-,+91-00000-44320,Kottayam,None known,2021-09-07
P02396,Gautam Solanki,M,2009-11-26,15,A+,+91-00000-95513,Kollam,None known,2023-12-27
P02397,Darika Gopal,F,1991-05-27,34,B-,+91-00000-97120,Kanyakumari,None known,2021-08-29
P02398,Yashoda Gera,F,1936-07-27,89,B+,+91-00000-63637,Kottayam,None known,2021-12-28
P02399,Veda Kade,F,1981-10-07,43,A+,+91-00000-46229,Kottayam,Sulfa drugs,2023-12-28
P02400,Gayathri Shankar,F,1985-04-04,40,AB-,+91-00000-92130,Alappuzha,None known,2023-08-08
P02401,Lila Tak,F,1990-12-01,34,O+,+91-00000-18313,Kottayam,None known,2021-11-06
P02402,Girik Ganesh,M,1958-11-03,66,AB-,+91-00000-84287,Kanyakumari,None known,2023-10-11
P02404,Bhanumati Kakar,F,1973-03-20,52,O-,+91-00000-55377,Pathanamthitta,None known,2023-08-17
P02405,Jeremiah Sampath,M,1957-03-16,68,AB+,+91-00000-95921,Kottayam,None known,2022-06-16
P02406,Vasatika Dhar,F,1979-11-30,45,A+,+91-00000-89805,Pathanamthitta,None known,2022-11-30
P02407,Darpan Shukla,M,1979-04-26,46,A+,+91-00000-94629,Thiruvananthapuram,None known,2022-02-13
P02408,Nikita Boase,F,1993-03-29,32,A-,+91-00000-30123,Kollam,None known,2022-10-30
P02409,Lucky Chada,M,1981-09-09,43,O+,+91-00000-77554,Pathanamthitta,None known,2022-08-23
P02410,Ayaan Dada,M,1955-11-24,69,A+,+91-00000-33689,Kollam,None known,2022-01-14
P02411,Hemani Mishra,F,1975-11-21,49,B+,+91-00000-56232,Kanyakumari,None known,2022-09-21
P02413,Hemangini Borde,F,1975-04-29,50,AB+,+91-00000-19794,Alappuzha,Sulfa drugs,2023-09-21
P02414,Qabil Choudhry,M,1936-12-04,88,B+,+91-00000-82644,Kanyakumari,NSAIDs,2021-09-06
P02415,Anjali Raj,F,1938-07-18,87,O-,+91-00000-86532,Alappuzha,None known,2022-03-01
P02416,Samuel Das,M,1942-02-11,83,O-,+91-00000-59911,Thiruvananthapuram,None known,2022-05-27
P02417,Jyoti Kuruvilla,F,2006-06-13,19,B+,+91-00000-55517,Alappuzha,None known,2023-05-20
P02418,Chaitaly Rajan,F,2020-11-08,4,O-,+91-00000-57027,Kanyakumari,NSAIDs,2021-08-26
P02419,Ishanvi Ramakrishnan,F,1972-01-28,53,O-,+91-00000-23356,Kollam,None known,2022-12-23
P02420,Wridesh Anne,M,1979-01-26,46,AB-,+91-00000-56582,Kollam,None known,2022-11-20
P02421,Harini Nagarajan,F,1962-05-21,63,B+,+91-00000-56779,Kollam,None known,2022-03-13
P02422,Anita Dyal,F,1962-12-16,62,AB-,+91-00000-97913,Kottayam,None known,2022-04-28
P02423,Riya Kapoor,F,1990-12-08,34,O-,+91-00000-36485,Kollam,None known,2022-11-15
P02425,Gauri Bose,F,1982-02-26,43,O+,+91-00000-91319,Pathanamthitta,Penicillin,2023-05-23
P02426,Veer Buch,M,1941-11-23,83,O+,+91-00000-11429,Kottayam,None known,2023-11-02
P02427,Lavanya Dash,F,1977-11-02,47,AB+,+91-00000-25409,Kanyakumari,None known,2022-03-24
P02428,Chaman Sekhon,F,1994-08-26,30,O-,+91-00000-34672,Alappuzha,None known,2021-10-03
P02429,Zayan Sidhu,M,1969-04-08,56,AB+,+91-00000-67456,Kanyakumari,None known,2022-09-30
P02430,Aarush Shenoy,M,1945-01-06,80,AB+,+91-00000-14242,Kollam,None known,2023-01-26
P02432,Gaurav Natt,M,1950-08-23,74,O-,+91-00000-91153,Alappuzha,None known,2022-08-28
P02435,Yug Pal,M,2007-07-09,18,O-,+91-00000-50534,Alappuzha,None known,2021-08-02
P02436,Akshay Mishra,M,2023-08-20,1,AB-,+91-00000-62121,Alappuzha,None known,2022-10-10
P02437,Vihaan Vora,M,2018-01-25,7,O-,+91-00000-96365,Kottayam,None known,2023-12-28
P02438,Imaran Ganguly,M,2007-01-02,18,AB+,+91-00000-11334,Thiruvananthapuram,Penicillin,2022-05-06
P02439,Theodore Kalita,M,1951-08-28,73,O+,+91-00000-27096,Pathanamthitta,None known,2022-11-21
P02440,Laksh Patil,M,1994-09-30,30,A+,+91-00000-28627,Kottayam,None known,2021-12-25
P02441,Mitali Butala,F,1956-08-08,68,O+,+91-00000-96244,Kanyakumari,NSAIDs,2022-08-31
P02442,Naveen Bhakta,M,1971-08-07,53,A+,+91-00000-79708,Kottayam,Penicillin,2022-04-01
P02443,Ekiya Bhatnagar,F,1959-01-15,66,A-,+91-00000-27558,Thiruvananthapuram,None known,2021-10-08
P02444,Meera Shere,F,2000-01-17,25,O-,+91-00000-52146,Pathanamthitta,None known,2022-11-20
P02445,Amaira Mishra,F,2006-08-05,18,B+,+91-00000-67411,Kollam,Sulfa drugs,2022-05-19
P02446,William Jayaraman,M,1957-10-05,67,A-,+91-00000-10680,Kollam,None known,2023-04-17
P02447,Advika Parmer,F,2019-05-04,6,B-,+91-00000-98366,Pathanamthitta,Sulfa drugs,2021-12-01
P02448,Varenya Sarin,F,2010-08-08,14,B+,+91-00000-16836,Kollam,None known,2023-07-15
P02449,Arya Kala,F,1986-11-24,38,A-,+91-00000-46443,Pathanamthitta,None known,2023-10-17
P02450,Amrita Zachariah,F,2003-05-11,22,B+,+91-00000-63208,Kottayam,None known,2021-12-19
P02452,Theodore Virk,M,1958-07-21,67,B-,+91-00000-22078,Kanyakumari,None known,2021-11-23
P02453,Caleb Modi,M,1965-08-13,59,B-,+91-00000-91145,Pathanamthitta,None known,2023-10-02
P02454,Eesha Kapoor,F,2017-07-29,7,AB-,+91-00000-51484,Kottayam,None known,2022-09-18
P02455,Faras Subramanian,M,1966-04-28,59,O+,+91-00000-88797,Kottayam,Penicillin,2022-09-04
P02456,Karan Peri,M,1942-07-13,83,AB+,+91-00000-55346,Kanyakumari,Sulfa drugs,2023-09-26
P02457,Wakeeta Majumdar,F,1980-08-30,44,AB-,+91-00000-87518,Kottayam,None known,2021-11-24
P02458,Inaya Saran,F,1966-10-06,58,B-,+91-00000-66328,Kollam,None known,2021-12-30
P02460,Harsh Tiwari,M,1973-06-10,52,B+,+91-00000-16734,Kanyakumari,Penicillin,2021-10-03
P02461,Raghav Wali,M,1997-05-05,28,AB+,+91-00000-53692,Alappuzha,Sulfa drugs,2023-03-23
P02462,Mason Nagar,M,1989-12-25,35,AB+,+91-00000-77910,Pathanamthitta,None known,2023-05-17
P02463,Praneel Agrawal,M,1943-05-20,82,A+,+91-00000-20584,Kanyakumari,Penicillin,2021-10-01
P02464,Lila Pandey,F,1965-05-06,60,O-,+91-00000-86141,Thiruvananthapuram,None known,2023-02-22
P02465,Ekapad Dave,M,1949-11-10,75,B+,+91-00000-53133,Alappuzha,None known,2023-07-08
P02466,Gaurang Chandra,M,1957-02-19,68,B-,+91-00000-10292,Kollam,None known,2023-08-24
P02469,Ridhi Nagi,F,1983-02-18,42,O-,+91-00000-21702,Kollam,None known,2021-11-25
P02470,Ati Kibe,F,1985-10-26,39,B+,+91-00000-95355,Kottayam,None known,2021-09-06
P02472,Ojasvi Misra,F,2018-06-19,7,O-,+91-00000-31688,Thiruvananthapuram,Penicillin,2022-06-03
P02473,Aarna Sankar,F,2018-07-04,7,A-,+91-00000-63794,Thiruvananthapuram,Sulfa drugs,2023-08-19
P02474,Nikita Rai,F,2012-11-16,12,O+,+91-00000-66545,Kanyakumari,None known,2023-09-01
P02475,Hitesh Sethi,M,2000-05-25,25,B+,+91-00000-78445,Pathanamthitta,None known,2023-06-21
P02476,Banjeet Misra,M,2021-12-15,3,A-,+91-00000-42297,Kollam,None known,2021-12-14
P02477,Warjas Bhandari,M,1999-10-30,25,O-,+91-00000-65259,Kottayam,None known,2023-09-19
P02478,Meghana Bakshi,F,1940-07-14,85,AB+,+91-00000-34309,Alappuzha,None known,2022-08-14
P02479,Omkaar Chandran,M,2024-03-10,1,AB+,+91-00000-31624,Kottayam,None known,2022-07-07
P02480,Balveer Brar,M,1970-05-18,55,AB+,+91-00000-74760,Kollam,NSAIDs,2023-04-12
P02481,Chameli Shroff,F,1975-06-17,50,AB-,+91-00000-50199,Alappuzha,None known,2022-06-27
P02482,Frado Wali,M,1971-05-24,54,O-,+91-00000-51582,Kottayam,None known,2022-04-14
P02484,Mugdha Das,F,1946-11-23,78,B-,+91-00000-71325,Kollam,None known,2022-07-22
P02485,Zehaan Bora,M,1970-07-26,55,O-,+91-00000-14540,Kanyakumari,None known,2021-11-25
P02486,Hritik Sood,M,1975-01-03,50,AB+,+91-00000-42556,Alappuzha,None known,2022-09-11
P02487,Harinakshi Dhar,F,1968-02-24,57,B+,+91-00000-68716,Kottayam,None known,2022-02-07
P02488,Chaitaly Ramanathan,F,2001-09-26,23,B+,+91-00000-98541,Pathanamthitta,None known,2021-08-06
P02489,Upma Ratta,F,1971-04-26,54,B+,+91-00000-20542,Alappuzha,None known,2022-06-05
P02490,Maanas Bava,M,1951-02-16,74,O+,+91-00000-31684,Pathanamthitta,None known,2023-09-06
P02491,Sudiksha Dada,F,1960-01-07,65,B+,+91-00000-62217,Kollam,None known,2023-11-05
P02492,Darpan Bora,M,1980-05-03,45,B+,+91-00000-52776,Alappuzha,NSAIDs,2021-10-28
P02493,Charan Som,M,2016-10-31,8,A+,+91-00000-83723,Thiruvananthapuram,None known,2023-08-28
P02494,Shivansh Kanda,M,1975-07-06,50,A+,+91-00000-18262,Thiruvananthapuram,None known,2023-10-21
P02495,Jagat Kalita,M,1940-02-16,85,B+,+91-00000-66651,Kollam,None known,2021-12-27
P02496,Ryan Divan,M,1983-11-14,41,AB-,+91-00000-55834,Kottayam,None known,2023-03-28
P02497,Parth Dey,M,1968-03-15,57,B-,+91-00000-10926,Kanyakumari,None known,2023-11-03
P02498,Ria Arora,F,1974-05-30,51,B-,+91-00000-83904,Alappuzha,None known,2022-01-11
P02499,Wriddhish Borra,M,1993-07-23,32,AB-,+91-00000-34390,Thiruvananthapuram,None known,2023-09-29
P02500,Chaman Sampath,F,1940-01-16,85,B-,+91-00000-40399,Pathanamthitta,None known,2021-09-04
P90001,Arun Pillai,M,1991-02-14,34,B+,+91-00000-90001,Thiruvananthapuram,None known,2025-03-03
P90002,Leela Menon,F,1969-05-09,56,O+,+91-00000-90002,Kollam,None known,2025-01-27
P90003,Anjali Nair,F,1998-08-21,26,A+,+91-00000-90003,Alappuzha,None known,2024-06-02
P90004,Joseph Varghese,M,1964-03-30,61,AB+,+91-00000-90004,Kottayam,Sulfa drugs,2025-01-20
P90005,Saraswathi Amma,F,1957-01-12,68,O-,+91-00000-90005,Thiruvananthapuram,None known,2024-11-04
```
