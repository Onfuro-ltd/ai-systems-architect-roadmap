# 06 — Inference Servers, Scheduling and Admission Control

## Purpose

An inference server turns model execution into a shared service. The production architecture also needs authentication, admission control, routing, observability and backpressure.

## Learning outcomes

By the end of this module, you should be able to:
- separate model server responsibilities from gateway/business policy
- explain request lifecycle through admission, queue, scheduler and worker
- design safe overload and cancellation behaviour
- compare serving runtimes using representative workloads and portability requirements

## Reference path

A practical path is `client -> auth/quota -> router -> admission -> scheduler -> inference worker -> stream/result -> telemetry`. The model server should not own unrelated business state.

## Admission control

Reject, defer or route work that cannot safely meet resource/SLO limits. Accepting every request is not graceful degradation.

## Scheduling

Schedulers balance active sequences, memory occupancy, priority and batching opportunities. Policies should be observable and testable.

## Streaming

Streaming improves perceived latency but complicates cancellation, partial responses, retries and client disconnect handling.

## Health and readiness

Separate process liveness from ability to serve the intended model/configuration. A process can be alive while model artifacts are missing or capacity is exhausted.

## Portability

Use a canonical application-facing inference contract so runtimes such as vLLM, TensorRT-LLM or hosted APIs remain replaceable.

## Failure modes

- health check says healthy while model is not ready
- admission accepts work that cannot meet SLO
- stream disconnect leads to duplicate retry/side effect
- runtime-specific API leaks into business logic
- queue or scheduler failure becomes a total outage

## Security and governance

Authenticate callers before admission. Keep model-serving credentials narrow, protect administrative endpoints, isolate tenants where necessary, and treat model artifacts/containers as signed or controlled supply-chain inputs.

## Economics and operations

Serving-runtime optimisations matter only when they reduce cost/latency without harming quality or portability. Include engineering cost and vendor/runtime lock-in in the decision.

## Practical exercise

Draw a serving architecture for interactive and background requests. Define authentication, quotas, admission, queue, runtime, telemetry, overload, cancellation and fallback.

## Architect checklist

- [ ] business policy is outside the model server
- [ ] admission rules are measurable
- [ ] health/readiness reflect real serving state
- [ ] runtime can be replaced behind a stable contract
- [ ] overload and cancellation are tested

## Primary reading

- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)
- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)

## Mastery gate

Explain when **Inference Servers, Scheduling and Admission Control** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Production inference is a scheduling and control service around model execution.

Next: **07 — Cloud GPUs vs Owned Hardware**.
