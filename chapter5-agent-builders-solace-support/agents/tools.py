"""
Tools available to the Researcher agent. Each function queries the real
SQLite database — this is what section 5.5 means by "a tool call must
genuinely execute against real data." The model never sees a chance to
fill in a plausible-looking result on its own; it only ever sees what
these functions actually return.
"""

import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path(__file__).parent.parent / "db" / "mock_data.db"


def _connect():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"{DB_PATH} not found. Run `python db/seed.py` first."
        )
    return sqlite3.connect(DB_PATH)


def get_invoice_history(customer_id: str, months: int = 3) -> list[dict]:
    """Return invoices for a customer from the last `months` months."""
    cutoff = (datetime.now() - timedelta(days=30 * months)).strftime("%Y-%m-%d")
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT invoice_date, amount_usd, status, description
           FROM invoices
           WHERE customer_id = ? AND invoice_date >= ?
           ORDER BY invoice_date DESC""",
        (customer_id, cutoff),
    )
    rows = cur.fetchall()
    conn.close()
    return [
        {"invoice_date": r[0], "amount_usd": r[1], "status": r[2], "description": r[3]}
        for r in rows
    ]


def get_error_logs(customer_id: str, since: str = "2026-01-01") -> list[dict]:
    """Return error log events for a customer since a given ISO date."""
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT event_date, error_code, message
           FROM error_logs
           WHERE customer_id = ? AND event_date >= ?
           ORDER BY event_date DESC""",
        (customer_id, since),
    )
    rows = cur.fetchall()
    conn.close()
    return [{"event_date": r[0], "error_code": r[1], "message": r[2]} for r in rows]


def get_account_status(customer_id: str) -> dict | None:
    """Return the account status record for a customer, or None if unknown."""
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT plan, status, since, seats FROM account_status WHERE customer_id = ?",
        (customer_id,),
    )
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return {"plan": row[0], "status": row[1], "since": row[2], "seats": row[3]}


# Tool schemas in Anthropic's function-calling format, for use by the
# Researcher agent when it decides which tools to call.
TOOL_SCHEMAS = [
    {
        "name": "get_invoice_history",
        "description": "Get a customer's invoice history for the last N months.",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "string"},
                "months": {"type": "integer", "description": "How many months back to look"},
            },
            "required": ["customer_id"],
        },
    },
    {
        "name": "get_error_logs",
        "description": "Get error log events for a customer since a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "string"},
                "since": {"type": "string", "description": "ISO date, e.g. 2026-06-01"},
            },
            "required": ["customer_id"],
        },
    },
    {
        "name": "get_account_status",
        "description": "Get a customer's current plan, status, and seat count.",
        "input_schema": {
            "type": "object",
            "properties": {"customer_id": {"type": "string"}},
            "required": ["customer_id"],
        },
    },
]

TOOL_FUNCTIONS = {
    "get_invoice_history": get_invoice_history,
    "get_error_logs": get_error_logs,
    "get_account_status": get_account_status,
}
