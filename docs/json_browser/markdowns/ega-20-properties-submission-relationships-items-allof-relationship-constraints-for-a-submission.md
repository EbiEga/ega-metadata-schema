# Relationship constraints for a submission Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submission_relationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a submission. Bare in mind that 'submissions' are referenced\_by other objects, hence the relationship shall exist in their respective JSON documents.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for a submission](ega-20-properties-submission-relationships-items-allof-relationship-constraints-for-a-submission.md))

any of

*   all of

    *   any of

        *   [Relationship type: same_as](ega-12-definitions-relationship-type-same_as.md "check type definition")

        *   [Relationship type: grouped_with](ega-12-definitions-relationship-type-grouped_with.md "check type definition")

        *   [Relationship type: is_after](ega-12-definitions-relationship-type-is_after.md "check type definition")

    *   any of

        *   [Relationship source: submission](ega-12-definitions-relationship-source-submission.md "check type definition")

        *   [Relationship target: submission](ega-12-definitions-relationship-target-submission.md "check type definition")

*   all of

    *   any of

        *   [Relationship type: child_of](ega-12-definitions-relationship-type-child_of.md "check type definition")

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