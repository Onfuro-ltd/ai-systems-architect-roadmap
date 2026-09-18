# 02 — Task Suites, Golden Datasets and Holdouts

## Purpose

An evaluation is only as useful as the tasks it represents.

Task suites should reflect real operating conditions, important edge cases and known failure modes.

## Core Principle

> Build evaluation data from the work you care about, not from convenient examples.

## Task Suite

A task suite is a curated collection of evaluation cases.

Each case can contain:

- input;
- relevant context;
- expected properties;
- reference answer where appropriate;
- rubric;
- metadata;
- risk level.

## Golden Dataset

A golden dataset contains carefully reviewed cases with trusted expected behaviour.

Goldens are useful for:

- regression;
- deterministic assertions;
- behavioural calibration.

"Golden" does not mean permanently correct.

Goldens need maintenance as requirements change.

## Reference Answer

A reference answer is useful when there is a known correct result.

Examples:

- extraction;
- classification;
- calculation;
- data transformation.

Open-ended tasks may require rubrics instead.

## Rubric

A rubric describes what good behaviour means.

Example dimensions:

- factual correctness;
- completeness;
- evidence;
- clarity;
- appropriate uncertainty.

Rubrics should be specific enough that different evaluators can apply them consistently.

## Production-Derived Cases

Production failures are valuable evaluation cases.

A useful loop is:

```text
Production Failure
       |
Root Cause
       |
Regression Case
       |
Fix
       |
Permanent Suite
```

This turns incidents into durable reliability improvements.

## Edge Cases

Include:

- ambiguous inputs;
- missing data;
- conflicting data;
- long context;
- tool failure;
- stale memory;
- malformed output;
- adversarial content.

## Distribution

The suite should reflect the real task distribution.

Do not let rare easy cases dominate the average.

Use slices.

Examples:

- language;
- customer type;
- document type;
- risk level;
- tool path;
- task difficulty.

## Holdout Set

A holdout is kept separate from day-to-day tuning.

It helps detect overfitting to the development suite.

If developers repeatedly inspect every holdout example, it stops functioning as a meaningful holdout.

## Contamination

Evaluation becomes misleading when the system is tuned directly against the answers.

Sources of contamination include:

- including gold answers in prompts;
- repeated manual optimisation on the same cases;
- training on the evaluation set;
- model familiarity with public benchmark items.

## Dataset Versioning

Track:

- dataset version;
- case additions;
- case removals;
- label changes;
- rubric changes.

Changes can alter scores even when the system does not change.

## Case Ownership

Important evaluation suites need an owner responsible for:

- curation;
- label quality;
- freshness;
- coverage;
- retirement.

## Synthetic Cases

Models can generate candidate test cases.

Synthetic cases are useful for expanding coverage but should be reviewed for realism and relevance.

## Difficulty

Include cases that separate system versions.

A suite containing only trivial cases cannot detect meaningful improvement.

## Exercise

Create a 30-case evaluation suite for a generic document review system.

Include:

- 15 common cases;
- 5 edge cases;
- 5 known failures;
- 3 adversarial cases;
- 2 ambiguous cases.

Define which are development and which remain holdout.

## Takeaway

> Representative task suites are the foundation of trustworthy evaluation.

Next: **03 — Deterministic and Behavioural Evaluation**.
