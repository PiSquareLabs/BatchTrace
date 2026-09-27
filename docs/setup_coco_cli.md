# Setup: CoCo CLI + snow CLI

Goal: clone → working CoCo CLI + snow CLI session in 15 minutes, same conventions for everyone.
This repo has **no real Snowflake account until M1 (#6)** — you can do steps 1-3 now; step 4
(connection test) only works once the team trial is activated and you have a user.

## 1. Prerequisites

- Python 3.10+ and `pip` (see root `requirements.txt` / `make install`)
- A Snowflake CLI (`snow`) install:

```bash
pip install snowflake-cli-labs
snow --version
```

- CoCo CLI installed and on your `PATH`. Follow the install instructions from the CoCo CLI
  hackathon kit (Snowflake CoCo CLI Hackathon 2026, GCC Edition). If `coco --version` fails,
  email `cococlihackgcc-support@hack2skill.com` — do this the same day, per the team plan.

## 2. Get your Snowflake user (after M1 / #6)

Person C (platform lead) activates the team trial and creates users for A and B. You will get:

- an **account identifier** (e.g. `abcd-xy12345`)
- a **username**
- a **role** to use day-to-day (`KAVACH_ENGINEER`, unless told otherwise)
- a default **warehouse** (`WH_BUILD`)

Don't share passwords. If you were issued a key pair instead of a password, keep the private
key (`*.p8`) outside the repo — see `.gitignore`.

## 3. Configure the snow CLI connection

Copy the example and fill in your own values — **never commit the real file**:

```bash
cp snowflake/config.toml.example snowflake/config.toml
```

Edit `snowflake/config.toml` with your account, user, role and warehouse. If you're using
key-pair auth, point `private_key_path` at your local `.p8` file (also never committed).

Point the snow CLI at it (or place it at the CLI's default location — see `snow --help`):

```bash
export SNOWFLAKE_HOME="$(pwd)/snowflake"   # macOS/Linux
# or on Windows PowerShell:
# $env:SNOWFLAKE_HOME = "$PWD\snowflake"
```

Test the connection:

```bash
snow connection test -c kavach
```

## 4. Test CoCo CLI

```bash
coco --version
coco session start   # or the equivalent trivial command from the CoCo kit
```

Run one trivial CoCo CLI session and log it in [`docs/coco_log.md`](coco_log.md) — prompt, what
CoCo generated, what you changed. This is expected of every teammate (issue #6) and judges will
look for it (issue #37).

## 5. Conventions while you work

- One branch per issue: `<issue#>-short-name`.
- PRs reference `Closes #n` (see `.github/pull_request_template.md`).
- All Snowflake objects are numbered, idempotent SQL files under `snowflake/`
  (`CREATE OR REPLACE` / `IF NOT EXISTS`) — nothing is created by hand in the UI that isn't also
  captured in a script.
- Every alert-derived fact shown to a user cites `source_file + page`.
- Clinical flags say "needs clinician review", never a diagnosis.
- Use X-Small warehouses with a 60s auto-suspend; run `AI_PARSE_DOCUMENT` once per file and store
  results — never re-parse the same file in a loop (protect the trial credits).

## 6. Troubleshooting

| Symptom | Likely cause |
|---|---|
| `snow connection test` fails with a network/DNS error | Wrong account identifier — copy it exactly from Snowsight's account URL. |
| `snow connection test` fails with 250001 | Wrong username/role/warehouse, or the role wasn't granted to your user yet — ask C. |
| CoCo CLI can't reach Snowflake | Make sure `SNOWFLAKE.COPILOT_USER` was granted to your role (done in #6). |
| Accidentally staged `config.toml` or a `.p8` key | `git restore --staged <file>`, then check `.gitignore` covers it (it should). |
