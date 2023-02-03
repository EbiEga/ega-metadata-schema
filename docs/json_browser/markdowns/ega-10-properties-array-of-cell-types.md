# Array of cell types Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes
```

Array of cell types, in case the sample is composed of cells (e.g. cell culture) or the cells from which the genetic material derived are known (e.g. extract DNA from astrocytes). Use this property as tags that befit your sample, picking as many cell types as your sample contains or may contain.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## cellTypes Type

`object[]` ([Cell type](ega-10-properties-array-of-cell-types-cell-type.md))

## cellTypes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
