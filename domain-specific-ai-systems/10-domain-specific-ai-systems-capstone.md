# 10 — Domain-Specific AI Systems Capstone

## Purpose

Design a model-independent domain AI platform whose accumulated intelligence survives changes in foundation models.

## Scenario

An enterprise operates a specialized domain with proprietary terminology, structured and unstructured data, expert procedures, deterministic policies, external systems, historical outcomes and several AI-powered workflows.

## Target architecture

```text
Domain intent
     ↓
Canonical ontology / schema
     ↓
Authorized knowledge + authoritative state
     ↓
Domain skills / workflows
     ↓
Model router + specialists
     ↓
Structured interpretation
     ↓
Deterministic policies / constraints
     ↓
Typed tools
     ↓
Permissions + approval
     ↓
Verified domain outcome
     ↓
Evaluation + curated feedback
     ↓
Versioned domain intelligence
```

## Required deliverables

Produce domain intelligence inventory; capability map; canonical ontology/schema; identity-resolution rules; authoritative-source hierarchy; knowledge/retrieval architecture; provenance/freshness model; deterministic policy engine; exception model; skill registry; workflow state machines; typed tool contracts; specialist/tuning decision framework; routing policy; domain gold set; slice metrics; catastrophic-failure gates; outcome/feedback pipeline; root-cause taxonomy; temporal knowledge/versioning; domain release manifest; observability; ownership/governance model; multitenant isolation; model-portability evaluation; and at least three ADRs.

## Failure matrix

Cover ambiguous terminology, duplicate entity identity, stale fact, conflicting sources, unauthorized retrieval, policy interpreted incorrectly, policy version mismatch, skill drift, tool schema change, model regression, specialist underperformance, tuning on volatile facts, evaluation contamination, feedback misclassification, cross-tenant leakage, historical reconstruction failure and provider migration failure.

## Acceptance criteria

The design passes only if domain concepts are explicit; current facts remain authoritative outside model weights; policies are deterministic where expressible; reusable procedures live in skills/workflows; tools are typed and permissioned; tuning is reserved for learned behaviour; evaluation reflects real domain failures; feedback is curated; temporal versions reconstruct historical decisions; tenant knowledge is isolated; releases identify all behaviour-affecting domain assets; and representative workflows can move to another eligible model without losing encoded domain intelligence.

## Final principle

> The strongest domain AI moat is not access to a particular foundation model. It is the organization's continuously evaluated system of knowledge, semantics, workflows, policies, tools and verified outcomes.

**Domain 26 — Domain-Specific AI Systems complete.**

Next domain: **27 — AI-Native Commerce and Operations**.
