# Array of Sample-label pairs of the ArrayAssay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_labels
```

Sample-Label pairs (format being 'EGAN\[0-9]{11}:Label' - e.g. 'EGAN00000000001:Cy3') to know which samples used in this assay are labelled by which chemicals. Could be omitted if the array is of one single label and colour.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## sample_labels Type

`object[]` ([Repeatable Sample-label node](ega-2-definitions-repeatable-sample-label-node.md))

## sample_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
