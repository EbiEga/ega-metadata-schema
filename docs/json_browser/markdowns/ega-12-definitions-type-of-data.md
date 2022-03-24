# Type of data Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/types_of_output_data/items
```

Type of data an experiment or analysis can produce (i.e. output), or an analysis can use as input. For example, in a sequencing experiment the output data would be 'genomic data', while that same type of data could be the input type of data for an analysis, which would then output 'processed sequencing data'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## items Type

`string` ([Type of data](ega-12-definitions-type-of-data.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"gene list"`                 |             |
| `"genomic data"`              |             |
| `"metagenomic data"`          |             |
| `"metatranscriptomic data"`   |             |
| `"synthetic DNA data"`        |             |
| `"transcriptomic data"`       |             |
| `"viral RNA data"`            |             |
| `"processed sequencing data"` |             |
| `"processed array data"`      |             |
