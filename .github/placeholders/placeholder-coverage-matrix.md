# ZAIA Placeholder Coverage Matrix

Status: active
Owner: environment owner

## 1. Purpose
Map placeholders to mandatory framework assets and define criticality for onboarding readiness.

## 2. Matrix
| Placeholder | Criticality | Required In Assets | Validation Rule |
|---|---|---|---|
| {{PROJECT_NAME}} | critical | prompts, final outputs, artifact templates | must be resolved in all project-facing headers |
| {{ENVIRONMENT_OWNER}} | critical | governance docs, runbooks, audit docs | must map to accountable role |
| {{DATA_CLASSIFICATION_BASELINE}} | critical | mcp governance, quality gates, onboarding docs | must be compatible with policy profile |
| {{COMPLIANCE_PROFILE}} | critical | risk/compliance assets, quality gates | must be defined and referenced in controls |
| {{MCP_ALLOWED_TOOLS}} | critical | mcp governance and baseline | must be explicit allowlist |
| {{RETENTION_DAYS}} | critical | audit and memory policies | must be numeric and policy-compliant |
| {{PROJECT_CODE}} | non-critical | artifact/report IDs where required | recommended for naming consistency |
| {{PROGRAM_NAME}} | non-critical | executive outputs | required only if program-level reporting is used |
| {{APPROVAL_MODEL}} | non-critical | gate and approval sections | should match governance workflow |
| {{PRIMARY_DOMAIN}} | non-critical | discovery/domain templates | should align terminology scope |
| {{QUALITY_GATE_POLICY}} | non-critical | quality gate docs | should reference adopted gate model |
| {{MCP_RESTRICTED_TOOLS}} | non-critical | mcp governance | should be explicitly documented |
| {{SOURCE_SYSTEMS}} | non-critical | integration and mcp docs | required for integration-heavy projects |
| {{TARGET_SYSTEMS}} | non-critical | integration and mcp docs | required for integration-heavy projects |
| {{ARTIFACT_ID_PREFIX}} | non-critical | templates and reports | optional if default ZAIA IDs are used |
| {{TRACEABILITY_DEPTH}} | non-critical | BTM and quality docs | should match project governance depth |
| {{REQUIRED_ARTIFACT_SET}} | non-critical | artifact governance docs | should match project delivery model |
| {{PII_HANDLING_POLICY}} | non-critical | risk/compliance docs | required when PII is in scope |
| {{ACCESS_CONTROL_MODEL}} | non-critical | compliance and mcp docs | required for restricted environments |
| {{RISK_TOLERANCE_LEVEL}} | non-critical | risk and executive outputs | should align with owner policy |

## 3. Coverage Decision Rules
1. complete: all critical placeholders resolved in all required assets.
2. partial: all critical placeholders resolved, with only non-critical unresolved placeholders.
3. blocked: any critical placeholder unresolved in a required asset.

## 4. Validation Frequency
- mandatory at project onboarding,
- mandatory after major governance or integration updates,
- recommended before release-readiness assessments.
