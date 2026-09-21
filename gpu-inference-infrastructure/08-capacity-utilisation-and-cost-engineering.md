# 08 — Capacity, Utilisation and Cost Engineering

## Purpose

Capacity planning converts demand forecasts and SLOs into safe serving headroom. Utilisation is valuable only while the system retains resilience and acceptable latency.

## Learning outcomes

By the end of this module, you should be able to:
- translate workload distributions into serving-capacity requirements
- plan normal, peak, failure and rollout-overlap capacity
- interpret utilisation together with queueing and SLOs
- calculate cost per successful outcome by workload class

## Demand model

Measure arrival rate, input/output lengths, context, concurrency, model mix, cancellation and time-of-day patterns.

## Headroom

Plan for failures, maintenance, deployment overlap and unexpected peaks. Average demand is not a safe capacity target.

## Utilisation

GPU utilisation alone is incomplete. Track memory/KV occupancy, queue depth, scheduler efficiency, tokens/sec and useful completed work.

## Autoscaling

GPU capacity may have long cold-start paths: provisioning, image pull, artifact load, compilation/warmup and cache population. Measure readiness end-to-end.

## Forecasting

Use historical demand plus planned growth and known events. Revisit forecasts as models or context policies change.

## Cost attribution

Attribute model/runtime/infrastructure cost to workload, tenant or outcome so optimisation decisions are visible.

## Failure modes

- sizing for average demand with no failure headroom
- autoscaler reacts after queues are already unrecoverable
- high GPU utilisation celebrated while p99 latency collapses
- costs cannot be traced to workload/outcome
- deployment overlap exhausts capacity

## Security and governance

Capacity controls should prevent deliberate or accidental resource exhaustion. Apply quotas, rate limits and workload admission by trusted identity.

## Economics and operations

Optimise the full cost curve: enough headroom for resilience, but not so much idle capacity that cost per useful outcome becomes unacceptable.

## Practical exercise

Create a weekly capacity plan from a synthetic traffic distribution. Include one-node failure, deployment overlap, a two-times burst and cold-start delay. Define the trigger for adding capacity.

## Architect checklist

- [ ] normal and failure capacity are both defined
- [ ] cold-start/readiness time is measured
- [ ] utilisation is paired with queue/SLO metrics
- [ ] cost is attributable
- [ ] growth assumptions are revisited

## Primary reading

- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)
- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)

## Mastery gate

Explain when **Capacity, Utilisation and Cost Engineering** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Capacity engineering balances useful utilisation with the headroom required to survive reality.

Next: **09 — Resilience, Observability and Scaling**.
