# 08 — Multimodal Evaluation, Safety and Security

## Purpose

Multimodal systems need evaluation that reflects each modality and the end-to-end action. They also expand the attack surface through media, metadata and generated content.

## Learning outcomes

By the end of this module, you should be able to:
- build modality-specific and end-to-end evaluation suites
- test indirect prompt injection through non-text artifacts
- separate perception errors from reasoning/policy failures
- design provenance, privacy and human-review controls proportional to consequence

## Evaluation layers

Test ingestion quality, perception/extraction, alignment/fusion, reasoning, policy and final outcome separately. This makes failures diagnosable.

## Task suites

Include blur, occlusion, unusual layouts, accents/noise, long video, conflicting modalities, manipulated/generated media and missing evidence.

## Grounding

For consequential claims, require links to page, region, timestamp or structured source. Evaluate whether cited evidence actually supports the claim.

## Adversarial media

Images, documents and audio can contain instructions aimed at the model. Test that content remains data and cannot grant authority.

## Synthetic media

Generated or manipulated media may be useful content but requires provenance and should not be assumed authentic evidence.

## Human review

Use review where uncertainty or consequence exceeds the validated automation boundary. Show reviewers the proposed action and evidence.

## Failure modes

- aggregate score hides a catastrophic modality slice
- model follows instructions embedded in a document/image/audio
- generated media accepted as real evidence
- private media leaks through logs or cross-tenant retrieval
- high-confidence perception error triggers irreversible action

## Security and governance

Apply data minimisation, access control, tenant isolation, retention policy and tool restrictions to all modalities. Consider consent and bystander data for audio/video. Preserve a kill switch for privileged automation.

## Evaluation

Combine deterministic checks, modality-specific metrics, behavioural grading and end-to-end outcomes. Track false-action rates, human corrections, latency and cost by risk slice.

## Practical exercise

Create an adversarial suite for a document-and-image agent containing hidden text, conflicting sources, corrupted files and synthetic evidence. Define pass/fail gates before tool use.

## Architect checklist

- [ ] evaluation covers each modality and end-to-end outcome
- [ ] adversarial media is tested
- [ ] provenance is part of scoring
- [ ] high-risk actions have explicit gates
- [ ] privacy/logging controls cover raw and derived media

## Primary reading

- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)
- [CLIP — Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356)

## Mastery gate

Design a production use of **Multimodal Evaluation, Safety and Security** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Multimodal reliability requires proving both what the system perceived and what it was allowed to do with that perception.

Next: **09 — Production Multimodal Infrastructure**.
