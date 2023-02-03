# Relationship type: referencedBy Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships/items/allOf/1/anyOf/2/allOf/0/anyOf/2
```

Node to be used as a relationship type for relationship contraints.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 2 Type

`object` ([Relationship type: referencedBy](ega-4-definitions-relationship-type-referencedby.md))

# 2 Properties

| Property        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-referencedby-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy/properties/rType") |

## rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-referencedby-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy/properties/rType")

### rType Type

unknown

### rType Constraints

**constant**: the value of this property must be equal to:

```json
"referencedBy"
```
