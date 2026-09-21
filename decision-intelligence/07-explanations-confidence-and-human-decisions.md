# 07 — Explanations, Confidence and Human Decisions

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Explanations, Confidence and Human Decisions** within Decision Intelligence;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Give decision-makers enough evidence to evaluate recommendations without manufacturing certainty.

## Decision explanation

Show relevant signals, forecast, uncertainty, binding constraints, objective trade-offs, alternatives and expected consequences.

## Reason codes

Structured reason codes are often more auditable than free-form explanations.

## Confidence

Separate predictive uncertainty, data-quality confidence, causal-evidence strength and decision robustness. They answer different questions.

## Human judgment

Human reviewers can contribute context unavailable to the system. Capture overrides and reasons without assuming the human is always correct.

## Approval design

Consequential recommendations should present the material decision, not require reviewers to reconstruct it from raw model output.

## Automation bias

Design interfaces to support appropriate skepticism and alternatives, especially where recommendations appear authoritative.

## Exercise

Create a decision card that presents one recommendation, two alternatives, uncertainty and binding constraints.

## Takeaway

> Decision UX should help humans understand the choice and its evidence, not persuade them to accept the machine.

Next: **08 — Outcome Feedback and Decision Evaluation**.
