# 05 — Parallelism and Multi-GPU Inference

## Purpose

Parallelism can fit larger models or serve more work, but every distribution boundary adds communication and failure cost.

## Learning outcomes

By the end of this module, you should be able to:
- distinguish replica/data, tensor, pipeline and expert parallelism
- explain when scale-out replicas are simpler than model sharding
- reason about topology and collective communication
- choose parallelism from model fit, throughput and reliability requirements

## Replica scaling

If a model fits comfortably on one serving unit, independent replicas are often the simplest way to add throughput and resilience.

## Tensor parallelism

Tensor operations are partitioned across devices. It can reduce per-device model state but requires frequent communication and topology-aware execution.

## Pipeline parallelism

Layers/stages are partitioned and microbatches flow through them. It can fit large models but introduces bubbles, scheduling complexity and stage imbalance.

## Expert parallelism

MoE experts can be distributed across devices. Routing imbalance and all-to-all communication become architectural concerns.

## Topology

NVLink/NVSwitch-class links, PCIe and multi-node networking have very different characteristics. The same GPU count can produce different outcomes under different topology.

## Failure domain

A sharded model may fail when any required participant fails, while replicated serving can route around one lost replica. Capacity plans must include this difference.

## Failure modes

- using multi-GPU because devices are available rather than because the workload requires it
- communication dominating computation
- pipeline stage imbalance reducing utilisation
- expert routing hotspots
- one failed rank taking down a large serving unit

## Security and governance

Distributed serving expands the administrative and network attack surface. Restrict management networks, authenticate service-to-service communication and preserve tenant policy above the distributed runtime.

## Economics and operations

Parallelism can increase both capex/hourly cost and engineering burden. Compare it with smaller models, quantization, replicas and routing before committing to a distributed topology.

## Practical exercise

Given a model that barely exceeds one GPU and a separate high-throughput model that fits easily, propose different scaling strategies. Justify topology, resilience and benchmark criteria.

## Architect checklist

- [ ] parallelism solves a stated capacity/throughput problem
- [ ] communication topology is documented
- [ ] failure behaviour is modelled
- [ ] simpler alternatives were benchmarked
- [ ] rollout and rollback can operate across the topology

## Primary reading

- [PyTorch Tensor Parallel documentation](https://docs.pytorch.org/docs/stable/distributed.tensor.parallel)
- [PyTorch Pipeline Parallel tutorial](https://docs.pytorch.org/tutorials/intermediate/pipelining_tutorial.html)
- [vLLM documentation](https://docs.vllm.ai/en/stable/)

## Mastery gate

Explain when **Parallelism and Multi-GPU Inference** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Use the least distributed architecture that satisfies model fit and workload SLOs.

Next: **06 — Inference Servers, Scheduling and Admission Control**.
