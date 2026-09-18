# 01 — What Is Multimodal AI?

Multimodal AI is the study and engineering of systems that can process, combine, reason over, or generate more than one type of information.

Common modalities include:

- text;
- images;
- audio;
- video;
- documents;
- structured data;
- sensor data;
- actions in software or physical environments.

The important idea is not simply that several media types exist in one product.

> **Core principle:** Multimodal AI becomes valuable when different modalities contribute to one useful reasoning or decision process.

---

## 1. What is a modality?

A modality is a form in which information is represented or perceived.

Examples:

```text
Text   -> words, code, tables
Image  -> pixels, objects, spatial relationships
Audio  -> speech, sound, timing, tone
Video  -> images over time + motion + often audio
Sensor -> temperature, position, force, depth, telemetry
Action -> clicks, API calls, robot movement, software changes
```

Different modalities contain different kinds of information.

A product photograph may reveal physical damage that is absent from the product description.

A customer voice message may contain an issue that has never been written in a support ticket.

A video may reveal sequence and causality that a single image cannot.

---

## 2. Multimodal does not mean "everything in one model"

There are two broad ways to build multimodal systems.

### Native multimodal model

One model is trained or adapted to process several modalities.

```text
Text + Image + Audio
        |
        v
Multimodal Model
        |
        v
Reasoning / Output
```

Potential advantages:

- easier cross-modal reasoning;
- fewer hand-offs;
- simpler application interface;
- shared internal representations.

Potential disadvantages:

- higher compute requirements;
- less specialised performance on some tasks;
- harder debugging;
- provider dependence;
- reduced control over individual perception stages.

### Composed multimodal system

Specialised systems handle different inputs.

```text
Image -> Vision System -----\
Audio -> Speech System ------+--> Orchestrator -> Reasoning Model
PDF   -> Parser ------------/
```

Potential advantages:

- specialised components;
- easier replacement;
- better observability;
- more control;
- easier deterministic verification.

Potential disadvantages:

- more engineering;
- more latency;
- cross-modal alignment can be harder;
- more integration boundaries.

Neither architecture is universally superior.

---

## 3. The real challenge: alignment

Suppose a system receives:

- a product image;
- a product title;
- a customer complaint;
- a supplier specification sheet.

The system must understand that all four refer to the same product and determine which information is authoritative for each question.

This is an alignment problem.

```text
Image object
     |
     +--> Product identity
     |
Listing title
     |
     +--> Product identity
     |
Supplier specification
     |
     +--> Product identity
     |
Customer complaint
     |
     +--> Product identity
```

Without correct alignment, multimodal reasoning can become confidently wrong.

---

## 4. Fusion: how modalities are combined

Multimodal systems need a mechanism for combining information.

At a high level, fusion can happen at different stages.

### Early fusion

Representations are combined before deeper reasoning.

```text
Image representation + Text representation
                 |
                 v
          Combined reasoning
```

### Late fusion

Each modality is processed separately and results are combined later.

```text
Image analysis ----\
                    +--> Decision layer
Text analysis -----/
```

### Hybrid fusion

Some processing is separate and some is shared.

This is common in practical systems because it balances specialisation and integration.

The exact implementation varies by model family and architecture, but the design question remains the same:

> At what point should information from different modalities influence each other?

---

## 5. Perception, reasoning, and action are different layers

A system may correctly perceive something and still reason incorrectly about it.

Example:

```text
Image:
Damaged cardboard box
```

Perception may correctly detect:

- crushed corner;
- torn packaging;
- exposed product.

But reasoning may still incorrectly conclude:

- damage occurred during delivery;
- supplier packaging was inadequate;
- customer should automatically receive a refund.

Those conclusions require additional evidence and business rules.

The correct architecture separates:

```text
Perception
    |
    v
Evidence
    |
    v
Reasoning
    |
    v
Policy / Validation
    |
    v
Action
```

Do not allow perception outputs to silently become business decisions.

---

## 6. Structured data is also part of multimodal systems

People often use "multimodal" to mean text plus images.

Enterprise systems usually need more.

For example:

```text
Product image
+
Supplier PDF
+
Customer review text
+
Sales database
+
Return-rate time series
```

The model may understand the image and text, while deterministic services calculate:

- margin;
- stock cover;
- return rates;
- fee impact.

The final intelligence comes from combining model perception with verified structured data.

---

## 7. Native multimodality is not automatically better

A larger general-purpose multimodal model may be excellent at:

- broad visual reasoning;
- describing scenes;
- interpreting screenshots;
- connecting text and images.

A specialist system may still outperform it at:

- barcode reading;
- exact document extraction;
- industrial defect detection;
- medical imaging workflows;
- high-precision OCR;
- identity verification;
- deterministic measurement.

Architecture should be driven by required accuracy and risk, not by novelty.

---

## 8. Multimodal hallucinations

Multimodal systems can hallucinate too.

Possible failures include:

- claiming an object exists when it does not;
- missing small but critical details;
- reading text incorrectly from an image;
- inferring causality from a video without evidence;
- inventing information hidden outside the frame;
- confusing visually similar products;
- incorrectly associating audio with a speaker;
- treating generated media as authentic evidence.

A confident visual description is not proof.

High-impact workflows require verification.

---

## 9. Provenance becomes more important

In text systems, citations often point to documents.

Multimodal systems may need richer provenance.

For example:

```text
Claim:
"The package is visibly crushed on the upper-right corner."

Evidence:
image_0042.jpg
region: x=0.71-0.94, y=0.03-0.31
source: customer-upload
captured_at: 2026-09-10T12:13:00Z
verification_status: unverified
```

For audio:

```text
source: call_1932.wav
speaker: customer
segment: 01:32-01:46
transcription_confidence: 0.92
```

This makes decisions easier to audit.

---

## 10. Multimodal input creates new security boundaries

Every modality can carry untrusted content.

Examples:

- an image containing malicious instructions for a vision-language model;
- a PDF containing hidden or misleading text;
- a webpage screenshot containing prompt injection;
- an audio recording instructing an agent to ignore policy;
- manipulated or synthetic media presented as evidence.

The same principle used in secure RAG applies:

> **Content is data, not authority.**

A retrieved image, transcript, document, or video does not gain permission to override system policy.

---

## 11. Multimodal AI and agents

Multimodal AI becomes especially powerful when combined with agents.

Example:

```text
Customer sends screenshot
        |
        v
Vision understanding
        |
        v
Identify order issue
        |
        v
Retrieve policy
        |
        v
Check order system
        |
        v
Recommend resolution
        |
        v
Human approval or safe action
```

The vision model provides perception.

The agent manages the workflow.

The tools provide access to systems.

The policy layer controls what may happen.

---

## 12. Multimodal AI in commerce

Commerce is naturally multimodal.

A single product can have:

- images;
- videos;
- listing text;
- technical specifications;
- packaging labels;
- customer reviews;
- return photographs;
- support conversations;
- structured sales and inventory data.

A future commerce intelligence system could reason across all of them.

Example:

```text
High return rate detected
        |
        v
Analyse return reasons
        |
        v
Inspect customer return images
        |
        v
Compare listing images
        |
        v
Check supplier specifications
        |
        v
Identify mismatch
        |
        v
Recommend listing or sourcing action
```

This is much more valuable than asking a model to merely caption an image.

---

## 13. Model-independent architecture

Do not design the business system around one multimodal model provider.

A stronger architecture is:

```text
Application
    |
    v
Multimodal Gateway
    |
    +--> Vision Model A
    +--> Vision Model B
    +--> Speech Model
    +--> Video Model
    +--> Local Specialist Model
    |
    v
Normalised Evidence
    |
    v
Reasoning / Workflow Layer
```

The application should own:

- identity;
- evidence;
- state;
- permissions;
- business rules;
- evaluation;
- audit history.

Models remain replaceable workers.

---

## 14. Cost and latency matter

Multimodal inference can be much more expensive than plain text processing.

Costs may come from:

- image resolution;
- number of images;
- video duration;
- audio duration;
- frame extraction;
- repeated model calls;
- large context windows;
- generation workloads.

A production system should ask:

```text
Can deterministic preprocessing reduce the workload?

Can we analyse selected frames instead of full video?

Can a smaller specialist model handle first-pass classification?

Should high-cost reasoning be reserved for ambiguous cases?
```

The correct metric remains:

> **Cost per successful outcome.**

---

## 15. A practical multimodal design pattern

A reliable production flow often looks like this:

```text
Input
  |
  v
Validate file / source
  |
  v
Deterministic preprocessing
  |
  v
Specialist perception model
  |
  v
Structured evidence
  |
  v
Reasoning model
  |
  v
Business rules
  |
  v
Human approval where required
  |
  v
Action
  |
  v
Evaluation
```

This architecture is less glamorous than "one model does everything," but usually easier to operate and trust.

---

## 16. Common mistakes

Avoid these patterns:

### Mistake 1 — Treating image upload as full multimodal intelligence

Accepting several file types is not the same as reasoning across them well.

### Mistake 2 — Sending all media directly to the largest model

This can be expensive, slow, and difficult to debug.

### Mistake 3 — Ignoring provenance

Generated, user-supplied, verified, and authoritative media should not be treated equally.

### Mistake 4 — Using AI where deterministic extraction is better

If exact parsing or measurement is available, use it.

### Mistake 5 — Trusting visual confidence

Models can sound certain while misreading important details.

### Mistake 6 — Allowing multimodal inputs to become instructions

Untrusted content must remain data.

---

## 17. When should you use multimodal AI?

Use it when meaningful information exists across multiple modalities and combining that information improves the outcome.

Good candidates include:

- visual quality inspection;
- document understanding;
- screenshot support workflows;
- image-based catalogue analysis;
- voice assistants;
- video understanding;
- content generation;
- accessibility;
- computer-use agents;
- robotics.

Do not use it simply because a model supports images or audio.

---

## 18. Mastery checklist

You should be able to explain:

- what a modality is;
- native vs composed multimodal systems;
- early vs late fusion at a conceptual level;
- perception vs reasoning vs action;
- why structured data still matters;
- multimodal hallucination risks;
- provenance and evidence requirements;
- multimodal prompt-injection risks;
- model-independent architecture;
- cost and latency trade-offs;
- when a specialist model is preferable.

You should also be able to design a simple multimodal workflow and identify where validation belongs.

---

## Build exercise

Design a **multimodal product investigation pipeline**.

Input:

- product listing text;
- three product images;
- one customer complaint;
- structured return-rate data.

Your system should produce:

```json
{
  "problem_detected": true,
  "evidence": [],
  "likely_causes": [],
  "confidence": 0.0,
  "recommended_next_action": "",
  "requires_human_review": true
}
```

Rules:

- preserve the source of every evidence item;
- do not allow image content to override system instructions;
- use deterministic calculations for return-rate metrics;
- separate observed facts from inferred causes;
- require human review before changing any live listing.

The purpose of the exercise is not to produce the best prompt. It is to design the system boundaries correctly.

---

## Decision framework

Before adding multimodal AI, ask:

```text
Does another modality contain information we currently miss?
        |
        no -> Do not add multimodal complexity
        |
       yes
        v
Can deterministic software solve it reliably?
        |
       yes -> Prefer deterministic processing
        |
        no
        v
Do we need specialist perception or general reasoning?
        |
        v
Choose architecture
        |
        v
Add provenance + validation + evaluation
```

---

## What comes next

Continue with:

**[02 — Vision Models](02-vision-models.md)**

The next chapter explains how AI systems represent and reason about visual information, and where general vision-language models differ from specialist computer-vision systems.
