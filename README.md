# NFDI4Microbiota - Metadata Standards

> [!TIP]
> Find out about research data management, FAIR principles for microbiology and more on our [Knowledge Base](https://knowledgebase.nfdi4microbiota.de)!

The primary objective of this GitHub page is to serve as **a centralized
repository for existing (meta)data standards**. The purpose is to
provide the international microbiological community with a
**comprehensive and easily accessible compilation of established
standards**, facilitating efficient navigation and utilization for
researchers involved in collecting and submitting (meta)data to public
repositories.

The [NFDI4Microbiota](https://nfdi4microbiota.de) is a consortium that is part
of the German National research Data Infrastructure ([NFDI](https://www.nfdi.de/?lang=en)).
In line with the consortium’s objectives, this page aims to address the challenges of
microbial (meta)data accessibility and consistency. The efficient
exchange of usable information between research groups, sequencing
centers, and data repositories has been a long-standing issue. Measure
2.1 (M2.1 "Data and Metadata Standards") specifically focuses on maximizing data quality within the
[NFDI4Microbiota](https://nfdi4microbiota.de/)
consortium by enforcing compliance with existing standards and identifying
additional tailored data standards and metadata requirements.

[**Goals**](#goals): By centralizing standard parameters
for metadata, the project ensures that generated data is reproducible
and comparable both spatially and temporally. To achieve this, two
**milestones** have been set:

-   defining data standards for different types of **raw data**, and
    ensuring their quality and reliability
-   defining data standards for **technical metadata**, further
    enhancing the consistency and usability of the collected metadata.
    <br><br>

After additional consideration and overviews of the current literature,
the creators of this GitHub repository also agreed that the following
sections could and should be found here:

-   examples of **commonly used licenses** under which researchers can
    deposit data
-   brief description of use of **Ontologies** and how they help you
    describe your data

In the context of metadata quality standards in microbial science, two
main categories are being considered:

-   [**Technical**](#technical-metadata-standards)
-   [**Biological/Environmental**](#bio-env-metadata-standards) <br><br>

These categories aim to encompass the necessary information that
researchers collecting and submitting metadata to public repositories
need to provide. By adhering to these standardized metadata categories,
researchers can ensure the integrity and interoperability of their data,
enabling effective collaboration and comparative analysis within the
international microbiological community.

## 1. Reading this Github

-   Begin by reading the **[NFDI4Microbiota
    introduction](#N4Mintroduction), [Standards and
    Policies](#nfdi4microbiotastandardsandpolicies)** information, and
    **[Goals](#goals)**
-   Next, read the information regarding [**technical metadata standards
    section**](#technical-metadata-standards)
-   Third, read the [**biological/environmental metadata standards
    section**](#biological-and-environmental-metadata-standards)
-   Fourth if further explanation about licensing and ontologies is
    required, read [**Licenses and ontologies section**](#license-ontology)

[**Figure 1.**](#figure1) Outlines the key aspects considered for
determining minimal metadata standards that can be universally
applicable across various datasets and microbiomes. These aspects
encompass both technical and biological/environmental (Bio/Env)
considerations. The figure illustrates the comprehensive approach used
to establish minimal metadata standards for diverse research settings by
combining already established standards for differing data types and
biomes. <br><br>

<!---
For making the access link for other people not on the collaborator list, it should be better to use the relative address instead of the constant one.
Thus, I replace the "https://github.com/mdsufz/NFDI4Microbiota_MetadataStandards/blob/main" with "."
-->

<img src="./images/Overview24June2022.jpg" id="figure1"
alt="Overview" /> **Figure 1. Flow Chart of Technical and
Biological/Environmental Metadata Standard Development**

This flow chart illustrates the process of developing metadata standards
for both Technical and Biological/Environmental aspects. Technical
parameters are categorized based on data types, while Bio/Env parameters
are organized according to biome types. Additionally, specific
considerations, such as file type and host, are taken into account to
enhance the comprehensiveness of the standards.



# [Technical Metadata Standards](#technical-metadata-standards)

## 2. Technical metadata section

### 2.1. Data types

The following data types were considered when establishing minimal
**technical** metadata standards for M2.1:

-   Genomes
-   Amplicon
-   Metagenomes
-   Metagenome assembled genomes (MAGs)
-   Transcriptomes
-   Metatranscriptomes
-   Proteomes
-   Metaproteomes
-   Metabolomes<br><br>

Standard parameter considerations for FASTQ and FASTA formats are
displayed in [**Figure 2.**](#figure2) and [**Figure 3.**](#figure3),
respectively. Parameter applicability to different data types and the
time of data generation (i.e., before sequencing or during data
processing) are shown on the left and right, respectively.

Additionally, standards are being considered for [**data transfer and
data integrity**](#data-transfer-data-integrity) to ensure quality is
maintained throughout various processes of data file exchange. <br><br>

### 2.2. Overview of minimal technical FASTQ and FASTA metadata considerations

<img src="./images/MinimalTechnicalTable_FASTQ.jpg" id="figure2"
alt="FASTQMetadataTablesOverview" /> **Figure 2. Overview of Minimal
Technical Metadata for FASTQ Files**

This figure provides an overview of the minimal technical metadata
relevant to FASTQ files. The left side lists the applicability of
parameters to different data types, such as (meta)genome,
(meta)transcriptome, etc. On the right side, the time of metadata
generation is indicated. <br><br>

<img src="./images/MinimalTechnicalTable_FASTA.jpg" id="figure3"
alt="FASTAMetadataTablesOverview" /> **Figure 3. Overview of Minimal
Technical Metadata for FASTA Files**

This figure presents an overview of the minimal technical metadata
relevant to FASTA files. On the left side, the applicability of
parameters to different data types, including (meta)genome,
(meta)transcriptome, etc., is listed. The right side provides
information about the time of metadata generation. <br><br>

### 2.3. Minimal technical metadata by technology and file type

Establishing a file-specific metadata standard list poses a significant
challenge due to variations in file types across instruments used in
metabolomic and proteomic analyses. Thus, researchers can find the
metadata standards for each specific technology within corresponding
links. This approach recognizes the complexities of defining
comprehensive and universally applicable metadata standards that differ
based on technology.

-   2.3.1. [Genome Sequencing](./Technical/Genome_Technical_Metadata.md)
    -   Genomic FASTQ
    -   Genomic FASTA
-   2.3.2. [Amplicon
    Sequencing](./Technical/Amplicon_Technical_Metadata.md)
    -   Amplicon FASTQ
-   2.3.3. [Metagenome
    Sequencing](./Technical/Metagenome_Technical_Metadata.md)
    -   Metagenome FASTQ
    -   Metagenome FASTA
    -   Metagenome assembled genome (MAG) FASTA
-   2.3.4. [Transcriptome
    Sequencing](./Technical/Transcriptome_Technical_Metadata.md)
    -   Transcriptome FASTQ
    -   Transcriptome FASTA
-   2.3.5. [Metatranscriptome
    Sequencing](./Technical/Metatranscriptome_Technical_Metadata.md)
    -   Metatranscriptome FASTQ
    -   Metatranscriptome FASTA
-   2.3.6. [Proteome
    sequencing](./Technical/Proteome_Technical_Metadata.md)
    -   Proteome
    -   Proteome - experimental protocol edition
-   2.3.7. Metaproteome sequencing
-   2.3.8. [Metabolome
    sequencing](./Technical/Metabolome_Technical_Metadata.md)
    -   Metabolome
    -   Metabolome - experimental protocol edition
-   2.3.9. [uVIGs](./Technical/uVIGs_Technical_Metadata.md)
    -   uVIG FASTQ
    -   uVIG FASTA
- 2.3.10. [Virus Genomes](./Technical/Virus_Technical_Metadata.md)
    -  Virus genome FASTQ/A
-   2.3.11. [BIOM or tabular
    files](./Technical/BIOM_or_Tabular_Technical_Metadata.md)



### 2.4. Data transfer and data integrity

The work of the [Data transfer and data
integrity](./Technical/Data_Transfer_Data_Integrity.md) section focuses
on:

-   Examples of existing data transfer & data integrity checks
-   Data integrity considerations by file type 



# [Biological and Environmental Metadata Standards](#bio-env-metadata-standards)

## 3. Bio/Env metadata section

### 3.1. Biomes considered

Six microbiomes were considered to compile a minimal set of biological
and environmental metadata standards. Environmental and biological
parameters were identified as minimums applicable to individual biomes
and/or hosts.

The Minimal **Biological and Environmental** microbiome metadata
standards within M2.1 were collected to apply to the following biomes:

-   [Marine](./Biological_Environmental/Marine_BioEnv_Metadata.md)
-   [Terrestrial](./Biological_Environmental/Terrestrial_BioEnv_Metadata.md)
-   [Terrestrial
    (constructed)](./Biological_Environmental/TerrestrialConstructed_BioEnv_Metadata.md)
-   [Plant-associated](./Biological_Environmental/PlantAssoc_BioEnv_Metadata.md)
-   [Animal-associated](./Biological_Environmental/AnimalAssoc_BioEnv_Metadata.md)
-   [Human-associated](./Biological_Environmental/Human_BioEnv_Metadata.md)
-   Microbe-associated

Tentative standard minimal biological and environmental parameter
considerations are displayed in [**Figure 4**](#figure4). Parameter
applicability to different biomes are shown on the left axis.




<img src="./images/BioEnvMetadata9Aug2023.jpg" id="figure4"
alt="BioEnvMetadata23June2022" /> **Figure 4. Tentative Minimal
Biological and Environmental Metadata**.

This figure presents the division of minimal biological and
environmental metadata into distinct categories. Site metadata includes
specifications and environmental parameters related to the geographic
sampling location, while sample material and host metadata provide
information specific to host-associated systems. The applicability of
these standards to different microbiomes is shown on the left.
Additionally, conditional metadata standards encompass pertinent minimal
cultivation information.

The references in the figure are from the following sources:

-   **Marine references**:
    -   GSC MIxS: Water MIMS (“GSC MIxS: WaterMIMS”)
    -   ENA MMC: ENA Checklist: Marine Microalgae (“ENA Marine
        Microalgae Checklist; Checklist: ERC000043”)
    -   ENA Tara Oceans; Checklist: ERC000030 (“ENA Tara Oceans;
        Checklist: ERC000030”)
    -   GSC Minimum Information about any (x) Sequence (MIxS); ENA
        checklist: Water environment (“GSC MIxS Water; ENA Checklist:
        ERC000024”)
    -   The environment ontology: contextualising biological and
        biomedical entities (Buttigieg et al. 2013)
    -   The minimum information about a genome sequence (MIGS)
        specification (Field et al. 2008)
    -   Minimum information about a marker gene sequence (MIMARKS) and
        minimum information about any (x) sequence (MIxS) specifications
        (Yilmaz et al. 2011)
    -   A standard MIGS/MIMS compliant XML Schema: Toward the
        development of the Genomic Contextual Data Markup Language
        (GCDML) (Kottmann et al. 2008)
    -   Standard reporting requirements for biological samples in
        metabolomics experiments: environmental context (Morrison et al.
        2007)
-   **Terrestrial / Terrestrial(constructed)**
    -   GSC MIxS: Miscellaneous Natural Or Artificial Environment MIMS
        (“GSC MIxS: MiscellaneousNaturalOrArtificialEnvironmentMIMS”)
    -   GSC MIxS: Sediment MIMS (“GSC MIxS: SedimentMIMS”)
    -   GSC MIXS: Soil MIMS (“GSC MIxS: SoilMIMS”)
    -   GSC MIxS: Wastewater Sludge MIMS (“GSC MIxS:
        WastewaterSludgeMIMS”)
    -   GSC MIxS: Built Environment MIMS (“GSC MIxS:
        BuiltEnvironmentMIMS”)
    -   The environment ontology: contextualising biological and
        biomedical entities (Buttigieg et al. 2013)
    -   The minimum information about a genome sequence (MIGS)
        specification (Field et al. 2008)
    -   Minimum information about a marker gene sequence (MIMARKS) and
        minimum information about any (x) sequence (MIxS) specifications
        (Yilmaz et al. 2011)
    -   A standard MIGS/MIMS compliant XML Schema: Toward the
        development of the Genomic Contextual Data Markup Language
        (GCDML) (Kottmann et al. 2008)
    -   Standard reporting requirements for biological samples in
        metabolomics experiments: environmental context (Morrison et al.
        2007)
-   **Plant-associated**
    -   GSC MIxS: Plant-associated MIMS (“GSC MIxS:
        Plant-associatedMIMS”)
    -   GSC MIxS: Agriculture MIMS (“GSC MIxS: AgricultureMIMS”)
    -   GSC MIxS: Symbiont-associated MIMS (“GSC MIxS:
        Symbiont-associatedMIMS”)
    -   ENA MMC: ENA Checklist: Marine Microalgae (“ENA Marine
        Microalgae Checklist; Checklist: ERC000043”)
    -   The environment ontology: contextualising biological and
        biomedical entities (Buttigieg et al. 2013)
    -   The minimum information about a genome sequence (MIGS)
        specification (Field et al. 2008)
    -   Minimum information about a marker gene sequence (MIMARKS) and
        minimum information about any (x) sequence (MIxS) specifications
        (Yilmaz et al. 2011)
    -   A standard MIGS/MIMS compliant XML Schema: Toward the
        development of the Genomic Contextual Data Markup Language
        (GCDML) (Kottmann et al. 2008)
    -   Standard reporting requirements for biological samples in
        metabolomics experiments: environmental context (Morrison et al.
        2007)
-   **Animal-associated**
    -   GSC MIxS: Host-associated MIMS (“GSC MIxS: Host-associatedMIMS”)
    -   The environment ontology: contextualising biological and
        biomedical entities (Buttigieg et al. 2013)
    -   The minimum information about a genome sequence (MIGS)
        specification (Field et al. 2008)
    -   Minimum information about a marker gene sequence (MIMARKS) and
        minimum information about any (x) sequence (MIxS) specifications
        (Yilmaz et al. 2011)
    -   A standard MIGS/MIMS compliant XML Schema: Toward the
        development of the Genomic Contextual Data Markup Language
        (GCDML) (Kottmann et al. 2008)
    -   Standard reporting requirements for biological samples in
        metabolomics experiments: environmental context (Morrison et al.
        2007)
-   **Human-associated**
    -   MIMS: metagenome/environmental, human-associated; version 6.0
        Package (“MIMS: Metagenome/Environmental, Human-Associated;
        Version 6.0 Package”)
    -   GSC MIxS human associated; ENA Checklist: ERC000014 (“GSC MIxS
        Human Associated; ENA Checklist: ERC000014”)
    -   GSC MIxS: Human-associated MIMS (“GSC MIxS:
        Human-associatedMIMS”)
    -   GSC MIxS: Human-gut MIMS (“GSC MIxS: Human-gutMIMS”)
    -   GSC MIxS: Human-oral MIMS (“GSC MIxS: Human-oralMIMS”)
    -   GSC MIxS: Human-skin MIMS (“GSC MIxS: Human-skinMIMS”)
    -   GSC MIxS: Human-vaginal MIMS (“GSC MIxS: Human-vaginalMIMS”)
    -   The environment ontology: contextualising biological and
        biomedical entities (Buttigieg et al. 2013)
    -   The minimum information about a genome sequence (MIGS)
        specification (Field et al. 2008)
    -   Minimum information about a marker gene sequence (MIMARKS) and
        minimum information about any (x) sequence (MIxS) specifications
        (Yilmaz et al. 2011)
    -   A standard MIGS/MIMS compliant XML Schema: Toward the
        development of the Genomic Contextual Data Markup Language
        (GCDML) (Kottmann et al. 2008)
    -   Standard reporting requirements for biological samples in
        metabolomics experiments: environmental context (Morrison et al.
        2007)
    -   U.S. Office of Management and Budget (OMB): About the Topic of
        Race (“U.s. Office of Management and Budget (OMB): About the
        Topic of Race”)

### 3.2. Data/metadata categorization

The categorization framework in [**Figure 5**](#figure5) should be
considered when determining the applicable metadata standards for each
dataset. This framework can serve as a valuable tool for connecting
information about samples from marine, terrestrial, or engineered
systems. Additionally, it facilitates the inclusion of cultivated
samples, whether they were cultured from a commercially-available source
or isolated from an environmental sample by the user.

To enhance searchability in downstream analyses, users can select
multiple environment categories if relevant. For instance, they may
choose both “marine” and “terrestrial” for a tidal flat site,
“engineered” and “terrestrial” for a greenhouse agricultural site, or
“engineered” and “marine” for a commercially-available culture initially
isolated from the ocean. <br><br>

#### **Category Flow Chart**

<img src="./images/CategoryFlowchart.JPG" id="figure5" />

**Figure 5. Tentative Categorization Framework for
Biological/Environmental Metadata Requirements**

This figure showcases a preliminary categorization framework to
establish minimal biological/environmental metadata requirements. The
framework connects host-associated systems to marine, terrestrial, or
engineered environments while enabling effective tracking of data
affiliated with cultivated samples. The structure should provide
valuable insights for organizing and comprehensively accessing diverse
datasets.



**Figures 6 - 8** show examples of minimal biological/environmental
metadata applicability to different sample categorizations. 



#### **Human Gut Example**

![](./images/CategoryFrameworkSlides_HumanGutExample_mb.gif) **Figure 6.
Example of Categorizing a Human Gut-Associated and Cultivated Sample
with Applicable Minimal Metadata**

This figure provides an illustrative example of the categorization
process for a human gut-associated and cultivated sample. It showcases
the minimal metadata that are applicable and relevant for this specific
sample type.



#### **Tidal Flat Example**

![](./images/CategoryFrameworkSlides_TidalFlatExample_mb.gif) **Figure
7. Example of Categorizing a Tidal Flat and Cultivated Sample with
Applicable Minimal Metadata**

This figure presents a practical example of categorizing a tidal flat
cultivated sample, along with the relevant minimal metadata. The
illustration demonstrates how the proposed framework accommodates
overlapping environments, such as terrestrial and marine, specifically
for intertidal regions.



#### **Lab Culture Example**

![](./images/CategoryFrameworkSlides_LabCultureExample_mb.gif) **Figure
8. Example of Categorizing a Known Lab Cultured Sample with Applicable
Minimal Metadata**

This figure presents an example of categorizing a known lab-cultured
sample, along with the corresponding minimal metadata. The
bidirectionality of the categorization framework is highlighted, as it
enables the linkage between known, commercially available cultures and
their original sample environments.



# [Licenses and ontologies](#license-ontology)

## 4. Use of licenses for deposited data

When depositing data to public repositories, researchers can use
established licenses to set certain restrictions on its use **or**
requiring certain acknowledgments when reusing it **or** publish it to
the public domain without any limitations. Licensing your data under
specific licenses enables other researchers to reuse your data (under
certain conditions), without explicit permission from the data
submitter. In any case, it is recommended to consider various factors
before deciding upon a deed (license). Ethical, privacy, and security
considerations may heavily influence the licensing process. The most
common licenses under use were established by a US non-profit
organization called [Creative Commons
(CC)](https://creativecommons.org/). We encourage the readers of this
repository to visit their site and familiarize themselves with the
process, logic, and use of licenses in detail. The CC homepage also
holds the [Frequently Asked Questions
(FAQ)](https://creativecommons.org/faq/) section. Here, we will only
briefly describe some of the [CC
licenses](https://creativecommons.org/share-your-work/cclicenses/). So,
in the end, researchers should think about how they want other people to
use their work and why they want to share their work in the first place
before deciding upon a deed (license).

Commonly used licenses:

-   [CC-BY](https://creativecommons.org/licenses/by/4.0/): Credit must
    be given to the creator.
-   [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/): Credit
    must be given to the creator. Adaptations must be shared under the
    same terms.
-   [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/): Credit
    must be given to the creator. Only noncommercial uses of the work
    are permitted.
-   [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/):
    Credit must be given to the creator. Only noncommercial uses of the
    work are permitted. Adaptations must be shared under the same terms.
-   [CC BY-ND](https://creativecommons.org/licenses/by-nd/4.0/): Credit
    must be given to the creator. No derivatives or adaptations of the
    work are permitted.
-   [CC BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/):
    Credit must be given to the creator. Only noncommercial uses of the
    work are permitted. No derivatives or adaptations of the work are
    permitted.
-   [CC0](https://creativecommons.org/publicdomain/zero/1.0/): Public
    domain dedication.


<table style="width:60%;">
<tr>
<th style="text-align: center;">
Acronym
</th>
<th style="text-align: center;">
Explanation
</th>
</tr>
<tr>
<td style="text-align: center;">
BY
</td>
<td style="text-align: center;">
Credit must be given to the creator
</td>
</tr>
<tr>
<td style="text-align: center;">
SA
</td>
<td style="text-align: center;">
Adaptations must be shared under the same terms
</td>
</tr>
<tr>
<td style="text-align: center;">
NC
</td>
<td style="text-align: center;">
Only noncommercial uses of the work are permitted
</td>
</tr>
<tr>
<td style="text-align: center;">
ND
</td>
<td style="text-align: center;">
No derivatives or adaptations of the work are permitted
</td>
</tr>
<tr>
<td style="text-align: center;">
0
</td>
<td style="text-align: center;">
Public domain dedication
</td>
</tr>
</table>




[CC-BY](https://creativecommons.org/licenses/by/4.0/): When data is
deposited under this deed (license), and it becomes free to share and
free to redistribute, including commercially, in any format or medium.
It also allows the user to build upon or transform the data/material for
any purpose, including commercial purposes. The deed (license) requires
the data reuser to give appropriate credit to the submitter/data
generator. In addition, the reuser must also provide a link to the deed
(license) and disclose any changes made when licensing their work when
derived from work already under deed (license).<br><br>

[CC0](https://creativecommons.org/publicdomain/zero/1.0/): When using
this deed (license), the data/material becomes a part of the public
domain. That means that the data deposited can be copied, modified,
distributed, and used even for commercial purposes, and the
depositor/generator of the data waives their right to the work. The
reuser of data does not need to seek the permission of the data/material
submitter or generator.

## 5. Use of controlled vocabularies (Ontologies)

Before diving into how controlled vocabularies (also known as ontologies) are used, let us first clearly understand what they are and why they are important. Throughout this section, we will use the terms *controlled vocabulary* and *ontology* interchangeably.

Imagine traveling back a few centuries to a time when Latin was the common language among scholars. Regardless of their native language or culture, scientists and scholars used Latin to communicate their ideas clearly and consistently. This shared language allowed ideas to spread widely, bridging gaps in distance, language, and even time. 

In a similar way, today we use controlled vocabularies to create a common language among researchers, and even between humans and computers. Ontologies standardize the meaning of terms within a specific scientific field, reducing confusion and making communication clearer. They help scientists clearly organize data, easily navigate large datasets, and discover new patterns or insights. Moreover, ontologies evolve continuously. New terms, definitions, and classifications are regularly added as our scientific knowledge expands. 

Sometimes it can feel overwhelming because multiple ontologies exist or a particular term has not yet been clearly defined. But do not be discouraged! As you gain experience, using controlled vocabularies will become second nature.

### 5.1 Practical Example: How to use Ontologies

To understand how ontologies can be practically applied, let us walk through an imaginary scenario. Suppose you are planning an experiment to collect metagenomic samples. You want to clearly record details such as where the samples were taken and how the data was obtained. For this example, let us say you collected your samples from the rhizosphere (the soil surrounding plant roots) of a forest in Germany and used Illumina sequencing technology for analysis. How would you clearly and precisely document these details?

First, you would visit an ontology service, such as the [EMBL-EBI Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/) or [OBO foundry](https://obofoundry.org/). Since you're just starting out, you might begin with a broad term like **biome** [\[ENVO_00000428\]](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000428?lang=en). By searching for "biome," you’ll find a list of [related terms](https://www.ebi.ac.uk/ols4/search?q=biome). One of these subclasses is **terrestrial biome** [\[ENVO:00000446\]](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000446?lang=en). But this might still be too broad, so you'll keep searching. After exploring further, you'll find the subclass **woodland biome** [\[ENVO:01000175\]](http://purl.obolibrary.org/obo/ENVO_01000175), and eventually the more specific subclass **temperate woodland biome** [\[ENVO:01000221\]](http://purl.obolibrary.org/obo/ENVO_01000221). This accurately describes the general environment of your sample. This accurately describes the general environment of your sample.Next, you might look up the more specific term **rhizosphere** to pinpoint the exact origin of your sample. Searching for [rhizosphere](https://www.ebi.ac.uk/ols4/search?q=rhizosphere+) returns a useful term: **rhizosphere environment** [\[ENVO:01000999\]](http://purl.obolibrary.org/obo/ENVO_01000999), defined as "an environmental system determined by the presence of a plant rhizosphere." Perfect! Now you've precisely defined the exact location of your sample collection.

Similarly, you can specify that your samples were collected in Germany at **Naturpark Frankenwald** [\[GAZ:00632507\]](http://purl.obolibrary.org/obo/GAZ_00632507), that your sequencing was done with **Illumina Sequencing**
[\[NCIT:C146817\]](http://purl.obolibrary.org/obo/NCIT_C146817), and even describe that you used a **minimal defined medium** [\[MCO:0000881\]](http://purl.obolibrary.org/obo/MCO_0000881).

If you find the examples here challenging or want more information, we strongly recommend visiting the [EnvO s use documentation](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS) which provides more detailed guidance.

Clearer examples of onotolgy uses for different Biomes and environments can also be found in this [GitHub page](./Biological_Environmental/) for seven different considered biomes.

It is however, also important to note, that in some cases some metadata annotations can not be possible with ontologies, values or free text, as the metadata fields is either not applicable to the project, was not collected or recorded or simply not provided due to ethical and legal resons. These different reasons for an absent value are explained in the table bellow.

|Phrase |Reason for use |When does it apply |INSDC token |DataCite code |ISO/GML (nilReason)|Definition|
|-------|---------------|-------------------|------------|--------------|-------|----------|
|not applicable; <br> not relevant |Field is outside the scope of the experiment |Depth for human stool sample |**not applicable** <br> for a control **missing: control sample** |**:unap**|**inapplicable**|Information is inappropriate to report; sometimes shows a gap in the standard itself.|
|not available|Value exists somewhere, but you cannot obtain it|Host BMI missing from a 1990 gut study| Top level: **missing** <br> or: **missing: third party data**| **:unav** | **missing**|Information of an expected format was not given because it is unavailable or unretrievable, with no expectation of later supply.|
|not recorded |Measurement was never captured|Ambient temperature not recorded during environmental swabbing| **missing: not collected** <br> **missing: lab stock** | **:unav**| **missing**|Information was expected but never collected at source.|
|not provided |Value exists but is under embargo / pending| Exact collection date withheld until publication of the clinical trial| **not provided**| **:tba**| **template** <br> or **other:pending**|Information of an expected format was not given now, but will be supplied later.|
|restricted access|Value exists but must remain confidential| Coordinates of endangered species or patient postcode that could be used to identify individual| **restricted access** | **:unal** <br> or **:unac** if the restriction is temporary | **withheld**|Information exists but cannot be released openly because of privacy, conservation or legal constraints.|

Sources: <br>
[INSDC Missing Value Reporting Terms](https://www.insdc.org/technical-specifications/missing-value-reporting/); <br>
[DataCite - Appendix 3: Standard values for unknown information](https://datacite-metadata-schema.readthedocs.io/en/4.6/appendices/appendix-3/#appendix-3-standard-values-for-unknown-information); <br>
[ISO 19115-3](https://schemas.isotc211.org/19115/-3/gco/1.0/gco/) <br>


# About

 [![CC BY License illustration](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/) This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

# References

Bowers, R., N. Kyrpides, R. Stepanauskas, et al. 2017. “Minimum
Information about a Single Amplified Genome (MISAG) and a
Metagenome-Assembled Genome (MIMAG) of Bacteria and Archaea.” *Nat
Biotechnol* 35: 725–31. <https://doi.org/10.1038/nbt.3893>.

Buttigieg, P. L., N. Morrison, B. Smith, C. J. Mungall, S. E. Lewis, and
ENVO Consortium. 2013. “The Environment Ontology: Contextualising
Biological and Biomedical Entities.” *Journal of Biomedical Semantics* 4
(1): 43. <https://doi.org/10.1186/2041-1480-4-43>.

“ENA Marine Microalgae Checklist; Checklist: ERC000043.”
<https://www.ebi.ac.uk/ena/browser/view/ERC000043>.

“ENA Tara Oceans; Checklist: ERC000030.”
<https://www.ebi.ac.uk/ena/browser/view/ERC000030>.

Field, D., G. Garrity, T. Gray, N. Morrison, J. Selengut, P. Sterk, T.
Tatusova, et al. 2008. “The Minimum Information about a Genome Sequence
(MIGS) Specification.” Nature Biotechnology. 2008.
<https://doi.org/10.1038/nbt1360>.

“German National Research Data Infrastructure.”
<https://www.nfdi.de/?lang=en>.

“GSC MIxS Human Associated; ENA Checklist: ERC000014.”
<https://www.ebi.ac.uk/ena/browser/view/ERC000014>.

“GSC MIxS Water; ENA Checklist: ERC000024.”
<https://www.ebi.ac.uk/ena/browser/view/ERC000024>.

“GSC MIxS: AgricultureMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/AgricultureMIMS/>.

“GSC MIxS: BuiltEnvironmentMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/BuiltEnvironmentMIMS/>.

“GSC MIxS: Host-associatedMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Host-associatedMIMS/>.

“GSC MIxS: Human-associatedMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Human-associatedMIMS/>.

“GSC MIxS: Human-gutMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Human-gutMIMS/>.

“GSC MIxS: Human-oralMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Human-oralMIMS/>.

“GSC MIxS: Human-skinMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Human-skinMIMS/>.

“GSC MIxS: Human-vaginalMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Human-vaginalMIMS/>.

“GSC MIXS: MicrobialMatBiofilmMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/MicrobialMatBiofilmMIMS/>.

“GSC MIxS: MiscellaneousNaturalOrArtificialEnvironmentMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/MiscellaneousNaturalOrArtificialEnvironmentMIMS/>.

“GSC MIxS: Plant-associatedMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Plant-associatedMIMS/>.

“GSC MIxS: SedimentMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/SedimentMIMS/>.

“GSC MIxS: SoilMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/SoilMIMS/>.

“GSC MIxS: Symbiont-associatedMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/Symbiont-associatedMIMS/>.

“GSC MIxS: WastewaterSludgeMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/WastewaterSludgeMIMS/>.

“GSC MIxS: WaterMIMS.”
<https://genomicsstandardsconsortium.github.io/mixs/WaterMIMS/>.

Kottmann, R., T. Gray, S. Murphy, L. Kagan, S. Kravitz, T. Lombardot, D.
Field, F. O. Glöckner, and Genomic Standards Consortium. 2008. “A
Standard MIGS/MIMS Compliant XML Schema: Toward the Development of the
Genomic Contextual Data Markup Language (GCDML).” OMICS: A Journal of
Integrative Biology. 2008. <https://doi.org/10.1089/omi.2008.0A10>.

“MIMS: Metagenome/Environmental, Human-Associated; Version 6.0 Package.”
<https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.human-associated.5.0/>.

Morrison, Norman, Daniel Bearden, Jacob G. Bundy, Timothy Collette,
Fraser Currie, Matthew Davey, Migdalia Dominguez, et al. 2007. “Standard
Reporting Requirements for Biological Samples in Metabolomics
Experiments: Environmental Context.” *Metabolomics* 3 (2): 203–10.
<https://doi.org/10.1007/s11306-007-0067-1>.

Murray, A. E., J. Freudenstein, S. Gribaldo, et al. 2020. “Roadmap for
Naming Uncultivated Archaea and Bacteria.” *Nat Microbiol* 5: 987–94.
<https://doi.org/10.1038/s41564-020-0733-x>.

“NFDI4Microbiota.” <https://nfdi4microbiota.de/>.

“U.s. Office of Management and Budget (OMB): About the Topic of Race.”
<https://www.census.gov/topics/population/race/about.html>.

Yilmaz, Pelin et al. 2011. “Minimum Information about a Marker Gene
Sequence (MIMARKS) and Minimum Information about Any (x) Sequence (MIxS)
Specifications.” *Nature Biotechnology* 29 (5): 415–20.
<https://doi.org/10.1038/nbt.1823>.
