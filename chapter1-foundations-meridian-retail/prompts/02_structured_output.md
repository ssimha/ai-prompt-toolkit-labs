# Prompt 2 — Structured Output

Chain this after Prompt 1, or combine into a single prompt once you're
comfortable with both.

```
Return ONLY a JSON array, no explanation before or after it. Each
element must have exactly these fields: "date" (YYYY-MM-DD string),
"store_id" (string), "item_code" (string), "amount_usd" (number,
two decimal places).

Do not include markdown code fences. Do not include any text other
than the JSON array itself.

{CLEANED_ROWS}
```

**Check yourself:** does your model's raw response start with `[` and
end with `]`, with nothing else around it? If it wraps the array in a
code fence or adds a sentence like "Here's your data:", that's the
failure mode section 1.5 describes. Retry with:

```
Your last response wasn't valid JSON. Return only the JSON array,
nothing else.
```
