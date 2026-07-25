# Prompt 6 — Reconciliation Against the General Ledger (section 3.10)

This is the LLM-based half of verification; ledger/reconcile.py is the
mechanical half. Use both, per the chapter's point that they're
complementary.

```
Here is an AI-generated COGS variance figure: {paste a generated
current_quarter_usd, prior_quarter_usd, variance_pct}.

Reconcile this against the general ledger export below. Confirm:
1. Does the current-quarter figure match the GL total exactly, to the
   cent?
2. Does the prior-period figure match the correct comparison period in
   the GL, not an adjacent one?
3. List any discrepancy, however small, rather than rounding it away.

General ledger export:
{paste ledger/gl_export.csv}
```

Then run the mechanical check on the same claim:
```
python ledger/reconcile.py your_claim.json
```

They should agree. If the LLM-based check says "looks fine" but the
script finds a mismatch (or vice versa), that disagreement is itself
worth investigating — it means one of your two checks has a blind spot.

