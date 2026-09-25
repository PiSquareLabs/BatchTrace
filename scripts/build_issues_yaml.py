"""Generate issues/issues.yaml from Section 8 of CLAUDE_CODE_TEAM_PLAN.md.

Each issue body follows the plan's template:
  ## Context / ## Tasks / ## Snowflake features / ## CoCo CLI / ## Acceptance criteria / ## Depends on
Dependencies are written as plan ids (#n); the creator rewrites them to real issue numbers.
YAML is emitted by hand (JSON-quoted scalars + literal block bodies) to avoid a PyYAML dependency.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "CLAUDE_CODE_TEAM_PLAN.md"
OUT = ROOT / "issues" / "issues.yaml"

MILESTONES = {  # title -> due (IST date); due_on is 23:59 IST = 18:29:59Z
    "M0 · Pre-activation": "2026-09-26",
    "M1 · Snowflake foundation": "2026-09-27",
    "M2 · Core pipelines": "2026-09-30",
    "M3 · Intelligence & App": "2026-10-02",
    "M4 · Ship": "2026-10-04",
}
ROLES = {"A": "A: Data & Pipeline", "B": "B: Intelligence", "C": "C: Platform & Product"}
FIELD_KEYS = {"Tasks": "tasks", "CoCo CLI": "coco", "Acceptance": "acceptance", "Depends on": "depends",
              "Assignees": "assignees", "Body": "body"}
# Snowflake features per plan item (hand-mapped from §5 so every issue names what it shows)
FEATURES = {
    1: [], 2: [], 3: [],
    4: ["CoCo CLI setup", "snow CLI connections (key-pair)"],
    5: ["Streamlit in Snowflake (screen design)", "Cortex Agents (chat screen)"],
    6: ["Warehouses (X-Small, 60 s auto-suspend)", "Resource monitors", "RBAC (roles, users, grants)",
        "SNOWFLAKE.CORTEX_USER / COPILOT_USER database roles", "Cross-region Cortex inference", "CoCo CLI"],
    7: ["Databases & schemas", "Internal stages with SNOWFLAKE_SSE encryption", "Directory tables"],
    8: ["snow CLI stage copy / PUT", "Directory tables", "COPY INTO (CSV file formats)"],
    9: ["PUT + COPY INTO with INFER_SCHEMA (Parquet)", "Informational PK/FK constraints + comments", "CoCo CLI"],
    10: ["AI_PARSE_DOCUMENT (LAYOUT, page_split)", "TO_FILE over directory tables", "MERGE (idempotent loads)"],
    11: ["AI_COMPLETE with JSON-schema structured output", "AI_EXTRACT (comparison)"],
    12: ["Snowpark Python UDFs", "LATERAL FLATTEN over arrays"],
    13: ["EVAL schema tables/views", "SQL set comparison (precision / recall)"],
    14: ["AI_CLASSIFY", "SQL rules (CASE) over classified output"],
    15: ["Streams on directory tables", "Tasks / task graphs", "Dynamic Tables (downstream refresh)", "Custom CoCo skill"],
    16: ["COPY INTO from stage", "Snowpark UDF reuse for normalisation"],
    17: ["Dynamic Tables", "JAROWINKLER_SIMILARITY", "EDITDISTANCE"],
    18: ["EVAL schema views", "SQL confusion matrix"],
    19: ["Dynamic Tables / views", "Window functions (baseline vs post-dose labs)", "AI_COMPLETE (templated flag_reason)"],
    20: ["AI_COMPLETE", "AI_TRANSLATE", "App write-back table with audit columns"],
    21: ["Object tagging", "Masking policies", "Row access policies", "RBAC (read-only judge role)"],
    22: ["Cortex Search service (attributes for filtering)", "Chunking in SQL"],
    23: ["Semantic Views", "Cortex Analyst (verified queries)", "CoCo semantic-view skill"],
    24: ["Cortex Agents", "Cortex Analyst + Cortex Search tools", "Stored procedure as custom tool", "CoCo agent skill"],
    25: ["AI_AGG / AI_SUMMARIZE_AGG", "Snowflake ALERT objects", "Notification integration + SYSTEM$SEND_EMAIL"],
    26: ["Views / aggregations over CORE.NSQ_ALERT", "Time-series SQL"],
    27: ["Streamlit in Snowflake (multi-page)", "Snowpark session (get_active_session)"],
    28: ["Streamlit in Snowflake", "GET_PRESIGNED_URL on stage files"],
    29: ["Streamlit in Snowflake", "Write-back to APP tables", "Masking policies (role-aware view)"],
    30: ["Cortex Agents REST API", "Streamlit in Snowflake"],
    31: ["Streamlit in Snowflake charts", "EVAL metrics views"],
    32: ["Key-pair authentication service user", "Read-only role + masking for judges", "Streamlit Community Cloud mirror"],
    33: ["Zero-copy clone", "Idempotent SQL deploy (CREATE OR REPLACE / IF NOT EXISTS)", "Time Travel for safe resets"],
    34: ["Streams + Tasks (live upload)", "Snowflake Alerts + email", "Streamlit in Snowflake", "Cortex Agents"],
    35: [],
    36: [],
    37: ["CoCo CLI", "Custom CoCo skill (.cortex/skills)"],
    38: ["Resource monitors", "Warehouse suspend", "COPY INTO @stage (unload backup)"],
    39: [],
}
# CoCo guidance for `coco`-labelled items whose plan text has no separate "CoCo CLI:" line
COCO_DEFAULT = {
    22: "Use CoCo CLI to draft the chunking SQL and the `CREATE CORTEX SEARCH SERVICE` statement; log the session in `docs/coco_log.md`.",
    23: "Build it with CoCo's semantic-view skill; log the session (prompt → generated → edited) in `docs/coco_log.md`.",
    24: "Build it with CoCo's agent-studio skill; log the session in `docs/coco_log.md`.",
    27: "Scaffold the multi-page app and the SiS/Community-Cloud session helper with CoCo CLI; log the session in `docs/coco_log.md`.",
    37: "This item *is* the CoCo evidence: every member logs sessions; the custom skill lives in `.cortex/skills/kavach-monthly-run/`.",
}
CLOSED_AT_CREATION = {1, 3}  # already delivered -> created, then closed as completed
# Work already delivered by the data-acquisition run (branch claude/affectionate-dirac-rq2bxf)
STATUS_NOTES = {
    1: "**Done.** Delivered on branch `claude/affectionate-dirac-rq2bxf`: 52 alert PDFs + portal JSON "
       "(2024-01..2026-08) + drug master subset + reference docs, manifest, coverage table in "
       "`docs/DATA_SOURCES.md`; `make validate` passes. Closed as completed at creation; merge that branch to `main`.",
    2: "Gold template is ready (57 rows / 55 records, `verified` blank). Needs a human.",
    3: "**Done.** Delivered on branch `claude/affectionate-dirac-rq2bxf` (seed 42, scenarios A/B, decoys, "
       "answer key); `validate_data.py` synthetic checks pass. Closed as completed at creation; merge that branch to `main`.",
    4: "Partly done: README, .gitignore (.env, kaggle.json), .env.example exist. Templates, CoCo guide and "
       "snow config example still to do.",
}


def section8(text: str) -> list[str]:
    start = text.index("## 8. Issues")
    end = text.index("## 9. Instructions")
    return text[start:end].splitlines()


def parse(lines: list[str]) -> list[dict]:
    issues: list[dict] = []
    milestone = None
    cur = None
    field = None
    for line in lines:
        m = re.match(r"^### (M\d) · (.+?)(?:\s*\(.*\))?\s*$", line)
        if m:
            title = f"{m.group(1)} · {m.group(2)}"
            milestone = next(k for k in MILESTONES if k.startswith(m.group(1)))
            assert milestone == title or milestone.startswith(title[:4]), title
            continue
        m = re.match(r"^\*\*#(\d+) \[([A-C+]+)\] (.+)\*\*\s*$", line)
        if m:
            cur = {"id": int(m.group(1)), "owner_raw": m.group(2), "title": m.group(3).strip(),
                   "milestone": milestone, "labels_raw": [], "fields": {}}
            issues.append(cur)
            field = None
            continue
        if cur is None:
            continue
        m = re.match(r"^Labels:\s*(.+)$", line)
        if m:
            cur["labels_raw"] = [x.strip() for x in m.group(1).split(",") if x.strip()]
            continue
        m = re.match(r"^- (Tasks|CoCo CLI|Acceptance|Depends on|Assignees|Body):\s*(.*)$", line)
        if m:
            field = FIELD_KEYS[m.group(1)]
            cur["fields"][field] = [m.group(2)]  # element 0 is the inline lead (may be "")
            continue
        if field and (line.startswith("  ") or not line.strip()):
            cur["fields"][field].append(line[2:] if line.startswith("  ") else "")
    return issues


def as_md(parts: list[str], checkbox: bool) -> str:
    """Field lines -> markdown. Sub-bullets become checkboxes; a lone sentence becomes one checkbox."""
    lead, out = (parts[0] if parts else ""), []
    lead = lead[:1].upper() + lead[1:]
    rest = parts[1:]
    has_bullets = any(re.match(r"^\s*(- |\d+\. )", r) for r in rest)
    if lead:
        out.append((f"- [ ] {lead}" if checkbox and not has_bullets and not any(r.strip() for r in rest) else lead))
    for r in rest:
        b = re.match(r"^(\s*)- (.*)$", r)
        if b:
            indent, item = b.group(1), b.group(2).rstrip(";").rstrip()
            out.append(f"{indent}- [ ] {item}" if checkbox and not indent else f"{indent}- {item}")
        else:
            out.append(r)
    txt = "\n".join(out).strip()
    return re.sub(r"\n{3,}", "\n\n", txt)


def dep_ids(text: str, all_ids: list[int], by_ms: dict[str, list[int]]) -> list[int]:
    ids: set[int] = set()
    for a, b in re.findall(r"#(\d+)(?:\s*[–-]\s*#?(\d+))?", text):
        lo, hi = int(a), int(b) if b else int(a)
        ids.update(range(lo, hi + 1))
    if re.search(r"most of M2/M3", text):
        ids.update(by_ms["M2 · Core pipelines"] + by_ms["M3 · Intelligence & App"])
    return sorted(i for i in ids if i in all_ids)


def build(issues: list[dict]) -> list[dict]:
    all_ids = [i["id"] for i in issues]
    by_ms: dict[str, list[int]] = {}
    for i in issues:
        by_ms.setdefault(i["milestone"], []).append(i["id"])
    out = []
    for i in issues:
        f = i["fields"]
        owners = [o for o in i["owner_raw"].split("+")]
        owner = "A" if len(owners) > 1 else owners[0]  # #37: owner A, assigned to all three
        prio = next((x for x in i["labels_raw"] if re.fullmatch(r"P[0-2]", x)), "P1" if i["id"] == 40 else None)
        labels = ([f"owner:{owner}"] if i["id"] != 40 else ["owner:C"]) + i["labels_raw"]
        assignees = [f"@PERSON_{o}" for o in owners]
        dep_text = " ".join(x for x in f.get("depends", []) if x.strip())
        deps = dep_ids(dep_text, all_ids, by_ms)
        if i["id"] == 40:
            body = "_(Generated at creation time: task list of every issue grouped by milestone, owner table, key dates.)_"
        else:
            tasks_md = as_md(f.get("tasks", []), checkbox=True)
            acc_md = as_md(f.get("acceptance", []), checkbox=True)
            coco_md = as_md(f.get("coco", [""]), checkbox=False) or COCO_DEFAULT.get(i["id"], "") or "_Optional — log any notable CoCo session in `docs/coco_log.md`._"
            feats = FEATURES[i["id"]]
            ctx = (f"**Owner:** Person {' + '.join(owners)} ({', '.join(ROLES[o] for o in owners)}) · "
                   f"**Milestone:** {i['milestone']} · **Priority:** {prio}\n\n"
                   f"Part of **Kavach** — see `CLAUDE_CODE_TEAM_PLAN.md` §8 (plan item #{i['id']}). "
                   "Principles: Snowflake-first, everything as code under `snowflake/`, cite `source_file + page`, "
                   "\"needs clinician review\" wording, protect the credits.")
            if i["id"] in STATUS_NOTES:
                ctx += f"\n\n> **Status:** {STATUS_NOTES[i['id']]}"
            if len(deps) > 6:
                dep_md = "- " + ", ".join(f"#{d}" for d in deps)
            else:
                dep_md = "\n".join(f"- #{d}" for d in deps) if deps else "_None_"
            extra = re.sub(r"#\d+(?:\s*[–-]\s*#?\d+)?,?", "", dep_text).strip(" ,")
            if extra:
                dep_md += f"\n\n_Note: {extra}_"
            body = "\n\n".join([
                "## Context\n" + ctx,
                "## Tasks\n" + tasks_md,
                "## Snowflake features\n" + ("\n".join(f"- {x}" for x in feats) if feats else "_None: this item is outside Snowflake._"),
                "## CoCo CLI\n" + coco_md,
                "## Acceptance criteria\n" + acc_md,
                "## Depends on\n" + dep_md,
            ])
        if i["id"] in CLOSED_AT_CREATION:
            body = body.replace("- [ ] ", "- [x] ")
        out.append({"id": i["id"], "close_at_creation": i["id"] in CLOSED_AT_CREATION, "title": f"[{i['owner_raw']}] {i['title']}", "owner": owner,
                    "assignees": assignees, "labels": labels, "priority": prio,
                    "milestone": i["milestone"], "milestone_due": MILESTONES[i["milestone"]],
                    "depends_on": deps, "status_note": STATUS_NOTES.get(i["id"], ""), "body": body})
    return out


def q(v) -> str:
    return json.dumps(v, ensure_ascii=False)


def to_yaml(items: list[dict]) -> str:
    lines = ["# Generated by scripts/build_issues_yaml.py from CLAUDE_CODE_TEAM_PLAN.md §8 — do not edit by hand.",
             "# @PERSON_A/B/C are replaced with real GitHub usernames at creation time.",
             "milestones:"]
    for t, d in MILESTONES.items():
        lines += [f"  - title: {q(t)}", f"    due_on: {q(d + 'T18:29:59Z')}"]
    lines.append("issues:")
    for it in items:
        lines.append(f"  - id: {it['id']}")
        for k in ("title", "close_at_creation", "owner", "assignees", "labels", "priority", "milestone", "milestone_due",
                  "depends_on", "status_note"):
            lines.append(f"    {k}: {q(it[k])}")
        lines.append("    body: |-")
        lines += [("      " + ln) if ln else "" for ln in it["body"].splitlines()]
    return "\n".join(lines) + "\n"


def main() -> int:
    items = build(parse(section8(PLAN.read_text(encoding="utf-8"))))
    assert [i["id"] for i in items] == list(range(1, 41)), [i["id"] for i in items]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(to_yaml(items), encoding="utf-8")
    (OUT.parent / "issues.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} issues -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
