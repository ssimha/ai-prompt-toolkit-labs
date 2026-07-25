# Exercise 1 — A Sixth Store With a New Quirk

`raw-data/store_11.csv` has been added, and it breaks your Prompt 1
few-shot examples in two new ways:

1. It's **pipe-delimited**, not comma-delimited.
2. Its date format is `29-Jun-2026` — day, abbreviated month, year —
   which none of your five original few-shot examples cover.

Run your existing Prompt 1 against it unmodified and see what happens.
Then fix it: either add a new few-shot example covering this date
format, or adjust your prompt's instructions to handle delimiter
detection. Confirm your fix still works correctly against the original
five stores too — don't fix Store 11 by breaking the others.

