# 02 — Workflows, State Machines and Agent Loops

## Purpose

Workflows and agent loops are the two primary control structures for AI work.

State machines make their transitions explicit.

## Core Principle

> Put predictable transitions in software and reserve model reasoning for transitions that genuinely require judgement.

## Sequential Workflow

The simplest pattern is sequential execution.

```text
Step A
  |
Step B
  |
Step C
```

Use it when each step depends on the previous one and the order is stable.

## Prompt Chaining

Prompt chaining is a model-assisted sequential workflow.

Each call transforms or evaluates the output of the previous call.

Useful examples include:

- extract -> validate -> summarise;
- draft -> critique -> revise;
- classify -> specialised handling.

Programmatic gates can be inserted between model calls.

## State Machines

A state machine defines valid states and transitions.

Example:

```text
RECEIVED
   |
VALIDATED
   |
ANALYSING
   |
WAITING_APPROVAL
   |
EXECUTING
   |
COMPLETED
```

Failure states may include:

```text
RETRYABLE_FAILED
FAILED
CANCELLED
ESCALATED
```

State machines make recovery and audit easier than implicit conversational state.

## Transition Guards

A transition can require:

- schema validation;
- policy check;
- approval;
- tool result;
- evaluation threshold.

A model may recommend a transition, while deterministic software decides whether it is valid.

## Agent Loop

A bounded agent loop can be represented as:

```text
while not done:
    observe
    reason
    propose action
    validate
    execute
    update state
    evaluate progress
```

The loop should not depend on the model alone to decide whether it should continue forever.

## Step Budget

Useful budgets include:

- maximum turns;
- maximum tool calls;
- maximum cost;
- maximum elapsed time;
- maximum retries.

Budgets should be visible in state.

## Checkpoints

Longer workflows benefit from checkpoints.

A checkpoint can preserve:

- state;
- completed outputs;
- evidence;
- pending work;
- version metadata.

Checkpoints support recovery without repeating every earlier step.

## Resumability

A resumable workflow should answer:

- Where did execution stop?
- Which actions already occurred?
- Which actions are safe to repeat?
- What context must be reconstructed?
- Has external state changed?

Resumability requires more than conversation history.

## Deterministic Gates

Use deterministic gates where requirements are crisp.

Examples:

- required field present;
- amount under threshold;
- test suite passed;
- file exists;
- approval token valid.

Do not ask a model to decide facts software can verify exactly.

## Model Gates

Model judgement can be appropriate for fuzzy criteria.

Examples:

- whether evidence is persuasive;
- whether a draft meets a subjective rubric;
- whether more research is needed.

Model gates should be evaluated for reliability.

## Workflow Versioning

Changes to orchestration can change system behaviour.

Track:

- workflow version;
- transition changes;
- prompt changes;
- tool changes;
- policy changes.

A running workflow may need to remain on the version it started with.

## Exercise

Design a state machine for a generic document review workflow.

Include:

- normal states;
- approval;
- retry;
- escalation;
- cancellation;
- resumption.

Mark which transitions are deterministic and which use model judgement.

## Takeaway

> Explicit state turns multi-step AI behaviour into an operable system.

Next: **03 — Delegation and Specialist Agents**.
