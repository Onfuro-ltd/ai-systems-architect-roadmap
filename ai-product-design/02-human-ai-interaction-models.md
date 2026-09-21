# 02 — Human-AI Interaction Models

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Human-AI Interaction Models** within AI Product Design;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Choose the interaction pattern that matches the task rather than defaulting every AI feature to chat.

## Patterns

Useful patterns include autocomplete, inline transformation, search/answer, copilot, draft/review, recommendation, structured workflow, background agent, voice interaction and bounded autonomous execution.

## Chat

Chat is flexible but can hide state, permissions and workflow progress. Use structured UI when users need to compare, approve, edit or track operations.

## Mixed initiative

Humans and AI can alternate initiative. Make it clear who currently controls the next consequential step.

## State

Show durable task state outside the conversation when workflows span multiple steps or time.

## Interruptibility

Users should be able to pause, cancel, redirect or take over long-running AI work where feasible.

## Progressive disclosure

Expose complexity, evidence and controls when needed without forcing every user to inspect internal details.

## Accessibility

AI interaction should preserve keyboard, screen-reader, captioning and other accessibility needs; generated interfaces must not become an accessibility regression.

## Exercise

Choose interaction patterns for drafting an email, investigating a business anomaly, completing a form and monitoring a long-running process.

## Takeaway

> Chat is one interface pattern for AI, not the architecture of an AI product.

Next: **03 — Uncertainty, Confidence and Evidence**.
