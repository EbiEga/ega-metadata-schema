# Data files produced from an assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_files
```

This property contains the specific files (e.g. raw CRAM files) derived from performing the sequencing or hybridization and scanning with the sampled material.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## assay\_files Type

`object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

## assay\_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
