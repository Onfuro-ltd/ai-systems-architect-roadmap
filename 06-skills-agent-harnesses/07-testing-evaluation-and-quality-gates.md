# 07 — Testing, Evaluation and Quality Gates

## Purpose

Skills and harnesses need repeatable tests before they are trusted in production.

Testing should cover deterministic software behaviour and probabilistic model behaviour separately where possible.

## Core Principle

> Evaluate the capability, not just a demonstration.

## Test Layers

A mature capability can use several layers of testing.

### Contract Tests

Verify inputs, outputs and schemas.

### Deterministic Unit Tests

Verify rules, routing, validation and lifecycle logic.

### Tool Integration Tests

Verify capability interfaces and error handling.

### Behavioural Evaluations

Measure whether model-driven behaviour satisfies task expectations.

### End-to-End Tests

Verify the complete skill and harness path.

### Production Monitoring

Detect regressions and failures under real operating conditions.

## Golden Cases

A skill can maintain representative cases with expected properties.

Golden cases should include:

- normal cases;
- boundary cases;
- failure cases;
- ambiguous cases;
- adversarial cases where relevant.

They should not be limited to examples used while developing the prompt.

## Assertions

Some outputs support exact assertions.

Others require behavioural checks.

Examples include:

- schema validity;
- required evidence present;
- prohibited action absent;
- calculation within tolerance;
- correct tool selected;
- escalation triggered when required.

## Model-Based Evaluation

A model can assist with evaluation where deterministic checks are insufficient.

Model judges introduce their own uncertainty and should not automatically be treated as ground truth.

High-consequence evaluations may require human review or multiple independent checks.

## Regression Testing

Changes to any of these can change behaviour:

- model;
- prompt;
- skill instructions;
- tool schemas;
- context selection;
- retrieval;
- validation;
- policy.

Regression suites should run when behaviour-affecting components change.

## Quality Gates

A quality gate defines conditions that must be met before promotion.

Examples include:

- all contract tests pass;
- no critical policy violations;
- behavioural success above an agreed threshold;
- no material regression on critical cases;
- latency within operational limits;
- cost within budget.

Thresholds should be tied to use-case risk rather than arbitrary benchmark numbers.

## Failure Analysis

Evaluation should produce actionable failure categories.

Examples include:

- wrong capability selected;
- missing context;
- reasoning error;
- invalid tool request;
- tool failure;
- validation failure;
- policy rejection;
- escalation failure.

Failure taxonomy helps teams fix systems instead of merely tuning prompts.

## Evaluation Ownership

Each production skill should have someone responsible for its evaluation suite.

Without ownership, tests become stale while models, tools and workflows change.

## Domain Boundary

This lesson introduces skill- and harness-level testing.

Domain 10 covers evaluation and reliability as a dedicated discipline, including broader methodology, production evaluation and outcome economics.

## Exercise

Create a quality gate for a generic document-review skill.

Include:

1. contract tests;
2. five golden cases;
3. one adversarial case;
4. one tool failure;
5. one missing-context case;
6. promotion criteria;
7. rollback criteria.

## Takeaway

> A skill is not production-ready because it worked once.

Production capability requires repeatable evidence that it behaves acceptably across expected and failure conditions.

Next: **08 — Portability, Versioning and Governance**.
