# 02 — Model Licensing and Governance

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Model Licensing and Governance** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

License review is part of model architecture.

Maintain a registry containing model/revision, source, weight/code/asset licenses, commercial and redistribution rights, restrictions, notices, modification status, derived-artifact lineage, approval owner, and review date. Do not assume every file in a repository has identical terms.

Pin model and license versions: a new model release may change legal terms. Quantizations, conversions, adapters, merged models, distillations, and fine-tunes need traceable lineage.

Use promotion states such as discovered, under review, approved for experiment, approved for production, restricted, and retired. Combine legal/governance review with supply-chain controls: trusted source, integrity verification, controlled loading, dependency provenance, and immutable artifact identity.

Customer contracts, residency commitments, security obligations, and internal policy may be stricter than an upstream license. Seek qualified legal review where consequence warrants it.

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

Next: **03 — Model Formats and Quantization**.
