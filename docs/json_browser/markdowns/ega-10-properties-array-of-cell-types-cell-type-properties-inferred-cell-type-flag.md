# Inferred cell type flag Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeInferred
```

A flag to specify whether the cell type classification was inferred though single-cell analysis (e.g. cell clustering or trajectory analysis) or was determined otherwise (i.e. was visually observed or asserted to be in the sample).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## cellTypeInferred Type

`string` ([Inferred cell type flag](ega-10-properties-array-of-cell-types-cell-type-properties-inferred-cell-type-flag.md))

## cellTypeInferred Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation                                                                                             |
| :--------------- | :------------------------------------------------------------------------------------------------------ |
| `"inferred"`     | The cell type was inferred through single-cell analysis.                                                |
| `"not inferred"` | The cell type was not inferred through single-cell analysis (i.e. it was asserted to be in the sample). |
