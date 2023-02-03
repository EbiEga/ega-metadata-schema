# Untitled undefined type in EGA common metadata definitions Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/2/properties/objectId
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectId Type

unknown

# objectId Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [egaAccession](#egaaccession) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-experiments-id-egax.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/2/properties/objectId/properties/egaAccession") |

## egaAccession



`egaAccession`

*   is optional

*   Type: `string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-experiments-id-egax.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-experiments-id-egax.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/2/properties/objectId/properties/egaAccession")

### egaAccession Type

`string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-experiments-id-egax.md))

### egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAX[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAX%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### egaAccession Examples

```json
"EGAX00002189113"
```
