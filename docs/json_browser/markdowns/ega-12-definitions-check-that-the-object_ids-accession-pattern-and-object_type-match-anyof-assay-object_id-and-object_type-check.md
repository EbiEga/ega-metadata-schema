# Assay: object_id and object_type check Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/6
```

A check that ensures that, if 'assay' is given as the object_type and an EGA accession for it is given, it matches the corresponding EGA ID pattern.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 6 Type

unknown ([Assay: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check.md))

# 6 Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)     | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check-properties-object_id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/6/properties/object_id")     |
| [object_type](#object_type) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check-properties-object_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/6/properties/object_type") |

## object_id



`object_id`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check-properties-object_id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/6/properties/object_id")

### object_id Type

unknown

## object_type



`object_type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check-properties-object_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/6/properties/object_type")

### object_type Type

unknown

### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"assay"` |             |
