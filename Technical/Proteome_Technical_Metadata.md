## 2.6 Proteomics

A searchable and exportable tab-separated
[table](Proteome_Technical_Metadata.tsv) of the following metadata is
now available.

## Minimal technical metadata for proteomics

| **metadata** | **definition** | **reference of definition\[<url_to_definition>\]** | **expected unit of measurement** | **example** | **sources (where this or similar matadata field is mentioned)** | |
|--------|-----------|----------|---------|----------|----------|----------------|
| Project title | Name of the project | | | e.g. Identification of a cryptic MHC-E epitope from influenza virus | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Project description | Overall description of the project | | | e.g. B6-CIITA-E cell line (C57Bl/6 fibroblasts expressing MHC-II molecules I-Ab and I-Ed) was infected with Influenza A virus (A/Puerto Rico/8/1934, PR8) or left uninfected (control), and the MHC-class II-associated peptidome analysed via immunopeptidomics. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Contact information | Person(s) responsible for contact including their affiliation | | | e.g. email address | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”), **MIAPE** (Taylor et al. 2007) |  | 
| Sample species | Species of the sample | | | e.g. Mus musculus (mouse) | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| PX_ID | Unique dataset identifier | | | e.g. PXD045025 | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Instrument | Description of the instrument or the mass spectrometer. | [\[MS:1000463\]](http://purl.obolibrary.org/obo/MS_1000463) | | e.g. Orbitrap Fusion Lumos | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Modifications | What post-translational modifications were done if applicable | | | e.g. iodoacetamide derivatized residue orNo PTMs are included in the dataset | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| File type | Type of file uploaded | | | e.g. RAW, SEARCH, RESULT, etc. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Ion source | The method by which gas phase ions are generated from the sample. | [\[MS:1000008\]](http://purl.obolibrary.org/obo/MS_1000008) | | Peptide ions were introduced to the mass spectrometer using an Easy-Spray Source at 2000 V | **MIAPE** (Taylor et al. 2007) |  | 
| DOI | Digital Object Identifier of the publication associated with the dataset | | | e.g. DOI: 10.1038/S41590-023-01644-5 | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Post source component | Analyzer & activation/dissociation type | | |  | **MIAPE** (Taylor et al. 2007) |  | 

| Comments/questions: |
|---------------------|
|                     |

##   Minimal technical metadata for proteomics - experimental protocol edition

| **metadata** | **definition** | **reference of definition\[<url_to_definition>\]** | **expected unit of measurement** | **example** | **sources (where this or similar matadata field is mentioned)** | |
|--------|-----------|----------|---------|----------|----------|----------------|
| Sample processing protocol | Short description of sample preparation including extraction, separation, enrichment, clean-up, digestion and mass spectrometry protocols | | | e.g. 200x106 B6-CIITA-Ed cells were either mock infected or PR8-infected in suspension in 0.1% BSA/PBS for 1 hr and incubated at 37 °C, 6% CO2 for ~18 hr. Cells were harvested with PBS containing 2 mM EDTA. Cell lysis and immunoprecipitation of peptide/MHC-II complexes were carried out largely as previously described55, and all chemicals used after cell harvest were analytical grade or equivalent when available. Following lysis, all steps were conducted in Protein LoBind tubes from Eppendorf or glass Econo-Columns (Bio-Rad 7371012). Briefly, anti-MHC-II antibody (clone M5/114.5, BioXCell) was cross-linked to Protein G Sepharose beads (GE 17061801). Lysates and beads were co-incubated and rotated overnight at 4 °C. After washing, peptide/MHC-II complexes were eluted in 10% acetic acid, and the collected material was lyophilized. After immunoprecipitation, purified peptide/MHC complexes were dissolved in 120 µl loading buffer (0.1% trifluoroacetic acid (TFA), 1% acetonitrile (ACN) in water). Using an Ultimate 300 HPLC system (Thermo Fisher), samples were loaded onto a 4.6 x 50-mm ProSwift RP-1S (Thermo Fisher) monolith column, and peptides were eluted by applying a 10 min linear gradient from 3% to 30% ACN in 0.1% TFA at a flow rate of 500 nl/min. Fractions were collected in 1-minute intervals. Alternate fractions (odd and even) were combined in two final fractions, dried, resuspended in 20 ul of loading buffer, and analyzed by LC-MS2. Peptides were analyzed by LC-MS2 using an Ultimate 3000 RSLCnano System supplemented with a PepMap C18 column (2 µm particle size, 75 µm × 50 cm, Thermo Fisher) directly interphased with an Orbitrap Fusion™ Lumos™ Tribrid™ Mass Spectrometer (Thermo Fisher). A 60 min linear gradient from 3% to 25% ACN in 5% DMSO/0.1% formic acid at a flow rate of 250 nl/min was applied for peptide elution. Peptide ions were introduced to the mass spectrometer using an Easy-Spray Source at 2000 V. Detection was performed with a resolution of 120,000 for full MS (300-1500 m/z scan range), and precursors were selected using TopSpeed ion selection within a 2 second cycle time, and a quadrupole isolation width of 1.2 amu for fragmentation. For MS2 acquisition, the resolution was set at 30,000 and high-energy collisional dissociation (HCD) energy was set at 28 for peptides with 2 to 4 charges and 32 for peptides that were singly charged. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”), **MIAPE** (Taylor et al. 2007) |  | 
| Data processing protocol | Short description of bioinformatics pipeline, software tools including versions, main search parameters and quantitative analysis | | | LC-MS2 datasets were analyzed using PEAKS v10.6 with the following parameters: precursor mass tolerance: 5 ppm; fragment mass tolerance: 0.05 Da; digestion: none; fixed modifications: none. The search database included the full reference sequences of the pDZ PR8 gene segments translated in all six reading frames (positive and negative sense), irrespective of start and stop codons, concatenated with the canonical PR8 viral proteome, and the reviewed mouse entries in Uniprot (Swissprot version 17 July 2019). For immunopeptidomics data, a threshold of -10lgP=20 was applied across all datasets, resulting in an estimate false discovery rate of ~1%. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”), **Adapted from MIAPE** (Taylor et al. 2007) |  | 
| Growth protocol | Description of the growth protocol or organism preparation | | | e.g. B6-CIITA-Ed cells were either mock infected or PR8-infected in suspension in 0.1% BSA/PBS for 1 hr and incubated at 37 °C, 6% CO2 for ~18 hr. Cells were harvested with PBS containing 2 mM EDTA. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Treatment protocol | Description of the treatments applied to the organism prior to sample acquisition | | |  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Extraction protocol | Description of the extraction of proteins from the treated sample(s) | | | Feces (100 mg) of mice were individually grounded with liquid nitrogen and the homogenate was resuspended with prechilled 80% methanol by well vortex. The samples were incubated on ice for 5 min and then were centrifuged at 15,000 x g, 4 °C for 20 min. Some of supernatant was diluted to final concentration containing 53% methanol by LC-MS grade water. The samples were subsequently transferred to a fresh Eppendorf tube and then were centrifuged at 15,000 x g, 4 °C for 20 min. Finally, the supernatant was injected into the LC-MS/MS system analysis. | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Separation protocol | Description of the separation of proteins and/or peptides | | |  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Digestion protocol | A technique for proteolysis of proteins into peptides by treatment with any of various enzymes. | [\[NCIT:C70845\]](http://purl.obolibrary.org/obo/NCIT_C70845) | |  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Acquisition protocol | Description of the acquisition of mass spectra from the peptide sample | | |  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 
| Protocol parameters | List of parameter names | | |  | **ProteomeXchange Consortium Guidelines** (“Data Submission Guidelines for the ProteomeXchange Consortium V3.0.1”) |  | 

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
