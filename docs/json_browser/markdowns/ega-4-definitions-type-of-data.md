# Type of data Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/typesOfOutputData/items
```

Type of data an experiment or analysis can produce (i.e. output), or an analysis can use as input. For example, in a sequencing experiment the output data would be 'genomic data', while that same type of data could be the input type of data for an analysis, which would then output 'processed sequencing data'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`string` ([Type of data](ega-4-definitions-type-of-data.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation                                                                                                                                                                                             |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"gene list"`                 | \[OBI:0000118]                                                                                                                                                                                          |
| `"genomic data"`              | \[EFO:0004600]                                                                                                                                                                                          |
| `"metagenomic data"`          | \[EFO:0004602]                                                                                                                                                                                          |
| `"metatranscriptomic data"`   | \[EFO:0004603]                                                                                                                                                                                          |
| `"synthetic DNA data"`        | \[EFO:0004604]                                                                                                                                                                                          |
| `"transcriptomic data"`       | \[EFO:0004601]                                                                                                                                                                                          |
| `"viral RNA data"`            | \[EFO:0004605]                                                                                                                                                                                          |
| `"processed sequencing data"` | \[EFO:0004663]: raw sequencing data (e.g. FastQ files) were processed in any way (e.g. normalization, noise reduction, alignment...) and transformed into processed genotype data files \[EFO:0004663]. |
| `"processed array data"`      | \[EFO:0004096]: raw array data (e.g. CEL files) were processed in any way (e.g. normalization, noise reduction...) and transformed into processed array data files \[EFO:0004096].                      |
