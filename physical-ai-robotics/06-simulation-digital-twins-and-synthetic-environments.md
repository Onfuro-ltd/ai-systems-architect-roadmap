# 06 — Simulation, Digital Twins and Synthetic Environments

## Purpose

Use simulated environments to develop, train and evaluate physical AI before exposing people or equipment to unnecessary risk.

## Simulation roles

Simulation supports algorithm development, reinforcement/imitation learning, synthetic data, scenario testing, regression, rare-event testing and capacity planning.

## Sim-to-real gap

Physics, friction, lighting, materials, sensor noise, actuator response and human behaviour are never perfectly simulated.

Success in simulation is evidence, not proof of real-world safety.

## Domain randomization

Vary textures, lighting, geometry, noise, dynamics and other parameters to reduce dependence on one synthetic environment.

## Digital twins

A digital twin may represent a specific facility, machine or process using synchronized operational data. Define which state is authoritative and how stale twin data is detected.

## Scenario library

Version normal, edge, adversarial and failure scenarios so releases can be compared against the same test suite.

## Hardware-in-the-loop

Where useful, combine simulated environment components with real controllers/sensors/hardware to expose integration failures earlier.

## Exercise

Design a simulation-to-real promotion process for a mobile manipulator, including scenarios that must still be tested physically.

## Takeaway

> Simulation expands testing safely and cheaply, but real-world validation remains a separate gate.

Next: **07 — Edge Inference and Real-Time Robotics**.
