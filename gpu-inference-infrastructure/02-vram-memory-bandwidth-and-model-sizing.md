# VRAM, Memory Bandwidth and Model Sizing

## Purpose

Fitting model weights is only the first capacity test.

## Core architecture

Estimate weight memory from parameter count and representation, then add quantization metadata, KV cache, temporary tensors, runtime workspace, communication buffers, fragmentation, concurrency, and operational headroom. Explain why memory bandwidth can dominate autoregressive decode. For MoE distinguish total and active parameters, resident experts, routing and communication. Host-RAM or NVMe offload can increase executable capacity while harming latency. Multi-GPU sharding adds capacity and communication. Exercise: size one model at multiple precisions and contexts with realistic concurrency and headroom.

## Production standard

Start from representative workloads and measurable SLOs. Preserve model, artifact, runtime, hardware and configuration identity. Test normal load, peak load and failure conditions. Keep authorization, business state and consequential controls outside probabilistic inference. Connect infrastructure telemetry to task quality and successful outcomes.

## Architect checklist

Confirm capacity, bandwidth, compute, context, concurrency, queueing, tenancy, privacy, failure recovery, observability, rollout/rollback and lifecycle economics are explicit rather than assumed.

## Takeaway

> Fitting model weights is only the first capacity test.

Next: **Prefill, Decode and KV Cache**.
