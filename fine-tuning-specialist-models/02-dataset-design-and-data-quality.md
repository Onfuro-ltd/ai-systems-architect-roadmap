# 02 — Dataset Design and Data Quality

## Purpose
Training data defines the behaviour a tuning process can learn.

> A small, representative, governed dataset can be more valuable than a large collection of noisy examples.

## Data specification
Define task, production inputs, desired outputs, allowed variation, failure classes, difficult cases, exclusions, quality rubric, privacy constraints, and acceptance criteria before collecting examples.

Match training representation to production: instructions, context, messages, tool schemas, or structured outputs.

## Coverage and quality
Cover common cases, important rare cases, ambiguity, malformed inputs, boundaries, and cases requiring abstention, escalation, or tool use. Consequence matters as well as frequency.

Establish a labeling rubric. Track label source and adjudicate difficult cases. Bad labels teach bad behaviour.

## Deduplication and splits
Near-duplicates can overweight patterns and leak between train and test. Deduplicate semantically where practical.

Create held-out evaluation before iterative tuning contaminates the project. Split by meaningful units such as document family, source, entity, customer-safe cohort, or time when random rows would leak patterns.

## Provenance and governance
Track source, rights, collection time, transformations, synthetic status, label source, privacy classification, tenant scope, dataset version, and approval.

Minimize sensitive data. Never place secrets into training data.

Do not casually mix tenant data. Verify contractual and privacy rights for shared training.

## Synthetic and negative examples
Label synthetic origin explicitly and validate against trusted references. Keep a real-world holdout.

Include negative examples for insufficient evidence, invalid requests, ambiguity, prohibited actions, unavailable tools, and escalation.

## Contamination
Prevent held-out examples and near-duplicates from entering training, synthetic generation, retrieval during training, or labeling references.

## Dataset versioning
Every release needs immutable identity and a changelog covering additions, removals, corrected labels, filtering, transformations, and split definitions.

## Feedback
Production interactions are candidates, not automatic truth:

```text
Interaction → outcome → verification → curation → dataset candidate
```

## Exercise
Design a dataset for a narrow extraction specialist. Specify schema, sources, rubric, hard negatives, split strategy, privacy/tenant controls, synthetic policy, versioning, and quality gates.

## Takeaway
> Dataset design is model design by another route. What you include, exclude, label, duplicate, and hold out determines what the specialist learns and what evaluation can honestly prove.

Next: **03 — Supervised Fine-Tuning**.
