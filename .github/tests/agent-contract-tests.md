# ZAIA Agent Contract Tests

Status: active
Owner: environment owner
Scope: all ZAIA subagents and orchestrator interface validation

## 1. Purpose
This document defines contract tests that prove subagents follow ZAIA input/output contracts, confidence behavior, and escalation rules.

## 2. Test Targets
Subagents in scope:
- discovery
- process
- requirements
- domain
- integration
- nfr
- risk-compliance
- backlog
- quality
- knowledge-repository

Orchestrator checks in scope:
- input envelope completeness before delegation
- output envelope completeness after subagent response
- confidence-threshold routing behavior
- escalation routing to orchestrator-only path

## 3. Required Contract Fields
### 3.1 Input envelope
Required fields:
- task_id
- objective
- working_context
- permissions_scope
- data_classification
- required_confidence_threshold

### 3.2 Output envelope
Required fields:
- status (completed | completed_with_notes | escalated | failed)
- technical_artifact
- confidence_score (0.0-1.0)
- confidence_rationale
- claim labels for major statements (FACT | INFERENCE | ASSUMPTION | UNCERTAIN)
- open_issues with blocking or non-blocking priority
- episodic_memory_entry (max 200 chars)
- source_links with freshness assessment

## 4. Core Contract Test Matrix
Apply every test case to every subagent in scope.

| Test ID | Test Name | Input Fixture | Expected Result |
|---|---|---|---|
| CT-001 | Accept valid envelope | valid-input.json | status is completed or completed_with_notes; output envelope fully populated |
| CT-002 | Reject missing required fields | missing-required-fields.json | status is escalated; reason identifies missing fields |
| CT-003 | Low confidence handling | low-confidence-context.json | behavior follows threshold policy (0.6-0.79 notes; 0.4-0.59 escalate; <0.4 blocking escalate) |
| CT-004 | Scope boundary enforcement | out-of-scope-request.json | status is escalated with scope-exceeded rationale |
| CT-005 | Always emit episodic memory | any fixture | output contains episodic_memory_entry <= 200 chars |
| CT-006 | Claim labeling presence | any fixture | major statements include FACT/INFERENCE/ASSUMPTION/UNCERTAIN labels |
| CT-007 | Open issue priority validity | any fixture | each open issue has priority blocking or non-blocking |
| CT-008 | Source freshness presence | any fixture | source_links include freshness attribute |
| CT-009 | Confidence range validity | any fixture | confidence_score is in range 0.0-1.0 |
| CT-010 | Escalation destination policy | missing-required-fields.json or low-confidence-context.json | escalation addressed to orchestrator path only |
| CT-011 | Shared-contract reference integrity | repo files | agent and selected prompt files reference shared contracts for input/output/confidence |
| CT-012 | Version tag presence in shared modules | .github/contracts/*.md, .github/policies/*.md | each file contains `Version: x.y.z` metadata line |

## 5. Confidence Behavior Assertions
For every subagent:
- 0.80-1.00: output may be completed.
- 0.60-0.79: output may be completed_with_notes and must annotate uncertainty.
- 0.40-0.59: final result must not be treated as complete; escalate with blockers.
- below 0.40: immediate blocking escalation.

## 6. Orchestrator Validation Checks
Run these checks per subagent invocation:
1. Reject delegation if input envelope is incomplete.
2. Reject acceptance if output envelope is incomplete.
3. Reject acceptance if claim labels are missing for major statements.
4. Reject acceptance if confidence_score is outside 0.0-1.0.
5. Reject acceptance if escalation bypasses orchestrator path.

## 7. Execution Procedure
1. Select subagent under test.
2. Run CT-001 through CT-012 with relevant fixture files.
3. Record pass/fail and evidence snippets.
4. Repeat for all subagents.
5. Produce summary report by agent and by test case.

Reference integrity checks:
- Run `rg "\\.github/contracts/subagent-input-envelope\\.md|\\.github/contracts/subagent-output-envelope\\.md|\\.github/contracts/confidence-and-escalation\\.md" .github/agents .github/prompts`.
- Run `rg "^Version:\\s+[0-9]+\\.[0-9]+\\.[0-9]+" .github/contracts .github/policies`.

Automated repository-level check:
- Run `.github/tests/orchestration_contract_validator.py --path Documents/Analysis`.
- This check validates TA-ID UTC format, required output-envelope markers, and basic final_status consistency markers in persisted markdown artifacts.

## 8. Pass Criteria
A subagent passes contract validation only if:
- all CT-001 through CT-012 pass,
- no blocking deviations remain,
- confidence and escalation behavior matches policy.

## 9. Failure Handling
If any contract test fails:
1. mark agent version as non-releasable,
2. open remediation task,
3. rerun full matrix after fix,
4. update versioning changelog with regression note.


