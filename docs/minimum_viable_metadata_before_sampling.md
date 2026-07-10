Use this checklist before sampling or before starting data generation. It is intended to reduce missing metadata at the point of repository submission.

## A. Study-level planning

- [ ] Define the study title and short description.
- [ ] Define the main research question.
- [ ] Define the sample groups, treatments, controls, and time points.
- [ ] Define biological replicates and technical replicates.
- [ ] Define the expected data types: amplicon, genome, metagenome, MAG, transcriptome, metatranscriptome, proteome, metaproteome, metabolome, virus/uVIG.
- [ ] Select the likely target repository before data generation.
- [ ] Check whether the target repository requires a specific checklist, template, package, or accession structure.
- [ ] Check whether the data are open, embargoed, restricted, or controlled access.
- [ ] Check whether ethics approval, consent, GDPR, Nagoya Protocol, pathogen-risk, conservation, or institutional restrictions apply.

## B. Identifier planning

- [ ] Define a stable sample identifier format.
- [ ] Ensure sample identifiers do not contain spaces or special characters that repositories reject.
- [ ] Ensure sample identifiers are unique within the study.
- [ ] Define how biological replicates, technical replicates, subsamples, extracts, libraries, and files will be linked.
- [ ] Define parent-child relationships between original samples, derived samples, DNA/RNA/protein/metabolite extracts, libraries, runs, and processed outputs.
- [ ] Decide where accession numbers, DOIs, and reviewer links will be recorded after submission.

## C. Sampling metadata

- [ ] Record who collected the sample.
- [ ] Record collection date and, where appropriate, time zone.
- [ ] Record geographic location using the repository-required format.
- [ ] Record latitude/longitude where allowed.
- [ ] Record whether exact coordinates must be restricted.
- [ ] Record sample material.
- [ ] Record sample amount or size.
- [ ] Record sampling device and sampling method.
- [ ] Record environmental context, host context, or built/wastewater system context.
- [ ] Record temperature, pH, salinity, depth, altitude, or other context-specific measurements where relevant.
- [ ] Record sample storage conditions and transport conditions.
- [ ] Record preservation method and time between collection and processing.

## D. Host-associated metadata, if applicable

- [ ] Record host scientific name with NCBI Taxonomy identifier where possible.
- [ ] Record host body site, tissue, organ, or material using an ontology term where possible.
- [ ] Record host age, sex, genotype, phenotype, diet, treatment, disease state, or other relevant factors where ethically and legally allowed.
- [ ] Record whether any host-associated metadata must be restricted or generalized.
- [ ] Record consent/access limitations for human-associated samples.

## E. Technical metadata

- [ ] Record extraction protocol or kit.
- [ ] Record nucleic acid, protein, or metabolite extraction method.
- [ ] Record library preparation method, if applicable.
- [ ] Record sequencing, mass spectrometry, NMR, or other instrument platform.
- [ ] Record instrument model and software versions where available.
- [ ] Record read layout, read length, library strategy, and library source for sequencing data.
- [ ] Record assembly, binning, annotation, or processing software versions and parameters.
- [ ] Record quality-control steps and thresholds.
- [ ] Record raw-file names, processed-file names, and file relationships.
- [ ] Record checksums for deposited files where possible.

## F. Ontologies and controlled vocabularies

- [ ] Identify which fields should use ontology terms.
- [ ] Select terms from appropriate resources, such as ENVO, NCBI Taxonomy, UBERON, PO, ChEBI, GO, NCIT, MCO, or repository-specific vocabularies.
- [ ] Record both labels and identifiers where possible.
- [ ] Verify terms in OLS, OBO Foundry, BioPortal, ZOOMA, or a repository-specific lookup service.
- [ ] Avoid using ontology identifiers that have not been checked.

## G. Missing-value planning

- [ ] Decide how missing values will be reported before data entry starts.
- [ ] Do not use blank cells for required metadata fields.
- [ ] Distinguish between `not applicable`, `not available`, `not recorded`, `not provided`, and `restricted access`.
- [ ] Use repository-approved missing-value tokens where available.
- [ ] Document why sensitive values are restricted.

## H. License and access planning

- [ ] Decide the license for data.
- [ ] Decide the license for metadata.
- [ ] Decide the license for code/scripts, if included.
- [ ] Check whether the target repository supports the chosen license.
- [ ] Check whether institutional, funder, ethics, or legal requirements restrict reuse.
- [ ] Record embargo dates, access conditions, and data-use limitations.

## I. Pre-submission validation

- [ ] Test the selected repository submission route early, before manuscript submission.
- [ ] Download or inspect repository templates.
- [ ] Run repository validation where available.
- [ ] Resolve all required-field errors.
- [ ] Resolve ontology or controlled-vocabulary warnings where possible.
- [ ] Confirm that all files listed in metadata are actually present.
- [ ] Confirm that all checksums match.
- [ ] Confirm that sample IDs match across metadata, raw files, processed files, and analysis outputs.

## J. Manuscript readiness

- [ ] Record final repository accession numbers.
- [ ] Record DOI, if available.
- [ ] Record reviewer/private-access link, if available.
- [ ] Record release or embargo date.
- [ ] Prepare the Data Availability Statement.
- [ ] Ensure the Data Availability Statement matches the actual repository record.
- [ ] Archive the final submitted metadata table with the project documentation.
