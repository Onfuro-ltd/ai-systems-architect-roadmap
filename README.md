# AI Systems Architect Roadmap

**A practical, evidence-driven roadmap for founders, engineers and technical leaders who want to design, build and operate AI-native systems.**

This is not another list of AI tools, prompt tricks or weekly framework recommendations.

The project teaches the durable architecture behind modern AI systems — from foundation models and retrieval to agents, MCP, memory, evaluation, security, inference infrastructure and decision intelligence — and requires practical evidence before a technology or pattern is treated as production-ready.

## Start here

If you are learning in sequence:

1. Read the [Master Roadmap](./roadmap/master-roadmap.md).
2. Understand the [Competency Levels](./roadmap/competency-levels.md): **Understand → Build → Architect → Lead**.
3. Follow the [Learning Phases](./roadmap/learning-phases.md).
4. Begin with [AI Foundations](./foundations/README.md).
5. Use the [Assessment Model](./roadmap/assessment-model.md) to prove mastery rather than simply marking pages complete.

If you are evaluating a new AI technology, start with the [AI Technology Decision Framework](./docs/decision-framework.md) and [Technology Radar](./technology-radar/README.md).

## What makes this roadmap different

Most AI learning resources optimise for one of three things: explaining a model, teaching a framework, or helping someone reproduce a demo.

This roadmap is organised around a harder question:

> **Can you make sound architectural decisions and build AI systems that remain useful when models, vendors and frameworks change?**

That means every serious topic must eventually connect:

```text
Concept
   ↓
Mechanism
   ↓
Hands-on evidence
   ↓
Failure modes
   ↓
Security + governance
   ↓
Economics + operations
   ↓
Architecture decision
   ↓
Measured outcome
```

## Core principle

Models are powerful but replaceable components.

Durable capability comes from the layers an organisation owns and improves:

```text
Knowledge
Skills
Memory
Data
Tools / MCP
Workflows / Agents
Permissions
Evaluation
Observability
Feedback loops
Domain logic
```

The project therefore treats model choice as an architectural decision, not the architecture itself.

## The roadmap

The curriculum covers 28 connected domains:

1. [AI Foundations](./foundations/README.md)
2. [Modern Foundation Models](./foundations/README.md)
3. [AI Application Engineering](./application-engineering/README.md)
4. [Knowledge Systems and RAG](./knowledge-systems-rag/README.md)
5. [Agents](./agents/README.md)
6. [Skills and Agent Harnesses](./06-skills-agent-harnesses/README.md)
7. [MCP and Tool Ecosystems](./07-mcp-tool-ecosystems/README.md)
8. [Memory Systems](./08-memory-systems/README.md)
9. [Orchestration and Multi-Agent Systems](./09-orchestration-multi-agent/README.md)
10. [Evaluation and Reliability](./10-evaluation-reliability/README.md)
11. [Security, Permissions and Governance](./11-security-permissions-governance/README.md)
12. [AI System Design](./ai-system-design/README.md)
13. [Data and Event Architecture](./data-event-architecture/README.md)
14. [Open-Source and Local AI](./open-source-local-ai/README.md)
15. [Fine-Tuning and Specialist Models](./fine-tuning-specialist-models/README.md)
16. [GPU and Inference Infrastructure](./gpu-inference-infrastructure/README.md)
17. [MLOps and LLMOps](./mlops-llmops/README.md)
18. [Multimodal AI](./multimodal-ai/README.md)
19. [Computer Use and Interface Agents](./computer-use-interface-agents/README.md)
20. [Physical AI and Robotics](./physical-ai-robotics/README.md)
21. [AI Economics and Model Routing](./ai-economics-model-routing/README.md)
22. [Enterprise AI](./enterprise-ai/README.md)
23. [AI Product Design](./ai-product-design/README.md)
24. [Business Automation](./business-automation/README.md)
25. [Decision Intelligence](./decision-intelligence/README.md)
26. [Domain-Specific AI Systems](./domain-specific-ai-systems/README.md)
27. [AI-Native Commerce and Operations](./ai-native-commerce-operations/README.md)
28. [Build an AI Operating System](./ai-operating-system/README.md)

> **Domain 02 note:** Modern Foundation Models is currently taught within the shared [Foundations curriculum](./foundations/README.md), alongside the fundamental model concepts it builds on. It remains a distinct architectural domain in the master roadmap.

See the [Master Roadmap](./roadmap/master-roadmap.md) for the architectural scope of each domain.

For the canonical directory for every domain, including the shared Domain 01/02 Foundations home and legacy-track status, see the [Authoritative Domain Directory Map](./roadmap/domain-directory-map.md).

## Foundations curriculum

The first complete curriculum track is [AI Foundations](./foundations/README.md):

- [AI history and evolution](./foundations/01-ai-history-and-evolution.md)
- [Neural networks to transformers](./foundations/02-neural-networks-to-transformers.md)
- [Transformers and attention](./foundations/03-transformers-and-attention.md)
- [Tokens, context and embeddings](./foundations/04-tokens-context-and-embeddings.md)
- [Training, inference and scaling](./foundations/05-training-inference-and-scaling.md)
- [Reasoning and test-time compute](./foundations/06-reasoning-and-test-time-compute.md)
- [Mixture of Experts](./foundations/07-mixture-of-experts.md)
- [Multimodal foundations](./foundations/08-multimodal-foundations.md)
- [Foundations capstone](./foundations/09-foundations-capstone.md)

The capstone requires a reproducible model-comparison laboratory, failure taxonomy and architecture decision record. Reading alone does not count as mastery.

## Technology Radar

New AI technology is classified as:

- **IGNORE** — insufficient value/evidence or unacceptable trade-offs;
- **WATCH** — strategically interesting but immature or not yet needed;
- **EXPERIMENT** — worth a controlled test against a baseline;
- **ADOPT** — proven enough for defined production use cases;
- **BUILD AROUND** — a durable principle, protocol or capability the architecture should intentionally support.

Verdicts are expected to change when evidence changes.

See [Technology Radar](./technology-radar/README.md) and the [Decision Framework](./docs/decision-framework.md).

## Architecture philosophy

The project is guided by several rules:

**Architecture over tools.** Start with the problem and required capability, then choose technology.

**Evidence over demos.** A successful demo establishes possibility, not production reliability.

**Deterministic boundaries around probabilistic models.** Models can propose and interpret; critical permissions, invariants and exact validations belong in deterministic systems where possible.

**Evaluation before autonomy.** Increasing an agent's permissions without measuring behaviour increases risk faster than capability.

**Model independence where practical.** Do not place organisational knowledge, workflows and governance entirely inside one provider's interface.

**Outcomes over benchmark theatre.** Measure successful tasks, reliability, latency, operational burden and business/user value.

Read the project philosophy in [`docs/`](./docs/).

## Contributing

This project is being structured for a large contributor community rather than as a personal notes repository.

Before proposing curriculum or technology reviews, read:

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [Curriculum Authoring Standard](./docs/curriculum-authoring-standard.md)
- [AI Technology Decision Framework](./docs/decision-framework.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)

Submissions should distinguish evidence from opinion, cite primary sources where possible, disclose material limitations, and explain how a concept affects real system design.

GitHub stars, vendor claims and influencer popularity are not evidence of production readiness.

## Project status

**Current stage: 28-domain curriculum drafted; v1.0 repository audit and hardening in progress.**

The authoritative curriculum sequence has now been drafted through Domain 28. Before a v1.0 release, the repository is undergoing privacy cleanup, authoritative-domain structure verification, legacy-track consolidation, navigation validation and editorial normalization. See the [v1.0 Repository Audit and Hardening Plan](./docs/v1-repository-audit-and-hardening.md).

The roadmap is intentionally living. AI models, protocols and techniques will change; the project's responsibility is to preserve durable knowledge while updating conclusions when strong evidence changes.

## Long-term objective

The curriculum ultimately converges on a capstone architecture in which models are interchangeable workers inside a governed AI operating layer:

```text
Human / System Intent
        ↓
Orchestration
        ↓
Model Routing
        ↓
Agents / Workflows
        ↓
Skills + Memory + Knowledge
        ↓
MCP / Tools
        ↓
Policy + Permissions
        ↓
Business Systems
        ↓
Outcomes
        ↓
Evaluation + Learning
```

Security, observability, auditability, cost control and human control surround the full system.

The goal is not simply to **use AI**.

The goal is to learn how to **architect systems powered by AI**.
