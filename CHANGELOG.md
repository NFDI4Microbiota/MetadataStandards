# Changelog

All notable changes to the NFDI4Microbiota Metadata Standards repository are documented here.

This repository provides practical orientation for microbiota researchers preparing metadata for public deposition. It does not define a new metadata standard and does not replace repository-specific submission systems.

## [Unreleased]

### Added

- Added a Quick Start workflow for First Stage Researchers preparing microbiota metadata before repository submission.
- Added a compact repository-mapping guide that links data types to appropriate domain-specific and generalist repositories.
- Added external validation and submission resources, including ENA Webin/Webin-CLI, the EMBL-EBI Data Submission Wizard, NCBI SRA Submission Portal, DDBJ D-way/DRA, PRIDE/ProteomeXchange, MetaboLights, Metabolomics Workbench, MassIVE/GNPS, NMDC schema/submission resources, Zenodo, Figshare, EGA, dbGaP, and JGA.
- Added ontology examples for common microbiota metadata fields, including environmental context, host taxonomy, body site/material, sequencing method, growth medium, and chemical compounds.
- Added a “minimum viable metadata before sampling” checklist to support metadata planning before data generation.
- Added guidance that points users to the NFDI4Microbiota Knowledge Base for general repository-selection criteria, licensing background, RDM explanations, and broader ontology training.

### Changed

- Reorganized user-facing guidance so that the repository focuses on metadata preparation and submission orientation, while broader RDM explanations are delegated to the NFDI4Microbiota Knowledge Base.
- Clarified that repository-specific validators and submission portals remain the authoritative validation route before final deposition.
- Clarified that missing-value terms should follow repository-specific accepted tokens whenever those are available.

### To fix before release

- Separate `standard_id`, `source_checklist`, and `source_url` in schema files where checklist names are currently stored in `MIXS_ID`.

## [1.1.0] - 2026-07-08

### Added

- Added a stronger repository scope statement to the README, clarifying that the repository helps researchers identify metadata fields, standards, ontology terms, licensing choices, and missing-value reporting practices before deposition.
- Added an explicit statement that the repository does not define a new metadata standard and does not replace ENA, NCBI SRA, DDBJ, PRIDE, MetaboLights, Metabolomics Workbench, MassIVE/GNPS, or other repository submission systems.
- Added and/or expanded explanations of controlled vocabularies, ontologies, and missing-value reporting.
- Added practical ontology examples for microbiota metadata annotation.
- Added schema files using `schema` naming for biological/environmental metadata artefacts.

### Changed

- Renamed the user-facing README section from “Reading this Github” to “How to use this repository”.
- Revised the README for clarity and updated repository purpose and usage instructions.
- Clarified the distinction between controlled vocabularies and ontologies.
- Updated technical metadata documentation for metagenomic, transcriptomic, metatranscriptomic, proteomic, metabolomic, virus, uVIG, BIOM/tabular, and data-transfer/data-integrity sections.
- Refined formatting and references in metagenomic FASTQ metadata.
- Refined transcriptomic FASTQ metadata definitions.
- Updated metatranscriptomic FASTQ formatting and removed provisional notes.
- Refactored data-transfer and data-integrity documentation structure.

### Fixed

- Fixed several malformed URLs in biological/environmental metadata schema files.
- Fixed or improved malformed table formatting in the virus technical metadata page.
- Removed unresolved “comments/questions” sections from technical metadata documentation.
- Removed internal comments from uVIG, virus, BIOM/tabular, data-transfer/data-integrity, proteome, metabolome, transcriptome, metatranscriptome, and metagenome documentation where applicable.
- Fixed ontology formatting in `Human_BioEnv_Metadata.md`.

### Removed

- Removed the `insert_length` row from the transcriptomic technical metadata table.
- Removed provisional notes and comments that were not suitable for public release.

## [1.0.0] - 2023-08-14

### Added

- Added bibliography file.
- Added new table figures and GIFs.
- Added updated technical and biological/environmental metadata tables with references.
- Added hyperlinks to metadata standards, standards repositories, and tools.
- Added introductory text and license badge.
- Added `LICENSE`, `CHANGELOG.md`, and `NEXT_VERSION.md`.

### Changed

- Applied aesthetic updates to repository documentation.
