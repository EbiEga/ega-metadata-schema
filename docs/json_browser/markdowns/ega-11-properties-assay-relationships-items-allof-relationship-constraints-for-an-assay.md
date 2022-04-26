# Relationship constraints for an assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_relationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a XXXXX.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for an assay](ega-11-properties-assay-relationships-items-allof-relationship-constraints-for-an-assay.md))

any of

*   all of

    *   [Relationship type: referenced_by](ega-12-definitions-relationship-type-referenced_by.md "check type definition")

    *   any of

        *   [Relationship target: dataset](ega-12-definitions-relationship-target-dataset.md "check type definition")

        *   [Relationship target: analysis](ega-12-definitions-relationship-target-analysis.md "check type definition")

        *   [Relationship source: sample](ega-12-definitions-relationship-source-sample.md "check type definition")

        *   [Relationship source: experiment](ega-12-definitions-relationship-source-experiment.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: grouped_with](ega-12-definitions-relationship-type-grouped_with.md "check type definition")

        *   [Relationship type: is_after](ega-12-definitions-relationship-type-is_after.md "check type definition")

        *   [Relationship type: same_as](ega-12-definitions-relationship-type-same_as.md "check type definition")

    *   any of

        *   [Relationship source: assay](ega-12-definitions-relationship-source-assay.md "check type definition")

        *   [Relationship target: assay](ega-12-definitions-relationship-target-assay.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: child_of](ega-12-definitions-relationship-type-child_of.md "check type definition")

        *   [Relationship type: family_relationship_with](ega-12-definitions-relationship-type-family_relationship_with.md "check type definition")

        *   [Relationship type: grouped_with](ega-12-definitions-relationship-type-grouped_with.md "check type definition")

        *   [Relationship type: same_as](ega-12-definitions-relationship-type-same_as.md "check type definition")

        *   [Relationship type: referenced_by](ega-12-definitions-relationship-type-referenced_by.md "check type definition")

        *   [Relationship type: develops_from](ega-12-definitions-relationship-type-develops_from.md "check type definition")

        *   [Relationship type: member_of](ega-12-definitions-relationship-type-member_of.md "check type definition")

        *   [Relationship type: is_after](ega-12-definitions-relationship-type-is_after.md "check type definition")

    *   any of

        *   [Relationship source: external_accession](ega-12-definitions-relationship-source-external_accession.md "check type definition")

        *   [Relationship source: external_URL](ega-12-definitions-relationship-source-external_url.md "check type definition")

        *   [Relationship target: external_accession](ega-12-definitions-relationship-target-external_accession.md "check type definition")

        *   [Relationship target: external_URL](ega-12-definitions-relationship-target-external_url.md "check type definition")
