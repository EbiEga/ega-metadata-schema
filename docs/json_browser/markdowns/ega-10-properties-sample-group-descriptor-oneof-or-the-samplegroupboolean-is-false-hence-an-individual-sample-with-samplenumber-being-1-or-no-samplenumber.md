# Or the sampleGroupBoolean is 'false', hence an individual sample with sampleNumber being '1' or no sampleNumber Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 1 Type

unknown ([Or the sampleGroupBoolean is 'false', hence an individual sample with sampleNumber being '1' or no sampleNumber](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber.md))

# 1 Properties

| Property                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sampleGroupBoolean](#samplegroupboolean) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber-properties-samplegroupboolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/1/properties/sampleGroupBoolean") |
| [sampleNumber](#samplenumber)             | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber-properties-samplenumber.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/1/properties/sampleNumber")             |

## sampleGroupBoolean



`sampleGroupBoolean`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber-properties-samplegroupboolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/1/properties/sampleGroupBoolean")

### sampleGroupBoolean Type

unknown

### sampleGroupBoolean Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `false` |             |

## sampleNumber



`sampleNumber`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber-properties-samplenumber.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/oneOf/1/properties/sampleNumber")

### sampleNumber Type

unknown

### sampleNumber Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `1`   |             |
