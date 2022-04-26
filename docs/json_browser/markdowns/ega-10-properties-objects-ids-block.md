# Object's IDs block Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_id
```

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## object\_id Type

`object` ([Object's IDs block](ega-10-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that analysis EGA ID (EGAZ) is correct](ega-10-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct.md "check type definition")
