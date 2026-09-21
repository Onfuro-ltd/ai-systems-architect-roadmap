# 07 — Policy, Security, Governance and Human Authority

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Policy, Security, Governance and Human Authority** within Build an AI Operating System;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Create an independent control layer that constrains every AI capability.

## Policy hierarchy

Apply legal/contractual requirements, organizational policy, tenant policy, domain rules, delegated user authority and workflow-specific constraints with explicit precedence.

## Security

Assume prompts, retrieved documents, websites, tool output and model output can be untrusted.

Enforce least privilege, tenant isolation, secret management, input/output validation and sandboxing outside the model.

## Approval

Human approval is a permission transition. Show the proposed effect, evidence, uncertainty and reversibility.

## Progressive autonomy

```text
Recommend
 → Draft
 → Execute with approval
 → Bounded autonomous execution
```

Advance only with evaluation evidence and rollback capability.

## Audit

Record identity, authorization, material evidence, release versions, action, approval and outcome. Do not require hidden chain-of-thought for accountability.

## Governance

Maintain capability inventory, risk class, owners, evaluations, data use, autonomy level and review cadence.

## Emergency control

Provide kill switches, capability revocation, credential revocation and safe degradation independent of model cooperation.

## Exercise

Design a policy decision point that governs knowledge access, model eligibility and tool execution for the same request.

## Takeaway

> Human authority is preserved when autonomy is delegated through explicit, enforceable and revocable boundaries.

Next: **08 — Evaluation, Observability, Economics and Learning**.
