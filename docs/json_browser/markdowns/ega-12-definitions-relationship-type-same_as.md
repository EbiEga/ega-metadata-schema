# Relationship type: same\_as Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships/items/allOf/1/anyOf/2/allOf/0/anyOf/3
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## 3 Type

`object` ([Relationship type: same\_as](ega-12-definitions-relationship-type-same_as.md))

# 3 Properties

| Property           | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :----------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-same_as-properties-r_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/r-type-same_as/properties/r_type") |

## r\_type



`r_type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-same_as-properties-r_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/r-type-same_as/properties/r_type")

### r\_type Type

unknown

### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"same_as"
```
