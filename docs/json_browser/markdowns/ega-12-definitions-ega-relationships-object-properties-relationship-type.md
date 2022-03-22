# Relationship type Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type
```

ID (e.g. same_as) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## r_type Type

`string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

## r_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                        | Explanation |
| :--------------------------- | :---------- |
| `"referenced_by"`            |             |
| `"develops_from"`            |             |
| `"same_as"`                  |             |
| `"member_of"`                |             |
| `"grouped_with"`             |             |
| `"family_relationship_with"` |             |
| `"child_of"`                 |             |
| `"parent_of"`                |             |
| `"is_after"`                 |             |
| `"published_in"`             |             |
| `"submitted_by"`             |             |
| `"contact_of"`               |             |
| `"main_contact_of"`          |             |

## r_type Examples

```json
"referenced_by"
```
