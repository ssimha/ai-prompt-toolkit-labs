# Prompt 1 — Structured Contract First (section 4.3)

Use this before asking for any endpoint implementation.

```
Define Pydantic models for a shipment status response. Fields:
shipment_id (str), status (one of: "pending", "in_transit",
"delivered", "exception"), estimated_delivery (date, nullable),
last_updated (datetime), carrier (str).

Return ONLY the Pydantic model code, no endpoint implementation yet,
no explanation.
```

Compare what you get against `app/models.py` in this repo. Review the
contract on its own — field types, nullability, the enum — before
moving on to Prompt 2. This is the point of the chapter: catching a
wrong field type here is far easier than catching it once it's buried
inside a working-looking endpoint.

