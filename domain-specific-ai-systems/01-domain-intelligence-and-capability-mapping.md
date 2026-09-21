# 01 — Domain Intelligence and Capability Mapping

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Domain Intelligence and Capability Mapping** within Domain-Specific AI Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Identify what knowledge and behaviour make a domain system genuinely competent.

## Intelligence inventory

Map terminology, entities, relationships, authoritative data, policies, calculations, procedures, exceptions, tools, decision rights, historical outcomes and evaluation criteria.

## Capability map

Define concrete capabilities such as classify, extract, reconcile, recommend, forecast, investigate, generate, validate or execute.

Avoid vague requirements such as "understand our business."

## Knowledge types

Separate facts that change, stable definitions, deterministic rules, reusable procedures, user/session context and learned behavioural patterns.

## Architecture decision

```text
Changing fact → authoritative data / retrieval / tool
Exact rule → code / policy
Reusable procedure → skill / workflow
User/session context → state / memory
Stable behavioural gap → consider tuning
Capability gap → specialist/stronger model
```

## Tacit knowledge

Interview domain experts around exceptions and difficult cases. Written SOPs often omit the reasoning that experienced operators use.

## Ownership

Every domain capability needs an accountable domain owner who defines correctness.

## Exercise

Build an intelligence inventory for a domain you know and map every item to its durable architectural home.

## Takeaway

> Before choosing a model, decide what the organization actually needs to know and do.

Next: **02 — Domain Ontologies, Semantics and Canonical Models**.
