# 05 — Vision-Language-Action and Embodied Models

## Purpose

Understand models that connect language and perception to robot actions without treating them as complete safety systems.

## Embodied models

Vision-language-action and related models can map observations and instructions to action representations, plans, waypoints, skills or control-relevant outputs.

## Action abstraction

Prefer bounded skills or motion goals over unrestricted low-level actuation where architecture permits.

```text
Model → select skill / target pose / bounded plan → deterministic safety + controller
```

## Training data

Embodied data can include demonstrations, teleoperation, trajectories, images/video, robot state, language annotations and simulation.

Data distribution strongly determines what the model can generalize to.

## Distribution shift

New objects, lighting, environments, robot hardware and human behaviour can move outside training experience.

Use uncertainty, operating-domain constraints and fallback.

## Foundation-model role

Large models can improve semantic task decomposition and generalization, while specialist perception/control often remains necessary.

## Verification

Before execution, check action bounds, collision/safety constraints, authority and current state. After execution, verify physical outcome.

## Exercise

Design an embodied model interface that can request approved manipulation skills but cannot directly command arbitrary joint torques.

## Takeaway

> Embodied foundation models can broaden robot capability, but their outputs should enter a constrained robotics stack rather than bypass it.

Next: **06 — Simulation, Digital Twins and Synthetic Environments**.
