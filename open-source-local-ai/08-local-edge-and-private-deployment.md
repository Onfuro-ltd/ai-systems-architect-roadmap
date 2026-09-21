# 08 — Local, Edge and Private Deployment

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Local, Edge and Private Deployment** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Developer-local, edge-device, private-server, and private-cloud inference have different trust and operational boundaries.

Privacy is end-to-end: map prompts, retrieval, logs, telemetry, outputs, caches, backups, tools, administrators, and network paths. Self-hosting the model while exporting sensitive traces elsewhere is not a private architecture.

Edge inference can reduce latency, network dependence, and raw-data transmission, but faces memory, compute, power, thermals, storage, device diversity, physical compromise, and update/rollback constraints.

Use verified artifacts, secure update channels, device/server identity, protected endpoints, least privilege, network controls, and versioned rollout/rollback. Support offline devices and version skew where necessary.

Classify data before routing: restricted workloads may require private/local-only routes. If no compliant model is available, safe degradation or rejection can be correct.

Local inference does not make agent tools safe; permissions, secrets, approvals, audit, and idempotency remain separate controls.

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

Next: **09 — Benchmarking Quality, Latency and Cost**.
