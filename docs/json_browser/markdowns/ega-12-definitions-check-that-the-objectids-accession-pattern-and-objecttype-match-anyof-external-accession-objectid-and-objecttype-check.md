# External accession: objectId and objectType check Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/1
```

A check that ensures that, if 'externalAccession' is given as the objectType, the corresponding node exists within objectId

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([External accession: objectId and objectType check](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check.md))

# 1 Properties

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)     | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check-properties-objectid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/1/properties/objectId")     |
| [objectType](#objecttype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check-properties-objecttype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/1/properties/objectType") |

## objectId



`objectId`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check-properties-objectid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/1/properties/objectId")

### objectId Type

unknown

## objectType



`objectType`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check-properties-objecttype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/1/properties/objectType")

### objectType Type

unknown

### objectType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"externalAccession"` |             |
