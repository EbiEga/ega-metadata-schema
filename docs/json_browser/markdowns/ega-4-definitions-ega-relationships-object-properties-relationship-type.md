# Relationship type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rType
```

ID (e.g. sameAs) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## rType Type

`string` ([Relationship type](ega-4-definitions-ega-relationships-object-properties-relationship-type.md))

## rType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation    |
| :------------------------- | :------------- |
| `"referencedBy"`           | \[SIO:000252]  |
| `"developsFrom"`           | \[RO:0002202]  |
| `"sameAs"`                 | \[NCIT:C64637] |
| `"memberOf"`               | \[RO:0002350]  |
| `"groupedWith"`            |                |
| `"familyRelationshipWith"` | \[EFO:0004424] |
| `"childOf"`                | \[GSSO:000728] |
| `"isAfter"`                | \[SIO:000211]  |
| `"publishedIn"`            | \[EFO:0001796] |
| `"submittedBy"`            | \[NCIT:C25695] |
| `"contactOf"`              | \[NCIT:C25461] |
| `"mainContactOf"`          |                |

## rType Examples

```json
"referencedBy"
```
