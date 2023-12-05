## 2.4 Transcriptome sequencing

A searchable and exportable tab-separated
[table](Transcriptome_Technical_Metadata.tsv) of the following metadata
is now available.

## Minimal technical metadata for `Transcriptomic FASTQ` file

  🔹 *italics = potential considerations*

| **metadata**         | **definition**                                                                                     | **examples**                                                  | **source**                                                                                                                             |
|-----------------|---------------------|------------------|-----------------|
| sample_name          | Identifier of the sample                                                                           | e.g. ISDsoil1                                                 | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| seq_meth             | Sequencing method used                                                                             | 454 Genome Sequencer FLX \[OBI:0000702\]                      | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **ENA Metadata Validation: Instrument** (“ENA Metadata Validation: Instrument”) |
| lib_layout           | Specify whether to expect single, paired, or other configuration of reads                          | e.g. single-end, paired end or others                         | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| lib_source           | The lib_source specifies the type of source material that is being sequenced                       | e.g. genomic, metagenomic, transcriptomic, etc.               | **ENA Metadata Validation: Source** (“ENA Metadata Validation: Source”)                                                                |
| lib_strategy         | Sequencing technique intended for this library                                                     | e.g. WGS, Amplicon, etc.                                      | **ENA Metadata Validation: Strategy** (“ENA Metadata Validation: Strategy”)                                                            |
| lib_selection        | Whether any method was used to select and/or enrich the material being sequenced                   | e.g. Random, PCR, etc.                                        | **ENA Metadata Validation: Selection** (“ENA Metadata Validation: Selection”)                                                          |
| nucl_acid_ext        | Literature reference or SOP describing nucleic extraction                                          | e.g. CTAB extraction, Phenol-Cloroform Extraction             | **The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                                        |
| nucl_acid_ext_treat  | Treatment of nucleic acid after extraction                                                         | e.g. DNase, RNase                                             | **Adapted from The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                           |
| 🔹 *insert_length*   | *for inner dist. calc.* (or incl. in lib_layout?)(Array Express parameter: insert “Nominal Length” |                                                               |                                                                                                                                        |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                                       | e.g. 32,283,453                                               | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                                       | e.g. 6,400,000,000                                            | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| average_length       | As basepairs_count divided by sequence_count                                                       | e.g. 198                                                      | **Calculated as basepairs_count/sequence_count**                                                                                       |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering                          |                                                               | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering                          |                                                               | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| rRNA treatment       |                                                                                                    | Depletion (Pre-seq, molecular), Removal (Post-seq data), None | **Advances and Challenges in Metatranscriptomic Analysis** (Shakya et al. 2019)                                                        |
| cDNA_ampl_meth       | Technique used to amplify a cDNA library                                                           | e.g. MMLV, AMV                                                | **The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                                        |
| cDNA_oligo           | Type of primer used for cDNA synthesis from RNA                                                    | e.g. polyA or random                                          | **The FAIR Cookbook** (Rocca-Serra et al. 2022)                                                                                        |
| checksum             | Hash value for data integrity                                                                      | e.g. MD5: cbc41d0e49636872a765b950cb7f410a                    | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                                    |

| Comments/questions:                                                                                                                                |
|------------------------------------------------------------------------|
| Added insert length, reverse transcriptase, and the primer set as possible technical parameters. Could go under “Protocol” parameter. -NME 27APR22 |
| Added cDNA_ampl_meth and cDNA_oligo to the table -MB 11AUG23                                                                                       |

## Minimal technical metadata for `Transcriptomic FASTA` file

| **metadata** | **definition**                                                                                   | **examples**                                                                | **source**                                                                                           |
|-----------------|---------------------|------------------|-----------------|
| run_ref      | Accessions/identifiers linking to the raw data (FASTQ)                                           | e.g. accession = “ERR178314”                                                | **ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”)              |
| Locus        | Physical location of a gene on a chromosome                                                      | e.g. “GAAA01000000 93507 rc mRNA”, “11q1.4-q2.1”                            | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| Description  | Sample description                                                                               | e.g. TSA: Latimeria chalumnae voucher 08118, transcriptome shotgun assembly | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| DB Link      | BioProject/Biosample/SRA                                                                         | e.g. PRJNA1035062                                                           | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| Reference    | Author/Consortium/Title/Journal                                                                  |                                                                             | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| Seq length   | Number of nucleotides in a transcript. Sequences should be greater than 200 bp in length.        |                                                                             | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| Seq quality  | The accuracy and reliability of the nucleotide sequence information obtained from RNA sequencing |                                                                             | **Adapted from ENA Submitting Transcriptome Assemblies** (“ENA Submitting Transcriptome Assemblies”) |
| Protocols    | Links to protocol accessions                                                                     |                                                                             |                                                                                                      |

| Comments/questions:                                                                                                                        |
|------------------------------------------------------------------------|
| Don’t know which protocol accessions were meant here, was it SOP, and protocol for what, so I left it empty for the time being -MB 11AUG23 |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** (Field et al. 2008),
**Minimum information about a marker gene sequence (MIMARKS) and minimum
information about any (x) sequence (MIxS) specifications** (Yilmaz et
al. 2011) and **Advances and Challenges in Metatranscriptomic Analysis**
(Shakya et al. 2019) can be found online. We also highly encourage the
readers of this GitHub to read **The FAIR cookbook** recipes
(Rocca-Serra et al. 2022), and look for examples of submitted
Transcriptomic samples in **Transcriptome Shotgun Assembly Sequence
Database** (“Transcriptome Shotgun Assembly Sequence Database”).

# References

“ENA Metadata Validation: Instrument.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument>.

“ENA Metadata Validation: Selection.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection>.

“ENA Metadata Validation: Source.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source>.

“ENA Metadata Validation: Strategy.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy>.

“ENA Submitting Transcriptome Assemblies.”
<https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html>.

Field, D., G. Garrity, T. Gray, N. Morrison, J. Selengut, P. Sterk, T.
Tatusova, et al. 2008. “The Minimum Information about a Genome Sequence
(MIGS) Specification.” Nature Biotechnology. 2008.
<https://doi.org/10.1038/nbt1360>.

“GSC MIXS: MIGSBacteria.”
<https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/>.

Leinonen, R., H. Sugawara, M. Shumway, and International Nucleotide
Sequence Database Collaboration. 2011. “The Sequence Read Archive.”
*Nucleic Acids Research* 39 (Database issue): D19–21.
<https://doi.org/10.1093/nar/gkq1019>.

NCBI Hackathons. “<span class="nocase">SRA-Tinder: A Tool to Discover
Related Sequence Read Archive (SRA) Experiments</span>.”
<https://github.com/NCBI-Hackathons/SRA_Tinder>.

Rocca-Serra, Philippe, Alasdair J G Gray, Alejandra Delfin Rossaro,
Andrea Splendiani, Andrea Zaliani, Andreas Pippow, Anne Cambon-Thomsen,
et al. 2022. “The FAIR Cookbook.”
<https://github.com/FAIRplus/the-fair-cookbook/>.

Shakya, Migun, Christopher Quince, James H Campbell, and Zamin K Yang.
2019. “Advances and Challenges in Metatranscriptomic Analysis.”
*Frontiers in Genetics* 10 (September): 904.
<https://doi.org/10.3389/fgene.2019.00904>.

“Transcriptome Shotgun Assembly Sequence Database.”
<https://www.ncbi.nlm.nih.gov/genbank/tsa/>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
