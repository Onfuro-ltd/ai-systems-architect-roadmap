# 08 — Cost, Latency and Outcome Economics

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Cost, Latency and Outcome Economics** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

An AI system that is accurate but too slow or expensive may still be a poor production system.

Evaluation should measure the economics of outcomes, not model quality alone.

## Core Principle

> Optimise for acceptable outcomes per unit of cost and time.

## Total Cost

AI-system cost can include:

- input tokens;
- output tokens;
- reasoning tokens where applicable;
- embeddings;
- retrieval;
- tool/API charges;
- infrastructure;
- human review;
- retries;
- failed runs.

Track cost at the task level.

## Latency

Useful measures include:

- time to first useful output;
- total task latency;
- tool latency;
- queue latency;
- approval latency.

A long workflow may have different acceptable latency from an interactive assistant.

## Quality-Cost Frontier

Compare variants across quality and cost.

A larger model may produce slightly better output at much higher cost.

A smaller model may be acceptable for routine tasks.

## Routing Economics

Model routing can choose:

- smaller model for simple task;
- stronger model for difficult task;
- escalation for uncertainty.

Evaluate routing against a baseline.

## Retry Economics

Retries consume cost.

Track:

- retries per task;
- cost of retries;
- success after retry.

A system that succeeds only after many retries may be operationally weak.

## Multi-Agent Economics

Multiple agents multiply model calls.

Compare multi-agent performance against:

- single agent;
- deterministic workflow.

The added quality must justify the extra cost and latency.

## Human Review Economics

Human review can be expensive but valuable for high-risk cases.

A selective review strategy can optimise:

```text
automation for low risk
+
human review for uncertain/high risk
```

## Outcome Metric

The real objective may be:

- issue resolved;
- report accepted;
- task completed;
- defect caught;
- decision improved.

Cost per successful outcome is often more useful than cost per model call.

## Failure Cost

Some failures are more expensive than others.

Examples:

- harmless formatting error;
- incorrect customer action;
- unauthorised write;
- missed compliance issue.

Weight evaluation by consequence where appropriate.

## Latency Budget

Break an end-to-end latency target into:

```text
routing
+ model
+ retrieval
+ tools
+ validation
+ orchestration
```

Then optimise the largest contributors.

## Caching

Caching can reduce cost and latency.

Evaluate whether cached information remains:

- fresh;
- authorised;
- correct for the task.

## Model Replacement

Before replacing a model for cost, run the complete evaluation suite.

Cheaper inference is not a saving if failure and human-review costs rise.

## Exercise

Compare three hypothetical system variants:

- premium model;
- routed model mix;
- multi-agent design.

Measure:

1. task success;
2. cost;
3. latency;
4. escalation;
5. failure consequence.

Choose based on the outcome frontier, not model prestige.

## Takeaway

> The production objective is not maximum intelligence. It is reliable value at acceptable cost and latency.

Next: **09 — Capstone**.
