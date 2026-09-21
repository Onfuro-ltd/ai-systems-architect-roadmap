# 10 — Final AI Operating System Capstone

## Purpose

Integrate all 28 roadmap domains into a production-grade, model-independent AI operating architecture.

## Prerequisite domains

This capstone integrates the preceding roadmap rather than replacing it.

Before attempting the final build, review the direct prerequisite map for [Domains 01–27](../roadmap/prerequisites-and-paths.md). In particular, the architecture must demonstrate evidence from:

- [Foundations and modern models](../foundations/README.md)
- [AI Application Engineering](../application-engineering/README.md), [Knowledge Systems and RAG](../knowledge-systems-rag/README.md) and [Agents](../agents/README.md)
- [Skills](../06-skills-agent-harnesses/README.md), [MCP](../07-mcp-tool-ecosystems/README.md), [Memory](../08-memory-systems/README.md) and [Orchestration](../09-orchestration-multi-agent/README.md)
- [Evaluation](../10-evaluation-reliability/README.md) and [Security/Governance](../11-security-permissions-governance/README.md)
- [System Design](../ai-system-design/README.md) and [Data/Event Architecture](../data-event-architecture/README.md)
- [MLOps/LLMOps](../mlops-llmops/README.md), [AI Economics/Model Routing](../ai-economics-model-routing/README.md) and [Enterprise AI](../enterprise-ai/README.md)
- the relevant specialist domains (14–20 and 23–27) for the selected implementation scope.

## Scenario

Design a multitenant AI platform supporting knowledge work, multimodal evidence, recommendations, durable business automation, computer-use fallback and bounded action across multiple domains. It can route among hosted, private and specialist models while preserving identity, policy, evaluation and human authority.

## Final architecture

```text
                 HUMAN / SYSTEM INTENT
                           ↓
             IDENTITY • TENANT • PURPOSE
                           ↓
               TASK / RISK CLASSIFICATION
                           ↓
               POLICY + PERMISSION GATE
                           ↓
                     ORCHESTRATOR
                    ↙             ↘
          DURABLE WORKFLOW       AGENT
                    ↘             ↙
                 SKILLS / PROCEDURES
                           ↓
        MEMORY + KNOWLEDGE + AUTHORITATIVE DATA
                           ↓
                     MODEL ROUTER
              ↙        ↓        ↓        ↘
           Small    Frontier  Specialist  Private
                           ↓
                 STRUCTURED PROPOSAL
                           ↓
             VALIDATION + POLICY RECHECK
                           ↓
                   MCP / TYPED TOOLS
                           ↓
              SYSTEMS OF RECORD / ACTION
                           ↓
              VERIFICATION / RECONCILIATION
                           ↓
                    VERIFIED OUTCOME
                           ↓
       EVALUATION • OBSERVABILITY • ECONOMICS
                           ↓
                  CURATED LEARNING LOOP
```

Surrounding the complete architecture:

```text
SECURITY | GOVERNANCE | AUDIT | DATA GOVERNANCE
RELIABILITY | COST CONTROL | HUMAN CONTROL | PORTABILITY
```

## Required deliverables

Produce system context and trust boundaries; multitenant identity/delegation; canonical capability contracts; registries for models, knowledge, memory, skills, workflows, tools, policies and evaluations; context assembly; provenance; model router; provider adapters; specialist/local strategy; agent architecture; durable workflow engine; MCP/tool gateway; authorization and policy decision points; approval framework; idempotency/reconciliation; UNKNOWN-state handling; multimodal pipeline; computer-use fallback controls; decision-intelligence services; observability/tracing; SLOs; cost-per-outcome model; evaluation suites; catastrophic-failure gates; release manifests; canary/rollback; incident response; kill switches; curated feedback; learning destinations; portability tests; progressive-autonomy framework; platform/team ownership; and architecture decision records.

## Required end-to-end demonstrations

### 1. Knowledge task

Authorized retrieval → evidence-grounded answer → provenance → evaluation.

### 2. Decision task

Signals → forecast → constraints → recommendation → explanation → human decision → outcome.

### 3. Action task

Intent → workflow → AI interpretation → policy → approval → tool → verification → reconciliation.

### 4. Agent task

Bounded plan → skills/tools → budgets → recovery → verified completion.

### 5. Model replacement

Swap the primary model/provider and demonstrate that domain knowledge, workflows, policies, tools and evaluation remain intact.

### 6. Failure recovery

Simulate provider outage, tool timeout after possible side effect, stale data, authorization denial and bad model release.

## Acceptance criteria

The architecture passes only if:

- models are replaceable beneath stable capability contracts;
- identity and tenant context propagate end-to-end;
- authorization occurs before retrieval and action;
- authoritative state remains outside model memory;
- context is provenance-aware and minimized;
- agents have bounded budgets and durable state;
- reusable procedures are versioned skills/workflows;
- hard rules and permissions are deterministic;
- tools are typed, permissioned and auditable;
- consequential actions are verified;
- UNKNOWN outcomes reconcile before retry;
- human authority is explicit and revocable;
- evaluation gates behaviour-affecting releases;
- observability links AI behaviour to business outcomes;
- costs are measured per successful outcome;
- feedback is curated before learning;
- production components cannot silently rewrite their own authority;
- provider/model migration is tested rather than assumed;
- failure modes have safe degradation and recovery;
- the organization retains ownership of its durable intelligence layer.

## The final operating loop

```text
Observe
  ↓
Understand
  ↓
Decide
  ↓
Act
  ↓
Verify
  ↓
Measure
  ↓
Evaluate
  ↓
Learn
  ↓
Improve
  ↺
```

Every arrow is governed by identity, evidence, permissions and measurable outcomes.

## Final principle

> Build systems in which models can become dramatically better—or be replaced entirely—without requiring the organization to surrender its data, workflows, policies, evaluations, tools, memory, knowledge or ability to understand why an action occurred.

**Domain 28 — Build an AI Operating System complete.**

**The authoritative 28-domain AI Systems Architect Roadmap is now complete at the curriculum level.**
