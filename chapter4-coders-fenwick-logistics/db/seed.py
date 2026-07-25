"""
Seeds db/fenwick.db with sample shipments, including SHIP-1004 — the
timezone-ambiguous one used to reproduce the section 4.5 bug: picked up
late evening Pacific time, which is already the next calendar day UTC.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "fenwick.db"


def build():
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE shipments (
            shipment_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            pickup_utc TEXT NOT NULL,
            transit_days INTEGER NOT NULL,
            carrier TEXT NOT NULL,
            last_updated TEXT NOT NULL
        )
    """)

    shipments = [
        # Ordinary case: pickup and UTC date align with local date
        ("SHIP-1001", "in_transit", "2026-07-01T14:00:00+00:00", 2, "MIDWEST_EXPRESS", "2026-07-01T14:05:00+00:00"),
        # Delivered shipment: estimated_delivery should be null per spec
        ("SHIP-1002", "delivered", "2026-06-28T10:00:00+00:00", 3, "ATLANTIC_LOGISTICS", "2026-07-01T09:00:00+00:00"),
        # Pending shipment
        ("SHIP-1003", "pending", "2026-07-05T12:00:00+00:00", 4, "PACIFIC_FREIGHT", "2026-07-03T08:00:00+00:00"),
        # THE TIMEZONE-AMBIGUOUS CASE (section 4.5 / exercise 1):
        # 2026-07-02T02:15:00 UTC = 2026-07-01T19:15:00 Pacific — still
        # July 1st locally, but already July 2nd in UTC.
        ("SHIP-1004", "in_transit", "2026-07-02T02:15:00+00:00", 2, "PACIFIC_FREIGHT", "2026-07-02T02:20:00+00:00"),
        # Exception case
        ("SHIP-1005", "exception", "2026-06-30T08:00:00+00:00", 2, "MIDWEST_EXPRESS", "2026-07-02T11:00:00+00:00"),
    ]
    cur.executemany(
        "INSERT INTO shipments (shipment_id, status, pickup_utc, transit_days, carrier, last_updated) VALUES (?,?,?,?,?,?)",
        shipments,
    )

    conn.commit()
    conn.close()
    print(f"Seeded {DB_PATH}")


if __name__ == "__main__":
    build()
