# 02 — Domain Ontologies, Semantics and Canonical Models

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Domain Ontologies, Semantics and Canonical Models** within Domain-Specific AI Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Give humans, software and models a shared representation of domain concepts.

## Canonical model

Define important entities, identifiers, attributes, relationships, units, states, events and lifecycle transitions.

## Vocabulary

Terms can be ambiguous across teams and systems. Maintain canonical names plus aliases and source-system mappings.

## Ontology depth

Do not build a huge formal ontology by default. Use only the semantic structure needed to improve interoperability, retrieval, validation and reasoning.

## Units and normalization

Money, quantities, dates, time zones, measurements and categorical values require explicit normalization.

## Identity resolution

Different systems may refer to the same real-world entity with different identifiers. Resolve identity deterministically where possible and preserve source IDs.

## Structured outputs

Models should return canonical IDs/enums and typed values where downstream automation depends on them.

## Versioning

Semantic changes are contract changes. Version definitions and mappings.

## Exercise

Create a canonical domain model for a workflow spanning three systems with conflicting terminology and identifiers.

## Takeaway

> Domain intelligence becomes reusable when concepts have stable meanings beyond any individual prompt or application.

Next: **03 — Proprietary Knowledge and Evidence Architecture**.
