# Exercise 2 — Break the Researcher's Tool Discipline on Purpose

Temporarily edit the Researcher's system prompt in
`agents/pipeline_agents.py::research()` to remove the sentence "Call
only what you need." Run TICKET-001 (the duplicate billing charge)
again several times.

Watch what happens to the tool calls it makes — does it start calling
get_error_logs or get_account_status for a ticket that's purely about
a billing duplicate? Check `logs/pipeline_trace.jsonl` to see exactly
what was called and with what arguments.

This is section 5.7's "tool misuse" failure mode, reproduced on
purpose. Restore the original prompt afterward and confirm the
unnecessary calls stop.

