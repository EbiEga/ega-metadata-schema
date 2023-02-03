# Software descriptions used in the protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolSoftware/items
```

Free form text to specify the programs and other operating information (including bespoken scripts) used by a computer that were used by the performer of the protocol. We highly recommend the usage of ontologized terms (e.g. 'SAMtools') from the [Software Ontology (SWO)](https://www.ebi.ac.uk/ols/ontologies/swo) along their versions (e.g. 'v3.0.1'), if applicable, and CURIEs between square brackets (e.g. '\[SWO:1100143]').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## items Type

`string` ([Software descriptions used in the protocol](ega-9-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

## items Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## items Examples

```json
"SAMtools v3.0.1 [SWO:1100143]"
```

```json
"MATLAB [SWO:0000005]"
```
