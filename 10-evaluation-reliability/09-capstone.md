# 09 — Capstone: Build an Evaluation and Reliability System

## Objective

Design an evaluation architecture for a production AI system from development through live operation.

## Scenario

Choose a generic system such as:

- research agent;
- document reviewer;
- support assistant;
- operational workflow;
- coding assistant.

The capstone should evaluate the complete system, not only the base model.

## Part 1 — Success Definition

Define:

- system purpose;
- users;
- critical outcomes;
- unacceptable failures;
- reliability target.

## Part 2 — Evaluation Objects

Identify:

- component-level checks;
- skill-level checks;
- agent/workflow checks;
- end-to-end outcome.

## Part 3 — Task Suite

Build:

- common cases;
- edge cases;
- historical failures;
- adversarial cases;
- holdout cases.

Add slices.

## Part 4 — Evaluators

Use a layered evaluator stack:

- deterministic assertions;
- reference checks;
- behavioural rubric;
- model judge;
- human review.

Explain why each is used.

## Part 5 — Agent and Tool Evaluation

Evaluate:

- tool selection;
- argument validity;
- policy gates;
- retries;
- completion;
- unnecessary actions;
- trajectory.

## Part 6 — Reliability

Create:

- failure taxonomy;
- regression process;
- repeated-run policy;
- flakiness handling;
- rollback threshold.

## Part 7 — Production Monitoring

Define:

- sampling;
- shadow;
- canary;
- A/B where appropriate;
- drift;
- alerting;
- production judge.

## Part 8 — Economics

Measure:

- success;
- cost;
- latency;
- retry cost;
- human review;
- failure consequence.

## Part 9 — Release Gate

Create a promotion decision containing:

- required deterministic passes;
- behavioural threshold;
- no critical regression;
- cost budget;
- latency budget;
- security gate.

## Part 10 — Learning Loop

Design:

```text
Production
   |
Failure / Feedback
   |
Triage
   |
Evaluation Case
   |
Fix
   |
Regression Gate
   |
Release
```

## Architectural Review Questions

Before completion, answer:

1. Does the suite represent real work?
2. Are critical requirements deterministic where possible?
3. Is the judge calibrated?
4. Are high-risk cases reviewed appropriately?
5. Are agents evaluated by trajectory?
6. Are known failures permanent regression cases?
7. Can production drift be detected?
8. Are cost and latency measured per outcome?
9. Can the system roll back?
10. Is evaluation ownership clear?

## Completion Criteria

Another engineer should be able to determine:

- what success means;
- what is tested;
- how it is scored;
- what blocks release;
- how failures are classified;
- how production is monitored;
- how economics are evaluated;
- how incidents improve future reliability.

## Takeaway

> Evaluation is the evidence system that lets an AI product improve without guessing.

Next: **Domain 11 — Security, Permissions and Governance**.
