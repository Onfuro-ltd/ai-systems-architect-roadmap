# 04 — Causal Thinking and Intervention Effects

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Causal Thinking and Intervention Effects** within Decision Intelligence;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Avoid assuming that a predictive relationship tells us what will happen if we intervene.

## Correlation vs intervention

A variable can predict an outcome without changing that outcome when manipulated.

```text
Observed association ≠ causal effect of an action
```

## Confounding

A third factor can influence both treatment/action and outcome, creating misleading observational relationships.

## Counterfactual question

Decision-making often asks: what would happen under action A compared with action B for the same situation?

Only one outcome is normally observed.

## Evidence

Randomized experiments can estimate intervention effects under appropriate design. Quasi-experimental and causal-inference methods can help where experiments are impractical, but assumptions must be explicit.

## Causal diagrams

Use causal graphs to reason about variables, confounders, mediators and selection before choosing data/estimators.

## AI role

Language models can help formulate hypotheses or explain analyses, but should not invent causal identification from correlations.

## Exercise

Take a correlation between promotional spend and sales and list several causal structures that could produce it.

## Takeaway

> Prediction asks what accompanies an outcome; causal decision-making asks what changing an action would do to that outcome.

Next: **05 — Objectives, Constraints and Business Rules**.
