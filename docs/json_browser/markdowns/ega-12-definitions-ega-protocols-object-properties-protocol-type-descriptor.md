# Protocol type descriptor Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor
```

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type, and hence we highly recommend their usage.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## protocol_type_descriptor Type

`object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

# protocol_type_descriptor Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol_type](#protocol_type)                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_type")                                   |
| [protocol_subtype](#protocol_subtype)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_subtype")                         |
| [protocol_subtype_curie](#protocol_subtype_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_subtype_curie") |

## protocol_type

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`protocol_type`

*   is required

*   Type: `string` ([Type of protocol](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-type-of-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_type")

### protocol_type Type

`string` ([Type of protocol](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-type-of-protocol.md))

### protocol_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                 | Explanation |
| :------------------------------------ | :---------- |
| `"high Content Screen (HCS)"`         |             |
| `"conversion"`                        |             |
| `"delivery method"`                   |             |
| `"dissection"`                        |             |
| `"dissociation"`                      |             |
| `"enrichment"`                        |             |
| `"extraction"`                        |             |
| `"gene expression"`                   |             |
| `"growth"`                            |             |
| `"hybridization"`                     |             |
| `"hydrolysis collection"`             |             |
| `"labelling"`                         |             |
| `"nucleic acid library construction"` |             |
| `"nucleic acid sequencing"`           |             |
| `"sample collection"`                 |             |
| `"single cell isolation"`             |             |
| `"treatment"`                         |             |
| `"data transformation"`               |             |

## protocol_subtype

Name of the protocol's subtype. We highly recommend the usage of names given to ontologized protocols, specially those at the [Experimental Factor Ontology (EFO)](https://www.ebi.ac.uk/ols/ontologies/efo). For example, if the protocol corresponds to a data transformation of a genome, you may find your subtype at [genome analysis](http://edamontology.org/operation\_3918); while treating a patient with a drug would correspond to a [clinical treatment](http://www.ebi.ac.uk/efo/EFO\_0007056).

`protocol_subtype`

*   is optional

*   Type: `string` ([Subtype of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_subtype")

### protocol_subtype Type

`string` ([Subtype of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

### protocol_subtype Examples

```json
"clinical treatment"
```

```json
"array scanning and feature extraction"
```

```json
"Genome alignment"
```

```json
"Genome annotation"
```

```json
"Genome assembly"
```

```json
"Genome comparison"
```

```json
"Genome feature comparison"
```

```json
"Genome indexing"
```

```json
"Genome visualisation"
```

```json
"Whole genome methylation analysis"
```

## protocol_subtype_curie

Ontology term in CURIE format (e.g. 'EFO:0005518') of the protocol subtype. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index). This allows for a specific designation of the protocol within the overall general of the 'protocol_type' field. For instance, the CURIE for Treatment's subtype 'clinical treatment' would be 'EFO:0003814'. If the protocol does not require a subtype, use the CURIE for the protocol type per se (e.g. 'EFO:0005518' for 'Sample collection').

`protocol_subtype_curie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the protocol subtype](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_subtype_curie")

### protocol_subtype_curie Type

`string` ([Compact URI (CURIE) of the protocol subtype](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### protocol_subtype_curie Examples

```json
"EFO:0005518"
```

```json
"EFO:0002944"
```

```json
"EFO:0003813"
```

```json
"EFO:0003815"
```

```json
"EFO:0003814"
```

```json
"EFO:0004184"
```

```json
"EFO:0003789"
```

```json
"EFO:0009088"
```

```json
"EFO:0009089"
```

```json
"EFO:0003969"
```

```json
"EFO:0005520"
```

```json
"EFO:0000355"
```

```json
"EFO:0005519"
```

```json
"EFO:0003788"
```

```json
"EFO:0000395"
```

```json
"EFO:0010892"
```

```json
"EFO:0010214"
```
