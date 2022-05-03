# NFDI4Microbiota - Task Area 2.1 - Metadata

## NFDI4Microbiota introduction:
#### The National Research Data Infrastructure Germany (NFDI) is currently comprised of 19 consortia members spanning diverse fields, including physical sciences, human health, biology, artificial intelligence, cultural and economic science, among others[^19]. In July 2021, NFDI4Microbiota was selected to become a consortium member and holds a mission "_to be the central hub in Germany for supporting the microbiology community with access to data, analysis services, data/metadata standards and training_."[^20] Through building analytical tools, ensuring FAIR principles are followed, and standardizing metadata and data processing, NFDI4Microbiota will contribute to the interdisciplanary NFDI network from the microbiological perspective. 

## NFDI4Microbiota Task Area 2 - Standards and Policies:
#### NFDI4Microbiota aims to address issues of microbial data accessibility and consistency. These issues have long presented challenges for the efficient  exchange of useable information between research groups, data generators (e.g. sequencing centers), and data repositories. Specifically, Measure 2.1 (M2.1) has the goal "_to maximize the quality of data entering the NFDI4Microbiota system by enforcingcompliance with existing standards, as well as to identify and promote additional tailored datastandards and metadata requirements within the NFDI4Microbiota systems._" Establishing standard parameters for metadata will ensure that generated data is reproducible and comparable, both spatially and temporally. 

## Task Area 2.1 Goals and milestones (MS) 2.1.1 and 2.1.2:
> #### Goals: To maximize the quality of data entering the NFDI4Microbiota system by enforcing compliance with existing standards, as well as to identify and promote additional tailored data standards and metadata requirements within the NFDI4Microbiota systems.
> #### MS2.1.1 Definition of data standards for the different types of raw data established
> #### MS2.1.2 Definition of data standards for the technical metadata established

### To address metadata quality standards in microbial science, three metadata categories are being considered:
- Technical 
- Biological
- Environmental

### This Github page focuses on minimal **technical** metadata standards within M2.1 applicable to the following data types:
- Genomes
- Metagenomes
- Metagenome assembled genomes
- Transcriptomes
- Metatranscriptomes
- Proteomes
- Metaproteomes
- Metabolomes

### Additionally, standards are being considered for data integrity and data transfer to ensure quality is maintained throughout various processes of data file exchange. 

<br/><br/>

# Section 1. Overview of minimal technical FASTQ and FASTA metadata considerations (as of 29APR22)
![FASTQMetadataTablesOverview_working29APR22](https://user-images.githubusercontent.com/101716821/165967974-0626a7fa-6c5b-4cd2-af9c-a07c5f322f53.jpg)
#### **Figure 1.** Overview of minimal technical metadata considered for FASTQ files. Parameter applicabilty to data types ((meta)genome, (meta)transcriptome, etc.) is listed on the left y-axis, and time of metadata generation is listed on the right.    

<br/><br/>

![FASTAMetadataTablesOverview_working29APR22](https://user-images.githubusercontent.com/101716821/165967971-18850bfb-10b9-4aad-a838-7d0654739ea1.jpg)
#### **Figure 2.** Overview of minimal technical metadata considered for FASTA files. Parameter applicabilty to data types ((meta)genome, (meta)transcriptome, etc.) is listed on the left y-axis, and time of metadata generation is listed on the right. 

<br/><br/>

# Section 2. Minimal technical metadata by technology and file type 
## (Questions/comments are listed below the tables within each subsection)

   - 2.1 [Genome Sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Genome-Technical-Metadata/README.md)
     - Genomic FASTQ
     - Genomic FASTA
   - 2.2 [Amplicon Sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Amplicon-Technical-Metadata/README.md)
     - Amplicon FASTQ
   - 2.3 [Metagenome Sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Metagenome-Technical-Metadata/README.md)
     - Metagenome FASTQ
     - Metagenome FASTA
     - Metagenome assembled genome FASTA
   - 2.4 [Transcriptome Sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Transcriptome-Technical-Metadata/README.md)
     - Transcriptome FASTQ
     - Transcriptome FASTA
   - 2.5 [Metatranscriptome Sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Metatranscriptome-Technical-Metadata/README.md)
     - Metatranscriptome FASTQ
     - Metatranscriptome FASTA
   - 2.6 [Proteome sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Proteomics-Technical-Metadata/README.md)
     - Proteome
     - Proteome - experimental protocol edition
   - 2.7 Metaproteome sequencing 
   - 2.8 [Metabolome sequencing](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/Metabolome-Technical-Metadata)
     - Metabolome
     - Metabolome - experimental protocol edition
   - 2.9 [BIOM or tabular files](https://github.com/mdsufz/NFDI4Microbiota-Metadata/tree/BIOM-and-tabular-files)

<br/><br/>

# Section 3. [Data transfer and data integrity](https://github.com/mdsufz/NFDI4Microbiota-Metadata/blob/Data-transfer-and-data-integrity/README.md)
   - Examples of existing data transfer & data integrity checks
   - Data integrity considerations by file type


# References
[^1]:Field, D., Garrity, G., Gray, T., Morrison, N., Selengut, J., Sterk, P., Tatusova, T., Thomson, N., Allen, M. J., Angiuoli, S. V., Ashburner, M., Axelrod, N., Baldauf, S., Ballard, S., Boore, J., Cochrane, G., Cole, J., Dawyndt, P., De Vos, P., DePamphilis, C., … Wipat, A. (2008). The minimum information about a genome sequence (MIGS) specification. Nature biotechnology, 26(5), 541–547. https://doi.org/10.1038/nbt1360, https://gensc.org/mixs/,  
https://gensc.org/publications-2/

[^2]:Kasmanas, J. C., Bartholomäus, A., Corrêa, F. B., Tal, T., Jehmlich, N., Herberth, G., von Bergen, M., Stadler, P. F., de Carvalho, A. & da Rocha, U. N. (2021). HumanMetagenomeDB: a public repository of curated and standardized metadata for human metagenomes. Nucleic Acids Research, 49(D1), D743–D750., https://webapp.ufz.de/hmgdb/

[^3]:Corrêa, F. B., Saraiva, J. P., Stadler, P. F. & da Rocha, U. N. (2020). TerrestrialMetagenomeDB: a public repository of curated and standardized metadata for terrestrial metagenomes. Nucleic Acids Research, 48(D1), D626-D632., https://webapp.ufz.de/tmdb/

[^4]:Bowers, R., Kyrpides, N., Stepanauskas, R. et al. Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. Nat Biotechnol 35, 725–731 (2017). https://doi.org/10.1038/nbt.3893, https://gensc.org/mixs/

[^5]: Murray, A.E., Freudenstein, J., Gribaldo, S. et al. Roadmap for naming uncultivated Archaea and Bacteria. Nat Microbiol 5, 987–994 (2020). https://doi.org/10.1038/s41564-020-0733-x, https://www.isme-microbes.org/seqcode-initiative

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
