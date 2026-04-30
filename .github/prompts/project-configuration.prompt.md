# Prompt: Project Configuration and Placeholder Adaptation

## Intent
Configure ZAIA framework assets for a specific project context by filling placeholders and validating configuration completeness.

## When to Use
Use this prompt at project onboarding, before first production analytical cycle, or after major governance changes.

## Execution Instructions
1. Collect project configuration baseline:
- project name and domain
- owner and role mapping
- data classification policy
- compliance profile
- integration landscape

2. Apply configuration placeholders across framework files.

3. Validate that required placeholders are resolved in:
- agent contracts
- analytical prompts
- quality gates
- artifact templates
- final-output templates

4. Execute placeholder verification runbook and evaluate coverage matrix:
- .github/placeholders/placeholder-verification-runbook.md
- .github/placeholders/placeholder-coverage-matrix.md

5. Produce a configuration summary with unresolved placeholders and required owner decisions.

## Required Output
- configuration status: complete | partial | blocked
- resolved placeholder list
- unresolved placeholder list with blocking/non-blocking priority
- impacted file list
- recommended next actions
- verification evidence references (runbook + coverage matrix)

## Constraints
- Keep orchestrator-only MCP and user-contact boundaries intact.
- Do not remove mandatory contract fields while adapting placeholders.
- Preserve auditable confidence and escalation behavior.
