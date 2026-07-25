# Exercise 2 — A Corrupted Control Total

Imagine Store 05's point-of-sale system had a glitch and one transaction
was double-submitted. Take `raw-data/store_05.csv` and manually duplicate
the `June 29 2026,BAK-311,15` row, so Store 05's true control total is
now $408.00 instead of $393.00 — but nothing in the data itself flags
this as an error; it just looks like two separate $15 bakery purchases
on the same day.

Run your full pipeline (Prompts 1–2) against the modified file.

Then ask yourself: would your current verification step (section 1.10)
actually catch this? A naive control-total check against the *old*
$393.00 figure would catch it — but only because you happen to already
know the old total. In a real weekly process, you often don't have an
independent "old" total to compare against.

This is the honest limit of control totals: they catch drift from a
*known-correct* number. They don't, by themselves, catch a duplicate
that was already baked into the source data before your model ever saw
it. What additional check would catch a duplicate transaction
specifically? (Hint: think about what a self-verification prompt could
be asked to look for — duplicate rows with identical date, item, and
amount — that a control total alone can't.)

