# 08 — Audit, Incident Response and Governance

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Audit, Incident Response and Governance** within Security, Permissions and Governance;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Security controls need evidence, ownership and a response process when they fail.

Governance connects technical controls to organisational accountability.

## Core Principle

> If an AI system can take consequential action, the organisation should be able to reconstruct what happened and disable it quickly.

## Audit Trail

A useful audit record can include:

- actor;
- delegated identity;
- timestamp;
- action;
- target;
- tool;
- policy decision;
- approval;
- result;
- correlation ID;
- system version.

## Model Metadata

Where useful, record:

- model;
- version;
- skill;
- workflow version.

Avoid logging hidden model reasoning as a substitute for action evidence.

## Integrity

Protect audit records from unauthorised modification.

High-risk systems may need append-only or tamper-evident logging.

## Incident Detection

Signals can include:

- unusual tool use;
- permission denial spike;
- exfiltration pattern;
- unexpected code execution;
- cost anomaly;
- repeated approval request;
- cross-tenant attempt;
- policy bypass.

## Kill Switch

Operators should be able to disable:

- one capability;
- one agent;
- one MCP server;
- one workflow;
- one model route;
- the entire system.

Granular shutdown reduces blast radius.

## Incident Response

A response process can include:

```text
Detect
  |
Contain
  |
Preserve Evidence
  |
Assess Impact
  |
Eradicate Cause
  |
Recover
  |
Create Regression / Control
```

## Credential Rotation

If secrets may be exposed:

- revoke;
- rotate;
- invalidate sessions;
- inspect downstream access.

## Memory and Data Review

An incident may poison:

- memory;
- vector indexes;
- caches;
- summaries.

Recovery must account for persistent derived state.

## Governance Roles

Define responsibility for:

- product owner;
- security owner;
- model owner;
- tool owner;
- data owner;
- incident commander.

## Change Governance

High-risk changes may require review for:

- new tools;
- new permissions;
- new model;
- new MCP server;
- new data source;
- new autonomous action.

## Risk Register

Track known risks with:

- owner;
- likelihood;
- impact;
- mitigation;
- status.

## Framework Alignment

External frameworks can help structure governance.

Examples include:

- NIST AI RMF;
- NIST Generative AI Profile;
- OWASP GenAI guidance;
- OWASP Agentic Top 10;
- MITRE ATLAS.

Map controls to real system risks rather than treating compliance mapping as proof of security.

## Security Evaluation

Security testing can include:

- adversarial prompts;
- indirect injection;
- tool misuse;
- privilege escalation;
- memory poisoning;
- cross-tenant access;
- secret extraction;
- unsafe code execution.

Security findings should become regression tests where practical.

## Exercise

Write an incident runbook for an agent suspected of sending sensitive data through a legitimate tool.

Include:

1. containment;
2. credential actions;
3. evidence;
4. affected runs;
5. memory review;
6. recovery;
7. regression.

## Takeaway

> Governance makes security sustainable after deployment, not just at design time.

Next: **09 — Capstone**.
