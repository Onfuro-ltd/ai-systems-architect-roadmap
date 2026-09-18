# 02 — Interface Perception: DOM, Accessibility and Vision

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Interface Perception: DOM, Accessibility and Vision** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Ground agent decisions in the most reliable representation of the current interface.

## Perception sources

A browser or desktop agent may use DOM structure, accessibility tree, semantic element metadata, application APIs, screenshots, OCR, coordinates and prior state.

## Structured state first

When trustworthy, semantic elements provide labels, roles, values and relationships that are more stable than raw coordinates.

But structure can be incomplete, misleading, hidden or absent.

## Vision

Vision helps with canvas applications, remote desktops, images, charts, visual state, poorly exposed controls and layout-dependent tasks.

Pixels are powerful but can be ambiguous.

## Fusion

```text
DOM / accessibility
       +
Visual evidence
       +
Application state
       ↓
Grounded interface model
```

Conflicts should trigger re-observation or alternate evidence rather than silent guessing.

## Coordinates

Coordinates are ephemeral. Window size, scrolling, zoom, responsive layout and popups can invalidate them. Ground coordinate actions to a fresh observation.

## Injection

Visible page text may contain instructions aimed at the agent. Treat content as untrusted data unless it comes from an authorized instruction channel.

## Exercise

For five UI tasks, choose DOM/accessibility, vision, API or hybrid perception and justify the failure trade-offs.

## Takeaway

> Use the richest trustworthy structure available, then add vision where the interface cannot be understood structurally.

Next: **03 — Action Models and Interaction Primitives**.
