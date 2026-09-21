# AI Systems Architect Roadmap

## Mission

Develop the judgement and practical capability required to design, build, evaluate and operate AI-native systems.

This roadmap is not a checklist of fashionable tools. It is a progression from understanding models to architecting reliable systems that combine models, data, knowledge, tools, memory, workflows, security, evaluation and measurable outcomes.

## The four mastery lenses

Every domain is studied through four lenses:

1. **Understand** — explain the concepts, mechanisms, terminology and trade-offs.
2. **Build** — implement a working version and observe real failure modes.
3. **Architect** — choose appropriate patterns, boundaries, controls and technologies for production systems.
4. **Lead** — define standards, evaluate alternatives, govern risk and guide teams through change.

## Learning domains


> **Authoritative homes:** The linked headings below point to the canonical curriculum location for each domain. Domains 01 and 02 intentionally share the `foundations/` curriculum; Domains 06–11 use the dedicated P1 authoritative tracks. See [Domain Directory Map](./domain-directory-map.md) for the full mapping and legacy-track status.

### [01 — AI Foundations](../foundations/README.md)
AI history, machine learning, neural networks, transformers, attention, tokens, embeddings, training, inference, scaling and the evolution of foundation models.

### [02 — Modern Foundation Models](../foundations/README.md)
Model families, reasoning models, mixture-of-experts, context windows, multimodality, model capabilities, limitations and model selection.

### [03 — AI Application Engineering](../application-engineering/README.md)
Prompt/instruction design, structured outputs, function calling, tool use, streaming, state, retries, deterministic boundaries and production API integration.

### [04 — Knowledge Systems and RAG](../knowledge-systems-rag/README.md)
Embeddings, retrieval, chunking, ranking, hybrid search, vector stores, grounding, citations, knowledge freshness, access control and retrieval evaluation.

### [05 — Agents](../agents/README.md)
Agent loops, planning, execution, observation, recovery, tool selection, autonomy boundaries, failure modes and long-horizon work.

### [06 — Skills and Agent Harnesses](../06-skills-agent-harnesses/README.md)
Reusable skills, rules, hooks, context engineering, coding-agent harnesses, lifecycle controls, quality gates and portable operating knowledge.

### [07 — MCP and Tool Ecosystems](../07-mcp-tool-ecosystems/README.md)
Model Context Protocol, clients, servers, tools, resources, authentication, authorization, schemas, tool discovery and safe enterprise integration.

### [08 — Memory Systems](../08-memory-systems/README.md)
Working, episodic, semantic and procedural memory; retrieval, summarisation, consolidation, forgetting, staleness, privacy and memory evaluation.

### [09 — Orchestration and Multi-Agent Systems](../09-orchestration-multi-agent/README.md)
Workflow orchestration, specialist agents, delegation, event-driven coordination, parallelism, model routing, consensus, validation and when not to use multiple agents.

### [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md)
Task suites, golden datasets, regression tests, human evaluation, model-as-judge limitations, tool-use evaluation, hallucination measurement, cost-per-success and production monitoring.

### [11 — Security, Permissions and Governance](../11-security-permissions-governance/README.md)
Identity, least privilege, secrets, sandboxing, policy engines, approval gates, prompt injection, data exfiltration, auditability, incident response and AI governance.

### [12 — AI System Design](../ai-system-design/README.md)
Service boundaries, synchronous vs asynchronous execution, queues, workflow engines, state machines, fault tolerance, caching, idempotency, scalability and graceful degradation.

### [13 — Data and Event Architecture](../data-event-architecture/README.md)
Operational databases, warehouses, streams, event buses, CDC, data contracts, lineage, quality, tenancy and feedback data for AI systems.

### [14 — Open-Source and Local AI](../open-source-local-ai/README.md)
Open-weight models, licensing, quantisation, GGUF, llama.cpp, vLLM, serving, privacy, deployment trade-offs and local/edge inference.

### [15 — Fine-Tuning and Specialist Models](../fine-tuning-specialist-models/README.md)
Dataset design, SFT, LoRA/QLoRA, preference optimisation, distillation, synthetic data, evaluation, adapter lifecycle and deciding when fine-tuning is inappropriate.

### [16 — GPU and Inference Infrastructure](../gpu-inference-infrastructure/README.md)
GPU architecture, VRAM, memory bandwidth, batching, KV cache, parallelism, inference servers, cloud GPUs, owned hardware, utilisation and cost engineering.

### [17 — MLOps and LLMOps](../mlops-llmops/README.md)
Experiment tracking, model/version management, deployment, observability, rollback, evaluation pipelines, data/model drift and operational governance.

### [18 — Multimodal AI](../multimodal-ai/README.md)
Vision, image understanding/editing/generation, audio, speech, video, document intelligence and multimodal system design.

### [19 — Computer Use and Interface Agents](../computer-use-interface-agents/README.md)
Browser and desktop control, perception/action loops, accessibility trees, visual interaction, verification, sandboxing and reliability limits.

### [20 — Physical AI and Robotics](../physical-ai-robotics/README.md)
Embodied models, perception, planning, control, simulation, edge inference, safety and the boundary between digital and physical agents.

### [21 — AI Economics and Model Routing](../ai-economics-model-routing/README.md)
Token economics, latency, caching, model tiers, routing, fallback, specialist models, quality/cost frontiers and cost per successful outcome.

### [22 — Enterprise AI](../enterprise-ai/README.md)
Identity, tenancy, data residency, compliance, procurement, integration, governance, change management and operating AI across organisations.

### [23 — AI Product Design](../ai-product-design/README.md)
Human-AI interaction, uncertainty, approvals, trust, explainability, progressive autonomy, user control and designing products around capabilities rather than demos.

### [24 — Business Automation](../business-automation/README.md)
Workflow discovery, process decomposition, tool-enabled automation, exception handling, human-in-the-loop operations and measuring automation value.

### [25 — Decision Intelligence](../decision-intelligence/README.md)
Signals, forecasts, recommendations, confidence, constraints, business rules, causal thinking, optimisation, explanations and outcome feedback.

### [26 — Domain-Specific AI Systems](../domain-specific-ai-systems/README.md)
Turning domain knowledge, proprietary data, workflows, policies and evaluations into durable AI capability without unnecessarily coupling to one model vendor.

### [27 — AI-Native Commerce and Operations](../ai-native-commerce-operations/README.md)
Commerce is one practical domain for applying the architecture: inventory, pricing, advertising, catalogue quality, customer operations, forecasting, finance, reconciliation and marketplace workflows.

### [28 — Build an AI Operating System](../ai-operating-system/README.md)
Integrate the preceding domains into a model-independent platform containing model routing, agents, skills, memory, knowledge, MCP/tools, orchestration, permissions, evaluation, observability and feedback loops.

## Capstone architecture

```text
                         HUMAN INTENT
                              |
                              v
                       ORCHESTRATION
                              |
                       MODEL ROUTER
                 _________|_________
                |         |         |
             Frontier  Efficient  Specialist
                |         |         |
                +---------+---------+
                          |
                  AGENTS / WORKFLOWS
                          |
          +---------------+---------------+
          |               |               |
        Skills          Memory         Knowledge
          |               |               |
          +---------------+---------------+
                          |
                      MCP / TOOLS
                          |
                 POLICY & PERMISSIONS
                          |
                  BUSINESS SYSTEMS
                          |
                        EVENTS
                          |
                       OUTCOMES
                          |
                     EVALUATION
                          |
                       LEARNING
                          |
                          +------> system improvement
```

Security, observability, auditability, cost control, data governance and human control surround every layer.

## What completion means

Completion does not mean reading every page or memorising every framework. A learner should be able to:

- explain the major architectural choices and their trade-offs;
- build representative implementations rather than tutorial-only demos;
- identify failure and security modes before production deployment;
- select models and tools based on measured requirements;
- design evaluation and feedback before increasing autonomy;
- separate durable architecture from replaceable vendors;
- design AI systems whose success can be measured against real outcomes.

The roadmap is intentionally living. Technologies will move between the project's Technology Radar categories as evidence, maturity and architecture evolve.
