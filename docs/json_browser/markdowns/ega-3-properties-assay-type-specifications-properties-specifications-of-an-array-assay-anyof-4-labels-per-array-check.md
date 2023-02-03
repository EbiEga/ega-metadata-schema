# 4 labels per array check Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/anyOf/2
```

If 4 labels were used per array, the sampleLabel specifications will be expected and at least 4 items (one for each label)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## 2 Type

unknown ([4 labels per array check](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check.md))

# 2 Properties

| Property                                | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [nLabelsPerArray](#nlabelsperarray)     | Not specified | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check-properties-nlabelsperarray.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/anyOf/2/properties/nLabelsPerArray")     |
| [arraySampleLabels](#arraysamplelabels) | Not specified | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check-properties-arraysamplelabels.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/anyOf/2/properties/arraySampleLabels") |

## nLabelsPerArray



`nLabelsPerArray`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check-properties-nlabelsperarray.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/anyOf/2/properties/nLabelsPerArray")

### nLabelsPerArray Type

unknown

### nLabelsPerArray Constraints

**constant**: the value of this property must be equal to:

```json
4
```

## arraySampleLabels



`arraySampleLabels`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check-properties-arraysamplelabels.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/anyOf/2/properties/arraySampleLabels")

### arraySampleLabels Type

unknown

### arraySampleLabels Constraints

**minimum number of items**: the minimum number of items for this array is: `4`
