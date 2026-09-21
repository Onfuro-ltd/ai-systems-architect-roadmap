# 03 — Uncertainty, Confidence and Evidence

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Uncertainty, Confidence and Evidence** within AI Product Design;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Help users distinguish supported results from guesses without presenting misleading precision.

## Sources of uncertainty

Uncertainty can come from ambiguous intent, missing context, stale data, weak retrieval, perception errors, model limitations, conflicting evidence and tool failures.

## Confidence

A model saying "90% confident" is not automatically a calibrated probability. Use calibrated task-specific confidence only when validated.

## Product signals

Useful signals can include source coverage, missing required fields, conflicting evidence, validation status, freshness and whether a result was independently verified.

## Ask vs assume

When missing information materially changes the outcome, ask or escalate rather than silently filling the gap.

## Consequence

The threshold for proceeding should depend on consequence. A creative suggestion and a financial action should not share the same uncertainty policy.

## Unknown

Support explicit UNKNOWN / insufficient-evidence states.

## Exercise

Design uncertainty UX for an extraction product where some fields come from authoritative data, some from OCR and some from model inference.

## Takeaway

> Good uncertainty design tells the user what is known, what is inferred, and what still needs verification.

Next: **04 — Trust, Explainability and Provenance**.
