# Prompt 3 — Chain-of-Thought Debugging (section 4.5)

This is the prompt for Exercise 1. Do not look at `app/delivery.py`'s
`estimate_delivery_fixed` function until you've tried this.

```
Here is the estimated_delivery calculation logic and three example
cases where the output was off by one day. Work through this
systematically:
1. Trace the timezone handling at each step of the calculation.
2. Identify where a date conversion could shift by one day depending
   on timezone.
3. Check whether the three example cases share a common carrier or
   region that would explain the pattern.
4. State your hypothesis and what evidence in the code supports it,
   before proposing a fix.
```

Paste in `estimate_delivery_buggy` from `app/delivery.py`, plus this
case:

```
pickup_utc: 2026-07-02T02:15:00+00:00
carrier: PACIFIC_FREIGHT
transit_days: 2
Buggy result: 2026-07-04
```

A correct diagnosis should identify that `pickup_dt.date()` extracts
the UTC calendar date instead of the carrier's local calendar date —
and for a pickup late in the evening Pacific time, that's already the
next day in UTC. Compare the model's hypothesis and proposed fix
against `estimate_delivery_fixed` in the same file.

