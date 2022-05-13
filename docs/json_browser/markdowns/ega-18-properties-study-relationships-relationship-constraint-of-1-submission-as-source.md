# Relationship constraint of 1 submission as source Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships/contains
```

This node defines a relationship item containing a 'submission' as a source and of type 'referenced\_by'. This node can be used with the keyword 'contains' at each relationship array of all objects (but submission), in order to assert that all objects have a submission object (EGAB...) linked to them.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## contains Type

merged type ([Relationship constraint of 1 submission as source](ega-18-properties-study-relationships-relationship-constraint-of-1-submission-as-source.md))

all of

*   [Relationship type: referenced_by](ega-12-definitions-relationship-type-referenced_by.md "check type definition")

*   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")
