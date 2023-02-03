# Number of labels per array Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/nLabelsPerArray
```

A single array can be prepared with biological materials labelled differently for them to be compared in parallel. Here one shall specify the number of labels used in the single array (e.g. 2 for a Two-colour cDNA microarray). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## nLabelsPerArray Type

`number` ([Number of labels per array](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md))

## nLabelsPerArray Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                                                                                                                         |
| :---- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1`   | One single label was used for a single array                                                                                                        |
| `2`   | Two labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected.   |
| `3`   | Three labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected. |
| `4`   | Four labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected.  |
