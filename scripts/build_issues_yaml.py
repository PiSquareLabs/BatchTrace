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
# keyword (regex) -> Snowflake feature, used to fill "## Snowflake features"
FEATURES = [
    (r"stage|PUT\b|snow stage", "Internal stages (SSE) + directory tables"),
    (r"AI_PARSE_DOCUMENT", "AI_PARSE_DOCUMENT (LAYOUT, page_split)"),
    (r"AI_COMPLETE", "AI_COMPLETE (structured JSON output)"),
    (r"AI_EXTRACT", "AI_EXTRACT"),
    (r"AI_CLASSIFY", "AI_CLASSIFY"),
    (r"AI_AGG|AI_SUMMARIZE_AGG", "AI_AGG / AI_SUMMARIZE_AGG"),
    (r"AI_TRANSLATE", "AI_TRANSLATE"),
    (r"Snowpark|UDF", "Snowpark Python UDFs"),
    (r"Dynamic Table", "Dynamic Tables"),
    (r"\bstream\b", "Streams"),
    (r"\btask\b", "Tasks / task graphs"),
    (r"JAROWINKLER|EDITDISTANCE", "JAROWINKLER_SIMILARITY / EDITDISTANCE"),
    (r"Cortex Search", "Cortex Search"),
    (r"[Ss]emantic view|KAVACH_SV", "Semantic Views + Cortex Analyst"),
    (r"Cortex Agent|agent", "Cortex Agents"),
    (r"Streamlit|SiS\b", "Streamlit in Snowflake"),
    (r"GET_PRESIGNED_URL", "GET_PRESIGNED_URL"),
    (r"ALERT` object|SYSTEM\$SEND_EMAIL|email", "Snowflake Alerts + SYSTEM$SEND_EMAIL"),
    (r"masking|row access|tag", "Object tagging, masking & row access policies"),
    (r"RBAC|roles? `|KAVACH_ADMIN", "RBAC"),
    (r"resource monitor|warehouse", "Warehouses + resource monitors"),
    (r"zero-copy clone|clone", "Zero-copy clone"),
    (r"COPY INTO|INFER_SCHEMA", "COPY INTO + INFER_SCHEMA"),
    (r"stored procedure", "Stored procedures"),
    (r"CoCo", "CoCo CLI"),
]
# Work already delivered by the data-acquisition run (branch claude/affectionate-dirac-rq2bxf)
STATUS_NOTES = {
    1: "Delivered on branch `claude/affectionate-dirac-rq2bxf`: 52 alert PDFs + portal JSON (2024-01..2026-08) + "
       "drug master subset + reference docs, manifest, coverage table in docs/DATA_SOURCES.md; "
       "`make validate` passes. Close once that branch is merged to `main`.",
    2: "Gold template is ready (57 rows / 55 records, `verified` blank). Needs a human.",
    3: "Delivered on branch `claude/affectionate-dirac-rq2bxf` (seed 42, scenarios A/B, decoys, answer key); "
       "validate_data.py synthetic checks pass. Close once merged to `main`.",
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
            coco_md = as_md(f.get("coco", [""]), checkbox=False) or "_Optional — log any notable CoCo session in `docs/coco_log.md`._"
            blob = " ".join(sum(f.values(), [])) + " " + i["title"]
            feats = [name for pat, name in FEATURES if re.search(pat, blob)]
            feats = list(dict.fromkeys(feats))
            ctx = (f"**Owner:** Person {' + '.join(owners)} ({', '.join(ROLES[o] for o in owners)}) · "
                   f"**Milestone:** {i['milestone']} · **Priority:** {prio}\n\n"
                   f"Part of **Kavach** — see `CLAUDE_CODE_TEAM_PLAN.md` §8 (plan item #{i['id']}). "
                   "Principles: Snowflake-first, everything as code under `snowflake/`, cite `source_file + page`, "
                   "\"needs clinician review\" wording, protect the credits.")
            if i["id"] in STATUS_NOTES:
                ctx += f"\n\n> **Status:** {STATUS_NOTES[i['id']]}"
            dep_md = ("\n".join(f"- #{d}" for d in deps) if deps else "_None_")
            extra = re.sub(r"#\d+(?:\s*[–-]\s*#?\d+)?,?", "", dep_text).strip(" ,")
            if extra:
                dep_md += f"\n\n_Note: {extra}_"
            body = "\n\n".join([
                "## Context\n" + ctx,
                "## Tasks\n" + tasks_md,
                "## Snowflake features\n" + ("\n".join(f"- {x}" for x in feats) if feats else "_None (outside Snowflake)_"),
                "## CoCo CLI\n" + coco_md,
                "## Acceptance criteria\n" + acc_md,
                "## Depends on\n" + dep_md,
            ])
        out.append({"id": i["id"], "title": f"[{i['owner_raw']}] {i['title']}", "owner": owner,
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
        for k in ("title", "owner", "assignees", "labels", "priority", "milestone", "milestone_due",
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
