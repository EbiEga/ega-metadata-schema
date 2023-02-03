# Array of sample types Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleTypes
```

Array of sample types: the material entity (e.g. DNA) that is this sample. Use this property as tags that befit your sample, picking as many as needed. Choose the specific terms if possible (e.g. if the assayed molecule is cDNA, add 'cDNA' instead of just 'DNA'). This property should not be confused with the sample collection protocols: regardless of the procedure to collect the sample, this property specifies what this sample is representing.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleTypes Type

`string[]` ([Type of sample](ega-10-properties-array-of-sample-types-type-of-sample.md))

## sampleTypes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
