# Cell type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor
```

Property to describe a cell type: a distinct morphological or functional form of cell.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## cell-type-descriptor Type

`object` ([Cell type](ega-12-definitions-cell-type.md))

# cell-type-descriptor Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                            |
| :------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cell\_type\_curie](#cell_type_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_curie") |
| [cell\_type\_label](#cell_type_label) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_label")             |

## cell\_type\_curie



`cell_type_curie`

*   is optional

*   Type: `string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_curie")

### cell\_type\_curie Type

`string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## cell\_type\_label



`cell_type_label`

*   is optional

*   Type: `string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_label")

### cell\_type\_label Type

`string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

### cell\_type\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cell\_type\_label Examples

```json
"musculo-skeletal system cell"
```

```json
"neoplastic cell"
```

```json
"nervous system cell"
```
