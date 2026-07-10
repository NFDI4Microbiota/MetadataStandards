# Representing complex study designs

## Common relationships

| Relationship | Example | Recommended metadata handling |
|---|---|---|
| Original sample → subsample | soil core → sieved aliquot | Keep both identifiers and link with `derived_from` |
| Host → body site sample | participant P001 → stool sample S001 | Keep de-identified host ID and sample ID |
| Sample → extract | stool sample → DNA extract | Record extraction method, date, and extract ID |
| Extract → library | DNA extract → sequencing library | Record library strategy, selection, layout, platform |
| Raw data → processed output | FASTQ → BIOM table | Record software, version, parameters, and source files |
| Time series | same subject sampled monthly | Record time point, interval, and repeated-measure design |
| Treatment/control | treated soil vs untreated soil | Record treatment, dose, timing, control definition |
