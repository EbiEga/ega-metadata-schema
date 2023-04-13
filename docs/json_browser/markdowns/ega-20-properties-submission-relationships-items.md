# Untitled undefined type in EGA submission metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionRelationships/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## items Type

merged type ([Details](ega-20-properties-submission-relationships-items.md))

all of

*   one (and only one) of

    *   [The source is given (i.e. the target is inferred as the current instance)](ega-12-definitions-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

    *   [The target is given (i.e. the source is inferred as the current instance)](ega-12-definitions-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

*   any of

    *   all of

        *   any of

            *   [Relationship type: sameAs](ega-12-definitions-relationship-type-sameas.md "check type definition")

            *   [Relationship type: groupedWith](ega-12-definitions-relationship-type-groupedwith.md "check type definition")

            *   [Relationship type: isAfter](ega-12-definitions-relationship-type-isafter.md "check type definition")

        *   any of

            *   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")

            *   [Relationship target: submission](ega-12-definitions-relationship-target-submission.md "check type definition")

    *   all of

        *   any of

            *   [Relationship type: childOf](ega-12-definitions-relationship-type-childof.md "check type definition")

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