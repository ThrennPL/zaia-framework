# Example: Project Configuration and Placeholder Resolution

## Metadata
- project_name: ZAIA Sample Program
- project_code: ZSP
- environment_owner: Lead BA
- verification_date: 2026-04-30
- verification_status: complete

## Resolved Critical Placeholders
- {{PROJECT_NAME}} = ZAIA Sample Program
- {{ENVIRONMENT_OWNER}} = Lead BA
- {{DATA_CLASSIFICATION_BASELINE}} = internal
- {{COMPLIANCE_PROFILE}} = regulated-heavy
- {{MCP_ALLOWED_TOOLS}} = jira_read, confluence_read, git_metadata_read, ocr_extract_read
- {{RETENTION_DAYS}} = 365

## Resolved Non-Critical Placeholders
- {{PRIMARY_DOMAIN}} = retail onboarding
- {{QUALITY_GATE_POLICY}} = gate-0-to-gate-4
- {{TRACEABILITY_DEPTH}} = objective-to-test
- {{PII_HANDLING_POLICY}} = mask-before-subagent

## Unresolved Placeholders
- none

## Impacted Assets
- .github/mcp/governance-controls.md
- .github/quality-gates/gate-0-readiness.md
- .github/prompts/project-configuration.prompt.md
- .github/final-outputs/template-selection-rules.md

## Owner Sign-off
- signed_by: Lead BA
- sign_off_status: approved
- notes: ready for production analytical cycles
