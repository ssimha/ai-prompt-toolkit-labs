# Prompt 1 — Structured Output for Financial Data (section 3.3)

```
Return ONLY a JSON object with these fields: "metric" (string),
"current_quarter_usd" (number, in whole dollars, not thousands or
millions), "prior_quarter_usd" (number, in whole dollars),
"variance_pct" (number, rounded to 1 decimal place).

Do not abbreviate large numbers. Do not include currency symbols in
the numeric fields. No text before or after the JSON.

Consolidated COGS data across all subsidiaries:
{paste ledger/gl_export.csv contents, or describe it}
```

Feed the result straight into the reconciliation script:
```
python ledger/reconcile.py your_output.json
```

