# 06 — Caching, Batching and Context Economics

## Purpose

Reduce repeated AI work without changing semantics or weakening isolation.

## Context economics

Every unnecessary token can increase cost, prefill latency and infrastructure pressure. Context engineering is therefore an economic discipline.

## Retrieval

Retrieve the smallest evidence set that preserves task quality. More documents are not automatically better context.

## Caching layers

Possible caches include deterministic preprocessing, retrieval results, embeddings, stable prompt prefixes, provider/runtime prefix caches and complete responses for truly equivalent requests.

## Cache identity

Include all behaviour-affecting inputs and versions. A stale response from a different policy, tenant, model or source state is not a valid optimization.

## Privacy

Never share cached sensitive context across tenants/users unless the architecture explicitly permits it.

## Batching

Batch asynchronous work where the model/runtime/provider offers economic or throughput benefit and latency requirements permit.

## Output control

Constrain generation length and structured output to what the workflow actually consumes.

## Exercise

Redesign a high-volume document workflow to reduce context, duplicate retrieval and repeated model calls while preserving evaluation quality.

## Takeaway

> The cheapest inference is often the inference you safely avoid.

Next: **07 — Specialist, Local and Open-Model Economics**.
