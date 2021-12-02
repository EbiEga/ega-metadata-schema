# Microarray technology of the ArrayExperiment - CURIE Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology/properties/technology_curie
```

The CURIE (i.e. ontologized term - e.g. NCIT:C116153), chosen from a list of CVs, of the microarray technology used at the ArrayExperiment.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## technology_curie Type

`string` ([Microarray technology of the ArrayExperiment - CURIE](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698-properties-microarray-technology-of-the-arrayexperiment---curie.md))

## technology_curie Constraints

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

## technology_curie Examples

```json
"EFO:0010939"
```
