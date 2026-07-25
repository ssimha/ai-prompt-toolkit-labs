# Prompt 5 — Code Review Checklist (section 4.8)

```
Review the shipment status endpoint code below against this
checklist. For each item, answer yes/no and explain briefly:
1. Does every database query use parameterized queries (no raw string
   interpolation into SQL)?
2. Is every external input validated before use?
3. Are all error paths covered by the APIError pattern, not bare
   exceptions?
4. Does the response match the approved Pydantic model exactly?

Do not just say the code looks fine — check each point explicitly
against the actual code shown.
```

Paste in `app/routes/shipments.py` and `app/db.py`. A thorough review
should flag that `estimate_delivery_buggy` is being used instead of
`estimate_delivery_fixed` — even though that's not on the checklist
verbatim, it's the kind of thing point 4 (response correctness) should
catch. If your model doesn't flag it, that's worth noticing: it's the
exact self-verification blind spot section 4.8 warns about.

