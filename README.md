# The AI Prompt Toolkit — Companion Labs
### by Sirish M. Simha

This repository holds the runnable labs for *The AI Prompt Toolkit: From
Spreadsheets to Autonomous Agents*. Each chapter has its own folder,
structured the same way:

```
chapterN-<domain>-<case-study>/
  raw-data/            the messy starting material
  prompts/             the exact prompts from the chapter, ready to paste
  expected-output/     what a correct run should produce, for self-checking
  exercises/           extensions that push past what the chapter covers
  README.md            setup and a suggested working order for that lab
```

## What you need

- A web browser and any AI assistant (ChatGPT, Claude, Gemini, or similar)
  for Labs 1 to 4. No account beyond the assistant itself, and no API key.
- Python 3.10 or newer for the scripts in Labs 2, 3, 4 and 5.
- For Lab 5 only: your own Anthropic API key and a few dollars of API
  credit. See that folder's README. Running the sample batch costs a few
  cents.

## How to use a lab

1. Read the chapter first. The labs assume you have seen the reasoning
   behind each prompt, not just the prompt text.
2. Open the lab folder's README and follow its working order.
3. Run the prompts in order against the AI assistant of your choice. The
   book is deliberately model-agnostic; wording will differ between
   assistants, but the numbers should match the expected output.
4. Check your output against the files in `expected-output/`.
5. Attempt the exercises. They are designed to break your first working
   version in a specific, instructive way. That is the point, not a bug.

## The labs

| Chapter | Folder | Needs |
|---|---|---|
| 1. Foundations: Meridian Retail | `chapter1-foundations-meridian-retail/` | an AI assistant |
| 2. Sales & Marketing: Northwind B2B | `chapter2-sales-marketing-northwind/` | an AI assistant, plus Python (standard library only) |
| 3. Finance: Alden Manufacturing | `chapter3-finance-alden-manufacturing/` | an AI assistant, plus Python (standard library only) |
| 4. Coders: Fenwick Logistics | `chapter4-coders-fenwick-logistics/` | an AI assistant, plus `pip install -r requirements.txt` |
| 5. Agent Builders: Solace Support | `chapter5-agent-builders-solace-support/` | Anthropic API key (costs a few cents per run) |

### Chapter 1: Foundations (Meridian Retail)
Messy weekly store exports, the full few-shot, structured-output and
chain-of-thought prompt sequence, control totals to verify against, and
three exercises.

### Chapter 2: Sales & Marketing (Northwind B2B)
Brand-voice examples, segment profiles, the full prompt sequence, and two
dependency-free Python scripts: `claims_checker.py` (flags likely
unapproved marketing claims) and `validate_campaign_json.py` (validates the
structured campaign output).

### Chapter 3: Finance (Alden Manufacturing)
A multi-currency general ledger export (6 subsidiaries, 4 currencies) and
`reconcile.py`, a dependency-free script that converts currencies and checks
any claimed figure against the ledger to the cent. Includes planted errors
for you to catch.

### Chapter 4: Coders (Fenwick Logistics)
A FastAPI shipment-tracking project with a reproducible timezone bug. A
zero-dependency test runs with plain `python3`; the full app and its tests
need the packages in `requirements.txt`.

### Chapter 5: Agent Builders (Solace Support)
A multi-agent support pipeline (Classifier, Planner, Researcher, Drafter,
Reviewer) calling the Claude API against a seeded SQLite database, with
full logging. This is the one lab that costs real money to run, because it
makes live API calls.

## Found a problem?

If a lab does not run, a prompt does not reproduce the result described in
the book, or a file name does not match the text, please open an issue and
include the chapter, the section number, the exact command, the full error
text, and your operating system and Python version.

---
*Companion repository for The AI Prompt Toolkit by Sirish M. Simha.*
