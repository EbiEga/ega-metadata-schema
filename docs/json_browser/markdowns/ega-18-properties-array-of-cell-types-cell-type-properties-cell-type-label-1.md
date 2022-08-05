# Cell type label Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/inferred_cell_type
```

A flag to specify whether the cell type classification was determined though single-cell analysis (e.g. cell clustering or trajectory analysis) or not (i.e. was visually observed or it is expected).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## inferred\_cell\_type Type

`string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md))

## inferred\_cell\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation                                                  |
| :--------------- | :----------------------------------------------------------- |
| `"inferred"`     | The cell type was inferred through single-cell analysis.     |
| `"not inferred"` | The cell type was not inferred through single-cell analysis. |
