# Type of the object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type
```

Type of the object (e.g. 'sample') the JSON document describes.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## object_type Type

`string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

## object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"experiment"`      |             |
| `"study"`           |             |
| `"sample"`          |             |
| `"individual"`      |             |
| `"submission"`      |             |
| `"run"`             |             |
| `"dataset"`         |             |
| `"analysis"`        |             |
| `"policy"`          |             |
| `"DAC"`             |             |
| `"ArrayExperiment"` |             |
| `"ArrayAssay"`      |             |
| `"object-set"`      |             |
