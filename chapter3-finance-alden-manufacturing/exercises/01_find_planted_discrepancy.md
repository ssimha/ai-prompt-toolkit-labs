# Exercise 1 — Find the Planted Discrepancy

`ledger/sample_ai_claim.json` contains a real, planted error: one
subsidiary's Q2 figure was converted to USD using the wrong quarter's
FX rate (a genuinely easy mistake to make when six subsidiaries report
in four different currencies).

1. Before running anything, use Prompt 6 (the LLM-based reconciliation
   check) against `ledger/sample_ai_claim.json` and
   `ledger/gl_export.csv`, and see if your model catches it.
2. Then run the mechanical check:
   ```
   python ledger/reconcile.py ledger/sample_ai_claim.json
   ```
3. Compare: did the LLM catch the same discrepancy the script found?
   Did it catch it at the subsidiary level, the consolidated level, or
   both?
4. Open `ledger/gl_export.csv` and manually trace through which
   subsidiary and which FX rate column was misapplied. Confirm your
   understanding matches what the script reported.
