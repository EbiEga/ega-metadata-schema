# Pattern of an EGA sample's ID (EGAN...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/4/properties/object_id/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ega\_accession Type

`string` ([Pattern of an EGA sample's ID (EGAN...)](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check-properties-object_id-properties-pattern-of-an-ega-samples-id-egan.md))

## ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAN[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAN%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega\_accession Examples

```json
"EGAN00003245489"
```
