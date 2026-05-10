# Subagent Output Envelope Contract

Status: active
Owner: orchestrator governance
Version: 1.0.0

## Required fields
- status: completed | completed_with_notes | escalated | failed
- technical_artifact
- retrieval_first_performed
- context_version
- confidence_score
- confidence_rationale
- claim labels for major statements: FACT | INFERENCE | ASSUMPTION | UNCERTAIN
- positive_foundations
- remediation_proposals
- role_specific_value
- evidence_map
- open_issues (blocking | non-blocking)
- episodic_memory_entry
- source_links with freshness

## Validation rules
1. Missing any required field -> contract failure.
2. Unsupported FACT claim -> contract failure.
3. confidence_score must be in [0.0, 1.0].
