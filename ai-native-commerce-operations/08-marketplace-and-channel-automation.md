# 08 — Marketplace and Channel Automation

## Purpose

Operate many external commerce channels through stable internal capabilities.

## Channel adapters

Hide marketplace-specific authentication, schemas, limits, pagination, errors and webhook semantics behind versioned adapters.

## Canonical actions

Examples include publish listing, update inventory, update price, fetch orders, acknowledge fulfilment, retrieve reports and manage approved campaign actions.

## Notifications

Treat webhooks as signals requiring authentication, deduplication and reconciliation—not unquestionable truth.

## Rate limits

Use queues, budgets, backoff and priority. A marketplace outage should not create uncontrolled retry storms.

## Writes

```text
Canonical action
      ↓
Fresh state + policy
      ↓
Channel adapter
      ↓
External API
      ↓
Response
      ↓
Re-fetch / verify
      ↓
Confirmed / UNKNOWN / failed
```

## Portability

Domain workflows should not know channel-specific request structures.

## Interface fallback

Use browser/interface agents only where supported APIs are absent or insufficient, with stricter controls.

## Exercise

Design a channel abstraction that supports inventory updates across three marketplaces with different API semantics.

## Takeaway

> Multi-channel automation scales when channel complexity terminates at the adapter boundary.

Next: **09 — Commerce Control Tower and AI Operations**.
