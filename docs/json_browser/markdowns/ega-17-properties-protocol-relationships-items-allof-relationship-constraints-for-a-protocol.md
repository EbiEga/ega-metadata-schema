# Relationship constraints for a protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_relationships/items/allOf/1
```

Not all possible relationships between objects are allowed (e.g. an individual should not be linked to a policy). This node contains the restricted relationships that can be given for a protocol.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 1 Type

merged type ([Relationship constraints for a protocol](ega-17-properties-protocol-relationships-items-allof-relationship-constraints-for-a-protocol.md))

any of

*   all of

    *   [Relationship type: referenced_by](ega-12-definitions-relationship-type-referenced_by.md "check type definition")

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

        *   [Relationship type: grouped_with](ega-12-definitions-relationship-type-grouped_with.md "check type definition")

        *   [Relationship type: is_after](ega-12-definitions-relationship-type-is_after.md "check type definition")

        *   [Relationship type: same_as](ega-12-definitions-relationship-type-same_as.md "check type definition")

        *   [Relationship type: member_of](ega-12-definitions-relationship-type-member_of.md "check type definition")

    *   any of

        *   [Relationship source: protocol](ega-12-definitions-relationship-source-protocol.md "check type definition")

        *   [Relationship target: protocol](ega-12-definitions-relationship-target-protocol.md "check type definition")

*   all of

    *   any of

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