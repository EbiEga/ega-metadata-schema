# Untitled undefined type in EGA protocol metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## items Type

merged type ([Details](ega-9-properties-protocol-relationships-items.md))

all of

*   one (and only one) of

    *   [The source is given (i.e. the target is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

    *   [The target is given (i.e. the source is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

*   any of

    *   all of

        *   [Relationship type: referencedBy](ega-4-definitions-relationship-type-referencedby.md "check type definition")

        *   any of

            *   [Relationship source: submission](ega-4-definitions-relationship-source-submission.md "check type definition")

            *   [Relationship source: protocol](ega-4-definitions-relationship-source-protocol.md "check type definition")

            *   [Relationship target: sample](ega-4-definitions-relationship-target-sample.md "check type definition")

            *   [Relationship target: experiment](ega-4-definitions-relationship-target-experiment.md "check type definition")

            *   [Relationship target: analysis](ega-4-definitions-relationship-target-analysis.md "check type definition")

            *   [Relationship target: study](ega-4-definitions-relationship-target-study.md "check type definition")

            *   [Relationship target: individual](ega-4-definitions-relationship-target-individual.md "check type definition")

    *   all of

        *   any of

            *   [Relationship type: groupedWith](ega-4-definitions-relationship-type-groupedwith.md "check type definition")

            *   [Relationship type: isAfter](ega-4-definitions-relationship-type-isafter.md "check type definition")

            *   [Relationship type: sameAs](ega-4-definitions-relationship-type-sameas.md "check type definition")

            *   [Relationship type: memberOf](ega-4-definitions-relationship-type-memberof.md "check type definition")

        *   any of

            *   [Relationship source: protocol](ega-4-definitions-relationship-source-protocol.md "check type definition")

            *   [Relationship target: protocol](ega-4-definitions-relationship-target-protocol.md "check type definition")

    *   all of

        *   any of

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
