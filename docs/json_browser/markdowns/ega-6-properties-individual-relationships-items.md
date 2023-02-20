# Untitled undefined type in EGA individual metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualRelationships/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## items Type

merged type ([Details](ega-6-properties-individual-relationships-items.md))

all of

*   one (and only one) of

    *   [The source is given (i.e. the target is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

    *   [The target is given (i.e. the source is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

*   any of

    *   all of

        *   [Relationship type: referencedBy](ega-4-definitions-relationship-type-referencedby.md "check type definition")

        *   any of

            *   [Relationship target: sample](ega-4-definitions-relationship-target-sample.md "check type definition")

            *   [Relationship source: submission](ega-4-definitions-relationship-source-submission.md "check type definition")

            *   [Relationship source: protocol](ega-4-definitions-relationship-source-protocol.md "check type definition")

    *   all of

        *   any of

            *   [Relationship type: childOf](ega-4-definitions-relationship-type-childof.md "check type definition")

            *   [Relationship type: familyRelationshipWith](ega-4-definitions-relationship-type-familyrelationshipwith.md "check type definition")

            *   [Relationship type: groupedWith](ega-4-definitions-relationship-type-groupedwith.md "check type definition")

            *   [Relationship type: sameAs](ega-4-definitions-relationship-type-sameas.md "check type definition")

        *   any of

            *   [Relationship source: individual](ega-4-definitions-relationship-source-individual.md "check type definition")

            *   [Relationship target: individual](ega-4-definitions-relationship-target-individual.md "check type definition")

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