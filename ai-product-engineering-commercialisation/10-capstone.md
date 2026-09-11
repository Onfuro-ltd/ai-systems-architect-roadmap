# 10 — AI Product Engineering & Commercialisation Capstone

## Purpose

This capstone combines the product, engineering, economic, sales, and company-building principles from this section into one operating framework for taking an AI opportunity from problem discovery to a scalable business.

## Core principle

> Build the smallest system that proves valuable outcomes, then scale the product, economics, distribution, and controls together.

## 1. End-to-end AI company loop

```text
Customer problem
      ↓
Problem evidence
      ↓
AI opportunity
      ↓
Focused MVP
      ↓
User validation
      ↓
Production architecture
      ↓
Measured outcomes
      ↓
Pricing / unit economics
      ↓
Proof of value
      ↓
Repeatable sales
      ↓
Expansion
      ↓
Data + feedback moat
      ↺
```

Each stage should produce evidence for the next stage.

## 2. Reference AI product architecture

```text
                    Customers
                        ↓
                Product Experience
                        ↓
               Business Workflow
                        ↓
                AI Orchestration
             ↙          ↓          ↘
        Knowledge     Models       Tools
             ↘          ↓          ↙
                 Policy / Safety
                        ↓
                Business Systems
                        ↓
             Monitoring + Evaluation
                        ↓
                 Data + Feedback
```

The model is one component of the product, not the whole product.

## 3. Stage gates

### Gate 1 — Problem

Evidence that:

- the problem exists;
- the target customer experiences it;
- the cost or pain is meaningful;
- existing alternatives are inadequate.

### Gate 2 — MVP

Evidence that:

- the workflow works;
- users can obtain value;
- output quality is acceptable;
- the system can be operated safely.

### Gate 3 — Product-market evidence

Evidence that:

- users repeatedly use the product;
- customers achieve measurable outcomes;
- customers are willing to pay;
- retention or expansion signals exist.

### Gate 4 — Scale

Evidence that:

- unit economics are viable;
- deployment is repeatable;
- security and governance are mature;
- sales can become repeatable;
- infrastructure can handle growth.

## 4. AI product scorecard

Evaluate an opportunity across:

```text
Customer pain
Value created
AI advantage
Technical feasibility
Data advantage
Distribution
Defensibility
Unit economics
Security / risk
Scalability
```

A technically exciting opportunity should not automatically score highly.

## 5. Economic model

At customer level:

```text
Customer revenue
− AI inference
− retrieval / tool costs
− infrastructure allocation
− support / human review
− other variable delivery costs
= Contribution
```

At company level:

```text
Contribution
− product / engineering
− sales & marketing
− operations
− compliance / security
= Operating result
```

Stress-test the model at increasing usage and changing provider prices.

## 6. Enterprise deployment model

```text
Discovery
   ↓
Baseline
   ↓
Proof of Value
   ↓
Security / procurement
   ↓
Production
   ↓
Measured outcome
   ↓
Expansion
```

Production deployment should not depend on a heroic one-off implementation team.

## 7. Model independence

Design the product so that model providers can change without rebuilding the business.

Use abstraction around:

- model routing;
- structured outputs;
- evaluation;
- prompts / policies;
- provider integrations;
- observability.

The product's durable layer should contain the domain logic, workflows, data, evaluation, and customer relationships.

## 8. Failure containment

Every high-impact AI workflow should have an explicit failure strategy:

- validation;
- confidence or uncertainty handling;
- permission checks;
- rate / action limits;
- human escalation;
- rollback where possible;
- audit logging.

```text
AI suggestion
    ↓
Validation
    ↓
Policy
    ↓
Permission
    ↓
Execution
    ↓
Audit
```

## 9. SEMLIS capstone architecture

A model-independent SEMLIS intelligence layer can be conceptualised as:

```text
Amazon / eBay / Shopify / Other Sources
                    ↓
             Commerce Data Layer
                    ↓
          Normalisation + Quality
                    ↓
       Intelligence / Decision Engine
          ↙         ↓          ↘
   Forecasting   Detection   Recommendations
          ↘         ↓          ↙
             AI Orchestration
                    ↓
          Business Rules / Policy
                    ↓
          Permission / Approval
                    ↓
        Controlled Marketplace Action
                    ↓
          Outcome + Audit Data
                    ↓
          Evaluation / Feedback Loop
                    ↺
```

The strategic asset is the system around the models: commerce context, integrations, workflows, business rules, evaluations, feedback, and outcomes.

## 10. What not to build

Avoid:

- generic chatbot features with no differentiated workflow;
- unlimited autonomous access;
- expensive model calls where simple methods suffice;
- custom infrastructure without proven utilisation;
- pilots without success criteria;
- pricing disconnected from value and cost;
- customer-specific forks that destroy scalability.

## 11. AI company operating cadence

A mature company continuously reviews:

### Product

- activation;
- retention;
- outcomes;
- feature adoption.

### AI

- quality;
- evaluation scores;
- failure rates;
- model performance.

### Economics

- revenue;
- AI cost;
- contribution margin;
- acquisition cost;
- expansion.

### Operations

- incidents;
- latency;
- availability;
- security events.

### Commercial

- pipeline;
- conversion;
- sales cycle;
- pilot-to-production conversion.

## 12. Final architect checklist

Before declaring an AI product production-ready, ask:

1. Is the customer problem proven?
2. Is AI materially better than a non-AI solution for this workflow?
3. Is the system measurable?
4. Are model outputs evaluated continuously?
5. Are data and permissions controlled?
6. Can high-impact failures be contained?
7. Can models be changed without rewriting the product?
8. Are unit economics sustainable at scale?
9. Is pricing aligned with customer value?
10. Can the product pass enterprise security and procurement requirements?
11. Is deployment repeatable?
12. Does the business create a compounding advantage?

## Final takeaway

> The AI product is the intersection of customer value, intelligent software, controlled automation, sustainable economics, and continuous learning.

A strong AI architect therefore thinks simultaneously like a systems engineer, product strategist, security architect, and business operator.

That is the standard this roadmap is designed to develop.
