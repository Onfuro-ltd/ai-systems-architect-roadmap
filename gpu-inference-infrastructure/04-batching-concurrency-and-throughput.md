# 04 — Batching, Concurrency and Throughput

## Purpose

Maximum throughput and best interactive latency are different optimisation targets. Scheduling must balance utilisation with queueing, fairness and SLOs.

## Learning outcomes

By the end of this module, you should be able to:
- compare static and continuous batching conceptually
- explain saturation, queueing and tail latency under concurrency
- design workload classes and fairness controls
- build a production-shaped load test rather than a single-user benchmark

## Batching

Batching groups work so accelerators can process more useful computation together. Static batches suit predictable workloads; continuous batching admits and retires sequences dynamically.

## Concurrency

Concurrency includes active sequences, tokens, KV occupancy and downstream tool/workflow pressure—not just open HTTP connections.

## Saturation

As demand approaches capacity, queueing grows. Timeouts can trigger retries, which can amplify load. Bound queues and apply backpressure.

## Workload classes

Interactive, batch, premium and background work may require separate priorities, pools or quotas. A global FIFO queue can violate business SLOs.

## Fairness

Multi-tenant serving should account for per-tenant rate, concurrency and resource consumption so one client cannot monopolise capacity.

## Load testing

Use realistic input/output length distributions, bursts, cancellation and degraded-capacity scenarios. Report percentiles, not averages alone.

## Failure modes

- optimising throughput while interactive p95/p99 latency becomes unusable
- unbounded queues converting overload into delayed failure
- retry storms after timeouts
- large requests starving small requests
- tenant unfairness or cost abuse

## Security and governance

Admission control belongs at a trusted boundary. Enforce quotas and tenant identity outside the model, and avoid exposing scheduler administrative controls to untrusted callers.

## Economics and operations

Capacity utilisation improves unit economics only while SLOs remain acceptable. Measure cost per completed outcome by workload class, including retries and rejected work.

## Practical exercise

Design a scheduler for three workload classes sharing one GPU pool. Define priorities, queue bounds, fairness, overload behaviour and the metrics that prove the policy works.

## Architect checklist

- [ ] queue bounds are explicit
- [ ] latency percentiles and throughput are measured together
- [ ] workload classes have defined SLOs
- [ ] tenant fairness and quotas are enforced
- [ ] retry behaviour is bounded

## Primary reading

- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)

## Mastery gate

Explain when **Batching, Concurrency and Throughput** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Throughput is useful only when the scheduler preserves the latency and fairness the product requires.

Next: **05 — Parallelism and Multi-GPU Inference**.
