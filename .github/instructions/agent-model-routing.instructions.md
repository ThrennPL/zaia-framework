---
applyTo: "**"
---

# ZAIA Agent Model Routing Instructions

## Goal
Define default model assignment per agent and allow orchestrator-controlled model scaling.

## Model Profiles
Use profile labels instead of hardcoding vendor-specific runtime IDs:
- `economy`: low-cost, fast response profile
- `standard`: balanced default profile
- `deep`: high-accuracy, deeper-reasoning profile

Suggested environment mapping:
- `economy` -> {{MODEL_ECONOMY}}
- `standard` -> {{MODEL_STANDARD}}
- `deep` -> {{MODEL_DEEP}}

If placeholders are not configured, use platform defaults with equivalent capability tiers.

## Default Model Profile per Agent
- orchestrator: `standard`
- discovery: `standard`
- requirements: `standard`
- domain: `standard`
- integration: `deep`
- process: `standard`
- backlog: `economy`
- nfr: `deep`
- risk-compliance: `deep`
- quality: `deep`
- knowledge-repository: `economy`

## Orchestrator Model Override Policy
Orchestrator may override agent default profile per task invocation.

1. Downgrade to `economy` when all are true:
- request is low-risk and non-regulatory
- no cross-agent discrepancy expected
- no critical design decision or release gate decision
- expected output is short, non-blocking, and easy to verify

2. Keep `standard` when:
- task is normal analytical work with no critical blockers
- evidence is sufficient and complexity is medium

3. Upgrade to `deep` when any are true:
- compliance, privacy, or regulatory impact exists
- architecture trade-offs or integration conflicts are present
- required confidence threshold >= 0.90
- prior invocation returned low confidence or escalation
- discrepancy round is active or expected

## Cost and Quality Guardrails
- Do not downgrade below required task confidence threshold.
- For Gate-related go/no-go decisions, use at least `standard`; use `deep` for blockers.
- For compliance-heavy scenarios (S2), `deep` is mandatory for risk-compliance and quality agents.

## Audit Requirements for Model Overrides
For each subagent invocation, record:
- `default_model_profile`
- `selected_model_profile`
- `override_reason` (if selected differs from default)

Store these fields in task audit summary or external audit log.

## Safety Constraints
- Model override never changes role boundaries.
- Subagents still cannot communicate with users directly.
- Subagents still cannot use MCP tools directly.
