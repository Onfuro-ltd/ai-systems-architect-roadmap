# Inference Servers, Scheduling and Admission Control

## Purpose

A production inference control plane decides what work is allowed, where it runs, and what happens when capacity is unavailable.

## Core architecture

Design gateway, authentication, canonical inference API, policy, admission control, router/scheduler, serving pools, streaming, cancellation, metrics and accounting. Admission should consider eligibility, context/output limits, quotas, queue capacity, deadlines and fallback. Separate queue, execution and client deadlines. Cover resident vs dynamic model loading, adapter compatibility/isolation, meaningful readiness, backpressure and cost attribution. Keep runtime-specific APIs behind adapters and business policy outside model servers. Exercise: design a gateway for three models and two priority classes across shared tenant pools.

## Production standard

Start from representative workloads and measurable SLOs. Preserve model, artifact, runtime, hardware and configuration identity. Test normal load, peak load and failure conditions. Keep authorization, business state and consequential controls outside probabilistic inference. Connect infrastructure telemetry to task quality and successful outcomes.

## Architect checklist

Confirm capacity, bandwidth, compute, context, concurrency, queueing, tenancy, privacy, failure recovery, observability, rollout/rollback and lifecycle economics are explicit rather than assumed.

## Takeaway

> A production inference control plane decides what work is allowed, where it runs, and what happens when capacity is unavailable.

Next: **Cloud GPUs vs Owned Hardware**.
