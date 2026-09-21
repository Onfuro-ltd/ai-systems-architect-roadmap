# 07 — Hardware, Memory and Performance

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Hardware, Memory and Performance** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Performance emerges from model architecture, precision, memory hierarchy, compute, bandwidth, storage, runtime, and workload.

Capacity answers whether execution is possible. Bandwidth and compute determine much of the speed. Workload determines whether that speed is useful.

Size weights approximately, then include KV cache, runtime buffers, concurrency, and overhead. Autoregressive decode can be memory-bandwidth sensitive, so headline compute alone is insufficient.

Large system RAM can enable models beyond VRAM capacity, while offload or streamed-weight approaches can use NVMe as another tier. This expands executable capacity but can make storage bandwidth part of token latency.

For MoE distinguish total vs active parameters and account for expert placement/routing. Multi-device inference increases capacity but introduces interconnect/synchronization costs.

Owned hardware also requires power, thermals, redundancy, maintenance, and utilization analysis. Size hardware from measured workload SLOs, not from the largest accelerator specification available.

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

Next: **08 — Local, Edge and Private Deployment**.
