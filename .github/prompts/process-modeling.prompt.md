# Prompt: Process Modeling

## Intent
Run a process-focused analytical cycle to produce AS-IS and/or TO-BE process models suitable for downstream requirements, integration, and quality validation.

## When to Use
Use this prompt when process understanding, decision flow, exception handling, SLA constraints, or operational bottlenecks must be formalized.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define whether target is AS-IS, TO-BE, or both.
3. Specify expected model format: BPMN XML, Mermaid, PlantUML, or mixed output.
4. Invoke Process subagent with full input envelope.
5. Validate output envelope contract.
6. Apply confidence and escalation policy.
7. Return synthesized process handover package for downstream agents.

## Mandatory Input Envelope for Process Subagent
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
- `retrieval_first_performed`: true | false
- `context_version`
- `confidence_score` and `confidence_rationale`
- claim labels: FACT | INFERENCE | ASSUMPTION | UNCERTAIN
- `positive_foundations`
- `remediation_proposals`
- `role_specific_value`
- `open_issues` with blocking/non-blocking
- `episodic_memory_entry`
- `source_links` with freshness

## Required Process Content
Ensure the resulting artifact contains:
- actors/lanes and ownership boundaries
- main flow and sequencing
- variants and exceptions
- decision points and decision logic assumptions
- SLA and operational constraints
- bottlenecks/manual workarounds
- model output in requested notation(s)
- positive foundations that can be reused in TO-BE process design
- remediation proposals for bottlenecks and exception handling

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial process analysis and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Requirements subagent
- Integration subagent
- Quality subagent

Include explicit notes on:
- unresolved process ambiguities
- uncertain branches and assumptions
- missing evidence affecting implementation readiness

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- No implicit exception paths without explicit labeling.
- Do not present inferred flow as FACT.
- For architecture-impacting ambiguity, include Mermaid or PlantUML in output depending on diagram type, even when another notation is also provided.
