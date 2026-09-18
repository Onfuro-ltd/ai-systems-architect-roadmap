# 03 — Deterministic Automation vs AI Reasoning

## Purpose

Choose the correct computational mechanism for each workflow step.

## Deterministic first

Use code, rules, queries and calculators for exact arithmetic, thresholds, permissions, identity, schema checks, known transformations and state transitions.

## AI strengths

Models are useful for language interpretation, fuzzy classification, unstructured extraction, summarization, semantic matching and reasoning under bounded ambiguity.

## Hybrid pattern

```text
Validated input
   ↓
Deterministic preprocessing
   ↓
AI interpretation
   ↓
Structured output
   ↓
Deterministic validation / business rules
   ↓
Approved action
```

## Knowledge

Current facts should come from authoritative data/retrieval/tools rather than being expected from model memory.

## Confidence

Do not convert uncalibrated model confidence into business authority. Validate against task-specific evidence.

## Escalation

When ambiguity exceeds a defined boundary, route to another mechanism or a human.

## Exercise

For twenty workflow decisions, classify whether each belongs in code, data retrieval, AI, human judgment or a combination.

## Takeaway

> Use AI to resolve ambiguity, not to recreate deterministic business logic probabilistically.

Next: **04 — Durable Workflows, State and Orchestration**.
