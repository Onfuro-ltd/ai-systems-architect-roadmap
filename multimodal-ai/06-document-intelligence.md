# 06 — Document Intelligence

## Purpose

Documents combine text, layout, tables, images, handwriting and metadata. Reliable extraction often needs both deterministic parsing and visual/language understanding.

## Learning outcomes

By the end of this module, you should be able to:
- distinguish native digital parsing, OCR and visual document reasoning
- preserve page/region provenance for extracted fields
- design schema validation and human review for consequential extraction
- handle malicious or conflicting document content safely

## Document types

Native PDFs, scans, forms, slides and photos of documents require different ingestion. Detect format and quality before choosing the extraction path.

## Parsing vs OCR

Use native text/object extraction when available; OCR when pixels contain the text; visual reasoning when layout/relationships matter.

## Layout

Tables, headers, footnotes, merged cells and multi-column layouts carry meaning. Flattening to plain text can destroy structure.

## Structured extraction

Return typed fields with page/region references, validation status and uncertainty. Downstream systems should not parse free-form model prose if a schema can be used.

## Cross-page reasoning

Some facts require linking definitions, tables and appendices. Retrieval/chunking strategies should preserve document hierarchy.

## Authority

A document can be relevant but not authoritative. Store source identity, version and effective date where decisions depend on it.

## Failure modes

- wrong OCR digit causes a material field error
- table rows/columns become misaligned
- stale document version overrides current policy
- hidden or malicious text influences the model
- model fills a missing field instead of returning unknown

## Security and governance

Documents are a major indirect-prompt-injection surface. Keep document content in the data trust class, enforce access before retrieval, and validate any proposed action outside the model.

## Evaluation

Measure field precision/recall, exact-value error, page/region grounding, missing-field behaviour and human correction. Slice results by document type and scan quality.

## Practical exercise

Build a pipeline that extracts five fields from mixed native/scanned documents. Require provenance, schema validation, explicit unknowns and one deterministic cross-check.

## Architect checklist

- [ ] format detection chooses the extraction path
- [ ] every consequential field can point to evidence
- [ ] missing values remain missing rather than invented
- [ ] document authority/version is explicit
- [ ] extraction quality is measured by document slice

## Primary reading

- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)
- [Flamingo — a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)

## Mastery gate

Design a production use of **Document Intelligence** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Document intelligence is trustworthy when structured outputs remain traceable to the source artifact.

Next: **07 — Multimodal Context, Fusion and Routing**.
