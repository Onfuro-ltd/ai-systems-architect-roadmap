# 10 — Computer-Use and Interface Agents Capstone

## Purpose

Design an enterprise computer-use platform that can operate third-party interfaces while preserving user authority and safe recovery.

## Scenario

A multitenant operations platform must interact with legacy web portals and desktop-style interfaces where APIs are unavailable or incomplete. Agents may gather information, prepare forms and drafts, upload/download files and perform approved operational actions.

## Target architecture

```text
Human / workflow intent
        ↓
Identity + policy + permissions
        ↓
Durable workflow state
        ↓
Isolated session
        ↓
Observe
 DOM / accessibility / vision
        ↓
Grounded state
        ↓
Planner
        ↓
Action risk classification
        ↓
Approval when required
        ↓
Executor
        ↓
Re-observe + verify
        ↓
Outcome / checkpoint / recovery
        ↓
Audit + evaluation
```

## Required deliverables

Produce workflow catalogue and risk classes; perception strategy; canonical observation/action schemas; explicit state machines; semantic targeting; pre/postconditions; session and credential architecture; MFA/user-intervention path; tenant isolation; permission model; sandbox/network/file controls; prompt-injection defenses; consequential-action approval; idempotency and UNKNOWN-outcome handling; checkpoints; recovery ladder; kill switches; evaluation suite; critical-failure criteria; tracing; production session infrastructure; capacity model; artifact retention; version/compatibility tracking; incident runbooks; and at least three ADRs.

## Failure matrix

Cover stale interface state, wrong element, wrong account/tenant, popup/layout change, partial form, timeout after submission, duplicate action, expired login, MFA/challenge, malicious page instruction, sensitive-data exfiltration attempt, corrupt download, browser crash, worker loss, site redesign, approval mismatch and failed verification.

## Acceptance criteria

The system passes only if structured perception is preferred where trustworthy; vision is grounded to current state; every state-changing action has verification; consequential effects require appropriate authorization; content cannot grant permissions; credentials remain outside model context where possible; tenant sessions are isolated; retries distinguish safe reads from effects; UNKNOWN outcomes are reconciled before retry; security challenges are not bypassed; durable tasks can recover; critical failures are separately measured; and applications remain independent of one browser/runtime/model provider.

## Final principle

> The safest computer-use agent is not the one that acts most autonomously. It is the one that knows exactly what it is allowed to do, verifies what actually happened, and reliably stops when reality no longer matches its assumptions.

**Domain 19 — Computer Use and Interface Agents complete.**

Next domain: **20 — Physical AI and Robotics**.
