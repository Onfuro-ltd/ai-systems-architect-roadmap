# GPU Architecture for AI Inference

## Purpose

Accelerator specifications are ingredients; workload performance is the result.

## Core architecture

Explain compute units, matrix acceleration, precision, VRAM/HBM, caches, CPU/host roles, PCIe and GPU interconnects, kernels, drivers, runtimes, and utilization. Distinguish compute-bound, memory-bandwidth-bound, capacity-bound, communication-bound, and scheduler-bound inference. Prefill and decode can expose different bottlenecks. Benchmark the complete hardware plus software stack rather than selecting from peak FLOPS. Exercise: compare two accelerators for an interactive LLM workload and identify the likely bottlenecks.

## Production standard

Start from representative workloads and measurable SLOs. Preserve model, artifact, runtime, hardware and configuration identity. Test normal load, peak load and failure conditions. Keep authorization, business state and consequential controls outside probabilistic inference. Connect infrastructure telemetry to task quality and successful outcomes.

## Architect checklist

Confirm capacity, bandwidth, compute, context, concurrency, queueing, tenancy, privacy, failure recovery, observability, rollout/rollback and lifecycle economics are explicit rather than assumed.

## Takeaway

> Accelerator specifications are ingredients; workload performance is the result.

Next: **VRAM, Memory Bandwidth and Model Sizing**.
