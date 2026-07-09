# Ontology examples for microbiota metadata

Use ontology terms when they improve clarity, interoperability, and machine readability. Always verify the term label, definition, and identifier in an ontology lookup service before final submission.

Useful lookup services:

- [EMBL-EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols4/)
- [OBO Foundry](https://obofoundry.org/)
- [BioPortal](https://bioportal.bioontology.org/)
- [ZOOMA](https://www.ebi.ac.uk/spot/zooma/)

## General pattern

Prefer: [rhizosphere environment \[ENVO:01000999\]](http://purl.obolibrary.org/obo/ENVO_01000999) <br>
Avoid: soil near roots

Unless the target repository **explicitly** requires free text or no suitable ontology term exists in any of the lookup services.

## Examples by metadata field

|Metadata field | Weak entry | Better entry | Ontology / vocabulary | 
|---------------|------------|--------------|-----------------------|
|env_broad_scale	|forest	| [temperate woodland biome \[ENVO:01000221\]](http://purl.obolibrary.org/obo/ENVO_01000221)	| [ENVO](http://environmentontology.org/) |
|env_local_scale	|root soil	| [rhizosphere environment \[ENVO:01000999\]](http://purl.obolibrary.org/obo/ENVO_01000999)	|[ENVO](http://environmentontology.org/) |
|env_medium	|soil	| [soil \[ENVO:00001998\]](http://purl.obolibrary.org/obo/ENVO_00001998) [ENVO term selected from OLS]	|[ENVO](http://environmentontology.org/) |
|host scientific name	|human|	[Homo sapiens \[NCBITaxon:9606\]](http://purl.obolibrary.org/obo/NCBITaxon_9606)	| [NCBI Taxonomy](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) |
|host scientific name	|mouse	|[Mus musculus \[NCBITaxon:10090\]](http://purl.obolibrary.org/obo/NCBITaxon_10090)	| [NCBI Taxonomy](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) |
|host-associated body site	|gut	| [colon \[UBERON:0001155\]](http://purl.obolibrary.org/obo/UBERON_0001155) / intestinal region term selected from UBERON, depending on sampling site	| [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) |
|plant host	|Arabidopsis	| [Arabidopsis thaliana \[NCBITaxon:3702\]](http://purl.obolibrary.org/obo/NCBITaxon_3702)	| [NCBI Taxonomy](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) |
|plant structure	|leaf	| [leaf \[PO:0025034\]](http://purl.obolibrary.org/obo/PO_0025034) term selected from Plant Ontology	| [PO](https://www.ebi.ac.uk/ols4/ontologies/po) |
|sequencing method	|Illumina	| [Illumina Sequencing \[NCIT:C146817\]](http://purl.obolibrary.org/obo/NCIT_C146817)	| [NCIT](https://www.ebi.ac.uk/ols4/ontologies/ncit) |
|growth medium	|minimal medium	| [minimal defined medium \[MCO:0000881\]](http://purl.obolibrary.org/obo/MCO_0000881)	| [MCO](https://www.ebi.ac.uk/ols4/ontologies/mco) |
|chemical compound	|glucose	| [glucose \[CHEBI:17234\]](http://purl.obolibrary.org/obo/CHEBI_17234) term selected from ChEBI	| [ChEBI](https://www.ebi.ac.uk/ols4/ontologies/chebi) |
|disease state	|healthy / diseased	|use repository-recommended disease or phenotype ontology where applicable	| [DOID](https://www.ebi.ac.uk/ols4/ontologies/doid) / [MONDO](https://www.ebi.ac.uk/ols4/ontologies/mondo) / [HP](https://www.ebi.ac.uk/ols4/ontologies/hp) / [NCIT](https://www.ebi.ac.uk/ols4/ontologies/ncit), depending on context |

## Worked example: plant rhizosphere metagenome

A researcher collects metagenomic samples from the rhizosphere of a forest in Germany and sequences them using an Illumina platform.

Possible annotation:

|Field	|Value|
|-------|-----|
|env_broad_scale|	[temperate woodland biome \[ENVO:01000221\]](http://purl.obolibrary.org/obo/ENVO_01000221)|
|env_local_scale|	[rhizosphere environment \[ENVO:01000999\]](http://purl.obolibrary.org/obo/ENVO_01000999)|
|geo_loc_name|	[Naturpark Frankenwald \[GAZ:00632507\]](http://purl.obolibrary.org/obo/GAZ_00632507)|
|sequencing method|	[Illumina Sequencing \[NCIT:C146817\]](http://purl.obolibrary.org/obo/NCIT_C146817)|
|growth medium, if cultivation was performed	| [minimal defined medium \[MCO:0000881\]](http://purl.obolibrary.org/obo/MCO_0000881) |

## Practical checks before submission

- Does the ontology term actually describe the sample?
- Is the term too broad?
- Is the term too specific for the available evidence?
- Does the target repository accept this ontology?
- Does the repository require both a label and an identifier?
- Are free-text values still needed in addition to ontology IDs?
- Have all ontology IDs been checked in OLS, OBO Foundry, BioPortal, or a repository-specific lookup service?
