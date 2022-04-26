# Or the sample\_group\_boolean is 'false', hence an individual sample with sample\_number being '1' or no sample\_number Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 1 Type

unknown ([Or the sample\_group\_boolean is 'false', hence an individual sample with sample\_number being '1' or no sample\_number](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number.md))

# 1 Properties

| Property                                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                            |
| :---------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [sample\_group\_boolean](#sample_group_boolean) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/1/properties/sample_group_boolean") |
| [sample\_number](#sample_number)                | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/1/properties/sample_number")               |

## sample\_group\_boolean



`sample_group_boolean`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/1/properties/sample_group_boolean")

### sample\_group\_boolean Type

unknown

### sample\_group\_boolean Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `false` |             |

## sample\_number



`sample_number`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/1/properties/sample_number")

### sample\_number Type

unknown

### sample\_number Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `1`   |             |
