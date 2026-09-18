# 10 — MLOps and LLMOps Capstone

## Purpose

Design an enterprise operating system for the lifecycle of AI changes.

## Scenario

A multitenant platform uses hosted models, private open-weight models, RAG, tools, agents and specialist adapters. Multiple teams change prompts, models, datasets, retrieval, policies and runtimes.

The organization needs fast experimentation without uncontrolled production change.

## Target architecture

```text
Change proposal
      ↓
Versioned experiment
      ↓
Evaluation pipeline
      ↓
Registry + risk/policy gate
      ↓
Release manifest
      ↓
Shadow / canary / progressive rollout
      ↓
Production system
      ↓
Tracing + quality + cost + outcomes
      ↓
Drift / incident detection
      ↓
Rollback OR curated next experiment
```

## Required deliverables

Produce an experiment schema; artifact/version taxonomy; immutable system release manifest; dataset/index lineage; evaluation suites and promotion gates; CI/CD risk matrix; registry lifecycle; approval model; shadow/canary strategy; feature flags and routing; end-to-end tracing; privacy-safe telemetry; quality/cost dashboards; drift diagnostics; feedback curation; kill switches; incident runbooks; rollback and data-compatibility strategy; environment isolation; tenant controls; ownership/RACI; and at least three ADRs.

## Failure matrix

Cover bad model release, prompt regression, corrupted retrieval index, tool-schema incompatibility, provider behaviour change/outage, runaway cost, quality degradation without HTTP errors, sensitive logging, tenant leakage, compromised artifact, failed rollback and contaminated feedback.

## Acceptance criteria

The design passes only if every behaviour-affecting dependency is versioned; experiments are reproducible enough to explain results; clean evaluation can block promotion; approvals are scoped to workload risk; deployments are progressive where warranted; production quality is observable; feedback is verified before learning; drift is diagnosed before retraining; kill switches are scoped; rollback includes data/index compatibility; tenant boundaries are deterministic; and applications remain portable across model providers and runtimes.

## Final architecture principle

> Production AI should be able to answer four questions at any moment: What is running? Why was it approved? How is it performing? How do we safely undo it?

**Domain 17 — MLOps and LLMOps complete.**

Next domain: **18 — Multimodal AI**.
