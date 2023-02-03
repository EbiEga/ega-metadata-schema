# studyDesigns array Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyDesigns
```

List of study designs (a.k.a. experimental designs). Contains specific keywords (e.g. 'RNA stability design') as items that can be associated to the study, providing an overall view of the method of investigating particular types of research questions or solving particular types of problems.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## studyDesigns Type

`string[]` ([Enumeration of design keywords](ega-4-definitions-enumeration-of-design-keywords.md))

## studyDesigns Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
