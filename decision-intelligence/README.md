# Domain 25 — Decision Intelligence

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across decision framing, evidence, uncertainty, forecasting, optimisation, causal reasoning, human judgement and decision feedback loops.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Decision intelligence turns data, predictions, rules and objectives into evidence-backed recommendations and controlled decisions.

> A prediction estimates what may happen. A decision chooses what to do. The two are related, but they are not the same system.

## Domain structure

01 Decision Intelligence Foundations  
02 Signals, Features and Decision Context  
03 Forecasting, Prediction and Uncertainty  
04 Causal Thinking and Intervention Effects  
05 Objectives, Constraints and Business Rules  
06 Optimization, Recommendations and Decision Policies  
07 Explanations, Confidence and Human Decisions  
08 Outcome Feedback and Decision Evaluation  
09 Production Decision Intelligence Architecture  
10 Decision Intelligence Capstone

## Core architecture

```text
Authoritative data + events
          ↓
Signals / features
          ↓
Forecasts / predictions
          ↓
Uncertainty + causal evidence
          ↓
Objectives + constraints + business rules
          ↓
Decision policy / optimization
          ↓
Recommendation
          ↓
Approval / bounded execution
          ↓
Observed outcome
          ↓
Evaluation + learning
```

## Principles

1. Separate prediction from decision.
2. Preserve uncertainty.
3. Distinguish correlation from intervention effects.
4. Keep hard business constraints deterministic.
5. Make objectives and trade-offs explicit.
6. Evaluate recommendations by outcomes, not plausibility.
7. Do not optimize proxy metrics blindly.
8. Preserve human authority for consequential decisions.
9. Record decision context and alternatives.
10. Learn from outcomes without confusing observation with causation.

## Takeaway

> Decision intelligence is the architecture that connects evidence to action while making objectives, constraints, uncertainty and outcomes explicit.

Next: **01 — Decision Intelligence Foundations**.

## Canonical curriculum navigation

- [Decision Intelligence Foundations](./01-decision-intelligence-foundations.md)
- [Signals, Features and Decision Context](./02-signals-features-and-decision-context.md)
- [Forecasting, Prediction and Uncertainty](./03-forecasting-prediction-and-uncertainty.md)
- [Causal Thinking and Intervention Effects](./04-causal-thinking-and-intervention-effects.md)
- [Objectives, Constraints and Business Rules](./05-objectives-constraints-and-business-rules.md)
- [Optimization, Recommendations and Decision Policies](./06-optimization-recommendations-and-decision-policies.md)
- [Explanations, Confidence and Human Decisions](./07-explanations-confidence-and-human-decisions.md)
- [Outcome Feedback and Decision Evaluation](./08-outcome-feedback-and-decision-evaluation.md)
- [Production Decision Intelligence Architecture](./09-production-decision-intelligence-architecture.md)
- [Decision Intelligence Capstone](./10-decision-intelligence-capstone.md)
