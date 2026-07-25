"""
Written from the specification (section 4.7's prompt), not by reading
the implementation first — that's what makes these tests an independent
check rather than an echo of whatever the code already does.

Spec:
- 404 if shipment_id doesn't exist
- 200 with status one of the four valid enum values
- estimated_delivery is null for status="delivered"
- estimated_delivery is a valid date for status="in_transit" or "pending"

Requires: pip install -r requirements.txt (fastapi, pydantic, pytest,
httpx are not available in the sandbox this repo was built in — these
tests are written correctly but were not executed here; run them
yourself after installing dependencies).
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_unknown_shipment_returns_404():
    resp = client.get("/shipments/SHIP-DOES-NOT-EXIST")
    assert resp.status_code == 404
    body = resp.json()
    assert body["error_code"] == "SHIPMENT_NOT_FOUND"


def test_known_shipment_returns_valid_status():
    resp = client.get("/shipments/SHIP-1001")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] in ("pending", "in_transit", "delivered", "exception")


def test_delivered_shipment_has_null_estimated_delivery():
    resp = client.get("/shipments/SHIP-1002")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "delivered"
    assert body["estimated_delivery"] is None


def test_in_transit_shipment_has_a_date():
    resp = client.get("/shipments/SHIP-1001")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "in_transit"
    assert body["estimated_delivery"] is not None


def test_pending_shipment_has_a_date():
    resp = client.get("/shipments/SHIP-1003")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "pending"
    assert body["estimated_delivery"] is not None


def test_timezone_bug_case_ship_1004():
    """
    This test currently documents the BUGGY behavior (section 4.5).
    SHIP-1004 is picked up at 2026-07-02T02:15:00 UTC, which is
    2026-07-01T19:15:00 Pacific — still July 1st locally. The buggy
    calculation returns 2026-07-04; the correct answer (once you fix
    the endpoint to use estimate_delivery_fixed) is 2026-07-03.

    Exercise 1 asks you to update this test's assertion once you've
    applied the fix, and confirm it then fails against the buggy
    version and passes against the fixed one.
    """
    resp = client.get("/shipments/SHIP-1004")
    assert resp.status_code == 200
    body = resp.json()
    # This currently reflects the KNOWN BUG. Fix the endpoint, then
    # change this assertion to "2026-07-03" and confirm it passes.
    assert body["estimated_delivery"] == "2026-07-04"
