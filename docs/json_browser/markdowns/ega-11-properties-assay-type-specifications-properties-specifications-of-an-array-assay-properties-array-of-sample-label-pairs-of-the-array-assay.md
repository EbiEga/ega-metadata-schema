# Array of sample-label pairs of the array assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications/properties/array_sample_labels
```

Sample-Label pairs (e.g. sample 'EGAN00000000001' and label 'Cy3') to know which samples used in this assay are labelled by which chemicals. Can be omitted if the array is of one single label/colour.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## array\_sample\_labels Type

`object[]` ([Repeatable Sample-label node](ega-12-definitions-repeatable-sample-label-node.md))

## array\_sample\_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
