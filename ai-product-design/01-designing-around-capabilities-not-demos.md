# 01 — Designing Around Capabilities, Not Demos

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Designing Around Capabilities, Not Demos** within AI Product Design;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Build products around repeatable capability rather than impressive examples.

## Demo trap

A hand-picked prompt can hide failure distributions, latency, cost, context limits, tool errors and edge cases.

Product requirements need measured behaviour across representative tasks.

## Capability contract

For each AI feature define input types, supported tasks, quality threshold, known limitations, latency target, evidence requirements, permissions, fallback and escalation.

## Narrow before broad

A bounded workflow with explicit success criteria is often more valuable than a general assistant that appears capable but cannot be trusted operationally.

## Product boundary

Use deterministic software for exact rules, calculations, permissions and state transitions. Use models where interpretation, generation or fuzzy reasoning adds value.

## Model changes

Do not expose a product promise tied to one model's incidental behaviour. Maintain evaluations that protect the capability contract when models change.

## Exercise

Take a generic "AI business assistant" concept and redesign it as three bounded capabilities with measurable outcomes and explicit failure paths.

## Takeaway

> Productize the capability you can repeatedly prove, not the behaviour you happened to see in a demo.

Next: **02 — Human-AI Interaction Models**.
