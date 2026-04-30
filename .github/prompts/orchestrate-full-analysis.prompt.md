# Prompt: Orchestrate Full Analysis

## Intent
Run a complete ZAIA orchestration cycle for a user request and return one synthesized final report.

## Execution Instructions
1. Interpret user intent and define scope.
2. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
3. Build delegation plan (subtasks, dependencies, order, rationale).
4. Invoke required subagents with full input envelope.
5. Validate each subagent output envelope.
6. Resolve confidence gaps, escalations, and discrepancies.
7. Synthesize and return final user-facing report with mandatory sections.
8. Persist final synthesized report `.md` and Team Memory update artifact automatically before user handover.
9. Record audit events and episodic memory entries.

## Mandatory Subagent Input Envelope
Every subagent call must include:
- `task_id`
- `objective`
- `working_context`
- `permissions_scope`
- `data_classification`
- `required_confidence_threshold`

## Mandatory Subagent Output Envelope
Accept output only if it includes:
- `status`: completed | completed_with_notes | escalated | failed
- `technical_artifact`
- `retrieval_first_performed`: true | false
- `context_version`
- `confidence_score` and `confidence_rationale`
- claim labels: FACT | INFERENCE | ASSUMPTION | UNCERTAIN
- `positive_foundations`
- `remediation_proposals`
- `role_specific_value`
- `evidence_map` (major claims to source evidence)
- `open_issues` with blocking/non-blocking priority
- `episodic_memory_entry` (max 200 chars)
- `source_links` with freshness

Evidence-only validation:
- Reject unsupported FACT claims.
- Require UNCERTAIN label for non-source-backed statements.
- Require correction before synthesis when evidence traceability is missing.
- Treat prior subagent technical artifacts as valid sources when they are explicitly referenced by TASK-ID/TA-ID and mapped in `evidence_map`.

## Confidence Policy
Use weighted scoring:

`confidence = w_source_coverage * source_coverage + w_data_freshness * data_freshness + w_context_completeness * context_completeness + w_internal_consistency * internal_consistency`

Behavior:
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with explicit uncertainty annotations
- 0.40-0.59: no final subagent result; escalate with blockers
- below 0.40: immediate blocking escalation

## Discrepancy Protocol
If subagent outputs conflict:
1. Run one orchestrated discussion round.
2. Request each agent to maintain, revise, or scope claim.
3. Drive toward at least one reconciled design option.
4. Decide with explicit rationale and implementation impact.
5. If unresolved, escalate to user with structured options.

## Final Report Template (Mandatory)
1. Task context and scope
2. Subagent contributions (status, confidence, key findings)
3. Positive foundations
4. Discrepancies and discussion outcome
5. Orchestrator synthesis (FACT vs INFERENCE vs ASSUMPTION vs UNCERTAIN)
6. Recommendations and rationale
7. Open issues and decisions needed from user
8. Source trail and identifiers

## Constraints
- Orchestrator is the only user-facing agent.
- Subagents never communicate directly with user.
- Only orchestrator can use MCP tools.
- Never publish raw technical artifacts as final output.
- Require co-design outputs (remediation, not only gap lists).
- Subagents must not invent facts or requirements beyond provided context.
- If a final verdict is present, final report header status must be `completed`.
- Final output must include reference to a persisted Team Memory update artifact.
- Final report generation is automatic and must not depend on user reminder.
