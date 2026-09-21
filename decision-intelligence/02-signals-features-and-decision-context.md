# 02 — Signals, Features and Decision Context

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Signals, Features and Decision Context** within Decision Intelligence;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Build reliable decision context from authoritative operational evidence.

## Signals

Signals may come from transactions, events, time series, external data, user behaviour, forecasts, inventory, costs, service levels and other domain sources.

## Features

Features transform raw evidence into decision-relevant representations such as trends, rates, recency, volatility, seasonality and ratios.

## Point-in-time correctness

A historical decision evaluation must use only information available at the time of the decision. Future leakage creates false performance.

## Freshness

Track event time, ingestion time and feature computation time. Stale signals can produce rational decisions from outdated reality.

## Provenance

Record source, transformation and version for material decision inputs.

## Missingness

Missing data can itself be informative, but must not silently become zero or normal.

## Context boundaries

Include only information authorized and relevant to the decision.

## Exercise

Design a point-in-time feature set for a replenishment-like decision and identify potential leakage.

## Takeaway

> A decision is only as trustworthy as the temporal correctness and provenance of the context supplied to it.

Next: **03 — Forecasting, Prediction and Uncertainty**.
