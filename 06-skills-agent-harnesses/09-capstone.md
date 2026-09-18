# 09 — Capstone: Design a Production Skill and Harness

## Objective

Design a production-oriented reusable AI capability and the harness that controls its execution.

The capstone should demonstrate architectural understanding rather than depend on a particular model vendor or framework.

## Scenario

Choose a generic knowledge-work capability such as:

- document review;
- research synthesis;
- support triage;
- compliance pre-check;
- data-quality investigation;
- operational exception analysis.

Avoid building a generic chatbot.

## Part 1 — Skill Contract

Define:

- purpose;
- supported inputs;
- expected outputs;
- required context;
- tool dependencies;
- authority requirements;
- validation;
- failure behaviour;
- evaluation criteria;
- owner;
- version.

## Part 2 — Context Contract

Specify:

- required context;
- optional context;
- source authority;
- freshness rules;
- provenance;
- exclusion rules;
- context budget;
- conflict handling.

Explain the difference between knowledge, memory, state and current execution context.

## Part 3 — Harness Architecture

Design:

```text
Request
  |
Identity / Session
  |
Skill Selection
  |
Context Assembly
  |
Model Routing
  |
Tool Mediation
  |
Validation / Policy
  |
Action or Escalation
  |
Evaluation / Observability
  |
Outcome
```

Explain which controls are deterministic and which decisions may use model reasoning.

## Part 4 — Lifecycle Controls

Define hooks for:

- request validation;
- pre-model preparation;
- pre-tool authorisation;
- post-tool validation;
- retries;
- approvals;
- completion;
- error handling.

Add explicit limits for steps, retries, time and cost.

## Part 5 — Composition and Discovery

Place the capability in a small skill registry.

Define:

- discovery metadata;
- compatible upstream and downstream capabilities;
- ownership;
- version;
- lifecycle state.

Show how the skill could participate in a larger workflow without hidden dependencies.

## Part 6 — Evaluation

Create an evaluation suite containing:

- contract tests;
- normal cases;
- boundary cases;
- failure cases;
- ambiguous cases;
- at least one adversarial or untrusted-content case;
- tool failure;
- missing-context case.

Define the quality gate required for production promotion.

## Part 7 — Portability

Identify which components are:

- model-independent;
- provider-specific;
- tool-interface-specific;
- policy-specific.

Describe how you would change the model or tool provider without rewriting the durable capability contract.

## Part 8 — Failure Review

Document at least five possible failure modes.

For each, identify:

- detection;
- containment;
- recovery;
- escalation;
- evidence captured for later analysis.

## Completion Criteria

The capstone is complete when another engineer could inspect the design and understand:

- what the capability does;
- what it needs;
- what it may access;
- how it is controlled;
- how it fails;
- how it is evaluated;
- how it changes safely over time.

## Architectural Review Questions

Before considering the design complete, answer:

1. Is reusable expertise separated from one-off prompting?
2. Are capability boundaries explicit?
3. Does the harness mediate model-proposed actions?
4. Are context and authority limited to what is required?
5. Are deterministic controls used where consequences demand them?
6. Are failure and escalation behaviours explicit?
7. Can behaviour be evaluated repeatedly?
8. Can the capability evolve without losing ownership or traceability?
9. Could the model be changed without discarding the entire architecture?

## Takeaway

> The goal of a production AI capability is not autonomy for its own sake.

The goal is useful reasoning inside an architecture that is testable, observable, governable and appropriate to the consequences of the work.

Next: **Domain 07 — MCP and Tool Ecosystems**.
