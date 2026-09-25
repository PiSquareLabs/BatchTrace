# Bad Batch Tracer

Every month, India's drug regulator (CDSCO) publishes lists of drug batches that failed quality testing: "Not of Standard Quality" (NSQ) and spurious drugs. Hospitals rarely check these lists against what they have already dispensed. **Bad Batch Tracer** reads the monthly CDSCO alerts, extracts each failed batch, and matches it against a hospital's dispensing records. It also handles hand-typed and missing batch numbers. It then lists exposed patients and flags those whose labs suggest harm, for clinical follow-up.

Built for the Snowflake CoCo CLI Hackathon 2026 (GCC Edition), Track 4: Patient 360 & Clinical/Regulatory Copilot.

This repo currently contains the **data layer**:
- real public CDSCO alerts, as PDFs and portal JSON;
- a drug master subset;
- regulatory reference documents;
- a baseline parse with a gold template for accuracy evaluation;
- a fully **synthetic** hospital with an answer key.

> **No real patient data is used.** See `docs/DATA_SOURCES.md` for provenance, licences and known gaps.

## Quick start

```bash
make install                        # creates .venv and installs pinned requirements
cp .env.example .env                # set CONTACT_EMAIL (sent in the polite User-Agent)
make fetch && make synth && make validate
```

The `make` targets:

| Target | What it does |
|---|---|
| `make fetch` | CDSCO alert PDFs, the CDSCO portal JSON, the drug master and the reference docs. Idempotent: files already present with a matching sha256 are skipped. |
| `make gold` | Baseline PDF parse, then the gold template (`make parse` runs the parse alone). |
| `make synth` | Synthetic hospital, seed 42, deterministic. |
| `make validate` | All checks. Writes `docs/validation_report.txt`. |

All the data is already committed, so `make validate` works straight after `make install`.

## Repo map

```
├── CLAUDE_CODE_DATA_PLAN.md       data acquisition plan (phases A–H)
├── Makefile, requirements.txt, .env.example
├── docs/
│   ├── DATA_SOURCES.md            sources, licences, coverage, known gaps
│   └── validation_report.txt      output of scripts/validate_data.py
├── data/
│   ├── manifest.csv               every fetched/derived file: URL, sha256, bytes, fetched_at, status, pages
│   ├── raw/cdsco_alerts/          central/ state/ spurious/ combined/ other/ PDFs (+ listing index)
│   ├── raw/cdsco_portal/          portal JSON per month + portal_nsq.csv (2025-07..2026-08) + backfill CSV
│   ├── raw/drug_master/           drug_master_subset.csv.gz (full upstream CSV is gitignored)
│   ├── reference/                 CDSCO recall guideline, guidance document, D&C Act+Rules, Rule 65 extract
│   ├── interim/                   nsq_baseline_parsed.csv (pdfplumber baseline, not the product)
│   ├── gold/                      nsq_2025-06_central_gold.csv (to be hand-verified)
│   └── synthetic/
│       ├── hospital/              patients, wards, encounters, products, stock_batches,
│       │                          prescriptions, dispensing, labs (Parquet + CSV)
│       └── ground_truth/          exposures answer key — evaluation only, NEVER load into app tables
├── scripts/                       common.py + one script per phase (fetch_*, parse_baseline,
│                                  build_gold_template, generate_synthetic_hospital, validate_data)
└── snowflake/README.md            load plan (after trial activation, 27 Sept)
```

`data/synthetic/ground_truth/` is the answer key used to score the matcher. Keep it out of every Snowflake schema the app can read.
