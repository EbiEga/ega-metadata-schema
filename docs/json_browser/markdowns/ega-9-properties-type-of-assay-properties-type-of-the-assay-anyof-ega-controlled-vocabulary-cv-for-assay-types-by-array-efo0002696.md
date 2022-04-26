# EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json#/properties/assay_type_descriptor/properties/assay_type/anyOf/1
```

Controlled Vocabulary (CV) list for assay types by array \[EFO:0002696]: an assay that exploits an array as the instrument to find results. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 1 Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md))

## 1 Constraints

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
