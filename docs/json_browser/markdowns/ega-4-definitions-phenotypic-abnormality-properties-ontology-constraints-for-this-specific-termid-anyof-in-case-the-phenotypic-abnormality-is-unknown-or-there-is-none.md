# In case the phenotypic abnormality is unknown or there is none Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality/properties/termId/anyOf/1
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([In case the phenotypic abnormality is unknown or there is none](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md))

## 1 Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"NCIT:C17998"` | Unknown     |
| `"NCIT:C94232"` | Unaffected  |
