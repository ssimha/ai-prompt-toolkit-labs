# Ground-Truth Variance Summary

Computed directly from `ledger/gl_export.csv`, with real currency
conversion applied per subsidiary. Use this to check any AI-generated
analysis against — it's the equivalent of Chapter 1's control totals.

| Subsidiary | Currency | Q1 (USD) | Q2 (USD) | Change (USD) |
|---|---|---:|---:|---:|
| Ohio | USD | $1,050,000.00 | $1,120,500.00 | $70,500.00 |
| Texas | USD | $830,000.00 | $905,250.00 | $75,250.00 |
| Ontario | CAD | $448,350.00 | $474,240.00 | $25,890.00 |
| Bavaria | EUR | $580,500.00 | $605,920.00 | $25,420.00 |
| Shenzhen | CNY | $444,800.00 | $486,450.00 | $41,650.00 |
| Sao Paulo | BRL | $258,100.00 | $273,310.00 | $15,210.00 |
| **Consolidated** | | **$3,611,750.00** | **$3,865,670.00** | **$253,920.00** |

**Variance: 7.03%**

Ranked by dollar contribution to the change:
1. Texas — $75,250.00
2. Ohio — $70,500.00
3. Shenzhen — $41,650.00
4. Ontario — $25,890.00
5. Bavaria — $25,420.00
6. Sao Paulo — $15,210.00

Any AI-generated analysis that ranks these differently, or lands on a
different consolidated total, should be treated as a discrepancy to
investigate — not rounded away. Run `ledger/reconcile.py` against any
generated claim to check automatically.
