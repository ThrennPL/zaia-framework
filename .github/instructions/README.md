# ZAIA Instructions Set

This folder contains operational instruction overlays for runtime behavior.

## Files
1. orchestrator-routing.instructions.md
- Defines one-entry orchestration routing and execution modes.

2. simple-queries.instructions.md
- Defines how to handle low-risk simple requests without unnecessary delegation.

3. agent-model-routing.instructions.md
- Defines default model profile per agent and orchestrator-controlled downgrade/upgrade rules.

## Design principle
- Orchestrator always receives the request first.
- Orchestrator may choose lightweight mode for simple queries.
- Full orchestration is mandatory for analytical, compliance, or multi-agent tasks.
- Orchestrator controls final model selection per invocation, including profile overrides when justified.

## Related shared contracts and policies
- .github/contracts/subagent-input-envelope.md
- .github/contracts/subagent-output-envelope.md
- .github/contracts/confidence-and-escalation.md
- .github/contracts/discrepancy-protocol.md
- .github/policies/model-routing-policy.md
- .github/policies/single-agent-exception-policy.md
- .github/policies/artifact-location-policy.md
