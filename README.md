# NFDI4Microbiota-Metadata Task Area 2.1
> #### Goals: To maximize the quality of data entering the NFDI4Microbiota system by enforcing compliance with existing standards, as well as to identify and promote additional tailored data standards and metadata requirements within the NFDI4Microbiota systems.

<br/><br/>

## Minimal technical metadata by technology and file type:
<br/><br/>
## `Genome sequencing`
## &emsp; Minimal technical metadata for `genomic FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3]|
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
| trnas | Total number of tRNAs identified | MIMAG_v5[^4], SeqCode[^5] |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5[^4], SeqCode[^5] |
| compl_score | Completeness score | MIMAG_v5[^4], SeqCode[^5] |
| compl_software | Tools used for completion estimate | MIMAG_v5[^4], SeqCode[^5] |
| contam_score | Contamination score | MIMAG_v5[^4], SeqCode[^5] |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5[^4], SeqCode[^5] |

<br/><br/>

## `Amplicon sequencing`
## &emsp; Minimal technical metadata for `amplicon FASTQ` data
|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI) |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3]|
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| target_gene | Targeted gene name for marker gene studies (e.g. 16S rRNA, ITS) | MIMARKS_Sv5[^6] |
| target_subfragment | Name of the targeted subregion (e.g. V3-V4, ITS1) | MIMARKS_Sv5[^6] |
| pcr_primers | Forward and reverse primer sequences used | MIMARKS_Sv5[^6] |
| checksum | Hash value (e.g. MD5) for data integrity | |

<br/><br/>

## `Metagenome sequencing`
## &emsp; Minimal technical metadata for `metagenomic FASTQ` data
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| _insert_length_ | _for inner dist. calc._ (or is this information included in lib_layout ?) |  |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
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
| LSU_recover | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E) | Adapted from MIMAG_v5[^4] |
| LSU_recover_software | Tools for LSU extraction | |
| SSU_recover | Detection of the 16S rRNA (BA) or 18S rRNA (E) | Adapted from MIMAG_v5[^4] |
| SSU_recover_software | Tools for SSU extraction | |
| trnas | Total number of tRNAs identified | MIMAG_v5[^4], SeqCode[^5] |
| trna_ext_software | Tools used for tRNA identification | MIMAG_v5[^4], SeqCode[^5] |
| compl_score | Completeness score | MIMAG_v5[^4], SeqCode[^5] |
| compl_software | Tools used for completion estimate | MIMAG_v5[^4], SeqCode[^5] |
| contam_score | Contamination score | MIMAG_v5[^4], SeqCode[^5] |
| contam_software| Tool(s) used in contamination screening | MIMAG_v5[^4], SeqCode[^5] |

<br/><br/>

## `Transcriptome sequencing`

## &emsp; Minimal technical metadata for `transcriptomic FASTQ` file
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) | Shakya, Migun et al.(2019)[^7] |
| _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | |
| checksum | Hash value (e.g. MD5) for data integrity | |

## `Metatranscriptome sequencing`

## &emsp; Minimal technical metadata for `metatranscriptomic FASTQ` file
&emsp; _italics: for potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1] |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5 or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) |Shakya, Migun et al.(2019)[^7] |
| _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | |
| checksum | Hash value (e.g. MD5) for data integrity | |

## `Proteome sequencing`
## `Metaproteome sequencing`
## `Metabolome sequencing`

## `Data transfer & data integrity considerations`
|**Repository or tool source** | **Data transfer integrity checks in place** |
|------------|------------------------|
| ENA | MD5sum available for "most" downloads. Submission tool generates this, otherwise user needs to upload[^8]ncbi  |
| NCBI GEO | MD5 "recommended" for submissions[^9] |
| NCBI SRA |  MD5 is a parameter during submission (as of the 2010 guide[^10]) There is a (separate?) ‘vdb-validate’ tool for checking download integrity[^11] |
| MGnify | "Intermediate checksums" in 2020 paper[^12] |
| MG RAST | "Data hygiene" (Preprocessing, dereplication, DRISEE, screening)[^13] |

## Data integrity considerations by file type
|**File type**| **Integrity check** | **Other considerations for quality and transferability** |
|------------|-------------------------|------------|
| FASTQ | Read count, checksum (MD5sum, SEQGUID[^14][^15], etc.) | Determination of +33/+64 format from compressed files |
| FASTA | Read count, checksum (MD5sum, SEQGUID[^14][^15], etc.) | |
| .faa | SEQGUID[^14][^15] | Annotation pipeline, assembly quality |
| GFF/GTF | | Annotation pipeline, assembly quality |


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

[^7]: Shakya, Migun et al. “Advances and Challenges in Metatranscriptomic Analysis.” Frontiers in genetics vol. 10 904. 25 Sep. 2019, doi:10.3389/fgene.2019.00904

[^8]: https://ena-docs.readthedocs.io/en/latest/faq/runs.html#

[^9]: https://www.ncbi.nlm.nih.gov/geo/info/seq.html

[^10]: https://anonsvn.ncbi.nlm.nih.gov/repos/v1/trunk/sra/doc/SRA_1-1/SRA_Quick_Start_Guide.pdf

[^11]: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=vdb-validate

[^12]: Alex L Mitchell, Alexandre Almeida, Martin Beracochea, Miguel Boland, Josephine Burgin, Guy Cochrane, Michael R Crusoe, Varsha Kale, Simon C Potter, Lorna J Richardson, Ekaterina Sakharova, Maxim Scheremetjew, Anton Korobeynikov, Alex Shlemov, Olga Kunyavskaya, Alla Lapidus, Robert D Finn, MGnify: the microbiome analysis resource in 2020, Nucleic Acids Research, Volume 48, Issue D1, 08 January 2020, Pages D570–D578, https://doi.org/10.1093/nar/gkz1035

[^13]: The Metagenomics RAST server — A public resource for the automatic phylogenetic and functional analysis of metagenomes
F. Meyer, D. Paarmann, M. D’Souza, R. Olson , E. M. Glass, M. Kubal, T. Paczian, A. Rodriguez, R. Stevens, A. Wilke, J. Wilkening, and R. A. Edwards
BMC Bioinformatics 2008, 9:386

https://help.mg-rast.org/user_manual.html#data-hygiene

[^14]: Bassi, S., Gonzalez, V. New checksum functions for Biopython. Nat Prec (2007). https://doi.org/10.1038/npre.2007.278.1

[^15]: Babnigg, G. and Giometti, C.S. (2006), A database of unique protein sequence identifiers for proteome studies. Proteomics, 6: 4514-4522. https://doi.org/10.1002/pmic.200600032
