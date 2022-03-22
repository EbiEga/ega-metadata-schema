# EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json#/properties/assay_type_descriptor/anyOf/1/oneOf/0/properties/assay_subtype
```

Controlled Vocabulary (CV) list for assay subtypes by array: any ontologized term for a subtype (i.e. child ontology) of an array assay \[EFO:0002696].

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## assay_subtype Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by array \[EFO:0002696\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-array-efo0002696.md))

## assay_subtype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"MC-4C"`  |             |
| `"UMI-4C"` |             |
