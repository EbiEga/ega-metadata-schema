# Array type of the ArrayExperiment - ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule/properties/assayed_molecule_id
```

The human readable ID (e.g. DNA assay), chosen from a list of CVs, of the assayed molecule.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## assayed_molecule_id Type

`string` ([Array type of the ArrayExperiment - ID](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---id.md))

## assayed_molecule_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                     | Explanation |
| :------------------------ | :---------- |
| `"DNA assay"`             |             |
| `"RNA assay"`             |             |
| `"Metabolomic profiling"` |             |
| `"Protein assay"`         |             |

## assayed_molecule_id Examples

```json
"DNA assay"
```
