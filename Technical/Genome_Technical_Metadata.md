## 2.1 Genome sequencing

A searchable and exportable tab-separated
[table](Genome_Technical_Metadata.tsv) of the following metadata is now
available.

## Minimal technical metadata for `Genomic FASTQ` data

| **metadata**         | **definition**                                                                                                                                                                                                                                                                                                                                                                                                             | **reference of definition\[<url_to_definition>\]**                                                                                       | **expected unit of measurement**                                    | **example**                                     | **sources (where this or similar matadata field is mentioned)**                                                                        |     |
|--------|-----------|----------|---------|----------|----------|----------------|
| samp_name            | A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. | [MIXS:0001107](https://genomicsstandardsconsortium.github.io/mixs/0001107/)                                                              | free text with identifier                                           | e.g. ISDsoil1                                   | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |     |
| seq_meth             | Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (<http://purl.obolibrary.org/obo/OBI_0400103>)                                                                                                                                                                                                                                                                        | [MIXS:0000050](https://genomicsstandardsconsortium.github.io/mixs/0000050/)                                                              | <name_of_seq_machine>\[ontology\]                                   | e.g. 454 Genome Sequencer FLX \[OBI:0000702\]   | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **ENA Metadata Validation: Instrument** (“ENA Metadata Validation: Instrument”) |     |
| lib_layout           | Specify whether to expect single, paired, or other configuration of reads                                                                                                                                                                                                                                                                                                                                                  | [MIXS:0000041](https://genomicsstandardsconsortium.github.io/mixs/0000041/)                                                              | free text string                                                    | e.g. single-end                                 | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |     |
| lib_source           | The lib_source specifies the type of source material that is being sequenced                                                                                                                                                                                                                                                                                                                                               | [Link to permitted values](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#permitted-values-for-library-source)    | Free text from selected list of values                              | e.g. GENOMIC, METAGENOMIC, TRANSCRIPTOMIC, etc. | **ENA Metadata Validation: Source** (“ENA Metadata Validation: Source”)                                                                |     |
| lib_strategy         | Sequencing technique intended for this library                                                                                                                                                                                                                                                                                                                                                                             | [Link to permitted values](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#permitted-values-for-library-strategy)  | Free text from selected list of values                              | e.g. WGS, WGA, Amplicon, etc.                   | **ENA Metadata Validation: Strategy** (“ENA Metadata Validation: Strategy”)                                                            |     |
| lib_selection        | Whether any method was used to select and/or enrich the material being sequenced                                                                                                                                                                                                                                                                                                                                           | [Link to permitted values](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#permitted-values-for-library-selection) | Free text from selected list of values                              | e.g. RANDOM, PCR, cDNA_oligo_dT etc.            | **ENA Metadata Validation: Selection** (“ENA Metadata Validation: Selection”)                                                          |     |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                                                                                                                                                                                                                                                                                                                                                               | e.g. 32,283,453                                                                                                                          | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                    |                                                 |                                                                                                                                        |     |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                                                                                                                                                                                                                                                                                                                                                               | e.g. 6,400,000,000                                                                                                                       | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                    |                                                 |                                                                                                                                        |     |
| average_length       | As basepairs_count divided by sequence_count                                                                                                                                                                                                                                                                                                                                                                               | e.g. 198                                                                                                                                 | **Calculated as basepairs_count/sequence_count**                    |                                                 |                                                                                                                                        |     |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                          | **SRA-Tinder** (NCBI Hackathons)                                    |                                                 |                                                                                                                                        |     |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                          | **SRA-Tinder** (NCBI Hackathons)                                    |                                                 |                                                                                                                                        |     |
| checksum             | Hash value for data integrity                                                                                                                                                                                                                                                                                                                                                                                              | e.g. MD5: cbc41d0e49636872a765b950cb7f410a                                                                                               | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md) |                                                 |                                                                                                                                        |     |

| Comments/questions:                                                     |
|------------------------------------------------------------------------|
| Should we also add nucl_ext_method and nucl_extr_treat here -MB 11AUG23 |

## Minimal technical metadata for `Genomic FASTA` data

| **metadata**         | **definition**                                                               | **reference of definition\[<url_to_definition>\]**                                 | **expected unit of measurement**                                                                                                     |
|-----------------|---------------------|------------------|-----------------|
| run_ref              | Accessions/identifiers linking to the raw data (FASTQ)                       | e.g. accession = “ERR178314”                                                       | **Adapted from ENA** (“ENA How to Submit Other Analyses: Submitting Read Alignments”)                                                |
| tax_ident            | The phylogenetic marker(s) used to assign an organism name to the SAG or MAG | e.g. 16s rRNA gene, multi-marker approach, other                                   | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| assembly_qual        | Assembly quality category                                                    | e.g. Medium Quality Draft                                                          | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| assembly_software    | Tool(s) used, version and parameters                                         | e.g. metaSPAdes (3.11.0);kmer set 21,33,55,77,99,121, default parameters otherwise | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| coverage             | The estimated depth of sequencing coverage (in x)                            |                                                                                    | **ENA Submitting Metagenome Assemblies** (“ENA Submitting Metagenome Assemblies”)                                                    |
| number_contig        | Total number of contigs                                                      | e.g. 40                                                                            | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020) |
| N50                  | The length of the shortest contig representing half of the assembly length   |                                                                                    | **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)                                                        |
| LSU_recover          | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E)                          | e.g. yes                                                                           | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| LSU_recover_software | Tools for LSU extraction                                                     |                                                                                    | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover          | Detection of the 16S rRNA (BA) or 18S rRNA (E)                               | e.g. yes                                                                           | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover_software | Tools for SSU extraction                                                     | e.g. rambl (v2); default parameters                                                | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| trnas                | Total number of tRNAs identified from the MAG                                | e.g. 18                                                                            | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)               |
| trna_ext_software    | Tools used for tRNA identification                                           | e.g. infernal (v2); default parameters                                             | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_score          | Completeness score                                                           | e.g. med; 60%                                                                      | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_software       | Tools used for completion estimate                                           | e.g. checkm (v1.1.6)                                                               | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_score         | Contamination score                                                          | e.g. 0.01                                                                          | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_software      | Tool(s) used in contamination screening                                      | e.g. checkm (v1.1.6)                                                               | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** (Field et al. 2008),
**Minimum information about a marker gene sequence (MIMARKS) and minimum
information about any (x) sequence (MIxS) specifications** (Yilmaz et
al. 2011), **Minimum information about a single amplified genome (MISAG)
and a metagenome-assembled genome (MIMAG) of bacteria and archaea**
(Bowers et al. 2017), and **Roadmap for naming uncultivated Archaea and
Bacteria** (Murray et al. 2020) can be found online.

We also encourage our readers to have a look at the **HumanMetagenomeDB:
a public repository of curated and standardized metadata for human
metagenomes** (Kasmanas et al. 2021) and **TerrestrialMetagenomeDB: a
public repository of curated and standardized metadata for terrestrial
metagenomes** (Corrêa et al. 2020) to better understand some of the
metadata fields that can be found in the tables above.

# References

Bowers, R., N. Kyrpides, R. Stepanauskas, et al. 2017. “Minimum
Information about a Single Amplified Genome (MISAG) and a
Metagenome-Assembled Genome (MIMAG) of Bacteria and Archaea.” *Nat
Biotechnol* 35: 725–31. <https://doi.org/10.1038/nbt.3893>.

Corrêa, Fabio B., João P. Saraiva, Peter F. Stadler, and Ulisses N. da
Rocha. 2020. “TerrestrialMetagenomeDB: A Public Repository of Curated
and Standardized Metadata for Terrestrial Metagenomes.” *Nucleic Acids
Research* 48 (D1): D626–32.
<https://academic.oup.com/nar/article/48/D1/D626/5625925>.

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

“GSC MIXS: MIGSBacteria.”
<https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/>.

“GSC MIXS: MIMAG.”
<https://genomicsstandardsconsortium.github.io/mixs/MIMAG/>.

Kasmanas, João C., Alexander Bartholomäus, Fabio B. Corrêa, Tal Tal,
Nico Jehmlich, Gunda Herberth, Martin von Bergen, Peter F. Stadler,
Alinne de Carvalho, and Ulisses N. da Rocha. 2021. “HumanMetagenomeDB: A
Public Repository of Curated and Standardized Metadata for Human
Metagenomes.” *Nucleic Acids Research* 49 (D1): D743–50.
<https://academic.oup.com/nar/article/49/D1/D743/5998395>.

Leinonen, R., H. Sugawara, M. Shumway, and International Nucleotide
Sequence Database Collaboration. 2011. “The Sequence Read Archive.”
*Nucleic Acids Research* 39 (Database issue): D19–21.
<https://doi.org/10.1093/nar/gkq1019>.

Murray, A. E., J. Freudenstein, S. Gribaldo, et al. 2020. “Roadmap for
Naming Uncultivated Archaea and Bacteria.” *Nat Microbiol* 5: 987–94.
<https://doi.org/10.1038/s41564-020-0733-x>.

NCBI Hackathons. “<span class="nocase">SRA-Tinder: A Tool to Discover
Related Sequence Read Archive (SRA) Experiments</span>.”
<https://github.com/NCBI-Hackathons/SRA_Tinder>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
