# Study type Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_types/items
```

One of the types of the study, expressing the overall purpose of the study. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition. The CV was inherited from ENA's study types.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json*](../out/EGA.study.json "open original schema") |

## items Type

`string` ([Study type](ega-18-properties-study-types-array-study-type.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                       | Explanation |
| :-------------------------- | :---------- |
| `"whole genome sequencing"` |             |
| `"metagenomics"`            |             |
| `"transcriptome analysis"`  |             |
| `"resequencing"`            |             |
| `"epigenetics"`             |             |
| `"synthetic genomics"`      |             |
| `"forensic"`                |             |
| `"paleo-genomics"`          |             |
| `"gene regulation"`         |             |
| `"cancer genomics"`         |             |
| `"population genomics"`     |             |
| `"RNASeq"`                  |             |
| `"exome sequencing"`        |             |
| `"pooled clone sequencing"` |             |
| `"COVID-19"`                |             |
