# Experiment type specifications Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications
```

Node containing additional attributes to describe the experiment, either array experiments (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO\_0002698) was used) or sequencing experiments (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO\_0003739) was used). For example, if an array was used, its Array Design Format (ADF) will be expected.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## experiment_type_specifications Type

`object` ([Experiment type specifications](ega-9-properties-experiment-type-specifications.md))

one (and only one) of

*   [The sequencing experiment descriptors are required](ega-9-properties-experiment-type-specifications-oneof-the-sequencing-experiment-descriptors-are-required.md "check type definition")

*   [The array experiment descriptors are required](ega-9-properties-experiment-type-specifications-oneof-the-array-experiment-descriptors-are-required.md "check type definition")

# experiment_type_specifications Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                  |
| :---------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_experiment](#array_experiment)           | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment")          |
| [sequencing_experiment](#sequencing_experiment) | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment") |

## array_experiment

Node containing the set of fields specific to an experiment of array-type (i.e. an array was used to obtain the raw data).

`array_experiment`

*   is optional

*   Type: `object` ([Specifications of an array experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment")

### array_experiment Type

`object` ([Specifications of an array experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md))

## sequencing_experiment

Node containing the set of fields specific to an experiment of sequencing-type (i.e. a sequencer was used to obtain the raw data).

`sequencing_experiment`

*   is optional

*   Type: `object` ([Specifications of a sequencing experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment")

### sequencing_experiment Type

`object` ([Specifications of a sequencing experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md))
