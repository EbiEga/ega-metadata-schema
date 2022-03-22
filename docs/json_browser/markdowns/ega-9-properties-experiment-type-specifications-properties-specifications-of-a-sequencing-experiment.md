# Specifications of a sequencing experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment
```

Node containing the set of fields specific to an experiment of sequencing-type (i.e. a sequencer was used to obtain the raw data).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## sequencing_experiment Type

`object` ([Specifications of a sequencing experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))

# sequencing_experiment Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :---------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [library_layout](#library_layout)   | `string` | Required | cannot be null | [EGA Experiment metadata schema](ega-12-definitions-sequencing-library-layout.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/library_layout") |
| [spot_descriptor](#spot_descriptor) | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-12-definitions-spot-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/spot_descriptor")          |

## library_layout

Whether the sequenced reads are paired or single. In other words, if the sequencing assay is paired- (OBI:0001850) or single-end (OBI:0002485). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`library_layout`

*   is required

*   Type: `string` ([Sequencing library layout](ega-12-definitions-sequencing-library-layout.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-12-definitions-sequencing-library-layout.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/library_layout")

### library_layout Type

`string` ([Sequencing library layout](ega-12-definitions-sequencing-library-layout.md))

### library_layout Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"paired-end"` |             |
| `"single-end"` |             |

## spot_descriptor

The 'spot_descriptor' specifies how to decode the individual reads of interest from the monolithic spot sequence. The spot descriptor contains aspects of the experimental design, platform, and processing information. There will be two methods of specification: one will be an index into a table of typical decodings, the other being an exact specification. This construct is needed for loading data and for interpreting the loaded sequencing assays. It can be omitted if the loader can infer read layout (from multiple input files or from one input files).

`spot_descriptor`

*   is optional

*   Type: `object[]` ([Spot decode spec](ega-12-definitions-spot-descriptor-spot-decode-spec.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-12-definitions-spot-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/spot_descriptor")

### spot_descriptor Type

`object[]` ([Spot decode spec](ega-12-definitions-spot-descriptor-spot-decode-spec.md))

### spot_descriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
