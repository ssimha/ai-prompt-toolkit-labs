# Prompt 1 — Few-Shot Cleaning

Use this prompt once per store file. Paste the store's raw CSV rows in place
of `{RAW_ROWS}`.

```
Clean each row to match this exact format. Examples:

Input:  Txn_Date: 3/7/26   | Amount: 45
Output: date: 2026-03-07 | amount_usd: 45.00

Input:  Day: March 8 2026  | Amount: $102.50
Output: date: 2026-03-08  | amount_usd: 102.50

Now apply the same transformation to every row in the data below.
Preserve the item code exactly as given, and add a store_id field
with the value {STORE_ID}.

{RAW_ROWS}
```

Try this on all five files in `raw-data/`. Each store uses a different
date format and column naming — that's the point. Confirm your output
dates all come back as YYYY-MM-DD regardless of which store you started
from, and that dollar amounts always show two decimal places.

