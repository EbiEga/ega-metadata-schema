# Experiment type specifications Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications
```

Node containing additional attributes to describe the experiment, either array experiments (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing experiments (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). For example, if an array was used, its Array Design Format (ADF) will be expected.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## experimentTypeSpecifications Type

`object` ([Experiment type specifications](ega-1-properties-experiment-type-specifications.md))

one (and only one) of

*   [The sequencing experiment descriptors are required](ega-1-properties-experiment-type-specifications-oneof-the-sequencing-experiment-descriptors-are-required.md "check type definition")

*   [The array experiment descriptors are required](ega-1-properties-experiment-type-specifications-oneof-the-array-experiment-descriptors-are-required.md "check type definition")

# experimentTypeSpecifications Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayExperiment](#arrayexperiment)           | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment")          |
| [sequencingExperiment](#sequencingexperiment) | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment") |

## arrayExperiment

Node containing the set of fields specific to an experiment of array-type (i.e. an array was used to obtain the raw data).

`arrayExperiment`

*   is optional

*   Type: `object` ([Specifications of an array experiment](ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment")

### arrayExperiment Type

`object` ([Specifications of an array experiment](ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md))

## sequencingExperiment

Node containing the set of fields specific to an experiment of sequencing-type (i.e. a sequencer was used to obtain the raw data).

`sequencingExperiment`

*   is optional

*   Type: `object` ([Specifications of a sequencing experiment](ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment")

### sequencingExperiment Type

`object` ([Specifications of a sequencing experiment](ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))
