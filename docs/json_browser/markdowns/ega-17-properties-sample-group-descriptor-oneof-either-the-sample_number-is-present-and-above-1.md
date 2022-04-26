# Either the sample\_number is present and above 1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 0 Type

unknown ([Either the sample\_number is present and above 1](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1.md))

# 0 Properties

| Property                                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sample\_group\_boolean](#sample_group_boolean) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_group_boolean") |
| [sample\_number](#sample_number)                | `integer`     | Required | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_number")               |

## sample\_group\_boolean



`sample_group_boolean`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_group_boolean")

### sample\_group\_boolean Type

unknown

### sample\_group\_boolean Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `true` |             |

## sample\_number



`sample_number`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_number")

### sample\_number Type

`integer`

### sample\_number Constraints

**minimum**: the value of this number must greater than or equal to: `2`
