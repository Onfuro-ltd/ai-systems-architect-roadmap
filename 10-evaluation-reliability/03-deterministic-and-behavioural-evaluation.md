# 03 — Deterministic and Behavioural Evaluation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Deterministic and Behavioural Evaluation** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

AI systems combine behaviour that software can verify exactly with behaviour that requires judgement.

Good evaluation uses deterministic checks wherever possible and behavioural evaluators where necessary.

## Core Principle

> Do not use an LLM judge for a property that ordinary software can verify exactly.

## Deterministic Checks

Examples:

- schema valid;
- JSON parseable;
- value within range;
- file exists;
- citation target exists;
- tool allowed;
- required field present;
- calculation correct.

These checks are cheap, repeatable and explainable.

## Reference-Based Checks

Where a reference answer exists, use metrics such as:

- exact match;
- set equality;
- numeric tolerance;
- precision / recall;
- classification accuracy.

Choose a metric that matches the error cost.

## Behavioural Evaluation

Behavioural tasks may need a rubric.

Examples:

- relevance;
- completeness;
- tone;
- evidence use;
- uncertainty;
- explanation quality.

Behavioural evaluation can be performed by humans or models.

## Composite Evaluation

A useful evaluation pipeline can be:

```text
Output
  |
Schema Check
  |
Deterministic Rules
  |
Reference Check
  |
Behavioural Rubric
  |
Overall Decision
```

A failure in a hard requirement can override a high subjective quality score.

## Hard Gates

Some requirements should be pass/fail.

Examples:

- no unauthorised action;
- valid output contract;
- required approval;
- no secret leakage.

Do not average critical failures away.

## Soft Metrics

Other criteria can be continuous.

Examples:

- completeness;
- readability;
- relevance;
- efficiency.

## Groundedness

For evidence-based tasks, evaluation can check whether claims are supported by available sources.

This can involve:

- citation validation;
- claim-source matching;
- human review;
- model-assisted grading.

Groundedness does not prove the source itself is true.

## Pairwise Comparison

Pairwise evaluation asks which of two outputs better meets the rubric.

This can be easier than assigning absolute scores.

Use randomised ordering to reduce position bias.

## Calibration

Calibrate behavioural evaluators against human-reviewed examples.

Measure disagreement.

A judge that sounds confident can still be poorly aligned with your rubric.

## Threshold Design

A threshold should reflect:

- consequence;
- baseline;
- variance;
- acceptable failure rate.

Avoid arbitrary numbers disconnected from the use case.

## Slice Analysis

Overall averages can hide failures.

Break down by:

- difficulty;
- category;
- tool path;
- language;
- risk;
- context length.

## Exercise

Create an evaluator stack for a generic research answer.

Use:

1. schema check;
2. citation existence;
3. claim support;
4. completeness rubric;
5. uncertainty rubric.

Specify which criteria are hard gates.

## Takeaway

> Reliability improves when exact requirements are tested exactly and subjective requirements are judged explicitly.

Next: **04 — Human Evaluation and Model Judges**.
