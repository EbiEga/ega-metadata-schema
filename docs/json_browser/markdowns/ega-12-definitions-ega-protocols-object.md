# EGA Protocols object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_protocols/items
```

A protocol is an information entity which is a set of instructions that describe an how a procedure, analysis or experiment is done. Comprises metadata (e.g. Type of protocol) of a plan specification, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

# items Properties

| Property                                                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :--------------------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol\_name](#protocol_name)                                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")                        |
| [protocol\_step\_index](#protocol_step_index)                    | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")                   |
| [previous\_protocol\_step\_index](#previous_protocol_step_index) | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index") |
| [protocol\_type\_descriptor](#protocol_type_descriptor)          | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")         |
| [protocol\_performers](#protocol_performers)                     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")             |
| [protocol\_instrument](#protocol_instrument)                     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")             |
| [protocol\_software](#protocol_software)                         | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")                 |
| [protocol\_description](#protocol_description)                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")          |

## protocol\_name

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`protocol_name`

*   is optional

*   Type: `string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")

### protocol\_name Type

`string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

### protocol\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### protocol\_name Examples

```json
"myProtocol-13"
```

```json
"Treatment for leukemia patients C30"
```

```json
"Sample collection from infected patients"
```

## protocol\_step\_index

Lexically ordered value (greater than 0) that allows for the protocol section to be sequentially ordered. The float primitive data type is used to allow for pipe sections to be inserted later on. In other words, adding a new intermediate step 1.1 between steps 1 and 2 afterwards. For example, in an experiment where we treated samples before its DNA extraction, the sample treatment protocol would have a lower 'protocol\_step\_index' than the DNA extraction.

`protocol_step_index`

*   is required

*   Type: `number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")

### protocol\_step\_index Type

`number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

### protocol\_step\_index Examples

```json
0.5
```

```json
1
```

```json
2.5
```

```json
2
```

```json
30
```

## previous\_protocol\_step\_index

The 'protocol\_step\_index' of the previous protocol, if hierarchically ordered. Set to '0' if this protocol is the first step. In case several protocols are not sequential, both can share the same 'previous\_protocol\_step\_index'.

`previous_protocol_step_index`

*   is required

*   Type: `number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index")

### previous\_protocol\_step\_index Type

`number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

### previous\_protocol\_step\_index Examples

```json
0
```

```json
0.5
```

```json
1
```

```json
2.5
```

```json
2
```

```json
30
```

## protocol\_type\_descriptor

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type, and hence we highly recommend their usage.

`protocol_type_descriptor`

*   is required

*   Type: `object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")

### protocol\_type\_descriptor Type

`object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

## protocol\_performers

Array of performers' descriptions of those individuals, groups, or institutions that executed the protocol.

`protocol_performers`

*   is optional

*   Type: `string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")

### protocol\_performers Type

`string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

### protocol\_performers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_instrument

Array of instruments used in the protocol.

`protocol_instrument`

*   is optional

*   Type: `string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")

### protocol\_instrument Type

`string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

### protocol\_instrument Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_software

Array of software descriptions used in the protocol.

`protocol_software`

*   is optional

*   Type: `string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")

### protocol\_software Type

`string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

### protocol\_software Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol\_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated between institutions or performers.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")

### protocol\_description Type

`string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

### protocol\_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```

```json
"Patients were given a ketogenic diet for 3 weeks at intervals consisting in..."
```
