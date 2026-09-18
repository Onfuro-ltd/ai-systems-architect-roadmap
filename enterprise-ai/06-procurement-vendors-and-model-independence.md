# 06 — Procurement, Vendors and Model Independence

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Procurement, Vendors and Model Independence** within Enterprise AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Evaluate AI suppliers as dependencies in an enterprise system rather than selecting them from demos alone.

## Due diligence

Assess capability evidence, security, privacy, data usage, residency, retention, subprocessors, availability, support, pricing, rate limits, model/version policy, deprecation, portability, contractual terms and exit options.

## Model independence

Use canonical internal interfaces, provider adapters, evaluation suites and portable business workflows so a provider can be changed without redesigning the enterprise.

Independence does not require using every provider simultaneously.

## Lock-in

Differentiate useful specialization from accidental coupling. Proprietary capabilities may be worth adopting when the value exceeds switching risk.

## Exit plan

Know how to export data/configuration, replace endpoints, migrate prompts/tools, reproduce evaluations and retire credentials.

## Procurement evidence

A provider's benchmark or security statement is input to diligence, not a substitute for workload-specific testing and contractual review.

## Concentration risk

Identify critical workflows dependent on one provider, region or platform and choose mitigations proportionate to consequence.

## Exercise

Create an enterprise vendor assessment for a hosted frontier model, a specialist SaaS AI product and a private open-model platform.

## Takeaway

> Enterprise model independence is the ability to change suppliers without losing the organization's encoded workflows, evidence and control plane.

Next: **07 — Human Oversight, Change Management and Adoption**.
