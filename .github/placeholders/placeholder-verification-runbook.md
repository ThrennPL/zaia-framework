# ZAIA Placeholder Verification Runbook

Status: active
Owner: environment owner

## 1. Purpose
Provide a deterministic procedure to validate whether ZAIA is correctly adapted to a specific project configuration.

## 2. Output Status Model
- complete: all critical placeholders resolved and no blocking gaps.
- partial: critical placeholders resolved, but non-critical gaps remain.
- blocked: one or more critical placeholders unresolved or policy conflicts detected.

## 3. Verification Scope
Verification must include:
- .github/agents/
- .github/prompts/
- .github/quality-gates/
- .github/artifacts/templates/
- .github/final-outputs/
- .github/mcp/

## 4. Step-by-Step Procedure
1. Load project configuration baseline and owner mapping.
2. Resolve placeholder values in a controlled configuration sheet.
3. Validate critical placeholders from placeholder-catalog.
4. Run coverage check against placeholder-coverage-matrix.
5. Confirm no unresolved critical placeholder remains in mandatory assets.
6. Validate orchestrator/subagent boundary rules are unchanged.
7. Record result as complete, partial, or blocked.

## 5. Blocking Conditions
Return blocked if any condition holds:
- unresolved critical placeholder,
- data classification placeholder mismatch,
- MCP allowlist placeholder unresolved,
- retention placeholder unresolved,
- owner placeholder unresolved.

## 6. Partial Conditions
Return partial if:
- all critical placeholders are resolved,
- unresolved placeholders remain only in optional or non-blocking sections.

## 7. Evidence Package
Every verification run must produce:
- verification timestamp
- owner
- resolved placeholder list
- unresolved placeholder list with priority
- impacted files
- status decision rationale

## 8. Gate Integration
Gate 0 readiness must include this verification run as mandatory evidence for project onboarding.
