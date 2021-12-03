# Type of protocol \[OBI:0000272]  Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type
```

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary list (to be upgraded on demand).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## protocol_type Type

`string` ([Type of protocol \[OBI:0000272\] ](ega-2-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md))

## protocol_type Constraints

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

## protocol_type Examples

```json
"Sample collection"
```
