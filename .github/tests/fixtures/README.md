# ZAIA Contract Test Fixtures

This directory contains reusable fixture classes for contract testing all ZAIA subagents.

## Fixture Classes
- valid-input.json
- missing-required-fields.json
- low-confidence-context.json
- out-of-scope-request.json

## Usage Rules
1. Use the same fixture classes for each subagent.
2. Adjust only domain content, never remove required structural keys unless the test case demands it.
3. Keep all fixture files ASCII and deterministic.
4. Store fixture updates under semantic version control and record changes in versioning changelog.

## Mapping to Contract Tests
- CT-001 uses valid-input.json.
- CT-002 uses missing-required-fields.json.
- CT-003 uses low-confidence-context.json.
- CT-004 uses out-of-scope-request.json.
- CT-005 through CT-010 use any fixture where relevant.

## Data Classification
Fixtures use synthetic placeholder content and must not include real sensitive business data.
