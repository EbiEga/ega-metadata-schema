# Individual's age at sample collection Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection
```

Property describing the individual's age at sample collection. Can either be the precise age an age range.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## ageAtCollection Type

`object` ([Individual's age at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md))

any of

*   [Either the age is needed](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-either-the-age-is-needed.md "check type definition")

*   [Or the age-range is needed](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-or-the-age-range-is-needed.md "check type definition")

# ageAtCollection Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [age](#age)           | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-4-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/age")                                                                                                                         |
| [ageRange](#agerange) | `object` | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange") |

## age

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

`age`

*   is optional

*   Type: `string` ([Individual's age](ega-4-definitions-individuals-age.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-4-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/age")

### age Type

`string` ([Individual's age](ega-4-definitions-individuals-age.md))

all of

*   [Pattern of a partial EGA ISO 8601 duration](ega-4-definitions-pattern-of-a-partial-ega-iso-8601-duration.md "check type definition")

### age Examples

```json
"P3Y6M4D"
```

```json
"P23DT23H"
```

```json
"P4Y"
```

## ageRange

Age range of the individual when the sample was collected. Composed of two (start and end) age points.

`ageRange`

*   is optional

*   Type: `object` ([Individual's age range at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange")

### ageRange Type

`object` ([Individual's age range at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md))
