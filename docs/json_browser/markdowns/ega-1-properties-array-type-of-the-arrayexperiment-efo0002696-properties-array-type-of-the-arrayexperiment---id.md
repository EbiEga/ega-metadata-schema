# Array type of the ArrayExperiment - ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type/properties/array_type_id
```

The human readable ID (e.g. Proteomic profiling by array), chosen from a list of CVs, of the array type used at the ArrayExperiment.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## array_type_id Type

`string` ([Array type of the ArrayExperiment - ID](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---id.md))

## array_type_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                | Explanation |
| :--------------------------------------------------- | :---------- |
| `"3C"`                                               |             |
| `"4C"`                                               |             |
| `"ChIP-chip by array"`                               |             |
| `"ChIP-chip by SNP array"`                           |             |
| `"ChIP-chip by tiling array"`                        |             |
| `"RNAi profiling by array"`                          |             |
| `"Comparative genomic hybridization by array"`       |             |
| `"Genotyping by array"`                              |             |
| `"Methylation profiling by array"`                   |             |
| `"microRNA profiling by RT-PCR"`                     |             |
| `"microRNA profiling by array"`                      |             |
| `"Proteomic profiling by array"`                     |             |
| `"RIP-chip (RNP immunoprecipitation-chip) by array"` |             |
| `"Tiling path by array"`                             |             |
| `"Transcription profiling by array"`                 |             |
| `"Transcription profiling by tiling array"`          |             |
| `"Translation profiling"`                            |             |

## array_type_id Examples

```json
"ChIP-chip by SNP array"
```
