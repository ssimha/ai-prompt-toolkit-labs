# Northwind Claims Ledger

The only factual claims marketing copy is allowed to make about
Northwind. Referenced in prompts/06_claims_ledger_check.md and used
by claims_checker.py. Update this file, not individual prompts, when
a claim changes — that's the whole point of a single source of truth.

| Claim | Exact approved wording | Notes |
|---|---|---|
| SSO availability | "SSO available on Business and Enterprise plans" | Not available on Starter |
| Audit trail | "Audit trail logs all permission changes, available on Enterprise plan" | Enterprise only |
| Time to first invite | "Median customer sees first teammate invited within 4 days of signup" | Internal data, Q2 2026 — do not round to "under a week" or restate as a different number |
| Integration count | "Integrates with Slack, Salesforce, and Google Workspace" | Do not say "integrates with everything" or list unreleased integrations |
| Uptime | "99.9% uptime over the trailing 12 months" | Do not say "100% uptime" or "never goes down" |

## Explicitly NOT approved (common temptations to avoid)

- Any specific percentage improvement claim ("40% faster", "60% more efficient") — no case study currently supports a specific performance percentage
- Customer count claims ("used by 10,000 companies") — not currently tracked/verified for public claims
- "Guaranteed" ROI, results, or outcomes of any kind
- Competitor comparisons naming a specific competitor by name
- "Best in class", "#1", or other superlative rankings — unverifiable and legally risky
