# 10 — Business Automation Capstone

## Purpose

Design an enterprise automation platform that combines deterministic workflows, AI reasoning and human exception handling.

## Scenario

A multitenant operations platform processes high-volume business cases across several external systems. Inputs may be structured or unstructured. Most cases should complete automatically, while ambiguous or consequential cases require human judgment or approval.

## Target architecture

```text
Business trigger
      ↓
Durable workflow
      ↓
Validation + deterministic rules
      ↓
AI interpretation where needed
      ↓
Structured proposal
      ↓
Fresh authoritative revalidation
      ↓
Policy + permissions + approval
      ↓
Tool execution
      ↓
Verification + reconciliation
      ↓
Completed / exception / UNKNOWN
      ↓
Outcome metrics + process intelligence
```

## Required deliverables

Produce process map and baseline; automation-candidate framework; step decomposition; deterministic/AI/human boundary matrix; state machines; workflow orchestration; schemas; tool registry; delegated identity; risk classes; approval model; exception taxonomy/queue; SLA/escalation; idempotency strategy; UNKNOWN-state recovery; reconciliation jobs; compensating actions; dead-letter handling; observability; SLOs; kill switches; automation inventory; release/change controls; cost model; outcome scorecard; progressive-autonomy criteria; retirement plan; and at least three ADRs.

## Failure matrix

Cover malformed input, missing data, conflicting evidence, model misclassification, invalid structured output, stale authoritative data, permission denial, tool timeout, duplicate event, duplicate worker, external write with unknown response, partial completion, human approval expiry, queue backlog, provider outage, changed API schema, reconciliation mismatch, runaway retry and bad automation release.

## Acceptance criteria

The design passes only if the process is measured before automation; unnecessary steps are removed rather than encoded; exact rules remain deterministic; workflow state is durable; AI output is validated; permissions precede actions; consequential operations have appropriate approval; external writes are verified; UNKNOWN outcomes are reconciled before retry; exceptions have owners and SLAs; repeated exceptions drive process improvement; automation value includes quality and rework; changes are versioned/reversible; and humans retain a workable recovery path.

## Final principle

> The mature automation system is not the one with the fewest humans. It is the one that reliably sends machines the repeatable work, humans the meaningful exceptions, and evidence back into continuous process improvement.

**Domain 24 — Business Automation complete.**

Next domain: **25 — Decision Intelligence**.
