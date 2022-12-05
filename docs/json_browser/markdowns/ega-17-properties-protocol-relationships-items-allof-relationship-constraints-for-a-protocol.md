# Relationship constraints for a protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a protocol.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for a protocol](ega-17-properties-protocol-relationships-items-allof-relationship-constraints-for-a-protocol.md))

any of

*   all of

    *   [Relationship type: referencedBy](ega-12-definitions-relationship-type-referencedby.md "check type definition")

    *   any of

        *   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")

        *   [Relationship source: protocol](ega-12-definitions-relationship-source-protocol.md "check type definition")

        *   [Relationship target: sample](ega-12-definitions-relationship-target-sample.md "check type definition")

        *   [Relationship target: experiment](ega-12-definitions-relationship-target-experiment.md "check type definition")

        *   [Relationship target: analysis](ega-12-definitions-relationship-target-analysis.md "check type definition")

        *   [Relationship target: study](ega-12-definitions-relationship-target-study.md "check type definition")

        *   [Relationship target: individual](ega-12-definitions-relationship-target-individual.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: groupedWith](ega-12-definitions-relationship-type-groupedwith.md "check type definition")

        *   [Relationship type: isAfter](ega-12-definitions-relationship-type-isafter.md "check type definition")

        *   [Relationship type: sameAs](ega-12-definitions-relationship-type-sameas.md "check type definition")

        *   [Relationship type: memberOf](ega-12-definitions-relationship-type-memberof.md "check type definition")

    *   any of

        *   [Relationship source: protocol](ega-12-definitions-relationship-source-protocol.md "check type definition")

        *   [Relationship target: protocol](ega-12-definitions-relationship-target-protocol.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: groupedWith](ega-12-definitions-relationship-type-groupedwith.md "check type definition")

        *   [Relationship type: sameAs](ega-12-definitions-relationship-type-sameas.md "check type definition")

        *   [Relationship type: referencedBy](ega-12-definitions-relationship-type-referencedby.md "check type definition")

        *   [Relationship type: developsFrom](ega-12-definitions-relationship-type-developsfrom.md "check type definition")

        *   [Relationship type: memberOf](ega-12-definitions-relationship-type-memberof.md "check type definition")

        *   [Relationship type: isAfter](ega-12-definitions-relationship-type-isafter.md "check type definition")

    *   any of

        *   [Relationship source: externalAccession](ega-12-definitions-relationship-source-externalaccession.md "check type definition")

        *   [Relationship source: externalURL](ega-12-definitions-relationship-source-externalurl.md "check type definition")

        *   [Relationship target: externalAccession](ega-12-definitions-relationship-target-externalaccession.md "check type definition")

        *   [Relationship target: externalURL](ega-12-definitions-relationship-target-externalurl.md "check type definition")
