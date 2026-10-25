# Exercise 3 — Write Your Own Few-Shot Examples

Starting next week, all eleven Meridian stores will add a new column:
`payment_method`, with values like "card", "cash", "mobile_wallet" —
but each store's POS system will format it differently, the same way
dates currently are (e.g., "CARD", "Card", "credit_card", "CC").

Write your own few-shot prompt, modeled on Prompt 1, that normalizes
`payment_method` into exactly three values: `card`, `cash`, `mobile`.
You'll need to invent 2–3 realistic messy input variants per store the
way this chapter's examples did, then demonstrate the correct output
for each.

This exercise has no answer key. The point is practicing the actual
skill: noticing where real-world data will be inconsistent *before*
you've seen every variant, and writing few-shot examples that
generalize instead of just matching the cases you've already seen.
