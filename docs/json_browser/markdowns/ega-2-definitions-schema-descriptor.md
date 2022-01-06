# Schema descriptor Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/schema_descriptor
```

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## schema_descriptor Type

`object` ([Schema descriptor](ega-2-definitions-schema-descriptor.md))

# schema_descriptor Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_type](#object_type)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")                                 |
| [described_by_schema_uri](#described_by_schema_uri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")                      |
| [object_schema_version](#object_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")            |
| [common_schema_version](#common_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version") |

## object_type

Type of the object (e.g. 'sample') the JSON document describes.

`object_type`

*   is required

*   Type: `string` ([Type of the object](ega-2-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")

### object_type Type

`string` ([Type of the object](ega-2-definitions-schema-descriptor-properties-type-of-the-object.md))

### object_type Constraints

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

## described_by_schema_uri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my_sample.json')

`described_by_schema_uri`

*   is required

*   Type: `string` ([URI of the schema](ega-2-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")

### described_by_schema_uri Type

`string` ([URI of the schema](ega-2-definitions-schema-descriptor-properties-uri-of-the-schema.md))

### described_by_schema_uri Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^https://github\.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA\..+\.json$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fgithub%5C.com%2FEbiEga%2Fega-metadata-schema%2Ftree%2Fmain%2Fschemas%2FEGA%5C..%2B%5C.json%24 "try regular expression with regexr.com")

### described_by_schema_uri Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json"
```

## object_schema_version

The version of the object's schema, the one specific for the object the JSON document corresponds to (e.g. 'EGA.sample.json'), not the common definitions schema's version (i.e. 'EGA.common-definitions.json').

`object_schema_version`

*   is required

*   Type: `string` ([Version of the object's schema](ega-2-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")

### object_schema_version Type

`string` ([Version of the object's schema](ega-2-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-2-definitions-semantic-versioning-pattern.md "check type definition")

## common_schema_version

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`common_schema_version`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-2-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version")

### common_schema_version Type

`string` ([Version of the common definition's schema](ega-2-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-2-definitions-semantic-versioning-pattern.md "check type definition")
