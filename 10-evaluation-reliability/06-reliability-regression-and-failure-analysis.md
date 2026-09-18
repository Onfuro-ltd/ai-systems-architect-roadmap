# 06 — Reliability, Regression and Failure Analysis

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Reliability, Regression and Failure Analysis** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Reliability engineering turns individual failures into systematic improvements.

A regression suite ensures that fixing one problem does not silently reintroduce another.

## Core Principle

> Every meaningful production failure should improve the test system.

## Failure Taxonomy

Create categories such as:

- intent misunderstanding;
- missing context;
- retrieval failure;
- reasoning error;
- hallucination;
- invalid tool call;
- wrong tool;
- policy failure;
- orchestration failure;
- timeout;
- bad recovery;
- premature completion.

A taxonomy supports trend analysis.

## Root Cause

The visible error may not be the root cause.

Example:

```text
Wrong Answer
  |
Why?
  |
Wrong Source Used
  |
Why?
  |
Retrieval Ranked Stale Document
  |
Why?
  |
No freshness signal
```

Fix the system cause, not only the final wording.

## Regression Case

Convert a failure into a reproducible evaluation case.

Preserve:

- input;
- environment;
- expected behaviour;
- failure category.

## Change Surface

Behaviour can change when any of these change:

- model;
- prompt;
- retrieval;
- memory;
- tool;
- policy;
- orchestration;
- SDK;
- external API.

Trigger regression evaluation accordingly.

## Reliability by Slice

Measure failure rate by category.

A stable average may hide a major regression in one slice.

## Flakiness

A flaky evaluation passes and fails nondeterministically.

Possible causes:

- model variance;
- unstable environment;
- race condition;
- weak judge;
- external dependency.

Track flakiness separately from true regression.

## Repeated Runs

For unstable cases, run multiple samples.

Estimate probability of failure rather than treating one pass as proof.

## Reliability Target

A target can be defined as:

- success rate;
- critical failure rate;
- escalation rate;
- tool error rate.

Tie targets to real consequences.

## Fallback

Reliability can include graceful degradation.

Examples:

- smaller feature set;
- human review;
- read-only mode;
- deterministic fallback.

## Rollback

When a release regresses behaviour, teams need a rollback path.

Evaluation should inform release operations but should not be the only rollback trigger.

## Incident Learning

A productive loop:

```text
Incident
  |
Contain
  |
Diagnose
  |
Create Eval
  |
Fix
  |
Regression Gate
  |
Monitor
```

## Exercise

Take five hypothetical failures and classify:

1. symptom;
2. root cause;
3. regression case;
4. mitigation;
5. monitoring signal.

## Takeaway

> Reliability grows when failures become permanent engineering knowledge.

Next: **07 — Production Evaluation and Monitoring**.
