"""
A real, rule-based claims checker — not an LLM call, deliberately. This
is the mechanical half of section 2.10's verification technique: catch
the obvious, checkable red flags (percentages, customer counts,
absolute language) with plain code before anything reaches a human or
an LLM-based ledger-check pass. It will not catch everything a careful
human or a good LLM claims-check prompt would catch — it's a first
pass, not a replacement for section 2.10's full technique.

Run: python claims/claims_checker.py claims/sample_overclaiming_draft.md
"""

import re
import sys
from pathlib import Path

# Patterns that are near-certain red flags regardless of ledger content —
# these phrase types are listed in claims_ledger.md's "explicitly NOT
# approved" section.
ABSOLUTE_LANGUAGE_PATTERNS = [
    r"\bguarantee[ds]?\b",
    r"\b100%\s*(uptime|guaranteed|satisfaction)\b",
    r"\bnever\s+(goes?\s+down|fails?|breaks?)\b",
    r"\bbest[\s-]in[\s-]class\b",
    r"\b#1\b",
    r"\beverything\b.{0,15}\balready\s+uses?\b",  # "integrates with everything you already use"
]

# Patterns that need a ledger cross-check — a percentage claim, a
# customer-count claim, etc. These aren't automatically wrong, but
# every match must trace to an approved line in the ledger.
NEEDS_LEDGER_CHECK_PATTERNS = [
    (r"\d{1,3}%\s*(faster|more|less|better|improvement|efficient)", "performance percentage claim"),
    (r"\d[\d,]*\+?\s*(customers|companies|users|teams)", "customer count claim"),
    (r"\d{1,3}(\.\d+)?%\s*uptime", "uptime figure"),
    (r"\bSSO\b", "SSO availability claim"),
    (r"\baudit trail\b", "audit trail claim"),
]


def check_draft(text: str) -> dict:
    findings = {"absolute_language_flags": [], "needs_ledger_check": []}

    for pattern in ABSOLUTE_LANGUAGE_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            findings["absolute_language_flags"].append(match.group(0))

    for pattern, label in NEEDS_LEDGER_CHECK_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            findings["needs_ledger_check"].append((label, match.group(0)))

    return findings


def print_report(findings: dict):
    print("=== Claims Checker Report ===\n")

    if findings["absolute_language_flags"]:
        print("DISALLOWED LANGUAGE (flag regardless of ledger):")
        for f in findings["absolute_language_flags"]:
            print(f"  - \"{f}\"")
    else:
        print("No disallowed absolute-language patterns found.")

    print()

    if findings["needs_ledger_check"]:
        print("CLAIMS REQUIRING LEDGER CROSS-CHECK:")
        for label, snippet in findings["needs_ledger_check"]:
            print(f"  - [{label}] \"{snippet}\" — verify this exact figure/claim appears in claims_ledger.md")
    else:
        print("No claims requiring ledger cross-check found.")

    print()
    total = len(findings["absolute_language_flags"]) + len(findings["needs_ledger_check"])
    print(f"Total flags: {total}")
    if total > 0:
        print("This draft needs human review against claims/claims_ledger.md before it ships (section 2.11).")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "claims/sample_overclaiming_draft.md"
    text = Path(path).read_text()
    findings = check_draft(text)
    print_report(findings)
