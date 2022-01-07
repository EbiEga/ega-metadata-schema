# Pattern of an EGA ArrayAssay's ID (EGAA...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/12/properties/object_id/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## ega_accession Type

`string` ([Pattern of an EGA ArrayAssay's ID (EGAA...)](ega-4-definitions-pattern-of-an-ega-arrayassays-id-egaa.md))

## ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAA[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAA%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega_accession Examples

```json
"EGAA00002189113"
```
