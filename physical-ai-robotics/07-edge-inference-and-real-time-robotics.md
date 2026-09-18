# 07 — Edge Inference and Real-Time Robotics

## Purpose

Place computation according to latency, connectivity, privacy, power and safety requirements.

## Timing classes

Separate hard/firm real-time control from soft real-time perception and higher-latency semantic reasoning.

Do not place a network-dependent LLM in a loop whose missed deadline can create unsafe motion.

## Edge vs cloud

```text
On-device: control, immediate safety, latency-critical perception
Edge/local: heavier perception, fleet-local services
Cloud: expensive semantic reasoning, analytics, training, noncritical planning
```

Actual placement depends on the system.

## Connectivity

Design safe behaviour for high latency, packet loss and complete disconnection. Local safety must remain effective without cloud access.

## Compute constraints

Robots have limited power, thermal envelope, memory and accelerator capacity. Quantization and specialist models may be necessary.

## Scheduling

Prioritize safety/control and critical perception over nonessential AI workloads.

## Updates

Model/software updates need compatibility checks, staged rollout, rollback and protection against interrupting active safety-critical tasks.

## Exercise

Partition a robot AI stack across real-time controller, onboard accelerator, facility edge server and cloud.

## Takeaway

> Put computation where its deadline and failure consequences require it; cloud intelligence must never become a single point of physical safety.

Next: **08 — Safety, Human Oversight and Governance**.
