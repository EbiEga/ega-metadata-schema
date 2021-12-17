# Microarray technology of the ArrayExperiment \[EFO:0002698] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology
```

Microarray technology applicable for the ArrayExperiment. It contains both the ID  (e.g. One-colour microarray) and the CURIE  (e.g. EFO:0010939) of the technology.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## technology Type

`object` ([Microarray technology of the ArrayExperiment \[EFO:0002698\]](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md))

# technology Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                              |
| :------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [technology_id](#technology_id)       | `string` | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_id")       |
| [technology_curie](#technology_curie) | `string` | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_curie") |

## technology_id

The human readable ID (e.g. Two-colour microarray), chosen from a list of CVs, of the microarray technology used at the ArrayExperiment.

`technology_id`

*   is required

*   Type: `string` ([Microarray technology of the ArrayExperiment - ID](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_id")

### technology_id Type

`string` ([Microarray technology of the ArrayExperiment - ID](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---id.md))

### technology_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                    | Explanation |
| :--------------------------------------- | :---------- |
| `"One-colour microarray"`                |             |
| `"Two-colour microarray"`                |             |
| `"Methylation microarray"`               |             |
| `"Protein microarray"`                   |             |
| `"Metabolomic microarray"`               |             |
| `"Single Nucleotide Polymorphism Array"` |             |
| `"Tissue Microarray"`                    |             |

### technology_id Examples

```json
"One-colour microarray"
```

## technology_curie

The CURIE (i.e. ontologized term - e.g. NCIT:C116153), chosen from a list of CVs, of the microarray technology used at the ArrayExperiment.

`technology_curie`

*   is optional

*   Type: `string` ([Microarray technology of the ArrayExperiment - CURIE](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_curie")

### technology_curie Type

`string` ([Microarray technology of the ArrayExperiment - CURIE](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---curie.md))

### technology_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation |
| :------------------------- | :---------- |
| `"EFO:0010939"`            |             |
| `"NCIT:C116153"`           |             |
| `"NCIT:C165222"`           |             |
| `"EFO:0002702"`            |             |
| `"Metabolomic microarray"` |             |
| `"NCIT:C116151"`           |             |
| `"NCIT:C19922"`            |             |

### technology_curie Examples

```json
"EFO:0010939"
```
