# 02 — Control Plane and Capability Architecture

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Control Plane and Capability Architecture** within Build an AI Operating System;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Create the internal contracts that let many AI applications share capabilities safely.

## Capability registry

Register models, agents, skills, workflows, knowledge sources, memories and tools with identity, version, owner, permissions, risk and evaluation status.

## Control plane

```text
Capability registry
Policy registry
Model registry/router
Skill/workflow registry
Tool registry
Evaluation registry
Release registry
Cost/budget controls
Observability metadata
```

The control plane manages configuration and authority; the data/action planes execute work.

## Canonical contracts

Applications should request capabilities such as classify, investigate, summarize, recommend or execute rather than hard-coding provider-specific APIs.

## Release manifest

A production capability may depend on model, prompt, retrieval index, skill, policy, tool schema and router versions. Record the complete behaviour-affecting release.

## Discovery

Agents and applications should discover only capabilities they are authorized to use.

## Ownership

Every capability needs technical owner, domain owner where applicable, lifecycle status and rollback/retirement path.

## Exercise

Design a registry schema that can represent a model, a domain skill and a consequential tool without treating them as identical objects.

## Takeaway

> A capability control plane turns an AI stack from a collection of integrations into an operable platform.

Next: **03 — Identity, Context, Memory and Knowledge Plane**.
