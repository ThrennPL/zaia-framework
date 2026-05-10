PROJECT: VoltReserve Hub Enterprise (VRH-E)
Document Ref: PRD/SD-2024-V1.2
Owner: Global Energy Logistics Division
Framework Baseline: ZAIA Phase G Compliance  

1. Executive Summary
System VRH-E ma stać się centralnym orkiestratorem dystrybucji mocy dla flot autonomicznych pojazdów dostawczych. Projekt musi zostać wdrożony w modelu hybrydowym (Cloud/DC) zgodnie z wytycznymi Phase E frameworku ZAIA.  

2. Detailed Functional Requirements (FR)
FR-1: Real-Time Arbitration. System musi rozstrzygać konflikty rezerwacji mocy w czasie poniżej 30ms, aby umożliwić dynamiczne trasowanie pojazdów w ruchu.  

FR-2: Predictive Telemetry. Agregacja danych telemetrycznych (prędkość, masa, SoC baterii, dokładna lokalizacja GPS) ze wszystkich pojazdów co 5 sekund.

FR-3: Multi-Tenant Sovereignty. Każdy podwykonawca floty ma pełny wgląd w dane swoich pojazdów, ale system musi umożliwiać "awaryjny podgląd" (Emergency Override) przez operatora głównego bez ścieżki audytowej w celu przyspieszenia reakcji.

FR-4: Legacy Integration. Pobieranie danych o stanie transformatorów z lokalnych stacji poprzez analizę obrazu/OCR z kamer analogowych (Pilot Phase E).  

3. Technical Specification & Constraints (SD)
3.1. Infrastructure & Data Residency
Deployment: Klaster Kubernetes w regionie us-east-1 (AWS) dla wszystkich klientów, w tym operujących w Unii Europejskiej (ze względu na dostępność specyficznych instancji GPU do AI).

Database: Wykorzystanie bazy NoSQL (MongoDB) do przechowywania transakcji finansowych i rezerwacji mocy bez włączonego mechanizmu ACID (w celu maksymalizacji wydajności wymaganej w FR-1).

3.2. Security & Compliance
Authentication: Integracja z zewnętrznym systemem Legacy dostawcy (protokół PAP, przesyłanie haseł otwartym tekstem wewnątrz sieci prywatnej).

GDPR/Privacy: Dane GPS są przechowywane w formie niezaszyfrowanej w logach diagnostycznych przez 90 dni, aby umożliwić "Diagnostics Reporting" zgodnie z Phase F frameworku ZAIA.  

4. Integration & Orchestration Rules
Orchestrator Authority: Zgodnie z zasadami ZAIA, Orkiestrator ma wyłączny dostęp do narzędzi MCP i jest jedynym punktem kontaktu dla użytkownika końcowego.  

Subagent Escalation: W przypadku wykrycia przeciążenia sieci, Subagent ds. Energii ma prawo automatycznie odciąć zasilanie od stacji o najniższym priorytecie bez zatwierdzenia przez bramkę jakości (Quality Gate