# 06 — Policy Engines, Approvals and Action Controls

## Purpose

Policy engines and approval gates convert organisational rules into enforceable runtime decisions.

## Core Principle

> Important action policy should be evaluated outside the model.

## Policy Decision

A policy decision can evaluate:

- identity;
- action;
- resource;
- context;
- risk;
- amount;
- tenant;
- time;
- prior approval.

## Policy Enforcement Point

The enforcement point sits before the privileged action.

```text
Model Proposal
   |
Validation
   |
Policy Decision
   |
Approval if required
   |
Tool Execution
```

## Allow, Deny, Escalate

Useful outcomes include:

- allow;
- deny;
- require approval;
- require more evidence;
- reduce scope.

Not every policy must be binary.

## Risk-Based Controls

Example:

```text
Read public data -> automatic
Read confidential data -> authorised identity
Write routine draft -> automatic
Send external message -> approval
Delete production data -> strong approval
```

## Approval Design

An approval request should show:

- proposed action;
- target;
- parameters;
- expected effect;
- relevant evidence;
- requesting identity;
- model/agent source.

Avoid vague prompts such as:

> "Agent wants permission. Approve?"

## Approval Scope

An approval can authorise:

- one action;
- action type;
- resource set;
- time window;
- bounded amount.

Avoid open-ended approval tokens.

## Step-Up Authentication

High-risk actions may require stronger user verification before approval.

## Dual Control

Some actions may require two independent approvals.

Use where consequence justifies the friction.

## Policy as Code

Policies can be version-controlled and tested.

Benefits:

- review;
- repeatability;
- rollback;
- change history.

## Policy Tests

Test:

- allowed case;
- denied case;
- boundary;
- missing identity;
- wrong tenant;
- expired approval.

## Model Recommendation

A model can recommend:

- risk class;
- policy category;
- escalation.

But deterministic policy should enforce crisp requirements.

## Emergency Stop

Systems should support disabling:

- tool;
- agent;
- server;
- workflow;
- model route.

An incident response process needs a real kill switch.

## Exercise

Design policy for a generic operations agent with three action levels:

1. read;
2. reversible write;
3. irreversible external action.

Define approval and identity requirements.

## Takeaway

> Policy separates what the model thinks should happen from what the organisation permits to happen.

Next: **07 — Secrets, Sandboxing and Runtime Security**.
