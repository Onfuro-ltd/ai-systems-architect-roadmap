# 09 — Production Domain AI Architecture and Governance

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **09 — Production Domain AI Architecture and Governance** within Domain-Specific AI Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Operate domain intelligence as a governed platform asset.

## Architecture

```text
Domain application
      ↓
Canonical domain API
      ↓
Identity / permissions
      ↓
Knowledge + policy + skills
      ↓
Model router
      ↓
Typed tools / workflows
      ↓
Validation + outcome verification
      ↓
Domain evaluation / feedback
```

## Registry

Maintain versions and owners for ontology/schema, knowledge sources, policies, skills, tools, evaluation sets, specialist models and routing rules.

## Release unit

A domain release may change several assets. Use a manifest so production behaviour can be reproduced.

## Observability

Trace domain task, evidence, policy version, skill/workflow, model route, tools, validation, approval, outcome and cost.

## Governance

Define domain owner, data owner, policy owner, evaluation owner and technical/platform owner.

## Isolation

In multitenant systems, domain intelligence may be shared while tenant facts, permissions, memory and proprietary knowledge remain isolated.

## Portability test

Periodically run representative evaluations on alternate models to prove that domain capability is not accidentally trapped in one provider.

## Exercise

Design a control plane for several domain AI products sharing the same ontology, policies and skills.

## Takeaway

> Domain intelligence should be versioned and governed like code, data and policy—not scattered across prompts.

Next: **10 — Domain-Specific AI Systems Capstone**.
