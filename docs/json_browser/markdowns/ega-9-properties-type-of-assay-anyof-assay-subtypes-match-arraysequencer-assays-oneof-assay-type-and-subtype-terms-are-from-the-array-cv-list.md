# Assay type and subtype terms are from the array CV list Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 0 Type

unknown ([Assay type and subtype terms are from the array CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list.md))

# 0 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                         |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay\_type](#assay_type)       | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-5.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_type")       |
| [assay\_subtype](#assay_subtype) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-3.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_subtype") |

## assay\_type

Controlled Vocabulary (CV) list for assay types by array \[EFO:0002696]: an assay that exploits an array as the instrument to find results. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_type`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-5.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-5.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_type")

### assay\_type Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-5.md))

### assay\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                          | Explanation |
| :--------------------------------------------- | :---------- |
| `"3C"`                                         | EFO:0007689 |
| `"4C"`                                         | EFO:0007690 |
| `"ChIP-chip by SNP array"`                     | EFO:0002764 |
| `"ChIP-chip by array"`                         | EFO:0002760 |
| `"ChIP-chip by tiling array"`                  | EFO:0002762 |
| `"RNAi profiling by array"`                    | EFO:0001030 |
| `"comparative genomic hybridization by array"` | EFO:0000749 |
| `"genotyping by array"`                        | EFO:0002767 |
| `"methylation profiling by array"`             | EFO:0002759 |
| `"microRNA profiling by RT-PCR"`               | EFO:0007687 |
| `"microRNA profiling by array"`                | EFO:0000753 |
| `"proteomic profiling by array"`               | EFO:0002765 |
| `"tiling path by array"`                       | EFO:0001031 |
| `"transcription profiling by array"`           | EFO:0002768 |
| `"transcription profiling by tiling array"`    | EFO:0002769 |
| `"translation profiling"`                      | EFO:0001033 |

## assay\_subtype

Controlled Vocabulary (CV) list for assay subtypes by array: any ontologized term for a subtype (i.e. child ontology) of an array assay \[EFO:0002696]. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_subtype`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696\]](ega-3.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-3.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_subtype")

### assay\_subtype Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696\]](ega-3.md))

### assay\_subtype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation    |
| :--------- | :------------- |
| `"MC-4C"`  | \[EFO:0009983] |
| `"UMI-4C"` | \[EFO:0009995] |
