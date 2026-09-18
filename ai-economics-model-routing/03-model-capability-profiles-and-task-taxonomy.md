# 03 — Model Capability Profiles and Task Taxonomy

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Model Capability Profiles and Task Taxonomy** within AI Economics and Model Routing;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Route from evidence about specific workloads rather than a single global model ranking.

## Task taxonomy

Classify work by capability needs: extraction, classification, transformation, coding, reasoning, multilingual work, tool use, vision, long context, structured output, generation and domain specialization.

Also record consequence, privacy, latency and volume.

## Capability profile

For each model/configuration track evaluated task quality, critical failures, context limits, modalities, structured/tool behaviour, latency distribution, throughput, availability, deployment regions, privacy eligibility and cost.

## Versioning

Profiles belong to specific model/provider/runtime versions. Do not treat a model family name as permanent evidence.

## Evaluation source

Prefer internal representative evaluations for routing. Public benchmarks can inform discovery but may not represent the actual workload.

## Confidence

Require enough observations before aggressive routing changes. Sparse evidence should produce conservative decisions.

## Exercise

Create a capability registry for five hypothetical models across ten task classes without declaring one universally best.

## Takeaway

> A router needs a map of task-specific capabilities, not a leaderboard.

Next: **04 — Routing Architectures and Policy Gates**.
