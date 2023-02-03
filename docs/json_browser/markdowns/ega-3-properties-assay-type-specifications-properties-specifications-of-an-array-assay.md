# Specifications of an array assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications
```

Node containing the set of fields specific to an assay of type 'array' (i.e. an array was used to obtain the raw data).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## arrayAssaySpecifications Type

`object` ([Specifications of an array assay](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

any of

*   [2 labels per array check](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-2-labels-per-array-check.md "check type definition")

*   [3 labels per array check](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-3-labels-per-array-check.md "check type definition")

*   [4 labels per array check](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check.md "check type definition")

# arrayAssaySpecifications Properties

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [nLabelsPerArray](#nlabelsperarray)     | `number` | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/nLabelsPerArray")                      |
| [arraySampleLabels](#arraysamplelabels) | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-array-of-samplelabel-pairs-of-the-array-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/arraySampleLabels") |

## nLabelsPerArray

A single array can be prepared with biological materials labelled differently for them to be compared in parallel. Here one shall specify the number of labels used in the single array (e.g. 2 for a Two-colour cDNA microarray). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`nLabelsPerArray`

*   is required

*   Type: `number` ([Number of labels per array](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/nLabelsPerArray")

### nLabelsPerArray Type

`number` ([Number of labels per array](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md))

### nLabelsPerArray Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                                                                                                                         |
| :---- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1`   | One single label was used for a single array                                                                                                        |
| `2`   | Two labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected.   |
| `3`   | Three labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected. |
| `4`   | Four labels were used for a single array. The node 'arraySampleLabels' specifying which samples were labelled by which compounds will be expected.  |

## arraySampleLabels

Sample-Label pairs (e.g. sample 'EGAN00000000001' and label 'Cy3') to know which samples used in this assay are labelled by which chemicals. Can be omitted if the array is of one single label/colour.

`arraySampleLabels`

*   is optional

*   Type: `object[]` ([Repeatable Sample-label node](ega-4-definitions-repeatable-sample-label-node.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-array-of-samplelabel-pairs-of-the-array-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/arraySampleLabels")

### arraySampleLabels Type

`object[]` ([Repeatable Sample-label node](ega-4-definitions-repeatable-sample-label-node.md))

### arraySampleLabels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
