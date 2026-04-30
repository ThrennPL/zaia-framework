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

2. Collect optional precision profile in the same pass (single configuration run):
- agent scope hints
- agent evidence-depth expectations
- agent escalation sensitivity
- agent quality strictness
- function-level quality/approval placeholders (if used)

3. Apply configuration placeholders across framework files.

4. Validate that required placeholders are resolved in:
- agent contracts
- analytical prompts
- quality gates
- artifact templates
- final-output templates

5. Execute placeholder verification runbook and evaluate coverage matrix:
- .github/placeholders/placeholder-verification-runbook.md
- .github/placeholders/placeholder-coverage-matrix.md

6. Produce a configuration summary with unresolved placeholders and required owner decisions.

## Required Output
- configuration status: complete | partial | blocked
- resolved placeholder list
- unresolved placeholder list with blocking/non-blocking priority
- impacted file list
- agent/function precision placeholder profile (resolved + unresolved)
- recommended next actions
- verification evidence references (runbook + coverage matrix)

## Constraints
- Keep orchestrator-only MCP and user-contact boundaries intact.
- Do not remove mandatory contract fields while adapting placeholders.
- Preserve auditable confidence and escalation behavior.
