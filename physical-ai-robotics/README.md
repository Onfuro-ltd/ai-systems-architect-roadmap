# Domain 20 — Physical AI and Robotics

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across robotics, perception, localisation, planning, control, embodied models, simulation, real-time inference, safety and fleet operations.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Physical AI closes the loop between perception, reasoning and action in the real world. Errors can damage equipment or injure people, so safety cannot depend on model judgement alone.

> An embodied model may propose behaviour. A safety-rated control architecture decides what the machine is physically allowed to do.

## Domain structure

01 Physical AI and Robotics Foundations  
02 Sensors, Perception and State Estimation  
03 Localization, Mapping and World Models  
04 Planning, Control and Actuation  
05 Vision-Language-Action and Embodied Models  
06 Simulation, Digital Twins and Synthetic Environments  
07 Edge Inference and Real-Time Robotics  
08 Safety, Human Oversight and Governance  
09 Robotics Infrastructure, Fleet Operations and Evaluation  
10 Physical AI and Robotics Capstone

## Core architecture

```text
Human / system intent
        ↓
Task planner / embodied model
        ↓
World state + uncertainty
        ↓
Policy / safety supervisor
        ↓
Motion / control planner
        ↓
Real-time controller
        ↓
Actuators
        ↓
Physical world
        ↓
Sensors
        └──────── feedback ────────┘
```

## Principles

1. Separate semantic reasoning from safety-critical control.
2. Never let an LLM directly define hard real-time safety.
3. Maintain explicit state and uncertainty.
4. Verify physical preconditions before action.
5. Enforce workspace, speed, force and authority limits outside the model.
6. Simulate before risky deployment.
7. Design fail-safe and emergency-stop paths independently.
8. Treat sensors and remote commands as potentially faulty/untrusted.
9. Evaluate complete closed-loop behaviour.
10. Preserve human authority over consequential physical actions.

## Takeaway

> Physical AI is where probabilistic intelligence meets irreversible reality; deterministic safety boundaries must become stronger as physical consequence increases.

Next: **01 — Physical AI and Robotics Foundations**.

## Canonical curriculum navigation

- [Physical AI and Robotics Foundations](./01-physical-ai-and-robotics-foundations.md)
- [Sensors, Perception and State Estimation](./02-sensors-perception-and-state-estimation.md)
- [Localization, Mapping and World Models](./03-localization-mapping-and-world-models.md)
- [Planning, Control and Actuation](./04-planning-control-and-actuation.md)
- [Vision-Language-Action and Embodied Models](./05-vision-language-action-and-embodied-models.md)
- [Simulation, Digital Twins and Synthetic Environments](./06-simulation-digital-twins-and-synthetic-environments.md)
- [Edge Inference and Real-Time Robotics](./07-edge-inference-and-real-time-robotics.md)
- [Safety, Human Oversight and Governance](./08-safety-human-oversight-and-governance.md)
- [Robotics Infrastructure, Fleet Operations and Evaluation](./09-robotics-infrastructure-fleet-operations-and-evaluation.md)
- [Physical AI and Robotics Capstone](./10-physical-ai-and-robotics-capstone.md)
