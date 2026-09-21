# 02 — Process Decomposition and Automation Boundaries

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Process Decomposition and Automation Boundaries** within Business Automation;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Break business work into steps with different automation characteristics.

## Decomposition

For each step identify input, transformation/decision, output, authoritative system, owner, rule, uncertainty, consequence and failure mode.

## Step classes

Useful classes include deterministic calculation, lookup/retrieval, validation, classification, extraction, generation, judgment, approval, external action and reconciliation.

## Boundaries

A workflow can automate low-risk preparation while retaining human authority over high-consequence decisions.

## Handoffs

Define machine-to-machine, AI-to-software, AI-to-human and human-to-AI contracts explicitly.

## Inputs

Reject or quarantine malformed inputs before reasoning. Do not use an LLM as a substitute for basic schema validation.

## Outputs

AI outputs entering downstream systems should use typed structures and deterministic validation.

## Exercise

Decompose an invoice-like process into deterministic, AI-assisted and human-controlled steps with clear interfaces.

## Takeaway

> Process decomposition reveals where probabilistic intelligence belongs—and where it does not.

Next: **03 — Deterministic Automation vs AI Reasoning**.
