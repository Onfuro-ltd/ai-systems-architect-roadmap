# Domain 19 — Computer Use and Interface Agents

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
