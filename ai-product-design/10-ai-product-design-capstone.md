# 10 — AI Product Design Capstone

## Purpose

Design an AI product that is useful, understandable, controllable and measurable from first interaction through production operation.

## Scenario

A business operations product uses AI to investigate issues, combine evidence, recommend actions, prepare changes and eventually execute selected low-risk workflows under bounded authority.

## Target experience

```text
User goal
   ↓
AI capability boundary
   ↓
Evidence-backed proposal
   ↓
Uncertainty / missing information
   ↓
Edit / approve / reject / escalate
   ↓
Bounded action
   ↓
Verified outcome
   ↓
Correction + feedback
   ↓
Product evaluation
```

## Required deliverables

Produce user/job definition; bounded capability contract; task/risk taxonomy; interaction-pattern choices; durable task-state model; uncertainty language and states; evidence/provenance UX; approval design; progressive-autonomy ladder; user-control model; correction UX; undo/reversibility rules; failure taxonomy; graceful-degradation matrix; UNKNOWN-outcome handling; accessibility requirements; feedback model; verified-learning pipeline; product scorecard; user-research plan; AI capability architecture; release/evaluation gates; kill switches; cost-per-outcome model; lifecycle/retirement plan; and at least three ADRs.

## Failure matrix

Cover hallucinated answer, missing evidence, stale data, misleading confidence, wrong citation, permission denial, tool failure, provider outage, slow response, partial workflow completion, unknown external action outcome, ineffective approval, user over-trust, user under-trust, inaccessible generated UI, feedback contamination, model regression and cost increase.

## Acceptance criteria

The design passes only if product promises map to evaluated capability; exact rules remain deterministic; uncertainty can be represented as UNKNOWN; evidence is inspectable where consequential; approvals show material effects; autonomy is bounded and evidence-driven; users can interrupt/correct/recover; partial and ambiguous outcomes are explicit; failure modes have safe next steps; feedback is curated before learning; value metrics include outcomes and critical errors; product state survives model sessions; and the product remains portable across model/provider changes.

## Final principle

> Design AI products so that users remain oriented: they should know what the system is doing, why it believes the result, what it will do next, and where human authority still applies.

**Domain 23 — AI Product Design complete.**

Next domain: **24 — Business Automation**.
