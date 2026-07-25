"""
Unlike test_shipments.py, this test file has zero external dependencies
(no FastAPI, no pytest even required — plain assertions) and was
actually run and verified while building this lab. Run it directly:

    python tests/test_delivery_standalone.py

to confirm the bug and fix both behave as the chapter describes, before
you've installed anything else.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.delivery import estimate_delivery_buggy, estimate_delivery_fixed


def test_ordinary_case_bug_and_fix_agree():
    # When pickup's UTC date and local date are the same, bug and fix
    # should agree — the bug only manifests in the boundary case.
    pickup = "2026-07-01T14:00:00+00:00"  # midday UTC, still midday-ish everywhere relevant
    carrier = "MIDWEST_EXPRESS"
    buggy = estimate_delivery_buggy(pickup, 2, carrier)
    fixed = estimate_delivery_fixed(pickup, 2, carrier)
    assert buggy == fixed, f"expected agreement, got buggy={buggy} fixed={fixed}"
    print(f"PASS: ordinary case — both give {fixed}")


def test_boundary_case_bug_and_fix_disagree():
    # SHIP-1004's exact scenario: late-evening Pacific pickup that's
    # already the next day in UTC.
    pickup = "2026-07-02T02:15:00+00:00"
    carrier = "PACIFIC_FREIGHT"
    buggy = estimate_delivery_buggy(pickup, 2, carrier)
    fixed = estimate_delivery_fixed(pickup, 2, carrier)
    assert str(buggy) == "2026-07-04", f"expected buggy=2026-07-04, got {buggy}"
    assert str(fixed) == "2026-07-03", f"expected fixed=2026-07-03, got {fixed}"
    assert buggy != fixed
    print(f"PASS: boundary case — buggy={buggy} (wrong), fixed={fixed} (correct)")


def test_unknown_carrier_raises():
    try:
        estimate_delivery_fixed("2026-07-01T14:00:00+00:00", 2, "NOT_A_REAL_CARRIER")
        assert False, "should have raised ValueError"
    except ValueError:
        print("PASS: unknown carrier raises ValueError as expected")


if __name__ == "__main__":
    test_ordinary_case_bug_and_fix_agree()
    test_boundary_case_bug_and_fix_disagree()
    test_unknown_carrier_raises()
    print("\nAll standalone delivery tests passed.")
