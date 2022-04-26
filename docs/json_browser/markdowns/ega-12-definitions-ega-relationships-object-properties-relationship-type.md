# Relationship type Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type
```

ID (e.g. same\_as) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## r\_type Type

`string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

## r\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                        | Explanation    |
| :--------------------------- | :------------- |
| `"referenced_by"`            | \[SIO:000252]  |
| `"develops_from"`            | \[RO:0002202]  |
| `"same_as"`                  | \[NCIT:C64637] |
| `"member_of"`                | \[RO:0002350]  |
| `"grouped_with"`             |                |
| `"family_relationship_with"` | \[EFO:0004424] |
| `"child_of"`                 | \[GSSO:000728] |
| `"is_after"`                 | \[SIO:000211]  |
| `"published_in"`             | \[EFO:0001796] |
| `"submitted_by"`             | \[NCIT:C25695] |
| `"contact_of"`               | \[NCIT:C25461] |
| `"main_contact_of"`          |                |

## r\_type Examples

```json
"referenced_by"
```
