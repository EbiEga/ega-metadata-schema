# EGA Protocols object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_protocols/items
```

A protocol is an information entity which is a set of instructions that describe an how a procedure, analysis or experiment is done. Comprises metadata (e.g. Type of protocol) of a plan specification, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## items Type

`object` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

# items Properties

| Property                                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol_name](#protocol_name)                               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")                        |
| [protocol_step_index](#protocol_step_index)                   | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")                   |
| [previous_protocol_step_index](#previous_protocol_step_index) | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index") |
| [protocol_type_descriptor](#protocol_type_descriptor)         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")         |
| [protocol_performers](#protocol_performers)                   | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")             |
| [protocol_instrument](#protocol_instrument)                   | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")             |
| [protocol_software](#protocol_software)                       | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")                 |
| [protocol_description](#protocol_description)                 | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")          |

## protocol_name

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`protocol_name`

*   is optional

*   Type: `string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")

### protocol_name Type

`string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

### protocol_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### protocol_name Examples

```json
"myProtocol-13"
```

```json
"Treatment for leukemia patients C30"
```

```json
"Sample collection from infected patients"
```

## protocol_step_index

Lexically ordered value (greater than 0) that allows for the protocol section to be sequentially ordered. The float primitive data type is used to allow for pipe sections to be inserted later on. In other words, adding a new intermediate step 1.1 between steps 1 and 2 afterwards. For example, in an experiment where we treated samples before its DNA extraction, the sample treatment protocol would have a lower 'protocol_step_index' than the DNA extraction.

`protocol_step_index`

*   is required

*   Type: `number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")

### protocol_step_index Type

`number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

### protocol_step_index Examples

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

## previous_protocol_step_index

The 'protocol_step_index' of the previous protocol, if hierarchically ordered. Set to '0' if this protocol is the first step. In case several protocols are not sequential, both can share the same 'previous_protocol_step_index'.

`previous_protocol_step_index`

*   is required

*   Type: `number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index")

### previous_protocol_step_index Type

`number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

### previous_protocol_step_index Examples

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

## protocol_type_descriptor

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type, and hence we highly recommend their usage.

`protocol_type_descriptor`

*   is required

*   Type: `object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")

### protocol_type_descriptor Type

`object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

## protocol_performers

Array of performers' descriptions of those individuals, groups, or institutions that executed the protocol.

`protocol_performers`

*   is optional

*   Type: `string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")

### protocol_performers Type

`string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

### protocol_performers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol_instrument

Array of instruments used in the protocol.

`protocol_instrument`

*   is optional

*   Type: `string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")

### protocol_instrument Type

`string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

### protocol_instrument Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol_software

Array of software descriptions used in the protocol.

`protocol_software`

*   is optional

*   Type: `string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")

### protocol_software Type

`string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

### protocol_software Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## protocol_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated between institutions or performers.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")

### protocol_description Type

`string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

### protocol_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```

```json
"Patients were given a ketogenic diet for 3 weeks at intervals consisting in..."
```
