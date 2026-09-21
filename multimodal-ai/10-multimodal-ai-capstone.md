# 10 — Multimodal AI Capstone

## Objective

Design an enterprise-grade multimodal system that combines at least three modalities and structured data while preserving provenance, uncertainty, policy and measurable outcomes.

## Scenario

Choose a generic workflow such as:

- product-quality investigation;
- support evidence review;
- document-and-voice case analysis;
- industrial inspection;
- accessibility assistant.

Do not choose a scenario where multimodal input adds no measurable value.

## Baseline

Define a simpler baseline first:

- text-only;
- deterministic parser;
- specialist single-modality model;
- human-only process.

The capstone must demonstrate why the multimodal design is worth its complexity.

## Inputs and trust

For every input define:

- source;
- subject/entity;
- timestamp;
- authorization;
- trust class;
- retention;
- whether it can contain untrusted instructions.

## Architecture

Produce a diagram covering:

```text
Artifacts / Structured Data
          |
Validation + Identity
          |
Preprocessing / Specialist Perception
          |
Normalized Evidence + Provenance
          |
Fusion / Routing / Reasoning
          |
Policy + Deterministic Rules
          |
Human Approval where required
          |
Action / Output
          |
Evaluation + Feedback
```

## Evidence model

Create a stable evidence schema that can represent:

- document page/region;
- image bounding region;
- audio timestamp/speaker label;
- video interval/frame;
- structured record;
- source confidence/trust;
- transformation/model identity.

The final system should not depend on a provider-specific response format.

## Alignment and fusion

Explain how the system determines that different modalities refer to the same entity/event.

Choose early, late or hybrid fusion and justify the choice.

## Routing

Define which tasks use:

- deterministic processing;
- specialist model;
- general multimodal model;
- reasoning model;
- human review.

Add escalation and fallback rules.

## Security

Threat-model:

- indirect prompt injection in every modality;
- malicious upload;
- cross-tenant leakage;
- sensitive-media logging;
- synthetic/manipulated evidence;
- tool misuse after misleading perception.

## Evaluation

Build a task suite including:

- ordinary examples;
- low-quality media;
- conflicting modalities;
- missing evidence;
- manipulated/generated content;
- adversarial instructions;
- edge cases by modality.

Measure perception/extraction, grounding, route selection, reasoning, false actions, human correction, latency and cost.

## Infrastructure

Specify:

- raw/derived artifact storage;
- asynchronous processing;
- idempotency;
- caching;
- deletion propagation;
- model/runtime observability;
- cost attribution.

## Human authority

For consequential actions, show exactly what a reviewer sees:

- proposed action;
- supporting evidence;
- source provenance;
- uncertainty;
- policy reason.

## Primary reading

- [CLIP](https://arxiv.org/abs/2103.00020)
- [Flamingo](https://arxiv.org/abs/2204.14198)
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- [Whisper](https://arxiv.org/abs/2212.04356)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

## Architecture decision records

Write at least three ADRs:

1. native multimodal vs composed specialist architecture;
2. evidence/fusion strategy;
3. routing and human-approval boundary.

## Mastery gate

The capstone passes only if another engineer can trace every consequential conclusion back to evidence, identify where uncertainty enters, see which component owns authority, reproduce the evaluation, and replace a model provider without redesigning the business workflow.

## Takeaway

> Multimodal intelligence is production-ready when heterogeneous evidence remains traceable, controlled and measurably more useful than the simpler baseline.

Next: **Domain 19 — Computer Use and Interface Agents**.
