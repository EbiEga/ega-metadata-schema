# Pattern of an EGA sample's ID (EGAN...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id/allOf/1/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## ega_accession Type

`string` ([Pattern of an EGA sample's ID (EGAN...)](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct-properties-pattern-of-an-ega-samples-id-egan.md))

## ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAN[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAN%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega_accession Examples

```json
"EGAN00003245489"
```
