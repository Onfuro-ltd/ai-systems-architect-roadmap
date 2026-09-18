# 03 — Action Models and Interaction Primitives

## Purpose

Represent interface actions as explicit, constrained operations.

## Primitives

Typical actions include navigate, click/activate, type, select, scroll, drag, upload/download, keyboard shortcut, wait, read, copy, and close/open window or tab.

## Semantic targets

Prefer:

```text
click(role=button, name="Continue")
```

over an unexplained coordinate when semantic targeting is available.

## Preconditions

Each state-changing action should have expected preconditions: correct page, correct account/tenant, target visible/enabled, required values present and authorization valid.

## Postconditions

Define what success should look like before execution. After acting, observe and verify that state.

## Typing

Sensitive fields need special handling. Do not expose secrets to the reasoning context when a secure credential mechanism can fill them.

## Downloads/uploads

Validate source/destination, file identity/type and authorization. Treat downloaded files as untrusted input.

## Action budgets

Limit steps, retries, time, spend and potentially destructive operations.

## Exercise

Define a typed action schema for browser automation with preconditions, postconditions, risk class and evidence.

## Takeaway

> An interface action should be a verifiable state transition, not an unstructured instruction to click somewhere.

Next: **04 — Planning, State and Verification Loops**.
