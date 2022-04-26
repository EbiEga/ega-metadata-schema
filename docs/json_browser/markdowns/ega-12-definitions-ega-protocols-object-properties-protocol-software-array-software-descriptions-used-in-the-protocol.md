# Software descriptions used in the protocol Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software/items
```

Free form text to specify the programs and other operating information (including bespoken scripts) used by a computer that were used by the performer of the protocol. Include the version of the program, if applicable. We highly recommend the usage of ontologized terms (e.g. 'SAMtools') from the [Software Ontology (SWO)](https://www.ebi.ac.uk/ols/ontologies/swo) along their versions (e.g. 'v3.0.1') and CURIEs between square brackets (e.g. '\[SWO:1100143]').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`string` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

## items Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## items Examples

```json
"SAMtools v3.0.1 [SWO:1100143]"
```

```json
"MATLAB [SWO:0000005]"
```
