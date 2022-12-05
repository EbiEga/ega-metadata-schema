# Protocol type descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor
```

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocolTypeDescriptor Type

`object` ([Protocol type descriptor](ega-17-properties-protocol-type-descriptor.md))

# protocolTypeDescriptor Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolType](#protocoltype)                 | `string` | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolType")                                  |
| [protocolSubtype](#protocolsubtype)           | `string` | Optional | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype")                        |
| [protocolSubtypeCurie](#protocolsubtypecurie) | Merged   | Required | cannot be null | [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtypeCurie") |

## protocolType

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`protocolType`

*   is required

*   Type: `string` ([Type of protocol](ega-17-properties-protocol-type-descriptor-properties-type-of-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolType")

### protocolType Type

`string` ([Type of protocol](ega-17-properties-protocol-type-descriptor-properties-type-of-protocol.md))

### protocolType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                 | Explanation    |
| :------------------------------------ | :------------- |
| `"high Content Screen (HCS)"`         | \[EFO:0007570] |
| `"conversion"`                        | \[EFO:0005520] |
| `"delivery method"`                   | \[EFO:0000395] |
| `"dissection"`                        |                |
| `"dissociation"`                      |                |
| `"enrichment"`                        | \[EFO:0009089] |
| `"extraction"`                        | \[EFO:0002944] |
| `"gene expression"`                   | \[EFO:0003788] |
| `"growth"`                            | \[EFO:0003789] |
| `"hybridization"`                     | \[EFO:0003815] |
| `"hydrolysis collection"`             | \[EFO:0010892] |
| `"labelling"`                         | \[EFO:0003813] |
| `"nucleic acid library construction"` | \[EFO:0004184] |
| `"nucleic acid sequencing"`           | \[EFO:0004170] |
| `"sample collection"`                 | \[EFO:0005518] |
| `"single cell isolation"`             | \[EFO:0010214] |
| `"treatment"`                         | \[EFO:0003969] |
| `"data transformation"`               | \[OBI:0200000] |

## protocolSubtype

Name of the protocol's subtype. We highly recommend the usage of names given to ontologized protocols, specially those at the [Experimental Factor Ontology (EFO)](https://www.ebi.ac.uk/ols/ontologies/efo). For example, if the protocol corresponds to a data transformation of a genome, you may find your subtype at [genome analysis](http://edamontology.org/operation_3918); while treating a patient with a drug would correspond to a [clinical treatment](http://www.ebi.ac.uk/efo/EFO_0007056).

`protocolSubtype`

*   is optional

*   Type: `string` ([Subtype of the protocol](ega-17-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype")

### protocolSubtype Type

`string` ([Subtype of the protocol](ega-17-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

### protocolSubtype Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### protocolSubtype Examples

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

## protocolSubtypeCurie

Ontology term in CURIE format (e.g. 'EFO:0005518') of the protocol subtype. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index). This allows for a specific designation of the protocol within the overall general of the 'protocolType' field. For instance, the CURIE for Treatment's subtype 'clinical treatment' would be 'EFO:0003814'. If the protocol does not require a subtype, use the CURIE for the protocol type per se (e.g. 'EFO:0005518' for 'Sample collection').

`protocolSubtypeCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the protocol subtype](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtypeCurie")

### protocolSubtypeCurie Type

`string` ([Compact URI (CURIE) of the protocol subtype](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

*   any of

    *   [Untitled undefined type in EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype-allof-ontology-validation-of-it-being-part-of-efos-protocol-obi0000272-or-planned-process-efo0004542-or-edams-analysis-operation2945-anyof-0.md "check type definition")

    *   [Untitled undefined type in EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype-allof-ontology-validation-of-it-being-part-of-efos-protocol-obi0000272-or-planned-process-efo0004542-or-edams-analysis-operation2945-anyof-1.md "check type definition")

    *   [Untitled undefined type in EGA protocol metadata schema](ega-17-properties-protocol-type-descriptor-properties-compact-uri-curie-of-the-protocol-subtype-allof-ontology-validation-of-it-being-part-of-efos-protocol-obi0000272-or-planned-process-efo0004542-or-edams-analysis-operation2945-anyof-2.md "check type definition")

### protocolSubtypeCurie Examples

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

```json
"EFO:0000494"
```

```json
"operation:3223"
```
