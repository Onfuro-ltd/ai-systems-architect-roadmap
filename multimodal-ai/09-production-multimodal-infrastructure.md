# 09 — Production Multimodal Infrastructure

## Purpose

Multimodal production systems move large heterogeneous artifacts through ingestion, preprocessing, specialist inference, storage, retrieval and downstream reasoning. The platform must manage media lifecycle as well as models.

## Learning outcomes

By the end of this module, you should be able to:
- design storage and processing paths by modality
- separate synchronous and asynchronous media work
- build artifact identity, lineage and derived-evidence storage
- operate modality-specific capacity, observability and cost controls

## Artifact ingestion

Validate type, size, source and malware/security constraints before processing. Give each source artifact a stable identity.

## Processing graph

Image normalization, OCR, transcription, frame extraction and embedding may be independent asynchronous stages. Persist outputs so expensive work is not repeated unnecessarily.

## Storage tiers

Raw media, normalized media, thumbnails/frames, transcripts and derived evidence have different retention and access needs.

## Caching

Cache deterministic transforms and safe model results using artifact/model/config identity. Do not reuse results across authorization boundaries.

## Serving

Different modalities may require different hardware and batching. Route perception workloads independently from language reasoning when that improves utilisation.

## Observability

Trace artifact ID through transformations, model calls, derived evidence and final outcomes. Track processing latency, failure class, storage, model cost and human review.

## Lifecycle

Deletion must propagate through raw artifacts, derived frames, transcripts, embeddings, caches and memory where applicable.

## Failure modes

- same artifact processed repeatedly because identity is missing
- derived copies survive deletion
- video/audio jobs overwhelm interactive text capacity
- cache leaks data across users/tenants
- operators cannot connect final claim to source transformation

## Security and governance

Apply least privilege to media stores and processors, scan/validate untrusted uploads, isolate tenants, redact logs and control egress from processing workers.

## Evaluation

Track storage/egress, preprocessing, specialist inference, reasoning inference and review cost separately. Optimise cost per successful multimodal task.

## Practical exercise

Design infrastructure for images, scanned PDFs, audio and video. Define synchronous/asynchronous boundaries, artifact lineage, retention, deletion and cost attribution.

## Architect checklist

- [ ] every artifact and derivative has identity
- [ ] processing is resumable/idempotent
- [ ] deletion propagates
- [ ] capacity is separated where workload shapes differ
- [ ] end-to-end lineage is observable

## Primary reading

- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)
- [Flamingo — a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)

## Mastery gate

Design a production use of **Production Multimodal Infrastructure** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Multimodal infrastructure is a governed artifact pipeline, not just another model endpoint.

Next: **10 — Multimodal AI Capstone**.
