# ZAIA Prompt and Skill Versioning Policy

Status: active
Owner: environment owner

## 1. Purpose
Define a strict semantic versioning model for orchestrator instructions, subagent definitions, and scenario prompts.

## 2. Versioning Scope
Assets in scope:
- .github/copilot-instructions.md
- .github/agents/*.md
- .github/prompts/*.prompt.md
- future skill specification files

## 3. Semantic Versioning Rules
Format: MAJOR.MINOR.PATCH

- MAJOR
  - contract-breaking changes
  - scope or capability boundary changes
  - output format incompatibilities

- MINOR
  - backward-compatible behavior extension
  - new supported scenario or stricter optional guidance

- PATCH
  - clarifications, typo fixes, non-contract wording improvements
  - no contract behavior change

## 4. Mandatory Change Metadata
Every version change must record:
- asset_id
- old_version
- new_version
- change_type (MAJOR | MINOR | PATCH)
- author
- date
- rationale
- impacted_contracts
- contract_test_result_reference

## 5. Release Checklist
1. Identify impacted assets.
2. Determine semantic bump level.
3. Run contract tests for impacted agents/prompts.
4. Validate no forbidden behavior was introduced.
5. Update CHANGELOG.md.
6. Approve release according to bump level policy.

## 6. Approval Policy
- MAJOR: explicit owner approval required.
- MINOR: owner or delegated maintainer approval required.
- PATCH: maintainer approval allowed.

## 7. Regression Requirement
No version may be promoted if contract tests fail for impacted scope.

## 8. Traceability Requirement
Each changelog entry must link to:
- affected files
- test evidence location
- rollback target version
