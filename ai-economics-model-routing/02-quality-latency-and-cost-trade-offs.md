# 02 — Quality, Latency and Cost Trade-offs

## Purpose

Treat quality, latency, reliability and cost as a joint optimization problem.

## Pareto frontier

Some models are dominated: another option may be better or equal on required quality, latency and cost. Focus on non-dominated choices for each workload.

## Quality threshold

For many tasks the goal is not maximum possible benchmark quality. It is quality above a defined acceptance threshold with acceptable critical-error risk.

## Latency

TTFT, total latency and tail latency can affect abandonment, worker productivity and downstream queueing. Latency therefore has business cost.

## Reliability

Availability, schema adherence, tool-call correctness and provider limits affect effective economics.

## Consequence weighting

High-risk tasks may justify more expensive models, additional verification or human approval.

## Utility

A routing objective can conceptually combine task success, latency, cost and risk, but do not hide hard safety/policy constraints inside a weighted score.

## Exercise

Plot several model configurations on quality/latency/cost axes and identify which remain eligible after task and risk thresholds.

## Takeaway

> First satisfy hard requirements; then optimize economics among the options that remain.

Next: **03 — Model Capability Profiles and Task Taxonomy**.
