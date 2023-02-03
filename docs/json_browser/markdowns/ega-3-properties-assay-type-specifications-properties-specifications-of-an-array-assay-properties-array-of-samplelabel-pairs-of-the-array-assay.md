# Array of sampleLabel pairs of the array assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/arraySampleLabels
```

Sample-Label pairs (e.g. sample 'EGAN00000000001' and label 'Cy3') to know which samples used in this assay are labelled by which chemicals. Can be omitted if the array is of one single label/colour.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## arraySampleLabels Type

`object[]` ([Repeatable Sample-label node](ega-4-definitions-repeatable-sample-label-node.md))

## arraySampleLabels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
