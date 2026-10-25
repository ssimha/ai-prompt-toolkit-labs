"""
The five agents from Chapter 5, section 5.3-5.4: Classifier, Planner,
Researcher, Drafter, Reviewer. Model tiering follows section 5.11 —
fast/cheap for high-volume low-stakes steps, strongest available for
the Reviewer and Planner.

Swap the model names below for whatever tiers you have access to.
These are recommendations to test, per section 1.12/5.11, not fixed rules.
"""

import json
import os
from .claude_client import call, text_of, tool_calls_of
from .tools import TOOL_SCHEMAS, TOOL_FUNCTIONS

# Defaults can be overridden in your .env file (see .env.example), so if a
# model name is retired or you want to test a different tier, you never
# need to edit code.
MODEL_FAST = os.getenv("MODEL_FAST", "claude-haiku-5-5")        # Classifier: high volume, low individual stakes
MODEL_MID = os.getenv("MODEL_MID", "claude-sonnet-5-5")         # Researcher: moderate stakes, schema-following
MODEL_STRONG = os.getenv("MODEL_STRONG", "claude-sonnet-5-5")   # Drafter: customer-visible output
MODEL_STRONGEST = os.getenv("MODEL_STRONGEST", "claude-opus-5-5")  # Reviewer + Planner: highest-stakes checks


def classify(ticket_text: str) -> dict:
    system = (
        "You are the Classifier agent for a support ticket pipeline. "
        "Return ONLY a JSON object with fields: category "
        "(one of: billing, technical, account, feature_request, outage), "
        "urgency (integer 1-10), description (short restatement of the issue). "
        "No text before or after the JSON."
    )
    resp = call(system=system, user=ticket_text, model=MODEL_FAST, max_tokens=200)
    raw = text_of(resp).strip().strip("`").lstrip("json").strip()
    return json.loads(raw)


def plan_next_step(classification: dict) -> str:
    system = (
        "You are the routing planner for a support ticket pipeline. "
        "Available next steps: research, skip_to_draft, human_escalation. "
        "Rules:\n"
        "- category=outage with urgency >= 8 -> human_escalation\n"
        "- category=account with a simple description (password, email change) -> skip_to_draft\n"
        "- everything else -> research\n"
        "Return ONLY the step name, nothing else."
    )
    resp = call(system=system, user=json.dumps(classification), model=MODEL_STRONGEST, max_tokens=20)
    return text_of(resp).strip()


def research(ticket_text: str, classification: dict) -> dict:
    system = (
        "You are the Researcher agent. Decide which tool(s) to call to gather "
        "the data needed to answer this ticket. Call only what you need."
    )
    user = f"Ticket: {ticket_text}\nClassification: {json.dumps(classification)}"
    resp = call(system=system, user=user, model=MODEL_MID, max_tokens=500, tools=TOOL_SCHEMAS)

    results = {}
    for tc in tool_calls_of(resp):
        fn = TOOL_FUNCTIONS.get(tc["name"])
        if fn:
            results[tc["name"]] = fn(**tc["input"])
    return results


def draft(ticket_text: str, classification: dict, retrieved_data: dict) -> str:
    system = (
        "You are the Drafter agent. Write a helpful, accurate reply to the "
        "customer using ONLY the retrieved data provided — never invent an "
        "amount, date, or account detail not present in it. If the retrieved "
        "data doesn't cover something the customer asked, say a team member "
        "will follow up rather than guessing."
    )
    user = (
        f"Ticket: {ticket_text}\n"
        f"Classification: {json.dumps(classification)}\n"
        f"Retrieved data: {json.dumps(retrieved_data)}"
    )
    resp = call(system=system, user=user, model=MODEL_STRONG, max_tokens=400)
    return text_of(resp)


def review(ticket_text: str, retrieved_data: dict, draft_reply: str) -> dict:
    system = (
        "You are the Reviewer agent. You did not write the draft — your job "
        "is only to check it. Verify: (1) does it address what the customer "
        "asked, (2) does every factual claim match the retrieved data exactly "
        "— list any that don't, (3) is the tone appropriate. "
        "Return ONLY a JSON object with fields: decision "
        "(one of: SEND, SEND_WITH_FLAG, ESCALATE_HUMAN), "
        "unmatched_claims (array of strings, empty if none), "
        "reasoning (short string)."
    )
    user = (
        f"Ticket: {ticket_text}\n"
        f"Retrieved data: {json.dumps(retrieved_data)}\n"
        f"Draft reply: {draft_reply}"
    )
    resp = call(system=system, user=user, model=MODEL_STRONGEST, max_tokens=400)
    raw = text_of(resp).strip().strip("`").lstrip("json").strip()
    return json.loads(raw)
