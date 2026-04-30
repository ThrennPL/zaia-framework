# Example: Risk and Compliance Decision Pack

## Header
- Report ID: RPT-2026-004
- Task ID: T-20260430-104
- Template Type: Risk and Compliance Decision Pack
- Version: 1.0
- Status: approved
- Owner: Compliance Lead
- Date: 2026-04-30
- Data Classification: restricted

## 1. Task Context and Scope
- Objective: Validate compliance readiness for onboarding data handling changes.
- Scope: customer PII storage and retention controls.
- Assessment boundary: onboarding and KYC-linked integration points.

## 2. Subagent Contributions
- Risk and Compliance produced risk register and control gaps.
- NFR aligned retention and auditability requirements.
- Integration highlighted cross-system access points.

## 3. Discrepancies and Outcome
- Conflict: retention period interpretation differs between two policy docs.
- Outcome: escalate to policy owner and apply stricter interim retention.

## 4. Orchestrator Synthesis (FACT | INFERENCE | ASSUMPTION | UNCERTAIN)
- FACT: audit logging is mandatory for access events.
- INFERENCE: stricter interim retention lowers regulatory exposure.
- ASSUMPTION: policy owner decision expected within one week.
- UNCERTAIN: legal interpretation for legacy archive scope.

## 5. Recommendations and Rationale
- Enforce stricter retention now.
- Block release if legal decision is not recorded by deadline.

## 6. Open Issues and Required Decisions
- Blocking: legal decision on archive scope.
- Non-blocking: update control ownership matrix.

## 7. Source Trail and Identifiers
- Sources: SRC-70, SRC-72, SRC-74.
- Linked IDs: NFR-COMP-004, QGC-RELEASE-2026-001.

## 8. Risk-Specific Addendum
- Risk register summary: 2 high, 3 medium.
- DPIA note: update required.
- Control gaps: encryption key rotation evidence missing.
