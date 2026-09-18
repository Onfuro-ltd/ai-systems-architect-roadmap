# Legacy and Supplemental Content Map

This document records the P2 chapter-by-chapter classification of legacy, overlapping and supplemental curriculum.

It exists so content can be removed from authoritative navigation without losing traceability.

## 1. Archived combined MCP / skills track

Archived location: `archive/legacy/mcp-skills-tools/`

| Archived chapter | Authoritative destination |
| --- | --- |
| `01-what-is-mcp.md` | Domain 07 — `01-mcp-foundations.md` |
| `02-tool-protocols.md` | Domain 07 — `03-clients-servers-and-transports.md`, `04-tool-contracts-schemas-and-discovery.md` |
| `03-skills-and-capabilities.md` | Domain 06 — `01-skills-and-capabilities.md` |
| `04-agent-harnesses.md` | Domain 06 — `04-agent-harness-architecture.md` |
| `05-context-management.md` | Domain 06 — `03-context-engineering-for-skills.md`; conceptual boundary also clarified by Domain 08 |
| `06-tool-security.md` | Domain 07 — MCP-specific trust; Domain 11 — `05-agent-and-tool-security.md` |
| `07-mcp-architecture.md` | Domain 07 — `01-mcp-foundations.md`, `03-clients-servers-and-transports.md` |
| `08-enterprise-tool-ecosystems.md` | Domain 07 — `08-enterprise-capability-ecosystems.md` |
| `09-capstone.md` | Split into Domain 06 and Domain 07 capstones |
| `README.md` | Replaced by independent Domain 06 and Domain 07 READMEs |

## 2. Archived security and governance track

Archived location: `archive/legacy/ai-security-governance/`

| Archived chapter | Authoritative destination |
| --- | --- |
| `01-ai-threat-modelling.md` | Domain 11 — `01-ai-threat-modelling.md` |
| `02-ai-identity-and-access-control.md` | Domain 11 — `02-identity-least-privilege-and-capabilities.md` |
| `03-prompt-injection-defence.md` | Domain 11 — `03-prompt-injection-and-untrusted-content.md` |
| `04-data-security-and-privacy.md` | Domain 11 — `04-data-security-privacy-and-isolation.md` |
| `05-agent-security.md` | Domain 11 — `05-agent-and-tool-security.md` |
| `06-ai-safety-engineering.md` | Reliability material maps to Domain 10; action/security controls map to Domain 11 |
| `07-governance-frameworks.md` | Domain 11 — `08-audit-incident-response-and-governance.md` |
| `09-capstone.md` | Domain 11 — `09-capstone.md` |
| `README.md` | Replaced by Domain 11 README |

## 3. Archived open-source models and infrastructure track

Archived location: `archive/legacy/open-source-models-infrastructure/`

| Archived chapter | Authoritative destination |
| --- | --- |
| `01-open-source-ai-models.md` | Domain 14 — Open-Source and Local AI |
| `02-model-hosting-and-inference.md` | Domains 14 and 16 |
| `03-gpu-infrastructure.md` | Domain 16 — GPU and Inference Infrastructure |
| `04-fine-tuning-fundamentals.md` | Domain 15 — Fine-Tuning and Specialist Models |
| `05-lora-and-parameter-efficient-training.md` | Domain 15 — LoRA and QLoRA |
| `06-data-preparation.md` | Domain 15 — dataset design and data quality |
| `07-evaluation-and-model-selection.md` | Domain 15 evaluation; general evaluation principles in Domain 10 |
| `08-enterprise-ai-infrastructure.md` | Domain 16 production infrastructure; enterprise operating concerns also connect to Domain 22 |
| `09-capstone.md` | Superseded by the separate Domain 14, 15 and 16 capstones |
| `README.md` | Replaced by independent Domain 14–16 READMEs |

## 4. Supplemental AI product engineering and commercialisation

Supplemental location: `supplemental/ai-product-engineering-commercialisation/`

This material remains intentionally available because commercialisation, pricing, enterprise sales and company-building are not fully represented by one authoritative architecture domain.

| Supplemental chapter | Relationship to authoritative roadmap |
| --- | --- |
| `01-ai-product-strategy.md` | Extends Domain 23 — AI Product Design |
| `02-identifying-valuable-ai-problems.md` | Extends Domain 23 |
| `03-ai-mvp-design.md` | Extends Domain 23 |
| `04-user-research-and-validation.md` | Extends Domain 23 |
| `05-ai-saas-architecture.md` | Crosses Domains 12 and 23 |
| `06-ai-unit-economics.md` | Extends Domain 21 — AI Economics and Model Routing |
| `07-pricing-ai-products.md` | Supplemental commercial pricing; adjacent to Domain 21 |
| `08-enterprise-ai-sales.md` | Supplemental go-to-market material; adjacent to Domain 22 — Enterprise AI |
| `09-building-ai-companies.md` | Supplemental company-building material |
| `10-capstone.md` | Supplemental commercialisation capstone |
| `README.md` | Supplemental track navigation |

## 5. Domain 18 multimodal consolidation

Canonical location: `multimodal-ai/`

The ten-chapter structure introduced on 18 September 2026 is canonical after P2. The earlier nine-chapter structure is preserved at `archive/legacy/multimodal-ai-pre-p2/` because several chapters contain richer explanatory material worth reviewing during P3.

| Archived pre-P2 chapter | Canonical destination |
| --- | --- |
| `01-what-is-multimodal-ai.md` | `01-multimodal-foundations-and-architecture.md` |
| `02-vision-models.md` | `02-vision-and-image-understanding.md` |
| `03-image-understanding.md` | `02-vision-and-image-understanding.md` and `06-document-intelligence.md` |
| `04-image-generation.md` | `03-image-generation-and-editing-systems.md` |
| `05-video-generation.md` | `05-video-intelligence-and-generation.md` |
| `06-audio-and-speech.md` | `04-audio-and-speech-systems.md` |
| `07-multimodal-agents.md` | `07-multimodal-context-fusion-and-routing.md`; agent execution concepts remain in Domains 05/09/19 |
| `08-enterprise-multimodal-systems.md` | `08-multimodal-evaluation-safety-and-security.md` and `09-production-multimodal-infrastructure.md` |
| `09-capstone.md` | `10-multimodal-ai-capstone.md` |

## P2 authority rule

- `archive/legacy/` preserves historical curriculum and migration sources.
- `supplemental/` contains useful non-authoritative extensions.
- the [Authoritative Domain Directory Map](../roadmap/domain-directory-map.md) remains the canonical map for the 28 domains.
- archived material must not be linked as the primary curriculum from root or master-roadmap navigation.
