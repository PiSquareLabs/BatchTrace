# Demo script (draft) — under 4 minutes

This is a **first draft** (#5). It gets finalised with timings and two dry runs in #34.

**The story:** in 2025, contaminated cough syrup ("Coldrif") was linked to child deaths in India.
CDSCO publishes monthly lists of failed batches, but hospitals rarely check them against what
they have already dispensed. Kavach does that check automatically, inside Snowflake.

**Demo data:** real public CDSCO alert PDFs matched against a fully **synthetic** hospital
(seed 42). No real patient data is used. The lead case is scenario A:
- batch `OL-032309`, KOFVON LS cough syrup;
- flagged in the Feb-2024 list for "Ethylene Glycol (EG) exceeding the permissible limit";
- 6 children exposed;
- 3 of them with creatinine more than 2x baseline;
- callback scripts in Malayalam.

---

## 0:00–0:25 — The problem (beat 1: "A new CDSCO month drops")

> "Every month CDSCO publishes the drug batches that failed quality testing. Coldrif showed what
> happens when a hospital doesn't check that list against what it has already given patients.
> A new list just dropped. Let's see what Kavach does with it."

*Screen:* the CDSCO alert PDF, then the architecture diagram for about 5 seconds.

## 0:25–0:55 — Upload → automatic processing (beat 2, #15)

> "We drop the PDF into a Snowflake stage. A stream sees the new file and a task runs the whole
> pipeline:
> - AI_PARSE_DOCUMENT reads the PDF;
> - AI_COMPLETE extracts every batch;
> - UDFs normalise the batch numbers;
> - AI_CLASSIFY scores severity;
> - a Dynamic Table matches against our dispensing records.
>
> Nobody presses a button."

*Screen:*
- run `snow stage copy` (or show the upload);
- show the task history turning green.

*Fallback:* have a pre-recorded clip ready in case the live run is slow.

## 0:55–1:10 — The email alert (beat 3, #25)

> "Minutes later, pharmacy gets this: a Snowflake Alert with the new matches."

*Screen:* the email in the inbox, with the subject line and a one-line summary.

## 1:10–2:40 — Inbox → batch → patients (beat 4, #28 #29)

**Screen 1: Alert Inbox (about 20 s)**
> "Of all the batches in this month's list, one is critical and matches our stock: a paediatric
> cough syrup contaminated with ethylene glycol."
- Point at the KPI cards and the monthly brief, then open the critical row.

**Screen 2: Batch Detail (about 35 s)**
> "Every fact links to the source PDF and page. Kavach found **6 children** who received this
> batch.
> - Four matched exactly, most from QR scans.
> - One was hand-typed as 'ol-032309' and still matched.
> - One had no batch recorded at all, so it goes on the watchlist.
>
> Stock is still sitting in SAT1, so quarantine it now."
- Click "Open source PDF (page n)".
- Point at the match reasons and the quarantine row.

**Screen 3: Patient Card (about 35 s)**
> "**Three** of these children show creatinine above twice their baseline within days of the
> dose. Kavach marks that as *needs clinician review*, never a diagnosis. The callback script is
> already written in Malayalam, the family's language."
- Show the medication timeline with the flagged dose highlighted, then the lab chart with the
  shaded window.
- Switch the script to Malayalam.
- Click **Escalate to clinician**, which writes back to `APP.ACTION_ITEMS`.

## 2:40–3:15 — Ask Kavach (beat 5, #30)

> "For anything else, just ask."

*Screen:*
- Click the starter question "Which children got OL-032309 and who has a lab flag?"
- The answer comes back as a table with the citation.
- Optionally ask a follow-up: "What does CDSCO guidance say about recall timelines?", answered
  from Cortex Search.

## 3:15–3:45 — How accurate is Kavach? (beat 6, #31)

> "We don't just claim this works; we measure it.
> - Extraction is scored against a hand-verified gold set: [X]%.
> - Matching is scored against the synthetic hospital's answer key: [Y]%, with [Z] near-miss
>   decoys correctly left out."

*Screen:* the accuracy page. Also show the regulator panel for about 5 seconds if time allows.

## 3:45–3:55 — Close

> "All of it runs in Snowflake, from stages and tasks through Cortex AI and agents to Streamlit.
> We built it with CoCo CLI. That's Kavach."

---

## Placeholders to fill in #34

| Placeholder | Source |
|---|---|
| `[X]%` extraction accuracy | `EVAL.EXTRACTION_METRICS` (#13) |
| `[Y]%` matching accuracy, `[Z]` decoys | `EVAL.MATCH_METRICS` (#18) |
| PDF page `n` | the `CORE.NSQ_ALERT` row for `OL-032309` |
| Exact / probable / watchlist split | the actual `CORE.BATCH_MATCHES` output (the 4/1/1 above is the ground-truth expectation) |

## Open questions

1. **Time shift.** The real alert is from Feb 2024, but the story says "a new month drops". Do
   we replay the Feb-2024 PDF as if it were new, or just narrate it as a past month?
2. **Dispensed after the alert.** Three of the six doses were given Aug–Oct 2024, *after* the
   alert. That is a strong point ("this would have been caught"), but is it deliberate in the
   generator, or should it be changed?
3. **Live or recorded.** Should the upload and task run (beat 2) be live or pre-recorded? Live
   is riskier on trial credits and latency.
4. **Masking.** Show masking live by switching roles, or only mention it?
