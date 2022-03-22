# Assay type and subtype terms are from the array CV list Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## 0 Type

unknown ([Assay type and subtype terms are from the array CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list.md))

# 0 Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [assay_type](#assay_type)       | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_type")                                                                                                 |
| [assay_subtype](#assay_subtype) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-array-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_subtype") |

## assay_type

Controlled Vocabulary (CV) list for assay types by array \[EFO:0002696]: an assay that exploits an array as the instrument to find results.

`assay_type`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_type")

### assay_type Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md))

### assay_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                          | Explanation |
| :--------------------------------------------- | :---------- |
| `"3C"`                                         |             |
| `"4C"`                                         |             |
| `"ChIP-chip by SNP array"`                     |             |
| `"ChIP-chip by array"`                         |             |
| `"ChIP-chip by tiling array"`                  |             |
| `"RNAi profiling by array"`                    |             |
| `"comparative genomic hybridization by array"` |             |
| `"genotyping by array"`                        |             |
| `"methylation profiling by array"`             |             |
| `"microRNA profiling by RT-PCR"`               |             |
| `"microRNA profiling by array"`                |             |
| `"proteomic profiling by array"`               |             |
| `"tiling path by array"`                       |             |
| `"transcription profiling by array"`           |             |
| `"transcription profiling by tiling array"`    |             |
| `"translation profiling"`                      |             |

## assay_subtype

Controlled Vocabulary (CV) list for assay subtypes by array: any ontologized term for a subtype (i.e. child ontology) of an array assay \[EFO:0002696].

`assay_subtype`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-array-efo0002696.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-array-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_subtype")

### assay_subtype Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-array-efo0002696.md))

### assay_subtype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"MC-4C"`  |             |
| `"UMI-4C"` |             |
