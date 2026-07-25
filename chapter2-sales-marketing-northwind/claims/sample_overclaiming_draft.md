# Sample Draft — Deliberately Over-Claiming (for Exercise / Prompt 6)

The actual draft to run the checker against is
`sample_overclaiming_draft.txt` in this same folder (plain text, no
markdown, so the checker isn't confused by documentation around it).
This file explains what's wrong with it and why.

Run:
```
python claims/claims_checker.py claims/sample_overclaiming_draft.txt
```

## What should be flagged

1. "60% faster project setup" — not in the ledger; no case study
   supports a specific percentage
2. "guaranteed result" — explicitly disallowed regardless of ledger
   content
3. "10,000+ customers" — customer count claims are not approved
4. "integrate with everything" — the ledger lists three specific
   integrations only
5. "100% uptime, no exceptions" — the ledger's actual approved figure
   is 99.9% over trailing 12 months, and directly contradicts this claim

