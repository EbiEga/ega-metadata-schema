# Type of protocol Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor/properties/protocol_type
```

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## protocol_type Type

`string` ([Type of protocol](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor-properties-type-of-protocol.md))

## protocol_type Constraints

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
