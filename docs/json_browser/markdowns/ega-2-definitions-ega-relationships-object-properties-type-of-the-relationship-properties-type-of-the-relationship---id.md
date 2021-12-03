# Type of the relationship - ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_id
```

The human readable ID (e.g. same_as), chosen from a list of CVs, of the type of the relationship.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## r_type_id Type

`string` ([Type of the relationship - ID](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---id.md))

## r_type_id Constraints

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

## r_type_id Examples

```json
"referenced_by"
```
