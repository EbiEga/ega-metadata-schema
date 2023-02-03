# Type of protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolType
```

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocolType Type

`string` ([Type of protocol](ega-9-properties-protocol-type-descriptor-properties-type-of-protocol.md))

## protocolType Constraints

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
