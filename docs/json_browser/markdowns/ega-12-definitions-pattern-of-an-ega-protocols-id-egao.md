# Pattern of an EGA protocol's ID (EGAO...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/objectId/allOf/1/properties/egaAccession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## egaAccession Type

`string` ([Pattern of an EGA protocol's ID (EGAO...)](ega-12-definitions-pattern-of-an-ega-protocols-id-egao.md))

## egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAO[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAO%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## egaAccession Examples

```json
"EGAO00001159483"
```