# Phase F Workflow: Artifact Generator

Status: active
Owner: environment owner

## 1. Objective
Automate generation of project artifacts from approved ZAIA templates with traceability-safe defaults.

## 2. Scope
In scope:
- PRD generation scaffold
- Solution Design scaffold
- ADR scaffold
- BTM scaffold
- QGC scaffold
- TMP scaffold
- final synthesized orchestrator report generation

Out of scope:
- automatic content approval
- automatic publication to external systems

## 3. Inputs
Required:
- task_id
- artifact_type
- owner
- project configuration placeholder values
- source references

Optional:
- linked artifact IDs
- predefined scope snippets

## 4. Generation Steps
1. Validate artifact_type against allowed template list.
2. Load template from .github/artifacts/templates/.
3. Resolve placeholders using approved configuration map.
4. Inject required metadata header.
5. Insert baseline traceability section.
6. Emit draft artifact to target workspace path.
7. For orchestration closure, auto-generate final synthesized report `.md` and Team Memory update artifact before user handover.
8. Record generation event in audit log.

## 5. Validation Rules
Generation must fail if:
- required placeholder is unresolved,
- required header field is missing,
- invalid artifact ID format is detected,
- source references are empty.

## 6. Output Contract
- generation_status: success | failed
- output_path
- generated_artifact_id
- unresolved_placeholders
- validation_issues

## 7. Safety Constraints
- no external write operations in Phase F baseline,
- no override of orchestrator-only MCP authority,
- generated artifacts remain draft until quality gate validation.
- final report generation cannot be delayed until user reminder.
