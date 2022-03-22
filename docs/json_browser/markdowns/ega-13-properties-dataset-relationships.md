# Dataset relationships Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a dataset) the EGA.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.dataset.json*](../out/EGA.dataset.json "open original schema") |

## dataset_relationships Type

`object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

## dataset_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
