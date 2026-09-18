# Authoritative Domain Directory Map

This file is the canonical repository map from the 28-domain master roadmap to the curriculum directories that currently teach each domain.

The map separates **authoritative curriculum homes** from older combined, overlapping or supplemental tracks. A legacy directory remaining in the repository does not make it authoritative.

## Authoritative domains

| Domain | Name | Authoritative home | Status |
| ---: | --- | --- | --- |
| 01 | AI Foundations | [`foundations/README.md`](../foundations/README.md) | Shared Foundations curriculum home with Domain 02. |
| 02 | Modern Foundation Models | [`foundations/README.md`](../foundations/README.md) | Distinct roadmap domain taught within the shared Foundations curriculum. |
| 03 | AI Application Engineering | [`application-engineering/README.md`](../application-engineering/README.md) | Authoritative curriculum track. |
| 04 | Knowledge Systems and RAG | [`knowledge-systems-rag/README.md`](../knowledge-systems-rag/README.md) | Authoritative curriculum track. |
| 05 | Agents | [`agents/README.md`](../agents/README.md) | Authoritative curriculum track. |
| 06 | Skills and Agent Harnesses | [`06-skills-agent-harnesses/README.md`](../06-skills-agent-harnesses/README.md) | Authoritative P1 track. |
| 07 | MCP and Tool Ecosystems | [`07-mcp-tool-ecosystems/README.md`](../07-mcp-tool-ecosystems/README.md) | Authoritative P1 track. |
| 08 | Memory Systems | [`08-memory-systems/README.md`](../08-memory-systems/README.md) | Authoritative P1 track. |
| 09 | Orchestration and Multi-Agent Systems | [`09-orchestration-multi-agent/README.md`](../09-orchestration-multi-agent/README.md) | Authoritative P1 track. |
| 10 | Evaluation and Reliability | [`10-evaluation-reliability/README.md`](../10-evaluation-reliability/README.md) | Authoritative P1 track. |
| 11 | Security, Permissions and Governance | [`11-security-permissions-governance/README.md`](../11-security-permissions-governance/README.md) | Authoritative P1 track. |
| 12 | AI System Design | [`ai-system-design/README.md`](../ai-system-design/README.md) | Authoritative curriculum track. |
| 13 | Data and Event Architecture | [`data-event-architecture/README.md`](../data-event-architecture/README.md) | Authoritative curriculum track. |
| 14 | Open-Source and Local AI | [`open-source-local-ai/README.md`](../open-source-local-ai/README.md) | Authoritative curriculum track. |
| 15 | Fine-Tuning and Specialist Models | [`fine-tuning-specialist-models/README.md`](../fine-tuning-specialist-models/README.md) | Authoritative curriculum track. |
| 16 | GPU and Inference Infrastructure | [`gpu-inference-infrastructure/README.md`](../gpu-inference-infrastructure/README.md) | Authoritative curriculum track. |
| 17 | MLOps and LLMOps | [`mlops-llmops/README.md`](../mlops-llmops/README.md) | Authoritative curriculum track. |
| 18 | Multimodal AI | [`multimodal-ai/README.md`](../multimodal-ai/README.md) | Authoritative curriculum track. |
| 19 | Computer Use and Interface Agents | [`computer-use-interface-agents/README.md`](../computer-use-interface-agents/README.md) | Authoritative curriculum track. |
| 20 | Physical AI and Robotics | [`physical-ai-robotics/README.md`](../physical-ai-robotics/README.md) | Authoritative curriculum track. |
| 21 | AI Economics and Model Routing | [`ai-economics-model-routing/README.md`](../ai-economics-model-routing/README.md) | Authoritative curriculum track. |
| 22 | Enterprise AI | [`enterprise-ai/README.md`](../enterprise-ai/README.md) | Authoritative curriculum track. |
| 23 | AI Product Design | [`ai-product-design/README.md`](../ai-product-design/README.md) | Authoritative curriculum track. |
| 24 | Business Automation | [`business-automation/README.md`](../business-automation/README.md) | Authoritative curriculum track. |
| 25 | Decision Intelligence | [`decision-intelligence/README.md`](../decision-intelligence/README.md) | Authoritative curriculum track. |
| 26 | Domain-Specific AI Systems | [`domain-specific-ai-systems/README.md`](../domain-specific-ai-systems/README.md) | Authoritative curriculum track. |
| 27 | AI-Native Commerce and Operations | [`ai-native-commerce-operations/README.md`](../ai-native-commerce-operations/README.md) | Authoritative curriculum track. |
| 28 | Build an AI Operating System | [`ai-operating-system/README.md`](../ai-operating-system/README.md) | Authoritative curriculum track. |

## Structural notes

### Domains 01 and 02

Domains 01 and 02 intentionally share `foundations/`.

The existing Foundations curriculum covers the fundamental model layer and modern foundation-model concepts, including transformers, context, training/inference, reasoning and test-time compute, mixture-of-experts and multimodal foundations. Domain 02 remains distinct in the architectural roadmap even though it does not require a duplicate root curriculum directory.

### Domains 06–11

P1 restores the authoritative structure for these domains:

- Domain 06 — Skills and Agent Harnesses
- Domain 07 — MCP and Tool Ecosystems
- Domain 08 — Memory Systems
- Domain 09 — Orchestration and Multi-Agent Systems
- Domain 10 — Evaluation and Reliability
- Domain 11 — Security, Permissions and Governance

Each now has a dedicated authoritative curriculum track.

## Legacy and supplemental directories

P2 has classified and relocated the known overlapping tracks:

| Location | Classification | Status |
| --- | --- | --- |
| `archive/legacy/mcp-skills-tools/` | Archived combined source for Domains 06/07/11 | Migration mapped; not authoritative. |
| `archive/legacy/ai-security-governance/` | Archived predecessor to Domains 10/11 | Migration mapped; not authoritative. |
| `archive/legacy/open-source-models-infrastructure/` | Archived combined predecessor to Domains 14–16 | Migration mapped; not authoritative. |
| `supplemental/ai-product-engineering-commercialisation/` | Supplemental commercialisation track | Intentionally retained; not an authoritative domain. |
| `archive/legacy/multimodal-ai-pre-p2/` | Archived pre-P2 Domain 18 chapter structure | Unique detail retained for P3 editorial migration. |

See [`docs/legacy-supplemental-content-map.md`](../docs/legacy-supplemental-content-map.md) for chapter-by-chapter mapping.

## Authority rule

> When curriculum content conflicts or overlaps, the directory listed in the authoritative-domain table above is the canonical home for that domain.

The master roadmap defines scope. This file defines repository location.
