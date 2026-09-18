# Prefill, Decode and KV Cache

## Purpose

Context consumes infrastructure as both processing work and persistent generation state.

## Core architecture

Separate prefill, time to first token, and autoregressive decode. Explain KV-cache purpose and how architecture, sequence length, precision and active sequences determine capacity. Long context increases prefill work, memory pressure, contention and tail latency. Use retrieval, summarization and context budgets rather than treating maximum context as free. Cover KV paging/block management, safe prefix reuse, cancellation, and workload-specific context distributions. Exercise: compare short interactive, long-document and background-generation workloads.

## Production standard

Start from representative workloads and measurable SLOs. Preserve model, artifact, runtime, hardware and configuration identity. Test normal load, peak load and failure conditions. Keep authorization, business state and consequential controls outside probabilistic inference. Connect infrastructure telemetry to task quality and successful outcomes.

## Architect checklist

Confirm capacity, bandwidth, compute, context, concurrency, queueing, tenancy, privacy, failure recovery, observability, rollout/rollback and lifecycle economics are explicit rather than assumed.

## Takeaway

> Context consumes infrastructure as both processing work and persistent generation state.

Next: **Batching, Concurrency and Throughput**.
