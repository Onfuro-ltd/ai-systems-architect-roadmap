# 01 — Multimodal Foundations and Architecture

## Purpose

Understand how different modalities enter, move through and leave an AI system.

## Modalities

Common inputs and outputs include text, images, diagrams, screenshots, scanned documents, speech, environmental audio, music, video, depth/sensor data and generated media.

A multimodal model may process several modalities natively, while a multimodal system can also orchestrate multiple specialist models.

## Native vs composed systems

```text
Native multimodal model
vs
Vision + OCR + speech + LLM + specialist tools
```

Choose by measured quality, latency, explainability, control and cost.

## Representation

Media may be represented as learned embeddings/tokens, extracted text, structured detections, timestamps, frames, regions, audio features or metadata.

Each representation discards some information.

## Pipeline boundaries

Separate ingestion, validation, preprocessing, inference, fusion, policy, generation and storage. This allows independent testing and replacement.

## Provenance

Retain artifact identity, source, capture/upload time, transformations, model versions and derived outputs where the use case requires traceability.

## Uncertainty

Perception is probabilistic. Low-quality images, accents, noise, occlusion, compression and ambiguous scenes can propagate errors into later reasoning.

## Exercise

Design two architectures for a customer-submitted video: one native multimodal model and one composed specialist pipeline. Compare failure visibility and cost.

## Takeaway

> Multimodal architecture is the controlled conversion of different evidence types into representations that a system can reason over without losing track of uncertainty or provenance.

Next: **02 — Vision and Image Understanding**.
