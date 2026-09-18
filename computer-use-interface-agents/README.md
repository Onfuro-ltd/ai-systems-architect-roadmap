# Domain 19 — Computer Use and Interface Agents

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across computer-use agents, UI perception, browser/desktop control, accessibility surfaces, action verification and safe interface automation.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Computer-use agents operate software interfaces on behalf of users by observing interface state, deciding what to do, executing actions, and verifying the result.

> A computer-use agent is not reliable because it can click. It is reliable when it can prove what state it observed, what action it intended, what actually happened, and when it must stop.

## Domain structure

01 Computer-Use Agent Architecture  
02 Interface Perception: DOM, Accessibility and Vision  
03 Action Models and Interaction Primitives  
04 Planning, State and Verification Loops  
05 Authentication, Sessions and Identity  
06 Permissions, Sandboxing and Consequential Actions  
07 Reliability, Recovery and Idempotency  
08 Evaluation and Observability  
09 Production Browser and Desktop Agent Infrastructure  
10 Computer-Use and Interface Agents Capstone

## Core loop

```text
Goal
 ↓
Observe interface
 ↓
Build grounded state
 ↓
Choose permitted action
 ↓
Execute
 ↓
Observe result
 ↓
Verify expected state transition
 ↓
Continue / recover / escalate / stop
```

## Principles

1. Prefer structured interface state over pixels when trustworthy.
2. Use vision when structure is missing or insufficient.
3. Ground every action to current state.
4. Re-observe after state-changing actions.
5. Separate proposal from authorization and execution.
6. Require stronger approval for consequential actions.
7. Never assume a click succeeded.
8. Make retries state-aware and idempotent where possible.
9. Treat web/interface content as untrusted input.
10. Preserve human control, auditability and safe stopping.

## Takeaway

> Interface agents turn probabilistic perception and planning into real actions, so deterministic permission and verification boundaries become more important—not less.

Next: **01 — Computer-Use Agent Architecture**.

## Canonical curriculum navigation

- [Computer-Use Agent Architecture](./01-computer-use-agent-architecture.md)
- [Interface Perception: DOM, Accessibility and Vision](./02-interface-perception-dom-accessibility-and-vision.md)
- [Action Models and Interaction Primitives](./03-action-models-and-interaction-primitives.md)
- [Planning, State and Verification Loops](./04-planning-state-and-verification-loops.md)
- [Authentication, Sessions and Identity](./05-authentication-sessions-and-identity.md)
- [Permissions, Sandboxing and Consequential Actions](./06-permissions-sandboxing-and-consequential-actions.md)
- [Reliability, Recovery and Idempotency](./07-reliability-recovery-and-idempotency.md)
- [Evaluation and Observability](./08-evaluation-and-observability.md)
- [Production Browser and Desktop Agent Infrastructure](./09-production-browser-and-desktop-agent-infrastructure.md)
- [Computer-Use and Interface Agents Capstone](./10-computer-use-interface-agents-capstone.md)
