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

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cellTypeId](#celltypeid)             | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeId") |
| [cellTypeLabel](#celltypelabel)       | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeLabel")                 |
| [inferredCellType](#inferredcelltype) | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/inferredCellType")            |

## cellTypeId



`cellTypeId`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the cell type](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeId")

### cellTypeId Type

`string` ([Compact URI (CURIE) of the cell type](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

### cellTypeId Examples

```json
"CL:0002092"
```

```json
"CL:0000127"
```

```json
"CL:0000128"
```

## cellTypeLabel



`cellTypeLabel`

*   is optional

*   Type: `string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellTypeLabel")

### cellTypeLabel Type

`string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md))

### cellTypeLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cellTypeLabel Examples

```json
"bone marrow cell"
```

```json
"astrocyte"
```

```json
"oligodendrocyte"
```

## inferredCellType

A flag to specify whether the cell type classification was determined though single-cell analysis (e.g. cell clustering or trajectory analysis) or not (i.e. was visually observed or it is expected).

`inferredCellType`

*   is required

*   Type: `string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/inferredCellType")

### inferredCellType Type

`string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md))

### inferredCellType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation                                                  |
| :--------------- | :----------------------------------------------------------- |
| `"inferred"`     | The cell type was inferred through single-cell analysis.     |
| `"not inferred"` | The cell type was not inferred through single-cell analysis. |
