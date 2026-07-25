"""
Estimated-delivery calculation for shipments — including the deliberate
off-by-one timezone bug from Chapter 4, section 4.5, and the fix.

Ship dates are stored as UTC ISO datetimes (as they'd come from a
carrier's API). The bug: taking the UTC date directly, instead of
converting to the carrier's local timezone first, before adding transit
days. For a shipment picked up late in the evening local time — which
is already the next day in UTC — this produces a delivery estimate one
day later than it should be.

Exercise 1 asks you to reproduce this bug using the chain-of-thought
diagnostic prompt from prompts/03_chain_of_thought_debugging.md before
looking at estimate_delivery_fixed below.
"""

from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo

CARRIER_TIMEZONES = {
    "PACIFIC_FREIGHT": "America/Los_Angeles",
    "MIDWEST_EXPRESS": "America/Chicago",
    "ATLANTIC_LOGISTICS": "America/New_York",
}


def estimate_delivery_buggy(pickup_utc_iso: str, transit_days: int, carrier: str) -> date:
    """
    BUGGY VERSION — kept here on purpose for the Chapter 4 lab.
    Takes the UTC date directly without converting to the carrier's
    local timezone first.
    """
    pickup_dt = datetime.fromisoformat(pickup_utc_iso)
    pickup_date_utc = pickup_dt.date()  # <-- bug: this is the UTC date, not local
    return pickup_date_utc + timedelta(days=transit_days)


def estimate_delivery_fixed(pickup_utc_iso: str, transit_days: int, carrier: str) -> date:
    """
    FIXED VERSION — converts to the carrier's local timezone before
    extracting the date, so a late-evening local pickup that's already
    "tomorrow" in UTC is correctly treated as today, locally.
    """
    tz_name = CARRIER_TIMEZONES.get(carrier)
    if tz_name is None:
        raise ValueError(f"Unknown carrier: {carrier}")

    pickup_dt_utc = datetime.fromisoformat(pickup_utc_iso)
    if pickup_dt_utc.tzinfo is None:
        raise ValueError("pickup_utc_iso must be timezone-aware (include UTC offset)")

    pickup_dt_local = pickup_dt_utc.astimezone(ZoneInfo(tz_name))
    pickup_date_local = pickup_dt_local.date()
    return pickup_date_local + timedelta(days=transit_days)
