# Object's IDs block Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/object_id
```

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: an policy (by using EGA-policy-id-pattern)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## object\_id Type

`object` ([Object's IDs block](ega-16-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that policy EGA ID (EGAP) is correct](ega-16-properties-objects-ids-block-allof-check-that-policy-ega-id-egap-is-correct.md "check type definition")
