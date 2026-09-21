# 05 — Governance, Risk, Compliance and Audit

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Governance, Risk, Compliance and Audit** within Enterprise AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Translate organizational risk requirements into controls that operate throughout the AI lifecycle.

## Risk classification

Classify use cases by consequence, autonomy, data sensitivity, affected population, reversibility and legal/regulatory context.

Higher risk requires stronger evidence and controls.

## Control lifecycle

```text
Use case
 ↓
Risk classification
 ↓
Required controls
 ↓
Design + evaluation evidence
 ↓
Approval
 ↓
Production monitoring
 ↓
Periodic review / incident / change
```

## Control types

Controls can include access restrictions, data minimization, approved models, evaluation thresholds, human approval, logging, rate limits, tool restrictions, explainability/evidence, retention and incident response.

## Compliance

Map applicable legal, contractual and industry requirements to concrete system controls with qualified legal/compliance input where necessary.

## Auditability

Record versioned model/system configuration, evidence sources, authorization, approvals, material actions, evaluation and outcome without relying on hidden reasoning.

## Exceptions

Governance needs a controlled exception process with owner, rationale, compensating controls and expiry.

## Change

Material model, data, tool, autonomy or workflow changes can alter risk and should trigger re-evaluation.

## Exercise

Create a control matrix for low-risk summarization, internal decision support and a consequential action-taking agent.

## Takeaway

> Good AI governance converts policy into enforceable architecture, measurable evidence and accountable ownership.

Next: **06 — Procurement, Vendors and Model Independence**.
