# 02 — Vision and Image Understanding

## Purpose

Vision systems turn pixels into evidence such as objects, text, regions and relationships. Reliable applications must understand both the capability and the uncertainty of that perception.

## Learning outcomes

By the end of this module, you should be able to:
- distinguish classification, detection, segmentation, OCR, grounding and visual reasoning
- explain how resolution, crop and preprocessing affect downstream evidence
- preserve coordinates and source provenance through transformations
- choose between specialist vision systems and general vision-language models

## Task types

Classification answers what category is present; detection locates objects; segmentation identifies regions; OCR extracts text; grounding connects language to regions; VQA and vision-language reasoning interpret broader relationships.

## Image quality

Resolution, lighting, blur, compression, orientation, crop, occlusion and scale can dominate results. Validate input quality before blaming or trusting the model.

## Coordinates and transforms

Cropping/resizing changes coordinate frames. If later actions depend on positions, store transformations and map evidence back to the original artifact.

## OCR vs visual reasoning

Use deterministic/specialist OCR when exact text is the primary requirement. Use broader visual reasoning when layout, scene context or relationships matter. Combine them when evidence must be both exact and contextual.

## Screenshots and interfaces

Screenshots mix text, layout and state. Accessibility trees or structured UI data can be more reliable than pixels alone when available.

## Specialist vs general models

General VLMs offer breadth; specialist detectors/OCR/inspection models may offer better calibration, latency or domain precision. Benchmark the actual task.

## Failure modes

- small but critical detail missed
- visually similar objects confused
- OCR text hallucinated or misread
- coordinate transformation invalidates localization
- single-view image hides relevant evidence

## Security and governance

Images can contain prompt injection or sensitive content. Do not let text visible inside an image redefine system instructions. Apply access controls to image stores and minimise retention of sensitive imagery.

## Evaluation

Use task-specific metrics such as precision/recall, OCR error, localization/IoU, grounding accuracy and human correction. For consequential decisions measure downstream false-action rates.

## Practical exercise

Build an inspection pipeline that must identify an object, read a label and verify a structured identifier before recommending an action. Preserve image regions and OCR evidence.

## Architect checklist

- [ ] input quality checks exist
- [ ] coordinate transformations are traceable
- [ ] exact extraction uses deterministic/specialist verification where justified
- [ ] confidence does not substitute for validation
- [ ] evaluation reflects the real image distribution

## Primary reading

- [CLIP — Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [Flamingo — a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

## Mastery gate

Design a production use of **Vision and Image Understanding** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Vision models produce probabilistic evidence; architecture determines when that evidence is trustworthy enough to use.

Next: **03 — Image Generation and Editing Systems**.
