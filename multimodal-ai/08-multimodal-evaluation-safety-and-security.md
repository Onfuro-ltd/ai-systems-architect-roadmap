# 08 — Multimodal Evaluation, Safety and Security

## Purpose

Evaluate multimodal systems against modality-specific failures and cross-modal attack surfaces.

## Evaluation

Build representative suites for image quality, OCR, spatial reasoning, audio recognition, accents/noise, temporal video reasoning, document layout and cross-modal tasks.

Measure end-to-end task success as well as component quality.

## Perturbations

Test blur, crop, rotation, compression, low light, noise, missing frames, poor scans, long documents, overlapping speech and corrupted metadata where relevant.

## Prompt injection through media

Images, documents, transcripts and web screenshots may contain instructions intended to manipulate an agent.

Treat retrieved/media content as untrusted evidence, not system authority.

## Adversarial media

Consider deceptive edits, spoofed screenshots, manipulated documents, synthetic voices and generated imagery. Verification requirements should match consequence.

## Privacy and consent

Media can expose faces, voices, locations, documents and bystanders. Minimize collection and retention, enforce access, and apply consent/legal requirements appropriate to the use case.

## Generated media

Apply policy, provenance and human review appropriate to risk. Exact requirements vary by deployment and jurisdiction.

## Exercise

Threat-model a multimodal agent that can receive images and documents and then call operational tools.

## Takeaway

> A multimodal attack can enter through what the system sees or hears, so perception must never bypass policy and authorization boundaries.

Next: **09 — Production Multimodal Infrastructure**.
