# 09 — AI Product Architecture and Lifecycle

## Purpose

Connect product experience to the underlying AI control plane throughout the feature lifecycle.

## Architecture

```text
Product UI / API
      ↓
Task + identity + permissions
      ↓
AI capability contract
      ↓
Routing / RAG / agent / tools
      ↓
Validation + policy
      ↓
Product state
      ↓
User control / approval
      ↓
Outcome + telemetry
```

## Capability boundary

The product should call stable internal capabilities rather than hard-code one provider/model into the UX.

## Product state

Persist drafts, approvals, task status and outcomes in application state, not solely in model conversation.

## Release

Product, prompt, model, retrieval, tool and policy changes can all alter behaviour. Use versioning and evaluation from Domain 17.

## Lifecycle

Discovery → bounded prototype → offline evaluation → user research → controlled pilot → progressive release → operation → improvement → retirement.

## Kill switches

Provide feature/capability controls that can disable risky AI behaviour without taking down unrelated product functions.

## Cost

Include model, tool, human-review and failure costs in product unit economics.

## Exercise

Create a lifecycle and architecture for an AI feature that starts as a copilot and may later receive bounded action authority.

## Takeaway

> The UX should remain stable around a capability contract even while the models beneath it evolve.

Next: **10 — AI Product Design Capstone**.
