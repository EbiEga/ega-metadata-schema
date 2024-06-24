# Relationship constraint of 1 submission as source Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyRelationships/contains
```

This node defines a relationship item containing a 'submission' as a source and of type 'referencedBy'. This node can be used with the keyword 'contains' at each relationship array of all objects (but submission), in order to assert that all objects have a submission object (EGAB...) linked to them.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## contains Type

merged type ([Relationship constraint of 1 submission as source](ega-8-properties-policy-relationships-relationship-constraint-of-1-submission-as-source.md))

all of

* [Relationship type: referencedBy](ega-4-defs-relationship-type-referencedby.md "check type definition")

* [Relationship source: submission](ega-4-defs-relationship-source-submission.md "check type definition")
