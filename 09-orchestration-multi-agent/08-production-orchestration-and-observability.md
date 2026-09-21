# 08 — Production Orchestration and Observability

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Production Orchestration and Observability** within Orchestration and Multi-Agent Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Production orchestration must be inspectable as a system, not merely readable as a transcript.

Operators need to understand where work is, why it moved and what failed.

## Core Principle

> Trace the orchestration graph, not just individual model calls.

## Root Run

Every orchestration should have a root run identifier.

Child work should preserve lineage.

```text
Run 100
 |
 +-- Task 101
 |    +-- Agent A
 |
 +-- Task 102
      +-- Agent B
```

## Trace Model

A trace can include:

- root run;
- workflow;
- state transition;
- model call;
- tool call;
- agent delegation;
- event;
- approval;
- retry.

## State Transition Log

Record:

- previous state;
- next state;
- reason;
- actor;
- timestamp;
- workflow version.

This makes orchestration explainable.

## Agent Lineage

Track:

- parent agent;
- child agent;
- delegation reason;
- task;
- context scope;
- permissions;
- outcome.

## Metrics

Useful metrics include:

- completion rate;
- p50/p95 latency;
- worker count;
- model calls;
- tool calls;
- retries;
- escalations;
- cancellation rate;
- cost per root run.

## Queue Metrics

For asynchronous workflows, track:

- queue depth;
- oldest task age;
- processing rate;
- retry queue;
- dead-letter volume.

## Progress Metrics

Long-running tasks benefit from measurable progress.

Examples:

- subtasks completed;
- required evidence collected;
- files processed;
- tests passing;
- branches completed.

Avoid fake progress percentages without a meaningful denominator.

## Cost Attribution

Attribute cost to the root task.

Include:

- model tokens;
- model calls;
- tool/API cost;
- compute;
- external services.

A worker's cost should roll up to the parent.

## Structured Logs

Logs should identify:

- run;
- component;
- state;
- action;
- result;
- error class.

Do not rely only on natural-language agent transcripts.

## Sensitive Data

Observability should avoid unnecessarily logging:

- secrets;
- credentials;
- private documents;
- full memory contents.

Use references and redaction where possible.

## Operational Controls

Operators may need:

- pause;
- resume;
- cancel;
- retry;
- reassign;
- approve;
- inspect state.

These should be explicit system functions.

## SLOs

Critical orchestrations may need objectives for:

- completion;
- latency;
- error rate;
- recovery;
- queue delay.

## Incident Questions

During an incident, answer:

- Which runs are affected?
- Which component failed?
- Which state are they in?
- Did external side effects occur?
- Can they resume safely?
- Which version is running?
- Are costs increasing unexpectedly?

## Exercise

Design a dashboard for a long-running multi-agent workflow.

Include:

1. root runs;
2. state;
3. workers;
4. retries;
5. cost;
6. queue depth;
7. failures;
8. approvals.

## Takeaway

> Production orchestration is an operational system, not a collection of prompts.

Next: **09 — Capstone**.
