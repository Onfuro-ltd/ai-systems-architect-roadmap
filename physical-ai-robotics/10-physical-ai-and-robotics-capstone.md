# 10 — Physical AI and Robotics Capstone

## Purpose

Design an enterprise embodied-AI platform that can perceive, plan and act while keeping physical safety independent of probabilistic model behaviour.

## Scenario

A fleet of mobile manipulators moves objects in facilities shared with people. Semantic AI interprets tasks and unfamiliar objects; deterministic robotics components handle localization, motion, control and safety.

## Target architecture

```text
Human / operational intent
          ↓
Identity + authority
          ↓
Task orchestrator
          ↓
Embodied / semantic model
          ↓
Bounded skill or goal proposal
          ↓
World-state validation
          ↓
Deterministic safety supervisor
          ↓
Motion planner
          ↓
Real-time controller
          ↓
Actuators → physical world → sensors
          ↑                       ↓
          └──── state estimate ───┘
```

## Required deliverables

Produce operating-domain definition; task/skill catalogue; sensor architecture; calibration/time-sync plan; state-estimation design; localization/map/world-model architecture; coordinate-frame contract; motion/control boundaries; embodied-model interface; action constraints; simulation and scenario library; sim-to-real promotion; edge/cloud partition; connectivity-loss behaviour; real-time priority model; human approval/takeover design; hazard analysis; emergency-stop/safety architecture; cybersecurity threat model; fleet identity/control plane; telemetry and privacy policy; evaluation suite; critical safety metrics; staged deployment/rollback; maintenance/calibration plan; incident evidence model; failure matrix; and at least three ADRs.

## Failure matrix

Cover sensor failure, bad calibration, localization drift, stale map, perception hallucination, human entering workspace, object shift, planning failure, controller fault, actuator fault, network loss, cloud outage, overheated/overloaded edge compute, compromised command channel, bad model update, battery/power issue, simulation mismatch and failed emergency recovery.

## Acceptance criteria

The design passes only if semantic AI cannot bypass physical safety constraints; hard real-time control does not depend on cloud/model latency; uncertainty is represented; coordinate frames and calibration are explicit; stale world state is detectable; physical preconditions are checked; safety remains local during network loss; the operating domain is bounded; emergency controls are independent; field failures become regression scenarios; fleet updates are staged and reversible; sensitive sensor retention is minimized; and verified physical outcomes—not demo quality—determine success.

## Final principle

> Physical autonomy should increase only as evidence, verification and independent safety controls increase with it.

**Domain 20 — Physical AI and Robotics complete.**

Next domain: **21 — AI Economics and Model Routing**.
