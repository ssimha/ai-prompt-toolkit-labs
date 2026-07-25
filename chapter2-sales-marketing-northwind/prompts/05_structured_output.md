# Prompt 5 — Structured Output for Campaign Data (section 2.7)

```
Return ONLY a JSON array, no explanation before or after it. Each
element must have exactly these fields: "subject" (string, under 60
chars), "body" (string), "send_delay_days" (integer), "segment_tag"
(string).

Do not include markdown code fences. Do not include any text other
than the JSON array itself.

Generate this for a 5-email enterprise nurture sequence.
```

Validate your output against the schema:
```
python expected-output/validate_campaign_json.py <path_to_your_output.json>
```

If your model wraps the output in a code fence or adds a sentence
before/after it despite the instruction, that's the exact failure mode
section 2.7 describes — retry with: "Your last response wasn't valid
JSON. Return only the JSON array, nothing else."

