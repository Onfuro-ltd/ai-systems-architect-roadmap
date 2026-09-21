# 03 — Inventory, Demand and Replenishment Intelligence

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Inventory, Demand and Replenishment Intelligence** within AI-Native Commerce and Operations;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Connect inventory state and demand uncertainty to replenishment decisions.

## Inventory state

Distinguish on-hand, available, reserved, inbound, damaged, transfer, committed and channel-visible quantities.

## Demand

Forecast at the decision-relevant grain and preserve uncertainty, seasonality, promotions, stockouts and lifecycle effects.

## Stockout censoring

Observed sales during a stockout do not reveal unconstrained demand. Treat availability effects explicitly.

## Replenishment

```text
Inventory position
 + demand distribution
 + lead-time uncertainty
 + service objective
 + order constraints
 + cash/capacity
        ↓
Replenishment recommendation
```

## Decisions

Separate demand forecast from reorder quantity. Constraints and economics determine the action.

## Exceptions

New products, intermittent demand, discontinuations and supplier disruption may need specialist logic or human judgment.

## Outcomes

Measure availability, lost-sales proxies, excess stock, ageing, working capital and forecast/replenishment error.

## Exercise

Design a replenishment recommendation that exposes demand range, lead-time risk and binding constraints rather than one unexplained order quantity.

## Takeaway

> Inventory intelligence is a decision problem under uncertainty, not simply a sales forecast.

Next: **04 — Pricing, Margin and Commercial Decisioning**.
