# Prompt 6 — The Claims Ledger Check (section 2.10)

**Generation, grounded in the ledger:**
```
You may only state factual claims about Northwind that appear in the
claims ledger below. If a persuasive point would benefit from a
statistic or capability not listed here, do not invent one — write
around it or flag the gap instead.

Claims ledger:
{paste the table from claims/claims_ledger.md}

Now write the email described above.
```

**Separate verification pass, run on ANY draft (including ones written
without the ledger constraint):**
```
List every factual claim made in the copy below. For each one, cite
which line in the claims ledger supports it. Flag any claim with no
matching ledger line.

Claims ledger:
{paste the table from claims/claims_ledger.md}

Copy to check:
{paste draft}
```

Test the verification pass against `claims/sample_overclaiming_draft.txt`
— it should flag all 5 issues listed in
`claims/sample_overclaiming_draft.md`. Then run the mechanical first
pass too:
```
python claims/claims_checker.py claims/sample_overclaiming_draft.txt
```
Compare what the rule-based checker catches against what the LLM
verification pass catches — they won't be identical, which is exactly
why section 2.10 recommends both, not just one.
