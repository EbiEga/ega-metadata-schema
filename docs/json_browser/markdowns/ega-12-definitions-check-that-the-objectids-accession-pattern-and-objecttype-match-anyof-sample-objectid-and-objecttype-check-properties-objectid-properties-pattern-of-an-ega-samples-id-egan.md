# Pattern of an EGA sample's ID (EGAN...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4/properties/objectId/properties/egaAccession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## egaAccession Type

`string` ([Pattern of an EGA sample's ID (EGAN...)](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-samples-id-egan.md))

## egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAN[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAN%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## egaAccession Examples

```json
"EGAN00003245489"
```