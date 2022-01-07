# External accessions array Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions
```

Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## external_accessions Type

`object[]` ([Object of external accession of the object](ega-4-definitions-object-of-external-accession-of-the-object.md))

## external_accessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
