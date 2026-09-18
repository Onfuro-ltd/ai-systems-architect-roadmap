# 08 — Operational Governance and Model Registry

## Purpose

Operational governance defines which AI artifacts may run, for which workloads, under whose approval and with what evidence.

## Registry

A production registry should capture artifact identity, type, base/provider revision, license, data lineage, evaluation, risk classification, owner, approved workloads, runtime compatibility, approval, deployment state and retirement status.

## Lifecycle

```text
Candidate → evaluated → approved → canary → production → deprecated → retired
```

Restricted or quarantined states may be needed.

## Separation of duties

High-risk changes can require different people or roles to create, evaluate and approve them. Apply least privilege to artifact upload, registry mutation and production promotion.

## Workload approval

Approval should be scoped. A model approved for summarization is not automatically approved for consequential tool execution.

## Expiry and review

Licenses, provider terms, evaluations, data policies and risk assumptions can change. Schedule revalidation based on risk.

## Audit

Record who changed what, when, why, evidence used and resulting deployment. Governance should be machine-queryable where practical.

## Retirement

Remove traffic, update routing dependencies, preserve required evidence, revoke access and delete artifacts according to policy.

## Exercise

Design a registry schema and approval workflow for hosted models, open-weight models and fine-tuned adapters.

## Takeaway

> A registry is the control ledger for deployable AI capability, not a folder of model files.

Next: **09 — LLMOps Platform Architecture**.
