# NFDI4Microbiota-Metadata Task Area 2.1
> #### Goals: To maximize the quality of data entering the NFDI4Microbiota system by enforcing compliance with existing standards, as well as to identify and promote additional tailored data standards and metadata requirements within the NFDI4Microbiota systems.


# Minimal technical metadata by technology and file type:

# `Genome sequencing`
## &emsp; Minimal technical metadata for `genomic FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3]|
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| checksum | Hash value (e.g. MD5) for data integrity | |

## &emsp; Minimal technical metadata for `genomic FASTA` data

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| run_ref | Accessions/identifiers linking to the raw data (FAST Q) | Adapted from ENA |
| tax_ident | Phylogenetic marker(s) for MAG assignation | MIMAG_v5[^4] |
| assembly_qual | Assembly quality category (e.g. Medium Quality Draft) | MIGS_BAv5[^1] |
| assembly_software | Tool(s) used, version and parameters | MIGS_BAv5[^1] |
| coverage | The estimated depth of sequencing coverage (in x) | |
| number_contig | Total number of contigs | MIGS_BAv5[^1] |
| LSU_recover | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E) | Adapted from MIMAG_v5[^4] |
| LSU_recover_software | Tools for LSU extraction | |
| SSU_recover | Detection of the 16S rRNA (BA) or 18S rRNA (E) | Adapted from MIMAG_v5[^4] |
| SSU_recover_software | Tools for SSU extraction | |
| trnas | Total number of tRNAs identified | MIMAG_v5, SeqCode[^5] |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5[^4], SeqCode[^5] |
| compl_score | Completeness score | MIMAG_v5, SeqCode |
| compl_software | Tools used for completion estimate | MIMAG_v5[^4], SeqCode[^5] |
| contam_score | Contamination score | MIMAG_v5[^4], SeqCode[^5] |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5[^4], SeqCode[^5] |

<br/><br/>

# `Amplicon sequencing`
## &emsp; Minimal technical metadata for `amplicon FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3]|
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| target_gene | Targeted gene name for marker gene studies (e.g. 16S rRNA, ITS) | MIMARKS_Sv5[^6] |
| target_subfragment | Name of the targeted subregion (e.g. V3-V4, ITS1) | MIMARKS_Sv5[^6] |
| pcr_primers | Forward and reverse primer sequences used | MIMARKS_Sv5[^6] |
| checksum | Hash value (e.g. MD5) for data integrity | |

<br/><br/>

# `Metagenome sequencing`
## &emsp; Minimal technical metadata for `metagenomic FASTQ` data
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| _insert_length_ | _for inner dist. calc._ (or is this included in lib_source ?) |  |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| quality_score | Q30, quality above 30 | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| checksum | Hash value (e.g. MD5) for data integrity | |

## &emsp; Minimal technical metadata for `metagenomic FASTA` file

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| run_ref | Accessions/identifiers linking to the raw data (FAST Q) | Adapted from ENA |
| tax_ident | Phylogenetic marker(s) for MAG assignation | MIMAG_v5[^4] |
| assembly_qual | Assembly quality category (e.g. Medium Quality Draft) | MIGS_BAv5[^1] |
| assembly_software | Tool(s) used, version and parameters | MIGS_BAv5[^1] |
| _coverage_ (or "completeness" below) | _The estimated coverage of sequencing coverage_ | |
| _depth_ | _calculated depth in x_ | |
| number_contig | Total number of contigs | MIGS_BAv5[^1] |
| LSU_recover | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E) | Adapted from MIMAG_v5 |
| LSU_recover_software | Tools for LSU extraction | |
| SSU_recover | Detection of the 16S rRNA (BA) or 18S rRNA (E) | Adapted from MIMAG_v5 |
| SSU_recover_software | Tools for SSU extraction | |
| trnas | Total number of tRNAs identified | MIMAG_v5[^4], SeqCode[^5] |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5[^4], SeqCode[^5] |
| compl_score | Completeness score | MIMAG_v5, SeqCode |
| compl_software | Tools used for completion estimate | MIMAG_v5[^4], SeqCode[^5] |
| contam_score | Contamination score | MIMAG_v5[^4], SeqCode[^5] |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5[^4], SeqCode[^5] |

<br/><br/>

# `Transcriptome sequencing`

## &emsp; Minimal technical metadata for `transcriptomic FASTQ` file
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) | |
| _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | |
| checksum | Hash value (e.g. MD5) for data integrity | |


## &emsp; Minimal technical metadata for `metatranscriptomic FASTQ` file
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) | |
| _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | |
| checksum | Hash value (e.g. MD5) for data integrity | |

# References
[^1]:Field, D., Garrity, G., Gray, T., Morrison, N., Selengut, J., Sterk, P., Tatusova, T., Thomson, N., Allen, M. J., Angiuoli, S. V., Ashburner, M., Axelrod, N., Baldauf, S., Ballard, S., Boore, J., Cochrane, G., Cole, J., Dawyndt, P., De Vos, P., DePamphilis, C., … Wipat, A. (2008). The minimum information about a genome sequence (MIGS) specification. Nature biotechnology, 26(5), 541–547. https://doi.org/10.1038/nbt1360

(https://gensc.org/mixs/)
(https://gensc.org/publications-2/)

[^2]:Kasmanas, J. C., Bartholomäus, A., Corrêa, F. B., Tal, T., Jehmlich, N., Herberth, G., von Bergen, M., Stadler, P. F., de Carvalho, A. & da Rocha, U. N. (2021). HumanMetagenomeDB: a public repository of curated and standardized metadata for human metagenomes. Nucleic Acids Research, 49(D1), D743–D750. 

(https://webapp.ufz.de/hmgdb/)

[^3]:Corrêa, F. B., Saraiva, J. P., Stadler, P. F. & da Rocha, U. N. (2020). TerrestrialMetagenomeDB: a public repository of curated and standardized metadata for terrestrial metagenomes. Nucleic Acids Research, 48(D1), D626-D632. 

(https://webapp.ufz.de/tmdb/)

[^4]:Bowers, R., Kyrpides, N., Stepanauskas, R. et al. Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. Nat Biotechnol 35, 725–731 (2017). https://doi.org/10.1038/nbt.3893

https://gensc.org/mixs/

[^5]: Murray, A.E., Freudenstein, J., Gribaldo, S. et al. Roadmap for naming uncultivated Archaea and Bacteria. Nat Microbiol 5, 987–994 (2020). https://doi.org/10.1038/s41564-020-0733-x

https://www.isme-microbes.org/seqcode-initiative

[^6]: Yilmaz, Pelin et al. “Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications.” Nature biotechnology vol. 29,5 (2011): 415-20. doi:10.1038/nbt.1823

https://gensc.org/mixs/
