# Prompt: Discrepancy Resolution

## Intent
Run one controlled discrepancy-resolution round when two or more subagent technical artifacts contain conflicting claims.

## When to Use
Use this prompt when orchestrator detects conflict that can change synthesis outcome, quality status, or user-facing recommendations.

## Execution Instructions
1. Assign or reuse TASK-ID in format T-YYYYMMDD-NNN.
2. Identify conflict scope and impacted decisions.
3. Share only conflict-relevant sections with participating subagents.
4. Request each subagent response in one of three positions:
- maintain
- revise
- scope
5. Require evidence-backed rationale from each participant.
6. Drive participants to produce at least one reconciled design option.
7. Synthesize one decision with explicit rationale and implementation impact.
8. If unresolved after one round, escalate to user with structured options.

## Mandatory Input Envelope
For each participating subagent call include:
- task_id
- objective
- working_context
- permissions_scope
- data_classification
- required_confidence_threshold

## Mandatory Output Envelope Validation
Require:
- status
- technical_artifact delta or addendum
- retrieval_first_performed: true | false
- context_version
- confidence_score and confidence_rationale
- claim labels (FACT | INFERENCE | ASSUMPTION | UNCERTAIN)
- positive_foundations
- remediation_proposals
- role_specific_value
- open_issues with blocking/non-blocking
- episodic_memory_entry
- source_links with freshness

## Decision Output Contract
Return:
- conflict_summary
- agent_positions
- evidence_comparison
- reconciled_design_options
- orchestrator_decision
- decision_rationale
- unresolved_flag
- user_escalation_options (only if unresolved)

## Constraints
- Exactly one orchestrated discussion round before unresolved escalation.
- Before escalation, include at least one option with trade-offs and implementation impact.
- No direct subagent-user interaction.
- No direct subagent MCP usage.
- Do not suppress uncertainty in high-impact conflicts.
