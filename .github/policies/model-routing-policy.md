# Model Routing Policy

Status: active
Owner: orchestrator governance
Version: 1.0.0

Reference source:
- .github/instructions/agent-model-routing.instructions.md

## Baseline
- Each agent has a default model profile.
- Orchestrator may override profile per invocation.
- Overrides must be auditable.

## Required audit fields
- default_model_profile
- selected_model_profile
- override_reason
