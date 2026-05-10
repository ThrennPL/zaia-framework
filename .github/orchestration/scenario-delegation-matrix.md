# ZAIA Scenario Delegation Matrix

Status: active
Owner: orchestrator governance

## 1. Purpose
Define a practical execution matrix for orchestrator delegation by scenario, including baseline and supplemental agent sets, required technical artifacts, and final orchestrator output.

## 2. Scenario Matrix

| Scenario | Trigger | Required agents | Supplemental agents | Required subagent artifacts | Final orchestrator artifact |
|---|---|---|---|---|---|
| S1 Discovery-Framing | unclear scope, missing stakeholders | discovery | domain | stakeholder map, constraints/assumptions split, open issues | Discovery Outcome Report |
| S2 Compliance-Heavy | control gaps, regulatory/privacy risk | risk-compliance | integration, nfr, quality | risk register, control gaps, mitigation sequence, residual risk | Risk and Compliance Decision Pack |
| S3 Requirements Clarification | objective known, requirements unclear | requirements | discovery, domain, process | FR catalog, acceptance criteria, traceability map | Discovery Outcome Report with requirements addendum |
| S4 Design-Decision | architecture options conflict | integration, nfr | requirements, domain, quality | option analysis, interface map, trade-offs, diagrams | Design Decision Pack |
| S5 Delivery Readiness | pre-release gate check | backlog, quality | requirements, nfr, integration | delivery backlog map, blocker list, readiness checks | Delivery Readiness Pack |
| S6 Integration Validation | interface change or compatibility risk | integration | domain, quality, process | system landscape, contracts, dependency risks | Design Decision Pack |
| S7 Knowledge Curation | reuse/duplication opportunities | knowledge-repository | discovery | overlap map, normalization actions, stale source notes | Executive Summary for Stakeholders or report appendix |
| S8 NFR-Driven | missing measurable NFR targets | nfr | risk-compliance, integration, quality | NFR catalog, measurable targets, validation strategy | Design Decision Pack or Delivery Readiness Pack |
| S9 Process Modeling | unclear process or exception paths | process | domain, requirements, integration | AS-IS/TO-BE model, decision points, exception handling | Discovery Outcome Report or Design Decision Pack |

## 3. Sequential and Parallel Rules
- Run independent required agent sets in parallel when there is no evidence conflict.
- Use one discrepancy round for conflicting outputs (maintain/revise/scope).
- Continue non-conflicting tracks while discrepancy round is in progress.
- Block only decisions directly affected by unresolved conflict.

## 4. Minimum Completion Checklist per Scenario
1. Trigger and scenario label recorded.
2. Required agent set invoked or explicitly justified via single-agent exception.
3. Output envelope validated for all returned technical artifacts.
4. Final template selected using template-selection-rules.
5. Team Memory update referenced in final report.
6. Audit summary persisted for the TASK-ID.

## 5. References
- .github/agents/orchestrator.md
- .github/final-outputs/template-selection-rules.md
- .github/final-outputs/templates/
- .github/quality-gates/
