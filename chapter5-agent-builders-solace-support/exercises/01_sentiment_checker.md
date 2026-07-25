# Exercise 1 — Add a Sentiment Checker Agent

Add a fifth agent, SentimentChecker, that runs immediately after
Classifier and can override the Planner's routing regardless of
category — an unusually upset customer (all caps, profanity, repeated
contact attempts mentioned in the text) should route straight to
human_escalation even for what would otherwise be a routine ticket.

Implementation notes:
- Add `agents/pipeline_agents.py::check_sentiment(ticket_text) -> dict`
  returning `{"escalate_override": bool, "reason": str}`.
- Wire it into `main.py::run_ticket` between classify() and
  plan_next_step() — if escalate_override is true, skip the planner
  entirely and set the outcome directly, the same way the hard
  keyword guardrail already does.
- Think about model tier: this runs on every single ticket (high
  volume), but a missed escalation here is costly (a very upset
  customer going through the normal automated path). Where does that
  put it in the tiering from section 5.11 — closer to the Classifier
  or closer to the Reviewer?
