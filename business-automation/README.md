# Domain 24 — Business Automation

## Purpose

Business automation turns repeatable operational work into controlled systems that combine deterministic software, AI reasoning, tools and human judgment.

> The goal is not to automate every step. It is to remove unnecessary human effort while preserving human authority where ambiguity, consequence or exception requires it.

## Domain structure

01 Workflow Discovery and Automation Selection  
02 Process Decomposition and Automation Boundaries  
03 Deterministic Automation vs AI Reasoning  
04 Durable Workflows, State and Orchestration  
05 Tool-Enabled Automation and System Actions  
06 Exceptions, Approvals and Human-in-the-Loop Operations  
07 Reconciliation, Idempotency and Recovery  
08 Automation Evaluation and Process Intelligence  
09 Production Automation Architecture and Governance  
10 Business Automation Capstone

## Core architecture

```text
Business trigger
      ↓
Workflow state
      ↓
Deterministic rules
      ↓
AI reasoning where ambiguity exists
      ↓
Policy + permission gate
      ↓
Tool / system action
      ↓
Verification + reconciliation
      ↓
Exception / approval if required
      ↓
Business outcome
      ↓
Measurement + improvement
```

## Principles

1. Understand the process before automating it.
2. Automate outcomes, not historical inefficiency.
3. Keep exact rules deterministic.
4. Use AI where interpretation or uncertainty adds value.
5. Persist workflow state outside the model.
6. Make consequential actions explicit and authorized.
7. Design exception paths before happy-path scale.
8. Reconcile external state before retrying effects.
9. Measure business outcomes, not automation volume.
10. Preserve manual recovery and operational ownership.

## Takeaway

> Good automation does not remove humans indiscriminately; it moves human attention from repetitive execution toward exceptions, judgment and improvement.

Next: **01 — Workflow Discovery and Automation Selection**.
