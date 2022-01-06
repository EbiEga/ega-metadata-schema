# Object's IDs block Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id
```

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: a individual (by using EGA-individual-id-pattern)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.individual.json*](../out/EGA.individual.json "open original schema") |

## object_id Type

`object` ([Object's IDs block](ega-3-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that individual EGA ID (EGAI) is correct](ega-3-properties-objects-ids-block-allof-check-that-individual-ega-id-egai-is-correct.md "check type definition")
