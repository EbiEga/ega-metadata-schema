# Either the sampleNumber is present and above 1 Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 0 Type

unknown ([Either the sampleNumber is present and above 1](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1.md))

# 0 Properties

| Property                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sampleGroupBoolean](#samplegroupboolean) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1-properties-samplegroupboolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/0/properties/sampleGroupBoolean") |
| [sampleNumber](#samplenumber)             | `integer`     | Required | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1-properties-samplenumber.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/0/properties/sampleNumber")             |

## sampleGroupBoolean



`sampleGroupBoolean`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1-properties-samplegroupboolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/0/properties/sampleGroupBoolean")

### sampleGroupBoolean Type

unknown

### sampleGroupBoolean Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `true` |             |

## sampleNumber



`sampleNumber`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1-properties-samplenumber.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/0/properties/sampleNumber")

### sampleNumber Type

`integer`

### sampleNumber Constraints

**minimum**: the value of this number must greater than or equal to: `2`
