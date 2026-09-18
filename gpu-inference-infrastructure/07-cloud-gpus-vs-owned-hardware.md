# 07 — Cloud GPUs vs Owned Hardware

## Purpose

Cloud, rented and owned accelerators are financing and operating models as much as hardware choices. Compare them using demand shape, utilisation, control, reliability and total lifecycle cost.

## Learning outcomes

By the end of this module, you should be able to:
- build a cloud-versus-owned TCO model
- reason about utilisation and demand volatility
- include facilities, staffing, spares and capacity risk in owned-hardware economics
- design a hybrid decision that preserves workload portability

## Cloud/rented capacity

Advantages can include fast provisioning, elasticity, hardware variety and regional choice. Costs include hourly rates, idle reservations, storage/network, quota scarcity and provider dependence.

## Owned capacity

Advantages can include control, predictable access and strong economics at sustained utilisation. Costs include capital, power, cooling, facilities, networking, maintenance, spares, staffing and refresh cycles.

## Utilisation

An idle owned accelerator can have poor cost per useful task. A highly utilised stable workload may justify ownership. Use realistic demand rather than theoretical 100% utilisation.

## Capacity risk

Cloud capacity can be unavailable when needed; owned capacity can fail or become obsolete. Model both forms of risk.

## Hybrid architecture

A model router can direct eligible workloads among hosted APIs, rented GPUs and private capacity according to policy, capability and economics.

## Decision horizon

Hardware decisions span years while model/runtime efficiency changes quickly. Include option value and refresh risk.

## Failure modes

- comparing only purchase price with hourly rental
- assuming owned hardware will remain highly utilised
- ignoring cloud capacity/quota constraints
- ignoring power/cooling/network/facility limits
- business logic tied to one hardware provider

## Security and governance

Private hardware does not automatically make a workload compliant, and cloud does not automatically make it insecure. Evaluate identity, encryption, residency, access, logging and vendor contracts separately.

## Economics and operations

Use cost per successful outcome across a realistic horizon. Include financing/depreciation, utilisation, engineering, downtime, support and expected refresh—not just GPU price.

## Practical exercise

Build a three-year scenario for variable demand. Compare hosted API, rented GPU and owned capacity under low/base/high utilisation and one major hardware failure.

## Architect checklist

- [ ] TCO includes facilities and people
- [ ] demand variability is modelled
- [ ] capacity failure/shortage is included
- [ ] quality and SLOs are held constant across options
- [ ] application portability is preserved

## Primary reading

- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)
- [NVIDIA CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)

## Mastery gate

Explain when **Cloud GPUs vs Owned Hardware** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Hardware ownership is justified by sustained workload economics and control requirements, not by avoiding an API bill in isolation.

Next: **08 — Capacity, Utilisation and Cost Engineering**.
