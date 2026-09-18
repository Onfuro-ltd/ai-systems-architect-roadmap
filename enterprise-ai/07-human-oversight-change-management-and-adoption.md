# 07 — Human Oversight, Change Management and Adoption

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Human Oversight, Change Management and Adoption** within Enterprise AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Design the human system around AI so people can use, supervise and challenge it effectively.

## Meaningful oversight

A human approval step is useful only when the reviewer can understand the proposed action, relevant evidence, uncertainty and consequence and has time/authority to reject it.

## Progressive autonomy

```text
Suggest → draft → execute with approval → bounded autonomy → broader autonomy
```

Move between stages based on evidence, not enthusiasm.

## Roles

Define product owner, domain owner, platform owner, security/risk owner, data owner and operational responder.

## Change management

Prepare users for changed workflows, responsibilities, escalation paths and failure modes. Training should include when not to trust the AI.

## Adoption metrics

Measure useful completion, correction, override, escalation, cycle time and outcome—not merely logins or messages sent.

## Feedback

Provide easy mechanisms to report errors and capture corrections, but curate feedback before it becomes training/evaluation data.

## Workforce design

AI may redistribute tasks rather than simply remove them. Redesign processes around strengths of humans, deterministic software and models.

## Exercise

Create a progressive-autonomy rollout for an AI assistant moving from recommendations to bounded operational actions.

## Takeaway

> Enterprise adoption is successful when responsibility and workflow improve alongside model capability.

Next: **08 — Enterprise AI Platform and Team Topology**.
