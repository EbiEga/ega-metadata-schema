# Dataset type Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_type
```

Type of the dataset, expressing the overall purpose of the dataset. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition. The CV was inherited from ENA's dataset types.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json*](../out/EGA.dataset.json "open original schema") |

## dataset_type Type

`string` ([Dataset type](ega-13-properties-dataset-type.md))

## dataset_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                               | Explanation |
| :------------------------------------------------------------------ | :---------- |
| `"whole genome sequencing"`                                         |             |
| `"exome sequencing"`                                                |             |
| `"genotyping by array"`                                             |             |
| `"transcriptome profiling by high-throughput sequencing"`           |             |
| `"transcriptome profiling by array"`                                |             |
| `"amplicon sequencing"`                                             |             |
| `"methylation binding domain sequencing"`                           |             |
| `"methylation profiling by high-throughput sequencing"`             |             |
| `"phenotype information"`                                           |             |
| `"genomic variant calling"`                                         |             |
| `"chromatin accessibility profiling by high-throughput sequencing"` |             |
| `"histone modification profiling by high-throughput sequencing"`    |             |
| `"chip-Seq"`                                                        |             |
| `"study summary information"`                                       |             |

## dataset_type Examples

```json
"whole genome sequencing"
```
