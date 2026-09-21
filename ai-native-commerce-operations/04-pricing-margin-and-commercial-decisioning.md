# 04 — Pricing, Margin and Commercial Decisioning

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Pricing, Margin and Commercial Decisioning** within AI-Native Commerce and Operations;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Make pricing decisions using complete economics, constraints and evidence.

## Unit economics

Include selling price, taxes, marketplace fees, fulfilment, postage, packaging, product cost, advertising allocation, returns/refunds and other material variable costs.

## Margin truth

Keep financial calculations deterministic and versioned.

## Price decision

```text
Current economics
 + market/context signals
 + inventory position
 + demand evidence
 + strategic objective
 + hard constraints
        ↓
Feasible price actions
        ↓
Recommendation
```

## Constraints

Respect legal/policy rules, minimum margins where applicable, channel restrictions, contractual constraints and approval thresholds.

## Elasticity

Historical price/sales association is not automatically causal price elasticity. Promotions, seasonality and competition can confound it.

## Experimentation

Where appropriate, controlled tests can estimate response while respecting customer, legal and commercial constraints.

## Outcomes

Measure contribution, volume, conversion, inventory effect and longer-term consequences—not revenue alone.

## Exercise

Design a price recommendation service that cannot propose an economically invalid price even if the model recommends it.

## Takeaway

> AI may interpret commercial context; deterministic economics defines whether a proposed price is feasible.

Next: **05 — Advertising and Growth Optimization**.
