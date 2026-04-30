# ZAIA Placeholder Catalog

Status: active
Owner: environment owner
Purpose: standard placeholder set for project-level adaptation

## 1. Placeholder Format
Use uppercase tokens wrapped in double braces:
- {{PLACEHOLDER_NAME}}

## 2. Core Identity Placeholders
- {{PROJECT_NAME}}
- {{PROJECT_CODE}}
- {{PROGRAM_NAME}}
- {{ENVIRONMENT_OWNER}}

## 3. Governance Placeholders
- {{DATA_CLASSIFICATION_BASELINE}}
- {{RETENTION_DAYS}}
- {{COMPLIANCE_PROFILE}}
- {{APPROVAL_MODEL}}

## 4. Operating Model Placeholders
- {{PRIMARY_DOMAIN}}
- {{STAKEHOLDER_GROUPS}}
- {{DELIVERY_MODEL}}
- {{QUALITY_GATE_POLICY}}

## 5. Integration and Tooling Placeholders
- {{MCP_ALLOWED_TOOLS}}
- {{MCP_RESTRICTED_TOOLS}}
- {{SOURCE_SYSTEMS}}
- {{TARGET_SYSTEMS}}

## 6. Traceability and Artifact Placeholders
- {{ARTIFACT_ID_PREFIX}}
- {{TRACEABILITY_DEPTH}}
- {{REQUIRED_ARTIFACT_SET}}

## 7. Security and Risk Placeholders
- {{PII_HANDLING_POLICY}}
- {{ACCESS_CONTROL_MODEL}}
- {{RISK_TOLERANCE_LEVEL}}

## 8. Agent and Function Precision Placeholders (Optional)
Use these placeholders to refine agent behavior and function-level expectations without breaking default ZAIA usage.

Placement rule:
- Define and document the exact agent-specific placeholder keys inside the corresponding `.github/agents/<agent>.md` file.
- Keep naming aligned to the catalog pattern for consistency.

Suggested naming patterns:
- {{AGENT_<AGENT_NAME>_SCOPE_HINT}}
- {{AGENT_<AGENT_NAME>_ESCALATION_SENSITIVITY}}
- {{AGENT_<AGENT_NAME>_EVIDENCE_DEPTH}}
- {{FUNCTION_<FUNCTION_NAME>_QUALITY_THRESHOLD}}
- {{FUNCTION_<FUNCTION_NAME>_APPROVAL_REQUIRED}}

Examples:
- {{AGENT_RISK_COMPLIANCE_EVIDENCE_DEPTH}} = high
- {{AGENT_DISCOVERY_SCOPE_HINT}} = customer onboarding only
- {{FUNCTION_GATE_VALIDATION_QUALITY_THRESHOLD}} = strict

Default behavior rule:
- If optional agent/function placeholder is unresolved, ZAIA falls back to standard contract behavior and default governance constraints.

## 9. Validation Checklist
A project configuration is complete only when:
1. All critical placeholders are resolved.
2. No unresolved critical placeholder remains in mandatory contracts.
3. Placeholder resolution is documented with owner and date.
4. Changes preserve orchestrator/subagent boundary rules.

## 10. Critical Placeholder Set
Critical placeholders that must be resolved before productive use:
- {{PROJECT_NAME}}
- {{ENVIRONMENT_OWNER}}
- {{DATA_CLASSIFICATION_BASELINE}}
- {{COMPLIANCE_PROFILE}}
- {{MCP_ALLOWED_TOOLS}}
- {{RETENTION_DAYS}}
