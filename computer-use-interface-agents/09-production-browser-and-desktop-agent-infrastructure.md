# 09 — Production Browser and Desktop Agent Infrastructure

## Purpose

Operate browser and desktop agents as isolated, observable, recoverable infrastructure.

## Architecture

```text
Workflow request
   ↓
Identity + policy
   ↓
Session allocator
   ↓
Isolated browser/desktop
   ↓
Agent controller
   ↓
Perception + action adapters
   ↓
Target applications
   ↓
Evidence / artifacts / audit
```

## Session infrastructure

Manage profile lifecycle, cookies, storage, downloads, viewport, locale, expiry and cleanup. Reuse sessions only when security and workflow semantics justify it.

## Isolation

Separate tenants and risky workloads at appropriate browser/container/VM boundaries. Restrict filesystem, network and clipboard according to policy.

## Concurrency

Browsers consume CPU, RAM and sometimes GPU resources. Capacity planning includes active sessions, page complexity, media, model calls and long waits.

## Artifacts

Store screenshots, downloads and recordings only when needed, with access controls and retention. Prefer structured evidence over indiscriminate screen recording.

## Orchestration

Long tasks need durable workflow state, cancellation, timeouts, checkpoints, approval waits and recovery after worker loss.

## Versioning

Track browser/runtime version, automation adapter, perception model, agent policy, prompt/skill and target-site compatibility.

## Site change

Monitor failure clusters and grounding drift. Do not automatically patch selectors from unverified model guesses into production.

## Exercise

Design a multi-region browser-agent platform supporting thousands of isolated sessions with durable workflows and human approvals.

## Takeaway

> Production computer use is a secure remote-execution platform wrapped around an AI controller.

Next: **10 — Computer-Use and Interface Agents Capstone**.
