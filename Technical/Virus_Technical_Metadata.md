## 2.9 Minimal Information about a Genome Sequence: virus

## Minimal technical metadata for `virus FASTQ and FASTA` data

| **metadata** | **definition** | **examples** | **source** |                                                                                                                                                                    | **examples**                                           | **source**                                                                                                           |
|-----------------|----------------|-----------------|----------------|
| samp_name | A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name | - | [MIXS:0001107]{https://genomicsstandardsconsortium.github.io/mixs/0001107/} |
| lib_screen | Specific enrichment or screening methods applied before and/or after creating libraries | - | [MIXS:0000043]{https://genomicsstandardsconsortium.github.io/mixs/0000043/} |
| ref_db | List of database(s) used for ORF annotation, along with version number and reference to website or publication | - | [MIXS:0000062]{https://genomicsstandardsconsortium.github.io/mixs/0000062/} |
| nucl_acid_amp | A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids | - | [MIXS:0000038]{https://genomicsstandardsconsortium.github.io/mixs/0000038/} |
| lib_size | Total number of clones in the library prepared for the project | - | [MIXS:0000039]{https://genomicsstandardsconsortium.github.io/mixs/0000039/} |
| assembly_name | Name/version of the assembly provided by the submitter that is used in the genome browsers and in the community | - | [MIXS:0000057]{https://genomicsstandardsconsortium.github.io/mixs/0000057/} |
| temp | Temperature of the sample at the time of sampling | - | [MIXS:0000113]{https://genomicsstandardsconsortium.github.io/mixs/0000113/} |
| compl_score | Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores | - | [MIXS:0000069]{https://genomicsstandardsconsortium.github.io/mixs/0000069/} |
| nucl_acid_ext | A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample | - | [MIXS:0000037]{https://genomicsstandardsconsortium.github.io/mixs/0000037/} |
| samp_size | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected | - | [MIXS:0000001]{https://genomicsstandardsconsortium.github.io/mixs/0000001/} |
| isol_growth_condt | Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material| - | [MIXS:0000003]{https://genomicsstandardsconsortium.github.io/mixs/0000003/} |
| alt | Heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earth's surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air | - | [MIXS:0000094]{https://genomicsstandardsconsortium.github.io/mixs/0000094/} |
| source_mat_id | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2) | - | [MIXS:0000026]{https://genomicsstandardsconsortium.github.io/mixs/0000026/} |
| estimated_size | The estimated size of the genome prior to sequencing | - | [MIXS:0000024]{https://genomicsstandardsconsortium.github.io/mixs/0000024/} |
| samp_vol_we_dna_ext | Volume (ml) or mass (g) of total collected sample processed for DNA extraction. Note: total sample collected should be entered under the term Sample Size (MIXS:0000001) | - | [MIXS:0000111]{https://genomicsstandardsconsortium.github.io/mixs/0000111/} |
| pathogenicity | To what extent is the entity pathogenic | - | [MIXS:0000027]{https://genomicsstandardsconsortium.github.io/mixs/0000027/} |
| lib_reads_seqd | Total number of clones sequenced from the library | - | [MIXS:0000040]{https://genomicsstandardsconsortium.github.io/mixs/0000040/} |
| encoded_traits | Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage | - | [MIXS:0000034]{https://genomicsstandardsconsortium.github.io/mixs/0000034/} |
| propagation | The type of reproduction from the parent stock | - | [MIXS:0000033]{https://genomicsstandardsconsortium.github.io/mixs/0000033/} |
| samp_collect_device | The device used to collect an environmental sample | - | [MIXS:0000002]{https://genomicsstandardsconsortium.github.io/mixs/0000002/} |
| number_contig | Total number of contigs in the cleaned/submitted assembly that makes up a given genome, SAG, MAG, or UViG | - | [MIXS:0000060]{https://genomicsstandardsconsortium.github.io/mixs/0000060/} |
| biotic_relationship | Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object | - | [MIXS:0000028]{https://genomicsstandardsconsortium.github.io/mixs/0000028/} |
| num_replicons | Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote | - | [MIXS:0000022]{https://genomicsstandardsconsortium.github.io/mixs/0000022/} |
| lib_layout | Specify whether to expect single, paired, or other configuration of reads | - | [MIXS:0000041]{https://genomicsstandardsconsortium.github.io/mixs/0000041/} |
| assembly_qual | The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the large subunit (LSU) RNA, small subunit (SSU) and the presence of 5.8S rRNA or 5S rRNA depending on whether it is a eukaryotic or prokaryotic genome, respectively. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling 90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated | - | [MIXS:0000056]{https://genomicsstandardsconsortium.github.io/mixs/0000056/} |
| ref_biomaterial | Primary publication if isolated before genome publication; otherwise, primary genome report | - | [MIXS:0000025]{https://genomicsstandardsconsortium.github.io/mixs/0000025/} |
| project_name | Name of the project within which the sequencing was organized | - | [MIXS:0000092]{https://genomicsstandardsconsortium.github.io/mixs/0000092/} |
| lib_vector | Cloning vector type(s) used in construction of libraries | - | [MIXS:0000042]{https://genomicsstandardsconsortium.github.io/mixs/0000042/} |
| host_spec_range | The range and diversity of host species that an organism is capable of infecting, defined by NCBI taxonomy identifier | - | [MIXS:0000030]{https://genomicsstandardsconsortium.github.io/mixs/0000030/} |
| neg_cont_type | The substance or equipment used as a negative control in an investigation | - | [MIXS:0001321]{https://genomicsstandardsconsortium.github.io/mixs/0001321/} |
| virus_enrich_appr | List of approaches used to enrich the sample for viruses, if any | - | [MIXS:0000036]{https://genomicsstandardsconsortium.github.io/mixs/0000036/} |
| adapters | Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters | - | [MIXS:0000048]{https://genomicsstandardsconsortium.github.io/mixs/0000048/} |
| assembly_software | Tool(s) used for assembly, including version number and parameters | - | [MIXS:0000058]{https://genomicsstandardsconsortium.github.io/mixs/0000058/} |
| tax_ident | The phylogenetic marker(s) used to assign an organism name to the SAG or MAG | - | [MIXS:0000053]{https://genomicsstandardsconsortium.github.io/mixs/0000053/} |
| annot | Tool used for annotation, or for cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter | - | [MIXS:0000059]{https://genomicsstandardsconsortium.github.io/mixs/0000059/} |
| pos_cont_type | The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive | - | [MIXS:0001322]{https://genomicsstandardsconsortium.github.io/mixs/0001322/} |
| subspecf_gen_lin | Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g., serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123 | - | [MIXS:0000020]{https://genomicsstandardsconsortium.github.io/mixs/0000020/} |
| feat_pred | Method used to predict UViGs features such as ORFs, integration site, etc | - | [MIXS:0000061]{https://genomicsstandardsconsortium.github.io/mixs/0000061/} |
| env_local_scale | Report the entity or entities which are in the sample or specimen s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS | - | [MIXS:0000013]{https://genomicsstandardsconsortium.github.io/mixs/0000013/} |
| compl_software | Tools used for completion estimate, i.e. checkm, anvi'o, busco | - | [MIXS:0000070]{https://genomicsstandardsconsortium.github.io/mixs/0000070/} |
| samp_mat_process | A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed | - | [MIXS:0000016]{https://genomicsstandardsconsortium.github.io/mixs/0000016/} |
| sim_search_meth | Tool used to compare ORFs with database, along with version and cutoffs used | - | [MIXS:0000063]{https://genomicsstandardsconsortium.github.io/mixs/0000063/} |
| host_disease_stat | List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text | - | [MIXS:0000031]{https://genomicsstandardsconsortium.github.io/mixs/0000031/} |
| depth | The vertical distance below local surface | - | [MIXS:0000018]{https://genomicsstandardsconsortium.github.io/mixs/0000018/} |
| samp_collect_method | The method employed for collecting the sample | - | [MIXS:0001225]{https://genomicsstandardsconsortium.github.io/mixs/0001225/} |
| specific_host | Report the host's taxonomic name and/or NCBI taxonomy ID | - | [MIXS:0000029]{https://genomicsstandardsconsortium.github.io/mixs/0000029/} |
| env_medium | Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top) | - | [MIXS:0000014]{https://genomicsstandardsconsortium.github.io/mixs/0000014/} |
| samp_taxon_id | NCBI taxon id of the sample. Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome for mock community/positive controls, or 'blank sample' for negative controls | - | [MIXS:0001320]{https://genomicsstandardsconsortium.github.io/mixs/0001320/} |
| geo_loc_name | The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ) | - | [MIXS:0000010]{https://genomicsstandardsconsortium.github.io/mixs/0000010/} |
| collection_date | The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant | - | [MIXS:0000011]{https://genomicsstandardsconsortium.github.io/mixs/0000011/} |
| seq_meth | Sequencing machine used | - | [MIXS:0000050]{https://genomicsstandardsconsortium.github.io/mixs/0000050/} |
| lat_lon | The geographical origin of the sample as defined by latitude and longitude | - | [MIXS:0000009]{https://genomicsstandardsconsortium.github.io/mixs/0000009/} |
| elev | Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit | - | [MIXS:0000093]{https://genomicsstandardsconsortium.github.io/mixs/0000093/} |
| env_broad_scale | Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO s biome class: http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS | - | [MIXS:0000012]{https://genomicsstandardsconsortium.github.io/mixs/0000012/} |
| tax_class | Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes | - | [MIXS:0000064]{https://genomicsstandardsconsortium.github.io/mixs/0000064/} |
| experimental_factor | Variable aspects of an experiment design that can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI) | - | [MIXS:0000008]{https://genomicsstandardsconsortium.github.io/mixs/0000008/} |
| associated_resource | A related resource that is referenced, cited, or otherwise associated to the sequence | - | [MIXS:0000091]{https://genomicsstandardsconsortium.github.io/mixs/0000091/} |
| sop | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences | - | [MIXS:0000090]{https://genomicsstandardsconsortium.github.io/mixs/0000090/} |

| Comments/questions:                                                     |
|------------------------------------------------------------------------|
| From [https://genomicsstandardsconsortium.github.io/mixs/0010005/](https://genomicsstandardsconsortium.github.io/mixs/0010005/) |


The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** (Field et al. 2008),
**Minimum information about a marker gene sequence (MIMARKS) and minimum
information about any (x) sequence (MIxS) specifications** (Yilmaz et
al. 2011), **Minimum information about a single amplified genome (MISAG)
and a metagenome-assembled genome (MIMAG) of bacteria and archaea**
(Bowers et al. 2017), **Minimum Information about an Uncultivated Virus
Genome (MIUViG)** (Roux et al. 2019) and **Roadmap for naming
uncultivated Archaea and Bacteria** (Murray et al. 2020) can be found
online.

# References

Bowers, R., N. Kyrpides, R. Stepanauskas, et al. 2017. “Minimum
Information about a Single Amplified Genome (MISAG) and a
Metagenome-Assembled Genome (MIMAG) of Bacteria and Archaea.” *Nat
Biotechnol* 35: 725–31. <https://doi.org/10.1038/nbt.3893>.

“ENA How to Submit Other Analyses: Submitting Read Alignments.”
<https://ena-docs.readthedocs.io/en/latest/submit/analyses/read-alignments.html>.

“ENA Metadata Validation: Instrument.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument>.

“ENA Metadata Validation: Selection.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection>.

“ENA Metadata Validation: Source.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source>.

“ENA Metadata Validation: Strategy.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy>.

“ENA Submitting Metagenome Assemblies.”
<https://ena-docs.readthedocs.io/en/latest/submit/assembly/metagenome.html>.

Field, D., G. Garrity, T. Gray, N. Morrison, J. Selengut, P. Sterk, T.
Tatusova, et al. 2008. “The Minimum Information about a Genome Sequence
(MIGS) Specification.” Nature Biotechnology. 2008.
<https://doi.org/10.1038/nbt1360>.

“GSC MIXS: MIMAG.”
<https://genomicsstandardsconsortium.github.io/mixs/0010011/>.

"GSC MIXS: MIGSVI."
<https://genomicsstandardsconsortium.github.io/mixs/0010005/>

Leinonen, R., H. Sugawara, M. Shumway, and International Nucleotide
Sequence Database Collaboration. 2011. “The Sequence Read Archive.”
*Nucleic Acids Research* 39 (Database issue): D19–21.
<https://doi.org/10.1093/nar/gkq1019>.

“GSC MIXS: MIUVIG.”
<https://genomicsstandardsconsortium.github.io/mixs/0010012/>.

Murray, A. E., J. Freudenstein, S. Gribaldo, et al. 2020. “Roadmap for
Naming Uncultivated Archaea and Bacteria.” *Nat Microbiol* 5: 987–94.
<https://doi.org/10.1038/s41564-020-0733-x>.

NCBI Hackathons. “<span class="nocase">SRA-Tinder: A Tool to Discover
Related Sequence Read Archive (SRA) Experiments</span>.”
<https://github.com/NCBI-Hackathons/SRA_Tinder>.

Roux, Simon, Evelien Adriaenssens, Bas Dutilh, and et al. 2019. “Minimum
Information about an Uncultivated Virus Genome (MIUViG).” *Nature
Biotechnology* 37: 29–37. <https://doi.org/10.1038/nbt.4306>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
