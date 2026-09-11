# 06 — AI Unit Economics

## Purpose

AI products have a distinctive cost structure. Model inference, retrieval, storage, observability, GPUs, human review, and third-party services can scale with usage. A product that looks profitable at low volume can become structurally unprofitable at scale if these costs are not modelled early.

## Core principle

> Revenue must scale faster than the variable cost of delivering AI value.

AI unit economics should be understood before aggressive growth.

## 1. The AI cost stack

Typical variable costs include:

- model inference;
- embeddings and reranking;
- vector/database usage;
- GPU compute;
- object storage and bandwidth;
- tool/API calls;
- observability;
- human review;
- support attributable to AI workflows.

Fixed and semi-fixed costs may include:

- engineering;
- platform infrastructure;
- model hosting;
- security;
- evaluation infrastructure;
- compliance.

## 2. Unit definition

Choose a unit that represents customer value and can be measured consistently.

Examples:

- per active user;
- per company;
- per AI workflow;
- per 1,000 analysed products;
- per completed agent task.

Avoid choosing a unit merely because it is easy to bill.

## 3. Contribution margin

A basic model is:

```text
Revenue per customer
− AI variable costs
− other variable delivery costs
= Contribution margin
```

Track both absolute contribution and contribution margin percentage.

## 4. Model cost is not product cost

A model call is only one part of the economics.

```text
User request
    ↓
Orchestration
    ↓
Retrieval
    ↓
Model inference
    ↓
Tool calls
    ↓
Validation
    ↓
Storage / logging
    ↓
Human review (when required)
```

The complete workflow must be costed.

## 5. Cost optimisation hierarchy

Optimise in this order:

1. eliminate unnecessary AI work;
2. reduce context and redundant calls;
3. use caching where appropriate;
4. route simple work to smaller/cheaper models;
5. batch suitable workloads;
6. optimise retrieval;
7. improve prompts and structured outputs;
8. consider self-hosted models when utilisation justifies it.

Do not optimise infrastructure before proving the workload.

## 6. Model routing

A mature AI platform should not automatically send every request to the most expensive model.

```text
Task
 ↓
Complexity / risk assessment
 ↓
Model router
 ├── Small model
 ├── Specialist model
 └── Frontier model
```

Routing should be governed by quality, latency, risk, and cost—not cost alone.

## 7. AI SaaS pricing

Possible pricing structures include:

### Seat-based

Simple and predictable, but can undercharge high-usage customers.

### Usage-based

Aligns revenue with consumption, but can make bills less predictable.

### Tiered

Combines predictability with usage boundaries.

### Outcome/value-based

Prices around measurable business value. This can be powerful but requires credible outcome measurement.

Hybrid pricing is often appropriate for AI products.

## 8. Gross-margin guardrails

Define economic guardrails before scaling.

Examples:

- maximum AI cost per customer;
- target contribution margin;
- maximum cost per successful workflow;
- maximum model spend as a percentage of revenue.

Guardrails should trigger investigation rather than encourage unsafe quality degradation.

## 9. SEMLIS application

For SEMLIS, the relevant unit may eventually be something such as a customer account, analysed SKU, AI workflow, or managed decision—not simply a chat message.

A simplified model:

```text
Marketplace data
      ↓
Analysis / detection
      ↓
AI reasoning
      ↓
Recommendation
      ↓
Optional execution
```

The platform should measure the cost of the complete decision workflow and compare it with the value created for the merchant.

The economic objective is not to minimise AI spend at any cost. It is to maximise **valuable outcomes per unit of AI spend**.

## 10. Metrics to monitor

At minimum:

- revenue per customer;
- AI cost per customer;
- AI cost per successful workflow;
- contribution margin;
- model mix;
- cache hit rate;
- average tokens/workflow where relevant;
- tool/API cost;
- human-review cost;
- infrastructure utilisation;
- retention and expansion.

## 11. Common mistakes

### Mistake 1 — Pricing before measuring cost

Creates hidden negative margins.

### Mistake 2 — Using the largest model everywhere

Wastes money without necessarily improving outcomes.

### Mistake 3 — Ignoring non-model costs

Retrieval, tools, storage, monitoring, and human review can materially affect economics.

### Mistake 4 — Optimising cost before value

A cheap AI system that fails the customer's job is still a bad product.

### Mistake 5 — Assuming API prices remain constant

Business models should tolerate provider pricing changes and model migrations.

## 12. Enterprise decision framework

Before scaling an AI feature, answer:

1. What is the billable unit?
2. What is the customer's measurable value?
3. What does one successful workflow cost end-to-end?
4. What happens to margin at 10×, 100×, and 1,000× usage?
5. Which work can use cheaper models?
6. What happens if model/API prices change?
7. What infrastructure should be owned versus rented?
8. What quality level must never be sacrificed for cost?

## Takeaway

> Sustainable AI products engineer economics as deliberately as they engineer intelligence.

The strongest AI companies continuously optimise the relationship between **customer value, system quality, and compute cost**.
