# ZAIA Project Artifact Quality Tests

Status: active
Owner: quality owner
Scope: project artifacts (PRD, SD, ADR, FR, NFR, BTM, QGC, TMP)

## 1. Purpose
Define quality tests for project artifacts as a separate stream from agent contract tests.

## 2. Test Scope
This test strategy validates artifact quality before quality-gate progression.
It does not replace subagent contract tests.

## 3. Quality Test Categories
### 3.1 Metadata completeness
Validate that each artifact has:
- valid artifact ID in required format
- owner
- status
- date
- required header fields from template

### 3.2 Internal consistency
Validate that each artifact:
- has no self-contradictory statements
- keeps terminology stable inside the artifact
- has explicit assumptions and constraints where required

### 3.3 Cross-artifact consistency
Validate that:
- domain terms are aligned with glossary outputs
- references to linked artifacts exist and are current
- traceability links are coherent across PRD, SD, ADR, and BTM

### 3.4 Coverage quality
Validate that:
- user stories cover modeled process paths
- acceptance criteria exist for functional requirements
- NFR items include mitigation direction for identified risk

### 3.5 Claim labeling and evidence
Validate that major claims remain traceable and uncertainty is visible when required.

## 4. Test Matrix
| Test ID | Category | Artifact Types | Pass Condition |
|---|---|---|---|
| AQT-001 | Metadata completeness | all | required header fields present and non-empty |
| AQT-002 | ID format validity | all | artifact ID matches naming standard |
| AQT-003 | Internal consistency | PRD, SD, ADR | no critical contradictions |
| AQT-004 | Cross-reference validity | all with links | all referenced IDs exist and resolve |
| AQT-005 | Traceability completeness | PRD, BTM, QGC | required trace path is complete |
| AQT-006 | Coverage checks | requirements/backlog-linked artifacts | stories and criteria coverage is adequate |
| AQT-007 | NFR mitigation linkage | SD, NFR, risk outputs | each critical NFR risk has mitigation direction |
| AQT-008 | Evidence quality | all | source trail exists with freshness notes |

## 5. Execution Order
1. Run metadata and ID checks.
2. Run internal consistency checks.
3. Run cross-artifact checks.
4. Run coverage checks.
5. Run evidence and labeling checks.
6. Emit quality result: pass | pass_with_notes | fail.

## 6. Failure Handling
If any blocking failure appears:
1. set gate result to fail,
2. create remediation actions with owners,
3. rerun impacted tests after correction,
4. attach evidence to QGC record.

## 7. Reporting Output
Each run must produce:
- tested artifact list
- passed tests
- failed tests
- blocking vs non-blocking findings
- remediation plan and re-test trigger
