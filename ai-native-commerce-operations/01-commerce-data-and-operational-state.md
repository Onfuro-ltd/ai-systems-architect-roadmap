# 01 — Commerce Data and Operational State

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Commerce Data and Operational State** within AI-Native Commerce and Operations;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Create a trustworthy operational state across fragmented commerce systems.

## Canonical entities

Common entities include product, SKU, listing, channel, marketplace, inventory location, order, order line, shipment, return, customer interaction, campaign, fee, tax record and financial transaction.

## Source identity

Preserve channel-native IDs while mapping them to canonical internal identities.

## State

Commerce APIs often expose delayed, partial or eventually consistent views. Record source time, ingestion time and reconciliation status.

## Events

Use webhooks/events where available and scheduled reconciliation to repair missed or out-of-order changes.

## Idempotency

Orders, stock changes and financial events require stable external identities and deduplication.

## Provenance

A derived metric should be traceable to source records and transformation version.

## Data quality

Track missing mappings, duplicates, stale feeds, conflicting states and impossible values as operational issues.

## Exercise

Design a canonical data model that can ingest orders and inventory from three different commerce channels without embedding channel assumptions into downstream AI.

## Takeaway

> AI cannot repair an operational truth layer that the architecture never made trustworthy.

Next: **02 — Catalogue and Product Intelligence**.
