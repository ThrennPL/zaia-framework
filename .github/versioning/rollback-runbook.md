# ZAIA Rollback Runbook

Status: active
Owner: environment owner

## 1. Purpose
Define deterministic rollback procedures for orchestrator instructions, subagent definitions, and prompts.

## 2. Rollback Triggers
Start rollback when at least one condition is true:
- contract test failure after release
- severe behavior regression
- policy compliance breach
- confidence/escalation logic regression

## 3. Rollback Modes
### 3.1 MAJOR or MINOR rollback (manual)
Required steps:
1. identify target stable version,
2. obtain explicit owner approval,
3. restore target files,
4. execute contract tests for impacted scope,
5. verify orchestrator and subagent boundary constraints,
6. document rollback in changelog.

### 3.2 PATCH rollback (automated-eligible)
Allowed only if:
- rollback target is last stable patch,
- contract tests pass after rollback,
- no MAJOR/MINOR contract boundary is crossed.

Automated flow:
1. revert to previous patch,
2. run contract tests,
3. publish rollback result,
4. append changelog entry.

## 4. Required Rollback Record
Every rollback entry must include:
- rollback_id
- trigger reason
- affected assets
- from_version
- to_version
- approval reference
- contract test result reference
- timestamp

## 5. Verification Checklist Post-Rollback
1. Input/output envelope constraints still hold.
2. Confidence threshold behavior still holds.
3. Escalation path remains orchestrator-only.
4. Mandatory final report sections remain enforced.
5. MCP access boundary remains orchestrator-only.

## 6. Stop Conditions
Do not finalize rollback if:
- contract tests are failing,
- escalation boundaries are violated,
- changelog entry is missing,
- owner approval is missing for MAJOR/MINOR.
