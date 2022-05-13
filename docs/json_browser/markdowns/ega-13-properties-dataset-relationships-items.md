# Untitled undefined type in EGA dataset metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_relationships/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## items Type

merged type ([Details](ega-13-properties-dataset-relationships-items.md))

all of

*   one (and only one) of

    *   [The source is given (i.e. the target is inferred as the current instance)](ega-12-definitions-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

    *   [The target is given (i.e. the source is inferred as the current instance)](ega-12-definitions-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

*   any of

    *   all of

        *   [Relationship type: referenced_by](ega-12-definitions-relationship-type-referenced_by.md "check type definition")

        *   any of

            *   [Relationship source: Policy](ega-12-definitions-relationship-source-policy.md "check type definition")

            *   [Relationship source: assay](ega-12-definitions-relationship-source-assay.md "check type definition")

            *   [Relationship source: analysis](ega-12-definitions-relationship-source-analysis.md "check type definition")

            *   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")

    *   all of

        *   any of

            *   [Relationship type: grouped_with](ega-12-definitions-relationship-type-grouped_with.md "check type definition")

            *   [Relationship type: is_after](ega-12-definitions-relationship-type-is_after.md "check type definition")

            *   [Relationship type: same_as](ega-12-definitions-relationship-type-same_as.md "check type definition")

        *   any of

            *   [Relationship source: dataset](ega-12-definitions-relationship-source-dataset.md "check type definition")

            *   [Relationship target: dataset](ega-12-definitions-relationship-target-dataset.md "check type definition")

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
