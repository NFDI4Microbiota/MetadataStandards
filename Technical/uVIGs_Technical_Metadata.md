## 2.9 Uncultivated Virus Genome

## Minimal technical metadata for `uVIG FASTQ` data

| **metadata**         | **definition**                                                                                                                                                                        | **examples**                                           | **source**                                                                                                           |
|-----------------|---------------------|------------------|-----------------|
| sample_name          | Identifier of the sample                                                                                                                                                              | e.g. ISDsoil1                                          | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                  |
| seq_meth             | Sequencing method used                                                                                                                                                                | e.g. 454 Genome Sequencer FLX OBI:0000702              | **GSC MIxS/MIGS Miuvig** (“Miuvig”), **ENA Metadata Validation: Instrument** (“ENA Metadata Validation: Instrument”) |
| lib_layout           | Specify whether to expect single, paired, or other configuration of reads                                                                                                             | e.g. single-end, paired end or others                  | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                  |
| lib_source           | The lib_source specifies the type of source material that is being sequenced                                                                                                          | e.g. genomic, metagenomic, transcriptomic, etc.        | **ENA Metadata Validation: Source** (“ENA Metadata Validation: Source”)                                              |
| lib_strategy         | Sequencing technique intended for this library                                                                                                                                        | e.g. WGS, Amplicon, etc.                               | **ENA Metadata Validation: Strategy** (“ENA Metadata Validation: Strategy”)                                          |
| lib_selection        | Whether any method was used to select and/or enrich the material being sequenced                                                                                                      | e.g. Random, PCR, etc.                                 | **ENA Metadata Validation: Selection** (“ENA Metadata Validation: Selection”)                                        |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                                                                                                                          | e.g. 32,283,453                                        | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                     |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                                                                                                                          | e.g. 6,400,000,000                                     | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                     |
| average_length       | As basepairs_count divided by sequence_count                                                                                                                                          | e.g. 198                                               | **Calculated as basepairs_count/sequence_count**                                                                     |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering                                                                                                             |                                                        | **SRA-Tinder** (NCBI Hackathons)                                                                                     |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering                                                                                                             |                                                        | **SRA-Tinder** (NCBI Hackathons)                                                                                     |
| checksum             | Hash value for data integrity                                                                                                                                                         | e.g. MD5: cbc41d0e49636872a765b950cb7f410a             | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                  |
| nucl_acid_amp        | A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids | <https://phylogenomics.me/protocols/16s-pcr-protocol/> | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                  |

| Comments/questions:                                                     |
|------------------------------------------------------------------------|
| Should we also add nucl_ext_method and nucl_extr_treat here -MB 11AUG23 |

## Minimal technical metadata for `uVIG FASTQ` data

| **metadata**       | **definition**                                                                                                                                                                              | **examples**                                                                                                                                                                                            | **source**                                                                                                         |
|-----------------|---------------------|------------------|-----------------|
| run_ref            | Accessions/identifiers linking to the raw data (FASTQ)                                                                                                                                      | e.g. accession = “ERR178314”                                                                                                                                                                            | **Adapted from ENA** (“ENA How to Submit Other Analyses: Submitting Read Alignments”)                              |
| tax_ident          | The phylogenetic marker(s) used to assign an organism name to the SAG or MAG                                                                                                                | e.g. 16s rRNA gene, multi-marker approach, other                                                                                                                                                        | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| assembly_qual      | The assembly quality category is based on sets of criteria outlined for each assembly quality category.                                                                                     | e.g. Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| assembly_software  | Tool(s) used, version and parameters                                                                                                                                                        | e.g. metaSPAdes (3.11.0);kmer set 21,33,55,77,99,121, default parameters otherwise                                                                                                                      | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| mag_cov_software   | Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of uVIGs from metagenomic datasets                                               | e.g. bbmap, bowtie, bwa, other                                                                                                                                                                          | **ENA Submitting Metagenome Assemblies** (“ENA Submitting Metagenome Assemblies”)                                  |
| vir_ident_software | Tool(s) used for the identification of UViG as a viral genome, software or protocol name including version number, parameters, and cutoffs used                                             | e.g. VirSorter; 1.0.4; Virome database, category 2                                                                                                                                                      | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| number_contig      | Total number of contigs in the cleaned/submitted assembly that makes up a given UViG                                                                                                        | e.g. 40                                                                                                                                                                                                 | **GSC MIxS/MIGS Miuvig** (“Miuvig”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020) |
| N50                | The length of the shortest contig representing half of the assembly length                                                                                                                  |                                                                                                                                                                                                         | **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)                                      |
| trnas              | Total number of tRNAs identified from the MAG                                                                                                                                               | e.g. 18                                                                                                                                                                                                 | **GSC MIxS/MIGS Miuvig** (“Miuvig”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020) |
| trna_ext_software  | Tools used for tRNA identification                                                                                                                                                          | e.g. infernal (v2); default parameters                                                                                                                                                                  | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| compl_score        | Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. | e.g. med; 60%                                                                                                                                                                                           | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                            |
| compl_software     | Tools used for completion estimate                                                                                                                                                          | e.g. checkm (v1.1.6), anvi’o, busco                                                                                                                                                                     | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| source_uvig        | Type of dataset from which the UViG was obtained                                                                                                                                            | e.g. viral fraction metagenome (virome)                                                                                                                                                                 | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |
| pathogenicity      | To what is the entity pathogenic                                                                                                                                                            | e.g. human, animal, plant, fungi, bacteria                                                                                                                                                              | **GSC MIxS/MIGS Miuvig** (“Miuvig”)                                                                                |

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
<https://genomicsstandardsconsortium.github.io/mixs/MIMAG/>.

Leinonen, R., H. Sugawara, M. Shumway, and International Nucleotide
Sequence Database Collaboration. 2011. “The Sequence Read Archive.”
*Nucleic Acids Research* 39 (Database issue): D19–21.
<https://doi.org/10.1093/nar/gkq1019>.

“Miuvig.” <https://genomicsstandardsconsortium.github.io/mixs/Miuvig/>.

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
