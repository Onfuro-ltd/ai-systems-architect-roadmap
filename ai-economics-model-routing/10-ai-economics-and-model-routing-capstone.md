# 10 — AI Economics and Model Routing Capstone

## Purpose

Design a model-independent routing and economic-control platform.

## Scenario

A multitenant AI platform can use hosted frontier models, smaller hosted models, private open-weight models and tuned specialists. Workloads vary by privacy, modality, consequence, quality, latency, context and volume.

## Target architecture

```text
Task / workflow
      ↓
Task + risk classification
      ↓
Deterministic eligibility
 privacy / residency / license / tenant / capability
      ↓
Candidate model set
      ↓
Router
 quality / latency / availability / cost evidence
      ↓
Execution
      ↓
Validation / escalation / fallback
      ↓
Verified outcome
      ↓
Cost + quality + latency telemetry
      ↓
Capability registry + routing evaluation
```

## Required deliverables

Produce task taxonomy; capability registry; deterministic eligibility policy; canonical provider/runtime interface; routing strategies; cascade design; fallback matrix; context budgets; caching policy; batching strategy; specialist/local/open economics; hosted-versus-owned TCO; offline router evaluation; online experiment controls; oracle-gap analysis; drift/re-evaluation triggers; tenant/workflow cost attribution; budgets/anomaly detection; cost-per-success dashboard; routing rollback; and at least three ADRs.

## Failure matrix

Cover wrong task classification, policy-ineligible route, under-routing quality failure, over-routing cost waste, false confidence, cascade loop, provider outage, rate limit, latency spike, model-version drift, stale capability profile, cache leakage, excessive context, retry storm, local capacity failure, cost anomaly and bad online reward signal.

## Acceptance criteria

The design passes only if policy eligibility precedes optimization; no model is globally ranked as best; capability evidence is task-specific and versioned; critical quality floors cannot be traded for cost; cascades have reliable validation and bounded attempts; fallbacks remain compliant; cache identity preserves tenant/policy semantics; total workflow cost includes retries and tools; self-hosting uses realistic utilization/TCO; routing itself is evaluated; online exploration is risk-bounded; spend is attributable to useful outcomes; and applications remain independent of model/provider choice.

## Final principle

> The economically intelligent AI system does not ask which model is cheapest or strongest. It asks which eligible route delivers the required outcome with the best measured combination of quality, latency, reliability and total cost.

**Domain 21 — AI Economics and Model Routing complete.**

Next domain: **22 — Enterprise AI**.
