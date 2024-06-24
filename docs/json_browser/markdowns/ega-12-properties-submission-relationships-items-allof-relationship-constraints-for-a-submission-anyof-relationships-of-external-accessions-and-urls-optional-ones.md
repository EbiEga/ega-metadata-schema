# Relationships of external accessions and URLs (optional ones) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionRelationships/items/allOf/1/anyOf/1
```

Almost any relationship is imaginable with external accessions and URLs.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## 1 Type

merged type ([Relationships of external accessions and URLs (optional ones)](ega-12-properties-submission-relationships-items-allof-relationship-constraints-for-a-submission-anyof-relationships-of-external-accessions-and-urls-optional-ones.md))

all of

* any of

  * [Relationship type: childOf](ega-4-defs-relationship-type-childof.md "check type definition")

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
