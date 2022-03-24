# Specifications of an array assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications
```

Node containing the set of fields specific to an assay of type 'array' (i.e. an array was used to obtain the raw data).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json*](../out/EGA.assay.json "open original schema") |

## array_assay_specifications Type

`object` ([Specifications of an array assay](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

any of

*   [2 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-2-labels-per-array-check.md "check type definition")

*   [3 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-3-labels-per-array-check.md "check type definition")

*   [4 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check.md "check type definition")

# array_assay_specifications Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [n_labels_per_array](#n_labels_per_array)   | `number` | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications/properties/n_labels_per_array")                      |
| [array_sample_labels](#array_sample_labels) | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-array-of-sample-label-pairs-of-the-array-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications/properties/array_sample_labels") |

## n_labels_per_array

A single array can be prepared with biological materials labelled differently for them to be compared in parallel. Here one shall specify the number of labels used in the single array (e.g. 2 for a Two-colour cDNA microarray). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`n_labels_per_array`

*   is required

*   Type: `number` ([Number of labels per array](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications/properties/n_labels_per_array")

### n_labels_per_array Type

`number` ([Number of labels per array](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-number-of-labels-per-array.md))

### n_labels_per_array Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                                                                                                                            |
| :---- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1`   | 2: two labels were used for a single array. The node 'array_sample_labels' specifying which samples were labelled by which compounds will be expected. |
| `2`   |                                                                                                                                                        |
| `3`   |                                                                                                                                                        |
| `4`   |                                                                                                                                                        |

## array_sample_labels

Sample-Label pairs (e.g. sample 'EGAN00000000001' and label 'Cy3') to know which samples used in this assay are labelled by which chemicals. Can be omitted if the array is of one single label/colour.

`array_sample_labels`

*   is optional

*   Type: `object[]` ([Repeatable Sample-label node](ega-12-definitions-repeatable-sample-label-node.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-array-of-sample-label-pairs-of-the-array-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications/properties/array_sample_labels")

### array_sample_labels Type

`object[]` ([Repeatable Sample-label node](ega-12-definitions-repeatable-sample-label-node.md))

### array_sample_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
