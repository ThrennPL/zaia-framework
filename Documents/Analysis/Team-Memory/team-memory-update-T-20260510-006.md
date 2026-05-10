# Team Memory Update

Status: completed
Task ID: T-20260510-006
Date: 2026-05-10

## Learned patterns
- S3 na VRH-E ujawnia stale luki: brak AC per FR i brak formalnej traceability.
- Security/compliance powinny byc traktowane jako blocking juz na etapie doprecyzowania wymagan, nie dopiero przy design review.

## Reuse recommendations
1. Wymagac AC Given-When-Then dla kazdego FR jako warunek wyjscia z S3.
2. Wymagac nieusuwalnego sladu audytowego dla kazdego uprzywilejowanego override.
3. Uzywac mini-matrycy FR->AC->test->dowod jako stalego zalacznika do raportu finalnego.
