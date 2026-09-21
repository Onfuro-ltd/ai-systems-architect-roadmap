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

## Recommended learning paths

The repository is now navigable as a complete 28-domain curriculum rather than a Foundations-only track.

Choose the path that matches your goal:

- **Full AI systems architect path** — follow the [Learning Phases](./roadmap/learning-phases.md) from Foundations through the AI Operating System capstone.
- **Application and agent engineering** — Domains 03–13, then 21 and 24.
- **Inference/platform engineering** — Domains 01–03, 10, 12–17 and 21–22.
- **Security/governance** — Domains 03, 05, 07, 09–13, 17 and 22.
- **Multimodal/interface systems** — Domains 01–03, 10–12 and 18–20.
- **AI product, automation and decision systems** — Domains 03, 10–13 and 21–28.

Use the [Prerequisites and Recommended Paths](./roadmap/prerequisites-and-paths.md) for dependency-aware routes and the [Domain Status Matrix](./roadmap/domain-status.md) for curriculum completion status.

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

## Licensing

This repository uses a scoped dual-license model:

- **Software/code:** [Apache License 2.0](./LICENSES/Apache-2.0.txt)
- **Curriculum/documentation:** [Creative Commons Attribution 4.0 International](./LICENSES/CC-BY-4.0.txt)

The root [LICENSE](./LICENSE) defines the scope, including treatment of embedded code examples and third-party material.

## Project status

**Current stage: v1.0 release candidate; P0–P5 engineering hardening and the licensing decision are complete on the release branch, with final publication pending cumulative review, merge-to-main validation and final tag/release verification.**

The authoritative curriculum, repository hardening and scoped dual-license model are complete as a release candidate. The remaining publication gates are operational: review and merge the cumulative release branch into `main`, confirm CI on that exact main commit, run the tag-ready gate on merged main, then create and verify the v1.0 tag/release. See the [v1.0 Release Checklist](./docs/v1.0-release-checklist.md) and [Release Policy](./docs/release-policy.md).

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
