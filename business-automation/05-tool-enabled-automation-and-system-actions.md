# 05 — Tool-Enabled Automation and System Actions

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Tool-Enabled Automation and System Actions** within Business Automation;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Connect automated workflows to business systems through governed capabilities.

## Tool contract

Each tool should define typed input/output, authentication, permissions, side effects, timeout/error semantics, idempotency behaviour and audit metadata.

## Read and write separation

Read tools can often have broader automation than write tools. State-changing capabilities need stronger checks.

## Action flow

```text
Proposed action
 ↓
Fresh authoritative state
 ↓
Permission + policy
 ↓
Input validation
 ↓
Execution
 ↓
Result verification
 ↓
Audit
```

## Credentials

Use delegated/scoped machine identities and secret stores. Do not place raw credentials in model context.

## APIs first

Prefer supported APIs and events over UI automation. Use interface agents when necessary and apply Domain 19 controls.

## Side effects

Classify tools by consequence and reversibility. Payment, publication, deletion and security changes should not look like ordinary read calls.

## Exercise

Design a tool registry for an automation platform with explicit read/write, risk and approval metadata.

## Takeaway

> Tools turn reasoning into consequences; therefore tool boundaries must be more deterministic than the reasoning that selects them.

Next: **06 — Exceptions, Approvals and Human-in-the-Loop Operations**.
