## 2.6 Proteomics

A searchable and exportable tab-separated
[table](Proteome_Technical_Metadata.tsv) of the following metadata is
now available.

## Minimal technical metadata for proteomics

| **metadata**          | **definition/examples**                                             | **source**                                                                                                                                                    |
|------------------|------------------------------------|------------------|
| Project title         | Name of the project                                                 | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Project description   | Overall description of the project                                  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Contact information   | person(s) responsible for contact including their affiliation       | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13), **MIAPE** (Taylor et al. 2007) |
| Sample species        | Species of the sample                                               | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| PX_ID                 | Unique dataset identifier                                           | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Instrument            | Mass spectrometer & manufacturer                                    | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Modifications         | What post-translational modifications were done if applicable       | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| File type             | Type of file uploaded (e.g. RAW, SEARCH, RESULT, etc.)              | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Ion source            | ESI, MALDI or other ionisation source including relevant parameters | **MIAPE** (Taylor et al. 2007)                                                                                                                                |
| DOI                   | ID number of the publication associated with the dataset            | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                 |
| Post source component | Analyzer & activation/dissociation type                             | **MIAPE** (Taylor et al. 2007)                                                                                                                                |

| Comments/questions: |
|---------------------|
|                     |

##   Minimal technical metadata for proteomics - experimental protocol edition

| **metadata**               | **definition/examples**                                                                                                                   | **source**                                                                                                                                                                 |
|------------------|------------------------------------|------------------|
| Sample processing protocol | short description of sample preparation including extraction, separation, enrichment, clean-up, digestion and mass spectrometry protocols | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13), **MIAPE** (Taylor et al. 2007)              |
| Data processing protocol   | short description of bioinformatics pipeline, software tools including versions, main search parameters and quantitative analysis         | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13), **Adapted from MIAPE** (Taylor et al. 2007) |
| Growth protocol            | description of the growth protocol or organism preparation                                                                                | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Treatment protocol         | description of the treatments applied to the organism prior to sample acquisition                                                         | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Extraction protocol        | description of the extraction of proteins from the treated sample(s)                                                                      | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Separation protocol        | description of the separation of proteins and/or peptides                                                                                 | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Digestion protocol         | description of the digestion of the proteins into peptides                                                                                | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Acquisition protocol       | description of the acquisition of mass spectra from the peptide sample                                                                    | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |
| Protocol parameters        | list of parameter names                                                                                                                   | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1” 2019-10-13)                                              |

| Comments/questions:                                                            |
|------------------------------------------------------------------------|
| 🔹 Discussion question: one or two fields for protocols or more? -SS 02May2022 |

We also highly encourage the readers of this GitHub to look for examples
of submitted proteomic samples and analyses in **PRIDE: PRoteomics
IDEntifications Database** (“PRIDE: PRoteomics IDEntifications
Database”), **PeptideAtlas** (“PeptideAtlas”), **MassIVE: Mass
Spectrometry Interactive Virtual Environment** (“MassIVE: Mass
Spectrometry Interactive Virtual Environment”), **iProX: Integrated
Proteome Resources** (“iProX: Integrated Proteome Resources”) and read
the publication and view the corresponding repository of **jPOSTrepo: an
international standard data repository for proteomes** (Okuda et al.
2017).

# References

“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1.”
2019-10-13. 2019-10-13.
<https://www.proteomexchange.org/docs/guidelines_px.pdf>.

“iProX: Integrated Proteome Resources.”
<https://www.iprox.cn/page/helpEn.html#pag5>.

“MassIVE: Mass Spectrometry Interactive Virtual Environment.”
<https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp>.

Okuda, Shujiro, Yu Watanabe, Yuki Moriya, Shin Kawano, Tadashi Yamamoto,
Masaki Matsumoto, Tomoyo Takami, et al. 2017.
“<span class="nocase">jPOSTrepo</span>: An International Standard Data
Repository for Proteomes.” *Nucleic Acids Research* 45 (D1): D1107–11.
<https://doi.org/10.1093/nar/gkw1080>.

“PeptideAtlas.” <https://peptideatlas.org/>.

“PRIDE: PRoteomics IDEntifications Database.”
<https://www.ebi.ac.uk/pride/markdownpage/submitdatapage#submit_dataset>.

Taylor, Chris, Norman Paton, Kathryn Lilley, Pierre-Alain Binz, Randall
K Julian, Andrew R Jones, Weimin Zhu, Rolf Apweiler, Ruedi Aebersold,
and Eric W Deutsch. 2007. “The Minimum Information about a Proteomics
Experiment (MIAPE).” *Nature Biotechnology* 25 (8): 887–93.
<https://doi.org/10.1038/nbt1329>.
