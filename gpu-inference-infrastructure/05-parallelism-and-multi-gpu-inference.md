# Parallelism and Multi-GPU Inference

## Purpose

More GPUs add resources and communication; they do not guarantee proportional performance.

## Core architecture

Explain tensor, pipeline, replica/data and expert parallelism plus hybrid combinations. Tensor and expert approaches depend strongly on communication and topology; pipeline approaches introduce scheduling and imbalance; replicas are often simpler when a model fits independently. Compare scale-up with scale-out, intra-node with inter-node communication, placement/topology awareness, and failure domains. Benchmark scaling efficiency rather than assuming linear gains. Exercise: compare a sharded large model with a smaller replicated model on quality, throughput, reliability and cost.

## Production standard

Start from representative workloads and measurable SLOs. Preserve model, artifact, runtime, hardware and configuration identity. Test normal load, peak load and failure conditions. Keep authorization, business state and consequential controls outside probabilistic inference. Connect infrastructure telemetry to task quality and successful outcomes.

## Architect checklist

Confirm capacity, bandwidth, compute, context, concurrency, queueing, tenancy, privacy, failure recovery, observability, rollout/rollback and lifecycle economics are explicit rather than assumed.

## Takeaway

> More GPUs add resources and communication; they do not guarantee proportional performance.

Next: **Inference Servers, Scheduling and Admission Control**.
