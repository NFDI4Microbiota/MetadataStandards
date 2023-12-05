## 2.2 Amplicon sequencing

A searchable and exportable tab-separated
[table](Amplicon_Technical_Metadata.tsv) of the following metadata is
now available.

## Minimal technical metadata for `Amplicon FASTQ` data

| **metadata**         | **definition**                                                                   | **examples**                                           | **source**                                                                                                                             |
|------------------|--------------------|------------------|------------------|
| sample_name          | Identifier of the sample                                                         | e.g. ISDsoil1                                          | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| seq_meth             | Sequencing method used                                                           | 454 Genome Sequencer FLX \[OBI:0000702\]               | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”), **ENA Metadata Validation: Instrument** (“ENA Metadata Validation: Instrument”) |
| lib_layout           | Specify whether to expect single, paired, or other configuration of reads        | e.g. single-end, paired end or others                  | **GSC MIxS/MIGS Bacteria** (“GSC MIXS: MIGSBacteria”)                                                                                  |
| lib_source           | The lib_source specifies the type of source material that is being sequenced     | e.g. genomic, metagenomic, transcriptomic, etc.        | **ENA Metadata Validation: Source** (“ENA Metadata Validation: Source”)                                                                |
| lib_strategy         | Sequencing technique intended for this library                                   | e.g. WGS, Amplicon, etc.                               | **ENA Metadata Validation: Strategy** (“ENA Metadata Validation: Strategy”)                                                            |
| lib_selection        | Whether any method was used to select and/or enrich the material being sequenced | e.g. Random, PCR, etc.                                 | **ENA Metadata Validation: Selection** (“ENA Metadata Validation: Selection”)                                                          |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                     | e.g. 32,283,453                                        | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                     | e.g. 6,400,000,000                                     | **Adapted from NCBI-SRA** (Leinonen et al. 2011)                                                                                       |
| average_length       | As basepairs_count divided by sequence_count                                     | e.g. 198                                               | **Calculated as basepairs_count/sequence_count**                                                                                       |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering        |                                                        | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering        |                                                        | **SRA-Tinder** (NCBI Hackathons)                                                                                                       |
| target_gene          | Targeted gene name for marker gene studies                                       | e.g. 16S rRNA, ITS                                     | **GSC MIXS: MIMARKSSpecimen** (“GSC MIXS: MIMARKSSpecimen”)                                                                            |
| target_subfragment   | Name of the targeted subregion                                                   | e.g. V3-V4, ITS1                                       | **GSC MIXS: MIMARKSSpecimen** (“GSC MIXS: MIMARKSSpecimen”)                                                                            |
| pcr_primers          | Forward and reverse primer sequences used                                        | e.g. FWD:GTGCCAGCMGCCGCGGTAA; REV:GGACTACHVGGGTWTCTAAT | **GSC MIXS: MIMARKSSpecimen** (“GSC MIXS: MIMARKSSpecimen”)                                                                            |
| checksum             | Hash value for data integrity                                                    | e.g. MD5: cbc41d0e49636872a765b950cb7f410a             | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                                    |

| Comments/questions:                                                     |
|------------------------------------------------------------------------|
| Should we also add nucl_ext_method and nucl_extr_treat here -MB 11AUG23 |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** (Field et al. 2008) and
**Minimum information about a marker gene sequence (MIMARKS) and minimum
information about any (x) sequence (MIxS) specifications** (Yilmaz et
al. 2011) can be found online.

# References

“ENA Metadata Validation: Instrument.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument>.

“ENA Metadata Validation: Selection.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection>.

“ENA Metadata Validation: Source.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source>.

“ENA Metadata Validation: Strategy.”
<https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy>.

Field, D., G. Garrity, T. Gray, N. Morrison, J. Selengut, P. Sterk, T.
Tatusova, et al. 2008. “The Minimum Information about a Genome Sequence
(MIGS) Specification.” Nature Biotechnology. 2008.
<https://doi.org/10.1038/nbt1360>.

“GSC MIXS: MIGSBacteria.”
<https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/>.

“GSC MIXS: MIMARKSSpecimen.”
<https://genomicsstandardsconsortium.github.io/mixs/MIMARKSSpecimen/>.

Leinonen, R., H. Sugawara, M. Shumway, and International Nucleotide
Sequence Database Collaboration. 2011. “The Sequence Read Archive.”
*Nucleic Acids Research* 39 (Database issue): D19–21.
<https://doi.org/10.1093/nar/gkq1019>.

NCBI Hackathons. “<span class="nocase">SRA-Tinder: A Tool to Discover
Related Sequence Read Archive (SRA) Experiments</span>.”
<https://github.com/NCBI-Hackathons/SRA_Tinder>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
