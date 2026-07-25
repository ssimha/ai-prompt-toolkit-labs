# Chapter 1 Lab — Meridian Retail

Companion lab for Chapter 1 (Foundations) of *The AI Prompt Toolkit*.

## Contents

- `raw-data/` — five messy store exports (store_02, 03, 05, 07, 09), each
  with a different date format, column naming, and amount format, exactly
  as described in section 1.1. `store_11.csv` is added for Exercise 1 —
  don't look at it until you get there.
- `prompts/` — the three prompts from the chapter: few-shot cleaning,
  structured output, and chain-of-thought reconciliation. Paste-ready.
- `expected-output/` — `clean_data.json` (the fully correct parsed output,
  42 rows) and `control_totals.md` (per-store and grand totals to check
  your work against).
- `exercises/` — three extensions: a sixth store with a new format quirk,
  a corrupted control total that exposes a real limit of control-total
  verification, and a from-scratch few-shot writing exercise.

## Suggested order

1. Read `prompts/01_few_shot_cleaning.md`, run it against each file in
   `raw-data/` (excluding store_11 for now).
2. Read `prompts/02_structured_output.md`, chain it after step 1.
3. Check your combined output against `expected-output/control_totals.md`
   and `clean_data.json`.
4. Read `prompts/03_chain_of_thought_reconciliation.md` and work through
   the PROMO-REGIONAL-JUL discrepancy.
5. Move to `exercises/` in order.

