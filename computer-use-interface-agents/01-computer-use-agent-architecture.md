# 01 — Computer-Use Agent Architecture

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Computer-Use Agent Architecture** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Understand the control loop that lets an AI operate an existing user interface.

## Architecture

```text
User / workflow goal
      ↓
Policy + session context
      ↓
Observation
      ↓
State representation
      ↓
Planner / action selection
      ↓
Permission gate
      ↓
Executor
      ↓
New observation
      ↓
Verification
```

## Why interfaces are difficult

Interfaces change, load asynchronously, hide state, show transient dialogs, reorder elements, require authentication, and may not expose stable APIs.

The agent operates through a representation of state, not direct knowledge of the application.

## Agent state

Track current goal, completed steps, observations, action history, expected transitions, uncertainty, retry budget and approval state.

Do not use model conversation alone as the authoritative execution ledger.

## APIs vs interfaces

Prefer supported APIs for stable machine-to-machine operations when available and appropriate. Interface automation is valuable for systems without APIs, mixed human workflows, legacy applications and tasks requiring visual interaction.

## Hybrid execution

A mature agent may combine APIs, DOM/accessibility structure, browser automation and vision. Route each operation to the most reliable allowed mechanism.

## Stop conditions

Define success, impossible state, authorization required, unexpected state, repeated failure, budget exceeded and unsafe ambiguity.

## Exercise

Design a browser agent that gathers information from one system and enters it into another while requiring approval before final submission.

## Takeaway

> Computer use is a closed-loop control problem: observe, act, verify, and stop safely.

Next: **02 — Interface Perception: DOM, Accessibility and Vision**.
