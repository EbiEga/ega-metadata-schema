# Specifications of an array experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment
```

Node containing the set of fields specific to an experiment of array-type (i.e. an array was used to obtain the raw data).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## array_experiment Type

`object` ([Specifications of an array experiment](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md))

# array_experiment Properties

| Property                      | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------- | :------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_labels](#array_labels) | `array` | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-label-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/array_labels")               |
| [adf_files](#adf_files)       | `array` | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-design-format-adf-ncitc172213-file-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/adf_files") |

## array_labels

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. Can be repeated so that dual labelled arrays can be taken into account.

`array_labels`

*   is required

*   Type: `object[]` ([Repeatable array_label node](ega-12-definitions-repeatable-array_label-node.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-label-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/array_labels")

### array_labels Type

`object[]` ([Repeatable array_label node](ega-12-definitions-repeatable-array_label-node.md))

### array_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## adf_files

The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip. They can be standard (sold by a company) or custom. Its format is of a spreadsheet-like tab-delimited text file with metadata header rows, followed by a multi-column table of probe information. For example, see ADF for [arrayexpress:E-MTAB-3050](https://www.ebi.ac.uk/arrayexpress/files/A-GEOD-28079/A-GEOD-28079.adf.txt) or [arrayexpress:E-MEXP-1712](https://www.ebi.ac.uk/arrayexpress/files/A-AFFY-125/A-AFFY-125.adf.txt). This node is an array of file nodes in case the ADF is given in several formats (e.g. tsv, xlsx, csv...).

`adf_files`

*   is required

*   Type: `object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-design-format-adf-ncitc172213-file-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/adf_files")

### adf_files Type

`object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

### adf_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
