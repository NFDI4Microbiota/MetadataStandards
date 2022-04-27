# NFDI4Microbiota-Metadata Task Area 2.1
> #### Goals: To maximize the quality of data entering the NFDI4Microbiota system by enforcing compliance with existing standards, as well as to identify and promote additional tailored data standards and metadata requirements within the NFDI4Microbiota systems.


# Minimal technical metadata by technology and file type:

# `Genome sequencing`
## &emsp; Minimal technical metadata for `genomic FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5 |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRU-MENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5 |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB/Terrestrial Metagenome DB |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB/Terrestrial Metagenome DB |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB/Terrestrial Metagenome DB |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB|
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB |
| checksum | Hash value (e.g. MD5) for data integrity | |

## &emsp; Minimal technical metadata for `genomic FASTA` data

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| run_ref | Accessions/identifiers linking to the raw data (FAST Q) | Adapted from ENA |
| tax_ident | Phylogenetic marker(s) for MAG assignation | MIMAG_v5 |
| assembly_qual | Assembly quality category (e.g. Medium Quality Draft) | MIGS_BAv5 |
| assembly_software | Tool(s) used, version and parameters | MIGS_BAv5 |
| coverage | The estimated depth of sequencing coverage (in x) | |
| number_contig | Total number of contigs | MIGS_BAv5 |
| LSU_recover | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E) | Adapted from MIMAG_v5 |
| LSU_recover_software | Tools for LSU extraction | |
| SSU_recover | Detection of the 16S rRNA (BA) or 18S rRNA (E) | Adapted from MIMAG_v5 |
| SSU_recover_software | Tools for SSU extraction | |
| trnas | Total number of tRNAs identified | MIMAG_v5, SeqCode |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5, SeqCode |
| compl_score | Completeness score | MIMAG_v5, SeqCode |
| compl_software | Tools used for completion estimate | MIMAG_v5, SeqCode |
| contam_score | Contamination score | MIMAG_v5, SeqCode |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5, SeqCode |

<br/><br/>

# `(16S rRNA) Amplicon sequencing`
## &emsp; Minimal technical metadata for `amplicon FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5 |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRU-MENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5 |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB/Terrestrial Metagenome DB |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB/Terrestrial Metagenome DB |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB/Terrestrial Metagenome DB |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB|
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB |
| target_gene | Targeted gene name for marker gene studies (e.g. 16S rRNA, ITS) | MIMARKS_Sv5 |
| target_subfragment | Name of the targeted subregion (e.g. V3-V4, ITS1) | MIMARKS_Sv5 |
| pcr_primers | Forward and reverse primer sequences used | MIMARK_Sv5 |
| checksum | Hash value (e.g. MD5) for data integrity | |

<br/><br/>

# `Metagenome sequencing`
## &emsp; Minimal technical metadata for `metagenomic FASTQ` data
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5 |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRU-MENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5 |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| _insert_length_ | _for inner dist. calc._ (or is this included in lib_source ?) |  |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB/Terrestrial Metagenome DB |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB/Terrestrial Metagenome DB, JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB/Terrestrial Metagenome DB |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB, JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB |
| quality_score | Q30, quality above 30 | Human Metagenome DB/Terrestrial Metagenome DB |
| checksum | Hash value (e.g. MD5) for data integrity | |

## &emsp; Minimal technical metadata for `metagenomic FASTA` file

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| run_ref | Accessions/identifiers linking to the raw data (FAST Q) | Adapted from ENA |
| tax_ident | Phylogenetic marker(s) for MAG assignation | MIMAG_v5 |
| assembly_qual | Assembly quality category (e.g. Medium Quality Draft) | MIGS_BAv5 |
| assembly_software | Tool(s) used, version and parameters | MIGS_BAv5 |
| _coverage_ (or "completeness" below) | _The estimated coverage of sequencing coverage_ | |
| _depth_ | _calculated depth in x_ | |
| number_contig | Total number of contigs | MIGS_BAv5 |
| LSU_recover | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E) | Adapted from MIMAG_v5 |
| LSU_recover_software | Tools for LSU extraction | |
| SSU_recover | Detection of the 16S rRNA (BA) or 18S rRNA (E) | Adapted from MIMAG_v5 |
| SSU_recover_software | Tools for SSU extraction | |
| trnas | Total number of tRNAs identified | MIMAG_v5, SeqCode |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5, SeqCode |
| compl_score | Completeness score | MIMAG_v5, SeqCode |
| compl_software | Tools used for completion estimate | MIMAG_v5, SeqCode |
| contam_score | Contamination score | MIMAG_v5, SeqCode |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5, SeqCode |

<br/><br/>

# `Transcriptome sequencing`

## &emsp; Minimal technical metadata for `transcriptomic FASTQ` file
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5 |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRU-MENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5 |
| lib_source | Genomic, metagenomic | transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB/Terrestrial Metagenome DB |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB/Terrestrial Metagenome DB, JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB/Terrestrial Metagenome DB |
| sequence_count_qual | Number of reads int he library (sequencing depth) after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB, JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB/Terrestrial Metagenome DB |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) | |
| _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | |
| checksum | Hash value (e.g. MD5) for data integrity | |
