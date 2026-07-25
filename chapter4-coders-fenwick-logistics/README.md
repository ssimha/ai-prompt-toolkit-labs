# Chapter 4 Lab — Fenwick Logistics Shipment API

A working FastAPI project implementing the shipment-tracking endpoint
from Chapter 4 (Coders), including a genuinely reproducible bug (not
just a described one) for Exercise 1.

## What's actually real here vs. described

- **Real and tested in this repo already**: the timezone bug and its
  fix in `app/delivery.py` — `tests/test_delivery_standalone.py` has
  zero external dependencies and was run and verified while this lab
  was built. Run it yourself right now with just `python3`, no install
  needed:
  ```
  python tests/test_delivery_standalone.py
  ```
- **Real, but needs your own install**: the full FastAPI app, its
  endpoint, and `tests/test_shipments.py` — these need `fastapi`,
  `pydantic`, `pytest`, and `httpx` installed. They're written
  correctly against current FastAPI/Pydantic v2 conventions, but
  weren't executed in the environment this repo was built in (no
  internet access there) — you'll be the first to actually run them
  end to end.

## Setup

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Seed the database:**
   ```
   python db/seed.py
   ```
   Creates `db/fenwick.db` with five sample shipments, including
   SHIP-1004 — the timezone-ambiguous one.

3. **Run the app:**
   ```
   uvicorn app.main:app --reload
   ```
   Then try `GET http://localhost:8000/shipments/SHIP-1004` and compare
   the `estimated_delivery` field against what
   `test_delivery_standalone.py` told you to expect.

4. **Run the full test suite:**
   ```
   pytest tests/test_shipments.py -v
   ```

5. **Run the type checker:**
   ```
   mypy app/
   ```

## Sample shipments (seeded by db/seed.py)

| ID | Status | Notes |
|---|---|---|
| SHIP-1001 | in_transit | ordinary case |
| SHIP-1002 | delivered | estimated_delivery should be null |
| SHIP-1003 | pending | ordinary case |
| SHIP-1004 | in_transit | **the timezone bug case — see Exercise 1** |
| SHIP-1005 | exception | |

## Working through the chapter

Go through `prompts/` in order (01 through 05) — each corresponds
directly to a numbered section in Chapter 4. Then move to `exercises/`:

1. **Fix the timezone bug for real** — the endpoint currently uses the
   buggy calculation on purpose; make it use the fixed one and update
   the test that documents this.
2. **Catch a tautological test** — generate a test from the
   implementation instead of the spec, and see it defend the bug
   instead of catching it.
3. **Build a new endpoint from scratch** — apply every technique in
   the chapter to a feature that doesn't exist yet.

## Project structure

```
app/
  main.py          FastAPI app + router registration
  models.py        The approved Pydantic contract (section 4.3)
  errors.py        APIError + shared exception handler (section 4.4's convention)
  db.py            Real SQLite queries — no fake/invented data
  delivery.py      The timezone bug AND the fix, both included on purpose
  routes/
    shipments.py   The existing endpoint, using the buggy calculation
db/
  seed.py          Seeds fenwick.db with 5 sample shipments
tests/
  test_delivery_standalone.py   Zero-dependency, already verified
  test_shipments.py             Full endpoint tests, needs fastapi/pytest installed
prompts/           The five prompts from the chapter, paste-ready
exercises/         Three exercises, referenced above
```

