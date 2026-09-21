# 01 — Open Source vs Open Weight AI

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Open Source vs Open Weight AI** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

The word open is multidimensional. Distinguish open-source software, open weights, source-available releases, research-only releases, commercially usable models, and proprietary hosted models.

A downloadable checkpoint does not automatically grant unrestricted commercial use, modification, redistribution, or reproducibility. Evaluate weights, architecture, inference code, training code/data, tokenizer, evaluation assets, license rights, and deployment control separately.

Open weights can improve privacy options, offline use, customization, latency control, experimentation, and provider independence, but they transfer operational responsibility. Hosted models can provide frontier capability, elasticity, managed reliability, and lower operational burden.

Model independence is an architecture property: use a canonical model interface and routing/evaluation layer so open-weight and hosted models remain replaceable deployment choices.

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

Next: **02 — Model Licensing and Governance**.
