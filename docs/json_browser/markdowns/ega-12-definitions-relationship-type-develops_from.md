# Relationship type: develops\_from Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_relationships/items/allOf/1/anyOf/2/allOf/0/anyOf/3
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 3 Type

`object` ([Relationship type: develops\_from](ega-12-definitions-relationship-type-develops_from.md))

# 3 Properties

| Property           | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :----------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-develops_from-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-develops_from/properties/r_type") |

## r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-develops_from-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-develops_from/properties/r_type")

### r\_type Type

unknown

### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"develops_from"
```