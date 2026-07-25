"""
Reconciles an AI-generated (or hand-entered) financial claim against the
real general ledger export, to the cent — section 3.10's mechanical
verification step. This does real currency conversion using the actual
FX rates in gl_export.csv; it does not trust any pre-computed total
handed to it.

Run: python ledger/reconcile.py ledger/sample_ai_claim.json
"""

import csv
import json
import sys
from pathlib import Path

GL_PATH = Path(__file__).parent / "gl_export.csv"
TOLERANCE_USD = 0.01  # to the cent, per section 3.10's "however small" rule


def load_gl():
    rows = list(csv.DictReader(open(GL_PATH)))
    per_sub = {}
    q1_total = 0.0
    q2_total = 0.0
    for r in rows:
        q1_usd = round(float(r["q1_cogs_local"]) * float(r["fx_rate_to_usd_q1"]), 2)
        q2_usd = round(float(r["q2_cogs_local"]) * float(r["fx_rate_to_usd_q2"]), 2)
        per_sub[r["subsidiary"]] = {"q1_usd": q1_usd, "q2_usd": q2_usd}
        q1_total += q1_usd
        q2_total += q2_usd
    return {
        "per_subsidiary": per_sub,
        "q1_total_usd": round(q1_total, 2),
        "q2_total_usd": round(q2_total, 2),
    }


def reconcile(claim: dict, gl: dict) -> list[str]:
    """
    claim is expected to look like:
    {
        "metric": "COGS",
        "current_quarter_usd": ...,
        "prior_quarter_usd": ...,
        "variance_pct": ...,
        "subsidiary_breakdown": {  # optional
            "Ohio": {"q1_usd": ..., "q2_usd": ...},
            ...
        }
    }
    """
    issues = []

    claimed_q2 = claim.get("current_quarter_usd")
    claimed_q1 = claim.get("prior_quarter_usd")

    if claimed_q2 is None or claimed_q1 is None:
        return ["Claim is missing current_quarter_usd or prior_quarter_usd."]

    q2_diff = round(abs(claimed_q2 - gl["q2_total_usd"]), 2)
    q1_diff = round(abs(claimed_q1 - gl["q1_total_usd"]), 2)

    if q2_diff > TOLERANCE_USD:
        issues.append(
            f"Q2 TOTAL MISMATCH: claimed ${claimed_q2:,.2f}, "
            f"actual GL total is ${gl['q2_total_usd']:,.2f} "
            f"(difference: ${q2_diff:,.2f})"
        )
    if q1_diff > TOLERANCE_USD:
        issues.append(
            f"Q1 TOTAL MISMATCH: claimed ${claimed_q1:,.2f}, "
            f"actual GL total is ${gl['q1_total_usd']:,.2f} "
            f"(difference: ${q1_diff:,.2f})"
        )

    claimed_variance = claim.get("variance_pct")
    if claimed_variance is not None:
        actual_variance = round(
            (gl["q2_total_usd"] - gl["q1_total_usd"]) / gl["q1_total_usd"] * 100, 2
        )
        if round(abs(claimed_variance - actual_variance), 2) > 0.05:
            issues.append(
                f"VARIANCE % MISMATCH: claimed {claimed_variance}%, "
                f"actual is {actual_variance}%"
            )

    # If a subsidiary breakdown was included, check each one too —
    # this is where a rate-confusion or double-count error at the
    # subsidiary level shows up even if it happens to net out at the
    # consolidated total.
    breakdown = claim.get("subsidiary_breakdown", {})
    for sub_name, claimed_vals in breakdown.items():
        actual = gl["per_subsidiary"].get(sub_name)
        if actual is None:
            issues.append(f"Unknown subsidiary in claim: '{sub_name}'")
            continue
        for period in ("q1_usd", "q2_usd"):
            if period not in claimed_vals:
                continue
            diff = round(abs(claimed_vals[period] - actual[period]), 2)
            if diff > TOLERANCE_USD:
                issues.append(
                    f"{sub_name} {period.upper()} MISMATCH: claimed "
                    f"${claimed_vals[period]:,.2f}, actual ${actual[period]:,.2f} "
                    f"(difference: ${diff:,.2f})"
                )

    return issues


if __name__ == "__main__":
    claim_path = sys.argv[1] if len(sys.argv) > 1 else "ledger/sample_ai_claim.json"
    claim = json.loads(Path(claim_path).read_text())
    gl = load_gl()

    print("=== Reconciliation Report ===\n")
    print(f"GL Q1 total (ground truth): ${gl['q1_total_usd']:,.2f}")
    print(f"GL Q2 total (ground truth): ${gl['q2_total_usd']:,.2f}\n")

    issues = reconcile(claim, gl)
    if not issues:
        print("Claim reconciles exactly to the general ledger. No discrepancies found.")
    else:
        print(f"{len(issues)} discrepancy(ies) found \u2014 per section 3.10, none of these get rounded away:\n")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
