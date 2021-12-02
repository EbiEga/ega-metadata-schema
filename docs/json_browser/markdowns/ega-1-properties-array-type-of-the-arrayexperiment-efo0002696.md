# Array type of the ArrayExperiment \[EFO:0002696] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type
```

Type of array (not its purpose per se) providing a glimpse of the used technology. It contains both the human readable ID (e.g. Proteomic profiling by array) and CURIE (e.g. EFO:0002765) of the array type.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## array_type Type

`object` ([Array type of the ArrayExperiment \[EFO:0002696\]](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md))

# array_type Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                 |
| :------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_type_id](#array_type_id)       | `string` | Required | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type/properties/array_type_id")       |
| [array_type_curie](#array_type_curie) | `string` | Optional | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type/properties/array_type_curie") |

## array_type_id

The human readable ID (e.g. Proteomic profiling by array), chosen from a list of CVs, of the array type used at the ArrayExperiment.

`array_type_id`

*   is required

*   Type: `string` ([Array type of the ArrayExperiment - ID](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type/properties/array_type_id")

### array_type_id Type

`string` ([Array type of the ArrayExperiment - ID](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---id.md))

### array_type_id Constraints

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

### array_type_id Examples

```json
"ChIP-chip by SNP array"
```

## array_type_curie

The CURIE (i.e. ontologized term - e.g. EFO:0002765), chosen from a list of CVs, of the array type used at the ArrayExperiment.

`array_type_curie`

*   is optional

*   Type: `string` ([Array type of the ArrayExperiment - CURIE](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type/properties/array_type_curie")

### array_type_curie Type

`string` ([Array type of the ArrayExperiment - CURIE](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696-properties-array-type-of-the-arrayexperiment---curie.md))

### array_type_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"EFO:0007689"` |             |
| `"EFO:0007690"` |             |
| `"EFO:0002760"` |             |
| `"EFO:0002764"` |             |
| `"EFO:0002762"` |             |
| `"EFO:0001030"` |             |
| `"EFO:0000749"` |             |
| `"EFO:0002767"` |             |
| `"EFO:0002759"` |             |
| `"EFO:0007687"` |             |
| `"EFO:0000753"` |             |
| `"EFO:0002765"` |             |
| `"EFO:0005517"` |             |
| `"EFO:0001031"` |             |
| `"EFO:0002768"` |             |
| `"EFO:0002769"` |             |
| `"EFO:0001033"` |             |

### array_type_curie Examples

```json
"EFO:0007689"
```
