## 2.5 Metatranscriptome sequencing

A searchable and exportable tab-separated
[table](Metatranscriptome_Technical_Metadata.tsv) of the following
metadata is now available.

##   Minimal technical metadata for `Metatranscriptomic FASTQ` file

  🔹 *italics = potential considerations*

| **metadata**         | **definition/examples**                                                                                     | **source**                                                                                                                                                                                                              |
|------------------|------------------------------------|------------------|
| sample_name          | Identifier of the sample                                                                                    | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                            |
| seq_meth             | Sequencing method used (e.g. Illumina HiSeq 2000)                                                           | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/), [“ENA Metadata Validation: Instrument”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument) |
| lib_layout           | Single-end, paired end or others                                                                            | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                            |
| lib_source           | Genomic, metagenomic, transcriptomic, etc.                                                                  | [“ENA Metadata Validation: Source”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source)                                                                                                       |
| lib_strategy         | WGS, Amplicon, etc.                                                                                         | [“ENA Metadata Validation: Strategy”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy)                                                                                                   |
| lib_selection        | Random, PCR, etc.                                                                                           | [“ENA Metadata Validation: Selection”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection)                                                                                                 |
| nucl_acid_ext        | Literature reference or SOP describing nucleic extraction i.e. CTAB extraction, Phenol-Cloroform Extraction | **The FAIR Cookbook** ([Rocca-Serra et al. (2022)](https://github.com/FAIRplus/the-fair-cookbook/))                                                                                                                     |
| nucl_acid_ext_treat  | Treatment of nucleic acid after extraction i.e. DNase, RNase                                                | **Adapted from The FAIR Cookbook** ([Rocca-Serra et al. (2022)](https://github.com/FAIRplus/the-fair-cookbook/))                                                                                                        |
| 🔹 *insert_length*   | *for inner dist. calc.* (or incl. in lib_layout?)(Array Express parameter: insert “Nominal Length”          |                                                                                                                                                                                                                         |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’                                                | **Adapted from NCBI-SRA** ([Leinonen et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013647/))                                                                                                             |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’                                                | **Adapted from NCBI-SRA** ([Leinonen et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013647/))                                                                                                             |
| average_length       | As basepairs_count divided by sequence_count                                                                | **Calculated as basepairs_count/sequence_count**                                                                                                                                                                        |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering                                   | **SRA-Tinder** ([NCBI Hackathons](https://github.com/NCBI-Hackathons/SRA_Tinder))                                                                                                                                       |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering                                   | **SRA-Tinder** ([NCBI Hackathons](https://github.com/NCBI-Hackathons/SRA_Tinder))                                                                                                                                       |
| rRNA treatment       | Depletion (Pre-seq, molecular), Removal (Post-seq data), None                                               | **Advances and Challenges in Metatranscriptomic Analysis** ([Shakya et al. (2019)](https://doi.org/10.3389/fgene.2019.00904))                                                                                           |
| cDNA_ampl_meth       | Technique used to amplify a cDNA library i.e. MMLV, AMV                                                     | **The FAIR Cookbook** ([Rocca-Serra et al. (2022)](https://github.com/FAIRplus/the-fair-cookbook/))                                                                                                                     |
| cDNA_oligo           | Type of primer used for cDNA synthesis from RNA, i.e. polyA or random                                       | **The FAIR Cookbook** ([Rocca-Serra et al. (2022)](https://github.com/FAIRplus/the-fair-cookbook/))                                                                                                                     |
| checksum             | Hash value (e.g. MD5) for data integrity                                                                    | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                                                                                                                     |

| Comments/questions:                                          |
|--------------------------------------------------------------|
| Added cDNA_ampl_meth and cDNA_oligo to the table -MB 11AUG23 |

##   Minimal technical metadata for `Metatranscriptomic FASTA` file

| **metadata** | **definition/examples**                                                                     | **source**                                                                                                                                  |
|------------------|------------------------------------|------------------|
| run_ref      | Accessions/identifiers linking to the raw data (FASTQ)                                      | [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html)                   |
| Locus        | (e.g. “GAAA01000000 93507 rc mRNA linear TSA 20-JUL-2015”                                   | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| Definition   | TSA: Latimeria chalumnae voucher 08118, transcriptome shotgun assembly                      | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| DB Link      | BioProject/Biosample/SRA                                                                    | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| Reference    | Author/Consortium/Title/Journal                                                             | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| Seq length   | (e.g. “Sequences should be greater than 200 bp in length.”                                  | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| Seq quality  | (e.g. Ambiguous bases should not be more than total 10% length or more than 14n’s in a row” | **Adapted from:** [“ENA Submitting Transcriptome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/transcriptome.html) |
| Protocols    | Links to protocol accessions                                                                |                                                                                                                                             |

| Comments/questions:                                                                                                                        |
|------------------------------------------------------------------------|
| Don’t know which protocol accessions were meant here, was it SOP, and protocol for what, so I left it empty for the time being -MB 11AUG23 |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** ([Field et al.
(2008)](https://doi.org/10.1038/nbt1360)), **Advances and Challenges in
Metatranscriptomic Analysis** ([Shakya et al.
(2019)](https://doi.org/10.3389/fgene.2019.00904)) can be found online.
We also highly encourage the readers of this GitHub to read **The FAIR
cookbook** recipes ([Rocca-Serra et al.
(2022)](https://github.com/FAIRplus/the-fair-cookbook/)), and look for
examples of submitted transcriptomic samples in [**“Transcriptome
Shotgun Assembly Sequence
Database”**](https://www.ncbi.nlm.nih.gov/genbank/tsa/).

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
