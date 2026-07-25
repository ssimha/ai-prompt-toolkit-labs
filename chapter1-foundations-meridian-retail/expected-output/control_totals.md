# Control Totals — Use These to Verify Your Output

Computed directly from the raw files in `raw-data/`. If your model's
cleaned output doesn't match these, something went wrong in cleaning —
that's the point of section 1.10's control-total check.

| Store | Total (USD) |
|-------|------------:|
| 02    |      731.00 |
| 03    |    1,033.00 |
| 05    |      393.00 |
| 07    |      858.00 |
| 09    |      433.00 |
| **Grand total** | **3,448.00** |

## PROMO-REGIONAL-JUL rows (used in Prompt 3)

| Store | Date       | Amount |
|-------|------------|-------:|
| 02    | 2026-07-02 | 210.00 |
| 03    | 2026-07-01 | 410.00 |
| 07    | 2026-06-30 | 395.00 |

Sum: $1,015.00. This is the number your model should independently
arrive at when reconciling — and the discrepancy against the "expected"
$750.00 in Prompt 3 is deliberate. See that prompt file for how to use it.

`clean_data.json` in this folder is the fully parsed, correct version of
all five raw files — 42 rows, every date normalized to YYYY-MM-DD, every
amount as a two-decimal number. Diff your model's structured output
against it.
