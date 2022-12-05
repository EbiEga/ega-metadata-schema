# Relationship constraints for a dataset Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetRelationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a dataset.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for a dataset](ega-13-properties-dataset-relationships-items-allof-relationship-constraints-for-a-dataset.md))

any of

*   all of

    *   [Relationship type: referencedBy](ega-12-definitions-relationship-type-referencedby.md "check type definition")

    *   any of

        *   [Relationship source: Policy](ega-12-definitions-relationship-source-policy.md "check type definition")

        *   [Relationship source: assay](ega-12-definitions-relationship-source-assay.md "check type definition")

        *   [Relationship source: analysis](ega-12-definitions-relationship-source-analysis.md "check type definition")

        *   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: groupedWith](ega-12-definitions-relationship-type-groupedwith.md "check type definition")

        *   [Relationship type: isAfter](ega-12-definitions-relationship-type-isafter.md "check type definition")

        *   [Relationship type: sameAs](ega-12-definitions-relationship-type-sameas.md "check type definition")

    *   any of

        *   [Relationship source: dataset](ega-12-definitions-relationship-source-dataset.md "check type definition")

        *   [Relationship target: dataset](ega-12-definitions-relationship-target-dataset.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: childOf](ega-12-definitions-relationship-type-childof.md "check type definition")

        *   [Relationship type: familyRelationshipWith](ega-12-definitions-relationship-type-familyrelationshipwith.md "check type definition")

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
