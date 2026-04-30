# Phase E MVP: OCR Pilot Definition

Status: pilot
Owner: environment owner

## 1. Objective
Validate OCR-assisted ingestion for PDFs and images as read-only evidence extraction.

## 2. Pilot Scope
In scope:
- synthetic or approved sample PDFs
- synthetic or approved sample images
- text extraction and structural hints

Out of scope:
- automatic write-back to project artifacts
- OCR-driven autonomous decisioning

## 3. OCR Intake Flow
1. Orchestrator receives source document.
2. Orchestrator validates data classification and policy constraints.
3. Orchestrator runs OCR extraction via allowlisted read-only tool.
4. Orchestrator annotates extraction confidence and quality notes.
5. Orchestrator logs OCR call and extraction metadata.
6. Orchestrator passes extracted text as source context to subagents.

## 4. Confidence and Quality Annotation
Each OCR extraction must include:
- extraction_confidence_score (0.0-1.0)
- extraction_quality_note
- suspected_noise_areas
- suspected_missing_text_areas

## 5. Source Freshness and Provenance
For each OCR-derived source add:
- source_type: pdf | image
- extraction_timestamp_utc
- original_source_reference
- freshness_assessment

## 6. Pilot Success Criteria
Pilot is successful when:
- extraction is audit-logged for all test samples,
- confidence annotations are present in every extraction,
- no direct subagent OCR tool usage occurs,
- no policy violations are detected.

## 7. Pilot Risk Controls
- require human review for low-confidence extraction,
- mark OCR-derived uncertain claims as UNCERTAIN,
- block progression if critical sections are missing in extraction.
