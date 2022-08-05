# Cell type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items
```

One of the cell types that can be found in your sample or from which the genetic content was derived.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## items Type

`object` ([Cell type](ega-18-properties-array-of-cell-types-cell-type.md))

# items Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                      |
| :------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cell\_type\_id](#cell_type_id)             | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/cell_type_id") |
| [cell\_type\_label](#cell_type_label)       | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/cell_type_label")                 |
| [inferred\_cell\_type](#inferred_cell_type) | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/inferred_cell_type")            |

## cell\_type\_id



`cell_type_id`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the cell type](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/cell_type_id")

### cell\_type\_id Type

`string` ([Compact URI (CURIE) of the cell type](ega-18-properties-array-of-cell-types-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

### cell\_type\_id Examples

```json
"CL:0002092"
```

```json
"CL:0000127"
```

```json
"CL:0000128"
```

## cell\_type\_label



`cell_type_label`

*   is optional

*   Type: `string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/cell_type_label")

### cell\_type\_label Type

`string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label.md))

### cell\_type\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cell\_type\_label Examples

```json
"bone marrow cell"
```

```json
"astrocyte"
```

```json
"oligodendrocyte"
```

## inferred\_cell\_type

A flag to specify whether the cell type classification was determined though single-cell analysis (e.g. cell clustering or trajectory analysis) or not (i.e. was visually observed or it is expected).

`inferred_cell_type`

*   is required

*   Type: `string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cell_types/items/properties/inferred_cell_type")

### inferred\_cell\_type Type

`string` ([Cell type label](ega-18-properties-array-of-cell-types-cell-type-properties-cell-type-label-1.md))

### inferred\_cell\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation                                                  |
| :--------------- | :----------------------------------------------------------- |
| `"inferred"`     | The cell type was inferred through single-cell analysis.     |
| `"not inferred"` | The cell type was not inferred through single-cell analysis. |
