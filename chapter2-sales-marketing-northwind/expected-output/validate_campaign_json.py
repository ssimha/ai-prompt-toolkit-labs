"""
Validates that generated campaign JSON matches the expected shape from
section 2.7 — the mechanical check you'd run before trusting output
enough to load it into an actual email tool. This is the marketing-
domain equivalent of Chapter 1's control-total check: cheap, automatic,
and catches a malformed-output problem before a human ever looks at it.

Run: python expected-output/validate_campaign_json.py <path_to_json>
"""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "subject": str,
    "body": str,
    "send_delay_days": int,
    "segment_tag": str,
}

MAX_SUBJECT_LENGTH = 60
VALID_SEGMENT_TAGS = {"startup", "mid-market", "enterprise"}


def validate(data) -> list[str]:
    errors = []

    if not isinstance(data, list):
        return ["Top-level JSON must be an array, not an object or other type."]

    if len(data) == 0:
        errors.append("Array is empty — expected at least one email.")

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"Item {i}: expected an object, got {type(item).__name__}")
            continue

        for field, expected_type in REQUIRED_FIELDS.items():
            if field not in item:
                errors.append(f"Item {i}: missing required field '{field}'")
            elif not isinstance(item[field], expected_type):
                errors.append(
                    f"Item {i}: field '{field}' should be {expected_type.__name__}, "
                    f"got {type(item[field]).__name__}"
                )

        if "subject" in item and isinstance(item["subject"], str):
            if len(item["subject"]) > MAX_SUBJECT_LENGTH:
                errors.append(
                    f"Item {i}: subject is {len(item['subject'])} chars, "
                    f"exceeds max of {MAX_SUBJECT_LENGTH}"
                )

        if "segment_tag" in item and item["segment_tag"] not in VALID_SEGMENT_TAGS:
            errors.append(
                f"Item {i}: segment_tag '{item['segment_tag']}' not one of {VALID_SEGMENT_TAGS}"
            )

        if "send_delay_days" in item and isinstance(item["send_delay_days"], int):
            if item["send_delay_days"] < 0:
                errors.append(f"Item {i}: send_delay_days cannot be negative")

    return errors


def try_parse(raw_text: str):
    """
    Mirrors section 2.7's defensive-parse advice: strip common LLM
    output artifacts (code fences, stray whitespace) before giving up.
    """
    cleaned = raw_text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.lstrip("json").strip()
    return json.loads(cleaned)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "expected-output/campaign_schema_example.json"
    raw = Path(path).read_text()

    try:
        data = try_parse(raw)
    except json.JSONDecodeError as e:
        print(f"FAILED TO PARSE: {e}")
        print("This is exactly the malformed-output failure mode section 2.7 warns about.")
        sys.exit(1)

    errors = validate(data)
    if errors:
        print(f"{len(errors)} validation error(s) found:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"Valid. {len(data)} email(s) match the expected schema.")
