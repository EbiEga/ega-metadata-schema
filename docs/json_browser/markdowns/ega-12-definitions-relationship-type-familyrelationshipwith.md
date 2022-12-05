# Relationship type: familyRelationshipWith Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyRelationships/items/allOf/1/anyOf/2/allOf/0/anyOf/1
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## 1 Type

`object` ([Relationship type: familyRelationshipWith](ega-12-definitions-relationship-type-familyrelationshipwith.md))

# 1 Properties

| Property        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :-------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-familyrelationshipwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith/properties/rType") |

## rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-familyrelationshipwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith/properties/rType")

### rType Type

unknown

### rType Constraints

**constant**: the value of this property must be equal to:

```json
"familyRelationshipWith"
```
