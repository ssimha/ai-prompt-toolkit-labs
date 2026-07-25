# Prompt 4 — Test Generation From Specification (section 4.7)

```
Write pytest tests for a shipment status endpoint with this
specification (not the implementation — you have not seen it):
- Returns 404 if shipment_id doesn't exist
- Returns 200 with status one of the four valid enum values
- estimated_delivery is null for status="delivered" shipments
- estimated_delivery is a valid future date for status="in_transit"

Write tests against this specification. Do not assume any particular
implementation detail beyond what's stated above.
```

Compare what you get against `tests/test_shipments.py`. Notice that
file was written the same way — from the spec, not from reading
`shipments.py` first — which is why it's able to catch the timezone
bug in `test_timezone_bug_case_ship_1004` rather than just confirming
whatever the code already does.

