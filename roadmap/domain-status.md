# Domain Completion and Status Matrix

This matrix is the reader-facing status view for the authoritative 28-domain curriculum.

**Status meaning**

- **Authoritative** — this is the canonical curriculum home.
- **P3 normalized** — README/chapter navigation, learning outcomes, exercises and editorial gates passed the P3 audit.
- **Shared home** — Domain 02 is distinct in the roadmap but intentionally shares the Foundations directory with Domain 01.

| Domain | Name | Home | Chapters | Learning phase | Curriculum status |
| ---: | --- | --- | ---: | --- | --- |
| 01 | AI Foundations | [`foundations/README.md`](../foundations/README.md) | 9 | 0 — Orientation and AI literacy | Authoritative · P3 normalized |
| 02 | Modern Foundation Models | [`foundations/README.md`](../foundations/README.md) | 9 | 0 — Orientation and AI literacy | Authoritative · P3 normalized · Shared home |
| 03 | AI Application Engineering | [`application-engineering/README.md`](../application-engineering/README.md) | 15 | 1 — Reliable AI applications | Authoritative · P3 normalized |
| 04 | Knowledge Systems and RAG | [`knowledge-systems-rag/README.md`](../knowledge-systems-rag/README.md) | 12 | 2 — Knowledge and grounding | Authoritative · P3 normalized |
| 05 | Agents | [`agents/README.md`](../agents/README.md) | 11 | 3 — Agents and tools | Authoritative · P3 normalized |
| 06 | Skills and Agent Harnesses | [`06-skills-agent-harnesses/README.md`](../06-skills-agent-harnesses/README.md) | 9 | 4 — Skills, memory and harness engineering | Authoritative · P3 normalized |
| 07 | MCP and Tool Ecosystems | [`07-mcp-tool-ecosystems/README.md`](../07-mcp-tool-ecosystems/README.md) | 9 | 3 — Agents and tools | Authoritative · P3 normalized |
| 08 | Memory Systems | [`08-memory-systems/README.md`](../08-memory-systems/README.md) | 9 | 4 — Skills, memory and harness engineering | Authoritative · P3 normalized |
| 09 | Orchestration and Multi-Agent Systems | [`09-orchestration-multi-agent/README.md`](../09-orchestration-multi-agent/README.md) | 9 | 6 — Orchestration and production architecture | Authoritative · P3 normalized |
| 10 | Evaluation and Reliability | [`10-evaluation-reliability/README.md`](../10-evaluation-reliability/README.md) | 9 | 5 — Evaluation, security and governance | Authoritative · P3 normalized |
| 11 | Security, Permissions and Governance | [`11-security-permissions-governance/README.md`](../11-security-permissions-governance/README.md) | 9 | 5 — Evaluation, security and governance | Authoritative · P3 normalized |
| 12 | AI System Design | [`ai-system-design/README.md`](../ai-system-design/README.md) | 11 | 6 — Orchestration and production architecture | Authoritative · P3 normalized |
| 13 | Data and Event Architecture | [`data-event-architecture/README.md`](../data-event-architecture/README.md) | 12 | 6 — Orchestration and production architecture | Authoritative · P3 normalized |
| 14 | Open-Source and Local AI | [`open-source-local-ai/README.md`](../open-source-local-ai/README.md) | 11 | 7 — Open models, fine-tuning and infrastructure | Authoritative · P3 normalized |
| 15 | Fine-Tuning and Specialist Models | [`fine-tuning-specialist-models/README.md`](../fine-tuning-specialist-models/README.md) | 10 | 7 — Open models, fine-tuning and infrastructure | Authoritative · P3 normalized |
| 16 | GPU and Inference Infrastructure | [`gpu-inference-infrastructure/README.md`](../gpu-inference-infrastructure/README.md) | 10 | 7 — Open models, fine-tuning and infrastructure | Authoritative · P3 normalized |
| 17 | MLOps and LLMOps | [`mlops-llmops/README.md`](../mlops-llmops/README.md) | 10 | 7 — Open models, fine-tuning and infrastructure | Authoritative · P3 normalized |
| 18 | Multimodal AI | [`multimodal-ai/README.md`](../multimodal-ai/README.md) | 10 | 8 — Multimodal and interface agents | Authoritative · P3 normalized |
| 19 | Computer Use and Interface Agents | [`computer-use-interface-agents/README.md`](../computer-use-interface-agents/README.md) | 10 | 8 — Multimodal and interface agents | Authoritative · P3 normalized |
| 20 | Physical AI and Robotics | [`physical-ai-robotics/README.md`](../physical-ai-robotics/README.md) | 10 | 8 — Multimodal and interface agents | Authoritative · P3 normalized |
| 21 | AI Economics and Model Routing | [`ai-economics-model-routing/README.md`](../ai-economics-model-routing/README.md) | 10 | 6 — Orchestration and production architecture | Authoritative · P3 normalized |
| 22 | Enterprise AI | [`enterprise-ai/README.md`](../enterprise-ai/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 23 | AI Product Design | [`ai-product-design/README.md`](../ai-product-design/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 24 | Business Automation | [`business-automation/README.md`](../business-automation/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 25 | Decision Intelligence | [`decision-intelligence/README.md`](../decision-intelligence/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 26 | Domain-Specific AI Systems | [`domain-specific-ai-systems/README.md`](../domain-specific-ai-systems/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 27 | AI-Native Commerce and Operations | [`ai-native-commerce-operations/README.md`](../ai-native-commerce-operations/README.md) | 10 | 9 — Decision intelligence and AI-native business systems | Authoritative · P3 normalized |
| 28 | Build an AI Operating System | [`ai-operating-system/README.md`](../ai-operating-system/README.md) | 10 | 10 — Capstone: AI operating system | Authoritative · P3 normalized |

## Repository hardening context

The curriculum-status matrix is separate from repository release readiness. P1 restored the authoritative domain structure, P2 consolidated legacy/supplemental content, and P3 normalized the curriculum. P4 improves navigation and contributor experience. Release engineering remains a separate P5 gate.

See:

- [Master Roadmap](./master-roadmap.md)
- [Prerequisites and Recommended Paths](./prerequisites-and-paths.md)
- [Assessment Model](./assessment-model.md)
- [v1.0 Repository Audit and Hardening Plan](../docs/v1-repository-audit-and-hardening.md)
