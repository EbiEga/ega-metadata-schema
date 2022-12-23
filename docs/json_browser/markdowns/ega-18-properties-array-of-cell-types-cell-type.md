# Cell type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items
```

One of the cell types that can be found in your sample or from which the genetic content was derived.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## items Type

`object` ([Cell type](ega-18-properties-array-of-cell-types-cell-type.md))

# items Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cellType](#celltype)                 | Merged   | Required | cannot be null | [EGA sample metadata schema](ega-12-definitions-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellType")                                                               |
| [cellTypeInferred](#celltypeinferred) | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-inferred-cell-type-flag.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeInferred") |

## cellType

Property to describe a cell type: a distinct morphological or functional form of cell.

`cellType`

*   is required

*   Type: `object` ([Cell type](ega-12-definitions-cell-type.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellType")

### cellType Type

`object` ([Cell type](ega-12-definitions-cell-type.md))

all of

*   [Ontology term](ega-12-definitions-ontology-term.md "check type definition")

## cellTypeInferred

A flag to specify whether the cell type classification was inferred though single-cell analysis (e.g. cell clustering or trajectory analysis) or was determined otherwise (i.e. was visually observed or asserted to be in the sample).

`cellTypeInferred`

*   is required

*   Type: `string` ([Inferred cell type flag](ega-18-properties-array-of-cell-types-cell-type-properties-inferred-cell-type-flag.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-inferred-cell-type-flag.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeInferred")

### cellTypeInferred Type

`string` ([Inferred cell type flag](ega-18-properties-array-of-cell-types-cell-type-properties-inferred-cell-type-flag.md))

### cellTypeInferred Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation                                                                                             |
| :--------------- | :------------------------------------------------------------------------------------------------------ |
| `"inferred"`     | The cell type was inferred through single-cell analysis.                                                |
| `"not inferred"` | The cell type was not inferred through single-cell analysis (i.e. it was asserted to be in the sample). |
