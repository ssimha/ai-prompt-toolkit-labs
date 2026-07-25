"""
Builds db/mock_data.db from scratch with realistic, fully invented data:
invoices, error logs, and account statuses for a handful of customers.

This is the "real system" the Researcher agent's tools query against —
per section 5.5, a tool call must hit real data, never a model-generated
guess. Run this once before using the pipeline.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "mock_data.db"


def build():
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE invoices (
            id INTEGER PRIMARY KEY,
            customer_id TEXT NOT NULL,
            invoice_date TEXT NOT NULL,
            amount_usd REAL NOT NULL,
            status TEXT NOT NULL,
            description TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE error_logs (
            id INTEGER PRIMARY KEY,
            customer_id TEXT NOT NULL,
            event_date TEXT NOT NULL,
            error_code TEXT NOT NULL,
            message TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE account_status (
            customer_id TEXT PRIMARY KEY,
            plan TEXT NOT NULL,
            status TEXT NOT NULL,
            since TEXT NOT NULL,
            seats INTEGER NOT NULL
        )
    """)

    invoices = [
        ("CUST-88213", "2026-03-01", 149.00, "paid", "March subscription - Team plan"),
        ("CUST-88213", "2026-03-01", 149.00, "paid", "March subscription - Team plan (duplicate charge)"),
        ("CUST-88213", "2026-02-01", 149.00, "paid", "February subscription - Team plan"),
        ("CUST-88213", "2026-01-01", 149.00, "paid", "January subscription - Team plan"),
        ("CUST-40522", "2026-03-05", 49.00, "paid", "March subscription - Starter plan"),
        ("CUST-40522", "2026-02-05", 49.00, "paid", "February subscription - Starter plan"),
        ("CUST-77190", "2026-03-10", 899.00, "overdue", "March subscription - Enterprise plan"),
        ("CUST-77190", "2026-02-10", 899.00, "paid", "February subscription - Enterprise plan"),
    ]
    cur.executemany(
        "INSERT INTO invoices (customer_id, invoice_date, amount_usd, status, description) VALUES (?,?,?,?,?)",
        invoices,
    )

    error_logs = [
        ("CUST-77190", "2026-07-01T14:22:00", "SYNC_TIMEOUT", "Integration sync to Salesforce timed out after 30s"),
        ("CUST-77190", "2026-07-01T14:25:00", "SYNC_TIMEOUT", "Integration sync to Salesforce timed out after 30s"),
        ("CUST-77190", "2026-07-01T15:00:00", "SYNC_FAILED", "Integration sync failed: invalid auth token"),
        ("CUST-40522", "2026-06-28T09:10:00", "LOGIN_FAILED", "Password reset link expired"),
    ]
    cur.executemany(
        "INSERT INTO error_logs (customer_id, event_date, error_code, message) VALUES (?,?,?,?)",
        error_logs,
    )

    accounts = [
        ("CUST-88213", "Team", "active", "2025-09-12", 8),
        ("CUST-40522", "Starter", "active", "2026-01-20", 1),
        ("CUST-77190", "Enterprise", "past_due", "2024-03-01", 120),
    ]
    cur.executemany(
        "INSERT INTO account_status (customer_id, plan, status, since, seats) VALUES (?,?,?,?,?)",
        accounts,
    )

    conn.commit()
    conn.close()
    print(f"Seeded {DB_PATH}")


if __name__ == "__main__":
    build()
