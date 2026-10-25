# Exercise 3 — Engineer a Case Where Self-Consistency Runs Disagree

Section 3.5's example (Prompt 3) uses data where the top drivers are
fairly clear-cut (Texas and Ohio dominate). Modify the subsidiary
breakdown so that three or four subsidiaries have very similar dollar
contributions to the change — close enough that which ones count as
"top 3" could reasonably vary run to run.

1. Adjust the numbers in a copy of the subsidiary breakdown from
   Prompt 2 so that, say, four subsidiaries each contribute between
   $30K and $35K to the change (recompute variance_pct accordingly —
   you can use `ledger/reconcile.py`'s approach as a reference for how
   to keep the totals consistent).
2. Run the self-consistency prompt (Prompt 3) three times against this
   modified data.
3. Do your three runs actually disagree on which subsidiaries make the
   "top 3"? If they do, that's the self-consistency check doing its
   job — flagging genuine ambiguity in close-call rankings. If they
   don't disagree even with genuinely close numbers, consider whether
   the model might be anchoring on the order data was presented in,
   rather than re-deriving the ranking each time — worth testing by
   shuffling the subsidiary order between runs.
