# Prompt: Knowledge Reuse Review

## Intent
Run a knowledge-focused analytical cycle to evaluate analytical coverage, identify duplication, and recommend safe reuse of existing artifacts.

## When to Use
Use this prompt when historical context, repository hygiene, and reuse opportunities must be assessed before new analytical work proceeds.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define knowledge-review scope and target corpus boundaries.
3. Invoke Knowledge Repository subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized knowledge handover package for downstream agents.

## Mandatory Input Envelope for Knowledge Repository Subagent
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

## Required Knowledge Review Content
Ensure the resulting artifact contains:
- analytical coverage report (covered vs uncovered areas)
- duplicate and overlap findings
- stale or weak-source warnings
- artifact-level reuse recommendations
- repository hygiene observations and retrieval friction points
- positive foundations in reusable repository assets
- remediation proposals for retrieval/reuse governance

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial knowledge analysis and blockers
- below 0.40: blocking escalation, stop downstream progression

## Output Handover Contract
Produce a synthesized handover package for:
- Discovery subagent
- Domain subagent
- Quality subagent

Include explicit notes on:
- unresolved historical ambiguity
- stale-source exposure risk
- missing context needed for safe reuse

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not claim historical facts without source support.
- Do not present inferred similarity as confirmed reuse suitability.
