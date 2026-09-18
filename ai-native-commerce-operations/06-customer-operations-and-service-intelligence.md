# 06 — Customer Operations and Service Intelligence

## Purpose

Use AI to improve customer operations while preserving policy, evidence and human escalation.

## Capabilities

AI can classify contacts, retrieve order/product evidence, summarize history, draft responses, recommend resolutions and execute bounded service actions.

## Evidence

Ground responses in current order, shipment, return, product and policy data.

## Policy

Refund, replacement, compensation and account actions should be constrained by deterministic policy and delegated authority.

## Workflow

```text
Customer contact
      ↓
Intent / urgency
      ↓
Authorized customer + order context
      ↓
Evidence-grounded response / proposal
      ↓
Policy + permissions
      ↓
Draft / approval / bounded action
      ↓
Outcome + follow-up
```

## Escalation

Escalate safety issues, legal threats, repeated unresolved failures, ambiguous identity, policy exceptions and other defined high-consequence cases.

## Quality

Measure resolution, first-contact resolution, recontact, correction, escalation, customer outcome and policy error—not response speed alone.

## Exercise

Design a customer-service copilot that can draft broadly but execute refunds only inside deterministic limits.

## Takeaway

> Service AI should reduce customer effort without giving probabilistic reasoning unrestricted authority over customer remedies.

Next: **07 — Finance, Tax and Reconciliation Intelligence**.
