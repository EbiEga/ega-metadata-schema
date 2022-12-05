# Relationship type: groupedWith Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships/items/allOf/1/anyOf/2/allOf/0/anyOf/0
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 0 Type

`object` ([Relationship type: groupedWith](ega-12-definitions-relationship-type-groupedwith.md))

# 0 Properties

| Property        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :-------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-groupedwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith/properties/rType") |

## rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-groupedwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith/properties/rType")

### rType Type

unknown

### rType Constraints

**constant**: the value of this property must be equal to:

```json
"groupedWith"
```