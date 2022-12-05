# File content item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items
```

Item describing the type of data a file contains or represents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([File content item](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

# items Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [typeOfDataCurie](#typeofdatacurie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/typeOfDataCurie") |
| [typeOfDataTerm](#typeofdataterm)   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/typeOfDataTerm")               |

## typeOfDataCurie



`typeOfDataCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the type of data.](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/typeOfDataCurie")

### typeOfDataCurie Type

`string` ([Compact URI (CURIE) of the type of data.](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data-allof-compact-uri-curie-pattern.md "check type definition")

### typeOfDataCurie Examples

```json
"format:1919"
```

```json
"format:3326"
```

## typeOfDataTerm

Term that specifies the type of data content.

`typeOfDataTerm`

*   is optional

*   Type: `string` ([Term of the type of data](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/typeOfDataTerm")

### typeOfDataTerm Type

`string` ([Term of the type of data](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md))

### typeOfDataTerm Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### typeOfDataTerm Examples

```json
"Sequence record format"
```

```json
"Data index format"
```
