# 10 — Hybrid Routing and Model Independence

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **10 — Hybrid Routing and Model Independence** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Different workloads require different capability, privacy, latency, availability, and economics.

Use: workflow → canonical AI request → policy/privacy gate → capability filter → model router → approved local/private/hosted route → canonical validation/evaluation.

Policy eligibility comes before optimization. A restricted request must never fall back to a disallowed external route because the private model is unavailable.

Maintain a capability registry with approved models, capabilities, context limits, deployment locations, governance/license status, evaluation evidence, cost characteristics, and health.

Use cheaper/smaller models for bounded tasks and escalate difficult cases when measured value justifies it. Do not rely solely on model self-confidence.

Version routing rules, adapters, evaluation data, thresholds, and artifacts. Shadow/canary new routes where safe. A fallback is not resilience until it has been tested with production-shaped load.

Record selected route, eligibility, reason/policy version, model/artifact, latency, cost, fallback/escalation, validation, and evaluated outcome.

## Architecture lens

Evaluate this topic through **Understand → Build → Architect → Lead**. Separate model capability from system guarantees, and measure representative workloads rather than relying on model-size or benchmark marketing.

## Production rules

Keep business workflows above a stable model/runtime interface. Preserve artifact identity and provenance. Test quality, latency, reliability, privacy, security, and cost. Treat model/runtime changes as versioned production changes with rollback.

## AI-system boundary

```text
Business workflow
      ↓
Canonical AI capability
      ↓
Policy / governance
      ↓
Runtime or model adapter
      ↓
Inference
      ↓
Validation + evaluation
```

Probabilistic output never replaces deterministic authorization, state, or consequential execution controls.

## Exercise

Create an architecture decision record for this topic using a representative workload. Define requirements, alternatives, measurements, failure modes, governance, observability, and the evidence required for adoption.

## Takeaway

Choose technology from measured requirements and lifecycle cost, not novelty.

Next: **11 — Open-Source and Local AI Capstone**.
