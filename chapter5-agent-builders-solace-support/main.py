"""
The orchestrator: a plain deterministic Python controller (section 5.4 —
"a simple, deterministic orchestrator is often the right choice when the
sequence is fixed") that calls the Planner only for the routing decision
it can't easily hardcode, and enforces the guardrails from section 5.10
in code rather than trusting a prompt to remember them.

Run: python main.py data/sample_tickets.json
"""

import json
import sys
import uuid
from datetime import datetime
from pathlib import Path

from agents.pipeline_agents import classify, plan_next_step, research, draft, review

LOG_PATH = Path(__file__).parent / "logs" / "pipeline_trace.jsonl"

# --- Guardrails enforced in code, not prompt wording (section 5.10) ---
HARD_ESCALATION_KEYWORDS = ["legal action", "lawsuit", "data privacy", "gdpr", "sue"]
BILLING_ESCALATION_THRESHOLD_USD = 500


def log_step(ticket_id: str, step: str, payload: dict):
    LOG_PATH.parent.mkdir(exist_ok=True)
    entry = {
        "ticket_id": ticket_id,
        "step": step,
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload,
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")


def contains_hard_escalation_keyword(text: str) -> bool:
    lowered = text.lower()
    return any(kw in lowered for kw in HARD_ESCALATION_KEYWORDS)


def run_ticket(ticket: dict) -> dict:
    ticket_id = ticket.get("id", str(uuid.uuid4()))
    text = ticket["text"]
    customer_id = ticket["customer_id"]

    state = {"ticket_id": ticket_id, "customer_id": customer_id, "ticket_text": text}

    # Hard guardrail: legal/privacy language bypasses the whole pipeline,
    # before the Classifier's output is even used (section 5.10).
    if contains_hard_escalation_keyword(text):
        state["outcome"] = "ESCALATE_HUMAN"
        state["reason"] = "hard_guardrail_keyword_match"
        log_step(ticket_id, "guardrail_escalation", state)
        return state

    classification = classify(text)
    state["classification"] = classification
    log_step(ticket_id, "classify", classification)

    next_step = plan_next_step(classification)
    # Defensive fallback: the Planner can occasionally return something
    # outside the three valid steps (e.g. an empty string if its response
    # got cut off mid-thinking before any visible answer text). Treat
    # that as "research" rather than silently skipping data retrieval —
    # fail toward gathering more data, not less.
    if next_step not in ("research", "skip_to_draft", "human_escalation"):
        log_step(ticket_id, "plan_fallback", {"raw_next_step": next_step, "fallback_to": "research"})
        next_step = "research"
    state["planned_step"] = next_step
    log_step(ticket_id, "plan", {"next_step": next_step})

    if next_step == "human_escalation":
        state["outcome"] = "ESCALATE_HUMAN"
        state["reason"] = "planner_routed_to_human"
        return state

    retrieved_data = {}
    if next_step == "research":
        retrieved_data = research(text, classification, customer_id)
        state["retrieved_data"] = retrieved_data
        log_step(ticket_id, "research", retrieved_data)

    # Hard guardrail: high-value billing disputes always get human eyes,
    # regardless of how confident the Reviewer sounds (section 5.9).
    if classification.get("category") == "billing":
        amounts = [
            inv.get("amount_usd", 0)
            for inv in retrieved_data.get("get_invoice_history", [])
        ]
        if amounts and max(amounts) > BILLING_ESCALATION_THRESHOLD_USD:
            state["outcome"] = "ESCALATE_HUMAN"
            state["reason"] = f"billing_over_threshold_${max(amounts)}"
            log_step(ticket_id, "guardrail_escalation", state)
            return state

    draft_reply = draft(text, classification, retrieved_data)
    state["draft_reply"] = draft_reply
    log_step(ticket_id, "draft", {"draft_reply": draft_reply})

    review_result = review(text, retrieved_data, draft_reply)
    state["review"] = review_result
    log_step(ticket_id, "review", review_result)
    state["outcome"] = review_result["decision"]

    return state


def main(tickets_path: str):
    tickets = json.loads(Path(tickets_path).read_text())
    results = []
    for ticket in tickets:
        print(f"--- Processing {ticket['id']} ---")
        result = run_ticket(ticket)
        print(f"Outcome: {result['outcome']}\n")
        results.append(result)

    out_path = Path(__file__).parent / "logs" / "run_results.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"Full results written to {out_path}")


if __name__ == "__main__":
    tickets_file = sys.argv[1] if len(sys.argv) > 1 else "data/sample_tickets.json"
    main(tickets_file)
