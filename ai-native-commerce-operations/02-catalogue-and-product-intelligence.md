# 02 — Catalogue and Product Intelligence

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Catalogue and Product Intelligence** within AI-Native Commerce and Operations;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Use AI to improve product information while preserving factual accuracy and channel constraints.

## Product truth

Maintain authoritative product attributes, identifiers, dimensions, materials, compatibility, compliance evidence and media separately from generated listing copy.

## Enrichment

AI can classify products, normalize attributes, detect missing information, propose titles/descriptions, map taxonomies and analyze images.

## Grounding

Generated claims must be supported by product evidence. Do not invent specifications or compatibility to improve copy.

## Channel adaptation

```text
Canonical product truth
        ↓
Channel rules + taxonomy
        ↓
AI transformation
        ↓
Deterministic validation
        ↓
Human review where needed
        ↓
Listing
```

## Quality

Evaluate factual correctness, attribute completeness, taxonomy accuracy, policy compliance, discoverability and conversion outcomes separately.

## Media

Apply provenance and rights controls to generated/edited media and retain originals.

## Exercise

Design a catalogue enrichment pipeline that produces channel-specific listings from one canonical product record.

## Takeaway

> Generative catalogue systems should transform product truth, never manufacture it.

Next: **03 — Inventory, Demand and Replenishment Intelligence**.
