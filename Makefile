PY ?= .venv/bin/python

.PHONY: install fetch fetch-alerts fetch-portal fetch-drugs fetch-refs parse gold synth validate

install:
	python3 -m venv .venv
	$(PY) -m pip install -r requirements.txt

fetch: fetch-alerts fetch-portal fetch-drugs fetch-refs

fetch-alerts:
	$(PY) scripts/fetch_cdsco_alerts.py

fetch-portal:
	$(PY) scripts/fetch_cdsco_portal.py

fetch-drugs:
	$(PY) scripts/fetch_drug_master.py

fetch-refs:
	$(PY) scripts/fetch_reference_docs.py

parse:
	$(PY) scripts/parse_baseline.py

gold: parse
	$(PY) scripts/build_gold_template.py

synth:
	$(PY) scripts/generate_synthetic_hospital.py --seed 42

validate:
	$(PY) scripts/validate_data.py
