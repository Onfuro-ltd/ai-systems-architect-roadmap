# 03 — Prefill, Decode and KV Cache

## Purpose

Prompt processing and token generation are different phases with different resource behaviour. Treating them as one undifferentiated latency number hides important capacity and scheduling decisions.

## Learning outcomes

By the end of this module, you should be able to:
- distinguish prefill, time to first token and decode
- explain why KV cache exists and how it scales with active sequences
- design context budgets from workload evidence
- reason about prefix caching, chunked/disaggregated prefill and cancellation without assuming one runtime

## Prefill

The input sequence is processed to build internal state. Longer prompts increase work before the first generated token and can create bursty compute demand.

## Decode

Generation proceeds token by token. Each step reuses cached attention state while reading model weights/state, so the performance shape differs from prefill.

## KV cache

Caching prior key/value states avoids recomputing the full prefix at every decode step. The cache becomes a major shared resource under long contexts and concurrency.

## Context is infrastructure

Advertised maximum context is not free capacity. It affects prefill latency, memory occupancy, queueing and cost. Design application-level context budgets.

## Cache management

Paged/block-based KV management reduces fragmentation and allows more flexible allocation. Prefix caching can help repeated trusted prefixes, but cache identity and authorization boundaries matter.

## Scheduling

Runtimes may chunk prefill or separate prefill/decode resources. Evaluate these patterns against workload mix rather than assuming they improve every service.

## Failure modes

- tracking total latency while ignoring time to first token
- unbounded context causing KV exhaustion and tail-latency spikes
- unsafe cache reuse across tenants or incompatible prompt state
- cancelled requests retaining resources too long
- long-prefill jobs starving interactive decode

## Security and governance

Cache reuse must respect identity and data isolation. Never allow cross-tenant prefix reuse merely because tokens match. Context limits are resource-governance controls as well as product controls.

## Economics and operations

Measure TTFT, inter-token latency, throughput, memory occupancy and successful-task cost by context bucket. A feature that increases maximum context may reduce useful concurrent capacity.

## Practical exercise

Benchmark short interactive, long-document and background-generation profiles. Record TTFT, decode rate, KV occupancy and queue time, then propose context and scheduling policies.

## Architect checklist

- [ ] prefill and decode metrics are separated
- [ ] context distributions are measured
- [ ] KV occupancy is observable
- [ ] caching has identity/isolation rules
- [ ] cancellation and overload release resources predictably

## Primary reading

- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [PagedAttention / vLLM paper](https://arxiv.org/abs/2309.06180)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)

## Mastery gate

Explain when **Prefill, Decode and KV Cache** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Context length is a capacity decision, not just a model feature.

Next: **04 — Batching, Concurrency and Throughput**.
