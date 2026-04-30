# Prompt: Requirements Pack

## Intent
Run a requirements-focused analytical cycle to produce a structured, testable requirements package ready for backlog refinement and quality validation.

## When to Use
Use this prompt when the objective is to convert analytical context into implementation-relevant requirements and acceptance logic.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define requirements scope and boundaries.
3. Invoke Requirements subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized requirements handover package for downstream agents.

## Mandatory Input Envelope for Requirements Subagent
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

## Required Requirements Content
Ensure the resulting artifact contains:
- business requirements (BR)
- functional requirements (FR)
- system requirements (SR)
- NFR candidates requiring NFR validation
- user stories in format: As a..., I want..., so that...
- acceptance criteria in Given-When-Then
- explicit business rules

## Quality Rules for Requirements
- Requirements must be atomic, clear, and testable.
- Separate requirement statements from design decisions.
- Quantify ambiguous qualifiers whenever possible.
- Link key requirements to source evidence and process context.
- Mark inferred statements explicitly.

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial requirements and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Backlog subagent
- Quality subagent
- NFR subagent

Include explicit notes on:
- unresolved requirement ambiguities
- missing acceptance evidence
- traceability gaps requiring closure

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not output stories without acceptance criteria.
- Do not present inferred requirements as FACT.
