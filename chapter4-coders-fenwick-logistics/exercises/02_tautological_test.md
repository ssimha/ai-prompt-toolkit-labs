# Exercise 2 — Catch a Tautological Test

Write a new test for the shipments endpoint using a bare prompt with no
specification, just: "write a test for the shipment status endpoint" —
paste in `app/routes/shipments.py` so the model can see the
implementation directly.

Compare what you get against `tests/test_shipments.py`. Look
specifically for a test that just re-asserts whatever the code happens
to already do — for example, asserting the exact buggy 2026-07-04 date
for SHIP-1004 as if it were correct, with no reference to what the
right answer should actually be.

This is section 4.7's warning made concrete: a test generated from the
implementation, rather than the specification, tends to defend
whatever bugs are already there instead of catching them.
