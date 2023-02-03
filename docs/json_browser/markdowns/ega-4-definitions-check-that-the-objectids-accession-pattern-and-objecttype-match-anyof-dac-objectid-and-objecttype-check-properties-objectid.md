# Untitled undefined type in EGA common metadata definitions Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/10/properties/objectId
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectId Type

unknown

# objectId Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [egaAccession](#egaaccession) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-dacs-id-egac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/10/properties/objectId/properties/egaAccession") |

## egaAccession



`egaAccession`

*   is optional

*   Type: `string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-dacs-id-egac.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-dacs-id-egac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/10/properties/objectId/properties/egaAccession")

### egaAccession Type

`string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check-properties-objectid-properties-pattern-of-an-ega-dacs-id-egac.md))

### egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAC[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAC%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### egaAccession Examples

```json
"EGAC00001000908"
```
