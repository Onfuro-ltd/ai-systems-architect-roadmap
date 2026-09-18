# 06 — Exceptions, Approvals and Human-in-the-Loop Operations

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Exceptions, Approvals and Human-in-the-Loop Operations** within Business Automation;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Design operations around the reality that some cases should not be automated.

## Exception taxonomy

Classify missing data, conflicting data, policy exception, low-confidence interpretation, unusual value, unavailable dependency, permission issue and unknown outcome.

## Exception queue

Send cases with structured context: workflow, reason, evidence, proposed resolution, urgency and actions available to the reviewer.

## Approval

Approval should expose material effects and allow edit/reject/escalate—not merely a generic Approve button.

## SLA

Human queues need priority, ownership, ageing and escalation just like machine queues.

## Learning

Analyze recurring exceptions. Some indicate missing deterministic rules, poor data, weak integrations or process design—not a need for a larger model.

## Progressive automation

When a class of exceptions becomes reliably solvable, evaluate whether it can move into bounded automation.

## Exercise

Design an exception operations console for a workflow processing thousands of cases per day.

## Takeaway

> Human-in-the-loop works when humans receive the difficult decisions, not when they become unpaid retry logic for weak automation.

Next: **07 — Reconciliation, Idempotency and Recovery**.
