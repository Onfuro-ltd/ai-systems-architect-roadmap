# 05 — Model Routing and Inference Plane

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Model Routing and Inference Plane** within Build an AI Operating System;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Make models interchangeable execution resources selected by measured requirements.

## Inference interface

Normalize messages/context, structured outputs, tools, modalities, streaming, usage and errors behind provider/runtime adapters.

## Eligibility before optimization

Filter candidates by privacy, residency, licensing, modality, context, tool support, safety and workload approval before considering cost.

## Routing

```text
Task requirements
      ↓
Eligible model set
      ↓
Capability evidence
      ↓
Quality / latency / cost policy
      ↓
Selected model
      ↓
Validation
      ↓
Accept / escalate
```

## Portfolio

Support frontier hosted models, smaller hosted models, private/open models and tuned specialists where justified.

## Fallback

Fallback routes must remain policy- and capability-compatible. Separate outage fallback from quality escalation.

## Economics

Measure total cost per verified successful outcome, including retries, context, tools and human review.

## Portability

Continuously test representative workloads against alternative models so theoretical provider independence remains real.

## Exercise

Design a router for low-risk extraction, confidential analysis, multimodal work and high-reasoning tasks.

## Takeaway

> In the AI OS, the model is a routed compute capability—not the permanent home of the application's intelligence.

Next: **06 — Tools, MCP and Action Plane**.
