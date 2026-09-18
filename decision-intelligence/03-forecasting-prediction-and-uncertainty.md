# 03 — Forecasting, Prediction and Uncertainty

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Forecasting, Prediction and Uncertainty** within Decision Intelligence;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Represent possible futures without turning estimates into facts.

## Forecast types

Systems may estimate demand, probability, duration, value, risk, anomaly, ranking or future state.

## Distribution

Where possible, preserve ranges, quantiles or scenario distributions rather than only point estimates.

## Calibration

A probability should be treated as meaningful confidence only when calibration has been evaluated for the relevant population and period.

## Error asymmetry

Overprediction and underprediction may have different business costs. Evaluate errors against the decision they support.

## Segmentation

Aggregate accuracy can hide poor performance for important subgroups, products, locations or regimes.

## Drift

Monitor changing data, relationships, seasonality and operational policy that can invalidate historical predictive performance.

## Model ensembles

Multiple models can improve robustness in some settings, but disagreement is also a useful uncertainty signal.

## Exercise

Convert a point demand forecast into a decision-ready forecast containing uncertainty and asymmetric error costs.

## Takeaway

> A forecast should describe uncertainty about the future, not conceal it behind a single precise number.

Next: **04 — Causal Thinking and Intervention Effects**.
