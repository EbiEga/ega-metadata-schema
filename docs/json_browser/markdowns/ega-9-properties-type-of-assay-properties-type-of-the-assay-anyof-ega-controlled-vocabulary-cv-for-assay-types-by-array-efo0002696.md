# EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/properties/assay_type/anyOf/1
```

Controlled Vocabulary (CV) list for assay types by array \[EFO:0002696]: an assay that exploits an array as the instrument to find results.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## 1 Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md))

## 1 Constraints

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
