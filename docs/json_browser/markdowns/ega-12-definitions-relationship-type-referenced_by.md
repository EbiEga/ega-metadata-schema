# Relationship type: referenced\_by Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_relationships/items/allOf/1/anyOf/1/allOf/0/anyOf/3
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## 3 Type

`object` ([Relationship type: referenced\_by](ega-12-definitions-relationship-type-referenced_by.md))

# 3 Properties

| Property           | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                   |
| :----------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-referenced_by-properties-r_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/r-type-referenced_by/properties/r_type") |

## r\_type



`r_type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-referenced_by-properties-r_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/r-type-referenced_by/properties/r_type")

### r\_type Type

unknown

### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"referenced_by"
```
