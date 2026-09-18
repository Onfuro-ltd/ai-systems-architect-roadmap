# 10 — Enterprise AI Capstone

## Purpose

Design a governed, model-independent enterprise AI platform spanning multiple business units, tenants and risk classes.

## Scenario

A global organization operates internal assistants, document intelligence, customer workflows and bounded action-taking agents. It uses hosted and private models and integrates with enterprise systems across several jurisdictions.

## Target architecture

```text
Users / systems
      ↓
Enterprise identity
      ↓
Tenant + authorization + purpose
      ↓
AI control plane
 policy / governance / routing / evaluation
      ↓
AI capabilities
 models / agents / RAG / memory / skills
      ↓
Typed tool + integration layer
      ↓
Systems of record and action
      ↓
Verified outcomes
      ↓
Observability / audit / FinOps / feedback
```

## Required deliverables

Produce AI use-case portfolio and risk taxonomy; enterprise reference architecture; operating model; RACI; identity/delegation design; deterministic tenancy; data classification; residency map; authorized retrieval architecture; retention/deletion model; AI/model gateway; tool/integration registry; write-action controls; governance/control matrix; audit model; exception process; vendor/procurement framework; portability/exit plan; concentration-risk analysis; human-oversight model; progressive-autonomy framework; adoption/change plan; shared platform services; team topology; SLOs; dependency map; incident/degradation plans; business-continuity strategy; cost attribution; evaluation/release governance; and at least three ADRs.

## Failure matrix

Cover wrong tenant, excessive permissions, unauthorized retrieval, residency breach, provider policy change, model deprecation, vendor outage, prompt injection through enterprise content, bad model release, tool side effect, ineffective human approval, shadow AI, stale knowledge, audit gap, cost runaway, dependency outage and failed provider migration.

## Acceptance criteria

The design passes only if identity and tenant context propagate end-to-end; authorization occurs before retrieval/action; systems of record remain authoritative; residency includes derived data and logs; governance controls are executable; material changes trigger evaluation; providers are replaceable behind canonical contracts where practical; human oversight is meaningful; domain teams retain outcome ownership; shared controls are easy to adopt; SLOs include quality where appropriate; incident ownership is explicit; costs are attributable; and organizational knowledge/workflows survive model replacement.

## Final principle

> The enterprise should own the durable intelligence layer—its data, workflows, permissions, evaluations, integrations and outcome feedback—even when external models supply much of the probabilistic intelligence.

**Domain 22 — Enterprise AI complete.**

Next domain: **23 — AI Product Design**.
