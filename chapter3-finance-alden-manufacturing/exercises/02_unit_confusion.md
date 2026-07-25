# Exercise 2 — Catch a Dramatic Unit-Confusion Error

`ledger/sample_ai_claim_unit_confusion.json` contains a different kind
of error: Ohio's Q2 figure was left in thousands ($1,120.50 instead of
$1,120,500.00) — the classic thousands-vs-actual-dollars mistake named
in section 3.3.

1. Run the reconciliation script against it:
   ```
   python ledger/reconcile.py ledger/sample_ai_claim_unit_confusion.json
   ```
2. Notice how large the resulting variance_pct swing is (the claim
   shows COGS *decreasing* 24%, when it actually increased 7%) — a
   unit error this size is often more visible than the Exercise 1
   FX-rate error, precisely because it's so large it looks obviously
   wrong once you know to look. Write a sentence on why a smaller
   version of this same bug (say, one subsidiary out of twenty instead
   of six) might be much harder to eyeball without the reconciliation
   script.
3. Fix the claim file yourself (correct Ohio's Q2 figure) and confirm
   the script then reports a clean reconciliation.

