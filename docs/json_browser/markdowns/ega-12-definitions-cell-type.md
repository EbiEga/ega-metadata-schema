# Cell type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellTypeDescriptor
```

Property to describe a cell type: a distinct morphological or functional form of cell.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## cellTypeDescriptor Type

`object` ([Cell type](ega-12-definitions-cell-type.md))

# cellTypeDescriptor Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                        |
| :------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cellTypeCurie](#celltypecurie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellTypeDescriptor/properties/cellTypeCurie") |
| [cellTypeLabel](#celltypelabel) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellTypeDescriptor/properties/cellTypeLabel")             |

## cellTypeCurie



`cellTypeCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellTypeDescriptor/properties/cellTypeCurie")

### cellTypeCurie Type

`string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## cellTypeLabel



`cellTypeLabel`

*   is optional

*   Type: `string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellTypeDescriptor/properties/cellTypeLabel")

### cellTypeLabel Type

`string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

### cellTypeLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cellTypeLabel Examples

```json
"musculo-skeletal system cell"
```

```json
"neoplastic cell"
```

```json
"nervous system cell"
```
