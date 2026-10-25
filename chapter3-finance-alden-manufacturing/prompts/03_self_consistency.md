# Prompt 3 — Self-Consistency Prompting (section 3.5)

Run this three separate times (fresh conversations, or explicitly
asking the model to reason independently each time):

```
Run this variance analysis independently, without seeing any prior
attempt. Identify the top 3 drivers of the COGS increase (using the
subsidiary breakdown from Prompt 2) and estimate each driver's dollar
contribution.
```

After collecting all three runs, ask:

```
Here are three independent variance analyses of the same data:
Run 1: {paste}
Run 2: {paste}
Run 3: {paste}

Compare them: which drivers appeared in all three? Which dollar
estimates were consistent versus divergent? Flag any driver that
appeared in only one of the three runs as lower confidence.
```

Given the actual data, Texas and Ohio should reliably appear as the
top two drivers across all three runs — if your three runs disagree on
that, something about the prompt or model is producing unstable
reasoning worth investigating before you trust it further. See
exercises/03_self_consistency_disagreement.md for a case engineered to
actually produce disagreement.
