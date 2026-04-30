# Prompt: Backlog Decomposition

## Intent
Run a backlog-focused analytical cycle to transform validated analytical outputs into refinement-ready delivery items.

## When to Use
Use this prompt when requirements and context are ready to be decomposed into execution structures for planning and delivery.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define decomposition scope (epic/feature/story/use case/task depth).
3. Invoke Backlog subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized backlog handover package for quality and planning decisions.

## Mandatory Input Envelope for Backlog Subagent
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

## Required Backlog Content
Ensure the resulting artifact contains:
- epics
- features
- user stories and/or use cases
- technical tasks
- dependency mapping and sequencing constraints
- prioritization rationale (value, dependency, risk)
- refinement blockers and assumptions

## Traceability Requirement
Require explicit mapping:
- objective -> epic -> story/use case -> technical task -> test intent

Flag all broken or missing links as open issues.

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial decomposition and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Quality subagent
- Orchestrator final synthesis

Include explicit notes on:
- dependency uncertainty
- prioritization assumptions
- unresolved decomposition gaps affecting refinement readiness

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not output backlog structures without traceability mapping.
- Do not present inferred priority as FACT.
