# Sample group descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping
```

Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e.g. blood samples from different donors) physically or during the experimentation and analysis. One sample corresponds to one biological replicate \[EFO:0002091] (e.g. genetic content from a single cell, a tissue, buccal swab, etc.) from a single individual or from several individuals. Shall not be mistaken for technical replicates \[EFO:0002090] being used several times (see <https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/miscellaneous/sample_replicate.jpg>).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleGrouping Type

`object` ([Sample group descriptor](ega-10-properties-sample-group-descriptor.md))

one (and only one) of

*   [Either the sampleNumber is present and above 1](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1.md "check type definition")

*   [Or the sampleGroupBoolean is 'false', hence an individual sample with sampleNumber being '1' or no sampleNumber](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber.md "check type definition")

# sampleGrouping Properties

| Property                                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :------------------------------------------ | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sampleGroupBoolean](#samplegroupboolean)   | `boolean` | Required | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-sample-group-boolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleGroupBoolean")          |
| [sampleNumber](#samplenumber)               | `integer` | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-number-of-samples.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleNumber")                   |
| [sampleGroupingLabel](#samplegroupinglabel) | `string`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-label-of-the-sample-grouping.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleGroupingLabel") |

## sampleGroupBoolean

Boolean flag on whether the sample object is a group or an individual sample. Please note that boolean values (true or false) cannot be quoted, nor in uppercase.

`sampleGroupBoolean`

*   is required

*   Type: `boolean` ([Sample group boolean](ega-10-properties-sample-group-descriptor-properties-sample-group-boolean.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-sample-group-boolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleGroupBoolean")

### sampleGroupBoolean Type

`boolean` ([Sample group boolean](ega-10-properties-sample-group-descriptor-properties-sample-group-boolean.md))

### sampleGroupBoolean Examples

```json
true
```

## sampleNumber

Number of individual samples (e.g. 300) encompassed by the sample group

`sampleNumber`

*   is optional

*   Type: `integer` ([Number of samples](ega-10-properties-sample-group-descriptor-properties-number-of-samples.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-number-of-samples.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleNumber")

### sampleNumber Type

`integer` ([Number of samples](ega-10-properties-sample-group-descriptor-properties-number-of-samples.md))

### sampleNumber Examples

```json
300
```

## sampleGroupingLabel

Optional label of the sample grouping, used to add context to the group.

`sampleGroupingLabel`

*   is optional

*   Type: `string` ([Label of the sample grouping](ega-10-properties-sample-group-descriptor-properties-label-of-the-sample-grouping.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor-properties-label-of-the-sample-grouping.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping/properties/sampleGroupingLabel")

### sampleGroupingLabel Type

`string` ([Label of the sample grouping](ega-10-properties-sample-group-descriptor-properties-label-of-the-sample-grouping.md))

### sampleGroupingLabel Examples

```json
"Group of samples X based on the day they were taken."
```
