"""Shared helpers: polite HTTP session, sha256, manifest writer.

Rules enforced here (see CLAUDE_CODE_DATA_PLAN.md §0):
- custom User-Agent with a contact address (CONTACT_EMAIL in .env)
- >= 2 s between requests to cdsco hosts
- max 3 retries with exponential backoff
- TLS verification is never disabled
"""
from __future__ import annotations

import csv
import hashlib
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MANIFEST = DATA / "manifest.csv"
MANIFEST_FIELDS = [
    "source_url", "local_path", "sha256", "bytes", "fetched_at_utc",
    "http_status", "content_type", "pages", "notes",
]

load_dotenv(ROOT / ".env")
CONTACT = os.environ.get("CONTACT_EMAIL", "see-repo-README")
USER_AGENT = f"BadBatchTracer-Hackathon/0.1 (contact: {CONTACT})"

POLITE_HOSTS = ("cdsco.gov.in", "cdscoonline.gov.in")
POLITE_DELAY_S = 2.0
MAX_RETRIES = 3
TIMEOUT_S = 60

log = logging.getLogger("bbt")
if not log.handlers:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

_session: requests.Session | None = None
_last_hit: dict[str, float] = {}


def session() -> requests.Session:
    global _session
    if _session is None:
        s = requests.Session()
        s.headers.update({"User-Agent": USER_AGENT})
        _session = s
    return _session


def _is_polite_host(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in POLITE_HOSTS)


def polite_get(url: str, **kw) -> requests.Response:
    """GET with UA, per-host delay for cdsco, retries with exponential backoff.

    Raises on final failure. 4xx responses (other than 429) are not retried:
    a block is logged and returned to the caller, never worked around.
    """
    kw.setdefault("timeout", TIMEOUT_S)
    host = urlparse(url).hostname or ""
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        if _is_polite_host(url):
            wait = POLITE_DELAY_S - (time.monotonic() - _last_hit.get(host, 0.0))
            if wait > 0:
                time.sleep(wait)
        try:
            r = session().get(url, **kw)
            _last_hit[host] = time.monotonic()
            if r.status_code == 429 or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}", response=r)
            return r
        except requests.exceptions.SSLError:
            # Never silently disable verification — surface it (plan §0 rule 4).
            _last_hit[host] = time.monotonic()
            raise
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            _last_hit[host] = time.monotonic()
            last_exc = e
            if attempt < MAX_RETRIES:
                backoff = 2 ** (attempt + 1)
                log.warning("GET %s failed (%s); retry %d in %ds", url, e, attempt + 1, backoff)
                time.sleep(backoff)
    assert last_exc is not None
    raise last_exc


def sha256(path: Path | str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path | str) -> str:
    return Path(path).resolve().relative_to(ROOT).as_posix()


def load_manifest() -> dict[str, dict]:
    """Manifest rows keyed by local_path."""
    if not MANIFEST.exists():
        return {}
    with open(MANIFEST, newline="", encoding="utf-8") as f:
        return {r["local_path"]: r for r in csv.DictReader(f)}


def record_manifest(source_url: str, local_path: Path | str, http_status: int | str = "",
                    content_type: str = "", pages: int | str = "", notes: str = "") -> dict:
    """Upsert one row (keyed by local_path) and rewrite the manifest sorted by path."""
    p = Path(local_path)
    rows = load_manifest()
    row = {
        "source_url": source_url,
        "local_path": rel(p),
        "sha256": sha256(p),
        "bytes": p.stat().st_size,
        "fetched_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "http_status": http_status,
        "content_type": content_type,
        "pages": pages,
        "notes": notes,
    }
    rows[row["local_path"]] = row
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        w.writeheader()
        for k in sorted(rows):
            w.writerow({fld: rows[k].get(fld, "") for fld in MANIFEST_FIELDS})
    return row


def already_have(local_path: Path | str) -> bool:
    """Idempotency: file exists and its sha256 matches the manifest."""
    p = Path(local_path)
    if not p.exists():
        return False
    row = load_manifest().get(rel(p))
    return bool(row) and row["sha256"] == sha256(p)
