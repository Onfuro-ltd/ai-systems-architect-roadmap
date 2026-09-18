# 06 — Permissions, Sandboxing and Consequential Actions

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Permissions, Sandboxing and Consequential Actions** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Prevent an interface agent from converting ambiguous instructions or hostile content into unauthorized real-world effects.

## Permission layers

```text
User intent
 ↓
Platform policy
 ↓
Tenant/role permission
 ↓
Tool/interface capability
 ↓
Action-specific approval
 ↓
Execution
```

Every layer must permit the action.

## Risk classes

Separate read-only navigation, reversible edits, communications, purchases/payments, account/security changes, deletion, publication and other consequential operations.

Approval strength should follow consequence.

## Sandboxing

Use isolated browser/desktop environments, filesystem boundaries, network controls, download quarantine and scoped credentials where appropriate.

## Prompt injection

A webpage, email, PDF or message can tell the agent to ignore instructions or disclose information. Content cannot grant permissions.

## Data exfiltration

Restrict which origins, tools, clipboard operations, uploads and outbound destinations can receive sensitive data.

## Confirmation

Before a consequential action, show the user the material facts: target, account, amount/content, destination and irreversible effects as applicable.

## Least privilege

Grant only the capabilities needed for the current workflow and expire them.

## Exercise

Threat-model an agent that can read email, browse vendor sites and prepare purchases but needs human approval to place an order.

## Takeaway

> The model may propose an action; deterministic policy decides whether the system is allowed to perform it.

Next: **07 — Reliability, Recovery and Idempotency**.
