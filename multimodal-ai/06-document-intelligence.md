# 06 — Document Intelligence

## Purpose

Turn PDFs, scans, forms, tables and mixed-layout documents into trustworthy structured evidence.

## Document layers

A document can contain embedded text, scanned images, layout, tables, handwriting, signatures, diagrams, annotations and metadata.

Text extraction alone may lose essential meaning.

## Pipeline

```text
Original document
      ↓
Type / integrity detection
      ↓
Native text extraction where available
      ↓
OCR / layout / table processing where needed
      ↓
Structured representation
      ↓
Retrieval / reasoning
      ↓
Citation to source page/region
```

## Prefer native structure

Use embedded text and document structure before OCR when reliable. OCR is a fallback or complementary perception layer, not a universal first step.

## Tables and forms

Preserve row/column relationships, units, headers and page context. Flattening tables into arbitrary text can corrupt meaning.

## Citations

For evidence-sensitive workflows, retain page, bounding region or source element so outputs can be inspected.

## Security

Documents are untrusted input. Treat embedded instructions as data, scan attachments as appropriate, isolate parsers, limit resource consumption and prevent document content from overriding system policy.

## Exercise

Design ingestion for mixed digital/scanned financial documents where exact amounts, tables and page-level citations are required.

## Takeaway

> Document intelligence preserves structure and provenance while converting visual and textual evidence into machine-usable form.

Next: **07 — Multimodal Context, Fusion and Routing**.
