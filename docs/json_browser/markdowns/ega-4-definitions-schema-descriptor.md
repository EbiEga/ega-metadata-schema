# Schema descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/schemaDescriptor
```

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

# schemaDescriptor Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectType](#objecttype)                     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectType")                                |
| [describedBySchemaUri](#describedbyschemauri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/describedBySchemaUri")                       |
| [objectSchemaVersion](#objectschemaversion)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectSchemaVersion")            |
| [commonSchemaVersion](#commonschemaversion)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/commonSchemaVersion") |

## objectType

Type of the object (e.g. 'sample') the JSON document describes.

`objectType`

*   is required

*   Type: `string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectType")

### objectType Type

`string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

### objectType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"experiment"` |             |
| `"study"`      |             |
| `"sample"`     |             |
| `"individual"` |             |
| `"submission"` |             |
| `"assay"`      |             |
| `"dataset"`    |             |
| `"analysis"`   |             |
| `"policy"`     |             |
| `"DAC"`        |             |
| `"protocol"`   |             |
| `"object-set"` |             |

## describedBySchemaUri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my\_sample.json')

`describedBySchemaUri`

*   is required

*   Type: `string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/describedBySchemaUri")

### describedBySchemaUri Type

`string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

### describedBySchemaUri Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https://github\.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA\..+\.json$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fgithub%5C.com%2FEbiEga%2Fega-metadata-schema%2Ftree%2Fmain%2Fschemas%2FEGA%5C..%2B%5C.json%24 "try regular expression with regexr.com")

### describedBySchemaUri Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json"
```

## objectSchemaVersion

The version of the object's schema, the one specific for the object the JSON document corresponds to (e.g. 'EGA.sample.json'), not the common definitions schema's version (i.e. 'EGA.common-definitions.json').

`objectSchemaVersion`

*   is required

*   Type: `string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectSchemaVersion")

### objectSchemaVersion Type

`string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-semantic-versioning-pattern.md "check type definition")

## commonSchemaVersion

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`commonSchemaVersion`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/commonSchemaVersion")

### commonSchemaVersion Type

`string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-semantic-versioning-pattern.md "check type definition")
