# Exercise 3 — Design Escalation Rules for a New Category

Solace is adding a new ticket category: "security" (suspected account
compromise, suspicious login activity, requests to disable 2FA).

Design and implement the routing and guardrail rules for this category
in `main.py`, following the pattern of the existing billing threshold
and hard-keyword guardrails. Consider:

- Should "security" tickets ever be allowed to reach the Drafter
  and go out automatically, or should every one of them hit
  human_escalation unconditionally? Justify your answer using the
  cost-of-being-wrong framing from section 5.9.
- If you do allow some security tickets to be auto-handled (e.g., a
  routine "how do I enable 2FA" question), how does your Classifier
  or Planner tell that apart from an actual compromise report?

