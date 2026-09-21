# 06 — Specialist Models, Tuning and Routing

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Specialist Models, Tuning and Routing** within Domain-Specific AI Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Use model specialization only where it creates measured domain value.

## Root-cause first

Before tuning, ask whether the gap is missing knowledge, weak retrieval, missing rule, poor workflow, insufficient tool access, context design or genuine learned behaviour.

## Specialists

Smaller specialist models can serve classification, extraction, ranking, vision or domain language tasks when evaluation supports them.

## Fine-tuning

Tune stable behavioural patterns, formats or domain transformations that are difficult to achieve reliably through simpler architecture.

Do not fine-tune volatile facts.

## Routing

```text
Domain task
 ↓
Policy eligibility
 ↓
Capability requirement
 ↓
General / specialist / local / tuned model
 ↓
Domain validation
```

## Distillation

Where permitted, a stronger system can help create/label candidate training data for a specialist, but expert verification and independent evaluation remain necessary.

## Economics

Compare specialist quality, latency, serving cost, maintenance and data lifecycle against general-model alternatives.

## Exercise

Choose architecture for five domain gaps and justify which require retrieval, rules, skills, tuning or specialist routing.

## Takeaway

> Specialize the model only after proving that the missing capability belongs in model behaviour.

Next: **07 — Domain Evaluation and Gold Standards**.
