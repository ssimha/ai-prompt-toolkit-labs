# The AI Prompt Toolkit — Companion Labs
### by Sirish Simha

This repository holds the runnable labs referenced throughout *The Prompt
Toolkit: From Spreadsheets to Autonomous Agents*. Each chapter gets its own
folder, structured the same way:

```
chapterN-<domain>-<case-study>/
  raw-data/           the messy starting material
  prompts/             the exact prompts from the chapter, ready to paste
  expected-output/     what a correct run should produce, for self-checking
  exercises/            extensions that push past what the chapter covers
```

## How to use a lab

1. Read the chapter first. The labs assume you've seen the reasoning behind
   each prompt, not just the prompt text.
2. Run the prompts in order against a model of your choice — any of them.
   This book is deliberately model-agnostic; part of the exercise is seeing
   how your model of choice performs and comparing notes.
3. Check your output against the files in `expected-output/`.
4. Attempt the exercises. They're designed to break your first working
   version in a specific, instructive way — that's the point, not a bug.

## Chapter 1 — Foundations: Meridian Retail

`chapter1-foundations-meridian-retail/` — five (then six) messy weekly
store exports, the full few-shot / structured-output / chain-of-thought
prompt sequence from the chapter, control totals to verify against, and
three exercises covering a new data quirk, a corrupted control total, and
writing your own few-shot examples from scratch.

## Chapter 5 — Agent Builders: Solace Support

`chapter5-agent-builders-solace-support/` — a real, runnable multi-agent
pipeline: Classifier, Planner, Researcher, Drafter, and Reviewer agents,
calling the actual Claude API against a real (seeded, invented-data)
SQLite database. Requires your own Anthropic API key — see that folder's
README for setup. Includes full logging/tracing and three exercises.

Note: this is the one lab in the repo that costs real API usage when run,
since it makes genuine LLM calls rather than using pre-computed expected
output.

## Chapter 4 — Coders: Fenwick Logistics

`chapter4-coders-fenwick-logistics/` — a working FastAPI project: a
shipment-tracking endpoint, a real SQLite-backed data layer, and a
genuinely reproducible timezone bug (not just described — verified with
a zero-dependency test you can run right now with plain `python3`).
Includes the full prompt sequence from the chapter and three exercises.
Full app tests need `pip install -r requirements.txt`.

## Chapter 2 — Sales & Marketing: Northwind B2B

`chapter2-sales-marketing-northwind/` — brand-voice examples, segment
profiles, the full six-prompt sequence from the chapter, and two real,
tested Python scripts: `claims_checker.py` (mechanically flags likely
unapproved marketing claims — verified against a deliberately
over-claiming sample draft) and `validate_campaign_json.py` (schema
validator for the structured campaign output). Both are dependency-free
and runnable immediately, no install needed.

## Chapter 3 — Finance: Alden Manufacturing

`chapter3-finance-alden-manufacturing/` — a real multi-currency general
ledger export (6 subsidiaries, 4 currencies, real FX rates) and
`reconcile.py`, a dependency-free Python script that performs actual
currency conversion and checks any claimed figure against the GL to the
cent. Verified against a correct claim (clean pass), a planted
FX-rate-confusion bug, and a planted unit-confusion bug — all three
catch or pass exactly as intended. Includes all six prompts from the
chapter and three exercises.

## All five chapters and their labs are now complete.

Chapters 1, 2, 3, 4, and 5 each have a full companion lab in this
repository.

---
*Companion repository for The AI Prompt Toolkit. Questions, corrections, or
found a bug in a lab — open an issue.*

