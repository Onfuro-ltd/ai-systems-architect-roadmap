# 08 — Multimodal Foundations

Multimodal AI systems work with more than one kind of data: text, images, audio, video, documents, sensor streams or other structured signals.

The important architectural idea is not simply that a model can "see" or "hear." It is that different modalities must be transformed into representations that can interact inside a shared reasoning or generation system.

## Learning outcomes

By the end of this module, you should be able to:

- explain what a modality is;
- distinguish multimodal understanding from multimodal generation;
- describe common ways modalities are encoded and connected;
- understand contrastive representation learning at a conceptual level;
- reason about image patching, audio frames and temporal video input;
- identify cost, latency and reliability differences across modalities;
- understand why modality-specific preprocessing and validation still matter.

## 1. What is a modality?

A modality is a type or channel of information.

Examples:

```text
text
images
audio
video
PDF / document layout
sensor data
structured tables
```

A multimodal system combines two or more of these in one workflow or model.

## 2. Multimodal does not mean one architecture

There are several broad patterns.

### Separate encoders with a shared representation

```text
image → image encoder ─┐
                       ├→ shared representation space
text  → text encoder  ─┘
```

CLIP is a historically important example. It trained image and text encoders so matching image/text pairs would be represented close together.

Primary source: https://arxiv.org/abs/2103.00020

### Modality encoder connected to a language model

```text
image
  ↓
vision encoder
  ↓
projection / adapter
  ↓
language-model representation
  ↓
text generation
```

This pattern lets a language model condition on visual features without requiring every component to be trained from scratch as one monolith.

### Cross-attention between modalities

One stream can attend to another through dedicated cross-attention layers.

```text
text representations ─────┐
                          ├→ cross-attention → fused state
image representations ────┘
```

### Unified token/representation systems

Some systems encode multiple modalities into token-like representations that can be processed by a shared model stack.

The engineering details differ substantially across models.

## 3. Images as model input

A model does not usually ingest an image as a human visual experience. The image is transformed into numerical representations.

Vision Transformer-style systems commonly divide images into patches:

```text
image
  ↓
patches
  ↓
patch embeddings
  ↓
transformer processing
```

A high-resolution image may therefore produce substantially more visual tokens or internal representations than a low-resolution one, increasing compute.

## 4. Documents are more than images or text

A document may contain:

- text;
- tables;
- images;
- layout;
- headings;
- coordinates;
- handwriting;
- page relationships.

Treating a PDF only as extracted plain text may lose layout meaning. Treating every page only as an image may lose searchable textual structure and increase inference cost.

A strong document pipeline may combine:

```text
native text extraction
+ layout structure
+ image/vision analysis where needed
+ tables / metadata
+ provenance
```

The best path depends on the document type.

## 5. Audio

Audio is a time-varying signal. Systems typically transform raw waveforms into frames, spectral representations or learned audio tokens/features before higher-level processing.

A speech pipeline may separate:

```text
speech audio
   ↓
automatic speech recognition
   ↓
text model
   ↓
response text
   ↓
text-to-speech
```

Or a multimodal model may process audio representations more directly.

Architecturally these have different latency, privacy and controllability characteristics.

## 6. Video

Video adds a temporal dimension on top of vision.

A naive strategy that independently processes every frame becomes expensive quickly.

Video systems therefore need choices around:

- frame sampling;
- temporal compression;
- scene segmentation;
- audio alignment;
- motion representation;
- long-range temporal context.

The systems question becomes:

> Which moments and modalities contain the information required for the task?

This is a retrieval/selection problem as much as a model problem.

## 7. Contrastive learning intuition

CLIP provides a useful foundation concept.

Training pairs an image with its associated text and encourages matching representations to be closer than mismatched pairs.

```text
image encoder → image vector ───┐
                                ├→ similarity objective
text encoder  → text vector  ───┘
```

At scale, this can produce representations that support flexible zero-shot classification and retrieval.

It also helped establish language as a powerful interface to visual concepts.

Primary source: https://arxiv.org/abs/2103.00020

## 8. Multimodal foundation models

Models such as GPT-4 demonstrated large-scale systems accepting both image and text input while producing text output.

Primary source: https://arxiv.org/abs/2303.08774

The important systems trend is broader than any one model:

```text
language
   ↓
common control/interface layer
   ↓
vision + audio + video + tools + documents
```

Language increasingly becomes the interface through which users describe goals across different modalities.

## 9. Understanding vs generation

Do not group these into one capability.

### Multimodal understanding

Examples:

- describe an image;
- extract information from a receipt;
- analyse a chart;
- transcribe speech;
- classify video activity.

### Multimodal generation

Examples:

- generate/edit an image;
- generate speech;
- create video;
- synthesise music;
- produce multimodal documents.

Different models, datasets, safety controls and evaluation methods may be required.

## 10. Modality conversion creates information loss

Every conversion can discard information.

Examples:

```text
PDF → plain text
may lose layout

video → transcript
may lose visual action

image → caption
may lose small details

audio → transcript
may lose tone / speaker / timing
```

A system should preserve the original source and provenance when later verification may be required.

## 11. Multimodal hallucination

A vision-language model can produce confident descriptions of details that are absent, ambiguous or visually unreadable.

Similarly, speech systems can mis-transcribe names or numbers while producing grammatically plausible text.

Consequential workflows require verification.

Examples:

- validate extracted totals against document structure;
- require confidence/secondary checks for serial numbers;
- retain cropped evidence alongside extracted fields;
- distinguish "not visible" from guessed content;
- use deterministic barcode/OCR/parsing tools where they outperform general models.

## 12. Resolution and detail are resource decisions

More visual detail can improve small-object or text recognition but increases compute and latency.

A useful production pattern is progressive inspection:

```text
low-cost overview
      ↓
identify relevant region/page/frame
      ↓
higher-detail analysis only there
```

This is analogous to retrieval before long-context reasoning.

## 13. Multimodal context is also a budget

Text tokens are easy to count conceptually. Images, audio and video also consume bounded model resources, even if a provider abstracts the exact representation.

Measure:

- image resolution/count;
- document pages;
- audio duration;
- video duration/frame sampling;
- latency;
- model cost;
- success rate.

Do not assume "one image" is a constant-size workload.

## 14. Security and privacy

Multimodal data can contain information users did not intend to submit:

- faces;
- addresses;
- screens in the background;
- geolocation clues;
- audio from bystanders;
- hidden document metadata;
- signatures;
- account details.

Architects should consider minimisation, redaction, retention, access control and provider data handling before sending raw media to external models.

## 15. Tool vs general-model decision

A general multimodal model is not automatically the best solution.

```text
Task: read barcode
→ barcode decoder may be superior

Task: exact document fields
→ native parser/OCR + validation may be superior

Task: interpret messy mixed-layout evidence
→ multimodal model may add substantial value
```

Use specialised deterministic tools where exactness matters and models where semantic interpretation is the hard part.

## 16. Practical build

Create a small evaluation corpus containing:

- clean images;
- low-resolution images;
- screenshots;
- one chart;
- one multi-page document;
- audio with names/numbers;
- short video.

For each task, compare:

1. general multimodal model;
2. specialised tool where applicable;
3. hybrid pipeline.

Measure:

```text
field/task accuracy
unsupported claims
latency
cost
need for human review
```

The goal is to discover where multimodal models should sit in a system, not simply whether they can process the file.

## 17. Failure modes

### Visual guessing
The model describes details not actually visible.

### Conversion loss
Important structure disappears during preprocessing.

### Excessive media context
The entire video/document is sent when only a small portion matters.

### Modality mismatch
A model is selected because it supports images, even though a specialist parser is more reliable.

### Provenance loss
Generated interpretations are stored without retaining the source evidence.

### Privacy leakage
Background or metadata content is transmitted unnecessarily.

## 18. Architect's checklist

You should be able to explain:

- what multimodal representation means;
- separate encoders vs fused/unified approaches;
- why documents require layout-aware thinking;
- why video creates a temporal-selection problem;
- understanding vs generation;
- why modality conversion loses information;
- why multimodal context has cost;
- when a deterministic specialist tool should replace or verify a general model.

## Primary reading

- Radford et al., **Learning Transferable Visual Models From Natural Language Supervision (CLIP)** — https://arxiv.org/abs/2103.00020
- Vaswani et al., **Attention Is All You Need** — https://arxiv.org/abs/1706.03762
- OpenAI, **GPT-4 Technical Report** — https://arxiv.org/abs/2303.08774

## Mastery gate

**Understand:** explain how multiple modalities can be encoded and made to interact without anthropomorphising the model.

**Build:** compare general, specialist and hybrid approaches on a small multimodal evaluation set.

**Architect:** design a media/document pipeline that explicitly handles selection, provenance, privacy, verification, cost and modality-specific failure modes.
