# Section 3. Data transfer and data integrity

## `Examples of existing data transfer & data integrity checks`

| **Repository or tool source** | **Data transfer integrity checks in place**                                                                                                                                                                                                                                                                             |
|-------------------------|------------------------------------------------|
| ENA                           | MD5sum available for “most” downloads. Submission tool generates this, otherwise user needs to upload [“Common Run Submission Errors”](https://ena-docs.readthedocs.io/en/latest/faq/runs.html)                                                                                                                     |
| NCBI GEO                      | MD5 “recommended” for submissions [“Submitting High-Throughput Sequence Data to GEO”](https://www.ncbi.nlm.nih.gov/geo/info/seq.html)                                                                                                                                                                                   |
| NCBI SRA                      | MD5 is a parameter during submission (as of the 2010 guide [“SRA Submission Quick Start Guide”](https://anonsvn.ncbi.nlm.nih.gov/repos/v1/trunk/sra/doc/SRA_1-1/SRA_Quick_Start_Guide.pdf)) There is a ‘vdb-validate’ tool for checking download integrity [“SRA-Tools”](https://github.com/ncbi/sra-tools/tree/master) |
| MGnify                        | “Intermediate checksums” in **MGnify: the microbiome analysis resource in 2020** ([Mitchell et al. (2020)](https://doi.org/10.1093/nar/gkz1035))                                                                                                                                                                        |
| MG RAST                       | “Data hygiene” (Preprocessing, dereplication, DRISEE, screening) ([Meyer et al. (2008)](https://help.mg-rast.org/user_manual.html#data-hygiene))                                                                                                                                                                        |

| Comments/questions: |
|---------------------|
|                     |

## `Data integrity considerations by file type`

| **File type** | **Integrity check**                                                                                                                                                                         | **Other considerations for quality and transferability** |
|------------------|------------------------------------|------------------|
| FASTQ         | Read count, checksum (MD5sum, SEGUID ([Bassi and Gonzalez (2007)](https://doi.org/10.1038/npre.2007.278.1)), ([Babnigg and Giometti (2006)](https://doi.org/10.1002/pmic.200600032)), etc.) | Determination of +33/+64 format from compressed files    |
| FASTA         | Read count, checksum (MD5sum, SEGUID ([Bassi and Gonzalez (2007)](https://doi.org/10.1038/npre.2007.278.1)), ([Babnigg and Giometti (2006)](https://doi.org/10.1002/pmic.200600032), etc.)  |                                                          |
| .faa          | SEGUID ([Bassi and Gonzalez (2007)](https://doi.org/10.1038/npre.2007.278.1)), ([Babnigg and Giometti (2006)](https://doi.org/10.1002/pmic.200600032)                                       | Annotation pipeline, assembly quality                    |
| GFF/GTF       |                                                                                                                                                                                             | Annotation pipeline, assembly quality                    |

| Comments/questions: |
|---------------------|
|                     |

# References

Babnigg, G., and C. S. Giometti. 2006. “A Database of Unique Protein
Sequence Identifiers for Proteome Studies.” *Proteomics* 6: 4514–22.
<https://doi.org/10.1002/pmic.200600032>.

Bassi, S., and V. Gonzalez. 2007. “New Checksum Functions for
Biopython.” *Nat Prec*. <https://doi.org/10.1038/npre.2007.278.1>.

“Common Run Submission Errors.”
<https://ena-docs.readthedocs.io/en/latest/faq/runs.html>.

Meyer, F., D. Paarmann, M. D’Souza, R. Olson, E. M. Glass, M. Kubal, T.
Paczian, et al. 2008. “The Metagenomics RAST Server — a Public Resource
for the Automatic Phylogenetic and Functional Analysis of Metagenomes.”
*BMC Bioinformatics* 9: 386.
<https://help.mg-rast.org/user_manual.html#data-hygiene>.

Mitchell, Alex L, Alexandre Almeida, Martin Beracochea, Miguel Boland,
Josephine Burgin, Guy Cochrane, Michael R Crusoe, et al. 2020. “MGnify:
The Microbiome Analysis Resource in 2020.” *Nucleic Acids Research* 48
(D1): D570–78. <https://doi.org/10.1093/nar/gkz1035>.

“SRA Submission Quick Start Guide.”
<https://anonsvn.ncbi.nlm.nih.gov/repos/v1/trunk/sra/doc/SRA_1-1/SRA_Quick_Start_Guide.pdf>.

“SRA-Tools.” <https://github.com/ncbi/sra-tools/tree/master>.

“Submitting High-Throughput Sequence Data to GEO.”
<https://www.ncbi.nlm.nih.gov/geo/info/seq.html>.
