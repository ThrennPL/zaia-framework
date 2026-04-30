# Prompt: Risk and Compliance Review

## Intent
Run a risk and compliance analytical cycle to identify, classify, and prioritize regulatory and operational risks with mitigation and residual-risk visibility.

## When to Use
Use this prompt when solution scope includes regulated data, policy-sensitive operations, audit obligations, or high delivery uncertainty.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define risk/compliance scope and assessment depth.
3. Invoke Risk and Compliance subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized risk/compliance handover package for decision and quality gate use.

## Mandatory Input Envelope for Risk and Compliance Subagent
- `task_id`
- `objective`
- `working_context`
- `permissions_scope`
- `data_classification`
- `required_confidence_threshold`

## Mandatory Output Envelope Validation
Require all fields:
- `status`: completed | completed_with_notes | escalated | failed
- `technical_artifact`
- `confidence_score` and `confidence_rationale`
- claim labels: FACT | INFERENCE | ASSUMPTION | UNCERTAIN
- `open_issues` with blocking/non-blocking
- `episodic_memory_entry`
- `source_links` with freshness

## Required Risk and Compliance Content
Ensure the resulting artifact contains:
- risk register entries by category (regulatory, operational, project, analytical)
- risk severity and likelihood
- control and compliance gap findings
- DPIA trigger assessment where applicable
- data classification and access-control concerns
- mitigation candidates and residual risk notes

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial risk analysis and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Orchestrator decision synthesis
- Quality subagent validation
- NFR subagent follow-up where quality gaps are risk-driven

Include explicit notes on:
- unresolved compliance ambiguity
- control gaps with blocking impact
- decisions required from human owners

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not present inferred obligations as legal facts.
- Do not suppress high-impact uncertainty.
