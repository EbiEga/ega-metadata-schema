# Either the sample_number is present and above 1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## 0 Type

unknown ([Either the sample_number is present and above 1](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1.md))

# 0 Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                             |
| :-------------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sample_group_boolean](#sample_group_boolean) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_group_boolean") |
| [sample_number](#sample_number)               | `integer`     | Required | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_number")               |

## sample_group_boolean



`sample_group_boolean`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_group_boolean.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_group_boolean")

### sample_group_boolean Type

unknown

### sample_group_boolean Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `true` |             |

## sample_number



`sample_number`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1-properties-sample_number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping/oneOf/0/properties/sample_number")

### sample_number Type

`integer`

### sample_number Constraints

**minimum**: the value of this number must greater than or equal to: `2`
