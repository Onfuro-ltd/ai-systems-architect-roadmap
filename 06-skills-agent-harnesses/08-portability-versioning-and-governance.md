# 08 — Portability, Versioning and Governance

## Purpose

Reusable AI capabilities change over time.

Teams need ways to version, migrate, own, retire and move capabilities across models and platforms without losing control of behaviour.

## Core Principle

> Treat skills as governed software assets, not disposable prompt fragments.

## Versioned Surface

Behaviour can change when any of these change:

- instructions;
- model;
- context strategy;
- schemas;
- tools;
- knowledge sources;
- validation;
- policies;
- evaluation suites.

A useful version should identify the behaviour-affecting configuration well enough to reproduce and evaluate it.

## Semantic Change

Not every text edit requires a major version.

What matters is whether the externally meaningful behaviour or contract changes.

Teams can define their own version policy, but it should distinguish:

- compatible improvements;
- contract changes;
- breaking changes;
- emergency fixes.

## Model Portability

A portable skill separates durable operating knowledge from model-specific details where practical.

This can include keeping:

- task contracts;
- validation;
- tool interfaces;
- evaluation suites;
- workflow rules

outside provider-specific prompt syntax.

Portability is an architectural option, not a claim that all models are interchangeable.

## Tool Portability

Skills should depend on capabilities where possible rather than hard-coded infrastructure details.

For example, a skill may require a search capability while the harness decides whether that capability is provided by MCP, a direct API or another interface.

Domain 07 explores this boundary in detail.

## Ownership

A governed skill should identify:

- owner;
- maintainer;
- status;
- version;
- evaluation status;
- dependencies;
- change history.

Ownership should remain visible as capability libraries grow.

## Lifecycle States

A capability can move through states such as:

```text
Draft
  |
Experimental
  |
Validated
  |
Production
  |
Deprecated
  |
Retired
```

Promotion should depend on evidence, not enthusiasm.

## Deprecation

Deprecation should identify:

- replacement capability;
- migration path;
- deadline;
- affected consumers;
- compatibility risks.

Removing a skill without understanding dependencies can break downstream workflows.

## Governance

Governance should be proportional to consequence.

Low-risk drafting capability may need lightweight controls.

A capability able to mutate important systems may require:

- stronger permissions;
- approvals;
- auditability;
- stricter evaluation;
- rollback;
- incident ownership.

Domain 11 covers security, permissions and governance in depth.

## Change Management

Before promoting a changed skill, teams can ask:

- What changed?
- Why?
- Which evaluations passed?
- Which consumers are affected?
- Does the change alter permissions?
- Is rollback possible?
- Is documentation current?

This creates an evidence trail around capability evolution.

## Exercise

Define a lifecycle and version policy for a library of generic AI skills.

Include:

1. ownership;
2. versioning;
3. evaluation requirements;
4. promotion gates;
5. deprecation;
6. rollback;
7. retirement.

Then describe how you would replace the underlying model without losing evidence about capability quality.

## Takeaway

> Durable capability needs lifecycle management.

Versioning and governance make skills maintainable across model, tool and organisational change.

Next: **09 — Capstone**.
