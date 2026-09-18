# 05 — llama.cpp and Portable Inference

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — llama.cpp and Portable Inference** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Portable inference runtimes show how quantized open-weight models can execute across CPUs, GPUs, laptops, workstations, and servers.

A llama.cpp-style runtime is valuable for local experimentation, offline/private workflows, heterogeneous hardware, and selected production use cases. GGUF-style artifacts and CPU/GPU offload demonstrate heterogeneous placement across memory tiers.

Memory mapping and OS page caching mean storage can influence large-model behaviour. Fitting on disk does not imply interactive performance.

Keep applications behind a canonical inference contract so the portable runtime is one adapter, not the business architecture.

Benchmark the exact model + quantization + runtime + hardware combination for quality, TTFT, decode rate, context, memory, utilization, storage behaviour, power, and concurrency.

Do not assume a lightweight single-user runtime is automatically optimal for high-concurrency production serving.

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

Next: **06 — vLLM and Production Model Serving**.
