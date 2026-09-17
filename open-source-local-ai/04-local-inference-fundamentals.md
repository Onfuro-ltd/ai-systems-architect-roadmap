# 04 — Local Inference Fundamentals

## Purpose

Local inference means operating the execution boundary yourself.

Understand model load, tokenization, prefill, autoregressive decode, stopping, and streaming. Measure queue time, time to first token, inter-token latency, total latency, and throughput.

Performance can be limited by compute, memory bandwidth/capacity, storage, kernels, synchronization, or data movement. CPU inference can be viable for quantized/smaller models and low concurrency. GPUs provide high parallel compute/bandwidth but introduce VRAM, power, utilization, and cost constraints.

Long contexts increase prefill work and KV-cache demand. Single-request speed and multi-user throughput are different objectives; batching trades utilization against latency.

Expose a stable internal inference API even on one machine. Plan for OOM, corrupt artifacts, load failure, runaway context, stalled generation, thermal throttling, disk pressure, overload, and worker crash.

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

Next: **05 — llama.cpp and Portable Inference**.
