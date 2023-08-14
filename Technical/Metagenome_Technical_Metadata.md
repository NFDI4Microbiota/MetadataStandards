## 2.3 Metagenome sequencing

A searchable and exportable tab-separated
[table](Metagenome_Technical_Metadata.tsv) of the following metadata is
now available.

## Minimal technical metadata for `Metagenomic FASTQ` data

  🔹 *italics = potential considerations*

| **metadata**         | **definition/examples**                                                                                     | **source**                                                                                                                             |
|------------------|------------------------------------|------------------|
| sample_name          | Identifier of the sample                                                                                    | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| seq_meth             | Sequencing method used (e.g. Illumina HiSeq 2000)                                                           | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **ENA Metadata Validation: Instrument** (“ENA Metadata Validation: Instrument”) |
| lib_layout           | Single-end, paired end or others                                                                            | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| lib_source           | Genomic, metagenomic, transcriptomic, etc.                                                                  | **ENA Metadata Validation: Source** (“ENA Metadata Validation: Source”)                                                                |
| lib_strategy         | WGS, Amplicon, etc.                                                                                         | **ENA Metadata Validation: Strategy** (“ENA Metadata Validation: Strategy”)                                                            |
| lib_selection        | Random, PCR, etc.                                                                                           | **ENA Metadata Validation: Selection** (“ENA Metadata Validation: Selection”)                                                          |
| nucl_acid_ext        | Literature reference or SOP describing nucleic extraction i.e. CTAB extraction, Phenol-Cloroform Extraction | **The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                                        |
| nucl_acid_ext_treat  | Treatment of nucleic acid after extraction i.e. DNase, RNase                                                | **Adapted from The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                           |
| 🔹 *insert_length*   | *for inner dist. calc.* (or incl. in lib_layout?)(Array Express parameter: insert “Nominal Length”          |                                                                                                                                        |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                                                | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                                                | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| average_length       | As basepairs_count divided by sequence_count                                                                | **Calculated as basepairs_count/sequence_count**                                                                                       |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering                                   | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering                                   | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| quality_score        | Q30, quality above 30                                                                                       | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| checksum             | Hash value (e.g. MD5) for data integrity                                                                    | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                                    |

| Comments/questions:                                                                                                                                             |
|------------------------------------------------------------------------|
| Is insert length included in lib_format? If not, it seems this should be a minimal metadata parameter -NME 27APR22                                              |
| Not sure to understand the difference between metagenomic FASTA and metagenome assembled genome FASTA here. Quality score needs a better definition -CP 17JUL22 |
| Created two new rows, nucl_acid_ext and nucl_acid_ext_treat -MB 10AUG23                                                                                         |

##   Minimal technical metadata for `Metagenomic FASTA` file

| **metadata**         | **definition/examples**                                | **source**                                                                                                                           |
|------------------|------------------------------------|------------------|
| run_ref              | Accessions/identifiers linking to the raw data (FASTQ) | **Adapted from ENA** (“ENA How to Submit Other Analyses: Submitting Read Alignments”)                                                |
| tax_ident            | Phylogenetic marker(s) for MAG assignation             | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| assembly_qual        | Assembly quality category (e.g. Medium Quality Draft)  | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| assembly_software    | Tool(s) used, version and parameters                   | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| coverage             | The estimated depth of sequencing coverage             | **ENA Submitting Metagenome Assemblies** (“ENA Submitting Metagenome Assemblies”)                                                    |
| number_contig        | Total number of contigs                                | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020) |
| LSU_recover          | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E)    | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| LSU_recover_software | Tools for LSU extraction                               | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover          | Detection of the 16S rRNA (BA) or 18S rRNA (E)         | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover_software | Tools for SSU extraction                               | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| trnas                | Total number of tRNAs identified                       | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)               |
| trna_ext_software    | Tools used for tRNA identification                     | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_score          | Completeness score                                     | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_software       | Tools used for completion estimate                     | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_score         | Contamination score                                    | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_software      | Tool(s) used in contamination screening                | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |

| Comments/questions:                                                                                                                    |
|------------------------------------------------------------------------|
| Is coverage factored into completeness? If not, it seems we should consider separating genome coverage and sequence depth -NME 27APR22 |
| We need a reference for a consensual definitions of these terms to avoid confusion -CP 17JUL22                                         |
| Took the definitions from ENA Submitting Metagenome Asseblies, replaced coverage and depth with one definition -MB 11AUG23             |

<br/><br/> \##   Minimal technical metadata for
`Metagenome Assembled Genome (MAG) FASTA` file

| **metadata**         | **definition/examples**                                                    | **source**                                                                                                                           |
|------------------|------------------------------------|------------------|
| run_ref              | Accessions/identifiers linking to the raw data (FASTQ)                     | **Adapted from ENA** (“ENA How to Submit Other Analyses: Submitting Read Alignments”)                                                |
| tax_ident            | Phylogenetic marker(s) for MAG assignation                                 | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| assembly_qual        | Assembly quality category (e.g. Medium Quality Draft)                      | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| assembly_software    | Tool(s) used, version and parameters                                       | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                |
| coverage             | The estimated depth of sequencing coverage                                 | **ENA Submitting Metagenome Assemblies** (“ENA Submitting Metagenome Assemblies”)                                                    |
| number_contig        | Total number of contigs                                                    | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020) |
| N50                  | The length of the shortest contig representing half of the assembly length | **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)                                                        |
| LSU_recover          | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E)                        | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| LSU_recover_software | Tools for LSU extraction                                                   | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover          | Detection of the 16S rRNA (BA) or 18S rRNA (E)                             | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| SSU_recover_software | Tools for SSU extraction                                                   | **Adapted from GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                 |
| trnas                | Total number of tRNAs identified                                           | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”), **Roadmap for naming uncultivated Archaea and Bacteria** (Murray et al. 2020)               |
| trna_ext_software    | Tools used for tRNA identification                                         | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_score          | Completeness score                                                         | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| compl_software       | Tools used for completion estimate                                         | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_score         | Contamination score                                                        | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |
| contam_software      | Tool(s) used in contamination screening                                    | **GSC MIXS: MIMAG** (“GSC MIXS: MIMAG”)                                                                                              |

| Comments/questions:                                                                                                                                      |
|------------------------------------------------------------------------|
| Not sure to understand what is the source metadata -CP 17JUL22                                                                                           |
| As far as I understand that would be the same as run_ref i.e. raw data that was used to recover the MAG -MB 10AUG23                                      |
| Took the definitions from ENA Submitting Metagenome Asseblies, depth with coverage, removed source as it should be the same thing as run_ref -MB 11AUG23 |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** (Field et al. 2008),
**Minimum information about a marker gene sequence (MIMARKS) and minimum
information about any (x) sequence (MIxS) specifications** (Yilmaz et
al. 2011), **Minimum information about a single amplified genome (MISAG)
and a metagenome-assembled genome (MIMAG) of bacteria and archaea**
(Bowers et al. 2017), and **Roadmap for naming uncultivated Archaea and
Bacteria** (Murray et al. 2020) can be found online. We also highly
encourage the readers of this GitHub to read **The FAIR cookbook**
recipes (Rocca-Serra et al. 2022).

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

“GSC MIXS: MIGSBacteria.”
<https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/>.

“GSC MIXS: MIMAG.”
<https://genomicsstandardsconsortium.github.io/mixs/MIMAG/>.

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

Rocca-Serra, Philippe, Alasdair J G Gray, Alejandra Delfin Rossaro,
Andrea Splendiani, Andrea Zaliani, Andreas Pippow, Anne Cambon-Thomsen,
et al. 2022. “The FAIR Cookbook.”
<https://github.com/FAIRplus/the-fair-cookbook/>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
