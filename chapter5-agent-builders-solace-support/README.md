# Chapter 5 Lab — Solace Support Agent Pipeline

A working, runnable version of the four-agent pipeline from Chapter 5
(Agent Builders), using the real Claude API against a real (mock) SQLite
database — not simulated tool results.

## What's actually real here vs. mocked

- **Real**: the LLM calls (Classifier, Planner, Researcher, Drafter,
  Reviewer all genuinely call Claude), the tool-execution layer (SQLite
  queries actually run), the guardrail logic, the logging.
- **Mocked/invented**: the underlying data itself — Solace, its customers,
  invoices, and error logs are all fictional, seeded by `db/seed.py`.

## Setup

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Add your API key:**
   ```
   cp .env.example .env
   ```
   Open `.env` and paste in your own key from
   https://console.anthropic.com/settings/keys — never commit this file
   (it's already in `.gitignore`).

3. **Seed the mock database:**
   ```
   python db/seed.py
   ```
   This creates `db/mock_data.db` with invented invoices, error logs, and
   account records for three test customers. Safe to re-run any time —
   it rebuilds from scratch.

4. **Run the pipeline against the sample tickets:**
   ```
   python main.py data/sample_tickets.json
   ```

## What to expect

Five sample tickets in `data/sample_tickets.json`, each exercising a
different path through the pipeline:

- **TICKET-001** — a billing dispute under the $500 escalation threshold;
  should flow all the way through to a Reviewer decision. Watch whether
  the Drafter and Reviewer correctly notice the actual duplicate charge
  present in the mock invoice data.
- **TICKET-002** — a simple password reset; should route through
  `skip_to_draft`, bypassing Research entirely.
- **TICKET-003** — a technical outage report; watch how the Classifier
  scores urgency and whether the Planner escalates it.
- **TICKET-004** — contains the phrase "legal action"; should hit the
  hard code-level guardrail and escalate before the Classifier ever runs.
- **TICKET-005** — a feature request; lowest stakes, good for checking
  the Drafter doesn't over-promise a roadmap commitment it has no data on.

## Inspecting what happened

- `logs/pipeline_trace.jsonl` — one line per agent step, per ticket. This
  is the observability layer from section 5.12 — use it to trace exactly
  what each agent saw and returned, especially for debugging a
  surprising outcome.
- `logs/run_results.json` — the final state object for every ticket in
  the batch, written after `main.py` finishes.

## Model tiering used here

Set in `agents/pipeline_agents.py`, matching section 5.11:

| Agent | Model tier | Why |
|---|---|---|
| Classifier | fast/cheap (Haiku tier) | high volume, individually low-stakes |
| Researcher | mid tier (Sonnet) | needs reliable tool-schema following |
| Drafter | mid-strong tier (Sonnet) | customer-visible output |
| Planner | strongest (Opus tier) | routing mistakes cascade downstream |
| Reviewer | strongest (Opus tier) | last check before send |

Swap these for whatever models you have access to and re-run — the
book is deliberately model-agnostic; this table is a starting point to
test against your own results, not a fixed rule.

## Before you run this for real: cost note

Every ticket run through this pipeline makes 3-5 real API calls (more if
research is triggered). Running the sample batch of 5 tickets costs a
small, real amount against your API key. Check current pricing at
https://docs.claude.com before running large batches.

## Exercises

See `exercises/` — extending the pipeline with a Sentiment Checker
agent, deliberately breaking tool discipline to observe the failure
mode from section 5.7, and designing guardrails for a new ticket
category from scratch.

