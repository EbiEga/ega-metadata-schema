# Assay relationships Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities, one of which shall be the current assay.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.assay.json*](../out/EGA.assay.json "open original schema") |

## assay_relationships Type

`object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

## assay_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
