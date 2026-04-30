# Prompt: Discovery Analysis

## Intent
Run a discovery-focused analytical cycle to structure early-stage understanding before design and backlog decomposition.

## When to Use
Use this prompt when the request includes unclear scope, fragmented source materials, unknown stakeholders, or missing context.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define discovery objective and scope boundaries.
3. Invoke Discovery subagent with full input envelope.
4. Validate output envelope contract.
5. Check confidence and apply escalation behavior if needed.
6. Return a synthesized discovery package for downstream agents.

## Mandatory Input Envelope for Discovery Subagent
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

## Required Discovery Content
Ensure the resulting artifact contains:
- stakeholder map
- problem framing and business drivers
- constraints and assumptions
- open questions
- information gaps
- hypotheses and validation priorities

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial analysis and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Requirements subagent
- Process subagent
- Domain subagent

Include explicit notes on:
- unresolved blockers
- uncertainty hotspots
- missing evidence requiring retrieval

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not present assumptions as facts.
- Do not skip claim labeling.
