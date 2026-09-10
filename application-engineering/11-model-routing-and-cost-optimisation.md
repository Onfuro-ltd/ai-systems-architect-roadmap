# Model Routing and Cost Optimisation

## Purpose

Production AI systems should not simply ask: "What is the most powerful model available?"

The better question is:

> What level of intelligence is required for this specific task, at an acceptable cost, latency and risk level?

Model routing is the architectural discipline of selecting the right model, configuration or execution path for each request.

## The core principle

Models are tools with different trade-offs.

A production system should optimise for:

- quality of outcome;
- reliability;
- latency;
- cost;
- privacy;
- availability;
- operational simplicity.

The objective is not minimum token cost or maximum model capability. It is the lowest total cost of achieving the required outcome reliably.

## Why one model is rarely enough

Different tasks have different requirements:

| Task | Typical requirement |
| --- | --- |
| Classification | Fast, cheap, consistent |
| Extraction | Structured output reliability |
| Customer response drafting | Language quality |
| Complex analysis | Reasoning capability |
| Private data processing | Privacy/control |
| High-volume automation | Cost efficiency |

Using a frontier model for every request can be wasteful. Using the cheapest model everywhere can reduce quality and increase operational cost through failures.

## Basic routing architecture

```text
                 Application Request
                         |
                         v
                  Routing Layer
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
   Fast Model      Reasoning Model    Private Model
        |                |                |
        +----------------+----------------+
                         |
                    Validation
                         |
                     Outcome
```

## Routing strategies

### Rule-based routing

Explicit business rules decide the model.

Example:

- translation → language model A;
- classification → small model;
- financial analysis → stronger reasoning model.

Advantages:
- predictable;
- easy to audit;
- simple to maintain.

Limitations:
- requires manual rules;
- may not adapt automatically.

### Capability-based routing

The system classifies the required capability first.

Example:

```text
Simple extraction
        |
        v
Small structured model

Complex reasoning
        |
        v
Frontier reasoning model
```

### Adaptive routing

The system uses signals such as:

- task complexity;
- historical success rate;
- confidence;
- latency requirements;
- cost limits.

This requires stronger evaluation and monitoring.

## The danger of model abstraction

Abstraction is valuable, but hiding all model differences is a mistake.

Good abstraction:

- common interfaces;
- logging;
- routing;
- cost tracking;
- fallback handling.

Bad abstraction:

- pretending every model behaves identically;
- removing model-specific strengths;
- preventing deliberate model selection.

The architecture should preserve intelligence differences while reducing unnecessary coupling.

## Cost optimisation techniques

### Prompt and context optimisation

Large contexts increase cost and latency.

Improve by:

- retrieving only relevant information;
- compressing context;
- removing duplicate instructions;
- controlling conversation history.

### Caching

Useful for:

- repeated queries;
- embeddings;
- expensive computations;
- stable reference information.

### Batching

Useful for high-volume asynchronous workloads.

### Smaller specialised models

A smaller model trained or configured for a narrow task can outperform a larger general model economically.

### Human escalation

Sometimes the cheapest reliable option is human review rather than excessive automated retries.

## Measure cost correctly

Token cost alone is not enough.

The important metric is:

```text
Cost per successful outcome
```

A cheap model that fails often may be more expensive than a stronger model that succeeds first time.

Include:

- model cost;
- retries;
- validation failures;
- human review;
- latency impact;
- engineering maintenance.

## Reliability and routing

Routing must include failure handling:

```text
Primary model
      |
      v
Validation
      |
 failure
      |
      v
Fallback model
      |
      v
Human escalation
```

A fallback should not simply be "another model". It should be an intentionally designed recovery path.

## Privacy-aware routing

Not every request should leave the organisation.

Routing decisions may depend on:

- data sensitivity;
- regulation;
- customer requirements;
- residency requirements;
- internal security policy.

Example:

```text
Public content
      -> external model

Sensitive customer data
      -> approved private environment
```

## Enterprise architecture pattern

A mature AI platform usually contains an AI gateway layer:

```text
Applications
      |
      v
AI Gateway
      |
+-----+------+-------+
|            |       |
Cloud      Local   Specialist
Models     Models    Models
```

The gateway manages:

- authentication;
- routing;
- quotas;
- cost tracking;
- observability;
- policy enforcement;
- provider changes.

## Failure modes

Common mistakes:

- always using the largest model;
- optimising cost before measuring quality;
- routing without evaluation data;
- switching models without regression tests;
- ignoring latency requirements;
- hiding important model differences.

## Practical exercise

Design a routing policy for an AI commerce system:

Requirements:

- classify thousands of products daily;
- analyse high-value pricing decisions;
- draft customer responses;
- protect private business data;
- control monthly AI spend.

Document:

- model selection rules;
- fallback strategy;
- cost assumptions;
- evaluation metrics;
- escalation conditions.

## Mastery gate

You understand this topic when you can:

- explain why the strongest model is not always the correct model;
- design a routing architecture;
- calculate cost per successful outcome;
- build evaluation before changing models;
- balance quality, cost, latency and privacy;
- explain when abstraction helps and when it hides important differences.

## Connection to AI operating systems

Model routing becomes increasingly important as AI systems mature. Future AI platforms will likely coordinate many models, tools and execution environments rather than depend on a single universal model.

The durable capability is not owning one model. It is intelligently managing a changing ecosystem of intelligence.
