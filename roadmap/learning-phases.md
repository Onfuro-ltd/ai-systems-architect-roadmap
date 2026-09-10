# Learning Phases

The roadmap is broad by design. These phases turn it into an executable learning and building journey.

Each phase combines theory, implementation, architecture and evaluation. Learners should not wait until the end to build systems.

## Phase 0 — Orientation and AI literacy

**Goal:** understand the landscape well enough to distinguish models, applications, agents, infrastructure and hype.

Study:
- AI history and terminology
- machine learning vs generative AI
- transformers, tokens and embeddings
- training vs inference
- model families and multimodality

Build:
- a small model/API playground
- token/context experiments
- a structured comparison of several model classes

Exit gate:
- explain the major concepts without vendor-specific language;
- identify what layer a new AI product actually changes.

## Phase 1 — Reliable AI applications

**Goal:** move from chat prompts to software components.

Study:
- instruction design
- structured outputs
- tool/function calling
- API reliability
- state, retries and validation

Build:
- a structured extraction service
- a tool-using application

Exit gate:
- demonstrate deterministic validation around probabilistic model output.

## Phase 2 — Knowledge and grounding

**Goal:** connect models to trustworthy, current knowledge.

Study:
- embeddings and retrieval
- RAG architectures
- hybrid search and ranking
- citations and provenance
- access-aware retrieval
- retrieval evaluation

Build:
- a cited knowledge assistant
- an evaluation set containing answerable, unanswerable and access-controlled questions

Exit gate:
- explain why retrieval failed and measure whether a change improved it.

## Phase 3 — Agents and tools

**Goal:** understand systems that can pursue goals and take actions.

Study:
- agent loops
- planning and decomposition
- tool discovery and selection
- MCP
- recovery and termination
- autonomy boundaries

Build:
- a read-only operational agent
- an MCP server exposing a narrow safe capability

Exit gate:
- show traces for successful and failed runs and explain why the agent behaved as it did.

## Phase 4 — Skills, memory and harness engineering

**Goal:** make agent behaviour reusable and cumulative.

Study:
- skills and procedural knowledge
- context engineering
- episodic/semantic memory
- hooks and lifecycle controls
- agent harnesses
- memory staleness and security

Build:
- a portable skill
- a retrieval-backed memory prototype
- a harness quality gate

Exit gate:
- demonstrate measurable improvement over a baseline agent rather than assuming the extra machinery helps.

## Phase 5 — Evaluation, security and governance

**Goal:** establish the controls required before meaningful autonomy.

Study:
- golden datasets and regression suites
- prompt injection and tool abuse
- identity and least privilege
- sandboxing and approval gates
- audit logs and incident response
- model and data governance

Build:
- an evaluation harness
- a permissioned action workflow with human approval
- adversarial tests

Exit gate:
- no write-capable agent proceeds to production without explicit permissions, evaluation and rollback design.

## Phase 6 — Orchestration and production architecture

**Goal:** design resilient AI workflows rather than fragile demos.

Study:
- workflow engines and queues
- event-driven architecture
- state machines and idempotency
- multi-agent patterns
- model routing and fallback
- observability and failure recovery

Build:
- a durable multi-step workflow
- a model router
- failure injection tests

Exit gate:
- recover correctly from model, tool, network and workflow failures.

## Phase 7 — Open models, fine-tuning and infrastructure

**Goal:** understand when to own more of the model/inference stack.

Study:
- open-weight deployment
- quantisation and serving
- GPU/VRAM economics
- fine-tuning and adapters
- dataset engineering
- MLOps/LLMOps

Build:
- local/open-model inference
- one narrowly scoped fine-tuning experiment with a baseline comparison

Exit gate:
- justify API vs cloud GPU vs owned infrastructure and RAG vs fine-tuning using evidence.

## Phase 8 — Multimodal and interface agents

**Goal:** extend AI beyond text.

Study:
- vision and documents
- image/video/audio systems
- speech interfaces
- browser/computer use
- verification and multimodal safety

Build:
- a multimodal workflow tied to a real task
- a computer-use experiment in a sandbox

Exit gate:
- quantify reliability and define when direct APIs are preferable to UI automation.

## Phase 9 — Decision intelligence and AI-native business systems

**Goal:** connect AI decisions to measurable organisational outcomes.

Study:
- forecasts and recommendations
- business constraints
- confidence and explanation
- feedback loops
- human decision rights
- cost per successful outcome

Build:
- a decision-support system using real or representative operational data
- outcome tracking that feeds evaluation

Exit gate:
- measure whether the system improves an operational metric, not merely whether users like its prose.

## Phase 10 — Capstone: AI operating system

Integrate:
- model routing
- agents/workflows
- skills
- memory
- knowledge/RAG
- MCP/tools
- policy and permissions
- evaluation
- observability
- outcome feedback

The capstone should be model-independent where practical and designed so individual providers can be replaced without rebuilding the organisation's knowledge and workflow layer.
