# Untitled undefined type in EGA assay metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayRelationships/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## items Type

merged type ([Details](ega-3-properties-assay-relationships-items.md))

all of

* one (and only one) of

  * [The source is given (i.e. the target is inferred as the current instance)](ega-4-defs-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

  * [The target is given (i.e. the source is inferred as the current instance)](ega-4-defs-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

* any of

  * all of

    * [Relationship type: referencedBy](ega-4-defs-relationship-type-referencedby.md "check type definition")

    * any of

      * [Relationship target: dataset](ega-4-defs-relationship-target-dataset.md "check type definition")

      * [Relationship target: analysis](ega-4-defs-relationship-target-analysis.md "check type definition")

      * [Relationship source: sample](ega-4-defs-relationship-source-sample.md "check type definition")

      * [Relationship source: experiment](ega-4-defs-relationship-source-experiment.md "check type definition")

      * [Relationship source: submission](ega-4-defs-relationship-source-submission.md "check type definition")

  * all of

    * any of

      * [Relationship type: groupedWith](ega-4-defs-relationship-type-groupedwith.md "check type definition")

      * [Relationship type: isAfter](ega-4-defs-relationship-type-isafter.md "check type definition")

      * [Relationship type: sameAs](ega-4-defs-relationship-type-sameas.md "check type definition")

    * any of

      * [Relationship source: assay](ega-4-defs-relationship-source-assay.md "check type definition")

      * [Relationship target: assay](ega-4-defs-relationship-target-assay.md "check type definition")

  * all of

    * any of

      * [Relationship type: childOf](ega-4-defs-relationship-type-childof.md "check type definition")

      * [Relationship type: familyRelationshipWith](ega-4-defs-relationship-type-familyrelationshipwith.md "check type definition")

      * [Relationship type: groupedWith](ega-4-defs-relationship-type-groupedwith.md "check type definition")

      * [Relationship type: sameAs](ega-4-defs-relationship-type-sameas.md "check type definition")

      * [Relationship type: referencedBy](ega-4-defs-relationship-type-referencedby.md "check type definition")

      * [Relationship type: developsFrom](ega-4-defs-relationship-type-developsfrom.md "check type definition")

      * [Relationship type: memberOf](ega-4-defs-relationship-type-memberof.md "check type definition")

      * [Relationship type: isAfter](ega-4-defs-relationship-type-isafter.md "check type definition")

    * any of

      * [Relationship source: externalAccession](ega-4-defs-relationship-source-externalaccession.md "check type definition")

      * [Relationship source: externalURL](ega-4-defs-relationship-source-externalurl.md "check type definition")

      * [Relationship target: externalAccession](ega-4-defs-relationship-target-externalaccession.md "check type definition")

      * [Relationship target: externalURL](ega-4-defs-relationship-target-externalurl.md "check type definition")
