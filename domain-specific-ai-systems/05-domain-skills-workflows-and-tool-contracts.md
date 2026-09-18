# 05 — Domain Skills, Workflows and Tool Contracts

## Purpose

Encode repeatable domain procedures as reusable capabilities rather than repeatedly teaching them through prompts.

## Skill

A domain skill packages purpose, prerequisites, inputs, procedure, tools, validation, escalation and expected output.

## Workflow

Use durable workflows for multi-step processes with state, timers, approvals, external effects or recovery.

## Tool contracts

Expose business capabilities through typed tools with permissions, risk, idempotency and audit semantics.

## Composition

```text
Domain workflow
   ↓
Skill
   ↓
Model reasoning where needed
   ↓
Typed tools
   ↓
Deterministic validation
```

## Separation

Do not bury API credentials, business rules or irreversible side effects inside free-form skill text.

## Versioning

Version skills and workflows independently from foundation models.

## Portability

A well-designed skill can be executed by different eligible models or deterministic components without rewriting the business process.

## Exercise

Turn an expert SOP into a reusable domain skill with explicit tool calls, validation and escalation.

## Takeaway

> Skills and workflows are how procedural organizational knowledge survives a model replacement.

Next: **06 — Specialist Models, Tuning and Routing**.
