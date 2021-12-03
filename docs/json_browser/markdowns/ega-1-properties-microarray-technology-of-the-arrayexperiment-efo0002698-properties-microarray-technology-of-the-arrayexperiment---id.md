# Microarray technology of the ArrayExperiment - ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_id
```

The human readable ID (e.g. Two-colour microarray), chosen from a list of CVs, of the microarray technology used at the ArrayExperiment.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## technology_id Type

`string` ([Microarray technology of the ArrayExperiment - ID](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---id.md))

## technology_id Constraints

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

## technology_id Examples

```json
"One-colour microarray"
```
