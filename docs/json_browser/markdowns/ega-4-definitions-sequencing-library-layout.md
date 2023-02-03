# Sequencing library layout Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment/properties/libraryLayout
```

Whether the sequenced reads are paired or single. In other words, if the sequencing assay is paired- (OBI:0001850) or single-end (OBI:0002485). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## libraryLayout Type

`string` ([Sequencing library layout](ega-4-definitions-sequencing-library-layout.md))

## libraryLayout Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"paired-end"` | \[OBI:0001850]: A transcription profiling assay that determines transcripts, gene structures, and gene expressions using Paired-End Tags and sequencing technology. Allows to sequence both ends of a fragment and generate high-quality, alignable sequence data. Paired-end sequencing facilitates detection of genomic rearrangements and repetitive sequence elements, as well as gene fusions and novel transcripts. |
| `"single-end"` | \[OBI:0002485]: A sequencing assay that incorporates single-end reads and sequencing technology to determine transcripts, gene structures, and gene expressions. Single-read sequencing involves sequencing DNA from only one end.                                                                                                                                                                                        |
