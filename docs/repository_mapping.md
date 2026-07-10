# Repository mapping for microbiota metadata preparation

<p align="center">
  <img src="../images/manuscript/FIG_4_2026-01-08_Community_metadata_standards_integrated_into_data_submission_workflows.png"
       alt="Community metadata standards integrated into data submission workflows."
       width="850">
</p>

**Figure 1. Community metadata standards integrated into data submission workflows.** Adapted from the associated manuscript figure. Created in BioRender.

---
This page provides a compact orientation for choosing a likely repository route during metadata preparation.

For general repository-selection criteria, repository finders, and a broader microbiology repository list, see the [NFDI4Microbiota Knowledge Base - Data Repositories](https://knowledgebase.nfdi4microbiota.de/RDM-Share/data-repositories.html)

This page does not replace repository-specific submission guidance.

| Data type / output | Likely repository route | Submission / validation resource | Use this GitHub repository for |
|---|---|---|---|
| Amplicon reads | ENA / NCBI SRA / DDBJ-DRA | ENA Webin, NCBI SRA Submission Portal, DDBJ D-way | Preparing sample, technical, and biological/environmental metadata before submission |
| Genomes | ENA / GenBank / DDBJ | ENA Webin/Webin-CLI, NCBI Submission Portal, DDBJ workflows | Preparing sequencing, assembly, organism, and provenance metadata |
| Metagenomes | ENA / NCBI SRA / DDBJ-DRA | ENA checklists, Webin/Webin-CLI, NCBI SRA Portal, DDBJ DRA validation | Preparing MIxS-aligned sample/context metadata |
| MAGs | ENA / NCBI / DDBJ assembly-related routes | Repository-specific assembly/MAG submission routes | Preparing assembly quality, binning, completeness, contamination, and provenance metadata |
| Metatranscriptomes | ENA / NCBI SRA / DDBJ-DRA; possibly GEO/ArrayExpress/GEA for processed expression outputs | ENA Webin, NCBI SRA/GEO guidance, DDBJ DRA/GEA | Preparing raw-read and experimental metadata |
| Transcriptomes | ENA / NCBI SRA / DDBJ-DRA; GEO/ArrayExpress/GEA for expression matrices where appropriate | ENA, NCBI, DDBJ repository-specific workflows | Preparing sequencing, library, sample, and analysis metadata |
| Proteomics | PRIDE / ProteomeXchange; MassIVE where appropriate | PX Submission Tool, PRIDE guidance, MassIVE submission | Preparing sample, instrument, protocol, and analysis metadata |
| Metaproteomics | PRIDE / ProteomeXchange or MassIVE | PX Submission Tool or MassIVE | Add a metaproteome-specific page/template before advertising full repository coverage |
| Metabolomics | MetaboLights or Metabolomics Workbench | MetaboLights Guided Submission/validation; Metabolomics Workbench upload/manage studies | Preparing biological, analytical, sample, assay, and metabolite metadata |
| MS/MS spectral data / molecular networking | MassIVE / GNPS | MassIVE/GNPS submission workflows | Preparing file manifest, sample mapping, and provenance metadata |
| Virus genomes / uVIGs | ENA / NCBI / DDBJ sequence repositories; specialised pathogen resources where appropriate | ENA/NCBI/DDBJ validation and pathogen-specific guidance where applicable | Preparing MIxS/MIUViG-related metadata |
| General supplementary files, scripts, figures, release archives | Zenodo, Figshare, institutional repository | Repository deposit form and DOI metadata | Preparing citation, license, file manifest, and access metadata |
| Sensitive human genotype/phenotype or omics data | EGA, dbGaP, JGA, or national controlled-access archive | Controlled-access submission and governance workflow | Preparing non-sensitive metadata and access-condition documentation before controlled-access submission |

## Submission helper tools and converters

The resources below may help with metadata conversion, checklist mapping, or repository submission. They are listed as practical aids, not as replacements for the official target repository. Always check the current documentation of the target repository before final deposition.

| Tool or workflow | Main use | Likely repository / data route | Notes |
|---|---|---|---|
| [ENA Webin / Webin-CLI](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/webin-cli.html)| Official ENA submission and validation route | ENA | Recommended route for many sequence-read, assembly, and analysis submissions to ENA. |
| [EMBL-EBI Data Submission Wizard](https://www.ebi.ac.uk/submission/) | Helps identify the appropriate EMBL-EBI archive | EMBL-EBI archives | Useful when users are unsure whether data belong in ENA, BioSamples, PRIDE, MetaboLights, ArrayExpress/BioStudies, or another EMBL-EBI archive. |
| [ENA Sample Checklists / BioSamples validation](https://www.ebi.ac.uk/ena/browser/checklists)| Checklist selection and sample metadata requirements | ENA / BioSamples | Useful for identifying mandatory, recommended, and optional metadata fields. |
| [annonex2embl](https://pypi.org/project/annonex2embl/) | Conversion/support for preparing EMBL/ENA-compatible annotation or submission files | ENA / EMBL-style sequence submission | Include as a helper tool where applicable; users still need to validate through ENA. |
| [EMBL2checklists](https://pypi.org/project/EMBL2checklists/) | Mapping or conversion support between EMBL-style metadata and checklist requirements | ENA checklists | Useful where users need to align existing EMBL/ENA-style records with checklist-based metadata expectations. |
| [Galaxy ENA upload](https://usegalaxy.eu/root?tool_id=ena_upload) | Galaxy-based workflow for submitting data to ENA | ENA | Useful for users already working in Galaxy or who prefer a graphical workflow environment. |
| [genome.uploader](https://github.com/EBI-Metagenomics/genome_uploader) | Genome submission helper | Genome/assembly repositories, depending on implementation | Include only with the exact tool link and scope; name is generic and should be disambiguated. |
| [METAGENOTE](https://github.com/niaid/metagenote) | Metagenome-oriented metadata annotation or submission support | Metagenomics / ENA-related workflows, depending on implementation | Useful to list as a metagenomics-specific support tool if the exact project link is available. |
| [subMG](https://github.com/metagenomics/subMG) | Automates data submission for metagenomics studies | Metagenomics submissions | Useful for reducing technical overhead in specific deposition tasks, but not a general metadata harmonisation framework. |
| [NMDC Submission Portal / NMDC submission schema](https://data.microbiomedata.org/submission/home) | Structured microbiome metadata entry and validation | NMDC-supported microbiome metadata workflows | Useful for ontology-integrated, MIxS-like metadata preparation; not a replacement for all target repositories. |

These tools vary in scope and maintenance status. They should be treated as practical support resources rather than authoritative standards. The authoritative requirements remain those of the target repository and its current submission documentation.

## Important rule

Use domain-specific repositories first. Use generalist repositories for supplementary files, release artefacts, or data types without a suitable domain-specific repository.

## Repository discovery

Use these external resources when no clear repository is obvious:

- [NFDI4Microbiota Knowledge Base - Data Repositories](https://knowledgebase.nfdi4microbiota.de/RDM-Share/data-repositories.html)
- [FAIRsharing](https://fairsharing.org/)
- [re3data](https://www.re3data.org/)
- [ELIXIR deposition database resources](https://elixir-europe.org/platforms/data/elixir-deposition-databases)
