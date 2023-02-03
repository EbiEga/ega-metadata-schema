# Pattern of an EGA assay's ID (EGAR...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/6/properties/objectId/properties/egaAccession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## egaAccession Type

`string` ([Pattern of an EGA assay's ID (EGAR...)](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-assay-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-assays-id-egar.md))

## egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAR[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAR%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## egaAccession Examples

```json
"EGAR00001314547"
```
