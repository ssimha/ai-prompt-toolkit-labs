# Exercise 3 — Add a New Endpoint, Using Every Technique in the Chapter

Fenwick needs a new endpoint: `POST /shipments/{shipment_id}/exception`
— for a warehouse worker to report a delivery exception (damaged goods,
address issue, etc.), which should set the shipment's status to
"exception" and log a reason.

Build this from scratch using the full sequence from this chapter:

1. Define the request/response Pydantic models first, in isolation
   (Prompt 1's technique), before any endpoint logic.
2. Write the endpoint using few-shot examples pulled from
   `app/routes/shipments.py` for error handling conventions (Prompt 2).
3. Write tests from the specification above, before or independently
   of the implementation (Prompt 4).
4. Run a code-review checklist pass on the finished endpoint
   (Prompt 5) — add a new checklist item specific to this endpoint:
   does it correctly reject setting a shipment to "exception" if it's
   already marked "delivered"?
5. Decide, and write down your reasoning: does this endpoint need the
   same billing-style human checkpoint treatment as Chapter 5's
   high-value tickets, or is warehouse-reported exception data
   low-stakes enough to skip a mandatory human review before it's
   saved? Justify it using section 4.11's framing, not just intuition.

