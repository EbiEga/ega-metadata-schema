# Sample: objectId and objectType check Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4
```

A check that ensures that, if 'sample' is given as the objectType and an EGA accession for it is given, it matches the corresponding EGA ID pattern.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 4 Type

unknown ([Sample: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check.md))

# 4 Properties

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)     | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check-properties-objectid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4/properties/objectId")     |
| [objectType](#objecttype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check-properties-objecttype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4/properties/objectType") |

## objectId



`objectId`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check-properties-objectid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4/properties/objectId")

### objectId Type

unknown

## objectType



`objectType`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check-properties-objecttype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck/anyOf/4/properties/objectType")

### objectType Type

unknown

### objectType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"sample"` |             |
