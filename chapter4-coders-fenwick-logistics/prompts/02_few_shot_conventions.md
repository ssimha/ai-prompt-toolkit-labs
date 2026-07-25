# Prompt 2 — Few-Shot Codebase Conventions (section 4.4)

Once the contract is approved, use this to generate error handling that
matches Fenwick's existing pattern — pull the real example straight
from `app/routes/shipments.py`.

```
Match this existing error-handling pattern used elsewhere in the
codebase. Example from another endpoint:

if shipment is None:
    raise APIError(code="SHIPMENT_NOT_FOUND", status_code=404,
                   detail=f"No shipment with id {shipment_id}")

Now write the not-found and invalid-carrier error cases for the new
shipment status endpoint using this exact same pattern.
```

Check your model's output against the actual `APIError` calls in
`app/routes/shipments.py` — same fields, same structure, no bare
`HTTPException` calls mixed in.
