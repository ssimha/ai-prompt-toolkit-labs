# Prompt 3 — Chain-of-Thought Reconciliation

Once you have all five stores cleaned and combined, use this to
investigate the PROMO-REGIONAL-JUL discrepancy referenced in section 1.6.

```
Compare the store totals below to the expected regional promo total
of $750.00 for item PROMO-REGIONAL-JUL. Work through this step by step:
1. List each store's reported amount for PROMO-REGIONAL-JUL.
2. Sum them and compare to the expected total.
3. If they don't match, identify which store(s) look anomalous and
   by how much.
4. State a hypothesis for the discrepancy before giving your final
   answer.
Show your work for each step.

Store 02: $210.00
Store 03: $410.00
Store 07: $395.00
```

The three PROMO-REGIONAL-JUL rows sum to $1,015.00 against an expected
$750.00 — a real discrepancy, left unresolved on purpose. Compare your
model's hypothesis (duplicate entry? Store 07 double-counted a split
transaction? the "expected" figure itself is stale?) against your own
read of the raw files. There is no single hidden right answer here —
the exercise is judging whether the model's step-by-step reasoning is
sound and whether it flags its own uncertainty rather than guessing
with false confidence.

