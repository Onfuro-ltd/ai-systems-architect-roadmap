# 01 — Multimodal Foundations and Architecture

## Purpose

Multimodal systems combine different forms of evidence. The architecture problem is not merely accepting images or audio; it is aligning sources, preserving provenance, managing uncertainty and deciding where different modalities should influence reasoning and action.

## Learning outcomes

By the end of this module, you should be able to:
- define modality, representation, alignment and fusion at a systems level
- distinguish native multimodal models from composed specialist pipelines
- separate perception, reasoning, policy and action
- design provenance and trust boundaries across mixed media and structured data

## Modalities and representations

Text, images, audio, video, documents, structured data and sensors encode different evidence. They may enter a model as learned tokens/embeddings or be converted into text, detections, timestamps, coordinates or structured fields. Every conversion can discard information.

## Native vs composed systems

A native multimodal model can jointly process several modalities. A composed system can combine vision, OCR, speech, parsers and a reasoning model. The correct choice depends on measured task quality, latency, cost, explainability and control.

## Alignment

Inputs must be associated with the correct entity, time and event. A photograph, transcript and database record can each be accurate while referring to different things. Entity/time alignment is a first-class data problem.

## Fusion

Early fusion combines representations before deeper reasoning; late fusion combines independently processed evidence; hybrid designs mix both. Choose the fusion point according to the task and validation needs.

## Perception, reasoning and action

Perception can identify a damaged object without proving why it was damaged or what business action should follow. Keep evidence extraction separate from policy and irreversible action.

## Structured data matters

Multimodal intelligence often combines probabilistic perception with authoritative structured data. Deterministic calculations and systems of record should remain authoritative where applicable.

## Provenance

Retain source identity, timestamps, transformations, model/runtime versions and links from derived claims to source regions/segments where consequence requires it.

## Failure modes

- misaligning evidence from different entities or times
- treating recognition as causal understanding
- losing coordinates/timestamps during preprocessing
- allowing generated or unverified media to become authoritative evidence
- sending every modality to one large model without measuring whether it helps

## Security and governance

Every modality can carry untrusted instructions or manipulated evidence. Treat content as data, preserve trust origin, minimise exposed tools and keep authorization/policy outside the multimodal model.

## Evaluation

Measure the end task, not whether the model produced an impressive description. Compare native and composed baselines on correctness, evidence quality, latency, cost and human correction.

## Practical exercise

Design two architectures for investigating a product issue using listing text, images, a supplier PDF and structured return-rate data. Compare a native multimodal model with a composed pipeline and define where verification occurs.

## Architect checklist

- [ ] entity/time alignment is explicit
- [ ] provenance survives transformations
- [ ] perception does not directly grant action authority
- [ ] deterministic sources remain authoritative where appropriate
- [ ] a simpler text/structured baseline is measured

## Primary reading

- [CLIP — Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [Flamingo — a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

## Mastery gate

Design a production use of **Multimodal Foundations and Architecture** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Multimodal value comes from controlled evidence fusion, not from the number of media types a model accepts.

Next: **02 — Vision and Image Understanding**.
