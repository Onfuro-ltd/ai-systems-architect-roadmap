# 07 — Multimodal Context, Fusion and Routing

## Purpose

A production system should not push every artifact into every model. Context assembly, fusion and routing decide which evidence is used, by which specialist, and in what representation.

## Learning outcomes

By the end of this module, you should be able to:
- design modality-aware context selection and budgets
- choose early, late or hybrid fusion deliberately
- route tasks among specialist and general models
- keep normalized evidence and business state independent of model provider

## Context budget

Images, frames, audio and extracted text consume different compute/context resources. Select evidence based on task relevance and risk.

## Evidence normalization

Convert model-specific results into stable application objects such as regions, fields, transcripts, timestamps and confidence/evidence references.

## Fusion

Some tasks benefit from joint reasoning; others are safer when each modality is independently analysed and results are combined with deterministic logic.

## Routing

Use task classification, modality, privacy, latency, cost and measured capability to select eligible models or pipelines.

## Escalation

A small specialist can handle routine perception while ambiguous cases escalate to a stronger multimodal reasoner or human.

## Model independence

Own identity, evidence, state, policy and evaluation in the application layer so perception/reasoning components remain replaceable.

## Failure modes

- all media sent to the most expensive model by default
- routing decision ignores data-residency or capability constraints
- fusion hides which source supported a conclusion
- normalized evidence drops uncertainty/provenance
- fallback changes behaviour without evaluation

## Security and governance

Routing is also a policy boundary. Eligibility must consider data classification, tenant, region and tool/action permissions. Untrusted content must never choose its own privileged route.

## Evaluation

Evaluate route accuracy, task success, cost, latency and fallback behaviour. Compare against a simple single-model baseline to prove routing creates value.

## Practical exercise

Design a router for text, screenshot, scanned PDF and audio requests. Define eligibility, preprocessing, escalation, normalized evidence and fallback.

## Architect checklist

- [ ] evidence objects are provider-neutral
- [ ] routing policy includes privacy/security constraints
- [ ] fusion remains explainable enough for the use case
- [ ] fallbacks are evaluated
- [ ] complexity beats a simpler baseline measurably

## Primary reading

- [CLIP — Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [Flamingo — a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

## Mastery gate

Design a production use of **Multimodal Context, Fusion and Routing** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Multimodal routing should spend complexity only where another modality or specialist measurably improves the outcome.

Next: **08 — Multimodal Evaluation, Safety and Security**.
