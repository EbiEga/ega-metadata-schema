# Protocol type descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor
```

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocolTypeDescriptor Type

`object` ([Protocol type descriptor](ega-9-properties-protocol-type-descriptor.md))

# protocolTypeDescriptor Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolType](#protocoltype)       | `string` | Required | cannot be null | [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolType")           |
| [protocolSubtype](#protocolsubtype) | Merged   | Required | cannot be null | [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype") |

## protocolType

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`protocolType`

*   is required

*   Type: `string` ([Type of protocol](ega-9-properties-protocol-type-descriptor-properties-type-of-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-type-of-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolType")

### protocolType Type

`string` ([Type of protocol](ega-9-properties-protocol-type-descriptor-properties-type-of-protocol.md))

### protocolType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                 | Explanation    |
| :------------------------------------ | :------------- |
| `"high Content Screen (HCS)"`         | \[EFO:0007570] |
| `"conversion"`                        | \[EFO:0005520] |
| `"delivery method"`                   | \[EFO:0000395] |
| `"dissection"`                        | \[EFO:0005519] |
| `"dissociation"`                      | \[EFO:0009088] |
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

Ontology term of the protocol subtype. Search for yours at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index). This allows for a specific designation of the protocol within the high level 'protocolType' field. For instance, for Treatment's subtype 'clinical treatment' ('termLabel') we would use 'EFO:0003814' ('termId'). In case the protocol does not have a subtype, use 'NCIT:C48660' for 'Not applicable'.

`protocolSubtype`

*   is required

*   Type: `object` ([Subtype of the protocol](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype")

### protocolSubtype Type

`object` ([Subtype of the protocol](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
