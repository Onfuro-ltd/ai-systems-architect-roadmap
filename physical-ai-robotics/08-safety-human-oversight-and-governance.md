# 08 — Safety, Human Oversight and Governance

## Purpose

Build independent controls around probabilistic embodied intelligence.

## Safety architecture

```text
AI proposal
   ↓
Deterministic constraints
   ↓
Safety supervisor
   ↓
Approved controller
   ↓
Physical action
```

Emergency stop and protective functions should not depend on an LLM deciding to cooperate.

## Limits

Enforce speed, force, workspace, joint, proximity, zone and action-authority limits using appropriate deterministic/safety mechanisms.

## Humans

Define when a human supervises, approves, takes over or must remain physically separated. Human-in-the-loop is meaningful only if the person has enough information and time to intervene.

## Operating domain

Specify environments, objects, payloads, lighting/weather, people proximity and other conditions under which autonomy is validated.

Outside the domain, degrade or stop.

## Hazard analysis

Identify hazards, initiating failures, severity, exposure and mitigations. Use applicable engineering safety standards and qualified specialists for real deployments.

## Security

Remote compromise can become physical harm. Protect update channels, credentials, command paths, networks and fleet management.

## Audit

Record commanded intent, approved action, relevant state, safety intervention and outcome without relying on hidden reasoning.

## Exercise

Threat- and hazard-model a collaborative robot performing a variable manipulation task near workers.

## Takeaway

> Safety must be an independent system property, not a behaviour we merely ask the model to exhibit.

Next: **09 — Robotics Infrastructure, Fleet Operations and Evaluation**.
