# 10 — Multimodal AI Capstone

## Purpose

Design an enterprise multimodal evidence and generation platform.

## Scenario

A multitenant AI platform receives text, photographs, screenshots, PDFs, scans, audio and video. It must answer questions, extract structured facts, generate approved media and support downstream workflows without treating probabilistic perception as authoritative truth.

## Target architecture

```text
Upload / capture / generated request
            ↓
Authorization + validation
            ↓
Immutable original + provenance
            ↓
Modality router
 ┌──────────┼──────────┬──────────┐
 ↓          ↓          ↓          ↓
Vision   Document    Audio      Video
 ↓          ↓          ↓          ↓
Specialist extraction / representation
            ↓
Evidence contracts + fusion
            ↓
Reasoning / generation
            ↓
Deterministic validation + policy
            ↓
Approval / action / delivered asset
            ↓
Outcome evaluation + audit
```

## Required deliverables

Produce modality inventory; ingestion contracts; storage/lifecycle design; provenance schema; vision/OCR/document pipeline; speech/audio architecture; video sampling/indexing; image/video generation workflow; modality router; evidence-fusion contract; conflict handling; context-budget strategy; privacy/consent model; media prompt-injection threat model; generated-media controls; evaluation suites; asynchronous processing architecture; caching; cost attribution; observability; resilience; human approval boundaries; and at least three ADRs.

## Failure matrix

Cover corrupt media, wrong MIME, OCR error, visual hallucination, missed video event, transcription error, spoofed/manipulated media, embedded prompt injection, privacy leakage, tenant crossover, generation-policy failure, exact-text/geometry error, provider outage, processing timeout, runaway media cost and lost provenance.

## Acceptance criteria

The original artifact remains traceable; modality-specific quality is measured; OCR is not confused with understanding; consequential actions require verification; evidence retains page/region/timestamp provenance; media content cannot override system policy; tenant/privacy boundaries are deterministic; long processing is resumable; generated assets have approval controls; storage/retention is explicit; costs are attributable; and models/providers remain replaceable behind canonical interfaces.

## Final principle

> Multimodal AI should expand what a system can perceive and create without weakening the deterministic controls that make the surrounding system trustworthy.

**Domain 18 — Multimodal AI complete.**

Next domain: **19 — Computer Use and Interface Agents**.
