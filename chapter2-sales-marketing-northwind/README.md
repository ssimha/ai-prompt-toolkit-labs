# Chapter 2 Lab — Northwind B2B

Companion lab for Chapter 2 (Sales & Marketing) of *The AI Prompt Toolkit*.

## What's actually real here vs. what you run yourself

- **Real and tested in this repo already**: `claims/claims_checker.py`
  and `expected-output/validate_campaign_json.py` — both are
  dependency-free Python scripts (standard library only) that were
  actually run and verified while building this lab. No API key, no
  install, run them right now:
  ```
  python claims/claims_checker.py claims/sample_overclaiming_draft.txt
  python expected-output/validate_campaign_json.py expected-output/campaign_schema_example.json
  ```
- **You run yourself**: the actual prompts against a model of your
  choice — this chapter, like Chapter 1, is model-agnostic and
  paste-ready rather than wired to a live API.

## Contents

- `brand-voice/` — the two reference voice examples from section 2.3,
  and the three segment profiles (startup, mid-market, enterprise)
  from section 2.4.
- `claims/` — the claims ledger (section 2.10), a deliberately
  over-claiming sample draft with 5 known issues, and the mechanical
  claims checker script.
- `prompts/` — all six prompts from the chapter, paste-ready, in
  chapter order.
- `expected-output/` — the expected JSON shape from section 2.7 and a
  real schema validator to check your own generated output against.
- `exercises/` — three extensions: judging an over-personalization
  example, writing a new claims-ledger entry from scratch, and
  building a full 5-email sequence end to end.

## Suggested order

1. Read `brand-voice/examples.md` and `brand-voice/segments.md`.
2. Work through `prompts/01` through `prompts/04` — brand voice,
   segmentation, chaining, A/B variants.
3. Run `prompts/05`, then validate your output:
   ```
   python expected-output/validate_campaign_json.py your_output.json
   ```
4. Run the claims checker against the known-bad sample first, so you
   know what a real catch looks like, before trusting it on your own
   drafts:
   ```
   python claims/claims_checker.py claims/sample_overclaiming_draft.txt
   ```
5. Work through `prompts/06`'s two-part claims-ledger check (LLM-based),
   and compare what it catches against what the mechanical checker
   caught — they're complementary, not redundant, which is the point
   made in section 2.10.
6. Move to `exercises/`.

## An honest note on the claims checker

`claims_checker.py` is intentionally simple, pattern-based, and not
exhaustive — it will not catch a fabricated claim phrased in a way that
doesn't match its regex patterns. It's the fast, free, mechanical first
pass; the LLM-based check in `prompts/06` and the human checkpoint in
section 2.11 are what actually make the verification complete. Don't
mistake a clean checker run for a fully verified draft.
