# Relationship constraints for a study Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyRelationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a study.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for a study](ega-11-properties-study-relationships-items-allof-relationship-constraints-for-a-study.md))

any of

*   all of

    *   [Relationship type: referencedBy](ega-4-definitions-relationship-type-referencedby.md "check type definition")

    *   any of

        *   [Relationship target: analysis](ega-4-definitions-relationship-target-analysis.md "check type definition")

        *   [Relationship target: experiment](ega-4-definitions-relationship-target-experiment.md "check type definition")

        *   [Relationship source: submission](ega-4-definitions-relationship-source-submission.md "check type definition")

        *   [Relationship source: protocol](ega-4-definitions-relationship-source-protocol.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: groupedWith](ega-4-definitions-relationship-type-groupedwith.md "check type definition")

        *   [Relationship type: isAfter](ega-4-definitions-relationship-type-isafter.md "check type definition")

        *   [Relationship type: sameAs](ega-4-definitions-relationship-type-sameas.md "check type definition")

    *   any of

        *   [Relationship source: study](ega-4-definitions-relationship-source-study.md "check type definition")

        *   [Relationship target: study](ega-4-definitions-relationship-target-study.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: childOf](ega-4-definitions-relationship-type-childof.md "check type definition")

        *   [Relationship type: familyRelationshipWith](ega-4-definitions-relationship-type-familyrelationshipwith.md "check type definition")

        *   [Relationship type: groupedWith](ega-4-definitions-relationship-type-groupedwith.md "check type definition")

        *   [Relationship type: sameAs](ega-4-definitions-relationship-type-sameas.md "check type definition")

        *   [Relationship type: referencedBy](ega-4-definitions-relationship-type-referencedby.md "check type definition")

        *   [Relationship type: developsFrom](ega-4-definitions-relationship-type-developsfrom.md "check type definition")

        *   [Relationship type: memberOf](ega-4-definitions-relationship-type-memberof.md "check type definition")

        *   [Relationship type: isAfter](ega-4-definitions-relationship-type-isafter.md "check type definition")

    *   any of

        *   [Relationship source: externalAccession](ega-4-definitions-relationship-source-externalaccession.md "check type definition")

        *   [Relationship source: externalURL](ega-4-definitions-relationship-source-externalurl.md "check type definition")

        *   [Relationship target: externalAccession](ega-4-definitions-relationship-target-externalaccession.md "check type definition")

        *   [Relationship target: externalURL](ega-4-definitions-relationship-target-externalurl.md "check type definition")