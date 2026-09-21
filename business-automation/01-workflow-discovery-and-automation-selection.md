# 01 — Workflow Discovery and Automation Selection

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Workflow Discovery and Automation Selection** within Business Automation;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Identify which business processes are worth automating and which should remain human-led.

## Discover the real process

Observe actual work rather than relying only on procedure documents. Capture triggers, inputs, systems, decisions, handoffs, queues, exceptions, approvals, outputs and outcomes.

## Candidate dimensions

Evaluate frequency, manual effort, variability, data availability, rule clarity, consequence, reversibility, exception rate, system accessibility and measurable value.

## Bad candidates

Do not automate a broken process merely because it consumes time. First ask whether steps can be removed, simplified or redesigned.

## Automation spectrum

```text
Manual
 → assisted
 → deterministic automation
 → AI-assisted workflow
 → approval-based execution
 → bounded autonomy
```

## Baseline

Before automation, measure cycle time, labour effort, error/rework, backlog, service level and outcome quality.

## Process owner

Every candidate needs an accountable business owner who defines correct outcomes and exceptions.

## Exercise

Map five recurring processes and rank their automation readiness using explicit evidence rather than perceived annoyance.

## Takeaway

> The first automation decision is not how to automate a process; it is whether the process deserves to exist in its current form.

Next: **02 — Process Decomposition and Automation Boundaries**.
