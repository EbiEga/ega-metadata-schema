# EGA Protocols object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object
```

Object containing the base metadata attributes of a Protocol object in the EGA. Comprises metadata (e.g. Type of protocol) of a plan specification, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## protocols_object Type

`object` ([EGA Protocols object](ega-4-definitions-ega-protocols-object.md))

# protocols_object Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                 |
| :-------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol_name](#protocol_name)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")               |
| [protocol_type](#protocol_type)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type")                  |
| [protocol_curie](#protocol_curie)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_curie")         |
| [protocol_description](#protocol_description) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description") |

## protocol_name

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`protocol_name`

*   is optional

*   Type: `string` ([Name of the protocol \[NCIT:C42614\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")

### protocol_name Type

`string` ([Name of the protocol \[NCIT:C42614\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md))

### protocol_name Examples

```json
"myProtocol-13"
```

## protocol_type

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary list (to be upgraded on demand).

`protocol_type`

*   is required

*   Type: `string` ([Type of protocol \[OBI:0000272\] ](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type")

### protocol_type Type

`string` ([Type of protocol \[OBI:0000272\] ](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md))

### protocol_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                     | Explanation |
| :---------------------------------------- | :---------- |
| `"Sample collection"`                     |             |
| `"Nucleic acid extraction"`               |             |
| `"Nucleic acid labeling"`                 |             |
| `"Nucleic acid hybridization to array"`   |             |
| `"Array scanning and feature extraction"` |             |
| `"Nucleic acid library construction"`     |             |
| `"Growth"`                                |             |
| `"Dissociation"`                          |             |
| `"Enrichment"`                            |             |
| `"Treatment"`                             |             |
| `"Conversion"`                            |             |
| `"Clinical treatment"`                    |             |
| `"Dissection"`                            |             |
| `"Gene expression"`                       |             |

### protocol_type Examples

```json
"Sample collection"
```

## protocol_curie

Ontology term (e.g. 'EFO:0005518') of the Type of protocol.

`protocol_curie`

*   is optional

*   Type: `string` ([Name of the protocol type \[NCIT:C21270\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_curie")

### protocol_curie Type

`string` ([Name of the protocol type \[NCIT:C21270\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md))

### protocol_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"EFO:0005518"` |             |
| `"EFO:0002944"` |             |
| `"EFO:0003813"` |             |
| `"EFO:0003815"` |             |
| `"EFO:0003814"` |             |
| `"EFO:0004184"` |             |
| `"EFO:0003789"` |             |
| `"EFO:0009088"` |             |
| `"EFO:0009089"` |             |
| `"EFO:0003969"` |             |
| `"EFO:0005520"` |             |
| `"EFO:0000355"` |             |
| `"EFO:0005519"` |             |
| `"EFO:0003788"` |             |

### protocol_curie Examples

```json
"EFO:0005518"
```

## protocol_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated by anyone who is granted access.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol \[NCIT:C25365\]](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")

### protocol_description Type

`string` ([Description of the protocol \[NCIT:C25365\]](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md))

### protocol_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```
