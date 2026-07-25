"""
Real SQLite queries against the shipments table — no in-memory fake,
same principle as Chapter 5's tools.py: what the endpoint returns
should come from real data, not something a model filled in.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "fenwick.db"


def _connect():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"{DB_PATH} not found. Run `python db/seed.py` first.")
    return sqlite3.connect(DB_PATH)


def get_shipment(shipment_id: str) -> dict | None:
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT shipment_id, status, pickup_utc, transit_days, carrier, last_updated
           FROM shipments WHERE shipment_id = ?""",
        (shipment_id,),
    )
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return {
        "shipment_id": row[0],
        "status": row[1],
        "pickup_utc": row[2],
        "transit_days": row[3],
        "carrier": row[4],
        "last_updated": row[5],
    }
