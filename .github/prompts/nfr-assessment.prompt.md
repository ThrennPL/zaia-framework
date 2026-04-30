# Prompt: NFR Assessment

## Intent
Run an NFR-focused analytical cycle to produce a measurable, testable non-functional requirement set with explicit gaps and mitigation direction.

## When to Use
Use this prompt when quality attributes, operational constraints, and compliance-related non-functional expectations must be validated.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define NFR scope and priority quality attributes.
3. Invoke NFR subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized NFR handover package for downstream agents.

## Mandatory Input Envelope for NFR Subagent
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

## Required NFR Coverage Areas
Ensure the resulting artifact addresses:
- security
- performance
- availability
- compliance
- observability
- auditability
- retention
- scalability
- maintainability

## Category Alignment Requirement
Align proposed project-level NFR entries to categories:
- NFR-SEC-{NNN}
- NFR-PERF-{NNN}
- NFR-AVAIL-{NNN}
- NFR-COMP-{NNN}
- NFR-OBS-{NNN}

ID assignment remains orchestrator-controlled.

## Required NFR Output Content
Ensure output includes:
- measurable thresholds/targets
- verification strategy per NFR
- dependency and impact notes
- gap analysis
- mitigation direction

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial NFR analysis and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Risk and Compliance subagent
- Quality subagent
- Integration subagent (if operational constraints are impacted)

Include explicit notes on:
- unverifiable NFR statements
- high-risk quality gaps
- unresolved assumptions affecting delivery readiness

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not output vague NFR statements without measurable criteria.
- Do not present inferred thresholds as FACT.
