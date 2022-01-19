# Pattern of an EGA experiment's ID (EGAX...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/2/properties/object_id/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## ega_accession Type

`string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check-properties-object_id-properties-pattern-of-an-ega-experiments-id-egax.md))

## ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAX[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAX%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega_accession Examples

```json
"EGAX00002189113"
```
