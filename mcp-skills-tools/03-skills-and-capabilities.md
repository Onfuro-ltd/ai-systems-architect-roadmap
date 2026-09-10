# 03 — Skills and Capabilities

## Overview

AI skills are reusable capability packages that help AI systems perform specialised tasks consistently.

A skill is not simply a long prompt renamed with a new label. A useful skill combines:

- instructions;
- domain knowledge;
- workflows;
- tool usage guidance;
- validation rules;
- expected outputs.

## Core Principle

> Skills should package repeatable expertise, not just instructions.

## Skill Architecture

```
User Goal
   |
   ↓
Skill Selection
   |
   ↓
Instructions + Knowledge + Tools
   |
   ↓
Execution
   |
   ↓
Validation
```

## Skills vs Prompts

A prompt:

- tells a model what to do once;
- usually has limited structure;
- often depends on the user.

A skill:

- is reusable;
- has defined inputs and outputs;
- can be tested;
- can be version controlled;
- can become part of an agent system.

## Skills vs Agents

A skill provides capability.

An agent decides when and how to use capabilities.

```
Agent
  |
  +-- Skill: Analyse Data
  |
  +-- Skill: Generate Report
  |
  +-- Skill: Review Policy
```

## Enterprise Skill Design

Good skills require:

- clear purpose;
- ownership;
- versioning;
- permissions;
- evaluation tests;
- documentation.

## HumanScope Example

HumanScope is a good example of a specialised AI behaviour layer.

However, it should only be applied when the task benefits from human-style communication, judgement, or explanation.

Not every AI operation needs the same style layer.

## SEMLIS Application

Future SEMLIS skills could include:

- Amazon Listing Analysis;
- Profit Investigation;
- VAT Review;
- Customer Complaint Analysis;
- Inventory Forecasting.

Skills become reusable business intelligence components.
