# EGA protocol metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its protocol metadata object. A protocol is an information entity of a set of instructions that describe an how a procedure, analysis or experiment is done. Comprises metadata (e.g. Type of protocol) of a plan specification, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents (i.e. researchers). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json](../../../schemas/EGA.protocol.json "open original schema") |

## EGA protocol metadata schema Type

`object` ([EGA protocol metadata schema](ega-17.md))

# EGA protocol metadata schema Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                       |
| :------------------------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                                | Merged   | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_id")                       |
| [schema\_descriptor](#schema_descriptor)                | `object` | Optional | cannot be null | [EGA protocol metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/schema_descriptor")              |
| [object\_title](#object_title)                          | `string` | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-name-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_title")                 |
| [protocol\_type\_descriptor](#protocol_type_descriptor) | `object` | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_type_descriptor") |
| [protocol\_description](#protocol_description)          | `string` | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-description-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_description")  |
| [protocol\_performers](#protocol_performers)            | `array`  | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-performers-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_performers")     |
| [protocol\_instruments](#protocol_instruments)          | `array`  | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-instrument-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_instruments")    |
| [protocol\_software](#protocol_software)                | `array`  | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-software-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_software")         |
| [protocol\_relationships](#protocol_relationships)      | `array`  | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_relationships")     |
| [protocol\_attributes](#protocol_attributes)            | `array`  | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_attributes")    |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions.

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-17-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-17-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that protocol EGA ID (EGAO) is correct](ega-17-properties-objects-ids-block-allof-check-that-protocol-ega-id-egao-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`object_title`

*   is optional

*   Type: `string` ([Name of the protocol](ega-17-properties-name-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-name-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_title")

### object\_title Type

`string` ([Name of the protocol](ega-17-properties-name-of-the-protocol.md))

### object\_title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_title Examples

```json
"myProtocol-13"
```

```json
"Treatment for leukemia patients C30"
```

```json
"Sample collection from infected patients"
```

## protocol\_type\_descriptor

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type.

`protocol_type_descriptor`

*   is required

*   Type: `object` ([Protocol type descriptor](ega-17-properties-protocol-type-descriptor.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_type_descriptor")

### protocol\_type\_descriptor Type

`object` ([Protocol type descriptor](ega-17-properties-protocol-type-descriptor.md))

## protocol\_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated between institutions or performers.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol](ega-17-properties-description-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-description-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_description")

### protocol\_description Type

`string` ([Description of the protocol](ega-17-properties-description-of-the-protocol.md))

### protocol\_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```

```json
"Patients were given a ketogenic diet for 3 weeks at intervals consisting in..."
```

## protocol\_performers

Array of performers' descriptions of those individuals, groups, or institutions that executed the protocol.

`protocol_performers`

*   is optional

*   Type: `string[]` ([Performer of the protocol](ega-17-properties-protocol-performers-array-performer-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-performers-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_performers")

### protocol\_performers Type

`string[]` ([Performer of the protocol](ega-17-properties-protocol-performers-array-performer-of-the-protocol.md))

### protocol\_performers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_instruments

Array of instruments used in the protocol. It is not indispensable to provide each and every piece of instruments used, but a set of the ones you would highlight in your protocol for other researchers to know, since it will help them discover your data.

`protocol_instruments`

*   is optional

*   Type: `string[]` ([Instrument used in the protocol](ega-17-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-instrument-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_instruments")

### protocol\_instruments Type

`string[]` ([Instrument used in the protocol](ega-17-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

### protocol\_instruments Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_software

Array of software descriptions used in the protocol. It is not indispensable to provide each and every piece of software used, but a set of the ones you would highlight in your protocol for other researchers to know, since it will help them discover your data.

`protocol_software`

*   is optional

*   Type: `string[]` ([Software descriptions used in the protocol](ega-17-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-software-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_software")

### protocol\_software Type

`string[]` ([Software descriptions used in the protocol](ega-17-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

### protocol\_software Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a protocol being linked to an experiment) the EGA.

`protocol_relationships`

*   is required

*   Type: an array of merged types ([Details](ega-17-properties-protocol-relationships-items.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_relationships")

### protocol\_relationships Type

an array of merged types ([Details](ega-17-properties-protocol-relationships-items.md))

### protocol\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_attributes

Custom attributes of a protocol: reusable attributes to encode tag-value pairs (e.g. Tag being 'step index' and its Value '2') with optional units. Its properties are inherited from the common-definitions.json schema.

`protocol_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_attributes")

### protocol\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### protocol\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
