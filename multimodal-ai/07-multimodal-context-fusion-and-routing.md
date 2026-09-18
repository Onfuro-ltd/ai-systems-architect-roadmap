# 07 — Multimodal Context, Fusion and Routing

## Purpose

Decide which evidence each model receives and how outputs from different perception systems are combined.

## Early vs late fusion

Early fusion sends multiple modalities into a joint model. Late fusion processes modalities separately and combines structured results later.

Hybrid designs are common.

## Routing

```text
Input classification
   ├─ image specialist
   ├─ OCR/document pipeline
   ├─ speech pipeline
   ├─ video pipeline
   └─ native multimodal model
          ↓
Evidence fusion
          ↓
Reasoning
```

Route by task quality, modality, privacy, latency and cost.

## Evidence contracts

Normalize specialist outputs into explicit structures containing source identity, timestamp/page/region, confidence where meaningful, model/version and extracted facts.

## Conflicts

When modalities disagree, do not silently average them. Define precedence, re-check, alternate model, deterministic verification or human escalation.

## Context budgets

Images, frames, audio and documents can consume substantial context/compute. Retrieve relevant evidence rather than forwarding every artifact.

## Model independence

Keep fusion and business reasoning above provider-specific multimodal APIs.

## Exercise

Design a claim-review workflow combining a form, photographs, a phone recording and a short video while preserving evidence provenance.

## Takeaway

> Multimodal fusion should combine evidence, not erase where that evidence came from.

Next: **08 — Multimodal Evaluation, Safety and Security**.
