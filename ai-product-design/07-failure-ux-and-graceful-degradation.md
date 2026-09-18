# 07 — Failure UX and Graceful Degradation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Failure UX and Graceful Degradation** within AI Product Design;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Design useful behaviour when models, tools, data or providers fail.

## Failure classes

Distinguish unavailable service, timeout, insufficient evidence, policy restriction, permission denial, invalid output, tool failure, stale data, ambiguous outcome and quality uncertainty.

## Specific messages

Tell users what is known and what they can safely do next. Avoid generic "something went wrong" when the system knows the failure stage.

## Degradation

Possible modes include alternate approved model, read-only results, deterministic search, queued processing, partial completion, draft-only operation or human escalation.

## Unknown outcome

If an external action may have happened, say its status is unknown and reconcile before offering retry.

## Partial success

Show which parts succeeded and which did not.

## Reliability expectations

Set expectations for long-running work and asynchronous completion rather than presenting all AI as instant chat.

## Exercise

Create failure UX for a workflow whose model succeeds but its final external tool call times out after submission.

## Takeaway

> Graceful degradation preserves user safety and useful progress when the ideal AI path is unavailable.

Next: **08 — Feedback, Learning and Product Evaluation**.
