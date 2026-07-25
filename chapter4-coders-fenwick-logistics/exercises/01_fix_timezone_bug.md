# Exercise 1 — Fix the Timezone Bug for Real

`app/routes/shipments.py` currently imports and uses
`estimate_delivery_buggy` from `app/delivery.py` on purpose.

1. Run `python tests/test_delivery_standalone.py` first — no other
   dependencies needed — and confirm you see the bug and fix disagree
   on SHIP-1004's scenario (2026-07-04 vs. 2026-07-03).
2. Use `prompts/03_chain_of_thought_debugging.md` against a model of
   your choice, without looking at `estimate_delivery_fixed` first,
   and see if it independently arrives at the same diagnosis.
3. Edit `app/routes/shipments.py` to import and use
   `estimate_delivery_fixed` instead, passing the carrier correctly.
4. Update `tests/test_shipments.py::test_timezone_bug_case_ship_1004`
   — change the asserted date from `"2026-07-04"` to `"2026-07-03"`,
   and update the docstring/comment since it's no longer describing a
   known bug.
5. If you have `fastapi`, `pydantic`, and `pytest` installed, run the
   full suite with `pytest tests/test_shipments.py -v` and confirm
   everything passes against the fixed endpoint.
