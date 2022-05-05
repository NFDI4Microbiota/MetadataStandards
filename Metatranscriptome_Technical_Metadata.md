## 2.5 Metatranscriptome sequencing

## &emsp; Minimal technical metadata for `metatranscriptomic FASTQ` file
&emsp; &#x1F539; _italics = potential considerations_

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| sample_name | Identifier of the sample | Adapted from MIGS_BAv5[^1]  |
| seq_meth | Sequencing method used (e.g. Illumina HiSeq 2000)|MIGS_BAv5[^1] or INSTRUMENT (ENA/NCBI), JGI IMG |
| lib_layout | Single-end, paired end or others | MIGS_BAv5[^1] |
| lib_source | Genomic, metagenomic, transcriptomic, etc. | Source (ENA/NCBI) |
| lib_strategy | WGS, Amplicon, etc. | Strategy (ENA/NCBI) |
| lib_selection | Random, PCR, etc. | Selection (ENA/NCBI) |
| &#x1F539; _nucleic acid extraction method_ | _Technique._ _Treatments as subcategory? (e.g. DNase, RNase)_ | FAIR cookbook[^18] |
| &#x1F539; _insert_length_ | _for inner dist. calc._ (or incl. in lib_layout?)(Array Express parameter: insert "Nominal Length" | ArrayExpress[^17] |
| sequence_count | Number of reads in the library (sequencing depth) | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| basepairs_count | Number of base pairs (nucleotides) in the library | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| average_length | As basepairs_count divided by sequence_count | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| sequence_count_qual | Number of reads in the library (sequencing depth) after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3], JGI IMG |
| basepairs_count_qual | Number of base pairs (nucleotides) in the library after quality filtering | Human Metagenome DB[^2]/Terrestrial Metagenome DB[^3] |
| rRNA depletion | (e.g. none, pre-sequencing (molecular), post-sequencing (in-silico)) | Shakya, Migun et al.(2019)[^7] |
| &#x1F539; _Rev. transcriptase used_ | _(e.g. MMLV, AMV)_ | |
| &#x1F539; _primers/oligos_ | _(e.g. random primer set metadata, oligo(dT), both)_ | FAIR cookbook[^18] |
| checksum | Hash value (e.g. MD5) for data integrity | |

|Comments/questions: |
|--------------------|
| |

## &emsp; Minimal technical metadata for `Metatranscriptomic FASTA` file

|**metadata**| **definition/examples** | **source** |
|------------|-------------------------|------------|
| run_ref | Accessions/identifiers linking to the raw data (FAST Q) | Adapted from ENA and TSA DB[^16] |
| Locus | (e.g. "GAAA01000000 93507 rc mRNA linear TSA 20-JUL-2015" | Transcriptome Shotgun Assembly DB[^16] |
| Definition |  TSA: Latimeria chalumnae voucher 08118, transcriptome shotgun assembly | Transcriptome Shotgun Assembly DB[^16] |
| DB Link | BioProject/Biosample/SRA | Transcriptome Shotgun Assembly DB[^16] |
| Reference | Author/Consortium/Title/Journal | Transcriptome Shotgun Assembly DB[^16] |
| Seq length | (e.g. "Sequences should be greater than 200 bp in length." | Transcriptome Shotgun Assembly DB[^16] |
| Seq quality | (e.g. Ambiguous bases should not be more than total 10% length or more than 14n's in a row" | Transcriptome Shotgun Assembly DB[^16] |
| Protocols | Links to protocol accessions | ArrayExpress DB[^17] |

|Comments/questions: |
|--------------------|
| |

# References
[^1]:Field, D., Garrity, G., Gray, T., Morrison, N., Selengut, J., Sterk, P., Tatusova, T., Thomson, N., Allen, M. J., Angiuoli, S. V., Ashburner, M., Axelrod, N., Baldauf, S., Ballard, S., Boore, J., Cochrane, G., Cole, J., Dawyndt, P., De Vos, P., DePamphilis, C., … Wipat, A. (2008). The minimum information about a genome sequence (MIGS) specification. Nature biotechnology, 26(5), 541–547. https://doi.org/10.1038/nbt1360, https://gensc.org/mixs/,  
https://gensc.org/publications-2/

[^2]:Kasmanas, J. C., Bartholomäus, A., Corrêa, F. B., Tal, T., Jehmlich, N., Herberth, G., von Bergen, M., Stadler, P. F., de Carvalho, A. & da Rocha, U. N. (2021). HumanMetagenomeDB: a public repository of curated and standardized metadata for human metagenomes. Nucleic Acids Research, 49(D1), D743–D750., https://webapp.ufz.de/hmgdb/

[^3]:Corrêa, F. B., Saraiva, J. P., Stadler, P. F. & da Rocha, U. N. (2020). TerrestrialMetagenomeDB: a public repository of curated and standardized metadata for terrestrial metagenomes. Nucleic Acids Research, 48(D1), D626-D632., https://webapp.ufz.de/tmdb/

[^4]:Bowers, R., Kyrpides, N., Stepanauskas, R. et al. Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. Nat Biotechnol 35, 725–731 (2017). https://doi.org/10.1038/nbt.3893, https://gensc.org/mixs/

[^5]: Murray, A.E., Freudenstein, J., Gribaldo, S. et al. Roadmap for naming uncultivated Archaea and Bacteria. Nat Microbiol 5, 987–994 (2020). https://doi.org/10.1038/s41564-020-0733-x,  https://www.isme-microbes.org/seqcode-initiative

[^6]: Yilmaz, Pelin et al. “Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications.” Nature biotechnology vol. 29,5 (2011): 415-20. doi:10.1038/nbt.1823,  https://gensc.org/mixs/

[^7]: Shakya, Migun et al. “Advances and Challenges in Metatranscriptomic Analysis.” Frontiers in genetics vol. 10 904. 25 Sep. 2019, doi:10.3389/fgene.2019.00904

[^8]: https://ena-docs.readthedocs.io/en/latest/faq/runs.html#

[^9]: https://www.ncbi.nlm.nih.gov/geo/info/seq.html

[^10]: https://anonsvn.ncbi.nlm.nih.gov/repos/v1/trunk/sra/doc/SRA_1-1/SRA_Quick_Start_Guide.pdf

[^11]: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=vdb-validate

[^12]: Alex L Mitchell, Alexandre Almeida, Martin Beracochea, Miguel Boland, Josephine Burgin, Guy Cochrane, Michael R Crusoe, Varsha Kale, Simon C Potter, Lorna J Richardson, Ekaterina Sakharova, Maxim Scheremetjew, Anton Korobeynikov, Alex Shlemov, Olga Kunyavskaya, Alla Lapidus, Robert D Finn, MGnify: the microbiome analysis resource in 2020, Nucleic Acids Research, Volume 48, Issue D1, 08 January 2020, Pages D570–D578, https://doi.org/10.1093/nar/gkz1035

[^13]: The Metagenomics RAST server — A public resource for the automatic phylogenetic and functional analysis of metagenomes
F. Meyer, D. Paarmann, M. D’Souza, R. Olson , E. M. Glass, M. Kubal, T. Paczian, A. Rodriguez, R. Stevens, A. Wilke, J. Wilkening, and R. A. Edwards
BMC Bioinformatics 2008, 9:386,  https://help.mg-rast.org/user_manual.html#data-hygiene

[^14]: Bassi, S., Gonzalez, V. New checksum functions for Biopython. Nat Prec (2007). https://doi.org/10.1038/npre.2007.278.1

[^15]: Babnigg, G. and Giometti, C.S. (2006), A database of unique protein sequence identifiers for proteome studies. Proteomics, 6: 4514-4522. https://doi.org/10.1002/pmic.200600032

[^16]: https://www.ncbi.nlm.nih.gov/genbank/tsa/

[^17]:  Athar A. et al., 2019. ArrayExpress update - from bulk to single-cell expression data. Nucleic Acids Res, doi: 10.1093/nar/gky964. Pubmed ID 30357387.  https://www.ebi.ac.uk/arrayexpress/

[^18]:The FAIR Cookbook: a deliverable of the FAIRplus project (grant agreement 802750), funded by the IMI programme, a private-public partnership that receives support from the European Union’s Horizon 2020 research and innovation programme and EFPIA Companies.   https://faircookbook.elixir-europe.org/content/recipes/interoperability/transcriptomics-metadata.html

[^19]:https://www.nfdi.de/

[^20]:https://nfdi4microbiota.de/

[^21]:Hedlund et al. (In review) https://disc-genomics.uibk.ac.at/seqcode//files/Hedlund_et_al.pdf
