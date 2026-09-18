# 08 — Feedback, Learning and Product Evaluation

## Purpose

Measure whether the AI product improves outcomes and convert feedback into trustworthy improvement evidence.

## Product metrics

Measure task completion, accepted/corrected output, time saved, resolution, escalation, abandonment, repeat use, critical error and downstream outcome where appropriate.

Chat count and token consumption are activity metrics, not value.

## Feedback signals

Thumbs, edits, retries, overrides and complaints are useful but noisy. Preserve context and distinguish preference from factual correction.

## Verified feedback

Curate corrections against authoritative outcomes before adding them to evaluation or training datasets.

## Evaluation loop

```text
Product usage
   ↓
Outcome + feedback
   ↓
Curated evidence
   ↓
Evaluation set
   ↓
Experiment
   ↓
Controlled release
```

## Experiments

A/B or controlled experiments are appropriate only when user risk and product semantics allow them. Hard safety/policy constraints remain fixed.

## Qualitative research

Interview users and inspect failure workflows. Metrics can reveal where failure occurs but not always why.

## Exercise

Define a product scorecard for an AI feature that must improve speed without increasing critical errors.

## Takeaway

> Product learning begins with verified outcomes, not with automatically training on every user reaction.

Next: **09 — AI Product Architecture and Lifecycle**.
