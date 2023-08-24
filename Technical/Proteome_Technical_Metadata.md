## 2.6 Proteomics

A searchable and exportable tab-separated
[table](Proteome_Technical_Metadata.tsv) of the following metadata is
now available.

## Minimal technical metadata for proteomics

| **metadata**          | **definition/examples**                                             | **source**                                                                                                                                                                                            |
|------------------|------------------------------------|------------------|
| Project title         | Name of the project                                                 | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Project description   | Overall description of the project                                  | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Contact information   | person(s) responsible for contact including their affiliation       | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf), **MIAPE** ([Taylor et al. (2007)](https://doi.org/10.1038/nbt1329)) |
| Sample species        | Species of the sample                                               | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| PX_ID                 | Unique dataset identifier                                           | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Instrument            | Mass spectrometer & manufacturer                                    | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Modifications         | What post-translational modifications were done if applicable       | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| File type             | Type of file uploaded (e.g. RAW, SEARCH, RESULT, etc.)              | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Ion source            | ESI, MALDI or other ionisation source including relevant parameters | **MIAPE** ([Taylor et al. (2007)](https://doi.org/10.1038/nbt1329))                                                                                                                                   |
| DOI                   | ID number of the publication associated with the dataset            | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                      |
| Post source component | Analyzer & activation/dissociation type                             | **MIAPE** ([Taylor et al. (2007)](https://doi.org/10.1038/nbt1329))                                                                                                                                   |

| Comments/questions: |
|---------------------|
|                     |

##   Minimal technical metadata for proteomics - experimental protocol edition

| **metadata**               | **definition/examples**                                                                                                                   | **source**                                                                                                                                                                                                         |
|------------------|------------------------------------|------------------|
| Sample processing protocol | short description of sample preparation including extraction, separation, enrichment, clean-up, digestion and mass spectrometry protocols | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf), **MIAPE** ([Taylor et al. (2007)](https://doi.org/10.1038/nbt1329))              |
| Data processing protocol   | short description of bioinformatics pipeline, software tools including versions, main search parameters and quantitative analysis         | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf), **Adapted from MIAPE** ([Taylor et al. (2007)](https://doi.org/10.1038/nbt1329)) |
| Growth protocol            | description of the growth protocol or organism preparation                                                                                | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Treatment protocol         | description of the treatments applied to the organism prior to sample acquisition                                                         | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Extraction protocol        | description of the extraction of proteins from the treated sample(s)                                                                      | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Separation protocol        | description of the separation of proteins and/or peptides                                                                                 | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Digestion protocol         | description of the digestion of the proteins into peptides                                                                                | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Acquisition protocol       | description of the acquisition of mass spectra from the peptide sample                                                                    | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |
| Protocol parameters        | list of parameter names                                                                                                                   | [“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”](https://www.proteomexchange.org/docs/guidelines_px.pdf)                                                                                   |

| Comments/questions:                                                            |
|------------------------------------------------------------------------|
| 🔹 Discussion question: one or two fields for protocols or more? -SS 02May2022 |

We also highly encourage the readers of this GitHub to look for examples
of submitted proteomic samples and analyses in [“PRIDE: PRoteomics
IDEntifications
Database”](https://www.ebi.ac.uk/pride/markdownpage/submitdatapage#submit_dataset),
[“PeptideAtlas”](https://peptideatlas.org/), [“MassIVE: Mass
Spectrometry Interactive Virtual
Environment”](https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp),
[“iProX: Integrated Proteome
Resources”](https://www.iprox.cn/page/helpEn.html#pag5) and read the
publication and view the corresponding repository of **jPOSTrepo: an
international standard data repository for proteomes** ([Okuda et al.
(2017)](https://doi.org/10.1093/nar/gkw1080)).

# References

“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1.”
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
