# Data sources

> **No real patient data is used anywhere in this repo.** The hospital side is 100% synthetic (Phase G).
> All CDSCO material is public data fetched politely: custom User-Agent with a contact address, at least 2 s between requests, at most 3 retries, TLS verification always on.
> Every downloaded file is recorded in `data/manifest.csv` with its URL, sha256, size, fetch time (UTC), HTTP status and page count.

## 1. CDSCO monthly alert PDFs (`data/raw/cdsco_alerts/`)

- **Source:** the listing pages at https://cdsco.gov.in/opencms/opencms/en/Alerts/ and `/en/Latest-Alerts/`, which were merged and de-duplicated by `num_id`. The index is saved to `alerts_index.csv` (300 rows).
- **How the files are fetched:** each `download_file_division.jsp?num_id=…` link returns a small HTML page containing an `<iframe src=…>` that points at the real PDF under `/opencms/resources/UploadCDSCOWeb/…`. The script resolves that iframe and downloads the PDF.
- **Selection:** titles matching `NSQ|Not of Standard|Not Standard|Drug Alert|Spurious|Revise`, released between 2024-01-01 and the fetch date, plus the "Samples declared NSQ 2017-2023" summary and the "NSQ Alert on New Link" notice. One title matched the regex only by accident ("…revised GST rate Structure") and was excluded. `alerts_selected.csv` records every selection and its fetch status.
- **Naming:** files are named `YYYY-MM` after the month the alert is **for**, not the release month.
  - From Aug 2024 to Dec 2024, CDSCO published "Drug Alert for the Month of …" alongside a separate "State Drug Alert". The non-state PDF is headed "A. CDSCO/Central Laboratories", so it is filed under `central/`.
  - From Dec 2023 to Mar 2024 there was no separate state list, so those PDFs are filed under `combined/`.
- **Terms:** Government of India public regulatory notices, published for stakeholder awareness. They are redistributed here unmodified, with their source URLs.
- **Fetched:** 25 Sept 2026. 52 PDFs, about 19 MB in total; the largest file is under 3 MB.

### Coverage
| Alert month | combined | central | state | spurious |
|---|---|---|---|---|
| 2023-12 | ✅ 12p | — | — | — |
| 2024-01 | ✅ 8p | — | — | — |
| 2024-02 | ✅ 12p | — | — | — |
| 2024-03 | ✅ 7p | — | — | — |
| 2024-04 | — | ✅ 11p | — | ✅ 3p |
| 2024-05 | — | ✅ 9p | ✅ 6p | — |
| 2024-06 | — | ✅ 6p | ✅ 9p | — |
| 2024-07 | — | ✅ 11p | ✅ 3p | — |
| 2024-08 | — | ✅ 8p | ✅ 3p | ✅ 2p |
| 2024-09 | — | ✅ 9p | ✅ 5p | ✅ 2p |
| 2024-10 | — | ✅ 9p | ✅ 9p | ✅ 2p |
| 2024-11 | — | ✅ 8p | ✅ 18p | ✅ 2p |
| 2024-12 | — | ✅ 9p | ✅ 18p | — |
| 2025-01 | — | ✅ 10p | ✅ 22p | — |
| 2025-02 | — | ✅ 6p | ✅ 16p | ✅ 1p |
| 2025-03 | — | ✅ 9p | ✅ 9p | ✅ 1p |
| 2025-04 | — | ✅ 7p | ✅ 22p | ✅ 1p |
| 2025-05 | — | ✅ 7p | ✅ 19p | ✅ 2p |
| 2025-06 | — | ✅ 6p | ✅ 15p | ✅ 2p |
| 2025-07 | — | — | — | — |

**other/** (revised lists, multi-year summary, notices):
- `availability_of_not_standard_quality_nsq_alert_on_new_link_in_cdsco_website.pdf` (1p)
- `drug_alert_for_the_month_of_revised_dec_2023.pdf` (1p)
- `drug_alert_for_the_month_of_revised_jan_2024.pdf` (1p)
- `drug_alert_for_the_month_of_revised_march_2023.pdf` (1p)
- `list_of_drugs_medical_devices_vaccine_and_cosmetics_declared_as_not_of_standard_quality_sp.pdf` (1p)
- `revise_list_drug_alert_january_2025.pdf` (1p)
- `revise_list_drug_alert_may_2025.pdf` (1p)
- `revise_list_drug_alert_november_2024.pdf` (1p)
- `samples_declared_nsq_2017_2023.pdf` (5p)

### Known gaps
- **July 2025 is missing from the old site.** From Aug 2025, lists are published only on the new portal (see the `other/` notice). July 2025 is checked on the portal in Phase C.
- **Spurious lists are missing for 2024-05, 2024-06, 2024-07, 2024-12 and 2025-01.** For 2024-01 to 2024-03, spurious items are inside the combined list. For Jan 2025, the "January 2025 Revised" file in `other/` covers NSQ, spurious, adulterated and misbranded items.
- **No separate state list before May 2024.**
- Many states don't submit state NSQ data every month, so state lists vary a lot in size (3 to 22 pages).
- Revised lists in `other/` correct earlier months. The baseline parser does not apply them yet.
