## 2.1 Genome sequencing

A searchable and exportable tab-separated
[table](Genome_Technical_Metadata.tsv) of the following metadata is now
available.

## Minimal technical metadata for `Genomic FASTQ` data

| **metadata**         | **definition/examples**                                                   | **source**                                                                                                                                                                                                              |
|------------------|------------------------------------|------------------|
| sample_name          | Identifier of the sample                                                  | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                            |
| seq_meth             | Sequencing method used (e.g. Illumina HiSeq 2000)                         | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/), [“ENA Metadata Validation: Instrument”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument) |
| lib_layout           | Single-end, paired end or others                                          | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                            |
| lib_source           | Genomic, metagenomic, transcriptomic, etc.                                | [“ENA Metadata Validation: Source”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source)                                                                                                       |
| lib_strategy         | WGS, Amplicon, etc.                                                       | [“ENA Metadata Validation: Strategy”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy)                                                                                                   |
| lib_selection        | Random, PCR, etc.                                                         | [“ENA Metadata Validation: Selection”](https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection)                                                                                                 |
| sequence_count       | Number of reads in the library (sequencing depth) or ‘spots’              | **Adapted from NCBI-SRA** ([Leinonen et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013647/))                                                                                                             |
| basepairs_count      | Number of base pairs (nucleotides) in the library or ‘bases’              | **Adapted from NCBI-SRA** ([Leinonen et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013647/))                                                                                                             |
| average_length       | As basepairs_count divided by sequence_count                              | **Calculated as basepairs_count/sequence_count**                                                                                                                                                                        |
| sequence_count_qual  | Number of reads in the library (sequencing depth) after quality filtering | **SRA-Tinder** ([NCBI Hackathons](https://github.com/NCBI-Hackathons/SRA_Tinder))                                                                                                                                       |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | **SRA-Tinder** ([NCBI Hackathons](https://github.com/NCBI-Hackathons/SRA_Tinder))                                                                                                                                       |
| checksum             | Hash value (e.g. MD5) for data integrity                                  | [Data transfer and data integrity](Data_Transfer_Data_Integrity.md)                                                                                                                                                     |

| Comments/questions:                                                     |
|------------------------------------------------------------------------|
| Should we also add nucl_ext_method and nucl_extr_treat here -MB 11AUG23 |

## Minimal technical metadata for `Genomic FASTA` data

| **metadata**         | **definition/examples**                                                    | **source**                                                                                                                                                                                                                 |
|------------------|------------------------------------|------------------|
| run_ref              | Accessions/identifiers linking to the raw data (FASTQ)                     | **Adapted from:** [“ENA How to Submit Other Analyses: Submitting Read Alignments”](https://ena-docs.readthedocs.io/en/latest/submit/analyses/read-alignments.html)                                                         |
| tax_ident            | Phylogenetic marker(s) for MAG assignation                                 | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |
| assembly_qual        | Assembly quality category (e.g. Medium Quality Draft)                      | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                               |
| assembly_software    | Tool(s) used, version and parameters                                       | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/)                                                                                                                               |
| coverage             | The estimated depth of sequencing coverage (in x)                          | [“ENA Submitting Metagenome Assemblies”](https://ena-docs.readthedocs.io/en/latest/submit/assembly/metagenome.html)                                                                                                        |
| number_contig        | Total number of contigs                                                    | [“GSC MIXS: MIGSBacteria”](https://genomicsstandardsconsortium.github.io/mixs/MIGSBacteria/), **Roadmap for naming uncultivated Archaea and Bacteria** ([Murray et al. (2020)](https://doi.org/10.1038/s41564-020-0733-x)) |
| N50                  | The length of the shortest contig representing half of the assembly length | **Roadmap for naming uncultivated Archaea and Bacteria** ([Murray et al. (2020)](https://doi.org/10.1038/s41564-020-0733-x))                                                                                               |
| LSU_recover          | Detection of the 23S rRNA (BA) or 5.8S/28S rRNA (E)                        | **Adapted from:** [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                           |
| LSU_recover_software | Tools for LSU extraction                                                   | **Adapted from:** [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                           |
| SSU_recover          | Detection of the 16S rRNA (BA) or 18S rRNA (E)                             | **Adapted from:** [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                           |
| SSU_recover_software | Tools for SSU extraction                                                   | **Adapted from:** [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                           |
| trnas                | Total number of tRNAs identified                                           | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/), **Roadmap for naming uncultivated Archaea and Bacteria** ([Murray et al. (2020)](https://doi.org/10.1038/s41564-020-0733-x))               |
| trna_ext_software    | Tools used for tRNA identification                                         | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |
| compl_score          | Completeness score                                                         | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |
| compl_software       | Tools used for completion estimate                                         | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |
| contam_score         | Contamination score                                                        | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |
| contam_software      | Tool(s) used in contamination screening                                    | [“GSC MIXS: MIMAG”](https://genomicsstandardsconsortium.github.io/mixs/MIMAG/)                                                                                                                                             |

The publications describing the reasons for formation of **The minimum
information about a genome sequence (MIGS)** ([Field et al.
(2008)](https://doi.org/10.1038/nbt1360)), **Minimum information about a
marker gene sequence (MIMARKS) and minimum information about any (x)
sequence (MIxS) specifications** ([Yilmaz et al.
(2011)](https://doi.org/10.1038/nbt.1823)), **Minimum information about
a single amplified genome (MISAG) and a metagenome-assembled genome
(MIMAG) of bacteria and archaea** ([Bowers et al.
(2017)](https://doi.org/10.1038/nbt.3893)), and **Roadmap for naming
uncultivated Archaea and Bacteria** ([Murray et al.
(2020)](https://doi.org/10.1038/s41564-020-0733-x)) can be found online.

We also encourage our readers to have a look at the
[**HumanMetagenomeDB: a public repository of curated and standardized
metadata for human metagenomes**](https://webapp.ufz.de/hmgdb/)
([Kasmanas et al.
(2021)](https://academic.oup.com/nar/article/49/D1/D743/5998395)) and
[**TerrestrialMetagenomeDB: a public repository of curated and
standardized metadata for terrestrial
metagenomes**](https://webapp.ufz.de/tmdb/) ([Corrêa et al.
(2020)](https://academic.oup.com/nar/article/48/D1/D626/5625925)) to
better understand some of the metadata fields that can be found in the
tables above.

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
