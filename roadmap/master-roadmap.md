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

### 01 — AI foundations
AI history, machine learning, neural networks, transformers, attention, tokens, embeddings, training, inference, scaling and the evolution of foundation models.

### 02 — Modern foundation models
Model families, reasoning models, mixture-of-experts, context windows, multimodality, model capabilities, limitations and model selection.

### 03 — AI application engineering
Prompt/instruction design, structured outputs, function calling, tool use, streaming, state, retries, deterministic boundaries and production API integration.

### 04 — Knowledge systems and RAG
Embeddings, retrieval, chunking, ranking, hybrid search, vector stores, grounding, citations, knowledge freshness, access control and retrieval evaluation.

### 05 — Agents
Agent loops, planning, execution, observation, recovery, tool selection, autonomy boundaries, failure modes and long-horizon work.

### 06 — Skills and agent harnesses
Reusable skills, rules, hooks, context engineering, coding-agent harnesses, lifecycle controls, quality gates and portable operating knowledge.

### 07 — MCP and tool ecosystems
Model Context Protocol, clients, servers, tools, resources, authentication, authorization, schemas, tool discovery and safe enterprise integration.

### 08 — Memory systems
Working, episodic, semantic and procedural memory; retrieval, summarisation, consolidation, forgetting, staleness, privacy and memory evaluation.

### 09 — Orchestration and multi-agent systems
Workflow orchestration, specialist agents, delegation, event-driven coordination, parallelism, model routing, consensus, validation and when not to use multiple agents.

### 10 — Evaluation and reliability
Task suites, golden datasets, regression tests, human evaluation, model-as-judge limitations, tool-use evaluation, hallucination measurement, cost-per-success and production monitoring.

### 11 — Security, permissions and governance
Identity, least privilege, secrets, sandboxing, policy engines, approval gates, prompt injection, data exfiltration, auditability, incident response and AI governance.

### 12 — AI system design
Service boundaries, synchronous vs asynchronous execution, queues, workflow engines, state machines, fault tolerance, caching, idempotency, scalability and graceful degradation.

### 13 — Data and event architecture
Operational databases, warehouses, streams, event buses, CDC, data contracts, lineage, quality, tenancy and feedback data for AI systems.

### 14 — Open-source and local AI
Open-weight models, licensing, quantisation, GGUF, llama.cpp, vLLM, serving, privacy, deployment trade-offs and local/edge inference.

### 15 — Fine-tuning and specialist models
Dataset design, SFT, LoRA/QLoRA, preference optimisation, distillation, synthetic data, evaluation, adapter lifecycle and deciding when fine-tuning is inappropriate.

### 16 — GPU and inference infrastructure
GPU architecture, VRAM, memory bandwidth, batching, KV cache, parallelism, inference servers, cloud GPUs, owned hardware, utilisation and cost engineering.

### 17 — MLOps and LLMOps
Experiment tracking, model/version management, deployment, observability, rollback, evaluation pipelines, data/model drift and operational governance.

### 18 — Multimodal AI
Vision, image understanding/editing/generation, audio, speech, video, document intelligence and multimodal system design.

### 19 — Computer use and interface agents
Browser and desktop control, perception/action loops, accessibility trees, visual interaction, verification, sandboxing and reliability limits.

### 20 — Physical AI and robotics
Embodied models, perception, planning, control, simulation, edge inference, safety and the boundary between digital and physical agents.

### 21 — AI economics and model routing
Token economics, latency, caching, model tiers, routing, fallback, specialist models, quality/cost frontiers and cost per successful outcome.

### 22 — Enterprise AI
Identity, tenancy, data residency, compliance, procurement, integration, governance, change management and operating AI across organisations.

### 23 — AI product design
Human-AI interaction, uncertainty, approvals, trust, explainability, progressive autonomy, user control and designing products around capabilities rather than demos.

### 24 — Business automation
Workflow discovery, process decomposition, tool-enabled automation, exception handling, human-in-the-loop operations and measuring automation value.

### 25 — Decision intelligence
Signals, forecasts, recommendations, confidence, constraints, business rules, causal thinking, optimisation, explanations and outcome feedback.

### 26 — Domain-specific AI systems
Turning domain knowledge, proprietary data, workflows, policies and evaluations into durable AI capability without unnecessarily coupling to one model vendor.

### 27 — AI-native commerce and operations
Commerce is one practical domain for applying the architecture: inventory, pricing, advertising, catalogue quality, customer operations, forecasting, finance, reconciliation and marketplace workflows.

### 28 — Build an AI operating system
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
