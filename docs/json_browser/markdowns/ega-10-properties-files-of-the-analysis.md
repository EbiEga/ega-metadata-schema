# Files of the analysis Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_files
```

This property contains the files derived from performing any processing or analysis over raw data (e.g. VCF, aligned BAM...) and those that add context to it (e.g. CSV, TXT...).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysis\_files Type

`object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

## analysis\_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
