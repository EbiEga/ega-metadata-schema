# Assay files object from an ArrayAssay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/assay_files
```

This array object contains the specific files derived from performing an hybridization of the assayed molecule to a physical array. Given the amount of technologies available for such purpose, the allowed filetypes shall be agreed upon and updated accordingly.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## assay_files Type

`object[]` ([EGA File object](ega-4-definitions-ega-file-object.md))

## assay_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
