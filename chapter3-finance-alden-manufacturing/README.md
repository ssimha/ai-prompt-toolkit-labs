# Chapter 3 Lab — Alden Manufacturing

Companion lab for Chapter 3 (Finance) of *The Prompt Toolkit*.

## What's actually real here vs. what you run yourself

- **Real and tested in this repo already**: `ledger/reconcile.py` — a
  dependency-free Python script (standard library only) that performs
  actual multi-currency conversion from `ledger/gl_export.csv` and
  checks any claimed figure against it to the cent. Verified against
  three cases while building this lab:
  - a correct claim (reconciles cleanly, zero false positives)
  - a planted FX-rate-confusion bug (Exercise 1) — caught at both the
    subsidiary and consolidated level
  - a planted unit-confusion bug (Exercise 2) — caught with a dramatic,
    unmissable variance swing
- **You run yourself**: the six prompts against a model of your choice.
  Like Chapters 1 and 2, this lab is model-agnostic and paste-ready.

## Try the reconciliation script right now

```
python ledger/reconcile.py ledger/sample_ai_claim.json
```
This runs against the deliberately buggy claim by default — you should
see it flag a $6,900 mismatch on Shenzhen's Q2 figure. Then try the
clean version:
```
python ledger/reconcile.py ledger/sample_ai_claim_correct.json
```
This should report a clean reconciliation with no discrepancies.

## Contents

- `ledger/gl_export.csv` — the real general ledger export: 6
  subsidiaries, 4 currencies, real FX rates for Q1 and Q2.
- `ledger/reconcile.py` — the reconciliation script described above.
- `ledger/sample_ai_claim.json` — a claim with a planted FX-rate bug
  (this is the default file the script points to).
- `ledger/sample_ai_claim_correct.json` — the same claim, corrected.
- `ledger/sample_ai_claim_unit_confusion.json` — a claim with a
  planted thousands-vs-actual-dollars bug (Exercise 2).
- `prompts/` — all six prompts from the chapter, in order.
- `expected-output/correct_variance_summary.md` — the ground-truth
  numbers, computed directly from the GL, to check any analysis against.
- `exercises/` — three extensions: finding the planted FX bug, catching
  the unit-confusion bug, and engineering a case where self-consistency
  runs genuinely disagree.

## Suggested order

1. Run the reconciliation script against both sample claims first (see
   above) so you know what a real catch and a clean pass both look like.
2. Work through `prompts/01` through `prompts/06` in order.
3. Move to `exercises/`, in order — Exercise 1 and 2 both build directly
   on the sample claim files already in this repo.

## An honest note

The reconciliation script catches exactly what it's told to check:
total mismatches, variance-percentage mismatches, and (if you include a
subsidiary breakdown in your claim) per-subsidiary mismatches — all to
the cent. It will not catch an error that happens to net out to the
correct total through two compensating mistakes, and it does not
replace the LLM-based reconciliation check in Prompt 6 or the human
checkpoint in section 3.11. Use both, the way the chapter recommends.
