# ZAIA E2E Smoke Runbook

Status: active
Owner: quality owner

## Purpose
Run a fast end-to-end smoke check for ZAIA orchestration baseline consistency.

## Scope
The smoke test validates:
1. Core governance/config files exist.
2. Scenario matrix covers S1-S9.
3. Agent docs point to shared contracts.
4. Template selection rules include extended mapping.
5. Historical artifact validator reports only known baseline issues.

## Command
Run from repository root:

python .github/tests/zaia_e2e_smoke.py

## Pass Criteria
1. All checks return PASS.
2. Overall status is PASS.

## Notes
1. Historical validator issues from legacy artifacts are currently treated as known baseline issues.
2. Any new validator issue is treated as E2E failure.
