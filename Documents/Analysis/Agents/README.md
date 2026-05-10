# Katalogi Artefaktow Agentow

Cel: oddzielic artefakty operacyjne pracy agentow od konfiguracji w .github.

## Struktura
- Agenci/orchestrator/
- Agenci/discovery/
- Agenci/requirements/
- Agenci/domain/
- Agenci/integration/
- Agenci/process/
- Agenci/backlog/
- Agenci/nfr/
- Agenci/risk-compliance/
- Agenci/quality/
- Agenci/knowledge-repository/

## Zasady zapisu
1. Kazdy agent zapisuje swoj technical artifact do dedykowanego katalogu.
2. Nazwa pliku: {task-topic-slug}-{TASK-ID}.md
3. Team Memory update zawsze zapisuj do Documents/Analysis/Team-Memory/.
4. Finalny raport orkiestratora zapisuj w katalogu glownym Documents/Analysis/.
5. Konfiguracje, szablony i testy pozostaja w .github/.

## Migracja
- Historyczne raporty moga pozostac w obecnej lokalizacji.
- Nowe raporty od daty wdrozenia powinny trafiac do katalogow Agenci/.

Powiazanie polityki:
- .github/policies/artifact-location-policy.md

