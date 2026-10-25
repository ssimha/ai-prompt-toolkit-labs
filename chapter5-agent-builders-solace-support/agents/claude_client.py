"""
Thin wrapper around the Anthropic client so every agent authenticates
and logs the same way. Requires ANTHROPIC_API_KEY to be set — copy
.env.example to .env and add your own key before running anything here.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv()

_client = None


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY not set. Copy .env.example to .env "
                "and add your own key from https://console.anthropic.com/settings/keys"
            )
        _client = anthropic.Anthropic(api_key=api_key)
    return _client


def call(system: str, user: str, model: str = os.getenv("MODEL_STRONG", "claude-sonnet-5-5"),
         max_tokens: int = 1000, temperature: float = 0.0,
         tools: list | None = None) -> anthropic.types.Message:
    """
    Single-turn call to Claude. Kept deliberately simple — no retry
    logic, no streaming — since the point of this lab is the agent
    design, not a production HTTP client. Add retries yourself if you
    extend this for real use, per section 1.5's retry-on-malformed-
    output pattern.
    """
    client = get_client()
    kwargs = dict(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    if tools:
        kwargs["tools"] = tools
    return client.messages.create(**kwargs)


def text_of(message: anthropic.types.Message) -> str:
    """Extract concatenated text content from a Claude response."""
    return "".join(block.text for block in message.content if block.type == "text")


def tool_calls_of(message: anthropic.types.Message) -> list[dict]:
    """Extract tool_use blocks from a Claude response, if any."""
    return [
        {"name": block.name, "input": block.input, "id": block.id}
        for block in message.content
        if block.type == "tool_use"
    ]
