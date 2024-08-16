## 2.9 BIOM or tabular files

| **metadata** | **definition**                                                                                                                                                                                      | **reference of definition\[<url_to_definition>\]**                                                  | **expected unit of measurement**            | **example**                                      | **sources( where this or similar matadata field is mentioned)**                       |     |
|--------|-----------|----------|---------|----------|----------|----------------|
| run_ref      | Accessions/identifiers linking to the raw data (FASTQ)                                                                                                                                              | [Link to reference](https://ena-docs.readthedocs.io/en/latest/submit/analyses/read-alignments.html) | run_accession in the format SRR, ERR or DRR | e.g. RUN_REF accession = “ERR178314”             | **Adapted from ENA** (“ENA How to Submit Other Analyses: Submitting Read Alignments”) |     |
| sop          | Reference(s) to Standard operating procedures used in generation of data or assembly and/or annotation of genomes, metagenomes or environmental sequences and link to text explanation of procedure | [MIXS:0000090](https://genomicsstandardsconsortium.github.io/mixs/0000090/)                         | PMID, DOI, URL                              | e.g. <https://doi.org/10.1038/s41586-020-2192-1> | **GSC MIXS: MIMARKSSpecimen** (“GSC MIXS: MIMARKSSpecimen”)                           |     |

| Comments/questions: |
|---------------------|
|                     |

# References

“ENA How to Submit Other Analyses: Submitting Read Alignments.”
<https://ena-docs.readthedocs.io/en/latest/submit/analyses/read-alignments.html>.

“GSC MIXS: MIMARKSSpecimen.”
<https://genomicsstandardsconsortium.github.io/mixs/MIMARKSSpecimen/>.
