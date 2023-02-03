# Specifications of a sequencing experiment Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment
```

Node containing the set of fields specific to an experiment of sequencing-type (i.e. a sequencer was used to obtain the raw data).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## sequencingExperiment Type

`object` ([Specifications of a sequencing experiment](ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))

# sequencingExperiment Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                         |
| :-------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [libraryLayout](#librarylayout)   | `string` | Required | cannot be null | [EGA Experiment metadata schema](ega-4-definitions-sequencing-library-layout.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment/properties/libraryLayout") |
| [spotDescriptor](#spotdescriptor) | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-4-definitions-spot-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment/properties/spotDescriptor")          |

## libraryLayout

Whether the sequenced reads are paired or single. In other words, if the sequencing assay is paired- (OBI:0001850) or single-end (OBI:0002485). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`libraryLayout`

*   is required

*   Type: `string` ([Sequencing library layout](ega-4-definitions-sequencing-library-layout.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-4-definitions-sequencing-library-layout.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment/properties/libraryLayout")

### libraryLayout Type

`string` ([Sequencing library layout](ega-4-definitions-sequencing-library-layout.md))

### libraryLayout Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"paired-end"` | \[OBI:0001850]: A transcription profiling assay that determines transcripts, gene structures, and gene expressions using Paired-End Tags and sequencing technology. Allows to sequence both ends of a fragment and generate high-quality, alignable sequence data. Paired-end sequencing facilitates detection of genomic rearrangements and repetitive sequence elements, as well as gene fusions and novel transcripts. |
| `"single-end"` | \[OBI:0002485]: A sequencing assay that incorporates single-end reads and sequencing technology to determine transcripts, gene structures, and gene expressions. Single-read sequencing involves sequencing DNA from only one end.                                                                                                                                                                                        |

## spotDescriptor

The 'spotDescriptor' specifies how to decode the individual reads of interest from the monolithic spot sequence. The spot descriptor contains aspects of the experimental design, platform, and processing information. There will be two methods of specification: one will be an index into a table of typical decodings, the other being an exact specification. This construct is needed for loading data and for interpreting the loaded sequencing assays. It can be omitted if the loader can infer read layout (from multiple input files or from one input files).

`spotDescriptor`

*   is optional

*   Type: `object[]` ([Spot decode spec](ega-4-definitions-spot-descriptor-spot-decode-spec.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-4-definitions-spot-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment/properties/spotDescriptor")

### spotDescriptor Type

`object[]` ([Spot decode spec](ega-4-definitions-spot-descriptor-spot-decode-spec.md))

### spotDescriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
