# 02 — VRAM, Memory Bandwidth and Model Sizing

## Purpose

Fitting model weights is only the first capacity test. Production memory planning must include the dynamic state and runtime overhead created by real prompts, outputs and concurrency.

## Learning outcomes

By the end of this module, you should be able to:
- estimate model-weight memory from parameter count and representation
- explain the role of KV cache, runtime workspace and fragmentation
- reason about memory bandwidth as a decode constraint
- build a capacity model that includes context distribution, concurrency and operational headroom

## Weight memory

A first approximation is parameters multiplied by bytes per represented parameter. Quantized formats add metadata and may require scales, zero-points or runtime-specific packing.

## Runtime memory

Production serving also consumes KV cache, temporary tensors, CUDA graphs or runtime workspaces, communication buffers, allocator headroom and framework overhead.

## KV cache

KV memory grows with active sequence state and architecture. Long context and many concurrent sequences can exhaust memory even when weights occupy only part of VRAM.

## Bandwidth

Autoregressive decoding repeatedly accesses large model state for relatively little new work per token. Effective memory bandwidth can therefore be a stronger limiter than headline arithmetic throughput in some regimes.

## MoE models

Separate total parameters from active parameters, but do not assume inactive experts cost nothing. Residency strategy, routing, expert parallelism and communication determine actual memory and performance.

## Offload and sharding

CPU/NVMe offload can increase executable capacity while increasing latency. Tensor/pipeline sharding can fit larger models but introduces interconnect and scheduling costs.

## Failure modes

- capacity spreadsheet excludes KV cache or runtime workspace
- quantized model fits but kernels or quality are unsuitable
- long-context requests evict useful capacity and collapse concurrency
- host offload causes unacceptable tail latency
- memory fragmentation or OOM creates retry storms

## Security and governance

Memory planning is also an isolation concern. Enforce tenant/context limits before allocation, prevent one workload from exhausting shared serving capacity, and avoid using untrusted prompt length as an unrestricted resource request.

## Economics and operations

Model several workload percentiles rather than one maximum context. Cost depends on both static model residency and dynamic occupancy. The economical configuration is the one that meets quality/SLOs at realistic utilization.

## Practical exercise

Create a sizing sheet for one model under three representations and three context/concurrency profiles. Include weights, estimated dynamic state, headroom and a measurement plan to validate each estimate.

## Architect checklist

- [ ] weight size and runtime memory are separated
- [ ] KV/context assumptions are explicit
- [ ] bandwidth and capacity are both considered
- [ ] headroom exists for fragmentation and failures
- [ ] limits prevent one workload from exhausting the pool

## Primary reading

- [NVIDIA CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [PagedAttention / vLLM paper](https://arxiv.org/abs/2309.06180)

## Mastery gate

Explain when **VRAM, Memory Bandwidth and Model Sizing** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> VRAM sizing is workload sizing: weights, context, concurrency and runtime behaviour must be modelled together.

Next: **03 — Prefill, Decode and KV Cache**.
