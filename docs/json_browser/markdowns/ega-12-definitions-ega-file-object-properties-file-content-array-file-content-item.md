# File content item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content/items
```

Item describing the type of data a file contains or represents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([File content item](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

# items Properties

| Property                                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type\_of\_data\_curie](#type_of_data_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content/items/properties/type_of_data_curie") |
| [type\_of\_data\_term](#type_of_data_term)   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content/items/properties/type_of_data_term")               |

## type\_of\_data\_curie



`type_of_data_curie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the type of data.](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content/items/properties/type_of_data_curie")

### type\_of\_data\_curie Type

`string` ([Compact URI (CURIE) of the type of data.](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-compact-uri-curie-of-the-type-of-data-allof-compact-uri-curie-pattern.md "check type definition")

### type\_of\_data\_curie Examples

```json
"format:1919"
```

```json
"format:3326"
```

## type\_of\_data\_term

Term that specifies the type of data content.

`type_of_data_term`

*   is optional

*   Type: `string` ([Term of the type of data](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content/items/properties/type_of_data_term")

### type\_of\_data\_term Type

`string` ([Term of the type of data](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-term-of-the-type-of-data.md))

### type\_of\_data\_term Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### type\_of\_data\_term Examples

```json
"Sequence record format"
```

```json
"Data index format"
```
