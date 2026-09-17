# 08 — Evaluation and Regression Testing

## Purpose
A tuned model is a production change. Evaluation determines whether it improves the intended workload without damaging important behaviour.

> Never let the training objective grade its own success.

## Independent holdout
Keep evaluation data inaccessible to training and synthetic-generation pipelines. Include common cases, hard cases, rare consequential failures, out-of-domain inputs, and escalation cases.

## Compare real alternatives

```text
Base + best prompt
Base + RAG/tools
Alternative existing model
Tuned candidate
Specialist + escalation
```

Do not compare a tuned model only against a deliberately weak baseline.

## Metrics
Use task-appropriate exact/field accuracy, precision/recall/F1, ranking, schema validity, tool correctness, abstention, critical error rate, semantic rubric, or human preference.

Analyze meaningful slices so aggregate improvement cannot hide severe subgroup regressions.

## Regression suite
Test instruction hierarchy, structured outputs, tool boundaries, refusal/escalation, relevant languages/domains, context behaviour, and safety/system requirements.

## Model judges
Judges can scale evaluation but may prefer style or familiar outputs. Calibrate them with deterministic checks and trusted human review.

## Statistical discipline
Record sample sizes and uncertainty. Repeated tuning against one test set contaminates it; refresh holdouts where needed.

## Operational evaluation
Benchmark the exact deployed artifact/runtime for latency, TTFT, throughput, memory, failure rate, and cost.

## Shadow, canary and outcome
After offline gates, use shadow or limited canary traffic where safe, preserving rollback. Connect predictions to verified downstream outcomes when possible.

Define promotion thresholds before viewing favorite runs.

## Exercise
Build an evaluation plan with clean holdout, slices, regression suite, judge calibration, operational benchmark, shadow/canary, promotion thresholds, and rollback triggers.

## Takeaway
> A tuned model is better only when independent evaluation shows improved real-task outcomes within acceptable regression, latency, reliability, and cost boundaries.

Next: **09 — Adapter and Model Lifecycle and Governance**.
